# Batch 2 / Wave B 多模块重分类审计报告（relaxed object-coverage rule）

> 日期：2026-06-20  
> 范围：`ASD-0524` 到 `ASD-0600` 中当前 `to_read` 的 Batch 2 / Wave B 记录  
> 本轮口径：不再完全依赖旧 Notes；Notes 只作线索。分类以论文原文、PDF、DOI / publisher landing page、arXiv、PMC、官方项目页等一手来源为优先证据。  
> 注意：主列表仍处于 legacy schema 阶段，`Main class` / `Secondary class` 暂作 filing baseline。本报告与已更新 Notes / Remarks 记录新的 `scientific_object_modules` 事实。

## 1. 执行概况

| 指标 | 数量 |
|---|---:|
| 本 wave 实际复核 `to_read` 记录 | 54 |
| 高置信分类事实变化 | 8 |
| 高置信保持不变 | 34 |
| medium / low 或需全文队列 | 12 |
| 本轮同步更新 Notes | 8 |
| 本轮同步更新主列表 Remarks | 8 |
| 本轮直接改动 legacy `Main class` / `Secondary class` | 0 |

本轮主控合并原则：

- 只合并 `high` confidence 且有一手来源支撑的变化。
- `notes_only`、metadata-only、或 reviewer 标为 `medium / low / full_text_required` 的记录不强行改分类，只进入队列。
- 已确认变化同步写入对应 note；主列表暂不改 legacy filing 字段，只在 `Remarks` 追加 `RelaxedMultiModule2026-06-20`，等待后续 schema migration。

## 2. 高置信分类变化

| ID | 题名 | legacy filing | relaxed modules | primary filing | 结论 | Note / Remarks |
|---|---|---|---|---|---|---|
| `ASD-0525` | TeLLAgent | `01 / 01.04` | `03;04` | `04` | 从独立 `01.04` 移出；organic solar-cell material validation 与 molecule/material candidate evidence 支持化学 + 材料。 | 已更新 |
| `ASD-0531` | GALILEO | `07 / 07.04` | `06;07` | `07` | therapeutic peptide discovery 为医学主线；membrane biology、immune-cell functional assays 支持生命科学。 | 已更新 |
| `ASD-0537` | Medea | `07 / 07.04` | `06;07` | `07` | therapeutic endpoints 支持医学；omics/pathway/biological-target analyses 支持生命科学。 | 已更新 |
| `ASD-0540` | Robin | `07 / 07.04` | `06;07` | `07` | dry AMD / ripasudil 支持医学；RPE phagocytosis、RNA-seq、ABCA1 支持生命科学。 | 已更新 |
| `ASD-0545` | IMMUNIA | `07 / 07.01` | `06;07` | `07` | precision immunotherapy biomarker discovery 支持医学；surfaceome genes 与 tumor-immune crosstalk 支持生命科学。 | 已更新 |
| `ASD-0548` | OpenScientist | `07 / 07.04` | `06;07` | `07` | disease / clinical cases 支持医学；single-cell transcriptomics、proteomics、mechanism analyses 支持生命科学。 | 已更新 |
| `ASD-0554` | BioAgent | `01 / 01.04` | `06;07` | `07` | BRAF V600E melanoma、TP53 pan-cancer、PBMC 3k single-cell immune profiling 已构成具体对象 benchmark studies，不能留在 `01.04`。 | 已更新 |
| `ASD-0564` | SPARK cancer pathology | `07 / 07.01` | `06;07` | `07` | cancer pathology / patient biomarker validation 支持医学；tumor biology / spatial biology 支持生命科学。 | 已更新 |

## 3. 高置信保持不变的代表性边界样本

| ID | 题名 | 结论 | 说明 |
|---|---|---|---|
| `ASD-0542` | MADD | 保持 `07` | drug-discovery orchestra，有 biological targets / hit molecules / docking benchmark，但对象仍是药物发现。 |
| `ASD-0549` | DeepInflation | 保持 `02` | inflationary cosmology、inflaton potentials、CMB observables 是明确宇宙学对象。 |
| `ASD-0557` | Azobenzene isomerization workflow | 保持 `03` | 分子异构化、AIMD/DFT、IR/Raman 与反应/机理对象均为化学。 |
| `ASD-0565` | Radiation-tolerant HEAs | 保持 `04` | radiation tolerance 是 alloy material property，不单独触发 `02`。 |
| `ASD-0572` | Random heteropolymer blends | 保持 `04` | protein stabilization 是性能 assay / objective，直接优化对象仍是 polymer-blend material。 |
| `ASD-0575` | Curious formulation robot / protocell behavior | 保持 `03` | protocell 作为 chemical formulation/model system 处理，不扩到 `06`。 |
| `ASD-0597` | Chemputation augmented by LLMs | 保持 `03` | scientific literature 是输入媒介；最终对象是 chemical synthesis execution，不归 `11.07`。 |
| `ASD-0600` | Universal chemical synthesis literature execution | 保持 `03` | 虽然名为 universal system，但有 concrete chemical synthesis execution，不能进入 `01.04`。 |

