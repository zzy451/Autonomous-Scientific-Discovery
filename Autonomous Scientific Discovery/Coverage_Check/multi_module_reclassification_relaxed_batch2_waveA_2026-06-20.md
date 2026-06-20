# Batch 2 / Wave A relaxed 多模块重分类审计报告

> 日期：2026-06-20  
> 范围：`agent_master_paper_list.md` confirmed Batch 2 / Wave A。  
> 对应计划：`Coverage_Check/multi_module_reclassification_relaxed_round_plan_451_confirmed_2026-06-20.md`。  
> 本 wave 执行新硬规则：不能完全参考 Notes；以原文 / DOI / publisher page / arXiv / PMC / project page 等一手来源为主。已确认的 high-confidence 分类变化，同步修订对应 Notes。

## 一、执行口径

- 本 wave 不扩量，不新增论文，只复核已 confirmed records 的 `scientific_object_modules`。
- 本地 Notes 仅作线索；若 Note 仍保留旧单模块或 `01.04` 旧口径，主控在一手来源确认后同步修订。
- `01.04` 只作为没有任何具体科学对象实验、验证、benchmark task、case study 或结果报告的 general-method bucket。
- 主列表 schema 尚未迁移，因此本 wave 不直接覆盖 legacy `Main class / Secondary class` 字段；分类事实先写入审计报告和 Notes。

## 二、覆盖情况

| Reviewer | 计划 ID 边界 | 实际 reviewed `to_read` records | 说明 |
|---|---|---:|---|
| A-Reviewer-1 | `ASD-0155`-`ASD-0381` | 14 | `ASD-0254` 主控进一步全文复核后覆盖 Reviewer 的保守判断 |
| A-Reviewer-2 | `ASD-0385`-`ASD-0447` | 5 | 该 ID 段中大量记录不是本 wave confirmed core |
| A-Reviewer-3 | `ASD-0455`-`ASD-0508` | 14 | 无 high-confidence note update；`ASD-0478` 保留主控复核 |
| A-Reviewer-4 | `ASD-0510`-`ASD-0523` | 14 | `ASD-0510`, `ASD-0522`, `ASD-0523` 已同步修 note |

| Metric | Count |
|---|---:|
| reviewed records | 47 |
| high-confidence stable keep records | 35 |
| high-confidence classification changes | 6 |
| medium-confidence add-module candidates | 2 |
| remaining full-text / main-control review queue | 6 |
| direct master-list edits | 0 |
| note updates completed | 6 |

## 三、主控裁决表

