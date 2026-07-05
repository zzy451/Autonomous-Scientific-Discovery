# ASD Phase 6 follow-up round 17 plan

Date: 2026-07-04
Round label: `Phase6FollowupR17Approx`

This round continues the bounded Phase 6 follow-up line after `Phase6FollowupR16Approx`, using the approximate multi-agent fallback because real sub-agent tooling is unavailable in this environment.

## 1. Scope

Frozen focus set:

- `ASD-0568`
- `ASD-0581`
- `ASD-0582`
- `ASD-0591`
- `ASD-0668`
- `ASD-0672`

## 2. Why this round exists

The post-R16 queue still exposes hard no-local-PDF rows at the top. Following the current user rule, this packet skips those hard routes and targets the next clean local archived PDF source-limited pocket.

All six rows already have canonical local archived PDFs, stable materials-module anchors, and enough readable first-page or early-page full text to clear the old source-limited ceiling.

## 3. Approximate role topology

- `Evidence-Agent-A` approximate ownership: `ASD-0568`, `ASD-0581`
- `Evidence-Agent-B` approximate ownership: `ASD-0582`, `ASD-0591`
- `Evidence-Agent-C` approximate ownership: `ASD-0668`, `ASD-0672`
- `Classification-Reviewer`: controller-owned adjudication from merged evidence only

No `PDF-Archive-Agent` ownership is frozen at launch time because all six rows already have canonical local archived PDFs.

## 4. Controller discipline

- evidence slices are read-only
- merged evidence is controller-owned
- adjudication is controller-owned
- writeback starts only after the landing subset is frozen
- only the controller may edit master / progress / closeout / git
- closeout must state that this was an approximate multi-agent / controller-executed role round, not a literal sub-agent round
