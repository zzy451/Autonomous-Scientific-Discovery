# Patel et al. 2025 - Machine Learning Copilot Agent: An LLM-Guided Workflow for Prognostic Gene Discovery

## 2026-07-05 Phase6NoteRevisionR25 harmonization

- Frozen landing decision: scientific_object_modules=06;07; object_coverage_mode=multi_module; primary_module_for_filing=07; general_method_bucket=none; source_limited=no.
- Current note-status rule: treat this record as already included / landed under the current authoritative pair; older to_read, pending, conservative-hold, or stale single-module / 01.04 shorthand below is superseded by this harmonization.
- Current PDF/source rule: the authoritative local archived PDF is Reference_PDF\06_Life_Sciences\Patel_2025_ML_Copilot_Prognostic_Gene_Discovery.pdf; older pending, abstract-only, no-local-PDF, or stale source_limited=yes wording below is superseded by this harmonization.
## Phase6FollowupR20 Frozen Adjudication

- `paper_id`: `ASD-0543`
- `final_adjudicated_modules`: `06;07`
- `primary_module_for_filing`: `07`
- `canonical_local_pdf`: `Reference_PDF/06_Life_Sciences/Patel_2025_ML_Copilot_Prognostic_Gene_Discovery.pdf`
- `frozen_source_state`: `source_limited=no`
- `first_hand_pdf_status`: local archived PDF sampled in `Phase6FollowupR20`
- `superseded_note_wording`: any older safety-supported, dataset-page-only, or `source_limited=yes` wording in this note is superseded by this frozen round update
- `adjudication_note`: preserve the stable `06;07` reading with `07` primary; this note remains filed under `06` for convenience only and the note path is not sole classification authority

**论文信息**
- 标题：Machine Learning Copilot Agent: An LLM-Guided Workflow for Prognostic Gene Discovery
- 作者：Patel et al.
- 年份：2025
- 来源 / venue：SSRN Electronic Journal
- DOI / arXiv / URL：https://doi.org/10.2139/ssrn.5343855
- PDF / 本地文件路径：当前未保存本地 PDF；SSRN / 论文落地页在本轮复核中未通过安全访问，因此本笔记不基于论文全文，而基于 Crossref DOI 元数据与官方作者数据集 / 项目页面
- 论文类型：预印本 / workflow paper
- 当前状态：to_read
- 阅读日期：2026-06-23
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | 标题；官方作者数据集 / repo / docs | 标题明确写出 `Copilot Agent` 与 `LLM-Guided Workflow`，官方配套资源也显示其为 workflow-oriented agent system | 中高 |
| `06` 生命科学对象 | 成立 | 官方 Hugging Face 数据集 `Project-Lambda-TCGA-HNSCC` 与 `Case-Study-HNSCC-ML-Copilot-Agent` | 数据集直接暴露 survival-associated genes、selected gene features 与 prognostic gene discovery framing | 中高 |
| `07` 医学对象 | 成立 | 官方 Hugging Face 数据集页面与字段 | 数据集中直接出现 HNSCC patient cohorts、overall survival、disease-specific survival、progression-free survival、clinical stage 等医学终点 | 中高 |
| 方法流程 | workflow / copilot framing 成立 | 标题；官方 docs / package / repo | 可确认这是面向 prognostic gene discovery 的 LLM-guided workflow，而不是静态单次模型输出 | 中 |
| 安全访问状态 | `blocked_paper_landing_used_official_dataset_pages` | 本轮复核记录 | 论文 landing / full article 未因安全原因继续访问，因此当前 landed judgment 不能伪装成全文支撑 | 高 |
| 来源级别 | `project_or_benchmark_page` 且 `source_limited` | 本轮复核结论 | 虽然已能 landed `06;07`，但证据仍来自官方数据集 / 项目资源，而非论文全文 | 高 |

## 0. 摘要翻译

