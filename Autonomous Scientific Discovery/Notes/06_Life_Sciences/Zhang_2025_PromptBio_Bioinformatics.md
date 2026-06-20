# Zhang et al. 2025 - PromptBio: A Multi-Agent AI Platform for Bioinformatics Data Analysis

**论文信息**
- 标题：PromptBio: A Multi-Agent AI Platform for Bioinformatics Data Analysis
- 作者：Zhang et al.
- 年份：2025
- 来源 / venue：bioRxiv
- DOI / arXiv / URL：https://doi.org/10.1101/2025.07.05.663295
- PDF / 本地文件路径：当前未保存本地 PDF；本笔记基于 bioRxiv / Crossref 官方摘要
- 论文类型：系统论文 / multi-agent bioinformatics platform
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | official abstract | `PromptGenie` 明确是 multi-agent system，多个 specialized agents 协作 | 高 |
| 科学对象归类 | 暂保留 `06.03` | official abstract | 全文持续围绕 bioinformatics、omics pipelines、multi-omics analysis | 中高 |
| 平台压力 | `06.03 / 01.04` 高压样本 | official abstract | 同时强调 `modular AI platform`、`workflow generation`、`agent orchestration` | 高 |
| 方法流程 | 分为 PromptGenie / DiscoverFlow / ToolsGenie | official abstract | 包含 stepwise HITL、automated workflows、dynamic code generation 三种模式 | 高 |
| 验证方式 | 平台能力验证 | official abstract | 强调 design, capabilities, validation, extensibility, monitoring, compliance | 中高 |

## 0. 摘要翻译

PromptBio 被描述为一个面向可扩展、可复现、可适配生物信息学分析的模块化 AI 平台，由生成式 AI 和自然语言交互驱动。它包含三种互补模式：PromptGenie 提供多 Agent、逐步的人在回路工作流；DiscoverFlow 提供大规模多组学分析的一体化自动流程；ToolsGenie 动态生成可执行生物信息学代码以支持定制分析。系统中有 DataAgent、OmicsAgent、AnalysisAgent、QAgent 等专门角色，并整合 Omics Tools、Analysis Tools、MLGenie 等工具链。当前证据说明它既有明确的生命科学 / 组学对象，又带有很强的平台与 `01.04` 压力，因此本轮先保守保留在 `06.03` 并标记为高压边界样本。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：存在多 Agent 协作、工具调用、流程生成与自动化分析
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：部分是
  - 多 Agent 协作：是
- 在科研流程中承担的明确角色：数据摄入、omics 分析、统计解释、问答总结、工作流编排

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：06
- 二级类：06.03
- 三级类：bioinformatics / multi-omics analysis agents
- 四级专题：multi-agent bioinformatics platforms
- 四级专题是否为新增：否
- 归类理由：现阶段验证对象与工具链稳定锚定在组学 / 生物信息学分析
- 归类置信度：中

### 2.2 对象优先判定

- 最终科学研究对象：bioinformatics data analysis，尤其是 omics / multi-omics workflows
- 最终科学问题：如何用 Agent 平台降低高通量生物信息学分析门槛并自动化多组学流程
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：尽管平台性很强，但当前可见任务仍集中在生物信息学对象而非全领域科研基础设施

### 2.3 容易混淆的边界

- 可能误归类到：01.04
- 最终判定：本轮暂保留 06.03
- 判定理由：平台与流程编排色彩很强，但摘要中的数据域、工具域和验证场景都明确偏向 bioinformatics / multi-omics
- 是否需要二次复核：是，属于本轮最典型的 `01.04 / concrete domain` 高压样本之一

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：未见明确证据
- Multi-Agent System：是
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：是
- Hybrid Agent：是
- 其他：workflow generation platform

### 3.2 科研流程角色

- 文献检索与阅读：否
- 知识抽取与组织：是
- 科学问题提出：部分是
- 假设生成：部分是
- 实验设计：否
- 仿真建模：否
- 工具调用与代码执行：是
- 实验执行：否
- 数据分析：是
- 结果解释：是
- 证据评估与验证：是
- 论文写作：部分是
- 端到端科研流程自动化：是

### 3.3 自主能力

- 任务分解：是
- 计划生成：是
- 工具调用：是
- 记忆与状态维护：未见明确证据
- 反馈迭代：是
- 自主决策：部分是
- 多 Agent 协作：是
- 环境交互：是
- 闭环实验：否

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 实验驱动：否
- 仿真驱动：否
- 多模态：部分是
- 多尺度建模：否
- 高通量筛选：否
- 知识图谱：否
- 数字孪生：否
- 机器人平台：否
- 其他：workflow orchestration

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：降低高通量生物信息学分析门槛，提高可复现性与可扩展性
- 现有科研流程或方法的痛点：标准流程、定制流程和交互式解释往往分散在不同工具链
- 核心假设或直觉：多 Agent + 自然语言接口能把标准组学分析和定制分析整合起来

