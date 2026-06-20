# Sui et al. 2026 - Medea: An omics AI agent for therapeutic discovery

**论文信息**
- 标题：Medea: An omics AI agent for therapeutic discovery
- 作者：Sui et al.
- 年份：2026
- 来源 / venue：bioRxiv / PMC mirror
- DOI / arXiv / URL：https://doi.org/10.64898/2026.01.16.696667
- PDF / 本地文件路径：当前未保存本地 PDF；本笔记基于 PMC 可访问全文摘要与 GitHub 项目页
- 论文类型：研究论文 / omics therapeutic-discovery agent
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | PMC abstract | 系统对 omics objective 执行透明多步分析并调用工具 | 高 |
| 科学对象归类 | `07.04` | PMC abstract | 任务落点是 therapeutic discovery、target identification、synthetic lethality、immunotherapy response prediction | 高 |
| 方法流程 | 四模块工作流 | PMC abstract + GitHub | planning、code execution、literature reasoning、consensus 四模块 | 高 |
| 工具调用 | 明确 | PMC abstract | 调用 20 种工具，跨 transcriptomics、vulnerability maps、pathway knowledge、ML models | 高 |
| 边界判断 | 不转 `06` | PMC abstract | 终点是治疗靶点与疗效响应，而非一般 omics 机制研究 | 高 |

## 0. 摘要翻译

Medea 是一个面向治疗发现的 omics AI agent。PMC 摘要显示，它围绕多组学目标执行透明的多步分析流程，并整合规划、代码分析、文献推理与共识四个模块。系统调用 20 种工具，在靶点识别、合成致死推理和膀胱癌免疫治疗响应预测等任务上共完成 5679 次分析。现有证据足以支持它稳定留在 `07.04`，因为其最终对象不是一般生命科学机制，而是治疗发现与疗效预测。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：有明确科研目标、多步规划、工具调用、验证意识与模块协作
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：是
- 在科研流程中承担的明确角色：靶点识别、代码分析、文献推理、共识整合、治疗发现

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：07
- 二级类：07.04
- 三级类：omics therapeutic discovery
- 四级专题：multi-tool therapeutic discovery agents
- 四级专题是否为新增：否
- 归类理由：直接目标是治疗靶点、合成致死与免疫治疗响应预测
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：disease- and therapy-oriented multi-omics discovery tasks
- 最终科学问题：如何用多组学 Agent 自动完成治疗相关分析与发现
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：omics 只是数据层，真正的终点是 therapeutic discovery

### 2.3 容易混淆的边界

- 可能误归类到：06.03
- 最终判定：保留 07.04
- 判定理由：摘要持续强调 target nomination、synthetic lethality、immunotherapy response，而非一般生命机制
- 是否需要二次复核：否，主类足够稳定

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：是
- Multi-Agent System：是
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：未见明确证据
- Hybrid Agent：是
- 其他：verification-aware omics agent

### 3.2 科研流程角色

- 文献检索与阅读：是
- 知识抽取与组织：是
- 科学问题提出：部分是
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
- 多 Agent 协作：是
- 环境交互：是
- 闭环实验：否

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 实验驱动：否
- 仿真驱动：否
- 多模态：部分是
- 多尺度建模：否
- 高通量筛选：是
- 知识图谱：部分是
- 数字孪生：否
- 机器人平台：否
- 其他：multi-tool omics workflow

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：多组学治疗发现分析链条复杂，人工完成成本高
- 现有科研流程或方法的痛点：工具分散、解释难、跨任务整合差
- 核心假设或直觉：把规划、代码分析、文献推理和共识整合起来能形成可靠治疗发现 Agent

### 4.2 系统流程

1. 输入：omics therapeutic-discovery objective
2. 任务分解 / 规划：planning module 分解任务
3. 工具、数据库、模型或实验平台调用：code execution、omics resources、ML models、pathway knowledge
4. 中间结果反馈：文献推理与共识模块校正结论
5. 决策或迭代：跨步骤继续 refinement
6. 输出：治疗靶点、合成致死关系、响应预测结果

