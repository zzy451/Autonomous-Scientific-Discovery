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
from check_data_consistency import (
    CLASSIFICATION_CODE_INDEX_SCHEMA_PATH,
    validate_payload_against_schema_file,
)
from export_structured_data import MASTER_HEADER, MASTER_PATH, parse_markdown_table


ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "Data"
CLASSIFICATION_CODE_INDEX_PATH = DATA_DIR / "classification_code_index.json"

PRIMARY_CODE_PATTERN = re.compile(r"^(0[1-9]|1[0-1]|01\.04)$")
FORMAL_PRIMARY_CODE_PATTERN = re.compile(r"^(0[1-9]|1[0-1])$")
SECONDARY_CODE_PATTERN = re.compile(r"^[0-9]{2}\.[0-9]{2}$")
DATE_PATTERN = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
TERM_STATUS_VALUES = {"active", "deprecated", "needs_review"}
SECONDARY_REVIEW_STATUS_VALUES = {"unreviewed", "reviewed", "needs_split", "needs_merge"}


def load_payload() -> Dict[str, Any]:
    if not CLASSIFICATION_CODE_INDEX_PATH.exists():
        raise SystemExit(
            "Data/classification_code_index.json is missing. "
            "Initialize the taxonomy owner file before using this helper."
        )
    payload = json.loads(CLASSIFICATION_CODE_INDEX_PATH.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise SystemExit("classification_code_index.json must be a JSON object.")
    return payload


def write_payload(payload: Dict[str, Any]) -> None:
    CLASSIFICATION_CODE_INDEX_PATH.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Maintain Data/classification_code_index.json as the taxonomy vocabulary owner. "
            "This command updates the owner file directly and synchronizes mapping dictionaries "
            "from the term arrays."
        )
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    sync_parser = subparsers.add_parser(
        "sync",
        help="Normalize term ordering and synchronize mapping dictionaries from term arrays.",
    )
    add_common_write_args(sync_parser)

    primary_parser = subparsers.add_parser(
        "upsert-primary",
        help="Add or update one primary taxonomy term and resynchronize the owner file.",
    )
    primary_parser.add_argument("--primary-code", required=True)
    primary_parser.add_argument("--label", default="")
    primary_parser.add_argument("--definition", default="")
    primary_parser.add_argument("--include-json", default="")
    primary_parser.add_argument("--exclude-json", default="")
    primary_parser.add_argument("--status", choices=sorted(TERM_STATUS_VALUES), default="")
    primary_parser.add_argument("--source", default="")
    add_common_write_args(primary_parser)

    secondary_parser = subparsers.add_parser(
        "upsert-secondary",
        help="Add or update one secondary taxonomy term and resynchronize the owner file.",
    )
    secondary_parser.add_argument("--secondary-code", required=True)
    secondary_parser.add_argument("--parent-primary-code", default="")
    secondary_parser.add_argument("--label", default="")
    secondary_parser.add_argument("--definition", default="")
    secondary_parser.add_argument("--include-json", default="")
    secondary_parser.add_argument("--exclude-json", default="")
    secondary_parser.add_argument("--status", choices=sorted(TERM_STATUS_VALUES), default="")
    secondary_parser.add_argument(
        "--review-status",
        choices=sorted(SECONDARY_REVIEW_STATUS_VALUES),
        default="",
    )
    secondary_parser.add_argument("--source", default="")
    add_common_write_args(secondary_parser)

    return parser.parse_args()


