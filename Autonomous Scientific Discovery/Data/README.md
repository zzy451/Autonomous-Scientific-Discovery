# ASD structured data

This directory is the machine-readable layer for ASD long-running collaboration. It exists so that statistics, queries, manifests, and downstream analyses are rebuilt from the same authoritative project records instead of drifting across notes, ad hoc spreadsheets, or one-off scripts.

## Authoritative hierarchy

The current structured-data system distinguishes four fact-source classes:

1. Paper and classification facts:
   - `Paper_Lists/agent_master_paper_list.md`
2. Source / PDF / progress facts:
   - `Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`
3. Discipline-local code assignment facts:
   - `Data/discipline_code_assignments.jsonl`
4. Taxonomy vocabulary facts:
   - `Data/classification_code_index.json`

Field ownership is intentionally split, but the current export layer still carries a small amount of compatibility fallback while row-level schema migration remains incomplete:

- `agent_master_paper_list.md` owns paper identity, inclusion status, legacy class fields, and the canonical classification overlay carried in `Remarks`.
- `note_path` is master-owned in governance terms, but the exporter currently resolves it as `progress.note_path or master.Note path`.
- The progress tracker owns PDF/evidence workflow fields such as `pdf_status`, `evidence_status`, `note_status`, `master_status`, `final_modules_or_bucket`, `source_limited`, `batch`, and `closed`.
- `pdf_path` is progress-owned in governance terms, but the exporter currently resolves it as `progress.pdf_path or master.PDF path`.
- `discipline_code_assignments.jsonl` owns stable `discipline_local_code` assignment records and `assignment_status`.
- `classification_code_index.json` owns primary / secondary taxonomy vocabulary labels, definitions, include/exclude boundaries, term status, and term source.

`final_modules_or_bucket` should be treated as a workflow mirror from the reaudit process, not as the canonical classification fact source. It is parsed as a semicolon-delimited mirror list whose order is preserved for drift auditing.

Canonical structured classification remains derived from the master list plus the current project parsing rules around `scientific_object_modules`, `general_method_bucket`, `object_coverage_mode`, and `primary_module_for_filing`. In current script behavior, `Remarks` structured tokens take priority, unresolved legacy `01 / 01.04` rows are normalized into the separate `01.04` general bucket, and only then does legacy `Main class` serve as a fallback for formal-module export.

The current lifecycle-derived lane also includes `record_status`, `inclusion_decision`, and `duplicate_of`. When an excluded record's `Exclusion reason` explicitly marks it as a duplicate of another `ASD-xxxx` record, export derives a structured duplicate linkage instead of leaving that evidence only in free text.

Formal Phase 3 governance artifacts:

- semantics freeze: `Coverage_Check/structured_data_authoritative_semantics_freeze_2026-07-02.md`
- baseline acceptance checklist: `Coverage_Check/structured_data_authoritative_acceptance_checklist_447_2026-07-02.md`

Formal Phase 4 analysis artifact:

- canonical-only analysis semantics: `Coverage_Check/structured_data_canonical_analysis_semantics_2026-07-02.md`

Formal Phase 5 collaboration artifacts:

- collaboration SOP: `Coverage_Check/structured_data_collaboration_sop_2026-07-02.md`
- baseline update rules: `Coverage_Check/structured_data_baseline_update_rules_2026-07-02.md`
- red-line file list: `Coverage_Check/structured_data_red_line_files_2026-07-03.md`

Live accepted baseline note:

- current accepted counts and accepted active-ID baseline should be read from `Coverage_Check/structured_data_authoritative_acceptance_checklist_447_2026-07-02.md`
- `structured_data_authoritative_semantics_freeze_2026-07-02.md` freezes field semantics and ownership, but it is not the live baseline-number source

Most files under `Data/` are derived. The current exceptions are `Data/discipline_code_assignments.jsonl` and `Data/classification_code_index.json`, which own management-code and taxonomy-vocabulary facts respectively. `Notes/`, `Reference_PDF/`, and `Coverage_Check/` reports are supporting evidence layers, not independent sources of truth for structured counts.

If derived structured outputs disagree with their owner files, fix the owner file first and then regenerate. Do not hand-edit derived `Data/*.json`, `Data/*.jsonl`, `Data/*.csv`, or `Data/*.sqlite` as a substitute for repairing the owner records.

## Responsibility map

Treat the structured stack as:

