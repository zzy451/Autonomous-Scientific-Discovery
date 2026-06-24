# Wang et al. 2026 - ClimAgent: LLM as Agents for Autonomous Open-ended Climate Science Analysis

**论文信息**
- 标题：ClimAgent: LLM as Agents for Autonomous Open-ended Climate Science Analysis
- 作者：Hao Wang; Jindong Han; Wei Fan; Hao Liu
- 年份：2026
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2604.16922 ; HTML full text: https://arxiv.org/html/2604.16922v2
- PDF / 本地文件路径：`Autonomous Scientific Discovery/Reference_PDF/05_Earth_and_Environmental_Sciences/Wang_2026_ClimAgent.pdf`；已归档并核对 versioned official arXiv PDF v2（`https://arxiv.org/pdf/2604.16922v2`）与 official arXiv HTML full text；non-versioned `https://arxiv.org/pdf/2604.16922` 返回 `404`，不是成功归档来源；v3 landing 仍为 withdrawn
- 论文类型：预印本 / climate-science agent system
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## 2026-06-24 Direct-Landing Refresh

- Final adjudication: `yes_direct_landing`
- Supported modules: `05`
- `final_01_04_bucket`: `none`
- `primary_module_for_filing`: `05`
- Boundary type: `withdrawn-record / versioned-v2 lineage pressure, not 05-direction instability`
- Confidence: `high`
- `source_limited`: `no`
- Safety / access status: `no_safety_skip`; official arXiv HTML full text at `https://arxiv.org/html/2604.16922v2` and versioned official arXiv PDF v2 at `https://arxiv.org/pdf/2604.16922v2` were available and checked, while the v3 landing remains withdrawn as of `2026-06-24`.
- Source status refresh: official HTML full text and the archived versioned official PDF v2 now form the decisive first-hand source package; the successful archive source was `https://arxiv.org/pdf/2604.16922v2`, while non-versioned `https://arxiv.org/pdf/2604.16922` returned `404`.
- Repo status refresh: the cited repo remains broken / `404`, and the visible public repo state is still a placeholder rather than a substantive paper-supporting release.
- Inclusion wording refresh: this now crosses the direct-landing threshold because the official arXiv HTML full text plus the archived versioned official PDF v2 provide strong first-hand support for an Agent-oriented climate-science workflow rather than a single-turn model paper.
- Classification wording refresh: concrete climate-science task, environment, tool, and benchmark coverage support `05` directly rather than `01.04`; the platform / benchmark surface does not override the Earth-science object landing.
- Risk wording refresh: withdrawn v3 lineage and broken cited repo still add reproducibility pressure, but they do not overturn the `05` landing because both the official HTML full text and the archived versioned official PDF v2 are available.

## Evidence Log

### 2026-06-24 Evidence Refresh

- First-hand source summary checked this round: withdrawn arXiv landing page, official arXiv HTML full text at `https://arxiv.org/html/2604.16922v2`, versioned official arXiv PDF v2 at `https://arxiv.org/pdf/2604.16922v2`, and accessible arXiv abstract / landing-page metadata.
- Official source status as of `2026-06-24`: official HTML full text is available; versioned official arXiv PDF v2 is available and archived locally at `Autonomous Scientific Discovery/Reference_PDF/05_Earth_and_Environmental_Sciences/Wang_2026_ClimAgent.pdf`; non-versioned `https://arxiv.org/pdf/2604.16922` returned `404`; v3 landing remains withdrawn.
- Repo status as of `2026-06-24`: cited repo broken / `404`; public repo only placeholder and not a substantive release.
- Classification remains anchored in concrete climate-science tasks and environment coverage, so the supported module stays `05` rather than `01.04`.
- This note now lands directly with `confidence=high` and `source_limited=no`, while preserving explicit withdrawn-v3 lineage and repo-breakage risk wording.

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是，直接落地 | arXiv abstract / HTML / PDF v2 | 系统不是单轮问答，而是面向开放式 climate science analysis 的端到端 agent workflow | 高 |
| 科学对象归类 | `05.02` | 标题；HTML | 任务、工具、数据库和 benchmark 都锚定 climate science | 高 |
| 方法流程 | 明确多步 | HTML | 系统会做任务分解、工具选择、代码执行、分析与报告生成 | 高 |
| 工具 / 环境约束 | 强 climate specialization | HTML | Climate Environment 覆盖 `25` 个子领域、`150` 个工具、`30` 个数据库 | 高 |
| 实验验证 | benchmark + 专家复核 | HTML | ClimaBench 覆盖 `2000-2025` 的真实 climate 场景，共 `220` 个开放问题 | 高 |
| 证据风险 | withdrawn | arXiv abstract page | arXiv 页面明确标记 withdrawn，原因与合作者同意有关 | 高 |

