#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List


ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "Data"
PREVIEW_PATH = DATA_DIR / "discipline_code_initial_assignment_preview.csv"
LEDGER_PATH = DATA_DIR / "discipline_code_assignments.jsonl"

ASSIGNMENT_ID_PATTERN = "DCA-{index:06d}"
DISCIPLINE_CODE_PATTERN = re.compile(r"^[0-9]{2}-[0-9]{2}-[0-9]{3}$")
PRIMARY_TAXONOMY_2LVL_PATTERN = re.compile(r"^[0-9]{2}\.[0-9]{2}$")
PAPER_ID_PATTERN = re.compile(r"^ASD-[0-9]{4}$")
STATUS_ACTIVE = "active_code"
STATUS_PENDING = "pending_secondary"
STATUS_GENERAL_METHOD = "non_discipline_general_method"
ALLOWED_STATUSES = {
    STATUS_ACTIVE,
    STATUS_PENDING,
    STATUS_GENERAL_METHOD,
}
DATE_PATTERN = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")


def load_preview_rows() -> List[Dict[str, str]]:
    with PREVIEW_PATH.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError(f"Preview is empty: {PREVIEW_PATH}")
    return rows


def split_review_flags(value: str) -> List[str]:
    return [item.strip() for item in value.split(";") if item.strip()]


def derive_rank_from_code(code: str) -> str:
    return code.rsplit("-", 1)[-1]


def validate_preview_rows(
    rows: List[Dict[str, str]],
    strict_review: bool,
) -> Dict[str, int]:
    seen_paper_ids = set()
    active_codes = set()
    summary = {
        STATUS_ACTIVE: 0,
        STATUS_PENDING: 0,
        STATUS_GENERAL_METHOD: 0,
    }
    blocking_review_flags = {
        "secondary_not_in_taxonomy_index",
    }
    review_gate_hits: List[str] = []

    for row in rows:
        paper_id = row["paper_id"].strip()
        if not PAPER_ID_PATTERN.fullmatch(paper_id):
            raise ValueError(f"Invalid paper_id in preview: {paper_id!r}")
        if paper_id in seen_paper_ids:
            raise ValueError(f"Duplicate paper_id in preview: {paper_id}")
        seen_paper_ids.add(paper_id)

        status = row["proposed_assignment_status"].strip()
        if status not in ALLOWED_STATUSES:
            raise ValueError(
                f"{paper_id} has invalid proposed_assignment_status: {status!r}"
            )
        summary[status] += 1

        review_flags = split_review_flags(row["review_flags"])
        if strict_review:
            blocked = sorted(flag for flag in review_flags if flag in blocking_review_flags)
            if blocked:
                review_gate_hits.append(f"{paper_id}: {', '.join(blocked)}")

        discipline_local_code = row["proposed_discipline_local_code"].strip()
        discipline_local_rank = row["discipline_local_rank"].strip()
        primary_taxonomy_code_2lvl = row["proposed_primary_taxonomy_code_2lvl"].strip()
        pending_reason = row["pending_reason"].strip()

        if status == STATUS_ACTIVE:
            if not DISCIPLINE_CODE_PATTERN.fullmatch(discipline_local_code):
                raise ValueError(
                    f"{paper_id} active_code row missing valid proposed_discipline_local_code"
                )
            if discipline_local_code in active_codes:
                raise ValueError(
                    f"Duplicate active proposed_discipline_local_code in preview: {discipline_local_code}"
                )
            active_codes.add(discipline_local_code)
            if derive_rank_from_code(discipline_local_code) != discipline_local_rank:
                raise ValueError(
                    f"{paper_id} discipline_local_rank does not match proposed_discipline_local_code"
                )
            if not PRIMARY_TAXONOMY_2LVL_PATTERN.fullmatch(primary_taxonomy_code_2lvl):
                raise ValueError(
                    f"{paper_id} active_code row missing valid proposed_primary_taxonomy_code_2lvl"
                )
            if pending_reason:
                raise ValueError(f"{paper_id} active_code row should not carry pending_reason")
        elif status == STATUS_PENDING:
            if discipline_local_code:
                raise ValueError(
                    f"{paper_id} pending_secondary row must not carry proposed_discipline_local_code"
                )
            if discipline_local_rank:
                raise ValueError(
                    f"{paper_id} pending_secondary row must not carry discipline_local_rank"
                )
            if primary_taxonomy_code_2lvl:
                raise ValueError(
                    f"{paper_id} pending_secondary row must not carry proposed_primary_taxonomy_code_2lvl"
                )
            if not pending_reason:
                raise ValueError(f"{paper_id} pending_secondary row missing pending_reason")
        else:
            if discipline_local_code:
                raise ValueError(
                    f"{paper_id} non_discipline_general_method row must not carry proposed_discipline_local_code"
                )
            if discipline_local_rank:
                raise ValueError(
                    f"{paper_id} non_discipline_general_method row must not carry discipline_local_rank"
                )
            if primary_taxonomy_code_2lvl:
                raise ValueError(
                    f"{paper_id} non_discipline_general_method row must not carry proposed_primary_taxonomy_code_2lvl"
                )
            if pending_reason:
                raise ValueError(
                    f"{paper_id} non_discipline_general_method row must not carry pending_reason"
                )

    if review_gate_hits:
        joined = "\n".join(review_gate_hits)
        raise ValueError(
            "Review gate failed; preview still contains blocked review flags:\n" + joined
        )
    return summary


