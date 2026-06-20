# Luo 2025 - From intention to implementation: automating biomedical research via LLMs

**论文信息**
- 标题：From intention to implementation: automating biomedical research via LLMs
- 作者：Yi Luo et al.
- 年份：2025
- 来源 / venue：Science China Information Sciences
- DOI / arXiv / URL：https://doi.org/10.1007/s11432-024-4485-0 ; https://arxiv.org/abs/2412.09429
- PDF / 本地文件路径：未落本地 PDF；本轮依据 Springer 官方页与 arXiv 摘要级一手来源
- 论文类型：系统论文 / biomedical dry-lab research workflow automation
- 当前状态：已读 / confirmed core；2026-06-20 relaxed multi-module 复核后建议从独立 `01.04` 迁出，记录 `06;07`
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | arXiv abstract; Springer metadata | BioResearcher 被定义为端到端自动化 biomedical research system | 高 |
| 科学对象归类 | `06;07` | arXiv / full-text Appendix C | end-to-end objectives include liposarcoma, thyroid cancer, HCC, viral respiratory infection, transcriptomics, scRNA-seq, gene-expression, pathways and prognosis tasks | 高 |
| 方法流程 | 多步研究工作流 | arXiv abstract | 通过 task decomposition, hierarchical learning, reviewer agent, metrics 运行 | 高 |
| 实验验证 | 任务级评测 | arXiv abstract | 以 8 个 unmet research objectives 和 protocol quality 为核心验证 | 中 |
| 边界判断 | `07 + 06 > 01.04` | arXiv full text / Appendix C | 在 relaxed 口径下，具体 biomedical dry-lab objectives 和组学 / 基因表达任务已构成对象层 benchmark / case evidence，不应继续留在无具体对象实验的 `01.04` bucket | 高 |

## 0. 摘要翻译

论文提出 BioResearcher，目标是自动化 biomedical dry-lab research workflow。系统把复杂科研任务拆解为文献检索、文献处理、实验设计、编程与审阅等环节，并使用层级式 LLM Agent 组织整个流程。旧笔记曾把它放入独立 `01.04`，理由是主贡献偏 workflow automation；但 2026-06-20 relaxed 口径要求按实际对象覆盖记录模块。全文附录中的 end-to-end objectives 明确围绕 liposarcoma、thyroid cancer、HCC、viral respiratory infection 等医学对象，并使用 transcriptomics、scRNA-seq、gene-expression、pathway / prognosis modeling 等生命科学对象和数据，因此应记录 `07` 与 `06`，而不是继续作为无具体对象实验的 `01.04` 样本。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：具备明确科研目标、多步流程、任务分解、工具使用、LLM reviewer、中间反馈与专门 research role
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：是
- 在科研流程中承担的明确角色：文献处理、研究设计、协议生成、编程与中间审核

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- scientific_object_modules：`06;07`
- object_coverage_mode：`multi_module`
- has_concrete_object_experiments：yes
- general_method_bucket：none
- primary_module_for_filing：`07`
- 一级类：07；并记录 06
- 二级类：07.04 / 06.03 边界
- 三级类：biomedical dry-lab research automation with transcriptomics / gene-expression objectives
- 四级专题：Biomedical research workflow automation agents
- 四级专题是否为新增：否
- 归类理由：论文确实提出通用 biomedical workflow automation，但其评测和 case objectives 已经落到 liposarcoma / cancer / infection 等医学对象，以及 transcriptomics、scRNA-seq、gene-expression、pathway analysis 等生命科学对象；按 relaxed multi-module rule，应记录 `07;06`
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：biomedical dry-lab research objectives；具体覆盖 disease / cancer research 与 omics / gene-expression analysis
- 最终科学问题：如何把具体 biomedical dry-lab objectives 自动化为可检索文献 / 数据集、设计 protocol、生成并执行代码的 Agent pipeline
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：LLM 与多 Agent 只是实现手段；真正需要判定的是系统主要研究对象仍是 research workflow 本身

### 2.3 容易混淆的边界

- 可能误归类到：01.04
- 最终判定：`07;06`
- 判定理由：旧口径强调主贡献是否是 workflow platform；新口径强调是否存在具体对象实验 / benchmark task / case result。全文给出 8 个 end-to-end liposarcoma objectives，并在搜索与实验设计评测中覆盖 thyroid cancer、HCC、viral respiratory infection 等疾病及 transcriptomics / scRNA-seq / gene-expression 对象，足以离开独立 `01.04`
- 是否需要二次复核：不需要维持 `01.04`；若后续做 row-level schema migration，应把本记录从 independent `01.04` bucket 移出并记录 `scientific_object_modules = 06;07`

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：是
- Multi-Agent System：是
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：未突出
- Hybrid Agent：是
- 其他：Reviewer agent

### 3.2 科研流程角色

- 文献检索与阅读：是
- 知识抽取与组织：是
- 科学问题提出：部分
- 假设生成：部分
- 实验设计：是
- 仿真建模：否
- 工具调用与代码执行：是
- 实验执行：否
- 数据分析：部分
- 结果解释：部分
- 证据评估与验证：是
- 论文写作：未突出
- 端到端科研流程自动化：是

### 3.3 自主能力

