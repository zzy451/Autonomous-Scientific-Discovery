# Batch 3 多模块重分类审计汇总报告

> Transitional note 2026-06-20：本文件保留为早期多模块审计记录。当前重新开审时，以 `multi_module_reclassification_relaxed_round_plan_451_confirmed_2026-06-20.md` 为优先口径；不能用“主对象 / 核心贡献 / 只是 demo”排除模块，必须逐项检查具体科学对象实验、验证、benchmark task、case study 或结果报告。

> 日期：2026-06-20  
> 范围：`agent_master_paper_list.md` confirmed 记录序号 227-339。  
> 对应计划：`Coverage_Check/multi_module_reclassification_flat_batch_plan_451_confirmed_2026-06-20.md`。  
> 覆盖报告：`multi_module_reclassification_batch3_waveA_2026-06-20.md` 与 `multi_module_reclassification_batch3_waveB_2026-06-20.md`。  
> 当前阶段：Batch 3 已完成 Reviewer 审核与主控合并；本批不修改主列表。

## 一、批次基线

Batch 3 开始前主列表状态：

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

## 二、完成情况

| Wave | Reviewed records | Reviewer-covered records | 主控状态 |
|---|---:|---:|---|
| Wave A | 57 | 57 | 已完成 |
| Wave B | 56 | 56 | 已完成 |
| Batch 3 total | 113 | 113 | 已完成 |

本批 113 条均已由只读 Reviewer 覆盖，并由主控按统一口径合并。Reviewer 均未编辑 `agent_master_paper_list.md`。

## 三、本批已落地主列表改动

本批无已落地主列表改动。

| Change type | Count |
|---|---:|
| add_module | 0 |
| move_primary | 0 |
| move_to_01.04 | 0 |
| demote/background-review candidate | 0 |

原因：本批 Reviewer 提出的潜在问题主要属于全文证据补强、Agent-strength 复核、平台 demo 权重或边界解释，不满足“高置信、规则一致、不依赖缺失全文、不会造成 schema 半迁移”的直接改表条件。

## 四、批次统计

| Metric | Count |
|---|---:|
| reviewed records | 113 |
| unchanged by 主控 | 113 |
| add_module | 0 |
| move_primary | 0 |
| move_to_01.04 | 0 |
| demote/background-review candidate | 0 |
| main-control / full-text follow-up queue | 42 |
| records with `full_text_required=yes` from Reviewer output | 43 |

本批不修改 `agent_master_paper_list.md`。批次后主列表 record-level confirmed count 仍为 `451`，`needs_review` 仍为 `0`，confirmed `08` 仍为 `3`。

## 五、Batch 3 主要口径校准

1. 本批未发现高置信 multi-module assignment。跨平台、跨工具、跨 benchmark、跨案例或应用场景不等于跨一级科学对象模块。
2. `03 / 04` 边界继续稳定：reaction、organic synthesis、transition-state search、catalytic mechanism 归 `03`；MOF、nanoparticle、电解质、polymer、perovskite、superconductor、solid-state、phase diagram、materials characterization 归 `04`。
3. `05 / 10` 边界在 Batch 3 中高频出现且基本稳定：climate、atmospheric、geospatial、Earth observation analysis 归 `05`；Mars rover、Europa spacecraft、EO-1、sensorweb、spacecraft mission-science operations 归 `10`。
4. `11.07 / 01.04` 边界继续按对象判定。peer review、paper revision、reproducibility、citation attribution、research community simulation、scientific publishing ecosystem 属 scientific knowledge production itself，归 `11.07`；general full-lifecycle research-agent system 仍进独立 `01.04`。
5. `06 / 07` 边界继续按 biological mechanism / protein / omics vs disease / therapeutic / clinical endpoint 判定。gene expression、cell annotation、protein discovery、virtual cell model 保持 `06`；drug discovery、therapeutic reasoning、CAR-T therapy 保持 `07`。
6. `08` 仍不为平衡数量而放宽。`ASD-0634` 与 `ASD-0695` 进入或保持 `08` 是因为对象证据分别指向 plant / food science，而不是为了填补低覆盖类。
7. `01.04` 继续作为独立 general-method bucket 使用，不计入正式 `01` 对象模块。跨学科 demo 或 benchmark 只有在无具体对象实验证据时才支持 `01.04`，但对象贡献明确时不得因平台感退回 `01.04`。
8. 当前没有足够证据支持重构一级分类，问题主要集中在边界解释与低覆盖类稀缺性判断。

## 六、Batch 3 后续复核队列

Batch 3 暂列以下 42 条为后续全文或主控复核队列，均暂不改表。

