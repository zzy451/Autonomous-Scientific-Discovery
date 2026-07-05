# Structured Data Catalog Round 70 Closeout

Date: 2026-07-06

## Round Goal

Strengthen the snapshot-provenance chain in SQLite metadata by exposing the `papers.jsonl` export timestamp directly alongside the registry snapshot metadata.

## Gap Identified

After the previous rounds, SQLite `metadata` already exposed the `discipline_local_code_registry` snapshot provenance fields, and the checker already enforced that:

- `papers.jsonl.exported_at` is uniform
- `discipline_local_code_registry.generated_at` matches it

But the query layer still lacked one direct piece:

- the `papers.jsonl` export timestamp itself was not stored in SQLite `metadata`

That meant the link between the paper snapshot batch and the registry snapshot batch was validated in code, but not fully visible in the SQLite evidence surface.

## What Changed

Updated:

- `scripts/build_analysis_db.py`
- `Data/README.md`

### 1. SQLite metadata now includes `papers_exported_at`

`build_analysis_db.py` now writes:

- `papers_exported_at`

into the SQLite `metadata` table.

### 2. Build self-validation now requires exported-at uniformity

`validate_metadata_and_summary_tables(...)` now explicitly requires:

- `papers.jsonl.exported_at` must be uniform for the build
- registry snapshot metadata fields used for SQLite metadata must also be uniform

This gives the build layer an internal guard against snapshot-metadata drift before metadata rows are written.

### 3. README query note updated

`Data/README.md` now states that the `metadata` query exposes:

- the current `papers.jsonl` export timestamp
- the current registry snapshot provenance metadata

## Validation

Executed:

```bash
python scripts/run_structured_data_pipeline.py
python scripts/query_analysis_db.py metadata
```

Result:

- pipeline passed
- metadata query passed

Observed query output now includes:

- `papers_exported_at = 2026-07-05T22:44:28+00:00`
- `discipline_local_code_registry_generated_at = 2026-07-05T22:44:28+00:00`

which directly demonstrates that the paper snapshot batch and registry snapshot batch are aligned in the SQLite query layer.

## Outcome

This round makes the export-batch linkage more directly auditable. The SQLite metadata surface now exposes both sides of the snapshot-provenance relationship: the paper snapshot export timestamp and the derived discipline registry snapshot provenance.
