# ASD Phase 6 queue refresh after R6 closeout

Date: 2026-07-03
Round label: `Phase6QueueRefreshAfterR6`

This round does not create new authoritative facts. It refreshes the structured queue and packet layer so it reflects the already-landed authoritative state after `Phase6FollowupR6`.

## 1. Why this round was needed

`Phase6FollowupR6` landed one real authoritative delta:

- `ASD-0381`
  - keep `scientific_object_modules=03`
  - change `source_limited=yes -> no`
  - change evidence state from preview/metadata to `first_hand_html_full_text_and_supplementary`

That change should not remain trapped only in:

- `Paper_Lists/agent_master_paper_list.md`
- `Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`
- the updated note

It also has to propagate into the machine-generated Phase 6 preparation assets before those assets are reused for another evidence or note round.

## 2. Read-only audit stage

Read-only agents used in this round:

- `Aristotle`
  - verified the post-R6 baseline remained `447 / 421 / 26 / canonical 01.04 = 9 / drift 0`
  - confirmed the repo carried one real R6 delta that warranted queue-layer propagation
- `Huygens`
  - verified that `ASD-0381` should drop out of the high-pressure full-text frontier and out of the note-revision frontier after refresh
  - highlighted that `ASD-0569` becomes the cleanest non-safety replacement for the vacated high-pressure slot

No sub-agent edited project files in this round.

Completed agents were closed at round end.

## 3. Controller commands executed

The controller ran these commands in this round:

1. `python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"`
2. `python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" summary`
3. `python "Autonomous Scientific Discovery/scripts/generate_phase6_preparation_queues.py"`
4. `python "Autonomous Scientific Discovery/scripts/generate_phase6_round1_packets.py"`
5. after detecting a stale downstream packet read, patch `scripts/generate_phase6_round1_packets.py` to remove hardcoded queue counts and make the plan text dynamic
6. rerun `python "Autonomous Scientific Discovery/scripts/generate_phase6_round1_packets.py"` serially
7. `python "Autonomous Scientific Discovery/scripts/export_structured_data.py"`
8. `python "Autonomous Scientific Discovery/scripts/check_data_consistency.py"`
9. `python "Autonomous Scientific Discovery/scripts/build_analysis_db.py"`
10. `python "Autonomous Scientific Discovery/scripts/query_analysis_db.py" summary`

## 4. Honesty note on packet regeneration

The controller initially parallelized:

- queue regeneration
- packet regeneration

That first controller attempt was not safe enough, because packet regeneration may read the old queue before the refreshed queue file finishes writing.

Observed symptom:

- the refreshed full-text queue already demoted `ASD-0381`
- but the first regenerated `structured_data_phase6_followup_round1_slice_A_447_2026-07-02.tsv` still contained the stale pre-R6 `ASD-0381` row

The controller did **not** keep that stale packet family.

What happened instead:

1. the mismatch was explicitly checked
2. the packet-generation script was patched to remove the stale hardcoded `137` queue-count wording
3. packet regeneration was rerun serially after queue regeneration

The final refreshed packet family in this round is therefore the post-correction serial output, not the first stale intermediate output.

## 5. Verified baseline

Serial controller verification confirmed the baseline is still:

- active confirmed-core: `447`
- active local PDFs: `421`
- active no-local-PDF: `26`
- canonical `01.04` bucket count: `9`
- workflow mirror drift count: `0`
- workflow mirror semantic drift count: `0`
- workflow mirror order drift count: `0`

Consistency checks passed.

## 6. Refresh results

### 6.1 Queue-family count changes

Observed count changes after the R6 delta:

- note revision queue candidates: `176 -> 175`
- full-text follow-up queue candidates: unchanged at `134`
- representative paper pool rows: unchanged at `54`
- module coverage pool rows: unchanged at `11`
- boundary case pool rows: unchanged at `9`

### 6.2 Semantic changes now reflected

Key queue-layer corrections now visible:

- `ASD-0381` is removed from the note-revision queue
- `ASD-0381` is removed from the top high-pressure follow-up frontier
- `ASD-0381` now appears later in the full-text queue as:
  - `evidence_status=first_hand_html_full_text_and_supplementary`
  - `source_limited=no`
  - `followup_reasons=no_local_pdf`
  - `priority_score=55`
- the chemical module coverage summary now records:
  - `active_source_limited_count: 12 -> 11`
- the refreshed reusable `followup_round1` queue/slice/plan layer now drops stale `ASD-0381` from slice A
- the refreshed `followup_round1` plan text now uses dynamic queue counts instead of the stale hardcoded `137`

## 7. Files refreshed in this round

Structured exports / analysis outputs:

- `Data/papers.jsonl`
- `Data/papers.csv`
- `Data/papers.sqlite`
- `Data/registry/asset_manifest.jsonl`
- `Data/registry/classification_assignments.jsonl`
- `Data/registry/paper_identifier_aliases.jsonl`
- `Data/registry/paper_registry.jsonl`
- `Data/registry/pdf_archive_registry.jsonl`
- `Data/registry/taxonomy_registry.json`

Phase 6 queue / pool assets:

- `Coverage_Check/structured_data_phase6_note_revision_queue_447_2026-07-02.tsv`
- `Coverage_Check/structured_data_phase6_full_text_followup_queue_447_2026-07-02.tsv`
- `Coverage_Check/structured_data_phase6_module_coverage_pool_447_2026-07-02.tsv`
- `Coverage_Check/structured_data_phase6_preparation_round1_2026-07-02.md`

Refreshed downstream packet family:

- `Coverage_Check/structured_data_phase6_followup_round1_slice_A_447_2026-07-02.tsv`
- `Coverage_Check/structured_data_phase6_followup_round1_slice_C_447_2026-07-02.tsv`
- `Coverage_Check/structured_data_phase6_followup_round1_plan_447_2026-07-02.md`
- `Coverage_Check/structured_data_phase6_writing_support_round1_modules_447_2026-07-02.tsv`

Historical round-1 artifacts outside this regenerated reusable queue/slice/plan layer were not separately rewritten in this closeout.

Script hardening landed in this round:

- `scripts/generate_phase6_round1_packets.py`

## 8. Controller takeaway for the next packet

After refresh, `ASD-0381` should no longer be treated as a high-pressure follow-up frontier paper.

If the next bounded full-text packet wants a clean non-safety replacement for the vacated slot, the strongest default candidate is:

- `ASD-0569`

If chemistry continuity is valued more than raw queue pressure, that should be recorded as an explicit controller override rather than silently pretending the refreshed queue still supports the old `ASD-0381` packet position.

## 9. Conclusion

`Phase6QueueRefreshAfterR6` closes the state drift between:

- the authoritative layer after `Phase6FollowupR6`
- the Phase 6 preparation queues
- the downstream packet family that future controller rounds may reuse

The baseline did not move.

The real outcome of this round is narrower and important:

- one landed R6 evidence delta is now propagated through the queue layer
- stale downstream packetization was detected honestly
- the packet-generation path was corrected and rerun serially
