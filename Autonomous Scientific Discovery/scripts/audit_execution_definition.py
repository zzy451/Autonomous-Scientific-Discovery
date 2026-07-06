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
PDF_ARCHIVE_REGISTRY_JSONL = DATA_DIR / "registry" / "pdf_archive_registry.jsonl"
CLASSIFICATION_ASSIGNMENTS_JSONL = DATA_DIR / "registry" / "classification_assignments.jsonl"
CLASSIFICATION_CODE_INDEX = DATA_DIR / "classification_code_index.json"
PREVIEW_CSV = DATA_DIR / "discipline_code_initial_assignment_preview.csv"
FIELD_OWNERSHIP_MATRIX = DATA_DIR / "field_ownership_matrix.md"
DISCIPLINE_CODE_ASSIGNMENT_POLICY = DATA_DIR / "discipline_code_assignment_policy.md"
PRIMARY_FILING_POLICY = DATA_DIR / "primary_filing_policy.md"
CHECK_POLICY = DATA_DIR / "check_policy.md"
DISCIPLINE_SCHEMA = DATA_DIR / "schema" / "discipline_code_assignments.schema.json"
CLASSIFICATION_SCHEMA = DATA_DIR / "schema" / "classification_code_index.schema.json"
README = DATA_DIR / "README.md"
FIELD_DICTIONARY = DATA_DIR / "field_dictionary.md"
INTEGRITY_REPORT = DATA_DIR / "integrity_check_report.md"
SQLITE_PATH = DATA_DIR / "papers.sqlite"
CHANGE_LOG_JSONL = DATA_DIR / "change_log.jsonl"
PIPELINE_SCRIPT = ROOT / "scripts" / "run_structured_data_pipeline.py"
QUERY_SCRIPT = ROOT / "scripts" / "query_analysis_db.py"
EXPORT_SCRIPT = ROOT / "scripts" / "export_structured_data.py"
BUILD_SCRIPT = ROOT / "scripts" / "build_analysis_db.py"
APPEND_CHANGE_LOG_SCRIPT = ROOT / "scripts" / "append_change_log.py"
MANAGE_DISCIPLINE_CODE_ASSIGNMENTS_SCRIPT = ROOT / "scripts" / "manage_discipline_code_assignments.py"
MANAGE_CLASSIFICATION_CODE_INDEX_SCRIPT = ROOT / "scripts" / "manage_classification_code_index.py"
MANAGE_PROGRESS_TRACKING_SCRIPT = ROOT / "scripts" / "manage_progress_tracking.py"
MANAGE_MASTER_PAPER_LIST_SCRIPT = ROOT / "scripts" / "manage_master_paper_list.py"
MASTER_OWNER = ROOT / "Paper_Lists" / "agent_master_paper_list.md"
PROGRESS_OWNER = ROOT / "Coverage_Check" / "multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md"
PLAN_PATH = COVERAGE_DIR / "structured_data_long_term_catalog_and_index_plan_2026-07-05.md"
OUTPUT_PATH = COVERAGE_DIR / "structured_data_execution_definition_audit_latest.md"

