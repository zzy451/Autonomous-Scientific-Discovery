# Qu et al. 2025 - Automating Exploratory Multiomics Research via Language Models

**论文信息**
- 标题：Automating Exploratory Multiomics Research via Language Models
- 作者：Shang Qu et al.
- 年份：2025
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2506.07591
- PDF / 本地文件路径：`Reference_PDF/06_Life_Sciences/Qu_2025_PROTEUS_Multiomics.pdf`；本轮已核对 arXiv PDF `https://arxiv.org/pdf/2506.07591.pdf`
- 论文类型：研究论文 / multiomics research agent
- 当前状态：to_read / confirmed core
- 阅读日期：2026-06-22
- 笔记作者：Codex（Writeback-Agent-3）

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | p.1-2 Abstract | `PROTEUS` 从 raw multiomics data 自动生成 research objectives、analysis results 和 hypotheses。 | 高 |
| `06` 对象证据 | 明确支持 | p.2 Abstract | 论文核心围绕 biological entities relationships、multiomics analysis 和 hypothesis generation。 | 高 |
| `07` 对象证据 | 明确支持 | p.2, p.3, p.8 | 数据来自 10 个 clinical multiomics datasets；外部验证使用 same cancer types 的 CPTAC cohorts；结果多次涉及 survival / prognosis。 | 高 |
| 实验验证 | 10 数据集、360 条假设 | p.2 Abstract | 在 10 个 multiomics datasets 上自动提出 360 hypotheses，并做外部数据验证与自动 open-ended scoring。 | 高 |
| 边界裁决 | `06;07` | p.2-3, p.8 | 生命科学对象来自 multiomics 分子关系；医学健康对象来自 cancer cohorts、survival、prognosis 与临床变量分析。 | 高 |

## 0. 摘要翻译

本文提出 `PROTEUS` 在多组学场景下的扩展版本，用于从原始 multiomics 数据中自动开展探索式研究并提出新假设。系统将 biological entities 之间的关系组织为统一图结构，围绕研究方向选择、统计分析、假设生成与验证形成迭代式自动研究流程。论文在 10 个来自既有发表工作的临床多组学数据集上运行系统，共提出 360 条假设，并通过同癌种的 CPTAC 外部队列和自动 open-ended scoring 进行评估。最终分类不能只保留旧的 `06` 主体说法：分子组学与 biological relationship discovery 明确支持 `06`，而 cancer cohorts、survival / prognosis 与 clinical feature validation 明确支持 `07`。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：系统具备任务组织、工具调用、迭代分析与自主假设生成的多步科研流程。
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：未突出
- 在科研流程中承担的明确角色：组学数据探索、统计分析、结果整合、假设生成、外部验证

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 科学对象模块归类

- scientific_object_modules：`06;07`
- object_coverage_mode：`multi_module`
- has_concrete_object_experiments：`yes`
- general_method_bucket：`none`
- primary_module_for_filing：`06`
- note 所在目录说明：当前文件位于 `Notes/06_Life_Sciences/`，这是主展示/归档位置；权威分类事实仍是 `06;07`。
- 每个模块的对象实验证据：
  - `06`：multiomics biological entities relationships、transcript / protein / pathway 层分析与 hypothesis generation
  - `07`：clinical multiomics cancer cohorts、CPTAC same-cancer validation、survival / prognosis / clinic subtype 分析
- 归类理由：论文既研究生命科学中的 multiomics 分子关系，也做了明确的 cancer cohort 与临床变量验证，因此本轮接受 `06;07`
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：clinical multiomics datasets 中的 biological entities relationships，以及与 cancer cohorts 相关的 survival / prognosis / subtype 对象
- 最终科学问题：如何用 Agent 在复杂临床多组学数据中自动提出并验证高质量假设
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：平台外观不是分类依据；模块由实际对象覆盖决定

### 2.3 容易混淆的边界

- 可能误归类到：仅 `06`
- 最终判定：`06;07`
- 判定理由：如果只看组学主体容易保留 `06`，但同癌种 CPTAC 验证、survival / prognosis 和 clinical subtype 任务已足够独立支持 `07`
- 多模块覆盖说明：`06` 来自 multiomics 分子对象；`07` 来自临床癌症队列和临床结局变量
- 01.04 判定说明：论文有充分 concrete object evidence，不属于 `01.04`
- 是否需要二次复核：否，本轮 arXiv PDF 已足以闭合 `06/07` 边界

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：未明确
- Multi-Agent System：未强调
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：否
- Hybrid Agent：是

### 3.2 科研流程角色

