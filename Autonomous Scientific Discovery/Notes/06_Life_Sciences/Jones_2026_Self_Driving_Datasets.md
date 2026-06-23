# Jones et al. 2026 - Self-Driving Datasets: From 20 Million Papers to Nuanced Biomedical Knowledge at Scale

**论文信息**
- 标题：Self-Driving Datasets: From 20 Million Papers to Nuanced Biomedical Knowledge at Scale
- 作者：Haydn Jones; Yimeng Zeng; Alden Rose; Li S. Yifei; Yining Huang; Kaiwen Wu; Jiaming Liang; Maggie Ziyu Huan; Yoseph Barash; Cesar de la Fuente-Nunez; Osbert Bastani; Zachary Ives; Mark Yatskar; Jacob R. Gardner
- 年份：2026
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2605.07022
- PDF / 本地文件路径：当前写回以 arXiv abstract (`2605.07022`) 作为一手来源；本地未归档 PDF
- 论文类型：系统论文 / biomedical dataset-construction agents
- 当前状态：to_read
- 阅读日期：2026-06-20
- 笔记作者：Codex

## Evidence Log

## 2026-06-20 relaxed multi-module revision

```text
scientific_object_modules: 03;06;07
object_coverage_mode: multi_module
has_concrete_object_experiments: yes
general_method_bucket: none
primary_module_for_filing: 06
first_hand_sources_checked: arXiv abstract `2605.07022`
classification_evidence_source_level: first_hand_abstract_or_landing_page
module_assignment_evidence: `03` is supported by chemical-reaction extraction tasks; `06` is supported by gene-disease, protein localization, and biological knowledge-extraction tasks; `07` is supported by BBB permeability, oral bioavailability, LD50, and biomedical / pharmacological property tasks.
multi_module_object_coverage_note: The old 06-only filing is too narrow under the relaxed rule. The paper builds self-driving biomedical datasets, but its reported extraction tasks span chemistry, life science, and medical / pharmacological objects.
```

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | arXiv abstract / HTML / GitHub | Starling 被明确描述为 multi-agent deep research system | 高 |
| 明确科研目标 | 是 | arXiv abstract | 目标是把 PubMed 自主转成更大、更细致、更准确的 biomedical structured datasets | 高 |
| 多步行动 | 是 | arXiv abstract / HTML §1, §3 | 系统自动设计 retrieval filters、归纳 extraction schema、输出结构化 records 与 supporting passages | 高 |
| 科研流程角色 | 是 | arXiv abstract / GitHub README | 承担 literature search、knowledge extraction、evidence organization、dataset construction | 高 |
| 科学对象归类 | 支持 `03;06;07`，primary `06` | arXiv abstract | chemical reactions 支撑 `03`；gene-disease 与 protein localization 支撑 `06`；BBB、oral bioavailability 与 LD50 支撑 `07` | 高 |
| 边界判断 | 不是 `01.04`，也不能只写成 `06` | arXiv abstract | 虽有平台外观，但任务集合已经跨 chemistry、life science 与 medical / pharmacological objects，需按 relaxed multi-module rule 显式记为 `03;06;07` | 中高 |
| 主要剩余风险 | core-strength risk | arXiv abstract / GitHub | 更像高质量 dataset-building / literature-mining agent，而非更强的 hypothesis-to-experiment discovery loop | 中高 |

## 0. 摘要翻译

