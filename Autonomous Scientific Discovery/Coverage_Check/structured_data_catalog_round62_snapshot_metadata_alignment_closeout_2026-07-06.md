# Structured Data Catalog Round 62 Closeout

Date: 2026-07-06

## Round Goal

Strengthen derived snapshot metadata validation so the registry metadata is tied to the actual current export batch rather than merely being present and uniform.

## Gap Identified

The locked plan requires `discipline_local_code_registry` to carry:

- `is_derived_snapshot=true`
- `generated_at`
- `generated_by`
- `source_commit`
- `worktree_dirty`

The checker already verified that these metadata fields existed and were uniform across the registry, but it did not yet verify the more important alignment facts:

- `papers.jsonl.exported_at` itself must be valid and uniform
- `discipline_local_code_registry.generated_at` must match that `papers.jsonl.exported_at`
- `generated_by` should be the actual export script name
- `source_commit` should be a real git commit id rather than an arbitrary string

So the metadata contract existed, but its batch-level coherence was not fully enforced.

## What Changed

Updated:

- `scripts/check_data_consistency.py`

### 1. `papers.jsonl` export timestamp checks

Added direct validation that every paper row carries a valid UTC `exported_at` timestamp in the current frozen format:

- `YYYY-MM-DDTHH:MM:SS+00:00`

Also added a snapshot-level check that `papers.jsonl.exported_at` is uniform across the whole export batch.

### 2. Discipline registry metadata alignment checks

Strengthened `validate_discipline_local_code_registry(...)` so it now requires:

- `generated_at` to equal the unique `papers.jsonl.exported_at`
- `generated_by` to be exactly `export_structured_data.py`
- `source_commit` to be a non-empty 40-hex git commit id

This moves the registry metadata from “present and uniform” to “present, uniform, and aligned to the actual export batch”.

## Validation

Executed:

```bash
python scripts/export_structured_data.py
python scripts/check_data_consistency.py
python scripts/build_analysis_db.py
```

Result:

- `export` passed
- `check` passed
- `build` passed

Current live-data verification:

- `papers.jsonl exported_at` values: `{'2026-07-05T22:11:18+00:00'}`
- `discipline_local_code_registry generated_at` values: `{'2026-07-05T22:11:18+00:00'}`
- `discipline_local_code_registry generated_by` values: `{'export_structured_data.py'}`
- `discipline_local_code_registry source_commit` values: `{'687288fad3bda3e656e7b8fbf456db5c118bd2fc'}`

## Outcome

This round tightens the auditability of the derived snapshot layer. The discipline-local registry metadata is now checked not only for existence but also for exact alignment with the current export batch and git provenance shape.
