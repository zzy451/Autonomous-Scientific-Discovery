# The Silent Failures in Agentic Data Science

**论文信息**

- ID：ASD-0877
- 标题：The Silent Failures in Agentic Data Science
- 作者：Li, Xue; Xia, Hongqian; Gomm, Daniel; Santos, Aécio; Wolff, Cornelius; Hulsebos, Madelon
- 年份：2026
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2610.14115
- 一手阅读来源：https://arxiv.org/abs/2610.14115
- 来源层级：全文
- 阅读版本：对应缓存来源版本，参见Evidence Log
- 阅读版本题名：The Silent Failures in Agentic Data Science
- 原始全文缓存：C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/.tmp_asd_pdfs/2610.14115.html
- PDF / 本地文件路径：未归档PDF
- 当前状态：included
- 阅读日期：2026-10-22
- 笔记作者：Codex（读者证据包经主控审核整合）

## Evidence Log

| 判断项 | 结论 / 原文概括 | 证据位置 | 可信度 |
|---|---|---|---|
| Agent流程从任务制定延伸到模型开发。 | 评测目标是自动化数据科学设计和执行工作流。 | 全文摘要及Introduction | high |
| 研究使用三个评测分支。 | 220任务失效分析、六类受控测试和Kaggle专家方案比较。 | 全文摘要及方法 | high |
| 受控组合重复五次。 | 每个Agent-task-hint combination运行五次并汇总。 | 全文方法节 | high |
| 多数方案至少出现一种失效。 | 包括数据泄漏和验证不当等问题。 | 全文摘要及结果 | high |
| 数据泄漏与较高预测分数相关。 | 仅测准确率可能奖励错误方法。 | 全文摘要及结果讨论 | high |
| Kaggle科学对象未在摘要列明。 | 需逐任务核对后才能增加具体科学模块。 | 全文Kaggle评测节 | medium |

## 0. 摘要翻译

论文研究数据科学Agent的静默方法学错误，包含220项任务失效分析、六类受控失败测试，以及与Kaggle专家方案比较。每个Agent-task-hint组合运行五次。多数方案至少存在一种失误，且数据泄漏可能与更高预测分数同时出现。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 当前判断：included；读者建议：included。
研究执行任务设定、建模、编程、验证与分析的数据科学Agent流程，评估其多步操作及方法学正确性。

### 1.2 排除风险检查

建议01.03，关注数据科学分析程序、建模与验证工作流。Kaggle来源本身不足以支持自然科学模块；不是无具体对象的01.04，也不研究科学共同体或知识生产制度。
完整闭环不是纳入门槛；科研目标、多步行动、至少一项Agent能力及明确科研角色须同时成立。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：01
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：01（仅归档，不替代多模块事实）
- 模块内分类路径：01.03
- 分类深度：03/04使用二级；06/07使用固定三级；其余沿用现有树。
- 分类状态：原文证据复核

### 2.2 对象优先判定

作者报告多数Agent方案至少有一种失败；数据泄漏与更高预测性能正相关。定性比较显示Agent的问题求解创造性及领域知识弱于竞赛专家。

### 2.3 容易混淆的边界

建议01.03，关注数据科学分析程序、建模与验证工作流。Kaggle来源本身不足以支持自然科学模块；不是无具体对象的01.04，也不研究科学共同体或知识生产制度。

## 3. Agent 系统与科研流程角色

研究执行任务设定、建模、编程、验证与分析的数据科学Agent流程，评估其多步操作及方法学正确性。

科研流程与自主能力以本文实际行动和工具调用为依据：

三部分评估：220项任务中的失效分析；六类受控方法学失败测试；与Kaggle专家方案定性比较。每Agent-task-hint组合重复五次。

## 4. 方法设计

### 4.1 方法动机与设计

指出只看预测准确率或代码正确性会漏掉数据泄漏、验证不当等静默方法学错误。

### 4.2 系统流程与组件

三部分评估：220项任务中的失效分析；六类受控方法学失败测试；与Kaggle专家方案定性比较。每Agent-task-hint组合重复五次。

## 5. 实验与验证

### 5.1 验证方式、对象及任务

作者报告多数Agent方案至少有一种失败；数据泄漏与更高预测性能正相关。定性比较显示Agent的问题求解创造性及领域知识弱于竞赛专家。

### 5.2 基线、指标与结果

作者报告多数Agent方案至少有一种失败；数据泄漏与更高预测性能正相关。定性比较显示Agent的问题求解创造性及领域知识弱于竞赛专家。

### 5.3 科学贡献与证据强度

指出只看预测准确率或代码正确性会漏掉数据泄漏、验证不当等静默方法学错误。

证据层级：原始全文支持；作者报告结果不等于独立复现。

## 6. 与已有工作的关系

与Agentic data science、AutoML及数据分析Agent基准互补，聚焦方法有效性。

## 7. 局限性与风险

摘要与全文任务未为所有Kaggle案例明确科学对象；相关性结果不能证明泄漏造成性能提升；受控错误类别不能覆盖全部研究缺陷。

## 8. 对综述写作的价值

适合讨论科研Agent评测中的方法有效性与结果指标之间的差距。

推荐引用强度：普通引用，可在核对原文后用于相应领域案例。

## 9. 总结

### 9.1 一句话概括

分析科研数据Agent的隐蔽失败

### 9.2 速记版 pipeline

三部分评估：220项任务中的失效分析；六类受控方法学失败测试；与Kaggle专家方案定性比较。每Agent-task-hint组合重复五次。

### 9.3 标注字段汇总

```text
paper_id=ASD-0877
inclusion_status=included
scientific_object_modules=01
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=01
module_taxonomy_codes=01.03
source_level=fulltext
fulltext_followup_required=false
```

### 全文后续要求

本轮已读原始全文并完成对象分类；无需为纳入/分类另做全文补读。具体引用时仍需回查相应原文位置。


## 2026-10-29 PDF补齐归档

- 本地PDF：`Reference_PDF/01_Formal_Information_and_Computational_Sciences/ASD-0877_The_Silent_Failures_in_Agentic_Data_Science.pdf`，共19页；已核验标题、页面解析和逐页渲染。
- 下载来源：https://arxiv.org/pdf/2610.14115
- 版本：official arXiv preprint PDF; version as downloaded。
- 本轮为来源文件归档，不自动改变既有科学分类或将未决PR意见标记为已结案。
