# Geng et al. 2026 - Automating Structural Analysis Across Multiple Software Platforms Using Large Language Models

**论文信息**
- 标题：Automating Structural Analysis Across Multiple Software Platforms Using Large Language Models
- 作者：Ziheng Geng; Jiachen Liu; Ian Franklin; Ran Cao; Dan M. Frangopol; Minghui Cheng
- 年份：2026
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2604.09866
- PDF / 本地文件路径：已核对 arXiv PDF（`https://arxiv.org/pdf/2604.09866.pdf`）；当前未见本地 `Reference_PDF/` 归档副本，但本笔记判断基于一手全文，不属于 `source_limited`
- 论文类型：研究论文 / 跨平台结构分析多 Agent 系统
- 当前状态：已纳入
- 阅读日期：2026-06-24
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | arXiv PDF 摘要；引言 | 采用 two-stage multi-agent architecture，围绕结构分析任务执行解析、转换与求解 | 高 |
| 科学对象归类 | `09` | 标题；摘要 | 论文明确面向 frame structural analysis across ETABS、SAP2000、OpenSees，不是通用 Agent 平台 | 高 |
| 方法流程 | 统一 JSON + 并行代码翻译 | 摘要；方法部分 | Stage 1 协同推理几何、材料、边界和荷载信息，Stage 2 并行转写为多软件脚本 | 高 |
| 实验验证 | 20 个代表性 frame problems；十次重复试验；准确率均超 90% | 摘要；实验部分 | 结果强调跨平台稳定性，而非单平台演示 | 高 |
| 边界判断 | 不进入 `01.04` | 摘要；引言 | JSON 与脚本翻译只是手段，最终验证对象仍是结构工程分析工作流 | 高 |
| 来源状态 | 一手全文已核对 | arXiv PDF | 当前来源充足，可直接支持单模块 `09` 结论；是否有本地归档 PDF 不影响本轮判断 | 高 |

## 0. 摘要翻译

论文关注结构工程实践中常见的跨软件有限元分析需求。作者指出，现有 LLM 结构分析研究大多只针对单一平台，难以覆盖工程师在 ETABS、SAP2000 与 OpenSees 之间切换的真实工作流。为此，论文提出两阶段多 Agent 架构：第一阶段由多个代理协同解析用户输入，推断几何、材料、边界和荷载信息，并整理成统一 JSON；第二阶段由并行代码翻译代理将该 JSON 转成多平台可执行脚本。作者在 20 个代表性 frame problems 上进行十次重复试验，报告三类平台上的准确率均超过 90%。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：系统具有明确工程目标、多步分工、工具调用、并行脚本生成与结果验证
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：部分是
  - 多 Agent 协作：是
- 在科研流程中承担的明确角色：结构建模、脚本翻译、多软件平台适配、结果验证

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：`09`
- 覆盖模式：单模块
- 是否具有具体科学对象实验、验证、benchmark task、case study 或结果报告：是
- 独立 `01.04` 存放区：none
- Primary module for filing：`09`
- Primary module for filing 说明：仅用于笔记落盘和展示，不改变当前单模块事实
- 主展示模块一级类：`09` 工程与工业技术科学
- 主展示模块二级类：`09.05` 土木、建筑与水利工程
- 主展示模块三级类：跨平台结构工程分析 / FEA workflow automation
- 主展示模块四级专题：Cross-platform structural-analysis agents
- 其他覆盖模块及对应层级路径：无
- 四级专题是否为新增：否
- 是否进入独立 `01.04` 存放区：否
- 每个模块的对象实验证据：`09` 的证据来自多平台 frame problems、统一 JSON 结构语义表示与 ETABS/SAP2000/OpenSees 执行结果
- 归类理由：论文面向的是具体结构工程分析对象及其多软件实现，不是通用科研方法
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：frame structural analysis、有限元建模脚本、多软件工程分析工作流
- 最终科学问题：如何让 Agent 稳定完成跨 ETABS、SAP2000、OpenSees 的结构分析
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：多 Agent 与 JSON 只是实现机制，真实被分析和评估的是结构工程对象

### 2.3 容易混淆的边界

- 可能误归类到：`01.04`
- 最终判定：保持 `09`
- 判定理由：输入、输出、评价指标和 benchmark 都围绕结构分析对象，不是领域无关研究代理
- 多模块覆盖说明：无
- 01.04 判定说明：该文有清楚工程对象与跨平台实验，不符合 `01.04` 条件
- 是否需要二次复核：否；本轮已按一手全文刷新来源状态

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：否
- Multi-Agent System：是
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：否
- Hybrid Agent：是
- 其他：cross-platform code-translation agents

### 3.2 科研流程角色

- 文献检索与阅读：否
- 知识抽取与组织：是
- 科学问题提出：否
- 假设生成：否
- 实验设计：否
- 仿真建模：是
- 工具调用与代码执行：是
- 实验执行：否
- 数据分析：是
- 结果解释：部分是
- 证据评估与验证：是
- 论文写作：否
- 端到端科研流程自动化：是

### 3.3 自主能力

- 任务分解：是
- 计划生成：是
- 工具调用：是
- 记忆与状态维护：部分是
- 反馈迭代：是
- 自主决策：部分是
- 多 Agent 协作：是
- 环境交互：是
- 闭环实验：否

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：否
- 实验驱动：否
- 仿真驱动：是
- 多模态：否
- 多尺度建模：否
- 高通量筛选：否
- 知识图谱：否
- 数字孪生：否
- 机器人平台：否
- 其他：multi-software engineering workflow

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：弥补单平台结构分析代理无法覆盖真实工程工作流的问题
- 现有科研流程或方法的痛点：工程师往往需要在不同 FE 软件之间切换，人工转写成本高且容易出错
- 核心假设或直觉：先统一结构语义表示，再并行翻译到目标软件，可提高部署实用性和鲁棒性

