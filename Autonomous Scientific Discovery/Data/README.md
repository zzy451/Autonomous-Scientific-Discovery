# ASD structured data

This directory is the machine-readable layer for ASD long-running collaboration. It exists so that statistics, queries, manifests, and downstream analyses are rebuilt from the same authoritative project records instead of drifting across notes, ad hoc spreadsheets, or one-off scripts.

## Authoritative hierarchy

Only two files are allowed to originate structured facts:

- `Paper_Lists/agent_master_paper_list.md`
- `Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`

Field ownership is intentionally split:

- `agent_master_paper_list.md` owns paper identity, inclusion status, legacy class fields, note path, and the project-facing classification record.
- The progress tracker owns PDF/evidence workflow fields such as `pdf_status`, `pdf_path`, `evidence_status`, `note_status`, `master_status`, `final_modules_or_bucket`, `source_limited`, `batch`, and `closed`.

`final_modules_or_bucket` should be treated as a workflow mirror from the reaudit process, not as the canonical classification fact source. Canonical structured classification remains derived from the master list plus the current project parsing rules around `scientific_object_modules`, `general_method_bucket`, and `primary_module_for_filing`.

Everything under `Data/` is derived. `Notes/`, `Reference_PDF/`, and `Coverage_Check/` reports are supporting evidence layers, not independent sources of truth for structured counts.

If the structured outputs disagree with master/progress, fix master/progress first and then regenerate. Do not hand-edit `Data/*.json`, `Data/*.jsonl`, `Data/*.csv`, or `Data/*.sqlite` as a substitute for repairing the authoritative records.

## Three-layer model

Treat the structured stack as:

- fact layer: `Paper_Lists/agent_master_paper_list.md` + `Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`
- normalized registry layer: `Data/registry/`
- analysis layer: `papers.jsonl`, manifests, CSV, SQLite
- support/evidence: notes, local PDFs, audit reports

The registry layer is a normalized derivative of master + progress. It exists so downstream tools can join stable paper, taxonomy, classification, PDF, and asset records without re-parsing the authoritative markdown every time.

The registry layer is not a third source of truth. If a registry row disagrees with master/progress, repair master/progress and regenerate the registry. Do not resolve drift by hand-editing registry files.

This means:

- classification changes start in master/progress, never in registry/JSONL/CSV/SQLite
- PDF status changes start in progress, never in `pdf_archive_registry` or `pdf_manifest.json`
- query bugs are fixed in scripts, then outputs are regenerated

## Regeneration order

Run all structured-data rebuilds from the repository root, in this exact order:

```bash
python "Autonomous Scientific Discovery/scripts/export_structured_data.py"
python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"
python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"
```

The order matters:

1. `export_structured_data.py`
   Reads master + progress and rewrites both the normalized registry layer and the analysis-layer structured snapshot in `Data/`.
2. `check_data_consistency.py`
   Verifies that registry and analysis outputs still agree with the master/progress-derived facts before analysis artifacts are trusted.
3. `build_analysis_db.py`
   Builds analysis-friendly outputs from the checked snapshot: `papers.csv`, `paper_modules.csv`, and `papers.sqlite`.

Do not run `build_analysis_db.py` as a substitute for export. `build` assumes `papers.jsonl` and the manifests are already current.

## Typical file roles

