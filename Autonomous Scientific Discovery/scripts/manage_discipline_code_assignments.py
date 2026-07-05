#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from copy import deepcopy
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Tuple

from append_change_log import (
    append_row as append_change_log_row,
    current_commit,
    load_rows as load_change_log_rows,
    next_change_id,
)
from export_structured_data import (
    CHANGE_LOG_PATH,
    DISCIPLINE_CODE_ASSIGNMENTS_PATH,
    MASTER_HEADER,
    MASTER_PATH,
    PROGRESS_HEADER,
    PROGRESS_PATH,
    build_latest_change_log_index,
    build_papers,
    load_classification_code_index,
    load_jsonl_rows,
    parse_markdown_table,
)


ROOT = Path(__file__).resolve().parent.parent
LEDGER_PATH = DISCIPLINE_CODE_ASSIGNMENTS_PATH

ASSIGNMENT_ID_PATTERN = re.compile(r"^DCA-[0-9]{6}$")
DISCIPLINE_CODE_PATTERN = re.compile(r"^[0-9]{2}-[0-9]{2}-[0-9]{3}$")
PRIMARY_TAXONOMY_2LVL_PATTERN = re.compile(r"^[0-9]{2}\.[0-9]{2}$")
PAPER_ID_PATTERN = re.compile(r"^ASD-[0-9]{4}$")
DATE_PATTERN = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")

STATUS_ACTIVE = "active_code"
STATUS_RETIRED = "retired_code"
STATUS_REDIRECTED = "redirected_code"
STATUS_PENDING = "pending_secondary"
STATUS_GENERAL_METHOD = "non_discipline_general_method"
CURRENT_STATUSES = {
    STATUS_ACTIVE,
    STATUS_PENDING,
    STATUS_GENERAL_METHOD,
}
HISTORICAL_STATUSES = {
    STATUS_RETIRED,
    STATUS_REDIRECTED,
}


def load_current_papers() -> Dict[str, Dict[str, object]]:
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
    change_log_rows = load_jsonl_rows(CHANGE_LOG_PATH) if CHANGE_LOG_PATH.exists() else []
    latest_change_log_by_paper_id = build_latest_change_log_index(change_log_rows)
    papers = build_papers(
        master_table.rows,
        progress_rows,
        latest_change_log_by_paper_id,
        load_classification_code_index(),
    )
    return {str(paper["paper_id"]): paper for paper in papers}


def load_ledger_rows() -> List[Dict[str, object]]:
    if not LEDGER_PATH.exists():
        raise SystemExit(
            "Data/discipline_code_assignments.jsonl is missing. "
            "Initialize the owner ledger first."
        )
    rows = load_jsonl_rows(LEDGER_PATH)
    if not rows:
        raise SystemExit("Data/discipline_code_assignments.jsonl is empty.")
    return rows


def write_jsonl(path: Path, rows: List[Dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def next_assignment_id(rows: List[Dict[str, object]]) -> str:
    max_seen = 0
    for row in rows:
        assignment_id = str(row.get("assignment_id") or "")
        if ASSIGNMENT_ID_PATTERN.fullmatch(assignment_id):
            max_seen = max(max_seen, int(assignment_id[4:]))
    return f"DCA-{max_seen + 1:06d}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Maintain Data/discipline_code_assignments.jsonl as the stable owner ledger. "
            "This command updates the owner ledger directly and appends one change-log row "
            "for the affected paper unless --dry-run is used."
        )
    )
    parser.add_argument("--paper-id", required=True, help="Permanent ASD paper ID.")
    parser.add_argument(
        "--target-status",
        required=True,
        choices=sorted(CURRENT_STATUSES),
        help="The desired current snapshot status for this paper.",
    )
    parser.add_argument(
        "--assignment-reason",
        required=True,
        help="assignment_reason value for the new current row.",
    )
    parser.add_argument(
        "--change-reason",
        required=True,
        help="Human-readable audit reason written to Data/change_log.jsonl.",
    )
    parser.add_argument(
        "--effective-date",
        default=datetime.now().strftime("%Y-%m-%d"),
        help="Date written to assigned_at / retired_at as YYYY-MM-DD.",
    )
    parser.add_argument(
        "--changed-by",
        default="codex",
        help="Actor name for the ledger update and change log. Default: codex",
    )
    parser.add_argument(
        "--assigned-by",
        default="",
        help="assigned_by override for the new current row. Defaults to --changed-by.",
    )
    parser.add_argument(
        "--primary-taxonomy-code-2lvl",
        default="",
        help=(
            "Explicit secondary taxonomy code for active_code targets. "
            "Defaults to the current owner-derived legacy_secondary_class."
        ),
    )
    parser.add_argument(
        "--discipline-local-code",
        default="",
        help=(
            "Explicit discipline_local_code for active_code targets. "
            "Defaults to the next unused code in the chosen secondary bucket."
        ),
    )
    parser.add_argument(
        "--pending-reason",
        default="",
        help="Required for pending_secondary targets; must stay blank otherwise.",
    )
    parser.add_argument(
        "--close-current-as",
        default=None,
        choices=[STATUS_RETIRED, STATUS_REDIRECTED],
        help=(
            "Required when the current snapshot row is active_code and must be closed "
            "before appending a new current row."
        ),
    )
    parser.add_argument(
        "--related-commit",
        default="",
        help="Optional related_commit override for the appended change-log row.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview the ledger update and change-log payload without writing files.",
    )
    return parser.parse_args()


