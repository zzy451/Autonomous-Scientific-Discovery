# CABAL: Multi-Agent Simulacra for Tracing the Effects of Collusive Bidding in Peer Review

**论文信息**

- ID：ASD-0909
- 标题：CABAL: Multi-Agent Simulacra for Tracing the Effects of Collusive Bidding in Peer Review
- 作者：Zhou, Jicheng; Li, Kemou; Wong, Kahim; Li, Zheyuan; Shi, Zhuan; Li, Fengpeng; Wu, Haiwei; Zhou, Jiantao
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2609.05227
- 一手阅读来源：https://arxiv.org/abs/2609.05227
- 来源层级：全文
- 阅读版本：对应缓存来源版本，参见Evidence Log
- 阅读版本题名：CABAL: Multi-Agent Simulacra for Tracing the Effects of Collusive Bidding in Peer Review
- 原始全文缓存：C:/Users/20683/Desktop/综述/.tmp_asd_pdfs/source_F/2609.05227.pdf
- PDF / 本地文件路径：Reference_PDF/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Zhou_2026_CABAL.pdf
- 当前状态：included
- 阅读日期：2026-10-22
- 笔记作者：Codex（读者证据包经主控审核整合）

## Evidence Log

| 判断项 | 结论 / 原文概括 | 证据位置 | 可信度 |
|---|---|---|---|
| 研究设计 | 作者固定论文、审稿人、COI和分配程序，只改变审稿人是否合谋，以构造匹配反事实。 | §1 Introduction；§2 Problem Statement | high |
| Agent流程 | 工作流实例化诚实/合谋reviewer simulacra，执行投标、分配和评审。 | §3 CABAL；Fig. 2；§3.4 | high |
| 合谋机制 | 以互惠reviewer-paper affinity构造合谋圈和目标论文。 | §3.2 Expertise-Grounded Collusion Construction | high |
| 实验指标 | 分别报告目标分配获取、目标评分变化及会议整体效应。 | §4 Experiments；§§4.2–4.4 | high |
| 结果 | 报告目标捕获超过翻倍，合谋审稿人评分约高2分，会议层面影响较小。 | Abstract；§4 | high |
| 检测边界 | 正常专业亲和度会混淆正向投标图；Very-High诊断精度较高但覆盖有限。 | §5；Appendix D | high |

## 0. 摘要翻译

本文提出CABAL多Agent模拟平台，在固定会议论文、审稿人、利益冲突与分配机制的条件下，对比诚实和合谋审稿人的行为。系统依据审稿人与论文的专业亲和度构造合谋圈，Agent依次投标、参与分配并评审。实验显示，合谋提高目标论文获得合谋审稿人的概率及评分，但会议整体影响相对有限；现有投标图检测也容易受正常专业亲和度干扰。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 当前判断：included；读者建议：included。
全文明确使用LLM reviewer agents执行诚实或合谋策略，覆盖投标、审稿分配和评审等多步科研流程，研究对象是同行评议制度，符合科研目标、行动过程、Agent能力和科研角色四项标准。

### 1.2 排除风险检查

邻近01.03的一般网络/多Agent方法，但核心对象是科研同行评议制度，故归11.07。不是研究通用Agent能力。
完整闭环不是纳入门槛；科研目标、多步行动、至少一项Agent能力及明确科研角色须同时成立。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：11
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：11（仅归档，不替代多模块事实）
- 模块内分类路径：11.07
- 分类深度：03/04使用二级；06/07使用固定三级；其余沿用现有树。
- 分类状态：原文证据复核

### 2.2 对象优先判定

对象为科学会议同行评审。基线是在相同论文、审稿人、COI和分配机制下的全诚实Agent世界。指标包括目标论文assignment capture、评分变化、会议总体效果和检测precision/coverage。结果：目标捕获超过翻倍，合谋者评分比诚实共同审稿人高约2分；会议整体影响较小，投标图检测受正常affinity混淆。

### 2.3 容易混淆的边界

