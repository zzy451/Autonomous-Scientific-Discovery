# From Search to Research: Exploring Search Scaling in Autonomous Quantitative Factor Mining

**论文信息**

- ID：ASD-1105
- 标题：From Search to Research: Exploring Search Scaling in Autonomous Quantitative Factor Mining
- 作者：Deng, Kangcheng; Cai, Hui; Lu, Jiacheng; Qian, Chester Zhongshu; Sun, Rui; Luan, Beidi; Li, Jing; Jiang, Daxin; Bai, Zuo
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2609.35559
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1105.txt
- PDF / 本地文件路径：Reference_PDF/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Kangcheng_2026_From_Search_to_Research_Exploring_Search_Scaling_in_Autonomous_ASD1105.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 研究对象与任务 | 本文研究自主量化因子挖掘中的搜索扩展：在50项源自金融研究报告的任务上，增加代理搜索预算，测量研究表现如何变化以及收益来自何种搜索机制。代理生成并筛选候选量化因子，执行计算评估，研究从搜索到可验证研究结果的扩展规律。 | 全文TXT第1002行；核验TXT行号 1002 | The consistent gain indicates that exploring several initial directions can be more valuable than repeatedly improving one locally chosen direction. Together, the two experiments show that the return to additional search depends on both the inherited research state and whether the budget broadens or deepens the search. | 高（一手正文；非独立复现） |
| 系统输入及处理流程 | 每项任务提供金融研究报告中的问题/线索；代理在预算限制下探索因子表达、实现并评估候选因子，随搜索预算增加记录发现质量和机制。 | 全文TXT第3544行；核验TXT行号 3544 | Table E.1: Task-level metrics for Claude Opus 5 at iterations 3, 6, and 10. | 高（一手正文；非独立复现） |
| 实验或验证设置 | 每项任务提供金融研究报告中的问题/线索；代理在预算限制下探索因子表达、实现并评估候选因子，随搜索预算增加记录发现质量和机制。 | 全文TXT第6205行；核验TXT行号 6205 | Table E.4: Task-level metrics for DeepSeek-V4-Pro at iterations 3, 6, and 10. | 高（一手正文；非独立复现） |
| 作者报告的贡献 | 在50项任务上比较不同搜索规模及相关基线，分析成功率/因子质量随预算变化；仅报告论文实测数字。 | 全文TXT第7979行；核验TXT行号 7979 | Table E.6: Task-level metrics for GLM-5.2 at iterations 3, 6, and 10. | 高（一手正文；非独立复现） |
| 适用范围与边界 | 研究对象是金融市场预测因子及其挖掘，具备明确量化研究任务。本文可作为金融/经济研究Agent纳入；candidate建议与特定科学发现边界仍需整体名单规则统一。 | 全文TXT第9753行；核验TXT行号 9753 | Table E.8: Task-level metrics for Qwen3.7-Plus at iterations 3, 6, and 10. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

本文研究自主量化因子挖掘中的搜索扩展：在50项源自金融研究报告的任务上，增加代理搜索预算，测量研究表现如何变化以及收益来自何种搜索机制。代理生成并筛选候选量化因子，执行计算评估，研究从搜索到可验证研究结果的扩展规律。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。本文研究自主量化因子挖掘中的搜索扩展：在50项源自金融研究报告的任务上，增加代理搜索预算，测量研究表现如何变化以及收益来自何种搜索机制。代理生成并筛选候选量化因子，执行计算评估，研究从搜索到可验证研究结果的扩展规律。
  - 原文位置：全文TXT第1002行；核验TXT行号 1002；引文：The consistent gain indicates that exploring several initial directions can be more valuable than repeatedly improving one locally chosen direction. Together, the two experiments show that the return to additional search depends on both the inherited research state and whether the budget broadens or deepens the search.
- 多步行动过程：yes。每项任务提供金融研究报告中的问题/线索；代理在预算限制下探索因子表达、实现并评估候选因子，随搜索预算增加记录发现质量和机制。
  - 原文位置：全文TXT第3544行；核验TXT行号 3544；引文：Table E.1: Task-level metrics for Claude Opus 5 at iterations 3, 6, and 10.