论文认为，人工维护的生物医学数据库昂贵、滞后且会丢失实验语境，因此提出从 2250 万篇 PubMed 文献中自主构建结构化 biomedical datasets 的方案。系统包含实体标注、混合 sparse-dense retrieval，以及 Starling 多 Agent deep research agent；给定自然语言任务描述后，系统自动设计高精度/高召回检索过滤器、归纳抽取 schema，并输出带 supporting passages 的结构化记录。论文在六个 biomedical tasks 上共产出约 630 万条记录，并声称在规模与准确率上优于多种人工整理数据库；作者进一步将其定位为 AI-driven therapeutic design 的基础设施。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：存在明确科研目标、多步自主行动、显式多 Agent 角色分工、工具与检索调用、证据支持的结构化输出
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：是
- 在科研流程中承担的明确角色：文献检索与阅读、知识抽取与组织、证据评估、数据集构建

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：06（primary module for filing）
- 二级类：06.03
- 三级类：生物医学知识抽取 / 生物信息数据构建
- 四级专题：Multi-agent biomedical knowledge-extraction systems
- 四级专题是否为新增：否
- 归类理由：当前可识别任务同时覆盖 chemical-reaction extraction（`03`）、gene / protein biological knowledge extraction（`06`）以及 BBB permeability、oral bioavailability、LD50 等 pharmacological property extraction（`07`）；笔记落在 `06` 目录仅是 filing convenience，不覆盖 `03;06;07` 的多模块事实
- 归类置信度：中高

### 2.2 对象优先判定

- 最终科学研究对象：大规模 biomedical literature 中的 chemical reactions、gene / protein biological knowledge 以及 pharmacological property records
- 最终科学问题：如何从生物医学文献中自动构建高质量结构化知识数据集
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：multi-agent 架构只是手段，具体输出对象仍然属于生命科学 / 生物医学知识构建

### 2.3 容易混淆的边界

- 可能误归类到：01.04
- 最终判定：支持 `03;06;07`，primary `06`
- 判定理由：尽管系统形态偏平台化，但六项任务已经分别给出 chemistry、life science 与 medical / pharmacological object coverage，不能回收到 `01.04`，也不应继续只保留旧的 `06` 单模块表述
- 是否需要二次复核：是

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：是
- Multi-Agent System：是
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：否
- Hybrid Agent：是
- 其他：deep research agents

### 3.2 科研流程角色

- 文献检索与阅读：是
- 知识抽取与组织：是
- 科学问题提出：否
- 假设生成：部分是
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
- 多模态：否
- 多尺度建模：否
- 高通量筛选：否
- 知识图谱：部分是
- 数字孪生：否
- 机器人平台：否
- 其他：literature-scale dataset construction

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：替代昂贵且滞后的人工 curated biomedical repositories
- 现有科研流程或方法的痛点：数据库更新慢、覆盖不全、丢失 supporting context
- 核心假设或直觉：LLM + retrieval + multi-agent deep research 可把大规模 PubMed 自动转成结构化 biomedical datasets

### 4.2 系统流程

1. 输入：自然语言 biomedical extraction task
2. 任务分解 / 规划：设计 precision / recall 导向的 retrieval filters
3. 工具、数据库、模型或实验平台调用：调用 entity tagging、hybrid retrieval、schema induction、record extraction
4. 中间结果反馈：根据 supporting passages 和 schema 迭代修正抽取
5. 决策或迭代：输出结构化 records 与 nuance-rich fields
6. 输出：可用于下游生物医学研究的数据集

### 4.3 系统组件

- Agent 核心：Starling multi-agent deep research system
- 工具 / API / 数据库：PubMed corpus、ontology tagging、hybrid sparse-dense retrieval
- 记忆或状态模块：task schema 与 evidence-backed records
- 规划器：retrieval-filter 与 extraction-schema design
- 评估器 / verifier：supporting passages 与 frontier-model rejection
- 人类反馈或专家介入：未作为主流程核心
- 实验平台或仿真环境：六个 biomedical dataset-construction tasks

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：否
- 高通量计算：否
- 机器人实验：否
- 湿实验：否
- 临床数据：否
- 真实场景部署：否
- 专家评估：部分是

### 5.2 数据、任务与指标

