# Xu et al. 2026 - PantheonOS: An Evolvable Multi-Agent Framework for Automatic Genomics Discovery

**论文信息**
- 标题：PantheonOS: An Evolvable Multi-Agent Framework for Automatic Genomics Discovery
- 作者：Weize Xu; Erwin Poussi; Quan Zhong; Zehua Zeng; Christopher Zou; Xuehai Wang; Yifan Lu; Miao Cui; Daiji Okamura; Cinlong Huang; Jiayuan Ding; Zhe Zhao; Yuheng Yang; Xinhai Pan; Varshini Vijay; Naoki Konno; Nianping Liu; Lei Li; X. Rosa Ma; Stephanie D. Conley; Colin Kern; William R. Goodyer; Bogdan Bintu; Quan Zhu; Neil C. Chi; Jiang He; Lorenz Rognoni; Xiuwei Zhang; Jun Wu; David Ellison; Marlene Rabinovitch; Jesse M. Engreitz; Xiaojie Qiu
- 年份：2026
- 来源 / venue：bioRxiv
- DOI / arXiv / URL：https://doi.org/10.64898/2026.02.26.707870
- PDF / 本地文件路径：`Reference_PDF/06_Life_Sciences/Xu_2026_PantheonOS.pdf`（源文件来自 `C:\Users\20683\Desktop\pantheon-paper.pdf`）
- 论文类型：研究论文 / 系统论文 / genomics multi-agent framework
- 当前状态：已读
- 阅读日期：2026-07-09
- 笔记作者：Codex

## Evidence Log

记录所有关键判断对应的原文位置，后续写综述时优先回到这里核对。

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | p.1 Abstract; p.2 Introduction; p.20 Methods `AI Agent` / `Agent Team` | 论文明确是 `LLM-powered autonomous agent systems` 与 `evolvable ... multi-agent framework`，并在方法中定义 ReAct-style AI Agent、Agent Team、toolset、memory、agent evolution | 高 |
| 科学对象归类 | `06;07`，primary `06` | p.1 Abstract; p.2 Summary; p.3 Introduction | `automatic genomics discovery`、`single-cell biology`、`spatial genomics`、`gene panel design`、`human fetal heart multi-omics`、`heart diseases`、`cardiac regulatory and perturbation effects` 同时支撑生命科学与医学健康科学 | 高 |
| `06` 模块证据 | `06 -> 06.03`，主展示倾向 `06.03.01` | p.2 Summary; p.3; p.10-12; p.17-18 | 主系统围绕 `single-cell and multi-omics analysis`、`raw FASTQ processing`、`3D spatial genomics reconstruction`、E6.0 mouse embryo spatial transcriptomics、batch correction、gene panel design 展开，核心对象是基因组学 / 单细胞 / 空间组学 | 高 |
| `07` 模块证据 | `07 -> 07.01.08` 更稳 | p.12-14; p.15-18 | 全文不是泛泛 biomedical demo，而是具体分析 `heart disease genes`、`congenital heart disease (CHD)`、`heart disease ontogeny`、fetal heart disease gene modules、3D fetal heart perturbation and GRN effects；对象已进入疾病相关医学遗传与发育医学问题 | 高 |
| 方法流程 | 多 Agent 编排 + agentic code evolution + model router | p.3-4; p.8-10; p.15-17; p.20-21 | 包含 Omics-Expert-Team、Pantheon-Evolve、vcRouter、tool execution、code evolution、foundation-model routing，不是单次问答式系统 | 高 |
| 实验验证 | benchmark + computational validation + concrete discovery cases | p.7-10; p.10-18 | 基因 panel 设计、batch correction 演化、mouse embryo 3D spatial transcriptomics、fetal heart multi-omics / MERFISH+ integration、in-silico perturbation 和 GRN inference 构成对象级验证 | 高 |
| 科学贡献 | 自动 genomics discovery 平台，且有心脏疾病机制发现与预测 | p.1-3; p.12-18 | 论文不只做平台搭建，还报告 embryogenesis signaling、heart disease spatial gene programs、regulatory network inference 和 perturbation localization | 高 |
| 全文可得性 | 已完成本地全文核查 | 本地 PDF 全文 | 本轮已基于本地 PDF 完成全文核读，`source_limited` 状态解除 | 高 |

