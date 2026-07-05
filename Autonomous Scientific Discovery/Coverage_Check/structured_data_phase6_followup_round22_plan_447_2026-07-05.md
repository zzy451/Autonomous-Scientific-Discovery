# ASD Phase 6 follow-up round 22 plan

Date: 2026-07-05
Round label: `Phase6FollowupR22Approx`

This round closes the truthful remaining three-paper full-text-followup tail after `Phase6QueueRefreshAfterR26`, using the approximate multi-agent fallback because no real sub-agent launch interface is exposed in this environment.

## 1. Scope

Frozen focus set:

- `ASD-0637`
- `ASD-0644`
- `ASD-0717`

## 2. Why this round is bounded

The refreshed post-R26 queue no longer contains a truthful fresh `30`-paper follow-up packet.

Only three full-text-followup rows remain after freshness override:

- `ASD-0637`
- `ASD-0644`
- `ASD-0717`

Per the current governing plan stack, this should be handled as a bounded tail cleanup rather than padded into a fake standard `3 x 10 = 30` round.

## 3. Why these three rows are landable now

All three rows already have canonical local archived PDFs present in `Reference_PDF/`.

The controller has confirmed that:

- `ASD-0637` local archived arXiv PDF is readable and supports the stable `11.07` science-of-science citation-network reading
- `ASD-0644` local archived arXiv PDF is readable and supports the stable `11.02` social-behavior research automation reading
- `ASD-0717` local archived arXiv PDF is readable and supports the stable `11.07` scientific-literature / knowledge-production reading

No `PDF-Archive-Agent` ownership is needed because the PDFs are already archived locally.

## 4. Approximate role topology

- `Evidence-Agent-A` approximate ownership: `ASD-0637`
- `Evidence-Agent-B` approximate ownership: `ASD-0644`
- `Evidence-Agent-C` approximate ownership: `ASD-0717`
- `Classification-Reviewer`: controller-owned adjudication from merged evidence only
- `Writeback-Agent-1`: all three landed notes after the landing subset is frozen

## 5. Controller discipline

- evidence slices are read-only
- merged evidence is controller-owned
- adjudication is controller-owned from merged evidence only
- writeback starts only after the landing subset is frozen
- only the controller may edit master / progress / closeout / git
- closeout must state that this was a bounded approximate multi-agent tail round, not a real sub-agent round
