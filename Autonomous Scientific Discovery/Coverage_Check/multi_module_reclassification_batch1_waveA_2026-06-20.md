# Batch 1 / Wave A 多模块重分类审计报告

> 日期：2026-06-20  
> 范围：`agent_master_paper_list.md` confirmed 记录序号 1-57。  
> 对应计划：`Coverage_Check/multi_module_reclassification_flat_batch_plan_451_confirmed_2026-06-20.md`。  
> 当前阶段：Reviewer 审核进行中，本文档先记录基线、分工和待合并字段；最终主控裁决将在 Reviewer 返回后补入。

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

## 二、Wave A 分工

| Reviewer | Agent | 记录数 | 分配 ID |
|---|---|---:|---|
| A-Reviewer-1 | Lagrange | 15 | `ASD-0001`, `ASD-0002`, `ASD-0003`, `ASD-0004`, `ASD-0005`, `ASD-0006`, `ASD-0007`, `ASD-0008`, `ASD-0009`, `ASD-0010`, `ASD-0012`, `ASD-0013`, `ASD-0014`, `ASD-0016`, `ASD-0017` |
| A-Reviewer-2 | Russell | 14 | `ASD-0018`, `ASD-0019`, `ASD-0020`, `ASD-0022`, `ASD-0024`, `ASD-0025`, `ASD-0026`, `ASD-0028`, `ASD-0029`, `ASD-0030`, `ASD-0031`, `ASD-0032`, `ASD-0033`, `ASD-0034` |
| A-Reviewer-3 | Jason | 14 | `ASD-0035`, `ASD-0036`, `ASD-0037`, `ASD-0038`, `ASD-0040`, `ASD-0041`, `ASD-0044`, `ASD-0045`, `ASD-0046`, `ASD-0047`, `ASD-0048`, `ASD-0049`, `ASD-0051`, `ASD-0052` |
| A-Reviewer-4 | Gauss | 14 | `ASD-0053`, `ASD-0054`, `ASD-0055`, `ASD-0056`, `ASD-0057`, `ASD-0058`, `ASD-0059`, `ASD-0060`, `ASD-0061`, `ASD-0062`, `ASD-0063`, `ASD-0064`, `ASD-0065`, `ASD-0068` |

## 三、主控合并口径

本轮只做 Wave A 口径校准和审计记录。默认不直接改主列表，除非同时满足：

- Reviewer 证据清楚；
- 主控复核规则一致；
- 不依赖缺失全文；
- 不会造成 schema 迁移半成品。

## 四、Reviewer 原始输出

### A-Reviewer-1: Lagrange

状态：已返回，15 / 15 条完整覆盖。

主要结论：

- `ASD-0001`, `ASD-0007`, `ASD-0009`, `ASD-0016`: 保持 `04` 材料科学。
- `ASD-0003`, `ASD-0005`, `ASD-0010`, `ASD-0012`: 保持 `03` 化学科学。
- `ASD-0002`, `ASD-0008`, `ASD-0017`: 保持 `07` 医学与健康科学。
- `ASD-0014`: 保持 `06` 生命科学，但标记 `06/07` 边界与全文核验需求。
- `ASD-0004`, `ASD-0013`: 保持独立 `01.04` general-method bucket。
- `ASD-0006`: 建议 `main_control_review`，理由是当前证据不足以证明具体生命科学对象实验，可能更接近通用科研/reporting workflow。

### A-Reviewer-2: Russell

状态：已返回，14 / 14 条完整覆盖。

主要结论：

- `ASD-0018`, `ASD-0019`, `ASD-0032`: 保持独立 `01.04` general-method bucket。
- `ASD-0020`, `ASD-0033`: 保持 `06` 生命科学。
- `ASD-0034`: 倾向保持 `06`，但建议 `main_control_review` 和全文核验。
- `ASD-0022`, `ASD-0025`, `ASD-0029`: 保持 `03` 化学科学。
- `ASD-0024`, `ASD-0028`, `ASD-0030`: 保持 `07` 医学与健康科学。
- `ASD-0026`, `ASD-0031`: 保持 `04` 材料科学。

### A-Reviewer-3: Jason

状态：已返回，14 / 14 条完整覆盖。

主要结论：

- `ASD-0035`, `ASD-0045`, `ASD-0046`: 保持 `04` 材料科学。
- `ASD-0036`, `ASD-0037`, `ASD-0038`: 保持 `03` 化学科学。
- `ASD-0041`: 保持 `07` 医学与健康科学。
- `ASD-0044`: 保持 `02` 物理学、天文学与宇宙科学。
- `ASD-0047`, `ASD-0052`: 保持 `09` 工程与工业技术科学。
- `ASD-0040`, `ASD-0048`: 保持独立 `01.04` general-method bucket。
- `ASD-0049`: 倾向保持 `06`，但建议 `main_control_review` 和全文核验。
- `ASD-0051`: 保持 `06` 生命科学。

