# Cao 2026 - Mozi: Governed Autonomy for Drug Discovery LLM Agents

**论文信息**
- 标题：Mozi: Governed Autonomy for Drug Discovery LLM Agents
- 作者：He Cao; Siyu Liu; Fan Zhang; Zijing Liu; Hao Li; Bin Feng; Shengyuan Bai; Leqing Chen; Kai Xie; Yu Li
- 年份：2026
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2603.03655
- PDF / 本地文件路径：当前笔记基于 arXiv abstract 与 reviewer 一手 PDF 证据整理
- 论文类型：系统论文 / drug discovery agent
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | arXiv abstract L38-L42 | governed supervisor-worker hierarchy + stateful skill graphs，明确是多步 Agent 工作流 | 高 |
| 科学对象归类 | `07.04` | arXiv abstract L38-L42 | Workflow Plane 直接覆盖 canonical drug discovery stages，从 target identification 到 lead optimization | 高 |
| 方法流程 | 治理型长程 workflow | arXiv abstract L39-L42 | role-based tool isolation、reflection-based replanning、HITL checkpoints | 高 |
| 验证方式 | benchmark + in silico case study | arXiv abstract L41-L42；reviewer PDF evidence | PharmaBench 与 therapeutic case studies 支撑其主张 | 中高 |
| 边界判断 | 不回 `01.04` | arXiv abstract L39-L42 | governance 是方法设计，最终对象仍是药物发现长流程 | 高 |

## 0. 摘要翻译

论文指出，带工具的大语言模型 Agent 在药物发现这类高风险领域面临两个关键障碍：工具使用缺乏治理，以及长程流程可靠性不足。作者提出 Mozi，一个双层架构：Layer A 负责监督-执行层级治理，限制工具空间并支持反思式重规划；Layer B 将从 Target Identification 到 Lead Optimization 的药物发现阶段组织为有状态的 skill graphs，并在高不确定性决策点引入 HITL 检查。系统在 PharmaBench 上展示出更强的 orchestration accuracy，并在端到端治疗案例中展示了大化学空间导航、毒性约束与 in silico candidate 生成能力。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：面向 drug discovery；有多步行动流程；具备治理、工具调用、反思式重规划和长程 workflow 编排
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：是
- 在科研流程中承担的明确角色：workflow orchestration、target identification、candidate filtering、lead optimization

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
- 四级专题：Governed drug-discovery LLM agents
- 四级专题是否为新增：否
- 归类理由：论文从任务定义到验证都围绕 canonical drug discovery stages，不是通用科学 workflow 平台
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：drug discovery pipeline and therapeutic candidate generation
- 最终科学问题：如何在受治理约束下可靠执行长程药物发现 Agent 流程
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：governance plane 是方法机制；稳定科学对象仍是药物发现流程

### 2.3 容易混淆的边界

- 可能误归类到：01.04
- 最终判定：保留 07.04
- 判定理由：即便 workflow 外观很强，其 stateful skill graphs 仍锚定在药物发现阶段本身
- 是否需要二次复核：否，主类方向已较稳

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：部分是
- Multi-Agent System：是
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：是
- Hybrid Agent：是
- 其他：governed supervisor-worker hierarchy

### 3.2 科研流程角色

- 文献检索与阅读：部分是
- 知识抽取与组织：部分是
- 科学问题提出：部分是
- 假设生成：是
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
- 记忆与状态维护：是
- 反馈迭代：是
- 自主决策：是
- 多 Agent 协作：是
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
- 知识图谱：未明确
- 数字孪生：否
- 机器人平台：否
- 其他：governed autonomy

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：高风险药物发现流程中，普通 Agent 易因 hallucination 和长程 drift 导致不可复现
- 现有科研流程或方法的痛点：dependency-heavy pipeline 中早期错误会累积放大
- 核心假设或直觉：通过治理层与 workflow 层分离，可以把自由推理和结构化执行结合起来

### 4.2 系统流程

1. 输入：drug discovery objective
2. 任务分解 / 规划：Control Plane 分派 supervisor-worker tasks
3. 工具、数据库、模型或实验平台调用：Workflow Plane 调用 stateful skill graphs 覆盖 TI 到 LO
4. 中间结果反馈：reflection-based replanning 与 HITL checkpoints
5. 决策或迭代：继续候选筛选与优化
6. 输出：competitive in silico candidates 与完整推理轨迹

