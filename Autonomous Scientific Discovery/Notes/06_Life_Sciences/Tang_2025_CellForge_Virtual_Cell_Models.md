# Tang et al. 2025 - CellForge: Agentic Design of Virtual Cell Models

## 2026-06-24 Batch25Partial1 final adjudication writeback

- `scientific_object_modules`: `06`
- `object_coverage_mode`: `single_module`
- `has_concrete_object_experiments`: `yes`
- `general_method_bucket`: `none`
- `primary_module_for_filing`: `06`
- `first_hand_sources_checked`: arXiv abstract page `https://arxiv.org/abs/2508.02276`
- `classification_evidence_source_level`: `first_hand_abstract_or_landing_page`
- `source_limited`: `no`
- `note_revision_required`: `no`
- `module_assignment_evidence`: the abstract directly anchors the system in virtual-cell model design and single-cell multi-omics perturbation prediction. All validated objects remain within life-science single-cell biology rather than a domain-general `01.04` research-agent substrate.
- `multi_module_object_coverage_note`: authoritative classification is `06` only. The note remains in the class-06 folder because that is also the final primary module; file location is a filing convenience, not classification authority.

**论文信息**
- 标题：CellForge: Agentic Design of Virtual Cell Models
- 作者：Xiangru Tang; Zhuoyun Yu; Jiapeng Chen; Yan Cui; Daniel Shao; Weixu Wang; Fang Wu; Yuchen Zhuang; Wenqi Shi; Zhi Huang; Arman Cohan; Xihong Lin; Fabian Theis; Smita Krishnaswamy; Mark Gerstein
- 年份：2025
- 来源 / venue：arXiv / OpenReview
- DOI / arXiv / URL：https://arxiv.org/abs/2508.02276
- PDF / 本地文件路径：本轮以 arXiv abstract page 为一手来源；未在 workspace 中确认本地归档 PDF
- 论文类型：研究论文 / agentic virtual-cell model design
- 当前状态：to_read
- 阅读日期：2026-06-24
- 本轮写回口径：`modules=06`；`primary=06`；`source_limited=no`
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| 一手来源核对 | 已核对 arXiv 摘要页 | arXiv abs page | 当前判断基于摘要中的对象、流程和数据集描述 | 高 |
| Agent 纳入 | 是 | arXiv abstract | 系统由多 Agent 协作完成 task analysis、method design 和 executable implementation generation | 高 |
| 科学对象归类 | `06` only | arXiv abstract | 稳定对象是 virtual cell models 与 single-cell multi-omics perturbation tasks | 高 |
| 不进 `01.04` | 是 | arXiv abstract | 虽然方法贡献突出，但验证对象始终是 single-cell biology，而非无对象通用平台 | 高 |
| 方法流程 | data/task analysis -> design -> code generation -> evaluation | arXiv abstract | 系统从原始单细胞多组学数据和任务描述出发生成模型与实现 | 高 |
| 验证方式 | six datasets across perturbation modalities | arXiv abstract | 评测覆盖 gene knockouts、drug treatments、cytokine stimulations 等六个数据集 | 高 |

## 0. 摘要翻译

CellForge 试图让多 Agent 系统直接从单细胞多组学数据和任务描述出发，自主设计适配的 virtual cell 模型架构，并生成可执行代码。论文的方法创新确实很强，但它并不是领域无关的科研 Agent 平台，因为任务、数据、模型目标和评测都紧密锚定在 virtual-cell / single-cell biology 上。因此最终分类应保持 `06`，而不是退回 `01.04`。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：存在多 Agent 协作、任务分解、方法设计、代码生成和结果反馈的多步闭环
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：是
- 在科研流程中承担的明确角色：任务分析、模型设计、代码执行、结果评估

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：`06`
- 覆盖模式：单模块
- 是否具有具体科学对象实验、验证、benchmark task、case study 或结果报告：是
- 独立 `01.04` 存放区：none
- Primary module for filing：`06`
- Primary module for filing 说明：此处与最终模块一致；文件路径仅是归档位置。
- 主展示模块一级类：`06`
- 主展示模块二级类：`06.03`
- 主展示模块三级类：virtual-cell / single-cell model design
- 主展示模块四级专题：agentic virtual-cell and single-cell model-design systems
- 其他覆盖模块及对应层级路径：none
- 每个模块的对象实验证据：`06` 来自 virtual cell construction、single-cell perturbation prediction 与多组学数据集评测
- 归类理由：论文稳定研究对象是 single-cell biology 与 virtual-cell modeling
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：single-cell multi-omics perturbation tasks and virtual cell models
- 最终科学问题：如何让 Agent 自主设计可用于单细胞扰动预测的计算生物学模型
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：multi-agent collaboration 是方法外观，稳定对象仍是生命科学建模任务

### 2.3 容易混淆的边界

- 可能误归类到：`01.04`
- 最终判定：保持 `06`
- 判定理由：只要数据、任务和评测稳定围绕单细胞 biology，就不应视为通用科研平台
- 多模块覆盖说明：无；冻结口径不增加 `07`
- 01.04 判定说明：不适用；并非无具体对象实验的通用方法文献
- 是否需要二次复核：否；当前摘要已足以支撑最终分类。后续全文只会补足细节。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：是
- Multi-Agent System：是
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：未强调
- Hybrid Agent：是
- 其他：virtual-cell model-design agents

### 3.2 科研流程角色