| ID | 当前 legacy | 主要复核点 | 暂定处理 |
|---|---|---|---|
| `ASD-0609` | `03 / 03.03` | pH adjustment 的 second-level / evidence completeness | 暂保持 `03` |
| `ASD-0613` | `02 / 02.02` | nanoplasmonic physics vs materials characterization | 暂保持 `02` |
| `ASD-0614` | `04 / 04.01` | autonomy depth and workflow evidence | 暂保持 `04` |
| `ASD-0623` | `05 / 05.02` | withdrawn-status / core-strength | 暂保持 `05` |
| `ASD-0625` | `11 / 11.07` | ReviewBench / benchmark-heavy peer-review strength | 暂保持 `11.07` |
| `ASD-0626` | `11 / 11.07` | proactive review agent evidence depth | 暂保持 `11.07` |
| `ASD-0628` | `11 / 11.07` | ScholarPeer full-text evidence depth | 暂保持 `11.07` |
| `ASD-0631` | `04 / 04.04` | polymer electrolyte experiment/autonomy detail | 暂保持 `04` |
| `ASD-0634` | `08 / 08.01` | plant-science object evidence and low-coverage `08` pressure | 暂保持 `08` |
| `ASD-0636` | `11 / 11.07` | EGTR-Review evidence depth / duplicate pressure | 暂保持 `11.07` |
| `ASD-0648` | `10 / 10.02` | EO satellite autonomy 的 scientific core strength | 暂保持 `10` |
| `ASD-0651` | `05 / 05.02` | heatwave risk 的 `05 / 11 / 01.04` 边界 | 暂保持 `05` |
| `ASD-0656` | `11 / 11.07` | AAAI AI Review Pilot full-text evidence | 暂保持 `11.07` |
| `ASD-0659` | `01 / 01.04` | cross-domain demo 是否有对象层科学贡献 | 暂保持 `01.04` |
| `ASD-0663` | `01 / 01.04` | bio benchmark demo 是否足以转 `06` | 暂保持 `01.04` |
| `ASD-0664` | `03 / 03.03` | computational catalysis 的 `03 / 04 / 01.04` 边界 | 暂保持 `03` |
| `ASD-0667` | `04 / 04.04` | materials candidate novelty / evidence chain | 暂保持 `04` |
| `ASD-0671` | `01 / 01.04` | general research system core-strength | 暂保持 `01.04` |
| `ASD-0673` | `01 / 01.04` | AtomisticSkills cross-domain demo weight | 暂保持 `01.04` |
| `ASD-0676` | `01 / 01.04` | AutoSci 是否有足够具体对象实验，或只是 general research-agent system | 暂保持 `01.04` |
| `ASD-0682` | `04 / 04.01` | El Agente Sólido 的平台性与 solid-state 对象贡献强弱 | 暂保持 `04` |
| `ASD-0695` | `08 / 08.05` | flavor scientist 的食品科学对象证据与低覆盖 `08` 压力 | 暂保持 `08` |
| `ASD-0698` | `11 / 11.07` | APRES 是否属于 scientific knowledge production core 或偏工具化 | 暂保持 `11.07` |
| `ASD-0699` | `11 / 11.07` | reproducibility assessment / peer-review support 的 Agent 强度 | 暂保持 `11.07` |
| `ASD-0700` | `11 / 11.07` | peer-review mechanism design 的实证与 Agent role 强度 | 暂保持 `11.07` |
| `ASD-0701` | `11 / 11.07` | social-science reproducibility 与一般 social science 方法边界 | 暂保持 `11.07` |
| `ASD-0705` | `11 / 11.07` | LLM reproducibility assessment 是否满足 Agent 最低标准 | 暂保持 `11.07` |
| `ASD-0706` | `11 / 11.07` | aiXiv ecosystem 是否更像 knowledge-production system 或 general ASD platform | 暂保持 `11.07` |
| `ASD-0707` | `02 / 02.02` | ArgoLOOM framework-heavy physics object evidence | 暂保持 `02` |
| `ASD-0714` | `06 / 06.03` | K-Dense Analyst 的 biological object evidence 与 general analysis workflow 边界 | 暂保持 `06` |
| `ASD-0715` | `07 / 07.04` | BioDisco 的 therapeutic / biomedical endpoint 与生命科学机制边界 | 暂保持 `07` |
| `ASD-0717` | `11 / 11.07` | Paper Circle 是否是 scientific knowledge production object 或 general research framework | 暂保持 `11.07` |
| `ASD-0722` | `10 / 10.02` | Earth-observing sensorweb 的 `05 / 10` 归属与 scientific object weight | 暂保持 `10` |
| `ASD-0725` | `05 / 05.02` | atmospheric environmental research 的具体对象实验与平台强度 | 暂保持 `05` |
| `ASD-0726` | `05 / 05.02` | Climate Data Science Agentic AI 的对象贡献强度 | 暂保持 `05` |
| `ASD-0727` | `05 / 05.04` | GeoAgentic-RAG 的 geospatial reasoning 是否足够对象层 | 暂保持 `05` |
| `ASD-0728` | `06 / 06.01` | virtual cell model 的生命科学对象贡献与 framework-heavy 风险 | 暂保持 `06` |
| `ASD-0729` | `06 / 06.03` | protein discovery / directed evolution 的实验或结果证据 | 暂保持 `06` |
| `ASD-0731` | `06 / 06.03` | biomedical knowledge extraction 的 `06 / 07 / 11.07` 边界 | 暂保持 `06` |
| `ASD-0736` | `01 / 01.04` | AI-Researcher 是否有具体对象实验，或仅 general scientific innovation | 暂保持 `01.04` |
| `ASD-0737` | `01 / 01.04` | ScientistOne 的 evidence verification 是否转 `11.07` 或保持 general ASD | 暂保持 `01.04` |
| `ASD-0738` | `01 / 01.02` | AutoSOTA 的 AI model discovery 是否仍稳定为 formal/computational object | 暂保持 `01.02` |

## 七、批次后状态

Batch 3 结束后，主列表未发生行级修改：

- confirmed record-level count: 451
- `needs_review`: 0
- confirmed `08`: 3
- legacy confirmed `01.04`: 46
- legacy confirmed 主类分布仍保持本报告第一节所列基线

由于本轮仍未进行 row-level schema migration，`scientific_object_modules` 的正式 assignment count 暂不写入主列表；后续应在 451 条全部复核完成后，统一从审计报告与迁移字段生成模块 assignment count。
