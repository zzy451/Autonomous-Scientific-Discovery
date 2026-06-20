# Batch 1 / Wave B relaxed 多模块重分类审计报告

> 日期：2026-06-20  
> 范围：`agent_master_paper_list.md` confirmed 记录序号 58-113。  
> 对应计划：`Coverage_Check/multi_module_reclassification_relaxed_round_plan_451_confirmed_2026-06-20.md`。  
> 本文件是当前 relaxed 口径下的新一轮审计产物；此前保守试跑结论不再作为本轮分类依据。

## 一、执行口径

本 wave 按当前目标执行两件事：

- 先完成 56 篇 confirmed 文献的 relaxed multi-module 分类建议。
- 同步标出需要回原文、PDF、publisher page 或 full note 复核的记录，以及需要后续修正论文笔记中分类表述的记录。

分类硬口径：

- 只要论文对某一科学领域的具体对象做了可识别实验、验证、benchmark task、case study 或结果报告，就可以记录对应 `01-11` 科学对象模块。
- 不要求被记录模块构成论文核心贡献。
- 不因论文自称 general / cross-domain / platform 自动多模块；必须能写出对象层证据。
- `01.04` 只作为独立 general-method bucket，用于没有任何具体科学对象实验、验证、benchmark task、case study 或结果报告的 ASD / general research-agent 方法文献。
- 本 wave 不直接修改 `agent_master_paper_list.md`；原因是主列表 row-level schema migration 尚未完成，当前旧字段仍是 legacy filing display。

## 二、基线与覆盖

本轮开始前主列表头部基线：

| 指标 | 当前值 |
|---|---:|
| `candidate` | 0 |
| `to_read` | 451 |
| `background_only` | 370 |
| `excluded` | 50 |
| `needs_review` | 0 |
| legacy confirmed included-and-classified count | 451 |
| confirmed `08` count | 3 |

Wave B 覆盖情况：

| Reviewer | 记录数 | 分配 ID |
|---|---:|---|
| B-Reviewer-1 | 14 | `ASD-0069`, `ASD-0070`, `ASD-0071`, `ASD-0075`, `ASD-0076`, `ASD-0077`, `ASD-0079`, `ASD-0080`, `ASD-0081`, `ASD-0083`, `ASD-0084`, `ASD-0085`, `ASD-0089`, `ASD-0090` |
| B-Reviewer-2 | 14 | `ASD-0091`, `ASD-0093`, `ASD-0094`, `ASD-0095`, `ASD-0096`, `ASD-0097`, `ASD-0100`, `ASD-0111`, `ASD-0112`, `ASD-0113`, `ASD-0114`, `ASD-0115`, `ASD-0116`, `ASD-0117` |
| B-Reviewer-3 | 14 | `ASD-0118`, `ASD-0119`, `ASD-0120`, `ASD-0121`, `ASD-0124`, `ASD-0125`, `ASD-0126`, `ASD-0127`, `ASD-0128`, `ASD-0129`, `ASD-0132`, `ASD-0133`, `ASD-0134`, `ASD-0135` |
| B-Reviewer-4 | 14 | `ASD-0136`, `ASD-0137`, `ASD-0138`, `ASD-0139`, `ASD-0140`, `ASD-0141`, `ASD-0145`, `ASD-0146`, `ASD-0147`, `ASD-0149`, `ASD-0150`, `ASD-0151`, `ASD-0152`, `ASD-0154` |

四个只读 Reviewer 均已完成，56 / 56 条覆盖。Reviewer 未编辑任何项目文件。

## 三、主控裁决表

