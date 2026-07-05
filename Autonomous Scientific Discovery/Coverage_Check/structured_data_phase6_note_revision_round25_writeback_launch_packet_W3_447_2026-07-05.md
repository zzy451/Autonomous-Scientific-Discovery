# ASD Phase 6 note revision round 25 writeback launch packet W3

Date: 2026-07-05
Round label: `Phase6NoteRevisionR25Approx`
Owned agent: `Writeback-Agent-3` (approximate ownership)

## Ownership

You own exactly these note files and no others:

- `Notes/07_Medical_and_Health_Sciences/Roberts_2026_OpenScientist_Biomedical_Discovery.md`
- `Notes/01_Formal_Information_and_Computational_Sciences/Rahim_2026_BioAgent_Reproducible_Translational_Bioinformatics.md`
- `Notes/07_Medical_and_Health_Sciences/Wang_2026_Rhizome_OS_1.md`
- `Notes/07_Medical_and_Health_Sciences/Ke_2025_BioDisco.md`
- `Notes/07_Medical_and_Health_Sciences/Yang_2026_PROBE_Structure_Based_Drug_Design.md`
- `Notes/03_Chemical_Sciences/Li_2026_MolReAct_Lead_Optimization.md`
- `Notes/07_Medical_and_Health_Sciences/Baker_2026_CIWM_CRC_Drug_Response.md`
- `Notes/07_Medical_and_Health_Sciences/Zhou_2026_ToolMol.md`
- `Notes/01_Formal_Information_and_Computational_Sciences/Unknown_2025_SAGA.md`
- `Notes/09_Engineering_and_Industrial_Technology_Sciences/Xu_2025_CFDagent.md`

Do not edit any other file.

## Frozen adjudication anchors

Use only:

- `Coverage_Check/structured_data_phase6_note_revision_round25_landing_decision_447_2026-07-05.tsv`

You are not re-deciding classification.

## What to refresh

- add a top-of-file `Phase6NoteRevisionR25` harmonization override
- explicitly retire stale `to_read` / pending metadata when the current authoritative state is already landed
- keep note location as filing convenience only; do not let folder placement override the frozen multi-module anchor
- use the override block to retire older conservative-hold, `01.04`, or single-module shorthand where the landing row has already settled those boundaries

## Hard constraints

- do not edit `agent_master_paper_list.md`
- do not edit progress trackers
- do not edit round reports
- do not revert unrelated changes
- preserve the frozen modules / bucket exactly as landed in the controller packet

## Return packet

Report:

- owned note files
- changed note files
- untouched note files if any
- whether each changed file was wording-only
- blockers if any
