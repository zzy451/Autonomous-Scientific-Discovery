# Batch 1 / Wave B 多模块重分类审计报告

> 日期：2026-06-20  
> 范围：`agent_master_paper_list.md` confirmed 记录序号 58-113。  
> 对应计划：`Coverage_Check/multi_module_reclassification_flat_batch_plan_451_confirmed_2026-06-20.md`。  
> 当前阶段：Reviewer 审核进行中；本文档先记录基线、分工和待合并字段，最终主控裁决将在 Reviewer 返回后补入。

## 一、基线

本轮开始前主列表状态：

- master list total records: 871
- confirmed record-level count: 451
- `needs_review`: 0
- confirmed `08`: 3
- legacy confirmed `01.04`: 46

legacy confirmed 主类分布：

| Legacy main class | Count |
|---|---:|
| `01` | 52 |
| `02` | 29 |
| `03` | 60 |
| `04` | 95 |
| `05` | 23 |
| `06` | 51 |
| `07` | 51 |
| `08` | 3 |
| `09` | 34 |
| `10` | 23 |
| `11` | 30 |

## 二、Wave B 分工

| Reviewer | Agent | 记录数 | 分配 ID |
|---|---|---:|---|
| B-Reviewer-1 | Franklin | 14 | `ASD-0069`, `ASD-0070`, `ASD-0071`, `ASD-0075`, `ASD-0076`, `ASD-0077`, `ASD-0079`, `ASD-0080`, `ASD-0081`, `ASD-0083`, `ASD-0084`, `ASD-0085`, `ASD-0089`, `ASD-0090` |
| B-Reviewer-2 | Ampere | 14 | `ASD-0091`, `ASD-0093`, `ASD-0094`, `ASD-0095`, `ASD-0096`, `ASD-0097`, `ASD-0100`, `ASD-0111`, `ASD-0112`, `ASD-0113`, `ASD-0114`, `ASD-0115`, `ASD-0116`, `ASD-0117` |
| B-Reviewer-3 | Euclid | 14 | `ASD-0118`, `ASD-0119`, `ASD-0120`, `ASD-0121`, `ASD-0124`, `ASD-0125`, `ASD-0126`, `ASD-0127`, `ASD-0128`, `ASD-0129`, `ASD-0132`, `ASD-0133`, `ASD-0134`, `ASD-0135` |
| B-Reviewer-4 | Gibbs | 14 | `ASD-0136`, `ASD-0137`, `ASD-0138`, `ASD-0139`, `ASD-0140`, `ASD-0141`, `ASD-0145`, `ASD-0146`, `ASD-0147`, `ASD-0149`, `ASD-0150`, `ASD-0151`, `ASD-0152`, `ASD-0154` |

## 三、主控合并口径

本轮沿用 Wave A 校准后的口径：

- 平台感强但对象实验证据明确时，不回收到 `01.04`。
- drug discovery / DMTA / ADMET / target-protein / therapeutic candidate 目标优先 `07`。
- 分子性质、反应、量子化学、化学机器人和化学文献数据抽取通常保持 `03`；drug-likeness 或泛泛材料表述不足以自动多模块。
- omics、single-cell、perturb-seq、gene-set discovery 通常保持 `06`；precision medicine 或 disease framing 不足以自动转 `07`。
- 没有具体科学对象实验、主要验证 general research-agent workflow / automated research platform / code experimentation / idea generation 的记录保持独立 `01.04`。
- 正式 `01` 用于数学、算法、程序、形式系统、计算理论、知识表示、信息结构、系统科学与复杂性对象；独立 `01.04` 用于无具体对象实验的通用 ASD/general 方法。
- 不因为系统 general / cross-domain / multi-agent 就自动多模块；multi-module 必须由多个具体科学对象的独立实质实验或结果证据支撑。

默认不直接改主列表，除非同时满足：

- Reviewer 证据清楚；
- 主控复核规则一致；
- 不依赖缺失全文；
- 不会造成 schema 迁移半成品。

## 四、Reviewer 原始输出

### B-Reviewer-1: Franklin

状态：已返回，14 / 14 条完整覆盖。

主要结论：