- 任务分解：是
- 计划生成：是
- 工具调用：是
- 记忆与状态维护：部分
- 反馈迭代：是
- 自主决策：是
- 多 Agent 协作：是
- 环境交互：以软件工具为主
- 闭环实验：弱

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 实验驱动：否
- 仿真驱动：否
- 多模态：未突出
- 多尺度建模：否
- 高通量筛选：否
- 知识图谱：否
- 数字孪生：否
- 机器人平台：否
- 其他：workflow automation

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：减少 biomedical dry-lab research 中高人工成本、低复用、低自动化的问题
- 现有科研流程或方法的痛点：研究任务复杂、步骤分散、协议质量不稳定
- 核心假设或直觉：层级式 LLM Agent 可把 biomedical research task 转成结构化多步流程

### 4.2 系统流程

1. 输入：biomedical research objective
2. 任务分解 / 规划：拆分为搜索、阅读、设计、编程与审核
3. 工具、数据库、模型或实验平台调用：文献与软件工具
4. 中间结果反馈：reviewer agent 与 metrics 反馈
5. 决策或迭代：改写 protocol / code / design
6. 输出：面向 biomedical research 的自动化 protocol 与任务执行结果

### 4.3 系统组件

- Agent 核心：BioResearcher
- 工具 / API / 数据库：文献与编程工具
- 记忆或状态模块：层级式任务上下文
- 规划器：任务分解与层级学习
- 评估器 / verifier：LLM-based reviewer 与 evaluation metrics
- 人类反馈或专家介入：存在但不是主卖点
- 实验平台或仿真环境：dry-lab 研究任务

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：未突出
- 高通量计算：否
- 机器人实验：否
- 湿实验：否
- 临床数据：否
- 真实场景部署：否
- 专家评估：部分

### 5.2 数据、任务与指标

- 数据集 / 实验对象：8 个 end-to-end liposarcoma research objectives；另有 thyroid cancer、HCC、viral respiratory infection、pan-cancer / T cell exhaustion 等 search / experimental-design objectives
- 任务设置：自动完成 biomedical research workflow
- 对比基线：未在当前摘要证据中完全展开
- 评价指标：protocol quality 与任务完成表现
- 关键结果：自动化质量优于简单 pipeline 设定
- 是否有消融实验：摘要未明确
- 是否有失败案例或负结果：摘要未明确

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：主贡献仍偏 workflow automation，但评测任务和 case objectives 已经覆盖具体 disease / omics 对象；在 relaxed 口径下这足以支持 `07;06` 多模块记录
- 科学贡献是否经过验证：经过任务级评测
- 贡献强度判断：中
- 科学贡献类型：system_platform
- 证据强度：computationally_validated

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单点预测模型，而是端到端 biomedical research workflow Agent
- 与已有 Agent / 科研智能系统的区别：更明确聚焦 biomedical dry-lab process automation
- 与同一科学领域其他 Agent 文献的关系：可与 07 类药物发现 Agent 对照，展示“应用语境是 biomedical，但主对象仍可能是 workflow”
- 主要创新点：层级式 BioResearcher workflow

## 7. 局限性与风险

- Agent 自主性不足：真实 wet-lab 闭环未证明
- 科学验证不足：任务级成功不等于医学对象级发现
- 泛化性不足：8 个 objectives 的对象分布仍需全文核对
- 工具链依赖：依赖文献处理与代码工具
- 数据泄漏或 benchmark 偏差：需全文复核
- 成本、可复现性或安全风险：评测框架可能偏任务工程化

## 8. 对综述写作的价值

- 可放入哪个章节：07 医学与健康科学；同时作为 06 / 07 / 01.04 边界案例
- 可支撑哪个论点：通用 biomedical research-agent workflow 若包含具体 disease / omics objectives，应按对象证据记录具体模块，`01.04` 不能覆盖这些对象层实验
- 可用于哪个表格或图：01.04 / 06 / 07 边界案例表
- 适合作为代表性案例吗：适合做边界案例
- 推荐引用强度：普通引用
- 需要在正文中特别引用的页码 / 图 / 表：摘要与官方 metadata
- 需要与哪些论文并列比较：OriGene, PerTurboAgent, HealthFlow

## 9. 总结

### 9.1 一句话概括

面向具体 biomedical dry-lab objectives 的多 Agent 研究流程自动化系统。

### 9.2 速记版 pipeline

1. 接收 biomedical 研究目标
2. 拆分成搜索、阅读、设计、编程与审核
3. 调用工具并生成 protocol
4. reviewer agent 反馈修正
5. 输出自动化研究工作流结果

### 9.3 标注字段汇总

```text
是否纳入：是
scientific_object_modules：06;07
object_coverage_mode：multi_module
has_concrete_object_experiments：yes
general_method_bucket：none
primary_module_for_filing：07
主类：07
二级类：07.04 / 06.03
三级类：biomedical dry-lab research automation; transcriptomics / gene-expression / disease-object objectives
四级专题：Biomedical research workflow automation agents
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Retrieval-augmented Agent; Multi-Agent System; Hybrid Agent
科研流程角色：literature_search_and_reading; knowledge_extraction_and_organization; experimental_design; tool_use_and_code_execution; evidence_assessment_and_validation; end_to_end_research_automation
自主能力：task_decomposition; planning; tool_use; feedback_iteration; autonomous_decision_making; multi_agent_collaboration
验证方式：benchmark; expert_evaluation
交叉属性：computation_driven; data_driven
科学贡献类型：system_platform
证据强度：computationally_validated
归类置信度：高（2026-06-20 relaxed multi-module 复核；一手来源为 arXiv full text / Appendix C）
纳入置信度：高
推荐引用强度：普通引用
```
