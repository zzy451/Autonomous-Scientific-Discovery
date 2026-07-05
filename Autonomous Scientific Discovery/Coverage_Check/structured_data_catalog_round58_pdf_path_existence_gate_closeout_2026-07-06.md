# Structured Data Catalog Round 58 Closeout

Date: 2026-07-06

## Round Goal

Close another `ERROR`-level checker gap from `Data/check_policy.md`: any non-empty `pdf_path` must correspond to a real on-disk file instead of relying on downstream manifests to expose the problem indirectly.

## Gap Identified

The locked policy already lists this as an `ERROR`:

- non-empty `pdf_path` points to a missing file

The current checker already validated PDF existence through the derived `pdf_manifest` path, but the main `papers.jsonl` validation loop did not yet state the rule directly. That left the most authoritative derived record (`papers.jsonl`) slightly weaker than the policy.

## What Changed

Updated:

- `scripts/check_data_consistency.py`

Added direct checks in the main paper-row validation loop:

- if `pdf_path` is non-empty:
  - `pdf_exists` must be `true`
  - the file at `pdf_path` must exist on disk
- existing reverse check remains:
  - if `pdf_exists=true`, `pdf_path` must be non-empty

This makes the `papers.jsonl` checker enforce the file-integrity rule explicitly instead of depending on later manifest-layer validation.

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

Current live-data result:

- papers with non-empty `pdf_path` but missing on-disk file: `0`
- papers with non-empty `pdf_path` but `pdf_exists=false`: `0`

## Outcome

This round turns another policy-only integrity rule into a direct blocking check on the main structured paper snapshot. `pdf_path` now has explicit path-existence semantics at the `papers.jsonl` layer, not just in downstream manifests.
