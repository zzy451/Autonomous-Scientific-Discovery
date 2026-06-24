# Yang et al. 2026 - Think like a Scientist: Physics-guided LLM Agent for Equation Discovery

**论文信息**
- 标题：Think like a Scientist: Physics-guided LLM Agent for Equation Discovery
- 作者：Jianke Yang; Ohm Venkatachalam; Mohammad Kianezhad; Sharvaree Vadgama; Rose Yu
- 年份：2026
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2602.12259
- PDF / 本地文件路径：Reference_PDF/02_Physics_Astronomy_and_Cosmic_Sciences/Yang_2026_KeplerAgent_Equation_Discovery.pdf
- 论文类型：研究论文 / equation discovery agent
- 当前状态：to_read
- 阅读日期：2026-06-24
- 笔记作者：Codex
- 一手来源核对：arXiv PDF `https://arxiv.org/pdf/2602.12259.pdf`
- 复核结论：`supported_modules=02`; `general_method_bucket=none`; `primary_module_for_filing=02`; `confidence=high`; `source_limited=no`

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | Abstract | KeplerAgent 显式模拟科学家式多步推理，协调 physics-based tools 与 SR engines | 高 |
| 科学对象归类 | `02` | Abstract | 评价数据和目标都围绕 physical equation benchmarks 与 underlying physical systems | 高 |
| 方法流程 | 物理先验驱动 SR 配置 | Abstract; Sec. 1 | 先推断 symmetries / constraints，再配置 PySINDy 与 PySR 搜索候选方程 | 高 |
| 验证对象 | 物理系统 | Abstract; Sec. 1 | across a suite of physical equation benchmarks，并覆盖 ODE / PDE 物理系统 | 高 |
| 结果表现 | 超过直接 LLM 与传统 SR 基线 | Abstract | 在 symbolic accuracy 和 noisy-data robustness 上显著更好 | 高 |
| 边界判断 | 不进入 `01.04` | Abstract; Sec. 1 | 当前冻结规则下，物理方程 benchmark 与物理系统恢复属于具体 physics object coverage | 高 |

## 0. 摘要翻译

论文认为，现有 LLM equation discovery 方法往往直接从数据猜方程，而没有显式模拟科学家“先推断中间物理结构，再缩小候选空间”的推理过程。作者提出 KeplerAgent，让 agent 先用 physics-based tools 推断对称性、约束和候选项，再把这些信息转成 PySINDy 与 PySR 的函数库和结构配置。作者在一组 physical equation benchmarks 上验证该系统，报告其 symbolic accuracy 和对噪声的鲁棒性都优于 LLM 基线和传统 symbolic regression 配置。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：系统有明确科研目标，执行多步推理和工具调用，并围绕物理系统方程恢复进行反馈迭代
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 计划生成：是
- 工具调用：是
- 反馈迭代：是
- 自主决策：部分是
- 多 Agent 协作：否
- 在科研流程中承担的明确角色：结构推断、工具配置、候选方程搜索、结果评估

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：`02`
- 覆盖模式：单模块
- 是否具有具体科学对象实验、验证、benchmark task、case study 或结果报告：是
- 独立 `01.04` 存放区：none
- Primary module for filing：`02`
- Primary module for filing 说明：文件仍位于 `01` 目录，但当前主对象归档按裁定记为 `02`；目录位置不是分类权威
- 主展示模块一级类：`02`
- 主展示模块二级类：`02.02`
- 主展示模块三级类：physics equation discovery
- 其他覆盖模块及对应层级路径：无
- 每个模块的对象实验证据：`02` 来自 physical equation benchmarks、物理对称性约束、ODE / PDE 物理系统评测
- 归类理由：论文的 benchmark、先验、工具与评估都直接围绕物理系统的方程恢复
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：物理系统与其 governing equations
- 最终科学问题：能否让 agent 像科学家那样先提取物理结构，再恢复目标方程
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：KeplerAgent 是方法，物理系统及其方程才是具体研究对象

### 2.3 容易混淆的边界

- 可能误归类到：`01.04`
- 最终判定：保持 `02`
- 判定理由：在当前 relaxed rule 下，物理方程 benchmark 和物理系统恢复属于具体 physics object coverage，而非无对象通用方法
- 多模块覆盖说明：本轮冻结裁定只支持 `02`
- 01.04 判定说明：旧 `01.04` 语言已失效
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
- 高通量筛选：否
- 机器人平台：否
- 其他：symbolic regression workflow

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：现有 LLM-SR 方法多是直接猜方程，缺少科学家式中间推理
- 现有科研流程或方法的痛点：SR 的函数库、约束和搜索空间配置高度依赖专家经验
- 核心假设或直觉：如果 agent 先识别物理结构，再反向配置 SR 工具，就能提高方程恢复可靠性

