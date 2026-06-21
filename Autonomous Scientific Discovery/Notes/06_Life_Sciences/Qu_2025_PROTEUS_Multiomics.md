# Qu 2025 - Automating exploratory multiomics research via language models

**论文信息**
- 标题：Automating exploratory multiomics research via language models
- 作者：Shang Qu et al.
- 年份：2025
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2506.07591
- PDF / 本地文件路径：本轮使用 arXiv 摘要页一手证据；未保存本地 PDF
- 论文类型：系统论文
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

## 2026-06-21 relaxed round-2 boundary closure

- `first_hand_sources_checked`: arXiv abstract; arXiv full PDF `2506.07591`.
- Accepted relaxed classification: accept `scientific_object_modules=06;07`; `object_coverage_mode=multi_module`; `primary_module_for_filing=06`; `general_method_bucket=none`.
- Why: the paper's main workflow still targets multiomics molecular entities and biological-mechanism discovery, which keeps `06` as the filing module. At the same time, the full text is built on cancer clinical multiomics cohorts and repeatedly performs survival, prognosis, and other clinical-feature analyses with same-cancer CPTAC validation, which is enough to add `07` under the relaxed object-coverage rule.
- Note implication: this note should no longer keep `07` as a weaker metadata-level possibility. The current first-hand full text is sufficient to close the `06/07` boundary as `06;07`.

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | arXiv abstract | PROTEUS 是 fully automated system，从 raw data files 直接生成 data-driven hypotheses | 高 |
| 科学对象归类 | `06.03` | arXiv abstract | 论文锚定 clinical proteogenomics / multiomics，而主对象仍是 omics data 与 biological entities relationships | 高 |
| 边界判断 | `06` 优先于 `07` | arXiv abstract | 虽有 clinical framing，但输出对象是 multiomics hypothesis generation，不是患者级诊疗系统 | 高 |
| 方法流程 | exploratory + iterative | arXiv abstract | 从 open-ended data exploration 到 statistical analysis 再到 hypothesis proposal，且用 unified graph structures 管理研究过程 | 高 |
| 验证方式 | external data validation | arXiv abstract | 在 10 个 published clinical multiomics datasets 上产生 360 hypotheses，并做 external data validation 与自动评分 | 高 |

## 0. 摘要翻译

作者提出 PROTEUS，一个从原始数据文件中直接产生数据驱动假设的全自动系统，并把它应用于临床蛋白基因组学。该系统试图模拟科学过程的不同阶段，从开放式数据探索到具体统计分析，再到假设提出。系统把研究方向、分析工具和结果都表示为生物实体之间的关系，并用统一图结构来管理复杂研究流程。作者将 PROTEUS 应用于 10 个已发表的临床多组学数据集，最终得到 360 条假设，并通过外部数据验证和自动开放式评分来评估结果。论文认为，这种探索式、迭代式研究流程可以在高通量、异质的多组学数据中平衡可靠性与新颖性。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：具备自动化研究方向形成、统计分析、假设生成与迭代探索的多步科研流程
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：摘要未明确为社会式多代理，但模块分工清晰
- 在科研流程中承担的明确角色：数据探索、统计分析、假设提出

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：06
- 二级类：06.03
- 三级类：clinical proteogenomics / multiomics research
- 四级专题：Exploratory multiomics hypothesis-generation agents
- 四级专题是否为新增：否
- 归类理由：论文围绕多组学数据中的生物实体关系与数据驱动假设生成展开，主对象更接近 omics / life-science discovery
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：clinical proteogenomics / multiomics data 中的 biological entities relationships
- 最终科学问题：如何在高维多组学数据中自动生成可靠且新颖的生物学假设
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：fully automated system 是方法框架，主对象仍是多组学生物研究

### 2.3 容易混淆的边界

- 可能误归类到：07
- 最终判定：保留 06.03
- 判定理由：clinical 只定义数据来源和应用背景；当前系统的直接科研对象仍是 multiomics biology，而不是医疗决策
- 是否需要二次复核：是，但更偏证据强度复核

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：未明确
- Multi-Agent System：未明确
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：否
- Hybrid Agent：是
- 其他：graph-structured exploratory research system

### 3.2 科研流程角色

