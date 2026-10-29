# AgonAlpha: Autonomous Alpha Discovery via Prompt Economy and Scalable Agentic Search

**论文信息**

- ID：ASD-0977
- 标题：AgonAlpha: Autonomous Alpha Discovery via Prompt Economy and Scalable Agentic Search
- 作者：Ye, Weicheng; Sun, Youran; Ren, Xingyu; Yu, Shunyao; Yi, Chugang; Yang, Haizhao
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2608.11250
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0977.txt
- PDF / 本地文件路径：Reference_PDF/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Weicheng_2026_AgonAlpha_Autonomous_Alpha_Discovery_via_Prompt_Economy_and_Scalable_ASD0977.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 纳入与科学目标 | 研究提出AgonAlpha，将研究假设、可执行因子表达式、平台回测证据、解释与审查状态作为整体搜索对象。系统由提案与审查角色协作，审查者可重新运行模拟并否决不合格候选；调度器按待完成任务管理有限评估预算。作者报告五名用户、六种模型后端在WorldQuant BRAIN上的部署，并记录每个提交的提示到表达式来源。 | 摘要；TXT第423行；核验TXT行号 423 | Language models can propose many plausible trading factors, but an autonomous research system must also allocate its evaluation budget, verify its own evidence, and preserve how each candidate was produced. | 高（一手正文；非独立复现） |
| 方法与多步工作流 | 用户给出因子研究目标，提案角色生成假设和候选表达式；系统通过WorldQuant BRAIN执行模拟与筛选，审查角色在新上下文中检查证据、重跑模拟并可否决，调度器按候选状态分配并行预算。平台反馈用于继续搜索或停止，最终保留候选及其完整来源链。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。 | 摘要；TXT第424行；核验TXT行号 424 | We present AgonAlpha, an architecture that searches over frozen research artifacts—hypotheses, executable expressions, platform evidence, rationales, and review status—rather than formulas alone. | 高（一手正文；非独立复现） |
| Agent能力与行动 | AgonAlpha: Autonomous Alpha Discovery via Prompt Economy and Scalable Agentic Search。系统角色与能力：用户给出因子研究目标，提案角色生成假设和候选表达式；系统通过WorldQuant BRAIN执行模拟与筛选，审查角色在新上下文中检查证据、重跑模拟并可否决，调度器按候选状态分配并行预算。平台反馈用于继续搜索或停止，最终保留候选及其完整来源链。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。 | 摘要；TXT第425行；核验TXT行号 425 | To our knowledge, AgonAlpha is the first alpha-mining system to combine verified artifact search, a fresh-context adversarial reviewer with re-execution and veto authority, and pending-aware parallel budget allocation, together with a complete public evidence trail. Independent deployments on WorldQuant BRAIN produced SPECTACULAR-grade alphas across five users and six model backends, with Fitness reaching 9.50 and Sharpe reaching 3.48, while retaining prompt-to-expression provenance for every su | 高（一手正文；非独立复现） |
| 验证与结果 | 验证包括平台部署、因子表现及审查/并发调度分析；作者报告跨五用户、六后端的提交结果，Fitness最高9.50、Sharpe最高3.48。该工作主要贡献是金融因子搜索和可审计工作流，实证结果仍受平台仿真与样本设定约束。 | 摘要；TXT第426行；核验TXT行号 426 | Independent deployments on WorldQuant BRAIN produced SPECTACULAR-grade alphas across five users and six model backends, with Fitness reaching 9.50 and Sharpe reaching 3.48, while retaining prompt-to-expression provenance for every submission. | 高（一手正文；非独立复现） |
| 贡献与综述价值 | Agent化金融研究、对抗式证据复核、预算分配与可复现研究轨迹。 科学贡献与系统贡献按上述证据分别表述。 | Conclusion；TXT第2282行；核验TXT行号 2282 | AgonAlpha suggests that the core principles of the Agon philosophy can be compressed into a minimal yet complete discovery architecture: two roles and a 101-line prompt are sufficient to support an adversarially verified research workflow. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

研究提出AgonAlpha，将研究假设、可执行因子表达式、平台回测证据、解释与审查状态作为整体搜索对象。系统由提案与审查角色协作，审查者可重新运行模拟并否决不合格候选；调度器按待完成任务管理有限评估预算。作者报告五名用户、六种模型后端在WorldQuant BRAIN上的部署，并记录每个提交的提示到表达式来源。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。研究提出AgonAlpha，将研究假设、可执行因子表达式、平台回测证据、解释与审查状态作为整体搜索对象。系统由提案与审查角色协作，审查者可重新运行模拟并否决不合格候选；调度器按待完成任务管理有限评估预算。作者报告五名用户、六种模型后端在WorldQuant BRAIN上的部署，并记录每个提交的提示到表达式来源。
  - 原文位置：摘要；TXT第423行；核验TXT行号 423；引文：Language models can propose many plausible trading factors, but an autonomous research system must also allocate its evaluation budget, verify its own evidence, and preserve how each candidate was produced.
- 多步行动过程：yes。用户给出因子研究目标，提案角色生成假设和候选表达式；系统通过WorldQuant BRAIN执行模拟与筛选，审查角色在新上下文中检查证据、重跑模拟并可否决，调度器按候选状态分配并行预算。平台反馈用于继续搜索或停止，最终保留候选及其完整来源链。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。
  - 原文位置：摘要；TXT第424行；核验TXT行号 424；引文：We present AgonAlpha, an architecture that searches over frozen research artifacts—hypotheses, executable expressions, platform evidence, rationales, and review status—rather than formulas alone.
