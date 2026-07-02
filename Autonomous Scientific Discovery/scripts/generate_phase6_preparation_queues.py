#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import sqlite3
from pathlib import Path
from typing import Dict, Iterable, List


ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "Data"
COVERAGE_DIR = ROOT / "Coverage_Check"
PAPERS_JSONL = DATA_DIR / "papers.jsonl"
SQLITE_PATH = DATA_DIR / "papers.sqlite"
RUN_DATE = "2026-07-02"
ACTIVE_BASELINE = 447

NOTE_QUEUE_PATH = (
    COVERAGE_DIR / f"structured_data_phase6_note_revision_queue_{ACTIVE_BASELINE}_{RUN_DATE}.tsv"
)
FOLLOWUP_QUEUE_PATH = (
    COVERAGE_DIR / f"structured_data_phase6_full_text_followup_queue_{ACTIVE_BASELINE}_{RUN_DATE}.tsv"
)
REPRESENTATIVE_POOL_PATH = (
    COVERAGE_DIR / f"structured_data_phase6_representative_paper_pool_{ACTIVE_BASELINE}_{RUN_DATE}.tsv"
)
MODULE_COVERAGE_POOL_PATH = (
    COVERAGE_DIR / f"structured_data_phase6_module_coverage_pool_{ACTIVE_BASELINE}_{RUN_DATE}.tsv"
)
BOUNDARY_POOL_PATH = (
    COVERAGE_DIR / f"structured_data_phase6_boundary_case_pool_{ACTIVE_BASELINE}_{RUN_DATE}.tsv"
)
SUMMARY_PATH = (
    COVERAGE_DIR / f"structured_data_phase6_preparation_round1_{RUN_DATE}.md"
)


def load_jsonl(path: Path) -> List[Dict[str, object]]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def stringify_modules(paper: Dict[str, object]) -> str:
    modules = paper.get("scientific_object_modules", [])
    if isinstance(modules, list) and modules:
        return ";".join(str(module) for module in modules)
    bucket = str(paper.get("general_method_bucket", "none"))
    return "01.04" if bucket != "none" else ""


def citation_priority_score(value: str) -> int:
    mapping = {
        "core": 30,
        "standard": 20,
        "background": 10,
        "do_not_cite": 0,
    }
    return mapping.get(value.strip().lower(), 0)


def evidence_status_score(value: str) -> int:
    lowered = value.strip().lower()
    if "full_text" in lowered:
        return 16
    if "html_full_text" in lowered:
        return 14
    if "supporting_info" in lowered:
        return 12
    if "official_pages" in lowered or "official_repo" in lowered:
        return 10
    if "abstract" in lowered or "landing" in lowered:
        return 8
    return 0


