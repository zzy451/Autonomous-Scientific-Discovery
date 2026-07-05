# ASD Phase 6 follow-up round 19 plan

Date: 2026-07-05
Round label: `Phase6FollowupR19`

This round continues the post-R18 Phase 6 follow-up line using the restored standard real multi-agent shape:

- `30` papers per round
- `Evidence-Agent-A/B/C` each own `10` papers
- the round is frozen from the current post-R18 queue in contiguous row order

## 1. Scope

Frozen 30-paper focus set in current queue order:

- `ASD-0005`
- `ASD-0158`
- `ASD-0097`
- `ASD-0112`
- `ASD-0603`
- `ASD-0547`
- `ASD-0569`
- `ASD-0572`
- `ASD-0727`
- `ASD-0859`
- `ASD-0860`
- `ASD-0861`
- `ASD-0617`
- `ASD-0724`
- `ASD-0536`
- `ASD-0544`
- `ASD-0858`
- `ASD-0855`
- `ASD-0508`
- `ASD-0565`
- `ASD-0631`
- `ASD-0381`
- `ASD-0609`
- `ASD-0592`
- `ASD-0854`
- `ASD-0541`
- `ASD-0553`
- `ASD-0466`
- `ASD-0599`
- `ASD-0741`

## 2. Why this round exists

The post-R18 queue still contains mixed follow-up pressure:

- hard `no_local_pdf + source_limited` rows that should be checked conservatively and skipped when the PDF route still cannot be recovered
- already-true but still queue-exposed rows whose first-hand evidence should be re-read from accessible HTML / official page / abstract sources
- `archived_pdf + source_limited=yes` rows at the tail of this packet that are high-probability candidates for authoritative evidence upgrades

This round therefore follows the current plan stack exactly:

- freeze from the current queue in contiguous order
- keep evidence collection read-only
- do not hard-fight impossible PDF routes
- when PDF is unavailable, preserve truthful HTML / abstract / official-page evidence only

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
