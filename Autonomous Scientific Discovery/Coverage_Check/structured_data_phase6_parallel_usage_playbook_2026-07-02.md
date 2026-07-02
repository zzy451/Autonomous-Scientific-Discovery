# ASD Phase 6 parallel usage playbook

Date: 2026-07-02
Scope: post-Phase-5 writing-support and follow-up parallel production assets

This document turns the current Phase 6 outputs into a reusable controller-facing playbook. It does not create new authoritative facts. It explains which files now exist, what each one is for, how they relate to each other, and which ones are safe to use for future parallel work.

## 1. Current Phase 6 asset families

Phase 6 currently has four layers of assets:

1. preparation queues and pools
2. round-1 packetization outputs
3. historical follow-up round closeouts
4. scripts that regenerate or repacketize the assets

## 2. Source scripts

Current Phase 6 machine-generated assets come from:

- `scripts/generate_phase6_preparation_queues.py`
- `scripts/generate_phase6_round1_packets.py`

Current generated queue family:

- `Coverage_Check/structured_data_phase6_note_revision_queue_447_2026-07-02.tsv`
- `Coverage_Check/structured_data_phase6_full_text_followup_queue_447_2026-07-02.tsv`
- `Coverage_Check/structured_data_phase6_representative_paper_pool_447_2026-07-02.tsv`
- `Coverage_Check/structured_data_phase6_module_coverage_pool_447_2026-07-02.tsv`
- `Coverage_Check/structured_data_phase6_boundary_case_pool_447_2026-07-02.tsv`
- `Coverage_Check/structured_data_phase6_preparation_round1_2026-07-02.md`

Current packetization family:

- `Coverage_Check/structured_data_phase6_followup_round1_slice_A_447_2026-07-02.tsv`
- `Coverage_Check/structured_data_phase6_followup_round1_slice_B_447_2026-07-02.tsv`
- `Coverage_Check/structured_data_phase6_followup_round1_slice_C_447_2026-07-02.tsv`
- `Coverage_Check/structured_data_phase6_writing_support_round1_modules_447_2026-07-02.tsv`
- `Coverage_Check/structured_data_phase6_writing_support_round1_representatives_447_2026-07-02.tsv`
- `Coverage_Check/structured_data_phase6_followup_round1_plan_447_2026-07-02.md`

## 3. What each queue means

### 3.1 note revision queue

File:

- `structured_data_phase6_note_revision_queue_447_2026-07-02.tsv`

Use this when the next task is note-wording cleanup or note rewrite prioritization.

Guaranteed anchors:

- `paper_id`
- `note_path`
- `classification_anchor`
- `object_coverage_mode`
- `queue_reasons`

Safe interpretation:

- planning aid for note wording pressure
- not proof that a note is wrong

### 3.2 full-text follow-up queue

File:

- `structured_data_phase6_full_text_followup_queue_447_2026-07-02.tsv`

Use this when the next task is evidence refresh, PDF acquisition, or source-limited follow-up.

Guaranteed anchors:

- `paper_id`
- `classification_anchor`
- `pdf_status`
- `evidence_status`
- `source_limited`
- `followup_reasons`

Safe interpretation:

- canonical follow-up queue for access/evidence pressure
- not direct authority to change classification

### 3.3 representative paper pool

File:

- `structured_data_phase6_representative_paper_pool_447_2026-07-02.tsv`

Use this when drafting module subsections, selecting exemplars, or building section-level writing packets.

Guaranteed anchors:

- `module_code`
- `module_rank`
- `paper_id`
- `representative_score`
- `score_reasons`

Safe interpretation:

- heuristic writing-support pool
- not “best paper” truth

### 3.4 module coverage pool

File:

- `structured_data_phase6_module_coverage_pool_447_2026-07-02.tsv`

Use this when deciding which modules are writing-ready, PDF-poor, or source-limited-heavy.

Guaranteed anchors:

- `module_code`
- `active_assignment_count`
- `active_local_pdf_count`
- `active_missing_local_pdf_count`
- `active_source_limited_count`

Safe interpretation:

- staffing/readiness summary
- not a direct writeback queue

### 3.5 boundary case pool

File:

- `structured_data_phase6_boundary_case_pool_447_2026-07-02.tsv`

Use this when you need a watchlist of canonical-vs-mirror edge cases.

Current role under drift = `0`:

- mostly an `acceptable_mirror` watchlist
- not an active semantic-drift backlog

## 4. Recommended usage order

Future controller rounds should use Phase 6 assets in this order:

1. choose the task family:
   - note wording -> note revision queue
   - evidence / PDF / source-limited -> follow-up queue
   - writing examples -> representative pool
   - module staffing -> module coverage pool
   - canonical-vs-mirror watchlist -> boundary pool
2. if follow-up work is selected, start from:
   - `structured_data_phase6_followup_round1_plan_447_2026-07-02.md`
   - and the slice A / B / C packets
3. if writing support is selected, start from:
   - `structured_data_phase6_writing_support_round1_modules_447_2026-07-02.tsv`
   - `structured_data_phase6_writing_support_round1_representatives_447_2026-07-02.tsv`
4. if a future round lands note or authoritative changes, return to:
   - `export -> check -> build`

## 5. What the historical follow-up rounds already prove

Current historical Phase 6 rounds already show that the packet family is executable rather than hypothetical.

Key evidence:

- packet planning:
  - `structured_data_phase6_followup_round1_plan_447_2026-07-02.md`
- launch honesty and concurrency handling:
  - `structured_data_phase6_followup_round1_launch_status_2026-07-02.md`
- evidence/classification closeout:
  - `structured_data_phase6_followup_round1_closeout_2026-07-02.md`
- writeback + authoritative landing:
  - `structured_data_phase6_followup_round3_writeback_and_authoritative_closeout_2026-07-02.md`
- harmonization frontier closeout:
  - `structured_data_phase6_followup_round5_harmonization_closeout_2026-07-02.md`

What these files prove:

- queues can be packetized into disjoint slices
- packet execution can survive concurrency-limit delays if the controller records them honestly
- landed writeback still has to return to single-writer master/progress closeout
- Phase 6 is a planning-and-production layer on top of the stable `447 / 421 / 26` baseline, not a replacement for it

## 6. What these assets are not allowed to do

No Phase 6 queue, pool, packet, or closeout file directly authorizes edits to:

- `Paper_Lists/agent_master_paper_list.md`
- `Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`
- `Data/`

They are planning aids, packet aids, and closeout aids only.

## 7. Current practical reading of Phase 6 readiness

As of the current repo state:

- the five core queues/pools exist
- the queue-generation and round-1 packetization scripts exist
- the first follow-up and writeback rounds already have dated closeouts
- the repository therefore has a reusable Phase 6 parallel-production substrate

The main remaining controller discipline is not asset creation, but correct use:

- choose the right queue for the task
- keep sub-agents read-only unless note writeback ownership is explicitly frozen
- keep authoritative landing single-writer
- close agents at round end

## 8. Controller takeaway

Use this document as the Phase 6 entry point.

If a future round starts with:

- “which queue should I launch from?”
- “which packet file is the first real evidence packet?”
- “can I use this TSV directly to edit master?”

the answer should now be recoverable from this playbook alone.
