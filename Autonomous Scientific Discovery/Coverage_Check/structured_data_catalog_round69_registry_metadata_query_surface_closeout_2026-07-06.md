# Structured Data Catalog Round 69 Closeout

Date: 2026-07-06

## Round Goal

Strengthen the direct proof surface for `discipline_local_code_registry` provenance by adding a dedicated query entrypoint instead of relying only on the general `metadata` dump.

## Gap Identified

After the previous round, the SQLite `metadata` table already contained the registry snapshot provenance fields:

- generated time
- generator
- source commit
- worktree-dirty flag
- registry row count

But the only query entrypoint was the general `metadata` command, which mixed these rows with all other build metadata and could still be a weaker proof surface during audits.

## What Changed

Updated:

- `scripts/query_analysis_db.py`
- `Data/README.md`

### 1. Wider generic metadata view

`metadata_summary(...)` now uses a wider key/value display width so longer metadata keys are less likely to be truncated in terminal output.

### 2. Dedicated registry provenance query

Added a new query command:

- `discipline-registry-metadata`

This prints only the `discipline_local_code_registry_*` rows from SQLite `metadata`, giving a clean provenance surface for the derived snapshot layer.

### 3. README usage note

`Data/README.md` now documents:

- the new `discipline-registry-metadata` command
- that it is the focused query surface for registry snapshot provenance

## Validation

Executed:

```bash
python scripts/run_structured_data_pipeline.py
python scripts/query_analysis_db.py discipline-registry-metadata
```

Result:

- pipeline passed
- dedicated registry provenance query passed

Observed query output:

- `discipline_local_code_registry_generated_at = 2026-07-05T22:41:00+00:00`
- `discipline_local_code_registry_generated_by = export_structured_data.py`
- `discipline_local_code_registry_row_count = 447`
- `discipline_local_code_registry_source_commit = b9427057f9f5aa68d9c8fafcbc4b6eb29a117e8b`
- `discipline_local_code_registry_worktree_dirty = true`

## Outcome

This round gives the project a cleaner direct audit surface for registry snapshot provenance. Execution-definition item 9 can now be demonstrated not only from JSONL/CSV rows and generic SQLite metadata, but also from a focused query command dedicated to the derived registry snapshot.
