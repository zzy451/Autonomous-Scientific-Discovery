# ASD Phase 6 note revision round 25 writeback launch packet W2

Date: 2026-07-05
Round label: `Phase6NoteRevisionR25Approx`
Owned agent: `Writeback-Agent-2` (approximate ownership)

## Ownership

You own exactly these note files and no others:

- `Notes/06_Life_Sciences/Zhang_2026_BioGAIP_Bioinformatics.md`
- `Notes/06_Life_Sciences/Jin_2025_BioLab_Life_Sciences.md`
- `Notes/06_Life_Sciences/Kim_2026_PBio_Agent_Perturbation_Biology.md`
- `Notes/07_Medical_and_Health_Sciences/Gao_2025_PharmAgents.md`
- `Notes/01_Formal_Information_and_Computational_Sciences/Luo_2025_BioResearcher.md`
- `Notes/07_Medical_and_Health_Sciences/Jiang_2026_GALILEO_Therapeutic_Discovery.md`
- `Notes/06_Life_Sciences/Patel_2025_ML_Copilot_Prognostic_Gene_Discovery.md`
- `Notes/07_Medical_and_Health_Sciences/Park_2025_IMMUNIA_Surfaceome_Discovery.md`

Do not edit any other file.

## Frozen adjudication anchors

Use only:

- `Coverage_Check/structured_data_phase6_note_revision_round25_landing_decision_447_2026-07-05.tsv`

You are not re-deciding classification.

## What to refresh

- add a top-of-file `Phase6NoteRevisionR25` harmonization override
- explicitly retire stale `to_read` / pending metadata when the current authoritative state is already landed
- when a newer frozen PDF-backed block exists, mark older source-limited or no-local-PDF wording below as superseded legacy text
- keep source-limited wording only where the frozen landing row still says `source_limited=yes`

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
