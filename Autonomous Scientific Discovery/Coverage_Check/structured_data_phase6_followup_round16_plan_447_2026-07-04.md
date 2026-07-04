# ASD Phase 6 follow-up round 16 plan

Date: 2026-07-04
Round label: `Phase6FollowupR16Approx`

This round continues the bounded Phase 6 follow-up line after `Phase6FollowupR15Approx`, using the approximate multi-agent fallback because real sub-agent tooling is unavailable in this environment.

## 1. Scope

Frozen focus set:

- `ASD-0587`
- `ASD-0665`
- `ASD-0832`
- `ASD-0838`
- `ASD-0491`
- `ASD-0558`

## 2. Why this round exists

The post-R15 full-text follow-up queue still exposes several hard no-local-PDF rows that have already received bounded evidence-only treatment. Under the current user rule, those hard PDF routes should not be repeatedly re-fought when HTML / abstract / official-page evidence is already enough to keep a true paper indexed conservatively.

This packet therefore targets the next clean local archived PDF pressure pocket:

- six rows with canonical local archived PDFs
- six rows still marked `source_limited=yes` in the authoritative pair
- six rows with stable module anchors where local-PDF reread can clear the old source-limited ceiling without forcing a broad classification migration

`ASD-0466` is deliberately not included because its archived PDF is the official supplementary PDF while the main article remains gated, so it is not a clean full-text landing candidate.

## 3. Approximate role topology

- `Evidence-Agent-A` approximate ownership: `ASD-0587`, `ASD-0665`
- `Evidence-Agent-B` approximate ownership: `ASD-0832`, `ASD-0838`
- `Evidence-Agent-C` approximate ownership: `ASD-0491`, `ASD-0558`
- `Classification-Reviewer`: controller-owned adjudication from merged evidence only

No `PDF-Archive-Agent` ownership is frozen at launch time because all six rows already have canonical local archived PDFs.

## 4. Controller discipline

- evidence slices are read-only
- merged evidence is controller-owned
- adjudication is controller-owned
- writeback starts only after the landing subset is frozen
- only the controller may edit master / progress / closeout / git
- closeout must state that this was an approximate multi-agent / controller-executed role round, not a literal sub-agent round
