# Jiang and Karniadakis 2026 - AgenticSciML: collaborative multi-agent systems for emergent discovery in scientific machine learning

**论文信息**
- 标题：AgenticSciML: collaborative multi-agent systems for emergent discovery in scientific machine learning
- 作者：Jiang and Karniadakis
- 年份：2026
- 来源 / venue：npj Artificial Intelligence
- DOI / arXiv / URL：https://doi.org/10.1038/s44387-026-00102-5
- PDF / 本地文件路径：本轮未归档本地 PDF；已核对 npj Artificial Intelligence DOI 页面 abstract
- 论文类型：系统论文 / Agent 论文
- 当前状态：已读（本轮核对一手来源）；主列表流程状态仍可保持 `to_read`
- 阅读日期：2026-06-23
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | npj Artificial Intelligence DOI `10.1038/s44387-026-00102-5` abstract | 10+ specialized agents 协作提出、批评和改进 SciML 方案，满足多步 Agent 科研流程 | 高 |
| 科学对象归类 | `01` | npj Artificial Intelligence DOI `10.1038/s44387-026-00102-5` abstract | 论文直接针对 SciML architecture、loss、training strategy discovery，并在 physics-informed learning 与 operator learning tasks 上验证 | 高 |
| 方法流程 | 多 Agent 协作式 SciML 发现流程 | npj Artificial Intelligence DOI `10.1038/s44387-026-00102-5` abstract | specialized agents propose, critique, refine solutions，而非单次问答或纯平台展示 | 高 |
| 实验验证 | physics-informed learning + operator learning tasks | npj Artificial Intelligence DOI `10.1038/s44387-026-00102-5` abstract | 官方摘要明确给出 concrete SciML task coverage，并报告优于 human-designed / single-agent baselines | 高 |
| 边界判断 | `01`，不再维持 `01.04` authority | npj Artificial Intelligence DOI `10.1038/s44387-026-00102-5` abstract | 当前一手来源已经足以证明它不是“无具体对象实验的通用科研 Agent” | 高 |

## 0. 摘要翻译

论文提出 AgenticSciML，通过 10 多个专门化 agents 协作，为 scientific machine learning 任务发现更优的架构、损失函数和训练策略，并在 physics-informed learning 与 operator learning 任务上验证效果。按本轮复核，object-level evidence 已经足够把它稳定放在 `01`，不应再保留独立 `01.04` authority。

## 1. 是否纳入本综述

- 是否属于 Agent 文献：是
- 判断依据：面向明确科研目标，具有多步行动、反馈迭代和多 Agent 协作
- 判定置信度：高

## 2. 科学领域归类

- scientific_object_modules：`01`
- object_coverage_mode：`single_module`
- has_concrete_object_experiments：`yes`
- general_method_bucket：`none`
- primary_module_for_filing：`01`
- 归类理由：论文针对的稳定对象是 concrete scientific machine learning discovery task，本体属于形式 / 信息 / 计算科学
- 边界说明：虽然平台叙事较强，但已有 concrete SciML task evidence，因此不再维持 `01.04` authority
- 归类置信度：高

## 3. Agent 系统与科研流程角色

- Agent 类型：Multi-Agent System; Hybrid Agent
- 科研流程角色：hypothesis_generation; simulation_modeling; data_analysis; end_to_end_research_automation

## 4. 方法设计

系统用多名 specialized agents 对 SciML 方案进行提出、评议和 refinement，最终输出更优的 scientific machine learning solution。

## 5. 实验与验证

- 验证方式：benchmark
- 关键验证：physics-informed learning tasks；operator learning tasks
- 证据强度：`benchmark_only`

## 6. 与已有工作的关系

它和纯 `01.04` 通用科研 Agent 的关键区别在于：这里的验证对象已经不是泛化工作流能力，而是 concrete SciML object-level discovery task。

## 7. 局限性与风险

- 本轮未新增本地 PDF 归档
- 当前判断建立在 official abstract 上，但对模块归类已经足够，不构成继续维持 `01.04` authority 的理由

## 8. 对综述写作的价值

- 可放入章节：`01` 主章节
- 可支撑论点：平台外观并不自动等于 `01.04`；只要已有 concrete formal / computational object task，就应落到正式对象模块

## 9. 总结

### 9.1 一句话概括

面向 SciML 任务发现的多 Agent 协作系统。

### 9.2 标注字段汇总

```text
是否纳入：是
scientific_object_modules：01
object_coverage_mode：single_module
has_concrete_object_experiments：yes
general_method_bucket：none
primary_module_for_filing：01
first_hand_sources_checked：npj Artificial Intelligence DOI 10.1038/s44387-026-00102-5 abstract
local_pdf_archived_this_round：no
归类置信度：高
推荐引用强度：standard
```
