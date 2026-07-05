from __future__ import annotations

import csv
import json
import re
import sqlite3
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "Data"
COVERAGE_DIR = ROOT / "Coverage_Check"
PAPERS_JSONL = DATA_DIR / "papers.jsonl"
DISCIPLINE_ASSIGNMENTS_JSONL = DATA_DIR / "discipline_code_assignments.jsonl"
DISCIPLINE_REGISTRY_JSONL = DATA_DIR / "discipline_local_code_registry.jsonl"
DISCIPLINE_REGISTRY_CSV = DATA_DIR / "discipline_local_code_registry.csv"
CLASSIFICATION_CODE_INDEX = DATA_DIR / "classification_code_index.json"
PREVIEW_CSV = DATA_DIR / "discipline_code_initial_assignment_preview.csv"
FIELD_OWNERSHIP_MATRIX = DATA_DIR / "field_ownership_matrix.md"
CHECK_POLICY = DATA_DIR / "check_policy.md"
DISCIPLINE_SCHEMA = DATA_DIR / "schema" / "discipline_code_assignments.schema.json"
CLASSIFICATION_SCHEMA = DATA_DIR / "schema" / "classification_code_index.schema.json"
README = DATA_DIR / "README.md"
INTEGRITY_REPORT = DATA_DIR / "integrity_check_report.md"
SQLITE_PATH = DATA_DIR / "papers.sqlite"
PIPELINE_SCRIPT = ROOT / "scripts" / "run_structured_data_pipeline.py"
MASTER_OWNER = ROOT / "Paper_Lists" / "agent_master_paper_list.md"
PROGRESS_OWNER = ROOT / "Coverage_Check" / "multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md"
PLAN_PATH = COVERAGE_DIR / "structured_data_long_term_catalog_and_index_plan_2026-07-05.md"
OUTPUT_PATH = COVERAGE_DIR / "structured_data_execution_definition_audit_latest.md"

PAPER_ID_PATTERN = re.compile(r"ASD-\d{4}")
ALLOWED_ASSIGNMENT_STATUSES = {
    "active_code",
    "retired_code",
    "redirected_code",
    "pending_secondary",
    "non_discipline_general_method",
}


def load_jsonl(path: Path) -> list[dict[str, object]]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def check(condition: bool, success: str, failure: str) -> tuple[str, str]:
    return ("PASS", success) if condition else ("FAIL", failure)


def add_result(results: list[dict[str, str]], item: str, status: str, detail: str, evidence: str) -> None:
    results.append(
        {
            "item": item,
            "status": status,
            "detail": detail,
            "evidence": evidence,
        }
    )


def count_sqlite_table(conn: sqlite3.Connection, table: str) -> int:
    return int(conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0])