def ensure_date(value: str, label: str) -> str:
    normalized = value.strip()
    if not DATE_PATTERN.fullmatch(normalized):
        raise SystemExit(f"{label} must be YYYY-MM-DD: {value!r}")
    return normalized


def ensure_known_active_core_paper(
    papers_by_id: Dict[str, Dict[str, object]],
    paper_id: str,
) -> Dict[str, object]:
    if not PAPER_ID_PATTERN.fullmatch(paper_id):
        raise SystemExit(f"Invalid paper_id: {paper_id!r}")
    paper = papers_by_id.get(paper_id)
    if paper is None:
        raise SystemExit(f"Unknown paper_id in current owner snapshot: {paper_id}")
    if not bool(paper.get("active_confirmed_core")):
        raise SystemExit(
            f"{paper_id} is not active_confirmed_core in the current owner snapshot. "
            "This maintenance helper currently stays aligned to the active confirmed-core baseline."
        )
    return paper


def get_current_row_info(
    ledger_rows: List[Dict[str, object]],
    paper_id: str,
) -> Tuple[List[int], int | None]:
    paper_indices: List[int] = []
    current_index: int | None = None
    current_count = 0
    for index, row in enumerate(ledger_rows):
        if str(row.get("paper_id")) != paper_id:
            continue
        paper_indices.append(index)
        if str(row.get("assignment_status")) in CURRENT_STATUSES:
            current_index = index
            current_count += 1
    if current_count > 1:
        raise SystemExit(
            f"{paper_id} has {current_count} current snapshot rows in the ledger; "
            "repair the owner file before continuing."
        )
    return paper_indices, current_index


def load_secondary_codes() -> set[str]:
    payload = load_classification_code_index()
    return {
        str(code)
        for code in dict(payload.get("secondary_code_to_label") or {}).keys()
    }


def normalize_string(value: object) -> str:
    return str(value).strip() if value is not None else ""


def require_active_target_fields(
    paper: Dict[str, object],
    explicit_secondary_code: str,
    known_secondary_codes: set[str],
) -> Tuple[str, str | None, str | None]:
    source_primary_module = normalize_string(paper.get("primary_module_for_filing")) or None
    source_legacy_secondary = normalize_string(paper.get("legacy_secondary_class")) or None
    secondary_code = explicit_secondary_code or (source_legacy_secondary or "")

    if source_primary_module is None:
        raise SystemExit(
            "Cannot assign active_code when primary_module_for_filing is blank in the current owner snapshot. "
            "Fix the owner facts first."
        )
    if not PRIMARY_TAXONOMY_2LVL_PATTERN.fullmatch(secondary_code):
        raise SystemExit(
            "active_code target requires a valid primary_taxonomy_code_2lvl. "
            "Provide --primary-taxonomy-code-2lvl or repair legacy_secondary_class in the owner facts."
        )
    if secondary_code not in known_secondary_codes:
        raise SystemExit(
            f"Secondary taxonomy code is not present in Data/classification_code_index.json: {secondary_code}"
        )
    secondary_primary = secondary_code.split(".", 1)[0]
    if secondary_primary != source_primary_module:
        raise SystemExit(
            "primary_taxonomy_code_2lvl does not match the current owner-derived "
            f"primary_module_for_filing: {secondary_code} vs {source_primary_module}"
        )
    return secondary_code, source_primary_module, source_legacy_secondary


