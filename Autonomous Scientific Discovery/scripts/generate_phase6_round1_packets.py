#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path
from typing import Dict, Iterable, List


ROOT = Path(__file__).resolve().parent.parent
COVERAGE_DIR = ROOT / "Coverage_Check"
RUN_DATE = "2026-07-02"
ACTIVE_BASELINE = 447
ROUND_LABEL = "Phase6FollowupR1"

FOLLOWUP_QUEUE_PATH = (
    COVERAGE_DIR / f"structured_data_phase6_full_text_followup_queue_{ACTIVE_BASELINE}_{RUN_DATE}.tsv"
)
MODULE_POOL_PATH = (
    COVERAGE_DIR / f"structured_data_phase6_module_coverage_pool_{ACTIVE_BASELINE}_{RUN_DATE}.tsv"
)
REPRESENTATIVE_POOL_PATH = (
    COVERAGE_DIR / f"structured_data_phase6_representative_paper_pool_{ACTIVE_BASELINE}_{RUN_DATE}.tsv"
)

SLICE_A_PATH = (
    COVERAGE_DIR / f"structured_data_phase6_followup_round1_slice_A_{ACTIVE_BASELINE}_{RUN_DATE}.tsv"
)
SLICE_B_PATH = (
    COVERAGE_DIR / f"structured_data_phase6_followup_round1_slice_B_{ACTIVE_BASELINE}_{RUN_DATE}.tsv"
)
SLICE_C_PATH = (
    COVERAGE_DIR / f"structured_data_phase6_followup_round1_slice_C_{ACTIVE_BASELINE}_{RUN_DATE}.tsv"
)
WRITING_MODULES_PATH = (
    COVERAGE_DIR / f"structured_data_phase6_writing_support_round1_modules_{ACTIVE_BASELINE}_{RUN_DATE}.tsv"
)
WRITING_REPRESENTATIVES_PATH = (
    COVERAGE_DIR / f"structured_data_phase6_writing_support_round1_representatives_{ACTIVE_BASELINE}_{RUN_DATE}.tsv"
)
PLAN_PATH = (
    COVERAGE_DIR / f"structured_data_phase6_followup_round1_plan_{ACTIVE_BASELINE}_{RUN_DATE}.md"
)