## 0. 摘要翻译

论文提出 ClimAgent，用于开放式气候科学分析。系统把 climate science 研究任务拆分为多个可执行子任务，并在 climate-specific 工具、数据库和知识环境中自主完成建模、代码生成、分析和报告输出。作者同时构建了 ClimaBench，用真实气候问题评估 agent 系统在开放式地学分析中的能力。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是，暂定纳入
- 判断依据：系统围绕明确 climate-science 研究目标执行多步工作流，具备计划生成、工具调用、代码执行和反馈组织
- 判定置信度：中高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：部分是
  - 自主决策：是
  - 多 Agent 协作：未强调为主
- 在科研流程中承担的明确角色：问题分解、数据分析、模型执行、结果汇总、报告生成

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除，但要显式记录 withdrawn 风险

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：05
- 二级类：05.02
- 三级类：气候科学分析与开放问题研究
- 四级专题：climate-science specialized agent workflow
- 四级专题是否为新增：否
- 归类理由：系统的 benchmark、工具链、数据库和案例都稳定指向 climate science
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：开放式 climate science analysis
- 最终科学问题：如何让 agent 在气候科学中自主完成多步分析与发现流程
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：虽然有 platform / benchmark 外观，但其环境与问题集不是领域无关 workflow

### 2.3 容易混淆的边界

- 可能误归类到：01.04
- 最终判定：保留 05.02
- 判定理由：领域环境、任务和验证均强绑定气候科学，而非通用科研 Agent
- 是否需要二次复核：是

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：部分是
- Multi-Agent System：未明确为核心卖点
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：部分是
- Hybrid Agent：是
- 其他：climate-specialized analysis workflow

### 3.2 科研流程角色

- 文献检索与阅读：部分是
- 知识抽取与组织：是
- 科学问题提出：部分是
- 假设生成：是
- 实验设计：否
- 仿真建模：是
- 工具调用与代码执行：是
- 实验执行：否
- 数据分析：是
- 结果解释：是
- 证据评估与验证：部分是
- 论文写作：部分是
- 端到端科研流程自动化：是

### 3.3 自主能力

- 任务分解：是
- 计划生成：是
- 工具调用：是
- 记忆与状态维护：部分是
- 反馈迭代：部分是
- 自主决策：是
- 多 Agent 协作：未突出
- 环境交互：是
- 闭环实验：否

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 实验驱动：否
- 仿真驱动：是
- 多模态：部分是
- 多尺度建模：部分是
- 高通量筛选：否
- 知识图谱：否
- 数字孪生：否
- 机器人平台：否
- 其他：climate database + tool ecosystem

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：开放式气候科学分析需要跨工具、跨数据库、跨任务组织
- 现有科研流程或方法的痛点：普通 LLM 难以稳定调用 climate-specific tools 并形成完整分析链
- 核心假设或直觉：给 LLM 提供 climate-specific environment 后，可显著提升开放式气候分析能力

### 4.2 系统流程

1. 输入：开放式气候科学问题
2. 任务分解 / 规划：拆解为数据获取、建模、分析、解释等子任务
3. 工具、数据库、模型或实验平台调用：调用 climate-specific tools、databases 与代码环境
4. 中间结果反馈：汇总分析结果并根据需要修正流程
5. 决策或迭代：继续执行剩余子任务
6. 输出：分析结果与报告

### 4.3 系统组件

- Agent 核心：climate-science LLM agent workflow
- 工具 / API / 数据库：Climate Environment 中的专用工具和数据库
- 记忆或状态模块：任务上下文与中间分析状态
- 规划器：有
- 评估器 / verifier：ClimaBench 与专家复核
- 人类反馈或专家介入：专家评估
- 实验平台或仿真环境：climate analysis / modeling environment

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：部分是
- 高通量计算：否
- 机器人实验：否
- 湿实验：否
- 临床数据：否
- 真实场景部署：否
- 专家评估：是

### 5.2 数据、任务与指标

