# Yang et al. 2026 - Probe Before You Edit: Probing-Guided Molecular Optimization for LLM Agents in Structure-Based Drug Design

## 2026-06-24 Batch28Partial1 full reaudit revision

```text
paper_id: ASD-0817
supported_modules: 03;07
primary_module_for_filing: 07
object_coverage_mode: multi_module
has_concrete_object_experiments: yes
general_method_bucket: none
source_limited: no
safety_access_status: none
first_hand_source_checked: official arXiv PDF archived locally and checked (`Autonomous Scientific Discovery/Reference_PDF/07_Medical_and_Health_Sciences/Yang_2026_PROBE_Structure_Based_Drug_Design.pdf`)
classification_evidence_source_level: first_hand_full_text_with_local_archived_arxiv_pdf
note_revision_required: yes
archive_status_note: Official arXiv PDF archived locally and checked at `Autonomous Scientific Discovery/Reference_PDF/07_Medical_and_Health_Sciences/Yang_2026_PROBE_Structure_Based_Drug_Design.pdf`.
module_assignment_evidence: Module 03 is supported by pocket-aware molecular optimization and ligand-edit chemistry. Module 07 is supported by explicit structure-based drug-design and target-pocket medicinal objectives. Primary filing in 07 is an archival convenience, not the sole classification fact.
```

**论文信息**
- 标题：Probe Before You Edit: Probing-Guided Molecular Optimization for LLM Agents in Structure-Based Drug Design
- 作者：Zaifei Yang; Weiyu Chen; Yaqing Wang; James Kwok
- 年份：2026
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2606.00555
- PDF / 本地文件路径：official arXiv PDF archived locally and checked at `Autonomous Scientific Discovery/Reference_PDF/07_Medical_and_Health_Sciences/Yang_2026_PROBE_Structure_Based_Drug_Design.pdf`
- 论文类型：研究论文 / structure-based drug-design agent
- 当前状态：to_read
- 阅读日期：2026-06-20
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | abstract; main method | 有 affinity agent、druggability agent、co-optimization agent 的迭代闭环 | 高 |
| 科学对象归类 | supported_modules=`03;07`; primary_module_for_filing=`07` | title; abstract | target-pocket ligand optimization 同时覆盖 chemistry-side molecular optimization 与 structure-based drug-design medical objectives | 高 |
| 2026-06-24 full reaudit | source_limited=`no`; evidence source level=`first_hand_full_text_with_local_archived_arxiv_pdf` | official local arXiv PDF (`Autonomous Scientific Discovery/Reference_PDF/07_Medical_and_Health_Sciences/Yang_2026_PROBE_Structure_Based_Drug_Design.pdf`) | 当前冻结结果是 `03;07`；`07` 仅用于归档便利，不覆盖 `03` 的已支持模块事实；本地 official arXiv PDF 已同步核对 | 高 |
| 方法流程 | probe then edit 的多步优化 | method summary | 先做 pocket-specific site probing，再诱导 EditManual 做定向编辑 | 高 |
| 工具与环境 | 口袋感知分子优化 | abstract + HTML | 围绕 pocket-ligand response 组织局部探测与编辑建议 | 高 |
| 实验验证 | CrossDocked2020 benchmark | experiments | 主要是 benchmark / computational evidence，未见湿实验 | 高 |
| 边界判断 | 不是纯 `07`，也不是 `01.04` | title + abstract | 冻结 adjudication 保留 `03;07`：`07` 来自 structure-based drug design / target-pocket medicinal目标，`03` 来自分子优化与 ligand-edit chemistry 对象覆盖 | 高 |

## 0. 摘要翻译