- 文献检索与阅读：是
- 知识抽取与组织：是
- 科学问题提出：否
- 假设生成：是
- 实验设计：否
- 仿真建模：是
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
- 闭环实验：否；主要是计算建模闭环

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 实验驱动：否
- 仿真驱动：是
- 多模态：是
- 多尺度建模：部分是
- 高通量筛选：否
- 知识图谱：否
- 数字孪生：部分是
- 机器人平台：否
- 其他：single-cell multi-omics

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：降低 virtual cell 建模对跨学科专家经验的依赖
- 现有科研流程或方法的痛点：生物系统复杂、多组学数据异构，模型设计高度依赖人工
- 核心假设或直觉：多 Agent 讨论和协商比单 Agent 或纯人工设计更可能产生高质量模型结构

### 4.2 系统流程

1. 输入：raw single-cell multi-omics data and task descriptions
2. 任务分解 / 规划：Task Analysis 模块分析数据与任务
3. 工具、数据库、模型或实验平台调用：Method Design 模块中的专门 agents 协作提出结构方案
4. 中间结果反馈：不同 agents 交换意见并形成 consensus
5. 决策或迭代：Experiment Execution 模块生成可执行代码并评估结果
6. 输出：optimized virtual cell model architecture and executable implementation

### 4.3 系统组件

- Agent 核心：CellForge multi-agent framework
- 工具 / API / 数据库：literature retrieval、code generation、biological datasets
- 记忆或状态模块：任务状态与协商结果
- 规划器：task analysis and design deliberation
- 评估器 / verifier：benchmark performance on perturbation datasets
- 人类反馈或专家介入：强调 autonomous method development
- 实验平台或仿真环境：computational biology benchmarks

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：是
- 高通量计算：否
- 机器人实验：否
- 湿实验：否
- 临床数据：否
- 真实场景部署：否
- 专家评估：否

### 5.2 数据、任务与指标

- 数据集 / 实验对象：六个数据集，覆盖 gene knockouts、drug treatments、cytokine stimulations，以及 scRNA-seq、scATAC-seq、CITE-seq
- 任务设置：single-cell perturbation prediction and virtual cell modeling
- 对比基线：已有 task-specific state-of-the-art methods
- 评价指标：生成模型的竞争力与架构创新性
- 关键结果：摘要声称 CellForge consistently outperforms task-specific baselines
- 是否有消融实验：摘要未展开
- 是否有失败案例或负结果：摘要未展开

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：更偏向生命科学建模方法的自动化创新
- 科学贡献是否经过验证：是
- 贡献强度判断：中高
- 科学贡献类型：system_platform; single_cell_analysis
- 证据强度：computationally_validated
- 是否仍需要进一步全文复核：否；当前摘要已足以支撑 `06`。后续全文只会补足基准细节，不影响 frozen adjudication。

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单一 perturbation predictor，而是自主设计方法和代码的多 Agent 系统
- 与已有 Agent / 科研智能系统的区别：强调多 Agent deliberation 产生新的模型组件
- 与同一科学领域其他 Agent 文献的关系：可与 CASSIA、SpatialAgent、Talk2Biomodels 等生命科学系统比较
- 主要创新点：把方法设计本身变成 single-cell biology 场景中的 agentic workflow

## 7. 局限性与风险

- Agent 自主性不足：具体协商与验证过程仍待全文确认
- 科学验证不足：当前公开证据主要来自 arXiv 摘要
- 泛化性不足：迁移到更广泛 biological modeling tasks 的能力仍待观察
- 工具链依赖：高度依赖 LLM 与代码生成质量
- 数据泄漏或 benchmark 偏差：需待全文进一步核查
- 成本、可复现性或安全风险：多 Agent code generation 的成本和稳定性仍需关注

## 8. 对综述写作的价值

- 可放入哪个章节：06 生命科学中的 single-cell / virtual-cell agents
- 可支撑哪个论点：即使论文强调 method development，只要对象和评测稳定落在 single-cell biology，就应保留在具体学科模块
- 可用于哪个表格或图：`06 / 01.04` 边界案例表
- 适合作为代表性案例吗：是
- 推荐引用强度：core
- 需要在正文中特别引用的页码 / 图 / 表：后续全文可补；当前摘要已足够支持对象边界
- 需要与哪些论文并列比较：CASSIA、SpatialAgent、Talk2Biomodels

## 9. 总结

### 9.1 一句话概括

多 Agent 自主设计 virtual cell 模型并生成可执行实现。

### 9.2 速记版 pipeline

1. 读入单细胞多组学数据与任务
2. 多 Agent 讨论模型设计
3. 生成并执行代码
4. 输出更优 virtual cell model

### 9.3 标注字段汇总

```text
是否纳入：是
科学对象模块：06
覆盖模式：single_module
是否具有具体科学对象实验：yes
general_method_bucket：none
Primary module for filing：06
是否进入 01.04 存放区：no
主展示模块一级类：06
主展示模块二级类：06.03
主展示模块三级类：virtual-cell / single-cell model design
主展示模块四级专题：agentic virtual-cell and single-cell model-design systems
其他覆盖模块及对应层级路径：none
module_assignment_evidence：virtual cell construction, single-cell perturbation prediction, multi-omics dataset evaluation
multi_module_object_coverage_note：keep virtual-cell / single-cell biology framing explicit; do not retreat to 01.04
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Retrieval-augmented Agent; Multi-Agent System; Hybrid Agent
科研流程角色：literature_search_and_reading; knowledge_extraction_and_organization; hypothesis_generation; simulation_modeling; tool_use_and_code_execution; data_analysis; result_interpretation; evidence_assessment_and_validation; end_to_end_research_automation
自主能力：task_decomposition; planning; tool_use; memory_or_state_tracking; feedback_iteration; autonomous_decision_making; multi_agent_collaboration
验证方式：benchmark; computational_validation
交叉属性：computation_driven; data_driven; simulation_driven; multimodal
科学贡献类型：system_platform; single_cell_analysis
证据强度：computationally_validated
归类置信度：high
纳入置信度：high
推荐引用强度：core
```
