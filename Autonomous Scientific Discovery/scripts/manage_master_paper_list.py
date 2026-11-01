#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from copy import deepcopy
from datetime import datetime
from pathlib import Path
import re
from typing import Dict, List, Tuple

from append_change_log import (
    append_row as append_change_log_row,
    current_commit,
    load_rows as load_change_log_rows,
    next_change_id,
)
from export_structured_data import (
    MASTER_HEADER,
    MASTER_PATH,
    is_markdown_separator,
    read_text_lossy,
    split_markdown_row,
)


ROOT = Path(__file__).resolve().parent.parent
MASTER_COLUMNS = tuple(column for column in MASTER_HEADER if column != "ID")
DATE_PATTERN = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
CLASSIFICATION_FIELDS = {"Main class", "Secondary class", "Tertiary class", "Remarks"}
LIFECYCLE_FIELDS = {"Inclusion status", "Exclusion reason"}
METADATA_FIELDS = {"Paper title", "Authors", "Year", "Source", "DOI / arXiv / URL"}
SUPPORTING_PATH_FIELDS = {"PDF path", "Note path"}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Update one row in the master owner file Paper_Lists/agent_master_paper_list.md "
            "and append one matching audit row to Data/change_log.jsonl."
        )
    )
    parser.add_argument("--paper-id", required=True)
    parser.add_argument(
        "--set",
        action="append",
        default=[],
        help=(
            "Repeatable column update in the form column=value. "
            f"Allowed columns: {', '.join(MASTER_COLUMNS)}"
        ),
    )
    parser.add_argument("--reason", required=True, help="Human-readable change_log reason.")
    parser.add_argument(
        "--changed-at",
        default=datetime.now().strftime("%Y-%m-%d"),
        help="change_log changed_at date in YYYY-MM-DD format.",
    )
    parser.add_argument(
        "--changed-by",
        default="codex",
        help="change_log changed_by value. Default: codex",
    )
    parser.add_argument(
        "--related-commit",
        default="",
        help="Optional related_commit override for the appended change_log row.",
    )
    parser.add_argument(
        "--change-type",
        default="",
        help=(
            "Optional change_log change_type override. "
            "If omitted, the helper derives a semantic default from the changed master fields."
        ),
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview the owner-row update and change_log row without writing files.",
    )
    return parser


def parse_updates(raw_updates: List[str]) -> Dict[str, str]:
    if not raw_updates:
        raise SystemExit("At least one --set column=value update is required.")
    updates: Dict[str, str] = {}
    allowed = set(MASTER_COLUMNS)
    for raw in raw_updates:
        if "=" not in raw:
            raise SystemExit(f"--set must use column=value form: {raw!r}")
        column, value = raw.split("=", 1)
        normalized_column = column.strip()
        if normalized_column not in allowed:
            raise SystemExit(
                f"Unsupported master column {normalized_column!r}. "
                f"Allowed columns: {', '.join(MASTER_COLUMNS)}"
            )
        updates[normalized_column] = value.strip()
    return updates


def ensure_date(value: str) -> str:
    normalized = value.strip()
    if not DATE_PATTERN.fullmatch(normalized):
        raise SystemExit(f"--changed-at must be YYYY-MM-DD: {value!r}")
    return normalized


def derive_change_type(changed_fields: List[str]) -> str:
    changed = set(changed_fields)
    if changed and changed.issubset(CLASSIFICATION_FIELDS):
        return "classification_fact_update"
    if changed and changed.issubset(LIFECYCLE_FIELDS):
        return "record_status_update"
    if changed and changed.issubset(METADATA_FIELDS):
        return "master_metadata_update"
    if changed and changed.issubset(SUPPORTING_PATH_FIELDS):
        return "master_path_update"
    if changed == {"Citation priority"}:
        return "citation_priority_update"
    if changed == {"Evidence strength"}:
        return "evidence_strength_update"
    return "master_owner_update"


def parse_master_table() -> Tuple[List[str], int, List[Dict[str, str]]]:
    lines = read_text_lossy(MASTER_PATH).splitlines()
    header_marker = "| " + " | ".join(MASTER_HEADER) + " |"
    start_index = None
    for index, line in enumerate(lines):
        if line.strip() == header_marker:
            start_index = index
            break
    if start_index is None:
        raise SystemExit(f"Header marker not found in {MASTER_PATH}")

    data_start = start_index + 1
    if data_start < len(lines) and is_markdown_separator(lines[data_start]):
        data_start += 1

    rows: List[Dict[str, str]] = []
    for line in lines[data_start:]:
        if not line.startswith("| ASD-"):
            if rows:
                continue
            continue
        parts = split_markdown_row(line, len(MASTER_HEADER))
        rows.append(dict(zip(MASTER_HEADER, parts)))
    return lines, start_index, rows


