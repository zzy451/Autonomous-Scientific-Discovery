# Ojeda et al. 2026 - My Chemical Harness: Evolutionary Molecular Design over Synthetic Pathways with Large Language Model Agents

**论文信息**
- 标题：My Chemical Harness: Evolutionary Molecular Design over Synthetic Pathways with Large Language Model Agents
- 作者：César Ojeda; Darius A. Faroughy; Maryam Karimi; Payam Zarrintaj; Mir Mehdi Seyedebrahimi; Martín Carballo-Pacheco
- 年份：2026
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2606.11256
- PDF / 本地文件路径：当前笔记基于 arXiv HTML / PDF 与 batch9 reviewer evidence packs
- 论文类型：研究论文 / chemistry molecular-design agent
- 当前状态：to_read
- 阅读日期：2026-06-20
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | abstract; method | LLM 充当搜索策略控制器，配合本地化学代码执行、验证、打分与反思更新 | 高 |
| 科学对象归类 | `03 / 03.04` | abstract; intro | 搜索对象是可执行 synthetic pathways、molecules、reaction templates 与 building blocks | 高 |
| 方法流程 | route-native evolutionary design loop | method section | individual 是 synthetic pathway，LLM 做 query planning、policy setting 和反思修订 | 高 |
| 实验验证 | sEH proxy + TDC 13 oracle tasks | experiments | 比较 reflective LLM、single-pass LLM 和 deterministic controllers | 高 |
| 边界判定 | 不应移入 `07` 或 `01.04` | intro; discussion | 虽提到 drug discovery，但直接优化对象仍是分子与合成路径，而非临床/患者或通用平台 | 高 |
| 风险判定 | 主风险是 core-strength，不是 class risk | discussion | 下一步仍需接入真实 medicinal chemistry、合成与实验反馈 | 中高 |

## 0. 摘要翻译

论文提出 My Chemical Harness，把分子设计问题重新表述为对“可执行合成路径”的 evolutionary search，而不再只是对孤立分子结构的搜索。每个候选 individual 都是由可购买 building blocks 和 reaction templates 构成的可执行 synthetic pathway，本地确定性化学工具负责路径构造、验证、去重和打分，而 LLM 负责高层搜索策略、查询规划、反思修订与学习报告。作者在 sEH proxy 任务和 TDC 13 个 molecular design oracles 上进行验证，强调系统的强项是 synthesis-aware molecular design。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：具有明确科研目标、LLM 策略控制、多步工具执行、反馈修正和状态更新
- 判定置信度：高
- 是否面向明确科研目标：是，面向分子设计与 chemical space exploration
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：否
- 在科研流程中承担的明确角色：假设生成、工具调用、工作流编排、结果评估、反馈迭代

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：03
- 二级类：03.04
- 三级类：
- 四级专题：Synthetic-pathway-native molecular-design agents
- 四级专题是否为新增：否
- 归类理由：最终搜索与评估对象是分子、反应模板、building blocks 与合成路径，属于化学与分子设计对象
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：molecules and executable synthetic pathways
- 最终科学问题：如何在可执行合成约束下进行更有效的分子设计搜索
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：LLM agent 只是搜索策略层，真正被优化的是 chemistry-native object

### 2.3 容易混淆的边界

- 可能误归类到：07；01.04
- 最终判定：保持 `03 / 03.04`
- 判定理由：即使引言提到 drug discovery，直接优化对象仍是分子和反应路线，而不是临床或治疗对象
- 是否需要二次复核：否

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
- 其他：Synthesis-aware molecular-design agent

### 3.2 科研流程角色

- 文献检索与阅读：否
- 知识抽取与组织：部分是
- 科学问题提出：否
- 假设生成：是
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
- 记忆与状态维护：是
- 反馈迭代：是
- 自主决策：是
- 多 Agent 协作：否
- 环境交互：是
- 闭环实验：否

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：部分是
- 实验驱动：否
- 仿真驱动：否
- 多模态：否
- 多尺度建模：否
- 高通量筛选：是
- 知识图谱：否
- 数字孪生：否
- 机器人平台：否
- 其他：Synthetic-route-native search

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：避免传统分子设计先生成分子、再后验检查可合成性的断裂流程
- 现有科研流程或方法的痛点：很多生成模型会提出难以执行的分子候选或虚假的化学路径
- 核心假设或直觉：把 synthetic pathway 直接作为搜索个体，可让 LLM 以更真实的化学约束引导探索

