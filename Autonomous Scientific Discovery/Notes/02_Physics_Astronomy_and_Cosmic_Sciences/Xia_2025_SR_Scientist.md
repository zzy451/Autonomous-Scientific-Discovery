# Xia et al. 2025 - SR-SCIENTIST: Scientific Equation Discovery With Agentic AI

## 当前分类（2026-11-01 补证复核）

- 当前纳入状态：`to_read`；主归档：`02`。
- 当前对象模块：`02;03;04;06`。
- 本节为当前结论，取代后文不一致的历史分类；每个模块保留一个有证据支持的代表落点。

| 模块 | 二级 | 三级 | 当前状态 |
|---|---|---|---|
| 02 | 02.02 物理学 | 02.02.03 经典力学 | 已确定 |
| 03 | 03.02 基础化学 | 03.02.04 物理化学 | 已确定 |
| 04 | 04.01 材料基础 | 04.01.01 材料物理 | 已确定 |
| 06 | 06.01 生物学基础 | 06.01.13 计算生物学 | 已确定 |

### 模块03补证

- 原缺项原因：前轮只有领域数量与独立RL训练集变量描述，未核对实际测试集入口及其正式方程表。
- 本轮结论：本文p.5实际评估LSR-Synth，官方推理预处理加载lsr_synth_chem_react。基准官方模块将对象定义为反应动力学的浓度变化速率、时间与浓度；基准作者论文Table 4公开CKR17、CKR22等反应速率方程。该对象支持03.02.04物理化学，不据动力学方程推定反应路径或机理实证。
- 来源：local PDF；位置：pp.5–6, §4.1, Table 1；原文：We evaluate our methods on the synthetic part of the LLM-SRBench
- 来源：https://raw.githubusercontent.com/GAIR-NLP/SR-Scientist/00a44a11ff4bfd6e67cdfe8e6cc1ef5f5144b505/utils/data_preprocessing.py；位置：inference preprocessing；原文：for dataset_identifier in ['matsci','chem_react','bio_pop_growth','phys_osc']:
- 来源：https://raw.githubusercontent.com/deep-symbolic-mathematics/llm-srbench/6fdbe409b75ea749c0a93c69b6861637d804dec4/bench/datamodules.py；位置：ChemReactKineticsDataModule；原文：Rate of change of concentration in chemistry reaction kinetics
- 来源：https://arxiv.org/pdf/2504.10415；位置：benchmark paper, physical pp.14,24, Fig.9 and Table 4；原文：Chemistry: Reaction rate with respect to Time and Concentration；CKR17: −kA(t) + kf A(t)^0.33；CKR22: −kA(t)exp(−kst) + kqA(t)log(γt+1)。
- 解释范围：为合成方程任务的ID/OOD测试，不是新反应的湿实验发现；没有读取受限HF parquet；不以本文p.15独立RL训练示例替代测试证据。

### 模块04补证

- 原缺项原因：缺少正式测试集的材料对象定义及方程，前轮未将训练和测试证据区分核实。
- 本轮结论：本文实际测试LSR-Synth；官方推理入口加载matsci测试部分。基准作者论文Fig.9明确材料对象为应力随应变及温度变化，Table 4公开MatSci5、MatSci12等本构式，支持04.01.01材料物理。任务的物理语义已可识别，不必要求具体材料商品名。
- 来源：local PDF；位置：pp.5–6, §4.1, Table 1；原文：material science
- 来源：https://raw.githubusercontent.com/GAIR-NLP/SR-Scientist/00a44a11ff4bfd6e67cdfe8e6cc1ef5f5144b505/utils/data_preprocessing.py；位置：inference preprocessing；原文：for dataset_identifier in ['matsci','chem_react','bio_pop_growth','phys_osc']:
- 来源：https://arxiv.org/pdf/2504.10415；位置：benchmark paper, physical pp.14,27, Fig.9 and Table 4；原文：Material Science: Stress with respect to Strain and Temperature；MatSci5: E0ε² + η(T−T0)log(ε+1)；MatSci12: Kε^N exp(−Q/(RT)) + ε³η(T−T0)。
- 解释范围：仅支持合成材料本构方程任务；不声称真实材料测量或实验室材料发现。

- [本轮补证报告](../../Coverage_Check/classification_recheck_2026-11-01/completion_report.md)。

## 既有笔记与历史审计记录