### A-Reviewer-4: Gauss

状态：已返回，14 / 14 条完整覆盖。

主要结论：

- `ASD-0053`, `ASD-0059`, `ASD-0060`, `ASD-0062`: 保持独立 `01.04` general-method bucket；其中 `ASD-0060` 作为 cross-domain benchmark / general-method tension 进入主控复核。
- `ASD-0054`: 保持 `07` 医学与健康科学。
- `ASD-0055`, `ASD-0064`: 保持 `06` 生命科学；其中 `ASD-0055` 需要全文复核证据强度。
- `ASD-0056`, `ASD-0061`: 保持 `03` 化学科学；其中 `ASD-0056` 是 `03/04` 边界。
- `ASD-0057`: 保持 `09` 工程与工业技术科学。
- `ASD-0058`: 保持 `02` 物理学、天文学与宇宙科学。
- `ASD-0063`: 保持正式 `01` 形式、信息与计算科学，不进入 `01.04`。
- `ASD-0065`, `ASD-0068`: 保持 `04` 材料科学。

## 五、主控裁决表

Wave A 共 57 条，全部完成 Reviewer 覆盖。主控裁决如下：

| ID | Legacy filing | Reviewer suggestion | 主控裁决 | 是否改主列表 | 备注 |
|---|---|---|---|---|---|
| `ASD-0001` | `04 / 04.04` | `04` | 保持 `04` | 否 | 材料对象明确 |
| `ASD-0002` | `07 / 07.04` | `07` | 保持 `07` | 否 | healthcare / EHR 对象明确 |
| `ASD-0003` | `03 / 03.04` | `03` | 保持 `03` | 否 | chemistry tool benchmark 不足以加 `04` |
| `ASD-0004` | `01 / 01.04` | `01.04` | 保持独立 `01.04` | 否 | 通用 closed-loop research-agent |
| `ASD-0005` | `03 / 03.04` | `03` | 保持 `03` | 否 | 化学机器人实验；全文细节待补 |
| `ASD-0006` | `06 / 06.03` | `main_control_review` | 暂不改表，列入复核队列 | 否 | 具体生命科学对象证据不足，可能更接近 `01.04` |
| `ASD-0007` | `04 / 04.04` | `04` | 保持 `04` | 否 | 材料设计假设生成 |
| `ASD-0008` | `07 / 07.04` | `07` | 保持 `07` | 否 | DMTA / drug discovery 对象明确 |
| `ASD-0009` | `04 / 04.04` | `04` | 保持 `04` | 否 | 材料文献数据集构建 |
| `ASD-0010` | `03 / 03.04` | `03` | 保持 `03` | 否 | quantum chemistry |
| `ASD-0012` | `03 / 03.04` | `03` | 保持 `03` | 否 | chemistry robotics，机器人是方法 |
| `ASD-0013` | `01 / 01.04` | `01.04` | 保持独立 `01.04` | 否 | AI Scientist 系统，非具体科学对象实验 |
| `ASD-0014` | `06 / 06.03` | `06` | 保持 `06` | 否 | spatial biology / omics；`06/07` 待全文校验 |
| `ASD-0016` | `04 / 04.04` | `04` | 保持 `04` | 否 | autonomous materials lab |
| `ASD-0017` | `07 / 07.04` | `07` | 保持 `07` | 否 | drug discovery pipeline |
| `ASD-0018` | `01 / 01.04` | `01.04` | 保持独立 `01.04` | 否 | general research assistant workflow |
| `ASD-0019` | `01 / 01.04` | `01.04` | 保持独立 `01.04` | 否 | collaborative autonomous research platform |
| `ASD-0020` | `06 / 06.03` | `06` | 保持 `06` | 否 | genetic perturbation / functional genomics |
| `ASD-0022` | `03 / 03.04` | `03` | 保持 `03` | 否 | computational chemistry workflows |
| `ASD-0024` | `07 / 07.04` | `07` | 保持 `07` | 否 | drug candidates / target proteins |
| `ASD-0025` | `03 / 03.04` | `03` | 保持 `03` | 否 | chemistry tool agent；drug-likeness 不足以转 `07` |
| `ASD-0026` | `04 / 04.04` | `04` | 保持 `04` | 否 | AFM on materials samples |
| `ASD-0028` | `07 / 07.04` | `07` | 保持 `07` | 否 | ADMET / DTI / HTS drug-discovery pipelines |
| `ASD-0029` | `03 / 03.04` | `03` | 保持 `03` | 否 | molecular / reaction chemistry tasks |
| `ASD-0030` | `07 / 07.04` | `07` | 保持 `07` | 否 | drug-target / biological activity prediction |
| `ASD-0031` | `04 / 04.04` | `04` | 保持 `04` | 否 | inorganic / crystal materials design |
| `ASD-0032` | `01 / 01.04` | `01.04` | 保持独立 `01.04` | 否 | code-based general ASD workflow |
| `ASD-0033` | `06 / 06.03` | `06` | 保持 `06` | 否 | single-cell / omics；precision medicine framing 不足以转 `07` |
| `ASD-0034` | `06 / 06.03` | `main_control_review` | 保持 `06` 倾向，列入全文复核 | 否 | Perturb-seq / functional genomics 对象较稳 |
| `ASD-0035` | `04 / 04.04` | `04` | 保持 `04` | 否 | materials discovery hypotheses |
| `ASD-0036` | `03 / 03.03` | `03` | 保持 `03` | 否 | wet-lab chemistry experiments |
| `ASD-0037` | `03 / 03.03` | `03` | 保持 `03` | 否 | exploratory synthetic chemistry |
| `ASD-0038` | `03 / 03.04` | `03` | 保持 `03` | 否 | chemical reaction data mining |
| `ASD-0040` | `01 / 01.04` | `01.04` | 保持独立 `01.04` | 否 | general research idea generation |
| `ASD-0041` | `07 / 07.04` | `07` | 保持 `07` | 否 | drug discovery / therapeutic candidates |
| `ASD-0044` | `02 / 02.01` | `02` | 保持 `02` | 否 | cosmological simulations / galaxy formation |
| `ASD-0045` | `04 / 04.04` | `04` | 保持 `04` | 否 | materials QA/tool agent，发现强度另记 |
| `ASD-0046` | `04 / 04.04` | `04` | 保持 `04` | 否 | topological materials discovery |
| `ASD-0047` | `09 / 09.01` | `09` | 保持 `09` | 否 | CFD engineering workflow |
| `ASD-0048` | `01 / 01.04` | `01.04` | 保持独立 `01.04` | 否 | open-ended auto-research / ML benchmarks |
| `ASD-0049` | `06 / 06.03` | `main_control_review` | 保持 `06` 倾向，列入全文复核 | 否 | BIA 的 scRNA-seq / bioinformatics 对象较稳，但 PDF 证据不足 |
| `ASD-0051` | `06 / 06.03` | `06` | 保持 `06` | 否 | gene-set knowledge discovery |
| `ASD-0052` | `09 / 09.01` | `09` | 保持 `09` | 否 | finite element engineering analysis |
| `ASD-0053` | `01 / 01.04` | `01.04` | 保持独立 `01.04` | 否 | general autonomous hypothesis verification |
| `ASD-0054` | `07 / 07.04` | `07` | 保持 `07` | 否 | SARS-CoV-2 nanobody therapeutic candidates |
| `ASD-0055` | `06 / 06.03` | `main_control_review` | 保持 `06` 倾向，列入全文复核 | 否 | BioMaster 是 bioinformatics / omics workflow，全文证据待补 |
| `ASD-0056` | `03 / 03.04` | `main_control_review` | 暂保持 `03`，列入 `03/04` 边界复核 | 否 | organic laser emitters 可能涉及材料/器件性能 |
| `ASD-0057` | `09 / 09.04` | `09` | 保持 `09` | 否 | chemical process / instrumentation diagrams |
| `ASD-0058` | `02 / 02.01` | `02` | 保持 `02` | 否 | meteorites / astrobiology / space science |
| `ASD-0059` | `01 / 01.04` | `01.04` | 保持独立 `01.04` | 否 | general hypothesis-generation method |
| `ASD-0060` | `01 / 01.04` | `main_control_review` | 保持独立 `01.04`，列入 cross-domain benchmark 复核 | 否 | PiFlow 主要贡献是 principle-aware general MAS |
| `ASD-0061` | `03 / 03.04` | `03` | 保持 `03` | 否 | quantum chemistry / QM9 molecular properties |
| `ASD-0062` | `01 / 01.04` | `01.04` | 保持独立 `01.04` | 否 | federated scientific workflow infrastructure |
| `ASD-0063` | `01 / 01.02` | `01` | 保持正式 `01` | 否 | algorithmic / mathematical discovery，不是 `01.04` |
| `ASD-0064` | `06 / 06.03` | `06` | 保持 `06` | 否 | spatial transcriptomics / tumor microenvironment mechanism |
| `ASD-0065` | `04 / 04.04` | `04` | 保持 `04` | 否 | materials experiment workflow |
| `ASD-0068` | `04 / 04.04` | `04` | 保持 `04` | 否 | metamaterial modeling and inverse design |