- `ASD-0069`, `ASD-0089`: 保持独立 `01.04` general-method bucket。
- `ASD-0070`, `ASD-0076`: 保持 `03` 化学科学；其中 `ASD-0070` 需要复核其 hypothesis 数据构成是否跨材料/生命对象。
- `ASD-0075`, `ASD-0080`, `ASD-0084`: 保持 `04` 材料科学；其中 `ASD-0084` 仍是 metadata-level evidence，需要全文补强。
- `ASD-0071`, `ASD-0081`, `ASD-0085`: 保持 `06` 生命科学。
- `ASD-0077`, `ASD-0079`, `ASD-0083`: 保持 `07` 医学与健康科学；其中 `ASD-0077` 是 `07 / 01.04 / 06` 边界。
- `ASD-0090`: 保持 `02` 物理学、天文学与宇宙科学。
- 本切片未发现足够强的 multi-module assignment。

### B-Reviewer-2: Ampere

状态：已返回，14 / 14 条完整覆盖。

主要结论：

- `ASD-0091`, `ASD-0093`, `ASD-0094`, `ASD-0117`: 保持 `03` 化学科学；`ASD-0117` 需后续确认 zeolite/material performance 是否只是应用语境。
- `ASD-0095`, `ASD-0116`: 保持 `04` 材料科学。
- `ASD-0097`, `ASD-0114`: 保持 `06` 生命科学。
- `ASD-0112`, `ASD-0113`, `ASD-0115`: 保持 `07` 医学与健康科学；`ASD-0115` 是高优先级 `07 / 01.04` 边界样本。
- `ASD-0111`: 保持独立 `01.04` general-method bucket。
- `ASD-0096`: Reviewer 建议考虑 `04 + 07` multi-module，但置信度为 medium，需主控复核。
- `ASD-0100`: Reviewer 建议按 scientific reproducibility 强规则复核 `11.07 / 01.04` 边界。

### B-Reviewer-3: Euclid

状态：已返回，14 / 14 条完整覆盖。

主要结论：

- `ASD-0118`: 暂保持 `07`，但因具体 biomedical object evidence 偏抽象，建议主控复核。
- `ASD-0119`, `ASD-0135`: 保持 `04` 材料科学。
- `ASD-0120`, `ASD-0121`, `ASD-0127`, `ASD-0133`: 保持 `02` 物理学、天文学与宇宙科学；`ASD-0127` 需全文确认不是 generic data-analysis substrate。
- `ASD-0124`, `ASD-0125`, `ASD-0128`, `ASD-0129`: 保持 `09` 工程与工业技术科学。
- `ASD-0126`: 保持 `06` 生命科学。
- `ASD-0132`: 保持独立 `01.04` general-method bucket。
- `ASD-0134`: 保持 `03` 化学科学，但 benchmark-heavy core strength 需全文复核。
- 本切片未发现足够强的 multi-module assignment。

### B-Reviewer-4: Gibbs

状态：已返回，14 / 14 条完整覆盖。

主要结论：

- `ASD-0136`: 保持 `02` 物理学、天文学与宇宙科学。
- `ASD-0137`, `ASD-0138`, `ASD-0141`, `ASD-0152`: 保持 `06` 生命科学。
- `ASD-0139`, `ASD-0145`, `ASD-0146`, `ASD-0147`: 保持独立 `01.04` general-method bucket；`ASD-0139`, `ASD-0147` 需要全文补强。
- `ASD-0140`: 保持 `11.07`，但存在 `11.07 / 01.04` 边界压力。
- `ASD-0149`, `ASD-0150`: 保持 `03` 化学科学。
- `ASD-0151`, `ASD-0154`: 保持 `04` 材料科学。
- 本切片未发现足够强的 multi-module assignment。

## 五、主控裁决表

Wave B 共 56 条，全部完成 Reviewer 覆盖。主控裁决如下：

