# Liang et al. 2025 - Automating Structural Engineering Workflows with Large Language Model Agents

**论文信息**
- 标题：Automating Structural Engineering Workflows with Large Language Model Agents
- 作者：Haoran Liang; Yufa Zhou; Mohammad Talebi Kalaleh; Qipei Mei
- 年份：2025
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2510.11004
- PDF / 本地文件路径：当前笔记基于 arXiv abstract / PDF
- 论文类型：研究论文 / structural engineering multi-agent workflow system
- 当前状态：to_read
- 阅读日期：2026-06-20
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | arXiv abstract | 明确提出 `MASSE`，自称是 structural engineering 的 Multi-Agent System | 高 |
| 多步行动 | 是 | PDF §3-§4 | Analyst / Engineer / Management 三组 agent 协作完成规范解释、建模、校核与 adequacy decision | 高 |
| 工具调用 | 是 | PDF Fig.3-4 | 调用 FEM tools、technical documents、building codes、Python scripts | 高 |
| 科学对象归类 | `09.05` | title / abstract / intro | 对象是结构工程 workflows、load calculation、capacity verification、analysis / design tasks | 高 |
| 边界判断 | 不转 `01.04` | abstract / methods | 通用 workflow 外观很强，但输入、知识源、校核逻辑和案例都围绕结构工程对象 | 高 |
| 主要剩余风险 | core-strength risk | results / conclusion | 更像强工程分析自动化，而不是更强“新科学发现”型核心样本 | 中高 |

## 0. 摘要翻译

本文提出 `MASSE`，将大语言模型 Agent 与真实结构工程流程结合，自动完成设计规范解读、荷载计算、结构建模、承载力校核与安全判定。作者认为 LLM 在复杂推理、长程规划与工具使用上的能力已与结构工程任务较为契合，因此用一个 training-free 的 multi-agent system 去自动化大多数真实结构工程工作流。论文在真实案例上验证了其效果，声称能把专家两小时左右的工作压缩到几分钟，并提高可靠性与准确率。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：存在明确目标、多步分工、多 Agent 协作、工具调用、反馈校核和最终决策
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：是
- 在科研流程中承担的明确角色：结构分析、规范解释、荷载计算、承载力校核、工程判定

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：09
- 二级类：09.05
- 三级类：结构工程工作流与结构分析
- 四级专题：Structural-engineering workflow agents
- 四级专题是否为新增：否
- 归类理由：论文处理的对象始终是 buildings / bridges / infrastructure 的结构工程任务本体
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：结构工程工作流、结构分析、荷载与承载力判定
- 最终科学问题：如何用多 Agent 自动完成真实结构工程流程
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：multi-agent orchestration 只是手段，主对象仍然是具体结构工程对象

### 2.3 容易混淆的边界

- 可能误归类到：01.04
- 最终判定：保持 09.05
- 判定理由：building code、FEM tool、案例和 adequacy decision 都牢牢锚定结构工程对象
- 是否需要二次复核：建议

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：是
- Multi-Agent System：是
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：部分是
- Hybrid Agent：是
- 其他：structural engineering workflow agents

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
- 数据驱动：否
- 实验驱动：否
- 仿真驱动：是
- 多模态：否
- 多尺度建模：否
- 高通量筛选：否
- 知识图谱：否
- 数字孪生：否
- 机器人平台：否
- 其他：code / standards / FEM coupled workflow

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：把长期低自动化的结构工程流程转成可部署的 LLM-agent workflow
- 现有科研流程或方法的痛点：规范解释、荷载计算和承载力校核高度依赖专家人工
- 核心假设或直觉：LLM 的长程规划、复杂推理与工具使用能力适合结构工程任务

### 4.2 系统流程

1. 输入：工程任务、设计要求、规范与技术文档
2. 任务分解 / 规划：由 Analyst / Engineer / Management agents 分工
3. 工具、数据库、模型或实验平台调用：调用 FEM tools、codes、Python scripts
4. 中间结果反馈：对建模、荷载、校核结果做检查
5. 决策或迭代：输出 adequacy decision 与工作流结论
6. 输出：自动化结构工程分析 / 设计判定

