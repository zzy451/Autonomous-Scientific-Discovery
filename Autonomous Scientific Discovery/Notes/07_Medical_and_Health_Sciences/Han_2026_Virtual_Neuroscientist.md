# Han et al. 2026 - Towards a Virtual Neuroscientist: Autonomous Neuroimaging Analysis via Multi-Agent Collaboration

## 2026-06-24 Batch28Partial1 full reaudit revision

```text
paper_id: ASD-0814
supported_modules: 07
primary_module_for_filing: 07
object_coverage_mode: single_module
has_concrete_object_experiments: yes
general_method_bucket: none
source_limited: no
safety_access_status: none
first_hand_source_checked: official arXiv PDF archived locally and checked (`Autonomous Scientific Discovery/Reference_PDF/07_Medical_and_Health_Sciences/Han_2026_Virtual_Neuroscientist.pdf`)
classification_evidence_source_level: first_hand_full_text_with_local_archived_arxiv_pdf
note_revision_required: yes
archive_status_note: Official arXiv PDF archived locally and checked at `Autonomous Scientific Discovery/Reference_PDF/07_Medical_and_Health_Sciences/Han_2026_Virtual_Neuroscientist.pdf`.
module_assignment_evidence: Clinically actionable neuroimaging biomarker and diagnosis-prediction workflows on ADHD-200 and ADNI support module 07.
```

**论文信息**
- 标题：Towards a Virtual Neuroscientist: Autonomous Neuroimaging Analysis via Multi-Agent Collaboration
- 作者：Keqi Han; Songlin Zhao; Yao Su; Xiang Li; Yixuan Yuan; Lifang He; Carl Yang
- 年份：2026
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2605.09366
- PDF / 本地文件路径：official arXiv PDF archived locally and checked at `Autonomous Scientific Discovery/Reference_PDF/07_Medical_and_Health_Sciences/Han_2026_Virtual_Neuroscientist.pdf`
- 论文类型：研究论文 / neuroimaging multi-agent system
- 当前状态：to_read
- 阅读日期：2026-06-20
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | arXiv HTML v3 lines 101-107, 123-125 | 有 centralized planning、decentralized specialists、code-centric execution 和闭环 QC | 高 |
| 科学对象归类 | supported_modules=`07`; primary_module_for_filing=`07` | arXiv HTML v3 lines 89-92, 173-174 | 临床可操作 neuroimaging biomarkers 与 diagnosis prediction 直接支持医学/健康科学模块 07 | 高 |
| 2026-06-24 full reaudit | source_limited=`no`; evidence source level=`first_hand_full_text_with_local_archived_arxiv_pdf` | official local arXiv PDF (`Autonomous Scientific Discovery/Reference_PDF/07_Medical_and_Health_Sciences/Han_2026_Virtual_Neuroscientist.pdf`) | 当前写回已与 official arXiv PDF 本地归档路径同步并核对 | 高 |
| 方法流程 | 层级多 Agent 闭环 | arXiv HTML v3 lines 154-161 | QC judgment 会反馈给 Supervisor 做后续规划 | 高 |
| 医学对象 | ADHD-200 / ADNI 诊断预测与 biomarker workflow | arXiv HTML v3 lines 173-174, 275 | 任务锚定 MRI / fMRI 下的临床相关神经影像分析 | 高 |
| 实验验证 | computational benchmark with refinement | arXiv HTML v3 lines 178-205 | 有 held-out AUC/F1/ACC、多轮 refinement 和动态 pipeline 选择 | 高 |
| 边界判断 | 不应移入 `06` 或 `01.04` | abstract + HTML | 临床可操作生物标志物与诊断目标把它稳定压在医学侧 | 高 |

## 0. 摘要翻译

