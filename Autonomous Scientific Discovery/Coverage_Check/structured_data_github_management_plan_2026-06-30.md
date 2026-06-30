# ASD structured data and GitHub management plan

Date: 2026-06-30

This document fixes the next-stage execution plan for the Autonomous Scientific Discovery review project. Its purpose is to prevent plan drift across long Codex sessions and to make future data analysis, GitHub synchronization, PDF tracking, and classification updates reproducible.

## 1. Current authoritative state

- Project root: `Autonomous Scientific Discovery/`
- Canonical paper index: `Paper_Lists/agent_master_paper_list.md`
- Historical reaudit tracker: `Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`
- Historical `451` file names are retained only for tracker continuity.
- Current active confirmed-core unique works: `447`
- Current local readable PDF coverage: `421`
- Current no-local-PDF but DOI-indexable works: `26`
- Current classification system: formal `01-11` scientific-object modules plus independent `01.04` general-method bucket.

All new structured data must be derived from the canonical master list and the formal progress fields. Do not use a flat scan of `Notes/` as the source of truth.

## 2. Non-negotiable project rules

1. `ASD-xxxx` remains the permanent unique paper identity.
2. Classification codes must not replace the permanent paper ID.
3. A paper may have multiple `scientific_object_modules` under the relaxed multi-module rule.
4. `01.04` is an independent general-method bucket, not a formal scientific-object module inside the `01-11` count.
5. `primary_module_for_filing` controls note/PDF filing convenience only; it is not the complete classification fact.
6. PDF evidence must follow the progress file fields: `pdf_status`, `evidence_status`, and `pdf_path`.
7. "Full text checked" must not be treated as "local PDF archived" unless `pdf_path` points to a real readable local PDF.
8. Public GitHub upload must not blindly include copyrighted publisher PDFs.

## 3. ID design

### Permanent ID

Use the existing stable ID:

```text
ASD-0001
ASD-0002
...
```

This ID means one unique paper/work. It must stay stable across classification changes, note moves, PDF moves, duplicate reconciliation, and GitHub uploads.

### Classification call number

Optional classification-facing IDs such as `0101abc` may be introduced later only as secondary fields, for example:

```text
filing_call_number: "04.04-012"
module_call_numbers: ["03.03-008", "04.04-012"]
```

These are display, filing, or sorting codes. They must never become the primary key because the project allows multi-module classification and future reclassification.

## 4. Target structured data layer

Create a new structured data area:

```text
Autonomous Scientific Discovery/
  Data/
    papers.jsonl
    taxonomy_index.json
    pdf_manifest.json
    missing_pdf_manifest.json
    note_manifest.json
    README.md
  scripts/
    export_structured_data.py
    check_data_consistency.py
```

### File roles

- `Data/papers.jsonl`: one JSON object per paper; Git-friendly structured paper records.
- `Data/taxonomy_index.json`: code-to-label and label-to-code mappings for scientific modules and `01.04`.
- `Data/pdf_manifest.json`: local PDF inventory, including paths and hashes.
- `Data/missing_pdf_manifest.json`: the 26 no-local-PDF but DOI-indexable confirmed-core works.
- `Data/note_manifest.json`: note path inventory and note existence status.
- `Data/README.md`: human-readable explanation of the data model and regeneration workflow.
- `scripts/export_structured_data.py`: deterministic exporter from master/progress to `Data/`.
- `scripts/check_data_consistency.py`: validation script for counts, IDs, PDFs, and classification fields.

CSV and SQLite may be generated later from `papers.jsonl`. They should be treated as analysis outputs unless explicitly promoted.

## 5. Minimum `papers.jsonl` schema

Each record should include at least:

```json
{
  "paper_id": "ASD-0001",
  "title": "",
  "authors": "",
  "year": "",
  "source": "",
  "doi_or_url": "",
  "doi": "",
  "url": "",
  "is_agent": "",
  "inclusion_status": "",
  "scientific_object_modules": [],
  "general_method_bucket": "none",
  "object_coverage_mode": "",
  "primary_module_for_filing": "",
  "legacy_main_class": "",
  "legacy_secondary_class": "",
  "note_path": "",
  "pdf_status": "",
  "pdf_path": "",
  "evidence_status": "",
  "source_limited": "",
  "final_modules_or_bucket": "",
  "citation_priority": "",
  "remarks": ""
}
```

Implementation note: `scientific_object_modules` must be an array, not a semicolon-only string. If the master row only has legacy class fields, the exporter may infer a transitional value, but it must preserve the original legacy fields separately.

## 6. Taxonomy index design

`Data/taxonomy_index.json` should store both directions in one file:

