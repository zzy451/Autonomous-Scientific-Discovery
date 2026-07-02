#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Tuple


ROOT = Path(__file__).resolve().parent.parent
MASTER_PATH = ROOT / "Paper_Lists" / "agent_master_paper_list.md"
PROGRESS_PATH = (
    ROOT
    / "Coverage_Check"
    / "multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md"
)
DATA_DIR = ROOT / "Data"

MASTER_HEADER = [
    "ID",
    "Paper title",
    "Authors",
    "Year",
    "Source",
    "DOI / arXiv / URL",
    "PDF path",
    "Is Agent",
    "Inclusion status",
    "Exclusion reason",
    "Main class",
    "Secondary class",
    "Tertiary class",
    "Fourth-level topic",
    "New fourth-level",
    "Agent type",
    "Research workflow role",
    "Validation type",
    "Scientific contribution type",
    "Evidence strength",
    "Citation priority",
    "Note path",
    "Remarks",
]

PROGRESS_HEADER = [
    "paper_id",
    "title",
    "note_path",
    "pdf_status",
    "pdf_path",
    "evidence_status",
    "note_status",
    "master_status",
    "final_modules_or_bucket",
    "source_limited",
    "batch",
    "closed",
]

FORMAL_MODULES = {f"{idx:02d}" for idx in range(1, 12)}
GENERAL_BUCKET_CANONICAL = (
    "01.04_general_asd_methods_without_concrete_object_experiments"
)
OBJECT_COVERAGE_MODES = {
    "single_module",
    "multi_module",
    "general_method_without_concrete_object_experiments",
}

TAXONOMY_CODE_TO_LABEL = {
    "01": "Formal, Information and Computational Sciences",
    "01.04": "General ASD Methods without Concrete Object Experiments",
    "02": "Physics, Astronomy and Cosmic Sciences",
    "03": "Chemical Sciences",
    "04": "Materials Science",
    "05": "Earth and Environmental Sciences",
    "06": "Life Sciences",
    "07": "Medical and Health Sciences",
    "08": "Agricultural, Food, Forestry, Animal and Fishery Sciences",
    "09": "Engineering and Industrial Technology Sciences",
    "10": "Aerospace, Marine and Transportation Sciences",
    "11": "Social, Behavioral, Economic and Knowledge System Sciences",
}

REMARK_KEYS = [
    "scientific_object_modules",
    "object_coverage_mode",
    "primary_module_for_filing",
    "general_method_bucket",
    "first_hand_sources_checked",
]

REMARK_VALUE_PATTERNS = {
    "scientific_object_modules": re.compile(
        r"(?<![A-Za-z0-9_])scientific_object_modules\s*=\s*`?([0-9]{2}(?:\s*;\s*[0-9]{2})*)`?",
        re.IGNORECASE,
    ),
    "object_coverage_mode": re.compile(
        r"(?<![A-Za-z0-9_])object_coverage_mode\s*=\s*`?(single_module|multi_module|general_method_without_concrete_object_experiments)`?",
        re.IGNORECASE,
    ),
    "primary_module_for_filing": re.compile(
        r"(?<![A-Za-z0-9_])primary_module_for_filing\s*=\s*`?([0-9]{2})`?",
        re.IGNORECASE,
    ),
    "general_method_bucket": re.compile(
        r"(?<![A-Za-z0-9_])general_method_bucket\s*=\s*`?(none|01\.04(?:_general_asd_methods_without_concrete_object_experiments)?)`?",
        re.IGNORECASE,
    ),
    "first_hand_sources_checked": re.compile(
        r"(?<![A-Za-z0-9_])first_hand_sources_checked\s*=\s*",
        re.IGNORECASE,
    ),
}
FIRST_HAND_CONTINUATION_PREFIXES = (
    "official",
    "arxiv",
    "ar5iv",
    "crossref",
    "doi",
    "publisher",
    "pmc",
    "pubmed",
    "amazon",
    "science",
    "nature",
    "zenodo",
    "github",
    "repo",
    "project",
    "landing",
    "html",
    "pdf",
    "preprint",
    "canonical",
    "full paper",
    "full text",
    "biorxiv",
    "ssrn",
    "api",
    "dataset",
    "jpl",
)
FIRST_HAND_STOP_PREFIXES = (
    "evidence",
    "the ",
    "this ",
    "current ",
    "keep ",
    "note ",
    "prior ",
    "independent ",
    "legacy ",
    "stale ",
    "reviewer",
    "scientific_object_modules",
    "object_coverage_mode",
    "primary_module_for_filing",
    "general_method_bucket",
    "source_limited",
)