- 至少一种Agent能力：yes。每项任务提供金融研究报告中的问题/线索；代理在预算限制下探索因子表达、实现并评估候选因子，随搜索预算增加记录发现质量和机制。
  - 原文位置：全文TXT第6205行；核验TXT行号 6205；引文：Table E.4: Task-level metrics for DeepSeek-V4-Pro at iterations 3, 6, and 10.
- 明确科研流程角色：yes。研究对象是金融市场预测因子及其挖掘，具备明确量化研究任务。本文可作为金融/经济研究Agent纳入；candidate建议与特定科学发现边界仍需整体名单规则统一。
  - 原文位置：全文TXT第7979行；核验TXT行号 7979；引文：Table E.6: Task-level metrics for GLM-5.2 at iterations 3, 6, and 10.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：11
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：11（仅归档，不覆盖其他模块）
- 模块内分类路径：11.01.04 金融学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

- 金融市场横截面量化因子及其样本外风险调整收益、单调性和经济假设一致性

### 2.3 容易混淆的边界

代理按金融研究报告中的经济假设构造量化因子，执行回测、分析开发期反馈并迭代；独立评估器再以样本外回测和代码审计评分。工业/量化实践背景不改变其金融研究对象，归11.01.04。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签



### 3.2 科研流程角色



每项任务提供金融研究报告中的问题/线索；代理在预算限制下探索因子表达、实现并评估候选因子，随搜索预算增加记录发现质量和机制。

### 3.3 自主能力

每项任务提供金融研究报告中的问题/线索；代理在预算限制下探索因子表达、实现并评估候选因子，随搜索预算增加记录发现质量和机制。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

研究对象是金融市场预测因子及其挖掘，具备明确量化研究任务。本文可作为金融/经济研究Agent纳入；candidate建议与特定科学发现边界仍需整体名单规则统一。

### 4.2 系统流程与组件

每项任务提供金融研究报告中的问题/线索；代理在预算限制下探索因子表达、实现并评估候选因子，随搜索预算增加记录发现质量和机制。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

每项任务提供金融研究报告中的问题/线索；代理在预算限制下探索因子表达、实现并评估候选因子，随搜索预算增加记录发现质量和机制。 验证以文中所列任务、数据和对照为准。

### 5.2 基线、指标与结果

在50项任务上比较不同搜索规模及相关基线，分析成功率/因子质量随预算变化；仅报告论文实测数字。

### 5.3 科学贡献与证据强度

研究对象是金融市场预测因子及其挖掘，具备明确量化研究任务。本文可作为金融/经济研究Agent纳入；candidate建议与特定科学发现边界仍需整体名单规则统一。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

与一般LLM代理、科学工作流自动化及该领域既有基准/模型相关；本文的具体差异见上述任务设计和验证设置。

## 7. 局限性与风险

本文结果受其数据、模拟环境、评测指标和实验预算限制；不得将基准或仿真表现直接外推为真实部署成效。

## 8. 对综述写作的价值

可用于综述讨论该类Agent的研究对象、工作流角色和验证边界。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

本文研究自主量化因子挖掘中的搜索扩展：在50项源自金融研究报告的任务上，增加代理搜索预算，测量研究表现如何变化以及收益来自何种搜索机制。代理生成并筛选候选量化因子，执行计算评估，研究从搜索到可验证研究结果的扩展规律。

### 9.2 速记版 pipeline

每项任务提供金融研究报告中的问题/线索；代理在预算限制下探索因子表达、实现并评估候选因子，随搜索预算增加记录发现质量和机制。

### 9.3 标注字段汇总

```text
paper_id=ASD-1105
inclusion_status=to_read
scientific_object_modules=11
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=11
module_taxonomy_codes=11.01.04
source_level=first_hand_full_text
fulltext_followup_required=true
```

### 全文后续要求

当前纳入和分类证据已足够；第7节明确的结果/复现细节仍需继续回查。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O3 新实例 | 量化因子挖掘结果可由回测数据计算验证 | “50项源自金融研究报告的任务” · L29 |
| 验证强度 | V2 计算/仿真/回顾性 | 回测评估候选因子表现，属回顾性真实数据检验 | “代理生成并筛选候选量化因子，执行计算评估” · L29 |
| 系统自主性 | L2 闭环执行者 | Agent在预算内自主探索因子表达、实现并迭代评估 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
