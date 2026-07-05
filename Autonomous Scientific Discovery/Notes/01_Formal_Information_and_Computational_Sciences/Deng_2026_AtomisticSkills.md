# Deng 2026 - Harnessing AtomisticSkills for Agentic Atomistic Research

**论文信息**
- 标题：Harnessing AtomisticSkills for Agentic Atomistic Research
- 作者：Bowen Deng; Bohan Li; Matthew Cox; Hoje Chun; Juno Nam; Artur Lyssenko; Sathya Edamadaka; Jurgis Ruza; Xiaochen Du; Nofit Segal; Jesus Diaz Sanchez; Mingrou Xie; Ty Perez; Yu Yao; Miguel Steiner; Sauradeep Majumdar; Charles B. Musgrave III; Anirban Chandra; Abhirup Patra; Detlef Hohl; Connor W. Coley; Ju Li; Rafael Gomez-Bombarelli
- 年份：2026
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2605.24002
- PDF / 本地文件路径：`Reference_PDF/01_Formal_Information_and_Computational_Sciences/Deng_2026_AtomisticSkills.pdf`；本轮已核对 arXiv HTML full text v1，并与项目内归档 PDF 对齐
- 论文类型：系统论文 / atomistic research harness
- 当前状态：已读；已按 relaxed multi-module 口径完成复核
- 阅读日期：2026-06-23
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | arXiv HTML full text v1；项目内归档 PDF | 系统把 atomistic research tasks 封装成 skills 并由 Agent 编排执行 | 高 |
| 科学对象归类 | `03;04;07` | abstract；task descriptions；campaign examples | 材料、化学 / 催化、药物设计对象都有 concrete campaign coverage，因此不能写成 `01.04` only | 高 |
| `04` 证据 | 是 | Li-ion solid-state electrolytes；MOFs；XRD/materials tasks；Fe-oxide OER catalyst campaigns | 材料对象覆盖最强，因此 primary 设为 `04` | 高 |
| `03` 证据 | 是 | atomistic chemistry / catalysis mechanism tasks | 化学 / 催化对象提供真实 secondary 模块证据 | 高 |
| `07` 证据 | 是 | drug-design virtual-screening campaigns | 医学 / 药物发现对象覆盖明确存在 | 高 |

## 0. 摘要翻译

AtomisticSkills 试图把原子尺度研究中常见的计算与分析任务封装成可复用 skills，再由 Agent 进行编排与执行。虽然它具有明显平台和 harness 外观，但论文已经在材料、化学 / 催化、药物设计等对象上报告具体 campaign，因此本轮采用 `03;04;07`，主展示 / primary 为 `04`，并明确撤销旧的 `01.04` only 说法。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：面向明确 atomistic research 目标；具有多步任务编排；以 skill abstraction 和工具调用推进研究
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：未强调
- 在科研流程中承担的明确角色：workflow orchestration；tool use and code execution；feedback iteration；result interpretation

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：`03;04;07`
- 覆盖模式：多模块
- 是否具有具体科学对象实验、验证、benchmark task、case study 或结果报告：是
- 独立 `01.04` 存放区：none
- Primary module for filing：`04`
- Primary module for filing 说明：这是当前权威 filing convenience；当前 note 仍位于 `01` 文件夹只是旧路径，不是分类 authority
- 主展示模块一级类：`04` 材料科学
- 主展示模块二级类：atomistic materials campaigns
- 主展示模块三级类：electrolytes / MOFs / XRD / OER catalyst materials
- 主展示模块四级专题：skill-based atomistic research with materials-primary coverage
- 其他覆盖模块及对应层级路径：`03` 化学科学；`07` 医学与健康科学
- 四级专题是否为新增：否
- 是否进入独立 `01.04` 存放区：否
- 每个模块的对象实验证据：
  - `04`：Li-ion electrolytes、MOFs、XRD/materials tasks、Fe-oxide OER catalyst campaigns
  - `03`：atomistic chemistry / catalysis mechanism tasks
  - `07`：drug-design virtual screening campaigns
- 归类理由：材料对象覆盖最稳定最强；化学与医学对象都存在独立 secondary evidence
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：材料、化学 / 催化与药物设计中的原子尺度研究任务
- 最终科学问题：如何把 atomistic research tasks 组织成可复用 Agent skills
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：skills harness 是方法层实现；对象模块由具体 campaign 决定

### 2.3 容易混淆的边界

- 可能误归类到：独立 `01.04`
- 最终判定：不进入 `01.04`；采用 `03;04;07`
- 判定理由：有 concrete campaign coverage；平台外观不能覆盖对象事实
- 多模块覆盖说明：`04` 为 primary，但 `03` 与 `07` 也有真实对象覆盖，不能删成单模块
- 01.04 判定说明：否
- 是否需要二次复核：否；当前 HTML full text v1 已足够支持本轮归类

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：未强调
- Multi-Agent System：未强调
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：未强调
- Hybrid Agent：是
- 其他：skill-based atomistic research harness

### 3.2 科研流程角色

- 文献检索与阅读：未强调
- 知识抽取与组织：部分是
- 科学问题提出：部分是
- 假设生成：部分是
- 实验设计：否
- 仿真建模：是
- 工具调用与代码执行：是
- 实验执行：否
- 数据分析：是
- 结果解释：是
- 证据评估与验证：部分是
- 论文写作：否
- 端到端科研流程自动化：是

### 3.3 自主能力