def add_common_write_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--updated-at",
        default=datetime.now().strftime("%Y-%m-%d"),
        help="Owner updated_at date in YYYY-MM-DD format.",
    )
    parser.add_argument(
        "--updated-by",
        default="codex",
        help="Owner updated_by value. Default: codex",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview the owner-file changes without writing classification_code_index.json.",
    )
    parser.add_argument(
        "--append-change-log",
        action="store_true",
        help=(
            "Append per-paper audit rows to Data/change_log.jsonl for papers impacted by "
            "this taxonomy-owner update. For upsert-secondary, affected paper_ids default "
            "to master rows whose legacy Secondary class matches the updated code."
        ),
    )
    parser.add_argument(
        "--change-reason",
        default="",
        help="Human-readable audit reason written to Data/change_log.jsonl when --append-change-log is used.",
    )
    parser.add_argument(
        "--changed-by",
        default="codex",
        help="changed_by value for appended change-log rows. Default: codex",
    )
    parser.add_argument(
        "--related-commit",
        default="",
        help="Optional related_commit override for appended change-log rows.",
    )
    parser.add_argument(
        "--paper-id",
        action="append",
        default=[],
        help=(
            "Explicit impacted paper_id override. Repeatable. For upsert-secondary, omitted values "
            "default to master rows whose legacy Secondary class matches the updated code."
        ),
    )


def ensure_date(value: str) -> str:
    normalized = value.strip()
    if not DATE_PATTERN.fullmatch(normalized):
        raise SystemExit(f"--updated-at must be YYYY-MM-DD: {value!r}")
    return normalized


def parse_string_list_json(raw: str, flag_name: str) -> List[str] | None:
    if not raw.strip():
        return None
    try:
        value = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"{flag_name} must be valid JSON: {exc}") from exc
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise SystemExit(f"{flag_name} must decode to a JSON string array.")
    return value


def sync_mappings(payload: Dict[str, Any]) -> None:
    primary_terms = payload.get("primary_terms") or []
    secondary_terms = payload.get("secondary_terms") or []

    payload["primary_terms"] = sorted(
        primary_terms,
        key=lambda item: str(item["primary_code"]),
    )
    payload["secondary_terms"] = sorted(
        secondary_terms,
        key=lambda item: str(item["secondary_code"]),
    )
    payload["primary_code_to_label"] = {
        str(term["primary_code"]): str(term["label"])
        for term in payload["primary_terms"]
    }
    payload["secondary_code_to_label"] = {
        str(term["secondary_code"]): str(term["label"])
        for term in payload["secondary_terms"]
    }
    payload["label_to_primary_code"] = {
        str(term["label"]): str(term["primary_code"])
        for term in payload["primary_terms"]
    }
    payload["label_to_secondary_code"] = {
        str(term["label"]): str(term["secondary_code"])
        for term in payload["secondary_terms"]
    }


def validate_taxonomy_payload_semantics(payload: Dict[str, Any]) -> None:
    primary_terms = payload.get("primary_terms")
    secondary_terms = payload.get("secondary_terms")
    if not isinstance(primary_terms, list) or not isinstance(secondary_terms, list):
        raise SystemExit("classification_code_index payload must contain primary_terms and secondary_terms arrays.")

    seen_primary_codes: set[str] = set()
    seen_primary_labels: set[str] = set()
    for term in primary_terms:
        if not isinstance(term, dict):
            raise SystemExit("primary_terms rows must be objects.")
        code = str(term.get("primary_code") or "").strip()
        label = str(term.get("label") or "").strip()
        if not PRIMARY_CODE_PATTERN.fullmatch(code):
            raise SystemExit(f"Invalid primary_code in taxonomy owner payload: {code!r}")
        if code in seen_primary_codes:
            raise SystemExit(f"Duplicate primary_code in taxonomy owner payload: {code}")
        if label in seen_primary_labels:
            raise SystemExit(f"Duplicate primary label in taxonomy owner payload: {label!r}")
        seen_primary_codes.add(code)
        seen_primary_labels.add(label)

    seen_secondary_codes: set[str] = set()
    seen_secondary_labels: set[str] = set()
    for term in secondary_terms:
        if not isinstance(term, dict):
            raise SystemExit("secondary_terms rows must be objects.")
        code = str(term.get("secondary_code") or "").strip()
        label = str(term.get("label") or "").strip()
        parent_primary_code = str(term.get("parent_primary_code") or "").strip()
        if not SECONDARY_CODE_PATTERN.fullmatch(code):
            raise SystemExit(f"Invalid secondary_code in taxonomy owner payload: {code!r}")
        if not FORMAL_PRIMARY_CODE_PATTERN.fullmatch(parent_primary_code):
            raise SystemExit(
                f"Invalid parent_primary_code in taxonomy owner payload: {parent_primary_code!r}"
            )
        if code.split(".", 1)[0] != parent_primary_code:
            raise SystemExit(
                f"secondary_code does not match parent_primary_code: {code} vs {parent_primary_code}"
            )
        if parent_primary_code not in seen_primary_codes:
            raise SystemExit(
                f"secondary term parent_primary_code is missing from primary_terms: {parent_primary_code}"
            )
        if code in seen_secondary_codes:
            raise SystemExit(f"Duplicate secondary_code in taxonomy owner payload: {code}")
        if label in seen_secondary_labels:
            raise SystemExit(f"Duplicate secondary label in taxonomy owner payload: {label!r}")
        seen_secondary_codes.add(code)
        seen_secondary_labels.add(label)


