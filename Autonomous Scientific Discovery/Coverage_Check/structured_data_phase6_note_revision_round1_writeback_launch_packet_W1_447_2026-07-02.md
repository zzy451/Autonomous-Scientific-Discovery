# ASD Phase 6 note revision round 1 writeback launch packet W1

Date: 2026-07-02
Round label: `Phase6NoteRevisionR1`
Owned agent: `Writeback-Agent-1`

## Ownership

This agent owns exactly these note files in this round:

- `Notes/06_Life_Sciences/Zhang_2025_PromptBio_Bioinformatics.md`
- `Notes/06_Life_Sciences/Alber_2026_CellVoyager.md`
- `Notes/07_Medical_and_Health_Sciences/Che_2025_CSSTep.md`

Do not edit any other file.

## Final adjudication anchor

Use only the frozen landing subset in:

- `Coverage_Check/structured_data_phase6_note_revision_round1_landing_decision_447_2026-07-02.tsv`

You are not re-deciding classification.

## What to refresh

Refresh only note wording so it matches the current authoritative state:

- `ASD-0541`
  - make the independent `01.04` state read as current truth
  - remove wording that still sounds like live `06` object coverage
  - fix local-PDF wording so it matches current `archived_pdf` / `pdf_exists=yes` state
- `ASD-0097`
  - keep `06` as the only landed module
  - keep `07` only as future source-limited lead
  - reduce sections where old human-biomedical pressure still reads half-landed
- `ASD-0112`
  - keep `03` as the only landed module
  - keep `07` only as future source-limited lead
  - reduce sections where old COVID-related biomedical pressure still reads half-landed

## Hard constraints

- do not change modules beyond the adjudicated row
- do not edit `agent_master_paper_list.md`
- do not edit progress trackers
- do not edit round reports
- do not revert unrelated changes
- you are not alone in the codebase; adjust to current file state instead of forcing older wording back in

## Return packet

Report:

- owned note files
- changed note files
- untouched note files if any
- whether each changed file was wording-only
- blockers if any
