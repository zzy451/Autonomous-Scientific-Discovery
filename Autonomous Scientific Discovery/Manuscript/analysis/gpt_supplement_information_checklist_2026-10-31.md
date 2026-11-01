# GPT 意见中提炼的综述补充信息清单

> 本文件仅摘录 GPT 意见中提出的“综述还需要补充哪些信息”，用于后续写作规划；不表示这些内容已经全部核实或已经写入英文正文。

## 1. 明确核心概念与论文主线

- 明确 Scientific Agent 的定义与边界。
- 强调 Agent 不是由某一种模型架构定义，而是由其在科学环境中组织和执行目标导向行动的能力定义。
- 解释 Agent 与普通预测模型、固定自动化流程、Agent-based Simulation 的区别。
- 说明 Agent 不一定要求 LLM、完全自主、多 Agent 或实体机器人。
- 全文围绕以下问题组织：
  - **WHERE**：Agent 进入哪些科学领域？
  - **WHAT**：Agent 承担哪些科研角色？
  - **HOW**：Agent 采用哪些技术范式？
  - **HOW WELL**：Agent 的自主程度和科学证据如何？
  - Agent 如何跨学科参与科研，哪些因素决定其有效性和科学意义？

## 2. 引言中补充 Agent for Science 的发展逻辑

- 说明从传统 AI for Science 到 Agentic Science 的转变。
- 说明传统 AI 往往解决单一任务，而科研过程包括问题提出、文献调查、假设生成、实验设计、执行、分析和验证等相互依赖的环节。
- 说明 Agent 的价值在于组织多个科研行动，而不是只完成一次预测。
- 补充 Scientific Agent 的历史演进：
  - 早期符号推理、规划和知识系统；
  - 自主科学系统、航天系统与机器人；
  - 贝叶斯优化、主动学习和自适应控制；
  - LLM-based Agent 与 Hybrid Agent。
- 说明不同范式是能力扩展和共存关系，而不是简单的技术代际替代。

## 3. 补充研究问题

- **RQ1**：Agent 进入哪些科学领域，研究哪些 Scientific Objects？
- **RQ2**：Agent 承担哪些科研角色和行动？
- **RQ3**：不同技术范式如何支持这些科研活动？
- **RQ4**：不同环境中的自主程度和人机协作如何？
- **RQ5**：Agent 的科学贡献获得了什么程度的证据支持？
- **RQ6**：不同领域之间有哪些共同机制、差异和迁移机会？

## 4. 完善分类框架

### Agent Paradigms

- Symbolic / Knowledge-based
- Planning / Model-based
- Optimization / Probabilistic
- Learning-based
- LLM-based
- Hybrid

需要说明：

- 范式标签可以多选。
- Robotic Agent 表示执行环境或具身形态。
- Multi-Agent 表示组织结构。
- Robotic Agent 和 Multi-Agent 不应与决策范式混为一谈。

### Research Roles

- Knowledge Acquisition
- Question and Hypothesis Generation
- Research Planning and Design
- Experimentation and Execution
- Data Analysis and Interpretation
- Validation and Communication

### Execution Environments

- Digital / Knowledge
- Computational / Simulation
- Laboratory / Robotic
- Field / Observational
- Space / Autonomous Exploration
- Clinical / Operational

### Organization

- Single-agent
- Multi-agent
- Human–Agent collaboration

## 5. 补充自主性与人机协作信息

需要记录科研流程中的责任归属：

- 谁定义目标；
- 谁提出假设；
- 谁选择实验；
- 谁批准执行；
- 谁处理失败；
- 谁解释结果。

同时需要区分：

- Agent 能否自主执行；
- Agent 是否能够正确完成任务；
- Agent 是否产生了经过科学验证的新知识。

## 6. 补充科学证据分层

建议将证据分为：