- paper/progress fact layer: `Paper_Lists/agent_master_paper_list.md` + `Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`
- stable code assignment ledger: `Data/discipline_code_assignments.jsonl`
- taxonomy vocabulary owner: `Data/classification_code_index.json`
- canonical classification lane: `scientific_object_modules` + `general_method_bucket`
- workflow mirror lane: `final_modules_or_bucket` + progress workflow statuses
- normalized registry layer: `Data/registry/`
- analysis layer: `papers.jsonl`, manifests, CSV, SQLite
- support/evidence: notes, local PDFs, audit reports

The registry layer is a normalized derivative of master + progress. It exists so downstream tools can join stable paper, taxonomy, classification, PDF, and asset records without re-parsing the authoritative markdown every time.

The registry layer is not a source of truth. If a registry row disagrees with master, progress, discipline code assignments, or classification code index, repair the relevant owner and regenerate the registry. Do not resolve drift by hand-editing registry files.

This means:

- classification changes start in master/progress, never in registry/JSONL/CSV/SQLite
- PDF status changes start in progress, never in `pdf_archive_registry` or `pdf_manifest.json`
- discipline-local code changes start in `discipline_code_assignments.jsonl`, never in `discipline_local_code_registry.jsonl` or CSV
- taxonomy vocabulary changes start in `classification_code_index.json`, never in registry or SQLite
- daily export must not overwrite owner fact sources, including `discipline_code_assignments.jsonl` and `classification_code_index.json`
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
   Builds analysis-friendly outputs from the checked snapshot: `papers.csv`, `paper_modules.csv`, `canonical_paper_modules.csv`, `workflow_mirror_paper_modules.csv`, `mixed_scope_paper_modules.csv`, and `papers.sqlite`.

Both `export_structured_data.py` and `build_analysis_db.py` now carry runtime owner-path guardrails: if a future code change ever tries to write a guarded owner fact source such as `classification_code_index.json`, `discipline_code_assignments.jsonl`, or `change_log.jsonl`, the command aborts instead of silently overwriting the owner file.

`build_analysis_db.py` now also self-validates key derived analysis surfaces after writing outputs: `papers.csv` plus SQLite `papers` must remain faithful to the current `papers.jsonl` snapshot, the module-surface split must remain canonical/workflow/mixed-scope clean, `discipline_local_code_registry.csv` plus SQLite `discipline_local_code_registry` must remain faithful to the current JSONL snapshot, the SQLite analysis tables `paper_general_method_buckets`, `pdf_evidence_status`, `paper_assets`, and `notes` must remain faithful to their current derived source rows, the owner-loaded / inventory tables `classification_terms`, `discipline_code_assignments`, `change_log`, `pdf_inventory`, `missing_pdf_inventory`, and `note_inventory` must remain faithful to the source rows that build loaded for the current run, the metadata/sanity surfaces `taxonomy_index`, `metadata`, `active_confirmed_core_papers`, and `active_missing_local_pdf` must remain aligned with the current build inputs and active-record counts, and `analysis_object_scope_registry` must remain faithful to the currently declared object-scope rows in the build script while also covering every current SQLite table/view.

Do not run `build_analysis_db.py` as a substitute for export. `build` assumes `papers.jsonl` and the manifests are already current.

## Typical file roles

- `registry/paper_registry.jsonl`: normalized one-paper registry keyed by permanent `ASD-xxxx` paper IDs.
- `registry/paper_identifier_aliases.jsonl`: DOI / arXiv / source-URL alias registry for stable lookup without redefining the permanent `ASD-xxxx` key.
- `registry/taxonomy_registry.json`: normalized taxonomy term registry for formal `01-11` modules plus the separate `01.04` general bucket.
- `registry/classification_assignments.jsonl`: exploded paper-to-taxonomy assignment table derived from `scientific_object_modules` and `general_method_bucket`.
- `registry/pdf_archive_registry.jsonl`: normalized per-paper PDF availability/export record aligned to active local vs no-local PDF status, including derived evidence type/check-depth fields and `source_checked_at`.
- `registry/asset_manifest.jsonl`: normalized asset inventory covering at least note and primary PDF records; primary-PDF rows mirror derived source-check timing.
- `papers.jsonl`: record-level analysis snapshot for scripts, version control, and exact per-paper inspection, including derived source/PDF review timing.
- `papers.csv`: flattened spreadsheet view of `papers.jsonl`.
- `paper_modules.csv`: canonical exploded one-paper-to-many-modules export for the formal `scientific_object_modules` relation. This is the default flat analysis surface for module-level spreadsheet work and carries `is_primary_for_filing`, `confidence`, and `source` trace columns.
- `canonical_paper_modules.csv`: compatibility alias export carrying the same canonical rows as `paper_modules.csv` for older analysis surfaces that still reference the older canonical filename.
- `workflow_mirror_paper_modules.csv`: workflow-mirror-only flat assignment export for audit/debugging.
- `mixed_scope_paper_modules.csv`: compatibility mixed-scope flat export containing both canonical `scientific_object_modules` assignments and workflow-mirror `final_modules_or_bucket` assignments; use only when an explicit canonical-vs-workflow comparison surface is needed.
- `papers.sqlite`: normalized query database for joins, filters, and aggregation.
- `taxonomy_index.json`: code/label mapping for `01-11` and `01.04`.
- `classification_code_index.json`: taxonomy vocabulary owner for primary / secondary code labels, definitions, include/exclude boundaries, term status, and term source.
- `discipline_code_initial_assignment_preview.csv`: derived initial-assignment review sheet built from master + progress + taxonomy owner facts before freezing or editing the stable discipline-code ledger; review it, fix owner files, then rerun export instead of hand-editing the preview.
  `check_data_consistency.py` now also validates its current-snapshot paper coverage, status branching, no-fake-code rules, and active-code sequence stability.
