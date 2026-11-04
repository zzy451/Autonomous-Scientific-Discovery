# SGHA: Evidence-Grounded Research Problem Discovery with Local Language Models

**论文信息**

- ID：ASD-0924
- 标题：SGHA: Evidence-Grounded Research Problem Discovery with Local Language Models
- 作者：Sarvesh Gharat; Junpei Komiyama
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2608.17501
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0924.txt
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Gharat_2026_SGHA_Evidence_Grounded_Research_Problem_Discovery_with_Local_Language_ASD0924.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 研究目标/科学问题 | 本文提出 SGHA，从有界论文语料构建证据图，寻找结构性研究缺口并将其整理为可审计的问题表述。实验覆盖 bandits、上下文学习、推理与测试时计算、离线强化学习和不确定性估计五个机器学习领域。作者报告从 1,250 篇入选论文中抽取 1,044 篇结构化内容，经核验保留 39 个候选缺口并形成 15 个项目族；与 AI-Scientist-v2 的对比属于系统级比较。 | 本地全文：ASD-0924中与研究目标/科学问题直接相关的原文句子；核验TXT行号 945 | We evaluate SGHA as a system for producing research-problem formulations from scientific papers. The experiments are organized around three questions. First, can SGHA produce final project-family artifacts across different areas of machine learning? Second, how do these artifacts compare with outputs from automated ideation baselines under a common formulation-quality rubric? Third, how does the system behave in additional settings, including profile-conditioned generation, evolutionary exploration, and Bandits sensitivity analyses over model size and corpus size? | 高（一手正文；非独立复现） |
| 多步行动/研究流程 | 系统从论文抽取结构化证据并构建类型化图，识别结构模式和候选缺口，经过验证后将缺口组织成项目族，再生成形式化研究问题。 | 本地全文：ASD-0924中与多步行动/研究流程直接相关的原文句子；核验TXT行号 725 | SGHA then inserts the validated paper objects and evidence tuples into a typed evidence multigraph. The graph has different kinds of nodes for different scientific objects. Paper nodes represent source papers, while other nodes represent methods, assumptions, limitations, failure conditions, claims, tasks, datasets, metrics, and results. The edges come from the extracted tuples. For example, an edge may state that a method assumes an assumption, fails_under a condition, or is measured_by a metric. Each edge keeps its source provenance, including the paper identifier and supporting evidence span. Thus, the graph is not just a citation graph or a collection of paper summaries. It records the scientific relations that SGHA extracted from the corpus: what methods assume, where they are evaluated, what they improve over, where they fail, and which limitations remain unresolved. | 高（一手正文；非独立复现） |
| Agent实现与能力 | SGHA 使用冻结的本地 Qwen/Qwen3.5-9B 模型生成研究问题，通过证据抽取、图结构组织、缺口筛选与验证、项目族归纳形成问题表述。 | 本地全文：ASD-0924中与Agent实现与能力直接相关的原文句子；核验TXT行号 477 | We introduce the Structural Gap Hypothesis Agent (SGHA), a fully automated, corpus-first research-problem discovery system that runs entirely on a local LLM. SGHA structures a scientific literature corpus into evidence-linked paper objects and a typed evidence graph, detects unresolved structural patterns across papers, screens candidate gaps before formulation, and produces traceable research-problem families. In particular, it is able to output assumptions, objectives, success criteria, and remaining ambiguities. All LLM-based components of SGHA are executed using a locally served open-weight 9B language model, without requiring proprietary frontier-model APIs. We compare SGHA with the AI Scientist-v2 idea formulation module in five machine-learning domains. Our results suggest that explicit corpus structure and evidence-constrained reasoning can support promising, inspectable research-problem formulation without relying on frontier models during generation or verification. | 高（一手正文；非独立复现） |
| 实验任务与验证设置 | 实验覆盖五个机器学习领域及 1,250 篇筛选论文；作者以五家不同提供方的前沿模型进行方法标签遮蔽评审，并与同模型的 AI-Scientist-v2 ideation 工作流比较。 | 本地全文：ASD-0924中与实验任务与验证设置直接相关的原文句子；核验TXT行号 575 | We evaluate SGHA across five machine-learning domains: bandits, in-context learning, reasoning and test-time computation, offline reinforcement learning, and uncertainty estimation. The main experiments use a frozen local Qwen/Qwen3.5-9B model for generation, with no task-specific training or fine-tuning. Across 1,250 selected papers, SGHA extracts structured content from 1,044 papers. After verification, 39 candidate gaps remain and lead to 15 formalized project families. Our primary comparison is with the AI-Scientist-v2 ideation workflow configured with the same local model and matched output counts. This is a system-level comparison rather than an information-matched ablation: SGHA uses the bounded corpus, whereas the AI-Scientist-v2 retains its Semantic Scholar retrieval. Since SGHA is meant to write research-problem formulations rather than full project plans, we evaluate the comparison with a formulation-only rubric. Under this rubric, a method-label-masked evaluation using five frontier-model judges from different providers assigns SGHA higher mean scores on all but one of the formulation-quality criteria, including well-posedness, assumption-boundary clarity, formalizability, source-grounded specificity, and ambiguity handling. The local AI-Scientist-v2 baseline receives a higher mean score only on scope control, consistent with its tendency to produce narrower proposal-style ideas. The hosted judges are used only for post hoc evaluation after the candidate outputs have been frozen and are not part of SGHA’s generation or verification pipeline. Additional comparisons using Claude Opus in the AI-Scientist-v2 workflow and the public MOOSE-Star HC model [12] were conducted. In the Claude Opus diagnostic, which matches retained output counts but not compute or information budgets, SGHA receives a competitive numerical mean score on overall formulation quality to AI-Scientist-v2 with Claude Opus. | 高（一手正文；非独立复现） |
| 作者报告的结果/贡献 | 正文报告抽取 1,044 篇论文、验证后保留 39 个候选缺口并形成 15 个项目族。SGHA 在问题表述质量的大多数维度均值较高；作者明确说明该对比是系统级比较而非信息匹配消融。 科学贡献是提出以文献证据结构为基础的研究问题发现流程；系统贡献是 SGHA 的图构建、缺口验证和问题形式化机制。 | 本地全文中包含该原句的位置；核验TXT行号 575 | After verification, 39 candidate gaps remain and lead to 15 formalized project families. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