| ID | Legacy filing | Reviewer suggestion | 主控裁决 | 是否改主列表 | 备注 |
|---|---|---|---|---|---|
| `ASD-0069` | `01 / 01.04` | `01.04` | 保持独立 `01.04` | 否 | The AI Scientist 是通用自动科研流程，ML demos 不构成正式对象模块 |
| `ASD-0070` | `03 / 03.04` | `03`, `main_control_review` | 暂保持 `03`，列入全文复核 | 否 | Chem3 / hypothesis ranking 方向偏化学，但需确认 124 hypotheses 的领域构成 |
| `ASD-0071` | `06 / 06.03` | `06` | 保持 `06` | 否 | gene expression / omics data 是主对象，疾病语境不足以转 `07` |
| `ASD-0075` | `04 / 04.04` | `04` | 保持 `04` | 否 | nanohelix materials / structure-property optimization |
| `ASD-0076` | `03 / 03.04` | `03` | 保持 `03` | 否 | molecular optimization；drug-like metrics 不足以加 `07` |
| `ASD-0077` | `07 / 07.04` | `main_control_review` | 暂保持 `07`，列入全文复核 | 否 | STELLA 是 biomedical research agent，但 `06 / 07 / 01.04` 边界仍需全文证据 |
| `ASD-0079` | `07 / 07.04` | `07` | 保持 `07` | 否 | drug-target interaction prediction 属于 drug discovery 对象 |
| `ASD-0080` | `04 / 04.02` | `04` | 保持 `04` | 否 | MOF structures / porous materials，linker chemistry 是支撑对象 |
| `ASD-0081` | `06 / 06.03` | `06` | 保持 `06` | 否 | CRISPR / gene-editing experiment design |
| `ASD-0083` | `07 / 07.04` | `07` | 保持 `07` | 否 | dry AMD / therapeutic candidate / wet-lab validation 对象明确 |
| `ASD-0084` | `04 / 04.02` | `main_control_review` | 暂保持 `04`，列入全文复核 | 否 | alloy design 方向明确，但本地 note 仍是 metadata-level evidence |
| `ASD-0085` | `06 / 06.03` | `06` | 保持 `06` | 否 | protein discovery / protein design，biomaterials 只作交叉属性 |
| `ASD-0089` | `01 / 01.04` | `01.04` | 保持独立 `01.04` | 否 | research-code codification / general scientific coding workflow |
| `ASD-0090` | `02 / 02.02` | `02` | 保持 `02` | 否 | superconducting quantum processor / quantum states |
| `ASD-0091` | `03 / 03.04` | `03` | 保持 `03` | 否 | chemical search over molecules/reactions/spectra；polymer mention 不足以加 `04` |
| `ASD-0093` | `03 / 03.04` | `03` | 保持 `03`，列入全文证据补强 | 否 | ChemCrow 方向稳定，但 note 偏 metadata-heavy |
| `ASD-0094` | `03 / 03.03` | `03` | 保持 `03` | 否 | Coscientist 执行 wet/robotic chemistry reaction experiments |
| `ASD-0095` | `04 / 04.04` | `04` | 保持 `04` | 否 | materials-science data integration / interpretation |
| `ASD-0096` | `04 / 04.04` | add `07` | 暂不采纳 add_module，保持 `04`，列入复核 | 否 | dZiner full note 仍判定材料 inverse design 为主；WDR5 ligand 目前更像示例任务，不足以高置信新增 `07` |
| `ASD-0097` | `06 / 06.03` | `06` | 保持 `06` | 否 | single-cell / compbio analysis；COVID-19 语境不足以转 `07` |
| `ASD-0100` | `01 / 01.04` | `11` / `main_control_review` | 暂保持独立 `01.04`，列入 `11.07` 边界复核 | 否 | full note 当前仍把它作为 agent-driven scientific reproduction benchmark；科学复现强规则需后续统一校准 |
| `ASD-0111` | `01 / 01.04` | `01.04` | 保持独立 `01.04` | 否 | general scientific-agent capability benchmark，无具体对象实验 |
| `ASD-0112` | `07 / 07.04` | `07` | 保持 `07`，列入全文复核 | 否 | drug-molecule space / COVID-19 target-oriented design，需确认 therapeutic objective 主导 |
| `ASD-0113` | `07 / 07.04` | `07` | 保持 `07` | 否 | virtual pharma / target-lead-optimization endpoint |
| `ASD-0114` | `06 / 06.03` | `06` | 保持 `06` | 否 | protein / peptide design principles |
| `ASD-0115` | `07 / 07.04` | `07`, `main_control_review` | 保持 `07`，列入高优先级全文复核 | 否 | 本地 note 支持 biomedical validation 主导，但 general co-scientist framing 仍强 |
| `ASD-0116` | `04 / 04.04` | `04` | 保持 `04` | 否 | electromagnetic metamaterials / programmable metasurfaces |
| `ASD-0117` | `03 / 03.04` | `03` | 保持 `03`，列入全文复核 | 否 | OSDA molecules 是直接设计对象；zeolite/material performance 是否独立支撑 `04` 待查 |
| `ASD-0118` | `07 / 07.04` | `main_control_review` | 暂保持 `07`，列入全文复核 | 否 | Biomni generality 限定在 biomedical research，但具体对象实验仍偏抽象 |
| `ASD-0119` | `04 / 04.03` | `04` | 保持 `04` | 否 | MOF structures / porous-material properties |
| `ASD-0120` | `02 / 02.01` | `02` | 保持 `02` | 否 | ground-based gamma astronomy / CTA workflows |
| `ASD-0121` | `02 / 02.01` | `02` | 保持 `02` | 否 | cosmological parameter inference |
| `ASD-0124` | `09 / 09.05` | `09` | 保持 `09` | 否 | structural / civil engineering analysis |
| `ASD-0125` | `09 / 09.03` | `09` | 保持 `09` | 否 | power electronics modulation design |
| `ASD-0126` | `06 / 06.03` | `06` | 保持 `06` | 否 | genomics / bioinformatics workflow support |
| `ASD-0127` | `02 / 02.01` | `02` | 保持 `02`，列入全文复核 | 否 | AI Cosmologist 目前指向 cosmology data analysis，但需确认不是 generic automation substrate |
| `ASD-0128` | `09 / 09.01` | `09` | 保持 `09` | 否 | mechanics / elasticity / FEM engineering analysis |
| `ASD-0129` | `09 / 09.01` | `09` | 保持 `09` | 否 | CFD / OpenFOAM engineering simulation cases |
| `ASD-0132` | `01 / 01.04` | `01.04` | 保持独立 `01.04` | 否 | general scientific idea-generation method，不是 science-system object study |
| `ASD-0133` | `02 / 02.01` | `02` | 保持 `02` | 否 | galaxy observations / JWST astrophysical scenarios |
| `ASD-0134` | `03 / 03.01` | `03` | 保持 `03`，列入全文复核 | 否 | chemistry-specific reasoning benchmark；不因应用 mention 加 `04/07` |
| `ASD-0135` | `04 / 04.04` | `04` | 保持 `04` | 否 | metamaterial design / structure-property simulation |
| `ASD-0136` | `02 / 02.01` | `02` | 保持 `02` | 否 | astronomical observations / transient events |
| `ASD-0137` | `06 / 06.03` | `06` | 保持 `06` | 否 | primer design / amplicon sequencing |
| `ASD-0138` | `06 / 06.03` | `06` | 保持 `06` | 否 | scRNA-seq / spatial transcriptomics analysis |
| `ASD-0139` | `01 / 01.04` | `01.04` | 保持独立 `01.04`，列入全文复核 | 否 | physics framing 目前更像 scientific reasoning context，尚无实质 physics-object result |
| `ASD-0140` | `11 / 11.07` | `11` | 保持 `11.07`，列入边界复核 | 否 | note 支持 scientific hypothesis / knowledge production 对象；但 benchmark/general capability 压力真实存在 |
| `ASD-0141` | `06 / 06.03` | `06` | 保持 `06` | 否 | transcriptional regulation / multi-omics regulator analysis |
| `ASD-0145` | `01 / 01.04` | `01.04` | 保持独立 `01.04` | 否 | automated review 是 general research-agent feedback mechanism，不是 peer-review object |
| `ASD-0146` | `01 / 01.04` | `01.04` | 保持独立 `01.04` | 否 | general automated falsification / AIGS，ML tasks 是评估环境 |
| `ASD-0147` | `01 / 01.04` | `01.04` | 保持独立 `01.04`，列入全文复核 | 否 | idea novelty/diversity workflow，证据强度偏轻 |
| `ASD-0149` | `03 / 03.03` | `03` | 保持 `03` | 否 | reaction optimization / photocatalysis / biocatalysis |
| `ASD-0150` | `03 / 03.03` | `03` | 保持 `03` | 否 | aldol condensation reaction / chemistry SDL |
| `ASD-0151` | `04 / 04.04` | `04` | 保持 `04` | 否 | semiconductor metasurfaces / nanophotonics material system |
| `ASD-0152` | `06 / 06.03` | `06` | 保持 `06`，列入全文复核 | 否 | scRNA-seq ingestion/standardization，需补强 validation strength |
| `ASD-0154` | `04 / 04.04` | `04` | 保持 `04` | 否 | Sn-Bi thin-film phase diagram / autonomous materials science |

