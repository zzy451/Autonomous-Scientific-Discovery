# ASD structured data catalog round 4 closeout

Date: 2026-07-05
Scope: connect the discipline code assignment ledger into the derived registry and SQLite analysis layer

## What landed

This round connected the new owner ledger to the derived/query layer without changing the long-term plan file.

Implemented changes:

1. `scripts/export_structured_data.py`
   - now reads `Data/discipline_code_assignments.jsonl`
   - now generates:
     - `Data/discipline_local_code_registry.jsonl`
   - registry export now enforces the plan's "one row per paper" snapshot rule:
     - only current snapshot statuses are exposed
     - historical `retired_code` / `redirected_code` rows remain in the ledger owner, not in the derived registry snapshot
   - each registry row joins:
     - ledger owner fields
     - paper facts from `papers.jsonl` export inputs
     - derived snapshot metadata
   - snapshot metadata currently includes:
     - `is_derived_snapshot=true`
     - `generated_at`
     - `generated_by`
     - `source_commit`
     - `worktree_dirty`

2. `scripts/build_analysis_db.py`
   - now reads:
     - `Data/discipline_code_assignments.jsonl`
     - `Data/discipline_local_code_registry.jsonl`
   - now writes:
     - `Data/discipline_local_code_registry.csv`
   - SQLite now contains:
     - `discipline_code_assignments`
     - `discipline_local_code_registry`

3. `scripts/check_data_consistency.py`
   - now validates `discipline_local_code_registry.jsonl`
   - checks now cover:
     - row count parity with `discipline_code_assignments.jsonl`
     - `assignment_id` back-link
     - per-row field agreement with ledger owner and paper facts
     - `discipline_local_rank` derivation from `discipline_local_code`
     - uniform snapshot metadata across the registry

## New artifacts now present

Derived layer:

- `Data/discipline_local_code_registry.jsonl`
- `Data/discipline_local_code_registry.csv`

SQLite layer:

- table `discipline_code_assignments`
- table `discipline_local_code_registry`

Current row counts:

- `discipline_code_assignments.jsonl`: 447
- `discipline_local_code_registry.jsonl`: 447
- SQLite `discipline_code_assignments`: 447
- SQLite `discipline_local_code_registry`: 447

## Validation

Executed successfully from repo root:

```bash
python "Autonomous Scientific Discovery/scripts/export_structured_data.py"
python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"
python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"
```

Additional SQLite spot-check:

```sql
SELECT COUNT(*) FROM discipline_code_assignments;
SELECT COUNT(*) FROM discipline_local_code_registry;
```

Observed result:

- export passed
- check passed
- build passed
- SQLite row counts match the ledger/registry snapshot

## Current state after this round

The project now has all three layers for the discipline-code path:

1. owner ledger:
   - `Data/discipline_code_assignments.jsonl`
2. derived registry:
   - `Data/discipline_local_code_registry.jsonl`
   - `Data/discipline_local_code_registry.csv`
3. query layer:
   - SQLite `discipline_code_assignments`
   - SQLite `discipline_local_code_registry`

## Still not fully landed from the full plan

The discipline-code path is now materially connected, but the full long-term implementation is still incomplete.

Not yet completed:

- dedicated query commands for discipline-code / secondary-class inspection
- fuller SQLite normalization for additional planned tables such as:
  - `paper_general_method_buckets`
  - `pdf_evidence_status`
  - `paper_assets`
  - `notes`
  - `classification_terms`
- discipline-code / derived-layer reporting inside `check_data_consistency.py` beyond current structural validation

## Next recommended slice

Next implementation should continue from this integrated base and focus on one of:

1. extend SQLite with the remaining planned discipline-support tables/views
2. add `query_analysis_db.py` commands for:
   - `discipline-code-summary`
   - `discipline-code <code>`
   - `secondary-class-summary`
   - `secondary-class-pdf-coverage`
3. strengthen consistency checks around discipline-local registry semantics and downstream coverage reporting
