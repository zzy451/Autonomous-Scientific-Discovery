# Batch 4 / Wave A relaxed multi-module reclassification audit

> Date: 2026-06-20  
> Scope: Batch 4 / Wave A, `ASD-0740`-`ASD-0804` returned by four read-only reviewers.  
> Policy: relaxed scientific-object experiment-coverage rule. Notes are treated as clues only; final accepted changes require first-hand or authoritative source evidence.

## 1. 本轮范围与口径

本轮 reviewer 共返回 64 条记录，其中 confirmed core (`to_read`) 56 条，另含 `background_only` 与 `excluded` duplicate 记录。主控只合并高置信、证据清楚、且属于 confirmed core overlay 的变更；中等置信、仍需全文、或 background-only 的对象口径建议进入 follow-up queue。

本轮继续保持 legacy `Main class` / `Secondary class` 字段不迁移，只在 master list `Remarks`、对应 Notes 和本报告中记录 relaxed multi-module 事实。

## 2. 已合并的 high-confidence confirmed changes

| Paper ID | Legacy filing | Accepted relaxed modules | Primary filing | Evidence basis |
|---|---|---|---|---|
| `ASD-0740` | `03 / 03.04` | `03;04` | `03` | Organic emitter molecular search supports `03`; solid-state ASE and photophysical material-performance validation supports `04`. |
| `ASD-0742` | `06 / 06.01` | `06;07` | `06` | Kinetic biological models support `06`; precision-medicine, Crohn's/IL-6, COVID epidemiology and public-health model use cases support `07`. |
| `ASD-0745` | `06 / 06.03` | `06;07` | `06` | Life-science DNA/RNA/protein/cell tasks support `06`; therapeutic antibody / PD-1 / pembrolizumab optimization and assay validation support `07`. |
| `ASD-0782` | `09 / 09.01` | `02;09` | `09` | CFD workflow automation supports `09`; concrete fluid-dynamics validation including sphere drag and flow-field simulation supports `02`. |
| `ASD-0787` | `01 / 01.04` | `03;04;06` | `03` | Nature page lists concrete biology, chemistry and materials case studies: protein engineering, chemical reactivity/synthesis and MOF screening. Pure `01.04` bucket no longer applies. |
| `ASD-0790` | `04 / 04.04` | `03;04` | `04` | Heterogeneous catalyst material/surface search supports `04`; CO adsorption and surface-chemistry validation supports `03`. |
| `ASD-0792` | `04 / 04.04` | `03;04` | `04` | Catalyst candidate/surface discovery supports `04`; pathway enumeration, transition-state search, kinetics and reaction validation support `03`. |

## 3. Note updates completed

已同步修订 7 篇 note，均在标题下方加入 `2026-06-20 relaxed multi-module revision` 区块：

| Paper ID | Note path |
|---|---|
| `ASD-0740` | `Notes/03_Chemical_Sciences/Park_2026_Organic_Emitters_SelfDriving_Lab.md` |
| `ASD-0742` | `Notes/06_Life_Sciences/Wehling_2025_Talk2Biomodels.md` |
| `ASD-0745` | `Notes/06_Life_Sciences/Jin_2025_BioLab_Life_Sciences.md` |
| `ASD-0782` | `Notes/09_Engineering_and_Industrial_Technology_Sciences/Xu_2025_CFDagent.md` |
| `ASD-0787` | `Notes/01_Formal_Information_and_Computational_Sciences/Ding_2025_SciToolAgent.md` |
| `ASD-0790` | `Notes/04_Materials_Science/Rothfarb_2026_Heterogeneous_Catalyst_Discovery.md` |
| `ASD-0792` | `Notes/04_Materials_Science/Song_2026_CatDT_Heterogeneous_Catalyst_Discovery.md` |

## 4. Medium / full-text follow-up queue

| Paper ID | Current decision | Follow-up reason |
|---|---|---|
| `ASD-0743` | keep `06` for now | Possible `06;07`; full text should verify cancer case-study depth. |
| `ASD-0744` | keep `06` | Check whether datasets include sufficiently explicit medical/health objects for `07`. |
| `ASD-0751` | keep `02` | Preliminary cosmology contribution; core-strength/full-text check. |
| `ASD-0752` | keep `09` | Low-priority Agent/core-strength check. |
| `ASD-0759` | keep `02` | Optional case-level check for breadth of physics evidence. |
| `ASD-0761` | keep `02` | Optional `02` vs `01` watch for quantum-circuit architecture. |
| `ASD-0766` | keep `11.07` | Classification stable, but note/metadata refresh can be done later. |
| `ASD-0768` | keep `11.07` | Classification stable, but note/metadata refresh can be done later. |
| `ASD-0769` | keep top-level `07` | Secondary `07.04` may be weak; full-text secondary review needed. |
| `ASD-0773` | keep `07` | Possible `06` secondary if transcriptomic/pathway/PCD biological-result coverage is confirmed. |
| `ASD-0775` | keep `09` | Check whether instrument demonstrations report concrete chemistry/materials sample results sufficient for `03`/`04`. |
| `ASD-0785` | keep `background_only` / `05` | Possible `08` background tag if agriculture/forestry cases are explicit. |
| `ASD-0793` | keep `03` | Possible `03;04`, but full text should confirm material-family/surface coverage. |
| `ASD-0797` | keep `06` | Add `07` only if full text shows disease/therapeutic validation beyond Cell Painting phenomics. |
| `ASD-0802` | keep `background_only` / `05` | Possible `11.07` background boundary: environmental data management vs scientific knowledge/data-production system. |
| `ASD-0803` | keep `05` for now | Strong `05;11` pressure sample, but reviewer marked full-text/maybe; defer until boundary adjudication. |

## 5. Background-only / excluded observations not merged into confirmed overlay

- `ASD-0746` and `ASD-0767` remain excluded duplicates.
- `ASD-0776`, `ASD-0777`, `ASD-0778`, `ASD-0785`, `ASD-0795`, and `ASD-0802` remain `background_only`.
- `ASD-0795` has a strong object-coding suggestion toward `04` rather than legacy `09`, but because it is background-only and not part of the confirmed core overlay, it was not included in the confirmed module-count update in this wave.

## 6. Updated partial overlay counts

Post Batch 4 / Wave A audited relaxed overlay:

| Scientific object module | Expanded assignment count |
|---|---:|
| `01` | 46 |
| `02` | 30 |
| `03` | 69 |
| `04` | 100 |
| `05` | 34 |
| `06` | 62 |
| `07` | 61 |
| `08` | 3 |
| `09` | 35 |
| `10` | 23 |
| `11` | 31 |

| Relaxed-counting metric | Count |
|---|---:|
| Record-level confirmed included-and-classified count | 451 |
| Expanded module assignment count | 494 |
| Independent `01.04` general-method bucket count, after accepted relaxed migrations | 37 |

## 7. Main-control conclusion

Batch 4 / Wave A confirms that the relaxed rule primarily affects cross-boundary catalyst/materials, CFD/physics, life-science/medical and `01.04` general-agent records. The most important correction is `ASD-0787`: although it is platform-like, the original Nature page gives concrete biology, chemistry and materials case studies, so it should not remain a pure independent `01.04` bucket case under the current policy.
