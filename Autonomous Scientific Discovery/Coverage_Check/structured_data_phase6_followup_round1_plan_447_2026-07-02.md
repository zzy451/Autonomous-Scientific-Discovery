# ASD Phase 6 follow-up round 1 packet plan

Date: 2026-07-02
Round label: `Phase6FollowupR1`

This plan converts the previously generated Phase 6 preparation queues into a concrete first-round packet set for future multi-agent execution. No authoritative files are changed by this step.

## Scope selected for round 1

Round 1 uses the top `30` rows from:

- `Coverage_Check\structured_data_phase6_full_text_followup_queue_447_2026-07-02.tsv`

The queue is already priority-sorted. This round intentionally does **not** attempt to clear all `137` follow-up candidates at once.

## Why only 30 papers

1. The highest-priority part of the queue already contains the strongest pressure signals:
   - no local PDF
   - `source_limited=yes`
   - non-full-text evidence
2. The top 30 includes the full `26` no-local-PDF frontier plus the first `4` source-limited local-PDF records, which is enough to exercise a parallel evidence round without overloading merge review.
3. This keeps the next real multi-agent round aligned with the established `3 x 10` evidence-slice pattern.

## Slice allocation

- `Evidence-Agent-A`: `Coverage_Check\structured_data_phase6_followup_round1_slice_A_447_2026-07-02.tsv`
- `Evidence-Agent-B`: `Coverage_Check\structured_data_phase6_followup_round1_slice_B_447_2026-07-02.tsv`
- `Evidence-Agent-C`: `Coverage_Check\structured_data_phase6_followup_round1_slice_C_447_2026-07-02.tsv`

### Slice A profile

- highest-pressure mixed chemistry / materials / bio rows
- includes the earliest no-local-PDF and source-limited multi-module frontier

### Slice B profile

- remaining no-local-PDF frontier
- extends into modules `05`, `06`, `07`, `10`, `11`

### Slice C profile

- tail of no-local-PDF frontier plus the first local-PDF source-limited cases
- includes `01.04`, `01`, `02`, `03` boundary-sensitive follow-up items

## Writing-support sidecar selection

For writing support, this round prioritizes modules that are both consequential and clean enough to support immediate drafting:

- `04` Materials Science
- `03` Chemical Sciences
- `07` Medical and Health Sciences
- `09` Engineering and Industrial Technology Sciences
- `02` Physics, Astronomy and Cosmic Sciences

Outputs:

- `Coverage_Check\structured_data_phase6_writing_support_round1_modules_447_2026-07-02.tsv`
- `Coverage_Check\structured_data_phase6_writing_support_round1_representatives_447_2026-07-02.tsv`

These are not writeback packets. They are writing-support packets for future section drafting, representative-example selection, and coverage planning.

## Main-controller note

The generated slices and support packets are planning artifacts only. Any future execution round still has to follow:

- single-writer authoritative updates
- read-only evidence collection by sub-agents
- explicit packet launch
- explicit closeout and post-round git discipline
