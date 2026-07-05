# ASD Phase 6 follow-up round 20 plan

Date: 2026-07-05
Round label: `Phase6FollowupR20`

This round continues the post-R19 Phase 6 follow-up line using the restored standard real multi-agent shape:

- `30` papers per round
- `Evidence-Agent-A/B/C` each own `10` papers
- the round is refrozen from the current post-R19 queue with freshness override

## 1. Scope

Frozen 30-paper focus set in current queue order after skipping all R19 papers:

- `ASD-0743`
- `ASD-0744`
- `ASD-0745`
- `ASD-0770`
- `ASD-0531`
- `ASD-0543`
- `ASD-0545`
- `ASD-0554`
- `ASD-0556`
- `ASD-0052`
- `ASD-0775`
- `ASD-0652`
- `ASD-0655`
- `ASD-0701`
- `ASD-0766`
- `ASD-0768`
- `ASD-0035`
- `ASD-0525`
- `ASD-0680`
- `ASD-0681`
- `ASD-0683`
- `ASD-0649`
- `ASD-0650`
- `ASD-0034`
- `ASD-0678`
- `ASD-0716`
- `ASD-0510`
- `ASD-0645`
- `ASD-0524`
- `ASD-0736`

## 2. Why this round exists

The refreshed post-R19 queue still contains a broad mix of:

- `archived_pdf + source_limited=yes` rows that need current first-hand rechecks
- multi-module boundary rows whose current note / master wording may still depend on abstract-heavy evidence
- strong object-stable rows where truthful HTML / abstract / official-page evidence may be enough to refine source-state without overclaiming PDF access

This round therefore follows the current plan stack exactly:

- refreeze from the current queue rather than reuse stale packets
- skip all 30 papers from R19
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
