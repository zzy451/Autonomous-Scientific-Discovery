# Unknown 2026 - ScientistOne: Towards Human-Level Autonomous Research via Chain-of-Evidence Verification

**论文信息**
- 标题：ScientistOne: Towards Human-Level Autonomous Research via Chain-of-Evidence Verification
- 作者：Unknown
- 年份：2026
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2605.26340
- PDF / 本地文件路径：当前未配置本地 PDF；本 note 依据本轮 reviewer evidence pack 中已核对的 arXiv 摘要与项目页更新
- 论文类型：系统论文 / Agent 论文
- 当前状态：to_read
- 阅读日期：2026-06-24
- 笔记作者：Codex

## Evidence Log

## 2026-06-24 confirmed-core full-reaudit writeback

- `final_agent_inclusion`: `yes`
- `supported_modules`: `01`
- `final_01_04_bucket`: `none`
- `primary_module_for_filing`: `01`
- `confidence`: `medium`
- `source_limited`: `no`
- `safety_access_status`: `accessed_no_safety_issue`
- `final_reason`: Concrete computational / AI research-task evidence is enough for `01`, so this should not remain `Unknown` or `01.04`-only.
- `writeback_note`: 删除残留 `01.04` 口径；本轮不扩展额外模块。

```text
scientific_object_modules: 01
object_coverage_mode: single_module
has_concrete_object_experiments: yes
general_method_bucket: none
primary_module_for_filing: 01
first_hand_sources_checked: arXiv abstract; project page
classification_evidence_source_level: first_hand_abstract_or_landing_page
module_assignment_evidence: `01` is supported by frontier AI / computational research tasks, language-modeling and AI-systems research, the 75-paper audit, and chain-of-evidence verification over concrete research tasks.
multi_module_object_coverage_note: The old `01.04`-only wording is retired. Possible adjacent signals remain follow-up leads only and are not landed as extra modules in this round.
```

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | Abstract; title; system overview | 系统围绕自主研究目标组织多步 research workflow。 | 高 |
| 科学对象归类 | `01` | arXiv abstract; project page | 任务直接落在 frontier AI / computational research、language-modeling、AI-systems research 与 CoE verification。 | 中高 |
| 01.04 边界 | 不进入 `01.04` | abstract task framing | 已有 concrete computational research-task evidence，因此不能再写成纯通用方法。 | 中高 |
| 方法流程 | chain-of-evidence autonomous research workflow | abstract / workflow overview | 包含检索、假设、验证、审查与反馈迭代。 | 中高 |
| 实验验证 | CoE audit over 75 papers / 5 systems / 5 tasks | result overview | 当前验证证据足以支撑 `01`，但还不足以扩展更多模块。 | 中高 |
| 主要风险 | core-strength risk 略高于 class risk | abstract-level evidence | 风险在证据深度与强度，而不是 `01` 顶层模块本身。 | 中 |

## 0. 摘要翻译

ScientistOne 试图通过 chain-of-evidence verification 推动更接近 human-level 的 autonomous research workflow。根据本轮冻结裁决，当前可稳定落地的对象不是 `01.04` 通用科研框架，而是具体的 computational / AI research tasks，因此应写成 concrete `01`。本轮不再额外扩展其他模块，只保留相邻领域线索为后续全文复核 lead。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：围绕自主研究目标执行多步 workflow，具有规划、工具调用、反馈迭代与协作成分
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 计划生成：是
- 工具调用：是
- 反馈迭代：是
- 自主决策：部分是
- 多 Agent 协作：部分是
- 在科研流程中承担的明确角色：literature_search_and_reading; hypothesis_generation; evidence_assessment_and_validation; workflow_orchestration; feedback_iteration

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不适用

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：`01`
- 覆盖模式：单模块
- 是否具有具体科学对象实验、验证、benchmark task、case study 或结果报告：是
- 独立 `01.04` 存放区：`none`
- Primary module for filing：`01`
- 主展示模块一级类：`01`
- 主展示模块二级类：computational / AI research tasks
- 归类理由：本轮只稳定落地 concrete computational / AI research-task coverage；不再保留旧的 `01.04`-only 表述。
- 归类置信度：中

### 2.2 对象优先判定

- 最终科学研究对象：chain-of-evidence verification 下的 concrete computational / AI research tasks
- 最终科学问题：如何让 autonomous research system 在 AI / computational research tasks 上完成多步证据链生成与核验
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：决定它属于 `01` 的不是 agent 外观，而是其直接覆盖的计算与 AI 研究任务对象

### 2.3 容易混淆的边界

- 可能误归类到：`01.04` 通用 research-agent 方法，或 `11.07` 科学知识生产研究
- 最终判定：稳定为 concrete `01`
- 判定理由：当前可核实证据首先支持 AI / computational research tasks 本身；本轮不足以再把边界信号扩成 `07`、`09` 或 `11`
- 多模块覆盖说明：本轮不增加额外模块
- 01.04 判定说明：`general_method_bucket=none`
- 是否需要二次复核：否

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- Agent 类型：LLM Agent; Tool-using Agent; Hybrid Agent

### 3.2 科研流程角色

- 主要角色：literature_search_and_reading; hypothesis_generation; evidence_assessment_and_validation; workflow_orchestration; feedback_iteration

