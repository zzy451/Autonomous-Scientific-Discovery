#!/usr/bin/env python3
"""Run independent, resumable per-paper classification audits with Codex CLI."""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import json
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile
import threading
import tomllib
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any


SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
DATA_DIR = PROJECT_ROOT / "Data"
DEFAULT_RUN_DIR = PROJECT_ROOT / "Coverage_Check" / "codex_classification_audit_gpt-6.1-sol_2026-10-27"
REQUIRED_MODEL = "gpt-6.1-sol"
PAPERS_PATH = DATA_DIR / "papers.jsonl"
MODULES_PATH = DATA_DIR / "paper_modules.csv"
MODULE_TAXONOMY_PATH = DATA_DIR / "paper_module_taxonomy_assignments.jsonl"
DISCIPLINE_CODES_PATH = DATA_DIR / "discipline_code_assignments.jsonl"
CODE_INDEX_PATH = DATA_DIR / "classification_code_index.json"
PROMPT_PATH = PROJECT_ROOT / "prompts" / "codex_classification_audit_prompt.md"
SCHEMA_PATH = DATA_DIR / "schema" / "codex_classification_audit.schema.json"
LOCK = threading.Lock()


def read_jsonl(path: pathlib.Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.strip():
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{line_number}: {exc}") from exc
    return rows


def load_taxonomy() -> tuple[dict[str, Any], str]:
    index = json.loads(CODE_INDEX_PATH.read_text(encoding="utf-8"))
    primary = {row["primary_code"]: row["label"] for row in index["primary_terms"] if row["status"] == "active"}
    secondary = [row for row in index["secondary_terms"] if row["status"] == "active"]
    active_secondary_codes = {row["secondary_code"] for row in secondary}
    tertiary = [
        row
        for row in index["tertiary_terms"]
        if row["status"] == "active" and row["parent_secondary_code"] in active_secondary_codes
    ]
    lines = ["Active primary terms:"]
    for code, label in primary.items():
        if code != "01.04":
            lines.append(f"- {code}: {label}")
    lines.append("\nActive secondary terms (other legacy entries are not valid active assignments):")
    for row in secondary:
        lines.append(f"- {row['secondary_code']} ({row['parent_primary_code']}): {row['label']} | {row['definition']} Include: {'; '.join(row['include'])} Exclude: {'; '.join(row['exclude'])}")
    lines.append("\nActive tertiary terms:")
    for row in tertiary:
        lines.append(f"- {row['tertiary_code']} ({row['parent_secondary_code']}): {row['label']}")
    return index, "\n".join(lines)


def project_rules() -> str:
    return "The task prompt contains the operational boundary rules distilled from the project classification policy and domain rules."


def codex_config_overrides() -> list[str]:
    codex_home = pathlib.Path(os.environ.get("CODEX_HOME", "~/.codex")).expanduser()
    config_path = codex_home / "config.toml"
    if not config_path.is_file():
        return []
    try:
        config = tomllib.loads(config_path.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as exc:
        raise RuntimeError(f"cannot read Codex config {config_path}: {exc}") from exc
    if not config.get("plugins") and not config.get("marketplaces"):
        return []

    overrides = ["--ignore-user-config"]
    provider_name = config.get("model_provider")
    if provider_name:
        overrides.extend(["-c", f"model_provider={json.dumps(provider_name)}"])
        provider = config.get("model_providers", {}).get(provider_name, {})
        for key in (
            "name",
            "wire_api",
            "requires_openai_auth",
            "base_url",
            "supports_websockets",
            "request_max_retries",
            "stream_idle_timeout_ms",
            "env_key",
        ):
            if key in provider:
                value = provider[key]
                encoded = json.dumps(value, ensure_ascii=True) if isinstance(value, (str, bool, int, float)) else None
                if encoded is not None:
                    overrides.extend(["-c", f"model_providers.{provider_name}.{key}={encoded}"])
    for key in ("approval_policy", "service_tier"):
        if key in config and isinstance(config[key], (str, bool, int, float)):
            overrides.extend(["-c", f"{key}={json.dumps(config[key], ensure_ascii=True)}"])
    return overrides


def extract_pdf(pdf_path: pathlib.Path) -> tuple[str | None, str]:
    if not pdf_path.is_file():
        return None, "missing"
    with pdf_path.open("rb") as handle:
        if handle.read(5) != b"%PDF-":
            return None, "not_a_pdf_file"
    tool = shutil.which("pdftotext")
    if not tool:
        return None, "pdftotext_unavailable"
    proc = subprocess.run([tool, "-layout", "-enc", "UTF-8", str(pdf_path), "-"], capture_output=True, text=True)
    if proc.returncode != 0 or not proc.stdout.strip():
        return None, "pdf_text_extraction_failed"
    pages = proc.stdout.split("\f")
    text = "\n\n".join(f"===== PDF page {i} =====\n{page.strip()}" for i, page in enumerate(pages, 1) if page.strip())
    return text, "pdf_full_text_extracted"


def fetch_arxiv_pdf(arxiv_id: str, cache_dir: pathlib.Path) -> pathlib.Path | None:
    if not arxiv_id:
        return None
    cache_path = cache_dir / f"{arxiv_id.replace('/', '_')}.pdf"
    if cache_path.is_file() and cache_path.open("rb").read(5) == b"%PDF-":
        return cache_path
    cache_dir.mkdir(parents=True, exist_ok=True)
    url = f"https://arxiv.org/pdf/{arxiv_id}"
    request = urllib.request.Request(url, headers={"User-Agent": "ASD-classification-audit/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            data = response.read(100 * 1024 * 1024 + 1)
        if len(data) > 100 * 1024 * 1024 or not data.startswith(b"%PDF-"):
            return None
        temp_path = cache_path.with_suffix(".pdf.tmp")
        temp_path.write_bytes(data)
        temp_path.replace(cache_path)
        return cache_path
    except (OSError, urllib.error.URLError, TimeoutError):
        return None


def fetch_openalex_oa_pdf(doi: str, cache_dir: pathlib.Path) -> pathlib.Path | None:
    if not doi:
        return None
    doi_key = doi.removeprefix("https://doi.org/").removeprefix("http://doi.org/")
    cache_path = cache_dir / (hashlib.sha256(doi_key.encode("utf-8")).hexdigest()[:20] + ".pdf")
    if cache_path.is_file() and cache_path.open("rb").read(5) == b"%PDF-":
        return cache_path
    encoded_doi = urllib.parse.quote("https://doi.org/" + doi_key, safe="")
    api_url = f"https://api.openalex.org/works/{encoded_doi}"
    request = urllib.request.Request(api_url, headers={"User-Agent": "ASD-classification-audit/1.0 (mailto:openalex@openalex.org)"})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            work = json.loads(response.read(5 * 1024 * 1024))
        locations = [work.get("best_oa_location") or {}] + [location for location in work.get("locations", []) if location != work.get("best_oa_location")]
        pdf_urls = list(dict.fromkeys(location.get("pdf_url") for location in locations if location.get("pdf_url")))
        cache_dir.mkdir(parents=True, exist_ok=True)
        for pdf_url in pdf_urls[:5]:
            try:
                pdf_request = urllib.request.Request(pdf_url, headers={"User-Agent": "ASD-classification-audit/1.0"})
                with urllib.request.urlopen(pdf_request, timeout=45) as response:
                    data = response.read(100 * 1024 * 1024 + 1)
                if len(data) <= 100 * 1024 * 1024 and data.startswith(b"%PDF-"):
                    temp_path = cache_path.with_suffix(".pdf.tmp")
                    temp_path.write_bytes(data)
                    temp_path.replace(cache_path)
                    return cache_path
            except (OSError, urllib.error.URLError, TimeoutError):
                continue
    except (OSError, urllib.error.URLError, TimeoutError, json.JSONDecodeError):
        return None
    return None


def paper_doi(paper: dict[str, Any]) -> str:
    value = str(paper.get("doi") or "").strip()
    if value:
        return value
    candidate = str(paper.get("doi_or_url") or "").strip()
    if "doi.org/" in candidate:
        return candidate.split("doi.org/", 1)[1].split("?", 1)[0].split("#", 1)[0]
    if candidate.lower().startswith("10."):
        return candidate
    return ""


def note_evidence_excerpt(note_text: str) -> str:
    marker = "Evidence Log"
    start = note_text.find(marker)
    if start >= 0:
        excerpt = note_text[start:]
        for heading in ("\n## 0.", "\n## 1.", "\n## 科学领域归类", "\n## 2."):
            end = excerpt.find(heading)
            if end > 0:
                excerpt = excerpt[:end]
        return excerpt[:30000]
    return note_text[:12000]


def source_for_paper(paper: dict[str, Any], args: argparse.Namespace, run_dir: pathlib.Path) -> tuple[str, str, str]:
    override = args.pdf_override
    pdf_path = pathlib.Path(override).expanduser() if override else PROJECT_ROOT / str(paper.get("pdf_path") or "")
    pdf_text, pdf_status = extract_pdf(pdf_path) if (paper.get("pdf_path") or override) else (None, "missing")
    if not pdf_text and not args.no_fetch_arxiv and paper.get("arxiv_id"):
        fetched_pdf = fetch_arxiv_pdf(str(paper["arxiv_id"]), run_dir / "pdf_cache")
        if fetched_pdf:
            pdf_text, pdf_status = extract_pdf(fetched_pdf)
            if pdf_text:
                pdf_status = "official_arxiv_pdf_downloaded_and_extracted"
    doi = paper_doi(paper)
    if not pdf_text and not args.no_fetch_openalex and doi:
        fetched_pdf = fetch_openalex_oa_pdf(doi, run_dir / "pdf_cache")
        if fetched_pdf:
            pdf_text, pdf_status = extract_pdf(fetched_pdf)
            if pdf_text:
                pdf_status = "openalex_listed_oa_pdf_downloaded_and_extracted"
    note_path = PROJECT_ROOT / str(paper.get("note_path") or "")
    note_text = note_path.read_text(encoding="utf-8", errors="replace") if note_path.is_file() else ""
    metadata = "\n".join(
        f"{key}: {paper.get(key, '')}"
        for key in ("paper_id", "title", "authors", "year", "source", "doi", "doi_or_url", "url", "arxiv_id")
        if paper.get(key)
    )
    if pdf_text:
        body = f"Evidence source status: {pdf_status}.\n\nFull extracted PDF text follows.\n\n{pdf_text}"
        return "pdf_full_text", body, pdf_status
    if note_text:
        reason = f"PDF status: {pdf_status}; note supplied as secondary evidence only."
        body = f"Evidence source status: note_only. {reason}\n\nProject note evidence excerpt (not the paper itself; prior class claims must be ignored):\n{note_evidence_excerpt(note_text)}"
        body += f"\n\nBibliographic metadata and official source URL (not independently fetched by this runner):\n{metadata}"
        return "note_only", body, pdf_status
    return "metadata_only", f"Evidence source status: metadata_only.\n\n{metadata}", pdf_status


def build_prompt(
    paper: dict[str, Any], rules: str, codebook: str, source_type: str, source_text: str, extra_context: str = ""
) -> str:
    task = PROMPT_PATH.read_text(encoding="utf-8")
    return "\n\n".join(
        [
            task,
            "## Project classification policy and boundaries\n" + rules,
            "## Controlled taxonomy codebook\n" + codebook,
            "## Paper metadata\n" + json.dumps({k: paper.get(k) for k in ("paper_id", "title", "authors", "year", "source", "doi", "doi_or_url", "url", "arxiv_id")}, ensure_ascii=False, indent=2),
            f"## Evidence basis: {source_type}\n\n{source_text}",
            f"## Additional user-supplied context (secondary only)\n\n{extra_context}" if extra_context else "",
            f"Return the required JSON for paper_id {paper['paper_id']}. Do not include markdown fences or commentary.",
        ]
    )


def atomic_json(path: pathlib.Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def parse_codex_output(raw: str, paper_id: str) -> dict[str, Any]:
    decoder = json.JSONDecoder()
    matches = []
    for offset, character in enumerate(raw):
        if character != "{":
            continue
        try:
            value, _ = decoder.raw_decode(raw, offset)
        except json.JSONDecodeError:
            continue
        if isinstance(value, dict) and value.get("paper_id") == paper_id:
            matches.append(value)
    if matches:
        return matches[-1]
    raise ValueError(f"Codex output contains no complete JSON object for paper_id {paper_id}")


def log_jsonl(path: pathlib.Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with LOCK, path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, ensure_ascii=False) + "\n")


def validate_assessment(result: dict[str, Any], paper_id: str, index: dict[str, Any]) -> list[str]:
    errors = []
    if result.get("paper_id") != paper_id:
        errors.append(f"paper_id mismatch: {result.get('paper_id')!r}")
    primary_labels = {r["primary_code"]: r["label"] for r in index["primary_terms"] if r["status"] == "active"}
    secondary = {r["secondary_code"]: r for r in index["secondary_terms"] if r["status"] == "active"}
    active_secondary_codes = set(secondary)
    tertiary = {
        r["tertiary_code"]: r
        for r in index["tertiary_terms"]
        if r["status"] == "active" and r["parent_secondary_code"] in active_secondary_codes
    }
    seen = set()
    for row in result.get("modules", []):
        primary = row.get("primary_code")
        if primary in seen:
            errors.append(f"duplicate module {primary}")
        seen.add(primary)
        if primary not in primary_labels:
            errors.append(f"unknown primary code {primary}")
        if row.get("secondary_code"):
            sec = secondary.get(row["secondary_code"])
            if not sec or sec["parent_primary_code"] != primary:
                errors.append(f"invalid secondary code {row['secondary_code']} under {primary}")
        if row.get("tertiary_code"):
            tert = tertiary.get(row["tertiary_code"])
            if not tert or tert["parent_primary_code"] != primary:
                errors.append(f"invalid tertiary code {row['tertiary_code']} under {primary}")
            elif row.get("secondary_code") and row.get("secondary_code") != tert["parent_secondary_code"]:
                errors.append(f"tertiary/secondary mismatch for {primary}: {row['tertiary_code']}")
    if result.get("classification_bucket") == "01.04" and result.get("modules"):
        errors.append("01.04 bucket cannot coexist with scientific-object modules")
    module_codes = {row.get("primary_code") for row in result.get("modules", [])}
    evidence_codes = {row.get("primary_code") for row in result.get("object_evidence", [])}
    if module_codes - evidence_codes:
        errors.append(f"modules missing object evidence: {sorted(module_codes - evidence_codes)}")
    if not module_codes and result.get("classification_bucket") != "01.04":
        errors.append("no supported modules or 01.04 bucket")
    return errors


def normalize_assessment(result: dict[str, Any]) -> dict[str, Any]:
    """Keep one row per primary module while preserving duplicate-row review evidence."""
    result = dict(result)
    active_secondary = {
        row["secondary_code"]
        for row in json.loads(CODE_INDEX_PATH.read_text(encoding="utf-8"))["secondary_terms"]
        if row["status"] == "active"
    }
    active_tertiary = {
        row["tertiary_code"]
        for row in json.loads(CODE_INDEX_PATH.read_text(encoding="utf-8"))["tertiary_terms"]
        if row["status"] == "active"
    }
    taxonomy_review_reasons = list(result.get("human_review_reasons") or [])
    for row in result.get("modules", []):
        secondary_code = row.get("secondary_code")
        tertiary_code = row.get("tertiary_code")
        if secondary_code and secondary_code not in active_secondary:
            taxonomy_review_reasons.append(
                f"Model proposed non-active secondary code {secondary_code}; cleared pending human review."
            )
            row["secondary_code"] = None
            row["secondary_label"] = None
        if tertiary_code and tertiary_code not in active_tertiary:
            taxonomy_review_reasons.append(
                f"Model proposed non-active tertiary code {tertiary_code}; cleared pending human review."
            )
            row["tertiary_code"] = None
            row["tertiary_label"] = None
        if row.get("tertiary_code") and not row.get("secondary_code"):
            row["tertiary_code"] = None
            row["tertiary_label"] = None
    if taxonomy_review_reasons:
        result["human_review_reasons"] = taxonomy_review_reasons
        result["needs_human_review"] = True
    rows = result.get("modules", [])
    evidence_codes = {entry.get("primary_code") for entry in result.get("object_evidence", [])}
    unsupported = [row.get("primary_code") for row in rows if row.get("primary_code") not in evidence_codes]
    if unsupported:
        rows = [row for row in rows if row.get("primary_code") in evidence_codes]
        result["modules"] = rows
        reasons = list(result.get("human_review_reasons") or [])
        reasons.append(
            "Model listed module(s) without corresponding concrete-object evidence; those unsupported modules were dropped pending review: "
            + ", ".join(str(code) for code in unsupported)
        )
        result["human_review_reasons"] = reasons
        result["needs_human_review"] = True
    grouped: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        grouped.setdefault(row.get("primary_code", ""), []).append(row)
    normalized: list[dict[str, Any]] = []
    review_reasons = list(result.get("human_review_reasons") or [])
    rank = {"high": 3, "medium": 2, "low": 1}
    for primary, candidates in grouped.items():
        candidates = sorted(
            candidates,
            key=lambda row: (
                bool(row.get("tertiary_code")),
                bool(row.get("secondary_code")),
                rank.get(row.get("confidence"), 0),
            ),
            reverse=True,
        )
        normalized.append(candidates[0])
        if len(candidates) > 1:
            alternatives = [
                f"{row.get('secondary_code') or 'null'}/{row.get('tertiary_code') or 'null'} ({row.get('taxonomy_gap_reason') or row.get('confidence')})"
                for row in candidates[1:]
            ]
            evidence = [
                {key: entry.get(key) for key in ("concrete_object", "reported_action_or_result", "quote", "location")}
                for entry in result.get("object_evidence", [])
                if entry.get("primary_code") == primary
            ]
            review_reasons.append(
                f"Model returned multiple lower-level assignments for module {primary}; alternatives retained for human review: {', '.join(alternatives)}. Module evidence: {json.dumps(evidence, ensure_ascii=False)}"
            )
    if len(normalized) != len(rows):
        result["modules"] = normalized
        result["human_review_reasons"] = review_reasons
        result["needs_human_review"] = True
    return result


def run_one(
    paper: dict[str, Any], args: argparse.Namespace, rules: str, codebook: str, index: dict[str, Any], run_dir: pathlib.Path
) -> tuple[str, str]:
    paper_id = paper["paper_id"]
    result_path = run_dir / "results" / f"{paper_id}.json"
    if result_path.exists() and not args.force:
        try:
            saved = json.loads(result_path.read_text(encoding="utf-8"))
            if saved.get("status") == "completed" and saved.get("model") == args.model:
                return paper_id, "skipped_completed"
        except (OSError, json.JSONDecodeError):
            pass
    source_type, source_text, pdf_status = source_for_paper(paper, args, run_dir)
    extra_context_parts = []
    if args.context_file:
        extra_context_parts.append(args.context_file.read_text(encoding="utf-8", errors="replace"))
    if args.context_dir:
        for suffix in (".md", ".txt"):
            context_path = args.context_dir / f"{paper_id}{suffix}"
            if context_path.is_file():
                extra_context_parts.append(context_path.read_text(encoding="utf-8", errors="replace"))
                break
    prompt = build_prompt(paper, rules, codebook, source_type, source_text, "\n\n".join(extra_context_parts))
    prompt_hash = hashlib.sha256(prompt.encode("utf-8")).hexdigest()
    if result_path.exists() and not args.force:
        try:
            saved = json.loads(result_path.read_text(encoding="utf-8"))
            if (
                saved.get("status") == "completed"
                and saved.get("model") == args.model
                and saved.get("input_sha256") == prompt_hash
            ):
                return paper_id, "skipped_completed"
        except (OSError, json.JSONDecodeError):
            pass

    codex = args.codex_bin
    with tempfile.TemporaryDirectory(prefix=f"asd-audit-{paper_id}-") as temp_dir:
        raw_temp_path = pathlib.Path(temp_dir) / "last_message.json"
        cmd = [codex, "exec", *args.codex_config_args, "--ephemeral", "--skip-git-repo-check", "-s", "read-only", "--output-schema", str(SCHEMA_PATH), "-o", str(raw_temp_path)]
        cmd.extend(["-c", f'model_reasoning_effort="{args.reasoning_effort}"'])
        if args.model:
            cmd.extend(["-m", args.model])
        cmd.append("-")
        (run_dir / "logs").mkdir(parents=True, exist_ok=True)
        try:
            proc = subprocess.run(cmd, cwd=PROJECT_ROOT, input=prompt, text=True, capture_output=True, timeout=args.timeout)
            raw_path = run_dir / "raw" / f"{paper_id}.txt"
            raw_path.write_text(raw_temp_path.read_text(encoding="utf-8") if raw_temp_path.is_file() else "", encoding="utf-8")
            (run_dir / "logs" / f"{paper_id}.stdout.txt").write_text(proc.stdout, encoding="utf-8")
            (run_dir / "logs" / f"{paper_id}.stderr.txt").write_text(proc.stderr[-12000:], encoding="utf-8")
            if proc.returncode != 0:
                raise RuntimeError(f"codex exit {proc.returncode}: {(proc.stderr or proc.stdout)[-3000:]}")
            raw = raw_path.read_text(encoding="utf-8")
            if not raw.strip():
                raise RuntimeError(f"Codex returned no final message. stderr: {proc.stderr[-3000:]} stdout: {proc.stdout[-1000:]}")
            assessment = normalize_assessment(parse_codex_output(raw, paper_id))
            validation = validate_assessment(assessment, paper_id, index)
            if validation:
                raise ValueError("invalid assessment: " + "; ".join(validation))
            wrapper = {
                "status": "completed",
                "paper_id": paper_id,
                "model": args.model,
                "input_sha256": prompt_hash,
                "audited_at": dt.datetime.now(dt.timezone.utc).isoformat(),
                "source_type": source_type,
                "pdf_status": pdf_status,
                "source_characters": len(source_text),
                "assessment": assessment,
            }
            atomic_json(result_path, wrapper)
            return paper_id, "completed"
        except Exception as exc:  # checkpoint individual failures so the batch can continue
            failure = {
                "status": "error",
                "paper_id": paper_id,
                "model": args.model,
                "input_sha256": prompt_hash,
                "source_type": source_type,
                "pdf_status": pdf_status,
                "error": str(exc),
                "failed_at": dt.datetime.now(dt.timezone.utc).isoformat(),
            }
            atomic_json(result_path, failure)
            log_jsonl(run_dir / "errors.jsonl", failure)
            return paper_id, "error"


def current_assignments(papers: list[dict[str, Any]]) -> tuple[dict[str, set[str]], dict[tuple[str, str], dict[str, Any]], dict[str, dict[str, Any]]]:
    modules: dict[str, set[str]] = {}
    if MODULES_PATH.exists():
        with MODULES_PATH.open(encoding="utf-8-sig", newline="") as handle:
            for row in csv.DictReader(handle):
                if row.get("active_confirmed_core") == "1" and row.get("module_kind") == "formal_module":
                    modules.setdefault(row["paper_id"], set()).add(row["module_code"])
    for paper in papers:
        if paper.get("active_confirmed_core") and paper.get("scientific_object_modules"):
            modules.setdefault(paper["paper_id"], set()).update(str(x) for x in paper["scientific_object_modules"])
    per_module: dict[tuple[str, str], dict[str, Any]] = {}
    for row in read_jsonl(MODULE_TAXONOMY_PATH):
        if row.get("assignment_status") == "active_mapping":
            per_module[(row["paper_id"], row["module_context"])] = row
    primary: dict[str, dict[str, Any]] = {}
    for row in read_jsonl(DISCIPLINE_CODES_PATH):
        if row.get("assignment_status") == "active_code":
            primary[row["paper_id"]] = row
    return modules, per_module, primary


def compare_results(papers: list[dict[str, Any]], run_dir: pathlib.Path) -> list[dict[str, Any]]:
    current_modules, module_assignments, primary_assignments = current_assignments(papers)
    diffs: list[dict[str, Any]] = []
    for paper in papers:
        if not paper.get("active_confirmed_core"):
            continue
        paper_id = paper["paper_id"]
        result_path = run_dir / "results" / f"{paper_id}.json"
        if not result_path.is_file():
            diffs.append({"paper_id": paper_id, "title": paper.get("title", ""), "difference_type": "audit_missing", "current": "", "audit": "", "reason": "No saved audit result."})
            continue
        saved = json.loads(result_path.read_text(encoding="utf-8"))
        if saved.get("status") != "completed":
            diffs.append({"paper_id": paper_id, "title": paper.get("title", ""), "difference_type": "audit_error", "current": "", "audit": "", "reason": saved.get("error", "Audit did not complete.")})
            continue
        assessment = saved["assessment"]
        audited_modules = {row["primary_code"]: row for row in assessment.get("modules", [])}
        existing = current_modules.get(paper_id, set())
        for code in sorted(set(audited_modules) - existing):
            diffs.append({"paper_id": paper_id, "title": paper.get("title", ""), "difference_type": "module_added_by_audit", "module": code, "current": "absent", "audit": code, "reason": assessment["overall_rationale"], "evidence": json.dumps([e for e in assessment.get("object_evidence", []) if e["primary_code"] == code], ensure_ascii=False), "source_type": saved.get("source_type", "")})
        for code in sorted(existing - set(audited_modules)):
            diffs.append({"paper_id": paper_id, "title": paper.get("title", ""), "difference_type": "module_missing_in_audit", "module": code, "current": code, "audit": "absent", "reason": assessment["overall_rationale"], "evidence": json.dumps(assessment.get("object_evidence", []), ensure_ascii=False), "source_type": saved.get("source_type", "")})
        for code in sorted(set(audited_modules) & existing):
            model_row = audited_modules[code]
            current_row = module_assignments.get((paper_id, code))
            baselines: list[tuple[str, Any, Any]] = []
            if current_row:
                baselines.append(("paper_module_taxonomy_assignments", current_row.get("secondary_taxonomy_code"), current_row.get("tertiary_taxonomy_code")))
            if code == str(paper.get("primary_module_for_filing") or ""):
                assignment = primary_assignments.get(paper_id, {})
                secondary = assignment.get("primary_taxonomy_code_2lvl") or paper.get("legacy_secondary_class")
                tertiary = assignment.get("primary_taxonomy_code_3lvl") or paper.get("legacy_tertiary_class")
                if secondary is not None or tertiary is not None:
                    baselines.append(("discipline_code_assignments/legacy_filing", secondary, tertiary))
            if not baselines:
                baselines.append(("no_existing_module_level_assignment", None, None))
            evidence = json.dumps([e for e in assessment.get("object_evidence", []) if e["primary_code"] == code], ensure_ascii=False)
            unique_baselines: dict[tuple[Any, Any], list[str]] = {}
            for source, current_secondary, current_tertiary in baselines:
                unique_baselines.setdefault((current_secondary, current_tertiary), []).append(source)
            for (current_secondary, current_tertiary), sources in unique_baselines.items():
                source_label = ", ".join(sources)
                if model_row.get("secondary_code") != current_secondary and (model_row.get("secondary_code") is not None or current_secondary is not None):
                    diffs.append({"paper_id": paper_id, "title": paper.get("title", ""), "difference_type": "secondary_code_mismatch", "module": code, "current": current_secondary or "null", "audit": model_row.get("secondary_code") or "null", "reason": f"Compared with {source_label}. {model_row.get('taxonomy_gap_reason') or ''}", "evidence": evidence, "source_type": saved.get("source_type", "")})
                if model_row.get("tertiary_code") != current_tertiary and (model_row.get("tertiary_code") is not None or current_tertiary is not None):
                    diffs.append({"paper_id": paper_id, "title": paper.get("title", ""), "difference_type": "tertiary_code_mismatch", "module": code, "current": current_tertiary or "null", "audit": model_row.get("tertiary_code") or "null", "reason": f"Compared with {source_label}. {model_row.get('taxonomy_gap_reason') or ''}", "evidence": evidence, "source_type": saved.get("source_type", "")})
        current_bucket = "01.04" if paper.get("general_method_bucket") not in (None, "", "none") else None
        audit_bucket = assessment.get("classification_bucket")
        if current_bucket != audit_bucket:
            diffs.append({"paper_id": paper_id, "title": paper.get("title", ""), "difference_type": "general_method_bucket_mismatch", "current": current_bucket or "null", "audit": audit_bucket or "null", "reason": assessment["overall_rationale"], "evidence": json.dumps(assessment.get("object_evidence", []), ensure_ascii=False), "source_type": saved.get("source_type", "")})
        if assessment.get("needs_human_review") or saved.get("source_type") != "pdf_full_text":
            review_reasons = list(assessment.get("human_review_reasons") or []) + list(assessment.get("source_limitations") or [])
            diffs.append({"paper_id": paper_id, "title": paper.get("title", ""), "difference_type": "source_or_model_review_required", "current": ";".join(sorted(existing)), "audit": ";".join(sorted(audited_modules)), "reason": "; ".join(review_reasons) or f"Evidence source was {saved.get('source_type')}.", "evidence": json.dumps(assessment.get("object_evidence", []), ensure_ascii=False), "source_type": saved.get("source_type", "")})
    return diffs


def write_reports(papers: list[dict[str, Any]], run_dir: pathlib.Path) -> None:
    diffs = compare_results(papers, run_dir)
    report_path = run_dir / "classification_differences.csv"
    fields = ["paper_id", "title", "difference_type", "module", "current", "audit", "reason", "evidence", "source_type"]
    with report_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(diffs)
    review_fields = fields + ["review_status", "human_decision", "reviewer_notes"]
    with (run_dir / "manual_review_queue.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=review_fields, extrasaction="ignore")
        writer.writeheader()
        for row in diffs:
            writer.writerow({**row, "review_status": "not_started", "human_decision": "", "reviewer_notes": ""})
    statuses = {}
    source_counts: dict[str, int] = {}
    for paper in papers:
        if not paper.get("active_confirmed_core"):
            continue
        result_path = run_dir / "results" / f"{paper['paper_id']}.json"
        if result_path.is_file():
            saved = json.loads(result_path.read_text(encoding="utf-8"))
            statuses[saved.get("status", "unknown")] = statuses.get(saved.get("status", "unknown"), 0) + 1
            if saved.get("status") == "completed":
                source = saved.get("source_type", "unknown")
                source_counts[source] = source_counts.get(source, 0) + 1
    type_counts: dict[str, int] = {}
    for row in diffs:
        type_counts[row["difference_type"]] = type_counts.get(row["difference_type"], 0) + 1
    summary = {
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "core_paper_count": sum(bool(p.get("active_confirmed_core")) for p in papers),
        "result_status_counts": statuses,
        "evidence_source_counts": source_counts,
        "difference_rows": len(diffs),
        "difference_type_counts": type_counts,
        "manual_review_queue": "manual_review_queue.csv",
        "classification_differences": "classification_differences.csv",
        "writeback_performed": False,
    }
    atomic_json(run_dir / "summary.json", summary)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", type=pathlib.Path, default=DEFAULT_RUN_DIR)
    parser.add_argument("--jobs", type=int, default=2)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--paper-id", action="append", default=[])
    parser.add_argument("--pdf-override", type=pathlib.Path, help="Use this PDF for the single paper selected with --paper-id")
    parser.add_argument("--context-file", type=pathlib.Path, help="Additional context text to include with each selected paper")
    parser.add_argument("--context-dir", type=pathlib.Path, help="Per-paper context files named ASD-####.md or .txt")
    parser.add_argument("--no-fetch-arxiv", action="store_true", help="Do not retrieve missing PDFs from official arXiv URLs")
    parser.add_argument("--no-fetch-openalex", action="store_true", help="Do not retrieve OpenAlex-listed open-access PDFs")
    parser.add_argument("--model", choices=[REQUIRED_MODEL], default=REQUIRED_MODEL)
    parser.add_argument("--reasoning-effort", choices=["low", "medium", "high", "xhigh"], default="medium")
    parser.add_argument("--codex-bin", default="codex")
    parser.add_argument("--timeout", type=int, default=900)
    parser.add_argument("--force", action="store_true", help="rerun even papers with completed results")
    parser.add_argument("--no-compare", action="store_true")
    args = parser.parse_args()
    if args.jobs < 1:
        parser.error("--jobs must be >= 1")
    if not shutil.which(args.codex_bin):
        parser.error(f"Codex CLI not found: {args.codex_bin}")
    try:
        args.codex_config_args = codex_config_overrides()
    except RuntimeError as exc:
        parser.error(str(exc))
    papers = [p for p in read_jsonl(PAPERS_PATH) if p.get("active_confirmed_core") is True]
    selected = set(args.paper_id)
    if args.pdf_override and len(selected) != 1:
        parser.error("--pdf-override requires exactly one --paper-id")
    if args.context_file:
        args.context_file = args.context_file.expanduser().resolve()
        if not args.context_file.is_file():
            parser.error(f"context file does not exist: {args.context_file}")
    if args.context_dir:
        args.context_dir = args.context_dir.expanduser().resolve()
    if selected:
        papers = [p for p in papers if p["paper_id"] in selected]
        missing = selected - {p["paper_id"] for p in papers}
        if missing:
            parser.error(f"paper IDs are not active confirmed core records: {sorted(missing)}")
    if args.limit is not None:
        papers = papers[:args.limit]
    run_dir = args.run_dir if args.run_dir.is_absolute() else PROJECT_ROOT / args.run_dir
    existing_manifest_path = run_dir / "manifest.json"
    if existing_manifest_path.is_file():
        try:
            existing_manifest = json.loads(existing_manifest_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            parser.error(f"cannot read existing run manifest {existing_manifest_path}: {exc}")
        if existing_manifest.get("model") != args.model:
            parser.error(
                f"run directory is already associated with model {existing_manifest.get('model')!r}; "
                f"use a fresh --run-dir for {args.model}"
            )
    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / "results").mkdir(exist_ok=True)
    (run_dir / "raw").mkdir(exist_ok=True)
    (run_dir / "logs").mkdir(exist_ok=True)
    index, codebook = load_taxonomy()
    rules = project_rules()
    manifest = {
        "created_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "project_root": str(PROJECT_ROOT),
        "paper_count_selected": len(papers),
        "selected_paper_ids": [p["paper_id"] for p in papers],
        "codex_version": subprocess.run([args.codex_bin, "--version"], capture_output=True, text=True).stdout.strip(),
        "model": args.model,
        "reasoning_effort": args.reasoning_effort,
        "jobs": args.jobs,
        "codex_user_config_ignored_for_plugins": "--ignore-user-config" in args.codex_config_args,
        "prompt_sha256": hashlib.sha256(PROMPT_PATH.read_bytes()).hexdigest(),
        "code_index_sha256": hashlib.sha256(CODE_INDEX_PATH.read_bytes()).hexdigest(),
        "writeback_performed": False,
    }
    manifest_path = run_dir / "manifest.json"
    invocation = {
        "started_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "jobs": args.jobs,
        "reasoning_effort": args.reasoning_effort,
        "timeout_seconds": args.timeout,
        "codex_user_config_ignored_for_plugins": manifest["codex_user_config_ignored_for_plugins"],
    }
    if manifest_path.exists():
        existing_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        existing_manifest.setdefault("invocations", []).append(invocation)
        existing_manifest["last_jobs"] = args.jobs
        existing_manifest["last_reasoning_effort"] = args.reasoning_effort
        existing_manifest["codex_user_config_ignored_for_plugins"] = manifest["codex_user_config_ignored_for_plugins"]
        atomic_json(manifest_path, existing_manifest)
    else:
        manifest["invocations"] = [invocation]
        atomic_json(manifest_path, manifest)
    pending = []
    for paper in papers:
        result_path = run_dir / "results" / f"{paper['paper_id']}.json"
        if result_path.exists() and not args.force:
            try:
                saved = json.loads(result_path.read_text(encoding="utf-8"))
                if saved.get("status") == "completed" and saved.get("model") == args.model:
                    continue
            except (OSError, json.JSONDecodeError):
                pass
        pending.append(paper)
    print(f"Selected {len(papers)} confirmed-core papers; {len(pending)} need audit; run directory: {run_dir}", flush=True)
    outcomes: dict[str, int] = {}
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        futures = [pool.submit(run_one, paper, args, rules, codebook, index, run_dir) for paper in pending]
        for future in as_completed(futures):
            paper_id, status = future.result()
            outcomes[status] = outcomes.get(status, 0) + 1
            print(f"{paper_id}: {status} ({sum(outcomes.values())}/{len(futures)})", flush=True)
    if not args.no_compare:
        write_reports([p for p in read_jsonl(PAPERS_PATH) if p.get("active_confirmed_core") is True], run_dir)
        print(f"Wrote comparison and review queue under {run_dir}", flush=True)
    return 1 if outcomes.get("error") else 0


if __name__ == "__main__":
    raise SystemExit(main())