## 0. 摘要翻译

论文指出，大语言模型驱动的自主 Agent 系统与单细胞生物学的结合，正在推动生物医学发现范式转变；但现有 biological agent systems 多建立在单 Agent 架构上，要么过窄、要么过泛，因而大多只能处理 routine analyses。作者提出 PantheonOS，这是一套可演化、注重隐私保护的多 Agent 框架，目标是在“通用性”和“深度领域特异性”之间取得平衡。其关键能力是 agentic code evolution：系统可以通过提出代码变异、评估适应度并保留改进，自动演化现有 batch correction 与 reinforcement-learning augmented gene panel selection 算法，并取得超过人工设计基线的表现。

在科学对象层面，PantheonOS 不只做通用平台展示，而是报告了多个具体对象级案例：在早期小鼠胚胎三维空间数据中揭示 proximal-distal axis formation 中 Cer1-Nodal 的旁分泌抑制；整合 human fetal heart multi-omics 与 whole-heart 3D MERFISH+ 数据，解析 heart diseases 背后的分子程序；并通过 virtual cell model routing 预测 cardiac regulatory 与 perturbation effects。总体上，论文主张由自演化 AI systems 驱动的 biology and medicine discovery 已经具有可操作的系统原型。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：全文明确是 LLM-powered autonomous multi-agent framework；含 ReAct-style reasoning-acting loop、tool execution、多 Agent team、code evolution、routing、memory 与 distributed execution
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：是
- 在科研流程中承担的明确角色：多组学 / 单细胞 / 空间组学分析编排、算法进化、foundation model 选择、疾病基因空间解析、扰动预测、GRN 推断与结果解释

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：`06;07`
- 覆盖模式：多模块
- 是否具有具体科学对象实验、验证、benchmark task、case study 或结果报告：是
- 独立 `01.04` 存放区：none
- Primary module for filing：`06`
- Primary module for filing 说明：全文主轴仍是 `automatic genomics discovery`、single-cell / spatial genomics 与 multi-omics analysis；`07` 是基于心脏疾病基因、疾病发生程序和心脏调控扰动的独立医学覆盖模块
- 主展示模块一级类：`06`
- 主展示模块二级类：`06.03` 生物技术相关科学
- 主展示模块三级类：`06.03.01` 基因组学
- 主展示模块四级专题：Single-cell and spatial genomics agent systems
- 其他覆盖模块及对应层级路径：
  - `06 -> 06.03.04` 单细胞生物学
  - `07 -> 07.01.08` 医学遗传学
- 四级专题是否为新增：是
- 是否进入独立 `01.04` 存放区：否
- 每个模块的对象实验证据：
  - `06`：p.2-3 与 p.10-12 明确给出 single-cell biology、raw FASTQ processing、multi-omics analysis、3D spatial genomics reconstruction、early mouse embryo spatial transcriptomics、batch correction、gene panel design、virtual cell model selection
  - `07`：p.12-18 明确给出 human fetal heart single-cell multi-omics、heart disease genes、congenital heart disease modules、heart disease ontogeny、fetal heart perturbation、cardiac GRN inference 与 disease-gene spatial architecture
- 归类理由：PantheonOS 已经不是 general agent benchmark。全文主对象首先是 genomics / single-cell / spatial omics，因此 `06` 必须进入；同时其 human fetal heart multi-omics、CHD / cardiomyopathy / OTM / FTAAD 等疾病基因集、心脏病发生程序与调控扰动预测构成稳定的医学对象证据，因此 `07` 也必须进入
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：genomics、single-cell biology、spatial transcriptomics、multi-omics integration、fetal heart disease genes、cardiac regulatory networks 与 perturbation effects
- 最终科学问题：如何用可演化多 Agent 系统自动推进 genomics / single-cell discovery，并在人类胎儿心脏数据上解析疾病相关分子程序、调控网络与扰动效应
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：LLM、多 Agent、router、code evolution 都只是实现机制；主类必须由被研究的具体生命和医学对象决定

