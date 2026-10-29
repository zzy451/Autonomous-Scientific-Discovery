# Vibe-FDTR: An agent-oriented framework for reproducible frequency-domain thermoreflectance data analysis

**论文信息**

- ID：ASD-0993
- 标题：Vibe-FDTR: An agent-oriented framework for reproducible frequency-domain thermoreflectance data analysis
- 作者：Fuwei Yang; Weiheng Li; Bai Song
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2607.28200
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0993.txt
- PDF / 本地文件路径：Reference_PDF/04_Materials_Science/Yang_2026_Vibe_FDTR_An_agent_oriented_framework_for_reproducible_frequency_ASD0993.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 纳入与科学目标 | Vibe-FDTR面向频域热反射（FDTR）热物性分析，将配置驱动且约束物理/参数一致性的代码包与Agent技能结合，让LLM把自然语言需求转成可核验步骤。评估同时包含合成单步任务和基于金镀层石墨实测数据的多步任务；可选专家模式还能进行敏感性与不确定性分析并给实验规划建议。 | 摘要；TXT第258行；核验TXT行号 258 | Frequency-domain thermoreflectance (FDTR) is a laser pump-probe technique widely used to measure thermal properties at the micro- and nanoscale; however, it relies on a complex data analysis procedure that demands substantial domain expertise and is susceptible to subtle human errors. | 高（一手正文；非独立复现） |
| 方法与多步工作流 | 用户以自然语言描述FDTR分析需求；Agent技能解析目标并调用配置驱动分析包，按步骤准备参数、拟合数据、检查输出和报告结果。专家模式会运行敏感性/不确定性评估，为条件不充分的任务给出有物理依据的建议。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。 | 摘要；TXT第258行；核验TXT行号 258 | Here, we present Vibe-FDTR, an agent-oriented framework that enables large language model (LLM) agents to perform reliable and reproducible FDTR analyses directly from natural language requests. | 高（一手正文；非独立复现） |
| Agent能力与行动 | Vibe-FDTR: An agent-oriented framework for reproducible frequency-domain thermoreflectance data analysis。系统角色与能力：用户以自然语言描述FDTR分析需求；Agent技能解析目标并调用配置驱动分析包，按步骤准备参数、拟合数据、检查输出和报告结果。专家模式会运行敏感性/不确定性评估，为条件不充分的任务给出有物理依据的建议。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。 | 摘要；TXT第258行；核验TXT行号 258 | This framework couples a configuration-driven FDTR code package, which enforces physical and parametric consistency, with procedural agent skills that translate user intentions into organized and verifiable analysis steps. | 高（一手正文；非独立复现） |
| 验证与结果 | 合成单步和真实数据多步任务成功率分别为100%和98.9%；移除技能后降至91.4%和36.7%，同时移除领域代码包则降至38.6%和0%。Vibe-FDTR相对Code-agent降低87.7%计算成本、执行时间减少超过60%。 | 摘要；TXT第258行；核验TXT行号 258 | We evaluate Vibe-FDTR using a controlled benchmark with two levels: synthetic single-step tasks and real-data multi-step tasks based on measurements of gold-coated graphite samples. | 高（一手正文；非独立复现） |
| 贡献及适用对象 | 支持综述关于技能化知识封装提升科学分析复现性、降低成本的论点。 科学贡献与系统贡献按上述证据分别表述。 | 摘要；TXT第258行；核验TXT行号 258 | Finally, an optional expert mode supports experimental planning via autonomous sensitivity and uncertainty evaluations, and formulates physically grounded recommendations for underspecified tasks. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

Vibe-FDTR面向频域热反射（FDTR）热物性分析，将配置驱动且约束物理/参数一致性的代码包与Agent技能结合，让LLM把自然语言需求转成可核验步骤。评估同时包含合成单步任务和基于金镀层石墨实测数据的多步任务；可选专家模式还能进行敏感性与不确定性分析并给实验规划建议。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。Vibe-FDTR面向频域热反射（FDTR）热物性分析，将配置驱动且约束物理/参数一致性的代码包与Agent技能结合，让LLM把自然语言需求转成可核验步骤。评估同时包含合成单步任务和基于金镀层石墨实测数据的多步任务；可选专家模式还能进行敏感性与不确定性分析并给实验规划建议。
  - 原文位置：摘要；TXT第258行；核验TXT行号 258；引文：Frequency-domain thermoreflectance (FDTR) is a laser pump-probe technique widely used to measure thermal properties at the micro- and nanoscale; however, it relies on a complex data analysis procedure that demands substantial domain expertise and is susceptible to subtle human errors.
- 多步行动过程：yes。用户以自然语言描述FDTR分析需求；Agent技能解析目标并调用配置驱动分析包，按步骤准备参数、拟合数据、检查输出和报告结果。专家模式会运行敏感性/不确定性评估，为条件不充分的任务给出有物理依据的建议。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。
  - 原文位置：摘要；TXT第258行；核验TXT行号 258；引文：Here, we present Vibe-FDTR, an agent-oriented framework that enables large language model (LLM) agents to perform reliable and reproducible FDTR analyses directly from natural language requests.
