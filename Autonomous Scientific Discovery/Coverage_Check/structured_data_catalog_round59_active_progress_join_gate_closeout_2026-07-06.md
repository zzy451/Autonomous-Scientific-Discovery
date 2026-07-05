# Structured Data Catalog Round 59 Closeout

Date: 2026-07-06

## Round Goal

Close the remaining owner-join integrity gap from `Data/check_policy.md`: active records must not silently lose their link to the progress fact source.

## Gap Identified

The locked `ERROR` policy already said:

- master and progress cannot be joined for active records

But `scripts/check_data_consistency.py` still treated missing progress rows too permissively inside `validate_authoritative_sources()`:

- it used `progress_by_id.get(paper_id, {})`
- so an active record with no progress row could still fall through to later field comparisons using blank defaults

That meant the checker was not enforcing the join rule directly.

## What Changed

Updated:

- `scripts/check_data_consistency.py`

Inside `validate_authoritative_sources()`:

- fetch `progress_row = progress_by_id.get(paper_id)`
- if `active_confirmed_core=true`, require `progress_row is not None`
- only after that, normalize with `progress_row = progress_row or {}`

This turns the active master/progress join requirement into an explicit blocking check instead of an accidental byproduct of other field validations.

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

- active confirmed-core rows missing from the progress owner file: `0`

## Outcome

This round converts another owner-integrity rule into a direct checker gate. Active confirmed-core papers can no longer lose their progress-owner linkage without triggering an `ERROR`.