def main() -> None:
    papers = load_jsonl(PAPERS_JSONL)
    assignments = load_jsonl(DISCIPLINE_ASSIGNMENTS_JSONL)
    registry = load_jsonl(DISCIPLINE_REGISTRY_JSONL)
    preview_rows = load_csv_rows(PREVIEW_CSV)
    classification_index = load_json(CLASSIFICATION_CODE_INDEX)
    readme_text = read_text(README)
    integrity_report_text = read_text(INTEGRITY_REPORT)
    active_papers = [row for row in papers if bool(row.get("active_confirmed_core"))]

    with sqlite3.connect(SQLITE_PATH) as conn:
        sqlite_registry_count = count_sqlite_table(conn, "discipline_local_code_registry")
        metadata_rows = conn.execute(
            "SELECT key, value FROM metadata WHERE key IN ("
            "'papers_exported_at',"
            "'discipline_local_code_registry_generated_at',"
            "'discipline_local_code_registry_generated_by',"
            "'discipline_local_code_registry_source_commit',"
            "'discipline_local_code_registry_worktree_dirty',"
            "'discipline_local_code_registry_row_count'"
            ") ORDER BY key"
        ).fetchall()

    metadata = {row[0]: row[1] for row in metadata_rows}
    current_snapshot_rows = [
        row
        for row in assignments
        if row.get("assignment_status") in {"active_code", "pending_secondary", "non_discipline_general_method"}
    ]

    results: list[dict[str, str]] = []

    paper_ids = [str(row.get("paper_id", "")) for row in papers]
    unique_paper_ids = set(paper_ids)
    status, detail = check(
        len(paper_ids) == len(unique_paper_ids) and all(PAPER_ID_PATTERN.fullmatch(pid) for pid in paper_ids),
        f"All {len(paper_ids)} papers use unique ASD-xxxx paper_id values.",
        "papers.jsonl contains duplicate or malformed ASD paper IDs.",
    )
    add_result(results, "1", status, detail, "Data/papers.jsonl")

    structured_fields_ok = all(
        isinstance(row.get("scientific_object_modules"), list)
        and isinstance(row.get("general_method_bucket"), str)
        and isinstance(row.get("object_coverage_mode"), str)
        and isinstance(row.get("primary_module_for_filing"), str)
        for row in papers
    )
    status, detail = check(
        structured_fields_ok,
        f"All {len(papers)} papers carry structured classification fields.",
        "Some papers are missing structured classification fields.",
    )
    add_result(results, "2", status, detail, "Data/papers.jsonl")

    evidence_fields_ok = all(
        isinstance(row.get("pdf_status"), str)
        and isinstance(row.get("evidence_status"), str)
        and isinstance(row.get("source_limited"), str)
        for row in papers
    )
    status, detail = check(
        evidence_fields_ok,
        f"All {len(papers)} papers carry structured evidence-status fields.",
        "Some papers are missing structured evidence-status fields.",
    )
    add_result(results, "3", status, detail, "Data/papers.jsonl")

    index_ok = (
        CLASSIFICATION_CODE_INDEX.exists()
        and "primary_code_to_label" in classification_index
        and "secondary_terms" in classification_index
    )
    status, detail = check(
        index_ok,
        "classification_code_index.json exists and exposes taxonomy-owner structures.",
        "classification_code_index.json is missing or lacks required taxonomy-owner structures.",
    )
    add_result(results, "4", status, detail, "Data/classification_code_index.json")

    active_ids = {str(row["paper_id"]) for row in active_papers}
    current_snapshot_ids = {str(row["paper_id"]) for row in current_snapshot_rows}
    assignment_statuses_ok = all(str(row.get("assignment_status")) in ALLOWED_ASSIGNMENT_STATUSES for row in assignments)
    status, detail = check(
        current_snapshot_ids == active_ids and assignment_statuses_ok,
        f"discipline_code_assignments current snapshot covers all {len(active_ids)} active papers with allowed statuses.",
        "discipline_code_assignments current snapshot does not cover active papers correctly or contains invalid statuses.",
    )
    add_result(results, "5", status, detail, "Data/discipline_code_assignments.jsonl")

    status, detail = check(
        DISCIPLINE_ASSIGNMENTS_JSONL.exists() and assignment_statuses_ok,
        "Stable discipline code assignment ledger exists and uses auditable assignment statuses.",
        "Stable discipline code assignment ledger is missing or contains invalid statuses.",
    )
    add_result(results, "6", status, detail, "Data/discipline_code_assignments.jsonl")

    status, detail = check(
        CLASSIFICATION_CODE_INDEX.exists(),
        "classification_code_index.json is present as taxonomy vocabulary owner.",
        "classification_code_index.json is missing.",
    )
    add_result(results, "7", status, detail, "Data/classification_code_index.json")

    preview_ok = PREVIEW_CSV.exists() and len(preview_rows) == len(active_papers)
    status, detail = check(
        preview_ok,
        f"discipline_code_initial_assignment_preview.csv exists and matches the {len(active_papers)} active-paper review surface.",
        "discipline_code_initial_assignment_preview.csv is missing or does not match active-paper coverage.",
    )
    add_result(results, "8", status, detail, "Data/discipline_code_initial_assignment_preview.csv")

    registry_metadata_ok = (
        DISCIPLINE_REGISTRY_JSONL.exists()
        and DISCIPLINE_REGISTRY_CSV.exists()
        and SQLITE_PATH.exists()
        and len(registry) == len(active_papers)
        and sqlite_registry_count == len(registry)
        and metadata.get("discipline_local_code_registry_row_count") == str(len(registry))
        and metadata.get("discipline_local_code_registry_generated_at") == metadata.get("papers_exported_at")
        and metadata.get("discipline_local_code_registry_generated_by") == "export_structured_data.py"
    )
    status, detail = check(
        registry_metadata_ok,
        "discipline_local_code_registry is present in JSONL / CSV / SQLite with aligned derived snapshot metadata.",
        "discipline_local_code_registry surfaces or snapshot metadata are missing or inconsistent.",
    )
    add_result(results, "9", status, detail, "Data/discipline_local_code_registry.jsonl + Data/discipline_local_code_registry.csv + Data/papers.sqlite")

    governance_refs_ok = all(
        token in readme_text
        for token in (
            "field_ownership_matrix.md",
            "check_policy.md",
            "schema/discipline_code_assignments.schema.json",
            "schema/classification_code_index.schema.json",
        )
    )
    status, detail = check(
        governance_refs_ok,
        "README explicitly references the frozen ownership matrix, check policy, and both schema contracts.",
        "README does not yet explicitly reference all frozen governance contracts.",
    )
    add_result(results, "10", status, detail, "Data/README.md")

    report_ok = all(section in integrity_report_text for section in ("## ERROR", "## WARNING", "## INFO"))
    status, detail = check(
        report_ok,
        "Consistency checking currently emits ERROR / WARNING / INFO report sections.",
        "integrity_check_report.md is missing one or more ERROR / WARNING / INFO sections.",
    )
    add_result(results, "11", status, detail, "Data/integrity_check_report.md")

    workflow_ok = PIPELINE_SCRIPT.exists() and "owner fact source" in readme_text and "Workflow order" in readme_text
    status, detail = check(
        workflow_ok,
        "The owner fact source -> export -> check -> build workflow is documented and exposed via a canonical pipeline script.",
        "The owner fact source -> export -> check -> build workflow is not yet fully documented and exposed as a canonical pipeline.",
    )
    add_result(results, "12", status, detail, "scripts/run_structured_data_pipeline.py + Data/README.md")

    pass_count = sum(1 for row in results if row["status"] == "PASS")
    fail_count = sum(1 for row in results if row["status"] == "FAIL")

    lines = [
        "# Structured Data Execution Definition Audit",
        "",
        f"Plan: `{PLAN_PATH.relative_to(ROOT)}`",
        "",
        "## Summary",
        "",
        f"- `PASS`: {pass_count}",
        f"- `FAIL`: {fail_count}",
        "",
        "## Items",
        "",
    ]
    for row in results:
        lines.extend(
            [
                f"### Item {row['item']} - {row['status']}",
                "",
                row["detail"],
                "",
                f"Evidence: `{row['evidence']}`",
                "",
            ]
        )

    OUTPUT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUTPUT_PATH}")
    print(f"pass={pass_count} fail={fail_count}")


if __name__ == "__main__":
    main()
