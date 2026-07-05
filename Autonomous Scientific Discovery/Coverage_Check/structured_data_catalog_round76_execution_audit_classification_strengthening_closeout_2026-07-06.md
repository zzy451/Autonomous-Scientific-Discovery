# Structured Data Catalog Round 76 Closeout

Date: 2026-07-06

## Round Goal

Strengthen execution-definition item 2 ("每篇论文有结构化分类数组") so the audit relies on the actual classification expansion surfaces, not only on paper-row field presence.

## Gap Identified

Before this round, execution-definition item 2 in `audit_execution_definition.py` was still relatively weak:

- it checked that `papers.jsonl` rows carried classification-related fields

That was useful, but still indirect, because the project already materializes richer classification surfaces:

- `Data/registry/classification_assignments.jsonl`
- SQLite `paper_modules`
- SQLite `paper_general_method_buckets`

So the audit was not yet using the strongest available evidence for the classification-layer claim.

## What Changed

Updated:

- `scripts/audit_execution_definition.py`

Execution-definition item 2 now requires:

- structured classification fields exist in `papers.jsonl`
- `classification_assignments.jsonl` rows are structurally populated
- row count in `classification_assignments.jsonl` equals:
  - total formal-module assignments from `scientific_object_modules`
  - plus total general-method bucket assignments
- SQLite `paper_modules` row count equals the formal-module expansion count
- SQLite `paper_general_method_buckets` row count equals the general-method bucket expansion count

The item’s audit text and evidence pointer were updated accordingly.

## Validation

Executed:

```bash
python scripts/run_structured_data_pipeline.py --with-execution-audit
```

Result:

- `export` passed
- `check` passed
- `build` passed
- `audit_execution_definition.py` passed

Observed strengthened execution-definition item 2:

- `871` papers in `papers.jsonl`
- `1012` classification assignment rows
- SQLite `paper_modules = 843`
- SQLite `paper_general_method_buckets = 169`

Overall execution-definition audit result remained:

- `PASS=12`
- `FAIL=0`

## Outcome

This round makes the execution-definition audit more evidence-based for the classification layer. Item 2 now depends on the actual expanded classification surfaces in registry and SQLite, not just on the presence of classification fields in the paper snapshot.
