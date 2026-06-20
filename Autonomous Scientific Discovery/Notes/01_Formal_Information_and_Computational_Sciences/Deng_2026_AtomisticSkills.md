# Deng 2026 - Harnessing AtomisticSkills for Agentic Atomistic Research

**论文信息**
- 标题：Harnessing AtomisticSkills for Agentic Atomistic Research
- 作者：Bowen Deng; Bohan Li; Matthew Cox; Hoje Chun; Juno Nam; Artur Lyssenko; Sathya Edamadaka; Jurgis Ruza; Xiaochen Du; Nofit Segal; Jesus Diaz Sanchez; Mingrou Xie; Ty Perez; Yu Yao; Miguel Steiner; Sauradeep Majumdar; Charles B. Musgrave III; Anirban Chandra; Abhirup Patra; Detlef Hohl; Connor W. Coley; Ju Li; Rafael Gomez-Bombarelli
- 年份：2026
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2605.24002
- PDF / 本地文件路径：当前笔记基于 arXiv abstract 与 reviewer 一手证据整理
- 论文类型：系统论文 / atomistic research harness
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | arXiv abstract | 构建 agentic atomistic research 系统，并显式组织 research skills 与 tool use | 高 |
| 科学对象归类 | `01.04` | arXiv abstract | 主对象是跨领域 atomistic research harness，不是单一材料、化学或药物对象 | 高 |
| 方法流程 | 多工具研究编排 | arXiv abstract；reviewer evidence | 通过 AtomisticSkills 支持不同 atomistic research tasks 的调用与组织 | 中高 |
| 边界判断 | 不回到 `04` 或 `03` | arXiv abstract；reviewer evidence | 虽覆盖材料、化学、药物多个对象，但贡献集中在跨域研究基础设施 | 中高 |
| 风险判断 | class risk 已下降，全文仍需补强 | reviewer evidence | 当前主要剩余不确定性是全文中各 case 的权重和验证深度 | 中高 |

## 0. 摘要翻译

论文提出 AtomisticSkills/agentic atomistic research 框架，希望把原子尺度研究中常见的计算与分析任务封装为可复用技能，再由 Agent 进行编排和执行。当前证据显示，它虽然覆盖材料、化学和药物设计等案例，但最稳定的研究对象不是某一具体学科对象，而是通用 atomistic research 的能力基座。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：面向科研目标；具备多步任务编排；通过技能化工具调用支持研究执行
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：部分是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：部分是
  - 多 Agent 协作：未明确
- 在科研流程中承担的明确角色：工作流编排、工具执行、结果解释、跨任务迁移

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
- 四级专题：Agentic atomistic-research harness systems
- 四级专题是否为新增：否
- 归类理由：论文的稳定核心是可复用 atomistic research 技能和通用编排框架，而非单一具体科学对象
- 归类置信度：中高

### 2.2 对象优先判定

- 最终科学研究对象：通用 atomistic research workflow / skills harness
- 最终科学问题：如何把原子尺度研究中的异构工具与流程组织为可复用 Agent 技能系统
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：即便有材料或化学 case，主贡献仍是跨对象研究基础设施

### 2.3 容易混淆的边界

- 可能误归类到：04；03；07
- 最终判定：保留 01.04
- 判定理由：跨案例展示不足以把通用 harness 重新压回单一对象类
- 是否需要二次复核：是，主要查看全文中 case 比重与主张边界

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：部分是
- Tool-using Agent：是
- Retrieval-augmented Agent：未明确
- Multi-Agent System：未明确
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：未明确
- Hybrid Agent：是
- 其他：skill-based research harness

### 3.2 科研流程角色

- 文献检索与阅读：未明确
- 知识抽取与组织：部分是
- 科学问题提出：未明确
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

- 任务分解：部分是
- 计划生成：部分是
- 工具调用：是
- 记忆与状态维护：未明确
- 反馈迭代：是
- 自主决策：部分是
- 多 Agent 协作：未明确
- 环境交互：是
- 闭环实验：否

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：部分是
- 实验驱动：否
- 仿真驱动：是
- 多模态：未明确
- 多尺度建模：部分是
- 高通量筛选：未明确
- 知识图谱：否
- 数字孪生：否
- 机器人平台：否
- 其他：cross-domain atomistic workflows

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：atomistic research 工具链分散、迁移困难、跨任务复用弱
- 现有科研流程或方法的痛点：单个脚本或单域助手难覆盖多种 atomistic research 任务
- 核心假设或直觉：将 atomistic tasks 封装为 skills，可提升通用研究执行能力