### 4.2 系统流程

1. 输入：自然语言结构分析任务。
2. 任务分解 / 规划：多代理协同提取几何、材料、边界、荷载信息。
3. 工具、数据库、模型或实验平台调用：生成统一 JSON，并并行转写成 ETABS、SAP2000、OpenSees 脚本。
4. 中间结果反馈：检查多平台脚本的一致性与正确性。
5. 决策或迭代：根据执行结果修正推理链与脚本翻译。
6. 输出：多平台可执行结构分析脚本与分析结果。

### 4.3 系统组件

- Agent 核心：two-stage multi-agent architecture
- 工具 / API / 数据库：ETABS、SAP2000、OpenSees
- 记忆或状态模块：shared JSON representation
- 规划器：Stage 1 structured reasoning agents
- 评估器 / verifier：多平台执行准确率与重复试验一致性
- 人类反馈或专家介入：未作为主流程核心
- 实验平台或仿真环境：20 个代表性 frame problems

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：是
- 高通量计算：否
- 机器人实验：否
- 湿实验：否
- 临床数据：否
- 真实场景部署：否
- 专家评估：未强调

### 5.2 数据、任务与指标

- 数据集 / 实验对象：20 个 representative frame problems
- 任务设置：跨软件结构分析脚本自动生成与执行
- 对比基线：人工或单平台流程；不同平台脚本翻译结果
- 评价指标：十次重复试验中的准确率与稳定性
- 关键结果：ETABS、SAP2000、OpenSees 三个平台上的准确率均超过 90%
- 是否有消融实验：摘要层面未充分展开
- 是否有失败案例或负结果：仍存在 workflow acceleration 多于 discovery 的边界压力

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：否，核心贡献是结构分析 workflow 自动化
- 科学贡献是否经过验证：是
- 贡献强度判断：中
- 科学贡献类型：系统平台 / 工程分析自动化
- 证据强度：仿真支持

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单次脚本生成，而是跨多平台的结构分析工作流代理
- 与已有 Agent / 科研智能系统的区别：强调统一 JSON 语义层与并行代码翻译
- 与同一科学领域其他 Agent 文献的关系：可与单平台结构分析、多 Agent 2D/3D frame 代理共同构成 `09` 结构分析谱系
- 主要创新点：把多代理推理与多平台脚本转写结合起来，提高工程部署可用性

## 7. 局限性与风险

- Agent 自主性不足：更接近工程 workflow acceleration，而不是强 discovery loop
- 科学验证不足：主要仍是 benchmark 级验证
- 泛化性不足：当前实验聚焦 frame structural analysis
- 工具链依赖：依赖目标软件语法和建模习惯
- 数据泄漏或 benchmark 偏差：小规模题集和重复试验设置仍可能带来偏差
- 成本、可复现性或安全风险：不同平台和模型版本变化可能影响脚本稳定性
- 是否仍需进一步全文复核：否；本轮已基于一手全文完成刷新

## 8. 对综述写作的价值

- 可放入哪个章节：`09` 工程与工业技术科学中的结构分析工作流自动化子节
- 可支撑哪个论点：Agent 已从单平台分析走向多软件工程 workflow 编排
- 可用于哪个表格或图：结构分析代理家族表；`09` 与 `01.04` 边界案例表
- 适合作为代表性案例吗：适合作为工程部署导向的代表样本
- 推荐引用强度：普通引用
- 需要在正文中特别引用的页码 / 图 / 表：摘要中的 two-stage 架构与 >90% 跨平台结果
- 需要与哪些论文并列比较：`Liang_2025_Automated_Structural_Analysis`、`Geng_2026_Agentic_3D_Frame_Analysis`、`Liang_2025_MASSE_Structural_Engineering`

## 9. 总结

### 9.1 一句话概括

把一个结构分析任务同时翻译成多种有限元软件脚本的多 Agent 系统。

### 9.2 速记版 pipeline

1. 解析结构任务文本。
2. 统一整理成 JSON。
3. 并行翻译为多平台脚本。
4. 检查执行稳定性。
5. 输出结构分析结果。

### 9.3 标注字段汇总

```text
是否纳入：included
科学对象模块：09
覆盖模式：single_module
是否具有具体科学对象实验：yes
general_method_bucket：none
Primary module for filing：09
是否进入 01.04 存放区：否
主展示模块一级类：09
主展示模块二级类：09.05
主展示模块三级类：跨平台结构工程分析 / FEA workflow automation
主展示模块四级专题：Cross-platform structural-analysis agents
其他覆盖模块及对应层级路径：无
module_assignment_evidence：frame problems、统一 JSON 表示、ETABS/SAP2000/OpenSees 执行结果
multi_module_object_coverage_note：无
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Multi-Agent System; Hybrid Agent
科研流程角色：knowledge_extraction_and_organization; simulation_modeling; tool_use_and_code_execution; data_analysis; evidence_assessment_and_validation; end_to_end_research_automation
自主能力：task_decomposition; planning; tool_use; feedback_iteration; multi_agent_collaboration; environment_interaction
验证方式：benchmark; simulation_validation
交叉属性：computation_driven; simulation_driven
科学贡献类型：system_platform
证据强度：simulation_supported
归类置信度：high
纳入置信度：high
推荐引用强度：standard
first_hand_sources_checked：pdf; arxiv
classification_evidence_source_level：first_hand_full_text
note_revision_required：no
```
