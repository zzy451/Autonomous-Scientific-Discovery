# ASD Phase 6 queue refresh after R5 harmonization closeout

Date: 2026-07-02
Round label: `Phase6QueueRefreshAfterR5`

This round does not create new authoritative facts. It refreshes the Phase 6 preparation queues and structured exports so they reflect the already-landed authoritative state after `Phase6FollowupR3` and `Phase6FollowupR5`.

## 1. Why this round was needed

The earlier Phase 6 follow-up rounds already landed authoritative changes in:

- `Paper_Lists/agent_master_paper_list.md`
- `Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`

but the machine-generated Phase 6 preparation queues had not yet been regenerated from the post-R5 structured layer.

As a result, the stale queue family still contained outdated anchors for records such as:

- `ASD-0097`
- `ASD-0112`
- `ASD-0572`
- `ASD-0089`
- `ASD-0091`
- `ASD-0093`

## 2. Read-only agent review

Read-only agents used in this round:

- `Zeno`
  - audited current Phase 6 assets and confirmed that the next natural execution family remains `full_text_followup_queue`, but only after queue refresh
- `Boyle`
  - independently verified the required controller command order and confirmed the current baseline remains `447 / 421 / 26 / drift 0`

No sub-agent edited project files in this round.

## 3. Controller commands executed

The controller ran:

1. `python "Autonomous Scientific Discovery/scripts/export_structured_data.py"`
2. `python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"`
3. `python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"`
4. `python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" summary`
5. `python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" analysis-baseline`
6. `python "Autonomous Scientific Discovery/scripts/generate_phase6_preparation_queues.py"`
7. `python "Autonomous Scientific Discovery/scripts/generate_phase6_round1_packets.py"`

## 4. Verified baseline before queue refresh

The controller re-verified:

- active confirmed-core: `447`
- active local PDFs: `421`
- active no-local-PDF: `26`
- workflow mirror drift count: `0`
- workflow mirror semantic drift count: `0`
- workflow mirror order drift count: `0`

Canonical analysis baseline remained:

- active formal-module assignments: `575`
- active canonical `01.04` bucket assignments: `9`
- active total canonical assignments: `584`

## 5. Refresh results

The refreshed queue family now reflects the current post-R5 structured state.

Observed count changes:

- note revision queue candidates: `177 -> 176`
- full-text follow-up queue candidates: `137 -> 134`
- representative paper pool rows: unchanged at `54`
- module coverage pool rows: unchanged at `11`
- boundary case pool rows: unchanged at `9`

Key semantic corrections now reflected in the refreshed outputs:

- `ASD-0097` now anchors to `06` rather than stale `06;07`
- `ASD-0112` now anchors to `03` rather than stale `03;07`
- `ASD-0572` now appears as `source_limited=yes`
- `ASD-0089`, `ASD-0091`, and `ASD-0093` no longer remain in the stale follow-up positions created before their earlier authoritative/full-text landings

## 6. Files refreshed in this round

- structured exports:
  - `Data/papers.jsonl`
  - `Data/papers.csv`
  - `Data/papers.sqlite`
  - `Data/registry/asset_manifest.jsonl`
  - `Data/registry/classification_assignments.jsonl`
  - `Data/registry/paper_identifier_aliases.jsonl`
  - `Data/registry/paper_registry.jsonl`
  - `Data/registry/pdf_archive_registry.jsonl`
  - `Data/registry/taxonomy_registry.json`
- refreshed Phase 6 preparation assets:
  - `Coverage_Check/structured_data_phase6_note_revision_queue_447_2026-07-02.tsv`
  - `Coverage_Check/structured_data_phase6_full_text_followup_queue_447_2026-07-02.tsv`
  - `Coverage_Check/structured_data_phase6_module_coverage_pool_447_2026-07-02.tsv`
  - `Coverage_Check/structured_data_phase6_preparation_round1_2026-07-02.md`

The round also regenerated the existing Round-1 packet family so future launch packets derive from the refreshed queue state.

## 7. Conclusion

`Phase6QueueRefreshAfterR5` closes the queue-state drift between:

- the already-landed authoritative pair
- the structured export layer
- the Phase 6 preparation queue family

The repository is now ready for the next true Phase 6 production round to launch from refreshed queue assets instead of stale pre-R5 packets.
