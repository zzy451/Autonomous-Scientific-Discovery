# ASD structured data catalog round 10 closeout

Date: 2026-07-06
Scope: add first-pass derived lifecycle fields from existing owner data

## What landed

This round implemented the long-term plan's "derive lifecycle fields first, decide later whether to promote them to authoritative fields" path.

Implemented changes:

1. `scripts/export_structured_data.py`
   - now derives and exports:
     - `record_status`
     - `inclusion_decision`
     - `duplicate_of`
     - `last_reviewed_at`
     - `last_reviewed_by`
   - current derivation rules:
     - `record_status`
       - `active_confirmed_core` if `active_confirmed_core=true`
       - `background_only` from `inclusion_status=background_only`
       - `excluded` from `inclusion_status=excluded`
       - otherwise conservative fallback toward `candidate`
     - `inclusion_decision`
       - `confirmed_core` for active confirmed-core papers
       - otherwise follows current inclusion-status lane conservatively
     - `last_reviewed_at` / `last_reviewed_by`
       - derived from the latest entry per `paper_id` in `Data/change_log.jsonl`
       - currently blank for all rows because the change-log scaffold has not yet accumulated real audit entries

2. `scripts/build_analysis_db.py`
   - `papers.csv` now carries the derived lifecycle fields
   - SQLite `papers` table now stores the derived lifecycle fields

3. `scripts/check_data_consistency.py`
   - now validates:
     - allowed `record_status`
     - non-blank `inclusion_decision`
     - string shape for `duplicate_of`
     - date shape for non-empty `last_reviewed_at`
     - consistency between:
       - `active_confirmed_core`
       - `inclusion_status`
       - `record_status`
       - `inclusion_decision`

4. `scripts/query_analysis_db.py`
   - added command:
     - `lifecycle-summary`
   - added command:
     - `lifecycle-records`

## Current lifecycle query behavior

Executed successfully:

```bash
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" lifecycle-summary --all
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" lifecycle-records --record-status active_confirmed_core --limit 5
```

Current `lifecycle-summary --all` output is effectively:

- `active_confirmed_core / confirmed_core`: 447
- `background_only / background_only`: 371
- `excluded / excluded`: 53

This matches the current authoritative project state and gives a stable first-pass lifecycle layer without changing owner files.

## Validation

Executed successfully from repo root:

```bash
python "Autonomous Scientific Discovery/scripts/export_structured_data.py"
python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"
python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" lifecycle-summary --all
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" lifecycle-records --record-status active_confirmed_core --limit 5
```

Observed result:

- export passed
- check passed
- build passed
- lifecycle queries passed

## Important note

These lifecycle fields are still derived, not owner facts.

That means:

- they are useful now for reporting and querying
- they should not be hand-edited in derived outputs
- future promotion to authoritative fields should still follow the owner-first governance path

## Still not fully complete from the long-term plan

The long-term plan remains incomplete overall.

Still pending or partial:

- real `change_log.jsonl` usage, which will make `last_reviewed_at` / `last_reviewed_by` meaningful
- possible future explicit owner treatment for lifecycle fields
- richer lifecycle reporting inside the integrity report

## Next recommended slice

The next strongest continuation is to start using the audit path in real workflows:

1. begin appending real `change_log.jsonl` rows during owner updates
2. extend lifecycle reporting once review timestamps exist
3. continue any remaining owner-safe maintenance/reporting enhancements before considering field promotion
