# Unknown 2025 - AutoDiscovery: Open-ended Scientific Discovery via Bayesian Surprise

**论文信息**
- 标题：AutoDiscovery: Open-ended Scientific Discovery via Bayesian Surprise
- 作者：Unknown
- 年份：2025
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2507.00310
- PDF / 本地文件路径：`Autonomous Scientific Discovery/Reference_PDF/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Unknown_2025_AutoDiscovery.pdf`（official arXiv PDF archived locally and checked）
- 论文类型：研究论文 / open-ended scientific-discovery agent system
- 当前状态：to_read
- 阅读日期：2026-06-24
- 笔记作者：Codex

## Frozen Adjudication Writeback - 2026-06-24

This writeback aligns the note to the frozen Batch29Partial1 adjudication for `ASD-0856`.

```text
final_agent_inclusion: yes
scientific_object_modules: 06;07;11
object_coverage_mode: multi_module
has_concrete_object_experiments: yes
general_method_bucket: none
primary_module_for_filing: 11
confidence: high
source_limited: no
safety_access_status: none
first_hand_sources_checked: official arXiv PDF https://arxiv.org/pdf/2507.00310.pdf; local archive `Autonomous Scientific Discovery/Reference_PDF/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Unknown_2025_AutoDiscovery.pdf`
classification_evidence_source_level: first_hand_full_text_with_local_archived_arxiv_pdf
module_assignment_evidence: DiscoveryBench freshwater-fish and BLADE biological/fish datasets support `06`; SEA-AD human-brain cellular atlas with Alzheimer's-spectrum donor cognition and neuropathology supports `06;07`; economics, finance, and behavioral-science datasets such as NLS, mortgage, affairs, caschools, reading, teaching-ratings, and soccer support `11`.
multi_module_object_coverage_note: note location under `01_Formal_Information_and_Computational_Sciences` is historical filing only; the authoritative classification fact is frozen multi-module coverage `06;07;11`, with `11` as the primary filing module.
final_reason: this is not an independent `01.04` paper because the reported experiments span concrete life-science, biomedical, and social/behavioral/economic datasets.
```

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Frozen adjudication | `06;07;11`; `primary=11` | Batch29Partial1 frozen packet + arXiv PDF | 本轮明确退役旧 `01.04`-only 处理 | 高 |
| Agent 纳入 | 是 | arXiv PDF abstract / method | open-ended discovery loop combines hypothesis generation, search, update, and iterative surprise-driven exploration | 高 |
| 科学对象归类 | `06;07;11` | arXiv PDF Sec. 4.1 / Sec. 5 / appendix datasets | 数据集覆盖 biology, biomedical health, economics, finance, and behavioral science | 高 |
| 方法流程 | Bayesian-surprise research loop | arXiv PDF method sections | 通过 Bayesian surprise 与搜索过程在候选假设和研究方向之间迭代推进 | 高 |
| 实验验证 | 21 real-world datasets + human surprise evaluation | arXiv PDF experiments | 使用 21 个真实数据驱动发现任务与 human surprise evaluation 检验系统 | 高 |
| 边界判断 | 不再作为 `01.04` 独立通用方法 | arXiv PDF + Batch29Partial1 packet | hurricane 与 requirement-engineering 不计入高置信 `05` / `01`，但 biology / SEA-AD / economics-family 数据已足够支持 `06;07;11` | 高 |

## 0. 摘要翻译

AutoDiscovery 提出一种由 Bayesian surprise 驱动的开放式科学发现 Agent 框架。系统并不只是演示通用科研工作流，而是把假设生成、候选研究方向搜索、结果更新和 surprise-based selection 串成循环，并在 21 个真实数据驱动发现任务上进行实验。当前冻结口径下，论文的对象证据已经明确落到生命科学、医学健康和社会/行为/经济科学数据集，因此不再保留旧的独立 `01.04` 处理。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：系统围绕科学发现目标执行多步搜索、比较和更新，并具有规划、工具使用、反馈迭代和自主方向选择
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：部分是
- 在科研流程中承担的明确角色：假设生成、研究方向搜索、证据更新、结果评估

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不适用

## 2. 科学领域归类

### 2.1 主科学领域

