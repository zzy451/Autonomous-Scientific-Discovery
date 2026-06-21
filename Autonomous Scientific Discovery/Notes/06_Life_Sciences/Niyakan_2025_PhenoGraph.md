# Niyakan and Qian 2025 - PhenoGraph
## 2026-06-21 archive sync

- Canonical PDF path: `Reference_PDF/06_Life_Sciences/Niyakan_2025_PhenoGraph.pdf`
- Current-turn source refresh: the OpenReview full PDF was archived to the project `Reference_PDF/` directory on `2026-06-21`.
- Classification remains stable: `scientific_object_modules=06;07`; `object_coverage_mode=multi_module`; `primary_module_for_filing=06`; `general_method_bucket=none`.

**论文信息**
- 标题：PhenoGraph: A Multi-Agent Framework for Phenotype-driven Discovery in Spatial Transcriptomics Data Augmented with Knowledge Graphs
- 作者：Seyednami Niyakan, Xiaoning Qian
- 年份：2025
- 来源 / venue：Workshop on Generative AI for Biology at ICML 2025, PMLR 267；bioRxiv
- DOI / arXiv / URL：https://openreview.net/forum?id=4aa39a777762cc61ac3ba7dbbe09960c043918ea；bioRxiv: https://doi.org/10.1101/2025.06.06.658341
- PDF / 本地文件路径：临时读取 OpenReview PDF，未保存至项目目录
- 论文类型：系统论文 / omics discovery Agent
- 当前状态：已读全文文本；已纳入；round-2 边界已关闭为 `06;07`，`primary_module_for_filing=06`
- 阅读日期：2026-06-15
- 笔记作者：Codex

## Evidence Log

**2026-06-21 archive note**: OpenReview full PDF archived to project `Reference_PDF/` and rechecked against the existing full-text note.

## 2026-06-21 relaxed round-2 boundary closure

- `first_hand_sources_checked`: OpenReview full PDF for the ICML 2025 workshop version; Crossref DOI abstract for `10.1101/2025.06.06.658341`.
- Accepted relaxed classification: accept `scientific_object_modules=06;07`; `object_coverage_mode=multi_module`; `primary_module_for_filing=06`; `general_method_bucket=none`.
- Why: the system's core workflow remains phenotype-driven spatial-transcriptomics / TME analysis, which keeps `06` as the filing module. At the same time, the breast-carcinoma tumor-vs-normal case and the PDAC survival-phenotype case use TCGA clinical metadata, patient prognosis, clinically aggressive tumor-region localization, and prognostic spatial biomarkers, which is enough to add `07` under the relaxed object-coverage rule.
- Note implication: this note should no longer keep `07` as merely a tentative future possibility. The current first-hand full-text evidence is already sufficient to close the `06/07` boundary as `06;07`.

**证据级别**：full-text（OpenReview PDF 已下载到临时目录并转文本核读；未保存到项目目录）

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是，LLM-based multi-agent system | 摘要 p.1；lines 28-37, 76-91, 102-108 | automates full pipeline；dynamically selects, executes, corrects pipelines；multiple collaborative agents | 高 |
| 科学对象归类 | `06;07`，以 `06` 为 filing module | OpenReview full text；Crossref abstract | ST / TME / spatial-omics workflow支持 `06`，而 breast-carcinoma tumor phenotype 与 PDAC survival / prognosis / TCGA clinical metadata 也支持 `07` | 高 |
| 方法流程 | TCGA Agent + ML Agent + KG Agent，集成 bulk RNA-seq、ST、Scissor、PrimeKG | Fig.1/Methods lines 130-149, 157-160, 207-260, 283-286 | dataset discovery、phenotype association、knowledge graph contextualization | 高 |
| 实验验证 | breast carcinoma 与 pancreatic ductal carcinoma case studies | lines 353-361, 368-380 | 展示二分类 tumor phenotype 和 survival phenotype 分析 | 高 |
| 科学贡献 | 自动化 phenotype-guided ST data analysis 并生成生物解释 | 摘要与 Methods | 系统平台贡献强，生物发现为 case-study 级 | 高 |

## 0. 摘要翻译

Spatial transcriptomics 能揭示组织结构中的 gene expression patterns，有助于发现复杂 tumor microenvironments 中的分子机制。Phenotype-based discovery 可将空间表达模式与临床结局连接，但当前 ST 分析碎片化、劳动密集，需要手动寻找 bulk datasets、对齐多模态数据、选择和调优分析流程并解释结果。PhenoGraph 是一个 LLM-based multi-agent system，自动化 phenotype-driven ST data analysis，并用 biological knowledge graphs 增强可解释性。它根据用户查询动态选择、执行和修正 phenotype analysis pipelines，在多种 TME ST datasets 和 phenotype classes 上展示灵活性和有效性。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是。
- 判断依据：TCGA Agent、ML Agent、KG Agent 等多 Agent 分工，具备数据检索、代码执行、错误处理、memory、tool selection 和 KG reasoning。
- 判定置信度：高。
- 是否面向明确科研目标：是，phenotype-driven discovery in ST data。
- 是否具有多步行动过程：是。
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是，workflow orchestration。
  - 工具调用：是，GDC/TCGA API、Scissor、PrimeKG、LangChain。
  - 反馈迭代：是，ML Agent ReAct loop 和 error trace correction。
  - 自主决策：是，选择 dataset、phenotype type、hyperparameters。
  - 多 Agent 协作：是。