- **Operational Success**：流程或系统是否成功运行；
- **Task-level Correctness**：任务结果是否正确；
- **Scientific Validation**：结果是否经过实验、观测、临床或外部验证；
- **Scientific Discovery**：是否产生新的科学知识、规律、材料、机制或发现。

化学领域尤其需要区分：

- 成功执行已有反应；
- 提高反应筛选效率；
- 发现新的反应路径；
- 实际合成并表征新的化合物。

其他领域也应按照相同逻辑区分工作流成功、任务正确、实验或观测验证，以及新科学知识。

## 7. 为 11 个领域补充统一比较信息

每个领域都应尽量补充以下六类信息：

- **Scientific Context and Research Objects**：研究对象和科学背景；
- **Agent Roles in Scientific Workflows**：Agent 承担的科研角色；
- **Agent Paradigms and System Designs**：采用的技术范式和系统结构；
- **Interaction, Feedback and Adaptation**：工具、环境、反馈和适应机制；
- **Human Involvement and Autonomy**：人类介入方式和自主程度；
- **Scientific Outcomes and Evidence**：科学产出及其验证证据。

## 8. 增加跨领域综合分析

建议补充以下内容：

- 不同领域共享的科研工作流模式；
- 不同 Agent 范式之间的互补关系；
- 不同领域的环境约束和反馈来源；
- 自主程度与人机协作差异；
- 科学贡献和证据强度差异；
- 技术和任务在不同领域之间的可迁移性。

技术范式比较应讨论“什么任务适合什么范式”，例如：

- LLM：理解科学目标、生成候选方案；
- Symbolic Planner：约束检查和计划生成；
- Bayesian Optimizer：选择下一轮实验；
- Robotic Controller：执行实验；
- Verification Module：验证科学要求。

不应预设 Hybrid Agent 一定优于其他范式。

## 9. 分析领域差异与迁移边界

需要说明不同学科对 Agent 的核心要求不同：

- 数学：逻辑正确性；
- 化学：实验可行性和产物表征；
- 生物学：复杂机制和因果解释；
- 医学：临床证据、安全性和适用范围；
- 天文学：观测窗口、设备资源和环境约束。

同时说明：

- 任务分解、工具编排和状态管理具有一定通用性；
- 领域科学判断、实验可行性和证据标准不能直接迁移。

## 10. 补充挑战与未来方向

- Scientific Goal Formation；
- Long-horizon Autonomy；
- Scientific Reasoning；
- Physical-world Integration；
- Scientific Memory；
- Cross-domain Transfer；
- Human–Agent Collaboration；
- Reproducibility。

重点未来方向包括：

- 从任务执行走向科学问题和假设发现；
- 从单一 Agent 走向 Hybrid Scientific Systems；
- 从孤立任务成功走向可积累、可验证的科学知识。

## 11. 建议新增或完善的图表

- Overall Conceptual Framework；
- Historical Evolution and Agent Paradigms；
- Scientific Research Workflow；
- Scientific Domain Landscape；
- Domain × Workflow × Paradigm Matrix；
- Future Scientific Agent Ecosystem；
- Agent 定义与纳入标准表；
- Agent 技术范式比较表；
- Scientific Domains × Scientific Objects 表；
- 各领域代表系统比较表；
- Agent Actions × Human Responsibilities × Autonomy 表；
- 科学成果类型 × 验证证据表；
- 跨领域挑战与未来方向表。

## 12. 总体写作原则

- 以科学领域作为正文主体结构；
- 以科研工作流组织每个领域内部内容；
- 以 Agent 范式进行跨领域技术比较；
- 以自主性和人机协作分析 Agent 的参与程度；
- 以科学证据评价 Agent 的最终贡献；
- 不把 Traditional Agent → LLM Agent → Hybrid Agent 写成单线进化叙事；
- 不将所有 AI for Science 工作都视为 Scientific Agent；
- 不只比较技术能力，还要比较 Agent 对科学研究的实际贡献。
