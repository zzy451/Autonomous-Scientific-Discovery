# PrimeScientist: Strategic Allocation of Research Effort in Autonomous Research

**论文信息**

- ID：ASD-0946
- 标题：PrimeScientist: Strategic Allocation of Research Effort in Autonomous Research
- 作者：Yu, Xinle; Bai, Fan; Sun, Kaiser; Miao, Hengshuo; Anand, Abhay; Luo, Zhongyan; Zhou, Kun; Wang, Zhen
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2609.17846
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0946.txt
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Xinle_2026_PrimeScientist_Strategic_Allocation_of_Research_Effort_in_Autonomous_Research_ASD0946.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 研究目标/科学问题 | PrimeScientist将自主研究中的方向选择与资源投入共同建模为序贯决策，维护可执行计划树，并以自适应MCTS在研究尝试间分配剩余资源。评估覆盖AI研究、系统与代码优化、机器学习工程；作者报告在12项AI研究任务上战略分配提高研究质量和样本效率。 | 本地全文：ASD-0946中与研究目标/科学问题直接相关的原文句子；核验TXT行号 260 | Autonomous research agents aim to automate scientific workflows, from proposing ideas to conducting experiments and analyzing results. Yet current AI and research agents can propose more directions than available resources allow them to pursue. Moreover, each attempt could consume substantial resources, requiring agents to reconsider how to invest in subsequent research. Thus, deciding how to invest research effort strategically should be a defining capability of autonomous research agents. Accordingly, we introduce PrimeScientist, which jointly determines research direction and resource investment across successive research attempts. Specifically, we formulate this challenge of strategic research effort allocation as a sequential decision problem where remaining resources should explicitly guide the research policy. We first introduce an executable plan tree that preserves competing plans and their outcomes across attempts. Building on this representation, we propose an adaptive MCTS-based allocation policy that balances exploration and exploitation using experimental feedback and remaining resources. Comprehensive evaluations across AI research, systems and code optimization, and machine learning engineering show that strategic allocation improves research quality and sample efficiency together. Across 12 AI research tasks, PrimeScientist improves average reward by 10.3% with 50.6% fewer research attempts than AutoResearch under the same resource budget. We believe making research effort allocation an explicit optimization target establishes effective resource use as a core research capability for autonomous agents to drive scientific breakthroughs at scale.11 1 Code and data are available at https://github.com/Henri-XYu02/PrimeScientist. | 高（一手正文；非独立复现） |
| 多步行动/研究流程 | 每轮维护多个计划及执行状态，MCTS在探索与利用间权衡，依据进展和剩余预算选择下一方向与投入，再将实验反馈纳入后续决策。 | 本地全文：ASD-0946中与多步行动/研究流程直接相关的原文句子；核验TXT行号 267 | Building on this representation, we propose an adaptive MCTS-based allocation policy that balances exploration and exploitation using experimental feedback and remaining resources. | 高（一手正文；非独立复现） |
| Agent实现与能力 | PrimeScientist使用可执行计划树保存候选研究路线，并以基于MCTS的策略根据实验反馈和剩余资源分配后续研究预算。 | 本地全文：ASD-0946中与Agent实现与能力直接相关的原文句子；核验TXT行号 266 | We first introduce an executable plan tree that preserves competing plans and their outcomes across attempts. | 高（一手正文；非独立复现） |
| 实验任务与验证设置 | 实验覆盖AI研究、系统/代码优化和机器学习工程；作者另报告12项AI研究任务上的质量及样本效率结果。 | 本地全文：ASD-0946中与实验任务与验证设置直接相关的原文句子；核验TXT行号 774 | Benchmarks. Our evaluation spans three complementary areas of autonomous research: AI research, systems and code optimization, and machine learning engineering. This breadth tests research allocation across experimental design, implementation strategy, and model development. FIRE-Bench [58] evaluates agents on the rediscovery of well-established AI research findings. Given a research question, datasets, and experimental requirements, the agent implements experiments and reports conclusions; the benchmark's claim-level evaluator, based on RAGChecker [44], compares these conclusions with reference findings, and we report F1. AutoLab [60] tests performance optimization under correctness constraints. We evaluate its eight systems-optimization and puzzle tasks, using throughput-based rewards for the optimization tasks. MLE-Bench [5] evaluates end-to-end machine learning engineering on historical Kaggle competitions. We report the task-specific scores and metric directions shown in Table 4. Appendix E describes the tasks across all three benchmarks. | 高（一手正文；非独立复现） |
| 作者报告的结果/贡献 | 作者报告战略资源分配可同时改善研究质量与样本效率；结论应结合计划基线、任务域及预算配置理解。 贡献是将研究方向与计算资源投入联合纳入序贯政策，而不是每轮独立选择实验。 | 本地全文中包含该原句的位置；核验TXT行号 269 | Across 12 AI research tasks, PrimeScientist improves average reward by 10.3% with 50.6% fewer research attempts than AutoResearch under the same resource budget. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

