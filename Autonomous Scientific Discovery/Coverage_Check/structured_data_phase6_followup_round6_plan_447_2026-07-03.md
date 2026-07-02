# ASD Phase 6 follow-up round 6 packet plan

Date: 2026-07-03
Round label: `Phase6FollowupR6`

This plan freezes a new bounded Phase 6 evidence round after the queue refresh and the note-revision round 1 closeout. No authoritative files are changed by this packetization step.

## 1. Why this round exists

Current repo state already proves:

- queue refresh after `R5` is complete
- note revision round 1 is complete
- the baseline remains `447 / 421 / 26 / canonical 01.04 = 9 / drift 0`

The next natural controller action is therefore not another governance-doc round, but a fresh bounded evidence round launched from the refreshed full-text follow-up pressure frontier.

## 2. Focus-set selection rule

This round uses the refreshed:

- `Coverage_Check/structured_data_phase6_full_text_followup_queue_447_2026-07-02.tsv`

The queue is used only to identify the highest-pressure follow-up frontier. It is **not** treated as authoritative work-selection truth.

Controller decision:

- freeze a bounded 6-paper focus set from the current top queue pressure
- then reorder that set by current master-row order for actual execution

## 3. Frozen focus set

Queue-derived focus set:

- `ASD-0005`
- `ASD-0158`
- `ASD-0097`
- `ASD-0112`
- `ASD-0381`
- `ASD-0603`

Execution order for this round, after controller re-check against current master row order:

1. `ASD-0005`
2. `ASD-0097`
3. `ASD-0112`
4. `ASD-0158`
5. `ASD-0381`
6. `ASD-0603`

Why this set is worth a bounded round:

1. all 6 remain `no local PDF`
2. all 6 remain `source_limited=yes`
3. all 6 still rely on non-full-text evidence states
4. 4 of the 6 are chemistry automation / robotic-lab anchors whose first-hand access status may still move
5. `ASD-0097` and `ASD-0112` already had recent harmonization pressure and are good checks on whether the refreshed queue and authoritative state stay aligned under another evidence pass

## 4. Execution shape

This round uses the standard three-evidence-agent topology, but at bounded `3 x 2` scale.

Owned slices:

- `Evidence-Agent-A`
  - `Coverage_Check/structured_data_phase6_followup_round6_slice_A_447_2026-07-03.tsv`
- `Evidence-Agent-B`
  - `Coverage_Check/structured_data_phase6_followup_round6_slice_B_447_2026-07-03.tsv`
- `Evidence-Agent-C`
  - `Coverage_Check/structured_data_phase6_followup_round6_slice_C_447_2026-07-03.tsv`

## 5. Ownership discipline

This round is evidence-only at launch:

- `Evidence-Agent-A/B/C` are read-only
- no sub-agent may edit master, progress, report, notes, or `Reference_PDF/`
- a later writeback or archive step is allowed only if the controller freezes a landing subset after evidence merge and classification review

## 6. Main questions for this round

Each evidence slice should try to answer:

1. Is a stronger first-hand source now accessible than the currently recorded abstract / preview / metadata state?
2. Can a legal local PDF now be archived, or does the paper remain no-local-PDF?
3. Does the current authoritative module anchor still hold under refreshed first-hand evidence?
4. Is there any stronger object-level evidence that would justify note-only refresh or a future authoritative update?
5. Does the current `source_limited=yes` state still remain the right conservative reading?

## 7. Expected follow-up after evidence

If all three evidence packets return cleanly, the next controller step should be:

1. merge the evidence rows
2. launch one read-only `Classification-Reviewer`
3. decide whether this round is:
   - evidence-only and conservative-hold, or
   - note-only follow-up, or
   - authoritative landing candidate

Until that controller decision is frozen:

- no note writeback starts
- no archive write starts
- no authoritative file is edited
