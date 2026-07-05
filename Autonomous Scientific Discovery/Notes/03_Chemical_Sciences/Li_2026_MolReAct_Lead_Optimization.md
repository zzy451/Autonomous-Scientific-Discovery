# Li et al. 2026 - Reinforcement Learning with LLM-Guided Action Spaces for Synthesizable Lead Optimization

## 2026-07-05 Phase6NoteRevisionR25 harmonization

- Frozen landing decision: scientific_object_modules=03;07; object_coverage_mode=multi_module; primary_module_for_filing=07; general_method_bucket=none; source_limited=no.
- Current note-status rule: treat this record as already included / landed under the current authoritative pair; older to_read, pending, conservative-hold, or stale single-module / 01.04 shorthand below is superseded by this harmonization.
- Current PDF/source rule: the authoritative local archived PDF is Reference_PDF\07_Medical_and_Health_Sciences\Li_2026_MolReAct_Lead_Optimization.pdf; older pending, abstract-only, no-local-PDF, or stale source_limited=yes wording below is superseded by this harmonization.
## 2026-06-24 Batch28Partial1 full reaudit revision

```text
scientific_object_modules: 03;07
object_coverage_mode: multi_module
has_concrete_object_experiments: yes
general_method_bucket: none
primary_module_for_filing: 07
source_limited: no
safety_access_status: none
first_hand_sources_checked: official arXiv PDF archived locally and checked (`Autonomous Scientific Discovery/Reference_PDF/07_Medical_and_Health_Sciences/Li_2026_MolReAct_Lead_Optimization.pdf`)
classification_evidence_source_level: first_hand_full_text_with_local_archived_arxiv_pdf
note_revision_required: yes
archive_status_note: Official arXiv PDF archived locally and checked at `Autonomous Scientific Discovery/Reference_PDF/07_Medical_and_Health_Sciences/Li_2026_MolReAct_Lead_Optimization.pdf`.
module_assignment_evidence: 03 is supported by reaction templates, reactive sites, feasible synthetic routes, and multi-step synthetic trajectories. 07 is supported by synthesizable lead optimization, docking/TDC drug-discovery tasks, and therapeutic-property objectives.
multi_module_object_coverage_note: The frozen 2026-06-24 result is `03;07` with primary filing in `07`. That filing choice is for archive convenience only and does not erase the chemistry-side module fact.
```

**论文信息**
- 标题：Reinforcement Learning with LLM-Guided Action Spaces for Synthesizable Lead Optimization
- 作者：Tao Li; Kaiyuan Hou; Tuan Vinh; Monika Raj; Zhichun Guo; Carl Yang
- 年份：2026
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2604.07669
- PDF / 本地文件路径：official arXiv PDF archived locally and checked at `Autonomous Scientific Discovery/Reference_PDF/07_Medical_and_Health_Sciences/Li_2026_MolReAct_Lead_Optimization.pdf`
- 论文类型：研究论文 / synthesizable lead-optimization agent
- 当前状态：to_read
- 阅读日期：2026-06-20
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | abstract; HTML | 是 tool-augmented LLM agent + RL，执行 synthesis-constrained multi-step optimization | 高 |
| 科学对象归类 | supported_modules=`03;07`; primary_module_for_filing=`07` | abstract; introduction; tasks | chemistry-side synthesis trajectories 支持 `03`，而 lead optimization / drug-discovery tasks 同时支持 `07` | 高 |
| 2026-06-24 full reaudit | source_limited=`no`; evidence source level=`first_hand_full_text_with_local_archived_arxiv_pdf` | official local arXiv PDF (`Autonomous Scientific Discovery/Reference_PDF/07_Medical_and_Health_Sciences/Li_2026_MolReAct_Lead_Optimization.pdf`) | 当前冻结结果是 `03;07` 且 filing=`07`；该 filing 仅用于归档便利，不覆盖 `03` 的并行模块事实；本地 official arXiv PDF 已同步核对 | 高 |
| 方法流程 | synthesis-constrained MDP | main method | 调用化学工具识别 reactive sites / functional groups，提出模板化转化并做轨迹选择 | 高 |
| 实验验证 | 13 TDC tasks + 1 docking task | experiments | 涉及 DRD2、GSK3_beta、JNK3 等任务，但仍主要是计算 benchmark | 中高 |
| 边界判断 | 不再保持旧的纯 `03 / 03.04` 保守写法 | merged reviewer evidence | 冻结 adjudication 已收敛为 `03;07`，并以 `07` 作为 primary filing；这不是撤销 `03`，而是承认并行多模块事实 | 高 |
| 核心风险 | core-strength risk 高于 class risk | merged evidence | 冻结后类目已确定为 `03;07`；当前残余风险主要是 benchmark-to-real-drug-development 的外推强度，而不是模块是否成立 | 中高 |

