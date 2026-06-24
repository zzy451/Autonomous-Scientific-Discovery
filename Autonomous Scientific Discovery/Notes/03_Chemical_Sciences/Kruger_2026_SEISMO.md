# Kruger et al. 2026 - SEISMO: Increasing Sample Efficiency in Molecular Optimization with a Trajectory-Aware LLM Agent

## 2026-06-24 Batch28Partial1 full reaudit revision

```text
paper_id: ASD-0819
supported_modules: 03;07
primary_module_for_filing: 03
object_coverage_mode: multi_module
has_concrete_object_experiments: yes
general_method_bucket: none
source_limited: no
safety_access_status: none
first_hand_source_checked: official arXiv PDF archived locally and checked (`Autonomous Scientific Discovery/Reference_PDF/03_Chemical_Sciences/Kruger_2026_SEISMO.pdf`)
classification_evidence_source_level: first_hand_full_text_with_local_archived_arxiv_pdf
note_revision_required: yes
archive_status_note: Official arXiv PDF archived locally and checked at `Autonomous Scientific Discovery/Reference_PDF/03_Chemical_Sciences/Kruger_2026_SEISMO.pdf`.
module_assignment_evidence: Module 03 is supported by molecule-centric online optimization trajectories and chemistry-object property search. Module 07 is supported by medicinal-chemistry and drug-discovery-oriented optimization tasks. Primary filing in 03 is an archival convenience, not the sole classification fact.
```

**论文信息**
- 标题：SEISMO: Increasing Sample Efficiency in Molecular Optimization with a Trajectory-Aware LLM Agent
- 作者：Fabian P. Kruger; Andrea Hunklinger; Adrian Wolny; Tim J. Adler; Igor Tetko; Santiago David Villalba
- 年份：2026
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2602.00663
- PDF / 本地文件路径：official arXiv PDF archived locally and checked at `Autonomous Scientific Discovery/Reference_PDF/03_Chemical_Sciences/Kruger_2026_SEISMO.pdf`
- 论文类型：研究论文 / trajectory-aware molecular-optimization agent
- 当前状态：to_read
- 阅读日期：2026-06-20
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | abstract; HTML | 是 online inference-time molecular optimization LLM agent，逐步接收 oracle feedback | 高 |
| 科学对象归类 | supported_modules=`03;07`; primary_module_for_filing=`03` | abstract; task framing | 分子优化主对象支持 `03`，而 medicinal / drug-discovery-oriented task coverage 额外支持 `07` | 高 |
| 2026-06-24 full reaudit | source_limited=`no`; evidence source level=`first_hand_full_text_with_local_archived_arxiv_pdf` | official local arXiv PDF (`Autonomous Scientific Discovery/Reference_PDF/03_Chemical_Sciences/Kruger_2026_SEISMO.pdf`) | 当前冻结结果是 `03;07`；`03` 仅作为归档主路径，不覆盖 `07` 的并行模块事实；本地 official arXiv PDF 已同步核对 | 高 |
| 方法流程 | 轨迹条件化多步决策 | HTML | proposal 依赖 full optimization trajectory、task description、scores 与 optional explanation | 高 |
| 实验验证 | PMO benchmark 23 tasks | HTML | 报告 2-3x AUC 提升，常在 50 oracle calls 内接近最优 | 高 |
| 边界判断 | 不是纯 `03`，也不是 `01.04` | task mix | molecule-centric optimization 支持 `03`，而 medicinal-chemistry / drug-discovery task mix 也支持 `07`；冻结 adjudication 因此保留 `03;07` | 高 |
| 核心风险 | class risk | summary | 不确定点主要是 pharma relevance 是否足以把对象推向药物发现侧 | 中 |

## 0. 摘要翻译

