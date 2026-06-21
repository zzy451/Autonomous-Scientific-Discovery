# Chen et al. 2026 - STAT: A multi-agent framework for integrated and interactive spatial transcriptomics analysis

## 2026-06-21 relaxed round-2 boundary closure

- `scientific_object_modules`: `06;07`
- `object_coverage_mode`: `multi_module`
- `primary_module_for_filing`: `06`
- `general_method_bucket`: `none`
- `first_hand_sources_checked`: Crossref DOI abstract `10.64898/2026.05.01.722244`; official `STAT-agent` README; official `STAT-PaperRepro` benchmark `queries.json`; official `STAT-PaperRepro` dataset note `DATA.md`; official `STAT-PaperRepro/colorectal_cancer/README.md`
- `classification_evidence_source_level`: `project_or_benchmark_page`
- `note_revision_required`: `no`

This round closes the `06 / 07` boundary as `06;07`. `06` remains the primary filing module because the system is fundamentally a spatial transcriptomics / spatial omics analysis agent. `07` is now also supported under the relaxed object-coverage rule because the accessible first-hand evidence includes a mixed-resolution breast-cancer cohort, reproduction of a published colorectal-cancer study, and official benchmark / demo tasks on tumor-versus-immune communication, tumor-versus-stroma differential analysis, and tumor-microenvironment pathway analysis. These are recognizable oncology / pathology-oriented case studies rather than merely generic omics benchmarks.

**论文信息**
- 标题：STAT: A multi-agent framework for integrated and interactive spatial transcriptomics analysis
- 作者：Yuheng Chen; Shi Han; Zitong Chao; Yuyao Liu; Fan Zhang; Hao Chen; Jiguang Wang; Jiashun Xiao; Can Yang
- 年份：2026
- 来源 / venue：Research Square / preprint page
- DOI / arXiv / URL：https://doi.org/10.64898/2026.05.01.722244
- PDF / 本地文件路径：当前笔记基于 bioRxiv/Sciety 检索页、GitHub README 与 reviewer 一手证据；本地未保存 PDF
- 论文类型：研究论文 / multi-agent spatial transcriptomics framework
- 当前状态：to_read
- 阅读日期：2026-06-20
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | title / GitHub README / reviewer evidence | `STAT` 直接定义为 multi-agent framework for spatial transcriptomics analysis | 高 |
| 科学对象归类 | `06.03` | title / repo skill list | 核心对象是 spatial transcriptomics / spatial omics data analysis | 高 |
| 方法流程 | natural-language query -> planned verified executed analysis | README / reviewer evidence | 系统将自然语言请求转成可执行空间组学分析流程 | 高 |
| 边界判断 | 不应改到 `01.04` | object-first rule | 尽管 “framework” 表述强，但技能目录和案例都强绑定 spatial omics 任务 | 高 |
| 验证方式 | spatial omics task-level computational validation | repo / reviewer evidence | 有 ST analysis pipeline 和复现实验导向证据 | 中高 |

## 0. 摘要翻译

`STAT` 是一个面向空间转录组分析的 multi-agent framework。它允许用户用自然语言发起分析请求，然后由 Agent 规划、验证并执行空间组学数据分析流程。虽然论文把自己包装成一个 framework，但它并不是领域无关平台，因为内置技能和复现实验都紧紧围绕 spatial transcriptomics / spatial omics，因此主类仍应保留在 `06.03`。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：存在自然语言请求理解、分析规划、执行、验证和结果反馈
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：是
- 在科研流程中承担的明确角色：空间组学数据分析、结果解释、复现实验工作流

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：06
- 二级类：06.03
- 三级类：spatial transcriptomics analysis
- 四级专题：Multi-agent spatial-transcriptomics analysis systems
- 四级专题是否为新增：否
- 归类理由：论文的技能集合和任务对象都稳定锚定在 spatial transcriptomics analysis
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：spatial transcriptomics / spatial omics datasets
- 最终科学问题：如何让 Agent 更自主地完成 integrated and interactive spatial transcriptomics analysis
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：framework 和 conversational interface 只是形式，稳定对象仍是空间组学分析本身

### 2.3 容易混淆的边界

- 可能误归类到：01.04
- 最终判定：保持 06.03
- 判定理由：如果它是通用 scientific workflow framework，就不应内置如此具体的 spatial transcriptomics skills
- 是否需要二次复核：需要，以补足更细的 biological case depth

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：部分是
- Multi-Agent System：是
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：部分是
- Hybrid Agent：是
- 其他：spatial omics analytical agents

### 3.2 科研流程角色

