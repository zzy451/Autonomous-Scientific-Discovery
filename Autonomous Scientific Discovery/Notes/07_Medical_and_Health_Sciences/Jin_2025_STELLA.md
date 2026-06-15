# Jin 2025 - STELLA

**论文信息**
- 标题：STELLA: Self-Evolving LLM Agent for Biomedical Research
- 作者：Ruofan Jin, Zaixi Zhang, Mengdi Wang, Le Cong
- 年份：2025
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2507.02004
- PDF / 本地文件路径：arXiv PDF；本次笔记读取全文
- 论文类型：系统论文 / benchmark
- 当前状态：已读 / 已纳入
- 阅读日期：2026-06-15
- 笔记作者：Codex

## Evidence Log

**证据级别：full-text**（已读取 arXiv PDF 全文抽取文本；Evidence Log 位置来自论文摘要、正文、图 1-2、Methods。）

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 纳入，self-evolving biomedical LLM agent | Abstract；Introduction；Fig. 1 | STELLA 由 Manager、Dev、Critic、Tool Creation Agent 组成，可自动发现、测试、集成新生物信息学工具 | 高 |
| 科学对象归类 | 医学与健康科学 / 生物医学研究 Agent | Title；Abstract；Methods | 面向 biomedical research benchmark 与肿瘤耐药机制示例，强调 biomedical discovery | 高 |
| 方法流程 | Manager 规划，Dev 写代码/建环境，Critic 反馈，Tool Creation Agent 扩展 Tool Ocean，Template Library 自演化 | Introduction；Fig. 1；Results | 通过 Template Library 和 Tool Ocean 从经验中学习，形成多步推理与工具扩展闭环 | 高 |
| 实验验证 | HLE Biomedicine、LAB-Bench DBQA/LitQA 等 benchmark | Abstract；Results；Methods | 报告 HLE Biomedicine 约 26%、DBQA 54%、LitQA 63%，并随 trials 增加提升 | 高 |
| 科学贡献 | 提出可自我扩展工具和推理模板的 biomedical agent | Conclusion | 系统贡献强；真实实验室部署和湿实验验证仍是未来工作 | 中 |

## 0. 摘要翻译

STELLA 是一个用于生物医学研究的自演化 AI Agent。它通过多 Agent 架构协调任务，并用两个机制持续提升能力：一是记录成功推理策略的 Template Library，二是可动态扩展的 Tool Ocean，其中 Tool Creation Agent 会搜索、创建、测试并接入新的生物信息学工具。论文在 Humanity's Last Exam: Biomedicine、LAB-Bench DBQA 和 LitQA 上验证，显示性能优于若干强基线，并且随经验积累而提升。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是。
- 判断依据：多 Agent 协作、工具创建/调用、代码执行、Critic 反馈、经验库更新。
- 判定置信度：高。
- 是否面向明确科研目标：是，解决 biomedical research questions。
- 是否具有多步行动过程：是，规划、执行、评估、工具创建、总结。
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是，Manager Agent 生成多步计划。
  - 工具调用：是，Dev Agent 和 Tool Ocean 调用数据库、模型、API、代码工具。
  - 反馈迭代：是，Critic Agent 评估中间结果并反馈。
  - 自主决策：是，Tool Creation Agent 根据能力缺口创建工具。
  - 多 Agent 协作：是。
- 在科研流程中承担的明确角色：生物医学问题求解、工具发现与整合、代码分析、结果审查。

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否，明确是 Agent 系统。
- 是否只是单次问答、摘要或分类：否，有多步执行与自演化。
- 是否缺少行动闭环：否。
- 若排除，排除理由：不排除。

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：`07` 医学与健康科学
- 二级类：`07.04` 药学与生物医药
- 三级类：`07.04.01` 药物发现
- 四级专题：Biomedical research agents
- 四级专题是否为新增：否。
- 归类理由：虽然包含计算生物学和生物信息学工具，但论文定位为 biomedical research，并以医学/生物医学 benchmark 和肿瘤耐药示例验证。
- 归类置信度：中-高。

### 2.2 对象优先判定

- 最终科学研究对象：生物医学知识、疾病机制、数据库和工具生态。
- 最终科学问题：AI Agent 能否在生物医学研究中自动扩展工具与推理能力。
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：技术是 LLM multi-agent，自演化是方法；主对象是 biomedical research workflow。

