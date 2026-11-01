# SAIL: Scientific Agentic Intelligence via a Science-Aware Loop

**论文信息**

- ID：ASD-1097
- 标题：SAIL: Scientific Agentic Intelligence via a Science-Aware Loop
- 作者：SAIL Model Team; Boyuan Sun; Bryan Dai; Che Liu; Chi Liu; Derek Li; Hongming Piao; Mengzhuo Chen; Xidong Wang; Yan Shu; Yinda Chen; Ziyang Zeng
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2610.11451
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1097.txt
- PDF / 本地文件路径：全文已缓存；PDF尚未归档，详见资料清单
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 研究对象与任务 | SAIL是面向文献研究、科学编程和多步研究工作流的开放模型。作者提出science-aware improvement loop：由前沿模型驱动的代理分析失败案例，按文献检索与证据筛选、科学编程假设及长程规划等能力缺口构造训练任务，再用交互轨迹改进模型。论文重点是科学代理模型的训练与通用能力提升。 | 全文TXT第281行；核验TXT行号 281 | We introduce SAIL, an open model with 35B total and 3B active parameters for literature research, scientific coding, and multi-step research workflows. | 高（一手正文；非独立复现） |
| 系统输入及处理流程 | 系统在文献、代码仓库和研究任务中运行代理，分析任务失败并生成针对性问题、交互轨迹和训练数据；所得数据用于模型训练，再评估科学任务表现。 | 全文TXT第1128行；核验TXT行号 1128 | The comparison includes its base model, five other 35B models, and eight larger models ranging from 124B to 1.6T total parameters. | 高（一手正文；非独立复现） |
| 实验或验证设置 | 系统在文献、代码仓库和研究任务中运行代理，分析任务失败并生成针对性问题、交互轨迹和训练数据；所得数据用于模型训练，再评估科学任务表现。 | 全文TXT第1175行；核验TXT行号 1175 | data analysis, and end-to-end discovery. Higher scores are better. | 高（一手正文；非独立复现） |
| 作者报告的贡献 | 验证涉及文献检索、科学编码与多步工作流任务，并与基线模型比较；具体数值以论文报告为准。 | 全文TXT第2295行；核验TXT行号 2295 | Table 2: Additional benchmark results on scientific coding and research. | 高（一手正文；非独立复现） |
| 适用范围与边界 | 方法贡献以科学代理能力训练为主，跨多个学科任务而未锁定单一科学对象；可列01通用方法，11是否作为科学工作流模块需依据具体运行任务证据复核，因此保留needs_review。 | 全文TXT第2788行；核验TXT行号 2788 | Names within each group are listed alphabetically by first name. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

SAIL是面向文献研究、科学编程和多步研究工作流的开放模型。作者提出science-aware improvement loop：由前沿模型驱动的代理分析失败案例，按文献检索与证据筛选、科学编程假设及长程规划等能力缺口构造训练任务，再用交互轨迹改进模型。论文重点是科学代理模型的训练与通用能力提升。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。面向真实科研文献、实验观测或可执行计算研究任务，科研目标明确。
  - 原文位置：1 Introduction; local TXT line 442；核验TXT行号 442；引文：We introduce SAIL, an open model for literature retrieval and synthesis, scientific coding, and research workflows involving tool use.
- 多步行动过程：yes。正文描述多阶段研究或逐步工具调用，允许中间结果参与后续行动。
  - 原文位置：2.1 Diagnosing Capability Gaps; local TXT line 585；核验TXT行号 585；引文：The agents examine how the model carries an investigation from information gathering through implementation, experimentation, and analysis.
- 至少一种Agent能力：yes。具备工具调用、状态保持和依据反馈选择后续行动的能力。
  - 原文位置：4.2 Scientific Execution and Trajectory Collection; local TXT line 958；核验TXT行号 958；引文：Persistent runtimes retain their state across tool calls, allowing generated code, intermediate files, numerical results, and other artifacts to remain available throughout an episode.
- 明确科研流程角色：yes。承担科研资料分析、计算或证据解释等局部研究角色；不要求完成整条发现闭环。
  - 原文位置：5 Evaluation and Analysis; local TXT line 1094；核验TXT行号 1094；引文：on scientific literature, coding, data analysis, and research workflows.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：01;11
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：01（仅归档，不覆盖其他模块）
- 模块内分类路径：01.02.12 人工智能；11.07.08 科学方法论
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

实际任务涵盖文献检索/综合、科学代码、仓库执行与计算复现、数据分析、报告及端到端研究工作流。01对应Agent模型与计算科研任务的验证，11.07对应科学知识生产与研究报告评测；没有逐项对象证据的其他学科不据基准名称扩展。