@dataclass
class MarkdownTable:
    header: List[str]
    rows: List[Dict[str, str]]


def split_markdown_row(line: str, expected_cols: int) -> List[str]:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        raise ValueError(f"Not a markdown row: {line!r}")
    parts = [part.strip() for part in stripped[1:-1].split("|")]
    if len(parts) > expected_cols:
        merged = parts[: expected_cols - 1] + ["|".join(parts[expected_cols - 1 :]).strip()]
        parts = merged
    if len(parts) < expected_cols:
        parts.extend([""] * (expected_cols - len(parts)))
    return parts


def is_markdown_separator(line: str) -> bool:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return False
    cells = [cell.strip() for cell in stripped[1:-1].split("|")]
    if not cells:
        return False
    return all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells)


def parse_markdown_table(
    path: Path, header_marker: str, expected_header: List[str], data_prefix: str
) -> MarkdownTable:
    lines = read_text_lossy(path).splitlines()
    start_index = None
    for idx, line in enumerate(lines):
        if line.strip() == header_marker:
            start_index = idx
            break
    if start_index is None:
        raise ValueError(f"Header marker not found in {path}: {header_marker}")

    header = split_markdown_row(lines[start_index], len(expected_header))
    if header != expected_header:
        raise ValueError(f"Unexpected header in {path}: {header}")

    rows: List[Dict[str, str]] = []
    data_start = start_index + 1
    if data_start < len(lines) and is_markdown_separator(lines[data_start]):
        data_start += 1

    for line in lines[data_start:]:
        if not line.startswith(data_prefix):
            if rows:
                continue
            continue
        parts = split_markdown_row(line, len(expected_header))
        rows.append(dict(zip(expected_header, parts)))
    return MarkdownTable(header=header, rows=rows)


def read_text_lossy(path: Path) -> str:
    raw = path.read_bytes()
    for encoding in ("utf-8", "utf-8-sig", "gb18030"):
        try:
            return raw.decode(encoding)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", errors="replace")


def split_semicolon_list(value: str) -> List[str]:
    return [item.strip() for item in value.split(";") if item.strip()]


def parse_doi_and_arxiv(value: str) -> Tuple[str, str, str]:
    doi = ""
    arxiv_id = ""
    url = value.strip()
    doi_match = re.search(r"(10\.\d{4,9}/\S+)", value)
    if doi_match:
        doi = doi_match.group(1).rstrip(".,;")
    arxiv_match = re.search(r"arxiv\.org/(?:abs|pdf)/([0-9]{4}\.[0-9]{4,5}(?:v\d+)?)", value, re.I)
    if arxiv_match:
        arxiv_id = arxiv_match.group(1)
    return doi, arxiv_id, url


def normalize_extracted_remark_value(raw_value: str) -> str:
    value = raw_value.strip()
    while value and value[0] in "'\"([{":
        value = value[1:].lstrip()
    while value and value[-1] in "'\".,;)]}":
        value = value[:-1].rstrip()
    return value