SEISMO 关注昂贵 oracle 下的样本高效分子优化，提出一个基于完整优化轨迹和解释反馈的在线 LLM Agent。系统在每次 oracle call 后都会更新，用完整 trajectory、自然语言任务描述、标量分数和可选解释反馈来生成下一轮 proposal，目标是在较少调用次数下完成更高效的分子性质优化。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：有明确科研目标、多轮 proposal、持续 oracle 交互和反馈更新
- 判定置信度：高
- 是否面向明确科研目标：是，面向 sample-efficient molecular optimization
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：部分是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：否
- 在科研流程中承担的明确角色：候选生成、轨迹级决策、反馈利用、结果评估

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
- Primary module for filing：`03`
- Primary module for filing 说明：`03` 只用于 note / archive filing convenience，不覆盖 `07` 这一并行支持模块事实
- 主题路径备注：可归档在 `03.04` molecular-optimization 子话题下，但同时保留 `07` 的 medicinal / drug-discovery task coverage
- 每个模块的对象实验证据：`03` 由在线 molecule-centric optimization、property search 与 trajectory-aware chemistry-object optimization 支持；`07` 由 medicinal-chemistry / drug-discovery-oriented optimization tasks 支持
- 归类理由：论文同时覆盖 chemistry-side molecular optimization 与 medical-side drug-discovery task framing，对应冻结 adjudication `03;07`
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：online molecular optimization
- 最终科学问题：如何利用完整优化轨迹与解释反馈提升分子优化样本效率
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：trajectory-aware LLM agent 是方法，优化对象仍是分子和性质目标

### 2.3 容易混淆的边界

- 可能误归类到：07；01.04
- 最终判定：supported_modules=`03;07`; primary_module_for_filing=`03`
- 判定理由：虽然 paper 仍以 molecule-centric optimization 为主，但 medicinal-chemistry / drug-discovery task coverage 也已达到冻结多模块阈值
- Multi-module 覆盖说明：`03` 来自 chemistry-side molecule / property optimization，`07` 来自 drug-discovery-oriented task coverage；primary filing 仅是归档便利
- 01.04 判定说明：已有具体分子优化任务与结果，因此不进入独立 `01.04` 存放区
- 是否需要二次复核：否

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：部分是
- Tool-using Agent：是
- Retrieval-augmented Agent：否
- Multi-Agent System：否
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：否
- Hybrid Agent：是
- 其他：Trajectory-aware optimization agent

### 3.2 科研流程角色

- 文献检索与阅读：否
- 知识抽取与组织：否
- 科学问题提出：否
- 假设生成：是
- 实验设计：否
- 仿真建模：否
- 工具调用与代码执行：否
- 实验执行：否
- 数据分析：是
- 结果解释：部分是
- 证据评估与验证：是
- 论文写作：否
- 端到端科研流程自动化：是

### 3.3 自主能力

- 任务分解：部分是
- 计划生成：部分是
- 工具调用：是
- 记忆与状态维护：是
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
- 其他：oracle-guided optimization

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：提升昂贵 oracle 下的 sample efficiency
- 现有科研流程或方法的痛点：很多方法不能充分利用完整 trajectory 和解释反馈
- 核心假设或直觉：让 LLM 看到 full optimization trajectory，可做更稳定的 sequential proposal

### 4.2 系统流程

1. 输入：初始分子、优化任务和当前 trajectory
2. 任务分解 / 规划：根据已有 trajectory 组织下一步 proposal
3. 工具、数据库、模型或实验平台调用：调用 oracle 返回新分数和可选解释
4. 中间结果反馈：将 score 和 explanation 并入 trajectory
5. 决策或迭代：继续在线更新并提出新候选
6. 输出：更样本高效的优化分子

### 4.3 系统组件

- Agent 核心：trajectory-aware LLM controller
- 工具 / API / 数据库：molecular optimization oracle
- 记忆或状态模块：full optimization trajectory
- 规划器：trajectory-conditioned prompting
- 评估器 / verifier：oracle scores
- 人类反馈或专家介入：否
- 实验平台或仿真环境：PMO benchmark

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