def build_ledger_rows(
    rows: List[Dict[str, str]],
    assigned_at: str,
    assigned_by: str,
) -> List[Dict[str, object]]:
    ledger_rows: List[Dict[str, object]] = []
    for index, row in enumerate(rows, start=1):
        status = row["proposed_assignment_status"].strip()
        discipline_local_code = row["proposed_discipline_local_code"].strip() or None
        primary_taxonomy_code_2lvl = (
            row["proposed_primary_taxonomy_code_2lvl"].strip() or None
        )
        pending_reason = row["pending_reason"].strip() or None
        source_primary_module_for_filing = row["primary_module_for_filing"].strip() or None
        source_legacy_secondary_class = row["legacy_secondary_class"].strip() or None

        ledger_rows.append(
            {
                "assignment_id": ASSIGNMENT_ID_PATTERN.format(index=index),
                "paper_id": row["paper_id"].strip(),
                "discipline_local_code": discipline_local_code,
                "primary_taxonomy_code_2lvl": primary_taxonomy_code_2lvl,
                "assignment_status": status,
                "assigned_at": assigned_at,
                "assigned_by": assigned_by,
                "retired_at": None,
                "redirected_to_code": None,
                "assignment_reason": "initial_assignment",
                "pending_reason": pending_reason,
                "source_primary_module_for_filing": source_primary_module_for_filing,
                "source_legacy_secondary_class": source_legacy_secondary_class,
                "schema_version": 1,
            }
        )
    return ledger_rows


def write_jsonl(path: Path, rows: List[Dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def ensure_date(value: str) -> str:
    normalized = value.strip()
    if not DATE_PATTERN.fullmatch(normalized):
        raise SystemExit(f"--assigned-at must be YYYY-MM-DD: {value!r}")
    return normalized


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Initialize Data/discipline_code_assignments.jsonl from the reviewed "
            "initial preview. This command is explicit owner initialization, not daily export."
        )
    )
    parser.add_argument(
        "--assigned-at",
        default=datetime.now().strftime("%Y-%m-%d"),
        help="Assignment date in YYYY-MM-DD format. Default: today",
    )
    parser.add_argument(
        "--assigned-by",
        default="codex",
        help="assigned_by value to write into the ledger. Default: codex",
    )
    parser.add_argument(
        "--allow-unreviewed-preview",
        action="store_true",
        help=(
            "Allow initialization even when preview rows still carry blocked review flags "
            "such as secondary_not_in_taxonomy_index. This should only be used for explicit "
            "controller-approved baseline initialization."
        ),
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite an existing discipline_code_assignments.jsonl owner file.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview ledger initialization without writing discipline_code_assignments.jsonl.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    assigned_at = ensure_date(args.assigned_at)
    if LEDGER_PATH.exists() and not args.overwrite:
        if not args.dry_run:
            raise SystemExit(
                "discipline_code_assignments.jsonl already exists. "
                "Refusing to overwrite without --overwrite."
            )

    preview_rows = load_preview_rows()
    summary = validate_preview_rows(
        preview_rows,
        strict_review=not args.allow_unreviewed_preview,
    )
    ledger_rows = build_ledger_rows(
        preview_rows,
        assigned_at=assigned_at,
        assigned_by=args.assigned_by,
    )

    print(f"Prepared {len(ledger_rows)} ledger rows from {PREVIEW_PATH}")
    for status, count in summary.items():
        print(f"{status}: {count}")
    if args.allow_unreviewed_preview:
        print("Initialized with --allow-unreviewed-preview.")
    if args.dry_run:
        print("Dry run only; no files written.")
        return

    write_jsonl(LEDGER_PATH, ledger_rows)
    print(f"Wrote {LEDGER_PATH}")


if __name__ == "__main__":
    main()
