# Structured Data Catalog Round 71 Closeout

Date: 2026-07-06

## Round Goal

Add a single focused query surface that shows the current paper-snapshot provenance and discipline-registry-snapshot provenance together, so the alignment can be audited in one place.

## Gap Identified

Before this round:

- `metadata` exposed all build metadata
- `discipline-registry-metadata` exposed only the discipline registry provenance rows

So the information existed, but there was still no compact one-command surface that answered:

- what paper snapshot batch is currently loaded
- what discipline registry snapshot batch is currently loaded
- whether those two provenance timestamps align

without requiring manual comparison across multiple commands.

## What Changed

Updated:

- `scripts/query_analysis_db.py`
- `Data/README.md`

### 1. Added `snapshot-provenance` query command

New command:

- `snapshot-provenance`

It prints the compact provenance bundle from SQLite `metadata`:

- `papers_jsonl_sha256`
- `papers_exported_at`
- `discipline_local_code_registry_generated_at`
- `discipline_local_code_registry_generated_by`
- `discipline_local_code_registry_source_commit`
- `discipline_local_code_registry_worktree_dirty`
- `discipline_local_code_registry_row_count`

### 2. README usage note

`Data/README.md` now documents:

- the new `snapshot-provenance` command
- that it is the compact cross-snapshot provenance surface for the current paper batch and registry batch

## Validation

Executed:

```bash
python scripts/run_structured_data_pipeline.py
python scripts/query_analysis_db.py snapshot-provenance
```

Result:

- pipeline passed
- new provenance query passed

Observed query output:

- `discipline_local_code_registry_generated_at = 2026-07-05T22:47:53+00:00`
- `discipline_local_code_registry_generated_by = export_structured_data.py`
- `discipline_local_code_registry_row_count = 447`
- `discipline_local_code_registry_source_commit = c7f9747122abd3ddb17832d047d8fc51c09f747c`
- `discipline_local_code_registry_worktree_dirty = true`
- `papers_exported_at = 2026-07-05T22:47:53+00:00`
- `papers_jsonl_sha256 = 431b37872f7978974317bf013994fea986617d90ba125e374469fa94882739e1`

## Outcome

This round makes snapshot alignment more directly auditable. Instead of reconstructing provenance from separate metadata commands, the project now has one focused query command that shows the current papers snapshot and discipline registry snapshot provenance together.