def require_general_method_target(paper: Dict[str, object]) -> Tuple[str | None, str | None]:
    scientific_object_modules = list(paper.get("scientific_object_modules") or [])
    general_method_bucket = normalize_string(paper.get("general_method_bucket"))
    if scientific_object_modules or general_method_bucket == "none" or not general_method_bucket:
        raise SystemExit(
            "non_discipline_general_method target requires pure general-method owner facts: "
            "scientific_object_modules must be empty and general_method_bucket must be non-none."
        )
    return (
        normalize_string(paper.get("primary_module_for_filing")) or None,
        normalize_string(paper.get("legacy_secondary_class")) or None,
    )


def allocate_next_discipline_code(
    ledger_rows: List[Dict[str, object]],
    secondary_code: str,
) -> str:
    prefix = secondary_code.replace(".", "-") + "-"
    max_rank = 0
    for row in ledger_rows:
        discipline_local_code = row.get("discipline_local_code")
        if not isinstance(discipline_local_code, str):
            continue
        if not DISCIPLINE_CODE_PATTERN.fullmatch(discipline_local_code):
            continue
        if discipline_local_code.startswith(prefix):
            max_rank = max(max_rank, int(discipline_local_code.rsplit("-", 1)[-1]))
    return f"{secondary_code.replace('.', '-')}-{max_rank + 1:03d}"


def resolve_new_discipline_code(
    ledger_rows: List[Dict[str, object]],
    secondary_code: str,
    explicit_code: str,
) -> str:
    if explicit_code:
        normalized = explicit_code.strip()
        if not DISCIPLINE_CODE_PATTERN.fullmatch(normalized):
            raise SystemExit(f"Invalid --discipline-local-code: {explicit_code!r}")
        if normalized[:5] != secondary_code.replace(".", "-"):
            raise SystemExit(
                f"Explicit discipline_local_code does not match the chosen secondary code: "
                f"{normalized} vs {secondary_code}"
            )
        used_codes = {
            str(row["discipline_local_code"])
            for row in ledger_rows
            if isinstance(row.get("discipline_local_code"), str)
        }
        if normalized in used_codes:
            raise SystemExit(
                f"discipline_local_code is already present in the owner ledger and cannot be reused: {normalized}"
            )
        return normalized
    return allocate_next_discipline_code(ledger_rows, secondary_code)


def build_target_row(
    *,
    paper: Dict[str, object],
    target_status: str,
    assignment_reason: str,
    effective_date: str,
    assigned_by: str,
    explicit_secondary_code: str,
    explicit_discipline_code: str,
    pending_reason: str,
    known_secondary_codes: set[str],
    ledger_rows: List[Dict[str, object]],
) -> Dict[str, object]:
    if not assignment_reason.strip():
        raise SystemExit("--assignment-reason must be non-empty.")

    source_primary_module = normalize_string(paper.get("primary_module_for_filing")) or None
    source_legacy_secondary = normalize_string(paper.get("legacy_secondary_class")) or None

    target_row: Dict[str, object] = {
        "assignment_id": "",
        "paper_id": str(paper["paper_id"]),
        "discipline_local_code": None,
        "primary_taxonomy_code_2lvl": None,
        "assignment_status": target_status,
        "assigned_at": effective_date,
        "assigned_by": assigned_by,
        "retired_at": None,
        "redirected_to_code": None,
        "assignment_reason": assignment_reason.strip(),
        "pending_reason": None,
        "source_primary_module_for_filing": source_primary_module,
        "source_legacy_secondary_class": source_legacy_secondary,
        "schema_version": 1,
    }

    if target_status == STATUS_ACTIVE:
        if pending_reason.strip():
            raise SystemExit("active_code target must not carry --pending-reason.")
        secondary_code, source_primary_module, source_legacy_secondary = require_active_target_fields(
            paper=paper,
            explicit_secondary_code=explicit_secondary_code.strip(),
            known_secondary_codes=known_secondary_codes,
        )
        target_row["primary_taxonomy_code_2lvl"] = secondary_code
        target_row["discipline_local_code"] = resolve_new_discipline_code(
            ledger_rows=ledger_rows,
            secondary_code=secondary_code,
            explicit_code=explicit_discipline_code.strip(),
        )
        target_row["source_primary_module_for_filing"] = source_primary_module
        target_row["source_legacy_secondary_class"] = source_legacy_secondary
    elif target_status == STATUS_PENDING:
        if explicit_secondary_code.strip():
            raise SystemExit("pending_secondary target must not carry --primary-taxonomy-code-2lvl.")
        if explicit_discipline_code.strip():
            raise SystemExit("pending_secondary target must not carry --discipline-local-code.")
        if not pending_reason.strip():
            raise SystemExit("pending_secondary target requires non-empty --pending-reason.")
        target_row["pending_reason"] = pending_reason.strip()
    else:
        if explicit_secondary_code.strip():
            raise SystemExit(
                "non_discipline_general_method target must not carry --primary-taxonomy-code-2lvl."
            )
        if explicit_discipline_code.strip():
            raise SystemExit(
                "non_discipline_general_method target must not carry --discipline-local-code."
            )
        if pending_reason.strip():
            raise SystemExit(
                "non_discipline_general_method target must not carry --pending-reason."
            )
        source_primary_module, source_legacy_secondary = require_general_method_target(paper)
        target_row["source_primary_module_for_filing"] = source_primary_module
        target_row["source_legacy_secondary_class"] = source_legacy_secondary

    return target_row