### 2.3 容易混淆的边界

- 可能误归类到：独立 `01.04`；纯 `06`；`07.03.08` 医学信息学；`07.02.09` 心血管病学
- 最终判定：`06;07`，primary `06`，`07` 侧主落 `07.01.08`
- 判定理由：
  - 不应归 `01.04`：全文存在多个明确对象级实验与发现案例
  - 不应只归 `06`：fetal heart disease genes、CHD modules、heart disease ontogeny 与 cardiac perturbation 已经是独立医学对象证据
  - 不优先归 `07.03.08`：论文确实用了复杂信息学整合，但医学信息学是方法壳，不是其最稳定的医学对象
  - 不优先归 `07.02.09`：虽然对象涉及心脏疾病，但全文重心不是患者级诊断、治疗或临床流程，而是疾病基因、发育机制和调控架构，故更稳地落在 `07.01.08` 医学遗传学
- 多模块覆盖说明：`06` 提供生命科学主轴，`07` 提供疾病相关医学对象覆盖，两者均有全文级对象证据
- 01.04 判定说明：不进入；已有 concrete object experiments, validations, case studies, and reported results
- 是否需要二次复核：否；本轮已完成本地全文核查

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：是
- Multi-Agent System：是
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：未强调
- Hybrid Agent：是
- 其他：evolvable distributed scientific-agent framework

### 3.2 科研流程角色

- 文献检索与阅读：部分是
- 知识抽取与组织：是
- 科学问题提出：部分是
- 假设生成：部分是
- 实验设计：否
- 仿真建模：是
- 工具调用与代码执行：是
- 实验执行：否
- 数据分析：是
- 结果解释：是
- 证据评估与验证：是
- 论文写作：否
- 端到端科研流程自动化：是

### 3.3 自主能力

- 任务分解：是
- 计划生成：是
- 工具调用：是
- 记忆与状态维护：是
- 反馈迭代：是
- 自主决策：是
- 多 Agent 协作：是
- 环境交互：是
- 闭环实验：否

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 实验驱动：部分是
- 仿真驱动：是
- 多模态：是
- 多尺度建模：部分是
- 高通量筛选：部分是
- 知识图谱：未明确
- 数字孪生：否
- 机器人平台：否
- 其他：single-cell / spatial genomics; multi-omics integration; virtual cell routing

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：现有 biological agent systems 多为单 Agent、过窄或过泛，难以支撑 end-to-end genomics discovery 与复杂疾病相关数据分析
- 现有科研流程或方法的痛点：生物信息学与单细胞 / 空间组学流程工具链复杂、跨模态整合困难、算法优化成本高、虚拟细胞模型选择门槛高
- 核心假设或直觉：若把多 Agent 编排、tool execution、agentic code evolution 与 foundation-model routing 整合，就能把通用 LLM 能力转化为可演化的领域科研系统

### 4.2 系统流程

按输入到输出写清楚 pipeline：

1. 输入：自然语言科研目标、单细胞 / 空间组学 / multi-omics 数据、下游分析任务
2. 任务分解 / 规划：多 Agent team 拆解分析任务，调用 Omics-Expert-Team、Pantheon-Evolve 或 vcRouter 等组件
3. 工具、数据库、模型或实验平台调用：调用 FASTQ 处理、single-cell / spatial analysis 工具、batch correction、RL gene panel design、Moscot、Spateo、Tabula、scGPT 等
4. 中间结果反馈：用 fitness evaluation、benchmark metric、task performance 和映射结果对中间算法与模型选择进行回馈
5. 决策或迭代：持续执行 code mutation、algorithm evolution、model routing 和 multi-agent orchestration
6. 输出：genomics discovery、mouse embryo spatial signaling results、fetal heart disease gene spatial programs、perturbation effects 与 GRN predictions

### 4.3 系统组件

