# Wang et al. 2025 - GeneAgent: self-verification language agent for gene-set analysis using domain databases

**论文信息**
- 标题：GeneAgent: self-verification language agent for gene-set analysis using domain databases
- 作者：Wang et al.
- 年份：2025
- 来源 / venue：Nature Methods
- DOI / arXiv / URL：https://doi.org/10.1038/s41592-025-02748-6
- PDF / 本地文件路径：Nature Methods 正式页面 https://www.nature.com/articles/s41592-025-02748-6；官方 PDF https://www.nature.com/articles/s41592-025-02748-6.pdf；本地预印本归档 `Reference_PDF/06_Life_Sciences/Wang_2024_GeneAgent.pdf`
- 论文类型：research paper
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex
- 2026-06-22 re-audit sync：已按本轮 adjudication 复核 Nature Methods 正式全文 / 官方 PDF 与本地预印本；当前结论为 `supported_modules=06`、`primary_module_for_filing=06`、`final_01_04_bucket=no`，且 `source_limited=no` / `safety=no_safety_skip`，无需进一步全文复核。

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | Nature Methods 正式全文 / 官方 PDF：Abstract；Fig. 1 | 明确给出 generation -> self-verification -> modification -> summarization 四阶段流程，并在流程中自主调用领域数据库与验证步骤 | 高 |
| 科学对象归类 | `06.03`，且本轮仅支持模块 `06` | Nature Methods 正式全文 / 官方 PDF：Abstract；gene-set analysis task framing；case studies | 论文稳定围绕 gene sets、GO / pathway knowledge 和 biological mechanism explanation 展开，属于生命科学知识分析对象，而非通用科研方法 | 高 |
| 方法流程 | 明确闭环 | Nature Methods 正式全文 / 官方 PDF：Fig. 1；Methods / Results 中的 self-verification 描述 | 系统会先生成命名与解释，再检索和核验 claims，随后修正与汇总输出 | 高 |
| 实验验证 | 强 | Nature Methods 正式全文 / 官方 PDF：Results；benchmark evaluation；novel gene-set cases | 在 1,106 个 gene sets 上系统评测，并对 `15,903` 个 claims 做核验，其中 `99.6%` 被验证通过；另给出 melanoma 新 gene sets 案例 | 高 |
| 边界判断 | 不属于 `01.04`，应保留在 `06` | Nature Methods 正式全文 / 官方 PDF 全文对象 framing；本地预印本交叉核对 | 虽然系统外观像通用语言代理，但实验对象、数据库调用和结果解释都稳定锚定 gene-set biology，因此 `01.04` 不是正确 bucket | 高 |

## 0. 摘要翻译

论文提出 GeneAgent，把 GPT-4 与自验证流程、基因功能数据库和富集分析 API 结合，用于基因集功能命名与解释，并显著降低幻觉。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：有明确科研目标、四步闭环、自主数据库调用、事实核验和输出修正
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：否
- 在科研流程中承担的明确角色：知识抽取、数据分析、证据评估、结果解释

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 科学对象模块：06
- 覆盖模式：单模块
- 是否具有具体科学对象实验、验证、benchmark task、case study 或结果报告：是
- 独立 `01.04` 存放区：none
- Primary module for filing：06
- 一级类：06
- 二级类：06.03
- 三级类：
- 四级专题：Gene-set analysis agents
- 四级专题是否为新增：否
- 归类理由：最终对象是 gene sets、GO、pathway knowledge 与 biological mechanism interpretation
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：gene-set biological functions and pathways
- 最终科学问题：如何更准确解释基因集功能并减少 LLM 幻觉
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：虽然是通用语言代理外观，但任务与验证对象稳定属于生命科学知识分析

### 2.3 容易混淆的边界

- 可能误归类到：01.04
- 最终判定：保持 06.03
- 判定理由：对象是 gene functions / pathway knowledge，而不是领域无关 research-agent workflow
- 多模块覆盖说明：本轮 adjudication 仅支持 `06`，笔记落在生命科学目录仅作为 filing convenience，与对象归类一致
- 01.04 判定说明：不是独立 `01.04` 存放区论文，因为全文包含明确的 gene-set biological-function 任务、benchmark 和案例结果
- 是否需要二次复核：否

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：是
- Multi-Agent System：否
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：否
- Hybrid Agent：是
- 其他：self-verification agent