- 数据集 / 实验对象：22.5M-paper PubMed corpus；六个 biomedical tasks
- 任务设置：blood-brain barrier permeability、oral bioavailability、acute toxicity、gene-disease associations、protein localization、chemical reactions
- 对比基线：widely used curated counterparts
- 评价指标：record scale、frontier-model rejection rate、对照数据库 error rate
- 关键结果：约 6.3M 记录；frontier-model rejection `0.6-7.7%`
- 是否有消融实验：HTML 全文可进一步细读
- 是否有失败案例或负结果：摘要级证据未充分展开

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：更偏生命科学知识抽取与数据构建能力增强
- 科学贡献是否经过验证：部分是
- 贡献强度判断：中
- 科学贡献类型：系统平台 / 生物医学知识构建
- 证据强度：计算与对照数据库验证

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单次 predictor，而是 literature-to-dataset 的多 Agent deep-research system
- 与已有 Agent / 科研智能系统的区别：强调 evidence-linked dataset construction，而非单纯问答或单轮抽取
- 与同一科学领域其他 Agent 文献的关系：可与 CellAgent、GenoMAS、BioGAIP 构成 `06.03 / 01.04` 压力样本群
- 主要创新点：将大规模 biomedical literature 检索、schema induction 与 record extraction 联成自主工作流

## 7. 局限性与风险

- Agent 自主性不足：仍主要停留在 knowledge-construction，而非更强 discovery loop
- 科学验证不足：缺少湿实验或更强 hypothesis validation
- 泛化性不足：虽然任务多样，但仍主要在 biomedical dataset construction
- 工具链依赖：高度依赖 ontology tagging 与 retrieval stack
- 数据泄漏或 benchmark 偏差：需后续继续核
- 成本、可复现性或安全风险：大规模语料与模型调用成本较高

## 8. 对综述写作的价值

- 可放入哪个章节：06 生命科学中的 biomedical knowledge-extraction agents
- 可支撑哪个论点：Agent 已深入生命科学文献抽取和证据组织流程
- 可用于哪个表格或图：`06.03 / 01.04` 边界案例表；life-science workflow role 对比表
- 适合作为代表性案例吗：是，但需注明 core-strength 风险
- 推荐引用强度：普通引用
- 需要在正文中特别引用的页码 / 图 / 表：arXiv abstract / HTML 中的 six-task description 与 rejection-rate statement
- 需要与哪些论文并列比较：Liu_2025_GenoMAS; Zhang_2025_PromptBio_Bioinformatics; Zhang_2026_BioGAIP_Bioinformatics

## 9. 总结

### 9.1 一句话概括

从 PubMed 自主造 biomedical datasets。

### 9.2 速记版 pipeline

1. 输入 biomedical task
2. 设计检索过滤器
3. 归纳抽取 schema
4. 输出带证据的结构化 records
5. 构建下游可用数据集

### 9.3 标注字段汇总

```text
是否纳入：to_read
主类：06
二级类：06.03
三级类：生物医学知识抽取 / 生物信息数据构建
四级专题：Multi-agent biomedical knowledge-extraction systems
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Retrieval-augmented Agent; Multi-Agent System; Hybrid Agent
科研流程角色：literature_search_and_reading; knowledge_extraction_and_organization; tool_use_and_code_execution; data_analysis; result_interpretation; evidence_assessment_and_validation; end_to_end_research_automation
自主能力：task_decomposition; planning; tool_use; memory_or_state_tracking; feedback_iteration; autonomous_decision_making; multi_agent_collaboration; environment_interaction
验证方式：benchmark; computational_validation
交叉属性：computation_driven; data_driven
科学贡献类型：system_platform
证据强度：computationally_validated
归类置信度：中高
纳入置信度：高
推荐引用强度：standard
```
## 2026-06-24 writeback adjudication

- `scientific_object_modules`: `03;06;07`
- `object_coverage_mode`: `multi_module`
- `primary_module_for_filing`: `06`
- `general_method_bucket`: `none`
- `first_hand_sources_checked`: arXiv abstract `2605.07022`
- `classification_evidence_source_level`: `first_hand_abstract_or_landing_page`
- `source_limited`: `no`
- `note_revision_required`: `yes`

This writeback makes the multi-module evidence explicit. The paper should not be described as `06`-only or as an independent `01.04`-style general-method note, because the reported tasks cover chemical-reaction extraction (`03`), biological knowledge extraction (`06`), and pharmacological / biomedical property extraction (`07`).
