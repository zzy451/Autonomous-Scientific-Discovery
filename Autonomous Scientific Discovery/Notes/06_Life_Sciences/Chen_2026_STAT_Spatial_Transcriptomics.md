# Chen et al. 2026 - STAT: A multi-agent framework for integrated and interactive spatial transcriptomics analysis

## 2026-06-24 Batch30Partial2 writeback closure

- `paper_id`: `ASD-0743`
- `final_inclusion`: `yes`
- `scientific_object_modules`: `06;07`
- `object_coverage_mode`: `multi_module`
- `primary_module_for_filing`: `06`
- `general_method_bucket`: `none`
- `source_limited`: `yes`
- `safety_access_status`: `no_safety_skip__non_safety_access_limit`
- `first_hand_sources_checked`: DOI metadata abstract; official `STAT-agent` README; official `STAT-PaperRepro` benchmark / dataset materials
- `pdf_path`: `none`

**论文信息**
- 标题：STAT: A multi-agent framework for integrated and interactive spatial transcriptomics analysis
- 作者：Yuheng Chen; Shi Han; Zitong Chao; Yuyao Liu; Fan Zhang; Hao Chen; Jiguang Wang; Jiashun Xiao; Can Yang
- 年份：2026
- 来源 / venue：DOI / preprint ecosystem; official repo materials checked
- DOI / arXiv / URL：https://doi.org/10.64898/2026.05.01.722244
- PDF / 本地文件路径：无；当前环境下官方 DOI / preprint landing 仍受访问限制，未获取本地 PDF
- 论文类型：研究论文 / multi-agent spatial transcriptomics framework
- 当前状态：已纳入（source-limited，待全文跟进）
- 阅读日期：2026-06-24
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | DOI metadata abstract; official README | `STAT` 明确自称 multi-agent framework，并把自然语言请求转成规划、验证和执行式分析流程。 | 高 |
| `06` 模块 | 稳定支持 | title; README skill/task descriptions | 核心对象始终是 spatial transcriptomics / spatial omics analysis，因此 `06` 是稳定主模块。 | 高 |
| `07` 模块 | 稳定支持 | official reproduction / benchmark materials | 可访问一手材料包含 breast-cancer cohort、colorectal-cancer reproduction、tumor-vs-immune communication、tumor-vs-stroma differential analysis、tumor microenvironment pathway analysis，支持独立 `07` 肿瘤 / 病理相关对象覆盖。 | 中高 |
| 方法流程 | 多步 Agent workflow | abstract; README | natural-language query -> planning -> verification -> execution -> interactive analysis results。 | 高 |
| 证据状态 | source-limited | DOI / preprint landing status; repo materials | 官方 DOI / preprint landing 在当前环境仍受限，因此当前结论基于 DOI metadata abstract 与官方项目材料，不能虚构 PDF 已获取。 | 高 |

## 0. 摘要翻译

`STAT` 是一个面向 spatial transcriptomics 的多 Agent 分析框架，目标是把用户的自然语言分析需求转成可规划、可验证、可执行的空间组学分析流程。从当前可访问的一手证据看，它并不是领域无关的平台外壳，而是围绕 spatial transcriptomics / spatial omics 数据构建的专门系统，因此 `06` 是稳定主模块。同时，官方 README、reproduction repo 与 benchmark / dataset 说明中还明确出现乳腺癌、结直肠癌复现、肿瘤-免疫细胞通信、肿瘤-基质差异分析和肿瘤微环境通路分析等肿瘤 / 病理导向案例，足以在当前 relaxed rule 下支持额外的 `07` 覆盖。由于官方 DOI / preprint landing 在本环境受限，本 note 仍需保持 source-limited 表述。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：存在自然语言请求理解、分析规划、验证、执行与结果反馈的多步 Agent 流程
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：部分是
  - 多 Agent 协作：是
