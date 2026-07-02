## Summary

Describe the operational change in 2-5 lines:

- what changed
- why it changed
- whether it affects source-of-truth records, derived data, or collaboration policy

## Source-of-Truth Impact

Mark all that apply:

- [ ] No master/progress/report files were changed.
- [ ] `Autonomous Scientific Discovery/Paper_Lists/agent_master_paper_list.md` was changed.
- [ ] `Autonomous Scientific Discovery/Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md` was changed.
- [ ] `Autonomous Scientific Discovery/Coverage_Check/` report or audit files were changed.
- [ ] Only derived `Data/`, docs, CI, or governance files were changed.

## Baseline Impact

Mark one:

- [ ] This PR does not change the accepted baseline.
- [ ] This PR changes the accepted baseline and follows `structured_data_baseline_update_rules_2026-07-02.md`.

If this PR changes the baseline, fill all fields:

- old baseline:
- new baseline:
- approval by:
- snapshot id (`schema_version` / `papers_jsonl_sha256`):
- canonical-only semantics reconfirmed: `yes / no`

If master/progress/report files changed, explain the single-writer coordination:

- coordinating owner or reviewer:
- what authoritative fields were updated:
- why the change starts there instead of in `Data/`:

## Structured Data Regeneration

If master or progress changed, confirm the required order:

- [ ] `python "Autonomous Scientific Discovery/scripts/export_structured_data.py"`
- [ ] `python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"`
- [ ] `python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"`

Paste the key `check_data_consistency.py` output:

```text
papers.jsonl records:
active confirmed-core:
active local PDFs:
active no-local-PDF:
workflow mirror drift count:
workflow mirror semantic drift count:
workflow mirror order drift count:
All structured-data consistency checks passed.
```

## Data Products Touched

Mark all outputs or governance files changed in this PR:

- [ ] `Autonomous Scientific Discovery/Data/papers.jsonl`
- [ ] `Autonomous Scientific Discovery/Data/papers.csv`
- [ ] `Autonomous Scientific Discovery/Data/paper_modules.csv`
- [ ] `Autonomous Scientific Discovery/Data/papers.sqlite`
- [ ] `Autonomous Scientific Discovery/Data/pdf_manifest.json`
- [ ] `Autonomous Scientific Discovery/Data/missing_pdf_manifest.json`
- [ ] `Autonomous Scientific Discovery/Data/note_manifest.json`
- [ ] `Autonomous Scientific Discovery/Data/taxonomy_index.json`
- [ ] `Autonomous Scientific Discovery/Data/README.md`
- [ ] `.github/` or `CODEOWNERS`

## Validation Run

List the commands you actually ran for this PR:

```text
python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"
python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"
```

If you used `query_analysis_db.py`, note the command(s):

```text
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" summary
```

## Reviewer Focus

Call out anything reviewers should inspect carefully:

- source-of-truth semantics
- derived-data freshness
- single-writer-sensitive files
- CI / governance changes