def load_tsv(path: Path) -> List[Dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, fieldnames: Iterable[str], rows: List[Dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(fieldnames), delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    followup_rows = load_tsv(FOLLOWUP_QUEUE_PATH)
    module_rows = load_tsv(MODULE_POOL_PATH)
    representative_rows = load_tsv(REPRESENTATIVE_POOL_PATH)
    base_followup_fields = list(followup_rows[0].keys())
    total_followup_candidates = len(followup_rows)

    top30 = followup_rows[:30]
    top30_no_local_pdf = sum(1 for row in top30 if "no_local_pdf" in row["followup_reasons"])
    top30_source_limited = sum(1 for row in top30 if row["source_limited"] == "yes")
    top30_non_full_text = sum(
        1 for row in top30 if "non_full_text_evidence_status" in row["followup_reasons"]
    )
    slices = {
        "A": top30[:10],
        "B": top30[10:20],
        "C": top30[20:30],
    }

    for slice_name, rows in slices.items():
        for index, row in enumerate(rows, start=1):
            row["round_label"] = ROUND_LABEL
            row["assigned_agent"] = f"Evidence-Agent-{slice_name}"
            row["slice_rank"] = str(index)

    fieldnames = base_followup_fields + ["round_label", "assigned_agent", "slice_rank"]
    write_tsv(SLICE_A_PATH, fieldnames, slices["A"])
    write_tsv(SLICE_B_PATH, fieldnames, slices["B"])
    write_tsv(SLICE_C_PATH, fieldnames, slices["C"])

    selected_modules = {"04", "03", "07", "09", "02"}
    selected_module_rows = [row for row in module_rows if row["module_code"] in selected_modules]
    selected_module_rows.sort(
        key=lambda row: (
            {"04": 1, "03": 2, "07": 3, "09": 4, "02": 5}.get(row["module_code"], 9),
            row["module_code"],
        )
    )
    write_tsv(
        WRITING_MODULES_PATH,
        selected_module_rows[0].keys() if selected_module_rows else [],
        selected_module_rows,
    )

    selected_representatives = [
        row
        for row in representative_rows
        if row["module_code"] in selected_modules
    ]
    for row in selected_representatives:
        module_rank = int(row["module_rank"])
        if module_rank <= 2:
            row["recommended_section_role"] = "anchor"
        elif row["object_coverage_mode"] == "multi_module":
            row["recommended_section_role"] = "boundary"
        else:
            row["recommended_section_role"] = "exemplar"

        risk_notes: List[str] = []
        if row["source_limited"] == "yes":
            risk_notes.append("source_limited")
        if row["object_coverage_mode"] == "multi_module":
            risk_notes.append("cross_module")
        if row["citation_priority"] != "core":
            risk_notes.append("non_core_priority")
        row["coverage_risk_note"] = ";".join(risk_notes) if risk_notes else "low"

    selected_representatives.sort(
        key=lambda row: (
            {"04": 1, "03": 2, "07": 3, "09": 4, "02": 5}.get(row["module_code"], 9),
            int(row["module_rank"]),
            row["paper_id"],
        )
    )
    write_tsv(
        WRITING_REPRESENTATIVES_PATH,
        selected_representatives[0].keys() if selected_representatives else [],
        selected_representatives,
    )

    plan = f"""# ASD Phase 6 follow-up round 1 packet plan

Date: {RUN_DATE}
Round label: `{ROUND_LABEL}`

This plan converts the previously generated Phase 6 preparation queues into a concrete first-round packet set for future multi-agent execution. No authoritative files are changed by this step.

## Scope selected for round 1

Round 1 uses the top `30` rows from:

- `{FOLLOWUP_QUEUE_PATH.relative_to(ROOT)}`

The queue is already priority-sorted. This round intentionally does **not** attempt to clear all `{total_followup_candidates}` follow-up candidates at once.

## Why only 30 papers

1. The highest-priority part of the queue already contains the strongest pressure signals:
   - no local PDF
   - `source_limited=yes`
   - non-full-text evidence
2. The current top 30 includes:
   - `{top30_no_local_pdf}` rows still carrying `no_local_pdf` pressure
   - `{top30_source_limited}` rows still carrying `source_limited=yes`
   - `{top30_non_full_text}` rows still carrying non-full-text evidence pressure
   This is enough to exercise a parallel evidence round without overloading merge review.
3. This keeps the next real multi-agent round aligned with the established `3 x 10` evidence-slice pattern.

## Slice allocation

- `Evidence-Agent-A`: `{SLICE_A_PATH.relative_to(ROOT)}`
- `Evidence-Agent-B`: `{SLICE_B_PATH.relative_to(ROOT)}`
- `Evidence-Agent-C`: `{SLICE_C_PATH.relative_to(ROOT)}`

### Slice A profile

- highest-pressure mixed chemistry / materials / bio rows
- includes the earliest no-local-PDF and source-limited multi-module frontier

### Slice B profile

- remaining no-local-PDF frontier
- extends into modules `05`, `06`, `07`, `10`, `11`

### Slice C profile

- tail of no-local-PDF frontier plus the first local-PDF source-limited cases
- includes `01.04`, `01`, `02`, `03` boundary-sensitive follow-up items

## Writing-support sidecar selection

For writing support, this round prioritizes modules that are both consequential and clean enough to support immediate drafting:

- `04` Materials Science
- `03` Chemical Sciences
- `07` Medical and Health Sciences
- `09` Engineering and Industrial Technology Sciences
- `02` Physics, Astronomy and Cosmic Sciences

Outputs:

- `{WRITING_MODULES_PATH.relative_to(ROOT)}`
- `{WRITING_REPRESENTATIVES_PATH.relative_to(ROOT)}`

These are not writeback packets. They are writing-support packets for future section drafting, representative-example selection, and coverage planning.

## Main-controller note

The generated slices and support packets are planning artifacts only. Any future execution round still has to follow:

- single-writer authoritative updates
- read-only evidence collection by sub-agents
- explicit packet launch
- explicit closeout and post-round git discipline
"""
    PLAN_PATH.write_text(plan, encoding="utf-8")

    print(f"Wrote {SLICE_A_PATH}")
    print(f"Wrote {SLICE_B_PATH}")
    print(f"Wrote {SLICE_C_PATH}")
    print(f"Wrote {WRITING_MODULES_PATH}")
    print(f"Wrote {WRITING_REPRESENTATIVES_PATH}")
    print(f"Wrote {PLAN_PATH}")


if __name__ == "__main__":
    main()