本文提出 SGHA，从有界论文语料构建证据图，寻找结构性研究缺口并将其整理为可审计的问题表述。实验覆盖 bandits、上下文学习、推理与测试时计算、离线强化学习和不确定性估计五个机器学习领域。作者报告从 1,250 篇入选论文中抽取 1,044 篇结构化内容，经核验保留 39 个候选缺口并形成 15 个项目族；与 AI-Scientist-v2 的对比属于系统级比较。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。本文提出 SGHA，从有界论文语料构建证据图，寻找结构性研究缺口并将其整理为可审计的问题表述。实验覆盖 bandits、上下文学习、推理与测试时计算、离线强化学习和不确定性估计五个机器学习领域。作者报告从 1,250 篇入选论文中抽取 1,044 篇结构化内容，经核验保留 39 个候选缺口并形成 15 个项目族；与 AI-Scientist-v2 的对比属于系统级比较。
  - 原文位置：本地全文：ASD-0924中与研究目标/科学问题直接相关的原文句子；核验TXT行号 945；引文：We evaluate SGHA as a system for producing research-problem formulations from scientific papers. The experiments are organized around three questions. First, can SGHA produce final project-family artifacts across different areas of machine learning? Second, how do these artifacts compare with outputs from automated ideation baselines under a common formulation-quality rubric? Third, how does the system behave in additional settings, including profile-conditioned generation, evolutionary exploration, and Bandits sensitivity analyses over model size and corpus size?
- 多步行动过程：yes。系统从论文抽取结构化证据并构建类型化图，识别结构模式和候选缺口，经过验证后将缺口组织成项目族，再生成形式化研究问题。
  - 原文位置：本地全文：ASD-0924中与多步行动/研究流程直接相关的原文句子；核验TXT行号 725；引文：SGHA then inserts the validated paper objects and evidence tuples into a typed evidence multigraph. The graph has different kinds of nodes for different scientific objects. Paper nodes represent source papers, while other nodes represent methods, assumptions, limitations, failure conditions, claims, tasks, datasets, metrics, and results. The edges come from the extracted tuples. For example, an edge may state that a method assumes an assumption, fails_under a condition, or is measured_by a metric. Each edge keeps its source provenance, including the paper identifier and supporting evidence span. Thus, the graph is not just a citation graph or a collection of paper summaries. It records the scientific relations that SGHA extracted from the corpus: what methods assume, where they are evaluated, what they improve over, where they fail, and which limitations remain unresolved.
- 至少一种Agent能力：yes。SGHA 使用冻结的本地 Qwen/Qwen3.5-9B 模型生成研究问题，通过证据抽取、图结构组织、缺口筛选与验证、项目族归纳形成问题表述。
  - 原文位置：本地全文：ASD-0924中与Agent实现与能力直接相关的原文句子；核验TXT行号 477；引文：We introduce the Structural Gap Hypothesis Agent (SGHA), a fully automated, corpus-first research-problem discovery system that runs entirely on a local LLM. SGHA structures a scientific literature corpus into evidence-linked paper objects and a typed evidence graph, detects unresolved structural patterns across papers, screens candidate gaps before formulation, and produces traceable research-problem families. In particular, it is able to output assumptions, objectives, success criteria, and remaining ambiguities. All LLM-based components of SGHA are executed using a locally served open-weight 9B language model, without requiring proprietary frontier-model APIs. We compare SGHA with the AI Scientist-v2 idea formulation module in five machine-learning domains. Our results suggest that explicit corpus structure and evidence-constrained reasoning can support promising, inspectable research-problem formulation without relying on frontier models during generation or verification.