## 六、Wave B 口径校准结论

基于 56 条完整结果，本轮形成以下校准结论：

1. Wave B 仍未发现高置信 multi-module assignment。`ASD-0096` 是最接近多模块的样本，但本地 full note 将全篇稳定对象判为 materials inverse design；WDR5 ligand 暂作为交叉/示例任务处理，不直接新增 `07`。
2. 通用 co-scientist / general biomedical agent 不自动进入 `01.04`。如果最强可见验证绑定 biomedical discovery、drug repurposing、target discovery 或 biomedical task execution，可暂保留 `07`，但必须列入全文复核，例如 `ASD-0077`, `ASD-0115`, `ASD-0118`。
3. scientific reproducibility 与 general research-agent benchmark 的边界需要后续统一校准。`ASD-0100` 暂保持 `01.04`，因为当前 full note 将其解释为 agent-driven reproduction benchmark；但它与 `11.07` 的科学复现强规则存在真实张力。
4. 天文、宇宙学、量子实验、结构工程、CFD、power electronics 等平台感较强的记录，只要对象任务绑定具体科学对象或工程系统，仍保持对应对象模块，不回收到 `01.04`。
5. `03 / 04` 与 `03 / 07` 边界继续按直接研究对象处理。MOF、metamaterial、alloy 等归 `04`；small molecules / reactions / organic structure-directing agents 归 `03`；drug-target / drug molecule design 在治疗转化目标明确时归 `07`。
6. `06 / 07` 边界继续保持 Wave A 口径：omics、single-cell、gene editing、protein design 通常归 `06`；疾病语境或 biomedical venue 不足以自动转 `07`。
7. 当前没有足够证据支持重构一级分类，问题主要集中在边界解释与低覆盖类稀缺性判断。