论文提出一个“虚拟神经科学家”式多 Agent 神经影像分析系统，最新版本中系统名为 `NEXUS`。作者把原始 MRI 数据、科研目标、代码执行、质量控制和下游分析串成闭环，用于自动构建面向临床可操作生物标志物和诊断预测的 neuroimaging workflow。其核心不是一般神经科学知识图谱整理，也不是通用科研平台，而是医学相关的 neuroimaging analysis。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：具备层级多 Agent 分工、代码执行、运行时反馈、QC 回路和自主规划
- 判定置信度：高
- 是否面向明确科研目标：是，面向 neuroimaging biomarkers / diagnosis prediction
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：是
- 在科研流程中承担的明确角色：数据理解、数据处理、质量控制、下游分析、工作流规划

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：`07`
- 覆盖模式：single_module
- 是否具有具体科学对象实验、验证、benchmark task、case study 或结果报告：是
- 独立 `01.04` 存放区：none
- Primary module for filing：`07`
- Primary module for filing 说明：此处 filing 与模块事实一致，但 filing 字段仍只是归档便利字段
- 主题路径备注：可放在 `07.01` neuroimaging / biomarker 子话题下讨论，但这不是新增 scientific-object module
- 每个模块的对象实验证据：`07` 由 ADHD-200 / ADNI 上的 clinically actionable neuroimaging biomarker 与 diagnosis-prediction workflows 支持
- 归类理由：最终对象是临床相关神经影像生物标志物与诊断预测，属于医学与健康科学模块 `07`
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：medical neuroimaging biomarkers and diagnosis prediction
- 最终科学问题：如何用多 Agent 闭环自动化神经影像分析并支持临床相关预测
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：multi-agent 架构只是方法，验证对象和输出都围绕医学 neuroimaging task

### 2.3 容易混淆的边界

- 可能误归类到：06；01.04
- 最终判定：supported_modules=`07`; primary_module_for_filing=`07`
- 判定理由：虽然有 neuroscience 语境，但核心任务是临床可操作生物标志物与诊断预测，冻结 adjudication 只支持模块 `07`
- Multi-module 覆盖说明：不适用；当前冻结结果不是多模块
- 01.04 判定说明：已有明确医学对象实验与结果报告，因此不进入独立 `01.04` 存放区
- 是否需要二次复核：否

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：否
- Multi-Agent System：是
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：部分是
- Hybrid Agent：是
- 其他：Hierarchical neuroimaging analysis agents

### 3.2 科研流程角色

- 文献检索与阅读：否
- 知识抽取与组织：部分是
- 科学问题提出：否
- 假设生成：部分是
- 实验设计：否
- 仿真建模：否
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
- 记忆与状态维护：部分是
- 反馈迭代：是
- 自主决策：是
- 多 Agent 协作：是
- 环境交互：是
- 闭环实验：否

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 实验驱动：否
- 仿真驱动：否
- 多模态：是
- 多尺度建模：否
- 高通量筛选：否
- 知识图谱：否
- 数字孪生：否
- 机器人平台：否
- 其他：medical neuroimaging

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：减少神经影像分析从原始数据到可解释临床结果的人工流程负担
- 现有科研流程或方法的痛点：固定工作流难覆盖不同神经影像任务，人工 QC 和代码执行成本高
- 核心假设或直觉：多 Agent 分工加上 QC 反馈可提升 neuroimaging workflow 的灵活性和稳健性

### 4.2 系统流程

1. 输入：MRI / fMRI 数据与分析目标
2. 任务分解 / 规划：Supervisor 拆解工作流并分派给 specialist agents
3. 工具、数据库、模型或实验平台调用：代码执行、处理流程、QC 和下游预测模块
4. 中间结果反馈：QC verdict 和中间分析结果返回规划层
5. 决策或迭代：调整 pipeline 并继续 refinement
6. 输出：面向 biomarker / diagnosis prediction 的 neuroimaging workflow 与结果

### 4.3 系统组件

- Agent 核心：Supervisor、Data Awareness、Quality Control、Processing、Downstream Analysis agents
- 工具 / API / 数据库：code-centric execution stack
- 记忆或状态模块：workflow state
- 规划器：Supervisor
- 评估器 / verifier：QC agent
- 人类反馈或专家介入：有 alignment-style QC 检查
- 实验平台或仿真环境：ADHD-200 / ADNI neuroimaging datasets

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：否
- 高通量计算：否
- 机器人实验：否
- 湿实验：否
- 临床数据：是
- 真实场景部署：否
- 专家评估：是

