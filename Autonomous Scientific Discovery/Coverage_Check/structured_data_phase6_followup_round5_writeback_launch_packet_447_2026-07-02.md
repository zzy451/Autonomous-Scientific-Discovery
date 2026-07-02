# ASD Phase 6 follow-up round 5 harmonization writeback launch packet

Date: 2026-07-02
Round label: `Phase6FollowupR5`

This packet freezes the dedicated harmonization writeback round for the four-paper hold frontier. The ownership split is disjoint and complete for this round.

## Approved harmonization subset

Exactly these four papers are in scope:

- `ASD-0005`
- `ASD-0097`
- `ASD-0112`
- `ASD-0572`

No paper outside this set may be changed in the round.

## Ownership split

`Writeback-Agent-1` owns:

- `Notes/03_Chemical_Sciences/Song_2025_Robotic_AI_Chemist.md`
- `Notes/04_Materials_Science/Wu_2025_Random_Heteropolymer_Blends.md`

`Writeback-Agent-2` owns:

- `Notes/06_Life_Sciences/Alber_2026_CellVoyager.md`
- `Notes/07_Medical_and_Health_Sciences/Che_2025_CSSTep.md`

## Controller-frozen harmonization directions

- `ASD-0005` -> preserve current authoritative state `03;04`, keep `source_limited=yes`
- `ASD-0097` -> retract to stable core `06`, keep `source_limited=yes`
- `ASD-0112` -> retract to stable core `03`, keep `source_limited=yes`
- `ASD-0572` -> preserve `04;06`, but harmonize to `source_limited=yes`

## Hard rules

Writeback agents must not edit:

- `Paper_Lists/agent_master_paper_list.md`
- `Coverage_Check/multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`
- any file under `Coverage_Check/` other than reading these packets
- any note file outside the owned list

Writeback agents must:

- apply the frozen harmonization direction exactly
- treat note location as filing convenience only
- update only the listed note sections
- return the required completion packet with changed files and blockers

## Controller-only follow-up after writeback returns

After both writeback packets return and are reviewed, only the Main Controller may:

1. edit `agent_master_paper_list.md`
2. edit `multi_module_note_pdf_full_reaudit_progress_451_2026-06-21.md`
3. write the round closeout
4. rebuild structured data and run consistency checks