- scientific_object_modules：`06;07;11`
- object_coverage_mode：`multi_module`
- has_concrete_object_experiments：yes
- general_method_bucket：none
- primary_module_for_filing：`11`
- source_limited：no
- 一级类：11；并记录 `06` 与 `07`
- 二级类：本轮不硬化 11 的更细分二级类；保留顶层 `11` 主归档，并显式记录 `06;07`
- 三级类：cross-domain data-driven discovery over life, biomedical, and socio-behavioral datasets
- 四级专题：Bayesian-surprise open-ended scientific-discovery agents
- 四级专题是否为新增：否
- 归类理由：论文在真实数据集上的对象覆盖已经跨越 life science、biomedical health 和 social/behavioral/economic science，不能继续仅按通用方法或旧 `01.04` 叙事处理
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：biology datasets; Alzheimer's-spectrum brain atlas and neuropathology; economics / finance / behavioral-science discovery tasks
- 最终科学问题：如何在多类真实科学数据集上进行开放式、surprise-driven hypothesis exploration
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：Bayesian-surprise / search machinery 是方法实现；模块归类依据是实际实验覆盖的科学对象

### 2.3 容易混淆的边界

- 可能误归类到：01.04；05；01
- 最终判定：`06;07;11`
- 判定理由：`01.04` 只适用于无具体对象实验的通用科研方法；本文已有 concrete-object dataset coverage。另一方面，hurricane 与 requirement-engineering 证据不足以高置信扩展到 `05` 或 `01`
- 是否需要二次复核：不需要维持 `01.04`；若后续需要，只需检查更细的 11 下级边界

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：不明确
- Multi-Agent System：部分是
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：部分是（human surprise evaluation）
- Hybrid Agent：是
- 其他：Bayesian-surprise search agent

### 3.2 科研流程角色

- 文献检索与阅读：否
- 知识抽取与组织：部分是
- 科学问题提出：是
- 假设生成：是
- 实验设计：部分是
- 仿真建模：否
- 工具调用与代码执行：是
- 实验执行：否
- 数据分析：是
- 结果解释：是
- 证据评估与验证：是
- 论文写作：否
- 端到端科研流程自动化：部分是

### 3.3 自主能力

- 任务分解：部分是
- 计划生成：是
- 工具调用：是
- 记忆与状态维护：是
- 反馈迭代：是
- 自主决策：是
- 多 Agent 协作：部分是
- 环境交互：是
- 闭环实验：部分是

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 实验驱动：否
- 仿真驱动：否
- 多模态：不明确
- 多尺度建模：否
- 高通量筛选：否
- 知识图谱：否
- 数字孪生：否
- 机器人平台：否
- 其他：open-ended discovery over real-world datasets

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：希望把开放式科学发现从静态 benchmark 提升为可持续扩展研究方向的惊奇驱动流程
- 现有科研流程或方法的痛点：传统研究管线往往固定任务、固定假设，难以动态发现更有信息量的方向
- 核心假设或直觉：以 Bayesian surprise 作为导向，可以让 Agent 在多轮候选中优先探索更可能带来新解释或新模式的方向

### 4.2 系统流程

1. 输入：数据集、初始问题和候选解释方向
2. 任务分解 / 规划：生成并筛选候选假设或研究路径
3. 工具、数据库、模型或实验平台调用：在数据上运行分析与比较程序
4. 中间结果反馈：根据 surprise score 和观察到的结果更新优先级
5. 决策或迭代：保留高价值方向并继续探索
6. 输出：新的发现线索、假设比较和数据驱动解释

### 4.3 系统组件

- Agent 核心：Bayesian-surprise driven open-ended discovery loop
- 工具 / API / 数据库：数据分析与搜索组件
- 记忆或状态模块：候选方向与 surprise-based state update
- 规划器：存在研究路径选择逻辑
- 评估器 / verifier：human surprise evaluation + task-level metrics
- 人类反馈或专家介入：human surprise evaluation
- 实验平台或仿真环境：21 real-world discovery datasets

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：否
- 高通量计算：否
- 机器人实验：否
- 湿实验：否
- 临床数据：部分是
- 真实场景部署：否
- 专家评估：部分是

### 5.2 数据、任务与指标