```json
{
  "code_to_label": {
    "01": "Formal, Information and Computational Sciences",
    "01.04": "General ASD Methods without Concrete Object Experiments",
    "02": "Physics, Astronomy and Cosmic Sciences",
    "03": "Chemical Sciences",
    "04": "Materials Science",
    "05": "Earth and Environmental Sciences",
    "06": "Life Sciences",
    "07": "Medical and Health Sciences",
    "08": "Agricultural, Food, Forestry, Animal and Fishery Sciences",
    "09": "Engineering and Industrial Technology Sciences",
    "10": "Aerospace, Marine and Transportation Sciences",
    "11": "Social, Behavioral, Economic and Knowledge System Sciences"
  },
  "label_to_code": {}
}
```

The reverse index may be generated by script to avoid drift.

## 7. PDF and note management

PDFs should remain one canonical file per paper whenever legally available.

Do not rename all PDFs into classification-code-based filenames. Keep current descriptive filenames and manage the mapping in `pdf_manifest.json`.

`pdf_manifest.json` should include:

```json
{
  "paper_id": "ASD-0001",
  "title": "",
  "pdf_path": "",
  "pdf_status": "",
  "sha256": "",
  "primary_module_for_filing": "",
  "scientific_object_modules": [],
  "evidence_status": ""
}
```

For the 26 DOI-indexable but no-local-PDF works, use `missing_pdf_manifest.json`:

```json
{
  "paper_id": "ASD-0005",
  "title": "",
  "doi": "",
  "pdf_status": "no_local_pdf",
  "evidence_status": "",
  "source_limited": "",
  "access_note": ""
}
```

These 26 records remain confirmed-core and indexable. They are not missing literature records.

## 8. GitHub policy

The GitHub repository should receive:

- project notes, plans, policies, and reports
- structured data under `Data/`
- scripts under `scripts/`
- master list and taxonomy files
- manifest files for PDFs and missing PDFs

PDF upload policy:

- Do not blindly push all PDFs to a public repository.
- Only upload PDFs when license and redistribution status are clear.
- For private backup or private GitHub use, consider Git LFS for large PDF files.
- If PDFs are not uploaded, `pdf_manifest.json` still records local paths and hashes so the local evidence library remains auditable.

## 9. Consistency checks

Before committing a structured-data round, run checks for:

1. Active confirmed-core count remains `447`.
2. Active records with real local PDFs remain `421`.
3. Active no-local-PDF DOI-indexable records remain `26`.
4. Every active confirmed-core record has exactly one `paper_id`.
5. Every active confirmed-core record has either local PDF manifest coverage or missing PDF manifest coverage.
6. `scientific_object_modules` contains only `01-11` codes.
7. `01.04` appears only in `general_method_bucket` or `final_modules_or_bucket`, not as a normal scientific-object module.
8. Multi-module papers keep arrays and are not collapsed by `primary_module_for_filing`.
9. Each local PDF path exists and has a computed hash.
10. Each note path is recorded, even if note existence is flagged separately.

## 10. Execution phases

### Phase 1: Plan lock

- Create this plan file.
- Keep current master/progress untouched.
- Confirm worktree status after the plan file is added.

### Phase 2: Exporter and data files

- Create `Data/`.
- Create `scripts/export_structured_data.py`.
- Parse `agent_master_paper_list.md`.
- Parse progress tracker fields: `pdf_status`, `pdf_path`, `evidence_status`, `source_limited`, `closed`.
- Export `papers.jsonl`, `taxonomy_index.json`, `pdf_manifest.json`, `missing_pdf_manifest.json`, and `note_manifest.json`.

### Phase 3: Consistency checker

- Create `scripts/check_data_consistency.py`.
- Validate counts and file existence.
- Confirm the 26 no-local-PDF records are exactly:

```text
ASD-0005, ASD-0097, ASD-0112, ASD-0158, ASD-0381, ASD-0508, ASD-0536, ASD-0544, ASD-0547, ASD-0565, ASD-0569, ASD-0572, ASD-0592, ASD-0603, ASD-0609, ASD-0617, ASD-0631, ASD-0724, ASD-0727, ASD-0735, ASD-0854, ASD-0855, ASD-0858, ASD-0859, ASD-0860, ASD-0861
```

### Phase 4: GitHub readiness

- Add or verify Git remote for `zzy451/Autonomous-Scientific-Discovery`.
- Verify GitHub connectivity and push permission with dry-run first.
- Decide whether PDF files are included, excluded, or handled through Git LFS/private storage.
- Commit structured data and scripts before any upload.

### Phase 5: Analysis layer

- Generate CSV and SQLite from `papers.jsonl`.
- Build statistics from arrays, not from note folders.
- Separate record-level counts from expanded module-assignment counts.
- Keep `01.04` as an independent bucket count.

## 11. Default next action

The next concrete implementation step should be:

1. Create `Data/` and `scripts/` if needed.
2. Implement `scripts/export_structured_data.py`.
3. Generate the first structured data snapshot.
4. Implement and run `scripts/check_data_consistency.py`.
5. Review generated outputs before GitHub upload.