def write_tsv(path: Path, fieldnames: Iterable[str], rows: List[Dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(fieldnames), delimiter="\t")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def build_note_revision_queue(papers: List[Dict[str, object]]) -> List[Dict[str, object]]:
    rows: List[Dict[str, object]] = []
    for paper in papers:
        if not paper["active_confirmed_core"]:
            continue
        reasons: List[str] = []
        priority_score = 0

        if paper["object_coverage_mode"] == "multi_module":
            reasons.append("multi_module_note_wording_check")
            priority_score += 30
        if paper["general_method_bucket"] != "none":
            reasons.append("bucket_0104_note_wording_check")
            priority_score += 35
        if paper["note_status"] == "updated_source_limited":
            reasons.append("source_limited_note_refresh")
            priority_score += 20
        if paper["source_limited"] == "yes":
            reasons.append("source_limited_wording_confirmation")
            priority_score += 10

        if not reasons:
            continue

        priority_score += citation_priority_score(str(paper["citation_priority"])) // 2

        rows.append(
            {
                "paper_id": paper["paper_id"],
                "title": paper["title"],
                "note_path": paper["note_path"],
                "primary_module_for_filing": paper["primary_module_for_filing"],
                "classification_anchor": stringify_modules(paper),
                "object_coverage_mode": paper["object_coverage_mode"],
                "general_method_bucket": paper["general_method_bucket"],
                "note_status": paper["note_status"],
                "source_limited": paper["source_limited"],
                "pdf_exists": "yes" if paper["pdf_exists"] else "no",
                "citation_priority": paper["citation_priority"],
                "queue_reasons": ";".join(reasons),
                "priority_score": priority_score,
            }
        )

    rows.sort(
        key=lambda row: (
            -int(row["priority_score"]),
            row["primary_module_for_filing"],
            row["paper_id"],
        )
    )
    return rows


def build_full_text_followup_queue(papers: List[Dict[str, object]]) -> List[Dict[str, object]]:
    rows: List[Dict[str, object]] = []
    for paper in papers:
        if not paper["active_confirmed_core"]:
            continue
        reasons: List[str] = []
        priority_score = 0

        if not paper["pdf_exists"]:
            reasons.append("no_local_pdf")
            priority_score += 35
        if paper["source_limited"] == "yes":
            reasons.append("source_limited")
            priority_score += 20
        evidence_status = str(paper["evidence_status"])
        if "full_text" not in evidence_status.lower():
            reasons.append("non_full_text_evidence_status")
            priority_score += 10

        if not reasons:
            continue

        priority_score += citation_priority_score(str(paper["citation_priority"]))

        rows.append(
            {
                "paper_id": paper["paper_id"],
                "title": paper["title"],
                "primary_module_for_filing": paper["primary_module_for_filing"],
                "classification_anchor": stringify_modules(paper),
                "pdf_status": paper["pdf_status"],
                "evidence_status": paper["evidence_status"],
                "pdf_exists": "yes" if paper["pdf_exists"] else "no",
                "source_limited": paper["source_limited"],
                "first_hand_sources_checked": paper["first_hand_sources_checked"],
                "citation_priority": paper["citation_priority"],
                "followup_reasons": ";".join(reasons),
                "priority_score": priority_score,
            }
        )

    rows.sort(
        key=lambda row: (
            -int(row["priority_score"]),
            row["primary_module_for_filing"],
            row["paper_id"],
        )
    )
    return rows


def build_representative_pool(papers: List[Dict[str, object]]) -> List[Dict[str, object]]:
    by_module: Dict[str, List[Dict[str, object]]] = {}
    for paper in papers:
        if not paper["active_confirmed_core"]:
            continue
        modules = paper.get("scientific_object_modules", [])
        if not isinstance(modules, list):
            continue

        for module_code in modules:
            score = 0
            reasons: List[str] = []
            score += citation_priority_score(str(paper["citation_priority"]))
            if score:
                reasons.append(f"citation={paper['citation_priority']}")
            evidence_bonus = evidence_status_score(str(paper["evidence_status"]))
            score += evidence_bonus
            if evidence_bonus:
                reasons.append(f"evidence={paper['evidence_status']}")
            if paper["pdf_exists"]:
                score += 8
                reasons.append("local_pdf")
            if paper["note_exists"]:
                score += 6
                reasons.append("local_note")
            if paper["source_limited"] == "no":
                score += 6
                reasons.append("not_source_limited")
            if paper["primary_module_for_filing"] == module_code:
                score += 4
                reasons.append("primary_filing_match")
            if paper["object_coverage_mode"] == "single_module":
                score += 2
                reasons.append("single_module_anchor")

            by_module.setdefault(str(module_code), []).append(
                {
                    "module_code": str(module_code),
                    "paper_id": paper["paper_id"],
                    "title": paper["title"],
                    "year": paper["year"],
                    "source": paper["source"],
                    "citation_priority": paper["citation_priority"],
                    "evidence_status": paper["evidence_status"],
                    "pdf_exists": "yes" if paper["pdf_exists"] else "no",
                    "note_exists": "yes" if paper["note_exists"] else "no",
                    "source_limited": paper["source_limited"],
                    "object_coverage_mode": paper["object_coverage_mode"],
                    "primary_module_for_filing": paper["primary_module_for_filing"],
                    "representative_score": score,
                    "score_reasons": ";".join(reasons),
                }
            )

    rows: List[Dict[str, object]] = []
    for module_code, candidates in sorted(by_module.items()):
        candidates.sort(
            key=lambda row: (
                -int(row["representative_score"]),
                row["source_limited"],
                row["paper_id"],
            )
        )
        for rank, row in enumerate(candidates[:5], start=1):
            row["module_rank"] = rank
            rows.append(row)
    return rows


def build_module_coverage_pool(sqlite_conn: sqlite3.Connection) -> List[Dict[str, object]]:
    rows = sqlite_conn.execute(
        """
        SELECT
            c.module_code,
            t.label,
            c.active_assignment_count,
            c.active_local_pdf_count,
            c.active_missing_local_pdf_count,
            c.active_local_pdf_coverage_rate,
            c.active_note_count,
            c.active_missing_note_count,
            c.active_source_limited_count
        FROM canonical_formal_module_pdf_coverage_summary c
        JOIN taxonomy_index t ON t.code = c.module_code
        ORDER BY c.active_missing_local_pdf_count DESC, c.active_assignment_count DESC, c.module_code
        """
    ).fetchall()
    return [dict(row) for row in rows]


def build_boundary_case_pool(sqlite_conn: sqlite3.Connection) -> List[Dict[str, object]]:
    rows = sqlite_conn.execute(
        """
        SELECT
            paper_id,
            title,
            drift_class,
            boundary_case_kind,
            scientific_modules_canonical,
            normalized_general_method_bucket,
            final_assignments_canonical,
            active_confirmed_core
        FROM classification_boundary_analysis
        WHERE active_confirmed_core = 1
          AND drift_class <> 'aligned'
        ORDER BY
            CASE drift_class
                WHEN 'semantic_drift' THEN 1
                WHEN 'order_drift' THEN 2
                WHEN 'acceptable_mirror' THEN 3
                ELSE 9
            END,
            paper_id
        """
    ).fetchall()
    return [dict(row) for row in rows]


def write_summary(
    note_rows: List[Dict[str, object]],
    followup_rows: List[Dict[str, object]],
    representative_rows: List[Dict[str, object]],
    module_rows: List[Dict[str, object]],
    boundary_rows: List[Dict[str, object]],
) -> None:
    summary = f"""# ASD Phase 6 preparation queues and pools

Date: {RUN_DATE}

This file records the first machine-generated Phase 6 preparation outputs derived from the current canonical structured layer. These are candidate coordination assets, not direct writeback authority.

## Generated outputs

- `{NOTE_QUEUE_PATH.relative_to(ROOT)}`
- `{FOLLOWUP_QUEUE_PATH.relative_to(ROOT)}`
- `{REPRESENTATIVE_POOL_PATH.relative_to(ROOT)}`
- `{MODULE_COVERAGE_POOL_PATH.relative_to(ROOT)}`
- `{BOUNDARY_POOL_PATH.relative_to(ROOT)}`

## Current counts

- note revision queue candidates: `{len(note_rows)}`
- full-text follow-up queue candidates: `{len(followup_rows)}`
- representative paper pool rows: `{len(representative_rows)}`
- module coverage pool rows: `{len(module_rows)}`
- boundary case pool rows: `{len(boundary_rows)}`

## Queue semantics

### note revision queue

Heuristic candidate queue for records whose Notes are most likely to need wording refresh before future writeback. Current triggers are:

- `multi_module`
- independent `01.04` bucket
- `updated_source_limited`
- `source_limited=yes`

This queue does not prove a Note is wrong. It is a prioritization aid.

### full-text follow-up queue

Canonical follow-up queue for active confirmed-core records with one or more of:

- no local PDF
- `source_limited=yes`
- non-full-text evidence status

### representative paper pool

Per-module top-5 candidate papers for writing support. Ranking is heuristic and combines:

- citation priority
- evidence status
- local PDF
- local Note
- source-limited status
- primary filing match

### module coverage pool

Per-formal-module canonical coverage summary for staffing and writing readiness.

### boundary case pool

Current canonical-vs-mirror boundary pool. With drift currently cleared, this pool mostly functions as an `acceptable_mirror` watchlist rather than an active drift backlog.

## Important constraint

These outputs are planning aids for future parallel work. They do not authorize direct edits to:

- `Paper_Lists/agent_master_paper_list.md`
- `Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`
- `Data/`

Any future writeback still has to follow the single-writer and `export -> check -> build` discipline.
"""
    SUMMARY_PATH.write_text(summary, encoding="utf-8")


def main() -> None:
    papers = load_jsonl(PAPERS_JSONL)
    active_count = sum(1 for paper in papers if paper["active_confirmed_core"])
    if active_count != ACTIVE_BASELINE:
        raise SystemExit(
            f"Expected {ACTIVE_BASELINE} active confirmed-core papers, found {active_count}"
        )

    sqlite_conn = sqlite3.connect(SQLITE_PATH)
    sqlite_conn.row_factory = sqlite3.Row
    try:
        note_rows = build_note_revision_queue(papers)
        followup_rows = build_full_text_followup_queue(papers)
        representative_rows = build_representative_pool(papers)
        module_rows = build_module_coverage_pool(sqlite_conn)
        boundary_rows = build_boundary_case_pool(sqlite_conn)
    finally:
        sqlite_conn.close()

    write_tsv(
        NOTE_QUEUE_PATH,
        [
            "paper_id",
            "title",
            "note_path",
            "primary_module_for_filing",
            "classification_anchor",
            "object_coverage_mode",
            "general_method_bucket",
            "note_status",
            "source_limited",
            "pdf_exists",
            "citation_priority",
            "queue_reasons",
            "priority_score",
        ],
        note_rows,
    )
    write_tsv(
        FOLLOWUP_QUEUE_PATH,
        [
            "paper_id",
            "title",
            "primary_module_for_filing",
            "classification_anchor",
            "pdf_status",
            "evidence_status",
            "pdf_exists",
            "source_limited",
            "first_hand_sources_checked",
            "citation_priority",
            "followup_reasons",
            "priority_score",
        ],
        followup_rows,
    )
    write_tsv(
        REPRESENTATIVE_POOL_PATH,
        [
            "module_code",
            "module_rank",
            "paper_id",
            "title",
            "year",
            "source",
            "citation_priority",
            "evidence_status",
            "pdf_exists",
            "note_exists",
            "source_limited",
            "object_coverage_mode",
            "primary_module_for_filing",
            "representative_score",
            "score_reasons",
        ],
        representative_rows,
    )
    write_tsv(
        MODULE_COVERAGE_POOL_PATH,
        [
            "module_code",
            "label",
            "active_assignment_count",
            "active_local_pdf_count",
            "active_missing_local_pdf_count",
            "active_local_pdf_coverage_rate",
            "active_note_count",
            "active_missing_note_count",
            "active_source_limited_count",
        ],
        module_rows,
    )
    write_tsv(
        BOUNDARY_POOL_PATH,
        [
            "paper_id",
            "title",
            "drift_class",
            "boundary_case_kind",
            "scientific_modules_canonical",
            "normalized_general_method_bucket",
            "final_assignments_canonical",
            "active_confirmed_core",
        ],
        boundary_rows,
    )
    write_summary(
        note_rows=note_rows,
        followup_rows=followup_rows,
        representative_rows=representative_rows,
        module_rows=module_rows,
        boundary_rows=boundary_rows,
    )

    print(f"Wrote {NOTE_QUEUE_PATH}")
    print(f"Wrote {FOLLOWUP_QUEUE_PATH}")
    print(f"Wrote {REPRESENTATIVE_POOL_PATH}")
    print(f"Wrote {MODULE_COVERAGE_POOL_PATH}")
    print(f"Wrote {BOUNDARY_POOL_PATH}")
    print(f"Wrote {SUMMARY_PATH}")
    print(f"note revision queue rows: {len(note_rows)}")
    print(f"full-text follow-up queue rows: {len(followup_rows)}")
    print(f"representative paper pool rows: {len(representative_rows)}")
    print(f"module coverage pool rows: {len(module_rows)}")
    print(f"boundary case pool rows: {len(boundary_rows)}")


if __name__ == "__main__":
    main()
