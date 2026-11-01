#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List


ROOT = Path(__file__).resolve().parent.parent
CHANGE_LOG_PATH = ROOT / "Data" / "change_log.jsonl"


def load_rows() -> List[Dict[str, Any]]:
    if not CHANGE_LOG_PATH.exists():
        return []
    rows: List[Dict[str, Any]] = []
    for line in CHANGE_LOG_PATH.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def next_change_id(rows: List[Dict[str, Any]]) -> str:
    max_seen = 0
    for row in rows:
        change_id = str(row.get("change_id", ""))
        if change_id.startswith("CL-") and change_id[3:].isdigit():
            max_seen = max(max_seen, int(change_id[3:]))
    return f"CL-{max_seen + 1:06d}"


def parse_json_value(raw: str) -> Any:
    if raw == "":
        return None
    return json.loads(raw)


def current_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            cwd=ROOT,
            text=True,
            encoding="utf-8",
        ).strip()
    except Exception:
        return ""


def append_row(row: Dict[str, Any]) -> None:
    CHANGE_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with CHANGE_LOG_PATH.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Append one audit row to Data/change_log.jsonl. "
            "Use JSON literals for old/new values when structured payloads are needed."
        )
    )
    parser.add_argument("--paper-id", required=True)
    parser.add_argument("--change-type", required=True)
    parser.add_argument("--reason", required=True)
    parser.add_argument("--old-value-json", default="")
    parser.add_argument("--new-value-json", default="")
    parser.add_argument("--changed-at", default=datetime.now().strftime("%Y-%m-%d"))
    parser.add_argument("--changed-by", default="codex")
    parser.add_argument("--related-commit", default="")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    rows = load_rows()
    related_commit = args.related_commit or current_commit()
    row = {
        "change_id": next_change_id(rows),
        "paper_id": args.paper_id,
        "changed_at": args.changed_at,
        "changed_by": args.changed_by,
        "change_type": args.change_type,
        "old_value": parse_json_value(args.old_value_json),
        "new_value": parse_json_value(args.new_value_json),
        "reason": args.reason,
        "related_commit": related_commit,
    }
    append_row(row)
    print(f"Appended {row['change_id']} to {CHANGE_LOG_PATH}")


if __name__ == "__main__":
    main()