### 2.3 容易混淆的边界

实际任务涵盖文献检索/综合、科学代码、仓库执行与计算复现、数据分析、报告及端到端研究工作流。01对应Agent模型与计算科研任务的验证，11.07对应科学知识生产与研究报告评测；没有逐项对象证据的其他学科不据基准名称扩展。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签



### 3.2 科研流程角色



系统在文献、代码仓库和研究任务中运行代理，分析任务失败并生成针对性问题、交互轨迹和训练数据；所得数据用于模型训练，再评估科学任务表现。

### 3.3 自主能力

具备工具调用、状态保持和依据反馈选择后续行动的能力。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

方法贡献以科学代理能力训练为主，跨多个学科任务而未锁定单一科学对象；可列01通用方法，11是否作为科学工作流模块需依据具体运行任务证据复核，因此保留needs_review。

### 4.2 系统流程与组件

系统在文献、代码仓库和研究任务中运行代理，分析任务失败并生成针对性问题、交互轨迹和训练数据；所得数据用于模型训练，再评估科学任务表现。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

系统在文献、代码仓库和研究任务中运行代理，分析任务失败并生成针对性问题、交互轨迹和训练数据；所得数据用于模型训练，再评估科学任务表现。 验证以文中所列任务、数据和对照为准。

### 5.2 基线、指标与结果

验证涉及文献检索、科学编码与多步工作流任务，并与基线模型比较；具体数值以论文报告为准。

### 5.3 科学贡献与证据强度

方法贡献以科学代理能力训练为主，跨多个学科任务而未锁定单一科学对象；可列01通用方法，11是否作为科学工作流模块需依据具体运行任务证据复核，因此保留needs_review。

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

SAIL是面向文献研究、科学编程和多步研究工作流的开放模型。作者提出science-aware improvement loop：由前沿模型驱动的代理分析失败案例，按文献检索与证据筛选、科学编程假设及长程规划等能力缺口构造训练任务，再用交互轨迹改进模型。论文重点是科学代理模型的训练与通用能力提升。

### 9.2 速记版 pipeline

系统在文献、代码仓库和研究任务中运行代理，分析任务失败并生成针对性问题、交互轨迹和训练数据；所得数据用于模型训练，再评估科学任务表现。

### 9.3 标注字段汇总

```text
paper_id=ASD-1097
inclusion_status=to_read
scientific_object_modules=01;11
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=01
module_taxonomy_codes=01.02.12;11.07.08
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 PR剩余差异复核

- 来源深度：`verified_official_pdf_fulltext`。本轮涉及4条差异，其中2条已判定，2条待核。摘要或图注支持的判定不代表全文已逐页核验。

- 原1664行号 `1637`：`pending_evidence`。The complete PDF confirms model training and scientific-assistance benchmarks. Whether general literature retrieval/synthesis, repository reproduction, and research workflows independently establish scientific methodology (11.07.08) remains unresolved. Benchmark names alone justify neither retaining nor deleting module 11. Do not write back an automatic change.
  - 位置：PDF p.1 abstract; p.4 failure diagnosis; pp.11?14 evaluation/discussion；来源：https://arxiv.org/abs/2610.11451

- 原1664行号 `1638`：`reject_pr`。The original PDF studies training and improvement of the SAIL AI model. The current 01.02 computer-science category applies; the PR deletion relies on an outdated absence of taxonomy entries.
  - 位置：PDF p.1 abstract; p.4 failure diagnosis; pp.11?14 evaluation/discussion；来源：https://arxiv.org/abs/2610.11451

- 原1664行号 `1639`：`reject_pr`。SAIL training, failure-guided task construction, and comparative model evaluation directly support the current artificial-intelligence category (01.02.12). Do not clear the code.
  - 位置：PDF p.1 abstract; p.4 failure diagnosis; pp.11?14 evaluation/discussion；来源：https://arxiv.org/abs/2610.11451

- 原1664行号 `1640`：`pending_evidence`。The original PDF establishes an AI research-model goal, diagnosis/task construction/training/evaluation stages, planning/revision/tool-interaction capabilities, and a scientific-assistant workflow role. Module 01 is substantiated, but the combined 01+11 assignment remains unresolved because the scientific-object boundary for module 11 still needs a decision.
  - 位置：PDF p.1 abstract; p.4 failure diagnosis; pp.11?14 evaluation/discussion；来源：https://arxiv.org/abs/2610.11451

逐条引文、来源文件和限制见 `Coverage_Check/pr1_82_recheck_2026-10-29/final_review.json`。保留现有分类不等于全部分类边界已消除。
