# Structured Data Execution Definition Audit

Plan: `Coverage_Check\structured_data_long_term_catalog_and_index_plan_2026-07-05.md`

## Summary

- `PASS`: 23
- `FAIL`: 0

## Items

### Item 1 - PASS

All 871 papers use unique ASD-xxxx paper_id values.

Evidence: `Data/papers.jsonl`

### Item 2 - PASS

All 871 papers carry structured classification fields, with 1012 classification assignment rows aligned to SQLite paper_modules=843 and paper_general_method_buckets=169.

Evidence: `Data/papers.jsonl + Data/registry/classification_assignments.jsonl + Data/papers.sqlite`

### Item 3 - PASS

All 871 papers carry structured evidence-status fields, with 871 pdf_archive_registry rows mirrored into SQLite pdf_evidence_status.

Evidence: `Data/papers.jsonl + Data/registry/pdf_archive_registry.jsonl + Data/papers.sqlite`

### Item 4 - PASS

classification_code_index.json exists and exposes non-empty taxonomy-owner primary/secondary term structures with definition/include/exclude/status/source fields.

Evidence: `Data/classification_code_index.json`

### Item 5 - PASS

discipline_code_assignments current snapshot covers all 447 active papers with valid current-status semantics (active=423, pending=15, general_method=9).

Evidence: `Data/discipline_code_assignments.jsonl`

### Item 6 - PASS

Stable discipline code assignment ledger exists with unique DCA assignment IDs, valid assignment statuses, and auditable assignment metadata fields.

Evidence: `Data/discipline_code_assignments.jsonl`

### Item 7 - PASS

classification_code_index.json is present as taxonomy vocabulary owner and mirrors into SQLite classification_terms=52.

Evidence: `Data/classification_code_index.json + Data/papers.sqlite`

### Item 8 - PASS

discipline_code_initial_assignment_preview.csv matches the active-paper review surface and obeys preview assignment rules (active=423, pending=15, general_method=9).

Evidence: `Data/discipline_code_initial_assignment_preview.csv`

### Item 9 - PASS

discipline_local_code_registry is present in JSONL / CSV / SQLite with aligned derived snapshot metadata and current-snapshot semantics (active=423, pending=15, general_method=9).

Evidence: `Data/discipline_local_code_registry.jsonl + Data/discipline_local_code_registry.csv + Data/papers.sqlite`

### Item 10 - PASS

README references the frozen ownership matrix, assignment/filing policies, check policy, and both schema contracts, and those governance files exist.

Evidence: `Data/README.md + Data/field_ownership_matrix.md + Data/discipline_code_assignment_policy.md + Data/primary_filing_policy.md + Data/check_policy.md + Data/schema/*.json`

### Item 11 - PASS

Consistency checking emits structured severity summaries, finding-code summary, and detail rows with identifiers, fields, and owner-file attribution.

Evidence: `Data/integrity_check_report.md`

### Item 12 - PASS

The owner fact source -> export -> check -> build workflow is documented in README and exposed via a canonical pipeline script with preflight owner summary and optional execution audit.

Evidence: `scripts/run_structured_data_pipeline.py + Data/README.md`

### Item 13 - PASS

SQLite analysis DB contains all named core tables from the long-term plan: classification_terms, discipline_code_assignments, discipline_local_code_registry, notes, paper_assets, paper_general_method_buckets, paper_modules, papers, pdf_evidence_status.

Evidence: `Data/papers.sqlite`

### Item 14 - PASS

README and field_dictionary both document the four fact-source model and explicitly name master, progress, discipline-code ledger, and taxonomy-owner files.

Evidence: `Data/README.md + Data/field_dictionary.md`

### Item 15 - PASS

query_analysis_db.py exposes the named discipline/secondary-class query surfaces and README documents those commands for current structured-data querying.

Evidence: `scripts/query_analysis_db.py + Data/README.md`

### Item 16 - PASS

export_structured_data.py and build_analysis_db.py both carry explicit owner-path write guardrails for discipline_code_assignments.jsonl, classification_code_index.json, and change_log.jsonl, and README documents the same protection.

Evidence: `scripts/export_structured_data.py + scripts/build_analysis_db.py + Data/README.md`

### Item 17 - PASS

change_log.jsonl exists as a populated owner audit ledger, mirrors into SQLite change_log=13, and the change-log query surfaces are documented and exposed.

Evidence: `Data/change_log.jsonl + Data/papers.sqlite + scripts/query_analysis_db.py + Data/README.md`

### Item 18 - PASS

Explicit owner-maintenance helper commands exist for discipline-code, taxonomy, progress, master, and direct change-log updates, and README documents those operational entry points.

Evidence: `scripts/manage_*.py + scripts/append_change_log.py + Data/README.md`

### Item 19 - PASS

field_ownership_matrix.md encodes the canonical master-derived fallback/trace contract and the owner-vs-derived repair rule for discipline-code and taxonomy owner files.

Evidence: `Data/field_ownership_matrix.md`

### Item 20 - PASS

check_policy.md defines the frozen ERROR/WARNING/INFO build semantics, and check_data_consistency.py enforces schema-backed owner validation plus the same severity buckets.

Evidence: `Data/check_policy.md + scripts/check_data_consistency.py`

### Item 21 - PASS

Derived lifecycle fields are populated across all 871 papers, mirror into SQLite papers=871, and the lifecycle query surfaces are documented and exposed (active=447, background=371, excluded=22, duplicate=31).

Evidence: `Data/papers.jsonl + Data/papers.sqlite + scripts/query_analysis_db.py + Data/README.md`

### Item 22 - PASS

SQLite metadata carries the current papers/registry provenance bundle and the metadata / discipline-registry-metadata / snapshot-provenance query surfaces are documented and exposed.

Evidence: `Data/papers.sqlite + scripts/query_analysis_db.py + Data/README.md`

### Item 23 - PASS

Evidence/asset/note inventory surfaces are populated, mirrored into SQLite, and queryable via the documented missing-pdf/source-limited/coverage-summary/paper-assets/notes commands (assets=1742, notes=871, pdf_inventory=426, missing_pdf_inventory=25).

Evidence: `Data/pdf_manifest.json + Data/missing_pdf_manifest.json + Data/note_manifest.json + Data/registry/asset_manifest.jsonl + Data/papers.sqlite + scripts/query_analysis_db.py + Data/README.md`