- 至少一种Agent能力：yes。Vibe-FDTR: An agent-oriented framework for reproducible frequency-domain thermoreflectance data analysis。系统角色与能力：用户以自然语言描述FDTR分析需求；Agent技能解析目标并调用配置驱动分析包，按步骤准备参数、拟合数据、检查输出和报告结果。专家模式会运行敏感性/不确定性评估，为条件不充分的任务给出有物理依据的建议。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。
  - 原文位置：摘要；TXT第258行；核验TXT行号 258；引文：This framework couples a configuration-driven FDTR code package, which enforces physical and parametric consistency, with procedural agent skills that translate user intentions into organized and verifiable analysis steps.
- 明确科研流程角色：yes。合成单步和真实数据多步任务成功率分别为100%和98.9%；移除技能后降至91.4%和36.7%，同时移除领域代码包则降至38.6%和0%。Vibe-FDTR相对Code-agent降低87.7%计算成本、执行时间减少超过60%。
  - 原文位置：摘要；TXT第258行；核验TXT行号 258；引文：We evaluate Vibe-FDTR using a controlled benchmark with two levels: synthetic single-step tasks and real-data multi-step tasks based on measurements of gold-coated graphite samples.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：04
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：04（仅归档，不覆盖其他模块）
- 模块内分类路径：04.01 材料基础
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

对象是热物性测量数据分析，归04.01科学数据分析。技能与领域代码包对结果影响大，Agent单独生成代码不是其可靠性来源。

### 2.3 容易混淆的边界

对象是热物性测量数据分析，归04.01科学数据分析。技能与领域代码包对结果影响大，Agent单独生成代码不是其可靠性来源。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM科研Agent

### 3.2 科研流程角色

计算/数据分析

Vibe-FDTR: An agent-oriented framework for reproducible frequency-domain thermoreflectance data analysis。系统角色与能力：用户以自然语言描述FDTR分析需求；Agent技能解析目标并调用配置驱动分析包，按步骤准备参数、拟合数据、检查输出和报告结果。专家模式会运行敏感性/不确定性评估，为条件不充分的任务给出有物理依据的建议。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 3.3 自主能力

Vibe-FDTR: An agent-oriented framework for reproducible frequency-domain thermoreflectance data analysis。系统角色与能力：用户以自然语言描述FDTR分析需求；Agent技能解析目标并调用配置驱动分析包，按步骤准备参数、拟合数据、检查输出和报告结果。专家模式会运行敏感性/不确定性评估，为条件不充分的任务给出有物理依据的建议。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

支持综述关于技能化知识封装提升科学分析复现性、降低成本的论点。 科学贡献与系统贡献按上述证据分别表述。

### 4.2 系统流程与组件

用户以自然语言描述FDTR分析需求；Agent技能解析目标并调用配置驱动分析包，按步骤准备参数、拟合数据、检查输出和报告结果。专家模式会运行敏感性/不确定性评估，为条件不充分的任务给出有物理依据的建议。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

合成单步和真实数据多步任务成功率分别为100%和98.9%；移除技能后降至91.4%和36.7%，同时移除领域代码包则降至38.6%和0%。Vibe-FDTR相对Code-agent降低87.7%计算成本、执行时间减少超过60%。

### 5.2 基线、指标与结果

合成单步和真实数据多步任务成功率分别为100%和98.9%；移除技能后降至91.4%和36.7%，同时移除领域代码包则降至38.6%和0%。Vibe-FDTR相对Code-agent降低87.7%计算成本、执行时间减少超过60%。

### 5.3 科学贡献与证据强度

支持综述关于技能化知识封装提升科学分析复现性、降低成本的论点。 科学贡献与系统贡献按上述证据分别表述。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

作者比较仅靠代码Agent或通用Agent的分析方式，提出把物理一致性FDTR代码包与程序化技能共同提供给LLM。

## 7. 局限性与风险

作者及读者可确认的适用边界：基准由合成单步任务和金镀层石墨实测多步任务构成；FDTR是特定热物性反演问题，结果不能直接推广到其他测量模态。

## 8. 对综述写作的价值

支持综述关于技能化知识封装提升科学分析复现性、降低成本的论点。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

Vibe-FDTR面向频域热反射（FDTR）热物性分析，将配置驱动且约束物理/参数一致性的代码包与Agent技能结合，让LLM把自然语言需求转成可核验步骤。

### 9.2 速记版 pipeline

用户以自然语言描述FDTR分析需求；Agent技能解析目标并调用配置驱动分析包，按步骤准备参数、拟合数据、检查输出和报告结果。专家模式会运行敏感性/不确定性评估，为条件不充分的任务给出有物理依据的建议。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 9.3 标注字段汇总

```text
paper_id=ASD-0993
inclusion_status=to_read
scientific_object_modules=04
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=04
module_taxonomy_codes=04.01
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`04.01.03` 材料表征；二级：`04.01`。
- 原文位置：PDF p.2。
- 判定：FDTR测量材料热学性质，归材料表征。
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
