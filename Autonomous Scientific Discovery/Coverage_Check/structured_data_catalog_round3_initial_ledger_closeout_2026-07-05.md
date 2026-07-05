# ASD structured data catalog round 3 closeout

Date: 2026-07-05
Scope: initialize the first stable discipline code assignment ledger from the reviewed preview pipeline

## What landed

This round advanced the project from preview-only state to a real management-code owner ledger.

Implemented changes:

1. Added explicit owner-initialization script:
   - `scripts/init_discipline_code_assignments.py`
   - purpose: generate `Data/discipline_code_assignments.jsonl` from `Data/discipline_code_initial_assignment_preview.csv`
   - boundary:
     - this is an explicit initialization command
     - it is not part of daily `export_structured_data.py`
     - daily export still does not overwrite owner fact sources

2. Initialized the first ledger owner file:
   - `Data/discipline_code_assignments.jsonl`
   - generated with:
     - `assignment_reason=initial_assignment`
     - `assigned_at=2026-07-05`
     - `assigned_by=codex`
   - current initialized status counts:
     - `active_code`: 423
     - `pending_secondary`: 15
     - `non_discipline_general_method`: 9

3. Extended owner checks in:
   - `scripts/check_data_consistency.py`
   - new validation now covers:
     - `assignment_id` format and uniqueness
     - known `paper_id` back-link to papers/master-derived records
     - active-code uniqueness
     - at most one `active_code` per `paper_id`
     - code-null rules for `pending_secondary` and `non_discipline_general_method`
     - `redirected_to_code` semantics
     - `primary_taxonomy_code_2lvl` presence rules by status

## Initialization behavior

The initializer currently treats the preview as initialization-ready once the hard blocked flag
`secondary_not_in_taxonomy_index`
has been eliminated.

That means:

- seeded-but-unreviewed secondary terms are allowed to enter the initial ledger
- unresolved filing mismatches remain visible through `pending_secondary`
- pure general-method-only records remain explicit ledger rows with `non_discipline_general_method`

This keeps the initial ledger honest while preserving the review backlog inside structured fields rather than hiding it outside the ledger.

## Validation

Executed successfully from repo root:

```bash
python "Autonomous Scientific Discovery/scripts/init_discipline_code_assignments.py"
python "Autonomous Scientific Discovery/scripts/export_structured_data.py"
python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"
python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"
```

Observed result:

- initial ledger owner file written successfully
- export still writes derived outputs only
- owner consistency checks passed
- build still passes after ledger introduction

## Current limitation

The initialized ledger now exists and is checked, but the downstream derived discipline-local registry layer is not yet wired in.

Still missing from the long-term plan:

- `Data/discipline_local_code_registry.jsonl`
- `Data/discipline_local_code_registry.csv`
- SQLite ingestion for:
  - `discipline_code_assignments`
  - discipline-local registry snapshots

## Next recommended slice

Next implementation should connect the new owner ledger into the derived/query layer:

1. extend `export_structured_data.py` to read `Data/discipline_code_assignments.jsonl`
2. generate `Data/discipline_local_code_registry.jsonl`
3. extend `build_analysis_db.py` to ingest:
   - `discipline_code_assignments`
   - `discipline_local_code_registry`
4. export `discipline_local_code_registry.csv`
