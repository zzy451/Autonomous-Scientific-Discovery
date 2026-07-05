# Park and Lee 2025 - IMMUNIA: A Multi-LLM Reasoning Agent for Immunoregulatory Surfaceome Discovery

## 2026-07-05 Phase6NoteRevisionR25 harmonization

- Frozen landing decision: scientific_object_modules=06;07; object_coverage_mode=multi_module; primary_module_for_filing=07; general_method_bucket=none; source_limited=no.
- Current note-status rule: treat this record as already included / landed under the current authoritative pair; older to_read, pending, conservative-hold, or stale single-module / 01.04 shorthand below is superseded by this harmonization.
- Current PDF/source rule: the authoritative local archived PDF is Reference_PDF\07_Medical_and_Health_Sciences\Park_2025_IMMUNIA_Surfaceome_Discovery.pdf; older pending, abstract-only, no-local-PDF, or stale source_limited=yes wording below is superseded by this harmonization.
## Phase6FollowupR20 Frozen Adjudication

- `paper_id`: `ASD-0545`
- `final_adjudicated_modules`: `06;07`
- `primary_module_for_filing`: `07`
- `canonical_local_pdf`: `Reference_PDF/07_Medical_and_Health_Sciences/Park_2025_IMMUNIA_Surfaceome_Discovery.pdf`
- `frozen_source_state`: `source_limited=no`
- `first_hand_pdf_status`: local archived PDF sampled in `Phase6FollowupR20`
- `superseded_note_wording`: any older safety-supported abstract-only or `source_limited=yes` wording in this note is superseded by this frozen round update
- `adjudication_note`: preserve the stable `06;07` reading with `07` primary while retiring the earlier safe-abstract-only access framing

**论文信息**
- 标题：IMMUNIA: A Multi-LLM Reasoning Agent for Immunoregulatory Surfaceome Discovery
- 作者：Park and Lee
- 年份：2025
- 来源 / venue：bioRxiv
- DOI / arXiv / URL：https://doi.org/10.1101/2025.11.02.686138
- PDF / 本地文件路径：当前未保存本地 PDF；本轮基于 Crossref 返回摘要
- 论文类型：研究论文 / reasoning-centric biomarker-discovery agent
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

## 2026-06-23 safety-supported full-reaudit sync

- Final adjudication for this round: `supported_modules=06;07`; `final_01_04_bucket=none`; `primary_module_for_filing=07`; `confidence=medium`; `source_limited=yes`; `safety_access_status=safety_supported_non_safe_http_doi_redirect`.
- `first_hand_sources_checked`: safe Sciety article page with abstract for DOI `10.1101/2025.11.02.686138`; direct DOI recheck confirmed redirect to non-safe `http` bioRxiv and was not followed further.
- Current evidence wording: the safe abstract directly supports both the `07` precision-immunotherapy biomarker-discovery layer and the `06` immune-biology / surfaceome-gene layer; no unsafe full-article access was pursued.
- Safety-supported note: this is not a no-safety full-text landing. The current closeout depends on the safe abstract plus explicit refusal to continue through the non-safe DOI redirect.
- Note-path reminder: this note remains under `Notes/07_Medical_and_Health_Sciences/` because `07` is the adjudicated primary filing module; the note path is not independent classification authority.

## 2026-06-20 relaxed multi-module revision

This section supplements the older `07.01` primary filing with object-coverage modules.

