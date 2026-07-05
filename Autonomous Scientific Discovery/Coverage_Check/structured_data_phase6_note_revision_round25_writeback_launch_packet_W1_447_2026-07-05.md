# ASD Phase 6 note revision round 25 writeback launch packet W1

Date: 2026-07-05
Round label: `Phase6NoteRevisionR25Approx`
Owned agent: `Writeback-Agent-1` (approximate ownership)

## Ownership

You own exactly these note files and no others:

- `Notes/06_Life_Sciences/Nouri_2026_CellAtria_scRNAseq.md`
- `Notes/06_Life_Sciences/Qu_2025_PROTEUS_Multiomics.md`
- `Notes/06_Life_Sciences/Zhang_2026_AINative_Biofoundry_Enzyme_Engineering.md`
- `Notes/06_Life_Sciences/Shen_2025_Industrial_Automated_Protein_Evolution.md`
- `Notes/06_Life_Sciences/Jones_2026_Self_Driving_Datasets.md`
- `Notes/06_Life_Sciences/Lin_2025_Spatial_Transcriptomics_Pancreas_Maturation.md`
- `Notes/06_Life_Sciences/Wehling_2025_Talk2Biomodels.md`
- `Notes/06_Life_Sciences/Chen_2026_STAT_Spatial_Transcriptomics.md`

Do not edit any other file.

## Frozen adjudication anchors

Use only:

- `Coverage_Check/structured_data_phase6_note_revision_round25_landing_decision_447_2026-07-05.tsv`

You are not re-deciding classification.

## What to refresh

- add a top-of-file `Phase6NoteRevisionR25` harmonization override
- explicitly retire stale `to_read` / pending metadata when the current authoritative state is already landed
- keep source-limited wording only where the frozen landing row still says `source_limited=yes`
- when the landing row is `source_limited=no`, mark older abstract-only / no-local-PDF wording below as stale legacy text superseded by the new override

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
