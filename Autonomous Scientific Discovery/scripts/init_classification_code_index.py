#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

from export_structured_data import (
    MASTER_HEADER,
    MASTER_PATH,
    TAXONOMY_CODE_TO_LABEL,
    parse_markdown_table,
)
from manage_classification_code_index import (
    SECONDARY_CODE_PATTERN,
    sync_mappings,
    validate_payload_before_write,
)


ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "Data"
CLASSIFICATION_CODE_INDEX_PATH = DATA_DIR / "classification_code_index.json"
FORMAL_PRIMARY_CODE_PATTERN = re.compile(r"^(0[1-9]|1[0-1])$")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Initialize Data/classification_code_index.json from the current taxonomy code map "
            "and legacy secondary classes in the master owner file. "
            "This command is separate from daily export so taxonomy-owner initialization never "
            "happens implicitly in export_structured_data.py."
        )
    )
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
        "--overwrite",
        action="store_true",
        help="Allow overwriting an existing Data/classification_code_index.json.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview the initialized payload without writing classification_code_index.json.",
    )
    return parser


def load_master_secondary_codes() -> List[str]:
    master_table = parse_markdown_table(
        MASTER_PATH,
        header_marker="| " + " | ".join(MASTER_HEADER) + " |",
        expected_header=MASTER_HEADER,
        data_prefix="| ASD-",
    )
    secondary_codes = []
    for row in master_table.rows:
        secondary_code = str(row.get("Secondary class") or "").strip()
        if secondary_code and SECONDARY_CODE_PATTERN.fullmatch(secondary_code):
            secondary_codes.append(secondary_code)
    return sorted(dict.fromkeys(secondary_codes))


def build_primary_terms() -> List[Dict[str, Any]]:
    terms: List[Dict[str, Any]] = []
    for code, label in sorted(TAXONOMY_CODE_TO_LABEL.items()):
        if code == "01.04":
            terms.append(
                {
                    "primary_code": code,
                    "label": label,
                    "definition": (
                        "Separate general-method bucket for ASD / research-agent method papers "
                        "without concrete scientific-object experiments, validations, benchmark tasks, "
                        "case studies, or reported results."
                    ),
                    "include": [
                        "general research-agent framework papers without concrete scientific-object validation",
                        "general ASD methodology without object-level experiments",
                    ],
                    "exclude": [
                        "any paper with concrete object-level experiments in formal 01-11 modules",
                        "formal 01 computational-science research objects",
                    ],
                    "status": "active",
                    "source": "taxonomy_index.json + init_classification_code_index.py",
                }
            )
            continue

        terms.append(
            {
                "primary_code": code,
                "label": label,
                "definition": (
                    f"{label} research objects within the ASD formal scientific-object taxonomy, "
                    "excluding the separate 01.04 general-method-only bucket."
                ),
                "include": [
                    f"records whose concrete scientific-object experiments or validations belong in {label}",
                ],
                "exclude": [
                    "general ASD method papers without concrete scientific-object experiments",
                    "records whose concrete object support belongs primarily in another formal module",
                ],
                "status": "active",
                "source": "taxonomy_index.json + init_classification_code_index.py",
            }
        )
    return terms


def build_secondary_terms(secondary_codes: List[str]) -> List[Dict[str, Any]]:
    terms: List[Dict[str, Any]] = []
    for secondary_code in secondary_codes:
        parent_primary_code = secondary_code.split(".", 1)[0]
        if not FORMAL_PRIMARY_CODE_PATTERN.fullmatch(parent_primary_code):
            continue
        terms.append(
            {
                "secondary_code": secondary_code,
                "parent_primary_code": parent_primary_code,
                "label": f"Legacy secondary filing term {secondary_code}",
                "definition": (
                    f"Provisional legacy secondary filing term {secondary_code} inherited from the current "
                    "master list; retained for first-pass discipline filing and review, not yet a fully "
                    "normalized canonical secondary taxonomy term."
                ),
                "include": [
                    "Records currently carrying this legacy secondary class in the authoritative master list.",
                ],
                "exclude": [
                    "Records that only match the primary module but do not currently carry this exact legacy secondary class.",
                    "Any future normalized split or merge that replaces this provisional legacy filing term.",
                ],
                "status": "needs_review",
                "source": "legacy_secondary_class_seed_init",
                "review_status": "unreviewed",
            }
        )
    return terms


def build_payload(updated_at: str, updated_by: str) -> Dict[str, Any]:
    secondary_codes = load_master_secondary_codes()
    payload: Dict[str, Any] = {
        "schema_version": 1,
        "updated_at": updated_at,
        "updated_by": updated_by,
        "primary_terms": build_primary_terms(),
        "secondary_terms": build_secondary_terms(secondary_codes),
    }
    sync_mappings(payload)
    validate_payload_before_write(payload)
    return payload


def write_payload(payload: Dict[str, Any]) -> None:
    CLASSIFICATION_CODE_INDEX_PATH.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    updated_at = args.updated_at.strip()
    updated_by = args.updated_by.strip() or "codex"

    payload = build_payload(updated_at=updated_at, updated_by=updated_by)
    print(
        f"Prepared classification_code_index payload with "
        f"{len(payload['primary_terms'])} primary_terms and {len(payload['secondary_terms'])} secondary_terms."
    )

    if CLASSIFICATION_CODE_INDEX_PATH.exists() and not args.overwrite:
        if args.dry_run:
            print(
                "Dry run preview only; existing Data/classification_code_index.json would be left unchanged "
                "without --overwrite."
            )
            return
        raise SystemExit(
            "Data/classification_code_index.json already exists. "
            "Use --overwrite to replace it or --dry-run to preview initialization."
        )

    if args.dry_run:
        print("Dry run only; no files written.")
        return

    write_payload(payload)
    print(f"Wrote {CLASSIFICATION_CODE_INDEX_PATH}")


if __name__ == "__main__":
    main()
