# Xia et al. 2025 - SR-Scientist: Scientific Equation Discovery With Agentic AI

**论文信息**
- 标题：SR-Scientist: Scientific Equation Discovery With Agentic AI
- 作者：Shijie Xia; Yuhan Sun; Pengfei Liu
- 年份：2025
- 来源 / venue：ICLR 2026 Poster / arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2510.11661
- PDF / 本地文件路径：当前无本地 PDF；本 note 基于 arXiv abstract page、OpenReview metadata 与 batch14 reviewer evidence
- 论文类型：研究论文 / equation-discovery agent framework
- 当前状态：to_read
- 阅读日期：2026-06-20
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | arXiv abstract; OpenReview TL;DR | autonomous AI scientist writes code, evaluates equations, and optimizes over a long horizon | 高 |
| 科学对象归类 | `01 / 01.04` | abstract; reviewer pack | 主要贡献是跨领域 equation-discovery agent framework 与 RL-based capability enhancement | 高 |
| 方法流程 | long-horizon tool-driven loop | abstract | analyze data -> implement equation as code -> submit for evaluation -> optimize from feedback | 高 |
| 边界判断 | 从 `01.03` 转 `01.04` | object-first review | 多学科 benchmark + framework framing 显示是通用 scientific capability system | 中高 |
| 实验验证 | benchmark / robustness / symbolic accuracy | abstract | datasets covering four science disciplines; robustness to noise; OOD generalization | 高 |

## 0. 摘要翻译

作者认为，当前许多 scientific equation discovery methods 只把 LLM 当作 equation proposer。SR-Scientist 则把它提升为 autonomous AI scientist：它会写代码分析数据、把方程实现成代码、提交评估，并基于实验反馈继续优化方程。作者还开发了 end-to-end reinforcement learning framework 来进一步增强这种 agent capability。实验覆盖 chemistry、biology、physics、material science 四个学科数据。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：有明确科研目标、长程多步行动、code-interpreter tools、反馈迭代和自主优化
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：否
- 在科研流程中承担的明确角色：数据分析、代码执行、方程评估、结果优化

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：01
- 二级类：01.04
- 三级类：
- 四级专题：Agentic scientific equation-discovery systems
- 四级专题是否为新增：否
- 归类理由：论文稳定对象是跨领域 equation-discovery agent framework，而非具体科学规律对象本体
- 归类置信度：中高

### 2.2 对象优先判定

- 最终科学研究对象：cross-domain scientific equation-discovery workflow
- 最终科学问题：如何构建长程、tool-driven 的 scientific equation-discovery agent
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：不是因为用了 RL 或 LLM 就归 01.04，而是因为论文贡献稳定落在通用科研能力平台

### 2.3 容易混淆的边界

- 可能误归类到：01.03
- 最终判定：转入 01.04
- 判定理由：方程发现只是任务外观，论文真正研究的是通用 autonomous equation-discovery agent capability
- 是否需要二次复核：可选

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：否
- Multi-Agent System：否
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：否
- Hybrid Agent：是
- 其他：RL-enhanced autonomous AI scientist

### 3.2 科研流程角色

- 文献检索与阅读：否
- 知识抽取与组织：部分是
- 科学问题提出：否
- 假设生成：是
- 实验设计：否
- 仿真建模：部分是
- 工具调用与代码执行：是
- 实验执行：否
- 数据分析：是
- 结果解释：是
- 证据评估与验证：是
- 论文写作：否
- 端到端科研流程自动化：部分是

### 3.3 自主能力

- 任务分解：是
- 计划生成：是
- 工具调用：是
- 记忆与状态维护：部分是
- 反馈迭代：是
- 自主决策：是
- 多 Agent 协作：否
- 环境交互：是
- 闭环实验：否

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 实验驱动：否
- 仿真驱动：是
- 多模态：否
- 多尺度建模：否
- 高通量筛选：否
- 知识图谱：否
- 数字孪生：否
- 机器人平台：否
- 其他：reinforcement-learning enhanced agent

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：现有 methods 把 LLM 限制在 equation proposer 角色
- 现有科研流程或方法的痛点：缺少长程、tool-driven autonomous optimization
- 核心假设或直觉：如果 agent 能写代码、评估结果并利用反馈持续优化，方程发现能力会增强

