# Feng et al. 2025 - Earth-Agent: Unlocking the Full Landscape of Earth Observation with Agents

**论文信息**
- 标题：Earth-Agent: Unlocking the Full Landscape of Earth Observation with Agents
- 作者：Peilin Feng; Zhutao Lv; Junyan Ye; Xiaolei Wang; Xinjie Huo; Jinhua Yu; Wanghan Xu; Wenlong Zhang; Lei Bai; Conghui He; Weijia Li
- 年份：2025
- 来源 / venue：arXiv / ICLR 2026 conference paper
- DOI / arXiv / URL：https://arxiv.org/abs/2509.23141
- PDF / 本地文件路径：`Reference_PDF/05_Earth_and_Environmental_Sciences/Feng_2025_Earth_Agent.pdf`
- 论文类型：预印本 / Earth observation agent system
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Frozen Adjudication Writeback - 2026-07-04

- Final classification: `scientific_object_modules=05`; `object_coverage_mode=single_module`; `primary_module_for_filing=05`; `general_method_bucket=none`.
- Source status: locally archived conference/arXiv full text checked; authoritative round closes with `source_limited=no`.
- Landed subset note: keep the Earth-observation object reading focused on EO scientific tasks and Earth-Bench rather than reopening an independent `01.04` framing.

## Evidence Log

## 2026-07-04 Phase6FollowupR12Approx local PDF recheck

- `first_hand_sources_checked`: local archived conference/arXiv PDF `Reference_PDF/05_Earth_and_Environmental_Sciences/Feng_2025_Earth_Agent.pdf`; landing page `https://arxiv.org/abs/2509.23141`.
- Current authoritative classification: keep `scientific_object_modules=05`; `object_coverage_mode=single_module`; `primary_module_for_filing=05`; `general_method_bucket=none`.
- Local-PDF finding: the archived PDF is present and readable. The full text confirms EO-specific tool invocation, quantitative spatiotemporal reasoning, and Earth-Bench as a benchmark anchored on Earth-observation scientific tasks.
- Round effect: the old abstract-plus-GitHub ceiling is retired; this row now lands with first-hand full-text support while keeping the stable `05.04` Earth-observation anchor.

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | arXiv abstract | 系统进行 cross-modal、multi-step、quantitative spatiotemporal reasoning，不是静态 MLLM | 高 |
| 科学对象归类 | `05.04` | abstract | 任务明确是 geophysical parameter retrieval 与 Earth observation quantitative analysis | 高 |
| 方法流程 | 工具生态闭环 | abstract / GitHub | 在 MCP-based tool ecosystem 中执行 tool calling、memory update、deliberation 和 action | 高 |
| 工具绑定对象 | 很强 | GitHub README | 集成 104 个 specialized tools，覆盖 Index、Inversion、Perception、Analysis、Statistics 五类 EO 工具 | 高 |
| 实验验证 | Earth-Bench | arXiv / GitHub | Earth-Bench 含 248 个 expert-curated tasks、13,729 images，并做结果级与轨迹级评估 | 高 |

## 0. 摘要翻译

论文提出 Earth-Agent，用于统一 RGB 与 spectral EO data，并在 Agent 工具生态中完成 quantitative spatiotemporal reasoning。系统围绕 geophysical parameter retrieval、Earth system state understanding 和跨模态地理空间分析设计。作者构建 Earth-Bench，对系统的结果正确性和推理轨迹做双层评估，并报告其明显优于 general agents 和 remote-sensing MLLMs。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：系统具备多步推理、动态工具调用、状态更新和复杂 EO 任务执行
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：部分是
- 在科研流程中承担的明确角色：参数反演、时空定量分析、结果解释、轨迹推理

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：05
- 二级类：05.04
- 三级类：遥感与 Earth observation quantitative reasoning
- 四级专题：full-landscape EO agents
- 四级专题是否为新增：否
- 归类理由：对象、任务、工具、评测和贡献都深度绑定 Earth observation 与 geophysical parameter retrieval
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：Earth observation / geophysical parameter retrieval / quantitative EO analysis
- 最终科学问题：如何让 Agent 处理多模态 EO 数据并完成量化时空分析
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：MCP 工具生态和 ReAct-style loop 只是方法形式，稳定对象是 EO scientific tasks

### 2.3 容易混淆的边界

- 可能误归类到：01.04
- 最终判定：保留 05.04
- 判定理由：Earth-Bench 的任务和工具都不是领域无关 benchmark，而是 EO-specific scientific tasks
- 是否需要二次复核：否，`Phase6FollowupR12Approx` 已以本地全文再次确认主类和对象锚点

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：部分是
- Multi-Agent System：否
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：部分是
- Hybrid Agent：是
- 其他：ReAct-style EO tool agent

### 3.2 科研流程角色

- 文献检索与阅读：否
- 知识抽取与知识组织：部分是
- 科学问题提出：否
- 假设生成：否
- 实验设计：否
- 仿真建模：否
- 工具调用与代码执行：是
- 实验执行：否
- 数据分析：是
- 结果解释：是
- 证据评估与假设验证：是
- 论文写作：否
- 端到端科研流程自动化：是

