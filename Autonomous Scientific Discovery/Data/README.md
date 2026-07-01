# ASD structured data

This directory stores machine-readable exports derived from the canonical ASD project trackers.

## Source of truth

- `Paper_Lists/agent_master_paper_list.md`
- `Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`

Do not edit the generated JSON files by hand unless the regeneration workflow is explicitly being changed.

## Files

- `papers.jsonl`: one paper record per line; includes legacy fields plus derived structured classification fields.
- `papers.csv`: spreadsheet-friendly flat export of the same paper records.
- `paper_modules.csv`: exploded module-assignment table for one-to-many analysis.
- `papers.sqlite`: queryable analysis database with normalized tables.
- `field_dictionary.md`: authoritative field definitions for the structured exports and analysis database.
- `taxonomy_index.json`: scientific module and `01.04` code/label mappings.
- `pdf_manifest.json`: local archived PDF inventory with hashes.
- `missing_pdf_manifest.json`: active confirmed-core papers that currently have no local readable PDF but remain DOI/indexable.
- `note_manifest.json`: note path inventory and note existence flags.

## Regeneration

Run from the project root:

```bash
python "Autonomous Scientific Discovery/scripts/export_structured_data.py"
python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"
```

## Important rules

- `ASD-xxxx` is the permanent paper identity.
- `scientific_object_modules` is an array and may contain multiple formal `01-11` modules.
- `01.04` is kept in `general_method_bucket`, not inside `scientific_object_modules`.
- `primary_module_for_filing` is a filing convenience only.
- PDF truth follows the progress file fields and real local file existence.
