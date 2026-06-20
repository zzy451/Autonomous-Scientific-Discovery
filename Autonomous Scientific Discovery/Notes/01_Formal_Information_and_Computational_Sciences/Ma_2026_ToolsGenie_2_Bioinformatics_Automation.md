# Ma et al. 2026 - ToolsGenie 2.0: A Scalable and Extensible Multi-Agent System for Bioinformatics Automation

**论文信息**
- 标题：ToolsGenie 2.0: A Scalable and Extensible Multi-Agent System for Bioinformatics Automation
- 作者：Ma et al.
- 年份：2026
- 来源 / venue：Research Square Preprint
- DOI / arXiv / URL：https://doi.org/10.64898/2026.01.06.697527
- PDF / 本地文件路径：本轮基于 DOI 注册摘要与 reviewer 一手证据；未保存本地 PDF
- 论文类型：系统论文 / bioinformatics automation platform
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | DOI registration abstract | multi-agent AI framework + sub-agents + tools + Docker orchestration | 高 |
| 科学对象归类 | `01.04` | DOI registration abstract | 贡献中心是 automation platform，不是单一生命科学对象 | 高 |
| 方法流程 | ReAct workflow substrate | DOI registration abstract | natural language and file input drive broad bioinformatics analyses | 高 |
| 实验验证 | benchmark / engineering evaluation | DOI registration abstract | BixBench + in-house dataset accuracy and extensibility | 中高 |
| 边界判断 | 应离开 `06.03` | object-first reading | workflow substrate outweighs broad bioinformatics application surface | 高 |

## 0. 摘要翻译

ToolsGenie 2.0 是一个可扩展的多智能体生物信息学自动化平台，支持自然语言查询、文件输入、子代理扩展与自动化环境管理，以执行广谱 bioinformatics analyses。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：具备多 Agent 协作、工具调用、环境管理和多步分析流程
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：部分
  - 多 Agent 协作：是
- 在科研流程中承担的明确角色：工具编排、数据分析、结果整合、端到端自动化

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不适用

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：01
- 二级类：01.04
- 三级类：通用科研工作流 / 生信自动化平台
- 四级专题：Bioinformatics automation platform
- 四级专题是否为新增：否
- 归类理由：主贡献是可扩展工作流基础设施，而非某个稳定生命科学对象的发现
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：bioinformatics automation capability
- 最终科学问题：如何让多 Agent 稳定执行可扩展的 bioinformatics workflows
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：平台虽然生信领域锚定很强，但贡献中心仍是 workflow substrate

### 2.3 容易混淆的边界

- 可能误归类到：06.03
- 最终判定：改到 01.04
- 判定理由：并无单一稳定基因/蛋白/疾病对象，benchmark 与 extensibility 更像平台论文
- 是否需要二次复核：是

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Multi-Agent System：是
- Tool-using Agent：是

### 3.2 科研流程角色

- 数据分析：是
- 工具调用与代码执行：是
- 结果解释：是
- 端到端科研流程自动化：是

### 3.3 自主能力

- 任务分解：是
- 计划生成：是
- 工具调用：是
- 反馈迭代：是
- 多 Agent 协作：是

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：提高生信工作流的自动化、可扩展性和可复现性
- 现有科研流程或方法的痛点：环境管理、工具编排和跨任务复用困难
- 核心假设或直觉：ReAct 风格多 Agent 架构加容器环境可稳定支持大范围生信任务

### 4.2 系统流程

1. 输入：自然语言问题或文件。
2. 任务分解 / 规划：主 Agent 分派子任务和子代理。
3. 工具、数据库、模型或实验平台调用：调用 specialized tools 与 Docker environments。
4. 中间结果反馈：执行结果回流并继续修正。
5. 决策或迭代：必要时扩展子代理和工作流。
6. 输出：自动化 bioinformatics analysis result。

### 4.3 系统组件

- Agent 核心：ReAct-style multi-agent architecture
- 工具 / API / 数据库：specialized bioinformatics tools
- 记忆或状态模块：execution state / extensible agents
- 规划器：top-level coordinator
- 评估器 / verifier：BixBench-style benchmark checks

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 专家评估：否

### 5.2 数据、任务与指标

- 数据集 / 实验对象：in-house dataset 与 BixBench-like tasks
- 任务设置：广谱 bioinformatics automation
- 评价指标：accuracy, extensibility, reproducibility
- 关键结果：平台强调可扩展性与工程可复现

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：主贡献是平台与工作流能力
- 科学贡献是否经过验证：有平台级 benchmark 证据
- 贡献强度判断：中
- 科学贡献类型：system_platform; analysis
- 证据强度：benchmark_only

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：重点在工作流自动化与环境管理
- 与已有 Agent / 科研智能系统的区别：更强调 extensibility 和 containerized execution
- 与同一科学领域其他 Agent 文献的关系：可与 PromptBio、BioAgent workflow papers 对照
- 主要创新点：把 bioinformatics automation 做成多 Agent extensible substrate

## 7. 局限性与风险

- 生信领域锚定很强，容易让人误读为 `06`
- 但 confirmed-core 的主要判断点不是领域名，而是对象是否足够具体
- 是否仍需进一步全文复核：是

## 8. 对综述写作的价值

- 可放入哪个章节：01.04 通用科研智能系统
- 可支撑哪个论点：不是所有 bioinformatics agent 都应自动留在生命科学主类
- 适合作为代表性案例吗：适合做边界样本
- 推荐引用强度：standard

## 9. 总结

### 9.1 一句话概括

可扩展多 Agent 平台自动化执行生信工作流。

### 9.2 速记版 pipeline

1. 接收问题或文件
2. 拆分生信任务
3. 调用工具和环境
4. 回流修正
5. 输出分析结果

### 9.3 标注字段汇总

```text
是否纳入：to_read
主类：01
二级类：01.04
三级类：通用科研工作流 / 生信自动化平台
四级专题：Bioinformatics automation platform
Agent 类型：LLM Agent; Multi-Agent System; Tool-using Agent
科研流程角色：data_analysis; tool_use_and_code_execution; result_interpretation; end_to_end_research_automation
自主能力：task_decomposition; planning; tool_use; feedback_iteration; multi_agent_collaboration
验证方式：benchmark
交叉属性：computation_driven; data_driven
科学贡献类型：system_platform; analysis
证据强度：benchmark_only
归类置信度：高
纳入置信度：高
推荐引用强度：standard
```