def format_markdown_row(row: Dict[str, str]) -> str:
    cells = [str(row.get(column, "")).strip() for column in MASTER_HEADER]
    return "| " + " | ".join(cells) + " |"


def rebuild_master_file(lines: List[str], header_index: int, rows: List[Dict[str, str]]) -> str:
    data_start = header_index + 1
    if data_start < len(lines) and is_markdown_separator(lines[data_start]):
        data_start += 1

    data_line_indexes = [
        idx for idx, line in enumerate(lines[data_start:], start=data_start) if line.startswith("| ASD-")
    ]
    rebuilt_lines = list(lines)
    formatted_rows = [format_markdown_row(row) for row in rows]

    if len(data_line_indexes) != len(formatted_rows):
        raise SystemExit(
            "Master owner rewrite safety check failed: parsed row count does not match source row count."
        )

    for index, formatted in zip(data_line_indexes, formatted_rows):
        rebuilt_lines[index] = formatted
    return "\n".join(rebuilt_lines) + "\n"


def build_change_log_row(
    *,
    paper_id: str,
    changed_at: str,
    changed_by: str,
    change_type: str,
    reason: str,
    related_commit: str,
    old_value: Dict[str, str],
    new_value: Dict[str, str],
) -> Dict[str, object]:
    existing_rows = load_change_log_rows()
    return {
        "change_id": next_change_id(existing_rows),
        "paper_id": paper_id,
        "changed_at": changed_at,
        "changed_by": changed_by,
        "change_type": change_type,
        "old_value": old_value,
        "new_value": new_value,
        "reason": reason,
        "related_commit": related_commit,
    }


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    paper_id = args.paper_id.strip()
    updates = parse_updates(args.set)
    reason = args.reason.strip()
    changed_at = ensure_date(args.changed_at)
    if not paper_id:
        raise SystemExit("--paper-id must be non-empty.")
    if not reason:
        raise SystemExit("--reason must be non-empty.")

    lines, header_index, rows = parse_master_table()
    row_index = next((index for index, row in enumerate(rows) if row["ID"] == paper_id), None)
    if row_index is None:
        raise SystemExit(f"paper_id not found in master owner file: {paper_id}")

    original_row = rows[row_index]
    updated_row = deepcopy(original_row)
    changed_old: Dict[str, str] = {}
    changed_new: Dict[str, str] = {}
    for column, new_value in updates.items():
        old_value = str(original_row.get(column, ""))
        if old_value != new_value:
            changed_old[column] = old_value
            changed_new[column] = new_value
            updated_row[column] = new_value

    if not changed_new:
        print("No master owner changes required.")
        return

    rows[row_index] = updated_row
    new_text = rebuild_master_file(lines, header_index, rows)
    related_commit = args.related_commit.strip() or current_commit()
    change_type = args.change_type.strip() or derive_change_type(sorted(changed_new))
    change_log_row = build_change_log_row(
        paper_id=paper_id,
        changed_at=changed_at,
        changed_by=args.changed_by.strip() or "codex",
        change_type=change_type,
        reason=reason,
        related_commit=related_commit,
        old_value=changed_old,
        new_value=changed_new,
    )

    print(f"paper_id: {paper_id}")
    print(f"Changed fields: {', '.join(sorted(changed_new))}")
    print("Old values:")
    print(json.dumps(changed_old, ensure_ascii=False, indent=2))
    print("New values:")
    print(json.dumps(changed_new, ensure_ascii=False, indent=2))
    print(f"Planned change_log row: {change_log_row['change_id']} {change_log_row['change_type']}")

    if args.dry_run:
        print("Dry run only; no files written.")
        return

    MASTER_PATH.write_text(new_text, encoding="utf-8", newline="\n")
    append_change_log_row(change_log_row)
    print(f"Wrote {MASTER_PATH}")
    print(f"Appended {change_log_row['change_id']} to {ROOT / 'Data' / 'change_log.jsonl'}")


if __name__ == "__main__":
    main()
