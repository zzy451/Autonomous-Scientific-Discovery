# ASD Phase 6 follow-up round 14 plan

Date: 2026-07-04
Round label: `Phase6FollowupR14Approx`

This round continues the bounded Phase 6 follow-up line after `Phase6FollowupR13Approx`, again using an approximate multi-agent flow because real sub-agent tooling is still unavailable in this environment.

## 1. Scope

Frozen focus set:

- `ASD-0014`
- `ASD-0055`
- `ASD-0085`
- `ASD-0357`
- `ASD-0564`
- `ASD-0670`

## 2. Why this round exists

The user-facing rule for this stage is now explicit: if a paper remains hard-blocked for PDF retrieval, skip it rather than burning repeated rounds on the same blocked routes.

This packet therefore pivots from the currently blocked no-local-PDF frontier to the next clean high-yield pocket:

- six rows that already have canonical local archived PDFs
- six rows that still remain `source_limited=yes` in the authoritative pair
- six rows whose module anchors are already stable enough that local-PDF reread should be able to clear the old source-limited ceiling if the archived files remain readable

## 3. Round questions

1. Do the existing canonical local archived PDFs still read cleanly enough to support `first_hand_full_text` upgrades for these six rows?
2. Do the current module anchors remain stable under a fresh first-hand source check?
3. Is the landed subset partial or full once the local archived PDFs are rechecked?

## 4. Approximate role topology

- `Evidence-Agent-A` ownership: `ASD-0014`, `ASD-0055`
- `Evidence-Agent-B` ownership: `ASD-0085`, `ASD-0357`
- `Evidence-Agent-C` ownership: `ASD-0564`, `ASD-0670`
- `Classification-Reviewer`: merged-evidence adjudication only

No `PDF-Archive-Agent` ownership is frozen at launch time because all six rows already have canonical local archived PDFs.

## 5. Controller discipline

- each evidence slice is read-only
- merged evidence is controller-owned
- adjudication is controller-owned
- writeback starts only after the landing subset is frozen
- only the controller may edit master / progress / closeout / git