### 4.2 系统流程

1. 输入：待发现规律的数据
2. 任务分解 / 规划：决定分析、实现与评估步骤
3. 工具、数据库、模型或实验平台调用：code interpreter tools for data analysis and equation evaluation
4. 中间结果反馈：从 evaluation 得到 signal
5. 决策或迭代：基于反馈继续优化 equation
6. 输出：优化后的 equation discovery result

### 4.3 系统组件

- Agent 核心：SR-Scientist
- 工具 / API / 数据库：code interpreter; equation evaluation tools
- 记忆或状态模块：iteration history
- 规划器：long-horizon optimization policy
- 评估器 / verifier：equation evaluation loop
- 人类反馈或专家介入：minimal human-defined pipelines
- 实验平台或仿真环境：datasets across four science disciplines

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：是
- 高通量计算：否
- 机器人实验：否
- 湿实验：否
- 临床数据：否
- 真实场景部署：否
- 专家评估：否

### 5.2 数据、任务与指标

- 数据集 / 实验对象：chemistry; biology; physics; material science datasets
- 任务设置：scientific equation discovery
- 对比基线：baseline methods / equation proposers
- 评价指标：performance margin; noise robustness; OOD generalization; symbolic accuracy
- 关键结果：对 baseline 有 6%-35% 的绝对提升
- 是否有消融实验：当前摘要级证据不足
- 是否有失败案例或负结果：当前摘要级证据不足

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：重点是 workflow capability 提升
- 科学贡献是否经过验证：是
- 贡献强度判断：中
- 科学贡献类型：system_platform; general_scientific_research
- 证据强度：benchmark / computational_validation

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是 equation proposer，而是可执行分析与评估的 autonomous AI scientist
- 与已有 Agent / 科研智能系统的区别：还加入 RL framework 增强 agent capability
- 与同一科学领域其他 Agent 文献的关系：可与 KeplerAgent、STRIDE 形成 equation-discovery agent family
- 主要创新点：toolized long-horizon equation-discovery loop + RL enhancement

## 7. 局限性与风险

- Agent 自主性不足：仍主要在 benchmark 上验证
- 科学验证不足：无真实新规律发现或外部实验确认
- 泛化性不足：跨四学科 benchmark 不等于真实部署
- 工具链依赖：强
- 数据泄漏或 benchmark 偏差：需全文再看 LSR-Synth 与 RL 训练细节
- 成本、可复现性或安全风险：训练与 tool-execution cost 可能较高

## 8. 对综述写作的价值

- 可放入哪个章节：01.04 General scientific research-agent systems
- 可支撑哪个论点：跨学科 equation-discovery agent framework 更稳地应进入 01.04
- 可用于哪个表格或图：`01.03 / 01.04` 边界对照表
- 适合作为代表性案例吗：是
- 推荐引用强度：普通引用
- 需要在正文中特别引用的页码 / 图 / 表：后续全文再补
- 需要与哪些论文并列比较：ASD-0868; ASD-0869; ASD-0857

## 9. 总结

### 9.1 一句话概括

具备代码执行与反馈优化的方程发现 Agent。

### 9.2 速记版 pipeline

1. 读入数据
2. 写代码分析并实现方程
3. 提交评估
4. 读取反馈
5. 继续优化方程

### 9.3 标注字段汇总

```text
是否纳入：是
主类：01
二级类：01.04
三级类：
四级专题：Agentic scientific equation-discovery systems
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Hybrid Agent
科研流程角色：hypothesis_generation; tool_use_and_code_execution; evidence_assessment_and_validation; feedback_iteration
自主能力：task_decomposition; planning; tool_use; feedback_iteration; autonomous_decision_making
验证方式：benchmark; computational_validation
交叉属性：computation_driven; data_driven; simulation_driven
科学贡献类型：system_platform; general_scientific_research
证据强度：benchmark
归类置信度：中高
纳入置信度：高
推荐引用强度：standard
```