def is_likely_first_hand_continuation(clause: str) -> bool:
    lowered = clause.strip().lower()
    if not lowered:
        return False
    if "=" in lowered:
        return False
    if lowered.startswith(FIRST_HAND_STOP_PREFIXES):
        return False
    if lowered.startswith(FIRST_HAND_CONTINUATION_PREFIXES):
        return True
    return any(
        marker in lowered
        for marker in (" github", " ar5iv", " doi", " pdf", " html", " repo", " api")
    )


def extract_first_hand_sources_checked(remarks: str) -> str:
    matches = list(REMARK_VALUE_PATTERNS["first_hand_sources_checked"].finditer(remarks))
    if not matches:
        return ""
    tail = remarks[matches[-1].end() :]
    next_assignment = re.search(r"[;,]\s*[a-z_]+\s*=", tail, re.IGNORECASE)
    candidate = tail[: next_assignment.start()] if next_assignment else tail
    parts = [part.strip() for part in candidate.split(";") if part.strip()]
    if not parts:
        return ""
    kept_parts = [parts[0]]
    for part in parts[1:]:
        if not is_likely_first_hand_continuation(part):
            break
        kept_parts.append(part)
    return normalize_extracted_remark_value("; ".join(kept_parts))


def extract_remark_value(remarks: str, key: str) -> str:
    if not remarks:
        return ""
    if key == "first_hand_sources_checked":
        return extract_first_hand_sources_checked(remarks)
    pattern = REMARK_VALUE_PATTERNS[key]
    matches = list(pattern.finditer(remarks))
    if not matches:
        return ""
    return normalize_extracted_remark_value(matches[-1].group(1))


def extract_structured_remark_fields(remarks: str) -> Dict[str, str]:
    return {key: extract_remark_value(remarks, key) for key in REMARK_KEYS}


def normalize_general_method_bucket(raw_value: str, legacy_main: str, legacy_secondary: str) -> str:
    raw = raw_value.strip()
    if not raw and legacy_main == "01" and legacy_secondary == "01.04":
        raw = "01.04"
    raw_lower = raw.lower()
    if raw_lower in {"", "none"}:
        return "none"
    if raw_lower.startswith("01.04"):
        return GENERAL_BUCKET_CANONICAL
    return raw


def normalize_modules(raw_value: str, legacy_main: str, general_bucket: str) -> List[str]:
    modules = [code for code in split_semicolon_list(raw_value) if code in FORMAL_MODULES]
    if modules:
        return list(dict.fromkeys(modules))
    if general_bucket != "none":
        return []
    if legacy_main in FORMAL_MODULES:
        return [legacy_main]
    return []


def normalize_object_coverage_mode(raw_value: str, modules: List[str], general_bucket: str) -> str:
    raw = raw_value.strip()
    if raw in OBJECT_COVERAGE_MODES:
        return raw
    if general_bucket != "none":
        return "general_method_without_concrete_object_experiments"
    if len(modules) > 1:
        return "multi_module"
    if len(modules) == 1:
        return "single_module"
    return ""


def normalize_primary_module(raw_value: str, legacy_main: str, modules: List[str]) -> str:
    raw = raw_value.strip()
    if raw in FORMAL_MODULES:
        return raw
    if legacy_main in FORMAL_MODULES:
        return legacy_main
    return modules[0] if modules else ""


def path_exists(repo_relative_path: str) -> bool:
    if not repo_relative_path:
        return False
    return (ROOT / repo_relative_path).exists()