- 在科研流程中承担的明确角色：数据分析；结果解释；证据评估与验证；端到端组学分析自动化

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：`06;07`
- 覆盖模式：多模块
- 是否具有具体科学对象实验、验证、benchmark task、case study 或结果报告：是
- 独立 `01.04` 存放区：`none`
- Primary module for filing：`06`
- Primary module for filing 说明：仅用于笔记落盘与展示，不覆盖 `06;07` 的多模块事实
- 主展示模块一级类：`06`
- 主展示模块二级类：`06.03`
- 主展示模块三级类：spatial transcriptomics / spatial omics analysis
- 主展示模块四级专题：multi-agent spatial transcriptomics analysis systems
- 其他覆盖模块及对应层级路径：`07` 医学与健康科学 -> 肿瘤 / 病理相关空间组学案例
- 四级专题是否为新增：否
- 是否进入独立 `01.04` 存放区：否
- 每个模块的对象实验证据：
  - `06`：系统技能、任务定义和主问题稳定锚定 spatial transcriptomics / spatial omics 分析
  - `07`：官方复现与 benchmark 材料出现 breast cancer、colorectal cancer、tumor-vs-immune communication、tumor-vs-stroma differential analysis、tumor microenvironment pathway analysis
- 归类理由：`06` 是主对象模块；`07` 来自可识别的肿瘤 / 病理相关 case coverage，而不是泛化推断
- 归类置信度：中高

### 2.2 对象优先判定

- 最终科学研究对象：spatial transcriptomics / spatial omics datasets，以及其中的肿瘤 / 病理相关空间组学案例
- 最终科学问题：如何让多 Agent 系统更自主地完成 integrated and interactive spatial transcriptomics analysis
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：framework 只是系统形式，稳定对象仍是空间组学分析及其肿瘤相关案例

### 2.3 容易混淆的边界

- 可能误归类到：独立 `01.04`；或仅保留 `06`
- 最终判定：保持 `06;07`
- 判定理由：可访问的一手项目材料已足以支持 `06` 主对象和 `07` 癌症 / 病理相关案例覆盖；这不是因为“平台感强”就退回 `01.04`
- 多模块覆盖说明：`06` 来自核心对象；`07` 来自可识别的肿瘤 / 病理 case studies 与 reproduction tasks
- 01.04 判定说明：`none`
- 是否需要二次复核：需要全文跟进，但当前 `06;07` 结论已可稳定落地

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

- 文献检索与阅读：否
- 知识抽取与组织：部分是
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
- 自主决策：部分是
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

- 作者为什么提出该 Agent 系统：降低空间转录组分析的门槛、平台切换成本和复现负担
- 现有科研流程或方法的痛点：分析工具分散、交互复杂、复现难度高
- 核心假设或直觉：用多 Agent 规划、验证并执行空间组学分析，可以让分析更可交互、可复现、可自动化

### 4.2 系统流程

1. 输入：natural-language spatial transcriptomics query
2. 任务分解 / 规划：选择分析技能与执行顺序
3. 工具、数据库、模型或实验平台调用：执行 cell type annotation、deconvolution、domain detection、communication、trajectory 等分析
4. 中间结果反馈：对流程进行验证和修正
5. 决策或迭代：继续分析或调整 pipeline
6. 输出：interactive spatial transcriptomics analysis results

### 4.3 系统组件

- Agent 核心：STAT multi-agent framework
- 工具 / API / 数据库：spatial transcriptomics analysis skills 与 reproduction modules
- 记忆或状态模块：analysis planning and execution state
- 规划器：multi-agent orchestration over ST skills
- 评估器 / verifier：planned / verified / executed analysis checks
- 人类反馈或专家介入：用户以自然语言交互
- 实验平台或仿真环境：computational spatial-omics environment

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：否
- 高通量计算：否
- 机器人实验：否
- 湿实验：否
- 临床数据：部分是
- 真实场景部署：否
- 专家评估：未明确

### 5.2 数据、任务与指标