## 4. 需全文 / 中低置信队列

| ID | 当前倾向 | 队列理由 |
|---|---|---|
| `ASD-0524` AgenticSciML | 可能 `01`，不再纯 `01.04` | SciML / PINN / operator-learning benchmark 是否足以作为 formal/computational object，需要全文确认。 |
| `ASD-0528` AutoSciLab | 可能 `02;04` | projectile motion / Ising / nanophotonics case 是否均为对象层实验，需全文确认 nanophotonics 边界。 |
| `ASD-0530` Hierarchical AI Scientist Systems | 暂留 `01.04` | 目前未找到 concrete scientific-object experiment；若全文有对象案例再迁移。 |
| `ASD-0539` AI-Agent materials discovery | 暂保持 `04`，可能加 `03` | MoS2 材料对象明确；electrolyte-additive molecular inverse-design 是否足以加 `03` 需全文确认。 |
| `ASD-0541` PromptBio | 暂保持 `06` | bioinformatics / multi-omics 对象明确，但平台压力较强，后续全文复核。 |
| `ASD-0543` ML Copilot Agent | 暂保持 `06` | prognostic gene discovery 可能触发 `07`，但 reviewer 仅 notes_only，不能高置信变更。 |
| `ASD-0544` Cancer Biomarker Discovery | 暂保持 `07` | medical object 清楚，但 full paper 可补强 Agent workflow 与对象细节。 |
| `ASD-0547` Pixelated metasurface design | 暂保持 `04` | `09` 只有 plausible；需全文确认 device/fabrication-system 是否构成工程对象。 |
| `ASD-0553` ToolsGenie 2.0 | 暂留队列，不改 note | BixBench bioinformatics tasks 可能支持 `06`，但需要全文列出具体 biological data-analysis objects。 |
| `ASD-0587` MOSAIC chemical synthesis | 暂保持 `03` | publisher landing-page evidence 足以支持化学，但 full text 可补强 protocol / compound validation。 |
| `ASD-0596` Cell-Free Biofoundry | 暂保持 `06` | CFPS / protein-expression 对象稳定；Agent strength 仍需全文确认。 |
| `ASD-0599` AI-Native Biofoundry | 暂保持 `06` | enzyme engineering 对象稳定；全文需确认 autonomy details 与 reported enzyme metrics。 |

## 5. Note 同步清单

已同步高置信分类变化的 Notes：

- `Notes/01_Formal_Information_and_Computational_Sciences/Sun_2026_TeLLAgent.md`
- `Notes/07_Medical_and_Health_Sciences/Jiang_2026_GALILEO_Therapeutic_Discovery.md`
- `Notes/07_Medical_and_Health_Sciences/Sui_2026_Medea_Therapeutic_Discovery.md`
- `Notes/07_Medical_and_Health_Sciences/Ghareeb_2025_Robin.md`
- `Notes/07_Medical_and_Health_Sciences/Park_2025_IMMUNIA_Surfaceome_Discovery.md`
- `Notes/07_Medical_and_Health_Sciences/Roberts_2026_OpenScientist_Biomedical_Discovery.md`
- `Notes/01_Formal_Information_and_Computational_Sciences/Rahim_2026_BioAgent_Reproducible_Translational_Bioinformatics.md`
- `Notes/07_Medical_and_Health_Sciences/Trost_2026_SPARK_Cancer_Pathology.md`

这些 note 采用“追加 2026-06-20 relaxed multi-module revision 段”的方式，明确新字段并压过旧单模块表述；旧正文中的单模块残留留待后续 schema migration 或全文精读时整体清理。

## 6. Batch 2 目前累计变化

Wave A 已完成并提交，本 Wave B 新增 8 条高置信变化。Batch 2 当前已确认的高置信 relaxed multi-module / `01.04` migration 变化包括：

- Wave A：`ASD-0254`, `ASD-0385`, `ASD-0447`, `ASD-0510`, `ASD-0522`, `ASD-0523`
- Wave B：`ASD-0525`, `ASD-0531`, `ASD-0537`, `ASD-0540`, `ASD-0545`, `ASD-0548`, `ASD-0554`, `ASD-0564`

Batch 2 合计已确认高置信变化：14 条。

## 7. 下一步

1. 继续 Batch 3 / Wave A：`ASD-0601` 到 `ASD-0673`。
2. 对 `ASD-0553` ToolsGenie 2.0 单独做 full-text object-task 抽查，因为它是本轮最典型的 `01.04` / bioinformatics object boundary。
3. 后续 schema migration 时，把 `scientific_object_modules`、`general_method_bucket`、`primary_module_for_filing` 从 note/report/remarks 迁移为主列表正式字段，并重新计算 module assignment counts。