本轮无法通过安全路径访问 SSRN 论文落地页或全文，因此这里不能假装已经完成 paper-level full text review。当前能确认的是：标题将该系统明确描述为 Machine Learning Copilot Agent 与 LLM-guided workflow；同时，作者公开的官方 Hugging Face 数据集与配套项目资源直接暴露了其研究对象与病例结构。数据集中不仅包含 survival-associated genes、feature selection 和 prognostic gene discovery 等生命科学侧对象，也包含 HNSCC patient cohorts、overall survival、disease-specific survival、progression-free survival、clinical stage 等明确医学终点。按当前 relaxed multi-module 规则，这足以把该文 landed 为 `06;07`，其中 primary filing 应转向 `07`；但因为论文落地页在本轮因安全原因未访问，当前仍应显式保留 safety-supported、source-limited 的说明。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：标题与官方配套资源共同表明其为 LLM-guided workflow / copilot agent，而非静态单模型论文
- 判定置信度：中高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：待论文全文安全可达后可补细节；当前 workflow framing 支持倾向性判断
  - 工具调用：是，官方项目资源支持 workflow / package framing
  - 反馈迭代：待全文补强
  - 自主决策：待全文补强
  - 多 Agent 协作：未见明确证据
- 在科研流程中承担的明确角色：prognostic gene discovery workflow、特征选择、结果解释与病例级预后分析支持

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：当前证据下否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：当前无法全文级确认，但 workflow framing 已超过一次性预测表述
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：`06;07`
- 覆盖模式：多模块
- 是否具有具体科学对象实验、验证、benchmark task、case study 或结果报告：是
- 独立 `01.04` 存放区：none
- Primary module for filing：`07`
- Primary module for filing 说明：仅用于笔记落盘、排序和展示，不覆盖多模块事实；当前文件仍保留在旧 `06` 路径下，这不是最终分类权威。
- 主展示模块一级类：`07`
- 主展示模块二级类：`07.02/07.03/07.04` 边界中的医学预后任务
- 主展示模块三级类：HNSCC prognosis / prognostic biomarker-oriented workflow
- 主展示模块四级专题：LLM-guided prognostic gene discovery
- 其他覆盖模块及对应层级路径：`06 -> 06.03 -> gene-feature / prognostic gene discovery`
- 四级专题是否为新增：否
- 是否进入独立 `01.04` 存放区：否
- 每个模块的对象实验证据：
  - `06`：官方数据集直接出现 prognostic gene discovery、survival-associated genes、selected gene features 等基因层与生物信息分析对象
  - `07`：官方数据集直接出现 HNSCC patient cohorts、overall survival、disease-specific survival、progression-free survival、clinical stage、ICD-coded disease fields 等疾病 / 患者 / 预后终点对象
- 归类理由：生命科学侧与医学侧都有独立、对象层的官方资源证据，且不再只是标题猜测
- 归类置信度：中高
- `first_hand_sources_checked`：Crossref DOI metadata and deposited reference list `10.2139/ssrn.5343855`; official author Hugging Face datasets `Project-Lambda-TCGA-HNSCC` and `Case-Study-HNSCC-ML-Copilot-Agent`; official PyPI package; official GitHub repo; official docs
- `classification_evidence_source_level`：`project_or_benchmark_page`
- `note_revision_required`：`yes`
- `source_limited`：`yes`
- `safety_access_status`：`blocked_paper_landing_used_official_dataset_pages`

### 2.2 对象优先判定

- 最终科学研究对象：prognostic genes、HNSCC patient cohorts 与 survival-related medical endpoints
- 最终科学问题：如何通过 LLM-guided workflow 发现与疾病预后相关的基因特征，并在患者级生存终点上形成可用分析
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：LLM-guided workflow 只是方法层；真正被官方资源直接暴露并支撑的是基因对象与疾病预后对象

### 2.3 容易混淆的边界