### 4.2 系统流程

1. 输入：系统观测数据
2. 任务分解 / 规划：先推断 symmetry、constraints 等中间物理结构
3. 工具、数据库、模型或实验平台调用：调用 physics-based tools，再配置 PySINDy / PySR
4. 中间结果反馈：根据工具输出与候选方程结果不断收缩搜索空间
5. 决策或迭代：继续修正函数库与结构约束
6. 输出：更准确、可解释的物理方程

### 4.3 系统组件

- Agent 核心：KeplerAgent
- 工具 / API / 数据库：physics-based tools、PySINDy、PySR
- 记忆或状态模块：workspace; experience log
- 规划器：tool-augmented reasoning loop
- 评估器 / verifier：equation scoring; robustness checks
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

- 数据集 / 实验对象：suite of physical equation benchmarks
- 任务设置：从观测数据中恢复物理系统方程
- 对比基线：direct LLM-based baselines；standalone SR tools with standard configurations
- 评价指标：symbolic accuracy；对噪声的鲁棒性；预测能力
- 关键结果：KeplerAgent 更频繁恢复 ground-truth equations，并在 noisy settings 下更稳
- 是否有消融实验：首两页未展开
- 是否有失败案例或负结果：首两页未展开

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：重点不是新物理发现，而是更可靠的物理方程恢复流程
- 科学贡献是否经过验证：是
- 贡献强度判断：中
- 科学贡献类型：system_platform; physics_equation_discovery
- 证据强度：computational_validation

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是静态 equation proposer，而是物理先验驱动的多步 agent
- 与已有 Agent / 科研智能系统的区别：把中间物理结构提取显式插入 equation discovery pipeline
- 与同一科学领域其他 Agent 文献的关系：与 STRIDE、SR-Scientist 同属 equation-discovery family，但本篇当前裁定仅支持 `02`
- 主要创新点：物理工具编排 + SR backend 自动配置

## 7. 局限性与风险

- Agent 自主性不足：仍主要在 benchmark 环境中验证
- 科学验证不足：没有真实新物理定律发现
- 泛化性不足：跨更多非物理对象的证据本轮不计入
- 工具链依赖：强
- 数据泄漏或 benchmark 偏差：需读全文细审 benchmark construction
- 成本、可复现性或安全风险：依赖工具配置与长链搜索细节

## 8. 对综述写作的价值

- 可放入哪个章节：02 Physics, Astronomy and Cosmic Sciences
- 可支撑哪个论点：方程发现框架若验证对象是物理系统，就不应保留为旧 `01.04` 语言
- 可用于哪个表格或图：equation-discovery agents 对比表
- 适合作为代表性案例吗：是
- 推荐引用强度：standard
- 需要在正文中特别引用的页码 / 图 / 表：Abstract；Fig. 1
- 需要与哪些论文并列比较：STRIDE、SR-Scientist

## 9. 总结

### 9.1 一句话概括

用物理先验驱动 SR 工具配置的方程发现 agent。

### 9.2 速记版 pipeline

1. 读入物理系统数据
2. 推断中间物理结构
3. 配置 PySINDy / PySR
4. 迭代搜索并评估候选方程
5. 输出更稳的物理方程

### 9.3 标注字段汇总

```text
是否纳入：是
科学对象模块：02
覆盖模式：single_module
是否具有具体科学对象实验：yes
general_method_bucket：none
Primary module for filing：02
是否进入 01.04 存放区：否
module_assignment_evidence：physical equation benchmarks; physics-based tools; ODE/PDE physical systems
multi_module_object_coverage_note：none
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Hybrid Agent
科研流程角色：hypothesis_generation; tool_use_and_code_execution; data_analysis; result_interpretation; evidence_assessment_and_validation
自主能力：task_decomposition; planning; tool_use; memory_or_state_tracking; feedback_iteration; environment_interaction
验证方式：benchmark; computational_validation
交叉属性：computation_driven; data_driven; simulation_driven
科学贡献类型：system_platform; physics_equation_discovery
证据强度：high
归类置信度：high
纳入置信度：high
推荐引用强度：standard
```
