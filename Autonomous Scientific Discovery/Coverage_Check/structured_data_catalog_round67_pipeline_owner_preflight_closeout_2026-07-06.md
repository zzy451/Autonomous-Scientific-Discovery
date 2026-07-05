# Structured Data Catalog Round 67 Closeout

Date: 2026-07-06

## Round Goal

Strengthen the new pipeline entrypoint so the required `owner fact source -> export -> check -> build` workflow is not only runnable, but also visibly anchored to the current owner-file change surface before execution.

## Gap Identified

After the previous round, the repo had a canonical pipeline command:

- `scripts/run_structured_data_pipeline.py`

That already enforced the correct execution order.

But it still lacked a preflight view of the actual owner-fact-source state in the worktree. In practice, that meant users could run the pipeline without seeing:

- whether any of the four owner fact sources had changed
- whether `Data/change_log.jsonl` had changed alongside them

This was still weaker than the intended maintenance discipline.

## What Changed

Updated:

- `scripts/run_structured_data_pipeline.py`
- `Data/README.md`

### 1. Owner-source preflight summary

The pipeline script now inspects git status for the four owner fact sources:

- `Paper_Lists/agent_master_paper_list.md`
- `Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`
- `Data/discipline_code_assignments.jsonl`
- `Data/classification_code_index.json`

and also checks:

- `Data/change_log.jsonl`

Before running any derived-layer steps, it now prints:

- which owner fact sources are currently changed
- whether `change_log.jsonl` is changed

If owner files changed but `change_log.jsonl` did not, it prints an explicit warning.

### 2. README workflow note

The `Workflow order` section in `Data/README.md` now states that the pipeline preflight reports current owner-source and change-log status before running the canonical sequence.

## Validation

Executed:

```bash
python scripts/run_structured_data_pipeline.py
```

Observed current preflight output:

- `[pipeline] preflight owner fact source summary`
- `[pipeline] owner changed: none`
- `[pipeline] change_log changed: no`

Then the canonical sequence completed successfully:

- `export`
- `check`
- `build`

Derived results remained healthy:

- `papers.jsonl`: `871`
- active confirmed-core: `447`
- active local PDFs: `422`
- active no-local-PDF: `25`
- `discipline_local_code_registry`: `447`

## Outcome

This round upgrades the pipeline from “correct command order” to “correct command order with owner-source visibility”. The maintenance workflow is now more audit-friendly because the operator can immediately see whether the current run is grounded in owner-file changes and whether the audit log moved with them.