### 3.2 科研流程角色

- 文献检索与阅读：否
- 知识抽取与组织：是
- 科学问题提出：否
- 假设生成：部分
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
- 其他：biological databases

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：传统 gene-set naming 与解释容易受 LLM 幻觉与人工效率限制影响
- 现有科研流程或方法的痛点：通用 LLM 缺少稳定事实核验
- 核心假设或直觉：让 LLM 自主调用领域数据库核验与修正，可提升生命科学解释可靠性

### 4.2 系统流程

1. 输入：gene set
2. 任务分解 / 规划：生成初始名称与解释
3. 工具、数据库、模型或实验平台调用：g:Profiler、Enrichr、E-utils 等 API
4. 中间结果反馈：self-verification 检查 claims
5. 决策或迭代：modification 修正输出
6. 输出：最终 gene-set explanation

### 4.3 系统组件

- Agent 核心：GeneAgent
- 工具 / API / 数据库：biological databases and enrichment APIs
- 记忆或状态模块：有
- 规划器：有
- 评估器 / verifier：self-verification module
- 人类反馈或专家介入：有限
- 实验平台或仿真环境：无

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

- 数据集 / 实验对象：1,106 gene sets + 7 melanoma novel gene sets
- 任务设置：gene-set naming and explanation
- 对比基线：standard GPT-4 / standard GSEA-style workflows
- 评价指标：ROUGE、语义相似度、claim verification
- 关键结果：`99.6%` claims 成功验证
- 是否有消融实验：有限
- 是否有失败案例或负结果：数据库覆盖度仍是限制

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：提供对新基因集的生物学解释
- 科学贡献是否经过验证：经数据库和 benchmark / expert-style evaluation 支持
- 贡献强度判断：中到强
- 科学贡献类型：解释 / 系统平台
- 证据强度：专家确认

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是直接预测模型，而是带数据库核验闭环的生命科学解释 Agent
- 与已有 Agent / 科研智能系统的区别：生命科学对象锚定非常稳定
- 与同一科学领域其他 Agent 文献的关系：是 `06 / 01.04` 边界上的清晰 `06` 样本
- 主要创新点：LLM explanation + domain database verification 的耦合

## 7. 局限性与风险

- Agent 自主性不足：仍受数据库覆盖度制约
- 科学验证不足：主要是解释可靠性而非新湿实验闭环
- 泛化性不足：对弱覆盖新功能仍可能受限
- 工具链依赖：强
- 数据泄漏或 benchmark 偏差：存在风险
- 成本、可复现性或安全风险：API 依赖明显

## 8. 对综述写作的价值

- 可放入哪个章节：06 生命科学
- 可支撑哪个论点：对象优先规则下，生命科学知识分析 Agent 不应因语言代理外观被并入 01.04
- 可用于哪个表格或图：bioinformatics / gene-set analysis agents
- 适合作为代表性案例吗：是
- 推荐引用强度：普通引用
- 需要在正文中特别引用的页码 / 图 / 表：Fig. 1；verification results
- 需要与哪些论文并列比较：其他 omics / knowledge-analysis agents

## 9. 总结

### 9.1 一句话概括

自验证语言 Agent 用生物数据库解释基因集功能。

### 9.2 速记版 pipeline

1. 输入基因集
2. 生成初始解释
3. 调数据库核验
4. 修正输出
5. 汇总最终解释

### 9.3 标注字段汇总

```text
是否纳入：是
科学对象模块：06
覆盖模式：single_module
是否具有具体科学对象实验：是
general_method_bucket：none
Primary module for filing：06
是否进入 01.04 存放区：否
主类：06
二级类：06.03
三级类：
四级专题：Gene-set analysis agents
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Retrieval-augmented Agent; Hybrid Agent
科研流程角色：knowledge_extraction_and_organization; tool_use_and_code_execution; data_analysis; result_interpretation; evidence_assessment_and_validation; end_to_end_research_automation
自主能力：task_decomposition; planning; tool_use; memory_or_state_tracking; feedback_iteration; autonomous_decision_making; environment_interaction
验证方式：benchmark; expert_evaluation
交叉属性：computation_driven; data_driven
科学贡献类型：explanation; system_platform
证据强度：expert_confirmed
归类置信度：高
纳入置信度：高
推荐引用强度：普通引用
```
