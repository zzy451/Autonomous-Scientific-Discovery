# ASD Phase 6 follow-up round 13 plan

Date: 2026-07-04
Round label: `Phase6FollowupR13Approx`

This round continues the bounded Phase 6 follow-up line after `Phase6FollowupR12Approx`, again using an approximate multi-agent flow because real sub-agent tooling is still unavailable in this environment.

## 1. Scope

Frozen focus set:

- `ASD-0572`
- `ASD-0617`
- `ASD-0727`
- `ASD-0859`
- `ASD-0860`
- `ASD-0861`

## 2. Why this round exists

After `R12Approx` cleared the current local-PDF source-limited pocket, the refreshed post-R12 queue again exposes a bounded six-paper no-local-PDF / non-full-text frontier:

- one materials-plus-life cross-module self-driving lab row
- one programmable protein-evolution lab row
- one geospatial / Earth-observation framework row
- three EO-1 autonomous science application rows

This makes `R13` the cleanest next packet for testing whether official HTML, repository PDF, preprint PDF, or other first-hand sources can now retire stale `source_limited=yes` pressure without reopening stable module anchors.

## 3. Round questions

1. Can any of these six rows now be advanced from abstract / landing-page evidence to first-hand full-text or archived-PDF evidence?
2. Do the current module anchors remain stable under a fresh source check?
3. Which notes would need wording refresh if any authoritative landing becomes supportable?
4. Is the landed subset empty, partial, or full once fresh first-hand access is rechecked?

## 4. Approximate role topology

- `Evidence-Agent-A` ownership: `ASD-0572`, `ASD-0617`
- `Evidence-Agent-B` ownership: `ASD-0727`, `ASD-0859`
- `Evidence-Agent-C` ownership: `ASD-0860`, `ASD-0861`
- `Classification-Reviewer`: merged-evidence adjudication only

No `PDF-Archive-Agent` ownership is frozen at launch time. If any paper reaches a stable local-archive landing threshold, that archive step must still be explicitly recorded rather than assumed.

## 5. Controller discipline

- each evidence slice is read-only
- merged evidence is controller-owned
- adjudication is controller-owned
- writeback starts only after the landing subset is frozen
- only the controller may edit master / progress / closeout / git
