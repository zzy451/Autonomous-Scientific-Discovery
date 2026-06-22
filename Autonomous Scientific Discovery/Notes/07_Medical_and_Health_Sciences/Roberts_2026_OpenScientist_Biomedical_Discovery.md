# Roberts et al. 2026 - OpenScientist: evaluating an open agentic AI co-scientist to accelerate biomedical discovery

**论文信息**
- 标题：OpenScientist: evaluating an open agentic AI co-scientist to accelerate biomedical discovery
- 作者：Roberts et al.
- 年份：2026
- 来源 / venue：medRxiv / PMC mirror
- DOI / arXiv / URL：https://doi.org/10.64898/2026.03.15.26348338
- PDF / 本地文件路径：PMC 全文 https://pmc.ncbi.nlm.nih.gov/articles/PMC13015679/
- 论文类型：preprint / system paper
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

## 2026-06-22 Batch16 full-reaudit check

- Final adjudication: `supported_modules=06;07`; `final_01_04_bucket=none`; `primary_module_for_filing=07`; `confidence=medium-high`; `source_limited=no`; `safety_access_status=no_safety_skip`.
- First-hand source checked for this refresh: PMC full text `https://pmc.ncbi.nlm.nih.gov/articles/PMC13015679/`.
- Current evidence wording: biomedical case studies anchor `07`, while omics/cellular/proteomics analyses independently support `06`.
- Note-location reminder: this note remains filed under `Notes/07_Medical_and_Health_Sciences/` for filing convenience because `07` is the adjudicated primary filing; the note path is not independent classification authority.

## 2026-06-20 relaxed multi-module revision

This section preserves the earlier full-text evidence trail and is now aligned to the final landed adjudication rather than the older single-filing read.

