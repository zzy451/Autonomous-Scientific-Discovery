# Large-language-model-driven adaptive search space definition for autonomous closed-loop materials exploration

**论文信息**

- ID：ASD-0982
- 标题：Large-language-model-driven adaptive search space definition for autonomous closed-loop materials exploration
- 作者：Yuma Iwasaki; Ryo Toyama; Ryo Tamura; Shoichi Matsuda; Yuya Sakuraba; Masato Kotsugi; Yasuhiko Igarashi; Keitaro Sodeyama
- 年份：2026
- 来源 / venue：Communications Materials
- DOI / arXiv / URL：https://www.nature.com/articles/s43246-026-01304-9
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0982.txt
- PDF / 本地文件路径：Reference_PDF/04_Materials_Science/Iwasaki_2026_Large_language_model_driven_adaptive_search_space_definition_for_ASD0982.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 纳入与科学目标 | 论文提出面向自主闭环材料探索的自适应搜索空间框架：外层LLM根据已有进展提议更新材料搜索空间，内层贝叶斯优化在当前空间挑选候选。目标是减少专家手动指定和周期性重设搜索空间的负担，并扩展连续探索范围。作者报告对LLM先验知识较充分的目标性质，搜索空间更新带来更明显收益。 | 摘要；TXT第1行；核验TXT行号 1 | Autonomous closed-loop materials exploration systems that couple machine learning with robotic experimentation, often called self-driving laboratories, are increasingly used to accelerate materials discovery. | 高（一手正文；非独立复现） |
| 方法与多步工作流 | 材料目标和迭代实验/模型反馈进入外层LLM，由其提出新的搜索边界或候选域；内层贝叶斯优化在更新后的空间选点，实验平台或材料模型返回测量结果，再反馈到下一轮空间更新。输出是经多轮探索调整的搜索范围及候选实验。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。 | 摘要；TXT第1行；核验TXT行号 1 | Herein, we propose a data-driven framework that adaptively redefines the materials search space during operation for continuous exploration. | 高（一手正文；非独立复现） |
| Agent能力与行动 | Large-language-model-driven adaptive search space definition for autonomous closed-loop materials exploration。系统角色与能力：材料目标和迭代实验/模型反馈进入外层LLM，由其提出新的搜索边界或候选域；内层贝叶斯优化在更新后的空间选点，实验平台或材料模型返回测量结果，再反馈到下一轮空间更新。输出是经多轮探索调整的搜索范围及候选实验。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。 | 摘要；TXT第1行；核验TXT行号 1 | It comprises a large language model (LLM)-driven outer loop that proposes updated search spaces and an inner Bayesian optimization loop that selects candidate materials within each space. | 高（一手正文；非独立复现） |
| 验证与结果 | 对比固定或既有搜索空间策略，观察扩展空间下的探索效率，并分析目标性质与LLM先验知识的关系。需从正文结果段提取具体数据、实验平台和基线，摘要本身只支持趋势性结论。 | 摘要；TXT第1行；核验TXT行号 1 | This hierarchical scheme enables efficient exploration across substantially expanded search spaces. Target properties for which the LLM possesses extensive prior knowledge exhibit the most pronounced performance gains, suggesting that foundation models can leverage learned domain knowledge to generate informative search space updates. | 高（一手正文；非独立复现） |
| 贡献及适用对象 | 支持讨论LLM先验知识如何在自驱实验室中改进高层规划，同时指出其效果依赖目标领域知识。 科学贡献与系统贡献按上述证据分别表述。 | 摘要；TXT第1行；核验TXT行号 1 | However, their end-to-end autonomy is limited by the need for human experts to specify and periodically reconfigure the search space. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

论文提出面向自主闭环材料探索的自适应搜索空间框架：外层LLM根据已有进展提议更新材料搜索空间，内层贝叶斯优化在当前空间挑选候选。目标是减少专家手动指定和周期性重设搜索空间的负担，并扩展连续探索范围。作者报告对LLM先验知识较充分的目标性质，搜索空间更新带来更明显收益。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。论文提出面向自主闭环材料探索的自适应搜索空间框架：外层LLM根据已有进展提议更新材料搜索空间，内层贝叶斯优化在当前空间挑选候选。目标是减少专家手动指定和周期性重设搜索空间的负担，并扩展连续探索范围。作者报告对LLM先验知识较充分的目标性质，搜索空间更新带来更明显收益。
  - 原文位置：摘要；TXT第1行；核验TXT行号 1；引文：Autonomous closed-loop materials exploration systems that couple machine learning with robotic experimentation, often called self-driving laboratories, are increasingly used to accelerate materials discovery.
- 多步行动过程：yes。材料目标和迭代实验/模型反馈进入外层LLM，由其提出新的搜索边界或候选域；内层贝叶斯优化在更新后的空间选点，实验平台或材料模型返回测量结果，再反馈到下一轮空间更新。输出是经多轮探索调整的搜索范围及候选实验。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。
  - 原文位置：摘要；TXT第1行；核验TXT行号 1；引文：Herein, we propose a data-driven framework that adaptively redefines the materials search space during operation for continuous exploration.
