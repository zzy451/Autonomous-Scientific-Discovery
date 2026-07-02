#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Dict, Iterable, List


ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "Data"
EXPECTED_ACTIVE_CONFIRMED = 447
EXPECTED_ACTIVE_LOCAL_PDF = 421
EXPECTED_ACTIVE_NO_LOCAL_PDF = 26
EXPECTED_NO_LOCAL_IDS = {
    "ASD-0005",
    "ASD-0097",
    "ASD-0112",
    "ASD-0158",
    "ASD-0381",
    "ASD-0508",
    "ASD-0536",
    "ASD-0544",
    "ASD-0547",
    "ASD-0565",
    "ASD-0569",
    "ASD-0572",
    "ASD-0592",
    "ASD-0603",
    "ASD-0609",
    "ASD-0617",
    "ASD-0631",
    "ASD-0724",
    "ASD-0727",
    "ASD-0735",
    "ASD-0854",
    "ASD-0855",
    "ASD-0858",
    "ASD-0859",
    "ASD-0860",
    "ASD-0861",
}
FORMAL_MODULES = {f"{idx:02d}" for idx in range(1, 12)}
GENERAL_BUCKET_CANONICAL = (
    "01.04_general_asd_methods_without_concrete_object_experiments"
)
OBJECT_COVERAGE_MODES = {
    "single_module",
    "multi_module",
    "general_method_without_concrete_object_experiments",
}
REMARK_KEYS = (
    "scientific_object_modules",
    "object_coverage_mode",
    "primary_module_for_filing",
    "general_method_bucket",
    "first_hand_sources_checked",
)
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
POLLUTION_TOKENS = (
    "scientific_object_modules=",
    "object_coverage_mode=",
    "primary_module_for_filing=",
    "general_method_bucket=",
    "first_hand_sources_checked=",
    "evidence=",
    "source_limited=",
)
LOCAL_PDF_STATUSES = {
    "archived_pdf",
    "official_supplementary_pdf_archived_main_article_gated",
}
PAPER_ID_PATTERN = re.compile(r"^ASD-\d{4}$")


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> List[Dict[str, object]]:
    rows: List[Dict[str, object]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def split_semicolon_list(value: str) -> List[str]:
    return [item.strip() for item in value.split(";") if item.strip()]


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


def extract_last_remark_value(remarks: str, key: str) -> str:
    if not remarks:
        return ""
    if key == "first_hand_sources_checked":
        return extract_first_hand_sources_checked(remarks)
    matches = list(REMARK_VALUE_PATTERNS[key].finditer(remarks))
    if not matches:
        return ""
    return normalize_extracted_remark_value(matches[-1].group(1))


def extract_expected_structured_values(remarks: str) -> Dict[str, str]:
    return {key: extract_last_remark_value(remarks, key) for key in REMARK_KEYS}


def normalize_general_bucket(raw_value: str) -> str:
    raw = raw_value.strip().lower()
    if not raw or raw == "none":
        return "none"
    if raw.startswith("01.04"):
        return GENERAL_BUCKET_CANONICAL
    return raw_value.strip()


def normalize_module_list(raw_value: str) -> List[str]:
    modules = [code for code in split_semicolon_list(raw_value) if code in FORMAL_MODULES]
    return list(dict.fromkeys(modules))


def has_pollution_artifact(value: str) -> bool:
    lower_value = value.lower()
    return any(token in lower_value for token in POLLUTION_TOKENS)


def is_obvious_pdf_status_conflict(pdf_exists: bool, pdf_status: str) -> bool:
    status = pdf_status.strip().lower()
    if not status:
        return False
    if pdf_exists:
        return "no_local" in status or status == "safety_skip"
    return status in LOCAL_PDF_STATUSES


def main() -> None:
    strict_authoritative = os.environ.get("ASD_STRICT_AUTHORITATIVE", "1") != "0"
    papers = load_jsonl(DATA_DIR / "papers.jsonl")
    taxonomy_index = load_json(DATA_DIR / "taxonomy_index.json")
    pdf_manifest = load_json(DATA_DIR / "pdf_manifest.json")
    missing_pdf_manifest = load_json(DATA_DIR / "missing_pdf_manifest.json")
    note_manifest = load_json(DATA_DIR / "note_manifest.json")

    paper_ids = [row["paper_id"] for row in papers]
    assert_true(len(paper_ids) == len(set(paper_ids)), "Duplicate paper_id found in papers.jsonl")

    active = [row for row in papers if row["active_confirmed_core"]]
    active_local_pdf = [row for row in active if row["pdf_exists"]]
    active_no_local_pdf = [row for row in active if not row["pdf_exists"]]
    active_no_local_ids = {row["paper_id"] for row in active_no_local_pdf}
    assert_true(
        len(active_local_pdf) + len(active_no_local_pdf) == len(active),
        "Active paper PDF partition mismatch",
    )

    if strict_authoritative:
        assert_true(
            len(active) == EXPECTED_ACTIVE_CONFIRMED,
            f"Active confirmed-core count mismatch: {len(active)} != {EXPECTED_ACTIVE_CONFIRMED}",
        )
        assert_true(
            len(active_local_pdf) == EXPECTED_ACTIVE_LOCAL_PDF,
            f"Active local-PDF count mismatch: {len(active_local_pdf)} != {EXPECTED_ACTIVE_LOCAL_PDF}",
        )
        assert_true(
            len(active_no_local_pdf) == EXPECTED_ACTIVE_NO_LOCAL_PDF,
            f"Active no-local-PDF count mismatch: {len(active_no_local_pdf)} != {EXPECTED_ACTIVE_NO_LOCAL_PDF}",
        )
        assert_true(
            active_no_local_ids == EXPECTED_NO_LOCAL_IDS,
            "Active no-local-PDF ID set does not match authoritative 26-paper baseline",
        )

    taxonomy_codes = set(taxonomy_index["code_to_label"].keys())
    assert_true("01.04" in taxonomy_codes, "taxonomy_index.json missing 01.04")
    assert_true(FORMAL_MODULES.issubset(taxonomy_codes), "taxonomy_index.json missing formal module codes")

    for row in papers:
        paper_id = row["paper_id"]
        assert_true(
            isinstance(paper_id, str) and PAPER_ID_PATTERN.fullmatch(paper_id) is not None,
            f"Invalid paper_id format: {paper_id!r}",
        )
        assert_true(isinstance(row["pdf_exists"], bool), f"{paper_id} pdf_exists is not a bool")
        assert_true(isinstance(row["note_exists"], bool), f"{paper_id} note_exists is not a bool")
        assert_true(
            isinstance(row["active_confirmed_core"], bool),
            f"{paper_id} active_confirmed_core is not a bool",
        )

        modules = row["scientific_object_modules"]
        assert_true(isinstance(modules, list), f"{paper_id} scientific_object_modules is not a list")
        invalid_modules = [code for code in modules if code not in FORMAL_MODULES]
        assert_true(not invalid_modules, f"{paper_id} has invalid module codes: {invalid_modules}")
        assert_true(len(modules) == len(set(modules)), f"{paper_id} has duplicate scientific_object_modules")
        assert_true(
            GENERAL_BUCKET_CANONICAL not in modules,
            f"{paper_id} general method bucket leaked into scientific_object_modules",
        )

        general_bucket = row["general_method_bucket"]
        assert_true(
            general_bucket in {"none", GENERAL_BUCKET_CANONICAL},
            f"{paper_id} has invalid general_method_bucket: {general_bucket!r}",
        )

        object_coverage_mode = row["object_coverage_mode"]
        assert_true(
            object_coverage_mode in OBJECT_COVERAGE_MODES or object_coverage_mode == "",
            f"{paper_id} has invalid object_coverage_mode: {object_coverage_mode!r}",
        )

        primary_module = row["primary_module_for_filing"]
        assert_true(
            primary_module in FORMAL_MODULES or primary_module == "",
            f"{paper_id} has invalid primary_module_for_filing: {primary_module!r}",
        )

        first_hand_sources_checked = row["first_hand_sources_checked"]
        assert_true(
            isinstance(first_hand_sources_checked, str),
            f"{paper_id} first_hand_sources_checked is not a string",
        )
        assert_true(
            not has_pollution_artifact(first_hand_sources_checked),
            f"{paper_id} first_hand_sources_checked appears polluted: {first_hand_sources_checked!r}",
        )

        if general_bucket != "none":
            assert_true(
                modules == [],
                f"{paper_id} should not carry scientific_object_modules when general_method_bucket is set",
            )
            assert_true(
                object_coverage_mode == "general_method_without_concrete_object_experiments",
                f"{paper_id} has inconsistent object_coverage_mode for general_method_bucket",
            )
            assert_true(
                primary_module == "01",
                f"{paper_id} should file general-method bucket rows under module 01",
            )
        elif modules:
            expected_mode = "multi_module" if len(modules) > 1 else "single_module"
            assert_true(
                object_coverage_mode == expected_mode,
                f"{paper_id} has inconsistent object_coverage_mode {object_coverage_mode!r} for modules {modules}",
            )
            assert_true(
                primary_module in modules or primary_module == row["legacy_main_class"],
                f"{paper_id} primary_module_for_filing {primary_module!r} is neither in scientific_object_modules {modules} nor equal to legacy_main_class {row['legacy_main_class']!r}",
            )

        pdf_path = row["pdf_path"]
        assert_true(isinstance(pdf_path, str), f"{paper_id} pdf_path is not a string")
        if row["pdf_exists"]:
            assert_true(bool(pdf_path), f"{paper_id} has pdf_exists=true but empty pdf_path")
        assert_true(
            not is_obvious_pdf_status_conflict(row["pdf_exists"], row["pdf_status"]),
            f"{paper_id} has obvious pdf_exists/pdf_status conflict: pdf_exists={row['pdf_exists']}, pdf_status={row['pdf_status']!r}",
        )

        expected_from_remarks = extract_expected_structured_values(row["remarks"])
        expected_modules = normalize_module_list(expected_from_remarks["scientific_object_modules"])
        if expected_modules:
            assert_true(
                modules == expected_modules,
                f"{paper_id} scientific_object_modules disagrees with remarks: {modules} != {expected_modules}",
            )

        expected_coverage_mode = expected_from_remarks["object_coverage_mode"]
        if expected_coverage_mode:
            assert_true(
                object_coverage_mode == expected_coverage_mode,
                f"{paper_id} object_coverage_mode disagrees with remarks: {object_coverage_mode!r} != {expected_coverage_mode!r}",
            )

        expected_primary_module = expected_from_remarks["primary_module_for_filing"]
        if expected_primary_module:
            assert_true(
                primary_module == expected_primary_module,
                f"{paper_id} primary_module_for_filing disagrees with remarks: {primary_module!r} != {expected_primary_module!r}",
            )

        raw_expected_general_bucket = expected_from_remarks["general_method_bucket"]
        if raw_expected_general_bucket:
            expected_general_bucket = normalize_general_bucket(raw_expected_general_bucket)
            assert_true(
                general_bucket == expected_general_bucket,
                f"{paper_id} general_method_bucket disagrees with remarks: {general_bucket!r} != {expected_general_bucket!r}",
            )

        expected_first_hand = expected_from_remarks["first_hand_sources_checked"]
        if expected_first_hand:
            assert_true(
                first_hand_sources_checked == expected_first_hand,
                f"{paper_id} first_hand_sources_checked disagrees with remarks: {first_hand_sources_checked!r} != {expected_first_hand!r}",
            )

    pdf_manifest_ids = {row["paper_id"] for row in pdf_manifest}
    missing_manifest_ids = {row["paper_id"] for row in missing_pdf_manifest}
    active_ids = {row["paper_id"] for row in active}
    assert_true(
        pdf_manifest_ids.intersection(missing_manifest_ids) == set(),
        "Some papers appear in both pdf_manifest and missing_pdf_manifest",
    )
    assert_true(
        pdf_manifest_ids.union(missing_manifest_ids).issuperset(active_ids),
        "Some active confirmed-core papers are missing from both PDF manifests",
    )
    assert_true(
        pdf_manifest_ids == {row["paper_id"] for row in papers if row["pdf_exists"]},
        "pdf_manifest paper_id coverage does not match papers.jsonl pdf_exists=true rows",
    )
    assert_true(
        missing_manifest_ids == {row["paper_id"] for row in active_no_local_pdf},
        "missing_pdf_manifest paper_id coverage does not match active no-local-PDF rows",
    )

    for row in pdf_manifest:
        pdf_path = row["pdf_path"]
        assert_true((ROOT / pdf_path).exists(), f"PDF path does not exist: {pdf_path}")
        assert_true(bool(row["sha256"]), f"Missing sha256 for {row['paper_id']}")

    note_manifest_ids = {row["paper_id"] for row in note_manifest}
    assert_true(note_manifest_ids == set(paper_ids), "note_manifest paper_id coverage mismatch")

    print(f"papers.jsonl records: {len(papers)}")
    print(f"active confirmed-core: {len(active)}")
    print(f"active local PDFs: {len(active_local_pdf)}")
    print(f"active no-local-PDF: {len(active_no_local_pdf)}")
    print("All structured-data consistency checks passed.")


if __name__ == "__main__":
    main()
