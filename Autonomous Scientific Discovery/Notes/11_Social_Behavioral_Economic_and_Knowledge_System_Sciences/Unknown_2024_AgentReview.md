# Jin et al. 2024 - AgentReview: Exploring Peer Review Dynamics with LLM Agents

**论文信息**
- 标题：AgentReview: Exploring Peer Review Dynamics with LLM Agents
- 作者：Yiqiao Jin; Qinlin Zhao; Yiyang Wang; Hao Chen; Kaijie Zhu; Yijia Xiao; Jindong Wang
- 年份：2024
- 来源 / venue：EMNLP 2024 Main Track (Oral)
- DOI / arXiv / URL：https://arxiv.org/abs/2406.12708
- PDF / 本地文件路径：当前未在项目中记录本地归档 PDF；本笔记依据 arXiv 摘要页、arXiv PDF 与 arXiv HTML 全文的一手证据整理。
- 论文类型：研究论文 / peer-review simulation agent framework
- 当前状态：主表当前为 `to_read`；本 note 已完成一手来源写回
- 阅读日期：2026-06-24
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | arXiv abstract; Sec. 3 | 论文提出 LLM-based peer review simulation framework，而不是单次问答或静态分析脚本。 | 高 |
| 多步行动过程 | 是 | arXiv PDF method / workflow sections | 系统将 reviewer simulation、latent-factor control、decision analysis 串成可迭代流程。 | 高 |
| 科学对象归类 | `11` | arXiv abstract; introduction | 研究对象是 peer review dynamics、reviewer bias 与 scientific publication mechanism，本体是科学知识生产系统。 | 高 |
| 边界排除 | 不归 `01.04` | arXiv abstract; task framing | 虽然是通用 LLM/agent 框架外观，但验证对象不是“通用科研能力”，而是 scientific peer review itself。 | 高 |
| 实验与结果 | 有明确结果 | arXiv abstract; results | 文中报告 reviewer bias 可导致 37.1% decision variation，并用 sociological theories 解释。 | 高 |
| 价值判断 | 稳定归入 `11.07` | arXiv abstract; comments | 这是 science-of-science / peer-review mechanism 研究，而非普通 publishing assistant。 | 高 |

## 0. 摘要翻译

论文关注科学同行评审这一知识生产机制本身。作者指出，传统 peer review 研究往往依赖已有评审数据的统计分析，难以处理多变量、潜在变量和隐私约束。AgentReview 提出一个基于大语言模型的评审过程模拟框架，通过显式控制和拆解多种潜在因素来研究 peer-review dynamics。论文报告，评审者偏差可带来显著的决策波动，并用 social influence theory、altruism fatigue 和 authority bias 等社会学解释支撑结果。对本综述而言，这篇论文的关键不是“用了 LLM”，而是“把 scientific peer review 作为直接研究对象”。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：系统围绕明确科研目标构造多步模拟与分析流程，具备任务编排、角色分工、反馈分析和结果解释能力。
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：部分是
  - 反馈迭代：是
  - 自主决策：部分是
  - 多 Agent 协作：是
- 在科研流程中承担的明确角色：simulation modeling、evidence assessment、result interpretation、workflow orchestration

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：`11`
- 覆盖模式：单模块
- 是否具有具体科学对象实验、验证、benchmark task、case study 或结果报告：是
- 独立 `01.04` 存放区：none
- Primary module for filing：`11`
- Primary module for filing 说明：当前 note 位于 `11` 目录，仅作归档便利，不覆盖分类事实。
- 主展示模块一级类：`11` 社会、行为、经济与知识系统科学
- 主展示模块二级类：`11.07` 科学系统与知识生产研究
- 主展示模块三级类：scientific peer-review dynamics
- 主展示模块四级专题：peer-review simulation agents
- 其他覆盖模块及对应层级路径：无
- 是否进入独立 `01.04` 存放区：否
- 每个模块的对象实验证据：论文直接模拟和分析 scientific peer review、reviewer bias 与 paper decision variation。
- 归类理由：论文的直接研究对象是科学共同体中的评审机制和知识生产过程，而不是领域无关的科研工作流。
- 归类置信度：中高

### 2.2 对象优先判定

- 最终科学研究对象：scientific peer review、reviewer bias、publication decision dynamics
- 最终科学问题：如何用 agent-based simulation disentangle peer-review latent factors，并分析评审偏差如何影响科学知识生产
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：LLM 与 multi-agent 只是实现方式，决定主类的是被研究的“科学评审系统”本身

### 2.3 容易混淆的边界

- 可能误归类到：`01.04`
- 最终判定：保持 `11`
- 判定理由：这不是无具体对象的通用科研 agent，而是直接研究 scientific knowledge production itself
- 多模块覆盖说明：当前没有额外对象模块证据
- 01.04 判定说明：不进入 `01.04`，因为论文已经对科学系统对象给出明确模拟、分析和结果报告
- 是否需要二次复核：否；当前全文证据已足以支持模块判定

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：部分是
- Tool-using Agent：部分是
- Retrieval-augmented Agent：未强调
- Multi-Agent System：是
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：部分是
- Hybrid Agent：是
- 其他：peer-review simulation agents

### 3.2 科研流程角色

- 文献检索与阅读：否
- 知识抽取与组织：部分是
- 科学问题提出：否
- 假设生成：部分是
- 实验设计：部分是
- 仿真建模：是
- 工具调用与代码执行：部分是
- 实验执行：否
- 数据分析：是
- 结果解释：是
- 证据评估与验证：是
- 论文写作：否
- 端到端科研流程自动化：部分是

### 3.3 自主能力