def validate_payload_before_write(payload: Dict[str, Any]) -> None:
    validate_taxonomy_payload_semantics(payload)
    validate_payload_against_schema_file(
        payload=payload,
        schema_path=CLASSIFICATION_CODE_INDEX_SCHEMA_PATH,
        subject_label="classification_code_index.json",
    )


def find_term_index(
    terms: List[Dict[str, Any]],
    key: str,
    code: str,
) -> int | None:
    for index, term in enumerate(terms):
        if str(term.get(key) or "").strip() == code:
            return index
    return None


def upsert_primary_term(
    payload: Dict[str, Any], args: argparse.Namespace
) -> Tuple[str, str, Dict[str, Any] | None, Dict[str, Any]]:
    primary_code = args.primary_code.strip()
    if not PRIMARY_CODE_PATTERN.fullmatch(primary_code):
        raise SystemExit(f"Invalid --primary-code: {args.primary_code!r}")

    terms = deepcopy(payload.get("primary_terms") or [])
    index = find_term_index(terms, "primary_code", primary_code)
    existing = deepcopy(terms[index]) if index is not None else {}

    label = args.label.strip() or str(existing.get("label") or "").strip()
    definition = args.definition.strip() or str(existing.get("definition") or "").strip()
    include = parse_string_list_json(args.include_json, "--include-json")
    exclude = parse_string_list_json(args.exclude_json, "--exclude-json")
    status = args.status or str(existing.get("status") or "").strip()
    source = args.source.strip() or str(existing.get("source") or "").strip()

    if not label or not definition or include is None and "include" not in existing or exclude is None and "exclude" not in existing or not status or not source:
        raise SystemExit(
            "upsert-primary requires a complete primary term. "
            "For new terms, provide label/definition/include-json/exclude-json/status/source. "
            "For updates, missing fields may fall back to the existing owner term."
        )

    updated_term = {
        "primary_code": primary_code,
        "label": label,
        "definition": definition,
        "include": include if include is not None else list(existing["include"]),
        "exclude": exclude if exclude is not None else list(existing["exclude"]),
        "status": status,
        "source": source,
    }
    action = "update" if index is not None else "add"
    if index is not None:
        terms[index] = updated_term
    else:
        terms.append(updated_term)
    payload["primary_terms"] = terms
    return action, primary_code, (existing or None), updated_term