| ID | Legacy filing | 本轮建议模块 / bucket | 主控裁决 | 证据摘要 | 置信度 | 是否需回原文 / 修笔记 |
|---|---|---|---|---|---|---|
| `ASD-0069` | `01 / 01.04` | `01;11` | 记录离开 `01.04` 与 `11.07` 候选，不改表 | ML research tasks plus OpenReview / peer-review benchmark evidence | medium | 是，需原文确认 peer-review benchmark 是否是对象层结果 |
| `ASD-0070` | `03 / 03.04` | `03` | 保持 `03`，列入领域构成复核 | chemistry / natural-science hypotheses with experimentally reported outcomes | medium | 是，需核验 124 hypotheses 是否跨 `04/06` |
| `ASD-0071` | `06 / 06.03` | `06;07` | 记录 `07` add-module 候选，不改表 | gene expression data plus disease-condition / disease-associated gene tasks | medium | 是，需修 note 中 `06/07` 表述 |
| `ASD-0075` | `04 / 04.04` | `04` | 保持 `04` | nanohelix materials and structure-property / g-factor optimization | high | 否 |
| `ASD-0076` | `03 / 03.04` | `03` | 保持 `03` | SMILES molecules and PMO-1K molecular optimization tasks | high | 否 |
| `ASD-0077` | `07 / 07.04` | `07;06` | 记录 `06` add-module 候选，不改表 | biomedical benchmark questions plus cancer drug-resistance / biomedical-tool evidence | medium | 是，需回原文核验 `06` 生物对象强度 |
| `ASD-0079` | `07 / 07.04` | `07` | 保持 `07` | drugs, protein targets and DTI prediction benchmark | high | 否 |
| `ASD-0080` | `04 / 04.02` | `04` | 保持 `04` | MOF structures, porous materials and synthesized AI-MOFs | high | 否 |
| `ASD-0081` | `06 / 06.03` | `06` | 保持 `06` | genes, gRNA, CRISPR systems and gene-editing experiments | high | 否 |
| `ASD-0083` | `07 / 07.04` | `07` | 保持 `07` | dry AMD drug repurposing with wet-lab validation | high | 否 |
| `ASD-0084` | `04 / 04.02` | `04` | 保持 `04`，列入全文补证 | alloy structure / property design evidence currently still partly note-level | medium | 是，需补原文实验 / 验证细节 |
| `ASD-0085` | `06 / 06.03` | `06` | 保持 `06` | de novo proteins, structure, secondary structure and mechanical properties | high | 否 |
| `ASD-0089` | `01 / 01.04` | `01.04` bucket | 保持独立 `01.04` | research-method codification benchmark without concrete science object result | high | 否 |
| `ASD-0090` | `02 / 02.02` | `02` | 保持 `02` | superconducting quantum processor, qubits and entangled states | high | 否 |
| `ASD-0091` | `03 / 03.04` | `03` | 保持 `03` | small molecules, polymers, reactions and NMR chemical-search tasks | high | 否 |
| `ASD-0093` | `03 / 03.04` | `03` | 保持 `03`，列入全文补证 | ChemCrow chemistry tool use and chemistry benchmark tasks | medium | 是，note 仍偏 metadata-heavy |
| `ASD-0094` | `03 / 03.03` | `03` | 保持 `03` | palladium-catalysed cross-coupling and wet-lab chemistry tasks | high | 否 |
| `ASD-0095` | `04 / 04.04` | `04` | 保持 `04` | SEM images, materials simulation videos, phase transitions, nanoparticle self-assembly | high | 否 |
| `ASD-0096` | `04 / 04.04` | `03;04;07` | 记录 `03` 与 `07` add-module 候选，不改表 | MOF / linker material design plus surfactant molecules and WDR5 ligand case | medium | 是，高优先原文复核与 note 修订 |
| `ASD-0097` | `06 / 06.03` | `06;07` | 记录 `07` add-module 候选，不改表 | scRNA-seq biology plus COVID-19 disease / biomedical single-cell case | medium | 是，需修 note 中 `06/07` 边界表述 |
| `ASD-0100` | `01 / 01.04` | `01;11` | 记录离开 `01.04` 与 `11.07` 候选，不改表 | algorithm/code reproduction benchmark plus scientific reproducibility evaluation | medium | 是，需原文确认 `11.07` 强规则适用 |
| `ASD-0111` | `01 / 01.04` | `01.04` bucket | 暂保持独立 `01.04` | Humanity's Last Exam / general-purpose scientific-agent benchmark only at metadata level | medium | 是，需全文确认是否有具体领域 case |
| `ASD-0112` | `07 / 07.04` | `07`, possible `03` | 保持 `07`，列入 `03` 低强度复核 | drug molecules, COVID-19 targets and drug-like chemical space | medium | 是，需全文核验是否存在独立化学对象结果 |
| `ASD-0113` | `07 / 07.04` | `07` | 保持 `07`，列入验证强度复核 | drug targets, lead compounds and preclinical evaluation | medium | 是，需全文核实验证强度 |
| `ASD-0114` | `06 / 06.03` | `06` | 保持 `06` | proteins, peptides, protein stability and protein design principles | high | 是，需全文补 computational validation 细节 |
| `ASD-0115` | `07 / 07.04` | `07` | 保持 `07`，列入 general co-scientist 边界复核 | biomedical hypotheses, AML drug repurposing and antimicrobial resistance mechanisms | medium | 是，需原文确认非 `01.04` 与具体对象强度 |
| `ASD-0116` | `04 / 04.04` | `04` | 保持 `04` | electromagnetic metamaterials, programmable metasurfaces, experimental prototype | high | 否 |
| `ASD-0117` | `03 / 03.04` | `03`, possible `04` | 保持 `03`，列入 `03/04` 边界复核 | organic structure-directing agent molecules with porous-material downstream context | medium | 是，需全文确认 `04` 是否只是背景 |
| `ASD-0118` | `07 / 07.04` | `07`, possible `06` | 保持 `07`，记录 `06` 待查 | biomedical research tasks; possible life-science-only task list | medium | 是，需 task-level 原文核验和 note 修订 |
| `ASD-0119` | `04 / 04.03` | `04` | 保持 `04` | MOF structures and porous-material properties | high | 否 |
| `ASD-0120` | `02 / 02.01` | `02` | 保持 `02` | gamma-ray astronomy observations / CTA workflows | high | 否 |
| `ASD-0121` | `02 / 02.01` | `02` | 保持 `02` | cosmological parameters and ACT lensing constraints | high | 否 |
| `ASD-0124` | `09 / 09.05` | `09` | 保持 `09` | beam structural-analysis / OpenSeesPy engineering simulation | high | 否 |
| `ASD-0125` | `09 / 09.03` | `09` | 保持 `09` | power-electronics systems and converter modulation design | high | 否 |
| `ASD-0126` | `06 / 06.03` | `06` | 保持 `06` | genomics / bioinformatics workflow and nf-core support | high | 是，全文可补强 `06/07` 边界 |
| `ASD-0127` | `02 / 02.01` | `02` | 保持 `02`，列入 `02/01.04` 复核 | cosmology / astronomy data-analysis workflow | medium | 是，需原文确认不是 generic substrate |
| `ASD-0128` | `09 / 09.01` | `09` | 保持 `09` | mechanics, elasticity / FEM tasks and generated mechanics data | high | 否 |
| `ASD-0129` | `09 / 09.01` | `09` | 保持 `09` | CFD cases and OpenFOAM simulation setup / validation | high | 否 |
| `ASD-0132` | `01 / 01.04` | `01.04` bucket | 保持独立 `01.04` | general scientific idea-generation benchmark and human evaluation | medium-high | 否 |
| `ASD-0133` | `02 / 02.01` | `02` | 保持 `02` | multi-band galaxy observations and JWST Little Red Dot galaxies | high | 否 |
| `ASD-0134` | `03 / 03.01` | `03` | 保持 `03`，列入 benchmark-heavy 复核 | chemistry-specific reasoning tasks and SciBench chemistry datasets | medium-high | 是，需补 note 中 confirmed-core strength 表述 |
| `ASD-0135` | `04 / 04.04` | `04` | 保持 `04` | metamaterial patterns / properties and simulation design metrics | high | 否 |
| `ASD-0136` | `02 / 02.01` | `02` | 保持 `02` | astronomical observations and transient / supernova events | high | 否 |
| `ASD-0137` | `06 / 06.03` | `06` | 保持 `06` | primers, amplicon sequencing and targeted NGS workflow | high | 否 |
| `ASD-0138` | `06 / 06.03` | `06` | 保持 `06` | scRNA-seq and spatial transcriptomics datasets | high | 是，主表旧字段 / note 表述需确认 concrete-object wording |
| `ASD-0139` | `01 / 01.04` | `01.04` bucket | 保持独立 `01.04`，列入 `02` 复核 | physics-reasoning framing without stable physics object identified | medium | 是，需全文确认是否有具体物理对象 case |
| `ASD-0140` | `11 / 11.07` | `11` | 保持 `11.07` | scientific hypothesis generation / knowledge-production workflow | medium-high | 是，需 note 中强调非 `01.04` 原因 |
| `ASD-0141` | `06 / 06.03` | `06;07` | 记录 `07` add-module 候选，不改表 | transcriptional regulation plus esophageal cancer regulatory-circuit case | medium | 是，高优先回原文和 note 边界修订 |
| `ASD-0145` | `01 / 01.04` | `01.04` bucket | 保持独立 `01.04` | automated research-review-refinement workflow without concrete science object | high | 否 |
| `ASD-0146` | `01 / 01.04` | `01.04`, possible `01` | 保持独立 `01.04` 倾向，列入 `01` 复核 | ML task environments may be evaluation environments rather than final objects | medium | 是，需原文确认 relaxed 口径是否支持正式 `01` |
| `ASD-0147` | `01 / 01.04` | `01.04` bucket | 保持独立 `01.04`，列入轻量复核 | idea novelty / diversity evaluation lacks concrete domain object evidence | medium | 是，元数据和对象强度需修订 |
| `ASD-0149` | `03 / 03.03` | `03` | 保持 `03` | photocatalysis, biocatalysis, cross-coupling and enantioselective catalysis | high | 否 |
| `ASD-0150` | `03 / 03.03` | `03` | 保持 `03` | aldol condensation reaction and cost-yield Pareto optimization | high | 否 |
| `ASD-0151` | `04 / 04.04` | `04;02` | 记录 `02` add-module 候选，不改表 | metasurface material system plus spontaneous-emission physical process | medium-high | 是，高优先原文复核与 note 修订 |
| `ASD-0152` | `06 / 06.03` | `06` | 保持 `06` | public scRNA-seq datasets and standardized single-cell analysis outputs | high | 否 |
| `ASD-0154` | `04 / 04.04` | `04` | 保持 `04` | Sn-Bi binary thin-film system and temperature-composition phase diagram | high | 否 |