### 2.3 容易混淆的边界

- 可能误归类到：`06` 生命科学，或 `01.04` 通用科研 Agent。
- 最终判定：`07` 医学与健康科学。
- 判定理由：论文强调 biomedical benchmarks、肿瘤耐药、治疗再敏化策略等健康/医学问题；不是领域无关系统。
- 是否需要二次复核：是，若后续按“biomedical generalist agent”分拆，可能部分任务更偏 `06.03`。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是。
- Planning Agent：是。
- Tool-using Agent：是。
- Retrieval-augmented Agent：是，使用数据库/文献工具。
- Multi-Agent System：是。
- Robot / Embodied Agent：否。
- Human-in-the-loop Agent：弱，论文图示提到 human expert / wet experiment 可提供反馈。
- Hybrid Agent：是。
- 其他：self-evolving agent、tool-creation agent。

### 3.2 科研流程角色

- 文献检索与阅读：是。
- 知识抽取与组织：是。
- 科学问题提出：用户给定。
- 假设生成：是，例子中生成机制和治疗策略。
- 实验设计：计算/分析设计。
- 仿真建模：部分，foundation model / bioinformatics model 调用。
- 工具调用与代码执行：是。
- 实验执行：计算分析；湿实验为未来/外部反馈。
- 数据分析：是。
- 结果解释：是。
- 证据评估与验证：是，Critic Agent。
- 论文写作：Dev Agent 可 report writing。
- 端到端科研流程自动化：在 biomedical QA/analysis 范围内较强。

### 3.3 自主能力

- 任务分解：是。
- 计划生成：是。
- 工具调用：是。
- 记忆与状态维护：是，Template Library 与 Tool Ocean。
- 反馈迭代：是。
- 自主决策：是。
- 多 Agent 协作：是。
- 环境交互：代码环境、数据库、工具库。
- 闭环实验：计算闭环；真实 wet-lab 闭环待部署。

### 3.4 交叉属性标签

- 计算驱动：是。
- 数据驱动：是。
- 实验驱动：弱，未来可接 wet experiment。
- 仿真驱动：部分。
- 多模态：未作为核心。
- 多尺度建模：未强调。
- 高通量筛选：否。
- 知识图谱：可能使用网络整合，但非核心标签。
- 数字孪生：否。
- 机器人平台：否。
- 其他：self-evolution、tool discovery。

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：生物医学工具、数据和文献碎片化且快速变化，静态工具集的 Agent 难以跟上。
- 现有科研流程或方法的痛点：工具发现、学习和整合需要大量人工劳动；固定工具链扩展性差。
- 核心假设或直觉：Agent 应该能通过经验更新 reasoning templates，并根据任务自动发现/创建/测试新工具。

### 4.2 系统流程

1. 输入：高层 biomedical research prompt。
2. 任务分解 / 规划：Manager Agent 选择推理模板并制定多步计划。
3. 工具、数据库、模型或实验平台调用：Dev Agent 创建环境、写 Python、训练/调用模型；Tool Creation Agent 搜索 PubMed/GitHub 并创建工具。
4. 中间结果反馈：Critic Agent 检查分析是否可行、是否 actionable。
5. 决策或迭代：Manager 调整计划，更新 Template Library 和 Tool Ocean。
6. 输出：答案、分析报告、候选机制/策略，及新增工具/模板。

### 4.3 系统组件

- Agent 核心：Manager、Developer、Critic、Tool Creation Agent。
- 工具 / API / 数据库：Tool Ocean，包括数据库查询、foundation model、customized analysis、GitHub/PubMed 搜索等。
- 记忆或状态模块：Template Library、Tool Ocean。
- 规划器：Manager Agent。
- 评估器 / verifier：Critic Agent。
- 人类反馈或专家介入：图示中可接 human expert / wet experiment。
- 实验平台或仿真环境：benchmark QA 环境和生物信息学代码环境。

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是。
- 仿真验证：否。
- 高通量计算：否。
- 机器人实验：否。
- 湿实验：否，图示为可接入反馈。
- 临床数据：未作为主要验证。
- 真实场景部署：否。
- 专家评估：未见系统性专家评估。

### 5.2 数据、任务与指标

