# ASD Coverage Check: Core Notes and Master List

Date: 2026-06-15

## 1. Scope

This check covers the current master paper list and the first set of preliminary notes for core-priority papers.

Files checked:

- `Paper_Lists/agent_master_paper_list.md`
- `Notes/`
- `paper_note_templates_and_prompts/ASD_single_paper_note_template.md`

## 2. Master List Status

Total records: 110

| Inclusion status | Count |
|---|---:|
| `candidate` | 82 |
| `to_read` | 8 |
| `needs_review` | 17 |
| `background_only` | 3 |

| Main class | Count |
|---|---:|
| `01` | 14 |
| `02` | 2 |
| `03` | 26 |
| `04` | 16 |
| `06` | 17 |
| `07` | 14 |
| `09` | 3 |

No records currently belong to `05`, `08`, `10`, or `11` in this seed-survey batch.

## 3. Note Coverage

Populated note paths in master list: 10

All populated note paths exist.

Formal note files created:

| ID | Status | Main class | Note path |
|---|---|---|---|
| `ASD-0005` | `to_read` | `03` | `Notes/03_Chemical_Sciences/Song_2025_Robotic_AI_Chemist.md` |
| `ASD-0016` | `to_read` | `04` | `Notes/04_Materials_Science/Szymanski_2023_A_Lab.md` |
| `ASD-0021` | `background_only` | `03` | `Notes/03_Chemical_Sciences/Ramos_2025_LLMs_Autonomous_Agents_Chemistry.md` |
| `ASD-0035` | `to_read` | `04` | `Notes/04_Materials_Science/Ghafarollahi_2025_SciAgents.md` |
| `ASD-0037` | `to_read` | `03` | `Notes/03_Chemical_Sciences/Dai_2024_Autonomous_Mobile_Robots.md` |
| `ASD-0056` | `to_read` | `03` | `Notes/03_Chemical_Sciences/StriethKalthoff_2024_Organic_Laser_Emitters.md` |
| `ASD-0084` | `to_read` | `04` | `Notes/04_Materials_Science/Ghafarollahi_2025_AtomAgents_Alloy.md` |
| `ASD-0088` | `needs_review` | `07` | `Notes/07_Medical_and_Health_Sciences/Gao_2024_Biomedical_Discovery_AI_Agents.md` |
| `ASD-0093` | `to_read` | `03` | `Notes/03_Chemical_Sciences/Bran_2024_ChemCrow.md` |
| `ASD-0094` | `to_read` | `03` | `Notes/03_Chemical_Sciences/Boiko_2023_Coscientist.md` |

## 4. Corrections Applied

- Added DOI links for the 10 core-note records where stable DOIs were known.
- Corrected `ASD-0021` venue from `Science` to `Chemical Science`.
- Changed `ASD-0021` to `background_only` because it is a review article for chemistry-agent citation expansion, not a single core system paper.
- Changed 8 core system papers from `candidate` to `to_read`, because preliminary notes exist but full-text evidence has not yet been logged.
- Changed `ASD-0088` to `needs_review`, because it may be a perspective/review rather than a core system paper.
- Added note paths for all 10 preliminary notes.

## 5. High-Risk Items

| ID | Risk | Current handling | Next action |
|---|---|---|---|
| `ASD-0021` | Review article could be mistakenly counted as a core Agent system paper. | `background_only` | Use for chemistry citation expansion. |
| `ASD-0088` | Cell article may be a perspective or framework paper rather than a system paper. | `needs_review` | Read full text and decide `background_only` vs core inclusion. |
| `ASD-0056` | Boundary between chemistry and materials science. | `to_read`, current main class `03` | Check whether the final object is molecular emitter discovery or device/material performance. |
| `ASD-0093` | Tool-using LLM may be weaker than full closed-loop Agent. | `to_read` | Verify multistep action and research workflow role from full text. |

## 6. Coverage Gaps

- The first batch is dominated by chemistry, materials, life sciences, and biomedical papers.
- `05` Earth and environmental sciences, `08` agriculture/food, `10` aerospace/marine/transportation, and `11` social/knowledge-system sciences are absent from the current source batch.
- DOI and venue metadata remain incomplete for many non-core records.
- `needs_review` records increased to 17 after conservatively marking `ASD-0088`.

## 7. Next Actions

1. Upgrade the 8 `to_read` core system notes with full-text evidence locations.
2. Resolve `ASD-0088` as either `background_only` or a formally included system paper.
3. Use `ASD-0021` Ramos et al. 2025 and the Shanghai AI Lab seed survey for backward citation expansion in chemistry.
4. Expand from Nature, Science, Cell, PNAS, JACS, Advanced Materials, and Nature Machine Intelligence entry points.
5. Resolve the 17 `needs_review` records before calling this batch a formal inclusion set.