```text
scientific_object_modules: 06;07
object_coverage_mode: multi_module
has_concrete_object_experiments: yes
general_method_bucket: none
primary_module_for_filing: 07
first_hand_sources_checked: bioRxiv/Sciety abstract; LifeScience preprint page
classification_evidence_source_level: first_hand_abstract_or_landing_page
module_assignment_evidence: `07` is supported by precision immunotherapy biomarker discovery; `06` is supported by immunoregulatory surfaceome genes, tumor-immune crosstalk, and immune-biology candidate-gene reasoning.
multi_module_object_coverage_note: The translational/immunotherapy endpoint remains primary, but the gene/surfaceome/immune-biology evidence supports `06` under the relaxed rule.
```

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | Crossref abstract | IMMUNIA 是 multi-LLM reasoning agent，整合 structured prompting、contextual scoring 和 consensus reasoning | 高 |
| 科学对象归类 | `07.01` | Crossref abstract | 论文目标是 immunotherapy biomarker discovery、tumor-immune crosstalk 和 stromal immune checkpoint-like regulators | 高 |
| 方法流程 | 多步推理与 consensus | Crossref abstract | 通过 GPT-4o、GPT-5、Gemini 2.5 Pro 做共识推理，并以 positive/negative controls 检验判别 | 高 |
| 验证方式 | benchmark / controls + biological plausibility | Crossref abstract | 使用 HLA 和 contactin controls，并优先筛出若干 high-confidence candidate genes | 中高 |
| 边界判断 | `07` 优先于 `06` | Crossref abstract | 论文直接服务 precision immunotherapy biomarker discovery，而不是一般生命科学机制探索 | 高 |

## 0. 摘要翻译

论文指出，免疫治疗相关 biomarker discovery 往往需要跨越复杂免疫语境进行推理。作者提出 IMMUNIA，这是一个 multi-LLM reasoning agent，用于通过可解释、具生物学基础的分析来识别 immunoregulatory surfaceome genes。系统整合了 structured prompting、围绕 immunotherapy、inflammation 和 NF-kB signaling 的 contextual scoring，以及 GPT-4o、GPT-5 和 Gemini 2.5 Pro 之间的 consensus reasoning。通过正控制（HLA）和负控制（contactin）进行 benchmark，作者验证了模型的一致性和情境区分能力。系统筛出了 IL1R1、BSG、CD276、ALCAM、B2M、PTPRS、VCAN 和 MXRA5 等高置信候选，其中 PTPRS、VCAN 和 MXRA5 被描述为此前未充分识别的 stromal immune checkpoint-like regulators。整体上，这是一项面向 precision immunotherapy biomarker discovery 的医学研究 Agent。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：具有多模型共识推理、候选优选、控制校验和结果解释的多步流程
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：是
- 在科研流程中承担的明确角色：biomarker candidate prioritization、immune-context reasoning、结果解释

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：07
- 二级类：07.01
- 三级类：immunotherapy biomarker discovery
- 四级专题：surfaceome reasoning agents
- 四级专题是否为新增：否
- 归类理由：最终对象是免疫治疗相关 biomarker 与 tumor-immune crosstalk 调控因子，而不是一般免疫生物学机制
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：immunoregulatory surfaceome genes 与 immunotherapy biomarkers
- 最终科学问题：如何用 reasoning-centric AI 识别具有临床相关性的免疫治疗 biomarker 候选
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：multi-LLM consensus 是方法，稳定对象仍是医学导向的 biomarker discovery

### 2.3 容易混淆的边界

- 可能误归类到：06.02 / 06.03
- 最终判定：改入 07.01
- 判定理由：尽管使用免疫与表面组学语言，但最终目标是 precision immunotherapy biomarker discovery，而不是一般生命机制研究
- 是否需要二次复核：是，后续可补全文确认临床转化深度

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：未明确
- Multi-Agent System：是
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：未明确
- Hybrid Agent：是
- 其他：multi-LLM consensus reasoning agent

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
- 端到端科研流程自动化：部分是

### 3.3 自主能力

- 任务分解：是
- 计划生成：是
- 工具调用：是
- 记忆与状态维护：未明确
- 反馈迭代：是
- 自主决策：是
- 多 Agent 协作：是
- 环境交互：否
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
- 其他：precision immunotherapy

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：免疫治疗 biomarker discovery 需要跨复杂免疫语境做可解释推理
- 现有科研流程或方法的痛点：单模型或单视角分析难以兼顾生物学合理性与上下文一致性
- 核心假设或直觉：多 LLM 共识推理可帮助识别更可信的 immunoregulatory surfaceome candidates

### 4.2 系统流程

