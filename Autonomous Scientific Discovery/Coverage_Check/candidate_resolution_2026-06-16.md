# Candidate Resolution

Date: 2026-06-16

## Scope

This report resolves the 15 records still marked `candidate` after the strict review and to-read note batch.

## Inputs

- Master list: `Paper_Lists/agent_master_paper_list.md`
- Project rule: include scientific Agent papers only; classify by final scientific object.
- Review method: two read-only sub-agent review batches, followed by main-agent integration.

## Summary Decision

All 15 remaining `candidate` records were upgraded to `to_read`. No candidate was excluded or downgraded to `background_only` in this pass.

Reason: each record shows a multi-step scientific Agent workflow or a clear tool-using / multi-agent / planning agent role in a scientific research process. Several remain benchmark- or tool-assistant-heavy, so their notes flag limited scientific discovery strength.

## Resolved Records

| ID | Decision | Main class | Note path | Key caution |
|---|---|---|---|---|
| `ASD-0003` | `to_read` | `03` | `Notes/03_Chemical_Sciences/Wu_2025_ChemAgent.md` | Title/version variant: CheMatAgent appears in note/PDF. |
| `ASD-0007` | `to_read` | `04` | `Notes/04_Materials_Science/Kumbhar_2025_Hypothesis_Generation_Materials.md` | Hypothesis-generation system; verify material-validation strength when used as representative case. |
| `ASD-0025` | `to_read` | `03` | `Notes/03_Chemical_Sciences/McNaughton_2024_CACTUS.md` | Tool-assistant/benchmark-heavy; avoid overclaiming discovery. |
| `ASD-0028` | `to_read` | `07` | `Notes/07_Medical_and_Health_Sciences/Liu_2024_DrugAgent.md` | Drug-discovery programming agent; distinguish coding automation from direct discovery. |
| `ASD-0029` | `to_read` | `03` | `Notes/03_Chemical_Sciences/Li_2025_ChemHAS.md` | Title/version variant: ChemAmp may be current system name. |
| `ASD-0030` | `to_read` | `07` | `Notes/07_Medical_and_Health_Sciences/Lee_2025_CLADD.md` | Metadata/version cleanup may be needed. |
| `ASD-0038` | `to_read` | `03` | `Notes/03_Chemical_Sciences/Chen_2024_Chemical_Literature_Data_Mining_Agent.md` | System/title variant: ChemMiner appears in PDF. |
| `ASD-0044` | `to_read` | `02` | `Notes/02_Physics_Astronomy_and_Cosmic_Sciences/Zhang_2025_SimAgents.md` | Cosmological simulation workflow; validation is computational. |
| `ASD-0045` | `to_read` | `04` | `Notes/04_Materials_Science/Zhang_2024_HoneyComb.md` | Materials benchmark/tool system; not necessarily experimental discovery. |
| `ASD-0047` | `to_read` | `09` | `Notes/09_Engineering_and_Industrial_Technology_Sciences/Yue_2025_Foam_Agent.md` | Engineering CFD workflow automation. |
| `ASD-0049` | `to_read` | `06` | `Notes/06_Life_Sciences/Xin_2024_BIA.md` | PDF still blocked; note needs page-level supplement. |
| `ASD-0053` | `to_read` | `01` | `Notes/01_Formal_Information_and_Computational_Sciences/Takagi_2023_Autonomous_Hypothesis_Verification.md` | Toy-problem validation; use carefully. |
| `ASD-0059` | `to_read` | `01` | `Notes/01_Formal_Information_and_Computational_Sciences/Rabby_2025_MC_NEST.md` | Moved from `06` to `01.04`; object is general hypothesis-generation framework. |
| `ASD-0061` | `to_read` | `03` | `Notes/03_Chemical_Sciences/Polat_2025_xChemAgents.md` | Prediction/explainability strength; not strong experimental discovery. |
| `ASD-0095` | `to_read` | `04` | `Notes/04_Materials_Science/Bazgir_2025_MultiCrossModal.md` | Materials data integration; not new-material experimental discovery. |

## Updated Counts

After integration, the master list has no `candidate` records.

- `to_read`: 77
- `background_only`: 22
- `excluded`: 11
- `candidate`: 0

## Follow-Up

1. Metadata cleanup: `ASD-0003`, `ASD-0029`, `ASD-0030`, `ASD-0038`.
2. Avoid overclaiming benchmark/tool-assistant papers as experimentally validated discovery.
3. `ASD-0049` still needs PDF/full-text supplementation.