- 文献检索与阅读：未明确
- 知识抽取与组织：是
- 科学问题提出：是
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
- 记忆与状态维护：图结构承担部分状态管理
- 反馈迭代：是
- 自主决策：是
- 多 Agent 协作：摘要未展开
- 环境交互：是
- 闭环实验：否

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 实验驱动：否
- 仿真驱动：否
- 多模态：否
- 多尺度建模：否
- 高通量筛选：是
- 知识图谱：是
- 数字孪生：否
- 机器人平台：否
- 其他：open-ended research automation

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：临床多组学数据下游分析与假设形成复杂且高成本
- 现有科研流程或方法的痛点：高通量异质数据难以通过人工高效完成探索式研究
- 核心假设或直觉：把科学过程拆分成数据探索、分析与假设形成阶段，并统一表示为图结构，可实现开放式自动研究

### 4.2 系统流程

1. 输入：原始多组学数据文件
2. 任务分解 / 规划：形成研究方向与分析路径
3. 工具、数据库、模型或实验平台调用：执行统计分析并组织 biological entities relationships
4. 中间结果反馈：在探索式过程中迭代修正研究方向
5. 决策或迭代：输出新的假设并继续探索
6. 输出：data-driven hypotheses

### 4.3 系统组件

- Agent 核心：PROTEUS
- 工具 / API / 数据库：统计分析模块与 unified graph structures
- 记忆或状态模块：图结构
- 规划器：有
- 评估器 / verifier：external data validation 与 automatic open-ended scoring
- 人类反馈或专家介入：摘要未强调
- 实验平台或仿真环境：无

## 5. 实验与验证

### 5.1 验证方式

- benchmark：有自动评分
- 仿真验证：否
- 高通量计算：否
- 机器人实验：否
- 湿实验：否
- 临床数据：是
- 真实场景部署：否
- 专家评估：未明确

### 5.2 数据、任务与指标

- 数据集 / 实验对象：10 个已发表的 clinical multiomics datasets
- 任务设置：exploratory data analysis + statistical analysis + hypothesis proposal
- 对比基线：摘要未展开
- 评价指标：external data validation；automatic open-ended scoring
- 关键结果：360 total hypotheses
- 是否有消融实验：摘要未展开
- 是否有失败案例或负结果：摘要未展开

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：主要是新假设
- 科学贡献是否经过验证：有外部数据验证，但非湿实验
- 贡献强度判断：中高
- 科学贡献类型：hypothesis; system_platform
- 证据强度：computationally_validated

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单模型做一项预测，而是自动化 exploratory multiomics research
- 与已有 Agent / 科研智能系统的区别：突出从 raw data 到 hypotheses 的 open-ended path
- 与同一科学领域其他 Agent 文献的关系：可与 OmniCellAgent、CellAtria、BioDiscoveryAgent 并列为 omics-agent 案例
- 主要创新点：graph-structured exploratory research automation

## 7. 局限性与风险

- Agent 自主性不足：当前证据主要来自摘要
- 科学验证不足：缺少湿实验或临床转化验证
- 泛化性不足：主要聚焦临床多组学
- 工具链依赖：依赖统计分析与图结构工作流
- 数据泄漏或 benchmark 偏差：需全文复核
- 成本、可复现性或安全风险：未展开

## 8. 对综述写作的价值

- 可放入哪个章节：06 生命科学
- 可支撑哪个论点：Agent 可以直接在多组学数据上做探索式假设生成，而不只是辅助问答
- 可用于哪个表格或图：组学 Agent 假设生成表
- 适合作为代表性案例吗：适合
- 推荐引用强度：普通到核心之间
- 需要在正文中特别引用的页码 / 图 / 表：当前以 arXiv 摘要为主
- 需要与哪些论文并列比较：OmniCellAgent、CellAtria、BioDiscoveryAgent、CellVoyager

## 9. 总结

### 9.1 一句话概括

从原始多组学数据自动生成生物学假设的探索式 Agent 系统。

### 9.2 速记版 pipeline

1. 读入多组学原始数据  
2. 形成研究方向  
3. 做统计分析  
4. 生成并筛选假设  
5. 用外部数据再验证

### 9.3 标注字段汇总

```text
是否纳入：to_read
主类：06
二级类：06.03
三级类：clinical proteogenomics / multiomics research
四级专题：Exploratory multiomics hypothesis-generation agents
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Hybrid Agent
科研流程角色：knowledge_extraction_and_organization; scientific_question_formulation; hypothesis_generation; tool_use_and_code_execution; data_analysis; result_interpretation; evidence_assessment_and_validation; end_to_end_research_automation
自主能力：task_decomposition; planning; tool_use; memory_or_state_tracking; feedback_iteration; autonomous_decision_making
验证方式：clinical_data; computational_validation
交叉属性：computation_driven; data_driven; high_throughput_screening; knowledge_graph
科学贡献类型：hypothesis; system_platform
证据强度：computationally_validated
归类置信度：高
纳入置信度：高
推荐引用强度：standard
```