- 数据集 / 实验对象：Practical Molecular Optimization benchmark；23 tasks
- 任务设置：online molecular optimization
- 对比基线：现有分子优化方法
- 评价指标：AUC、oracle efficiency、time-to-near-optimum
- 关键结果：报告 2-3x AUC 提升，且常在 50 oracle calls 内接近最优
- 是否有消融实验：有任务与设置比较线索
- 是否有失败案例或负结果：未见外部实验验证

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：主要是分子优化 agent 设计创新
- 科学贡献是否经过验证：是
- 贡献强度判断：中
- 科学贡献类型：系统平台 / 设计 / 预测
- 证据强度：仅 benchmark

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是静态分子生成，而是在线 trajectory-aware optimization
- 与已有 Agent / 科研智能系统的区别：强调 full trajectory 作为决策上下文
- 与同一科学领域其他 Agent 文献的关系：是 `03 / 07` 多模块边界样本，当前归档主路径为 `03`
- 主要创新点：将 trajectory 和记分解释直接纳入 LLM 决策链

## 7. 局限性与风险

- Agent 自主性不足：主要在 benchmark 内运作
- 科学验证不足：缺少湿实验或真实药物开发 follow-up
- 泛化性不足：药物语境是否足以改变主类仍有争议
- 工具链依赖：强依赖 oracle 反馈质量
- 数据泄漏或 benchmark 偏差：PMO 任务构成会影响边界解读
- 成本、可复现性或安全风险：评测条件变化可能明显影响结果

## 8. 对综述写作的价值

- 可放入哪个章节：03 化学科学 / molecular optimization agents
- 可支撑哪个论点：即使 paper 更偏 molecule-centric optimization，也可能因 drug-discovery task coverage 同时支持 `07`；primary_module_for_filing=`03` 不等于排除 `07`
- 可用于哪个表格或图：`03 / 07 / 01.04` 边界表；online optimization agents 表
- 适合作为代表性案例吗：适合作为边界案例
- 推荐引用强度：普通引用
- 需要在正文中特别引用的页码 / 图 / 表：trajectory conditioning；PMO results
- 需要与哪些论文并列比较：MolMem、MolReAct

## 9. 总结

### 9.1 一句话概括

用完整优化轨迹提升分子优化样本效率的 LLM Agent。

### 9.2 速记版 pipeline

1. 读入当前分子与任务
2. 利用完整 trajectory 生成新候选
3. 调用 oracle 得分
4. 把反馈并回 trajectory
5. 继续在线优化

### 9.3 标注字段汇总

```text
是否纳入：是
科学对象模块：03;07
覆盖模式：multi_module
是否具有具体科学对象实验：yes
general_method_bucket：none
Primary module for filing：03
是否进入 01.04 存放区：no
其他覆盖模块及对应层级路径：03 = molecule-centric optimization; 07 = medicinal / drug-discovery task coverage
module_assignment_evidence：03 is supported by online molecular optimization trajectories and chemistry-object property search. 07 is supported by medicinal-chemistry and drug-discovery-oriented optimization tasks.
multi_module_object_coverage_note：Primary filing in 03 is for archive convenience only and does not erase the co-supported medical/drug-discovery module 07.
classification_evidence_source_level：first_hand_full_text_with_local_archived_arxiv_pdf
source_limited：no
safety_access_status：none
Agent 类型：LLM Agent; Tool-using Agent; Hybrid Agent
科研流程角色：hypothesis_generation; data_analysis; evidence_assessment_and_validation; workflow_orchestration
自主能力：planning; tool_use; memory_or_state_tracking; feedback_iteration; autonomous_decision_making; environment_interaction
验证方式：benchmark
交叉属性：computation_driven; data_driven; high_throughput_screening
科学贡献类型：system_platform; design; prediction
证据强度：benchmark_only
归类置信度：中
纳入置信度：高
推荐引用强度：普通引用
```
