#!/usr/bin/env python3
"""Triage Codex classification differences into an auditable review queue.

This report is deliberately read-only. It separates stale/invalid legacy codes,
taxonomy gaps, source-limited records, model uncertainty, and semantic conflicts
so a reviewer does not mistake duplicate baseline comparisons for independent
classification errors.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
DATA_DIR = PROJECT_ROOT / "Data"
DEFAULT_RUN_DIR = PROJECT_ROOT / "Coverage_Check" / "codex_classification_audit_gpt-6.1-sol_2026-10-27"


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def code_status(code: str, secondary: dict[str, dict[str, Any]], tertiary: dict[str, dict[str, Any]]) -> str:
    if not code or code in {"null", "absent"}:
        return "none"
    table = tertiary if code.count(".") == 2 else secondary
    return str(table.get(code, {}).get("status") or "missing")


def taxonomy_gap(row: dict[str, str]) -> bool:
    reason = (row.get("reason") or "").lower()
    return any(
        marker in reason
        for marker in (
            "no active",
            "no applicable",
            "taxonomy gap",
            "cannot be assigned more deeply",
            "no listed tertiary",
            "active codebook",
        )
    ) or (row.get("audit") in {"", "null", "absent"} and row.get("difference_type") in {"secondary_code_mismatch", "tertiary_code_mismatch"})


def classify_row(
    row: dict[str, str],
    assessment: dict[str, Any],
    secondary: dict[str, dict[str, Any]],
    tertiary: dict[str, dict[str, Any]],
) -> tuple[str, str]:
    source_type = row.get("source_type") or "unknown"
    if source_type != "pdf_full_text":
        return "source_limited_manual_review", "The audit did not use a complete extracted PDF."
    if assessment.get("needs_human_review"):
        return "model_uncertainty_manual_review", "The audit assessment itself requests human review."
    current_status = code_status(row.get("current", ""), secondary, tertiary)
    if current_status in {"needs_review", "missing"}:
        return "legacy_code_cleanup_review", f"Current comparison code has status {current_status}; resolve the owner record before treating it as a semantic conflict."
    if row.get("difference_type") in {"secondary_code_mismatch", "tertiary_code_mismatch"} and taxonomy_gap(row):
        return "taxonomy_gap_manual_review", "The audit or current taxonomy does not provide a directly comparable active code."
    if row.get("difference_type") in {"module_added_by_audit", "module_missing_in_audit", "general_method_bucket_mismatch"}:
        return "module_boundary_manual_review", "The audit and current record disagree about the supported scientific object or general-method bucket."
    return "semantic_code_manual_review", "Both sides have comparable active codes; inspect the quoted object/result evidence and PDF locator."


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", type=Path, default=DEFAULT_RUN_DIR)
    args = parser.parse_args()
    run_dir = args.run_dir if args.run_dir.is_absolute() else PROJECT_ROOT / args.run_dir
    diff_path = run_dir / "classification_differences.csv"
    if not diff_path.is_file():
        parser.error(f"missing comparison report: {diff_path}")

    index = json.loads((DATA_DIR / "classification_code_index.json").read_text(encoding="utf-8"))
    secondary = {row["secondary_code"]: row for row in index["secondary_terms"]}
    tertiary = {row["tertiary_code"]: row for row in index["tertiary_terms"]}
    assessments: dict[str, dict[str, Any]] = {}
    for result_path in (run_dir / "results").glob("ASD-*.json"):
        try:
            saved = json.loads(result_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        assessments[str(saved.get("paper_id"))] = saved.get("assessment") or {}

    with diff_path.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))

    seen: dict[tuple[str, str, str, str, str, str], int] = defaultdict(int)
    triaged: list[dict[str, Any]] = []
    for row in rows:
        key = (
            row.get("paper_id", ""),
            row.get("difference_type", ""),
            row.get("module", ""),
            row.get("current", ""),
            row.get("audit", ""),
            row.get("source_type", ""),
        )
        seen[key] += 1
        assessment = assessments.get(row.get("paper_id", ""), {})
        status, rationale = classify_row(row, assessment, secondary, tertiary)
        evidence = row.get("evidence") or "[]"
        try:
            evidence_rows = json.loads(evidence)
        except json.JSONDecodeError:
            evidence_rows = []
        triaged.append(
            {
                **row,
                "triage_status": status,
                "triage_rationale": rationale,
                "audit_needs_human_review": str(bool(assessment.get("needs_human_review"))).lower(),
                "evidence_row_count": len(evidence_rows) if isinstance(evidence_rows, list) else 0,
                "duplicate_comparison_row": "false",
                "review_status": "not_started",
                "human_decision": "",
                "reviewer_notes": "",
            }
        )

    for row in triaged:
        key = (
            row.get("paper_id", ""),
            row.get("difference_type", ""),
            row.get("module", ""),
            row.get("current", ""),
            row.get("audit", ""),
            row.get("source_type", ""),
        )
        if seen[key] > 1:
            row["duplicate_comparison_row"] = "true"

    fields = list(triaged[0]) if triaged else [
        "paper_id", "title", "difference_type", "module", "current", "audit", "reason", "evidence", "source_type",
        "triage_status", "triage_rationale", "audit_needs_human_review", "evidence_row_count",
        "duplicate_comparison_row", "review_status", "human_decision", "reviewer_notes",
    ]
    output_path = run_dir / "manual_review_triage.csv"
    with output_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(triaged)

    by_paper: dict[str, set[str]] = defaultdict(set)
    for row in triaged:
        by_paper[row["paper_id"]].add(row["triage_status"])
    summary = {
        "run_dir": str(run_dir),
        "model": "gpt-6.1-sol",
        "difference_rows": len(triaged),
        "difference_papers": len(by_paper),
        "triage_status_counts": dict(Counter(row["triage_status"] for row in triaged)),
        "duplicate_comparison_rows": sum(row["duplicate_comparison_row"] == "true" for row in triaged),
        "papers_by_triage_status_count": {
            " + ".join(sorted(statuses)): count
            for statuses, count in Counter(tuple(sorted(statuses)) for statuses in by_paper.values()).items()
        },
        "writeback_performed": False,
        "report": output_path.name,
    }
    (run_dir / "manual_review_triage_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