- 文献检索与阅读：部分是
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
- 记忆与状态维护：部分是
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
- 多模态：部分是
- 多尺度建模：部分是
- 高通量筛选：否
- 知识图谱：否
- 数字孪生：否
- 机器人平台：否
- 其他：spatial omics workflow reproduction

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：减少空间转录组分析的多平台切换与高门槛
- 现有科研流程或方法的痛点：分析方法繁多、工具分散、交互成本高
- 核心假设或直觉：如果由多 Agent 系统规划和验证 spatial omics analysis，就能降低分析摩擦并提高复现性

### 4.2 系统流程

1. 输入：natural-language spatial transcriptomics query
2. 任务分解 / 规划：选择分析技能和执行顺序
3. 工具、数据库、模型或实验平台调用：执行 cell type annotation、deconvolution、domain detection、communication、trajectory 等任务
4. 中间结果反馈：系统检查并修正分析过程
5. 决策或迭代：继续分析或调整 pipeline
6. 输出：interactive spatial transcriptomics analysis results

### 4.3 系统组件

- Agent 核心：STAT
- 工具 / API / 数据库：spatial transcriptomics analysis skills and reproducibility modules
- 记忆或状态模块：analysis planning and execution state
- 规划器：multi-agent orchestration over ST skills
- 评估器 / verifier：planned, verified, executed analysis checks
- 人类反馈或专家介入：用户以自然语言交互
- 实验平台或仿真环境：computational spatial-omics environment

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：否
- 高通量计算：否
- 机器人实验：否
- 湿实验：否
- 临床数据：否
- 真实场景部署：否
- 专家评估：未明确

### 5.2 数据、任务与指标

- 数据集 / 实验对象：spatial transcriptomics / spatial omics datasets
- 任务设置：interactive integrated analysis and paper-reproduction style workflows
- 对比基线：manual or less integrated analysis pipelines implied
- 评价指标：analysis completeness, correctness and usability
- 关键结果：系统可把自然语言请求转为已验证的空间组学分析流程
- 是否有消融实验：当前笔记未展开
- 是否有失败案例或负结果：当前笔记未展开

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：更偏向空间组学分析平台与 workflow 自动化
- 科学贡献是否经过验证：是
- 贡献强度判断：中
- 科学贡献类型：system_platform; single_cell_analysis
- 证据强度：medium_high_preprint

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单个分析模型，而是围绕空间组学技能集合的多 Agent 系统
- 与已有 Agent / 科研智能系统的区别：更强调 conversational spatial-omics workflow
- 与同一科学领域其他 Agent 文献的关系：可与 STAgent、SpatialAgent、CASSIA 对照
- 主要创新点：把 integrated, interactive spatial transcriptomics analysis 交给多 Agent framework

## 7. 局限性与风险

- Agent 自主性不足：平台表述较强，仍需全文确认 biological case depth
- 科学验证不足：当前主要依赖摘要、仓库和 reviewer 证据
- 泛化性不足：跨其他 omics modalities 的表现有待继续核实
- 工具链依赖：高度依赖 ST analysis ecosystem
- 数据泄漏或 benchmark 偏差：需要全文更细核查
- 成本、可复现性或安全风险：复现实验细节仍需后续确认

## 8. 对综述写作的价值

- 可放入哪个章节：06 生命科学中的 spatial omics agents
- 可支撑哪个论点：framework wording 很强的样本，只要技能和对象都绑定具体生命科学数据，仍应归到学科内
- 可用于哪个表格或图：`06.03 / 01.04` 边界案例表
- 适合作为代表性案例吗：是
- 推荐引用强度：标准到核心之间
- 需要在正文中特别引用的页码 / 图 / 表：后续全文补充
- 需要与哪些论文并列比较：Lin_2025_Spatial_Transcriptomics_Pancreas_Maturation; Wang_2025_SpatialAgent

## 9. 总结

### 9.1 一句话概括

多 Agent framework 把空间转录组分析变成可交互可执行 workflow。

### 9.2 速记版 pipeline

1. 接收自然语言分析请求
2. 规划空间组学技能链
3. 执行并验证分析
4. 输出可交互结果

### 9.3 标注字段汇总

```text
是否纳入：to_read
主类：06
二级类：06.03
三级类：spatial transcriptomics analysis
四级专题：Multi-agent spatial-transcriptomics analysis systems
Agent 类型：LLM Agent; Multi-Agent System; Tool-using Agent; Hybrid Agent
科研流程角色：data_analysis; knowledge_extraction_and_organization; workflow_orchestration; evidence_assessment_and_validation
自主能力：task_decomposition; planning; tool_use; feedback_iteration; autonomous_decision_making; multi_agent_collaboration
验证方式：benchmark; computational_validation
交叉属性：computation_driven; data_driven
科学贡献类型：system_platform; single_cell_analysis
证据强度：medium_high_preprint
归类置信度：高
纳入置信度：高
推荐引用强度：标准引用
```
