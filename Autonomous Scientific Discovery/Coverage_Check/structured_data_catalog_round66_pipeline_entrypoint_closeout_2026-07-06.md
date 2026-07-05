# Structured Data Catalog Round 66 Closeout

Date: 2026-07-06

## Round Goal

Turn the frozen workflow order from a documented expectation into a concrete runnable entrypoint so the project has an explicit `owner fact source -> export -> check -> build` execution surface.

## Gap Identified

The locked plan's execution definition requires that ongoing maintenance follow:

- owner fact source -> export -> check -> build

The repository already had the three core scripts:

- `scripts/export_structured_data.py`
- `scripts/check_data_consistency.py`
- `scripts/build_analysis_db.py`

and README already described the owner fact sources and guardrails.

But there was still no single canonical command surface that ran the required sequence in the required order. That made the workflow depend on manual command discipline instead of an explicit project entrypoint.

## What Changed

Added:

- `scripts/run_structured_data_pipeline.py`

This new script:

- runs `export_structured_data.py`
- then `check_data_consistency.py`
- then `build_analysis_db.py`
- aborts on the first failure
- prints step markers so the workflow order is visible in terminal output

Updated:

- `Data/README.md`

README now includes a dedicated `Workflow order` section that states the frozen day-to-day sequence:

1. change the appropriate owner fact source
2. run `export -> check -> build`
3. review derived outputs / report

and explicitly points users to `scripts/run_structured_data_pipeline.py`.

## Validation

Executed:

```bash
python scripts/run_structured_data_pipeline.py
```

Result:

- pipeline entrypoint ran successfully
- log order is explicit:
  - `[pipeline] running export_structured_data.py`
  - `[pipeline] running check_data_consistency.py`
  - `[pipeline] running build_analysis_db.py`
  - `[pipeline] export -> check -> build completed successfully`

Derived results remained healthy:

- `papers.jsonl`: `871`
- active confirmed-core: `447`
- active local PDFs: `422`
- active no-local-PDF: `25`
- `discipline_local_code_registry`: `447`

## Outcome

This round turns the workflow-order requirement into a real operational surface. The project no longer relies only on README prose plus human memory to preserve `export -> check -> build`; it now has a canonical runnable entrypoint for that sequence.