def build_papers(master_rows: Iterable[Dict[str, str]], progress_rows: Dict[str, Dict[str, str]]) -> List[Dict[str, object]]:
    exported_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    papers: List[Dict[str, object]] = []

    for row in master_rows:
        paper_id = row["ID"]
        progress = progress_rows.get(paper_id, {})
        remarks = row["Remarks"]

        structured_remarks = extract_structured_remark_fields(remarks)
        raw_modules = structured_remarks["scientific_object_modules"]
        raw_object_coverage_mode = structured_remarks["object_coverage_mode"]
        raw_primary_module = structured_remarks["primary_module_for_filing"]
        raw_general_bucket = structured_remarks["general_method_bucket"]
        first_hand_sources_checked = structured_remarks["first_hand_sources_checked"]

        general_method_bucket = normalize_general_method_bucket(
            raw_general_bucket, row["Main class"], row["Secondary class"]
        )
        scientific_object_modules = normalize_modules(
            raw_modules, row["Main class"], general_method_bucket
        )
        object_coverage_mode = normalize_object_coverage_mode(
            raw_object_coverage_mode, scientific_object_modules, general_method_bucket
        )
        primary_module_for_filing = normalize_primary_module(
            raw_primary_module, row["Main class"], scientific_object_modules
        )

        doi, arxiv_id, url = parse_doi_and_arxiv(row["DOI / arXiv / URL"])
        note_path = progress.get("note_path") or row["Note path"]
        pdf_path = progress.get("pdf_path") or row["PDF path"]
        pdf_exists = path_exists(pdf_path)
        note_exists = path_exists(note_path)
        source_limited = (progress.get("source_limited") or "").strip().lower()
        is_active_confirmed_core = (
            row["Inclusion status"] in {"to_read", "included"}
            and (bool(scientific_object_modules) or general_method_bucket != "none")
        )

        papers.append(
            {
                "paper_id": paper_id,
                "title": row["Paper title"],
                "authors": row["Authors"],
                "year": row["Year"],
                "source": row["Source"],
                "doi_or_url": row["DOI / arXiv / URL"],
                "doi": doi,
                "url": url,
                "arxiv_id": arxiv_id,
                "pdf_path": pdf_path,
                "pdf_exists": pdf_exists,
                "note_path": note_path,
                "note_exists": note_exists,
                "is_agent": row["Is Agent"],
                "inclusion_status": row["Inclusion status"],
                "exclusion_reason": row["Exclusion reason"],
                "legacy_main_class": row["Main class"],
                "legacy_secondary_class": row["Secondary class"],
                "legacy_tertiary_class": row["Tertiary class"],
                "fourth_level_topic": row["Fourth-level topic"],
                "new_fourth_level": row["New fourth-level"],
                "agent_type_raw": row["Agent type"],
                "agent_type": split_semicolon_list(row["Agent type"]),
                "research_workflow_role_raw": row["Research workflow role"],
                "research_workflow_role": split_semicolon_list(row["Research workflow role"]),
                "validation_type_raw": row["Validation type"],
                "validation_type": split_semicolon_list(row["Validation type"]),
                "scientific_contribution_type_raw": row["Scientific contribution type"],
                "scientific_contribution_type": split_semicolon_list(
                    row["Scientific contribution type"]
                ),
                "evidence_strength": row["Evidence strength"],
                "citation_priority": row["Citation priority"],
                "remarks": remarks,
                "scientific_object_modules": scientific_object_modules,
                "general_method_bucket": general_method_bucket,
                "object_coverage_mode": object_coverage_mode,
                "primary_module_for_filing": primary_module_for_filing,
                "first_hand_sources_checked": first_hand_sources_checked,
                "progress_title": progress.get("title", ""),
                "pdf_status": progress.get("pdf_status", ""),
                "evidence_status": progress.get("evidence_status", ""),
                "note_status": progress.get("note_status", ""),
                "master_status": progress.get("master_status", ""),
                "final_modules_or_bucket_raw": progress.get("final_modules_or_bucket", ""),
                "final_modules_or_bucket": split_semicolon_list(
                    progress.get("final_modules_or_bucket", "")
                ),
                "source_limited": source_limited,
                "batch": progress.get("batch", ""),
                "closed": progress.get("closed", ""),
                "active_confirmed_core": is_active_confirmed_core,
                "exported_at": exported_at,
            }
        )
    return papers


def build_taxonomy_index() -> Dict[str, Dict[str, str]]:
    label_to_code = {label: code for code, label in TAXONOMY_CODE_TO_LABEL.items()}
    return {"code_to_label": TAXONOMY_CODE_TO_LABEL, "label_to_code": label_to_code}


