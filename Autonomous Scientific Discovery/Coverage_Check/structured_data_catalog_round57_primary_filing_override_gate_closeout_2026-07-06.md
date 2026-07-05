# Structured Data Catalog Round 57 Closeout

Date: 2026-07-06

## Round Goal

Close one more policy-to-checker gap in the primary filing layer: if `primary_module_for_filing` falls outside `scientific_object_modules`, the record must carry a reviewable manual override rather than passing through a looser legacy fallback.

## Gap Identified

The locked policy already required this behavior:

- `Data/check_policy.md`
  - `primary_module_for_filing` outside `scientific_object_modules` without an override reason is an `ERROR`
- `Data/primary_filing_policy.md`
  - `manual_override` should be used only when the normal decision priorities do not resolve the filing position
  - every override must include a concrete reason

But `scripts/check_data_consistency.py` still had a wider acceptance rule:

- it allowed `primary_module_for_filing` outside `scientific_object_modules` as long as it matched `legacy_main_class`

That meant the checker was more permissive than the locked policy.

## What Changed

Updated:

- `scripts/check_data_consistency.py`

The module-validation branch now enforces:

- when `primary_module_for_filing` is outside `scientific_object_modules`
  - `primary_module_assignment_rule` must be `manual_override`
  - `primary_module_override_reason` must be non-empty

This removes the silent `legacy_main_class` escape hatch and makes the runtime checker match the documented policy.

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

Current live-data boundary count:

- records where `primary_module_for_filing` is outside `scientific_object_modules`: `1`

Current surviving boundary case:

- `ASD-0662`
  - `scientific_object_modules=["03","05","06","11"]`
  - `primary_module_for_filing="01"`
  - `primary_module_assignment_rule="manual_override"`
  - `primary_module_override_reason="needs_primary_module_review"`

So the stricter gate is now active and the current exception remains explicitly reviewable instead of being implicitly tolerated.

## Outcome

This round converts another documented filing-policy rule into a real blocking integrity check. Primary filing positions outside the formal module array can no longer slip through under a generic legacy-class fallback; they now require explicit manual-override traceability.
