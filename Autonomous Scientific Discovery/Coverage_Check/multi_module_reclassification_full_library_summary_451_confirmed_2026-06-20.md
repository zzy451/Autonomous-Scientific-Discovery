> Historical note 2026-06-20: 本文件对应第一轮 flat plan 的保守 / 过渡性汇总，仅可作为历史基线。本轮 451 篇 confirmed 文献的多模块分类以 `multi_module_reclassification_relaxed_round_plan_451_confirmed_2026-06-20.md` 为准；不得用本文中的 legacy single-primary、primary object 或 core-contribution 判断覆盖当前“可识别具体科学对象实验 / 验证 / benchmark task / case study / reported result 即可入对应模块”的规则。

# 451 篇 confirmed 文献多模块重分类全库审计汇总

> 日期：2026-06-20  
> 范围：`Paper_Lists/agent_master_paper_list.md` 中当前 `to_read` / `included` 且已有 legacy filing code 的 451 篇 confirmed 文献。  
> 对应计划：`Coverage_Check/multi_module_reclassification_flat_batch_plan_451_confirmed_2026-06-20.md`。  
> 审计模式：4 个平铺批次，每批拆为 2 个 wave，每个 wave 4 个只读 Reviewer；主控统一合并。  
> 当前结论：451 / 451 条已完成第一轮平铺复核；本轮未修改主列表。

## 一、当前权威基线

本总结以当前 `agent_master_paper_list.md` 头部为准：

- master list total records: 871
- `candidate`: 0
- `to_read`: 451
- `background_only`: 370
- `excluded`: 50
- `needs_review`: 0
- confirmed included-and-classified count: 451
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

说明：上述仍是 legacy filing distribution，不等于未来 row-level schema migration 后的 `scientific_object_modules` assignment count。当前主列表已在头部说明 `01.04` 是独立 general-method bucket，不再作为正式 `01` 对象模块的一部分。

## 二、全库执行覆盖

| Batch | Confirmed 序号 | Reviewed records | Reviewer-covered records | 主控状态 |
|---|---:|---:|---:|---|
| Batch 1 | 1-113 | 113 | 113 | 已完成 |
| Batch 2 | 114-226 | 113 | 113 | 已完成 |
| Batch 3 | 227-339 | 113 | 113 | 已完成 |
| Batch 4 | 340-451 | 112 | 112 | 已完成 |
| Total | 1-451 | 451 | 451 | 已完成 |

所有子 Agent 均为只读 Reviewer；主控负责合并、裁决和写报告。子 Agent 未编辑 `agent_master_paper_list.md`。

## 三、落地主列表改动

本轮未修改 `agent_master_paper_list.md`。

| Change type | Count |
|---|---:|
| add_module | 0 |
| move_primary | 0 |
| move_to_01.04 | 0 |
| demote/background-review candidate | 0 |

不改表的原因：

- 当前主列表仍使用 legacy filing fields，row-level schema migration 尚未完成。
- 本轮重点是按新口径完成全量复核和口径校准，而不是在 legacy columns 中做半迁移。
- Reviewer 提出的潜在改动大多依赖全文补强、二级位点复核、demo 权重判断、Agent-strength 判断或 Note / master trace 冲突整理。
- 未发现足够强、足够一致、且不依赖 schema 迁移的即时改表项。

## 四、全库统计

| Metric | Count |
|---|---:|
| reviewed records | 451 |
| Reviewer-covered records | 451 |
| unchanged by 主控 | 451 |
| add_module | 0 |
| move_primary | 0 |
| move_to_01.04 | 0 |
| demote/background-review candidate | 0 |
| main-control / full-text follow-up queue | 132 |
| records with `full_text_required=yes` from Reviewer output | 139 |

批次级来源：

| Batch | Reviewed | Follow-up queue | Reviewer `full_text_required=yes` |
|---|---:|---:|---:|
| Batch 1 | 113 | 21 | 31 |
| Batch 2 | 113 | 36 | 33 |
| Batch 3 | 113 | 42 | 43 |
| Batch 4 | 112 | 33 | 32 |

当前 confirmed-core count 相对早前 `500` milestone 的差值仍为 `-49`。本轮没有新增、删除或降级 confirmed 记录，因此这一差值没有变化。

## 五、主要校准结论

1. 新口径可执行：451 条平铺复核中，Reviewer 与主控能够稳定按“实际研究和实验覆盖的科学对象”判定，而不是按 Agent 技术、平台名称、venue 或自称通用性判定。
2. `01.04` 应继续作为独立 general-method bucket，而不是正式科学对象主类。它适合存放没有具体对象实验的 general ASD / research-agent workflow / general benchmark / equation-discovery framework / scientific-agent platform。
3. 平台感强不等于 `01.04`。只要实验、验证或科学贡献明确面向物理、化学、材料、生命、医学、地球环境、工程、航天或科学知识生产对象，就应保留对应对象模块。
4. 跨领域 demo 不因论文自称通用而自动 multi-module。Science Earth、SciDER、AutoDiscovery、SR-Scientist 等样本显示，跨领域 benchmark 或 demo 需要逐项检查；若 demo、benchmark task、case study 或结果报告可明确对应具体科学对象，应按新口径记录对应模块，而不要求该模块构成论文核心科学贡献。
5. `11.07` 的边界稳定：peer review、paper writing、reproducibility、scientific evaluation、ontology curation、scientific ecosystem 等 scientific knowledge production itself 归 `11.07`；一般 research-agent workflow 不因此转 `11.07`。
6. `05 / 10` 边界被多轮验证：rover / spacecraft mission-science operations 归 `10`；EO-1 或遥感平台用于火山、冰冻圈、洪水、气候、地理空间对象时归 `05`。
7. `03 / 04` 和 `03 / 07` 仍是高压边界。分子、反应、合成、吸附构型通常归 `03`；材料结构、性能、器件材料、催化材料候选通常归 `04`；therapeutic target、drug response、clinical / translational endpoint 通常归 `07`。
8. `06 / 07` 边界整体可复现：gene/protein/cell/omics/virtual-cell 归 `06`；disease、diagnosis、therapy、clinical biomarker、drug safety 归 `07`。
9. `08` 不应为平衡数量而放宽。当前 confirmed `08` 仍为 3；低覆盖反映样本稀缺和纳入口径严格，而不是需要人为扩展边界。
10. 当前没有足够证据支持重构一级分类，问题主要集中在边界解释与低覆盖类稀缺性判断。

## 六、对分类体系的影响

本轮审计支持继续采用当前体系：

- 正式对象模块仍为封闭 `01-11`。
- `01.04` 继续作为独立 general-method bucket，不计入正式 `01` 对象模块统计。
- 同一篇文献可多模块，但必须由多个具体科学对象的可识别实验、验证、benchmark task、case study 或结果报告支持；不要求每个模块构成核心科学贡献。
- legacy `Main class / Secondary class` 只能暂作 filing display，不应再被解释为唯一分类事实。
- 未来正式统计应区分 record-level confirmed count 与 module assignment count；前者当前仍为 451，后者需等 schema migration 后统一计算，且可以超过 451。

## 七、下一步产物

本轮同时生成独立二轮队列：

- `Coverage_Check/multi_module_reclassification_round2_high_risk_queue_2026-06-20.md`

该队列不要求立即改表，而是作为下一轮全文补强、Note 修订、schema migration 前的重点核验清单。
