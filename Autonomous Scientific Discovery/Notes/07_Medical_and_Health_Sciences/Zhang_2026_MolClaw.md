# Zhang 2026 - MolClaw: An Autonomous Agent with Hierarchical Skills for Drug Molecule Evaluation, Screening, and Optimization

**论文信息**
- 标题：MolClaw: An Autonomous Agent with Hierarchical Skills for Drug Molecule Evaluation, Screening, and Optimization
- 作者：Lisheng Zhang; Lilong Wang; Xiangyu Sun; Wei Tang; Haoyang Su; Yuehui Qian; Qikui Yang; Qingsong Li; Zhenyu Tang; Haoran Sun; Yingnan Han; Yankai Jiang; Wenjie Lou; Bowen Zhou; Xiaosong Wang; Lei Bai; Zhengwei Xie
- 年份：2026
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2604.21937
- PDF / 本地文件路径：当前笔记基于 arXiv abstract 与 reviewer 一手 PDF 证据整理
- 论文类型：系统论文 / drug discovery agent
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

## 2026-06-24 confirmed-core full-reaudit writeback

This writeback aligns the note to the frozen adjudication for `ASD-0675`.

```text
final_agent_inclusion: yes
scientific_object_modules: 07
object_coverage_mode: single_module
has_concrete_object_experiments: yes
general_method_bucket: none
primary_module_for_filing: 07
confidence: high
source_limited: no
safety_access_status: accessed_no_safety_issue
first_hand_sources_checked: arXiv abstract + reviewer full-text evidence pack
classification_evidence_source_level: first_hand_full_text
module_assignment_evidence: drug-molecule evaluation, screening, optimization, and MolBench end-to-end drug-discovery tasks all stay anchored in therapeutic-molecule discovery.
multi_module_object_coverage_note: molecule language and chemistry-tool workflow do not expand this note into `03`; the stable object remains drug discovery under `07`.
final_reason: The scientific object is drug-discovery workflow over therapeutic molecules, so `07` is stable.
```

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | arXiv abstract L37-L39 | 论文明确是 autonomous agent，并以三层 skill architecture 组织长程工作流 | 高 |
| 科学对象归类 | `07` | arXiv abstract L37-L39；reviewer full-text evidence pack | 直接对象是 therapeutic molecules 上的 drug discovery workflow，而不是一般化学对象优化 | 高 |
| 方法流程 | 层级化 workflow 编排 | arXiv abstract L37-L39 | tool-level、workflow-level、discipline-level 三层技能显式支持 sequential tool calls | 高 |
| 验证方式 | MolBench + computational workflows | arXiv abstract L39-L39；reviewer PDF evidence | benchmark 覆盖 8 到 50+ sequential tool calls，主要是 computational drug discovery | 中高 |
| 边界判断 | 不转 `03` 或 `01.04` | arXiv abstract；reviewer PDF evidence | 虽有分子和工具平台外观，但任务与 benchmark 都稳定锚定在 drug discovery | 高 |

## 0. 摘要翻译

论文指出，计算药物发现中的分子筛选与优化需要编排大量专业工具和多步工作流，而现有 AI Agents 在这些高复杂度场景下表现不稳。作者提出 MolClaw，一个 autonomous agent，通过 70 个技能构成的三层层级架构统一 30 多个专业资源：tool-level skills 负责原子操作，workflow-level skills 将其组合成带质量检查和反思的 validated pipelines，discipline-level skill 提供药物发现规划与验证所需的科学原则。作者还提出 MolBench，覆盖分子筛选、优化和端到端 discovery 挑战，要求 8 到 50+ 次连续工具调用，并报告 MolClaw 在所有指标上达到 SOTA。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：面向药物发现；多步长程 workflow；具备工具调用、反思、层级技能编排
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：未明确
- 在科研流程中承担的明确角色：分子评估、候选筛选、分子优化、workflow 编排

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 科学对象模块：07
- 覆盖模式：single_module
- 是否具有具体科学对象实验、验证、benchmark task、case study 或结果报告：yes
- 独立 `01.04` 存放区：none
- Primary module for filing：07
- Filing 说明：note 位于 `07_Medical_and_Health_Sciences` 目录与本轮裁决一致，但权威事实是 supported module `07`，不是分子/工具外观。
- 当前二级类措辞：`07.04` 可作为 drug-discovery descriptive wording 保留，但不应再让 `03` 漂移成为并列分类事实。
- 归类理由：虽然论文直接处理分子与计算化学工具，但最终科学对象、benchmark 和 workflow 验证场景都稳定落在 therapeutic-molecule drug discovery。
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：drug molecule screening and optimization for drug discovery
- 最终科学问题：如何让 autonomous agent 在复杂药物发现 workflow 中稳定完成分子筛选、评估与优化
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：层级技能系统是方法；任务本体仍是药物发现

### 2.3 容易混淆的边界

- 可能误归类到：03；01.04
- 最终判定：支持模块为 `07`
- 判定理由：分子与计算化学只是药物发现 workflow 的技术层外观，不足以把论文转成 `03`；同时 MolBench 与长程技能编排都围绕 therapeutic-molecule discovery，不属于 `01.04` 通用科研系统。
- 是否需要二次复核：否，主类方向较稳

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：未明确
- Multi-Agent System：未明确
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：未明确
- Hybrid Agent：是
- 其他：hierarchical skills architecture

### 3.2 科研流程角色