- `discipline_code_assignments.jsonl`: stable discipline-local code assignment ledger using `assignment_status`.
- `discipline_local_code_registry.jsonl`: derived snapshot joining paper facts, progress facts, taxonomy vocabulary, and discipline code assignments.
- `discipline_local_code_registry.csv`: spreadsheet-oriented derived snapshot for discipline-local code review.
- `field_ownership_matrix.md`: owner matrix for structured fields.
- `discipline_code_assignment_policy.md`: discipline-local code assignment policy.
- `primary_filing_policy.md`: policy for choosing the single filing module for multi-module papers.
- `check_policy.md`: `ERROR` / `WARNING` / `INFO` consistency-check policy.
- `schema/discipline_code_assignments.schema.json`: frozen schema contract for `Data/discipline_code_assignments.jsonl`.
- `schema/classification_code_index.schema.json`: frozen schema contract for `Data/classification_code_index.json`.
- `scripts/manage_discipline_code_assignments.py`: owner-maintenance helper for daily discipline-code ledger updates; appends a matching `change_log` row unless `--dry-run` is used.
- together, `field_ownership_matrix.md`, `check_policy.md`, and the two schema files above are the current frozen governance contracts referenced by the structured-data workflow.
- `pdf_manifest.json`: local archived PDF inventory with hashes.
- `missing_pdf_manifest.json`: active confirmed-core papers that remain valid records but currently have no local readable PDF.
- `note_manifest.json`: note-path inventory and note existence flags.
- `field_dictionary.md`: field semantics reference for the structured layer.

## Owner maintenance helpers

Daily export must not write owner fact sources. The corresponding owner-maintenance helpers are explicit commands:

- `scripts/init_discipline_code_assignments.py`
  Initializes `Data/discipline_code_assignments.jsonl` from the reviewed preview; this is for explicit initial ledger creation, not daily export. Use `--dry-run` to preview the initial ledger summary before writing the owner file.
- `scripts/manage_discipline_code_assignments.py`
  Updates the current discipline-code snapshot for one paper in the owner ledger and appends one audit row to `Data/change_log.jsonl`. Use `--dry-run` first when checking a planned reassignment.
- `scripts/manage_classification_code_index.py`
  Maintains `Data/classification_code_index.json` as the taxonomy vocabulary owner, with explicit `sync`, `upsert-primary`, and `upsert-secondary` entry points. For secondary-term updates, it can also append impacted-paper audit rows to `Data/change_log.jsonl` so taxonomy-owner changes that affect derived paper-level provenance stay reviewable. Daily export still only reads this file and must never rewrite it.
- `scripts/init_classification_code_index.py`
  Explicit taxonomy-owner initialization command. It seeds `Data/classification_code_index.json` from the current taxonomy code map plus legacy secondary classes in the master owner file, so taxonomy-owner initialization remains separate from daily export.
- `scripts/manage_progress_tracking.py`
  Updates one row in the progress owner file `Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md` and appends one matching audit row to `Data/change_log.jsonl`. Use this for PDF/source/evidence workflow updates instead of hand-editing derived registries.
- `scripts/manage_master_paper_list.py`
  Updates one row in the master owner file `Paper_Lists/agent_master_paper_list.md` and appends one matching audit row to `Data/change_log.jsonl`. Use this for paper/classification fact updates instead of hand-editing derived outputs.
- `scripts/append_change_log.py`
  Low-level manual audit helper for change types that are not yet covered by a dedicated owner-maintenance command.

## Workflow order

Day-to-day structured-data maintenance should follow the frozen workflow order:

1. change the appropriate owner fact source
2. run `export -> check -> build`
3. review the derived outputs / report

Use:

- `scripts/run_structured_data_pipeline.py`
  Runs the canonical `export_structured_data.py -> check_data_consistency.py -> build_analysis_db.py` sequence from repo root so routine maintenance follows the project workflow instead of ad hoc command order. The preflight step also reports which of the four owner fact sources are currently changed in the worktree and whether `Data/change_log.jsonl` changed alongside them.

## When to use JSONL, CSV, or SQLite

Use `papers.jsonl` when:

- you need the most faithful per-paper record
- array fields must stay as arrays
- you are writing scripts or reviewing exact exported values

Use `papers.csv` or `paper_modules.csv` when:

- you want spreadsheet review, quick filtering, or manual spot checks
- you need a flat table for sharing or lightweight statistics
- you understand that arrays are flattened for convenience

Use `canonical_paper_modules.csv` when:

- you are working with an older notebook or review sheet that still expects the legacy canonical filename
- you want the same canonical rows as `paper_modules.csv` without changing that downstream surface yet

Use `mixed_scope_paper_modules.csv` only when:

- you explicitly need both canonical and workflow-mirror assignment scopes in one flat export
- you are prepared to filter by `assignment_scope` before aggregating

The mixed-scope warning now applies only to the explicit compatibility surfaces:

- `mixed_scope_paper_modules.csv`
- SQLite `mixed_scope_paper_modules`
- SQLite `mixed_scope_module_assignment_counts`

Use `papers.sqlite` when:

- you need stable joins across papers, module assignments, manifests, and metadata
- you are doing repeated analysis or reproducible query work
- you need counts by module, missing-PDF inventory, or paper-level detail without reparsing JSONL

Inside SQLite, the default canonical classification surfaces are:

- `paper_modules`
- `module_assignment_counts`
- compatibility canonical aliases: `canonical_paper_modules`, `canonical_module_assignment_counts`
- workflow audit surfaces: `workflow_mirror_paper_modules`, `workflow_mirror_module_assignment_counts`
- `analysis_object_scope_registry`
- `classification_boundary_analysis`
- `classification_boundary_summary`

Compatibility mixed-scope SQL objects still exist, but they are inspection-only by default:

- `mixed_scope_paper_modules`
- `mixed_scope_module_assignment_counts`

Do not use those mixed-scope objects for canonical statistics unless you are explicitly filtering by `assignment_scope`.

Rule of thumb:

- master + progress own paper/classification and source/PDF workflow facts
- `discipline_code_assignments.jsonl` owns stable code assignment facts
- `classification_code_index.json` owns taxonomy vocabulary facts
- registry is the normalized derived layer
- `papers.jsonl` / manifests / CSV / SQLite are the analysis layer
- CSV is the lightweight human-analysis layer
- SQLite is the durable query/analysis layer

## `query_analysis_db.py` typical usage

All commands below are run from the repository root and read `Data/papers.sqlite`.

Unless a command is explicitly labeled `audit` / `mirror`, classification outputs should be interpreted as canonical-only.

If you need the fixed record-vs-assignment baseline before any module chart or table, start here:

```bash
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" analysis-baseline
```

Show metadata and module counts:

```bash
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" summary
```

Show raw build metadata:

```bash
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" metadata
```

Show only the current discipline registry snapshot provenance metadata:

```bash
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" discipline-registry-metadata
```

Show the current papers snapshot and discipline registry snapshot provenance together:

```bash
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" snapshot-provenance
```

List SQLite object-scope registry rows:

```bash
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" object-scope-registry
```

Show canonical formal-module distribution with shares:

```bash
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" module-distribution
```

Show canonical object-coverage mode counts:

```bash
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" object-coverage-summary
```

Inspect one paper in JSON form:

```bash
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" paper ASD-0001
```

List the active no-local-PDF inventory:

```bash
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" missing-pdf
```

List the active source-limited inventory:

```bash
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" source-limited
```

Show overall coverage / follow-up state summary:

```bash
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" coverage-summary
```

List active multi-module papers:

```bash
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" multi-module
```

List canonical multi-module combinations:

```bash
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" multi-module-combo-summary
```

List papers assigned to a formal module:

```bash
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" module 04
```

Show canonical formal-module PDF coverage:

```bash
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" module-pdf-coverage
```

Show canonical `01.04` general-method bucket summary:

```bash
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" bucket-0104-summary
```

Summarize the current discipline-code snapshot:

```bash
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" discipline-code-summary
```

Inspect one current or historical discipline-local code:

```bash
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" discipline-code 04-03-017
```