def upsert_secondary_term(
    payload: Dict[str, Any], args: argparse.Namespace
) -> Tuple[str, str, Dict[str, Any] | None, Dict[str, Any]]:
    secondary_code = args.secondary_code.strip()
    if not SECONDARY_CODE_PATTERN.fullmatch(secondary_code):
        raise SystemExit(f"Invalid --secondary-code: {args.secondary_code!r}")

    terms = deepcopy(payload.get("secondary_terms") or [])
    index = find_term_index(terms, "secondary_code", secondary_code)
    existing = deepcopy(terms[index]) if index is not None else {}

    derived_parent_code = secondary_code.split(".", 1)[0]
    parent_primary_code = args.parent_primary_code.strip() or str(
        existing.get("parent_primary_code") or derived_parent_code
    ).strip()
    label = args.label.strip() or str(existing.get("label") or "").strip()
    definition = args.definition.strip() or str(existing.get("definition") or "").strip()
    include = parse_string_list_json(args.include_json, "--include-json")
    exclude = parse_string_list_json(args.exclude_json, "--exclude-json")
    status = args.status or str(existing.get("status") or "").strip()
    review_status = args.review_status or str(existing.get("review_status") or "").strip()
    source = args.source.strip() or str(existing.get("source") or "").strip()

    if parent_primary_code != derived_parent_code:
        raise SystemExit(
            f"--parent-primary-code must match the prefix of secondary code: {secondary_code}"
        )
    if not label or not definition or include is None and "include" not in existing or exclude is None and "exclude" not in existing or not status or not review_status or not source:
        raise SystemExit(
            "upsert-secondary requires a complete secondary term. "
            "For new terms, provide parent-primary-code/label/definition/include-json/exclude-json/status/review-status/source. "
            "For updates, missing fields may fall back to the existing owner term."
        )

    updated_term = {
        "secondary_code": secondary_code,
        "parent_primary_code": parent_primary_code,
        "label": label,
        "definition": definition,
        "include": include if include is not None else list(existing["include"]),
        "exclude": exclude if exclude is not None else list(existing["exclude"]),
        "status": status,
        "source": source,
        "review_status": review_status,
    }
    action = "update" if index is not None else "add"
    if index is not None:
        terms[index] = updated_term
    else:
        terms.append(updated_term)
    payload["secondary_terms"] = terms
    return action, secondary_code, (existing or None), updated_term


def summarize_changes(before: Dict[str, Any], after: Dict[str, Any]) -> str:
    before_primary = len(before.get("primary_terms") or [])
    after_primary = len(after.get("primary_terms") or [])
    before_secondary = len(before.get("secondary_terms") or [])
    after_secondary = len(after.get("secondary_terms") or [])
    return (
        f"primary_terms {before_primary} -> {after_primary}; "
        f"secondary_terms {before_secondary} -> {after_secondary}; "
        f"updated_at {before.get('updated_at')} -> {after.get('updated_at')}; "
        f"updated_by {before.get('updated_by')} -> {after.get('updated_by')}"
    )


def impacted_paper_ids_for_secondary_code(secondary_code: str) -> List[str]:
    master_table = parse_markdown_table(
        MASTER_PATH,
        header_marker="| " + " | ".join(MASTER_HEADER) + " |",
        expected_header=MASTER_HEADER,
        data_prefix="| ASD-",
    )
    paper_ids = [
        str(row["ID"])
        for row in master_table.rows
        if str(row.get("Secondary class") or "").strip() == secondary_code
    ]
    return sorted(dict.fromkeys(paper_ids))


def normalize_impacted_paper_ids(raw_paper_ids: List[str]) -> List[str]:
    normalized = [paper_id.strip() for paper_id in raw_paper_ids if paper_id.strip()]
    return sorted(dict.fromkeys(normalized))


def resolve_impacted_paper_ids(
    *,
    args: argparse.Namespace,
    action_label: str,
    subject_code: str,
) -> List[str]:
    explicit_ids = normalize_impacted_paper_ids(args.paper_id)
    if explicit_ids:
        return explicit_ids
    if action_label.endswith("_secondary") and subject_code:
        return impacted_paper_ids_for_secondary_code(subject_code)
    return []


