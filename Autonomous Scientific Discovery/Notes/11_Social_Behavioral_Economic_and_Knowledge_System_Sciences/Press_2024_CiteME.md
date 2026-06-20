# Press et al. 2024 - CiteME: Can Language Models Accurately Cite Scientific Claims?

**论文信息**
- 标题：CiteME: Can Language Models Accurately Cite Scientific Claims?
- 作者：Ori Press; Andreas Hochlehnert; Ameya Prabhu; Vishaal Udandarao; Ofir Press; Matthias Bethge
- 年份：2024
- 来源 / venue：NeurIPS 2024 Datasets and Benchmarks / OpenReview
- DOI / arXiv / URL：https://openreview.net/forum?id=S9Qrrxpy6z
- PDF / 本地文件路径：当前笔记基于 OpenReview 摘要与 reviewer 一手全文证据
- 论文类型：benchmark-rich agent paper / scientific-claim attribution
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | 摘要；Section 3 | CiteAgent 是 autonomous system，会反复 search, read, select | 高 |
| 科学对象归类 | `11.07` | 摘要；正文 | 对象是 scientific claim citation attribution / verification | 高 |
| 方法流程 | 多步 search-read-select | Section 3 | 依次搜索文献、读取 PDF、改写查询并最终选择 citation | 高 |
| 工具调用 | 强 | 正文 | 使用 Semantic Scholar 与 open-access PDF text | 高 |
| 验证方式 | benchmark-first | 摘要 | 普通 LMs `4.2–18.5%`，人类 `69.7%`，CiteAgent 最佳约 `35.3%` | 高 |

## 0. 摘要翻译

论文提出 CiteME 任务，并引入一个可搜索和阅读论文的 CiteAgent 来做 scientific claim attribution。作者比较普通语言模型、人类与 agent 系统在 citation attribution 上的表现，发现现有模型与人类差距很大，而通过多步搜索和阅读可以显著提升结果，但仍远未达到人类水平。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：系统有明确 scholarly claim verification 目标，存在多步搜索、阅读、重试与选择流程
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：部分是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：否
- 在科研流程中承担的明确角色：文献搜索、证据阅读、citation attribution、证据评估

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：11
- 二级类：11.07
- 三级类：scientific-claim attribution and verification
- 四级专题：citation-grounding agent systems
- 四级专题是否为新增：否
- 归类理由：任务研究的是 scholarly communication 中 claim 与 citation 的对应关系
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：scientific claim attribution / verification
- 最终科学问题：语言模型能否为科学断言准确找到支撑性文献
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：benchmark 外观不能改变对象本身属于 scientific knowledge verification

### 2.3 容易混淆的边界

- 可能误归类到：01.04
- 最终判定：保留 11.07
- 判定理由：论文不在研究通用检索助手，而是在研究 scholarly claim attribution
- 是否需要二次复核：否

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：部分是
- Tool-using Agent：是
- Retrieval-augmented Agent：是
- Multi-Agent System：否
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：否
- Hybrid Agent：是
- 其他：citation attribution agent

### 3.2 科研流程角色

- 文献检索与阅读：是
- 知识抽取与组织：部分是
- 科学问题提出：否
- 假设生成：否
- 实验设计：否
- 仿真建模：否
- 工具调用与代码执行：是
- 实验执行：否
- 数据分析：是
- 结果解释：部分是
- 证据评估与验证：是
- 论文写作：否
- 端到端科研流程自动化：部分是

### 3.3 自主能力

- 任务分解：部分是
- 计划生成：部分是
- 工具调用：是
- 记忆与状态维护：是
- 反馈迭代：是
- 自主决策：是
- 多 Agent 协作：否
- 环境交互：是
- 闭环实验：否

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 实验驱动：否
- 仿真驱动：否
- 多模态：否
- 多尺度建模：否
- 高通量筛选：否
- 知识图谱：否
- 数字孪生：否
- 机器人平台：否
- 其他：scientific PDF reading

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：普通 LMs 在 scientific citation attribution 上表现很差
- 现有科研流程或方法的痛点：模型不会主动搜索、阅读和验证支撑证据
- 核心假设或直觉：把检索、阅读和重试串成 agent loop，可明显提升 attribution 准确率

