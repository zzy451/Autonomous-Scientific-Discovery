#!/usr/bin/env python3
from __future__ import annotations

import json
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


def main() -> None:
    papers = load_jsonl(DATA_DIR / "papers.jsonl")
    taxonomy_index = load_json(DATA_DIR / "taxonomy_index.json")
    pdf_manifest = load_json(DATA_DIR / "pdf_manifest.json")
    missing_pdf_manifest = load_json(DATA_DIR / "missing_pdf_manifest.json")
    note_manifest = load_json(DATA_DIR / "note_manifest.json")

    paper_ids = [row["paper_id"] for row in papers]
    assert_true(len(paper_ids) == len(set(paper_ids)), "Duplicate paper_id found in papers.jsonl")

    active = [row for row in papers if row["active_confirmed_core"]]
    assert_true(
        len(active) == EXPECTED_ACTIVE_CONFIRMED,
        f"Active confirmed-core count mismatch: {len(active)} != {EXPECTED_ACTIVE_CONFIRMED}",
    )

    active_local_pdf = [row for row in active if row["pdf_exists"]]
    assert_true(
        len(active_local_pdf) == EXPECTED_ACTIVE_LOCAL_PDF,
        f"Active local-PDF count mismatch: {len(active_local_pdf)} != {EXPECTED_ACTIVE_LOCAL_PDF}",
    )

    active_no_local_pdf = [row for row in active if not row["pdf_exists"]]
    assert_true(
        len(active_no_local_pdf) == EXPECTED_ACTIVE_NO_LOCAL_PDF,
        f"Active no-local-PDF count mismatch: {len(active_no_local_pdf)} != {EXPECTED_ACTIVE_NO_LOCAL_PDF}",
    )

    active_no_local_ids = {row["paper_id"] for row in active_no_local_pdf}
    assert_true(
        active_no_local_ids == EXPECTED_NO_LOCAL_IDS,
        "Active no-local-PDF ID set does not match expected 26-paper baseline",
    )

    taxonomy_codes = set(taxonomy_index["code_to_label"].keys())
    assert_true("01.04" in taxonomy_codes, "taxonomy_index.json missing 01.04")
    assert_true(FORMAL_MODULES.issubset(taxonomy_codes), "taxonomy_index.json missing formal module codes")

    for row in papers:
        modules = row["scientific_object_modules"]
        assert_true(isinstance(modules, list), f"{row['paper_id']} scientific_object_modules is not a list")
        invalid_modules = [code for code in modules if code not in FORMAL_MODULES]
        assert_true(not invalid_modules, f"{row['paper_id']} has invalid module codes: {invalid_modules}")
        assert_true(
            GENERAL_BUCKET_CANONICAL not in modules,
            f"{row['paper_id']} general method bucket leaked into scientific_object_modules",
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
