# ASD Phase 6 preparation queues and pools

Date: 2026-07-02

This file records the first machine-generated Phase 6 preparation outputs derived from the current canonical structured layer. These are candidate coordination assets, not direct writeback authority.

## Generated outputs

- `Coverage_Check\structured_data_phase6_note_revision_queue_447_2026-07-02.tsv`
- `Coverage_Check\structured_data_phase6_full_text_followup_queue_447_2026-07-02.tsv`
- `Coverage_Check\structured_data_phase6_representative_paper_pool_447_2026-07-02.tsv`
- `Coverage_Check\structured_data_phase6_module_coverage_pool_447_2026-07-02.tsv`
- `Coverage_Check\structured_data_phase6_boundary_case_pool_447_2026-07-02.tsv`

## Current counts

- note revision queue candidates: `171`
- full-text follow-up queue candidates: `129`
- representative paper pool rows: `54`
- module coverage pool rows: `11`
- boundary case pool rows: `9`

## Queue semantics

### note revision queue

Heuristic candidate queue for records whose Notes are most likely to need wording refresh before future writeback. Current triggers are:

- `multi_module`
- independent `01.04` bucket
- `updated_source_limited`
- `source_limited=yes`

This queue does not prove a Note is wrong. It is a prioritization aid.

### full-text follow-up queue

Canonical follow-up queue for active confirmed-core records with one or more of:

- no local PDF
- `source_limited=yes`
- non-full-text evidence status

### representative paper pool

Per-module top-5 candidate papers for writing support. Ranking is heuristic and combines:

- citation priority
- evidence status
- local PDF
- local Note
- source-limited status
- primary filing match

### module coverage pool

Per-formal-module canonical coverage summary for staffing and writing readiness.

### boundary case pool

Current canonical-vs-mirror boundary pool. With drift currently cleared, this pool mostly functions as an `acceptable_mirror` watchlist rather than an active drift backlog.

## Important constraint

These outputs are planning aids for future parallel work. They do not authorize direct edits to:

- `Paper_Lists/agent_master_paper_list.md`
- `Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`
- `Data/`

Any future writeback still has to follow the single-writer and `export -> check -> build` discipline.