论文研究结构基础药物设计中的 ligand 迭代优化，指出单步编辑很难同时提升 binding affinity 与 druggability，因此提出 PROBE 框架，通过“先 probe、再 edit”的口袋感知多 Agent 优化流程进行结构基础分子设计。系统围绕特定蛋白口袋和候选配体交互来组织优化，而不是围绕一般化学空间搜索。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：有明确科研目标、多 Agent 协同、局部探测、反馈归纳和多步分子优化
- 判定置信度：高
- 是否面向明确科研目标：是，面向 structure-based drug design
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：是
- 在科研流程中承担的明确角色：假设生成、工具调用、结果评估、协同优化

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：`03;07`
- 覆盖模式：multi_module
- 是否具有具体科学对象实验、验证、benchmark task、case study 或结果报告：是
- 独立 `01.04` 存放区：none
- Primary module for filing：`07`
- Primary module for filing 说明：`07` 只用于 note / archive filing convenience，不覆盖 `03` 这一并行支持模块事实
- 主题路径备注：可归档在 `07.04` structure-based drug-design 子话题下，但同时保留 `03` 的 chemistry / molecular-optimization 对象覆盖
- 每个模块的对象实验证据：`03` 由 pocket-aware molecular optimization、ligand editing 与 co-optimization chemistry object 支持；`07` 由 structure-based drug design、target-pocket medicinal objective、binding affinity / druggability task framing 支持
- 归类理由：论文同时覆盖 chemistry-side molecule editing / optimization 与 medical-side structure-based drug design，对应冻结 adjudication `03;07`
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：ligand optimization against specific protein pockets
- 最终科学问题：如何在结构基础药物设计中更有效地提升 ligand affinity 与 druggability
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：多 Agent 框架只是方法，真正被优化的是 drug-design object

### 2.3 容易混淆的边界

- 可能误归类到：03；01.04
- 最终判定：supported_modules=`03;07`; primary_module_for_filing=`07`
- 判定理由：对象既不是纯通用 chemistry optimization，也不是纯单模块 medical filing；冻结 adjudication 明确保留 chemistry-side `03` 与 drug-design-side `07`
- Multi-module 覆盖说明：`07` 来自 structure-based drug-design / target-pocket medicinal framing，`03` 来自 pocket-aware molecular optimization 与 ligand-edit chemistry；primary filing 仅是归档便利
- 01.04 判定说明：已有具体科学对象实验与 benchmark 结果，因此不进入独立 `01.04` 存放区
- 是否需要二次复核：否

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：否
- Multi-Agent System：是
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：否
- Hybrid Agent：是
- 其他：Pocket-aware drug-design agents

### 3.2 科研流程角色

- 文献检索与阅读：否
- 知识抽取与组织：部分是
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
- 环境交互：是
- 闭环实验：否

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：否
- 实验驱动：否
- 仿真驱动：是
- 多模态：否
- 多尺度建模：是
- 高通量筛选：否
- 知识图谱：否
- 数字孪生：否
- 机器人平台：否
- 其他：structure-based design

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：解决单步分子编辑难以同时优化 affinity 与 druggability 的问题
- 现有科研流程或方法的痛点：传统编辑式方法缺乏针对 pocket response 的细粒度局部探测
- 核心假设或直觉：先 probe 再 edit 可以更好地发现局部结构响应，再引导可控 ligand 优化

### 4.2 系统流程

1. 输入：protein pocket 与候选 ligand
2. 任务分解 / 规划：先做 pocket-specific probing
3. 工具、数据库、模型或实验平台调用：构建 site map、生成 EditManual、调用 affinity / druggability / co-optimization agents
4. 中间结果反馈：局部探测结果和优化指标回流
5. 决策或迭代：多 Agent 协同提出与修正编辑建议
6. 输出：优化后的 ligand candidates

### 4.3 系统组件

- Agent 核心：affinity agent、druggability agent、co-optimization agent
- 工具 / API / 数据库：site map / pocket-aware analysis tools
- 记忆或状态模块：workflow state
- 规划器：co-optimization controller
- 评估器 / verifier：affinity and druggability evaluation
- 人类反馈或专家介入：未强调
- 实验平台或仿真环境：CrossDocked2020

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：否
- 高通量计算：否
- 机器人实验：否
- 湿实验：否
- 临床数据：否
- 真实场景部署：否
- 专家评估：否