- 数据集 / 实验对象：ClimaBench，`220` 个开放问题
- 任务设置：开放式 climate science analysis
- 对比基线：普通 LLM / 非 climate-specialized workflows
- 评价指标：任务完成质量与专家评估
- 关键结果：论文声称 climate-specialized environment 能提升任务表现
- 是否有消融实验：摘要级证据未完全展开
- 是否有失败案例或负结果：withdrawn 本身构成显著风险信号

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：更偏 climate-specialized research workflow 与分析能力
- 科学贡献是否经过验证：有 benchmark 和专家评估支撑
- 贡献强度判断：中
- 科学贡献类型：system_platform
- 证据强度：受 withdrawn 风险影响，当前只能视为中等

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单次问答，而是气候科学专用多步 Agent
- 与已有 Agent / 科研智能系统的区别：强调 climate-specific environment 与开放式 benchmark
- 与同一科学领域其他 Agent 文献的关系：可与 EarthLink、TianJi、PANGAEA-GPT 并列比较
- 主要创新点：把 climate tools、databases 和开放问题组织进一个可执行环境

## 7. 局限性与风险

- Agent 自主性不足：摘要级证据尚不足以完全证明高强度科研自治
- 科学验证不足：主要依赖 benchmark
- 泛化性不足：是否能迁移到更多气候任务仍需观察
- 工具链依赖：强依赖专门气候工具环境
- 数据泄漏或 benchmark 偏差：开放式 benchmark 设计细节仍需全文核查
- 成本、可复现性或安全风险：最重要的风险是论文已 withdrawn

## 8. 对综述写作的价值

- 可放入哪个章节：地球与环境科学中的气候分析 Agent
- 可支撑哪个论点：`05 / 01.04` 边界下，domain-specific environment 可把系统稳定留在 `05`
- 可用于哪个表格或图：地球科学 Agent 边界样本表
- 适合作为代表性案例吗：谨慎，仅适合作为边界与风险样本
- 推荐引用强度：普通引用
- 需要在正文中特别引用的页码 / 图 / 表：后续需在正式写作中标注 withdrawn
- 需要与哪些论文并列比较：ASD-0632、ASD-0633、ASD-0635

## 9. 总结

### 9.1 一句话概括

气候科学专用 Agent 工作流；现已凭 official arXiv HTML full text 与 archived official PDF v2 达到 direct landing，但仍需显式保留 withdrawn v3 与版本谱系风险。

### 9.2 速记版 pipeline

1. 输入气候科学问题  
2. 拆解子任务  
3. 调用 climate tools 与数据库  
4. 分析并生成结果报告

### 9.3 标注字段汇总

```text
是否纳入：是，直接落地
主类：05
二级类：05.02
三级类：气候科学分析与开放问题研究
四级专题：climate-science specialized agent workflow
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Hybrid Agent
科研流程角色：knowledge_extraction_and_organization; hypothesis_generation; simulation_modeling; tool_use_and_code_execution; data_analysis; result_interpretation; end_to_end_research_automation
自主能力：task_decomposition; planning; tool_use; feedback_iteration; autonomous_decision_making; environment_interaction
验证方式：benchmark; expert_evaluation
交叉属性：computation_driven; data_driven; simulation_driven
科学贡献类型：system_platform
证据强度：first_hand_pdf_and_html_full_text
归类置信度：高
纳入置信度：高
推荐引用强度：standard
```

### 2026-06-24 Annotation Refresh

```text
final_agent_inclusion: yes_direct_landing
supported_modules: 05
final_01_04_bucket: none
primary_module_for_filing: 05
boundary_type: withdrawn-record / versioned-v2 lineage pressure, not 05-direction instability
confidence: high
source_limited: no
safety_access_status: no_safety_skip; official arXiv HTML full text and versioned official arXiv PDF v2 were available and checked, while the v3 landing remains withdrawn as of 2026-06-24
master_update_required: yes
source_status: archived local PDF at Autonomous Scientific Discovery/Reference_PDF/05_Earth_and_Environmental_Sciences/Wang_2026_ClimAgent.pdf; successful official archive source was https://arxiv.org/pdf/2604.16922v2; official HTML full text checked at https://arxiv.org/html/2604.16922v2; non-versioned https://arxiv.org/pdf/2604.16922 returned 404; withdrawn v3 landing still exists; cited repo broken/404; public repo only placeholder and not substantive
final_reason: This crosses the direct-landing threshold because official arXiv HTML full text and the archived official v2 PDF provide strong first-hand source support for clear concrete climate/Earth-science task evidence in 05; the withdrawn v3 lineage and repo breakage add reproducibility pressure but do not overturn the classification landing.
```
