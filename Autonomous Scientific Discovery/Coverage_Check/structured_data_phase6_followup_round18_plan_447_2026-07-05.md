# ASD Phase 6 follow-up round 18 plan

Date: 2026-07-05
Round label: `Phase6FollowupR18Approx`

This round continues the bounded Phase 6 follow-up line after `Phase6FollowupR17Approx`, using the approximate multi-agent fallback because real sub-agent tooling is unavailable in this environment.

## 1. Scope

Frozen focus set:

- `ASD-0765`
- `ASD-0772`
- `ASD-0049`
- `ASD-0137`
- `ASD-0141`
- `ASD-0370`

## 2. Why this round exists

The post-R17 queue still contains a clean pocket of `archived_pdf + source_limited=yes` rows whose current note/master wording still reflects abstract-level or blocked-access evidence.

All six rows now have canonical local archived PDFs that are present and readable. This makes them a better immediate target than the hard no-local-PDF frontier, which should continue to be skipped when the PDF route is genuinely hard.

## 3. Approximate role topology

- `Evidence-Agent-A` approximate ownership: `ASD-0765`, `ASD-0772`
- `Evidence-Agent-B` approximate ownership: `ASD-0049`, `ASD-0137`
- `Evidence-Agent-C` approximate ownership: `ASD-0141`, `ASD-0370`
- `Classification-Reviewer`: controller-owned adjudication from merged evidence only

No `PDF-Archive-Agent` ownership is frozen at launch time because all six rows already have canonical local archived PDFs.

## 4. Controller discipline

- evidence slices are read-only
- merged evidence is controller-owned
- adjudication is controller-owned
- writeback starts only after the landing subset is frozen
- only the controller may edit master / progress / closeout / git
- closeout must state that this was an approximate multi-agent / controller-executed role round, not a literal sub-agent round