- 至少一种Agent能力：yes。AgonAlpha: Autonomous Alpha Discovery via Prompt Economy and Scalable Agentic Search。系统角色与能力：用户给出因子研究目标，提案角色生成假设和候选表达式；系统通过WorldQuant BRAIN执行模拟与筛选，审查角色在新上下文中检查证据、重跑模拟并可否决，调度器按候选状态分配并行预算。平台反馈用于继续搜索或停止，最终保留候选及其完整来源链。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。
  - 原文位置：摘要；TXT第425行；核验TXT行号 425；引文：To our knowledge, AgonAlpha is the first alpha-mining system to combine verified artifact search, a fresh-context adversarial reviewer with re-execution and veto authority, and pending-aware parallel budget allocation, together with a complete public evidence trail. Independent deployments on WorldQuant BRAIN produced SPECTACULAR-grade alphas across five users and six model backends, with Fitness reaching 9.50 and Sharpe reaching 3.48, while retaining prompt-to-expression provenance for every su
- 明确科研流程角色：yes。验证包括平台部署、因子表现及审查/并发调度分析；作者报告跨五用户、六后端的提交结果，Fitness最高9.50、Sharpe最高3.48。该工作主要贡献是金融因子搜索和可审计工作流，实证结果仍受平台仿真与样本设定约束。
  - 原文位置：摘要；TXT第426行；核验TXT行号 426；引文：Independent deployments on WorldQuant BRAIN produced SPECTACULAR-grade alphas across five users and six model backends, with Fitness reaching 9.50 and Sharpe reaching 3.48, while retaining prompt-to-expression provenance for every submission.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：11
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：11（仅归档，不覆盖其他模块）
- 模块内分类路径：11.01 经济学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

金融市场中的股票alpha/因子研究，归入11.01。它是以平台模拟证据评价候选策略的研究Agent，不应泛化为一般科学实验。

### 2.3 容易混淆的边界

金融市场中的股票alpha/因子研究，归入11.01。它是以平台模拟证据评价候选策略的研究Agent，不应泛化为一般科学实验。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM科研Agent

### 3.2 科研流程角色

计算/数据分析

AgonAlpha: Autonomous Alpha Discovery via Prompt Economy and Scalable Agentic Search。系统角色与能力：用户给出因子研究目标，提案角色生成假设和候选表达式；系统通过WorldQuant BRAIN执行模拟与筛选，审查角色在新上下文中检查证据、重跑模拟并可否决，调度器按候选状态分配并行预算。平台反馈用于继续搜索或停止，最终保留候选及其完整来源链。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 3.3 自主能力

AgonAlpha: Autonomous Alpha Discovery via Prompt Economy and Scalable Agentic Search。系统角色与能力：用户给出因子研究目标，提案角色生成假设和候选表达式；系统通过WorldQuant BRAIN执行模拟与筛选，审查角色在新上下文中检查证据、重跑模拟并可否决，调度器按候选状态分配并行预算。平台反馈用于继续搜索或停止，最终保留候选及其完整来源链。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

Agent化金融研究、对抗式证据复核、预算分配与可复现研究轨迹。 科学贡献与系统贡献按上述证据分别表述。

### 4.2 系统流程与组件

用户给出因子研究目标，提案角色生成假设和候选表达式；系统通过WorldQuant BRAIN执行模拟与筛选，审查角色在新上下文中检查证据、重跑模拟并可否决，调度器按候选状态分配并行预算。平台反馈用于继续搜索或停止，最终保留候选及其完整来源链。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

验证包括平台部署、因子表现及审查/并发调度分析；作者报告跨五用户、六后端的提交结果，Fitness最高9.50、Sharpe最高3.48。该工作主要贡献是金融因子搜索和可审计工作流，实证结果仍受平台仿真与样本设定约束。

### 5.2 基线、指标与结果

验证包括平台部署、因子表现及审查/并发调度分析；作者报告跨五用户、六后端的提交结果，Fitness最高9.50、Sharpe最高3.48。该工作主要贡献是金融因子搜索和可审计工作流，实证结果仍受平台仿真与样本设定约束。

### 5.3 科学贡献与证据强度

Agent化金融研究、对抗式证据复核、预算分配与可复现研究轨迹。 科学贡献与系统贡献按上述证据分别表述。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

论文将自身置于LLM因子生成、因子搜索与交易回测研究中，指出以公式为唯一搜索单元的系统难保留假设、审查和证据来源；其对照重点是已有公式级Alpha系统与自评分/阈值验证。

## 7. 局限性与风险

作者及读者可确认的适用边界：作者将评估限定在统一的WorldQuant BRAIN协议（美国TOP3000股票、2019–2023窗口）；结果仍是平台模拟表现，不能直接等同真实交易收益。

## 8. 对综述写作的价值

Agent化金融研究、对抗式证据复核、预算分配与可复现研究轨迹。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

研究提出AgonAlpha，将研究假设、可执行因子表达式、平台回测证据、解释与审查状态作为整体搜索对象。

### 9.2 速记版 pipeline

用户给出因子研究目标，提案角色生成假设和候选表达式；系统通过WorldQuant BRAIN执行模拟与筛选，审查角色在新上下文中检查证据、重跑模拟并可否决，调度器按候选状态分配并行预算。平台反馈用于继续搜索或停止，最终保留候选及其完整来源链。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 9.3 标注字段汇总

```text
paper_id=ASD-0977
inclusion_status=to_read
scientific_object_modules=11
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=11
module_taxonomy_codes=11.01
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`11.01.04` 金融学；二级：`11.01`。
- 原文位置：PDF p.7。
- 判定：真实金融alpha检验、Fitness和Sharpe，属于金融学。
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