### 4.3 系统组件

- Agent 核心：Medea
- 工具 / API / 数据库：20 tools across transcriptomics、cancer vulnerability maps、pathways、ML models
- 记忆或状态模块：analysis state
- 规划器：planning module
- 评估器 / verifier：verification-aware analysis
- 人类反馈或专家介入：摘要未突出
- 实验平台或仿真环境：无

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：否
- 高通量计算：是
- 机器人实验：否
- 湿实验：否
- 临床数据：是
- 真实场景部署：否
- 专家评估：否

### 5.2 数据、任务与指标

- 数据集 / 实验对象：target identification、synthetic lethality、bladder-cancer immunotherapy response tasks
- 任务设置：开放式多组学治疗发现分析
- 对比基线：PMC 摘要称优于 existing approaches
- 评价指标：任务表现、透明性、verification-aware analysis
- 关键结果：完成 5679 次分析并在多个治疗相关任务上表现提升
- 是否有消融实验：摘要未展开
- 是否有失败案例或负结果：摘要未展开

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：是，偏治疗靶点与响应推断
- 科学贡献是否经过验证：有计算/数据层验证
- 贡献强度判断：中高
- 科学贡献类型：hypothesis / therapeutic_discovery / system_platform
- 证据强度：计算验证

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单个模型，而是多模块治疗发现 Agent
- 与已有 Agent / 科研智能系统的区别：verification-aware + multi-tool omics therapeutic workflow
- 与同一科学领域其他 Agent 文献的关系：可与 GALILEO、IMMUNIA、MADD、PromptBio 对比
- 主要创新点：以透明多步 Agent 链条处理治疗发现多组学任务

## 7. 局限性与风险

- Agent 自主性不足：没有湿实验闭环
- 科学验证不足：以计算/开放任务评测为主
- 泛化性不足：治疗任务类型虽多，但仍集中在 biomedical discovery
- 工具链依赖：高度依赖工具生态与数据资源
- 数据泄漏或 benchmark 偏差：需全文进一步检查
- 成本、可复现性或安全风险：多工具 orchestration 成本高

## 8. 对综述写作的价值

- 可放入哪个章节：07 医学与健康科学
- 可支撑哪个论点：多组学 Agent 已能稳定落在治疗发现对象上
- 可用于哪个表格或图：therapeutic discovery / omics agents table
- 适合作为代表性案例吗：适合
- 推荐引用强度：普通引用
- 需要在正文中特别引用的页码 / 图 / 表：后续补 PDF 细节
- 需要与哪些论文并列比较：0531、0541、0542、0545

## 9. 总结

### 9.1 一句话概括

Medea 用多组学 Agent 自动推进治疗发现分析。

### 9.2 速记版 pipeline

1. 接收治疗发现目标
2. 规划分析步骤
3. 调用多组学工具和文献推理
4. 共识整合结果
5. 输出靶点和响应发现

### 9.3 标注字段汇总

```text
是否纳入：to_read
主类：07
二级类：07.04
三级类：omics therapeutic discovery
四级专题：multi-tool therapeutic discovery agents
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Retrieval-augmented Agent; Multi-Agent System; Hybrid Agent
科研流程角色：literature_search_and_reading; knowledge_extraction_and_organization; scientific_question_formulation; hypothesis_generation; tool_use_and_code_execution; data_analysis; result_interpretation; evidence_assessment_and_validation; end_to_end_research_automation
自主能力：task_decomposition; planning; tool_use; memory_or_state_tracking; feedback_iteration; autonomous_decision_making; multi_agent_collaboration; environment_interaction
验证方式：benchmark; high_throughput_computation; clinical_data
交叉属性：computation_driven; data_driven; high_throughput_screening; knowledge_graph
科学贡献类型：hypothesis; therapeutic_discovery; system_platform
证据强度：computationally_validated
归类置信度：高
纳入置信度：高
推荐引用强度：standard
```
