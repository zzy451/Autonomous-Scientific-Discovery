# ASD Phase 6 writing support drift refresh round 1 plan

Date: 2026-07-05
Round label: `Phase6WritingSupportDriftRefreshR1Approx`
Execution mode: controller-executed approximate multi-agent round

This round is a bounded note-harmonization follow-up to `Phase6WritingSupportR2Approx`.

## 1. Why this round exists

`Phase6WritingSupportR2Approx` validated a truthful standard `30`-paper representative packet and found:

- `23` rows already `ready_low_risk`
- `7` rows `ready_with_note_drift`

The seven flagged rows are:

- `ASD-0090`
- `ASD-0687`
- `ASD-0653`
- `ASD-0662`
- `ASD-0691`
- `ASD-0693`
- `ASD-0696`

Under the current Phase 6 pool state, no truthful fresh standard `30`-paper packet remains:

- refreshed authoritative-maintenance queues are already below `30`
- the remaining representative pool after the prior `30`-paper packet is also below `30`

Therefore the truthful next step is a bounded `7`-note drift-refresh exception rather than a new standard `3 x 10 = 30` round.

## 2. Why approximate multi-agent mode is used

Real sub-agent tooling is still not exposed in the current session's tool surface.

The controller therefore uses the approved approximate multi-agent fallback while preserving:

- contiguous read-only evidence slices `A/B/C`
- a separate controller-owned classification-review pass over merged evidence
- frozen disjoint writeback ownership before note edits
- Main Controller single-write control over closeout, verification, and git

## 3. Frozen round shape

- bounded exception shape: `7` drift-flagged representative notes
- evidence slices:
  - `Evidence-Agent-A`: `3` notes
  - `Evidence-Agent-B`: `2` notes
  - `Evidence-Agent-C`: `2` notes
- writeback ownership:
  - `Writeback-Agent-1`: `4` notes
  - `Writeback-Agent-2`: `3` notes
- round type: note-only harmonization
- pre-authorized authoritative edits: none outside the owned note files and controller round artifacts

## 4. Scope

Frozen packet in inherited representative-pool order:

- `ASD-0090`
- `ASD-0687`
- `ASD-0653`
- `ASD-0662`
- `ASD-0691`
- `ASD-0693`
- `ASD-0696`

## 5. Round intent

This round does not reopen classification truth. It only aligns note wording with the already landed authoritative state.

Expected refresh scope:

- retire stale `to_read` residue
- retire stale `source_limited` / no-local-PDF residue where the authoritative state is already `source_limited=no`
- preserve all frozen modules, `01.04` decisions, and primary filing choices exactly as already landed
- avoid master-list, progress-tracker, and `Data/` edits