### 4.2 系统流程

1. 输入：atomistic research 目标
2. 任务分解 / 规划：选择对应 skills
3. 工具、数据库、模型或实验平台调用：执行计算、分析与解释工具
4. 中间结果反馈：根据输出调整后续步骤
5. 决策或迭代：在不同任务之间迁移与组合技能
6. 输出：研究结论、候选结果或工作流执行结果

### 4.3 系统组件

- Agent 核心：AtomisticSkills orchestrator
- 工具 / API / 数据库：多类 atomistic research tools
- 记忆或状态模块：摘要未明确
- 规划器：存在技能选择与编排逻辑
- 评估器 / verifier：存在结果评估
- 人类反馈或专家介入：未明确
- 实验平台或仿真环境：主要是计算环境

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：是
- 高通量计算：部分是
- 机器人实验：否
- 湿实验：否
- 临床数据：否
- 真实场景部署：否
- 专家评估：未明确

### 5.2 数据、任务与指标

- 数据集 / 实验对象：跨材料、化学、药物设计等 atomistic cases
- 任务设置：技能化科研任务执行与跨任务迁移
- 对比基线：摘要未完全展开
- 评价指标：任务完成质量、研究效率、工具协同能力
- 关键结果：证明通用 atomistic skills 可以被 Agent 编排用于多类对象
- 是否有消融实验：待全文核实
- 是否有失败案例或负结果：待全文核实

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：更偏通用研究基础设施
- 科学贡献是否经过验证：部分是
- 贡献强度判断：中
- 科学贡献类型：system_platform; general_scientific_research
- 证据强度：medium_pending_full_text

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单个 atomistic predictor，而是技能化研究系统
- 与已有 Agent / 科研智能系统的区别：强调 skill abstraction 与跨对象复用
- 与同一科学领域其他 Agent 文献的关系：与 AutoResearchClaw、AutoSci 同属偏平台型 01.04 分支
- 主要创新点：把 atomistic research pipeline 抽象为可复用技能集合

## 7. 局限性与风险

- Agent 自主性不足：摘要层面仍难判断规划深度
- 科学验证不足：现阶段主证据仍是 abstract 与 reviewer 一手阅读
- 泛化性不足：需确认是否真的跨对象稳定，而不只是多 case 展示
- 工具链依赖：高
- 数据泄漏或 benchmark 偏差：待全文核查
- 成本、可复现性或安全风险：异构工具链复现成本高
- 是否仍需进一步全文复核：是；重点核查 case 权重与验证细节

## 8. 对综述写作的价值

- 可放入哪个章节：01.04 通用科研平台 / 通用 scientific workflow
- 可支撑哪个论点：跨领域 demo 不能自动把平台型系统压到具体学科类
- 可用于哪个表格或图：01.04 与 concrete-domain 边界样本表
- 适合作为代表性案例吗：适合做边界样本
- 推荐引用强度：core
- 需要在正文中特别引用的页码 / 图 / 表：待全文补页码
- 需要与哪些论文并列比较：AutoResearchClaw、AutoSci、GraphAgents、MatClaw

## 9. 总结

### 9.1 一句话概括

面向原子尺度研究的通用技能化 Agent 平台。

### 9.2 速记版 pipeline

1. 接收 atomistic research 目标
2. 选择并编排 skills
3. 调用计算与分析工具
4. 基于反馈迭代
5. 输出跨任务研究结果

### 9.3 标注字段汇总

```text
是否纳入：是
主类：01
二级类：01.04
三级类：
四级专题：Agentic atomistic-research harness systems
Agent 类型：LLM Agent; Tool-using Agent; Hybrid Agent
科研流程角色：workflow_orchestration; tool_use_and_code_execution; feedback_iteration; result_interpretation
自主能力：planning; tool_use; feedback_iteration; autonomous_decision_making; environment_interaction
验证方式：benchmark; simulation_validation; computational_validation
交叉属性：computation_driven; simulation_driven
科学贡献类型：system_platform; general_scientific_research
证据强度：medium_pending_full_text
归类置信度：中高
纳入置信度：高
推荐引用强度：core
```
