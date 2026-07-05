# ASD structured data catalog round 5 closeout

Date: 2026-07-05
Scope: add discipline-code query commands and the next planned SQLite support tables

## What landed

This round extended the discipline-code path from "stored in SQLite" to "queryable and analysis-ready", and also filled several planned support tables that were still missing from the analysis layer.

Implemented changes:

1. `scripts/build_analysis_db.py`
   - added SQLite table:
     - `classification_terms`
     - `paper_general_method_buckets`
     - `pdf_evidence_status`
     - `paper_assets`
     - `notes`
   - continued to keep the already-landed:
     - `discipline_code_assignments`
     - `discipline_local_code_registry`
   - `classification_terms` now normalizes both:
     - primary terms from `classification_code_index.json`
     - secondary terms from `classification_code_index.json`
   - primary and secondary `01.04` can coexist honestly because the table now uses `(taxonomy_code, term_level)` as its primary key

2. `scripts/query_analysis_db.py`
   - added command:
     - `discipline-code-summary`
   - added command:
     - `discipline-code <code>`
   - added command:
     - `secondary-class-summary`
   - added command:
     - `secondary-class-pdf-coverage`

3. analysis-layer behavior now available
   - current discipline-code snapshot counts
   - one-code drilldown across ledger + current registry
   - secondary-class distribution
   - secondary-class local-PDF coverage

## Query commands now working

Executed successfully:

```bash
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" discipline-code-summary
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" discipline-code 04-04-001
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" secondary-class-summary
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" secondary-class-pdf-coverage
```

Observed behavior:

- `discipline-code-summary` reports:
  - current registry row count
  - active / pending / non-discipline-general-method counts
  - active-code secondary-class distribution
- `discipline-code <code>` shows:
  - matching ledger rows
  - matching current registry row
- `secondary-class-summary` joins:
  - discipline local registry
  - taxonomy secondary terms
- `secondary-class-pdf-coverage` reports:
  - current registry counts
  - active-code local PDF coverage
  - missing-local-PDF counts
  - source-limited counts

## New SQLite support tables now present

Spot-checked row counts:

- `classification_terms`: 48
- `paper_general_method_buckets`: 169
- `pdf_evidence_status`: 871
- `paper_assets`: 1742
- `notes`: 871
- `discipline_code_assignments`: 447
- `discipline_local_code_registry`: 447

## Validation

Executed successfully from repo root:

```bash
python "Autonomous Scientific Discovery/scripts/export_structured_data.py"
python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"
python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" discipline-code-summary
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" discipline-code 04-04-001
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" secondary-class-pdf-coverage
```

Observed result:

- export passed
- check passed
- build passed
- new discipline-code and secondary-class queries passed

## Important implementation note

`discipline_local_code_registry.jsonl` remains a one-row-per-paper current snapshot.

That means:

- current statuses included:
  - `active_code`
  - `pending_secondary`
  - `non_discipline_general_method`
- historical rows such as:
  - `retired_code`
  - `redirected_code`
  remain in `discipline_code_assignments.jsonl` and are intentionally not flattened into the current registry snapshot

This preserves the owner/derived split required by the plan.

## Still not fully complete from the long-term plan

The project is materially further along, but the full plan is still not fully closed.

Still pending or only partially implemented:

- richer discipline-code / secondary-class consistency reporting in `check_data_consistency.py`
- broader query coverage for all newly added tables
- possible dedicated SQLite views for discipline-code review workflows
- later lifecycle / change-log / integrity-report expansions still described in the long-term plan

## Next recommended slice

The next most aligned continuation is to strengthen the review/reporting layer:

1. add discipline-code and secondary-class findings to a structured integrity report output
2. extend `query_analysis_db.py` with focused inspection commands over:
   - `classification_terms`
   - `paper_general_method_buckets`
   - `pdf_evidence_status`
   - `paper_assets`
   - `notes`
3. continue filling remaining long-term maintenance/reporting pieces such as change-log and richer consistency artifacts
