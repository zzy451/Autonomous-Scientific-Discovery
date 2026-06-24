# Kim et al. 2026 - CoDaS: AI Co-Data-Scientist for Biomarker Discovery via Wearable Sensors

## 2026-06-24 Batch28Partial1 full reaudit revision

```text
paper_id: ASD-0815
supported_modules: 07
primary_module_for_filing: 07
object_coverage_mode: single_module
has_concrete_object_experiments: yes
general_method_bucket: none
source_limited: no
safety_access_status: none
first_hand_source_checked: official arXiv PDF archived locally and checked (`Autonomous Scientific Discovery/Reference_PDF/07_Medical_and_Health_Sciences/Kim_2026_CoDaS.pdf`)
classification_evidence_source_level: first_hand_full_text_with_local_archived_arxiv_pdf
note_revision_required: yes
archive_status_note: The canonical title is `CoDaS: AI Co-Data-Scientist for Biomarker Discovery via Wearable Sensors`. Official arXiv PDF archived locally and checked at `Autonomous Scientific Discovery/Reference_PDF/07_Medical_and_Health_Sciences/Kim_2026_CoDaS.pdf`.
module_assignment_evidence: Wearable-sensor biomarker-discovery experiments on mental-health and metabolic-health cohorts support module 07.
```

**论文信息**
- 标题：CoDaS: AI Co-Data-Scientist for Biomarker Discovery via Wearable Sensors
- 作者：Yubin Kim; Salman Rahman; Samuel Schmidgall; Chunjong Park; A. Ali Heydari; Ahmed A. Metwally; Hong Yu; Xin Liu; Xuhai Xu; Yuzhe Yang; Maxwell A. Xu; Zhihan Zhang; Cynthia Breazeal; Tim Althoff; Petar Sirkovic; Ivor Rendulic; Annalisa Pawlosky; Nicolas Stroppa; Juraj Gottweis; Elahe Vedadi; Alan Karthikesalingam; Pushmeet Kohli; Vivek Natarajan; Mark Malhotra; Shwetak Patel; Hae Won Park; Hamid Palangi; Daniel McDuff
- 年份：2026
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2604.14615
- PDF / 本地文件路径：official arXiv PDF archived locally and checked at `Autonomous Scientific Discovery/Reference_PDF/07_Medical_and_Health_Sciences/Kim_2026_CoDaS.pdf`
- 论文类型：研究论文 / wearable biomarker-discovery multi-agent system
- 当前状态：to_read
- 阅读日期：2026-06-20
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | arXiv abstract + HTML | 多 Agent 六阶段流程覆盖数据画像、假设生成、统计/ML 分析、对抗验证和报告综合 | 高 |
| 科学对象归类 | supported_modules=`07`; primary_module_for_filing=`07` | abstract; main experiments | wearable-sensor-derived digital biomarkers for depression and metabolic-health endpoints 直接支持模块 07 | 高 |
| 2026-06-24 full reaudit | source_limited=`no`; evidence source level=`first_hand_full_text_with_local_archived_arxiv_pdf` | official local arXiv PDF (`Autonomous Scientific Discovery/Reference_PDF/07_Medical_and_Health_Sciences/Kim_2026_CoDaS.pdf`) | 当前写回已与 official arXiv PDF 本地归档路径同步并核对；标题仍统一为正式题名 `CoDaS: AI Co-Data-Scientist for Biomarker Discovery via Wearable Sensors` | 高 |
| 方法流程 | iterative six-phase loop | main text | 有 hypothesis generation、adversarial validation、mechanistic reasoning、report synthesis 和人工监督 | 高 |
| 实验验证 | 3 个健康 cohort、9,279 observations | main text | 发现 mental-health 与 metabolic-health 候选 biomarkers，并做 11 项内部稳健性检查 | 高 |
| 边界判断 | 不应移入 `07.04` 或 `01.04` | abstract + experiments | 重点不是药物/靶点/治疗，而是数字健康 biomarker discovery | 高 |
| 科学贡献 | 主要是健康 biomarker discovery workflow | full text summary | 结果仍是 exploratory / hypothesis-generating，需 prospective validation | 高 |

## 0. 摘要翻译

