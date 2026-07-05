# Structured Data Catalog Round 61 Closeout

Date: 2026-07-06

## Round Goal

Close the `source_limited` semantic gap in the PDF evidence layer so that source-limited records cannot still appear as `full_text_checked`.

## Gap Identified

The locked long-term plan explicitly requires:

- when the record remains `source_limited=yes`, do not pretend it is `full text checked`

But the previous export logic still prioritized local-PDF presence over the source-limited flag when deriving `pdf_check_status`. As a result, several rows with:

- `source_limited = yes`
- local archived PDF present

were still exported as:

- `pdf_check_status = full_text_checked`

even though the progress-layer semantics said they remained source-limited.

Live inconsistent examples before this round included:

- `ASD-0466`
- `ASD-0541`
- `ASD-0553`
- `ASD-0599`
- `ASD-0741`
- `ASD-0768`

## What Changed

Updated:

- `scripts/export_structured_data.py`
- `scripts/check_data_consistency.py`

### 1. Export semantics

In `derive_pdf_check_status(...)`:

- `source_limited=yes` now takes precedence
- if a row remains source-limited, its derived `pdf_check_status` becomes `source_limited`
- local main-PDF presence no longer automatically upgrades a source-limited record to `full_text_checked`

### 2. Checker semantics

In `validate_pdf_archive_registry(...)`:

- rows with `source_limited=yes` must not carry `pdf_check_status=full_text_checked`

This locks the plan’s semantics directly into the checker.

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

- rows with `source_limited=yes` and `pdf_check_status=full_text_checked`: `0`

The six previously inconsistent rows now export as:

- `ASD-0466` -> `source_limited`
- `ASD-0541` -> `source_limited`
- `ASD-0553` -> `source_limited`
- `ASD-0599` -> `source_limited`
- `ASD-0741` -> `source_limited`
- `ASD-0768` -> `source_limited`

## Outcome

This round removes another semantic mismatch between progress-owner truth and the derived PDF evidence layer. A record can no longer remain explicitly source-limited while simultaneously presenting itself as full-text checked.