- 数据集 / 实验对象：spatial transcriptomics / spatial omics datasets；其中包含肿瘤相关案例
- 任务设置：interactive integrated analysis 与 paper-reproduction style workflows
- 对比基线：当前可访问材料未完整展开
- 评价指标：analysis completeness、correctness、usability 等工作流结果导向指标
- 关键结果：系统可把自然语言请求转成已规划、已验证、已执行的空间组学分析流程
- 是否有消融实验：当前可访问材料未完整展开
- 是否有失败案例或负结果：当前可访问材料未完整展开

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：更偏向空间组学分析系统与工作流自动化
- 科学贡献是否经过验证：是，但当前证据以 abstract + 官方项目材料为主
- 贡献强度判断：中
- 科学贡献类型：system_platform; single_cell_analysis; spatial_omics_analysis
- 证据强度：source_limited_project_or_benchmark_page

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单个预测模型，而是面向空间组学分析的多步 Agent workflow
- 与已有 Agent / 科研智能系统的区别：强调 conversational、interactive、reproducible spatial-omics analysis
- 与同一科学领域其他 Agent 文献的关系：可与 SpatialAgent、ST 相关组学 Agent 系统并列
- 主要创新点：把 integrated and interactive spatial transcriptomics analysis 显式交给多 Agent 系统执行

## 7. 局限性与风险

- Agent 自主性不足：平台能力仍需全文细化确认
- 科学验证不足：当前仍是 source-limited，尚未取得官方 PDF / full text
- 泛化性不足：跨更多 omics modalities 的表现仍待全文确认
- 工具链依赖：高度依赖 ST analysis ecosystem
- 数据泄漏或 benchmark 偏差：需要全文进一步核查
- 成本、可复现性或安全风险：当前主要风险是访问受限导致证据层级受限，而不是模块方向不稳

## 8. 对综述写作的价值

- 可放入哪个章节：`06` 生命科学中的 spatial omics agents；并在 `06/07` 边界中讨论肿瘤相关 case coverage
- 可支撑哪个论点：平台表述很强的论文，只要有稳定对象和明确病例 / 病理案例，仍可落到具体模块并支持多模块
- 可用于哪个表格或图：`06/07` relaxed multi-module boundary cases
- 适合作为代表性案例吗：可以，但需标注 source-limited
- 推荐引用强度：标准到核心之间
- 需要在正文中特别引用的页码 / 图 / 表：待全文可访问后补
- 需要与哪些论文并列比较：Wang_2025_SpatialAgent 及其他 spatial omics agents

## 9. 总结

### 9.1 一句话概括

多 Agent 空间转录组分析系统，并稳定覆盖肿瘤相关案例。

### 9.2 速记版 pipeline

1. 接收自然语言分析请求
2. 规划空间组学分析链
3. 验证并执行分析
4. 输出交互式结果

### 9.3 标注字段汇总

```text
是否纳入：是
科学对象模块：06;07
覆盖模式：多模块
是否具有具体科学对象实验：是
general_method_bucket：none
Primary module for filing：06
是否进入 01.04 存放区：否
主展示模块一级类：06
主展示模块二级类：06.03
主展示模块三级类：spatial transcriptomics / spatial omics analysis
主展示模块四级专题：multi-agent spatial transcriptomics analysis systems
其他覆盖模块及对应层级路径：07 -> 肿瘤 / 病理相关空间组学案例
module_assignment_evidence：06 来自核心 spatial omics 对象；07 来自 breast cancer、colorectal cancer、tumor microenvironment 等官方案例材料
multi_module_object_coverage_note：06 为主对象模块；07 由可识别的 oncology / pathology-oriented case coverage 支持
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Multi-Agent System; Hybrid Agent
科研流程角色：tool_use_and_code_execution; data_analysis; result_interpretation; evidence_assessment_and_validation; end_to_end_research_automation
自主能力：task_decomposition; planning; tool_use; feedback_iteration; multi_agent_collaboration
验证方式：benchmark
交叉属性：computation_driven; data_driven
科学贡献类型：system_platform; single_cell_analysis; spatial_omics_analysis
证据强度：source_limited_project_or_benchmark_page
归类置信度：中高
纳入置信度：高
推荐引用强度：standard
```
