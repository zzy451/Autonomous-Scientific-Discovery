# Jiang et al. 2026 - GALILEO: Embodied AI scientist for autonomous therapeutic discovery in dynamic membrane systems

## 2026-06-23 Batch16 partial-9 closeout

This round closes the record as source-limited `06;07` with `07` primary.

```text
scientific_object_modules: 06;07
object_coverage_mode: multi_module
general_method_bucket: none
primary_module_for_filing: 07
first_hand_sources_checked: local PDF search; Crossref DOI abstract metadata; DOI resolver header; official https bioRxiv DOI landing; HighWire https DOI endpoint
classification_evidence_source_level: first_hand_abstract_or_landing_page
source_limited_reason: no local PDF was found; the DOI resolver redirected through an unsafe http bioRxiv hop that was not followed; official https bioRxiv landing returned 403; HighWire https endpoint also returned 403
safety_access_status: blocked unsafe/403 access trail is visible, but safe Crossref abstract metadata remained available, so this is source-limited rather than full safety-skip
module_assignment_evidence: therapeutic peptide discovery, anti-tumor immune activation, and validation outcomes support `07`; membrane-system biology, LRRC8C / SLC25A1 target evidence, citrate-export metabolism, and CD8+ T-cell functional evidence support `06`
```

**论文信息**
- 标题：GALILEO: Embodied AI scientist for autonomous therapeutic discovery in dynamic membrane systems
- 作者：Jiang et al.
- 年份：2026
- 来源 / venue：Research Square Preprint
- DOI / arXiv / URL：https://doi.org/10.64898/2026.06.10.731360
- PDF / 本地文件路径：当前未保存本地 PDF；本笔记基于 Crossref 官方摘要
- 论文类型：研究论文 / embodied AI scientist
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

## 2026-06-20 relaxed multi-module revision

This section supplements the older `07.04` primary filing with object-coverage modules.

```text
scientific_object_modules: 06;07
object_coverage_mode: multi_module
has_concrete_object_experiments: yes
general_method_bucket: none
primary_module_for_filing: 07
first_hand_sources_checked: Crossref DOI abstract / bioRxiv DOI metadata
classification_evidence_source_level: first_hand_abstract_or_landing_page
module_assignment_evidence: `07` is supported by therapeutic peptide discovery and intervention-oriented validation; `06` is supported by membrane biology, immune-cell functional assays, LRRC8C/SLC25A1 targets, and T-cell function evidence.
multi_module_object_coverage_note: The medical endpoint remains primary for filing, but the wet-lab membrane/cell biology experiments are concrete life-science object evidence under the relaxed rule.
```

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | Crossref abstract | 明确有 `Observation-Thought-Action-Summary (OTAS)` reasoning loop | 高 |
| 科学对象归类 | `07.04` | Crossref abstract | 目标是 `therapeutic peptide discovery` 与 membrane-blocker intervention | 高 |
| 方法流程 | 机器人合成 + 表型反馈 | Crossref abstract | 结合 robotic peptide synthesis、multimodal phenotyping 和 wet-lab feedback | 高 |
| 实验验证 | 湿实验支持 | Crossref abstract | 通过电流阻断、代谢扰动、T-cell activation 等结果验证 | 高 |
| 边界判断 | 不转 `06` / `01.04` | Crossref abstract | 核心不是一般膜生物学平台，而是可干预治疗发现 | 高 |

## 0. 摘要翻译

GALILEO 被描述为一个面向动态膜系统自主治疗发现的 embodied AI scientist。与一般 AI scientist 不同，它把 OTAS 推理循环与机器人肽合成、多模态表型分析以及湿实验反馈结合起来。系统从临床启发的肽先验中检索候选，再通过可审计编辑操作优化序列，并利用湿实验反馈更新靶点信念、序列策略、实验选择与机制假设。当前官方摘要给出的结果已经明确落在 therapeutic peptide discovery 与可迁移膜阻断规则上，因此其稳定对象在 `07.04`。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：具备多步推理、工具调用、实验执行、反馈迭代和自主更新机制
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：摘要未明确
- 在科研流程中承担的明确角色：候选检索、肽编辑、实验规划、湿实验反馈整合、机制假设更新

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：07
- 二级类：07.04
- 三级类：therapeutic peptide discovery
- 四级专题：embodied therapeutic discovery agents
- 四级专题是否为新增：否
- 归类理由：最终对象是治疗肽发现与肿瘤相关膜靶点干预，不是一般生命机制探索
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：therapeutic peptides / membrane-targeted interventions
- 最终科学问题：如何自主发现并验证具有治疗潜力的膜系统干预肽
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：OTAS、retrieval-and-editing 和 embodied loop 是手段，稳定科学对象是治疗发现

### 2.3 容易混淆的边界

- 可能误归类到：06.03；01.04
- 最终判定：保留 07.04
- 判定理由：摘要持续强调 therapeutic discovery、tumor-dependent T-cell activation 和 intervention，而不是一般 omics / membrane biology 平台
- 是否需要二次复核：是，后续可补全文确认临床转化深度

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：是
- Multi-Agent System：未见明确证据
- Robot / Embodied Agent：是
- Human-in-the-loop Agent：未见明确证据
- Hybrid Agent：是
- 其他：OTAS reasoning loop

### 3.2 科研流程角色

- 文献检索与阅读：否
- 知识抽取与组织：部分是
- 科学问题提出：部分是
- 假设生成：是
- 实验设计：是
- 仿真建模：部分是
- 工具调用与代码执行：是
- 实验执行：是
- 数据分析：是
- 结果解释：是
- 证据评估与验证：是
- 论文写作：否
- 端到端科研流程自动化：是

### 3.3 自主能力

