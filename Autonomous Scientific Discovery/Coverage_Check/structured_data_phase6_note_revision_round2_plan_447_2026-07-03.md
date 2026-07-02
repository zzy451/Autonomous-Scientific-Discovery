# ASD Phase 6 note revision round 2 plan

Date: 2026-07-03
Round label: `Phase6NoteRevisionR2`

This round is a bounded Phase 6 note-wording harmonization round launched directly from the evidence and classification outputs of `Phase6FollowupR7`.

## 1. Scope

Approved landing subset:

- `ASD-0097`
- `ASD-0112`

This round is note-only. No master or progress writeback is planned unless note review exposes an unexpected authoritative mismatch.

## 2. Why this subset

`Phase6FollowupR7` returned stronger first-hand source evidence for both papers, but not an authority-level classification delta:

- `ASD-0097`
  - authoritative state remains `scientific_object_modules=06`
  - stronger first-hand support now includes the official Nature supplementary PDF
  - the note should reflect that the stable landed module is still `06`, while `07` remains only a future source-limited lead

- `ASD-0112`
  - authoritative state remains `scientific_object_modules=03`
  - stronger first-hand support now includes a cleaner publisher / Elsevier XML / HKUST abstract chain
  - the note should reflect that the stable landed module is still `03`, while `07` remains only a future source-limited lead

## 3. Read-only basis for this round

This round does not need a fresh evidence round. It is grounded on already returned read-only artifacts from `Phase6FollowupR7`:

- `Coverage_Check/structured_data_phase6_followup_round7_evidence_merge_template_447_2026-07-03.tsv`
- `Coverage_Check/structured_data_phase6_followup_round7_classification_review_447_2026-07-03.tsv`
- `Coverage_Check/structured_data_phase6_followup_round7_landing_decision_447_2026-07-03.tsv`

The controller may still use a read-only note-audit sub-agent before writeback to identify exact stale wording zones, but no new evidence or classification authority is introduced in this round.

## 4. Writeback topology

Landed note count is `2`, so this round uses:

- `Writeback-Agent-1`

Owned note files:

- `Notes/06_Life_Sciences/Alber_2026_CellVoyager.md`
- `Notes/07_Medical_and_Health_Sciences/Che_2025_CSSTep.md`

No other agent may edit these files in this round.

## 5. Controller rule for this round

The writeback agent may:

- tighten wording
- refresh evidence-log wording
- add the newly confirmed source chain
- clarify current authoritative anchor
- reduce stale boundary pressure

The writeback agent may not:

- change modules beyond the adjudicated row
- edit master/progress/report files
- expand or retract classification

## 6. Expected round outcome

After writeback, the notes should read as:

- `ASD-0097`: stable `06` record, with stronger first-hand support explicitly including the official Nature supplementary PDF, while old `07` remains only a future source-limited lead
- `ASD-0112`: stable `03` record, with stronger publisher / XML / institutional abstract wording, while old `07` remains only a future source-limited lead