- 至少一种Agent能力：yes。Large-language-model-driven adaptive search space definition for autonomous closed-loop materials exploration。系统角色与能力：材料目标和迭代实验/模型反馈进入外层LLM，由其提出新的搜索边界或候选域；内层贝叶斯优化在更新后的空间选点，实验平台或材料模型返回测量结果，再反馈到下一轮空间更新。输出是经多轮探索调整的搜索范围及候选实验。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。
  - 原文位置：摘要；TXT第1行；核验TXT行号 1；引文：It comprises a large language model (LLM)-driven outer loop that proposes updated search spaces and an inner Bayesian optimization loop that selects candidate materials within each space.
- 明确科研流程角色：yes。对比固定或既有搜索空间策略，观察扩展空间下的探索效率，并分析目标性质与LLM先验知识的关系。需从正文结果段提取具体数据、实验平台和基线，摘要本身只支持趋势性结论。
  - 原文位置：摘要；TXT第1行；核验TXT行号 1；引文：This hierarchical scheme enables efficient exploration across substantially expanded search spaces. Target properties for which the LLM possesses extensive prior knowledge exhibit the most pronounced performance gains, suggesting that foundation models can leverage learned domain knowledge to generate informative search space updates.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：04
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：04（仅归档，不覆盖其他模块）
- 模块内分类路径：04.02 结构材料与无机材料
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

对象是闭环材料探索中的实验搜索空间及候选材料，归入04.02。LLM负责高层搜索域定义，内层贝叶斯优化负责选点，分类时应区分Agent策略与优化算法本身。

### 2.3 容易混淆的边界

对象是闭环材料探索中的实验搜索空间及候选材料，归入04.02。LLM负责高层搜索域定义，内层贝叶斯优化负责选点，分类时应区分Agent策略与优化算法本身。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM科研Agent

### 3.2 科研流程角色

实验设计与执行

Large-language-model-driven adaptive search space definition for autonomous closed-loop materials exploration。系统角色与能力：材料目标和迭代实验/模型反馈进入外层LLM，由其提出新的搜索边界或候选域；内层贝叶斯优化在更新后的空间选点，实验平台或材料模型返回测量结果，再反馈到下一轮空间更新。输出是经多轮探索调整的搜索范围及候选实验。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 3.3 自主能力

Large-language-model-driven adaptive search space definition for autonomous closed-loop materials exploration。系统角色与能力：材料目标和迭代实验/模型反馈进入外层LLM，由其提出新的搜索边界或候选域；内层贝叶斯优化在更新后的空间选点，实验平台或材料模型返回测量结果，再反馈到下一轮空间更新。输出是经多轮探索调整的搜索范围及候选实验。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

支持讨论LLM先验知识如何在自驱实验室中改进高层规划，同时指出其效果依赖目标领域知识。 科学贡献与系统贡献按上述证据分别表述。

### 4.2 系统流程与组件

材料目标和迭代实验/模型反馈进入外层LLM，由其提出新的搜索边界或候选域；内层贝叶斯优化在更新后的空间选点，实验平台或材料模型返回测量结果，再反馈到下一轮空间更新。输出是经多轮探索调整的搜索范围及候选实验。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

对比固定或既有搜索空间策略，观察扩展空间下的探索效率，并分析目标性质与LLM先验知识的关系。需从正文结果段提取具体数据、实验平台和基线，摘要本身只支持趋势性结论。

### 5.2 基线、指标与结果

对比固定或既有搜索空间策略，观察扩展空间下的探索效率，并分析目标性质与LLM先验知识的关系。需从正文结果段提取具体数据、实验平台和基线，摘要本身只支持趋势性结论。

### 5.3 科学贡献与证据强度

支持讨论LLM先验知识如何在自驱实验室中改进高层规划，同时指出其效果依赖目标领域知识。 科学贡献与系统贡献按上述证据分别表述。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

本文与自驱实验室中的贝叶斯优化及预设搜索空间工作相关，进一步把LLM放在外层重新定义空间、BO放在内层选点。

## 7. 局限性与风险

作者及读者可确认的适用边界：搜索空间更新效果依赖目标性质及LLM已有先验知识；实验/材料平台和性质范围有限，不能据此推断对任意材料目标都同样有效。

## 8. 对综述写作的价值

支持讨论LLM先验知识如何在自驱实验室中改进高层规划，同时指出其效果依赖目标领域知识。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

论文提出面向自主闭环材料探索的自适应搜索空间框架：外层LLM根据已有进展提议更新材料搜索空间，内层贝叶斯优化在当前空间挑选候选。

### 9.2 速记版 pipeline

材料目标和迭代实验/模型反馈进入外层LLM，由其提出新的搜索边界或候选域；内层贝叶斯优化在更新后的空间选点，实验平台或材料模型返回测量结果，再反馈到下一轮空间更新。输出是经多轮探索调整的搜索范围及候选实验。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 9.3 标注字段汇总

```text
paper_id=ASD-0982
inclusion_status=to_read
scientific_object_modules=04
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=04
module_taxonomy_codes=04.02
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`04.02.02` 合金材料；二级：`04.02`。
- 原文位置：PDF p.2。
- 判定：16908个B2结构三元合金的磁性组成优化，比泛晶体标签精确。
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
