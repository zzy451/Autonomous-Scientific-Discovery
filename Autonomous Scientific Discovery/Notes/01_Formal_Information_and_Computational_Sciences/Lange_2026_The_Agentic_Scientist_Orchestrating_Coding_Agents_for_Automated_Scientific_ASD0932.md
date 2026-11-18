# The Agentic Scientist: Orchestrating Coding Agents for Automated Scientific (Co-)Discovery

**论文信息**

- ID：ASD-0932
- 标题：The Agentic Scientist: Orchestrating Coding Agents for Automated Scientific (Co-)Discovery
- 作者：Robert Tjarko Lange; Luca Grillotti; Yutaro Yamada; Rujikorn Charakorn; David Ha
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2610.18933
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0932.txt
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Lange_2026_The_Agentic_Scientist_Orchestrating_Coding_Agents_for_Automated_Scientific_ASD0932.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 研究目标/科学问题 | The Agentic Scientist 将多个编码Agent编排为自动科研流程，覆盖文献检索、构思、规划、沙盒实验、基线、消融、分析与写作，并用rubric检查及元控制器管理执行。论文展示AI研究与开放式架构研究案例，重点考察系统能否形成可验证的科学发现及论文。 | 本地全文：ASD-0932中与研究目标/科学问题直接相关的原文句子；核验TXT行号 553 | Modern coding agents are fundamentally reshaping the role of human input for computational research: they write code, launch in silico experiments, analyze their results, and autonomously operate with ever-increasing time horizons. Despite these developments, fully autonomous research agents suffer from a limited ‘ideation radius’ and myopic hill-climbing search dynamics. To bridge this gap, we introduce The Agentic Scientist, an end-to-end distributed pipeline for human researchers to conduct computational research alongside modern coding agents. Building on its predecessor (Lu et al., 2026, The AI Scientist,), our system decomposes research into task drafting, idea generation, planning, sandboxed experimentation, result aggregation, baseline and ablation construction, post-hoc analysis, and report writing. Importantly, each step in the pipeline is powered by the next generation of headless coding agents and leverages agentic self-verification. The overall research process is driven by a meta-controller that manages parallel research agents and enforces rubric verification at each stage. This design enables the same orchestration layer to be reused across heterogeneous domains with different execution environments, agentic coding harnesses, and evaluation metrics. Our system can be used across a spectrum of autonomy: either as a co-scientist tool, or to perform end-to-end scientific investigation. Within the co-scientist setting, we leveraged a development version of our system to submit a single research paper, which got accepted for publication at ALIFE 2026 (Yamada et al., 2026). We further apply The Agentic Scientist fully autonomously to open problem-solving tasks in machine learning, and demonstrate the system’s capability of scientific discovery across different domains of computational research, including: a hypernetwork-based inductive bias for rapid Transformer adaptation and a meta-trained evolution strategy that matches or exceeds CMA-ES on 5 of 7 unseen Brax control tasks. Our ablations suggest that reliable scientific autonomy depends not only on base model capabilities, but also on the cross-agent orchestration layer. We open-source The Agentic Scientist and its figure generation tool, autoillustrate, to aid collective development of automated (co-)scientist systems: | 高（一手正文；非独立复现） |
| 多步行动/研究流程 | 系统检索相关文献、提出研究构想和实验计划，在沙盒运行实验与基线/消融，分析结果并写论文；rubric和元控制器检查流程质量。 | 本地全文：ASD-0932中与多步行动/研究流程直接相关的原文句子；核验TXT行号 556 | Building on its predecessor (Lu et al., 2026, The AI Scientist,), our system decomposes research into task drafting, idea generation, planning, sandboxed experimentation, result aggregation, baseline and ablation construction, post-hoc analysis, and report writing. | 高（一手正文；非独立复现） |
| Agent实现与能力 | The Agentic Scientist 是由编码Agent协作的科研系统，含文献检索、ideation、执行、消融、任务起草和写作等专门角色，并由元控制器编排。 | 本地全文：ASD-0932中与Agent实现与能力直接相关的原文句子；核验TXT行号 555 | To bridge this gap, we introduce The Agentic Scientist, an end-to-end distributed pipeline for human researchers to conduct computational research alongside modern coding agents. | 高（一手正文；非独立复现） |
| 实验任务与验证设置 | 作者以自动AI研究任务和开放式架构研究案例展示流程，报告具体实验、消融和生成论文；其证据限于论文给出的案例设置。 | 本地全文：ASD-0932中与实验任务与验证设置直接相关的原文句子；核验TXT行号 1521 | Figure 10: (Left) Search trajectories for Doc-to-LoRA scientist runs given 40 idea iteration budget with Codex + GPT-5.6-Sol, Claude + Opus-5, and Pi + DeepSeek-V4-Pro on the multi-NIAH task. Both Codex and Claude runs improve steadily on the task. (Right) Exact-match accuracy is shown as a heatmap grouped by the number of test sample needles. Red crosses indicate invalid iterations. | 高（一手正文；非独立复现） |
| 作者报告的结果/贡献 | 正文案例展示系统可完成从构想到论文的长程科研工作流；对单个案例的结果不应解释为对所有科学任务均可自主发现。 贡献在于将编码Agent组织成覆盖研究全过程的协作流程，并以检查机制支持科研产物生成。 | 本地全文中包含该原句的位置；核验TXT行号 1597 | Figure 11: Doc-to-LoRA composition mechanism ablations figure in the generated report (Section C.1). (a) Hypernetwork’s head redesign, auxiliary objective, and unconditional merging stay at or below the 51.7%51.7\% exact-match accuracy, while query-conditioned composition reaches 98.0%98.0\%. (b) Starting from the query-blind (unconditional) merge, query-dependent merging provides a significant improvement; relevance-based text placement and delimiter-aligned chunking close the remaining gap. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