- 知识抽取与组织：是
- 假设生成：是
- 工具调用与代码执行：是
- 数据分析：是
- 结果解释：是
- 证据评估与验证：是
- 端到端科研流程自动化：是

### 3.3 自主能力

- 任务分解：是
- 计划生成：是
- 工具调用：是
- 反馈迭代：是
- 自主决策：是
- 环境交互：是

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：临床多组学研究高维、异质、探索空间大，人工开展 open-ended research 负担高
- 现有科研流程或方法的痛点：很难把多组学探索、统计分析和假设验证统一成自动流程
- 核心假设或直觉：把多组学研究中的 biological relationships 组织成统一图结构，可以支持自动化探索研究

### 4.2 系统流程

1. 输入：raw multiomics data files
2. 任务分解 / 规划：选择研究方向和关系类型
3. 工具、数据库、模型或实验平台调用：执行统计分析并组织实体关系图
4. 中间结果反馈：根据分析结果修正研究方向
5. 决策或迭代：生成并筛选 hypotheses
6. 输出：data-driven multiomics hypotheses

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 计算验证：是
- 临床数据：是
- 专家评估：部分是

### 5.2 数据、任务与指标

- 数据集 / 实验对象：10 个已发表的 clinical multiomics datasets
- 任务设置：exploratory multiomics analysis + hypothesis proposal
- 评价指标：外部 cohort validation + automatic open-ended scoring
- 关键结果：360 条 fully automatically proposed hypotheses

### 5.3 科学贡献

- 是否发现新知识、新机制、新假设或新实验结果：主要是多组学假设生成与外部验证
- 科学贡献是否经过验证：是，包含 same-cancer external cohorts validation
- 贡献强度判断：中到强
- 科学贡献类型：`hypothesis`; `system_platform`
- 证据强度：`computationally_validated`

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单一预测器，而是 multiomics exploratory research agent
- 与已有 Agent / 科研智能系统的区别：从 raw data 直接推进到 hypothesis generation，并带有临床 cohort external validation
- 与同一科学领域其他 Agent 文献的关系：是 `06/07` 边界下的代表性多组学案例

## 7. 局限性与风险

- 科学验证不足：没有湿实验或真实临床部署
- 泛化性不足：当前主要集中在 clinical multiomics cancer datasets
- 工具链依赖：依赖统计分析模块与图结构研究流程
- 成本、可复现性或安全风险：自动 open-ended scoring 仍可能受模型版本影响

## 8. 对综述写作的价值

- 可放入哪个章节：`06` 生命科学主展示章节，并在 `06/07` 边界中讨论
- 可支撑哪个论点：多组学 Agent 一旦包含癌症队列、survival 与 prognosis 验证，就可同时进入 `07`
- 适合作为代表性案例吗：适合
- 推荐引用强度：`standard`
- 是否还需要进一步全文复核：不需要；本轮 arXiv PDF 已足以支撑最终裁决

## 9. 总结

### 9.1 一句话概括

PROTEUS 自动开展临床多组学探索并生成可验证假设。

### 9.2 速记版 pipeline

1. 读取多组学数据
2. 组织 biological relationship 图结构
3. 执行统计分析
4. 生成并筛选 hypotheses
5. 用外部 cohort 验证

### 9.3 标注字段汇总

```text
是否纳入：是
scientific_object_modules：06;07
object_coverage_mode：multi_module
has_concrete_object_experiments：yes
general_method_bucket：none
primary_module_for_filing：06
module_assignment_evidence：10 个 clinical multiomics datasets；360 hypotheses；same-cancer CPTAC validation；survival / prognosis / subtype 分析
multi_module_object_coverage_note：multiomics 分子对象支撑 06；clinical cancer cohort 与结局变量支撑 07
first_hand_sources_checked：arXiv PDF https://arxiv.org/pdf/2506.07591.pdf
classification_evidence_source_level：first_hand_full_text
note_revision_required：yes
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Hybrid Agent
科研流程角色：knowledge_extraction_and_organization; hypothesis_generation; tool_use_and_code_execution; data_analysis; result_interpretation; evidence_assessment_and_validation; end_to_end_research_automation
自主能力：task_decomposition; planning; tool_use; feedback_iteration; autonomous_decision_making; environment_interaction
验证方式：benchmark; computational_validation; clinical_data
交叉属性：computation_driven; data_driven; knowledge_graph
科学贡献类型：hypothesis; system_platform
证据强度：computationally_validated
归类置信度：高
纳入置信度：高
推荐引用强度：standard
```