## 六、Wave A 口径校准结论

基于 57 条完整结果，本轮形成以下校准结论：

1. 平台感强但对象实验证据明确时，不回收到 `01.04`。例如 `ASD-0044` 保持 `02`，因为验证对象是 cosmological simulation / galaxy formation；`ASD-0047` 与 `ASD-0052` 保持 `09`，因为对象是 CFD / FEM 工程仿真。
2. drug discovery / DMTA / ADMET / target-protein / therapeutic candidate 目标优先 `07`，即使中间大量使用小分子、化学工具或 ML pipeline。代表记录包括 `ASD-0008`, `ASD-0017`, `ASD-0024`, `ASD-0028`, `ASD-0030`, `ASD-0041`。
3. 分子性质、反应、量子化学、化学机器人和化学文献数据抽取保持 `03`；drug-likeness 或材料表述不足以自动多模块。代表记录包括 `ASD-0003`, `ASD-0010`, `ASD-0012`, `ASD-0022`, `ASD-0025`, `ASD-0036`, `ASD-0038`。
4. omics、single-cell、perturb-seq、gene-set discovery 通常保持 `06`；precision medicine 或 disease framing 不足以自动转 `07`，除非目标是诊疗、药物转化或临床对象。代表记录包括 `ASD-0014`, `ASD-0020`, `ASD-0033`, `ASD-0034`, `ASD-0049`, `ASD-0051`。
5. 没有具体科学对象实验、主要验证 general research-agent workflow / automated research platform / code experimentation / idea generation 的记录保持独立 `01.04`。代表记录包括 `ASD-0004`, `ASD-0013`, `ASD-0018`, `ASD-0019`, `ASD-0032`, `ASD-0040`, `ASD-0048`。
6. 正式 `01` 与独立 `01.04` 的边界在 Wave A 中很清楚：`ASD-0063` 研究 algorithmic / mathematical discovery，保持正式 `01`；`ASD-0060` 虽有 nanomaterials / biomolecules / superconductors benchmark，但主要贡献是通用 principle-aware MAS，暂保持独立 `01.04`。
7. Wave A 没有发现足够强的 multi-module assignment。多数 cross-domain 或边界提示只是方法/benchmark/应用语境，不构成多个具体科学对象的独立实质贡献。