### 4.2 系统流程

1. 输入：待归因的 scientific claim
2. 任务分解 / 规划：先 search，再进入 read / re-search 循环
3. 工具、数据库、模型或实验平台调用：Semantic Scholar 与 open-access PDFs
4. 中间结果反馈：根据已读论文更新查询与候选判断
5. 决策或迭代：选择最终 citation
6. 输出：claim 对应的 supporting citation

### 4.3 系统组件

- Agent 核心：CiteAgent
- 工具 / API / 数据库：Semantic Scholar、open-access PDF text
- 记忆或状态模块：已搜索 / 已阅读 candidate set
- 规划器：search-read-select loop
- 评估器 / verifier：human benchmark + ablation
- 人类反馈或专家介入：benchmark labeling
- 实验平台或仿真环境：citation attribution task environment

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：否
- 高通量计算：否
- 机器人实验：否
- 湿实验：否
- 临床数据：否
- 真实场景部署：否
- 专家评估：是

### 5.2 数据、任务与指标

- 数据集 / 实验对象：CiteME benchmark
- 任务设置：scientific claim attribution
- 对比基线：普通 LMs、人类、ablation settings
- 评价指标：citation attribution accuracy
- 关键结果：best CiteAgent 约 `35.3%`，明显高于纯 LM，但仍低于人类
- 是否有消融实验：有
- 是否有失败案例或负结果：有明显 performance gap discussion

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：更偏 benchmark + agent workflow
- 科学贡献是否经过验证：是
- 贡献强度判断：中
- 科学贡献类型：benchmark
- 证据强度：中高

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：强调 scholarly claim verification 而非通用文献问答
- 与已有 Agent / 科研智能系统的区别：对象是 citation attribution / evidence grounding
- 与同一科学领域其他 Agent 文献的关系：可与 SciSciGPT、ReviewAgents、citation-network simulations 构成 `11.07` 内部不同子方向
- 主要创新点：把 citation attribution 做成 explicit agent loop

## 7. 局限性与风险

- Agent 自主性不足：强项集中在检索和选择，科学推理深度有限
- 科学验证不足：更像 benchmark-first agent paper
- 泛化性不足：仅覆盖 scientific claim attribution
- 工具链依赖：依赖开放 PDF 与检索 API
- 数据泄漏或 benchmark 偏差：需要持续关注 benchmark 设计
- 成本、可复现性或安全风险：主风险更偏 core-strength，而不是主类风险

## 8. 对综述写作的价值

- 可放入哪个章节：`11.07` 中的 scientific knowledge verification
- 可支撑哪个论点：benchmark 外观不妨碍对象稳定落在 `11.07`
- 可用于哪个表格或图：citation verification agent 对比表
- 适合作为代表性案例吗：可作为边界与 benchmark 样本
- 推荐引用强度：普通引用
- 需要在正文中特别引用的页码 / 图 / 表：Section 3 workflow 与人类 / agent 对比结果
- 需要与哪些论文并列比较：ASD-0624、ASD-0637、review / peer-review agents

## 9. 总结

### 9.1 一句话概括

用多步搜索与阅读的 CiteAgent 做 scientific claim attribution。

### 9.2 速记版 pipeline

1. 输入 scientific claim  
2. 搜索候选论文  
3. 读取并重试查询  
4. 选出支撑 citation

### 9.3 标注字段汇总

```text
是否纳入：是
主类：11
二级类：11.07
三级类：scientific-claim attribution and verification
四级专题：citation-grounding agent systems
Agent 类型：LLM Agent; Tool-using Agent; Retrieval-augmented Agent; Hybrid Agent
科研流程角色：literature_search_and_reading; tool_use_and_code_execution; data_analysis; evidence_assessment_and_validation
自主能力：tool_use; memory_or_state_tracking; feedback_iteration; autonomous_decision_making; environment_interaction
验证方式：benchmark; expert_evaluation
交叉属性：computation_driven; data_driven
科学贡献类型：benchmark
证据强度：high_primary_abstract
归类置信度：高
纳入置信度：高
推荐引用强度：standard
```