### 5.2 数据、任务与指标

- 数据集 / 实验对象：ADHD-200；ADNI
- 任务设置：diagnosis prediction and biomarker-oriented neuroimaging analysis
- 对比基线：固定 workflow baselines
- 评价指标：AUC、F1、ACC、completion / refinement behavior
- 关键结果：取得更好的 held-out 预测表现，并展示多轮 pipeline 探索与 QC 驱动 refinement
- 是否有消融实验：有模式比较与 run 统计
- 是否有失败案例或负结果：未形成湿实验或临床级 biomarker 确认

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：主要是 workflow 级医学分析系统
- 科学贡献是否经过验证：是
- 贡献强度判断：中
- 科学贡献类型：系统平台 / 预测
- 证据强度：专家确认

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单个影像预测模型，而是完整的 agentic neuroimaging workflow
- 与已有 Agent / 科研智能系统的区别：强调 QC 反馈与医学影像任务绑定，而非领域无关平台
- 与同一科学领域其他 Agent 文献的关系：可作为医学神经影像 Agent 的代表样本
- 主要创新点：将规划、代码执行、QC 和下游分析整合为闭环多 Agent 系统

## 7. 局限性与风险

- Agent 自主性不足：虽然闭环明确，但仍主要停留在 benchmark / workflow 层
- 科学验证不足：未证明强新医学机制或临床可转化 biomarkers
- 泛化性不足：集中于有限 neuroimaging datasets
- 工具链依赖：强依赖特定代码与 QC 栈
- 数据泄漏或 benchmark 偏差：需关注数据集与 prompt 定制偏差
- 成本、可复现性或安全风险：流程复杂，复现成本不低

## 8. 对综述写作的价值

- 可放入哪个章节：07 医学与健康科学 / neuroimaging agents
- 可支撑哪个论点：临床相关 biomarker 对象优先时，应留在医学类而不是神经生命科学或 `01.04`
- 可用于哪个表格或图：`07 / 06 / 01.04` 边界表；医学影像 Agent 表
- 适合作为代表性案例吗：适合
- 推荐引用强度：普通引用
- 需要在正文中特别引用的页码 / 图 / 表：agent architecture；QC loop；evaluation
- 需要与哪些论文并列比较：其他 clinical / neuroimaging multi-agent systems

## 9. 总结

### 9.1 一句话概括

面向临床神经影像生物标志物的闭环多 Agent 系统。

### 9.2 速记版 pipeline

1. 输入 MRI 数据与目标
2. 多 Agent 拆解流程
3. 执行处理与分析代码
4. QC 回传并调整
5. 输出诊断/生物标志物结果

### 9.3 标注字段汇总

```text
是否纳入：是
科学对象模块：07
覆盖模式：single_module
是否具有具体科学对象实验：yes
general_method_bucket：none
Primary module for filing：07
是否进入 01.04 存放区：no
其他覆盖模块及对应层级路径：none
module_assignment_evidence：Clinical neuroimaging biomarker and diagnosis-prediction workflows on ADHD-200 and ADNI support module 07.
multi_module_object_coverage_note：Single-module medical filing matches the frozen classification fact for ASD-0814.
classification_evidence_source_level：first_hand_full_text_with_local_archived_arxiv_pdf
source_limited：no
safety_access_status：none
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Multi-Agent System; Hybrid Agent
科研流程角色：tool_use_and_code_execution; data_analysis; result_interpretation; evidence_assessment_and_validation; workflow_orchestration
自主能力：task_decomposition; planning; tool_use; feedback_iteration; autonomous_decision_making; multi_agent_collaboration; environment_interaction
验证方式：benchmark; clinical_data; expert_evaluation
交叉属性：computation_driven; data_driven; multimodal
科学贡献类型：system_platform; prediction
证据强度：expert_confirmed
归类置信度：高
纳入置信度：高
推荐引用强度：普通引用
```
