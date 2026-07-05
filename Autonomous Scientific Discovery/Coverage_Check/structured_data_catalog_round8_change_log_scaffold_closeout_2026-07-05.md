# ASD structured data catalog round 8 closeout

Date: 2026-07-05
Scope: land the lightweight change-log audit path described in the long-term plan

## What landed

This round introduced the planned lightweight change-log scaffold without fabricating retrospective paper-change history.

Implemented changes:

1. added owner audit file:
   - `Data/change_log.jsonl`
   - current state:
     - empty scaffold
   - rationale:
     - the file now exists as the canonical append target for future paper-level change audit rows
     - historical events were not backfilled artificially

2. added append helper:
   - `scripts/append_change_log.py`
   - behavior:
     - appends one JSONL row
     - auto-generates `change_id` in `CL-000001` format
     - supports:
       - `paper_id`
       - `change_type`
       - `old_value_json`
       - `new_value_json`
       - `reason`
       - `changed_at`
       - `changed_by`
       - `related_commit`

3. extended `scripts/check_data_consistency.py`
   - validates `Data/change_log.jsonl` when present
   - current checks cover:
     - `change_id` format and uniqueness
     - known `paper_id`
     - `changed_at` date format
     - required text fields
     - presence of `old_value` and `new_value`

4. extended `scripts/build_analysis_db.py`
   - now loads `Data/change_log.jsonl`
   - now creates SQLite table:
     - `change_log`

5. extended `scripts/query_analysis_db.py`
   - added command:
     - `change-log`
   - supports:
     - `--paper-id`
     - `--change-type`
     - `--limit`

## Current behavior

Current query result:

```bash
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" change-log --limit 10
```

returns:

- `No rows found.`

This is expected for the current scaffolded state because no retrospective paper-level audit entries were invented.

SQLite spot-check:

- `SELECT COUNT(*) FROM change_log;`
- current result: `0`

## Validation

Executed successfully from repo root:

```bash
python "Autonomous Scientific Discovery/scripts/export_structured_data.py"
python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"
python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" change-log --limit 10
```

Observed result:

- export passed
- check passed
- build passed
- change-log query passed

## Important note

This round intentionally introduced the audit pipeline without manufacturing backfilled change rows.

That means:

- the file exists
- validation exists
- SQLite/table/query support exists
- future paper-level changes can now be logged cleanly
- but historical change coverage still depends on future append discipline, not synthetic reconstruction

## Still not fully complete from the long-term plan

The long-term plan is still not fully closed.

Still pending or partial:

- richer grouped sections inside `integrity_check_report.md`
- future use of `append_change_log.py` during real paper/classification/PDF/source updates
- lifecycle-field implementation and related audit/query surfaces

## Next recommended slice

The next strongest continuation is to deepen the maintenance/reporting layer:

1. improve `integrity_check_report.md` grouping by:
   - discipline-code
   - taxonomy
   - asset/note
   - PDF/source evidence
2. start using `change_log.jsonl` in real future owner updates
3. continue lifecycle-field implementation once the owner path is frozen enough