| ID | Legacy filing | 本轮建议模块 / bucket | 主控裁决 | 证据摘要 | 置信度 | note |
|---|---|---|---|---|---|---|
| `ASD-0155` | `04 / 04.04` | `04` | 保持 `04` | freeform dielectric metasurfaces / nanophotonic layouts | high | no update |
| `ASD-0156` | `04 / 04.01` | `04` | 保持 `04` | EM images, crystal reconstruction, material-property analysis | high | no update |
| `ASD-0158` | `03 / 03.03` | `03` | 保持 `03` | organic compounds and robotic flow synthesis | high | no update |
| `ASD-0179` | `03 / 03.03` | `03` | 保持 `03` | reaction-condition recommendation and robotic wet-lab validation | high | no update |
| `ASD-0186` | `11 / 11.07` | `11` | 保持 `11.07` | scientific paper review / peer-review feedback generation | high | no update |
| `ASD-0189` | `06 / 06.03` | `06` | 保持 `06` | proteomics datasets, proteins, biological hypotheses | high | no update |
| `ASD-0254` | `01 / 01.04` | `06;07` | 从独立 `01.04` 迁出，记录 `06;07` | arXiv full text Appendix C includes liposarcoma, thyroid cancer, HCC, viral infection, transcriptomics, scRNA-seq, gene-expression objectives | high | updated |
| `ASD-0276` | `06 / 06.03` | `06;07` candidate | 暂保持 `06`，列入 `07` add-module 待全文补证 | clinical multiomics / proteogenomics evidence suggests possible `07` | medium | queue |
| `ASD-0280` | `03 / 03.03` | `03` | 保持 `03` | synthesis search, experiment design / execution, spectral analysis | high | no update |
| `ASD-0290` | `03 / 03.02` | `03`, possible `04` | 保持 `03`，列入 `03/04` 复核 | catalyst discovery with quantum-chemical feedback; material-performance framing still unclear | medium | queue |
| `ASD-0333` | `03 / 03.04` | `03` | 保持 `03` | chemistry hypothesis rediscovery benchmark | high | no update |
| `ASD-0357` | `07 / 07.04` | `07` | 保持 `07` | disease mechanisms and therapeutic target discovery | high | no update |
| `ASD-0370` | `06 / 06.03` | `06` | 保持 `06` | protein fitness landscape and enzyme thermostability | high | no update |
| `ASD-0379` | `04 / 04.04` | `04` | 保持 `04` | palladium films and material-property Pareto front | high | no update |
| `ASD-0381` | `03 / 03.03` | `03` | 保持 `03` | rhodium-catalyzed hydroformylation / ligand optimization | high | no update |
| `ASD-0385` | `04 / 04.04` | `03;04` | 新增 `03`，primary filing 保持 `04` | multi-step synthetic route plus semiconductor nanoparticle shell-growth material object | high | updated |
| `ASD-0410` | `04 / 04.04` | `04` | 保持 `04` | closed-loop materials phase mapping and property optimization | high | no update |
| `ASD-0418` | `03 / 03.03` | `03` | 保持 `03` | Suzuki-Miyaura / catalytic reaction optimization | high | no update |
| `ASD-0428` | `03 / 03.03` | `03` | 保持 `03` | autonomous reaction discovery and new chemical reactivity | high | no update |
| `ASD-0447` | `01 / 01.04` | `03` | 从独立 `01.04` 迁出，记录 `03` | concrete synthesis of small organic molecules, oligopeptides, oligonucleotides; 24,936 base steps / 329 h | high | updated |
| `ASD-0455` | `04 / 04.04` | `04` | 保持 `04` | photocatalyst mixtures and hydrogen-evolution activity | high | no update |
| `ASD-0463` | `03 / 03.03` | `03` | 保持 `03` | organic target molecules and robotic synthesis recipes | high | no update |
| `ASD-0466` | `04 / 04.03` | `04` | 保持 `04`，Agent-loop 强度待全文复核 | CNT growth conditions and wall selectivity | medium | queue |
| `ASD-0478` | `04 / 04.04` | `04` | 暂保持 `04`，主控复核 | NIMS-OS materials closed-loop examples, but platform pressure high | medium | queue |
| `ASD-0484` | `04 / 04.03` | `04` | 保持 `04` | silver nanoparticles and optical spectra / morphology objectives | high | no update |
| `ASD-0487` | `04 / 04.04` | `04` | 保持 `04` | aqueous battery electrolyte discovery | high | no update |
| `ASD-0491` | `04 / 04.04` | `04` | 保持 `04` | perovskite thin films and solar-cell validation | high | no update |
| `ASD-0501` | `06 / 06.03` | `06` | 保持 `06` | yeast gene function and deletion mutants | high | no update |
| `ASD-0503` | `04 / 04.04` | `04` | 保持 `04` | thin-film optoelectronic materials | high | no update |
| `ASD-0504` | `09 / 09.02` | `09` | 保持 `09` | mechanical structures, 3D printing, toughness | high | no update |
| `ASD-0505` | `04 / 04.04` | `04` | 保持 `04` | inorganic target materials and solid-state phases | high | no update |
| `ASD-0506` | `03 / 03.03` | `03` | 保持 `03` | donor-acceptor molecules and photostability | high | no update |
| `ASD-0507` | `03 / 03.03` | `03` | 保持 `03` | reaction conditions across experimental reaction classes | high | no update |
| `ASD-0508` | `03 / 03.04` | `03` | 保持 `03` | dye-like molecules and multiproperty molecular discovery | high | no update |
| `ASD-0510` | `08 / 08.01` | `06;08` | 新增 `06`，primary filing 保持 `08` | Arabidopsis, potato, winter wheat plant-phenotyping tasks | high | updated |
| `ASD-0511` | `09 / 09.03` | `09` | 保持 `09` | scientific instruments / user-facility operation | high | no update |
| `ASD-0512` | `01 / 01.01` | `01` | 保持 `01` | cap set problem and online bin packing algorithms | high | no update |
| `ASD-0513` | `04 / 04.04` | `04` | 保持 `04` | networked autonomous materials exploration systems | high | no update |
| `ASD-0514` | `04 / 04.03` | `04` | 保持 `04` | gold nanoparticles and morphology / optical spectra | high | no update |
| `ASD-0515` | `04 / 04.04` | `04` | 保持 `04` | alloy films and anomalous Hall resistivity | high | no update |
| `ASD-0516` | `04 / 04.04` | `04` | 保持 `04` | silver thin films and optical properties | high | no update |
| `ASD-0517` | `04 / 04.03` | `04` | 保持 `04` | plasmonic nanoparticles and targeted optical properties | high | no update |
| `ASD-0518` | `06 / 06.03` | `06` | 保持 `06` | enzyme / protein variants and wet-lab activity gains | high | no update |
| `ASD-0519` | `03 / 03.02` | `03` | 保持 `03`，Agent 强度待全文复核 | electrochemical systems and hypothesis testing | medium | queue |
| `ASD-0520` | `04 / 04.04` | `03;04` candidate | 暂保持 `04`，列入 `03` add-module 待全文补证 | low-Ir OER electrocatalyst and electrochemical water splitting | medium | queue |
| `ASD-0521` | `06 / 06.03` | `06` | 保持 `06` | CRISPR systems, gRNAs, gene-editing experiments | high | no update |
| `ASD-0522` | `04 / 04.01` | `04;09` | 新增 `09`，primary filing 保持 `04` | material samples / AFM characterization plus AFM scientific-instrument operation | high | updated |
| `ASD-0523` | `01 / 01.02` | `01;11` | 新增 `11.07`，primary filing 保持 `01` | AI research automation plus automated peer review / scientific knowledge production | high | updated |