```text
scientific_object_modules: 06;07
object_coverage_mode: multi_module
has_concrete_object_experiments: yes
general_method_bucket: none
primary_module_for_filing: 07
first_hand_sources_checked: PMC full text `https://pmc.ncbi.nlm.nih.gov/articles/PMC13015679/`
classification_evidence_source_level: first_hand_full_text
module_assignment_evidence: `07` is supported by Alzheimer biomarkers, plasma-proteomics survival prediction, multiple-myeloma cohorts, and clinical/disease discovery cases; `06` is supported by single-cell transcriptomics, proteomics, and biological mechanism analyses.
multi_module_object_coverage_note: OpenScientist is not a `01.04`-only general co-scientist under the relaxed rule. Its landed note wording should retain exactly `06;07`, with `07` only as the primary filing module.
authoritative_note_refresh_status: the `2026-06-22 Batch16 full-reaudit check` block above is the controlling adjudication for note writeback.
```

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | Abstract; Fig. 1 | 具备文献检索、代码执行、知识状态维护、反馈迭代和多轮发现流程 | 高 |
| 科学对象归类 | `07.04` | Abstract; Introduction; case studies | 4 个核心案例都落在疾病、生物标志物、临床相关人类数据 | 高 |
| 方法流程 | 明确闭环 | Fig. 1; methods | query -> 检索 -> 代码分析 -> KSDS 更新 -> 下一轮迭代 -> final report | 高 |
| 实验验证 | 强于一般 benchmark | case studies; discussion | 有真实 biomedical case studies、外部 cohort 验证和专家评估 | 高 |
| 边界判断 | `07` 胜过 `01.04` | 全文整体 | 平台虽通用，但验证与贡献稳定锚定医学健康对象 | 高 |

## 0. 摘要翻译

OpenScientist 是一个开源 agentic AI 协同科学家，目标是在生物医学发现中半自主地调查研究者提出的问题，并输出可验证、与临床相关的科学洞见。作者用四个真实案例评估其能力，包括 Alzheimer 生物标志物、血浆蛋白组生存预测、神经纤维缠结单细胞转录组，以及多发性骨髓瘤假设生成与外部验证。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：有明确科研目标、多轮调查流程、文献检索、代码执行、知识状态维护与反馈迭代
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：部分
- 在科研流程中承担的明确角色：文献检索、假设生成、数据分析、证据评估、结果解释

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
- 四级专题：Open agentic AI co-scientists for biomedical discovery
- 四级专题是否为新增：否
- 归类理由：全部核心案例面向疾病、生物标志物、临床/人类数据与 biomedical discovery
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：biomedical and clinically relevant discovery tasks
- 最终科学问题：如何用 agentic AI co-scientist 生成和验证临床相关生物医学洞见
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：尽管平台外观通用，但系统验证和贡献稳定落在医学健康对象

### 2.3 容易混淆的边界

- 可能误归类到：01.04
- 最终判定：保持 07.04
- 判定理由：按项目规则，只要科学贡献稳定面向具体医学健康对象，就不能回退到通用科研 Agent
- 是否需要二次复核：否

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：是
- Multi-Agent System：部分
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：是
- Hybrid Agent：是
- 其他：co-scientist

### 3.2 科研流程角色

- 文献检索与阅读：是
- 知识抽取与组织：是
- 科学问题提出：部分
- 假设生成：是
- 实验设计：否
- 仿真建模：否
- 工具调用与代码执行：是
- 实验执行：否
- 数据分析：是
- 结果解释：是
- 证据评估与验证：是
- 论文写作：部分
- 端到端科研流程自动化：是

### 3.3 自主能力

- 任务分解：是
- 计划生成：是
- 工具调用：是
- 记忆与状态维护：是
- 反馈迭代：是
- 自主决策：是
- 多 Agent 协作：部分
- 环境交互：是
- 闭环实验：否

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 实验驱动：否
- 仿真驱动：否
- 多模态：是
- 多尺度建模：否
- 高通量筛选：否
- 知识图谱：否
- 数字孪生：否
- 机器人平台：否
- 其他：human biomedical datasets

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：降低 biomedical discovery 中文献检索、数据分析与假设生成的人工负担
- 现有科研流程或方法的痛点：多源生物医学数据复杂、分析链长、结果可验证性不足
- 核心假设或直觉：agentic workflow + code execution + knowledge state 能把 LLM 变成可用的 biomedical co-scientist

### 4.2 系统流程

1. 输入：scientist query 与数据文件
2. 任务分解 / 规划：系统建立调查计划并决定下一轮动作
3. 工具、数据库、模型或实验平台调用：PubMed、代码环境、外部数据分析工具
4. 中间结果反馈：KSDS 记录 findings、hypotheses、plots
5. 决策或迭代：进入下一轮分析，默认最多 10 轮
6. 输出：final report 与可验证洞见

### 4.3 系统组件

- Agent 核心：OpenScientist 主体
- 工具 / API / 数据库：PubMed、Python sandbox、外部数据分析工具
- 记忆或状态模块：KSDS
- 规划器：有
- 评估器 / verifier：有
- 人类反馈或专家介入：可选 co-investigator 模式
- 实验平台或仿真环境：无物理实验平台

## 5. 实验与验证

### 5.1 验证方式

- benchmark：有
- 仿真验证：否
- 高通量计算：否
- 机器人实验：否
- 湿实验：否
- 临床数据：是
- 真实场景部署：否
- 专家评估：是

### 5.2 数据、任务与指标

- 数据集 / 实验对象：Alzheimer biomarkers、plasma proteomics、single-cell transcriptomics、multiple myeloma cohorts
- 任务设置：从问题提出到文献、代码、数据分析和洞见生成的多轮发现流程
- 对比基线：标准 GPT-4、已发表模型与外部队列
- 评价指标：预测性能、外部验证、可解释性与专家判断
- 关键结果：识别 `%ptau217`；重建生存模型；提出 tau pathology 机制；提出并外部验证多发性骨髓瘤假设
- 是否有消融实验：有限
- 是否有失败案例或负结果：作者承认会漏检关键文献、叙事可能过度自信

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：有新假设与机制性洞见
- 科学贡献是否经过验证：有外部 cohort 和专家层面的支持
- 贡献强度判断：强
- 科学贡献类型：假设 / 数据分析 / 系统平台
- 证据强度：计算验证

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单模型，而是完整的 agentic discovery workflow
- 与已有 Agent / 科研智能系统的区别：验证对象稳定落在真实 biomedical discovery 场景
- 与同一科学领域其他 Agent 文献的关系：是 `07 / 01.04` 边界上的强锚点样本
- 主要创新点：把多轮检索、代码执行、知识状态与 biomedical case studies 融合成可验证 co-scientist 工作流

## 7. 局限性与风险

- Agent 自主性不足：仍需人类监督
- 科学验证不足：比一般 benchmark 强，但仍以计算与数据分析为主
- 泛化性不足：跨更多疾病场景还需验证
- 工具链依赖：强
- 数据泄漏或 benchmark 偏差：存在潜在风险
- 成本、可复现性或安全风险：临床相关叙事需要谨慎审查

## 8. 对综述写作的价值

- 可放入哪个章节：07 医学与健康科学
- 可支撑哪个论点：即使平台外观通用，只要核心验证落在医学对象上，就应归入 07
- 可用于哪个表格或图：biomedical co-scientist 代表案例表
- 适合作为代表性案例吗：是
- 推荐引用强度：核心引用
- 需要在正文中特别引用的页码 / 图 / 表：Fig. 1；四个 case studies
- 需要与哪些论文并列比较：其他 `07 / 01.04` 边界样本

## 9. 总结

### 9.1 一句话概括

开源 biomedical co-scientist 在真实案例中完成多轮发现流程。

### 9.2 速记版 pipeline

1. 接收研究问题与数据
2. 检索文献并执行代码
3. 保存知识状态并迭代
4. 生成假设与分析结果
5. 输出 final report

### 9.3 标注字段汇总

```text
是否纳入：是
主类：07
二级类：07.04
三级类：
四级专题：Open agentic AI co-scientists for biomedical discovery
Agent 类型：LLM Agent; Tool-using Agent; Retrieval-augmented Agent; Hybrid Agent
科研流程角色：literature_search_and_reading; knowledge_extraction_and_organization; hypothesis_generation; tool_use_and_code_execution; data_analysis; result_interpretation; evidence_assessment_and_validation; end_to_end_research_automation
自主能力：task_decomposition; planning; tool_use; memory_or_state_tracking; feedback_iteration; autonomous_decision_making; environment_interaction
验证方式：benchmark; clinical_data; expert_evaluation
交叉属性：computation_driven; data_driven; multimodal
科学贡献类型：hypothesis; system_platform
证据强度：computationally_validated
归类置信度：高
纳入置信度：高
推荐引用强度：核心引用
```
