# ASD Phase 6 note revision round 3 plan

Date: 2026-07-03
Round label: `Phase6NoteRevisionR3`

This round is a bounded Phase 6 note-wording harmonization round launched directly from the evidence and classification outputs of `Phase6FollowupR9`.

## 1. Scope

Approved landing subset:

- `ASD-0536`
- `ASD-0617`
- `ASD-0855`

This round is note-only. No master or progress writeback is planned unless note review exposes an unexpected authoritative mismatch.

## 2. Why this subset

`Phase6FollowupR9` returned stronger first-hand source chains for all three papers, but the controller intentionally kept the authoritative pair conservative:

- `ASD-0536`
  - authoritative state remains `scientific_object_modules=07`
  - controller rejected the reviewer-proposed `source_limited=yes -> no` landing because no first-hand full text or PDF was actually retrieved
  - the note should reflect stronger official JPA page visibility while still keeping `source_limited=yes`

- `ASD-0617`
  - authoritative state remains `scientific_object_modules=06`
  - stronger first-hand support now explicitly includes accessible supplementary artifacts on the Nature page
  - the note should reflect that workflow-detail support improved, while the main article and PDF remain gated

- `ASD-0855`
  - authoritative state remains `scientific_object_modules=11`
  - stronger first-hand support now explicitly includes an official ScienceDirect page with visible complimentary-access / PDF cues
  - the note should reflect stronger official-page evidence while keeping `source_limited=yes`

## 3. Read-only basis for this round

This round does not need a fresh evidence round. It is grounded on already returned read-only artifacts from `Phase6FollowupR9`:

- `Coverage_Check/structured_data_phase6_followup_round9_evidence_merge_template_447_2026-07-03.tsv`
- `Coverage_Check/structured_data_phase6_followup_round9_classification_review_447_2026-07-03.tsv`
- `Coverage_Check/structured_data_phase6_followup_round9_landing_decision_447_2026-07-03.tsv`

## 4. Writeback topology

Landed note count is `3`, so this round uses:

- `Writeback-Agent-1`

Owned note files:

- `Notes/07_Medical_and_Health_Sciences/Wang_2026_TCM_Agent_Herbal_Discovery.md`
- `Notes/06_Life_Sciences/Shen_2025_Industrial_Automated_Protein_Evolution.md`
- `Notes/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Unknown_2025_Automating_Scientific_Evaluation.md`

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
- flip `source_limited` against the controller landing decision

## 6. Expected round outcome

After writeback, the notes should read as:

- `ASD-0536`: stable `07` record, with stronger official JPA publisher-page wording explicitly mentioning visible HTML/PDF entries, while still keeping `source_limited=yes`
- `ASD-0617`: stable `06` record, with stronger Nature supplementary-access wording, while still making clear that the main article/PDF remain gated
- `ASD-0855`: stable `11` record, with stronger official ScienceDirect-page wording, while still keeping `source_limited=yes`