1. 输入：surfaceome / immune-context discovery task
2. 任务分解 / 规划：围绕 immunotherapy、inflammation、NF-kB signaling 建立上下文打分
3. 工具、数据库、模型或实验平台调用：GPT-4o、GPT-5、Gemini 2.5 Pro 做 consensus reasoning
4. 中间结果反馈：用 positive/negative controls 检验模型一致性与情境区分
5. 决策或迭代：优先排序高置信候选基因
6. 输出：precision immunotherapy biomarker candidates

### 4.3 系统组件

- Agent 核心：IMMUNIA
- 工具 / API / 数据库：structured prompting、contextual scoring、multi-LLM consensus
- 记忆或状态模块：未明确
- 规划器：reasoning and scoring workflow
- 评估器 / verifier：control-based benchmarking
- 人类反馈或专家介入：未展开
- 实验平台或仿真环境：无真实机器人实验

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：否
- 高通量计算：否
- 机器人实验：否
- 湿实验：否
- 临床数据：未明确
- 真实场景部署：否
- 专家评估：未明确

### 5.2 数据、任务与指标

- 数据集 / 实验对象：immunoregulatory surfaceome genes
- 任务设置：precision immunotherapy biomarker discovery
- 对比基线：positive / negative controls
- 评价指标：model consistency、contextual discrimination、candidate prioritization
- 关键结果：识别出多个 high-confidence candidate genes
- 是否有消融实验：摘要未展开
- 是否有失败案例或负结果：negative control 存在

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：是，提出新的 stromal immune checkpoint-like regulators 候选
- 科学贡献是否经过验证：有控制基准与生物学合理性层面的验证，但未见湿实验
- 贡献强度判断：中
- 科学贡献类型：hypothesis / biomarker_discovery
- 证据强度：simulation_supported

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：强调多 LLM 共识推理而不是单步分类或单模型 ranking
- 与已有 Agent / 科研智能系统的区别：更聚焦免疫治疗 biomarker discovery
- 与同一科学领域其他 Agent 文献的关系：可与 cancer pathology、cancer biomarker discovery、drug discovery Agent 形成医学边界比较
- 主要创新点：把 reasoning-centric multi-LLM consensus 明确用于 surfaceome biomarker discovery

## 7. 局限性与风险

- Agent 自主性不足：缺少真实实验闭环
- 科学验证不足：目前主要是 computational / reasoning 层验证
- 泛化性不足：聚焦 immunoregulatory surfaceome
- 工具链依赖：依赖多 LLM 共识稳定性
- 数据泄漏或 benchmark 偏差：需全文复核 control 设计
- 成本、可复现性或安全风险：多模型调用成本较高

## 8. 对综述写作的价值

- 可放入哪个章节：07 医学与健康科学
- 可支撑哪个论点：医学侧 Agent 已可围绕 immunotherapy biomarker 做多步 reasoning-driven discovery
- 可用于哪个表格或图：medical biomarker-discovery agent cluster
- 适合作为代表性案例吗：适合作为边界型案例
- 推荐引用强度：standard
- 需要在正文中特别引用的页码 / 图 / 表：后续补 PDF
- 需要与哪些论文并列比较：SPARK、cancer biomarker discovery、Medea、PromptBio

## 9. 总结

### 9.1 一句话概括

IMMUNIA 用多 LLM 共识推理发现免疫治疗 biomarker 候选。

### 9.2 速记版 pipeline

1. 建立免疫语境评分
2. 多 LLM 共识推理
3. 用正负控制检验
4. 排序候选基因
5. 输出高置信 biomarker 候选

### 9.3 标注字段汇总

```text
是否纳入：to_read
主类：07
二级类：07.01
三级类：immunotherapy biomarker discovery
四级专题：surfaceome reasoning agents
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Multi-Agent System; Hybrid Agent
科研流程角色：knowledge_extraction_and_organization; scientific_question_formulation; hypothesis_generation; tool_use_and_code_execution; data_analysis; result_interpretation; evidence_assessment_and_validation
自主能力：task_decomposition; planning; tool_use; feedback_iteration; autonomous_decision_making; multi_agent_collaboration
验证方式：benchmark
交叉属性：computation_driven; data_driven
科学贡献类型：hypothesis; biomarker_discovery
证据强度：simulation_supported
归类置信度：高
纳入置信度：高
推荐引用强度：standard
```