- 数据集 / 实验对象：Humanity's Last Exam: Biomedicine；LAB-Bench DBQA 和 LitQA；50 个 HLE representative questions；DBQA/LitQA 12.5% subset。
- 任务设置：与 Gemini 2.5 Pro、Claude 4 Opus、DeepSeek-R1、OpenAI o3、Biomni 等比较。
- 对比基线：state-of-the-art LLMs 和 Biomni biomedical agent。
- 评价指标：multiple-choice accuracy / benchmark score。
- 关键结果：HLE Biomedicine 约 26%，DBQA 约 54%，LitQA 约 63%；随 computation budget/trials 增加，HLE 表现几乎翻倍。
- 是否有消融实验：主要展示自演化随 trials 的增益；完整消融需复核。
- 是否有失败案例或负结果：结论中承认 benchmark 到真实实验室应用仍有 gap。

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：示例展示机制/策略生成，但主要贡献是系统和 benchmark 性能。
- 科学贡献是否经过验证：benchmark 验证；真实生物医学发现未独立湿实验验证。
- 贡献强度判断：中。
- 科学贡献类型：系统平台 / benchmark / 解释。
- 证据强度：benchmark only。

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：强调自我扩展工具与推理模板，而非固定模型预测。
- 与已有 Agent / 科研智能系统的区别：相比静态 biomedical agents，STELLA 的 Tool Ocean 和 Template Library 可随经验演化。
- 与同一科学领域其他 Agent 文献的关系：可与 Biomni、TxAgent、OmniCellAgent、TAIS、GeneAgent 并列。
- 主要创新点：Tool Creation Agent；Template Library；Tool Ocean 的动态扩展。

## 7. 局限性与风险

- Agent 自主性不足：benchmark 问答不等于完整实验发现；真实实验闭环未实现。
- 科学验证不足：缺少湿实验或临床验证。
- 泛化性不足：benchmark 子集和工具可用性可能影响结果。
- 工具链依赖：依赖搜索、GitHub 工具、conda/Python 环境和模型 API。
- 数据泄漏或 benchmark 偏差：大型模型可能见过 benchmark 或相关资料。
- 成本、可复现性或安全风险：自动创建和运行工具有安全风险；医学结论不可直接临床使用。

## 8. 对综述写作的价值

- 可放入哪个章节：医学与健康科学 Agent；自演化工具 Agent；biomedical research automation。
- 可支撑哪个论点：医学/生物医学 Agent 的瓶颈从“会不会答题”转向“能否动态扩展工具和经验”。
- 可用于哪个表格或图：自主演化能力表；Tool creation vs static toolset 对比表。
- 适合作为代表性案例吗：适合，但需标注 benchmark-only 证据。
- 推荐引用强度：核心引用。
- 需要在正文中特别引用的页码 / 图 / 表：Fig. 1-2；Methods benchmark 设置；Conclusion 的真实应用 gap。
- 需要与哪些论文并列比较：Biomni、TAIS、GeneAgent、DrugAgent、TxAgent。

## 9. 总结

### 9.1 一句话概括

可自建工具的生物医学 Agent。

### 9.2 速记版 pipeline

1. Manager 制定生物医学推理计划。
2. Dev 写代码并调用分析工具。
3. Critic 检查中间结果。
4. Tool Creation Agent 搜索并创建新工具。
5. 成功经验进入 Template Library 和 Tool Ocean。

### 9.3 标注字段汇总

```text
是否纳入：是
主类：07 医学与健康科学
二级类：07.04 药学与生物医药
三级类：07.04.01 药物发现
四级专题：Biomedical research agents
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Retrieval-augmented Agent; Multi-Agent System; Human-in-the-loop Agent; Hybrid Agent
科研流程角色：literature_search_and_reading; knowledge_extraction_and_organization; hypothesis_generation; experimental_design; tool_use_and_code_execution; data_analysis; result_interpretation; evidence_assessment_and_validation; paper_writing; end_to_end_research_automation
自主能力：task_decomposition; planning; tool_use; memory_or_state_tracking; feedback_iteration; autonomous_decision_making; multi_agent_collaboration; environment_interaction
验证方式：benchmark
交叉属性：computation_driven; data_driven
科学贡献类型：system_platform; benchmark; explanation
证据强度：benchmark_only
归类置信度：中-高
纳入置信度：高
推荐引用强度：核心引用
```
