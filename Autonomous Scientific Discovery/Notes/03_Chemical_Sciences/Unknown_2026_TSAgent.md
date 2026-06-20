# Unknown 2026 - TSAgent: An Agentic Workflow for Autonomous Transition State Search

**论文信息**
- 标题：TSAgent: An Agentic Workflow for Autonomous Transition State Search
- 作者：Unknown
- 年份：2026
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2605.14154
- PDF / 本地文件路径：当前笔记基于 arXiv abstract
- 论文类型：预印本 / transition-state-search agent
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | arXiv abstract | TS search 被定义为 long-horizon multi-step workflow，系统有 plan-execute-analyze-replan loop | 中高 |
| 科学对象归类 | `03.03` | abstract | 文章聚焦 mechanistic studies of catalytic materials 中的 TS identification bottleneck | 中高 |
| 多步反馈 | 是 | abstract | 系统根据 convergence diagnostics 与 geometric feedback 自适应调整策略 | 中高 |
| 评测对象 | 催化机理而非材料性能 | abstract | 使用 OC20NEB heterogeneous catalysis benchmark，并复现 NH3 dissociation 的 BEP scaling | 中高 |
| 边界判断 | 不应归 `04` | abstract | 论文研究的是 TS、势能面与反应机理，不是材料组成 / 结构 / 性能发现 | 中高 |

## 0. 摘要翻译

论文提出 TSAgent，用于以 DFT 级精度自动执行过渡态搜索。作者把 TS search 视为长程、多步、需要持续反馈调整的催化机理工作流，并设计了 plan-execute-analyze-replan loop 来处理收敛诊断和几何反馈。系统在 OC20NEB 异相催化 benchmark 上验证，并复现了 NH3 dissociation on metal and single-atom alloy surfaces 的 BEP scaling 关系。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：存在长期多步 workflow、规划、工具调用、反馈迭代和自动决策
- 判定置信度：中高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：未明确
- 在科研流程中承担的明确角色：过渡态搜索、收敛诊断、反应路径分析

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：03
- 二级类：03.03
- 三级类：催化反应机理与过渡态搜索
- 四级专题：autonomous transition-state-search agents
- 四级专题是否为新增：否
- 归类理由：最终对象是催化反应机理与 TS identification，而不是材料性能主问题
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：催化反应机理与过渡态
- 最终科学问题：如何用 Agent 自动完成 DFT 级 TS search 并复现关键机理关系
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：workflow 只是手段，稳定对象是 catalytic mechanism studies

### 2.3 容易混淆的边界

- 可能误归类到：04
- 最终判定：保留 03.03
- 判定理由：即使对象落在 catalytic material surfaces，上文的科学问题仍是反应机理、TS 和 BEP scaling
- 是否需要二次复核：是

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：否
- Multi-Agent System：未明确
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：否
- Hybrid Agent：是
- 其他：autonomous TS workflow

### 3.2 科研流程角色

- 文献检索与阅读：否
- 知识抽取与知识组织：否
- 科学问题提出：否
- 假设生成：否
- 实验设计：否
- 仿真建模：是
- 工具调用与代码执行：是
- 实验执行：否
- 数据分析：是
- 结果解释：是
- 证据评估与假设验证：是
- 论文写作：否
- 端到端科研流程自动化：是

### 3.3 自主能力

- 任务分解：是
- 计划生成：是
- 工具调用：是
- 记忆与状态维护：是
- 反馈迭代：是
- 自主决策：是
- 多 Agent 协作：未明确
- 环境交互：是
- 闭环实验：否

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：否
- 实验驱动：否
- 仿真驱动：是
- 多模态：否
- 多尺度建模：是
- 高通量筛选：否
- 知识图谱：否
- 数字孪生：否
- 机器人平台：否
- 其他：DFT workflow

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：TS identification 是催化机理研究中的关键瓶颈
- 现有科研流程或方法的痛点：TS search 不是单次计算，而是长链反复调整过程
- 核心假设或直觉：若把 TS search 写成 plan-execute-analyze-replan loop，就能提升自主机理搜索能力

### 4.2 系统流程

