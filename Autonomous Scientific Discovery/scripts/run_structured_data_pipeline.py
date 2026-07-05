from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run_step(script_name: str) -> None:
    script_path = ROOT / "scripts" / script_name
    command = [sys.executable, str(script_path)]
    print(f"[pipeline] running {script_name}", flush=True)
    subprocess.run(command, cwd=ROOT, check=True)


def main() -> None:
    for script_name in (
        "export_structured_data.py",
        "check_data_consistency.py",
        "build_analysis_db.py",
    ):
        run_step(script_name)
    print("[pipeline] export -> check -> build completed successfully", flush=True)


if __name__ == "__main__":
    main()
