# Structured Data Execution Definition Audit

Plan: `Coverage_Check\structured_data_long_term_catalog_and_index_plan_2026-07-05.md`

## Summary

- `PASS`: 12
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

discipline_local_code_registry is present in JSONL / CSV / SQLite with aligned derived snapshot metadata.

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