- 明确科研流程角色：yes。实验覆盖五个机器学习领域及 1,250 篇筛选论文；作者以五家不同提供方的前沿模型进行方法标签遮蔽评审，并与同模型的 AI-Scientist-v2 ideation 工作流比较。
  - 原文位置：本地全文：ASD-0924中与实验任务与验证设置直接相关的原文句子；核验TXT行号 575；引文：We evaluate SGHA across five machine-learning domains: bandits, in-context learning, reasoning and test-time computation, offline reinforcement learning, and uncertainty estimation. The main experiments use a frozen local Qwen/Qwen3.5-9B model for generation, with no task-specific training or fine-tuning. Across 1,250 selected papers, SGHA extracts structured content from 1,044 papers. After verification, 39 candidate gaps remain and lead to 15 formalized project families. Our primary comparison is with the AI-Scientist-v2 ideation workflow configured with the same local model and matched output counts. This is a system-level comparison rather than an information-matched ablation: SGHA uses the bounded corpus, whereas the AI-Scientist-v2 retains its Semantic Scholar retrieval. Since SGHA is meant to write research-problem formulations rather than full project plans, we evaluate the comparison with a formulation-only rubric. Under this rubric, a method-label-masked evaluation using five frontier-model judges from different providers assigns SGHA higher mean scores on all but one of the formulation-quality criteria, including well-posedness, assumption-boundary clarity, formalizability, source-grounded specificity, and ambiguity handling. The local AI-Scientist-v2 baseline receives a higher mean score only on scope control, consistent with its tendency to produce narrower proposal-style ideas. The hosted judges are used only for post hoc evaluation after the candidate outputs have been frozen and are not part of SGHA’s generation or verification pipeline. Additional comparisons using Claude Opus in the AI-Scientist-v2 workflow and the public MOOSE-Star HC model [12] were conducted. In the Claude Opus diagnostic, which matches retained output counts but not compute or information budgets, SGHA receives a competitive numerical mean score on overall formulation quality to AI-Scientist-v2 with Claude Opus.

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

SGHA 使用冻结的本地 Qwen/Qwen3.5-9B 模型生成研究问题，通过证据抽取、图结构组织、缺口筛选与验证、项目族归纳形成问题表述。

### 3.3 自主能力

SGHA 使用冻结的本地 Qwen/Qwen3.5-9B 模型生成研究问题，通过证据抽取、图结构组织、缺口筛选与验证、项目族归纳形成问题表述。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

科学贡献是提出以文献证据结构为基础的研究问题发现流程；系统贡献是 SGHA 的图构建、缺口验证和问题形式化机制。

### 4.2 系统流程与组件

系统从论文抽取结构化证据并构建类型化图，识别结构模式和候选缺口，经过验证后将缺口组织成项目族，再生成形式化研究问题。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

实验覆盖五个机器学习领域及 1,250 篇筛选论文；作者以五家不同提供方的前沿模型进行方法标签遮蔽评审，并与同模型的 AI-Scientist-v2 ideation 工作流比较。

### 5.2 基线、指标与结果

正文报告抽取 1,044 篇论文、验证后保留 39 个候选缺口并形成 15 个项目族。SGHA 在问题表述质量的大多数维度均值较高；作者明确说明该对比是系统级比较而非信息匹配消融。

### 5.3 科学贡献与证据强度

科学贡献是提出以文献证据结构为基础的研究问题发现流程；系统贡献是 SGHA 的图构建、缺口验证和问题形式化机制。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

论文以“SGHA: Evidence-Grounded Research Problem Discovery with Local Language Models”对应的研究任务为对象，具体与哪些既有系统或基准比较，应结合其正文相关工作和实验基线判断；不把工具名称直接视为科学对象。

## 7. 局限性与风险

该工作生成研究问题表述而非完整项目计划；与 AI-Scientist-v2 的信息输入不匹配，因此不能将系统级比较解释成单一组件的因果效果。

## 8. 对综述写作的价值

可用于综述“SGHA: Evidence-Grounded Research Problem Discovery with Local Language Models”所涉及的Agent任务、研究流程和验证方式；其证据边界为本论文实际报告的任务集与实验结果。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

SGHA 以论文证据图发现并形式化研究缺口，覆盖五个机器学习领域。

### 9.2 速记版 pipeline

系统从论文抽取结构化证据并构建类型化图，识别结构模式和候选缺口，经过验证后将缺口组织成项目族，再生成形式化研究问题。

### 9.3 标注字段汇总

```text
paper_id=ASD-0924
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
| 问题开放度 | O2 既定基准 | 从有界论文语料识别研究缺口并形式化为问题表述，问题本身可由文献结构核对 | “寻找结构性研究缺口并将其整理为可审计的问题表述” · L29 |
| 验证强度 | V1 基准/内部评测 | 使用五家前沿模型的方法标签遮蔽评审对问题表述质量打分，属LLM-as-judge | “a method-label-masked evaluation using five frontier-model judges” · L42 |
| 系统自主性 | L1 任务助手 | 系统从文献抽取证据并生成研究问题表述，但不自主推进实验和验证 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
