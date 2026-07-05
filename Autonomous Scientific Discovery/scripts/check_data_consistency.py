#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple


ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "Data"
REGISTRY_DIR = DATA_DIR / "registry"
CLASSIFICATION_CODE_INDEX_PATH = DATA_DIR / "classification_code_index.json"
DISCIPLINE_CODE_ASSIGNMENTS_PATH = DATA_DIR / "discipline_code_assignments.jsonl"
DISCIPLINE_LOCAL_CODE_REGISTRY_PATH = DATA_DIR / "discipline_local_code_registry.jsonl"
CHANGE_LOG_PATH = DATA_DIR / "change_log.jsonl"
INTEGRITY_CHECK_REPORT_PATH = DATA_DIR / "integrity_check_report.md"
SCHEMA_DIR = DATA_DIR / "schema"
CLASSIFICATION_CODE_INDEX_SCHEMA_PATH = (
    SCHEMA_DIR / "classification_code_index.schema.json"
)
DISCIPLINE_CODE_ASSIGNMENTS_SCHEMA_PATH = (
    SCHEMA_DIR / "discipline_code_assignments.schema.json"
)
MASTER_PATH = ROOT / "Paper_Lists" / "agent_master_paper_list.md"
PROGRESS_PATH = (
    ROOT
    / "Coverage_Check"
    / "multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md"
)
EXPECTED_ACTIVE_CONFIRMED = 447
EXPECTED_ACTIVE_LOCAL_PDF = 422
EXPECTED_ACTIVE_NO_LOCAL_PDF = 25
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
PRIMARY_MODULE_CONFIDENCE_VALUES = {"high", "medium", "low"}
PRIMARY_MODULE_ASSIGNMENT_RULE_VALUES = {
    "main_scientific_object",
    "main_validation_object",
    "direct_contribution_target",
    "substantive_application_object",
    "manual_override",
}
CLASSIFICATION_SOURCE_CONFIDENCE_VALUES = {"high", "medium", "low"}
CLASSIFICATION_PARSER_RULE_VALUES = {
    "structured_remark_token",
    "legacy_general_method_fallback",
    "legacy_main_class_fallback",
    "needs_review",
}
RECORD_STATUSES = {
    "candidate",
    "active_confirmed_core",
    "background_only",
    "excluded",
    "duplicate",
    "retired",
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
CHANGE_ID_PATTERN = re.compile(r"^CL-[0-9]{6}$")
DISCIPLINE_CODE_PATTERN = re.compile(r"^[0-9]{2}-[0-9]{2}-[0-9]{3}$")
PRIMARY_TAXONOMY_2LVL_PATTERN = re.compile(r"^[0-9]{2}\.[0-9]{2}$")
REGISTRY_REQUIRED_STEMS = (
    "paper_registry",
    "paper_identifier_aliases",
    "taxonomy_registry",
    "classification_assignments",
    "pdf_archive_registry",
    "asset_manifest",
)
CLASSIFICATION_SCOPE_MODULE = "scientific_object_modules"
CLASSIFICATION_SCOPE_GENERAL_BUCKET = "general_method_bucket"
ASSET_TYPE_NOTE = "note"
ASSET_TYPE_PRIMARY_PDF = "primary_pdf"
PDF_EVIDENCE_TYPE_VALUES = {
    "main_pdf",
    "supplementary_pdf",
    "html_full_text",
    "abstract",
    "official_page",
    "project_page",
}
PDF_CHECK_STATUS_VALUES = {
    "full_text_checked",
    "source_limited",
    "metadata_only",
}
MASTER_HEADER = (
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
)
PROGRESS_HEADER = (
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
)


def validate_classification_code_index_owner() -> None:
    validate_payload_against_schema_file(
        payload=load_json(CLASSIFICATION_CODE_INDEX_PATH),
        schema_path=CLASSIFICATION_CODE_INDEX_SCHEMA_PATH,
        subject_label="classification_code_index.json",
    )
    payload = load_json(CLASSIFICATION_CODE_INDEX_PATH)
    required_keys = (
        "primary_code_to_label",
        "secondary_code_to_label",
        "label_to_primary_code",
        "label_to_secondary_code",
        "primary_terms",
        "secondary_terms",
    )
    for key in required_keys:
        assert_true(
            key in payload,
            f"classification_code_index.json missing required key {key!r}",
        )

    primary_code_to_label = payload["primary_code_to_label"]
    label_to_primary_code = payload["label_to_primary_code"]
    secondary_code_to_label = payload["secondary_code_to_label"]
    label_to_secondary_code = payload["label_to_secondary_code"]
    primary_terms = payload["primary_terms"]
    secondary_terms = payload["secondary_terms"]

    assert_true(isinstance(primary_terms, list), "classification_code_index.json primary_terms must be a list")
    assert_true(isinstance(secondary_terms, list), "classification_code_index.json secondary_terms must be a list")

    seen_primary_codes = set()
    for term in primary_terms:
        assert_true(isinstance(term, dict), "classification_code_index.json primary_terms rows must be objects")
        code = term.get("primary_code")
        label = term.get("label")
        assert_true(isinstance(code, str) and code, "primary_terms row missing primary_code")
        assert_true(code not in seen_primary_codes, f"classification_code_index.json duplicate primary_code {code!r}")
        seen_primary_codes.add(code)
        assert_true(
            primary_code_to_label.get(code) == label,
            f"classification_code_index.json primary_code_to_label mismatch for {code!r}",
        )
        assert_true(
            label_to_primary_code.get(label) == code,
            f"classification_code_index.json label_to_primary_code mismatch for {label!r}",
        )

    seen_secondary_codes = set()
    for term in secondary_terms:
        assert_true(isinstance(term, dict), "classification_code_index.json secondary_terms rows must be objects")
        code = term.get("secondary_code")
        label = term.get("label")
        parent_primary_code = term.get("parent_primary_code")
        assert_true(isinstance(code, str) and code, "secondary_terms row missing secondary_code")
        assert_true(
            code not in seen_secondary_codes,
            f"classification_code_index.json duplicate secondary_code {code!r}",
        )
        seen_secondary_codes.add(code)
        assert_true(
            isinstance(parent_primary_code, str) and parent_primary_code in FORMAL_MODULES,
            f"classification_code_index.json secondary_code {code!r} has invalid parent_primary_code {parent_primary_code!r}",
        )
        assert_true(
            code.startswith(parent_primary_code + "."),
            f"classification_code_index.json secondary_code {code!r} does not match parent_primary_code {parent_primary_code!r}",
        )
        assert_true(
            secondary_code_to_label.get(code) == label,
            f"classification_code_index.json secondary_code_to_label mismatch for {code!r}",
        )
        assert_true(
            label_to_secondary_code.get(label) == code,
            f"classification_code_index.json label_to_secondary_code mismatch for {label!r}",
        )

    assert_true(
        set(secondary_code_to_label.keys()) == seen_secondary_codes,
        "classification_code_index.json secondary_code_to_label coverage does not match secondary_terms",
    )
    assert_true(
        set(label_to_secondary_code.values()) == seen_secondary_codes,
        "classification_code_index.json label_to_secondary_code coverage does not match secondary_terms",
    )


def validate_discipline_code_assignments_owner(papers: List[Dict[str, object]]) -> None:
    if not DISCIPLINE_CODE_ASSIGNMENTS_PATH.exists():
        return

    rows = load_jsonl(DISCIPLINE_CODE_ASSIGNMENTS_PATH)
    assert_true(rows, "discipline_code_assignments.jsonl must not be empty")
    validate_jsonl_rows_against_schema_file(
        rows=rows,
        schema_path=DISCIPLINE_CODE_ASSIGNMENTS_SCHEMA_PATH,
        subject_label="discipline_code_assignments.jsonl",
    )

    paper_rows_by_id = {str(row["paper_id"]): row for row in papers}
    seen_assignment_ids = set()
    active_codes = {}
    active_code_by_paper = {}
    current_snapshot_by_paper = {}
    all_used_codes = {}

    for index, row in enumerate(rows, start=1):
        assignment_id = row.get("assignment_id")
        paper_id = row.get("paper_id")
        assignment_status = row.get("assignment_status")
        discipline_local_code = row.get("discipline_local_code")
        primary_taxonomy_code_2lvl = row.get("primary_taxonomy_code_2lvl")
        redirected_to_code = row.get("redirected_to_code")
        pending_reason = row.get("pending_reason")

        assert_true(
            isinstance(assignment_id, str) and re.fullmatch(r"DCA-[0-9]{6}", assignment_id),
            f"discipline_code_assignments row {index} has invalid assignment_id: {assignment_id!r}",
        )
        assert_true(
            assignment_id not in seen_assignment_ids,
            f"discipline_code_assignments duplicate assignment_id: {assignment_id!r}",
        )
        seen_assignment_ids.add(assignment_id)

        assert_true(
            isinstance(paper_id, str) and paper_id in paper_rows_by_id,
            f"discipline_code_assignments references unknown paper_id: {paper_id!r}",
        )
        assert_true(
            assignment_status
            in {
                "active_code",
                "retired_code",
                "redirected_code",
                "pending_secondary",
                "non_discipline_general_method",
            },
            f"discipline_code_assignments {assignment_id} has invalid assignment_status: {assignment_status!r}",
        )

        if assignment_status in {"active_code", "retired_code", "redirected_code"}:
            assert_true(
                isinstance(discipline_local_code, str)
                and DISCIPLINE_CODE_PATTERN.fullmatch(discipline_local_code),
                f"discipline_code_assignments {assignment_id} must carry a valid discipline_local_code",
            )
            assert_true(
                isinstance(primary_taxonomy_code_2lvl, str)
                and PRIMARY_TAXONOMY_2LVL_PATTERN.fullmatch(primary_taxonomy_code_2lvl),
                f"discipline_code_assignments {assignment_id} must carry a valid primary_taxonomy_code_2lvl",
            )
            assert_true(
                discipline_local_code not in all_used_codes,
                "discipline_code_assignments reused historical discipline_local_code: "
                f"{discipline_local_code} ({all_used_codes.get(discipline_local_code)} vs {assignment_id})",
            )
            all_used_codes[discipline_local_code] = assignment_id
            if assignment_status == "active_code":
                assert_true(
                    discipline_local_code not in active_codes,
                    f"discipline_code_assignments duplicate active discipline_local_code: {discipline_local_code}",
                )
                active_codes[discipline_local_code] = assignment_id
                assert_true(
                    paper_id not in active_code_by_paper,
                    f"discipline_code_assignments paper_id has multiple active_code rows: {paper_id}",
                )
                active_code_by_paper[paper_id] = assignment_id
        else:
            assert_true(
                discipline_local_code is None,
                f"discipline_code_assignments {assignment_id} pending/general-method row must not carry discipline_local_code",
            )
            assert_true(
                primary_taxonomy_code_2lvl is None,
                f"discipline_code_assignments {assignment_id} pending/general-method row must not carry primary_taxonomy_code_2lvl",
            )

        if assignment_status == "pending_secondary":
            assert_true(
                isinstance(pending_reason, str) and pending_reason.strip(),
                f"discipline_code_assignments {assignment_id} pending_secondary row missing pending_reason",
            )
        elif assignment_status == "non_discipline_general_method":
            assert_true(
                pending_reason is None,
                f"discipline_code_assignments {assignment_id} non_discipline_general_method row must not carry pending_reason",
            )
        else:
            assert_true(
                pending_reason is None,
                f"discipline_code_assignments {assignment_id} active/retired/redirected row must not carry pending_reason",
            )

        if assignment_status == "redirected_code":
            assert_true(
                isinstance(redirected_to_code, str)
                and DISCIPLINE_CODE_PATTERN.fullmatch(redirected_to_code),
                f"discipline_code_assignments {assignment_id} redirected_code row missing valid redirected_to_code",
            )
        else:
            assert_true(
                redirected_to_code is None,
                f"discipline_code_assignments {assignment_id} non-redirected row must not carry redirected_to_code",
            )

        if assignment_status in {
            "active_code",
            "pending_secondary",
            "non_discipline_general_method",
        }:
            assert_true(
                paper_id not in current_snapshot_by_paper,
                "discipline_code_assignments paper_id has multiple current snapshot rows: "
                f"{paper_id}",
            )
            current_snapshot_by_paper[paper_id] = assignment_id

    for row in rows:
        if row["assignment_status"] == "redirected_code":
            assert_true(
                row["redirected_to_code"] in active_codes,
                f"discipline_code_assignments redirected_to_code does not point to an active code: {row['redirected_to_code']!r}",
            )

    expected_active_confirmed_core_ids = {
        str(row["paper_id"])
        for row in papers
        if bool(row["active_confirmed_core"])
    }
    current_snapshot_paper_ids = set(current_snapshot_by_paper)
    assert_true(
        current_snapshot_paper_ids == expected_active_confirmed_core_ids,
        "discipline_code_assignments current snapshot coverage must exactly match active_confirmed_core papers",
    )


def validate_discipline_local_code_registry(
    papers: List[Dict[str, object]],
) -> None:
    if not DISCIPLINE_LOCAL_CODE_REGISTRY_PATH.exists():
        return
    assert_true(
        DISCIPLINE_CODE_ASSIGNMENTS_PATH.exists(),
        "discipline_local_code_registry.jsonl exists but discipline_code_assignments.jsonl is missing",
    )

    registry_rows = load_jsonl(DISCIPLINE_LOCAL_CODE_REGISTRY_PATH)
    ledger_rows = load_jsonl(DISCIPLINE_CODE_ASSIGNMENTS_PATH)
    papers_by_id = {str(row["paper_id"]): row for row in papers}
    ledger_by_assignment_id = {
        str(row["assignment_id"]): row for row in ledger_rows
    }
    current_snapshot_assignment_ids = {
        str(row["assignment_id"])
        for row in ledger_rows
        if row["assignment_status"]
        in {"active_code", "pending_secondary", "non_discipline_general_method"}
    }

    assert_true(
        len(registry_rows) == len(current_snapshot_assignment_ids),
        "discipline_local_code_registry.jsonl row count does not match current snapshot rows in discipline_code_assignments.jsonl",
    )
    expected_active_confirmed_core_ids = {
        str(row["paper_id"])
        for row in papers
        if bool(row["active_confirmed_core"])
    }

    seen_paper_ids = set()
    generated_at_values = set()
    generated_by_values = set()
    source_commit_values = set()
    worktree_dirty_values = set()

    for index, row in enumerate(registry_rows, start=1):
        assignment_id = str(row.get("assignment_id", ""))
        paper_id = str(row.get("paper_id", ""))
        assert_true(
            assignment_id in ledger_by_assignment_id,
            f"discipline_local_code_registry unknown assignment_id at row {index}: {assignment_id!r}",
        )
        assert_true(
            assignment_id in current_snapshot_assignment_ids,
            f"discipline_local_code_registry must only expose current snapshot assignments: {assignment_id!r}",
        )
        assert_true(
            paper_id in papers_by_id,
            f"discipline_local_code_registry unknown paper_id at row {index}: {paper_id!r}",
        )
        assert_true(
            paper_id not in seen_paper_ids,
            f"discipline_local_code_registry duplicate paper_id: {paper_id!r}",
        )
        seen_paper_ids.add(paper_id)

        ledger_row = ledger_by_assignment_id[assignment_id]
        paper_row = papers_by_id[paper_id]
        assert_true(
            paper_id == str(ledger_row["paper_id"]),
            f"discipline_local_code_registry assignment/paper mismatch for {assignment_id}",
        )
        assert_true(
            row["assignment_status"] == ledger_row["assignment_status"],
            f"discipline_local_code_registry assignment_status mismatch for {assignment_id}",
        )
        assert_true(
            row["discipline_local_code"] == ledger_row["discipline_local_code"],
            f"discipline_local_code_registry discipline_local_code mismatch for {assignment_id}",
        )
        expected_rank = (
            str(row["discipline_local_code"]).rsplit("-", 1)[-1]
            if row["discipline_local_code"]
            else ""
        )
        assert_true(
            row["discipline_local_rank"] == expected_rank,
            f"discipline_local_code_registry discipline_local_rank mismatch for {assignment_id}",
        )
        assignment_status = str(row["assignment_status"])
        if assignment_status == "active_code":
            assert_true(
                row["discipline_display_order"] == row["discipline_local_code"],
                f"discipline_local_code_registry active_code discipline_display_order mismatch for {assignment_id}",
            )
        elif assignment_status == "pending_secondary":
            assert_true(
                str(row["discipline_display_order"]).startswith(
                    f"{row['primary_module_for_filing'] or 'ZZ'}-"
                )
                and "PENDING" in str(row["discipline_display_order"]),
                f"discipline_local_code_registry pending_secondary discipline_display_order mismatch for {assignment_id}",
            )
        elif assignment_status == "non_discipline_general_method":
            assert_true(
                str(row["discipline_display_order"]).startswith("GM-PENDING-"),
                f"discipline_local_code_registry general-method discipline_display_order mismatch for {assignment_id}",
            )
        assert_true(
            row["primary_taxonomy_code_2lvl"] == ledger_row["primary_taxonomy_code_2lvl"],
            f"discipline_local_code_registry primary_taxonomy_code_2lvl mismatch for {assignment_id}",
        )
        assert_true(
            row["assigned_at"] == ledger_row["assigned_at"],
            f"discipline_local_code_registry assigned_at mismatch for {assignment_id}",
        )
        assert_true(
            row["assigned_by"] == ledger_row["assigned_by"],
            f"discipline_local_code_registry assigned_by mismatch for {assignment_id}",
        )
        assert_true(
            row["retired_at"] == ledger_row["retired_at"],
            f"discipline_local_code_registry retired_at mismatch for {assignment_id}",
        )
        assert_true(
            row["redirected_to_code"] == ledger_row["redirected_to_code"],
            f"discipline_local_code_registry redirected_to_code mismatch for {assignment_id}",
        )
        assert_true(
            row["assignment_reason"] == ledger_row["assignment_reason"],
            f"discipline_local_code_registry assignment_reason mismatch for {assignment_id}",
        )
        assert_true(
            row["pending_reason"] == ledger_row["pending_reason"],
            f"discipline_local_code_registry pending_reason mismatch for {assignment_id}",
        )
        assert_true(
            row["primary_module_for_filing"] == paper_row["primary_module_for_filing"],
            f"discipline_local_code_registry primary_module_for_filing mismatch for {assignment_id}",
        )
        assert_true(
            row["primary_module_confidence"] == paper_row["primary_module_confidence"],
            f"discipline_local_code_registry primary_module_confidence mismatch for {assignment_id}",
        )
        assert_true(
            row["primary_module_assignment_rule"] == paper_row["primary_module_assignment_rule"],
            f"discipline_local_code_registry primary_module_assignment_rule mismatch for {assignment_id}",
        )
        assert_true(
            row["primary_module_override_reason"] == paper_row["primary_module_override_reason"],
            f"discipline_local_code_registry primary_module_override_reason mismatch for {assignment_id}",
        )
        assert_true(
            row["legacy_secondary_class"] == paper_row["legacy_secondary_class"],
            f"discipline_local_code_registry legacy_secondary_class mismatch for {assignment_id}",
        )
        assert_true(
            row["scientific_object_modules"] == paper_row["scientific_object_modules"],
            f"discipline_local_code_registry scientific_object_modules mismatch for {assignment_id}",
        )
        assert_true(
            row["general_method_bucket"] == paper_row["general_method_bucket"],
            f"discipline_local_code_registry general_method_bucket mismatch for {assignment_id}",
        )
        assert_true(
            row["title"] == paper_row["title"],
            f"discipline_local_code_registry title mismatch for {assignment_id}",
        )
        assert_true(
            row["note_path"] == paper_row["note_path"],
            f"discipline_local_code_registry note_path mismatch for {assignment_id}",
        )
        assert_true(
            row["pdf_path"] == paper_row["pdf_path"],
            f"discipline_local_code_registry pdf_path mismatch for {assignment_id}",
        )
        assert_true(
            row["active_confirmed_core"] == paper_row["active_confirmed_core"],
            f"discipline_local_code_registry active_confirmed_core mismatch for {assignment_id}",
        )
        assert_true(
            row["is_derived_snapshot"] is True,
            f"discipline_local_code_registry is_derived_snapshot must be true for {assignment_id}",
        )

        generated_at_values.add(str(row["generated_at"]))
        generated_by_values.add(str(row["generated_by"]))
        source_commit_values.add(str(row["source_commit"]))
        worktree_dirty_values.add(bool(row["worktree_dirty"]))

    assert_true(
        len(generated_at_values) == 1,
        "discipline_local_code_registry generated_at must be uniform across the snapshot",
    )
    assert_true(
        len(generated_by_values) == 1,
        "discipline_local_code_registry generated_by must be uniform across the snapshot",
    )
    assert_true(
        len(source_commit_values) == 1,
        "discipline_local_code_registry source_commit must be uniform across the snapshot",
    )
    assert_true(
        len(worktree_dirty_values) == 1,
        "discipline_local_code_registry worktree_dirty must be uniform across the snapshot",
    )
    assert_true(
        seen_paper_ids == expected_active_confirmed_core_ids,
        "discipline_local_code_registry paper coverage must exactly match active_confirmed_core papers",
    )


def validate_change_log_owner(papers: List[Dict[str, object]]) -> None:
    if not CHANGE_LOG_PATH.exists():
        return

    rows = load_jsonl(CHANGE_LOG_PATH)
    papers_by_id = {str(row["paper_id"]): row for row in papers}
    seen_change_ids = set()

    for index, row in enumerate(rows, start=1):
        change_id = row.get("change_id")
        paper_id = row.get("paper_id")
        changed_at = row.get("changed_at")
        changed_by = row.get("changed_by")
        change_type = row.get("change_type")
        reason = row.get("reason")

        assert_true(
            isinstance(change_id, str) and CHANGE_ID_PATTERN.fullmatch(change_id),
            f"change_log row {index} has invalid change_id: {change_id!r}",
        )
        assert_true(
            change_id not in seen_change_ids,
            f"change_log duplicate change_id: {change_id!r}",
        )
        seen_change_ids.add(change_id)

        assert_true(
            isinstance(paper_id, str) and paper_id in papers_by_id,
            f"change_log references unknown paper_id: {paper_id!r}",
        )
        assert_true(
            isinstance(changed_at, str) and re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", changed_at),
            f"change_log {change_id} has invalid changed_at: {changed_at!r}",
        )
        assert_true(
            isinstance(changed_by, str) and changed_by.strip(),
            f"change_log {change_id} missing changed_by",
        )
        assert_true(
            isinstance(change_type, str) and change_type.strip(),
            f"change_log {change_id} missing change_type",
        )
        assert_true(
            isinstance(reason, str) and reason.strip(),
            f"change_log {change_id} missing reason",
        )
        assert_true(
            "old_value" in row and "new_value" in row,
            f"change_log {change_id} must include old_value and new_value",
        )



def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> List[Dict[str, object]]:
    rows: List[Dict[str, object]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


class SchemaValidationError(Exception):
    pass


def resolve_schema_ref(root_schema: Dict[str, Any], ref: str) -> Dict[str, Any]:
    assert_true(ref.startswith("#/"), f"Unsupported schema ref: {ref!r}")
    target: Any = root_schema
    for part in ref[2:].split("/"):
        assert_true(
            isinstance(target, dict) and part in target,
            f"Broken schema ref: {ref!r}",
        )
        target = target[part]
    assert_true(isinstance(target, dict), f"Schema ref must resolve to object: {ref!r}")
    return target


def matches_json_type(value: Any, expected_type: str) -> bool:
    if expected_type == "object":
        return isinstance(value, dict)
    if expected_type == "array":
        return isinstance(value, list)
    if expected_type == "string":
        return isinstance(value, str)
    if expected_type == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected_type == "number":
        return (isinstance(value, int) or isinstance(value, float)) and not isinstance(
            value, bool
        )
    if expected_type == "boolean":
        return isinstance(value, bool)
    if expected_type == "null":
        return value is None
    raise SchemaValidationError(f"Unsupported schema type: {expected_type!r}")


def schema_condition_matches(
    value: Any,
    schema_fragment: Dict[str, Any],
    root_schema: Dict[str, Any],
    path: str,
) -> bool:
    try:
        validate_against_schema(
            value=value,
            schema=schema_fragment,
            root_schema=root_schema,
            path=path,
        )
    except SchemaValidationError:
        return False
    return True


def validate_against_schema(
    *,
    value: Any,
    schema: Dict[str, Any],
    root_schema: Dict[str, Any],
    path: str,
) -> None:
    if "$ref" in schema:
        validate_against_schema(
            value=value,
            schema=resolve_schema_ref(root_schema, str(schema["$ref"])),
            root_schema=root_schema,
            path=path,
        )
        return

    for subschema in schema.get("allOf", []):
        assert_true(isinstance(subschema, dict), f"Invalid allOf schema at {path}")
        validate_against_schema(
            value=value,
            schema=subschema,
            root_schema=root_schema,
            path=path,
        )

    conditional = schema.get("if")
    then_schema = schema.get("then")
    if isinstance(conditional, dict) and isinstance(then_schema, dict):
        if schema_condition_matches(
            value=value,
            schema_fragment=conditional,
            root_schema=root_schema,
            path=path,
        ):
            validate_against_schema(
                value=value,
                schema=then_schema,
                root_schema=root_schema,
                path=path,
            )

    expected_type = schema.get("type")
    if expected_type is not None:
        if isinstance(expected_type, list):
            if not any(matches_json_type(value, str(item)) for item in expected_type):
                raise SchemaValidationError(
                    f"{path} has type {type(value).__name__}, expected one of {expected_type!r}"
                )
        else:
            if not matches_json_type(value, str(expected_type)):
                raise SchemaValidationError(
                    f"{path} has type {type(value).__name__}, expected {expected_type!r}"
                )

    if "enum" in schema and value not in schema["enum"]:
        raise SchemaValidationError(f"{path} value {value!r} is outside enum {schema['enum']!r}")

    if "const" in schema and value != schema["const"]:
        raise SchemaValidationError(f"{path} value {value!r} does not match const {schema['const']!r}")

    if isinstance(value, str):
        min_length = schema.get("minLength")
        if isinstance(min_length, int) and len(value) < min_length:
            raise SchemaValidationError(
                f"{path} string is shorter than minLength {min_length}"
            )
        pattern = schema.get("pattern")
        if isinstance(pattern, str) and not re.fullmatch(pattern, value):
            raise SchemaValidationError(
                f"{path} value {value!r} does not match pattern {pattern!r}"
            )

    if isinstance(value, dict):
        required = schema.get("required", [])
        for key in required:
            if key not in value:
                raise SchemaValidationError(f"{path} is missing required key {key!r}")

        properties = schema.get("properties", {})
        for key, prop_schema in properties.items():
            if key in value:
                assert_true(
                    isinstance(prop_schema, dict),
                    f"Invalid property schema for {path}.{key}",
                )
                validate_against_schema(
                    value=value[key],
                    schema=prop_schema,
                    root_schema=root_schema,
                    path=f"{path}.{key}",
                )

        additional_properties = schema.get("additionalProperties", True)
        extra_keys = [key for key in value if key not in properties]
        if additional_properties is False and extra_keys:
            raise SchemaValidationError(
                f"{path} has unexpected keys: {', '.join(sorted(extra_keys))}"
            )
        if isinstance(additional_properties, dict):
            for key in extra_keys:
                validate_against_schema(
                    value=value[key],
                    schema=additional_properties,
                    root_schema=root_schema,
                    path=f"{path}.{key}",
                )

    if isinstance(value, list):
        items_schema = schema.get("items")
        if isinstance(items_schema, dict):
            for index, item in enumerate(value):
                validate_against_schema(
                    value=item,
                    schema=items_schema,
                    root_schema=root_schema,
                    path=f"{path}[{index}]",
                )


def validate_payload_against_schema_file(
    *,
    payload: Any,
    schema_path: Path,
    subject_label: str,
) -> None:
    assert_true(schema_path.exists(), f"Missing schema file: {schema_path}")
    schema = load_json(schema_path)
    try:
        validate_against_schema(
            value=payload,
            schema=schema,
            root_schema=schema,
            path=subject_label,
        )
    except SchemaValidationError as exc:
        raise AssertionError(f"{subject_label} failed schema validation: {exc}") from exc


def validate_jsonl_rows_against_schema_file(
    *,
    rows: List[Dict[str, object]],
    schema_path: Path,
    subject_label: str,
) -> None:
    assert_true(schema_path.exists(), f"Missing schema file: {schema_path}")
    schema = load_json(schema_path)
    for index, row in enumerate(rows, start=1):
        try:
            validate_against_schema(
                value=row,
                schema=schema,
                root_schema=schema,
                path=f"{subject_label}[{index}]",
            )
        except SchemaValidationError as exc:
            raise AssertionError(
                f"{subject_label} row {index} failed schema validation: {exc}"
            ) from exc


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def add_finding(
    findings: List[Dict[str, str]],
    *,
    severity: str,
    category: str,
    code: str,
    message: str,
    owner_file: str,
    subject_id: str = "",
) -> None:
    findings.append(
        {
            "severity": severity,
            "category": category,
            "code": code,
            "subject_id": subject_id,
            "message": message,
            "owner_file": owner_file,
        }
    )


def collect_non_blocking_findings(
    *,
    papers: List[Dict[str, object]],
    classification_code_index: Dict[str, object],
    discipline_code_assignments: List[Dict[str, object]],
    discipline_local_code_registry: List[Dict[str, object]],
) -> List[Dict[str, str]]:
    findings: List[Dict[str, str]] = []

    for paper in papers:
        paper_id = str(paper["paper_id"])
        if bool(paper["active_confirmed_core"]) and not bool(paper["pdf_exists"]):
            add_finding(
                findings,
                severity="WARNING",
                category="evidence",
                code="MISSING_LOCAL_PDF",
                subject_id=paper_id,
                message="Active confirmed-core paper currently has no local PDF.",
                owner_file="Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md",
            )
        if bool(paper["active_confirmed_core"]) and str(paper["source_limited"]).startswith("yes"):
            add_finding(
                findings,
                severity="WARNING",
                category="evidence",
                code="SOURCE_LIMITED",
                subject_id=paper_id,
                message="Active confirmed-core paper remains source-limited.",
                owner_file="Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md",
            )

    for assignment in discipline_code_assignments:
        paper_id = str(assignment["paper_id"])
        assignment_id = str(assignment["assignment_id"])
        status = str(assignment["assignment_status"])
        if status == "pending_secondary":
            add_finding(
                findings,
                severity="WARNING",
                category="discipline_code",
                code="PENDING_SECONDARY",
                subject_id=f"{paper_id} / {assignment_id}",
                message=(
                    "Discipline code assignment remains pending secondary review: "
                    f"{assignment.get('pending_reason') or '(no pending_reason)'}."
                ),
                owner_file="Data/discipline_code_assignments.jsonl",
            )
        elif status == "non_discipline_general_method":
            add_finding(
                findings,
                severity="INFO",
                category="discipline_code",
                code="NON_DISCIPLINE_GENERAL_METHOD",
                subject_id=f"{paper_id} / {assignment_id}",
                message="Record is intentionally kept outside normal discipline shelving as pure general-method-only.",
                owner_file="Data/discipline_code_assignments.jsonl",
            )

    for term in classification_code_index.get("secondary_terms", []):
        secondary_code = str(term.get("secondary_code", ""))
        status = str(term.get("status", ""))
        review_status = str(term.get("review_status", ""))
        if status != "active" or review_status != "reviewed":
            add_finding(
                findings,
                severity="WARNING",
                category="taxonomy",
                code="SECONDARY_TERM_NEEDS_REVIEW",
                subject_id=secondary_code,
                message=(
                    f"Secondary taxonomy term remains provisional "
                    f"(status={status or '(blank)'}, review_status={review_status or '(blank)'})."
                ),
                owner_file="Data/classification_code_index.json",
            )

    if discipline_local_code_registry:
        worktree_dirty_values = {bool(row.get("worktree_dirty")) for row in discipline_local_code_registry}
        if worktree_dirty_values == {True}:
            add_finding(
                findings,
                severity="INFO",
                category="derived_snapshot",
                code="DERIVED_SNAPSHOT_WORKTREE_DIRTY",
                message="Derived discipline-local registry snapshot was generated from a dirty worktree.",
                owner_file="Data/discipline_local_code_registry.jsonl",
            )

    return findings


def write_integrity_check_report(
    *,
    findings: List[Dict[str, str]],
    status: str,
) -> None:
    severity_order = ("ERROR", "WARNING", "INFO")
    category_order = (
        "identity",
        "evidence",
        "discipline_code",
        "taxonomy",
        "asset",
        "note",
        "derived_snapshot",
        "audit",
        "other",
    )
    counts = {
        severity: sum(1 for finding in findings if finding["severity"] == severity)
        for severity in severity_order
    }
    category_counts = {
        category: sum(1 for finding in findings if finding["category"] == category)
        for category in category_order
        if any(finding["category"] == category for finding in findings)
    }
    code_counts = {}
    for finding in findings:
        code_counts[finding["code"]] = code_counts.get(finding["code"], 0) + 1

    lines = [
        "# ASD integrity check report",
        "",
        f"Status: `{status}`",
        "",
        "## Summary",
        "",
        f"- `ERROR`: {counts['ERROR']}",
        f"- `WARNING`: {counts['WARNING']}",
        f"- `INFO`: {counts['INFO']}",
        "",
        "## Summary By Category",
        "",
    ]

    if category_counts:
        for category, count in category_counts.items():
            lines.append(f"- `{category}`: {count}")
    else:
        lines.append("- None")
    lines.extend(["", "## Summary By Finding Code", ""])
    if code_counts:
        for code, count in sorted(code_counts.items(), key=lambda item: (-item[1], item[0])):
            lines.append(f"- `{code}`: {count}")
    else:
        lines.append("- None")
    lines.append("")

    for severity in severity_order:
        lines.extend([f"## {severity}", ""])
        severity_findings = [finding for finding in findings if finding["severity"] == severity]
        if not severity_findings:
            lines.extend(["- None", ""])
            continue
        grouped: Dict[str, List[Dict[str, str]]] = {}
        for finding in severity_findings:
            grouped.setdefault(finding["category"], []).append(finding)
        for category in category_order:
            category_findings = grouped.get(category, [])
            if not category_findings:
                continue
            lines.extend([f"### {category}", ""])
            for finding in category_findings:
                parts = [f"`{finding['code']}`"]
                if finding["subject_id"]:
                    parts.append(f"`{finding['subject_id']}`")
                parts.append(finding["message"])
                lines.append("- " + " | ".join(parts))
                lines.append(f"  Owner file: `{finding['owner_file']}`")
            lines.append("")

    INTEGRITY_CHECK_REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def read_text_lossy(path: Path) -> str:
    raw = path.read_bytes()
    for encoding in ("utf-8", "utf-8-sig", "gb18030"):
        try:
            return raw.decode(encoding)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", errors="replace")


def is_markdown_separator(line: str) -> bool:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return False
    cells = [cell.strip() for cell in stripped[1:-1].split("|")]
    if not cells:
        return False
    return all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells)


def split_markdown_row_strict(line: str, expected_cols: int) -> List[str]:
    stripped = line.strip()
    assert_true(stripped.startswith("|") and stripped.endswith("|"), f"Malformed markdown row: {line!r}")
    parts = [part.strip() for part in stripped[1:-1].split("|")]
    assert_true(
        len(parts) == expected_cols,
        f"Unexpected markdown column count {len(parts)} != {expected_cols} in row: {line!r}",
    )
    return parts


def parse_markdown_table_strict(
    path: Path, header: Tuple[str, ...], data_prefix: str
) -> List[Dict[str, str]]:
    lines = read_text_lossy(path).splitlines()
    header_marker = "| " + " | ".join(header) + " |"
    try:
        start_index = next(index for index, line in enumerate(lines) if line.strip() == header_marker)
    except StopIteration as exc:
        raise AssertionError(f"Header marker not found in {path.relative_to(ROOT)}") from exc

    parsed_header = split_markdown_row_strict(lines[start_index], len(header))
    assert_true(tuple(parsed_header) == header, f"Unexpected header in {path.relative_to(ROOT)}")

    data_start = start_index + 1
    if data_start < len(lines) and is_markdown_separator(lines[data_start]):
        data_start += 1

    rows: List[Dict[str, str]] = []
    for line in lines[data_start:]:
        if not line.startswith(data_prefix):
            continue
        rows.append(dict(zip(header, split_markdown_row_strict(line, len(header)))))
    return rows


def load_json_rows(path: Path, list_keys: Iterable[str] = ("records",)) -> List[Dict[str, object]]:
    payload = load_json(path)
    if isinstance(payload, list):
        rows = payload
    elif isinstance(payload, dict):
        rows = None
        for list_key in list_keys:
            candidate = payload.get(list_key)
            if isinstance(candidate, list):
                rows = candidate
                break
        if rows is None:
            raise AssertionError(
                f"{path.relative_to(ROOT)} must serialize rows as JSONL, a top-level JSON array, or a JSON object with one of {tuple(list_keys)} as an array field"
            )
    else:
        raise AssertionError(
            f"{path.relative_to(ROOT)} must serialize rows as JSONL, a top-level JSON array, or a JSON object with one of {tuple(list_keys)} as an array field"
        )
    normalized_rows: List[Dict[str, object]] = []
    for index, row in enumerate(rows, start=1):
        assert_true(
            isinstance(row, dict),
            f"{path.relative_to(ROOT)} row {index} is not a JSON object",
        )
        normalized_rows.append(row)
    return normalized_rows


def load_registry_rows(stem: str) -> Tuple[Path, List[Dict[str, object]]]:
    candidates = [REGISTRY_DIR / f"{stem}.jsonl", REGISTRY_DIR / f"{stem}.json"]
    existing = [path for path in candidates if path.exists()]
    assert_true(
        len(existing) == 1,
        f"Expected exactly one registry file for {stem} under {REGISTRY_DIR.relative_to(ROOT)}; found {[path.name for path in existing] or 'none'}",
    )
    path = existing[0]
    list_keys = ("records", "taxonomy_terms") if stem == "taxonomy_registry" else ("records",)
    rows = load_jsonl(path) if path.suffix == ".jsonl" else load_json_rows(path, list_keys=list_keys)
    return path, rows


def require_row_fields(path: Path, rows: List[Dict[str, object]], field_names: Iterable[str]) -> None:
    required = tuple(field_names)
    for index, row in enumerate(rows, start=1):
        missing = [field_name for field_name in required if field_name not in row]
        assert_true(
            not missing,
            f"{path.relative_to(ROOT)} row {index} missing required fields: {missing}",
        )


def assert_unique_registry_key(
    path: Path, rows: List[Dict[str, object]], key_fields: Iterable[str]
) -> None:
    field_names = tuple(key_fields)
    seen = set()
    for index, row in enumerate(rows, start=1):
        key = tuple(row[field_name] for field_name in field_names)
        assert_true(
            key not in seen,
            f"{path.relative_to(ROOT)} has duplicate key {dict(zip(field_names, key))} at row {index}",
        )
        seen.add(key)


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


def validate_authoritative_sources(papers: List[Dict[str, object]]) -> None:
    master_rows = parse_markdown_table_strict(
        MASTER_PATH, header=MASTER_HEADER, data_prefix="| ASD-"
    )
    progress_rows = parse_markdown_table_strict(
        PROGRESS_PATH, header=PROGRESS_HEADER, data_prefix="| ASD-"
    )
    master_by_id = {row["ID"]: row for row in master_rows}
    progress_by_id = {row["paper_id"]: row for row in progress_rows}
    paper_rows_by_id = {row["paper_id"]: row for row in papers}

    assert_true(
        set(master_by_id.keys()) == set(paper_rows_by_id.keys()),
        "papers.jsonl paper_id coverage does not match agent_master_paper_list.md",
    )

    for paper_id, paper_row in paper_rows_by_id.items():
        master_row = master_by_id[paper_id]
        progress_row = progress_by_id.get(paper_id, {})
        assert_true(
            paper_row["title"] == master_row["Paper title"],
            f"{paper_id} title drift between master and papers.jsonl",
        )
        assert_true(
            paper_row["inclusion_status"] == master_row["Inclusion status"],
            f"{paper_id} inclusion_status drift between master and papers.jsonl",
        )
        assert_true(
            paper_row["remarks"] == master_row["Remarks"],
            f"{paper_id} remarks drift between master and papers.jsonl",
        )
        assert_true(
            paper_row["legacy_main_class"] == master_row["Main class"],
            f"{paper_id} legacy_main_class drift between master and papers.jsonl",
        )
        assert_true(
            paper_row["legacy_secondary_class"] == master_row["Secondary class"],
            f"{paper_id} legacy_secondary_class drift between master and papers.jsonl",
        )
        assert_true(
            paper_row["legacy_tertiary_class"] == master_row["Tertiary class"],
            f"{paper_id} legacy_tertiary_class drift between master and papers.jsonl",
        )
        expected_note_path = progress_row.get("note_path") or master_row["Note path"]
        expected_pdf_path = progress_row.get("pdf_path") or master_row["PDF path"]
        assert_true(
            paper_row["note_path"] == expected_note_path,
            f"{paper_id} note_path drift against master/progress derived expectation",
        )
        assert_true(
            paper_row["pdf_path"] == expected_pdf_path,
            f"{paper_id} pdf_path drift against master/progress derived expectation",
        )
        for progress_field, paper_field in (
            ("title", "progress_title"),
            ("pdf_status", "pdf_status"),
            ("evidence_status", "evidence_status"),
            ("note_status", "note_status"),
            ("master_status", "master_status"),
            ("batch", "batch"),
            ("closed", "closed"),
        ):
            assert_true(
                paper_row[paper_field] == progress_row.get(progress_field, ""),
                f"{paper_id} {paper_field} drift between progress and papers.jsonl",
            )
        assert_true(
            paper_row["source_limited"] == (progress_row.get("source_limited", "").strip().lower()),
            f"{paper_id} source_limited drift between progress and papers.jsonl",
        )


def collect_final_modules_mirror_drifts(
    papers: List[Dict[str, object]]
) -> List[Dict[str, object]]:
    drifts: List[Dict[str, object]] = []
    for row in papers:
        if not row["active_confirmed_core"]:
            continue
        final_assignments = tuple(
            module_code for module_code in row["final_modules_or_bucket"] if module_code != "01.04"
        )
        derived_assignments = tuple(row["scientific_object_modules"])
        derived_bucket = "01.04" if row["general_method_bucket"] != "none" else ""
        final_has_bucket = "01.04" if "01.04" in row["final_modules_or_bucket"] else ""
        if final_assignments == derived_assignments and final_has_bucket == derived_bucket:
            continue

        if final_has_bucket != derived_bucket:
            drift_kind = "semantic_drift"
            drift_reason = "general_bucket_mismatch"
        elif set(final_assignments) != set(derived_assignments):
            drift_kind = "semantic_drift"
            drift_reason = "formal_module_membership_mismatch"
        else:
            drift_kind = "order_drift"
            drift_reason = "formal_module_order_mismatch"

        drifts.append(
            {
                "paper_id": str(row["paper_id"]),
                "drift_kind": drift_kind,
                "drift_reason": drift_reason,
                "derived_modules": list(derived_assignments),
                "final_modules": list(final_assignments),
                "derived_bucket": derived_bucket,
                "final_bucket": final_has_bucket,
            }
        )
    return drifts


def validate_registry_layer(
    papers: List[Dict[str, object]],
    taxonomy_index: Dict[str, Dict[str, str]],
    require_registry: bool,
) -> None:
    if not REGISTRY_DIR.exists():
        assert_true(
            not require_registry,
            f"Registry directory missing: {REGISTRY_DIR.relative_to(ROOT)}",
        )
        print("Registry checks skipped because Data/registry is absent and ASD_REQUIRE_REGISTRY=0.")
        return

    paper_rows_by_id = {row["paper_id"]: row for row in papers}
    active_ids = {row["paper_id"] for row in papers if row["active_confirmed_core"]}
    active_local_ids = {
        row["paper_id"] for row in papers if row["active_confirmed_core"] and row["pdf_exists"]
    }
    active_no_local_ids = active_ids - active_local_ids

    registry_payloads = {
        stem: load_registry_rows(stem) for stem in REGISTRY_REQUIRED_STEMS
    }
    paper_registry_path, paper_registry_rows = registry_payloads["paper_registry"]
    alias_registry_path, alias_registry_rows = registry_payloads["paper_identifier_aliases"]
    taxonomy_registry_path, taxonomy_registry_rows = registry_payloads["taxonomy_registry"]
    assignments_path, assignment_rows = registry_payloads["classification_assignments"]
    pdf_registry_path, pdf_registry_rows = registry_payloads["pdf_archive_registry"]
    asset_manifest_path, asset_manifest_rows = registry_payloads["asset_manifest"]

    require_row_fields(paper_registry_path, paper_registry_rows, ("paper_id",))
    assert_unique_registry_key(paper_registry_path, paper_registry_rows, ("paper_id",))
    paper_registry_ids = {row["paper_id"] for row in paper_registry_rows}
    assert_true(
        paper_registry_ids == set(paper_rows_by_id.keys()),
        "paper_registry paper_id coverage does not match papers.jsonl",
    )

    require_row_fields(
        alias_registry_path,
        alias_registry_rows,
        ("paper_id", "alias_scheme", "alias_value", "is_primary_key"),
    )
    assert_unique_registry_key(
        alias_registry_path,
        alias_registry_rows,
        ("paper_id", "alias_scheme", "alias_value"),
    )
    valid_alias_schemes = {"doi", "arxiv_id", "url"}
    for row in alias_registry_rows:
        paper_id = row["paper_id"]
        assert_true(
            paper_id in paper_rows_by_id,
            f"paper_identifier_aliases references unknown paper_id: {paper_id!r}",
        )
        assert_true(
            row["alias_scheme"] in valid_alias_schemes,
            f"paper_identifier_aliases has invalid alias_scheme for {paper_id}: {row['alias_scheme']!r}",
        )
        assert_true(
            isinstance(row["alias_value"], str) and bool(row["alias_value"].strip()),
            f"paper_identifier_aliases has blank alias_value for {paper_id}",
        )
        assert_true(
            row["is_primary_key"] is False,
            f"paper_identifier_aliases should not redefine primary keys for {paper_id}",
        )

    require_row_fields(
        taxonomy_registry_path,
        taxonomy_registry_rows,
        ("taxonomy_code", "kind", "labels"),
    )
    assert_unique_registry_key(taxonomy_registry_path, taxonomy_registry_rows, ("taxonomy_code",))
    taxonomy_codes = {row["taxonomy_code"] for row in taxonomy_registry_rows}
    expected_taxonomy_codes = set(taxonomy_index["code_to_label"].keys())
    assert_true(
        taxonomy_codes == expected_taxonomy_codes,
        "taxonomy_registry taxonomy_code coverage does not match taxonomy_index.json",
    )
    for row in taxonomy_registry_rows:
        code = row["taxonomy_code"]
        assert_true(
            code in expected_taxonomy_codes,
            f"taxonomy_registry has unknown taxonomy_code: {code!r}",
        )
        expected_kind = "general_bucket" if code == "01.04" else "formal_module"
        labels = row["labels"]
        assert_true(
            isinstance(labels, dict) and isinstance(labels.get("display"), str),
            f"taxonomy_registry labels.display missing or invalid for {code}",
        )
        assert_true(
            labels["display"] == taxonomy_index["code_to_label"][code],
            f"taxonomy_registry label mismatch for {code}: {labels['display']!r}",
        )
        assert_true(
            row["kind"] == expected_kind,
            f"taxonomy_registry kind mismatch for {code}: {row['kind']!r}",
        )

    require_row_fields(
        assignments_path,
        assignment_rows,
        ("paper_id", "taxonomy_code", "assignment_kind", "assignment_source"),
    )
    assert_unique_registry_key(
        assignments_path,
        assignment_rows,
        ("paper_id", "assignment_source", "taxonomy_code"),
    )
    expected_assignment_rows = {}
    for row in papers:
        paper_id = row["paper_id"]
        for sort_order, module_code in enumerate(row["scientific_object_modules"], start=1):
            expected_assignment_rows[
                (paper_id, CLASSIFICATION_SCOPE_MODULE, module_code)
            ] = sort_order
        if row["general_method_bucket"] != "none":
            expected_assignment_rows[(paper_id, CLASSIFICATION_SCOPE_GENERAL_BUCKET, "01.04")] = 1
    actual_assignment_rows = {}
    for row in assignment_rows:
        paper_id = row["paper_id"]
        assignment_scope = row["assignment_source"]
        assignment_kind = row["assignment_kind"]
        taxonomy_code = row["taxonomy_code"]
        assert_true(
            paper_id in paper_rows_by_id,
            f"classification_assignments references unknown paper_id: {paper_id!r}",
        )
        assert_true(
            assignment_scope in {CLASSIFICATION_SCOPE_MODULE, CLASSIFICATION_SCOPE_GENERAL_BUCKET},
            f"classification_assignments has invalid assignment_scope for {paper_id}: {assignment_scope!r}",
        )
        if assignment_scope == CLASSIFICATION_SCOPE_MODULE:
            assert_true(
                assignment_kind == "formal_module",
                f"classification_assignments formal module must use assignment_kind=formal_module for {paper_id}: {assignment_kind!r}",
            )
            assert_true(
                taxonomy_code in FORMAL_MODULES,
                f"classification_assignments formal module must stay in 01-11 for {paper_id}: {taxonomy_code!r}",
            )
        else:
            assert_true(
                assignment_kind == "general_bucket",
                f"classification_assignments general bucket must use assignment_kind=general_bucket for {paper_id}: {assignment_kind!r}",
            )
            assert_true(
                taxonomy_code == "01.04",
                f"classification_assignments general bucket must use taxonomy_code 01.04 for {paper_id}: {taxonomy_code!r}",
            )
        actual_assignment_rows[(paper_id, assignment_scope, taxonomy_code)] = row.get("assignment_order")
    assert_true(
        set(actual_assignment_rows.keys()) == set(expected_assignment_rows.keys()),
        "classification_assignments coverage does not match papers.jsonl scientific_object_modules/general_method_bucket facts",
    )
    for key, expected_sort_order in expected_assignment_rows.items():
        actual_sort_order = actual_assignment_rows[key]
        if actual_sort_order is not None:
            assert_true(
                actual_sort_order == expected_sort_order,
                f"classification_assignments assignment_order mismatch for {key}: {actual_sort_order!r} != {expected_sort_order!r}",
            )

    require_row_fields(
        pdf_registry_path,
        pdf_registry_rows,
        ("paper_id", "active_confirmed_core", "pdf_exists", "pdf_status"),
    )
    assert_unique_registry_key(pdf_registry_path, pdf_registry_rows, ("paper_id",))
    pdf_registry_rows_by_id = {}
    for row in pdf_registry_rows:
        paper_id = row["paper_id"]
        assert_true(
            paper_id in paper_rows_by_id,
            f"pdf_archive_registry references unknown paper_id: {paper_id!r}",
        )
        assert_true(
            isinstance(row["active_confirmed_core"], bool),
            f"pdf_archive_registry active_confirmed_core must be bool for {paper_id}",
        )
        assert_true(
            isinstance(row["pdf_exists"], bool),
            f"pdf_archive_registry pdf_exists must be bool for {paper_id}",
        )
        pdf_registry_rows_by_id[paper_id] = row
    assert_true(
        active_ids.issubset(set(pdf_registry_rows_by_id.keys())),
        "pdf_archive_registry must cover every active confirmed-core paper",
    )
    registry_active_ids = {
        paper_id
        for paper_id, row in pdf_registry_rows_by_id.items()
        if row["active_confirmed_core"]
    }
    registry_active_local_ids = {
        paper_id
        for paper_id, row in pdf_registry_rows_by_id.items()
        if row["active_confirmed_core"] and row["pdf_exists"]
    }
    registry_active_no_local_ids = registry_active_ids - registry_active_local_ids
    assert_true(
        registry_active_ids == active_ids,
        "pdf_archive_registry active_confirmed_core coverage does not match papers.jsonl",
    )
    assert_true(
        registry_active_local_ids == active_local_ids,
        "pdf_archive_registry local-PDF active set does not match papers.jsonl",
    )
    assert_true(
        registry_active_no_local_ids == active_no_local_ids,
        "pdf_archive_registry no-local-PDF active set does not match papers.jsonl",
    )
    for paper_id in active_ids:
        registry_row = pdf_registry_rows_by_id[paper_id]
        paper_row = paper_rows_by_id[paper_id]
        assert_true(
            registry_row["pdf_status"] == paper_row["pdf_status"],
            f"pdf_archive_registry pdf_status mismatch for {paper_id}: {registry_row['pdf_status']!r} != {paper_row['pdf_status']!r}",
        )
        assert_true(
            registry_row["evidence_status"] == paper_row["evidence_status"],
            f"pdf_archive_registry evidence_status mismatch for {paper_id}: {registry_row['evidence_status']!r} != {paper_row['evidence_status']!r}",
        )
        if "pdf_path" in registry_row:
            assert_true(
                registry_row["pdf_path"] == paper_row["pdf_path"],
                f"pdf_archive_registry pdf_path mismatch for {paper_id}: {registry_row['pdf_path']!r} != {paper_row['pdf_path']!r}",
            )
        assert_true(
            registry_row["pdf_evidence_type"] in PDF_EVIDENCE_TYPE_VALUES,
            f"pdf_archive_registry has invalid pdf_evidence_type for {paper_id}: {registry_row['pdf_evidence_type']!r}",
        )
        assert_true(
            registry_row["pdf_check_status"] in PDF_CHECK_STATUS_VALUES,
            f"pdf_archive_registry has invalid pdf_check_status for {paper_id}: {registry_row['pdf_check_status']!r}",
        )
        assert_true(
            isinstance(registry_row["is_main_text"], bool),
            f"pdf_archive_registry is_main_text must be bool for {paper_id}",
        )
        assert_true(
            isinstance(registry_row["is_supplementary"], bool),
            f"pdf_archive_registry is_supplementary must be bool for {paper_id}",
        )
        assert_true(
            not (registry_row["is_main_text"] and registry_row["is_supplementary"]),
            f"pdf_archive_registry rows cannot be both main_text and supplementary for {paper_id}",
        )
        if registry_row["pdf_evidence_type"] == "main_pdf":
            assert_true(
                registry_row["is_main_text"] and not registry_row["is_supplementary"],
                f"pdf_archive_registry main_pdf rows must set is_main_text=true for {paper_id}",
            )
        if registry_row["pdf_evidence_type"] == "supplementary_pdf":
            assert_true(
                registry_row["is_supplementary"] and not registry_row["is_main_text"],
                f"pdf_archive_registry supplementary_pdf rows must set is_supplementary=true for {paper_id}",
            )
        if registry_row["pdf_check_status"] == "full_text_checked":
            assert_true(
                registry_row["pdf_evidence_type"] in {"main_pdf", "html_full_text", "supplementary_pdf"},
                f"pdf_archive_registry full_text_checked rows must come from a full-text evidence type for {paper_id}",
            )
        if registry_row["asset_size_bytes"] is not None:
            assert_true(
                isinstance(registry_row["asset_size_bytes"], int) and registry_row["asset_size_bytes"] >= 0,
                f"pdf_archive_registry asset_size_bytes must be non-negative int for {paper_id}",
            )

    require_row_fields(
        asset_manifest_path,
        asset_manifest_rows,
        ("paper_id", "asset_type", "path", "exists"),
    )
    note_asset_rows = []
    primary_pdf_asset_rows = []
    seen_asset_keys = set()
    for index, row in enumerate(asset_manifest_rows, start=1):
        paper_id = row["paper_id"]
        asset_type = row["asset_type"]
        assert_true(
            paper_id in paper_rows_by_id,
            f"asset_manifest references unknown paper_id: {paper_id!r}",
        )
        assert_true(
            isinstance(row["exists"], bool),
            f"asset_manifest exists must be bool for {paper_id}",
        )
        assert_true(
            isinstance(row.get("is_main_text"), bool),
            f"asset_manifest is_main_text must be bool for {paper_id}",
        )
        assert_true(
            isinstance(row.get("is_supplementary"), bool),
            f"asset_manifest is_supplementary must be bool for {paper_id}",
        )
        if row.get("asset_size_bytes") is not None:
            assert_true(
                isinstance(row["asset_size_bytes"], int) and row["asset_size_bytes"] >= 0,
                f"asset_manifest asset_size_bytes must be non-negative int for {paper_id}",
            )
        if asset_type in {ASSET_TYPE_NOTE, ASSET_TYPE_PRIMARY_PDF}:
            key = (paper_id, asset_type)
            assert_true(
                key not in seen_asset_keys,
                f"asset_manifest has duplicate {asset_type} record for {paper_id} at row {index}",
            )
            seen_asset_keys.add(key)
            if asset_type == ASSET_TYPE_NOTE:
                note_asset_rows.append(row)
            else:
                primary_pdf_asset_rows.append(row)
    assert_true(note_asset_rows, "asset_manifest missing note asset records")
    assert_true(primary_pdf_asset_rows, "asset_manifest missing primary_pdf asset records")
    note_assets_by_id = {row["paper_id"]: row for row in note_asset_rows}
    expected_note_ids = set(paper_rows_by_id.keys())
    assert_true(
        set(note_assets_by_id.keys()) == expected_note_ids,
        "asset_manifest note coverage does not match papers.jsonl paper_id coverage",
    )
    for paper_id, asset_row in note_assets_by_id.items():
        paper_row = paper_rows_by_id[paper_id]
        assert_true(
            asset_row["path"] == paper_row["note_path"],
            f"asset_manifest note path mismatch for {paper_id}: {asset_row['path']!r} != {paper_row['note_path']!r}",
        )
        assert_true(
            asset_row["exists"] == paper_row["note_exists"],
            f"asset_manifest note existence mismatch for {paper_id}: {asset_row['exists']!r} != {paper_row['note_exists']!r}",
        )
        assert_true(
            not asset_row["is_main_text"] and not asset_row["is_supplementary"],
            f"asset_manifest note rows must not be marked main/supplementary for {paper_id}",
        )
    primary_pdf_assets_by_id = {row["paper_id"]: row for row in primary_pdf_asset_rows}
    expected_primary_pdf_ids = set(paper_rows_by_id.keys())
    assert_true(
        set(primary_pdf_assets_by_id.keys()) == expected_primary_pdf_ids,
        "asset_manifest primary_pdf coverage does not match papers.jsonl paper_id coverage",
    )
    for paper_id in expected_primary_pdf_ids:
        asset_row = primary_pdf_assets_by_id[paper_id]
        paper_row = paper_rows_by_id[paper_id]
        assert_true(
            asset_row["path"] == paper_row["pdf_path"],
            f"asset_manifest primary_pdf path mismatch for {paper_id}: {asset_row['path']!r} != {paper_row['pdf_path']!r}",
        )
        assert_true(
            asset_row["exists"] == paper_row["pdf_exists"],
            f"asset_manifest primary_pdf existence mismatch for {paper_id}: {asset_row['exists']!r} != {paper_row['pdf_exists']!r}",
        )
        if asset_row["exists"]:
            assert_true(
                bool(asset_row["sha256"]),
                f"asset_manifest existing primary_pdf rows must carry sha256 for {paper_id}",
            )
            assert_true(
                asset_row["asset_size_bytes"] is not None,
                f"asset_manifest existing primary_pdf rows must carry asset_size_bytes for {paper_id}",
            )
        if asset_row["is_supplementary"]:
            assert_true(
                not asset_row["is_main_text"],
                f"asset_manifest supplementary primary_pdf rows must not be marked is_main_text for {paper_id}",
            )
        if asset_row["is_main_text"]:
            assert_true(
                not asset_row["is_supplementary"],
                f"asset_manifest main-text primary_pdf rows must not be marked is_supplementary for {paper_id}",
            )


def main() -> None:
    strict_authoritative = os.environ.get("ASD_STRICT_AUTHORITATIVE", "1") != "0"
    require_registry = os.environ.get("ASD_REQUIRE_REGISTRY", "1") != "0"
    findings: List[Dict[str, str]] = []
    try:
        validate_classification_code_index_owner()
        classification_code_index = load_json(CLASSIFICATION_CODE_INDEX_PATH)
        papers = load_jsonl(DATA_DIR / "papers.jsonl")
        taxonomy_index = load_json(DATA_DIR / "taxonomy_index.json")
        pdf_manifest = load_json(DATA_DIR / "pdf_manifest.json")
        missing_pdf_manifest = load_json(DATA_DIR / "missing_pdf_manifest.json")
        note_manifest = load_json(DATA_DIR / "note_manifest.json")
        discipline_code_assignments = (
            load_jsonl(DISCIPLINE_CODE_ASSIGNMENTS_PATH)
            if DISCIPLINE_CODE_ASSIGNMENTS_PATH.exists()
            else []
        )
        discipline_local_code_registry = (
            load_jsonl(DISCIPLINE_LOCAL_CODE_REGISTRY_PATH)
            if DISCIPLINE_LOCAL_CODE_REGISTRY_PATH.exists()
            else []
        )
        validate_discipline_code_assignments_owner(papers)
        validate_discipline_local_code_registry(papers)
        validate_change_log_owner(papers)

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
            assert_true(
                row.get("record_status") in RECORD_STATUSES,
                f"{paper_id} has invalid record_status: {row.get('record_status')!r}",
            )
            assert_true(
                isinstance(row.get("inclusion_decision"), str) and row.get("inclusion_decision", "").strip(),
                f"{paper_id} has blank inclusion_decision",
            )
            assert_true(
                isinstance(row.get("duplicate_of"), str),
                f"{paper_id} duplicate_of must be a string",
            )
            assert_true(
                isinstance(row.get("last_reviewed_at"), str),
                f"{paper_id} last_reviewed_at must be a string",
            )
            assert_true(
                isinstance(row.get("last_reviewed_by"), str),
                f"{paper_id} last_reviewed_by must be a string",
            )
            assert_true(
                isinstance(row.get("primary_module_confidence"), str),
                f"{paper_id} primary_module_confidence must be a string",
            )
            assert_true(
                isinstance(row.get("primary_module_assignment_rule"), str),
                f"{paper_id} primary_module_assignment_rule must be a string",
            )
            assert_true(
                isinstance(row.get("primary_module_override_reason"), str),
                f"{paper_id} primary_module_override_reason must be a string",
            )
            assert_true(
                isinstance(row.get("classification_source_field"), str),
                f"{paper_id} classification_source_field must be a string",
            )
            assert_true(
                isinstance(row.get("classification_source_confidence"), str)
                and row["classification_source_confidence"] in CLASSIFICATION_SOURCE_CONFIDENCE_VALUES,
                f"{paper_id} has invalid classification_source_confidence: {row.get('classification_source_confidence')!r}",
            )
            assert_true(
                isinstance(row.get("classification_parser_rule"), str)
                and row["classification_parser_rule"] in CLASSIFICATION_PARSER_RULE_VALUES,
                f"{paper_id} has invalid classification_parser_rule: {row.get('classification_parser_rule')!r}",
            )
            if row["classification_parser_rule"] == "needs_review":
                assert_true(
                    row["classification_source_confidence"] == "low",
                    f"{paper_id} needs_review classification trace must use source_confidence=low",
                )
            if row["classification_parser_rule"] == "structured_remark_token":
                assert_true(
                    row["classification_source_field"] == "Remarks",
                    f"{paper_id} structured_remark_token classification trace must use source_field=Remarks",
                )
                assert_true(
                    row["classification_source_confidence"] == "high",
                    f"{paper_id} structured_remark_token classification trace must use source_confidence=high",
                )
            if row["last_reviewed_at"]:
                assert_true(
                    re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", row["last_reviewed_at"]) is not None,
                    f"{paper_id} has invalid last_reviewed_at: {row['last_reviewed_at']!r}",
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
                    primary_module == "",
                    f"{paper_id} pure general-method rows should not force primary_module_for_filing",
                )
                assert_true(
                    row["primary_module_confidence"] == "",
                    f"{paper_id} pure general-method rows should not carry primary_module_confidence",
                )
                assert_true(
                    row["primary_module_assignment_rule"] == "",
                    f"{paper_id} pure general-method rows should not carry primary_module_assignment_rule",
                )
                assert_true(
                    row["primary_module_override_reason"] == "",
                    f"{paper_id} pure general-method rows should not carry primary_module_override_reason",
                )
            elif modules:
                assert_true(
                    row["primary_module_confidence"] in PRIMARY_MODULE_CONFIDENCE_VALUES,
                    f"{paper_id} has invalid primary_module_confidence: {row['primary_module_confidence']!r}",
                )
                assert_true(
                    row["primary_module_assignment_rule"] in PRIMARY_MODULE_ASSIGNMENT_RULE_VALUES,
                    f"{paper_id} has invalid primary_module_assignment_rule: {row['primary_module_assignment_rule']!r}",
                )
                expected_mode = "multi_module" if len(modules) > 1 else "single_module"
                assert_true(
                    object_coverage_mode == expected_mode,
                    f"{paper_id} has inconsistent object_coverage_mode {object_coverage_mode!r} for modules {modules}",
                )
                assert_true(
                    primary_module in modules or primary_module == row["legacy_main_class"],
                    f"{paper_id} primary_module_for_filing {primary_module!r} is neither in scientific_object_modules {modules} nor equal to legacy_main_class {row['legacy_main_class']!r}",
                )
                if len(modules) == 1:
                    assert_true(
                        row["primary_module_confidence"] == "high",
                        f"{paper_id} single-module rows should use primary_module_confidence=high",
                    )
                    assert_true(
                        row["primary_module_assignment_rule"] == "main_scientific_object",
                        f"{paper_id} single-module rows should use primary_module_assignment_rule=main_scientific_object",
                    )
                    assert_true(
                        row["primary_module_override_reason"] == "",
                        f"{paper_id} single-module rows should not carry primary_module_override_reason",
                    )
                elif row["primary_module_assignment_rule"] == "manual_override":
                    assert_true(
                        bool(row["primary_module_override_reason"]),
                        f"{paper_id} manual_override primary module rows must carry primary_module_override_reason",
                    )

            if row["active_confirmed_core"]:
                assert_true(
                    row["record_status"] == "active_confirmed_core",
                    f"{paper_id} active_confirmed_core rows must use record_status=active_confirmed_core",
                )
                assert_true(
                    row["inclusion_decision"] == "confirmed_core",
                    f"{paper_id} active_confirmed_core rows must use inclusion_decision=confirmed_core",
                )
            elif row["inclusion_status"] == "background_only":
                assert_true(
                    row["record_status"] == "background_only",
                    f"{paper_id} background_only rows must use record_status=background_only",
                )
            elif row["inclusion_status"] == "excluded":
                assert_true(
                    row["record_status"] == "excluded",
                    f"{paper_id} excluded rows must use record_status=excluded",
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
            if expected_primary_module and general_bucket == "none":
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

        validate_authoritative_sources(papers)
        validate_registry_layer(
            papers=papers,
            taxonomy_index=taxonomy_index,
            require_registry=require_registry,
        )
        final_modules_mirror_drifts = collect_final_modules_mirror_drifts(papers)
        semantic_drift_ids = [
            drift["paper_id"]
            for drift in final_modules_mirror_drifts
            if drift["drift_kind"] == "semantic_drift"
        ]
        order_drift_ids = [
            drift["paper_id"]
            for drift in final_modules_mirror_drifts
            if drift["drift_kind"] == "order_drift"
        ]

        findings = collect_non_blocking_findings(
            papers=papers,
            classification_code_index=classification_code_index,
            discipline_code_assignments=discipline_code_assignments,
            discipline_local_code_registry=discipline_local_code_registry,
        )
        write_integrity_check_report(findings=findings, status="passed")

        print(f"papers.jsonl records: {len(papers)}")
        print(f"active confirmed-core: {len(active)}")
        print(f"active local PDFs: {len(active_local_pdf)}")
        print(f"active no-local-PDF: {len(active_no_local_pdf)}")
        print(
            "workflow mirror drift count "
            f"(progress final_modules_or_bucket vs canonical derived classification): {len(final_modules_mirror_drifts)}"
        )
        print(
            "workflow mirror semantic drift count: "
            f"{len(semantic_drift_ids)}"
            + (f" [{', '.join(semantic_drift_ids)}]" if semantic_drift_ids else "")
        )
        print(
            "workflow mirror order drift count: "
            f"{len(order_drift_ids)}"
            + (f" [{', '.join(order_drift_ids)}]" if order_drift_ids else "")
        )
        print(f"integrity check report: {INTEGRITY_CHECK_REPORT_PATH}")
        print("All structured-data consistency checks passed.")
    except AssertionError as exc:
        add_finding(
            findings,
            severity="ERROR",
            category="other",
            code="CHECK_ABORTED",
            message=str(exc),
            owner_file="See assertion context in check_data_consistency.py",
        )
        write_integrity_check_report(findings=findings, status="failed")
        raise


if __name__ == "__main__":
    main()