### 3.3 自主能力

- 任务分解：是
- 计划生成：是
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
- 多模态：是
- 多尺度建模：部分是
- 高通量筛选：否
- 知识图谱：否
- 数字孪生：否
- 机器人平台：否
- 其他：remote sensing tool ecosystem

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：传统 remote-sensing MLLM 难以完成长链 quantitative EO reasoning
- 现有科研流程或方法的痛点：RGB 与 spectral 数据分裂，专用工具众多，单模型难以统一执行
- 核心假设或直觉：如果把多模态 EO 数据和专业工具放进可推理的 Agent loop，就能提升地学任务完成度

### 4.2 系统流程

1. 输入：EO scientific task
2. 任务分解 / 规划：根据任务需要制定多步 reasoning plan
3. 工具、数据库、模型或实验平台调用：调用 104 个 specialized EO tools 中的合适组件
4. 中间结果反馈：更新记忆和中间推理状态
5. 决策或迭代：继续调用工具或修正分析方向
6. 输出：定量 EO result 与 reasoning trajectory

### 4.3 系统组件

- Agent 核心：Earth-Agent
- 工具 / API / 数据库：Index、Inversion、Perception、Analysis、Statistics 五类 specialized EO tools
- 记忆或状态模块：ReAct-style memory update
- 规划器：deliberation + action loop
- 评估器 / verifier：Earth-Bench result-level 与 trajectory-level evaluation
- 人类反馈或专家介入：task curation
- 实验平台或仿真环境：Earth-Bench

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：否
- 高通量计算：否
- 机器人实验：否
- 湿实验：否
- 临床数据：否
- 真实场景部署：部分是
- 专家评估：是

### 5.2 数据、任务与指标

- 数据集 / 实验对象：Earth-Bench，248 个任务，13,729 张图像
- 任务设置：spectrum、products、RGB 三种模态下的 EO scientific tasks
- 对比基线：general agents 与 remote-sensing MLLMs
- 评价指标：final answer correctness 与 reasoning trajectory quality
- 关键结果：Earth-Agent 显著优于 general agents，并超过专门 remote-sensing MLLMs
- 是否有消融实验：当前笔记尚未系统抽取全文中的消融细节
- 是否有失败案例或负结果：当前摘要未详细展开

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：更偏 EO scientific workflow system
- 科学贡献是否经过验证：是
- 贡献强度判断：中高
- 科学贡献类型：系统平台
- 证据强度：high_full_text_checked

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不只是多模态 perception，而是完整的 EO tool-using reasoning agent
- 与已有 Agent / 科研智能系统的区别：统一 RGB、spectral 与 quantitative geoscientific reasoning
- 与同一科学领域其他 Agent 文献的关系：可与 OpenEarth-Agent 形成一组 `05.04` 强代表样本
- 主要创新点：把 EO task object、tool ecosystem 与 reasoning trajectory evaluation 统一起来

## 7. 局限性与风险

- Agent 自主性不足：当前主要证据仍来自 benchmark 和 repo
- 科学验证不足：尚未展示真实 Earth-science 发现闭环
- 泛化性不足：工具生态扩展性仍需持续观察
- 工具链依赖：高度依赖 specialized EO tools
- 数据泄漏或 benchmark 偏差：expert-curated benchmark 可能影响表现上限
- 成本、可复现性或安全风险：完整 tool ecosystem 的复现成本较高
- 是否仍需进一步全文复核：否；当前 authoritative source status 已升级为 first-hand full text

## 8. 对综述写作的价值

- 可放入哪个章节：Earth observation agents
- 可支撑哪个论点：平台感强不必然归 `01.04`，只要 scientific object 稳定锚定 EO，就应归 `05`
- 可用于哪个表格或图：EO agent 代表系统对照表
- 适合作为代表性案例吗：是
- 推荐引用强度：核心引用
- 需要在正文中特别引用的页码 / 图 / 表：Earth-Bench 任务构成与 tool ecosystem 概述
- 需要与哪些论文并列比较：ASD-0650、ASD-0851

## 9. 总结

### 9.1 一句话概括

把多模态 EO 数据和专业工具接入定量推理 Agent。

### 9.2 速记版 pipeline

1. 读取 EO 任务
2. 规划多步分析链
3. 调用专用 EO 工具
4. 输出结果并检查轨迹

### 9.3 标注字段汇总

```text
是否纳入：是
主类：05
二级类：05.04
三级类：遥感与 Earth observation quantitative reasoning
四级专题：full-landscape EO agents
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Hybrid Agent
科研流程角色：knowledge_extraction_and_organization; tool_use_and_code_execution; data_analysis; result_interpretation; evidence_assessment_and_validation; end_to_end_research_automation
自主能力：task_decomposition; planning; tool_use; memory_or_state_tracking; feedback_iteration; autonomous_decision_making; environment_interaction
验证方式：benchmark; expert_evaluation
交叉属性：computation_driven; data_driven; multimodal
科学贡献类型：system_platform
证据强度：medium_high_primary_abstract
归类置信度：高
纳入置信度：高
推荐引用强度：核心引用
```