## 七、待主控复核队列

Wave A 暂列以下记录为主控复核或后续全文复核：

| ID | 当前 legacy | 初步问题 | 暂定处理 |
|---|---|---|---|
| `ASD-0006` | `06 / 06.03` | DORA AI Scientist 可能更像通用科研/reporting workflow；具体生命科学对象证据不足 | 暂不改表，进入主控复核 |
| `ASD-0034` | `06 / 06.03` | Perturb-seq 对象稳定，但需全文确认系统细节和实验轮次 | 暂不改表，保持 `06` 倾向 |
| `ASD-0049` | `06 / 06.03` | BIA 证据目前来自 metadata/code；PDF/full text 不足 | 暂不改表，保持 `06` 倾向 |
| `ASD-0055` | `06 / 06.03` | BioMaster 是 bioinformatics / omics workflow，全文证据待补 | 暂不改表，保持 `06` 倾向 |
| `ASD-0056` | `03 / 03.04` | organic laser emitters 处于 `03/04` 边界 | 暂不改表，保持 `03`，后续看分子发现 vs 材料/器件性能主导 |
| `ASD-0060` | `01 / 01.04` | PiFlow 有多个具体 benchmark 领域，但主要贡献是通用 principle-aware MAS | 暂不改表，保持独立 `01.04`，作为 cross-domain benchmark 校准样本 |

## 八、本轮统计

| Metric | Count |
|---|---:|
| reviewed records | 57 |
| Reviewer-covered records | 57 |
| unchanged by主控 | 57 |
| add_module | 0 |
| move_primary | 0 |
| move_to_01.04 | 0 |
| demote/background-review candidate | 0 |
| main-control / full-text follow-up queue | 6 |
| records with `full_text_required=yes` from Reviewer output | 11 |

本轮不修改 `agent_master_paper_list.md`。主列表 record-level confirmed count 仍为 `451`，`needs_review` 仍为 `0`，confirmed `08` 仍为 `3`。

