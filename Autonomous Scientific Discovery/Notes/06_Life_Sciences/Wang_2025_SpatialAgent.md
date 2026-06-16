# Wang et al. 2025 - SpatialAgent

**论文信息**
- 标题：SpatialAgent: An autonomous AI agent for spatial biology
- 作者：Hanchen Wang, Yichun He, Paula P. Coelho, Matthew Bucci, Abbas Nazir, Bob Chen, Linh Trinh, Serena Zhang, Kexin Huang, Vineethkrishna Chandrasekar, Douglas C. Chung, Minsheng Hao, Ana Carolina Leote, Yongju Lee, Bo Li, Tianyu Liu, Jin Liu, Romain Lopez, Tawaun A. Lucas, Mingyu Ma, Nikita Makarov, Lisa McGinnis, Linna Peng, Stephen Ra, Gabriele Scalia, Avtar Singh, Liming Tao, Masatoshi Uehara, Chenyu Wang, Runmin Wei, Ryan Copping, Orit Rozenblatt-Rosen, Jure Leskovec, Aviv Regev
- 年份：2025
- 来源 / venue：bioRxiv preprint
- DOI / arXiv / URL：https://doi.org/10.1101/2025.04.03.646459；https://www.biorxiv.org/content/10.1101/2025.04.03.646459v1；官方代码/说明页：https://github.com/Genentech/SpatialAgent
- PDF / 本地文件路径：bioRxiv PDF/HTML 本次仍被 Cloudflare challenge 阻断；已使用 DOI/metadata、可访问摘要线索和官方 GitHub README，未完成全文 PDF 阅读
- 论文类型：系统论文 / 空间生物学 Agent
- 当前状态：已读摘要与官方仓库说明 / 已纳入 / 待全文复核
- 阅读日期：2026-06-16
- 笔记作者：Codex

## Evidence Log

证据级别：abstract+metadata + official repository（bioRxiv 全文未能访问；官方 GitHub 对架构和工具数量提供较强辅助证据，但不能替代论文全文页码）。

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是，空间生物学自主 Agent | 题名/摘要线索；官方 GitHub README Overview | 系统整合 LLM、dynamic tool execution 和 adaptive reasoning；采用 Plan-Act-Conclude 架构；含 72 tools 和 17 skill templates | 中-高 |
| 科学对象归类 | `06` 生命科学，spatial biology / spatial transcriptomics | 题名、摘要线索、官方 GitHub | 对象为 spatial biology、spatial transcriptomics、single-cell RNA-seq、cell-cell communication、tissue niches | 高 |
| 方法流程 | LLM Agent 规划 -> 调用空间组学/基因组/文献/数据库工具 -> 分析和解释 -> 生成假设或设计建议 | 官方 GitHub README；摘要线索 | 覆盖 experimental design、multimodal data analysis、hypothesis generation | 中 |
| 实验验证 | 多组织/多物种空间组学数据，含 human brain、heart、mouse colon colitis model 等；与方法/专家比较 | 摘要线索和第三方页面；待全文确认 | 据摘要线索称约 two million cells，并匹配/超过人类科学家或最佳计算方法 | 中 |
| 科学贡献 | 空间生物学研究工作流 Agent，支持 panel design、tissue niche annotation、cell-cell communication 分析 | 官方 GitHub / 摘要线索 | 贡献主要为领域专用 Agent 和空间组学任务表现；具体新发现需全文复核 | 中 |

## 0. 摘要翻译

SpatialAgent 是一个面向 spatial biology 的自主 AI Agent。它将 LLM、自适应推理和动态工具执行结合起来，用于空间生物学研究流程，包括实验设计、多模态空间组学数据分析、数据库/文献查询和假设生成。官方仓库说明其采用 Plan-Act-Conclude 架构，配备 72 个 specialized tools 和 17 个 skill templates。摘要层证据显示，作者在 human brain、heart、mouse colon colitis model 等空间组学数据上评估系统，并声称其在部分任务中达到或超过人类科学家/既有计算方法表现。由于 bioRxiv 全文仍不可访问，具体页码、figure/table、数据集和指标需二次复核。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是。
- 判断依据：题名明确为 autonomous AI agent；官方实现说明有 Plan-Act-Conclude、dynamic tool execution、tool registry、skill templates 和面向空间生物学任务的自动分析。
- 判定置信度：中-高；架构证据较强，但论文全文未读。
- 是否面向明确科研目标：是，spatial biology / spatial transcriptomics 研究。
- 是否具有多步行动过程：是，规划、工具调用、分析、解释、假设/设计输出。
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是，Plan-Act-Conclude。
  - 工具调用：是，72 tools。
  - 反馈迭代：可能有 adaptive reasoning，具体 loop 待全文。
  - 自主决策：是，动态选择工具和分析路径。
  - 多 Agent 协作：未见明确证据。