邻近01.03的一般网络/多Agent方法，但核心对象是科研同行评议制度，故归11.07。不是研究通用Agent能力。

## 3. Agent 系统与科研流程角色

全文明确使用LLM reviewer agents执行诚实或合谋策略，覆盖投标、审稿分配和评审等多步科研流程，研究对象是同行评议制度，符合科研目标、行动过程、Agent能力和科研角色四项标准。

科研流程与自主能力以本文实际行动和工具调用为依据：

固定会议substrate；根据reviewer-paper affinity与COI限制构造合谋圈；LLM审稿人Agent执行投标、分配后的评审；比较匹配的诚实/合谋世界，并对投标阶段检测器做压力测试。

## 4. 方法设计

### 4.1 方法动机与设计

在受控反事实设置中联结合谋策略、投标、审稿分配、下游评审和会议结果分析。

### 4.2 系统流程与组件

固定会议substrate；根据reviewer-paper affinity与COI限制构造合谋圈；LLM审稿人Agent执行投标、分配后的评审；比较匹配的诚实/合谋世界，并对投标阶段检测器做压力测试。

## 5. 实验与验证

### 5.1 验证方式、对象及任务

对象为科学会议同行评审。基线是在相同论文、审稿人、COI和分配机制下的全诚实Agent世界。指标包括目标论文assignment capture、评分变化、会议总体效果和检测precision/coverage。结果：目标捕获超过翻倍，合谋者评分比诚实共同审稿人高约2分；会议整体影响较小，投标图检测受正常affinity混淆。

### 5.2 基线、指标与结果

对象为科学会议同行评审。基线是在相同论文、审稿人、COI和分配机制下的全诚实Agent世界。指标包括目标论文assignment capture、评分变化、会议总体效果和检测precision/coverage。结果：目标捕获超过翻倍，合谋者评分比诚实共同审稿人高约2分；会议整体影响较小，投标图检测受正常affinity混淆。

### 5.3 科学贡献与证据强度

在受控反事实设置中联结合谋策略、投标、审稿分配、下游评审和会议结果分析。

证据层级：原始全文支持；作者报告结果不等于独立复现。

## 6. 与已有工作的关系

连接审稿人匹配与分配机制、策略性投标/合谋研究以及LLM同行评审模拟。

## 7. 局限性与风险

实验依赖模拟行为、合成投稿、affinity估算及特定会议设定，不能直接当作现实会议的合谋率或真实因果效应。

## 8. 对综述写作的价值

为11.07提供同行评议治理的Agent模拟证据，并展示科研制度作为多Agent实验对象的分类实例。

推荐引用强度：普通引用，可在核对原文后用于相应领域案例。

## 9. 总结

### 9.1 一句话概括

模拟同行评议中的合谋投标

### 9.2 速记版 pipeline

固定会议substrate；根据reviewer-paper affinity与COI限制构造合谋圈；LLM审稿人Agent执行投标、分配后的评审；比较匹配的诚实/合谋世界，并对投标阶段检测器做压力测试。

### 9.3 标注字段汇总

```text
paper_id=ASD-0909
inclusion_status=included
scientific_object_modules=11
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=11
module_taxonomy_codes=11.07
source_level=fulltext
fulltext_followup_required=false
```

### 全文后续要求

本轮已读原始全文并完成对象分类；无需为纳入/分类另做全文补读。具体引用时仍需回查相应原文位置。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O3 新实例 | 在固定论文、审稿人和分配机制下模拟同行评审，对比诚实和合谋行为，答案可由模拟输出计算 | “在固定会议论文、审稿人、利益冲突与分配机制的条件下” · L34 |
| 验证强度 | V2 计算/仿真/回顾性 | 在受控模拟中比较合谋与诚实Agent的assignment capture和评分，属计算实验 | “目标捕获超过翻倍，合谋者评分比诚实共同审稿人高约2分” · L90 |
| 系统自主性 | L1 任务助手 |  | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
