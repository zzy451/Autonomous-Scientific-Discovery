# Structured Data Catalog Round 63 Closeout

Date: 2026-07-06

## Round Goal

Strengthen the failed-state `integrity_check_report` so it better satisfies the locked reporting policy instead of collapsing every checker abort into a single generic error entry.

## Gap Identified

`Data/check_policy.md` requires the report to include, when practical:

- failing file / field
- `paper_id` or `assignment_id`
- machine-readable controlled error code
- recommended owner file to fix

The pass-state report already had structured `WARNING` / `INFO` findings, but the fail-state path in `scripts/check_data_consistency.py` still reduced any assertion abort to:

- category: `other`
- code: `CHECK_ABORTED`
- owner file: generic fallback

So when a hard check failed, the report lost most of the actionable attribution the policy expected.

## What Changed

Updated:

- `scripts/check_data_consistency.py`

### 1. Added failure-classification helper

Introduced:

- `extract_subject_id_from_message(...)`
- `classify_assertion_failure(...)`

These helpers now try to recover structured attribution from assertion messages, including:

- `subject_id`
  - `ASD-xxxx`
  - `DCA-xxxxxx`
  - `CL-xxxxxx`
- `category`
- machine-readable `code`
- recommended `owner_file`

### 2. Replaced generic fail-path finding

In the `except AssertionError` branch:

- instead of always appending one generic `CHECK_ABORTED`
- the checker now appends the classified failure finding

The fallback generic path still exists for assertion texts that do not match any known pattern, but common structured-data failures now produce a much more useful failed report.

## Validation

Executed:

```bash
python scripts/export_structured_data.py
python scripts/check_data_consistency.py
python scripts/build_analysis_db.py
```

Additional spot-check:

- imported `classify_assertion_failure(...)` directly and verified that representative assertion messages are mapped into structured findings with:
  - concrete `code`
  - concrete `category`
  - recovered `subject_id`
  - recommended `owner_file`

Result:

- `export` passed
- `check` passed
- `build` passed

## Outcome

This round improves the auditability of checker failures without changing owner facts or derived business logic. If a future blocking assertion fires, the generated report is now much closer to the plan’s required “actionable failure report” shape rather than degenerating into one opaque generic error entry.