- 在科研流程中承担的明确角色：实验设计助理、空间组学数据分析者、文献/数据库检索者、结果解释者、假设生成者。

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否，是工具调用和规划型 Agent。
- 是否只是单次问答、摘要或分类：否。
- 是否缺少行动闭环：不缺多步行动；闭环反馈强度待全文确认。
- 若排除，排除理由：不排除。

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：`06` 生命科学。
- 二级类：`06.03` 组学、生物信息学与系统生物学。
- 三级类：空间转录组学 / 单细胞空间生物学。
- 四级专题：Biology / omics research agents；可副标 Spatial biology agents。
- 四级专题是否为新增：否。
- 归类理由：研究对象是细胞、组织空间结构、空间转录组、细胞类型和细胞间通讯。
- 归类置信度：高。

### 2.2 对象优先判定

- 最终科学研究对象：空间转录组、single-cell RNA-seq、组织 niche、cell-cell communication。
- 最终科学问题：Agent 能否自主完成空间生物学实验设计、数据分析和假设生成。
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：LLM 和工具链是方法，验证任务和科学对象均属于生命科学。

### 2.3 容易混淆的边界

- 可能误归类到：`01.04` 通用科研 Agent；`07` 医学与健康科学。
- 最终判定：`06`。
- 判定理由：尽管可能使用疾病组织数据，核心是 spatial biology / omics 方法与生物机制分析，不是临床诊疗或药物转化。
- 是否需要二次复核：需要，全文需核对是否存在医学转化主问题。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是。
- Planning Agent：是。
- Tool-using Agent：是。
- Retrieval-augmented Agent：是，含数据库/文献/知识查询工具。
- Multi-Agent System：未确认。
- Robot / Embodied Agent：否。
- Human-in-the-loop Agent：可能有 human collaboration，细节待全文。
- Hybrid Agent：是。
- 其他：spatial biology domain agent。

### 3.2 科研流程角色

- 文献检索与阅读：是/可能，工具集中包含 literature mining 类能力。
- 知识抽取与组织：是。
- 科学问题提出：可能。
- 假设生成：是。
- 实验设计：是，含 gene panel design 等。
- 仿真建模：未确认。
- 工具调用与代码执行：是。
- 实验执行：否，主要是计算和设计。
- 数据分析：核心。
- 结果解释：核心。
- 证据评估与验证：部分支持，具体待全文。
- 论文写作：未见证据。
- 端到端科研流程自动化：空间组学计算研究链条层面部分支持。

### 3.3 自主能力

- 任务分解：是。
- 计划生成：是。
- 工具调用：是。
- 记忆与状态维护：待全文复核。
- 反馈迭代：可能有 adaptive reasoning，待全文。
- 自主决策：是。
- 多 Agent 协作：未确认。
- 环境交互：计算环境、空间组学工具、数据库。
- 闭环实验：否，未见湿实验闭环。

### 3.4 交叉属性标签

- 计算驱动：是。
- 数据驱动：是。
- 实验驱动：部分，支持实验设计但不执行湿实验。
- 仿真驱动：未确认。
- 多模态：是，空间转录组 + single-cell RNA-seq 等。
- 多尺度建模：可能，细胞-组织层面。
- 高通量筛选：否。
- 知识图谱：未确认。
- 数字孪生：否。
- 机器人平台：否。
- 其他：spatial omics；database tools；code execution。

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：空间生物学工作流跨实验设计、数据处理、空间统计、基因组分析和生物解释，专家瓶颈明显。
- 现有科研流程或方法的痛点：工具多、任务复杂、人工分析耗时，单一模型难覆盖完整研究链条。
- 核心假设或直觉：LLM Agent 若配备领域工具与技能模板，可以像空间生物学研究助理一样规划、执行和解释工作流。

### 4.2 系统流程

1. 输入：用户的空间生物学研究目标、数据集或 panel design / annotation / CCI 等任务。
2. 任务分解 / 规划：Plan-Act-Conclude 架构生成执行计划。
3. 工具、数据库、模型或实验平台调用：调用 CZI catalog、CellMarker、PanglaoDB、空间分析、genomic analysis、literature mining 等工具（工具清单需全文/仓库复核）。
4. 中间结果反馈：根据工具结果进行 adaptive reasoning；具体记忆机制待全文。
5. 决策或迭代：选择下一步分析、修正 panel 或生成新假设。
6. 输出：分析报告、细胞类型/空间 niche 解释、cell-cell communication pattern、panel 设计建议或新生物学假设。

### 4.3 系统组件

