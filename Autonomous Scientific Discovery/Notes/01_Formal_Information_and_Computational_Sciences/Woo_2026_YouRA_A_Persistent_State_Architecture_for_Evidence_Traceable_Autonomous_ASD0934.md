# YouRA: A Persistent-State Architecture for Evidence-Traceable Autonomous Research Agents

**论文信息**

- ID：ASD-0934
- 标题：YouRA: A Persistent-State Architecture for Evidence-Traceable Autonomous Research Agents
- 作者：Yoonkyu Woo; Woojin Lee; Jin-Xia Huang
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2610.01097
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0934.txt
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Woo_2026_YouRA_A_Persistent_State_Architecture_for_Evidence_Traceable_Autonomous_ASD0934.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 研究目标/科学问题 | YouRA 提出支持持久状态和证据追踪的自主研究架构，整合Verification State Architecture、独立控制器和执行Agent，跨研究过程保存假设、门控、证据指针、执行证据与失败历史。论文在来自近期ICLR、ICML和NeurIPS workshop的 201 项任务上评估，任务由 MLR-Bench 归入九个机器学习主题。 | 本地全文：ASD-0934中与研究目标/科学问题直接相关的原文句子；核验TXT行号 398 | End-to-end research agents can now produce complete scientific papers, yet manuscript claims often diverge from executed experiments. This gap is structural: research state, failure histories, and claim–evidence alignment are not maintained as persistent, verifiable state across long-horizon pipelines. We present YouRA (Your Research Agent), an architecture for stateful, evidence-traceable autonomous research. YouRA preserves research state, execution evidence, and failure history across the research trajectory by integrating three components: a Verification State Architecture (VSA) that tracks hypotheses, gates, and evidence pointers; an Independent Controller that turns state and reflection records into lifecycle, recovery, and debate/review control while separating control from execution; and Stateful Reflection that logs failures as structured lessons and routes recovery through bounded repair, redesign, or reset. On MLR-Bench’s predefined ten-task end-to-end subset, YouRA improves over both MLR-Agent and AI Scientist V2 on scalar Overall across all three matched backbones. An automated diagnostic using MLR-Bench’s hallucination taxonomy reports intersection/union counts for four fact-based failure types, and data-provenance diagnostic shows more real-data-based outputs. Ablating each of the four components (the VSA, the Independent Controller, MCP tool access, and reflection-guided recovery) supports their separable contributions. Removing either core-state component drops YouRA below the full system. Code: https://github.com/PrayPrey/Your-Research-Agent. | 高（一手正文；非独立复现） |
| 多步行动/研究流程 | VSA记录假设、门控和证据指针；控制器读取状态并分配或恢复工作；执行Agent运行工具并写回结果与失败证据，供后续阶段和审查使用。 | 本地全文中包含该原句的位置；核验TXT行号 2351 | The Independent Controller turns VSA records into stage transitions, recovery choices, and persona selection, making persistent state an active control surface rather than a passive log. It runs in an independent LLM context decoupled from the task-execution agent; in our implementation, this controller is GPT-5.2 OpenAI (2025), accessed through OpenRouter API. At each step it reads only two inputs: a compact summary of the current VSA and the most recent per-stage artifact pointer. Because the controller never sees the full execution trace, its context does not grow with the pipeline length, and its routing decisions are less directly exposed to the task-execution agent’s internal reasoning. The same Independent Controller is reused in Hypothesis Debate, where it selects personas and judges convergence; in Adversarial Fact Review, the independent critics are the reviewer personas, which run as context-isolated task agents of the backbone LLM, while the controller’s Stop hook handles only round-to-round continuation. Operationally, the controller’s per-stage output is consumed by a Stop hook that either approves termination, emits a resume prompt back to the task-execution LLM, or escalates a MUST_STOP signal when human intervention is required. | 高（一手正文；非独立复现） |
| Agent实现与能力 | YouRA由VSA状态层、独立控制器和工具型执行Agent组成，维护研究状态及证据轨迹，支持跨会话恢复、工作分配与独立审查。 | 本地全文：ASD-0934中与多步行动/研究流程直接相关的原文句子；核验TXT行号 398 | YouRA preserves research state, execution evidence, and failure history across the research trajectory by integrating three components: a Verification State Architecture (VSA) that tracks hypotheses, gates, and evidence pointers; an Independent Controller that turns state and reflection records into lifecycle, recovery, and debate/review control while separating control from execution; and Stateful Reflection that logs failures as structured lessons and routes recovery through bounded repair, redesign, or reset. | 高（一手正文；非独立复现） |
| 实验任务与验证设置 | 评估涉及 201 项来自近期ICLR/ICML/NeurIPS workshop的任务，覆盖MLR-Bench九个核心机器学习主题；与论文列出的Agent基线比较。 | 本地全文：ASD-0934中与实验任务与验证设置直接相关的原文句子；核验TXT行号 785 | We evaluate on MLR-Bench Chen et al. (2026), a benchmark for open-ended ML research agents that provides 201 workshop-derived research tasks, MLR-Judge rubrics, and the MLR-Agent baseline pipeline for idea generation, proposal formulation, experimentation, and paper writing. The 201 tasks are sourced from recent ICLR/ICML/NeurIPS workshops and are categorized by MLR-Bench into nine core ML topics: LLMs and Vision-Language Models, AI for Science, ML Theory, Trustworthy AI, Computer Vision, ML Systems, Multimodality, Reinforcement Learning, and other emerging topics. End-to-end and pairwise paper-level evaluation use the predefined ten-task subset specified by MLR-Bench (Table 1 and Table 2). As supplementary upstream context on the full task pool, Appendix Table 13 compares YouRA and MLR-Agent on Idea/Proposal-stage quality across all 201 tasks. | 高（一手正文；非独立复现） |
| 作者报告的结果/贡献 | 作者报告YouRA在所设任务集上的研究推进和证据追踪指标；表现应结合201项任务及各项基线设置理解。 系统贡献是以持久状态及证据指针维持研究连续性，并以独立控制器将任务分配、恢复和检查与执行隔离。 | 本地全文中包含该原句的位置；核验TXT行号 3193 | The unit of analysis is the matched (backbone, task) cell. Each cell score is the mean of the four LLM judges’ Overall scores, and because the three systems share the same 30 cells, task and backbone variation cancels within pairs. We test the mean Overall difference with a paired sign-flip permutation test using 100,000 random sign assignments (two-sided). Table 12 summarizes the results: YouRA leads MLR-Agent by +0.85+0.85 (p=0.006p{=}0.006) and AI Scientist V2 by +0.64+0.64 (p=0.044p{=}0.044), with both comparisons still significant under Holm correction (adjusted p=0.012p{=}0.012 and 0.0440.044). The per-backbone mean differences are positive across all three backbones for both comparisons, so no single backbone drives the result. Cells sharing a backbone are not fully independent; the permutation runs at the cell level, not on individual judge verdicts, which avoids treating the 120 judge scores as independent samples. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

