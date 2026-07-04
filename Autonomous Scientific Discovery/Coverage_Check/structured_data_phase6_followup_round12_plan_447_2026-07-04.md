# ASD Phase 6 follow-up round 12 plan

Date: 2026-07-04
Round label: `Phase6FollowupR12Approx`

This round continues the bounded Phase 6 follow-up line after `Phase6FollowupR11Approx`, again using an approximate multi-agent flow because real sub-agent tooling is still unavailable in this environment.

## 1. Scope

Frozen focus set:

- `ASD-0507`
- `ASD-0684`
- `ASD-0084`
- `ASD-0666`
- `ASD-0667`
- `ASD-0653`

## 2. Why this round exists

After excluding:

- the `R8-R11` recently handled rows
- recent note-only harmonization rows
- explicit safety-skip rows

the next fresh non-safety frontier is a six-paper set whose records all already have local archived PDFs but still remain `source_limited=yes` in the authoritative pair.

This makes `R12` the cleanest current opportunity to use first-hand local full-text evidence rather than re-fighting external publisher access blockers.

## 3. Round questions

1. Can the local archived PDFs support `first_hand_full_text` upgrades for these six rows?
2. Do the current module anchors remain stable under first-hand full-text review?
3. Which notes now require authoritative wording refresh because they still describe abstract-only or source-limited evidence?
4. Is there a bounded landed subset strong enough for note writeback plus authoritative landing in the same round?

## 4. Approximate role topology

- `Evidence-Agent-A` ownership: `ASD-0507`, `ASD-0684`
- `Evidence-Agent-B` ownership: `ASD-0084`, `ASD-0666`
- `Evidence-Agent-C` ownership: `ASD-0667`, `ASD-0653`
- `Classification-Reviewer`: merged-evidence adjudication only

No `PDF-Archive-Agent` ownership is frozen at launch time because all six papers already have canonical local archived PDFs.

## 5. Controller discipline

- each evidence slice is read-only
- merged evidence is controller-owned
- adjudication is controller-owned
- writeback starts only after the landing subset is frozen
- only the controller may edit master / progress / closeout / git

