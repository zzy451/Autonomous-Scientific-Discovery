from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OWNER_FACT_SOURCE_PATHS = (
    ROOT / "Paper_Lists" / "agent_master_paper_list.md",
    ROOT / "Coverage_Check" / "multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md",
    ROOT / "Data" / "discipline_code_assignments.jsonl",
    ROOT / "Data" / "classification_code_index.json",
)
CHANGE_LOG_PATH = ROOT / "Data" / "change_log.jsonl"


def get_git_status_paths(paths: tuple[Path, ...] | list[Path]) -> set[Path]:
    if not paths:
        return set()
    command = ["git", "status", "--porcelain", "--", *[str(path) for path in paths]]
    output = subprocess.check_output(command, cwd=ROOT, text=True, encoding="utf-8")
    changed_paths: set[Path] = set()
    for line in output.splitlines():
        if not line.strip():
            continue
        raw_path = line[3:].strip()
        if " -> " in raw_path:
            raw_path = raw_path.split(" -> ", 1)[1]
        changed_paths.add((ROOT / raw_path).resolve())
    return changed_paths


def print_preflight_summary() -> None:
    owner_changes = get_git_status_paths(list(OWNER_FACT_SOURCE_PATHS))
    change_log_changed = CHANGE_LOG_PATH.resolve() in get_git_status_paths([CHANGE_LOG_PATH])
    print("[pipeline] preflight owner fact source summary", flush=True)
    if owner_changes:
        for path in sorted(owner_changes):
            print(f"[pipeline] owner changed: {path.relative_to(ROOT)}", flush=True)
    else:
        print("[pipeline] owner changed: none", flush=True)
    print(
        "[pipeline] change_log changed: "
        + ("yes" if change_log_changed else "no"),
        flush=True,
    )
    if owner_changes and not change_log_changed:
        print(
            "[pipeline] warning: owner fact sources changed but Data/change_log.jsonl is unchanged",
            flush=True,
        )


def run_step(script_name: str) -> None:
    script_path = Path("scripts") / script_name
    command = [sys.executable, str(script_path)]
    print(f"[pipeline] running {script_name}", flush=True)
    subprocess.run(command, cwd=ROOT, check=True)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Run the canonical structured-data pipeline. "
            "Default workflow is export -> check -> build; "
            "--with-execution-audit additionally runs the Section 12 audit after build."
        )
    )
    parser.add_argument(
        "--with-execution-audit",
        action="store_true",
        help="Run audit_execution_definition.py after the canonical export -> check -> build sequence.",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    print_preflight_summary()
    for script_name in (
        "export_structured_data.py",
        "check_data_consistency.py",
        "build_analysis_db.py",
    ):
        run_step(script_name)
    if args.with_execution_audit:
        run_step("audit_execution_definition.py")
        print("[pipeline] export -> check -> build -> execution-audit completed successfully", flush=True)
    else:
        print("[pipeline] export -> check -> build completed successfully", flush=True)


if __name__ == "__main__":
    main()
