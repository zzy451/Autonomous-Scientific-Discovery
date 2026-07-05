# ASD structured data catalog round 6 closeout

Date: 2026-07-05
Scope: add structured integrity report output with severity-classified non-blocking findings

## What landed

This round extended the consistency-check layer from terminal-only pass/fail behavior to a persistent structured report artifact.

Implemented changes:

1. `scripts/check_data_consistency.py`
   - now writes:
     - `Data/integrity_check_report.md`
   - report generation now happens on:
     - successful check runs
     - failed check runs
   - successful runs write:
     - summary counts by severity
     - `WARNING` findings
     - `INFO` findings
   - failed runs still try to write:
     - a report with at least one `ERROR` finding before re-raising

2. severity handling now concretely surfaces planned non-blocking states
   - `WARNING` currently includes:
     - active confirmed-core papers missing local PDFs
     - active confirmed-core papers still marked `source_limited`
     - `pending_secondary` discipline-code ledger rows
     - secondary taxonomy terms still in provisional `needs_review / unreviewed` state
   - `INFO` currently includes:
     - `non_discipline_general_method` ledger rows
     - derived discipline-local registry snapshots generated from a dirty worktree

## Report artifact now present

Generated file:

- `Data/integrity_check_report.md`

Current top-level report state after a passing run:

- `Status: passed`
- `ERROR: 0`
- `WARNING: 96`
- `INFO: 10`

The report now gives a stable machine-readable-adjacent maintenance surface instead of forcing every review round to read raw terminal output only.

## Validation

Executed successfully from repo root:

```bash
python "Autonomous Scientific Discovery/scripts/export_structured_data.py"
python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"
python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"
```

Observed result:

- export passed
- check passed
- `Data/integrity_check_report.md` written
- build passed

## Current report semantics

The report is intentionally conservative:

- structural and semantic hard failures still abort the check
- non-blocking review states are preserved as `WARNING` / `INFO`
- the report points back to the relevant owner file for remediation

This keeps the current implementation aligned with the long-term plan's owner-first repair discipline.

## Still not fully complete from the long-term plan

The integrity-report layer now exists, but it is still an early structured version.

Still pending:

- richer controlled error codes across all findings
- fuller discipline-code and secondary-class summary sections inside the report
- more granular owner-path recommendations for every finding type
- broader inclusion of the newer analysis tables in report synthesis

## Next recommended slice

The next strongest follow-up is to keep deepening the reporting and query surface:

1. extend `integrity_check_report.md` with grouped discipline-code / secondary-class sections
2. add direct query commands for:
   - `classification_terms`
   - `paper_general_method_buckets`
   - `pdf_evidence_status`
   - `paper_assets`
   - `notes`
3. continue implementing the remaining long-term maintenance artifacts such as change-log support