### 4.2 系统流程

1. 输入：用户自然语言提出的 bioinformatics analysis task
2. 任务分解 / 规划：PromptGenie / DiscoverFlow / ToolsGenie 选择相应模式
3. 工具、数据库、模型或实验平台调用：调用 Omics Tools、Analysis Tools、MLGenie 等
4. 中间结果反馈：根据执行结果做统计解释和交互总结
5. 决策或迭代：继续分步分析或生成新的执行代码
6. 输出：可复现的 bioinformatics workflow 与分析结果

### 4.3 系统组件

- Agent 核心：PromptGenie、DiscoverFlow、ToolsGenie
- 工具 / API / 数据库：Omics Tools、Analysis Tools、MLGenie
- 记忆或状态模块：workflow state
- 规划器：multi-agent workflow generation
- 评估器 / verifier：validation / monitoring / compliance modules
- 人类反馈或专家介入：PromptGenie 支持 human-in-the-loop
- 实验平台或仿真环境：无

## 5. 实验与验证

### 5.1 验证方式

- benchmark：部分是
- 仿真验证：否
- 高通量计算：否
- 机器人实验：否
- 湿实验：否
- 临床数据：未见明确证据
- 真实场景部署：否
- 专家评估：未见明确证据

### 5.2 数据、任务与指标

- 数据集 / 实验对象：omics / multi-omics bioinformatics tasks
- 任务设置：stepwise workflow、end-to-end analysis、dynamic code generation
- 对比基线：摘要未展开
- 评价指标：设计能力、执行能力、验证能力与可扩展性
- 关键结果：证明平台可以支持 automated and customizable bioinformatics workflows
- 是否有消融实验：摘要未展开
- 是否有失败案例或负结果：摘要未展开

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：更偏平台与流程贡献
- 科学贡献是否经过验证：有官方摘要级能力验证
- 贡献强度判断：中
- 科学贡献类型：system_platform / analysis
- 证据强度：主摘要支持，仍待全文

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单模型分析器，而是 workflow-generation + orchestration 平台
- 与已有 Agent / 科研智能系统的区别：专门聚焦 bioinformatics / multi-omics 分析
- 与同一科学领域其他 Agent 文献的关系：可与 PROTEUS、CellAtria、OmniCellAgent 对比
- 主要创新点：把 stepwise HITL、automated workflows 与 dynamic code generation 放进同一平台

## 7. 局限性与风险

- Agent 自主性不足：人类介入比例与异常恢复机制未在摘要中充分展开
- 科学验证不足：目前更多是平台能力验证，不是强实验发现
- 泛化性不足：需要全文确认是否真正超出 bioinformatics 范围
- 工具链依赖：高度依赖 domain-standard bioinformatics tools
- 数据泄漏或 benchmark 偏差：平台验证细节仍待全文确认
- 成本、可复现性或安全风险：执行环境和依赖管理复杂

## 8. 对综述写作的价值

- 可放入哪个章节：06 生命科学
- 可支撑哪个论点：bioinformatics 方向出现了平台型多 Agent 工作流系统
- 可用于哪个表格或图：06 类平台型 / 数据分析型 Agent 对照表
- 适合作为代表性案例吗：适合作为边界案例
- 推荐引用强度：普通引用
- 需要在正文中特别引用的页码 / 图 / 表：后续补 PDF
- 需要与哪些论文并列比较：0537、0543、0254、0561

## 9. 总结

### 9.1 一句话概括

PromptBio 是高压边界型的多 Agent 生物信息学平台。

### 9.2 速记版 pipeline

1. 用户提出组学分析需求
2. 选择 stepwise / automated / codegen 模式
3. 调用标准分析工具
4. 组织解释结果
5. 输出可复现 workflow

### 9.3 标注字段汇总

```text
是否纳入：to_read
主类：06
二级类：06.03
三级类：bioinformatics / multi-omics analysis agents
四级专题：multi-agent bioinformatics platforms
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Multi-Agent System; Human-in-the-loop Agent; Hybrid Agent
科研流程角色：knowledge_extraction_and_organization; scientific_question_formulation; hypothesis_generation; tool_use_and_code_execution; data_analysis; result_interpretation; evidence_assessment_and_validation; paper_writing; end_to_end_research_automation
自主能力：task_decomposition; planning; tool_use; feedback_iteration; autonomous_decision_making; multi_agent_collaboration; environment_interaction
验证方式：benchmark
交叉属性：computation_driven; data_driven; multimodal
科学贡献类型：system_platform; analysis
证据强度：high_primary_abstract
归类置信度：中
纳入置信度：高
推荐引用强度：standard
```