- `registry/paper_registry.jsonl`: normalized one-paper registry keyed by permanent `ASD-xxxx` paper IDs.
- `registry/paper_identifier_aliases.jsonl`: DOI / arXiv / source-URL alias registry for stable lookup without redefining the permanent `ASD-xxxx` key.
- `registry/taxonomy_registry.json`: normalized taxonomy term registry for formal `01-11` modules plus the separate `01.04` general bucket.
- `registry/classification_assignments.jsonl`: exploded paper-to-taxonomy assignment table derived from `scientific_object_modules` and `general_method_bucket`.
- `registry/pdf_archive_registry.jsonl`: normalized per-paper PDF availability/export record aligned to active local vs no-local PDF status.
- `registry/asset_manifest.jsonl`: normalized asset inventory covering at least note and primary PDF records.
- `papers.jsonl`: record-level analysis snapshot for scripts, version control, and exact per-paper inspection.
- `papers.csv`: flattened spreadsheet view of `papers.jsonl`.
- `paper_modules.csv`: exploded one-paper-to-many-modules table containing both canonical `scientific_object_modules` assignments and workflow-mirror `final_modules_or_bucket` assignments; always filter by `assignment_scope` before using it for statistics.
- `papers.sqlite`: normalized query database for joins, filters, and aggregation.
- `taxonomy_index.json`: code/label mapping for `01-11` and `01.04`.
- `pdf_manifest.json`: local archived PDF inventory with hashes.
- `missing_pdf_manifest.json`: active confirmed-core papers that remain valid records but currently have no local readable PDF.
- `note_manifest.json`: note-path inventory and note existence flags.
- `field_dictionary.md`: field semantics reference for the structured layer.

## When to use JSONL, CSV, or SQLite

Use `papers.jsonl` when:

- you need the most faithful per-paper record
- array fields must stay as arrays
- you are writing scripts or reviewing exact exported values

Use `papers.csv` or `paper_modules.csv` when:

- you want spreadsheet review, quick filtering, or manual spot checks
- you need a flat table for sharing or lightweight statistics
- you understand that arrays are flattened for convenience

Use `papers.sqlite` when:

- you need stable joins across papers, module assignments, manifests, and metadata
- you are doing repeated analysis or reproducible query work
- you need counts by module, missing-PDF inventory, or paper-level detail without reparsing JSONL

Inside SQLite, prefer the explicit scope-separated views for classification work:

- `canonical_paper_modules`
- `workflow_mirror_paper_modules`
- `canonical_module_assignment_counts`
- `workflow_mirror_module_assignment_counts`
- `classification_boundary_analysis`
- `classification_boundary_summary`

Rule of thumb:

- master + progress are the only fact layer
- registry is the normalized derived layer
- `papers.jsonl` / manifests / CSV / SQLite are the analysis layer
- CSV is the lightweight human-analysis layer
- SQLite is the durable query/analysis layer

## `query_analysis_db.py` typical usage

All commands below are run from the repository root and read `Data/papers.sqlite`.

Unless a command is explicitly labeled `audit` / `mirror`, classification outputs should be interpreted as canonical-only.

Show metadata and module counts:

```bash
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" summary
```

Inspect one paper in JSON form:

```bash
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" paper ASD-0001
```

List the active no-local-PDF inventory:

```bash
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" missing-pdf
```

List active multi-module papers:

```bash
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" multi-module
```

List papers assigned to a formal module:

```bash
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" module 04
```

Operational notes:

- `summary` prints metadata plus canonical formal-module counts from SQLite.
- `paper` prints the full structured paper payload, including both canonical fields and workflow-mirror inspection fields; do not treat `final_modules_or_bucket` as canonical.
- `missing-pdf`, `multi-module`, and `module` print tab-separated tables for shell use or redirection.
- `boundary-cases` and `bucket-summary` are audit commands for canonical-vs-mirror inspection, not default canonical classification summaries.
- If `papers.sqlite` is stale or missing, rerun `build_analysis_db.py` after `export -> check`.

On Windows terminals that still default to GBK, Unicode-heavy titles may print poorly. If needed, run:

```powershell
$env:PYTHONIOENCODING='utf-8'
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" summary
```

## Non-negotiable structured-data rules

- `ASD-xxxx` is the permanent paper identity.
- `scientific_object_modules` is an array and may contain multiple formal `01-11` modules.
- `01.04` belongs in `general_method_bucket`, not inside `scientific_object_modules`.
- `primary_module_for_filing` is a filing convenience, not the complete classification fact.
- PDF truth follows the progress file plus real local file existence.
- A passing `check_data_consistency.py` run is the minimum bar before committing structured-data changes.