论文提出 CoDaS，一个面向可穿戴传感器数字生物标志物发现的多 Agent 系统。作者把数字健康中的 biomarker discovery 组织成多步 agentic 流程：从数据画像、候选假设生成，到统计与机器学习分析、对抗式验证、机理解释和报告综合。系统在三个健康相关人群队列上运行，目标覆盖抑郁相关表型和代谢健康表型，输出具体数字生物标志物候选。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：存在多 Agent 架构、明确的多步科研流程、统计工具/验证环节和人工监督
- 判定置信度：高
- 是否面向明确科研目标：是，面向 wearable-derived health biomarkers
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：是
- 在科研流程中承担的明确角色：假设生成、数据分析、证据评估、机理解释、报告综合

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：`07`
- 覆盖模式：single_module
- 是否具有具体科学对象实验、验证、benchmark task、case study 或结果报告：是
- 独立 `01.04` 存放区：none
- Primary module for filing：`07`
- Primary module for filing 说明：此处 filing 与模块事实一致，但 filing 字段仍只是归档便利字段
- 主题路径备注：可放在 `07.03` digital health / biomarker 子话题下讨论，但这不是新增 scientific-object module
- 每个模块的对象实验证据：`07` 由 wearable physiological signals、mental-health cohorts 与 metabolic-health cohorts 上的 biomarker-discovery experiments 支持
- 归类理由：最终对象是健康科学中的数字生物标志物，而不是药物发现或通用科研平台
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：digital biomarkers from wearable physiological signals
- 最终科学问题：如何用多 Agent 系统从可穿戴数据中提出、筛选和验证健康相关 biomarker
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：agentic 系统只是执行形式，主对象和输出都属于健康科学对象

### 2.3 容易混淆的边界

- 可能误归类到：07.04；01.04
- 最终判定：supported_modules=`07`; primary_module_for_filing=`07`
- 判定理由：论文不围绕药物、靶点或治疗设计，而是围绕数字健康 biomarker discovery；冻结 adjudication 只支持模块 `07`
- Multi-module 覆盖说明：不适用；当前冻结结果不是多模块
- 01.04 判定说明：已有具体健康对象实验与 cohort 结果，因此不进入独立 `01.04` 存放区
- 是否需要二次复核：否

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：部分是
- Multi-Agent System：是
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：是
- Hybrid Agent：是
- 其他：Digital health biomarker-discovery agents

### 3.2 科研流程角色

- 文献检索与阅读：部分是
- 知识抽取与组织：是
- 科学问题提出：部分是
- 假设生成：是
- 实验设计：否
- 仿真建模：否
- 工具调用与代码执行：是
- 实验执行：否
- 数据分析：是
- 结果解释：是
- 证据评估与验证：是
- 论文写作：是
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
- 数据驱动：是
- 实验驱动：否
- 仿真驱动：否
- 多模态：是
- 多尺度建模：否
- 高通量筛选：否
- 知识图谱：否
- 数字孪生：否
- 机器人平台：否
- 其他：digital health

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：减少数字健康 biomarker discovery 中从数据到候选物的人工探索成本
- 现有科研流程或方法的痛点：候选提出、统计验证、机理解释和结果综合往往分散在多个步骤和多类工具中
- 核心假设或直觉：让多 Agent 分担不同科研角色，可更高效地产生和筛选数字生物标志物

### 4.2 系统流程

1. 输入：wearable physiological signals and cohort metadata
2. 任务分解 / 规划：先做数据画像，再提出 biomarker hypotheses
3. 工具、数据库、模型或实验平台调用：统计分析、ML、对抗式验证和机理解释模块
4. 中间结果反馈：validation battery 和 critic/defender 结果回流
5. 决策或迭代：继续筛选、强化或放弃候选 biomarker
6. 输出：mental-health 与 metabolic-health biomarker candidates

### 4.3 系统组件

- Agent 核心：multi-agent six-phase workflow
- 工具 / API / 数据库：statistical / ML analysis and validation stack
- 记忆或状态模块：workflow state
- 规划器：agentic orchestrator
- 评估器 / verifier：11-check validation battery
- 人类反馈或专家介入：有 checkpoints 和 final review
- 实验平台或仿真环境：3 个健康 cohort

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：否
- 高通量计算：否
- 机器人实验：否
- 湿实验：否
- 临床数据：是
- 真实场景部署：否
- 专家评估：是