- Agent 核心：LLM-based SpatialAgent。
- 工具 / API / 数据库：72 specialized tools；17 skill templates；具体版本待全文/仓库复核。
- 记忆或状态模块：待全文复核。
- 规划器：Plan-Act-Conclude prompt / planner。
- 评估器 / verifier：任务评测和与人类/计算方法比较，细节待全文。
- 人类反馈或专家介入：可能有专家比较/协作，待全文。
- 实验平台或仿真环境：无机器人湿实验平台。

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是，空间生物学任务评测，细节待全文。
- 仿真验证：未确认。
- 高通量计算：是，空间组学/单细胞数据处理。
- 机器人实验：否。
- 湿实验：未确认。
- 临床数据：可能涉及 prostate cancer 或 colitis 等疾病组织数据，待全文。
- 真实场景部署：真实研究数据案例。
- 专家评估：摘要线索称与 human scientists 比较，待全文。

### 5.2 数据、任务与指标

- 数据集 / 实验对象：human brain、heart、mouse colon colitis model，约 two million cells 的摘要线索；具体以全文为准。
- 任务设置：空间数据分析、tissue niche annotation、cell-cell communication、gene panel design。
- 对比基线：最佳计算方法和人类科学家，具体名称待全文。
- 评价指标：任务准确性、细胞类型分辨率、生物一致性、专家评价等，具体待全文。
- 关键结果：摘要/官方线索称在关键任务上超过既有计算方法，并匹配或超过人类科学家。
- 是否有消融实验：待全文。
- 是否有失败案例或负结果：待全文。

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：可能产生 cell-cell communication patterns、panel design improvements 和 tissue niche insights；需全文确认。
- 科学贡献是否经过验证：目前证据主要是预印本摘要/仓库说明，需全文复核。
- 贡献强度判断：中。
- 科学贡献类型：系统平台 / 数据分析 / 假设生成 / 实验设计。
- 证据强度：abstract+metadata + official repository；非全文证据。

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单个空间组学算法，而是能规划并调用多个空间生物学工具的 Agent。
- 与已有 Agent / 科研智能系统的区别：深度绑定 spatial biology 工具生态和任务模板。
- 与同一科学领域其他 Agent 文献的关系：可与 CellVoyager、BioMaster、BioDiscoveryAgent、GeneAgent 并列为 omics Agent。
- 主要创新点：领域专用工具链 + Plan-Act-Conclude 架构覆盖空间组学研究链条。

## 7. 局限性与风险

- Agent 自主性不足：完整闭环、记忆机制和人工介入边界仍需全文确认。
- 科学验证不足：目前未能核验全文 figure/table 和外部实验验证。
- 泛化性不足：可能依赖特定空间组学数据类型、工具可用性和 prompt/skill templates。
- 工具链依赖：高度依赖数据库、空间分析库和 API。
- 数据泄漏或 benchmark 偏差：公开空间组学数据可能被模型或工具文档覆盖，需核查评测设计。
- 成本、可复现性或安全风险：复杂工具链和 API key 影响复现；生物医学解释需专家把关。

## 8. 对综述写作的价值

- 可放入哪个章节：生命科学中的 single-cell / spatial omics Agent。
- 可支撑哪个论点：领域工具链可以把 LLM Agent 从问答推进到真实组学研究流程。
- 可用于哪个表格或图：生命科学 Agent pipeline 对比表；工具调用与自主能力矩阵。
- 适合作为代表性案例吗：适合，但需全文复核后作为强代表。
- 推荐引用强度：核心候选 / 待全文确认。
- 需要在正文中特别引用的页码 / 图 / 表：待全文补充；当前可引用官方仓库和 bioRxiv DOI。
- 需要与哪些论文并列比较：CellVoyager、BioMaster、BioDiscoveryAgent、GeneAgent、OmniCellAgent。

## 9. 总结

### 9.1 一句话概括

空间生物学全流程工具调用 Agent。

### 9.2 速记版 pipeline

1. 输入空间生物学研究目标或数据。
2. Agent 规划分析路径。
3. 调用数据库、文献和空间分析工具。
4. 解释结果并生成假设或 panel 方案。
5. 与人类专家/计算方法比较评估。

### 9.3 标注字段汇总

```text
是否纳入：是
主类：06 生命科学
二级类：06.03 组学、生物信息学与系统生物学
三级类：空间转录组学 / 单细胞空间生物学
四级专题：Biology / omics research agents
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Retrieval-augmented Agent; Hybrid Agent
科研流程角色：实验设计; 文献检索与阅读; 知识抽取与组织; 工具调用与代码执行; 数据分析; 结果解释; 假设生成
自主能力：任务分解; 计划生成; 工具调用; 自主决策; 反馈迭代待复核
验证方式：benchmark; 高通量计算; 专家评估待全文确认
交叉属性：计算驱动; 数据驱动; 多模态; spatial omics
科学贡献类型：系统平台; 数据分析; 假设生成; 实验设计
证据强度：abstract+metadata + official repository，全文 PDF 待复核
归类置信度：高
纳入置信度：中-高
推荐引用强度：核心候选 / 待全文确认
```