- Agent 核心：PantheonOS evolvable distributed multi-agent framework
- 工具 / API / 数据库：Python / shell / notebook / file / web / scFM toolsets；GeneCards；UniProt；oncogene repositories；Moscot；Spateo；Scanpy；OpenST；Tangram；Tabula；scGPT
- 记忆或状态模块：ACE playbook memory、execution trajectory reflection、dynamic context injection
- 规划器：PantheonTeam / SequentialTeam / MoATeam / SwarmTeam 等 team patterns；planning agent / analyzer agent
- 评估器 / verifier：fitness evaluation、batch mixing / cell type conservation / ARI / NMI / speed、mapping coherence、GRN edge comparison
- 人类反馈或专家介入：无强依赖，但对话式 interaction 存在
- 实验平台或仿真环境：mouse embryo OpenST spatial transcriptomics、human fetal heart single-cell multi-omics、whole-heart 3D MERFISH+、virtual cell models

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：是
- 高通量计算：是
- 机器人实验：否
- 湿实验：否（系统本身未执行湿实验）
- 临床数据：否
- 真实场景部署：否
- 专家评估：未明确

### 5.2 数据、任务与指标

- 数据集 / 实验对象：
  - early mouse embryo OpenST 3D spatial transcriptomics
  - human fetal heart single-cell multi-omics
  - whole-heart 3D MERFISH+ at PCW12
  - kidney immuno-oncology and related datasets for gene panel design
  - CELLxGENE subset for batch correction evolution
- 任务设置：
  - RL-augmented gene panel design
  - batch correction evolution
  - single-cell / spatial transcriptomics integration
  - fetal heart disease gene spatial analysis
  - in-silico perturbation
  - GRN inference
- 对比基线：Harmony / Scanorama / BBKNN、raw LLM baselines、traditional panel methods、published scFM choices
- 评价指标：ARI、NMI、batch mixing、cell-type conservation、speed、routing accuracy、task inference accuracy、literature-validated GRN edges
- 关键结果：
  - evolved Harmony 等 batch correction variants 改善性能与速度
  - RL gene panel design 在 kidney / immuno-oncology datasets 上表现优于传统方法
  - 自动完成 E6.0 mouse embryo 3D spatial reconstruction 并解析 Cer1-Nodal signaling
  - 在 fetal heart 解析 heart disease gene modules、空间表达与调控机制
  - 通过 scGPT / Tabula 路由完成 perturbation 与 GRN prediction，并映射回 3D heart atlas
- 是否有消融实验：有部分比较与多方法基线，但非标准 ablation-first 论文
- 是否有失败案例或负结果：正文未系统展开失败案例

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：是
- 科学贡献是否经过验证：是，但主要是计算与对象级分析验证
- 贡献强度判断：强
- 科学贡献类型：system_platform / explanation / prediction / benchmark
- 证据强度：computationally_validated

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：PantheonOS 不是单模型 predictor，而是围绕真实生物对象分析流程构建的可演化多 Agent 操作系统
- 与已有 Agent / 科研智能系统的区别：相较 CellVoyager、SpatialAgent、Biomni 等单 Agent 或较静态系统，PantheonOS 更强调 distributed multi-agent architecture、agentic code evolution、foundation-model routing 与 privacy-aware deployment
- 与同一科学领域其他 Agent 文献的关系：属于 `06` 生命科学 Agent 前沿样本，同时也是 `06/07` 边界上少数有明确医学对象覆盖的高强度论文
- 主要创新点：把 multi-agent orchestration、algorithm evolution、single-cell / spatial genomics pipeline 和 disease-perturbation virtual-cell analysis 统一到一个可演化框架中

## 7. 局限性与风险

- Agent 自主性不足：虽然系统很强，但仍未达到 wet-lab closed-loop
- 科学验证不足：主要证据仍是计算验证和对象级分析结果，不是干预性实验或临床验证
- 泛化性不足：当前最强案例集中在 genomics、single-cell、fetal heart 与 cardiac biology
- 工具链依赖：高度依赖现有生信工具、foundation models 和复杂软件环境
- 数据泄漏或 benchmark 偏差：算法进化与模型路由结果仍需外部独立复现
- 成本、可复现性或安全风险：多 Agent、代码演化和多模型环境提高了复现与治理难度；作者也提示对敏感数据需谨慎使用

