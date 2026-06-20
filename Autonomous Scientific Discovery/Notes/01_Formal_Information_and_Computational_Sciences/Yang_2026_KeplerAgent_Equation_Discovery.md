# Yang et al. 2026 - Think like a Scientist: Physics-guided LLM Agent for Equation Discovery

## 2026-06-20 relaxed multi-module revision

```text
scientific_object_modules: 02
object_coverage_mode: single_module
has_concrete_object_experiments: yes
general_method_bucket: none
primary_module_for_filing: 02
first_hand_sources_checked: arXiv abstract / PDF page
classification_evidence_source_level: first_hand_abstract_or_landing_page
module_assignment_evidence: Physical equation benchmarks, symmetries, physics-guided tool configuration, and physical symbolic equations support 02.
multi_module_object_coverage_note: The previous independent 01.04 treatment reflected the method's domain-transferable workflow. Under the relaxed benchmark-object rule, physical equation-discovery tasks are concrete physics object coverage, so this record should move out of 01.04-only treatment.
```

**论文信息**
- 标题：Think like a Scientist: Physics-guided LLM Agent for Equation Discovery
- 作者：Jianke Yang; Ohm Venkatachalam; Mohammad Kianezhad; Sharvaree Vadgama; Rose Yu
- 年份：2026
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2602.12259
- PDF / 本地文件路径：当前无本地 PDF；本 note 基于 arXiv abstract page 与 batch14 reviewer evidence
- 论文类型：研究论文 / equation-discovery agent framework
- 当前状态：to_read
- 阅读日期：2026-06-20
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | arXiv abstract | KeplerAgent explicitly follows a multi-step scientific reasoning process | 高 |
| 科学对象归类 | `01 / 01.04` | abstract; reviewer pack | 贡献重心是 equation-discovery agent workflow 与 tool orchestration，而非单一科学对象 | 高 |
| 方法流程 | tool-augmented reasoning | abstract; reviewer pack | infer physical properties -> configure PySINDy / PySR -> refine candidates | 高 |
| 边界判断 | 从 `01.03` 转 `01.04` | object-first review | “physics-guided” 是先验与 benchmark 环境，不足以使其成为具体规律对象研究 | 中高 |
| 实验验证 | benchmark / computational validation | abstract | validates on physical equation benchmarks, not real new law discovery | 高 |

## 0. 摘要翻译

论文指出，许多现有 LLM-based equation discovery systems 直接从数据猜方程，而没有显式模拟科学家常用的多步推理过程。作者提出 KeplerAgent，让 agent 先推断 symmetry 等物理性质，再据此配置 PySINDy、PySR 等 symbolic regression engines 的函数库与结构约束。该系统在一组 physical equation benchmarks 上获得更高的 symbolic accuracy 和 noise robustness。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：有明确科研目标、多步推理、工具调用、工作区状态读写与反馈迭代
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：部分是
  - 多 Agent 协作：否
- 在科研流程中承担的明确角色：中间物理结构推断、工具配置、候选方程优化与验证

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：01
- 二级类：01.04
- 三级类：
- 四级专题：Physics-guided equation-discovery agents
- 四级专题是否为新增：否
- 归类理由：论文的稳定对象是通用 equation-discovery workflow 与 tool orchestration，而不是单一物理规律对象本体
- 归类置信度：中高

### 2.2 对象优先判定

- 最终科学研究对象：physics-guided but domain-transferable equation-discovery agent workflow
- 最终科学问题：如何让 agent 像科学家一样多步调用工具完成 equation discovery
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：这里不是因为用了 LLM 就进 01.04，而是因为论文贡献稳定落在领域可迁移 workflow capability

### 2.3 容易混淆的边界

- 可能误归类到：01.03
- 最终判定：转入 01.04
- 判定理由：`physics-guided` 是先验与验证语境，不等于论文在研究具体系统规律本体；其主要贡献是通用 scientific equation-discovery agent framework
- 是否需要二次复核：可选，但主类判断已基本稳定

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
- 其他：tool-orchestrating equation-discovery agent

### 3.2 科研流程角色

- 文献检索与阅读：否
- 知识抽取与组织：部分是
- 科学问题提出：否
- 假设生成：是
- 实验设计：否
- 仿真建模：部分是
- 工具调用与代码执行：是
- 实验执行：否
- 数据分析：是
- 结果解释：是
- 证据评估与验证：是
- 论文写作：否
- 端到端科研流程自动化：部分是

### 3.3 自主能力