### 4.3 系统组件

- Agent 核心：MASSE
- 工具 / API / 数据库：FEM tools、building codes、technical documents、scripts
- 记忆或状态模块：workflow state and shared context
- 规划器：Management layer
- 评估器 / verifier：capacity checks / adequacy decision
- 人类反馈或专家介入：真实工程师对比评估
- 实验平台或仿真环境：real-world case studies

## 5. 实验与验证

### 5.1 验证方式

- benchmark：部分是
- 仿真验证：是
- 高通量计算：否
- 机器人实验：否
- 湿实验：否
- 临床数据：否
- 真实场景部署：部分是
- 专家评估：是

### 5.2 数据、任务与指标

- 数据集 / 实验对象：real-world structural engineering cases
- 任务设置：设计规范解释、荷载计算、结构分析、adequacy decision
- 对比基线：11 位工程师人工流程
- 评价指标：耗时、可靠性、准确性
- 关键结果：约 132 分钟压缩到约 2 分钟
- 是否有消融实验：摘要级未充分展开
- 是否有失败案例或负结果：需全文继续核

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：更偏工程工作流自动化
- 科学贡献是否经过验证：是
- 贡献强度判断：中
- 科学贡献类型：系统平台 / 工程分析
- 证据强度：真实案例 + 专家评估

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单次预测，而是 end-to-end 结构工程 workflow automation
- 与已有 Agent / 科研智能系统的区别：更接近可部署的 professional structural-engineering system
- 与同一科学领域其他 Agent 文献的关系：可与 0755 / 0756 / VFEAgent / 0752 / 0753 构成结构分析样本簇
- 主要创新点：把 building-code interpretation、FEM、capacity checks 和最终 decision 串成多 Agent 系统

## 7. 局限性与风险

- Agent 自主性不足：虽是强 workflow automation，但更像工程自动化而非更强 discovery loop
- 科学验证不足：主要仍是 case-study / workflow validation
- 泛化性不足：对更广工程对象的稳定性仍需继续观察
- 工具链依赖：高度依赖 codes、technical docs 与 FEM stack
- 数据泄漏或 benchmark 偏差：需后续核
- 成本、可复现性或安全风险：真实工程部署安全性仍需谨慎

## 8. 对综述写作的价值

- 可放入哪个章节：09 工程与工业技术科学中的结构工程 analysis agents
- 可支撑哪个论点：Agent 已进入具体工程分析与判定流程
- 可用于哪个表格或图：structural-analysis 子群对比表；`09 / 01.04` 边界样本表
- 适合作为代表性案例吗：可作为工程 workflow 强样本，但需注明 core-strength 风险
- 推荐引用强度：普通引用
- 需要在正文中特别引用的页码 / 图 / 表：workflow architecture；real-world case comparison
- 需要与哪些论文并列比较：Geng_2026_CrossPlatform_Structural_Analysis; Geng_2026_Agentic_3D_Frame_Analysis; Liang_2025_Automated_Structural_Analysis

## 9. 总结

### 9.1 一句话概括

多 Agent 自动完成结构工程流程。

### 9.2 速记版 pipeline

1. 读取任务与规范
2. 分工解释与建模
3. 调 FEM / scripts
4. 做校核与 adequacy decision
5. 输出判定

### 9.3 标注字段汇总

```text
是否纳入：to_read
主类：09
二级类：09.05
三级类：结构工程工作流与结构分析
四级专题：Structural-engineering workflow agents
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Retrieval-augmented Agent; Multi-Agent System; Hybrid Agent
科研流程角色：knowledge_extraction_and_organization; simulation_modeling; tool_use_and_code_execution; data_analysis; result_interpretation; evidence_assessment_and_validation; end_to_end_research_automation
自主能力：task_decomposition; planning; tool_use; feedback_iteration; autonomous_decision_making; multi_agent_collaboration; environment_interaction
验证方式：simulation_validation; real_world_deployment; expert_evaluation
交叉属性：computation_driven; simulation_driven
科学贡献类型：system_platform
证据强度：real_world_deployment
归类置信度：高
纳入置信度：高
推荐引用强度：standard
```