## 四、已同步修订 Notes

| ID | Note path | 修订内容 |
|---|---|---|
| `ASD-0254` | `Notes/01_Formal_Information_and_Computational_Sciences/Luo_2025_BioResearcher.md` | 从 independent `01.04` 改为 `scientific_object_modules = 06;07`，补写 disease / omics objectives |
| `ASD-0385` | `Notes/04_Materials_Science/Volk_2023_AlphaFlow_Nanoparticle_Growth.md` | 从 `04` 单模块改为 `03;04`，保留 `04` primary filing |
| `ASD-0447` | `Notes/01_Formal_Information_and_Computational_Sciences/Manzano_2022_Universal_Chemical_Synthesis_Platform.md` | 从 independent `01.04` 改为 `03`，补写 concrete synthesis object evidence |
| `ASD-0510` | `Notes/08_Agricultural_Food_Forestry_Animal_and_Fishery_Sciences/Chen_2026_PhenoAssistant.md` | 从 `08` 单模块改为 `06;08`，保留 `08` primary filing |
| `ASD-0522` | `Notes/04_Materials_Science/Mandal_2024_AILA_Autonomous_Microscopy.md` | 从 `04` 单模块改为 `04;09`，补写 AFM instrument-operation evidence |
| `ASD-0523` | `Notes/01_Formal_Information_and_Computational_Sciences/Lu_2026_End_to_End_AI_Research.md` | 从 `01` 单模块改为 `01;11`，补写 automated peer-review / scientific knowledge production evidence |

## 五、待复核队列

| ID | 问题 | 下一步 |
|---|---|---|
| `ASD-0276` | clinical multiomics / proteogenomics 是否足以新增 `07` | 读全文数据集与疾病 / patient-level 描述后再决定是否修 note |
| `ASD-0290` | catalyst discovery 是否同时构成 `04` 材料性能对象 | 读全文确认 catalyst candidates 是 chemical catalyst object 还是 materials-performance object |
| `ASD-0466` | CNT 记录分类稳定为 `04`，但 Agent-loop 强度偏早期自动化 | 全文复核自动实验决策与反馈 loop 强度 |
| `ASD-0478` | NIMS-OS 平台化强，materials examples 是否足以稳定 `04` | 回原文确认 concrete materials experiment coverage |
| `ASD-0519` | electrochemistry HTE 分类为 `03` 稳定，但 Agent 纳入强度需查 | 全文复核自主决策 / feedback loop |
| `ASD-0520` | OER catalyst 可能支持 `03;04`，但 Agent-loop 和双模块强度需查 | 全文复核 electrochemical reaction 与 catalyst-material performance evidence |

## 六、Wave A 统计口径

本表只统计 high-confidence keep / high-confidence classification changes；medium candidates 不计入正式模块展开。

| Suggested module / bucket | Wave A count |
|---|---:|
| `01` | 2 |
| `03` | 13 |
| `04` | 17 |
| `06` | 7 |
| `07` | 2 |
| `08` | 1 |
| `09` | 3 |
| `11` | 2 |
| independent `01.04` bucket | 0 |

说明：multi-module records 已展开计数；`ASD-0276` 和 `ASD-0520` 的候选新增模块未计入上表。

## 七、主控结论

Batch 2 / Wave A 已完成 47 条 confirmed records 的 relaxed multi-module 复核。最重要的口径校准是：不能再因论文“平台化 / universal / workflow”而把有具体对象实验的记录留在 `01.04`。本 wave 中 `ASD-0254` 和 `ASD-0447` 是最明显的旧口径残留，均已按一手来源同步修订 Notes。

本 wave 仍不支持修改 `01-11` 一级体系；下一步应进入 Batch 2 / Wave B，并继续执行“原文优先 + high-confidence 同步修 note”的规则。
