# Structured Data Catalog Round 75 Closeout

Date: 2026-07-06

## Round Goal

Strengthen the evidence basis of execution-definition item 3 ("每篇论文有结构化资料状态") inside the execution-definition audit itself.

## Gap Identified

The execution-definition audit script already checked item 3, but the earlier version was still too weak:

- it only verified that a few evidence-related fields in `papers.jsonl` were strings

That was directionally useful, but not strong enough for a completion-oriented audit, because the project already has richer evidence-status surfaces:

- `Data/registry/pdf_archive_registry.jsonl`
- SQLite `pdf_evidence_status`

So the audit was under-using the actual current evidence.

## What Changed

Updated:

- `scripts/audit_execution_definition.py`

Execution-definition item 3 now requires all of the following:

- paper-level evidence-status fields are present in `papers.jsonl`
- `pdf_archive_registry.jsonl` row count matches `papers.jsonl`
- SQLite `pdf_evidence_status` row count matches `pdf_archive_registry.jsonl`
- registry rows carry structured evidence fields such as:
  - `pdf_evidence_type`
  - `pdf_check_status`
  - `source_limited`

The item’s success text and evidence pointer were updated accordingly.

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

Observed execution-definition audit output:

- item 3 now reports:
  - all `871` papers carry structured evidence-status fields
  - `871` `pdf_archive_registry` rows are mirrored into SQLite `pdf_evidence_status`

Overall audit result remained:

- `PASS=12`
- `FAIL=0`

## Outcome

This round improves the trustworthiness of the execution-definition audit. Item 3 now relies on the actual structured evidence surfaces that the project exports and loads into SQLite, rather than only on lightweight field-presence checks in `papers.jsonl`.
