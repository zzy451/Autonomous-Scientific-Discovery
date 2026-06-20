# Yadunandan and Ghosh 2025 - ReACT-Drug: Reaction-Template Guided Reinforcement Learning for de novo Drug Design

**论文信息**
- 标题：ReACT-Drug: Reaction-Template Guided Reinforcement Learning for de novo Drug Design
- 作者：R Yadunandan; Nimisha Ghosh
- 年份：2025
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2512.20958
- PDF / 本地文件路径：当前笔记基于 arXiv abstract + arXiv HTML + 官方 GitHub
- 论文类型：研究论文 / RL-based drug discovery agent
- 当前状态：to_read
- 阅读日期：2026-06-20
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | HTML method | PPO agent 在动态 action space 中多步选择 reaction templates | 高 |
| 科学对象归类 | `07 / 07.04` | title; abstract; README | 任务被直接定义为 de novo drug design for target proteins | 高 |
| 方法流程 | 工具与环境交互明确 | HTML; README | ESM-2、ChemBERTa、AutoDock Vina、reaction templates 形成迭代反馈环境 | 高 |
| 实验验证 | 计算 / docking 为主 | HTML results | 六个蛋白靶点、多目标 reward、100% validity / novelty | 高 |
| 边界判断 | 从 `03` 调到 `07` |全文主线 | reaction-template 是手段，最终对象是药物候选发现 | 高 |

## 0. 摘要翻译

作者提出 ReACT-Drug，用目标蛋白 embedding 找相似蛋白及其已知配体，构造 fragment-based 起始空间，再由 PPO agent 在化学合法的 reaction-template action space 中逐步生长分子，优化结合亲和力、药物相似性、合成可及性与新颖性。系统以目标蛋白驱动的 drug design 为核心，而不是无对象的通用分子生成。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：存在目标驱动、多步动作选择、reward 反馈、工具调用与环境交互
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 计划生成：是
- 工具调用：是
- 反馈迭代：是
- 自主决策：是
- 多 Agent 协作：否
- 在科研流程中承担的明确角色：候选初始化、分子编辑、评分、优化与筛选

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：07
- 二级类：07.04
- 三级类：
- 四级专题：Target-protein-conditioned de novo drug design agents
- 四级专题是否为新增：否
- 归类理由：文章的问题定义、输入对象、reward 设计与结果解释都围绕 drug discovery
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：target-protein-conditioned drug candidates
- 最终科学问题：如何在合成可行的化学变换空间中搜索更优药物候选
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：reaction templates 与 RL 是实现路径，不是主对象

### 2.3 容易混淆的边界

- 可能误归类到：03.04
- 最终判定：从 03.04 调整到 07.04
- 判定理由：如果只是通用分子 / 反应优化可归 03，但本文从 target protein、drug ligands、binding affinity 到候选解释都稳定锁定药物发现对象
- 是否需要二次复核：当前不需要

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：否
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：是
- Multi-Agent System：否
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：否
- Hybrid Agent：是
- 其他：Reinforcement Learning Agent

### 3.2 科研流程角色

- 文献检索与阅读：否
- 知识抽取与组织：部分是
- 科学问题提出：否
- 假设生成：是
- 实验设计：否
- 仿真建模：是
- 工具调用与代码执行：是
- 实验执行：否
- 数据分析：是
- 结果解释：部分是
- 证据评估与验证：是
- 论文写作：否
- 端到端科研流程自动化：部分是

### 3.3 自主能力

- 任务分解：部分是
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
- 其他：protein-conditioned molecular design

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：在 target-protein 驱动的药物设计中引入化学合法、可解释的多步分子编辑
- 现有科研流程或方法的痛点：通用生成方法难兼顾靶点信息、合成可行性与新颖性
- 核心假设或直觉：把动作空间限制在 reaction-template transformations 中，可提升药物候选搜索质量

### 4.2 系统流程