- 任务分解：是
- 计划生成：是
- 工具调用：是
- 记忆与状态维护：是
- 反馈迭代：是
- 自主决策：是
- 多 Agent 协作：未见明确证据
- 环境交互：是
- 闭环实验：是

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 实验驱动：是
- 仿真驱动：部分是
- 多模态：是
- 多尺度建模：否
- 高通量筛选：否
- 知识图谱：否
- 数字孪生：否
- 机器人平台：是
- 其他：peptide prior retrieval

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：弥合 therapeutic prediction 与 wet-lab intervention 之间的 gap
- 现有科研流程或方法的痛点：传统治疗肽发现难以把推理、合成、表型和机制更新打通
- 核心假设或直觉：把 reasoning loop 与 embodied wet-lab 平台联通，可以形成可审计、可迁移的治疗发现闭环

### 4.2 系统流程

1. 输入：动态膜系统中的 therapeutic discovery task
2. 任务分解 / 规划：通过 OTAS 循环形成观测、思考、行动与总结
3. 工具、数据库、模型或实验平台调用：从 clinically informed peptide prior 检索候选，并调用 robotic synthesis / phenotyping
4. 中间结果反馈：湿实验反馈更新 target beliefs、sequence policies、assay choices、mechanism hypotheses
5. 决策或迭代：继续筛选和编辑候选肽
6. 输出：具有功能验证的治疗肽与可迁移机制规则

### 4.3 系统组件

- Agent 核心：GALILEO
- 工具 / API / 数据库：clinically informed peptide prior、robotic peptide synthesis、multimodal phenotyping
- 记忆或状态模块：target beliefs / sequence policies
- 规划器：OTAS reasoning loop
- 评估器 / verifier：wet-lab functional readouts
- 人类反馈或专家介入：摘要未展开
- 实验平台或仿真环境：机器人肽合成与多模态表型系统

## 5. 实验与验证

### 5.1 验证方式

- benchmark：否
- 仿真验证：部分是
- 高通量计算：否
- 机器人实验：是
- 湿实验：是
- 临床数据：否
- 真实场景部署：否
- 专家评估：否

### 5.2 数据、任务与指标

- 数据集 / 实验对象：LRRC8C、SLC25A1 等膜系统相关治疗肽发现任务
- 任务设置：自主检索、编辑、合成并验证候选治疗肽
- 对比基线：摘要未展开
- 评价指标：currents blocking、metabolic perturbation、tumor-dependent T-cell activation、CD8+ T-cell function 等
- 关键结果：生成肽能阻断 LRRC8C 电流、扰动代谢并提升 T-cell 功能
- 是否有消融实验：摘要未展开
- 是否有失败案例或负结果：摘要未展开

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：是，发现并验证了新的 therapeutic peptide interventions
- 科学贡献是否经过验证：有湿实验反馈与功能读出支持
- 贡献强度判断：强
- 科学贡献类型：design / hypothesis / experimental_discovery / system_platform
- 证据强度：实验验证

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是静态预测器，而是把 reasoning、实验和机制更新闭环化
- 与已有 Agent / 科研智能系统的区别：强调 embodied wet-lab loop 与 auditable peptide editing
- 与同一科学领域其他 Agent 文献的关系：可与 MADD、IMMUNIA、Medea 等治疗发现 / 生物医药 Agent 对比
- 主要创新点：把 AI scientist 真正推进到治疗肽发现的实验闭环

## 7. 局限性与风险

- Agent 自主性不足：仍需全文确认人类监控与实验异常处理比例
- 科学验证不足：当前判断仍主要基于摘要
- 泛化性不足：是否能稳定迁移到更多靶点家族仍待全文确认
- 工具链依赖：依赖机器人合成与多模态表型平台
- 数据泄漏或 benchmark 偏差：不是主要风险
- 成本、可复现性或安全风险：实验与候选肽评估成本较高

## 8. 对综述写作的价值

- 可放入哪个章节：07 医学与健康科学
- 可支撑哪个论点：治疗发现 Agent 已经能形成 reasoning-to-intervention 的实验闭环
- 可用于哪个表格或图：therapeutic-discovery agent comparison
- 适合作为代表性案例吗：适合
- 推荐引用强度：普通到核心之间
- 需要在正文中特别引用的页码 / 图 / 表：后续补 PDF
- 需要与哪些论文并列比较：Medea、MADD、IMMUNIA、PromptBio

## 9. 总结

### 9.1 一句话概括

GALILEO 把治疗肽发现推进到 embodied 湿实验闭环。

### 9.2 速记版 pipeline

1. 从肽先验检索候选
2. OTAS 推理与局部编辑
3. 机器人合成和表型测试
4. 用湿实验反馈更新策略
5. 输出治疗候选与机制规则

### 9.3 标注字段汇总

```text
是否纳入：to_read
主类：07
二级类：07.04
三级类：therapeutic peptide discovery
四级专题：embodied therapeutic discovery agents
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Retrieval-augmented Agent; Robot / Embodied Agent; Hybrid Agent
科研流程角色：knowledge_extraction_and_organization; scientific_question_formulation; hypothesis_generation; experimental_design; simulation_modeling; tool_use_and_code_execution; experiment_execution; data_analysis; result_interpretation; evidence_assessment_and_validation; end_to_end_research_automation
自主能力：task_decomposition; planning; tool_use; memory_or_state_tracking; feedback_iteration; autonomous_decision_making; environment_interaction; closed_loop_experimentation
验证方式：simulation_validation; robotic_experiment; wet_lab_experiment
交叉属性：computation_driven; data_driven; experiment_driven; simulation_driven; multimodal; robotic_platform
科学贡献类型：design; hypothesis; experimental_discovery; system_platform
证据强度：experimentally_validated
归类置信度：高
纳入置信度：高
推荐引用强度：standard
```