- 在科研流程中承担的明确角色：数据集发现者、分析执行者、知识图谱解释者、假设生成辅助者。

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否。
- 是否只是单次问答、摘要或分类：否。
- 是否缺少行动闭环：否。
- 若排除，排除理由：不排除。

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：`06;07`
- 二级类：`06.03` 组学、生物信息学与系统生物学；附加 `07` 肿瘤与临床结局对象覆盖
- 三级类：Spatial transcriptomics and tumor microenvironment analysis
- 四级专题：Biology / omics research agents
- 四级专题是否为新增：否。
- 归类理由：核心工作流对象仍是 ST data、TME、phenotype-associated tissue domains 和分子机制，但正文中的 breast-carcinoma 和 PDAC survival cases 已提供独立医学 / prognosis object evidence。
- 归类置信度：高。

### 2.2 对象优先判定

- 最终科学研究对象：肿瘤微环境空间转录组和临床 phenotype 关联。
- 最终科学问题：如何自动发现与临床 phenotype 相关的空间组织区域和解释性基因/通路关系。
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：LLM/LangChain 是方法；科学对象为生命科学组学。

### 2.3 容易混淆的边界

- 可能误归类到：`07` only。
- 最终判定：`06;07`，但 filing 保持 `06`。
- 判定理由：虽然系统主轴仍是 ST / omics workflow automation，但 PDAC survival phenotype、patient prognosis、TCGA clinical metadata、poor-survival spots 与肿瘤区域重合、prognostic biomarkers 等正文证据已足以支持附加 `07`。
- 是否需要二次复核：否，就当前 `06/07` 边界而言已可关闭；后续只需补更细的 task inventory / page-level note。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是，GPT-4o。
- Planning Agent：是，orchestration/workflow。
- Tool-using Agent：是。
- Retrieval-augmented Agent：是，TCGA retrieval 与 KG。
- Multi-Agent System：是。
- Robot / Embodied Agent：否。
- Human-in-the-loop Agent：用户指定 query。
- Hybrid Agent：是。
- 其他：Knowledge Graph Agent, ReAct-based ML Agent。

### 3.2 科研流程角色

- 文献检索与阅读：KG/biological context，非传统文献。
- 知识抽取与组织：是。
- 科学问题提出：用户给定。
- 假设生成：是，KG Agent 辅助。
- 实验设计：分析流程设计。
- 仿真建模：统计/ML analysis。
- 工具调用与代码执行：是。
- 实验执行：计算分析。
- 数据分析：是。
- 结果解释：是。
- 证据评估与验证：case study validation。
- 论文写作：否。
- 端到端科研流程自动化：ST phenotype analysis pipeline。

### 3.3 自主能力

- 任务分解：是。
- 计划生成：是。
- 工具调用：是。
- 记忆与状态维护：是，short-term memory。
- 反馈迭代：是，ReAct loop 与 error trace correction。
- 自主决策：是。
- 多 Agent 协作：是。
- 环境交互：API、代码执行、KG 查询。
- 闭环实验：计算分析闭环。

### 3.4 交叉属性标签

- 计算驱动：是。
- 数据驱动：是。
- 实验驱动：基于既有 ST / TCGA 数据。
- 仿真驱动：否。
- 多模态：是，bulk RNA-seq + spatial transcriptomics + clinical metadata + KG。
- 多尺度建模：组织区域与基因层面。
- 高通量筛选：否。
- 知识图谱：是，PrimeKG。
- 数字孪生：否。
- 机器人平台：否。
- 其他：spatial omics, tumor microenvironment。

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：phenotype-guided ST 分析需要跨数据库、统计方法和生物知识的复杂人工流程。
- 现有科研流程或方法的痛点：手动找 TCGA cohort、对齐 bulk 与 ST、调参、解释 marker genes 都费时且碎片化。
- 核心假设或直觉：多 Agent 可把数据检索、ML 分析和 KG reasoning 模块化并自动串联。

### 4.2 系统流程

1. 输入：用户关于 tissue / disease / phenotype 的自然语言查询和 ST 数据。
2. 任务分解 / 规划：PhenoGraph 启动 end-to-end multi-agent workflow。
3. 工具、数据库、模型或实验平台调用：TCGA Agent 调 GDC/TCGA；ML Agent 执行 adapted Scissor；KG Agent 查询 PrimeKG。
4. 中间结果反馈：ML Agent 根据执行状态、工具输出和 error trace 迭代修正。
5. 决策或迭代：自动选择 phenotype type、TCGA cohort、spatial regularization 与解释路径。
6. 输出：phenotype-associated spots/genes、空间组织区域和 KG-grounded biological interpretation。

