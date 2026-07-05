# Structured Data Catalog Round 64 Closeout

Date: 2026-07-06

## Round Goal

Tighten `integrity_check_report.md` so it better satisfies the locked reporting policy's "failing file / field" requirement, not just owner-file attribution.

## Gap Identified

`Data/check_policy.md` explicitly asks the report to include, when practical:

- failing file / field
- `paper_id` or `assignment_id`
- machine-readable controlled error code
- recommended owner file to fix

The previous rounds had already improved:

- machine-readable `code`
- `subject_id`
- `owner_file`

But the report still lacked a dedicated `field` surface. In practice, readers had to infer the problematic field from the free-text message.

## What Changed

Updated:

- `scripts/check_data_consistency.py`

### 1. Findings now support an explicit `field`

`add_finding(...)` now accepts an optional `field` key, and the structured finding record carries it through the report pipeline.

### 2. Assertion-failure attribution now includes field hints

`classify_assertion_failure(...)` now returns `field` values for common failure families, for example:

- `scientific_object_modules`
- `general_method_bucket`
- `primary_module_for_filing`
- `pdf_path`
- `note_path`
- `source_limited`

### 3. Pass-state findings now expose fields too

Current non-blocking findings were updated with practical field labels, such as:

- `pdf_path / pdf_exists`
- `source_limited`
- `primary_module_confidence`
- `assignment_status / pending_reason`
- `status / review_status`
- `worktree_dirty`

### 4. Report rendering now prints field lines

`write_integrity_check_report(...)` now emits:

```text
Field: `...`
```

whenever a finding carries a field label.

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

Current report evidence:

- `Data/integrity_check_report.md` now shows explicit `Field:` lines in the warning / info sections
- representative examples include:
  - `pdf_path / pdf_exists`
  - `pdf_path / pdf_evidence_type`
  - `source_limited`

## Outcome

This round improves the structured readability of both pass-state and future fail-state integrity reports. The report layer now carries a clearer "which field is implicated" surface, which brings it closer to the locked policy's required actionable-check-report shape.
