# ASD Phase 6 follow-up round 7 closeout

Date: 2026-07-03
Round label: `Phase6FollowupR7`

This file will record the controller closeout for the bounded six-paper evidence round launched from the refreshed post-R6 full-text follow-up frontier.

## 1. Round scope

Frozen focus set:

- `ASD-0005`
- `ASD-0158`
- `ASD-0097`
- `ASD-0112`
- `ASD-0569`
- `ASD-0603`

This round was launched as:

- read-only evidence collection only
- no note writeback at launch
- no authoritative landing at launch
- no PDF archive writes at launch

## 2. Agent return status

All three evidence agents returned usable completion packets:

- `Evidence-Agent-A`
  - owned papers: `ASD-0005`, `ASD-0097`
  - return quality: usable

- `Evidence-Agent-B`
  - owned papers: `ASD-0112`, `ASD-0158`
  - return quality: usable

- `Evidence-Agent-C`
  - owned papers: `ASD-0569`, `ASD-0603`
  - return quality: usable

The independent `Classification-Reviewer` also returned a usable adjudication packet.

No sub-agent edited project files in this round.

## 3. Merged evidence summary

Controller-owned merged evidence file:

- `Coverage_Check/structured_data_phase6_followup_round7_evidence_merge_template_447_2026-07-03.tsv`

Per-paper high-level outcome:

- `ASD-0005`
  - stable `03;04`
  - stronger Birmingham accepted-manuscript lead exists
  - current environment still could not retrieve a readable manuscript or publisher PDF
  - keep `source_limited=yes`

- `ASD-0097`
  - stable `06`
  - stronger first-hand support now includes official Nature supplementary PDF
  - current evidence still does not justify relanding `07`
  - keep `source_limited=yes`

- `ASD-0112`
  - stable `03`
  - current evidence remains abstract / metadata led
  - `03/07` pressure remains only a future lead
  - keep `source_limited=yes`

- `ASD-0158`
  - stable `03`
  - chemistry anchor remains clear
  - Science full text / PDF still blocked here
  - keep `source_limited=yes`

- `ASD-0569`
  - stable `04`
  - strongest apparent delta in the round
  - Crossref confirms:
    - `license_URL = http://creativecommons.org/licenses/by/4.0/`
    - `link_URL = https://onlinelibrary.wiley.com/doi/pdf/10.1002/aisy.202200017`
    - `link_content_type = application/pdf`
  - but controller re-check on `2026-07-03` still received `403` / Cloudflare challenge from both Wiley article and Wiley PDF routes in this environment

- `ASD-0603`
  - stable `03`
  - concrete chemistry-object evidence remains clear
  - Science full text / PDF still blocked here
  - keep `source_limited=yes`

## 4. Controller decision

Controller-used adjudication files:

- `Coverage_Check/structured_data_phase6_followup_round7_classification_review_447_2026-07-03.tsv`
- `Coverage_Check/structured_data_phase6_followup_round7_landing_decision_447_2026-07-03.tsv`

Final controller decision for this round:

- no direct landings
- no note writeback launched
- no PDF archive write launched
- no authoritative files changed

Reasoning:

1. Five papers (`ASD-0005`, `ASD-0097`, `ASD-0112`, `ASD-0158`, `ASD-0603`) returned stronger or reconfirming evidence, but not a new authority-level delta.
2. `ASD-0569` was the only reviewer-proposed direct landing.
3. The controller accepted the reviewer’s stable `04` classification, but did **not** accept the proposed `source_limited=no` landing in this round.
4. Controller override reason:
   - Crossref metadata is strong and useful
   - but actual Wiley article/PDF access in this environment on `2026-07-03` still produced Cloudflare / `403`
   - under the current project rule, non-safety access blocking should remain visible as `source_limited`
   - therefore it is more conservative and more faithful to keep `ASD-0569` as a high-priority follow-up lead rather than claim the blocker is already resolved

This round therefore closes as an evidence-only conservative-hold round.

## 5. Baseline and git verification

Because no authoritative files changed in this round:

- baseline remains `447 / 421 / 26 / canonical 01.04 = 9 / drift 0`
- no `export -> check -> build` rerun was required for authoritative recount in this closeout

Round discipline still requires:

- git commit after closeout
- clean worktree after commit
- all round agents closed

All round agents were closed at controller closeout.