YouRA 提出支持持久状态和证据追踪的自主研究架构，整合Verification State Architecture、独立控制器和执行Agent，跨研究过程保存假设、门控、证据指针、执行证据与失败历史。论文在来自近期ICLR、ICML和NeurIPS workshop的 201 项任务上评估，任务由 MLR-Bench 归入九个机器学习主题。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。YouRA 提出支持持久状态和证据追踪的自主研究架构，整合Verification State Architecture、独立控制器和执行Agent，跨研究过程保存假设、门控、证据指针、执行证据与失败历史。论文在来自近期ICLR、ICML和NeurIPS workshop的 201 项任务上评估，任务由 MLR-Bench 归入九个机器学习主题。
  - 原文位置：本地全文：ASD-0934中与研究目标/科学问题直接相关的原文句子；核验TXT行号 398；引文：End-to-end research agents can now produce complete scientific papers, yet manuscript claims often diverge from executed experiments. This gap is structural: research state, failure histories, and claim–evidence alignment are not maintained as persistent, verifiable state across long-horizon pipelines. We present YouRA (Your Research Agent), an architecture for stateful, evidence-traceable autonomous research. YouRA preserves research state, execution evidence, and failure history across the research trajectory by integrating three components: a Verification State Architecture (VSA) that tracks hypotheses, gates, and evidence pointers; an Independent Controller that turns state and reflection records into lifecycle, recovery, and debate/review control while separating control from execution; and Stateful Reflection that logs failures as structured lessons and routes recovery through bounded repair, redesign, or reset. On MLR-Bench’s predefined ten-task end-to-end subset, YouRA improves over both MLR-Agent and AI Scientist V2 on scalar Overall across all three matched backbones. An automated diagnostic using MLR-Bench’s hallucination taxonomy reports intersection/union counts for four fact-based failure types, and data-provenance diagnostic shows more real-data-based outputs. Ablating each of the four components (the VSA, the Independent Controller, MCP tool access, and reflection-guided recovery) supports their separable contributions. Removing either core-state component drops YouRA below the full system. Code: https://github.com/PrayPrey/Your-Research-Agent.
- 多步行动过程：yes。VSA记录假设、门控和证据指针；控制器读取状态并分配或恢复工作；执行Agent运行工具并写回结果与失败证据，供后续阶段和审查使用。
  - 原文位置：本地全文：ASD-0934中与多步行动/研究流程直接相关的原文句子；核验TXT行号 2351；引文：The Independent Controller turns VSA records into stage transitions, recovery choices, and persona selection, making persistent state an active control surface rather than a passive log. It runs in an independent LLM context decoupled from the task-execution agent; in our implementation, this controller is GPT-5.2 OpenAI (2025), accessed through OpenRouter API. At each step it reads only two inputs: a compact summary of the current VSA and the most recent per-stage artifact pointer. Because the controller never sees the full execution trace, its context does not grow with the pipeline length, and its routing decisions are less directly exposed to the task-execution agent’s internal reasoning. The same Independent Controller is reused in Hypothesis Debate, where it selects personas and judges convergence; in Adversarial Fact Review, the independent critics are the reviewer personas, which run as context-isolated task agents of the backbone LLM, while the controller’s Stop hook handles only round-to-round continuation. Operationally, the controller’s per-stage output is consumed by a Stop hook that either approves termination, emits a resume prompt back to the task-execution LLM, or escalates a MUST_STOP signal when human intervention is required.