def validate_ledger_rows(
    ledger_rows: List[Dict[str, object]],
    papers_by_id: Dict[str, Dict[str, object]],
) -> None:
    seen_assignment_ids: set[str] = set()
    seen_codes: Dict[str, str] = {}
    active_codes: Dict[str, str] = {}
    current_rows_by_paper: Dict[str, int] = {}

    for index, row in enumerate(ledger_rows, start=1):
        assignment_id = normalize_string(row.get("assignment_id"))
        paper_id = normalize_string(row.get("paper_id"))
        assignment_status = normalize_string(row.get("assignment_status"))
        discipline_local_code = row.get("discipline_local_code")
        primary_taxonomy_code_2lvl = row.get("primary_taxonomy_code_2lvl")
        redirected_to_code = row.get("redirected_to_code")
        assigned_at = normalize_string(row.get("assigned_at"))
        assigned_by = normalize_string(row.get("assigned_by"))
        assignment_reason = normalize_string(row.get("assignment_reason"))
        pending_reason = row.get("pending_reason")

        if not ASSIGNMENT_ID_PATTERN.fullmatch(assignment_id):
            raise SystemExit(f"Ledger row {index} has invalid assignment_id: {assignment_id!r}")
        if assignment_id in seen_assignment_ids:
            raise SystemExit(f"Duplicate assignment_id in ledger: {assignment_id}")
        seen_assignment_ids.add(assignment_id)

        if not PAPER_ID_PATTERN.fullmatch(paper_id) or paper_id not in papers_by_id:
            raise SystemExit(f"Ledger row {index} has unknown paper_id: {paper_id!r}")
        if assignment_status not in CURRENT_STATUSES | HISTORICAL_STATUSES:
            raise SystemExit(
                f"Ledger row {index} has invalid assignment_status: {assignment_status!r}"
            )
        if not DATE_PATTERN.fullmatch(assigned_at):
            raise SystemExit(f"Ledger row {index} has invalid assigned_at: {assigned_at!r}")
        if not assigned_by:
            raise SystemExit(f"Ledger row {index} is missing assigned_by.")
        if not assignment_reason:
            raise SystemExit(f"Ledger row {index} is missing assignment_reason.")

        if assignment_status in CURRENT_STATUSES:
            current_rows_by_paper[paper_id] = current_rows_by_paper.get(paper_id, 0) + 1

        if assignment_status in {STATUS_ACTIVE, STATUS_RETIRED, STATUS_REDIRECTED}:
            if not isinstance(discipline_local_code, str) or not DISCIPLINE_CODE_PATTERN.fullmatch(
                discipline_local_code
            ):
                raise SystemExit(
                    f"Ledger row {index} requires a valid discipline_local_code for {assignment_status}."
                )
            if not isinstance(primary_taxonomy_code_2lvl, str) or not PRIMARY_TAXONOMY_2LVL_PATTERN.fullmatch(
                primary_taxonomy_code_2lvl
            ):
                raise SystemExit(
                    f"Ledger row {index} requires a valid primary_taxonomy_code_2lvl for {assignment_status}."
                )
            previous_owner = seen_codes.get(discipline_local_code)
            if previous_owner is not None:
                raise SystemExit(
                    "discipline_local_code must remain globally unique across active and historical rows: "
                    f"{discipline_local_code} already used by {previous_owner}"
                )
            seen_codes[discipline_local_code] = assignment_id
            if discipline_local_code[:5] != primary_taxonomy_code_2lvl.replace(".", "-"):
                raise SystemExit(
                    f"Ledger row {index} has mismatched discipline_local_code and primary_taxonomy_code_2lvl."
                )
            if assignment_status == STATUS_ACTIVE:
                active_codes[discipline_local_code] = assignment_id
            if pending_reason is not None:
                raise SystemExit(
                    f"Ledger row {index} must not carry pending_reason for {assignment_status}."
                )
        else:
            if discipline_local_code is not None:
                raise SystemExit(
                    f"Ledger row {index} must not carry discipline_local_code for {assignment_status}."
                )
            if primary_taxonomy_code_2lvl is not None:
                raise SystemExit(
                    f"Ledger row {index} must not carry primary_taxonomy_code_2lvl for {assignment_status}."
                )
            if assignment_status == STATUS_PENDING:
                if not isinstance(pending_reason, str) or not pending_reason.strip():
                    raise SystemExit(f"Ledger row {index} pending_secondary is missing pending_reason.")
            elif pending_reason is not None:
                raise SystemExit(
                    f"Ledger row {index} non_discipline_general_method must not carry pending_reason."
                )

        retired_at = row.get("retired_at")
        if assignment_status in HISTORICAL_STATUSES:
            if not isinstance(retired_at, str) or not DATE_PATTERN.fullmatch(retired_at):
                raise SystemExit(
                    f"Ledger row {index} historical status requires valid retired_at."
                )
        elif retired_at is not None:
            raise SystemExit(
                f"Ledger row {index} current snapshot status must not carry retired_at."
            )

        if assignment_status == STATUS_REDIRECTED:
            if not isinstance(redirected_to_code, str) or not DISCIPLINE_CODE_PATTERN.fullmatch(
                redirected_to_code
            ):
                raise SystemExit(
                    f"Ledger row {index} redirected_code requires valid redirected_to_code."
                )
        elif redirected_to_code is not None:
            raise SystemExit(
                f"Ledger row {index} non-redirected status must not carry redirected_to_code."
            )

    for paper_id, count in current_rows_by_paper.items():
        if count != 1:
            raise SystemExit(
                f"{paper_id} must have exactly one current snapshot row, found {count}."
            )

    for row in ledger_rows:
        if row["assignment_status"] == STATUS_REDIRECTED:
            redirected_to_code = str(row["redirected_to_code"])
            if redirected_to_code not in active_codes:
                raise SystemExit(
                    "redirected_to_code must point to an active discipline_local_code: "
                    f"{redirected_to_code}"
                )