**论文信息**
- 标题：SR-SCIENTIST: Scientific Equation Discovery With Agentic AI
- 作者：Shijie Xia; Yuhan Sun; Pengfei Liu
- 年份：2025
- 来源 / venue：ICLR 2026 Poster / arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2510.11661
- PDF / 本地文件路径：`Reference_PDF/02_Physics_Astronomy_and_Cosmic_Sciences/Xia_2025_SR_Scientist.pdf`；本轮核对本地归档 arXiv PDF
- 论文类型：研究论文 / equation discovery agent
- 当前状态：已读（本轮核对本地归档 PDF）；主列表流程状态仍可保持 `to_read`
- 阅读日期：2026-06-24
- 笔记作者：Codex
- 一手来源核对：本轮核对本地归档 arXiv PDF `Reference_PDF/02_Physics_Astronomy_and_Cosmic_Sciences/Xia_2025_SR_Scientist.pdf`，并对照 arXiv HTML / abstract `https://arxiv.org/abs/2510.11661`
- 复核结论：`supported_modules=02;03;04;06`; `general_method_bucket=none`; `primary_module_for_filing=02`; `confidence=medium-high`; `source_limited=no`

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | Abstract | autonomous AI scientist 能写代码、分析数据、提交评估并根据反馈长程优化方程 | 高 |
| 科学对象归类 | `02;03;04;06` | Abstract | datasets covering four science disciplines: chemistry, biology, physics, material science | 高 |
| `02` 证据 | 物理对象成立 | Abstract | four-discipline datasets 中明确包含 physics | 中高 |
| `03` 证据 | 化学对象成立 | Abstract | four-discipline datasets 中明确包含 chemistry | 中高 |
| `04` 证据 | 材料对象成立 | Abstract | four-discipline datasets 中明确包含 material science | 中高 |
| `06` 证据 | 生命对象成立 | Abstract | four-discipline datasets 中明确包含 biology | 中高 |
| 结果表现 | 多项指标提升 | Abstract | 比基线高 6% 到 35%，并展示 noise robustness、OOD generalization、symbolic accuracy | 高 |
| 边界判断 | 不进入 `01.04` | Abstract; 本轮裁定 | 虽然论文是长程 equation-discovery framework，但当前 relaxed rule 将四学科 benchmark 对象视为具体覆盖 | 中高 |

## 0. 摘要翻译

论文认为，现有 LLM scientific equation discovery 方法通常只把 LLM 当作 equation proposer，嵌在固定的人类流水线中，缺乏通过环境交互自主生成和修正假设的能力。作者提出 SR-SCIENTIST，把 LLM 提升为 autonomous AI scientist：系统能写代码分析数据、把方程实现成代码、提交评估，并根据实验反馈继续优化方程。作者还构建了一个 end-to-end reinforcement learning framework 来增强 agent 能力。实验覆盖 chemistry、biology、physics、material science 四个学科，显示系统在精度、泛化、噪声鲁棒性和 symbolic accuracy 上都优于基线。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：具有明确科研目标、长程多步行动、代码工具调用、反馈驱动优化和较高自主性
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 计划生成：是
- 工具调用：是
- 反馈迭代：是
- 自主决策：是
- 多 Agent 协作：否
- 在科研流程中承担的明确角色：数据分析、代码执行、方程评估、方程优化

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：`02;03;04;06`
- 覆盖模式：多模块
- 是否具有具体科学对象实验、验证、benchmark task、case study 或结果报告：是
- 独立 `01.04` 存放区：none
- Primary module for filing：`02`
- Primary module for filing 说明：当前按裁定以 `02` 归档展示，但多模块事实以对象证据为准
- 主展示模块一级类：`02`
- 主展示模块二级类：physics equation discovery
- 其他覆盖模块及对应层级路径：
  - `03`：chemistry equation discovery tasks
  - `04`：material science equation discovery tasks
  - `06`：biology equation discovery tasks
- 每个模块的对象实验证据：
  - `02`：physics datasets
  - `03`：chemistry datasets
  - `04`：material science datasets
  - `06`：biology datasets
- 归类理由：四学科 benchmark 数据集是明确的对象级验证，不再支持旧 `01.04` 语言
- 归类置信度：中高

### 2.2 对象优先判定

- 最终科学研究对象：物理、化学、材料、生命科学中的方程发现任务
- 最终科学问题：如何让 autonomous AI scientist 通过长程工具交互恢复科学方程
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：RL 与 code interpreter 是方法实现，模块判定看四学科数据对象

### 2.3 容易混淆的边界

- 可能误归类到：`01.04`
- 最终判定：保持 `02;03;04;06`
- 判定理由：旧笔记强调框架感，但当前裁定把四学科 benchmark 任务视为具体对象覆盖
- 多模块覆盖说明：本轮冻结裁定不再增删模块
- 01.04 判定说明：不适用
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
- 仿真驱动：是
- 多模态：否
- 高通量筛选：否
- 机器人平台：否
- 其他：reinforcement-learning enhanced scientific agent

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：摆脱“LLM 只是 equation proposer”的被动角色
- 现有科研流程或方法的痛点：缺少长程、tool-driven、自主优化能力
- 核心假设或直觉：让 agent 自己写代码、分析数据、读取反馈并持续优化方程，能更像科学家工作

### 4.2 系统流程

