# ASD structured data catalog round 9 closeout

Date: 2026-07-05
Scope: upgrade the integrity report from a flat finding list to grouped maintenance sections

## What landed

This round improved the reporting layer without changing any owner semantics or modifying the long-term plan file.

Implemented changes:

1. `scripts/check_data_consistency.py`
   - findings now carry a structured `category`
   - current categories in active use:
     - `evidence`
     - `discipline_code`
     - `taxonomy`
     - `derived_snapshot`
   - the report writer now emits:
     - summary counts by severity
     - summary counts by category
     - summary counts by finding code
     - grouped finding blocks inside each severity section

2. `Data/integrity_check_report.md`
   - now renders grouped maintenance sections instead of a single flat warning list
   - this makes it much easier to separate:
     - PDF/source follow-up work
     - discipline-code pending work
     - taxonomy review backlog
     - derived-snapshot state notes

## Current report structure

The report now contains:

1. `Summary`
   - `ERROR / WARNING / INFO`
2. `Summary By Category`
3. `Summary By Finding Code`
4. per-severity sections:
   - `ERROR`
   - `WARNING`
   - `INFO`
5. category sub-sections under the relevant severity

Current top-level grouped summary after this round:

- `evidence`: 45
- `discipline_code`: 24
- `taxonomy`: 36
- `derived_snapshot`: 1

Current top finding-code counts:

- `SECONDARY_TERM_NEEDS_REVIEW`: 36
- `MISSING_LOCAL_PDF`: 25
- `SOURCE_LIMITED`: 20
- `PENDING_SECONDARY`: 15
- `NON_DISCIPLINE_GENERAL_METHOD`: 9
- `DERIVED_SNAPSHOT_WORKTREE_DIRTY`: 1

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
- grouped `Data/integrity_check_report.md` written successfully
- build passed

## Why this matters

This round does not change facts, but it materially improves long-term operability.

The current structured stack now has a more usable maintenance surface:

- evidence debt is visibly separated from taxonomy debt
- taxonomy debt is visibly separated from discipline-code pending decisions
- derived snapshot notes are no longer mixed into paper-level review backlog

That aligns better with the long-term owner-first maintenance workflow described in the plan.

## Still not fully complete from the long-term plan

The plan is still not fully closed.

Still pending or partial:

- further compact rollups for discipline-code and secondary-class review inside the report
- future use of `change_log.jsonl` during real update rounds
- lifecycle-field implementation and its query/report surfaces

## Next recommended slice

The next strongest continuation is to start the lifecycle-field path or to bind change-log usage into real update workflows:

1. implement or derive the first-pass lifecycle registry fields more explicitly
2. begin writing real `change_log.jsonl` entries during owner updates
3. keep refining grouped maintenance reporting once lifecycle fields exist