## 8. 对综述写作的价值

- 可放入哪个章节：`06` 生命科学中的 genomics / single-cell / spatial omics agent systems；也应在 `06/07` 边界讨论中重点出现
- 可支撑哪个论点：生命科学 Agent 正在从 workflow automation 走向 self-evolving discovery systems，并开始稳定进入疾病相关医学对象
- 可用于哪个表格或图：life-science frontier systems table；`06/07` multi-module boundary case table；agentic code evolution case table
- 适合作为代表性案例吗：是
- 推荐引用强度：核心引用
- 需要在正文中特别引用的页码 / 图 / 表：p.1 Abstract；p.3 平台定位；p.12-14 fetal heart disease modules；p.15-17 vcRouter / perturbation / GRN
- 需要与哪些论文并列比较：`Alber_2026_CellVoyager`、`Wang_2025_SpatialAgent`、`Huang_2025_Biomni`、`Zhang_2026_BioGAIP_Bioinformatics`、`Roberts_2026_OpenScientist_Biomedical_Discovery`

## 9. 总结

### 9.1 一句话概括

可演化多 Agent 基因组学发现系统，并进入心脏疾病机制分析。

### 9.2 速记版 pipeline

1. 接收 genomics / multi-omics 科研任务
2. 多 Agent 拆解并调用分析工具与模型
3. 用 code evolution 和 model routing 改进算法选择
4. 在胚胎与胎儿心脏数据上输出生命与医学发现

### 9.3 标注字段汇总

```text
是否纳入：是
科学对象模块：06;07
覆盖模式：multi_module
是否具有具体科学对象实验：yes
general_method_bucket：none
Primary module for filing：06
是否进入 01.04 存放区：否
主展示模块一级类：06
主展示模块二级类：06.03
主展示模块三级类：06.03.01
主展示模块四级专题：Single-cell and spatial genomics agent systems
其他覆盖模块及对应层级路径：06 -> 06.03.04 单细胞生物学；07 -> 07.01.08 医学遗传学
module_assignment_evidence：single-cell biology, raw FASTQ processing, batch correction, RL gene panel design, embryo spatial transcriptomics, and virtual cell routing support 06; fetal heart multi-omics, heart disease gene modules, CHD-related spatial programs, cardiac perturbation, and GRN inference support 07
multi_module_object_coverage_note：PantheonOS is not retained as 01.04 because the full text contains concrete genomics and disease-related object evidence. Primary filing remains 06 because the platform's main instantiated object space is genomics / single-cell / spatial omics, while 07 is independently supported by fetal-heart disease genetics and cardiac regulatory analyses
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Retrieval-augmented Agent; Multi-Agent System; Hybrid Agent
科研流程角色：knowledge_extraction_and_organization; hypothesis_generation; simulation_modeling; tool_use_and_code_execution; data_analysis; result_interpretation; evidence_assessment_and_validation; end_to_end_research_automation
自主能力：task_decomposition; planning; tool_use; memory_or_state_tracking; feedback_iteration; autonomous_decision_making; multi_agent_collaboration; environment_interaction
验证方式：benchmark; simulation_validation; high_throughput_computation
交叉属性：computation_driven; data_driven; experiment_driven; simulation_driven; multimodal; multiscale_modeling; high_throughput_screening
科学贡献类型：system_platform; explanation; prediction; benchmark
证据强度：computationally_validated
归类置信度：high
纳入置信度：high
推荐引用强度：core
```

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O3 新实例 | 分析胎儿心脏多组学数据并解析疾病相关分子程序 | “human fetal heart single-cell multi-omics” · L206 |
| 验证强度 | V2 计算/仿真/回顾性 | 计算验证，系统本身未执行湿实验 | “湿实验：否（系统本身未执行湿实验）” · L197 |
| 系统自主性 | L2 闭环执行者 | 系统自主完成从数据处理到GRN inference的多步闭环 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