- 可能误归类到：`06` only、`07` only、`01.04`
- 最终判定：`06;07`，primary `07`
- 判定理由：标题与基因特征支持 `06`，HNSCC 生存终点与患者队列支持 `07`；两侧证据现在都已达到可 landed 水平
- 多模块覆盖说明：`06` 来自 gene-level / prognostic-feature discovery，`07` 来自疾病与患者生存终点；它们是对象层覆盖，不是标签层扩张
- 01.04 判定说明：即便论文落地页未安全访问，官方数据集已提供具体生命 / 医学对象证据，因此不能把它退回通用方法桶
- 是否需要二次复核：需要，但性质已改变。当前不是“必须先 hold 才安全”，而是“已可 landed，但未来若出现安全可达的官方论文页面，仍建议补做全文复核以加固细节”

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：待全文补强
- Tool-using Agent：是
- Retrieval-augmented Agent：待全文补强
- Multi-Agent System：未见明确证据
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：待全文补强
- Hybrid Agent：是
- 其他：copilot workflow agent

### 3.2 科研流程角色

- 文献检索与阅读：待全文补强
- 知识抽取与组织：是
- 科学问题提出：待全文补强
- 假设生成：部分是
- 实验设计：否
- 仿真建模：否
- 工具调用与代码执行：是
- 实验执行：否
- 数据分析：是
- 结果解释：是
- 证据评估与验证：部分是
- 论文写作：否
- 端到端科研流程自动化：部分是

### 3.3 自主能力

- 任务分解：待全文补强
- 计划生成：待全文补强
- 工具调用：是
- 记忆与状态维护：待全文补强
- 反馈迭代：待全文补强
- 自主决策：待全文补强
- 多 Agent 协作：未见明确证据
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
- 知识图谱：待全文补强
- 数字孪生：否
- 机器人平台：否
- 其他：clinical prognosis pressure

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：将 prognostic gene discovery workflow 进行 LLM-guided / copilot 化
- 现有科研流程或方法的痛点：人工完成基因预后发现与病例分层分析效率较低
- 核心假设或直觉：workflow-oriented copilot 能提升预后相关基因发现与病例级分析效率

### 4.2 系统流程

1. 输入：prognostic gene discovery task
2. 任务分解 / 规划：论文全文未安全访问，细节待补；当前可确认其为 workflow framing
3. 工具、数据库、模型或实验平台调用：官方 package / repo / dataset 资源支持其存在工具化执行链
4. 中间结果反馈：待全文补强
5. 决策或迭代：待全文补强
6. 输出：survival-associated genes、selected gene features 与面向 HNSCC 预后的分析结果

### 4.3 系统组件

- Agent 核心：Machine Learning Copilot Agent
- 工具 / API / 数据库：官方 Hugging Face datasets、官方 package / repo / docs
- 记忆或状态模块：待全文补强
- 规划器：待全文补强
- 评估器 / verifier：官方 case-study 数据集中的 survival / prognosis outputs
- 人类反馈或专家介入：待全文补强
- 实验平台或仿真环境：非仿真型，以组学 / 患者数据分析为主

## 5. 实验与验证

### 5.1 验证方式

- benchmark：待全文补强
- 仿真验证：否
- 高通量计算：待全文补强
- 机器人实验：否
- 湿实验：否
- 临床数据：是
- 真实场景部署：否
- 专家评估：待全文补强

### 5.2 数据、任务与指标

