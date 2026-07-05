# ASD Phase 6 follow-up round 21 plan

Date: 2026-07-05
Round label: `Phase6FollowupR21`

This round continues the post-R20 Phase 6 follow-up line using the standard real multi-agent shape:

- `30` papers per round
- `Evidence-Agent-A/B/C` each own `10` papers
- the round is refrozen from the current post-R20 queue with freshness override

## 1. Scope

Frozen 30-paper focus set in current queue order after skipping all 30 papers from R19 and all 30 papers from R20:

- `ASD-0737`
- `ASD-0738`
- `ASD-0549`
- `ASD-0567`
- `ASD-0613`
- `ASD-0707`
- `ASD-0748`
- `ASD-0750`
- `ASD-0734`
- `ASD-0535`
- `ASD-0570`
- `ASD-0571`
- `ASD-0614`
- `ASD-0635`
- `ASD-0651`
- `ASD-0725`
- `ASD-0728`
- `ASD-0729`
- `ASD-0731`
- `ASD-0526`
- `ASD-0747`
- `ASD-0749`
- `ASD-0753`
- `ASD-0754`
- `ASD-0647`
- `ASD-0648`
- `ASD-0625`
- `ASD-0626`
- `ASD-0629`
- `ASD-0636`

## 2. Why this round exists

The refreshed post-R20 queue now exposes the next contiguous pocket of records whose authoritative module direction is already mostly stable, but whose current source-state or note wording still rests on abstract-heavy / packet-only evidence labels.

This round therefore follows the current plan stack exactly:

- refreeze from the current queue rather than reuse stale packets
- skip all 30 papers from R19
- skip all 30 papers from R20
- keep evidence collection read-only
- do not hard-fight impossible PDF routes
- when PDF is unavailable, preserve truthful HTML / abstract / official-page evidence only
- if current local archived PDFs or first-hand full text are enough to clear stale queue pressure, land only the rows that can be upgraded truthfully

## 3. Real multi-agent topology

- `Evidence-Agent-A` ownership: the first `10` papers in slice A
- `Evidence-Agent-B` ownership: the next `10` papers in slice B
- `Evidence-Agent-C` ownership: the final `10` papers in slice C
- `Classification-Reviewer`: independent adjudication from merged evidence only

No `PDF-Archive-Agent` ownership is frozen at launch time. Any paper without a realistically obtainable PDF should remain conservative and source-truthful instead of being hard-pushed through repeated PDF retrieval attempts.

## 4. Controller discipline

- evidence slices are read-only
- merged evidence is controller-owned
- adjudication is reviewer-owned from merged evidence only
- writeback starts only after the landing subset is frozen
- only the controller may edit master / progress / closeout / git
- closeout must state that this was a real multi-agent round and must explicitly close all launched agent handles