def compute_sha256(path: Path) -> str:
    import hashlib

    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_pdf_manifest(papers: Iterable[Dict[str, object]]) -> List[Dict[str, object]]:
    manifest: List[Dict[str, object]] = []
    for paper in papers:
        pdf_path = str(paper["pdf_path"])
        if not pdf_path or not bool(paper["pdf_exists"]):
            continue
        repo_path = ROOT / pdf_path
        manifest.append(
            {
                "paper_id": paper["paper_id"],
                "title": paper["title"],
                "pdf_path": pdf_path,
                "sha256": compute_sha256(repo_path),
                "primary_module_for_filing": paper["primary_module_for_filing"],
                "scientific_object_modules": paper["scientific_object_modules"],
                "pdf_status": paper["pdf_status"],
                "evidence_status": paper["evidence_status"],
                "active_confirmed_core": paper["active_confirmed_core"],
            }
        )
    return manifest


def build_missing_pdf_manifest(papers: Iterable[Dict[str, object]]) -> List[Dict[str, object]]:
    manifest: List[Dict[str, object]] = []
    for paper in papers:
        if not bool(paper["active_confirmed_core"]):
            continue
        if bool(paper["pdf_exists"]):
            continue
        manifest.append(
            {
                "paper_id": paper["paper_id"],
                "title": paper["title"],
                "doi": paper["doi"],
                "url": paper["url"],
                "pdf_status": paper["pdf_status"],
                "evidence_status": paper["evidence_status"],
                "source_limited": paper["source_limited"],
                "access_note": paper["remarks"],
            }
        )
    return manifest


def build_note_manifest(papers: Iterable[Dict[str, object]]) -> List[Dict[str, object]]:
    manifest: List[Dict[str, object]] = []
    for paper in papers:
        manifest.append(
            {
                "paper_id": paper["paper_id"],
                "title": paper["title"],
                "note_path": paper["note_path"],
                "note_exists": paper["note_exists"],
                "active_confirmed_core": paper["active_confirmed_core"],
                "inclusion_status": paper["inclusion_status"],
            }
        )
    return manifest


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_jsonl(path: Path, rows: Iterable[Dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def main() -> None:
    DATA_DIR.mkdir(exist_ok=True)

    master_table = parse_markdown_table(
        MASTER_PATH,
        header_marker="| " + " | ".join(MASTER_HEADER) + " |",
        expected_header=MASTER_HEADER,
        data_prefix="| ASD-",
    )
    progress_table = parse_markdown_table(
        PROGRESS_PATH,
        header_marker="| " + " | ".join(PROGRESS_HEADER) + " |",
        expected_header=PROGRESS_HEADER,
        data_prefix="| ASD-",
    )
    progress_rows = {row["paper_id"]: row for row in progress_table.rows}

    papers = build_papers(master_table.rows, progress_rows)
    taxonomy_index = build_taxonomy_index()
    pdf_manifest = build_pdf_manifest(papers)
    missing_pdf_manifest = build_missing_pdf_manifest(papers)
    note_manifest = build_note_manifest(papers)

    write_jsonl(DATA_DIR / "papers.jsonl", papers)
    write_json(DATA_DIR / "taxonomy_index.json", taxonomy_index)
    write_json(DATA_DIR / "pdf_manifest.json", pdf_manifest)
    write_json(DATA_DIR / "missing_pdf_manifest.json", missing_pdf_manifest)
    write_json(DATA_DIR / "note_manifest.json", note_manifest)

    print(f"Exported {len(papers)} paper records to {DATA_DIR}")
    print(f"Exported {len(pdf_manifest)} local PDF manifest rows")
    print(f"Exported {len(missing_pdf_manifest)} missing PDF manifest rows")
    print(f"Exported {len(note_manifest)} note manifest rows")


if __name__ == "__main__":
    main()
