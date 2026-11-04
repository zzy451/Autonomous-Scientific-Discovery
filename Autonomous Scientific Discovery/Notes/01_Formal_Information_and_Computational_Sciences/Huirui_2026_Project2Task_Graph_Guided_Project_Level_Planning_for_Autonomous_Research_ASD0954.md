# Project2Task: Graph-Guided Project-Level Planning for Autonomous Research

**论文信息**

- ID：ASD-0954
- 标题：Project2Task: Graph-Guided Project-Level Planning for Autonomous Research
- 作者：Xu, Huirui; Xu, Runtao; Ren, Shuo; Zhang, Jiajun
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2608.05225
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0954.txt
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Huirui_2026_Project2Task_Graph_Guided_Project_Level_Planning_for_Autonomous_Research_ASD0954.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 科学对象 | 论文将长程科研项目拆分为相互关联的可执行研究任务。 | 本地原文 TXT 第290行；核验TXT行号 290 | Research agents are increasingly able to search the literature, propose hypotheses, generate code, run experiments, and draft manuscripts from a single topic. Yet a research project is not simply a larger task: it is a long-horizon research agenda that must be advanced through multiple bounded tasks with distinct but related research objectives. These tasks may explore alternative approaches to the project in parallel or address successive challenges in a dependency-aware sequence. This creates a planning problem that current single-task systems handle poorly. They either assign the entire project as one oversized task, split it into a flat list of vague and overlapping tasks, or leave humans to manually coordinate task boundaries and execution order. We introduce Project2Task, a project-level planning layer for autonomous research systems. Given a macro project brief, Project2Task constructs an innovation-atom lineage graph, selects a portfolio decomposition strategy using a lightweight Bernoulli block-model objective, generates bounded autoresearch tasks with explicit contribution ownership, resolves overlaps and fills in missing execution fields, and emits dependency-aware execution contracts that are independent of any particular downstream research executor. Each task is a bounded, executable research unit with its own objectives, inputs, expected artifacts, evaluation requirements, boundary constraints, and dependencies; together, the tasks advance the overarching project. Task artifacts may include code, datasets, benchmarks, experimental results, analyses, reports, or manuscripts. On a benchmark of ten project briefs yielding roughly 30 tasks, a manuscript-based portfolio evaluation shows that Project2Task achieves an average portfolio-quality score of 7.15, compared with 4.58 for the Brief Baseline and 5.31 for the Topic-only Setting. Its structured contracts also increase AutoResearchClaw’s downstream task accuracy from 0.536 to 0.759. These results demonstrate the value of an explicit project-to-task planning layer for producing coherent, non-redundant, and executable portfolios of autoresearch tasks. | 高（一手正文；非独立复现） |
| 研究方法与Agent行动 | 项目规划把目标、资源和文献证据转为带依赖关系的任务组合。 | 本地原文 TXT 第479行；核验TXT行号 479 | We define project-to-task planning as transforming a macro research project into a dependency-aware portfolio of bounded autoresearch tasks. Each task is a bounded, executable research unit within the project, with explicit objectives, inputs, expected artifacts, evaluation requirements, boundary constraints, and dependencies. Task artifacts may include code, datasets, benchmarks, experimental results, analyses, reports, or manuscripts. The input is X=(B,R,L)X=(B,R,L), where BB is a structured project brief, RR is a resource profile, and LL is literature evidence. These objects provide the project goal, candidate ideas, constraints, feasible validation scale, and external evidence for candidate claims. | 高（一手正文；非独立复现） |
| 实验任务与验证 | 基准包含十个项目实例及约三十个任务，覆盖多个研究领域。 | 本地原文 TXT 第968行；核验TXT行号 968 | Project-level autonomous research should be evaluated at the portfolio level rather than at the level of a single task alone. Each benchmark instance is therefore represented as a macro research project with six abstract dimensions: research theme, background, core problem, methodology, expected outcomes, and research significance. The constructed project-level research dataset is derived from two established academic benchmark sources with standardized curation and augmentation procedures. Specifically, we select 7 representative single-task samples from the NanoResearch dataset (Xu et al. 2026) and 3 valid samples from the ARC-Bench dataset (Liu et al. 2026) to form the base data pool. The resulting 10 project instances yield roughly 30 tasks and span several representative research domains, including Computer Vision (CV), Natural Language Processing (NLP), tabular machine learning, time series analysis, graph representation learning, audio processing, and multimodal learning. This domain diversity allows us to test the planner across different project settings, while the limited scale means the results should be interpreted as an initial project-level evaluation rather than as evidence of broad generalization. Unlike fine-grained, task-specific records in single-paper benchmarks, all selected base samples are generalized and upgraded into complete project-level research instances via large-language-model-driven augmentation. Detailed dataset construction methods are provided in Appendix B. | 高（一手正文；非独立复现） |
| 主要结果 | 作者以五个维度和统一评审设置比较任务组合质量。 | 本地原文 TXT 第982行；核验TXT行号 982 | Table 1 summarizes the evaluation metrics. We evaluate task-portfolio quality using the collection of generated manuscripts along five core dimensions: coherence, overlap control, coverage, consistency, and task division. For each dimension, an LLM judge outputs a score from 1 to 10 along with a brief justification based on the project theme and the full texts of the generated papers. This experiment therefore operationalizes task-portfolio quality through manuscript outputs; other autoresearch artifacts are outside its evaluation scope. We use Qwen3.6-Plus as the judge model (Qwen Team 2026) and keep the judge prompt, input format, scoring scale, and sampling settings identical across all compared methods. We average each reported score across five independent judge runs. In each run, we provide the judge with identical portfolio evidence and ask it to assign a score together with a concise justification. Full evaluation scoring criteria are provided in the Appendix C. | 高（一手正文；非独立复现） |
| 研究贡献或边界 | 五次独立评审的平均分显示Project2Task高于两个对照条件。 | 本地原文 TXT 第1032行；核验TXT行号 1032 | As shown in Figure 2, our proposed Project2Task method obtains higher scores than both comparison settings across all evaluation dimensions, with an average score of 7.15 compared with 5.31 for Topic and 4.58 for Brief. All reported scores are the means of five independent evaluation runs, and the detailed query-level results with standard deviations are provided in Table 2. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