### 5.2 数据、任务与指标

- 数据集 / 实验对象：3 个健康 cohort；9,279 participant-observations
- 任务设置：depression-related and metabolic-health biomarker discovery
- 对比基线：内部多环节验证与常规分析流程
- 评价指标：replication、stability、robustness、discriminative power 等 11 项检查
- 关键结果：发现 41 个 mental-health 候选 biomarker 与 25 个 metabolic 候选
- 是否有消融实验：未见完整系统消融
- 是否有失败案例或负结果：作者明确称结果仍是 hypothesis-generating

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：提出健康相关 biomarker hypotheses
- 科学贡献是否经过验证：部分是
- 贡献强度判断：中
- 科学贡献类型：系统平台 / 假设 / 数据分析
- 证据强度：专家确认

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单个预测模型，而是多步 biomarker discovery workflow
- 与已有 Agent / 科研智能系统的区别：明确把健康 biomarker discovery 拆成多角色 agent 流程
- 与同一科学领域其他 Agent 文献的关系：是数字健康与 wearable biomarker discovery 的代表样本
- 主要创新点：以多 Agent 闭环组织健康 biomarker discovery，并把 validation battery 放进工作流内部

## 7. 局限性与风险

- Agent 自主性不足：保留人工监督与终审
- 科学验证不足：未做前瞻性外部临床验证
- 泛化性不足：验证仍集中于有限 cohort
- 工具链依赖：依赖统计/ML 与 validation pipeline
- 数据泄漏或 benchmark 偏差：内部验证型结果仍可能受 cohort 偏差影响
- 成本、可复现性或安全风险：真实临床 / 监管适用性仍弱

## 8. 对综述写作的价值

- 可放入哪个章节：07 医学与健康科学 / digital health biomarker agents
- 可支撑哪个论点：只要最终对象是健康科学中的 biomarkers，就不应因方法叙事强而退回 `01.04`
- 可用于哪个表格或图：数字健康 Agent 表；`07.03 / 07.04 / 01.04` 边界表
- 适合作为代表性案例吗：适合
- 推荐引用强度：普通引用
- 需要在正文中特别引用的页码 / 图 / 表：six-phase loop；validation battery；cohort results
- 需要与哪些论文并列比较：其他医学 biomarker discovery agents

## 9. 总结

### 9.1 一句话概括

面向可穿戴数字生物标志物发现的多 Agent 系统。

### 9.2 速记版 pipeline

1. 读入可穿戴健康数据
2. 生成 biomarker 候选
3. 做统计与 ML 分析
4. 进行对抗验证与机理解释
5. 输出候选与报告

### 9.3 标注字段汇总

```text
是否纳入：是
科学对象模块：07
覆盖模式：single_module
是否具有具体科学对象实验：yes
general_method_bucket：none
Primary module for filing：07
是否进入 01.04 存放区：no
其他覆盖模块及对应层级路径：none
module_assignment_evidence：Wearable-sensor biomarker-discovery experiments on mental-health and metabolic-health cohorts support module 07.
multi_module_object_coverage_note：Single-module medical filing matches the frozen classification fact for ASD-0815.
classification_evidence_source_level：first_hand_full_text_with_local_archived_arxiv_pdf
source_limited：no
safety_access_status：none
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Multi-Agent System; Human-in-the-loop Agent; Hybrid Agent
科研流程角色：hypothesis_generation; tool_use_and_code_execution; data_analysis; result_interpretation; evidence_assessment_and_validation; paper_writing; workflow_orchestration
自主能力：task_decomposition; planning; tool_use; feedback_iteration; autonomous_decision_making; multi_agent_collaboration; environment_interaction
验证方式：benchmark; clinical_data; expert_evaluation
交叉属性：computation_driven; data_driven; multimodal
科学贡献类型：system_platform; hypothesis
证据强度：expert_confirmed
归类置信度：高
纳入置信度：高
推荐引用强度：普通引用
```