- 文献检索与阅读：未明确
- 知识抽取与组织：部分是
- 科学问题提出：部分是
- 假设生成：部分是
- 实验设计：部分是
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
- 记忆与状态维护：未明确
- 反馈迭代：是
- 自主决策：是
- 多 Agent 协作：未明确
- 环境交互：是
- 闭环实验：否

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 实验驱动：否
- 仿真驱动：是
- 多模态：否
- 多尺度建模：否
- 高通量筛选：部分是
- 知识图谱：否
- 数字孪生：否
- 机器人平台：否
- 其他：long-horizon workflow orchestration

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：复杂 drug discovery workflows 需要组织数十个专业工具
- 现有科研流程或方法的痛点：现有 Agent 在高复杂度、多步工具场景下表现脆弱
- 核心假设或直觉：把药物发现知识分成分层技能，可以提升长程任务稳定性

### 4.2 系统流程

1. 输入：drug discovery task
2. 任务分解 / 规划：discipline-level skill 提供全局规划
3. 工具、数据库、模型或实验平台调用：tool-level / workflow-level skills 执行具体任务
4. 中间结果反馈：quality check 与 reflection
5. 决策或迭代：继续 screening、evaluation、optimization
6. 输出：更优候选分子与完整 workflow traces

### 4.3 系统组件

- Agent 核心：MolClaw autonomous agent
- 工具 / API / 数据库：30+ domain resources
- 记忆或状态模块：摘要未完全展开
- 规划器：discipline-level skill
- 评估器 / verifier：workflow-level quality check
- 人类反馈或专家介入：摘要未强调
- 实验平台或仿真环境：computational drug discovery tool stack

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：是
- 高通量计算：部分是
- 机器人实验：否
- 湿实验：否
- 临床数据：否
- 真实场景部署：否
- 专家评估：否

### 5.2 数据、任务与指标

- 数据集 / 实验对象：MolBench
- 任务设置：molecular screening、optimization、end-to-end discovery
- 对比基线：existing agents / baselines
- 评价指标：all metrics 上的 SOTA；workflow competence
- 关键结果：性能优势主要集中在需要结构化 workflow 的任务
- 是否有消融实验：有
- 是否有失败案例或负结果：摘要指出对于 ad hoc scripting 可解决的任务，优势会消失

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：更偏计算药物发现工作流与候选优化
- 科学贡献是否经过验证：是
- 贡献强度判断：中
- 科学贡献类型：system_platform; drug_discovery
- 证据强度：medium_high_primary_abstract

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单模型分子生成，而是分层 workflow agent
- 与已有 Agent / 科研智能系统的区别：突出 70-skill hierarchical orchestration 与 MolBench
- 与同一科学领域其他 Agent 文献的关系：可与 Mozi、Rhizome OS-1、Latent-Y 对照
- 主要创新点：把 drug discovery 工具生态抽象为长程 hierarchical skills

## 7. 局限性与风险

- Agent 自主性不足：虽然长程 workflow 强，但仍缺少湿实验闭环
- 科学验证不足：主要停留在 docking、ADMET、MD、benchmark comparison 等计算层
- 泛化性不足：需全文确认不同任务族的稳定性
- 工具链依赖：高
- 数据泄漏或 benchmark 偏差：需关注 benchmark 设计
- 成本、可复现性或安全风险：复杂技能图谱复现实装成本较高
- 是否仍需进一步全文复核：否；主类和纳入判断已较稳，主要剩余风险是 core-strength

## 8. 对综述写作的价值

- 可放入哪个章节：07.04 药物发现 Agent
- 可支撑哪个论点：药物发现 Agent 的主要瓶颈正从“模型能力”转向“workflow orchestration competence”
- 可用于哪个表格或图：drug discovery benchmark / orchestration comparison
- 适合作为代表性案例吗：适合做 benchmark-heavy workflow 样本
- 推荐引用强度：core
- 需要在正文中特别引用的页码 / 图 / 表：70 skills、MolBench、workflow competence bottleneck
- 需要与哪些论文并列比较：Mozi、Rhizome OS-1、Latent-Y

## 9. 总结

### 9.1 一句话概括

用层级技能系统驱动药物分子筛选和优化的 Agent。

### 9.2 速记版 pipeline

1. 接收药物发现任务
2. 分层技能拆解流程
3. 调用多种专业工具
4. 做质量检查与反思
5. 输出候选与优化结果

### 9.3 标注字段汇总

```text
是否纳入：是
科学对象模块：07
覆盖模式：single_module
是否具有具体科学对象实验：yes
general_method_bucket：none
Primary module for filing：07
是否进入 01.04 存放区：否
secondary_bucket_wording：`07.04` may remain as descriptive drug-discovery wording, but the authoritative module decision is top-level `07`
module_assignment_evidence：drug-molecule evaluation, screening, optimization, and MolBench workflows remain therapeutic-molecule discovery tasks
multi_module_object_coverage_note：no accepted `03` expansion; molecule/tool language does not override the medical drug-discovery object
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Hybrid Agent
科研流程角色：workflow_orchestration; tool_use_and_code_execution; evidence_assessment_and_validation; feedback_iteration
自主能力：task_decomposition; planning; tool_use; feedback_iteration; autonomous_decision_making
验证方式：benchmark; computational_validation
交叉属性：computation_driven; data_driven; simulation_driven
科学贡献类型：system_platform; drug_discovery
证据强度：medium_high_primary_abstract
first_hand_sources_checked：arXiv abstract; reviewer full-text evidence pack
source_limited：no
safety_access_status：accessed_no_safety_issue
归类置信度：高
纳入置信度：高
推荐引用强度：core
```