### 3.3 自主能力

- 任务分解：是
- 计划生成：是
- 工具调用：是
- 记忆与状态维护：部分是
- 反馈迭代：是
- 自主决策：部分是
- 多 Agent 协作：部分是
- 环境交互：部分是
- 闭环实验：否

### 3.4 交叉属性标签

- 交叉属性：computation_driven

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：希望提升 autonomous research 的证据链验证能力
- 现有科研流程或方法的痛点：多步研究过程难以系统化地追踪、核验与修正
- 核心假设或直觉：通过 chain-of-evidence workflow，可以提高 AI 研究任务的可信性

### 4.2 系统流程

1. 输入：研究问题与上下文
2. 任务分解 / 规划：拆分研究步骤与证据需求
3. 工具、数据库、模型或实验平台调用：检索、分析与验证
4. 中间结果反馈：检查证据链一致性
5. 决策或迭代：根据验证结果修正研究路径
6. 输出：经证据链核验的研究结果

### 4.3 系统组件

- Agent 核心：chain-of-evidence autonomous research system
- 工具 / API / 数据库：检索与分析工具
- 记忆或状态模块：证据链与任务状态维护
- 规划器：存在
- 评估器 / verifier：存在
- 人类反馈或专家介入：未强调为核心
- 实验平台或仿真环境：75-paper / 5-system / 5-task audit setting

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

- 数据集 / 实验对象：75 papers / 5 systems / 5 tasks 的 CoE audit
- 任务设置：多步 autonomous research 与 evidence verification
- 对比基线：论文原文设置
- 评价指标：证据链核验与任务完成情况
- 关键结果：足以支撑 `01` 顶层对象归类
- 是否有消融实验：现 note 不展开
- 是否有失败案例或负结果：现 note 不展开

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：主要贡献是 computational research workflow 与 evidence verification，不是其他自然科学对象发现
- 科学贡献是否经过验证：是
- 贡献强度判断：中
- 科学贡献类型：system_platform; general_scientific_research
- 证据强度：medium_primary_abstract

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单步模型输出，而是 evidence-verification research workflow
- 与已有 Agent / 科研智能系统的区别：强调 chain-of-evidence verification
- 与同一科学领域其他 Agent 文献的关系：适合作为“从 01.04 退回 concrete 01”的样本
- 主要创新点：把研究执行与证据链核验统一进自主 research system

## 7. 局限性与风险

- Agent 自主性不足：仍可能依赖外部设定与人工解释
- 科学验证不足：当前主要依赖摘要级与项目页级证据
- 泛化性不足：跨任务稳定性仍待全文细查
- 工具链依赖：依赖检索与分析工具
- 数据泄漏或 benchmark 偏差：benchmark / audit 设定偏差风险存在
- 成本、可复现性或安全风险：多步系统复现成本较高
- 主要剩余风险：core-strength risk 略高于 class risk
- 是否仍需进一步全文复核：否，本轮分类写回已足够稳定

## 8. 对综述写作的价值

- 可放入哪个章节：形式、信息与计算科学中的 autonomous research systems
- 可支撑哪个论点：只要已有 concrete AI / computational research-task evidence，就不应继续写成 `01.04`
- 可用于哪个表格或图：`01.04` 退桶案例表；computational research Agent 样本表
- 适合作为代表性案例吗：适合作为边界修正样本
- 推荐引用强度：standard
- 需要在正文中特别引用的页码 / 图 / 表：CoE audit task framing
- 需要与哪些论文并列比较：其他 autonomous research / AI-research Agent 论文

## 9. 总结

### 9.1 一句话概括

一个应写成 concrete `01` 而非 `01.04` 的 chain-of-evidence research Agent。

### 9.2 速记版 pipeline

1. 接收研究问题
2. 规划证据链任务
3. 检索与分析
4. 核验并迭代
5. 输出研究结果

### 9.3 标注字段汇总

```text
是否纳入：是
科学对象模块：01
覆盖模式：single_module
是否具有具体科学对象实验：yes
general_method_bucket：none
Primary module for filing：01
是否进入 01.04 存放区：否
主展示模块一级类：01
主展示模块二级类：computational / AI research tasks
主展示模块三级类：chain-of-evidence autonomous research verification
主展示模块四级专题：ScientistOne
其他覆盖模块及对应层级路径：none landed this round
module_assignment_evidence：frontier AI / computational research tasks, language-modeling and AI-systems research, 75-paper CoE audit
multi_module_object_coverage_note：显式去除旧的 01.04-only 口径；邻近模块线索保留为 follow-up，不在本轮落地
Agent 类型：LLM Agent; Tool-using Agent; Hybrid Agent
科研流程角色：literature_search_and_reading; hypothesis_generation; evidence_assessment_and_validation; workflow_orchestration; feedback_iteration
自主能力：planning; tool_use; feedback_iteration; autonomous_decision_making; multi_agent_collaboration
验证方式：benchmark; computational_validation
交叉属性：computation_driven
科学贡献类型：system_platform; general_scientific_research
证据强度：medium_primary_abstract
归类置信度：medium
纳入置信度：high
推荐引用强度：standard
```
