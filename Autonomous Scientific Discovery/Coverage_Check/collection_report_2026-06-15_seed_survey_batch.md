# Scientific Agent Literature Collection Report

Date: 2026-06-15

Update note: this report records the initial seed-survey extraction batch. For the current master-list status after core-note creation and metadata cleanup, see `Coverage_Check/coverage_check_2026-06-15_core_notes_and_master_list.md`.

## 1. Scope

This is the first source-first literature collection batch for the Autonomous Scientific Discovery review.

Primary seed source:

- `From AI for Science to Agentic Science: A Survey on Autonomous Scientific Discovery`
- arXiv: `2508.14111v1`
- Source trail label in the master list: `ShanghaiAILabSeedSurvey`

This batch is a candidate pool, not a final inclusion set. Papers still require abstract/full-text verification against the Agent inclusion criteria.

## 2. Output Files

- Master paper list: `Paper_Lists/agent_master_paper_list.md`
- Raw extracted references: `Paper_Lists/seed_survey_refs_extracted.json`
- Structured extracted references: `Paper_Lists/seed_survey_refs_structured.json`
- Candidate JSON snapshot: `Paper_Lists/agent_candidates_seed_survey_110.json`

## 3. Batch Summary

| Main class / status | Count |
|---|---:|
| `01` Formal, Information, and Computational Sciences | 14 |
| `02` Physics, Astronomy, and Cosmic Sciences | 2 |
| `03` Chemical Sciences | 26 |
| `04` Materials Science | 16 |
| `06` Life Sciences | 17 |
| `07` Medical and Health Sciences | 14 |
| `09` Engineering and Industrial Technology Sciences | 3 |
| `needs_review` | 16 |
| `background_only` | 2 |
| **Total** | **110** |

Inclusion status:

| Status | Count |
|---|---:|
| `candidate` | 92 |
| `needs_review` | 16 |
| `background_only` | 2 |

Citation priority:

| Priority | Count |
|---|---:|
| `core` | 10 |
| `standard` | 100 |

## 4. Core-Priority Papers In This Batch

These were marked `core` because they are high-impact journal papers or especially central seed items. They still need full notes before formal use in the review.

| ID | Paper | Source | Initial class |
|---|---|---|---|
| `ASD-0005` | A multiagent-driven robotic AI chemist enabling autonomous chemical research on demand | JACS | `03` |
| `ASD-0016` | An autonomous laboratory for the accelerated synthesis of novel materials | Nature | `04` |
| `ASD-0021` | A review of large language models and autonomous agents in chemistry | Chemical Science | `03` |
| `ASD-0035` | SciAgents: automating scientific discovery through bioinspired multi-agent intelligent graph reasoning | Advanced Materials | `04` |
| `ASD-0037` | Autonomous mobile robots for exploratory synthetic chemistry | Nature | `03` |
| `ASD-0056` | Delocalized, asynchronous, closed-loop discovery of organic laser emitters | Science | `03` |
| `ASD-0084` | Automating alloy design and discovery with physics-aware multimodal multiagent AI | PNAS | `04` |
| `ASD-0088` | Empowering biomedical discovery with AI agents | Cell | `07` |
| `ASD-0093` | Augmenting large language models with chemistry tools | Nature Machine Intelligence | `03` |
| `ASD-0094` | Autonomous chemical research with large language models | Nature | `03` |

## 5. Known Limitations

- The batch is extracted from one seed survey, so it is biased toward papers cited by that survey.
- Some DOI / URL fields are missing because arXiv HTML references did not expose stable links for every item.
- `Unknown` source entries need metadata cleanup.
- `candidate` does not mean formally included. It means the paper appears plausibly relevant and should be screened.
- `needs_review` papers require manual Agent/science-object judgment.
- Chemistry, materials, biomedical, and life-science papers dominate this seed batch; other domains need source-first expansion from high-impact journals and citation graphs.

## 6. Next Actions

1. Full-note the 10 `core` papers first using `ASD_single_paper_note_template.md`.
2. Resolve the 16 `needs_review` papers.
3. Fill DOI / URL metadata for high-priority records.
4. Expand from Nature / Science / Cell family entry points beyond the seed survey.
5. Perform backward and forward citation expansion from the 10 `core` papers.
6. Create domain-specific lists after metadata cleanup:
   - `paper_list_03_chemical_sciences.md`
   - `paper_list_04_materials_science.md`
   - `paper_list_06_life_sciences.md`
   - `paper_list_07_medical_and_health_sciences.md`