- 任务分解：是
- 计划生成：是
- 工具调用：是
- 记忆与状态维护：是
- 反馈迭代：是
- 自主决策：部分是
- 多 Agent 协作：否
- 环境交互：是
- 闭环实验：否

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 实验驱动：否
- 仿真驱动：是
- 多模态：否
- 多尺度建模：否
- 高通量筛选：否
- 知识图谱：否
- 数字孪生：否
- 机器人平台：否
- 其他：symbolic regression workflow

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：现有 LLM-based systems 多为直接猜方程，缺少科学家式多步推理
- 现有科研流程或方法的痛点：难以把中间物理先验转化为 symbolic regression 的有效约束
- 核心假设或直觉：若 agent 能先抽取中间物理结构，再配置 SR engines，方程发现会更稳健

### 4.2 系统流程

1. 输入：观测数据
2. 任务分解 / 规划：先推断 symmetry 等物理属性
3. 工具、数据库、模型或实验平台调用：PySINDy; PySR 等 symbolic regression engines
4. 中间结果反馈：根据工具输出更新候选方程与约束
5. 决策或迭代：继续配置 / 修正 equation search
6. 输出：更高 symbolic accuracy 的 equation discovery result

### 4.3 系统组件

- Agent 核心：KeplerAgent
- 工具 / API / 数据库：physics-based tools; PySINDy; PySR
- 记忆或状态模块：workspace; experience log
- 规划器：tool-augmented reasoning loop
- 评估器 / verifier：equation scoring and robustness checks
- 人类反馈或专家介入：未强调
- 实验平台或仿真环境：physical equation benchmarks

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

- 数据集 / 实验对象：physical equation benchmarks
- 任务设置：symbolic equation discovery with noise robustness
- 对比基线：LLM baselines; traditional baselines
- 评价指标：symbolic accuracy; robustness to noisy data
- 关键结果：取得更高 accuracy 与 robustness
- 是否有消融实验：当前摘要级证据不足
- 是否有失败案例或负结果：当前摘要级证据不足

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：重点是 workflow capability，而非真实新规律发现
- 科学贡献是否经过验证：是
- 贡献强度判断：中
- 科学贡献类型：system_platform; general_scientific_research
- 证据强度：benchmark / computational_validation

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单次 equation proposal，而是 multi-step tool-using agent
- 与已有 Agent / 科研智能系统的区别：强调 physics-guided intermediate reasoning 到 SR configuration 的连接
- 与同一科学领域其他 Agent 文献的关系：可与 STRIDE、SR-Scientist 对照为 equation-discovery workflow family
- 主要创新点：把物理先验抽取和 symbolic regression orchestration 显式 agent 化

## 7. 局限性与风险

- Agent 自主性不足：仍主要是 benchmark-driven workflow
- 科学验证不足：没有真实新科学规律发现或外部实验确认
- 泛化性不足：虽跨方程 benchmark，但仍依赖物理先验语境
- 工具链依赖：强
- 数据泄漏或 benchmark 偏差：需全文再审 benchmark design
- 成本、可复现性或安全风险：tool orchestration 细节需全文补充

## 8. 对综述写作的价值

- 可放入哪个章节：01.04 General scientific research-agent systems
- 可支撑哪个论点：equation-discovery workflow 若贡献重心在通用 agent capability，应优先归 01.04
- 可用于哪个表格或图：`01.03 / 01.04` 边界对照表
- 适合作为代表性案例吗：是
- 推荐引用强度：普通引用
- 需要在正文中特别引用的页码 / 图 / 表：后续全文再补
- 需要与哪些论文并列比较：ASD-0869; ASD-0870; ASD-0857

## 9. 总结

### 9.1 一句话概括

Physics-guided 的通用方程发现 Agent workflow。

### 9.2 速记版 pipeline

1. 读取数据
2. 推断中间物理结构
3. 配置 SR 工具
4. 迭代搜索与评估
5. 输出方程

### 9.3 标注字段汇总

```text
是否纳入：是
主类：01
二级类：01.04
三级类：
四级专题：Physics-guided equation-discovery agents
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Hybrid Agent
科研流程角色：hypothesis_generation; tool_use_and_code_execution; evidence_assessment_and_validation; feedback_iteration
自主能力：task_decomposition; planning; tool_use; memory_and_state; feedback_iteration
验证方式：benchmark; computational_validation
交叉属性：computation_driven; data_driven; simulation_driven
科学贡献类型：system_platform; general_scientific_research
证据强度：benchmark
归类置信度：中高
纳入置信度：高
推荐引用强度：standard
```
