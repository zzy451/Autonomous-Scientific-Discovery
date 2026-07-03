# ASD Phase 6 follow-up round 11 plan

Date: 2026-07-04
Round label: `Phase6FollowupR11Approx`

This round continues the bounded Phase 6 follow-up line after `Phase6FollowupR10Approx`, again using an approximate multi-agent flow because real sub-agent tooling is still unavailable in this environment.

## 1. Scope

Frozen focus set:

- `ASD-0005`
- `ASD-0158`
- `ASD-0097`
- `ASD-0112`
- `ASD-0603`
- `ASD-0569`

## 2. Why this round exists

After the post-R10 queue refresh:

- these six rows remained the highest non-safety follow-up pressure set
- all six still had no local PDF
- none of them had yet received a post-R10 controller packet freeze

This round therefore advances the next fresh queue-visible frontier without reusing old launch truth directly.

## 3. Round questions

1. Can any of these six move from abstract / metadata / page-level evidence to stronger first-hand article, XML, preprint, or PDF evidence?
2. Can any local-PDF or legal full-text status improve without overstating access?
3. Do the existing module anchors remain stable under refreshed first-hand evidence?
4. Does any record become strong enough for note-only refresh or bounded authoritative landing?

## 4. Approximate role topology

- `Evidence-Agent-A` ownership: `ASD-0005`, `ASD-0158`
- `Evidence-Agent-B` ownership: `ASD-0097`, `ASD-0112`
- `Evidence-Agent-C` ownership: `ASD-0603`, `ASD-0569`
- `Classification-Reviewer`: merged-evidence adjudication only

No writeback or PDF-archive ownership is frozen at launch time.

## 5. Controller discipline

- each evidence slice is read-only
- merged evidence is controller-owned
- adjudication is controller-owned
- writeback starts only if a landing subset is actually frozen
- only the controller may edit master / progress / closeout / git