## 0. 摘要翻译

论文研究药物发现中的可合成 lead optimization，核心是把 lead refinement 约束到有效反应模板与多步反应轨迹中，避免生成不可合成分子。MolReAct 把任务建模为 synthesis-constrained MDP，由 tool-augmented LLM agent 识别 reactive sites 和 functional groups，再提出模板化转化，并通过 RL 在反应轨迹上进行样本高效优化。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：具有明确科研目标、多步决策、工具调用、轨迹级 RL 优化和反馈更新
- 判定置信度：高
- 是否面向明确科研目标：是，面向 synthesizable lead optimization
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：否
- 在科研流程中承担的明确角色：候选生成、反应位点识别、轨迹选择、结果评估

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
- 主题路径备注：当前 note 仍位于 `03` 文件夹中，但冻结 adjudication 的 primary filing 已是 `07`；真正的分类事实是并行模块 `03;07`
- 每个模块的对象实验证据：`03` 由 reaction templates、reactive sites、functional groups 与 synthesis-constrained multi-step chemical trajectories 支持；`07` 由 synthesizable lead optimization、TDC / docking drug-discovery tasks 与 therapeutic-property objectives 支持
- 归类理由：论文同时覆盖 chemistry-side synthesis-aware optimization 与 medical-side lead-optimization / drug-discovery object coverage，对应冻结 adjudication `03;07`
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：synthesis-constrained molecular / lead optimization trajectories
- 最终科学问题：如何在可合成约束下高效优化候选 lead 的性质
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：tool-augmented RL 是方法，主类仍需按被直接搜索和约束的对象来定

### 2.3 容易混淆的边界

- 可能误归类到：07；01.04
- 最终判定：supported_modules=`03;07`; primary_module_for_filing=`07`
- 判定理由：冻结 adjudication 已明确承认 chemistry-side synthesis object 与 medical-side lead-optimization object 的并行覆盖，不再保留旧的纯 `03 / 03.04` 保守写法
- Multi-module 覆盖说明：`03` 来自反应模板 / 合成轨迹 / chemistry-object optimization，`07` 来自 lead optimization / therapeutic task coverage；primary filing 仅是归档便利
- 01.04 判定说明：已有具体科学对象实验与 benchmark 结果，因此不进入独立 `01.04` 存放区
- 是否需要二次复核：否

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：否
- Multi-Agent System：否
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：否
- Hybrid Agent：是
- 其他：Synthesis-constrained optimization agent

### 3.2 科研流程角色

- 文献检索与阅读：否
- 知识抽取与组织：部分是
- 科学问题提出：否
- 假设生成：是
- 实验设计：否
- 仿真建模：否
- 工具调用与代码执行：是
- 实验执行：否
- 数据分析：是
- 结果解释：部分是
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
- 多 Agent 协作：否
- 环境交互：是
- 闭环实验：否

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 实验驱动：否
- 仿真驱动：否
- 多模态：否
- 多尺度建模：否
- 高通量筛选：是
- 知识图谱：否
- 数字孪生：否
- 机器人平台：否
- 其他：synthesis-aware molecular optimization

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：减少 lead optimization 中生成不可合成候选的问题
- 现有科研流程或方法的痛点：很多分子优化方法忽略反应模板与可合成性约束
- 核心假设或直觉：若把动作空间限制在化学上可执行的模板化转化中，可提高 lead refinement 的质量和实用性

### 4.2 系统流程

1. 输入：初始 lead molecule 与优化目标
2. 任务分解 / 规划：识别 reactive sites 和 functional groups，确定可行模板动作
3. 工具、数据库、模型或实验平台调用：chemical analysis tools + tool-augmented LLM
4. 中间结果反馈：oracle / docking / task scores 回流
5. 决策或迭代：RL 在合成轨迹中选择下一个模板变换
6. 输出：更可合成的优化 lead candidates

### 4.3 系统组件