1. 输入：催化反应体系与初始结构
2. 任务分解 / 规划：生成 TS search plan
3. 工具、数据库、模型或实验平台调用：执行 DFT-level TS search steps
4. 中间结果反馈：读取 convergence diagnostics 与 geometric feedback
5. 决策或迭代：重规划并继续搜索
6. 输出：TS identification 与机理结果

### 4.3 系统组件

- Agent 核心：TSAgent
- 工具 / API / 数据库：DFT / NEB-like search workflow
- 记忆或状态模块：search state 与 diagnostics
- 规划器：plan-execute-analyze-replan loop
- 评估器 / verifier：success rate、benchmark 与 BEP scaling reproduction
- 人类反馈或专家介入：当前摘要级信息未突出
- 实验平台或仿真环境：OC20NEB heterogeneous catalysis benchmark

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：是
- 高通量计算：否
- 机器人实验：否
- 湿实验：否
- 临床数据：否
- 真实场景部署：否
- 专家评估：是

### 5.2 数据、任务与指标

- 数据集 / 实验对象：OC20NEB 100 例；NH3 dissociation on metal and single-atom alloy surfaces
- 任务设置：自动 TS search
- 对比基线：expert DFT practitioners
- 评价指标：search success rate 与机理复现能力
- 关键结果：约 70% success rate，并复现 BEP scaling
- 是否有消融实验：当前摘要级笔记未展开
- 是否有失败案例或负结果：当前摘要级笔记未展开

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：更偏催化机理搜索自动化
- 科学贡献是否经过验证：是
- 贡献强度判断：中
- 科学贡献类型：system_platform / computational_chemistry
- 证据强度：仍需全文复核

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：直接承担 TS search 与机理分析任务，而不是静态预测
- 与已有 Agent / 科研智能系统的区别：围绕 TS bottleneck 设计长链 autonomous workflow
- 与同一科学领域其他 Agent 文献的关系：可作为 `03` 类较干净的催化机理 Agent 样本
- 主要创新点：把 TS search 从一次性工具调用升级为可重规划的 agent workflow

## 7. 局限性与风险

- Agent 自主性不足：当前强证据主要来自摘要
- 科学验证不足：需要全文确认 workflow 细节、失败模式与人工边界
- 泛化性不足：不同催化家族上的泛化能力尚不充分
- 工具链依赖：高度依赖 DFT / NEB 工作流稳定性
- 数据泄漏或 benchmark 偏差：benchmark 构造可能影响结论
- 成本、可复现性或安全风险：DFT 级 TS search 成本较高
- 是否仍需进一步全文复核：是

## 8. 对综述写作的价值

- 可放入哪个章节：计算催化机理 Agent
- 可支撑哪个论点：若最终科学问题是反应机理和 TS identification，应优先保留在 `03`
- 可用于哪个表格或图：`03 / 04` 边界案例对比
- 适合作为代表性案例吗：是
- 推荐引用强度：普通引用
- 需要在正文中特别引用的页码 / 图 / 表：OC20NEB 与 BEP scaling 结果
- 需要与哪些论文并列比较：ASD-0664

## 9. 总结

### 9.1 一句话概括

用 Agent workflow 自动做催化过渡态搜索。

### 9.2 速记版 pipeline

1. 规划 TS search
2. 跑 DFT 级搜索步骤
3. 读收敛与几何反馈
4. 重规划直到找到 TS

### 9.3 标注字段汇总

```text
是否纳入：是
主类：03
二级类：03.03
三级类：催化反应机理与过渡态搜索
四级专题：autonomous transition-state-search agents
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Hybrid Agent
科研流程角色：simulation_modeling; tool_use_and_code_execution; data_analysis; result_interpretation; evidence_assessment_and_validation; end_to_end_research_automation
自主能力：task_decomposition; planning; tool_use; memory_or_state_tracking; feedback_iteration; autonomous_decision_making; environment_interaction
验证方式：benchmark; computational_validation; expert_evaluation
交叉属性：computation_driven; simulation_driven; multiscale_modeling
科学贡献类型：system_platform
证据强度：medium_pending_full_text
归类置信度：高
纳入置信度：中高
推荐引用强度：普通引用
```