- 数据集 / 实验对象：HNSCC patient cohorts；survival-associated genes；selected prognostic features
- 任务设置：LLM-guided prognostic gene discovery workflow
- 对比基线：论文全文未安全访问，当前不作过度推断
- 评价指标：当前以 survival endpoints 与病例字段为对象层证据，不扩写未核实指标
- 关键结果：官方数据集已暴露基因特征输出与患者生存终点字段，足以支撑 `06;07`
- 是否有消融实验：待全文补强
- 是否有失败案例或负结果：待全文补强

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：更偏 gene discovery / prognosis-oriented system 平台贡献
- 科学贡献是否经过验证：是，但当前验证证据来自官方数据集 / 项目资源，而非论文全文
- 贡献强度判断：中
- 科学贡献类型：系统平台 / 基因发现 / 预测
- 证据强度：临床数据

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是静态模型论文，标题与官方资源都显示其为 agentic / workflow-oriented copilot
- 与已有 Agent / 科研智能系统的区别：聚焦 prognostic gene discovery 与患者预后端点，而非一般生信分析助手
- 与同一科学领域其他 Agent 文献的关系：可与 biomarker discovery、PromptBio、免疫治疗预后相关工作形成 `06/07` 边界比较
- 主要创新点：把基因预后发现与 HNSCC 生存分析放入同一 LLM-guided workflow 框架

## 7. 局限性与风险

- Agent 自主性不足：论文全文未安全访问，自治细节仍不足
- 科学验证不足：当前不能宣称已复核全文实验设计与完整指标
- 泛化性不足：已确认对象主要落在 HNSCC / prognosis 场景
- 工具链依赖：依赖官方项目与数据资源
- 数据泄漏或 benchmark 偏差：需要安全可达的论文或补充材料进一步复核
- 成本、可复现性或安全风险：当前最大的风险不是分类本身，而是 paper landing 安全受限导致的 source-limited 状态

## 8. 对综述写作的价值

- 可放入哪个章节：07 医学与健康科学，并在 `06/07` 边界讨论中提及
- 可支撑哪个论点：即便论文全文因安全原因不可达，官方数据集页面仍可能足以支撑 object-first landed judgment
- 可用于哪个表格或图：source-limited but landed `06;07` boundary cases
- 适合作为代表性案例吗：谨慎适合；正文应注明其为 safety-supported landing
- 推荐引用强度：普通引用
- 需要在正文中特别引用的页码 / 图 / 表：当前无法提供论文页码；若未来出现安全可达的官方 paper route，建议补全文位置
- 需要与哪些论文并列比较：ASD-0541、ASD-0545、ASD-0544

## 9. 总结

### 9.1 一句话概括

这是一个基于官方数据集而非论文全文落地的 `06;07` safety-supported landing。

### 9.2 速记版 pipeline

1. 设定预后基因发现任务
2. 以 LLM-guided workflow 推进分析
3. 输出候选基因与特征
4. 关联 HNSCC 生存终点
5. 形成预后分析结果

### 9.3 标注字段汇总

```text
是否纳入：included
科学对象模块：06;07
覆盖模式：multi_module
是否具有具体科学对象实验：yes
general_method_bucket：none
Primary module for filing：07
是否进入 01.04 存放区：no
主展示模块一级类：07
主展示模块二级类：07.02/07.03/07.04 boundary
主展示模块三级类：HNSCC prognosis / prognostic biomarker-oriented workflow
主展示模块四级专题：LLM-guided prognostic gene discovery
其他覆盖模块及对应层级路径：06 -> 06.03 -> gene-feature / prognostic gene discovery
module_assignment_evidence：prognostic gene discovery、survival-associated genes 与 selected gene features 支持 06；HNSCC cohorts、overall survival、disease-specific survival、progression-free survival、clinical stage 等支持 07
multi_module_object_coverage_note：当前 landed judgment 由官方作者数据集 / 项目页面支撑，而非论文全文；属于 safety-supported landing
Agent 类型：LLM Agent; Tool-using Agent; Hybrid Agent
科研流程角色：knowledge_extraction_and_organization; hypothesis_generation; tool_use_and_code_execution; data_analysis; result_interpretation; evidence_assessment_and_validation; end_to_end_research_automation
自主能力：tool_use; environment_interaction
验证方式：clinical_data
交叉属性：computation_driven; data_driven
科学贡献类型：system_platform; prediction; knowledge_discovery
证据强度：computationally_validated
归类置信度：medium_high
纳入置信度：medium_high
推荐引用强度：standard
```
