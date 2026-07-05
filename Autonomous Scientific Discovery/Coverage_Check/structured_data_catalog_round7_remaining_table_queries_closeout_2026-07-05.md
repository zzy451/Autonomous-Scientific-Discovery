# ASD structured data catalog round 7 closeout

Date: 2026-07-05
Scope: add direct query commands for the remaining newly landed analysis tables

## What landed

This round focused on turning the remaining new SQLite analysis tables into directly usable CLI surfaces.

Implemented changes:

1. `scripts/query_analysis_db.py`
   - added command:
     - `classification-terms`
   - added command:
     - `general-method-buckets`
   - added command:
     - `pdf-evidence-status`
   - added command:
     - `paper-assets`
   - added command:
     - `notes`

2. command coverage details
   - `classification-terms`
     - supports `--level primary|secondary`
     - supports `--status active|deprecated|needs_review`
   - `general-method-buckets`
     - supports `--all`
   - `pdf-evidence-status`
     - supports `--all`
     - supports `--missing-only`
   - `paper-assets`
     - supports `--asset-type note|primary_pdf`
     - supports `--missing-only`
   - `notes`
     - supports `--all`
     - supports `--missing-only`

3. Windows terminal robustness
   - `query_analysis_db.py` now reconfigures stdout/stderr with `errors='replace'`
   - this prevents default Windows `gbk` terminals from crashing on isolated unencodable characters during large table output

## Query commands now working

Executed successfully:

```bash
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" classification-terms --level secondary --status needs_review
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" general-method-buckets
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" pdf-evidence-status --missing-only
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" paper-assets --asset-type note --missing-only
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" notes --missing-only
```

Observed behavior:

- `classification-terms` exposes provisional secondary taxonomy terms cleanly
- `general-method-buckets` exposes current canonical `01.04` bucket papers
- `pdf-evidence-status --missing-only` surfaces the active no-local-PDF inventory from the dedicated table
- `paper-assets --asset-type note --missing-only` surfaces the current missing-note asset inventory without terminal encoding failure
- `notes --missing-only` currently returns no active confirmed-core missing-note rows

## Validation

Executed successfully from repo root:

```bash
python "Autonomous Scientific Discovery/scripts/export_structured_data.py"
python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"
python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" classification-terms --level secondary --status needs_review
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" general-method-buckets
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" pdf-evidence-status --missing-only
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" paper-assets --asset-type note --missing-only
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" notes --missing-only
```

Observed result:

- export passed
- check passed
- build passed
- all newly added query commands passed

## Current state after this round

The major currently landed analysis tables now all have direct CLI access:

- `classification_terms`
- `paper_general_method_buckets`
- `pdf_evidence_status`
- `paper_assets`
- `notes`
- plus the previously landed discipline-code and secondary-class query surfaces

This makes the current structured-data stack much closer to the long-term "owner -> export -> check -> build -> query" workflow described in the plan.

## Still not fully complete from the long-term plan

The project is still not fully closed against the entire long-term plan.

Still pending or partial:

- richer grouped sections in `integrity_check_report.md`
- discipline-code / secondary-class findings summarized more compactly for maintenance review
- possible dedicated query commands over change-log and future lifecycle fields once those artifacts land
- the long-term change-log / lifecycle artifact path itself is still not implemented

## Next recommended slice

The next strongest continuation is to keep building the maintenance/reporting layer:

1. group `integrity_check_report.md` by discipline-code / taxonomy / asset / evidence sections
2. add or initialize the lightweight `Data/change_log.jsonl` path described in the plan
3. continue explicit lifecycle-field implementation once the owner strategy is ready