### 4.2 系统流程

1. 输入：目标性质与 chemistry task
2. 任务分解 / 规划：LLM 设定查询与搜索策略
3. 工具、数据库、模型或实验平台调用：本地化学代码执行路径构造、验证、打分与筛选
4. 中间结果反馈：搜索结果与得分回传给 LLM
5. 决策或迭代：LLM 反思并调整反应家族、编辑类型和探索强度
6. 输出：更优的分子候选与可执行合成路径

### 4.3 系统组件

- Agent 核心：LLM policy controller
- 工具 / API / 数据库：local chemistry execution engine, route constructor, scoring tools
- 记忆或状态模块：search memory / reports
- 规划器：LLM controller
- 评估器 / verifier：pathway validation, deduplication, scoring modules
- 人类反馈或专家介入：未强调
- 实验平台或仿真环境：computational molecular-design environment

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：否
- 高通量计算：否
- 机器人实验：否
- 湿实验：否
- 临床数据：否
- 真实场景部署：否
- 专家评估：否

### 5.2 数据、任务与指标

- 数据集 / 实验对象：sEH proxy task；TDC 13 oracle tasks
- 任务设置：route-native molecular design
- 对比基线：reflective LLM vs single-pass LLM vs deterministic controllers
- 评价指标：oracle scores、synthesizability、AiZynthFinder success 等
- 关键结果：在多个任务上显示 reflective LLM controller 具有更强搜索能力
- 是否有消融实验：比较不同 controller 形态可视作部分消融
- 是否有失败案例或负结果：作者承认距离真实 medicinal chemistry 闭环仍有距离

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：提出 synthesis-aware molecular design workflow，并给出候选
- 科学贡献是否经过验证：是
- 贡献强度判断：中
- 科学贡献类型：系统平台 / 设计 / 预测
- 证据强度：仅 benchmark

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是直接对分子图做后验可合成性过滤，而是把路径本身作为搜索对象
- 与已有 Agent / 科研智能系统的区别：对象是 chemistry-native route search，不是通用 scientific workflow
- 与同一科学领域其他 Agent 文献的关系：是 `03 / 07 / 01.04` 边界上的稳定 `03` 样本
- 主要创新点：让 LLM 作为可执行合成路径搜索的高层控制器

## 7. 局限性与风险

- Agent 自主性不足：仍局限于计算搜索与路径评估
- 科学验证不足：没有湿实验或真实 medicinal chemistry 闭环验证
- 泛化性不足：是否能在更复杂化学空间中稳定工作仍待观察
- 工具链依赖：依赖本地化学执行引擎与评分器
- 数据泄漏或 benchmark 偏差：oracle benchmark 风险需关注
- 成本、可复现性或安全风险：合成可行性与安全性仍需实验确认

## 8. 对综述写作的价值

- 可放入哪个章节：03 化学科学 / 分子设计 Agent
- 可支撑哪个论点：药物语境不应自动把化学对象 paper 推到 `07`
- 可用于哪个表格或图：`03 / 07 / 01.04` 边界表； synthesis-aware design agents 表
- 适合作为代表性案例吗：适合
- 推荐引用强度：普通引用
- 需要在正文中特别引用的页码 / 图 / 表：method overview；benchmark results；discussion
- 需要与哪些论文并列比较：其他 molecular-design / drug-like chemistry agents

## 9. 总结

### 9.1 一句话概括

让 LLM 在可执行合成路径上做分子设计搜索。

### 9.2 速记版 pipeline

1. 把路径当作搜索个体
2. LLM 设搜索策略
3. 化学工具执行并打分
4. 根据结果反思修正
5. 输出更优分子与路线

### 9.3 标注字段汇总

```text
是否纳入：是
主类：03
二级类：03.04
三级类：
四级专题：Synthetic-pathway-native molecular-design agents
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Hybrid Agent
科研流程角色：hypothesis_generation; tool_use_and_code_execution; data_analysis; result_interpretation; evidence_assessment_and_validation; workflow_orchestration
自主能力：task_decomposition; planning; tool_use; memory; feedback_iteration; autonomous_decision_making; environment_interaction
验证方式：benchmark
交叉属性：computation_driven; data_driven; high_throughput_screening
科学贡献类型：system_platform; design; prediction
证据强度：benchmark_only
归类置信度：高
纳入置信度：高
推荐引用强度：普通引用
```