PrimeScientist将自主研究中的方向选择与资源投入共同建模为序贯决策，维护可执行计划树，并以自适应MCTS在研究尝试间分配剩余资源。评估覆盖AI研究、系统与代码优化、机器学习工程；作者报告在12项AI研究任务上战略分配提高研究质量和样本效率。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。PrimeScientist将自主研究中的方向选择与资源投入共同建模为序贯决策，维护可执行计划树，并以自适应MCTS在研究尝试间分配剩余资源。评估覆盖AI研究、系统与代码优化、机器学习工程；作者报告在12项AI研究任务上战略分配提高研究质量和样本效率。
  - 原文位置：本地全文：ASD-0946中与研究目标/科学问题直接相关的原文句子；核验TXT行号 260；引文：Autonomous research agents aim to automate scientific workflows, from proposing ideas to conducting experiments and analyzing results. Yet current AI and research agents can propose more directions than available resources allow them to pursue. Moreover, each attempt could consume substantial resources, requiring agents to reconsider how to invest in subsequent research. Thus, deciding how to invest research effort strategically should be a defining capability of autonomous research agents. Accordingly, we introduce PrimeScientist, which jointly determines research direction and resource investment across successive research attempts. Specifically, we formulate this challenge of strategic research effort allocation as a sequential decision problem where remaining resources should explicitly guide the research policy. We first introduce an executable plan tree that preserves competing plans and their outcomes across attempts. Building on this representation, we propose an adaptive MCTS-based allocation policy that balances exploration and exploitation using experimental feedback and remaining resources. Comprehensive evaluations across AI research, systems and code optimization, and machine learning engineering show that strategic allocation improves research quality and sample efficiency together. Across 12 AI research tasks, PrimeScientist improves average reward by 10.3% with 50.6% fewer research attempts than AutoResearch under the same resource budget. We believe making research effort allocation an explicit optimization target establishes effective resource use as a core research capability for autonomous agents to drive scientific breakthroughs at scale.11 1 Code and data are available at https://github.com/Henri-XYu02/PrimeScientist.
- 多步行动过程：yes。每轮维护多个计划及执行状态，MCTS在探索与利用间权衡，依据进展和剩余预算选择下一方向与投入，再将实验反馈纳入后续决策。
  - 原文位置：本地全文：ASD-0946中与多步行动/研究流程直接相关的原文句子；核验TXT行号 267；引文：Building on this representation, we propose an adaptive MCTS-based allocation policy that balances exploration and exploitation using experimental feedback and remaining resources.
- 至少一种Agent能力：yes。PrimeScientist使用可执行计划树保存候选研究路线，并以基于MCTS的策略根据实验反馈和剩余资源分配后续研究预算。
  - 原文位置：本地全文：ASD-0946中与Agent实现与能力直接相关的原文句子；核验TXT行号 266；引文：We first introduce an executable plan tree that preserves competing plans and their outcomes across attempts.