1. 输入：目标蛋白与相似蛋白已知配体
2. 任务分解 / 规划：构造 fragment-based 起始空间
3. 工具、数据库、模型或实验平台调用：ESM-2、ChemBERTa、reaction templates、AutoDock Vina
4. 中间结果反馈：binding affinity、QED、SA、novelty reward
5. 决策或迭代：PPO agent 选择下一步化学变换
6. 输出：更优 de novo drug candidates

### 4.3 系统组件

- Agent 核心：PPO reinforcement-learning agent
- 工具 / API / 数据库：ESM-2、ChemBERTa、AutoDock Vina、reaction templates
- 记忆或状态模块：molecular state / action history
- 规划器：dynamic action-space policy
- 评估器 / verifier：multi-objective reward
- 人类反馈或专家介入：否
- 实验平台或仿真环境：protein-target docking workflow

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

- 数据集 / 实验对象：六个蛋白靶点
- 任务设置：de novo drug design with reaction-template-guided RL
- 对比基线：相关分子生成 / 优化方法
- 评价指标：binding affinity、QED、SA、novelty、validity
- 关键结果：多靶点上报告 100% validity / novelty，并给出 docking 表现
- 是否有消融实验：有
- 是否有失败案例或负结果：未突出

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：主要是 drug design workflow 创新
- 科学贡献是否经过验证：是
- 贡献强度判断：中
- 科学贡献类型：设计 / 预测 / 系统平台
- 证据强度：计算验证

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是静态分子生成，而是动态 action space 中的多步 RL Agent
- 与已有 Agent / 科研智能系统的区别：对象强绑定 target-protein drug design
- 与同一科学领域其他 Agent 文献的关系：与 FRAGMENTA、ToolMol 构成高压 03/07 边界组
- 主要创新点：reaction-template-guided RL for target-driven drug design

## 7. 局限性与风险

- Agent 自主性不足：单 Agent 为主
- 科学验证不足：缺少湿实验和临床转化验证
- 泛化性不足：对靶点、模板库与 docking 流程依赖明显
- 工具链依赖：强
- 数据泄漏或 benchmark 偏差：需要持续留意
- 成本、可复现性或安全风险：主要为 in silico 层

## 8. 对综述写作的价值

- 可放入哪个章节：07 医学与健康科学 / 药物发现 Agent
- 可支撑哪个论点：药物发现对象应压过化学方法外观决定主类
- 可用于哪个表格或图：03/07 边界表；drug-design agent 对比表
- 适合作为代表性案例吗：适合做边界纠偏样本
- 推荐引用强度：普通引用
- 需要在正文中特别引用的页码 / 图 / 表：系统流程与 results
- 需要与哪些论文并列比较：FRAGMENTA、ToolMol、PROBE

## 9. 总结

### 9.1 一句话概括

面向目标蛋白的 reaction-template RL 药物设计 Agent。

### 9.2 速记版 pipeline

1. 输入目标蛋白
2. 找相似蛋白与配体
3. 用模板化学变换扩展分子
4. 依据多目标 reward 迭代
5. 输出更优药物候选

### 9.3 标注字段汇总

```text
是否纳入：是
主类：07
二级类：07.04
三级类：
四级专题：Target-protein-conditioned de novo drug design agents
Agent 类型：Planning Agent; Tool-using Agent; Retrieval-augmented Agent; Hybrid Agent; Reinforcement Learning Agent
科研流程角色：hypothesis_generation; simulation_modeling; tool_use_and_code_execution; data_analysis; evidence_assessment_and_validation
自主能力：planning; tool_use; feedback_iteration; autonomous_decision_making; environment_interaction
验证方式：benchmark; simulation_validation
交叉属性：computation_driven; data_driven; simulation_driven
科学贡献类型：design; prediction; system_platform
证据强度：computationally_validated
归类置信度：高
纳入置信度：高
推荐引用强度：standard
```