### 4.3 系统组件

- Agent 核心：TCGA Agent, ML Agent, Knowledge Graph Agent。
- 工具 / API / 数据库：GDC API, TCGA, Scissor variant, PrimeKG, LangChain, GPT-4o。
- 记忆或状态模块：short-term memory。
- 规划器：PhenoGraph orchestration。
- 评估器 / verifier：computational validity checks and case study biological plausibility。
- 人类反馈或专家介入：用户 query。
- 实验平台或仿真环境：计算组学分析环境。

## 5. 实验与验证

### 5.1 验证方式

- benchmark：case studies，非标准 benchmark。
- 仿真验证：否。
- 高通量计算：组学计算。
- 机器人实验：否。
- 湿实验：否。
- 临床数据：TCGA clinical phenotype metadata。
- 真实场景部署：否。
- 专家评估：未明确。

### 5.2 数据、任务与指标

- 数据集 / 实验对象：breast invasive carcinoma ST data + TCGA-BRCA；pancreatic ductal carcinoma survival phenotype 等。
- 任务设置：binary tumor vs normal phenotype；survival-based phenotype analysis。
- 对比基线：未见强 baseline。
- 评价指标：biological coherence、phenotype-associated spots/genes、KG explanation。
- 关键结果：TCGA Agent 自动识别 TCGA-BRCA；KG Agent 解释 breast carcinoma / invasive carcinoma ontology links、co-expression/PPI 等。
- 是否有消融实验：未见。
- 是否有失败案例或负结果：未突出。

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：提供 phenotype-associated tissue/gene hypotheses 和解释。
- 科学贡献是否经过验证：case study 和生物知识图谱支持，未做新湿实验。
- 贡献强度判断：中。
- 科学贡献类型：数据分析 / 解释 / 系统平台。
- 证据强度：临床/组学数据 + KG 支持。

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单个 ST clustering model，而是多 Agent 自动组装和修正分析流程。
- 与已有 Agent / 科研智能系统的区别：把 phenotype-annotated bulk data、ST 和 KG reasoning 集成在一个 Agent workflow。
- 与同一科学领域其他 Agent 文献的关系：可与 BioMaster、CellAgent、SpatialAgent、AutoBA 比较。
- 主要创新点：phenotype-driven ST discovery 的 multi-agent + KG framework。

## 7. 局限性与风险

- Agent 自主性不足：用户仍需提供合理 phenotype query 和 ST 数据。
- 科学验证不足：case study 为主，缺少系统 benchmark 和 wet-lab validation。
- 泛化性不足：大规模不同癌种和非肿瘤 ST 数据待验证。
- 工具链依赖：依赖 TCGA/GDC、Scissor、PrimeKG 和 LLM 的稳定性。
- 数据泄漏或 benchmark 偏差：case studies 可能使用已知 cancer markers。
- 成本、可复现性或安全风险：LLM 输出解释可能过度推断；临床 phenotype 数据需隐私和合规处理。

## 8. 对综述写作的价值

- 可放入哪个章节：生命科学 / omics research agents。
- 可支撑哪个论点：Agent 可承担“多模态生物数据整合 + 分析执行 + 机制解释”的全流程角色。
- 可用于哪个表格或图：Multi-agent components in omics workflows。
- 适合作为代表性案例吗：适合。
- 推荐引用强度：核心引用。
- 需要在正文中特别引用的页码 / 图 / 表：Figure 1, Figure 3, Methods 2.2-2.4。
- 需要与哪些论文并列比较：BioMaster、AstroAgents。

## 9. 总结

### 9.1 一句话概括

多 Agent 自动解析空间转录组 phenotype。

### 9.2 速记版 pipeline

1. 用户提出 phenotype/ST 查询。
2. TCGA Agent 找 bulk cohort。
3. ML Agent 执行 spatial Scissor。
4. KG Agent 用 PrimeKG 解释。
5. 输出空间 phenotype-associated regions。

### 9.3 标注字段汇总

```text
是否纳入：是
主类：06 生命科学
二级类：06.03 组学、生物信息学与系统生物学
三级类：Spatial transcriptomics and tumor microenvironment analysis
四级专题：Biology / omics research agents
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Retrieval-augmented Agent; Multi-Agent System; Human-in-the-loop Agent; Hybrid Agent
科研流程角色：知识抽取与组织; 假设生成; 实验设计/分析流程设计; 工具调用与代码执行; 数据分析; 结果解释; 证据评估与验证; 端到端科研流程自动化
自主能力：任务分解; 计划生成; 工具调用; 记忆与状态维护; 反馈迭代; 自主决策; 多 Agent 协作; 环境交互
验证方式：临床数据; case study; 知识图谱支持
交叉属性：计算驱动; 数据驱动; 多模态; 多尺度建模; 知识图谱
科学贡献类型：数据分析; 解释; 系统平台
证据强度：高；OpenReview PDF 全文文本核读，科学验证为 case-study 级
归类置信度：高
纳入置信度：高
推荐引用强度：核心引用
```