def build_change_log_row(
    *,
    paper_id: str,
    changed_at: str,
    changed_by: str,
    change_type: str,
    reason: str,
    old_rows: List[Dict[str, object]],
    new_rows: List[Dict[str, object]],
    related_commit: str,
) -> Dict[str, object]:
    existing_rows = load_change_log_rows()
    return {
        "change_id": next_change_id(existing_rows),
        "paper_id": paper_id,
        "changed_at": changed_at,
        "changed_by": changed_by,
        "change_type": change_type,
        "old_value": {"discipline_code_rows": old_rows},
        "new_value": {"discipline_code_rows": new_rows},
        "reason": reason,
        "related_commit": related_commit,
    }


def summarize_row(row: Dict[str, object]) -> str:
    return (
        f"{row['assignment_id']} "
        f"{row['assignment_status']} "
        f"code={row['discipline_local_code'] or 'null'} "
        f"secondary={row['primary_taxonomy_code_2lvl'] or 'null'} "
        f"pending={row['pending_reason'] or 'null'}"
    )


def main() -> None:
    args = parse_args()
    paper_id = args.paper_id.strip()
    effective_date = ensure_date(args.effective_date, "--effective-date")
    changed_by = args.changed_by.strip() or "codex"
    assigned_by = args.assigned_by.strip() or changed_by

    papers_by_id = load_current_papers()
    paper = ensure_known_active_core_paper(papers_by_id, paper_id)
    known_secondary_codes = load_secondary_codes()
    ledger_rows = load_ledger_rows()
    paper_indices, current_index = get_current_row_info(ledger_rows, paper_id)
    old_rows = [deepcopy(ledger_rows[index]) for index in paper_indices]

    target_row = build_target_row(
        paper=paper,
        target_status=args.target_status,
        assignment_reason=args.assignment_reason,
        effective_date=effective_date,
        assigned_by=assigned_by,
        explicit_secondary_code=args.primary_taxonomy_code_2lvl,
        explicit_discipline_code=args.discipline_local_code,
        pending_reason=args.pending_reason,
        known_secondary_codes=known_secondary_codes,
        ledger_rows=ledger_rows,
    )

    if current_index is None:
        target_row["assignment_id"] = next_assignment_id(ledger_rows)
        ledger_rows.append(target_row)
        change_type = "discipline_code_assignment_add_current"
    else:
        current_row = deepcopy(ledger_rows[current_index])
        current_status = str(current_row["assignment_status"])
        if current_status in {STATUS_PENDING, STATUS_GENERAL_METHOD}:
            target_row["assignment_id"] = str(current_row["assignment_id"])
            ledger_rows[current_index] = target_row
            change_type = "discipline_code_assignment_update_current"
        elif current_status == STATUS_ACTIVE:
            if not args.close_current_as:
                raise SystemExit(
                    "Current snapshot row is active_code. Provide --close-current-as "
                    "retired_code or redirected_code before appending a new current row."
                )
            if args.target_status != STATUS_ACTIVE and args.close_current_as == STATUS_REDIRECTED:
                raise SystemExit(
                    "redirected_code requires a new active_code target so redirected_to_code can point to it."
                )
            if args.target_status == STATUS_ACTIVE and (
                target_row["discipline_local_code"] == current_row["discipline_local_code"]
            ):
                raise SystemExit(
                    "Reassigning from active_code requires a new discipline_local_code; "
                    "the old code cannot be reused."
                )
            historical_row = deepcopy(current_row)
            historical_row["assignment_status"] = args.close_current_as
            historical_row["retired_at"] = effective_date
            if args.close_current_as == STATUS_REDIRECTED:
                historical_row["redirected_to_code"] = target_row["discipline_local_code"]
            else:
                historical_row["redirected_to_code"] = None
            ledger_rows[current_index] = historical_row
            target_row["assignment_id"] = next_assignment_id(ledger_rows)
            ledger_rows.append(target_row)
            change_type = "discipline_code_assignment_reassign_current"
        else:
            raise SystemExit(
                f"Unsupported current assignment_status for maintenance: {current_status!r}"
            )

    validate_ledger_rows(ledger_rows, papers_by_id)
    new_rows = [
        deepcopy(row)
        for row in ledger_rows
        if str(row.get("paper_id")) == paper_id
    ]
    if old_rows == new_rows:
        print(f"No owner changes required for {paper_id}.")
        return

    related_commit = args.related_commit.strip() or current_commit()
    change_log_row = build_change_log_row(
        paper_id=paper_id,
        changed_at=effective_date,
        changed_by=changed_by,
        change_type=change_type,
        reason=args.change_reason.strip(),
        old_rows=old_rows,
        new_rows=new_rows,
        related_commit=related_commit,
    )

    print(f"Paper: {paper_id}")
    print("Old rows:")
    for row in old_rows:
        print("  " + summarize_row(row))
    print("New rows:")
    for row in new_rows:
        print("  " + summarize_row(row))
    print(f"Change log: {change_log_row['change_id']} {change_type}")

    if args.dry_run:
        print("Dry run only; no files written.")
        return

    write_jsonl(LEDGER_PATH, ledger_rows)
    append_change_log_row(change_log_row)
    print(f"Wrote {LEDGER_PATH}")
    print(f"Appended {change_log_row['change_id']} to {ROOT / 'Data' / 'change_log.jsonl'}")


if __name__ == "__main__":
    main()