### 4.3 系统组件

- Agent 核心：dual-layer governed autonomy architecture
- 工具 / API / 数据库：drug discovery stage-specific tools
- 记忆或状态模块：stateful skill graphs
- 规划器：Control Plane
- 评估器 / verifier：governed data contracts 与 benchmark evaluation
- 人类反馈或专家介入：关键节点 HITL
- 实验平台或仿真环境：in silico pharmaceutical workflows

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：是
- 高通量计算：部分是
- 机器人实验：否
- 湿实验：否
- 临床数据：否
- 真实场景部署：否
- 专家评估：是

### 5.2 数据、任务与指标

- 数据集 / 实验对象：PharmaBench + therapeutic case studies
- 任务设置：从 target identification 到 lead optimization 的药物发现 workflow
- 对比基线：existing baselines
- 评价指标：orchestration accuracy、candidate quality、toxicity filtering performance
- 关键结果：PharmaBench 表现更优，并能在案例中导航巨大化学空间
- 是否有消融实验：摘要未完全展开
- 是否有失败案例或负结果：reviewer PDF evidence 显示主要局限是 reliance on in silico surrogates

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：更偏药物发现工作流与候选生成
- 科学贡献是否经过验证：部分是
- 贡献强度判断：中
- 科学贡献类型：system_platform; drug_discovery
- 证据强度：medium_high_primary_abstract

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是静态分子模型，而是治理型长程药物发现 Agent
- 与已有 Agent / 科研智能系统的区别：突出 governed autonomy 与 auditability
- 与同一科学领域其他 Agent 文献的关系：可与 MolClaw、Rhizome OS-1、Latent-Y、DrugAgent 对照
- 主要创新点：将治理约束内建到 drug discovery Agent long-horizon workflow

## 7. 局限性与风险

- Agent 自主性不足：保留 HITL 检查点
- 科学验证不足：主要验证仍为 benchmark 与 in silico case studies
- 泛化性不足：需全文确认不同 discovery stages 的泛化表现
- 工具链依赖：高
- 数据泄漏或 benchmark 偏差：待全文核查
- 成本、可复现性或安全风险：药物发现长流程成本高
- 是否仍需进一步全文复核：否；当前主类与纳入判断已足够稳，主要剩余风险是 core-strength

## 8. 对综述写作的价值

- 可放入哪个章节：07.04 药物发现 Agent
- 可支撑哪个论点：高风险药物发现流程正在从“能跑”转向“受治理且可审计地跑”
- 可用于哪个表格或图：drug discovery governance / reliability comparison
- 适合作为代表性案例吗：适合作为治理型 workflow 案例
- 推荐引用强度：core
- 需要在正文中特别引用的页码 / 图 / 表：TI-to-LO skill graphs、PharmaBench、therapeutic case studies
- 需要与哪些论文并列比较：MolClaw、Rhizome OS-1、Latent-Y

## 9. 总结

### 9.1 一句话概括

把药物发现长流程做成受治理的 LLM Agent 系统。

### 9.2 速记版 pipeline

1. 设定药物发现目标
2. 治理层分派任务
3. workflow 层调用药物发现技能
4. 反思与 HITL 检查
5. 输出候选与审计轨迹

### 9.3 标注字段汇总

```text
是否纳入：是
主类：07
二级类：07.04
三级类：
四级专题：Governed drug-discovery LLM agents
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Human-in-the-loop Agent; Hybrid Agent
科研流程角色：workflow_orchestration; tool_use_and_code_execution; feedback_iteration; hypothesis_generation
自主能力：task_decomposition; planning; tool_use; memory_or_state_tracking; feedback_iteration; autonomous_decision_making; multi_agent_collaboration
验证方式：benchmark; expert_evaluation; computational_validation
交叉属性：computation_driven; data_driven; simulation_driven
科学贡献类型：system_platform; drug_discovery
证据强度：medium_high_primary_abstract
归类置信度：高
纳入置信度：高
推荐引用强度：core
```