def build_change_log_rows(
    *,
    impacted_paper_ids: List[str],
    changed_at: str,
    changed_by: str,
    change_reason: str,
    related_commit: str,
    action_label: str,
    subject_code: str,
    before_term: Dict[str, Any] | None,
    after_term: Dict[str, Any] | None,
) -> List[Dict[str, Any]]:
    existing_rows = load_change_log_rows()
    rows: List[Dict[str, Any]] = []
    next_rows_seed = list(existing_rows)
    for paper_id in impacted_paper_ids:
        row = {
            "change_id": next_change_id(next_rows_seed),
            "paper_id": paper_id,
            "changed_at": changed_at,
            "changed_by": changed_by,
            "change_type": f"taxonomy_owner_{action_label}",
            "old_value": {
                "taxonomy_subject_code": subject_code,
                "term_before": before_term,
            },
            "new_value": {
                "taxonomy_subject_code": subject_code,
                "term_after": after_term,
            },
            "reason": change_reason,
            "related_commit": related_commit,
        }
        rows.append(row)
        next_rows_seed.append(row)
    return rows


def main() -> None:
    args = parse_args()
    updated_at = ensure_date(args.updated_at)
    updated_by = args.updated_by.strip() or "codex"
    changed_by = args.changed_by.strip() or "codex"

    original_payload = load_payload()
    payload = deepcopy(original_payload)
    before_term: Dict[str, Any] | None = None
    after_term: Dict[str, Any] | None = None

    if args.command == "sync":
        action_label = "sync"
        subject_code = ""
    elif args.command == "upsert-primary":
        action, code, before_term, after_term = upsert_primary_term(payload, args)
        action_label = f"{action}_primary"
        subject_code = code
    elif args.command == "upsert-secondary":
        action, code, before_term, after_term = upsert_secondary_term(payload, args)
        action_label = f"{action}_secondary"
        subject_code = code
    else:
        raise SystemExit(f"Unsupported command: {args.command}")

    sync_mappings(payload)
    if payload != original_payload:
        payload["updated_at"] = updated_at
        payload["updated_by"] = updated_by

    validate_payload_before_write(payload)

    if payload == original_payload:
        print("No owner changes required for classification_code_index.json.")
        return

    impacted_paper_ids = resolve_impacted_paper_ids(
        args=args,
        action_label=action_label,
        subject_code=subject_code,
    )
    change_log_rows: List[Dict[str, Any]] = []
    if args.append_change_log:
        if not args.change_reason.strip():
            raise SystemExit("--change-reason is required when --append-change-log is used.")
        if not impacted_paper_ids:
            raise SystemExit(
                "--append-change-log requires impacted paper_ids. "
                "Provide --paper-id or use upsert-secondary on a secondary code that maps to master rows."
            )
        related_commit = args.related_commit.strip() or current_commit()
        change_log_rows = build_change_log_rows(
            impacted_paper_ids=impacted_paper_ids,
            changed_at=updated_at,
            changed_by=changed_by,
            change_reason=args.change_reason.strip(),
            related_commit=related_commit,
            action_label=action_label,
            subject_code=subject_code,
            before_term=before_term,
            after_term=after_term,
        )

    print(f"Action: {action_label}{' ' + subject_code if subject_code else ''}")
    print(summarize_changes(original_payload, payload))
    if impacted_paper_ids:
        preview_ids = ", ".join(impacted_paper_ids[:8])
        if len(impacted_paper_ids) > 8:
            preview_ids += ", ..."
        print(
            f"Impacted paper_ids: {len(impacted_paper_ids)}"
            f"{' [' + preview_ids + ']' if preview_ids else ''}"
        )
    if args.append_change_log:
        print(f"Planned change_log rows: {len(change_log_rows)}")

    if args.dry_run:
        print("Dry run only; no files written.")
        return

    write_payload(payload)
    print(f"Wrote {CLASSIFICATION_CODE_INDEX_PATH}")
    for row in change_log_rows:
        append_change_log_row(row)
    if change_log_rows:
        print(f"Appended {len(change_log_rows)} rows to {ROOT / 'Data' / 'change_log.jsonl'}")


if __name__ == "__main__":
    main()
