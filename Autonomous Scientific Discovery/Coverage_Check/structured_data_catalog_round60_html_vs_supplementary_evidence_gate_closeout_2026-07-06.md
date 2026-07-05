# Structured Data Catalog Round 60 Closeout

Date: 2026-07-06

## Round Goal

Close the PDF-evidence-layer semantic gap behind the `ERROR` rule "supplementary PDF is marked as main full text" by aligning export semantics and checker semantics.

## Gap Identified

The locked plan / policy already required:

- supplementary PDF must be explicitly marked as supplementary
- supplementary PDF must not be treated as main full-text evidence

But the current implementation still allowed one problematic combination:

- `pdf_evidence_type = supplementary_pdf`
- `pdf_check_status = full_text_checked`

The exported live example was `ASD-0381`, whose real evidence state was:

- publisher HTML full text
- open supplementary PDF
- no archived main-paper PDF

Yet the old export logic prioritized `"supplement"` before `"html_full_text"`, so the row was flattened into a supplementary-PDF full-text state instead of an HTML-full-text state.

## What Changed

Updated:

- `scripts/export_structured_data.py`
- `scripts/check_data_consistency.py`

### 1. Export semantics

In `derive_pdf_evidence_type(...)`:

- keep `main_pdf` highest priority when a local main PDF exists
- when no local main PDF exists, prefer `html_full_text` before `supplementary_pdf`

So mixed states such as "HTML full text + supplementary" now resolve to:

- `pdf_evidence_type = html_full_text`

instead of incorrectly collapsing to supplementary-only evidence.

### 2. Checker semantics

In `validate_pdf_archive_registry(...)`:

- `supplementary_pdf` rows must not use `pdf_check_status = full_text_checked`
- `full_text_checked` rows must now come only from:
  - `main_pdf`
  - `html_full_text`

This removes the old path where supplementary evidence could still pass as a full-text-checked primary state.

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

- `ASD-0381` now exports as:
  - `pdf_evidence_type = html_full_text`
  - `pdf_check_status = full_text_checked`
- rows with `supplementary_pdf + full_text_checked`: `0`

## Outcome

This round removes one more semantic mismatch between the locked policy and the derived evidence layer. Supplementary PDF evidence can no longer masquerade as primary full-text evidence, and mixed HTML-plus-supplementary states now land in the correct `html_full_text` bucket.
