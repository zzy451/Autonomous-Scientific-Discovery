# ASD Phase 6 follow-up round 1 closeout

Date: 2026-07-02
Round label: `Phase6FollowupR1`

This file closes the first live Phase 6 follow-up round at the evidence-plus-classification stage. No authoritative files were edited in this round.

## 1. Round shape

Scope:

- source queue: `Coverage_Check/structured_data_phase6_full_text_followup_queue_447_2026-07-02.tsv`
- executed slice count: `3 x 10`
- executed paper count: `30`

Actual topology:

- `Evidence-Agent-A`: launched in first wave, completed, closed
- `Evidence-Agent-B`: launched in first wave, completed, closed
- `Evidence-Agent-C`: first launch attempt blocked by thread limit, later launched successfully, completed, closed
- `Classification-Reviewer`: launched after evidence merge, completed, closed

No silent downgrade was applied.

## 2. Controller-owned outputs

- merged evidence pack:
  - `Coverage_Check/structured_data_phase6_followup_round1_evidence_merge_template_447_2026-07-02.tsv`
- classification review pack:
  - `Coverage_Check/structured_data_phase6_followup_round1_classification_review_447_2026-07-02.tsv`
- launch record:
  - `Coverage_Check/structured_data_phase6_followup_round1_launch_status_2026-07-02.md`

## 3. Evidence summary

Merged evidence coverage for the 30-paper round:

- local PDF found in round evidence: `7`
- no local PDF in round evidence: `23`
- source-limited records: `19`
- non-source-limited records: `11`

Confidence profile:

- `high`: `18`
- `medium_high`: `4`
- `medium`: `7`
- `low`: `1`

Special access statuses surfaced in this round:

- `safety_skip`: `1` (`ASD-0547`)
- `waf_block`: `1` (`ASD-0544`)
- `cloudflare_block`: `1` (`ASD-0858`)

## 4. Classification summary

Classification-review outputs over the merged evidence pack:

- papers with multi-module support: `6`
- papers staying in independent `01.04`: `1` (`ASD-0006`)
- papers flagged `master_update_required=yes`: `7`
- papers flagged `note_revision_required=uncertain`: `6`

Reviewer-flagged master-update candidates:

- `ASD-0005`
- `ASD-0097`
- `ASD-0112`
- `ASD-0572`
- `ASD-0089`
- `ASD-0091`
- `ASD-0093`

Reviewer-flagged explicit safety-skip case:

- `ASD-0547`

## 5. Controller QA note

`ASD-0005` required controller-side correction during evidence merge.

- The raw `Evidence-Agent-A` completion packet wrongly inserted the Boiko 2023 / `ASD-0094` DOI-PDF pair into the Song 2025 row.
- The controller did **not** propagate those wrong Boiko fields into the merged evidence pack.
- The merged row was rebuilt conservatively from the current repo-documented Song 2025 first-hand leads only:
  - publisher landing page abstract
  - official ACS supporting-information page
- The row remains explicitly `source_limited=yes`.

## 6. Landing guidance for the next round

High-confidence direct landing candidates from the reviewer:

- `ASD-0158` -> `03`
- `ASD-0569` -> `04`
- `ASD-0735` -> `04`
- `ASD-0859` / `ASD-0860` / `ASD-0861` -> `05`
- `ASD-0617` -> `06`
- `ASD-0855` -> `11`
- `ASD-0090` -> `02`

Conservative-hold reminders from the reviewer:

- `ASD-0547` stays low-confidence and safety-limited
- `ASD-0097` keeps `07` only as adjunct to stable `06`
- `ASD-0112` keeps `07` only as adjunct to stable `03`
- `ASD-0724` stays `06` without adding `05`
- `ASD-0565` and `ASD-0631` remain abstract-level / access-limited `04`
- `ASD-0005` is acceptable as `03;04` but still source-limited

## 7. Next controller action

The next round should be a landing-selection and writeback-prep round, not a fresh evidence round.

Recommended next step order:

1. freeze the land-now subset from the `7` `master_update_required=yes` records
2. decide which of those `7` are strong enough to land immediately versus keep conservative
3. if any landing subset is approved, split note ownership for writeback and only then edit authoritative files

Until note ownership and landing scope are frozen, `agent_master_paper_list.md` and the progress tracker should remain unchanged.