论文提出Project2Task，将单一项目目标转换为一组有边界、依赖、贡献归属和执行要求的自动研究任务。计划器由结构化简报和文献等证据构建创新原子图，结合图引导的分解策略生成组合计划和任务合同。作者用10个项目测试组合质量和下游执行，报告评分与任务准确率的改善。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。研究目标是从项目简报规划下属科研任务。
  - 原文位置：TXT line 500；核验TXT行号 500；引文：A valid portfolio is therefore more than a list of titles. It should cover the macro project goal, assign core claims to task-specific owners, make reusable assets explicit, preserve feasible validation paths, and expose dependencies between tasks. These constraints are important because the same project code, dataset, or evaluation protocol may be shared across tasks, while the primary objective and output ownership of each task must remain distinct.
- 多步行动过程：yes。图构建、路由、任务编制、审核与交付是多步操作。
  - 原文位置：TXT line 903；核验TXT行号 903；引文：Validation and repair.
- 至少一种Agent能力：yes。计划器能使用证据和资源构造依赖感知任务组合。
  - 原文位置：TXT line 912；核验TXT行号 912；引文：The repaired portfolio is converted into a dependency model and per-task contracts. The dependency model contains edges, execution order, parallel groups, critical path, and roadmap. Dependency edges may specify upstream concepts, artifacts, methods, datasets, evaluations, or other required deliverables. Each contract contains the task topic, scoped goal, project context, role in the portfolio, boundaries, shared assets, dependencies, literature focus, experiment direction, evaluation guidance, reporting guidance, expected outputs, and success criteria.
- 明确科研流程角色：yes。输出下游Agent可执行的研究合同和执行顺序。
  - 原文位置：TXT line 968；核验TXT行号 968；引文：Project-level autonomous research should be evaluated at the portfolio level rather than at the level of a single task alone. Each benchmark instance is therefore represented as a macro research project with six abstract dimensions: research theme, background, core problem, methodology, expected outcomes, and research significance.

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

任务域涵盖多个机器学习问题，但文章研究对象是自动研究项目规划方法，无独立领域发现任务，保留01。

### 2.3 容易混淆的边界

任务域涵盖多个机器学习问题，但文章研究对象是自动研究项目规划方法，无独立领域发现任务，保留01。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM research planner

### 3.2 科研流程角色

研究项目规划

Project2Task 该系统接收项目级简报，将其拆解为依赖关系清晰的可执行任务，并定义贡献、输入、预期产物、验证条件和边界。评测使用10个项目简报与下游执行任务，支持其在计划层的方法归类。

### 3.3 自主能力

计划器能使用证据和资源构造依赖感知任务组合。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

方法贡献是项目级分解路由与创新原子血缘建模；系统贡献是任务合同生成、修复和下游适配接口。

### 4.2 系统流程与组件

输入项目目标、文献证据和环境资源，构造创新原子血缘图；路由器在四种分解策略间选择后，任务生成器为每个任务设置贡献所有者和验证要求；评估器检查覆盖、重叠、依赖可行性并修复问题，再将计划输出为任务合同供执行Agent使用。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

以两个项目级研究数据源构建10个项目简报；对每项组合从相干、重叠控制、覆盖、一致性、分工打分，每项重复五次；下游执行指定问题、数据集、基线与优化指标，对照AutoResearchClaw。

### 5.2 基线、指标与结果

作者报告Project2Task组合质量平均7.15，Topic-only为5.31、Brief为4.58；下游任务准确度由0.536提高到0.759。

### 5.3 科学贡献与证据强度

方法贡献是项目级分解路由与创新原子血缘建模；系统贡献是任务合同生成、修复和下游适配接口。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

与现有单任务科研Agent以及AutoResearchClaw下游执行管线区分：Project2Task在执行前增加项目级组合规划与贡献界定。

## 7. 局限性与风险

作者将验证限定于10个项目与两种测评协议；读者推断：下游实际科学领域不够宽，结果主要验证计划质量，不等同于科学发现结果。

## 8. 对综述写作的价值

支持综述讨论如何将科研Agent升级为项目组合级管理，尤其是任务分界和依赖决策。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

该系统接收项目级简报，将其拆解为依赖关系清晰的可执行任务，并定义贡献、输入、预期产物、验证条件和边界。评测使用10个项目简报与下游执行任务，支持其在计划层的方法归类。

### 9.2 速记版 pipeline

输入项目目标、文献证据和环境资源，构造创新原子血缘图；路由器在四种分解策略间选择后，任务生成器为每个任务设置贡献所有者和验证要求；评估器检查覆盖、重叠、依赖可行性并修复问题，再将计划输出为任务合同供执行Agent使用。

### 9.3 标注字段汇总

```text
paper_id=ASD-0954
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
| 问题开放度 | O2 既定基准 | 项目分解任务为预定义基准，通过既定评分评估组合质量 | “10个项目简报；对每项组合从相干、重叠控制、覆盖、一致性、分工打分” · L101 |
| 验证强度 | V1 基准/内部评测 | LLM评审打分并比较组合质量维度，无独立复现 | “每项重复五次” · L101 |
| 系统自主性 | L1 任务助手 | 系统将项目目标拆解为任务组合，人给定项目目标 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