- 任务分解：是
- 计划生成：是
- 工具调用：是
- 记忆与状态维护：部分是
- 反馈迭代：是
- 自主决策：是
- 多 Agent 协作：未强调
- 环境交互：是
- 闭环实验：否

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：部分是
- 实验驱动：否
- 仿真驱动：是
- 多模态：未强调
- 多尺度建模：部分是
- 高通量筛选：部分是
- 知识图谱：否
- 数字孪生：否
- 机器人平台：否
- 其他：cross-domain atomistic workflows

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：atomistic research 工具链分散，跨任务迁移与复用困难
- 现有科研流程或方法的痛点：单域脚本或单一助手难覆盖多类原子尺度研究任务
- 核心假设或直觉：把原子尺度任务封装成 skills，可提升通用研究执行能力

### 4.2 系统流程

1. 输入：atomistic research 目标
2. 任务分解 / 规划：选择对应 skills
3. 工具、数据库、模型或实验平台调用：执行计算、分析与解释工具
4. 中间结果反馈：根据输出调整后续步骤
5. 决策或迭代：在不同任务间迁移和组合 skills
6. 输出：研究结论、候选结果或工作流执行结果

### 4.3 系统组件

- Agent 核心：AtomisticSkills orchestrator
- 工具 / API / 数据库：多类 atomistic research tools
- 记忆或状态模块：有一定状态维护
- 规划器：有
- 评估器 / verifier：有
- 人类反馈或专家介入：非本轮分类关键
- 实验平台或仿真环境：以计算环境为主

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：是
- 高通量计算：部分是
- 机器人实验：否
- 湿实验：否
- 临床数据：否
- 真实场景部署：否
- 专家评估：未强调

### 5.2 数据、任务与指标

- 数据集 / 实验对象：Li-ion solid-state electrolytes；MOFs；XRD/materials tasks；Fe-oxide OER catalyst campaigns；atomistic chemistry tasks；drug-design campaigns
- 任务设置：skill-based scientific-task execution 与跨任务迁移
- 对比基线：论文原文设置
- 评价指标：任务完成质量、研究效率与工具协同能力
- 关键结果：`04` primary，`03` 与 `07` secondary 覆盖清晰
- 是否有消融实验：有部分分析
- 是否有失败案例或负结果：不是本轮分类关键

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：更偏通用研究基础设施，但具备 concrete object campaigns
- 科学贡献是否经过验证：是
- 贡献强度判断：中
- 科学贡献类型：system platform；benchmark
- 证据强度：一手 HTML full text；source_limited=no

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单一 atomistic predictor，而是 skill-based research harness
- 与已有 Agent / 科研智能系统的区别：突出 skill abstraction 与跨对象复用
- 与同一科学领域其他 Agent 文献的关系：是“平台感很强但 concrete campaigns 使其进入多模块”的典型样本
- 主要创新点：把 atomistic research pipeline 抽象成可复用 skills

## 7. 局限性与风险

- Agent 自主性不足：规划深度仍有限
- 科学验证不足：真实实验闭环较弱
- 泛化性不足：跨对象迁移强度仍需继续观察
- 工具链依赖：高
- 数据泄漏或 benchmark 偏差：需警惕
- 成本、可复现性或安全风险：异构工具链复现成本高
- 是否仍需进一步全文复核：否；当前 HTML full text v1 已足够支撑 `03;04;07`，后续只需做本地 PDF 归档同步

## 8. 对综述写作的价值

- 可放入哪个章节：materials-primary atomistic agents；`01.04` 边界纠偏案例
- 可支撑哪个论点：跨对象 demo 一旦形成 concrete campaigns，就不应继续保留 `01.04` only 叙述
- 可用于哪个表格或图：multi-module atomistic agents 表；`03 / 04 / 07` 边界表
- 适合作为代表性案例吗：适合
- 推荐引用强度：core
- 需要在正文中特别引用的页码 / 图 / 表：campaign coverage 相关部分
- 需要与哪些论文并列比较：GraphAgents；AutoSci；其他 atomistic research agents

## 9. 总结

### 9.1 一句话概括

原子尺度科研技能平台，但已具备材料主模块与化学、药物设计次覆盖。

### 9.2 速记版 pipeline

1. 接收 atomistic research 目标
2. 选择并编排 skills
3. 调用计算与分析工具
4. 根据反馈迭代
5. 输出研究结果

### 9.3 标注字段汇总

```text
是否纳入：是
科学对象模块：03;04;07
覆盖模式：multi_module
是否具有具体科学对象实验：yes
general_method_bucket：none
Primary module for filing：04
是否进入 01.04 存放区：否
主展示模块一级类：04
主展示模块二级类：atomistic materials campaigns
主展示模块三级类：electrolytes / MOFs / XRD / OER catalyst materials
主展示模块四级专题：skill-based atomistic research with materials-primary coverage
其他覆盖模块及对应层级路径：03;07
module_assignment_evidence：materials campaigns -> 04；chemistry/catalysis tasks -> 03；drug-design campaigns -> 07
multi_module_object_coverage_note：当前 note 路径仅是旧落盘；权威分类为 03;04;07，primary=04
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Hybrid Agent
科研流程角色：workflow_orchestration; tool_use_and_code_execution; feedback_iteration; result_interpretation
自主能力：task_decomposition; planning; tool_use; feedback_iteration; autonomous_decision_making; environment_interaction
验证方式：benchmark; simulation_validation
交叉属性：computation_driven; simulation_driven
科学贡献类型：system_platform; benchmark
证据强度：first_hand_full_text（arXiv HTML full text v1 + 项目内归档 PDF）
归类置信度：高
纳入置信度：高
推荐引用强度：core
```