1. 输入：待恢复规律的数据
2. 任务分解 / 规划：agent 决定先做哪些数据分析和方程尝试
3. 工具、数据库、模型或实验平台调用：code interpreter tools 用于分析数据和评估方程
4. 中间结果反馈：根据 evaluation results 读取误差和表现信号
5. 决策或迭代：继续修改方程并长期优化
6. 输出：更优的 equation discovery result

### 4.3 系统组件

- Agent 核心：SR-SCIENTIST
- 工具 / API / 数据库：code interpreter; equation evaluation tools
- 记忆或状态模块：experience buffer
- 规划器：long-horizon optimization policy
- 评估器 / verifier：equation evaluation loop
- 人类反馈或专家介入：minimal human-defined pipelines
- 实验平台或仿真环境：four-discipline scientific datasets

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

- 数据集 / 实验对象：chemistry、biology、physics、material science datasets
- 任务设置：scientific equation discovery
- 对比基线：baseline SR methods / equation proposers
- 评价指标：performance margin、noise robustness、OOD generalization、symbolic accuracy
- 关键结果：比基线高 6% 到 35%，并在 RL 后进一步提升
- 是否有消融实验：摘要提到 data analysis、experience buffer、long-horizon optimization 的重要性
- 是否有失败案例或负结果：首两页未细述

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：重点是跨学科方程恢复能力提升
- 科学贡献是否经过验证：是
- 贡献强度判断：中
- 科学贡献类型：system_platform; multi_domain_equation_discovery
- 证据强度：computational_validation

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是静态生成器，而是能自主写代码与多轮优化的 scientific agent
- 与已有 Agent / 科研智能系统的区别：引入 end-to-end RL 以增强 equation-discovery 行为
- 与同一科学领域其他 Agent 文献的关系：与 KeplerAgent、STRIDE 同属 equation-discovery agent family
- 主要创新点：long-horizon tool use + RL-enhanced optimization

## 7. 局限性与风险

- Agent 自主性不足：主要仍是 benchmark 环境中的 autonomy
- 科学验证不足：没有真实实验型新定律发现
- 泛化性不足：四学科 benchmark 覆盖不等于真实世界全域科研
- 工具链依赖：强
- 数据泄漏或 benchmark 偏差：需检查训练与评估隔离
- 成本、可复现性或安全风险：RL 训练和长程执行成本可能较高

## 8. 对综述写作的价值

- 可放入哪个章节：02 Physics 作为 filing，同时在 03 / 04 / 06 多模块表中出现
- 可支撑哪个论点：方程发现 agent 一旦在多学科数据对象上验证，就应从旧 `01.04` 描述转为对象覆盖描述
- 可用于哪个表格或图：equation-discovery agents across science domains
- 适合作为代表性案例吗：是
- 推荐引用强度：standard
- 需要在正文中特别引用的页码 / 图 / 表：Abstract；Fig. 1
- 需要与哪些论文并列比较：KeplerAgent、STRIDE

## 9. 总结

### 9.1 一句话概括

会写代码并长程优化方程的 autonomous equation-discovery agent。

### 9.2 速记版 pipeline

1. 读入数据
2. 写代码分析并实现候选方程
3. 提交评估
4. 读取反馈
5. 长程优化方程

### 9.3 标注字段汇总

```text
是否纳入：是
科学对象模块：02;03;04;06
覆盖模式：multi_module
是否具有具体科学对象实验：yes
general_method_bucket：none
Primary module for filing：02
是否进入 01.04 存放区：否
module_assignment_evidence：datasets covering chemistry, biology, physics, and material science
multi_module_object_coverage_note：四学科对象覆盖来自明确数据集与评测任务，而非单纯通用性声明
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Hybrid Agent
科研流程角色：hypothesis_generation; tool_use_and_code_execution; data_analysis; result_interpretation; evidence_assessment_and_validation
自主能力：task_decomposition; planning; tool_use; feedback_iteration; autonomous_decision_making; environment_interaction
验证方式：benchmark; computational_validation
交叉属性：computation_driven; data_driven; simulation_driven
科学贡献类型：system_platform; multi_domain_equation_discovery
证据强度：medium_high
归类置信度：medium_high
纳入置信度：high
推荐引用强度：standard
```


## 2026-10-29 三级分类复核

- 归档分类：`02.02.03` 经典力学；二级：`02.02`。
- 原文位置：PDF pp.6,8。
- 判定：Concrete experiment/task evidence supports 02.02.03 (经典力学). Figure 4: Equations discovered for the PO10 and PO37 physics problems. The variables ... represent acceleration in a non-linear harmonic oscillator, time, position, and velocity, respectively.
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O2 既定基准 | 在化学、生物、物理、材料四学科datasets上恢复方程 | “chemistry、biology、physics、material science datasets” · L226 |
| 验证强度 | V2 计算/仿真/回顾性 | 计算验证，比基线高6%到35% | “仿真验证：是” · L216 |
| 系统自主性 | L1 任务助手 | 系统执行equation discovery但主要在benchmark环境 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