## 七、待主控复核队列

Wave B 暂列以下记录为主控复核或后续全文复核：

| ID | 当前 legacy | 初步问题 | 暂定处理 |
|---|---|---|---|
| `ASD-0070` | `03 / 03.04` | MOOSE-Chem3 的 hypothesis set 是否覆盖材料/生命等多对象仍需确认 | 暂保持 `03`，全文复核 |
| `ASD-0077` | `07 / 07.04` | STELLA 的 biomedical benchmark 与具体对象实验强度需确认 | 暂保持 `07`，全文复核 |
| `ASD-0084` | `04 / 04.02` | alloy design 方向稳定，但本地证据仍偏 metadata-level | 暂保持 `04`，全文复核 |
| `ASD-0096` | `04 / 04.04` | Reviewer 建议 `04 + 07`，但 WDR5 ligand 是否足以独立支撑 `07` 不确定 | 暂不新增模块，保持 `04` |
| `ASD-0100` | `01 / 01.04` | scientific reproducibility benchmark 与 `11.07` 强规则冲突 | 暂保持 `01.04`，后续统一校准 |
| `ASD-0112` | `07 / 07.04` | drug molecule optimization 是否由 therapeutic objective 主导需全文确认 | 暂保持 `07` |
| `ASD-0115` | `07 / 07.04` | general co-scientist framing 强，但 note 支持 biomedical validation 主导 | 暂保持 `07`，高优先级全文复核 |
| `ASD-0117` | `03 / 03.04` | OSDA molecule 与 zeolite/material performance 边界需确认 | 暂保持 `03` |
| `ASD-0118` | `07 / 07.04` | Biomni 具体 biomedical object evidence 偏抽象 | 暂保持 `07`，全文复核 |
| `ASD-0127` | `02 / 02.01` | AI Cosmologist 是否有足够 cosmology object evidence 需全文确认 | 暂保持 `02` |
| `ASD-0134` | `03 / 03.01` | chemistry reasoning benchmark 的 confirmed-core strength 需补强 | 暂保持 `03` |
| `ASD-0139` | `01 / 01.04` | physics framing 是否包含 substantive physics-object result 需全文确认 | 暂保持 `01.04` |
| `ASD-0140` | `11 / 11.07` | scientific hypothesis generation 是 knowledge-production object 还是 general benchmark | 暂保持 `11.07` |
| `ASD-0147` | `01 / 01.04` | idea-generation workflow 证据偏轻 | 暂保持 `01.04` |
| `ASD-0152` | `06 / 06.03` | scRNA-seq standardization 方向稳定，但 validation strength 需补强 | 暂保持 `06` |

## 八、本轮统计

| Metric | Count |
|---|---:|
| reviewed records | 56 |
| Reviewer-covered records | 56 |
| unchanged by主控 | 56 |
| add_module | 0 |
| move_primary | 0 |
| move_to_01.04 | 0 |
| demote/background-review candidate | 0 |
| main-control / full-text follow-up queue | 15 |
| records with `full_text_required=yes` from Reviewer output | 20 |

本轮不修改 `agent_master_paper_list.md`。主列表 record-level confirmed count 仍为 `451`，`needs_review` 仍为 `0`，confirmed `08` 仍为 `3`。

Batch 1 至此完成 Wave A + Wave B 共 `113` 条 confirmed 记录的平铺复核。本批暂未发现高置信 multi-module assignment，也未发生主列表落地变更；主要产出是稳定了 `01.04 / domain`、`03 / 04`、`03 / 07`、`06 / 07`、`07 / 01.04`、`11.07 / 01.04` 等边界样本队列。