- 任务分解：是
- 计划生成：是
- 工具调用：部分是
- 记忆与状态维护：部分是
- 反馈迭代：是
- 自主决策：部分是
- 多 Agent 协作：是
- 环境交互：中等
- 闭环实验：偏弱，主要是模拟闭环而非物理实验闭环

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
- 其他：science-of-science / peer-review process analysis

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：希望在隐私受限、变量复杂的前提下更系统地研究同行评审机制
- 现有科研流程或方法的痛点：传统统计分析难以显式分离多种潜在因素，也难以进行受控机制研究
- 核心假设或直觉：agent-based simulation 可以更可控地重建和分析 peer-review dynamics

### 4.2 系统流程

1. 输入：论文、评审场景和待分析的 peer-review factors
2. 任务分解 / 规划：把评审模拟、变量控制、偏差分析和结果解释拆成可执行步骤
3. 工具、数据库、模型或实验平台调用：依赖 LLM-based simulation framework 与分析组件
4. 中间结果反馈：根据模拟结果更新 latent-factor interpretation
5. 决策或迭代：继续比较 reviewer bias、decision variation 和社会学解释
6. 输出：对 peer-review mechanism 的可解释分析结论

### 4.3 系统组件

- Agent 核心：LLM-based review simulation agents
- 工具 / API / 数据库：论文未把外部科学工具链作为重点
- 记忆或状态模块：存在情景与变量状态维护
- 规划器：有
- 评估器 / verifier：有，用于 bias analysis 和 decision variation analysis
- 人类反馈或专家介入：弱到中等
- 实验平台或仿真环境：peer-review simulation environment

## 5. 实验与验证

### 5.1 验证方式

- benchmark：部分是
- 仿真验证：是
- 高通量计算：否
- 机器人实验：否
- 湿实验：否
- 临床数据：否
- 真实场景部署：否
- 专家评估：部分是

### 5.2 数据、任务与指标

- 数据集 / 实验对象：peer review 场景、review decisions、latent-factor simulations
- 任务设置：模拟评审过程并分析偏差与决策变化
- 对比基线：传统 peer-review analysis 视角和非 agent 化分析思路
- 评价指标：decision variation、bias-related effects、机制解释能力
- 关键结果：论文报告 reviewer bias 可带来约 37.1% 的 decision variation
- 是否有消融实验：正文可继续深读，但当前已有充分结果证据
- 是否有失败案例或负结果：未作为 note 主结论

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：是，主要是对 peer-review mechanism 的机制性洞察
- 科学贡献是否经过验证：是，以 simulation analysis 和理论解释支撑
- 贡献强度判断：中
- 科学贡献类型：system_platform / explanation / knowledge_production
- 证据强度：simulation_supported
- 是否仍需进一步全文复核：否；当前一手全文证据已足以支持纳入与分类

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：研究对象不是自然科学对象，而是 scientific peer review 本身
- 与已有 Agent / 科研智能系统的区别：它不是通用科研助理，而是面向 science-of-science 的模拟分析框架
- 与同一科学领域其他 Agent 文献的关系：可与 ReviewGrounder、When Reviews Disagree 等 `11` 类知识生产研究记录并列比较
- 主要创新点：把 peer-review dynamics 作为可控 agent-based simulation 对象进行机制拆解

## 7. 局限性与风险

- Agent 自主性不足：更偏分析框架，非真实评审流程中的自主执行系统
- 科学验证不足：主要是 simulation 和理论解释，非真实制度干预实验
- 泛化性不足：结论受模拟设定和 latent-factor 建模方式影响
- 工具链依赖：依赖 LLM behavior 和设计好的模拟流程
- 数据泄漏或 benchmark 偏差：peer-review setting 的 external validity 仍需谨慎解读
- 成本、可复现性或安全风险：主要风险是 core-strength，而不是分类边界

## 8. 对综述写作的价值

- 可放入哪个章节：`11.07` 科学系统与知识生产研究
- 可支撑哪个论点：Agent 已开始直接研究 scientific knowledge production itself，而非只辅助自然科学实验
- 可用于哪个表格或图：`11` 类论文代表案例表；`11` 与 `01.04` 边界对照表
- 适合作为代表性案例吗：适合
- 推荐引用强度：standard
- 需要在正文中特别引用的页码 / 图 / 表：摘要、方法总览、结果部分关于 decision variation 的证据
- 需要与哪些论文并列比较：Unknown_2026_ReviewGrounder；Unknown_2026_When_Reviews_Disagree

## 9. 总结

### 9.1 一句话概括

用 LLM agents 模拟并分析 scientific peer review 机制。

### 9.2 速记版 pipeline

1. 定义同行评审场景  
2. 用 agents 模拟评审与潜在因素  
3. 分析 bias 与 decision variation  
4. 输出对 peer-review mechanism 的解释

### 9.3 标注字段汇总

```text
是否纳入：是
科学对象模块：11
覆盖模式：single_module
是否具有具体科学对象实验：yes
general_method_bucket：none
Primary module for filing：11
是否进入 01.04 存放区：否
主展示模块一级类：11
主展示模块二级类：11.07
主展示模块三级类：scientific peer-review dynamics
主展示模块四级专题：peer-review simulation agents
其他覆盖模块及对应层级路径：无
module_assignment_evidence：peer review dynamics、reviewer bias、decision variation 是直接研究对象
multi_module_object_coverage_note：无
Agent 类型：LLM Agent; Multi-Agent System; Hybrid Agent
科研流程角色：simulation_modeling; data_analysis; result_interpretation; evidence_assessment_and_validation
自主能力：task_decomposition; planning; feedback_iteration; multi_agent_collaboration
验证方式：simulation_validation; expert_evaluation
交叉属性：computation_driven; data_driven; simulation_driven
科学贡献类型：system_platform; explanation; knowledge_production
证据强度：simulation_supported
归类置信度：中高
纳入置信度：高
推荐引用强度：standard
```