- 至少一种Agent能力：yes。YouRA由VSA状态层、独立控制器和工具型执行Agent组成，维护研究状态及证据轨迹，支持跨会话恢复、工作分配与独立审查。
  - 原文位置：本地全文：ASD-0934中与Agent实现与能力直接相关的原文句子；核验TXT行号 398；引文：YouRA preserves research state, execution evidence, and failure history across the research trajectory by integrating three components: a Verification State Architecture (VSA) that tracks hypotheses, gates, and evidence pointers; an Independent Controller that turns state and reflection records into lifecycle, recovery, and debate/review control while separating control from execution; and Stateful Reflection that logs failures as structured lessons and routes recovery through bounded repair, redesign, or reset.
- 明确科研流程角色：yes。评估涉及 201 项来自近期ICLR/ICML/NeurIPS workshop的任务，覆盖MLR-Bench九个核心机器学习主题；与论文列出的Agent基线比较。
  - 原文位置：本地全文：ASD-0934中与实验任务与验证设置直接相关的原文句子；核验TXT行号 785；引文：We evaluate on MLR-Bench Chen et al. (2026), a benchmark for open-ended ML research agents that provides 201 workshop-derived research tasks, MLR-Judge rubrics, and the MLR-Agent baseline pipeline for idea generation, proposal formulation, experimentation, and paper writing. The 201 tasks are sourced from recent ICLR/ICML/NeurIPS workshops and are categorized by MLR-Bench into nine core ML topics: LLMs and Vision-Language Models, AI for Science, ML Theory, Trustworthy AI, Computer Vision, ML Systems, Multimodality, Reinforcement Learning, and other emerging topics. End-to-end and pairwise paper-level evaluation use the predefined ten-task subset specified by MLR-Bench (Table 1 and Table 2). As supplementary upstream context on the full task pool, Appendix Table 13 compares YouRA and MLR-Agent on Idea/Proposal-stage quality across all 201 tasks.

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

YouRA由VSA状态层、独立控制器和工具型执行Agent组成，维护研究状态及证据轨迹，支持跨会话恢复、工作分配与独立审查。

### 3.3 自主能力

YouRA由VSA状态层、独立控制器和工具型执行Agent组成，维护研究状态及证据轨迹，支持跨会话恢复、工作分配与独立审查。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

系统贡献是以持久状态及证据指针维持研究连续性，并以独立控制器将任务分配、恢复和检查与执行隔离。

### 4.2 系统流程与组件

VSA记录假设、门控和证据指针；控制器读取状态并分配或恢复工作；执行Agent运行工具并写回结果与失败证据，供后续阶段和审查使用。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

评估涉及 201 项来自近期ICLR/ICML/NeurIPS workshop的任务，覆盖MLR-Bench九个核心机器学习主题；与论文列出的Agent基线比较。

### 5.2 基线、指标与结果

作者报告YouRA在所设任务集上的研究推进和证据追踪指标；表现应结合201项任务及各项基线设置理解。

### 5.3 科学贡献与证据强度

系统贡献是以持久状态及证据指针维持研究连续性，并以独立控制器将任务分配、恢复和检查与执行隔离。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

论文以“YouRA: A Persistent-State Architecture for Evidence-Traceable Autonomous Research Agents”对应的研究任务为对象，具体与哪些既有系统或基准比较，应结合其正文相关工作和实验基线判断；不把工具名称直接视为科学对象。

## 7. 局限性与风险

任务来自机器学习研讨会问题，无法代表所有科学学科；持久记录也不能保证被记录的实验结论本身正确。

## 8. 对综述写作的价值

可用于综述“YouRA: A Persistent-State Architecture for Evidence-Traceable Autonomous Research Agents”所涉及的Agent任务、研究流程和验证方式；其证据边界为本论文实际报告的任务集与实验结果。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

YouRA以持久状态、证据指针和独立控制器支持可追溯的自主研究。

### 9.2 速记版 pipeline

VSA记录假设、门控和证据指针；控制器读取状态并分配或恢复工作；执行Agent运行工具并写回结果与失败证据，供后续阶段和审查使用。

### 9.3 标注字段汇总

```text
paper_id=ASD-0934
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
| 问题开放度 | O2 既定基准 | 在MLR-Bench的201项workshop任务上评估，任务预先定义 | “201 workshop-derived research tasks” · L42 |
| 验证强度 | V1 基准/内部评测 | 使用MLR-Judge rubrics评分并与基线比较Overall得分 | “MLR-Bench Chen et al. (2026), a benchmark” · L42 |
| 系统自主性 | L2 闭环执行者 | 系统跨会话保持研究状态并自主分配工作，形成持久闭环 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