## 四、Wave B 统计

| Metric | Count |
|---|---:|
| reviewed records | 56 |
| Reviewer-covered records | 56 |
| high / medium-high stable single-module or bucket records | 34 |
| relaxed add-module candidates | 9 |
| `01.04` exit candidates | 2 |
| uncertain `01.04` / object-module boundary cases | 5 |
| records needing original-paper / full-text recheck | 24 |
| records needing note wording or classification-note revision | 12 |
| direct master-list edits | 0 |

按本轮建议模块展开统计如下。此表是 Wave B 审计建议，不是当前主列表正式计数。

| Suggested module / bucket | Wave B count |
|---|---:|
| `01` | 2 |
| `02` | 9 |
| `03` | 11 |
| `04` | 13 |
| `06` | 14 |
| `07` | 10 |
| `09` | 4 |
| `11` | 3 |
| independent `01.04` bucket, high / medium-high confidence | 6 |
| uncertain: `01.04` / object-module boundary | 5 |

说明：multi-module candidates 会使模块展开数大于 reviewed record count；`ASD-0111`, `ASD-0139`, `ASD-0146`, `ASD-0147` 等仍需原文复核，不宜在 schema migration 前直接写入正式模块。

## 五、关键变化相对前一轮保守试跑

此前保守试跑在这一切片上没有稳定记录足够强的 multi-module assignment。当前 relaxed 口径下，该结论不再适合作为本轮分类依据。