- 明确科研流程角色：yes。实验覆盖AI研究、系统/代码优化和机器学习工程；作者另报告12项AI研究任务上的质量及样本效率结果。
  - 原文位置：本地全文：ASD-0946中与实验任务与验证设置直接相关的原文句子；核验TXT行号 774；引文：Benchmarks. Our evaluation spans three complementary areas of autonomous research: AI research, systems and code optimization, and machine learning engineering. This breadth tests research allocation across experimental design, implementation strategy, and model development. FIRE-Bench [58] evaluates agents on the rediscovery of well-established AI research findings. Given a research question, datasets, and experimental requirements, the agent implements experiments and reports conclusions; the benchmark's claim-level evaluator, based on RAGChecker [44], compares these conclusions with reference findings, and we report F1. AutoLab [60] tests performance optimization under correctness constraints. We evaluate its eight systems-optimization and puzzle tasks, using throughput-based rewards for the optimization tasks. MLE-Bench [5] evaluates end-to-end machine learning engineering on historical Kaggle competitions. We report the task-specific scores and metric directions shown in Table 4. Appendix E describes the tasks across all three benchmarks.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：01
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：01（仅归档，不覆盖其他模块）
- 模块内分类路径：01.02 计算机科学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

对象模块与代码沿用输入审计记录（01；01.02）；是否纳入与对象分类分开判断。

### 2.3 容易混淆的边界

对象模块与代码沿用输入审计记录（01；01.02）；是否纳入与对象分类分开判断。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

自主科研Agent

### 3.2 科研流程角色

科研问题处理；多步行动或评测

PrimeScientist使用可执行计划树保存候选研究路线，并以基于MCTS的策略根据实验反馈和剩余资源分配后续研究预算。

### 3.3 自主能力

PrimeScientist使用可执行计划树保存候选研究路线，并以基于MCTS的策略根据实验反馈和剩余资源分配后续研究预算。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

贡献是将研究方向与计算资源投入联合纳入序贯政策，而不是每轮独立选择实验。

### 4.2 系统流程与组件

每轮维护多个计划及执行状态，MCTS在探索与利用间权衡，依据进展和剩余预算选择下一方向与投入，再将实验反馈纳入后续决策。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

实验覆盖AI研究、系统/代码优化和机器学习工程；作者另报告12项AI研究任务上的质量及样本效率结果。

### 5.2 基线、指标与结果

作者报告战略资源分配可同时改善研究质量与样本效率；结论应结合计划基线、任务域及预算配置理解。

### 5.3 科学贡献与证据强度

贡献是将研究方向与计算资源投入联合纳入序贯政策，而不是每轮独立选择实验。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

论文以“PrimeScientist: Strategic Allocation of Research Effort in Autonomous Research”对应的研究任务为对象，具体与哪些既有系统或基准比较，应结合其正文相关工作和实验基线判断；不把工具名称直接视为科学对象。

## 7. 局限性与风险

策略表现依赖计划树构造、反馈可用性和资源预算；三个实验域不足以代表全部科研工作。

## 8. 对综述写作的价值

可用于综述“PrimeScientist: Strategic Allocation of Research Effort in Autonomous Research”所涉及的Agent任务、研究流程和验证方式；其证据边界为本论文实际报告的任务集与实验结果。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

PrimeScientist用MCTS计划树根据实验反馈和剩余预算分配研究投入。

### 9.2 速记版 pipeline

每轮维护多个计划及执行状态，MCTS在探索与利用间权衡，依据进展和剩余预算选择下一方向与投入，再将实验反馈纳入后续决策。

### 9.3 标注字段汇总

```text
paper_id=ASD-0946
inclusion_status=to_read
scientific_object_modules=01
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=01
module_taxonomy_codes=01.02
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O2 既定基准 | 在预定义AI研究任务基准上评估 | “FIRE-Bench [58] evaluates agents on the rediscovery of well-established AI research findings” · L42 |
| 验证强度 | V1 基准/内部评测 | 基准得分和F1指标评价 | “the benchmark's claim-level evaluator, based on RAGChecker [44], compares these conclusions with reference findings” · L42 |
| 系统自主性 | L2 闭环执行者 | 系统自主规划并迭代多步实验闭环 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