The Agentic Scientist 将多个编码Agent编排为自动科研流程，覆盖文献检索、构思、规划、沙盒实验、基线、消融、分析与写作，并用rubric检查及元控制器管理执行。论文展示AI研究与开放式架构研究案例，重点考察系统能否形成可验证的科学发现及论文。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。The Agentic Scientist 将多个编码Agent编排为自动科研流程，覆盖文献检索、构思、规划、沙盒实验、基线、消融、分析与写作，并用rubric检查及元控制器管理执行。论文展示AI研究与开放式架构研究案例，重点考察系统能否形成可验证的科学发现及论文。
  - 原文位置：本地全文：ASD-0932中与研究目标/科学问题直接相关的原文句子；核验TXT行号 553；引文：Modern coding agents are fundamentally reshaping the role of human input for computational research: they write code, launch in silico experiments, analyze their results, and autonomously operate with ever-increasing time horizons. Despite these developments, fully autonomous research agents suffer from a limited ‘ideation radius’ and myopic hill-climbing search dynamics. To bridge this gap, we introduce The Agentic Scientist, an end-to-end distributed pipeline for human researchers to conduct computational research alongside modern coding agents. Building on its predecessor (Lu et al., 2026, The AI Scientist,), our system decomposes research into task drafting, idea generation, planning, sandboxed experimentation, result aggregation, baseline and ablation construction, post-hoc analysis, and report writing. Importantly, each step in the pipeline is powered by the next generation of headless coding agents and leverages agentic self-verification. The overall research process is driven by a meta-controller that manages parallel research agents and enforces rubric verification at each stage. This design enables the same orchestration layer to be reused across heterogeneous domains with different execution environments, agentic coding harnesses, and evaluation metrics. Our system can be used across a spectrum of autonomy: either as a co-scientist tool, or to perform end-to-end scientific investigation. Within the co-scientist setting, we leveraged a development version of our system to submit a single research paper, which got accepted for publication at ALIFE 2026 (Yamada et al., 2026). We further apply The Agentic Scientist fully autonomously to open problem-solving tasks in machine learning, and demonstrate the system’s capability of scientific discovery across different domains of computational research, including: a hypernetwork-based inductive bias for rapid Transformer adaptation and a meta-trained evolution strategy that matches or exceeds CMA-ES on 5 of 7 unseen Brax control tasks. Our ablations suggest that reliable scientific autonomy depends not only on base model capabilities, but also on the cross-agent orchestration layer. We open-source The Agentic Scientist and its figure generation tool, autoillustrate, to aid collective development of automated (co-)scientist systems:
- 多步行动过程：yes。系统检索相关文献、提出研究构想和实验计划，在沙盒运行实验与基线/消融，分析结果并写论文；rubric和元控制器检查流程质量。
  - 原文位置：本地全文：ASD-0932中与多步行动/研究流程直接相关的原文句子；核验TXT行号 556；引文：Building on its predecessor (Lu et al., 2026, The AI Scientist,), our system decomposes research into task drafting, idea generation, planning, sandboxed experimentation, result aggregation, baseline and ablation construction, post-hoc analysis, and report writing.
- 至少一种Agent能力：yes。The Agentic Scientist 是由编码Agent协作的科研系统，含文献检索、ideation、执行、消融、任务起草和写作等专门角色，并由元控制器编排。
  - 原文位置：本地全文：ASD-0932中与Agent实现与能力直接相关的原文句子；核验TXT行号 555；引文：To bridge this gap, we introduce The Agentic Scientist, an end-to-end distributed pipeline for human researchers to conduct computational research alongside modern coding agents.
- 明确科研流程角色：yes。作者以自动AI研究任务和开放式架构研究案例展示流程，报告具体实验、消融和生成论文；其证据限于论文给出的案例设置。
  - 原文位置：本地全文：ASD-0932中与实验任务与验证设置直接相关的原文句子；核验TXT行号 1521；引文：Figure 10: (Left) Search trajectories for Doc-to-LoRA scientist runs given 40 idea iteration budget with Codex + GPT-5.6-Sol, Claude + Opus-5, and Pi + DeepSeek-V4-Pro on the multi-NIAH task. Both Codex and Claude runs improve steadily on the task. (Right) Exact-match accuracy is shown as a heatmap grouped by the number of test sample needles. Red crosses indicate invalid iterations.

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

The Agentic Scientist 是由编码Agent协作的科研系统，含文献检索、ideation、执行、消融、任务起草和写作等专门角色，并由元控制器编排。

### 3.3 自主能力

The Agentic Scientist 是由编码Agent协作的科研系统，含文献检索、ideation、执行、消融、任务起草和写作等专门角色，并由元控制器编排。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

贡献在于将编码Agent组织成覆盖研究全过程的协作流程，并以检查机制支持科研产物生成。

### 4.2 系统流程与组件

系统检索相关文献、提出研究构想和实验计划，在沙盒运行实验与基线/消融，分析结果并写论文；rubric和元控制器检查流程质量。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

作者以自动AI研究任务和开放式架构研究案例展示流程，报告具体实验、消融和生成论文；其证据限于论文给出的案例设置。

### 5.2 基线、指标与结果

正文案例展示系统可完成从构想到论文的长程科研工作流；对单个案例的结果不应解释为对所有科学任务均可自主发现。

### 5.3 科学贡献与证据强度

贡献在于将编码Agent组织成覆盖研究全过程的协作流程，并以检查机制支持科研产物生成。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

论文以“The Agentic Scientist: Orchestrating Coding Agents for Automated Scientific (Co-)Discovery”对应的研究任务为对象，具体与哪些既有系统或基准比较，应结合其正文相关工作和实验基线判断；不把工具名称直接视为科学对象。

## 7. 局限性与风险

案例任务和模型配置有限；生成稿件及通过rubric检查本身不能替代独立复现或领域专家对科学新颖性的确认。

## 8. 对综述写作的价值

可用于综述“The Agentic Scientist: Orchestrating Coding Agents for Automated Scientific (Co-)Discovery”所涉及的Agent任务、研究流程和验证方式；其证据边界为本论文实际报告的任务集与实验结果。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

The Agentic Scientist 编排编码Agent完成从文献构思到实验分析和写作的科研流程。

### 9.2 速记版 pipeline

系统检索相关文献、提出研究构想和实验计划，在沙盒运行实验与基线/消融，分析结果并写论文；rubric和元控制器检查流程质量。

### 9.3 标注字段汇总

```text
paper_id=ASD-0932
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
| 问题开放度 | O2 既定基准 | 系统在AI研究任务和开放式架构研究案例中展示，但评测基于预设场景 | “open problem-solving tasks in machine learning” · L36 |
| 验证强度 | V1 基准/内部评测 | 通过rubric检查和案例展示评估，未涉及独立复现 | “Importantly, each step in the pipeline is powered by the next generation” · L36 |
| 系统自主性 | L2 闭环执行者 | 系统协调多Agent完成从文献到实验到写作的研究流程闭环 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