本轮新增的主要迁移压力如下：

| 类型 | ID | 当前判断 |
|---|---|---|
| `01.04 -> 01;11` | `ASD-0069`, `ASD-0100` | ML / code reproduction 与 peer review / reproducibility evaluation 触发正式对象模块候选 |
| `06 -> 06;07` | `ASD-0071`, `ASD-0097`, `ASD-0141` | disease, COVID-19, cancer case 等医学对象证据需要原文确认 |
| `07 -> 07;06` | `ASD-0077`, `ASD-0118` | biomedical general-agent 可能同时有生命科学 / bioinformatics object tasks |
| `04 -> 03;04;07` | `ASD-0096` | dZiner 同时涉及 surfactant molecules、MOF/linker/material design 和 WDR5 ligand case |
| `04 -> 04;02` | `ASD-0151` | metasurface material system 与 spontaneous-emission physics process 同时出现 |
| `01.04 -> possible 01` | `ASD-0146` | ML task environments 是否是正式计算科学对象需原文复核 |

## 六、原文复核与笔记修订队列

以下记录需要优先回原文 / PDF / publisher page，且在确认后同步修订对应 `Notes/` 中的分类表述或 evidence 字段。

| ID | Note path | 需要修订 / 复核的问题 |
|---|---|---|
| `ASD-0069` | `Notes/01_Formal_Information_and_Computational_Sciences/Lu_2024_AI_Scientist.md` | 判断 AI Scientist 是否应从 pure `01.04` 改为正式 `01`，以及 peer-review benchmark 是否触发 `11.07` |
| `ASD-0071` | `Notes/06_Life_Sciences/Liu_2024_TAIS_Gene_Expression.md` | 补写 gene-expression 与 disease-condition evidence，说明是否新增 `07` |
| `ASD-0077` | `Notes/07_Medical_and_Health_Sciences/Jin_2025_STELLA.md` | 核对 biomedical benchmark / cancer drug-resistance case 是否支持 `06` |
| `ASD-0096` | `Notes/04_Materials_Science/Ansari_2024_dZiner.md` | 高优先核对 `03/04/07` 三模块证据，避免旧 note 只写材料 inverse design |
| `ASD-0097` | `Notes/06_Life_Sciences/Alber_2026_CellVoyager.md` | 补写 COVID-19 disease case 是否足以新增 `07` |
| `ASD-0100` | `Notes/01_Formal_Information_and_Computational_Sciences/Xiang_2025_SciReplicate_Bench.md` | 核对 scientific reproducibility / knowledge-production 是否应转 `11.07` 或同时记录 `01` |
| `ASD-0111` | 当前 note path 需核对 | 回原文确认是否只有 general benchmark，还是有具体领域 case |
| `ASD-0118` | 当前 note path 需核对 | 核对 Biomni task inventory 是否支持 `06`，并避免错误回收到 `01.04` |
| `ASD-0127` | 当前 note path 需核对 | 核对 AI Cosmologist 是否有稳定 cosmology object result，而非 generic data-analysis substrate |
| `ASD-0138` | `Notes/06_Life_Sciences/Xiao_2024_CellAgent_SingleCell_Analysis.md` | 主表 / note 中若仍有 `has concrete object = no` 风格表述，应改为具体 scRNA-seq / spatial transcriptomics object evidence |
| `ASD-0140` | `Notes/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Yang_2024_Open_Domain_Hypotheses_Discovery.md` | 强化其归 `11.07` 而非 `01.04` 的 scientific knowledge production 依据 |
| `ASD-0141` | `Notes/06_Life_Sciences/Zhang_2025_TransAgent_Transcriptional_Regulation.md` | 核对 esophageal cancer regulatory-circuit case 是否足以新增 `07` |
| `ASD-0146` | `Notes/01_Formal_Information_and_Computational_Sciences/Liu_2024_AIGS.md` | 核对 ML task environments 是否只是 evaluation，还是正式 `01` object evidence |
| `ASD-0147` | `Notes/01_Formal_Information_and_Computational_Sciences/Hu_2024_Nova.md` | 修订对象强度 / metadata uncertainty 表述 |
| `ASD-0151` | `Notes/04_Materials_Science/Desai_2026_Spontaneous_Emission_SDL.md` | 核对是否应记录 `02` physics process module，同时 primary filing 仍保留 `04` |

## 七、主控结论

Batch 1 / Wave B 已按 relaxed multi-module 口径完成新一轮复核。与旧保守报告相比，本 wave 明确出现多个 add-module 与 `01.04` exit 候选，尤其集中在 `01.04 / 01 / 11.07`、`06 / 07`、`03 / 04 / 07` 和 `04 / 02` 边界。

本 wave 不支持重构 `01-11` 一级体系；真正需要处理的是 row-level schema migration，以及将原文证据同步写回论文笔记，避免 note 继续保留“单主类 / 核心贡献优先 / 只是 demo 不计模块”的旧口径。
