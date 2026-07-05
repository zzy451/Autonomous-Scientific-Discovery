# Structured Data Catalog Round 68 Closeout

Date: 2026-07-06

## Round Goal

Strengthen the proof surface for execution-definition item 9 by exposing the `discipline_local_code_registry` snapshot metadata directly through SQLite metadata, not only inside JSONL / CSV rows.

## Gap Identified

Before this round, the registry snapshot already carried the required derived metadata in JSONL / CSV:

- `generated_at`
- `generated_by`
- `source_commit`
- `worktree_dirty`
- row-level snapshot markers

and the checker already validated those fields.

But the SQLite `metadata` table did not yet expose the registry snapshot metadata as explicit build metadata rows. That made execution-definition item 9 harder to prove from the query layer, even though the underlying JSONL rows were correct.

## What Changed

Updated:

- `scripts/build_analysis_db.py`
- `Data/README.md`

### 1. SQLite metadata now includes registry snapshot metadata

`build_analysis_db.py` now writes the following keys into SQLite `metadata`:

- `discipline_local_code_registry_row_count`
- `discipline_local_code_registry_generated_at`
- `discipline_local_code_registry_generated_by`
- `discipline_local_code_registry_source_commit`
- `discipline_local_code_registry_worktree_dirty`

### 2. Build self-validation now checks those rows

`validate_metadata_and_summary_tables(...)` now includes the same registry snapshot metadata in the expected metadata row set, so build self-validation will fail if SQLite metadata drifts from the current registry snapshot.

### 3. README query surface note

`Data/README.md` now states that the `metadata` query includes the current registry snapshot metadata fields, not only general build counters.

## Validation

Executed:

```bash
python scripts/run_structured_data_pipeline.py
python scripts/query_analysis_db.py metadata
```

Result:

- pipeline passed
- SQLite metadata query now exposes registry snapshot metadata rows

Observed metadata rows include:

- `discipline_local_code_registry_generated_at = 2026-07-05T22:37:47+00:00`
- `discipline_local_code_registry_generated_by = export_structured_data.py`
- `discipline_local_code_registry_row_count = 447`
- `discipline_local_code_registry_source_commit = 41b18b6372a142e34ac4ec361f25e0ebafd91bd1`
- `discipline_local_code_registry_worktree_dirty = true`

## Outcome

This round makes the registry snapshot metadata visible and self-validated in the SQLite query layer. That gives execution-definition item 9 a stronger direct proof surface: JSONL, CSV, and SQLite now all expose the derived snapshot metadata in auditable form.