### 5.2 数据、任务与指标

- 数据集 / 实验对象：CrossDocked2020
- 任务设置：structure-based ligand optimization
- 对比基线：现有分子编辑 / 优化方法
- 评价指标：affinity、druggability 和综合优化表现
- 关键结果：作者报告 benchmark 上达到更优表现
- 是否有消融实验：有方法组件比较线索
- 是否有失败案例或负结果：未见湿实验或外部验证

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：主要是药物设计优化流程创新
- 科学贡献是否经过验证：是
- 贡献强度判断：中
- 科学贡献类型：系统平台 / 设计 / 预测
- 证据强度：仅 benchmark

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单个分子编辑器，而是口袋感知多 Agent 优化闭环
- 与已有 Agent / 科研智能系统的区别：对 protein-pocket / ligand interaction 的对象锚定更强
- 与同一科学领域其他 Agent 文献的关系：是结构基础药物设计 Agent 的稳定样本
- 主要创新点：把局部探测和编辑建议显式组织为多 Agent 协同流程

## 7. 局限性与风险

- Agent 自主性不足：仍主要在 benchmark / computational setting 中验证
- 科学验证不足：没有湿实验或临床 follow-up
- 泛化性不足：是否能推广到更多 pocket / target 仍待验证
- 工具链依赖：依赖特定口袋分析与评估流程
- 数据泄漏或 benchmark 偏差：CrossDocked 式 benchmark 风险需关注
- 成本、可复现性或安全风险：结构评估与任务设定较依赖具体栈

## 8. 对综述写作的价值

- 可放入哪个章节：07 医学与健康科学 / structure-based drug-design agents
- 可支撑哪个论点：structure-based drug-design Agent 可以同时保留 `03` 与 `07`；primary_module_for_filing=`07` 只是归档便利，不是否定 chemistry-side object coverage
- 可用于哪个表格或图：`07 / 03 / 01.04` 边界表；drug-design agents 表
- 适合作为代表性案例吗：适合
- 推荐引用强度：普通引用
- 需要在正文中特别引用的页码 / 图 / 表：probe-edit loop；CrossDocked evaluation
- 需要与哪些论文并列比较：其他 structure-based molecular optimization agents

## 9. 总结

### 9.1 一句话概括

面向结构基础药物设计的口袋感知多 Agent 优化系统。

### 9.2 速记版 pipeline

1. 读取 pocket 与 ligand
2. 先做局部探测
3. 多 Agent 提出编辑策略
4. 评估 affinity 与 druggability
5. 迭代得到更优候选

### 9.3 标注字段汇总

```text
是否纳入：是
科学对象模块：03;07
覆盖模式：multi_module
是否具有具体科学对象实验：yes
general_method_bucket：none
Primary module for filing：07
是否进入 01.04 存放区：no
其他覆盖模块及对应层级路径：03 = chemistry / molecular optimization; 07 = structure-based drug design
module_assignment_evidence：03 is supported by pocket-aware molecular optimization and ligand-edit chemistry. 07 is supported by explicit structure-based drug-design and target-pocket medicinal objectives.
multi_module_object_coverage_note：Primary filing in 07 is for archive convenience only and does not erase the co-supported chemistry module 03.
classification_evidence_source_level：first_hand_full_text_with_local_archived_arxiv_pdf
source_limited：no
safety_access_status：none
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Multi-Agent System; Hybrid Agent
科研流程角色：hypothesis_generation; simulation_modeling; tool_use_and_code_execution; data_analysis; result_interpretation; evidence_assessment_and_validation; workflow_orchestration
自主能力：task_decomposition; planning; tool_use; feedback_iteration; autonomous_decision_making; multi_agent_collaboration; environment_interaction
验证方式：benchmark
交叉属性：computation_driven; simulation_driven; multiscale_modeling
科学贡献类型：system_platform; design; prediction
证据强度：benchmark_only
归类置信度：高
纳入置信度：高
推荐引用强度：普通引用
```
