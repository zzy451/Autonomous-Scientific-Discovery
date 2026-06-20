# Batch 1 高风险候选一手证据复核与 note 修订记录

> 日期：2026-06-20
> 对应计划：`multi_module_reclassification_relaxed_round_plan_451_confirmed_2026-06-20.md`
> 范围：Batch 1 / Wave B 中 5 篇高风险多模块候选：`ASD-0069`, `ASD-0096`, `ASD-0100`, `ASD-0141`, `ASD-0151`。
> 本轮性质：一手来源优先的分类证据复核 + 已有 note 分类表述修订。
> 本轮未修改 `Paper_Lists/agent_master_paper_list.md`。

## 一、执行口径

本轮按 relaxed multi-module object-coverage rule 执行：

- 只要论文对某一科学领域中的具体对象做了可识别实验、验证、benchmark task、case study 或结果报告，即可记录对应 `01-11` 模块。
- 不要求每个模块都是论文主贡献。
- `01.04` 只用于没有任何具体科学对象实验 / 验证 / benchmark task / case study / reported result 的通用 ASD 方法文献。
- 本地 Notes 只能作为线索；分类更新必须尽量回到原文、PDF、DOI / arXiv / publisher page、官方项目页或权威摘要。

## 二、复核结论

| ID | paper | first_hand_sources_checked | updated scientific_object_modules | primary_module_for_filing | note revision | confidence | full_text_required |
|---|---|---|---|---|---|---|---|
| `ASD-0069` | `The AI Scientist` | arXiv abstract / PDF v3; local note | `01;11` | `01` | 已在 note 加更新块 | `01`: medium-high; `11.07`: medium | no for initial reclassification |
| `ASD-0096` | `dZiner` | arXiv abstract; arXiv full text; local note | `03;04;07` | `04` | 已在 note 加更新块 | `03`: high; `04`: high; `07`: medium-high | no |
| `ASD-0100` | `SciReplicate-Bench` | arXiv abstract / PDF; local note | `01;11` | `11` | 已在 note 加更新块 | medium-high | no for initial reclassification |
| `ASD-0141` | `TransAgent` | DOI / bioRxiv metadata; accessible full-text mirror; official GitHub; local note | `06;07` | `06` | 已在 note 加更新块 | `06`: high; `07`: medium-high | no for classification |
| `ASD-0151` | `Self-driving lab discovers principles for steering spontaneous emission beyond conventional Fourier optics` | Nature Communications publisher page / PDF; local note | `04;02` | `04` | 已在 note 加更新块 | `04`: high; `02`: medium-high | no |

## 三、逐条证据摘要

### `ASD-0069` The AI Scientist

- 旧表述风险：note 和 master row 仍把该文献写作 `01 / 01.04` 通用科研 Agent。
- 当前判断：应离开独立 `01.04` only 处理，记录 `01;11`。
- `01` 证据：原文在 diffusion modeling、transformer language modeling、learning dynamics 等机器学习研究任务上执行 idea generation、coding、experiment、paper writing。
- `11.07` 证据：automated reviewer 使用 OpenReview / ICLR reviewer data，直接评估 scientific peer review / knowledge-production quality。
- 保留说明：ASD/general research-agent 属性可作为副标签，但不能替代正式对象模块。

### `ASD-0096` dZiner

- 旧表述风险：note 以 `04` 单模块为主，把 `03 / 07` 主要作为混淆边界。
- 当前判断：记录 `03;04;07`，`primary_module_for_filing = 04`。
- `03` 证据：surfactant molecules、SMILES、CMC optimization、chemical-property design。
- `04` 证据：MOF organic linkers、node-topology pairs、CO2 adsorption materials performance。
- `07` 证据：WDR5 protein target、ligand / inhibitor / drug candidate docking optimization、disease-relevant target。

### `ASD-0100` SciReplicate-Bench

- 旧表述风险：note 和 master row 写作 `01 / 01.04` 科研复现 benchmark。
- 当前判断：应离开独立 `01.04` only 处理，记录 `01;11`，建议 `primary_module_for_filing = 11`。
- `01` 证据：algorithmic reproduction、NLP research papers、reasoning graph、code generation / test execution。
- `11.07` 证据：scientific reproducibility、paper-to-code reproduction、research-paper understanding、knowledge-production evaluation benchmark。

### `ASD-0141` TransAgent

- 旧表述风险：note 认为稳定对象是 transcriptional regulation 而不是 clinical decision support，因此保留 `06`。
- 当前判断：该主归档判断仍成立，但 relaxed rule 下应追加 `07`，记录 `06;07`。
- `06` 证据：transcriptional regulation、multi-omics、epigenomics、gene expression profiles、enhancers / super-enhancers、gene regulatory networks、cardiomyocyte differentiation。
- `07` 证据：ESCC / esophageal squamous cell carcinoma super-enhancer regulatory circuit、oncogenic transcriptional regulators、cancer pathogenesis、potential therapeutic-target discovery。

### `ASD-0151` Desai 2026

- 旧表述风险：note 强调 `04` 主归档并写作“不转 `02`”。
- 当前判断：`primary_module_for_filing = 04` 仍成立，但 relaxed rule 下应追加 `02`，记录 `04;02`。
- `04` 证据：reconfigurable semiconductor / GaAs metasurfaces、InAs quantum dots、metasurface structure-property optimization、emission directivity materials performance。
- `02` 证据：spontaneous emission steering、far-field emission profile、Fourier optics、momentum matching、nanoscale light-matter interaction、governing-equation / operational-principle discovery。

## 四、对 Batch 1 后续合并的影响

- record-level confirmed count：本轮不改变，仍以主列表当前 `451` 为基线。
- `needs_review`：本轮未改主列表，仍以主列表当前 `0` 为基线。
- confirmed `08`：本轮未涉及，仍以主列表当前 `3` 为基线。
- module assignment impact：若未来 schema 接纳本轮结论，这 5 篇将贡献 `01:2`, `02:1`, `03:1`, `04:2`, `06:1`, `07:2`, `11:2` 的 assignment；assignment 总数可大于 record count。
- independent `01.04` bucket impact：`ASD-0069` 与 `ASD-0100` 不应继续作为 `01.04` only 记录；`01.04` 属性仅可作为 general ASD method / benchmark 标签保留。

## 五、已修订 note

- `Notes/01_Formal_Information_and_Computational_Sciences/Lu_2024_AI_Scientist.md`
- `Notes/04_Materials_Science/Ansari_2024_dZiner.md`
- `Notes/01_Formal_Information_and_Computational_Sciences/Xiang_2025_SciReplicate_Bench.md`
- `Notes/06_Life_Sciences/Zhang_2025_TransAgent_Transcriptional_Regulation.md`
- `Notes/04_Materials_Science/Desai_2026_Spontaneous_Emission_SDL.md`

## 六、后续建议

本轮只完成高风险候选的 source-level note 修订，未执行 master-list schema migration。下一步建议：

- 继续对 Batch 1 relaxed Wave A/B 的其他 `note_revision_required` 候选做同样的一手证据复核。
- 在累计足够高置信样本后，再统一设计 `scientific_object_modules` / `general_method_bucket` / `primary_module_for_filing` 等主列表 schema 迁移策略。
- 在 schema 未定前，不建议直接用 legacy `Main class` 字段承载多模块事实。