- 数据集 / 实验对象：21 real-world discovery datasets
- 任务设置：在不同学科对象上进行开放式假设探索与 surprise-based discovery
- 对比基线：以论文原文报告的 discovery baselines 为准
- 评价指标：task performance + human surprise evaluation
- 关键结果：DiscoveryBench freshwater-fish 与 BLADE biological/fish tasks 支持 `06`；SEA-AD supports `06;07`；economics / finance / behavioral-science tasks support `11`
- 是否有消融实验：论文有方法比较，但本轮不把其视为主分类核心
- 是否有失败案例或负结果：旧 note 中曾考虑 hurricane / requirement-engineering，但本轮未接受为高置信模块扩展

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：主要贡献是跨多学科数据集的 open-ended discovery workflow；对象证据来自具体数据任务而非单一自然科学实验
- 科学贡献是否经过验证：是
- 贡献强度判断：中
- 科学贡献类型：system_platform; hypothesis
- 证据强度：first_hand_full_text

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单一预测器，而是循环式 open-ended discovery workflow
- 与已有 Agent / 科研智能系统的区别：以 Bayesian surprise 作为研究方向切换和候选保留的关键驱动
- 与同一科学领域其他 Agent 文献的关系：是从旧 `01.04` 退役为 `06;07;11` 多模块的典型边界样本
- 主要创新点：把跨学科真实数据集上的 surprise-driven exploration 组织成可迭代 Agent 流程

## 7. 局限性与风险

- Agent 自主性不足：仍依赖数据集设定和可枚举候选空间
- 科学验证不足：对象证据更多来自 dataset task coverage，而非统一的真实实验部署
- 泛化性不足：跨领域任务并不自动意味着每个模块下的细粒度结论都稳定
- 工具链依赖：依赖 surprise scoring、搜索与分析工具
- 数据泄漏或 benchmark 偏差：多任务 benchmark 仍有数据选择偏差风险
- 是否仍需进一步全文复核：不需要为 `01.04` 重判；若后续细化 11 的下级类，可再看具体 socio-behavioral 子集

## 8. 对综述写作的价值

- 可放入哪个章节：11 社会、行为、经济与知识系统科学；并作为 `06 / 07 / 11` 多模块样本
- 可支撑哪个论点：只要真实实验 / 数据任务覆盖了具体对象，就不应继续作为独立 `01.04` 通用方法处理
- 可用于哪个表格或图：多模块迁移案例表；`01.04` 退役样本表
- 适合作为代表性案例吗：适合作为边界案例
- 推荐引用强度：standard
- 需要在正文中特别引用的页码 / 图 / 表：Sec. 4.1；Sec. 5；appendix dataset examples
- 需要与哪些论文并列比较：其他从旧 `01.04` 调整为 concrete-object multi-module 的 general-science agents

## 9. 总结

### 9.1 一句话概括

以 Bayesian surprise 驱动、并已落到 `06;07;11` 具体对象覆盖的开放式科学发现 Agent。

### 9.2 速记版 pipeline

1. 输入数据与初始问题
2. 生成候选假设或方向
3. 用 surprise 评估并更新优先级
4. 持续迭代探索
5. 输出更有信息量的发现线索

### 9.3 标注字段汇总

```text
是否纳入：是
scientific_object_modules：06;07;11
object_coverage_mode：multi_module
has_concrete_object_experiments：yes
general_method_bucket：none
primary_module_for_filing：11
source_limited：no
一级类：11；并记录 06；07
二级类：本轮不硬化 11 的更细分二级类
三级类：cross-domain data-driven discovery over life, biomedical, and socio-behavioral datasets
四级专题：Bayesian-surprise open-ended scientific-discovery agents
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Hybrid Agent
科研流程角色：scientific_question_formulation; hypothesis_generation; tool_use_and_code_execution; data_analysis; result_interpretation; evidence_assessment_and_validation; workflow_orchestration
自主能力：planning; tool_use; memory_or_state_tracking; feedback_iteration; autonomous_decision_making
验证方式：benchmark; clinical_data; expert_evaluation
交叉属性：computation_driven; data_driven
科学贡献类型：system_platform; hypothesis
证据强度：first_hand_full_text
归类置信度：高
纳入置信度：高
推荐引用强度：standard
```