PAPER_ID_PATTERN = re.compile(r"ASD-\d{4}")
ASSIGNMENT_ID_PATTERN = re.compile(r"DCA-\d{6}")
DATE_PATTERN = re.compile(r"20\d{2}-\d{2}-\d{2}")
DISCIPLINE_LOCAL_CODE_PATTERN = re.compile(r"^(0[1-9]|1[0-1])-(\d{2})-(\d{3})$")
SECONDARY_CODE_PATTERN = re.compile(r"^(0[1-9]|1[0-1])\.(\d{2})$")
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
    pdf_archive_registry = load_jsonl(PDF_ARCHIVE_REGISTRY_JSONL)
    classification_assignments = load_jsonl(CLASSIFICATION_ASSIGNMENTS_JSONL)
    preview_rows = load_csv_rows(PREVIEW_CSV)
    classification_index = load_json(CLASSIFICATION_CODE_INDEX)
    change_log_rows = load_jsonl(CHANGE_LOG_JSONL) if CHANGE_LOG_JSONL.exists() else []
    readme_text = read_text(README)
    field_dictionary_text = read_text(FIELD_DICTIONARY)
    integrity_report_text = read_text(INTEGRITY_REPORT)
    pipeline_script_text = read_text(PIPELINE_SCRIPT)
    query_script_text = read_text(QUERY_SCRIPT)
    export_script_text = read_text(EXPORT_SCRIPT)
    build_script_text = read_text(BUILD_SCRIPT)
    append_change_log_script_text = read_text(APPEND_CHANGE_LOG_SCRIPT)
    manage_discipline_code_assignments_script_text = read_text(MANAGE_DISCIPLINE_CODE_ASSIGNMENTS_SCRIPT)
    manage_classification_code_index_script_text = read_text(MANAGE_CLASSIFICATION_CODE_INDEX_SCRIPT)
    manage_progress_tracking_script_text = read_text(MANAGE_PROGRESS_TRACKING_SCRIPT)
    manage_master_paper_list_script_text = read_text(MANAGE_MASTER_PAPER_LIST_SCRIPT)
    active_papers = [row for row in papers if bool(row.get("active_confirmed_core"))]

    with sqlite3.connect(SQLITE_PATH) as conn:
        sqlite_papers_count = count_sqlite_table(conn, "papers")
        sqlite_registry_count = count_sqlite_table(conn, "discipline_local_code_registry")
        sqlite_pdf_evidence_count = count_sqlite_table(conn, "pdf_evidence_status")
        sqlite_paper_modules_count = count_sqlite_table(conn, "paper_modules")
        sqlite_general_method_buckets_count = count_sqlite_table(conn, "paper_general_method_buckets")
        sqlite_classification_terms_count = count_sqlite_table(conn, "classification_terms")
        sqlite_change_log_count = count_sqlite_table(conn, "change_log")
        sqlite_table_names = {
            str(row[0])
            for row in conn.execute(
                "SELECT name FROM sqlite_master WHERE type = 'table'"
            ).fetchall()
        }
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
    current_snapshot_by_paper_id = {
        str(row.get("paper_id")): row for row in current_snapshot_rows
    }

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
    formal_assignment_expected = sum(len(row.get("scientific_object_modules", [])) for row in papers)
    general_bucket_expected = sum(1 for row in papers if row.get("general_method_bucket") != "none")
    classification_assignment_rows_ok = all(
        isinstance(row.get("paper_id"), str)
        and isinstance(row.get("taxonomy_code"), str)
        and isinstance(row.get("assignment_kind"), str)
        for row in classification_assignments
    )
    status, detail = check(
        structured_fields_ok
        and classification_assignment_rows_ok
        and len(classification_assignments) == formal_assignment_expected + general_bucket_expected
        and sqlite_paper_modules_count == formal_assignment_expected
        and sqlite_general_method_buckets_count == general_bucket_expected,
        (
            f"All {len(papers)} papers carry structured classification fields, "
            f"with {len(classification_assignments)} classification assignment rows "
            f"aligned to SQLite paper_modules={sqlite_paper_modules_count} and "
            f"paper_general_method_buckets={sqlite_general_method_buckets_count}."
        ),
        "Structured classification surfaces are missing fields or drift across papers.jsonl / classification_assignments / SQLite module tables.",
    )
    add_result(results, "2", status, detail, "Data/papers.jsonl + Data/registry/classification_assignments.jsonl + Data/papers.sqlite")

    evidence_fields_ok = all(
        isinstance(row.get("pdf_status"), str)
        and isinstance(row.get("evidence_status"), str)
        and isinstance(row.get("source_limited"), str)
        for row in papers
    )
    pdf_registry_fields_ok = all(
        isinstance(row.get("pdf_evidence_type"), str)
        and isinstance(row.get("pdf_check_status"), str)
        and isinstance(row.get("source_limited"), str)
        for row in pdf_archive_registry
    )
    status, detail = check(
        evidence_fields_ok
        and len(pdf_archive_registry) == len(papers)
        and sqlite_pdf_evidence_count == len(pdf_archive_registry)
        and pdf_registry_fields_ok,
        (
            f"All {len(papers)} papers carry structured evidence-status fields, "
            f"with {len(pdf_archive_registry)} pdf_archive_registry rows mirrored into SQLite pdf_evidence_status."
        ),
        "Structured evidence-status surfaces are missing fields or drift across papers.jsonl / pdf_archive_registry / SQLite pdf_evidence_status.",
    )
    add_result(results, "3", status, detail, "Data/papers.jsonl + Data/registry/pdf_archive_registry.jsonl + Data/papers.sqlite")

    primary_terms = classification_index.get("primary_terms", [])
    secondary_terms = classification_index.get("secondary_terms", [])
    primary_term_fields_ok = all(
        isinstance(row, dict)
        and all(
            key in row
            for key in ("primary_code", "label", "definition", "include", "exclude", "status", "source")
        )
        for row in primary_terms
    )
    secondary_term_fields_ok = all(
        isinstance(row, dict)
        and all(
            key in row
            for key in (
                "secondary_code",
                "parent_primary_code",
                "label",
                "definition",
                "include",
                "exclude",
                "status",
                "source",
                "review_status",
            )
        )
        for row in secondary_terms
    )
    index_ok = (
        CLASSIFICATION_CODE_INDEX.exists()
        and "primary_code_to_label" in classification_index
        and "secondary_code_to_label" in classification_index
        and isinstance(primary_terms, list)
        and isinstance(secondary_terms, list)
        and bool(primary_terms)
        and bool(secondary_terms)
        and primary_term_fields_ok
        and secondary_term_fields_ok
    )
    status, detail = check(
        index_ok,
        (
            "classification_code_index.json exists and exposes non-empty taxonomy-owner "
            "primary/secondary term structures with definition/include/exclude/status/source fields."
        ),
        "classification_code_index.json is missing or lacks required non-empty taxonomy-owner term structures.",
    )
    add_result(results, "4", status, detail, "Data/classification_code_index.json")

    active_papers_by_id = {str(row["paper_id"]): row for row in active_papers}
    active_ids = set(active_papers_by_id)
    current_snapshot_ids = {str(row["paper_id"]) for row in current_snapshot_rows}
    assignment_statuses_ok = all(str(row.get("assignment_status")) in ALLOWED_ASSIGNMENT_STATUSES for row in assignments)
    current_assignment_counts: dict[str, int] = {}
    current_snapshot_unique_papers_ok = True
    current_snapshot_semantics_ok = True
    for row in current_snapshot_rows:
        paper_id = str(row.get("paper_id", "")).strip()
        status_name = str(row.get("assignment_status", "")).strip()
        current_assignment_counts[status_name] = current_assignment_counts.get(status_name, 0) + 1
        discipline_local_code = row.get("discipline_local_code")
        primary_taxonomy_code_2lvl = row.get("primary_taxonomy_code_2lvl")
        pending_reason = row.get("pending_reason")
        source_primary_module = row.get("source_primary_module_for_filing")
        paper = active_papers_by_id.get(paper_id)
        if paper is None:
            current_snapshot_unique_papers_ok = False
            continue
        modules = paper.get("scientific_object_modules", [])
        general_method_bucket = str(paper.get("general_method_bucket", ""))
        if status_name == "active_code":
            code_match = DISCIPLINE_LOCAL_CODE_PATTERN.fullmatch(str(discipline_local_code or "").strip())
            secondary_match = SECONDARY_CODE_PATTERN.fullmatch(str(primary_taxonomy_code_2lvl or "").strip())
            current_snapshot_semantics_ok = current_snapshot_semantics_ok and (
                code_match is not None
                and secondary_match is not None
                and code_match.group(1) == secondary_match.group(1)
                and code_match.group(2) == secondary_match.group(2)
                and str(source_primary_module or "").strip() == code_match.group(1)
                and pending_reason in (None, "")
            )
        elif status_name == "pending_secondary":
            current_snapshot_semantics_ok = current_snapshot_semantics_ok and (
                not discipline_local_code
                and not primary_taxonomy_code_2lvl
                and str(pending_reason or "").strip() in {
                    "missing_primary_module_for_filing",
                    "missing_or_uncertain_secondary_class",
                    "secondary_primary_mismatch",
                }
            )
        elif status_name == "non_discipline_general_method":
            current_snapshot_semantics_ok = current_snapshot_semantics_ok and (
                not discipline_local_code
                and not primary_taxonomy_code_2lvl
                and pending_reason in (None, "")
                and general_method_bucket != "none"
                and not modules
            )
    status, detail = check(
        current_snapshot_ids == active_ids
        and assignment_statuses_ok
        and current_snapshot_unique_papers_ok
        and current_snapshot_semantics_ok,
        (
            "discipline_code_assignments current snapshot covers all "
            f"{len(active_ids)} active papers with valid current-status semantics "
            f"(active={current_assignment_counts.get('active_code', 0)}, "
            f"pending={current_assignment_counts.get('pending_secondary', 0)}, "
            f"general_method={current_assignment_counts.get('non_discipline_general_method', 0)})."
        ),
        "discipline_code_assignments current snapshot does not cover active papers correctly or violates current-status ledger semantics.",
    )
    add_result(results, "5", status, detail, "Data/discipline_code_assignments.jsonl")

    assignment_ids = [str(row.get("assignment_id", "")).strip() for row in assignments]
    assignment_id_uniqueness_ok = len(assignment_ids) == len(set(assignment_ids))
    assignment_id_format_ok = all(ASSIGNMENT_ID_PATTERN.fullmatch(value) for value in assignment_ids)
    assignment_core_fields_ok = all(
        DATE_PATTERN.fullmatch(str(row.get("assigned_at", "")).strip())
        and bool(str(row.get("assigned_by", "")).strip())
        and bool(str(row.get("assignment_reason", "")).strip())
        and int(row.get("schema_version", 0)) == 1
        for row in assignments
    )
    status, detail = check(
        DISCIPLINE_ASSIGNMENTS_JSONL.exists()
        and assignment_statuses_ok
        and assignment_id_uniqueness_ok
        and assignment_id_format_ok
        and assignment_core_fields_ok,
        (
            "Stable discipline code assignment ledger exists with unique DCA assignment IDs, "
            "valid assignment statuses, and auditable assignment metadata fields."
        ),
        "Stable discipline code assignment ledger is missing or contains invalid assignment IDs, statuses, or required audit fields.",
    )
    add_result(results, "6", status, detail, "Data/discipline_code_assignments.jsonl")

    status, detail = check(
        CLASSIFICATION_CODE_INDEX.exists()
        and sqlite_classification_terms_count == len(primary_terms) + len(secondary_terms),
        (
            "classification_code_index.json is present as taxonomy vocabulary owner and "
            f"mirrors into SQLite classification_terms={sqlite_classification_terms_count}."
        ),
        "classification_code_index.json is missing or does not mirror cleanly into SQLite classification_terms.",
    )
    add_result(results, "7", status, detail, "Data/classification_code_index.json + Data/papers.sqlite")

    preview_status_counts: dict[str, int] = {}
    preview_current_statuses = {
        "active_code",
        "pending_secondary",
        "non_discipline_general_method",
    }
    preview_rows_ok = PREVIEW_CSV.exists() and len(preview_rows) == len(active_papers)
    preview_paper_ids_ok = {str(row.get("paper_id", "")) for row in preview_rows} == set(active_papers_by_id)
    preview_statuses_ok = all(
        str(row.get("proposed_assignment_status", "")) in preview_current_statuses
        for row in preview_rows
    )
    preview_pending_ok = True
    preview_general_method_ok = True
    preview_active_ok = True
    for row in preview_rows:
        status_name = str(row.get("proposed_assignment_status", "")).strip()
        preview_status_counts[status_name] = preview_status_counts.get(status_name, 0) + 1
        paper_id = str(row.get("paper_id", "")).strip()
        paper = active_papers_by_id.get(paper_id, {})
        modules = paper.get("scientific_object_modules", [])
        general_bucket = str(paper.get("general_method_bucket", ""))
        proposed_code = str(row.get("proposed_discipline_local_code", "")).strip()
        proposed_rank = str(row.get("discipline_local_rank", "")).strip()
        proposed_secondary = str(row.get("proposed_primary_taxonomy_code_2lvl", "")).strip()
        pending_reason = str(row.get("pending_reason", "")).strip()

        if status_name == "pending_secondary":
            preview_pending_ok = preview_pending_ok and (
                not proposed_code
                and not proposed_rank
                and not proposed_secondary
                and not DISCIPLINE_LOCAL_CODE_PATTERN.fullmatch(proposed_code)
                and pending_reason in {"missing_primary_module_for_filing", "missing_or_uncertain_secondary_class", "secondary_primary_mismatch"}
            )
        elif status_name == "non_discipline_general_method":
            preview_general_method_ok = preview_general_method_ok and (
                general_bucket != "none"
                and not modules
                and not proposed_code
                and not proposed_rank
                and not proposed_secondary
                and not pending_reason
            )
        elif status_name == "active_code":
            code_match = DISCIPLINE_LOCAL_CODE_PATTERN.fullmatch(proposed_code)
            secondary_match = SECONDARY_CODE_PATTERN.fullmatch(proposed_secondary)
            preview_active_ok = preview_active_ok and (
                code_match is not None
                and secondary_match is not None
                and proposed_rank == proposed_code.rsplit("-", 1)[-1]
                and code_match.group(1) == secondary_match.group(1)
                and code_match.group(2) == secondary_match.group(2)
                and not pending_reason
            )
    preview_ok = (
        preview_rows_ok
        and preview_paper_ids_ok
        and preview_statuses_ok
        and preview_pending_ok
        and preview_general_method_ok
        and preview_active_ok
    )
    status, detail = check(
        preview_ok,
        (
            "discipline_code_initial_assignment_preview.csv matches the active-paper review surface "
            f"and obeys preview assignment rules (active={preview_status_counts.get('active_code', 0)}, "
            f"pending={preview_status_counts.get('pending_secondary', 0)}, "
            f"general_method={preview_status_counts.get('non_discipline_general_method', 0)})."
        ),
        "discipline_code_initial_assignment_preview.csv is missing, mismatches active-paper coverage, or violates preview assignment rules.",
    )
    add_result(results, "8", status, detail, "Data/discipline_code_initial_assignment_preview.csv")

    registry_status_counts: dict[str, int] = {}
    registry_semantics_ok = True
    registry_metadata_uniform_ok = True
    for row in registry:
        paper_id = str(row.get("paper_id", "")).strip()
        assignment_status = str(row.get("assignment_status", "")).strip()
        registry_status_counts[assignment_status] = registry_status_counts.get(assignment_status, 0) + 1
        paper = active_papers_by_id.get(paper_id)
        assignment = current_snapshot_by_paper_id.get(paper_id)
        discipline_local_code = str(row.get("discipline_local_code") or "").strip()
        discipline_local_rank = str(row.get("discipline_local_rank") or "").strip()
        discipline_display_order = str(row.get("discipline_display_order") or "").strip()
        primary_taxonomy_code_2lvl = str(row.get("primary_taxonomy_code_2lvl") or "").strip()
        if paper is None or assignment is None:
            registry_semantics_ok = False
            continue
        if assignment_status != str(assignment.get("assignment_status", "")).strip():
            registry_semantics_ok = False
        if str(row.get("assignment_id", "")).strip() != str(assignment.get("assignment_id", "")).strip():
            registry_semantics_ok = False
        if str(row.get("title", "")).strip() != str(paper.get("title", "")).strip():
            registry_semantics_ok = False
        if row.get("scientific_object_modules") != paper.get("scientific_object_modules"):
            registry_semantics_ok = False
        if str(row.get("general_method_bucket", "")).strip() != str(paper.get("general_method_bucket", "")).strip():
            registry_semantics_ok = False
        if str(row.get("primary_module_for_filing", "")).strip() != str(paper.get("primary_module_for_filing", "")).strip():
            registry_semantics_ok = False
        if str(row.get("note_path", "")).strip() != str(paper.get("note_path", "")).strip():
            registry_semantics_ok = False
        if str(row.get("pdf_path", "")).strip() != str(paper.get("pdf_path", "")).strip():
            registry_semantics_ok = False
        if bool(row.get("active_confirmed_core")) != bool(paper.get("active_confirmed_core")):
            registry_semantics_ok = False
        if row.get("is_derived_snapshot") is not True:
            registry_semantics_ok = False
        if str(row.get("generated_by", "")).strip() != "export_structured_data.py":
            registry_metadata_uniform_ok = False
        if assignment_status == "active_code":
            code_match = DISCIPLINE_LOCAL_CODE_PATTERN.fullmatch(discipline_local_code)
            secondary_match = SECONDARY_CODE_PATTERN.fullmatch(primary_taxonomy_code_2lvl)
            registry_semantics_ok = registry_semantics_ok and (
                code_match is not None
                and secondary_match is not None
                and discipline_local_rank == discipline_local_code.rsplit("-", 1)[-1]
                and discipline_display_order == discipline_local_code
            )
        elif assignment_status == "pending_secondary":
            registry_semantics_ok = registry_semantics_ok and (
                not discipline_local_code
                and not discipline_local_rank
                and not primary_taxonomy_code_2lvl
                and discipline_display_order.startswith(
                    (str(row.get("primary_module_for_filing") or "").strip() or "ZZ") + "-"
                )
            )
        elif assignment_status == "non_discipline_general_method":
            registry_semantics_ok = registry_semantics_ok and (
                not discipline_local_code
                and not discipline_local_rank
                and not primary_taxonomy_code_2lvl
                and discipline_display_order.startswith("GM-PENDING-")
            )

    registry_metadata_ok = (
        DISCIPLINE_REGISTRY_JSONL.exists()
        and DISCIPLINE_REGISTRY_CSV.exists()
        and SQLITE_PATH.exists()
        and len(registry) == len(active_papers)
        and sqlite_registry_count == len(registry)
        and metadata.get("discipline_local_code_registry_row_count") == str(len(registry))
        and metadata.get("discipline_local_code_registry_generated_at") == metadata.get("papers_exported_at")
        and metadata.get("discipline_local_code_registry_generated_by") == "export_structured_data.py"
        and registry_metadata_uniform_ok
    )
    status, detail = check(
        registry_metadata_ok and registry_semantics_ok,
        (
            "discipline_local_code_registry is present in JSONL / CSV / SQLite with aligned derived snapshot metadata "
            f"and current-snapshot semantics (active={registry_status_counts.get('active_code', 0)}, "
            f"pending={registry_status_counts.get('pending_secondary', 0)}, "
            f"general_method={registry_status_counts.get('non_discipline_general_method', 0)})."
        ),
        "discipline_local_code_registry surfaces, snapshot metadata, or current-snapshot derived semantics are missing or inconsistent.",
    )
    add_result(results, "9", status, detail, "Data/discipline_local_code_registry.jsonl + Data/discipline_local_code_registry.csv + Data/papers.sqlite")

    governance_contracts = (
        (FIELD_OWNERSHIP_MATRIX, "field_ownership_matrix.md"),
        (DISCIPLINE_CODE_ASSIGNMENT_POLICY, "discipline_code_assignment_policy.md"),
        (PRIMARY_FILING_POLICY, "primary_filing_policy.md"),
        (CHECK_POLICY, "check_policy.md"),
        (DISCIPLINE_SCHEMA, "schema/discipline_code_assignments.schema.json"),
        (CLASSIFICATION_SCHEMA, "schema/classification_code_index.schema.json"),
    )
    governance_refs_ok = all(token in readme_text for _, token in governance_contracts)
    governance_files_exist = all(path.exists() for path, _ in governance_contracts)
    status, detail = check(
        governance_refs_ok and governance_files_exist,
        "README references the frozen ownership matrix, assignment/filing policies, check policy, and both schema contracts, and those governance files exist.",
        "README references and/or governance contract file existence are incomplete for the frozen ownership matrix, policy docs, check policy, or schema contracts.",
    )
    add_result(
        results,
        "10",
        status,
        detail,
        "Data/README.md + Data/field_ownership_matrix.md + Data/discipline_code_assignment_policy.md + Data/primary_filing_policy.md + Data/check_policy.md + Data/schema/*.json",
    )

    severity_counts = {}
    for severity in ("ERROR", "WARNING", "INFO"):
        match = re.search(
            rf"- `{severity}`:\s+(\d+)",
            integrity_report_text,
        )
        severity_counts[severity] = int(match.group(1)) if match else -1
    report_has_findings = any(count > 0 for count in severity_counts.values())
    report_sections_ok = all(
        section in integrity_report_text
        for section in ("## Summary", "## Summary By Finding Code", "## ERROR", "## WARNING", "## INFO")
    )
    report_summary_counts_ok = all(count >= 0 for count in severity_counts.values())
    report_detail_contract_ok = (
        ("Field:" in integrity_report_text and "Owner file:" in integrity_report_text)
        if report_has_findings
        else True
    )
    report_identifier_ok = (
        bool(re.search(r"`ASD-\d{4}`|`DCA-\d{6}`", integrity_report_text))
        if report_has_findings
        else True
    )
    report_ok = (
        report_sections_ok
        and report_summary_counts_ok
        and report_detail_contract_ok
        and report_identifier_ok
    )
    status, detail = check(
        report_ok,
        "Consistency checking emits structured severity summaries, finding-code summary, and detail rows with identifiers, fields, and owner-file attribution.",
        "integrity_check_report.md is missing required severity-summary, finding-code, identifier, field, or owner-file report structure.",
    )
    add_result(results, "11", status, detail, "Data/integrity_check_report.md")

    workflow_readme_ok = all(
        token in readme_text
        for token in (
            "Workflow order",
            "owner fact source",
            "scripts/run_structured_data_pipeline.py",
            "--with-execution-audit",
            "audit_execution_definition.py",
        )
    )
    workflow_pipeline_ok = all(
        token in pipeline_script_text
        for token in (
            "OWNER_FACT_SOURCE_PATHS",
            "print_preflight_summary",
            "export_structured_data.py",
            "check_data_consistency.py",
            "build_analysis_db.py",
            "--with-execution-audit",
            "audit_execution_definition.py",
        )
    )
    ordered_steps_ok = (
        pipeline_script_text.find("export_structured_data.py")
        < pipeline_script_text.find("check_data_consistency.py")
        < pipeline_script_text.find("build_analysis_db.py")
    )
    workflow_ok = (
        PIPELINE_SCRIPT.exists()
        and workflow_readme_ok
        and workflow_pipeline_ok
        and ordered_steps_ok
    )
    status, detail = check(
        workflow_ok,
        "The owner fact source -> export -> check -> build workflow is documented in README and exposed via a canonical pipeline script with preflight owner summary and optional execution audit.",
        "The canonical workflow is missing README coverage and/or pipeline-script support for owner preflight, ordered export/check/build execution, or optional execution audit.",
    )
    add_result(results, "12", status, detail, "scripts/run_structured_data_pipeline.py + Data/README.md")

    required_sqlite_tables = {
        "papers",
        "paper_modules",
        "paper_general_method_buckets",
        "discipline_code_assignments",
        "discipline_local_code_registry",
        "classification_terms",
        "pdf_evidence_status",
        "paper_assets",
        "notes",
    }
    status, detail = check(
        required_sqlite_tables.issubset(sqlite_table_names),
        (
            "SQLite analysis DB contains all named core tables from the long-term plan: "
            + ", ".join(sorted(required_sqlite_tables))
            + "."
        ),
        "SQLite analysis DB is missing one or more named core tables required by the long-term plan.",
    )
    add_result(results, "13", status, detail, "Data/papers.sqlite")

    four_fact_source_tokens = (
        "Paper_Lists/agent_master_paper_list.md",
        "Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md",
        "Data/discipline_code_assignments.jsonl",
        "Data/classification_code_index.json",
    )
    status, detail = check(
        FIELD_DICTIONARY.exists()
        and all(token in readme_text for token in four_fact_source_tokens)
        and all(token in field_dictionary_text for token in four_fact_source_tokens),
        (
            "README and field_dictionary both document the four fact-source model "
            "and explicitly name master, progress, discipline-code ledger, and taxonomy-owner files."
        ),
        "README and/or field_dictionary do not fully document the four fact-source model and its owner files.",
    )
    add_result(results, "14", status, detail, "Data/README.md + Data/field_dictionary.md")

    query_tokens = (
        "discipline-code-summary",
        "discipline-code",
        "secondary-class-summary",
        "secondary-class-pdf-coverage",
        "classification-terms",
    )
    status, detail = check(
        QUERY_SCRIPT.exists()
        and all(token in query_script_text for token in query_tokens)
        and all(token in readme_text for token in query_tokens),
        (
            "query_analysis_db.py exposes the named discipline/secondary-class query surfaces "
            "and README documents those commands for current structured-data querying."
        ),
        "query_analysis_db.py and/or README is missing the named discipline/secondary-class query surfaces from the current structured-data workflow.",
    )
    add_result(results, "15", status, detail, "scripts/query_analysis_db.py + Data/README.md")

    owner_guardrail_tokens = (
        "OWNER_GUARDED_PATHS",
        "assert_safe_output_paths",
        "classification_code_index.json",
        "discipline_code_assignments.jsonl",
        "change_log.jsonl",
    )
    owner_guardrail_readme_ok = all(
        token in readme_text
        for token in (
            "daily export must not overwrite owner fact sources",
            "discipline_code_assignments.jsonl",
            "classification_code_index.json",
            "change_log.jsonl",
        )
    )
    status, detail = check(
        all(token in export_script_text for token in owner_guardrail_tokens)
        and all(token in build_script_text for token in owner_guardrail_tokens)
        and owner_guardrail_readme_ok,
        (
            "export_structured_data.py and build_analysis_db.py both carry explicit owner-path write guardrails "
            "for discipline_code_assignments.jsonl, classification_code_index.json, and change_log.jsonl, "
            "and README documents the same protection."
        ),
        "Owner fact source write protection is missing from export/build scripts and/or README does not document the guarded owner files clearly.",
    )
    add_result(results, "16", status, detail, "scripts/export_structured_data.py + scripts/build_analysis_db.py + Data/README.md")

    change_log_fields_ok = all(
        isinstance(row.get("change_id"), str)
        and isinstance(row.get("paper_id"), str)
        and isinstance(row.get("changed_at"), str)
        and isinstance(row.get("changed_by"), str)
        and isinstance(row.get("change_type"), str)
        and "old_value" in row
        and "new_value" in row
        and isinstance(row.get("reason"), str)
        for row in change_log_rows
    )
    change_log_query_tokens = (
        "change-log-summary",
        "change-log",
    )
    status, detail = check(
        CHANGE_LOG_JSONL.exists()
        and bool(change_log_rows)
        and change_log_fields_ok
        and sqlite_change_log_count == len(change_log_rows)
        and "change_log" in sqlite_table_names
        and all(token in query_script_text for token in change_log_query_tokens)
        and all(token in readme_text for token in change_log_query_tokens),
        (
            "change_log.jsonl exists as a populated owner audit ledger, mirrors into SQLite "
            f"change_log={sqlite_change_log_count}, and the change-log query surfaces are documented and exposed."
        ),
        "change_log owner audit coverage is incomplete: the ledger is missing/empty, SQLite mirroring drifted, or change-log query surfaces are not fully exposed and documented.",
    )
    add_result(results, "17", status, detail, "Data/change_log.jsonl + Data/papers.sqlite + scripts/query_analysis_db.py + Data/README.md")

    owner_helper_scripts = (
        MANAGE_DISCIPLINE_CODE_ASSIGNMENTS_SCRIPT,
        MANAGE_CLASSIFICATION_CODE_INDEX_SCRIPT,
        MANAGE_PROGRESS_TRACKING_SCRIPT,
        MANAGE_MASTER_PAPER_LIST_SCRIPT,
        APPEND_CHANGE_LOG_SCRIPT,
    )
    owner_helper_readme_tokens = (
        "scripts/manage_discipline_code_assignments.py",
        "scripts/manage_classification_code_index.py",
        "scripts/manage_progress_tracking.py",
        "scripts/manage_master_paper_list.py",
        "scripts/append_change_log.py",
        "Daily export must not write owner fact sources. The corresponding owner-maintenance helpers are explicit commands:",
    )
    owner_helper_script_tokens_ok = (
        all(path.exists() for path in owner_helper_scripts)
        and all(
            token in manage_discipline_code_assignments_script_text
            for token in ("--paper-id", "--target-status", "--assignment-reason", "--change-reason", "--dry-run")
        )
        and all(
            token in manage_classification_code_index_script_text
            for token in ("sync", "upsert-primary", "upsert-secondary", "--dry-run")
        )
        and all(
            token in manage_progress_tracking_script_text
            for token in ("--paper-id", "--set", "--reason", "--dry-run")
        )
        and all(
            token in manage_master_paper_list_script_text
            for token in ("--paper-id", "--set", "--reason", "--dry-run")
        )
        and all(
            token in append_change_log_script_text
            for token in ("--paper-id", "--change-type", "--reason")
        )
    )
    status, detail = check(
        owner_helper_script_tokens_ok
        and all(token in readme_text for token in owner_helper_readme_tokens),
        (
            "Explicit owner-maintenance helper commands exist for discipline-code, taxonomy, progress, master, "
            "and direct change-log updates, and README documents those operational entry points."
        ),
        "One or more owner-maintenance helper commands is missing required CLI surface coverage or README does not document the explicit owner-maintenance entry points clearly.",
    )
    add_result(results, "18", status, detail, "scripts/manage_*.py + scripts/append_change_log.py + Data/README.md")

    field_ownership_matrix_text = read_text(FIELD_OWNERSHIP_MATRIX)
    field_ownership_tokens = (
        "source_file: Paper_Lists/agent_master_paper_list.md",
        "fallback_order:",
        "required_trace_fields:",
        "source_confidence",
        "parser_rule",
        "discipline_code_assignments.jsonl",
        "classification_code_index.json",
        "repair the owner file, then rerun `export -> check -> build`",
    )
    status, detail = check(
        all(token in field_ownership_matrix_text for token in field_ownership_tokens),
        (
            "field_ownership_matrix.md encodes the canonical master-derived fallback/trace contract "
            "and the owner-vs-derived repair rule for discipline-code and taxonomy owner files."
        ),
        "field_ownership_matrix.md is missing one or more frozen canonical-lane fallback/trace or owner-vs-derived repair semantics required by the long-term plan.",
    )
    add_result(results, "19", status, detail, "Data/field_ownership_matrix.md")

    check_policy_text = read_text(CHECK_POLICY)
    check_policy_tokens = (
        "`ERROR`",
        "`WARNING`",
        "`INFO`",
        "Must be fixed before build / commit",
        "Does not block, but must enter review backlog",
        "Does not block",
    )
    severity_enforcement_tokens = (
        "validate_classification_code_index_owner(",
        "validate_discipline_code_assignments_owner(",
        "validate_payload_against_schema_file(",
        "validate_jsonl_rows_against_schema_file(",
        'severity_order = ("ERROR", "WARNING", "INFO")',
    )
    status, detail = check(
        all(token in check_policy_text for token in check_policy_tokens)
        and all(token in read_text(ROOT / "scripts" / "check_data_consistency.py") for token in severity_enforcement_tokens),
        (
            "check_policy.md defines the frozen ERROR/WARNING/INFO build semantics, and "
            "check_data_consistency.py enforces schema-backed owner validation plus the same severity buckets."
        ),
        "The frozen severity/build policy is not fully documented in check_policy.md and/or check_data_consistency.py is missing the expected schema-backed owner validation and severity enforcement hooks.",
    )
    add_result(results, "20", status, detail, "Data/check_policy.md + scripts/check_data_consistency.py")

    lifecycle_query_tokens = (
        "lifecycle-summary",
        "lifecycle-records",
    )
    lifecycle_fields_ok = all(
        isinstance(row.get("record_status"), str)
        and isinstance(row.get("inclusion_decision"), str)
        and isinstance(row.get("duplicate_of"), str)
        and isinstance(row.get("last_reviewed_at"), str)
        and isinstance(row.get("last_reviewed_by"), str)
        for row in papers
    )
    lifecycle_semantics_ok = all(
        (
            bool(row.get("active_confirmed_core"))
            and str(row.get("record_status")) == "active_confirmed_core"
            and str(row.get("inclusion_decision")) == "confirmed_core"
        )
        or (
            not bool(row.get("active_confirmed_core"))
        )
        for row in papers
    )
    lifecycle_duplicate_format_ok = all(
        not str(row.get("duplicate_of") or "").strip()
        or PAPER_ID_PATTERN.fullmatch(str(row.get("duplicate_of") or "").strip()) is not None
        for row in papers
    )
    lifecycle_status_counts: dict[str, int] = {}
    for row in papers:
        status_name = str(row.get("record_status") or "").strip()
        lifecycle_status_counts[status_name] = lifecycle_status_counts.get(status_name, 0) + 1
    status, detail = check(
        lifecycle_fields_ok
        and lifecycle_semantics_ok
        and lifecycle_duplicate_format_ok
        and sqlite_papers_count == len(papers)
        and QUERY_SCRIPT.exists()
        and all(token in query_script_text for token in lifecycle_query_tokens)
        and all(token in readme_text for token in lifecycle_query_tokens),
        (
            "Derived lifecycle fields are populated across all "
            f"{len(papers)} papers, mirror into SQLite papers={sqlite_papers_count}, "
            "and the lifecycle query surfaces are documented and exposed "
            f"(active={lifecycle_status_counts.get('active_confirmed_core', 0)}, "
            f"background={lifecycle_status_counts.get('background_only', 0)}, "
            f"excluded={lifecycle_status_counts.get('excluded', 0)}, "
            f"duplicate={lifecycle_status_counts.get('duplicate', 0)})."
        ),
        "Derived lifecycle fields are missing/inconsistent, SQLite papers drifted from papers.jsonl, or lifecycle query surfaces are not fully exposed and documented.",
    )
    add_result(results, "21", status, detail, "Data/papers.jsonl + Data/papers.sqlite + scripts/query_analysis_db.py + Data/README.md")

    metadata_query_tokens = (
        "metadata",
        "discipline-registry-metadata",
        "snapshot-provenance",
    )
    required_metadata_keys = {
        "papers_exported_at",
        "discipline_local_code_registry_generated_at",
        "discipline_local_code_registry_generated_by",
        "discipline_local_code_registry_source_commit",
        "discipline_local_code_registry_worktree_dirty",
        "discipline_local_code_registry_row_count",
    }
    status, detail = check(
        required_metadata_keys.issubset(metadata.keys())
        and QUERY_SCRIPT.exists()
        and all(token in query_script_text for token in metadata_query_tokens)
        and all(token in readme_text for token in metadata_query_tokens),
        (
            "SQLite metadata carries the current papers/registry provenance bundle and "
            "the metadata / discipline-registry-metadata / snapshot-provenance query surfaces are documented and exposed."
        ),
        "SQLite metadata provenance keys are incomplete or the metadata/provenance query surfaces are not fully exposed and documented.",
    )
    add_result(results, "22", status, detail, "Data/papers.sqlite + scripts/query_analysis_db.py + Data/README.md")

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