- Agent 核心：tool-augmented LLM agent + RL controller
- 工具 / API / 数据库：reactive-site / functional-group analysis tools
- 记忆或状态模块：trajectory state
- 规划器：LLM-guided action-space construction
- 评估器 / verifier：TDC / docking task evaluators
- 人类反馈或专家介入：未强调
- 实验平台或仿真环境：Therapeutic Data Commons tasks + docking task

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

- 数据集 / 实验对象：13 TDC tasks + 1 structure-based docking task
- 任务设置：synthesizable lead optimization
- 对比基线：现有 lead / molecular optimization methods
- 评价指标：task performance、样本效率、可合成性约束下的优化表现
- 关键结果：覆盖 DRD2、GSK3_beta、JNK3 等治疗相关任务，表现优于常规基线
- 是否有消融实验：有方法组件对比线索
- 是否有失败案例或负结果：未见湿实验

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：主要是 lead optimization workflow 创新
- 科学贡献是否经过验证：是
- 贡献强度判断：中
- 科学贡献类型：系统平台 / 设计 / 预测
- 证据强度：仅 benchmark

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是一般分子优化，而是带可合成约束和反应模板动作空间的轨迹优化
- 与已有 Agent / 科研智能系统的区别：把 lead optimization 明确约束到化学可执行轨迹上
- 与同一科学领域其他 Agent 文献的关系：是 batch10 中最强的 `03 / 07` 冻结多模块样本之一
- 主要创新点：用 LLM 引导动作空间，再用 RL 在可合成轨迹上做 lead refinement

## 7. 局限性与风险

- Agent 自主性不足：仍主要停留在计算 benchmark
- 科学验证不足：没有湿实验或真实药物开发 follow-up
- 泛化性不足：对象边界受 task mix 影响较大
- 工具链依赖：依赖模板化化学分析工具
- 数据泄漏或 benchmark 偏差：TDC 任务构成会强烈影响主类解读
- 成本、可复现性或安全风险：方法有效性高度依赖评测设定

## 8. 对综述写作的价值

- 可放入哪个章节：03/07 交叉案例；或按归档便利放入 07 药物发现 Agent 小节并交叉引用 chemistry-side lead optimization
- 可支撑哪个论点：`03 / 07` 边界不能只看标题中的 drug discovery 语境，也不能只看化学动作空间；冻结结果允许二者并行成立
- 可用于哪个表格或图：`03 / 07 / 01.04` 边界表；lead optimization agents 表
- 适合作为代表性案例吗：适合做边界样本
- 推荐引用强度：普通引用
- 需要在正文中特别引用的页码 / 图 / 表：action-space design；TDC task setup；discussion
- 需要与哪些论文并列比较：MolMem、SEISMO、其他 lead-optimization agents

## 9. 总结

### 9.1 一句话概括

用 LLM 引导可合成动作空间的 lead 优化 Agent。

### 9.2 速记版 pipeline

1. 读入 lead 分子和目标
2. 识别可反应位点
3. 构造模板化动作空间
4. 用 RL 选择下一步变换
5. 迭代得到更优且可合成的候选

### 9.3 标注字段汇总

```text
是否纳入：是
科学对象模块：03;07
覆盖模式：multi_module
是否具有具体科学对象实验：yes
general_method_bucket：none
Primary module for filing：07
是否进入 01.04 存放区：no
其他覆盖模块及对应层级路径：03 = synthesis-aware chemistry optimization; 07 = lead optimization / drug discovery
module_assignment_evidence：03 is supported by reaction templates, reactive sites, feasible synthetic routes, and multi-step synthetic trajectories. 07 is supported by synthesizable lead optimization, docking/TDC drug-discovery tasks, and therapeutic-property objectives.
multi_module_object_coverage_note：The frozen 2026-06-24 result is `03;07` with primary filing in `07`. That filing choice is for archive convenience only and does not erase the chemistry-side module fact.
classification_evidence_source_level：first_hand_full_text_with_local_archived_arxiv_pdf
source_limited：no
safety_access_status：none
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Hybrid Agent
科研流程角色：hypothesis_generation; tool_use_and_code_execution; data_analysis; evidence_assessment_and_validation; workflow_orchestration
自主能力：task_decomposition; planning; tool_use; feedback_iteration; autonomous_decision_making; environment_interaction
验证方式：benchmark
交叉属性：computation_driven; data_driven; high_throughput_screening
科学贡献类型：system_platform; design; prediction
证据强度：benchmark_only
归类置信度：中
纳入置信度：高
推荐引用强度：普通引用
```
