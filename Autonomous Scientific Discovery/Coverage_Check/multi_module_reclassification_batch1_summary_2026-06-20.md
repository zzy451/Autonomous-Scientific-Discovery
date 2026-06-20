# Batch 1 多模块重分类审计汇总

> Transitional note 2026-06-20：本文件保留为早期多模块审计记录。当前重新开审时，以 `multi_module_reclassification_relaxed_round_plan_451_confirmed_2026-06-20.md` 为优先口径；不能用“主对象 / 核心贡献 / 只是 demo”排除模块，必须逐项检查具体科学对象实验、验证、benchmark task、case study 或结果报告。

> 日期：2026-06-20  
> 范围：`agent_master_paper_list.md` confirmed 记录序号 1-113。  
> 对应批次：`Coverage_Check/multi_module_reclassification_flat_batch_plan_451_confirmed_2026-06-20.md` 的 Batch 1。  
> 子报告：`multi_module_reclassification_batch1_waveA_2026-06-20.md` 与 `multi_module_reclassification_batch1_waveB_2026-06-20.md`。  

## 一、批次基线

Batch 1 开始前主列表状态：

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

## 二、执行覆盖

| Wave | Reviewed records | Reviewer-covered records | 主控状态 |
|---|---:|---:|---|
| Wave A | 57 | 57 | 已合并 |
| Wave B | 56 | 56 | 已合并 |
| Batch 1 total | 113 | 113 | 已完成 |

本批所有分配记录均已由只读 Reviewer 覆盖，且均已完成主控裁决。子 Agent 均未编辑主列表。

## 三、主控落地结论

本批不修改 `agent_master_paper_list.md`。原因是：

- 未发现高置信、证据充分、且不依赖 schema 迁移的即时改表项。
- Reviewer 提出的潜在变更多为 medium confidence 或依赖全文证据。
- 当前主列表仍处于 legacy filing 字段过渡期；本轮目标优先是审计与口径稳定，不强行做半成品 schema 迁移。

| Metric | Count |
|---|---:|
| reviewed records | 113 |
| unchanged by主控 | 113 |
| add_module | 0 |
| move_primary | 0 |
| move_to_01.04 | 0 |
| demote/background-review candidate | 0 |
| main-control / full-text follow-up queue | 21 |
| records with `full_text_required=yes` from Reviewer output | 31 |

主列表 record-level confirmed count 仍为 `451`，`needs_review` 仍为 `0`，confirmed `08` 仍为 `3`。

## 四、边界校准

Batch 1 的关键校准结论如下：

1. 平台感强但对象实验证据明确时，不回收到 `01.04`。天文、宇宙学、量子实验、材料实验、结构工程、CFD、power electronics 等记录均按最终对象模块保留。
2. 没有具体科学对象实验、主要验证 general research-agent workflow / automated research platform / code experimentation / idea generation 的记录，保留独立 `01.04`。
3. 本批未发现高置信 multi-module assignment。`ASD-0096` 是最接近的样本，但主控暂不采纳新增 `07`，因为本地 full note 仍支持材料 inverse design 为主。
4. drug discovery / target-protein / therapeutic candidate 目标优先 `07`；分子优化、化学反应、量子化学和化学机器人通常保持 `03`。
5. omics、single-cell、gene editing、protein design 通常保持 `06`；precision medicine、disease framing 或 biomedical venue 不自动转 `07`。
6. scientific reproducibility / general research-agent benchmark 与 `11.07` 的边界需要后续统一校准，代表样本是 `ASD-0100`。
7. 当前没有足够证据支持重构一级分类，问题主要集中在边界解释与低覆盖类稀缺性判断。

## 五、Batch 1 后续复核队列

| ID | 当前 legacy | 边界问题 | 暂定处理 |
|---|---|---|---|
| `ASD-0006` | `06 / 06.03` | DORA AI Scientist 可能更像通用科研/reporting workflow | 暂不改表，后续全文复核 |
| `ASD-0034` | `06 / 06.03` | Perturb-seq 对象稳定，但系统细节和实验轮次需全文确认 | 暂保持 `06` |
| `ASD-0049` | `06 / 06.03` | BIA 证据目前来自 metadata/code，PDF/full text 不足 | 暂保持 `06` |
| `ASD-0055` | `06 / 06.03` | BioMaster 是 bioinformatics / omics workflow，全文证据待补 | 暂保持 `06` |
| `ASD-0056` | `03 / 03.04` | organic laser emitters 处于 `03 / 04` 边界 | 暂保持 `03` |
| `ASD-0060` | `01 / 01.04` | cross-domain benchmark 与 general-method tension | 暂保持 `01.04` |
| `ASD-0070` | `03 / 03.04` | MOOSE-Chem3 hypothesis set 是否覆盖多对象 | 暂保持 `03` |
| `ASD-0077` | `07 / 07.04` | STELLA 的 biomedical benchmark 与具体对象实验强度 | 暂保持 `07` |
| `ASD-0084` | `04 / 04.02` | alloy design 方向稳定，但证据仍偏 metadata-level | 暂保持 `04` |
| `ASD-0096` | `04 / 04.04` | dZiner 是否应追加 `07` | 暂不新增模块，保持 `04` |
| `ASD-0100` | `01 / 01.04` | scientific reproducibility benchmark 与 `11.07` 强规则冲突 | 暂保持 `01.04` |
| `ASD-0112` | `07 / 07.04` | drug molecule optimization 是否由 therapeutic objective 主导 | 暂保持 `07` |
| `ASD-0115` | `07 / 07.04` | general co-scientist framing 与 biomedical validation 主导之间的边界 | 暂保持 `07` |
| `ASD-0117` | `03 / 03.04` | OSDA molecule 与 zeolite/material performance 边界 | 暂保持 `03` |
| `ASD-0118` | `07 / 07.04` | Biomni 具体 biomedical object evidence 偏抽象 | 暂保持 `07` |
| `ASD-0127` | `02 / 02.01` | AI Cosmologist 的 cosmology object evidence 需全文确认 | 暂保持 `02` |
| `ASD-0134` | `03 / 03.01` | chemistry reasoning benchmark 的 confirmed-core strength 需补强 | 暂保持 `03` |
| `ASD-0139` | `01 / 01.04` | physics framing 是否包含 substantive physics-object result | 暂保持 `01.04` |
| `ASD-0140` | `11 / 11.07` | scientific hypothesis generation 是 knowledge-production object 还是 general benchmark | 暂保持 `11.07` |
| `ASD-0147` | `01 / 01.04` | idea-generation workflow 证据偏轻 | 暂保持 `01.04` |
| `ASD-0152` | `06 / 06.03` | scRNA-seq standardization 方向稳定，但 validation strength 需补强 | 暂保持 `06` |

## 六、下一步

下一步按计划进入 Batch 2 / Wave A，仍采用四个只读 Reviewer、每人约 14-15 篇的 micro-batch 设计。Batch 2 不按风险优先抽样，继续按 confirmed 记录出现顺序平铺推进。