Show current secondary-class summary from the discipline registry:

```bash
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" secondary-class-summary
```

Show current secondary-class local-PDF coverage:

```bash
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" secondary-class-pdf-coverage
```

List normalized taxonomy owner terms:

```bash
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" classification-terms --level secondary
```

List canonical general-method bucket records:

```bash
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" general-method-buckets
```

List asset-inventory rows:

```bash
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" paper-assets --asset-type primary_pdf
```

List note-inventory rows:

```bash
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" notes --missing-only
```

Summarize audit rows by `change_type`:

```bash
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" change-log-summary
```

List lightweight audit rows:

```bash
python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" change-log
```

Operational notes:

- `analysis-baseline` is the fixed canonical record-vs-assignment glossary output for the current active confirmed-core snapshot.
- `summary` prints metadata plus canonical formal-module counts from SQLite.
- `metadata` prints the raw build metadata rows loaded into SQLite `metadata`, including both the current `papers.jsonl` export timestamp and the current `discipline_local_code_registry` snapshot metadata (`generated_at`, `generated_by`, `source_commit`, `worktree_dirty`, row count).
- `discipline-registry-metadata` prints just the `discipline_local_code_registry` snapshot provenance rows from SQLite `metadata`.
- `snapshot-provenance` prints the compact cross-snapshot provenance bundle for the current `papers.jsonl` batch plus the current `discipline_local_code_registry` batch.
- `object-scope-registry` prints the current `analysis_object_scope_registry` rows so the declared semantics of SQLite objects can be inspected directly.
- `module-distribution` converts those canonical module counts into a stable distribution table with assignment shares.
- `object-coverage-summary` is the canonical record-level split between `single_module`, `multi_module`, and `general_method_without_concrete_object_experiments`.
- `paper` prints the full structured paper payload, including both canonical fields and workflow-mirror inspection fields; do not treat `final_modules_or_bucket` as canonical.
- `missing-pdf`, `multi-module`, and `module` print tab-separated tables for shell use or redirection.
- `source-limited` prints the active source-limited inventory and can be expanded with `--all` when non-core rows matter.
- `multi-module-combo-summary` is the canonical combination-frequency view for multi-module papers.
- `module-pdf-coverage` is the canonical per-module PDF coverage table.
- `bucket-0104-summary` is the canonical `01.04` bucket count, distinct from the mirror audit command.
- `discipline-code-summary` is the current discipline-code snapshot summary from the ledger-derived registry, grouped by `assignment_status`, primary filing module, and secondary filing code.
- `discipline-code` joins the stable ledger with the current derived registry so one code can be traced through its active / retired / redirected lifecycle context.
- `secondary-class-summary` and `secondary-class-pdf-coverage` are the spreadsheet-friendly secondary-filing review surfaces built from `discipline_local_code_registry` plus taxonomy-owner terms.
- `classification-terms` is the direct taxonomy vocabulary inspection surface for `classification_code_index.json` after it is loaded into SQLite.
- `general-method-buckets` lists canonical `01.04` bucket records from the explicit `paper_general_method_buckets` relation instead of inferring them from mixed-scope module tables.
- `paper-assets` and `notes` expose the normalized asset/note inventory tables for missing-file review, export sanity checks, and downstream maintenance audits.
- `change-log-summary` is the audit summary surface for owner-maintenance activity by `change_type`.
- `change-log` lists raw audit rows from `Data/change_log.jsonl` after they are loaded into SQLite.
- `boundary-cases` and `bucket-summary` are audit commands for canonical-vs-mirror inspection, not default canonical classification summaries.
- If `papers.sqlite` is stale or missing, rerun `build_analysis_db.py` after `export -> check`.

Interpretation guardrails:

- formal `01-11` module rows are expanded assignment counts, not unique-paper counts
- canonical `01.04` bucket statistics are always kept separate from formal `01-11`
- `summary` and `analysis-baseline` should be read together before writing any module count into a report
- `paper_modules.csv` is now canonical-only; if you intentionally need canonical + workflow mirror together, switch to `mixed_scope_paper_modules.csv` or SQLite `mixed_scope_*`

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
- `final_modules_or_bucket` is a workflow mirror, not the canonical classification source.
- PDF truth follows the progress file plus real local file existence.
- `discipline_local_code` truth follows `Data/discipline_code_assignments.jsonl`.
- taxonomy vocabulary truth follows `Data/classification_code_index.json`.
- Daily export only writes derived outputs; owner fact sources require explicit initialization or maintenance flow.
- A passing `check_data_consistency.py` run is the minimum bar before committing structured-data changes.
