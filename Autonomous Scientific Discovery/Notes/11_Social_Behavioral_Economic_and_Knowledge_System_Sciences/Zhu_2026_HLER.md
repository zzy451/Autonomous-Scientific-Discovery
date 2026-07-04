# Zhu and Wang 2026 - HLER: Human-in-the-Loop Economic Research via Multi-Agent Pipelines for Empirical Discovery

**论文信息**
- 标题：HLER: Human-in-the-Loop Economic Research via Multi-Agent Pipelines for Empirical Discovery
- 作者：Chen Zhu; Xiaolu Wang
- 年份：2026
- 来源 / venue：arXiv / SSRN working-paper style
- DOI / arXiv / URL：https://arxiv.org/abs/2603.07444
- PDF / 本地文件路径：`Reference_PDF/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Zhu_2026_HLER.pdf`
- 论文类型：研究论文 / empirical economics multi-agent pipeline
- 当前状态：to_read；2026-07-04 local-PDF full-text writeback completed
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

## Frozen Adjudication Writeback - 2026-07-04

- Final classification: `scientific_object_modules=11`; `object_coverage_mode=single_module`; `primary_module_for_filing=11`; `general_method_bucket=none`.
- Source status: locally archived PDF checked; authoritative round closes with `source_limited=no`.
- Landed subset note: keep the empirical-economics `11.01` reading and do not reopen `11.07`.

## 2026-07-04 Phase6FollowupR15Approx local PDF recheck

- `first_hand_sources_checked`: local archived PDF `Reference_PDF/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Zhu_2026_HLER.pdf`; arXiv `https://arxiv.org/abs/2603.07444`.
- Current authoritative classification: keep `scientific_object_modules=11`; `object_coverage_mode=single_module`; `primary_module_for_filing=11`; `general_method_bucket=none`.
- Local-PDF finding: the archived PDF is present and readable. The first-page full text directly confirms the HLER title, author block, and empirical-economics multi-agent pipeline framing.
- Round effect: the old abstract-led source-limited ceiling is retired; this row now lands with first-hand full-text support while keeping the stable economics-facing `11.01` boundary.

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | abstract / PDF | 专门 agents 执行 data auditing、hypothesis generation、econometric analysis、drafting、review | 高 |
| 科学对象归类 | `11.01` | abstract / PDF | 对象明确是 empirical economics and related social sciences，不是 science-of-science | 高 |
| 方法流程 | 多阶段 HITL 流程 | PDF | empirical research 被分解为 structured stages，并有双层反馈回路和 human decision gates | 高 |
| 数据与对象绑定 | 很强 | PDF | dataset-aware hypothesis generation 受变量结构与计量可行性约束 | 高 |
| 边界判断 | 不应归 `01.04` 或 `11.07` | PDF | 研究的不是科研系统本身，而是经济学经验研究问题的发现和计量执行 | 高 |

## 0. 摘要翻译

论文提出 HLER，一个面向经验经济学研究的人类参与式多 Agent 流水线。系统把 empirical research 分解为数据审计、数据画像、问题生成、计量分析、论文草稿和自动审查等阶段，并通过两层反馈回路和 human decision gates 保持可行性与研究质量。其核心不是研究科研流程本身，而是帮助开展基于真实数据的经济学经验研究。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：存在明确的 specialized agents、多步流程、双层反馈回路和 human decision gates
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：部分是
  - 多 Agent 协作：是
- 在科研流程中承担的明确角色：data auditing、hypothesis generation、econometric analysis、manuscript drafting、automated review

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：11
- 二级类：11.01
- 三级类：经验经济学研究自动化
- 四级专题：empirical economics multi-agent pipelines
- 四级专题是否为新增：否
- 归类理由：系统的对象始终是 empirical economics，而不是抽象科研流程或科研共同体本身
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：empirical economic research
- 最终科学问题：如何围绕真实数据结构生成并执行可行的经济学经验研究
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：multi-agent pipeline 只是组织形式，稳定对象是 empirical economics

### 2.3 容易混淆的边界

- 可能误归类到：01.04、11.07
- 最终判定：保留 11.01
- 判定理由：系统不是研究 peer review、reproducibility 或科研共同体，而是做 economics-specific empirical discovery
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
- 其他：econometrics-aware workflow system

### 3.2 科研流程角色

- 文献检索与阅读：部分是
- 知识抽取与知识组织：是
- 科学问题提出：是
- 假设生成：是
- 实验设计：是
- 仿真建模：否
- 工具调用与代码执行：是
- 实验执行：否
- 数据分析：是
- 结果解释：是
- 证据评估与假设验证：是
- 论文写作：是
- 端到端科研流程自动化：是

### 3.3 自主能力

- 任务分解：是
- 计划生成：是
- 工具调用：是
- 记忆与状态维护：是
- 反馈迭代：是
- 自主决策：部分是
- 多 Agent 协作：是
- 环境交互：是
- 闭环实验：否

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 实验驱动：否
- 仿真驱动：否
- 多模态：否
- 多尺度建模：否
- 高通量筛选：否
- 知识图谱：否
- 数字孪生：否
- 机器人平台：否
- 其他：econometric identification constraints

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：经验经济学研究依赖数据结构、变量可用性与计量识别条件，普通研究助手难以稳定适配
- 现有科研流程或方法的痛点：缺少围绕 empirical economics 真实需求的结构化 research decomposition
- 核心假设或直觉：如果让多 Agent 围绕数据结构和识别约束分阶段协作，并保留 HITL 决策门，可提升研究可行性

### 4.2 系统流程

1. 输入：真实经验数据与高层研究意图
2. 任务分解 / 规划：拆成 auditing、profiling、hypothesis generation、econometric analysis、drafting、review
3. 工具、数据库、模型或实验平台调用：执行计量分析与文本生成
4. 中间结果反馈：两层 feedback loops 与 human decision gates 校正研究方向
5. 决策或迭代：修改问题、分析策略或稿件内容
6. 输出：可执行经验研究问题、计量结果与论文草稿

### 4.3 系统组件

- Agent 核心：specialized research agents
- 工具 / API / 数据库：dataset profiling、econometric analysis environment、drafting / review modules
- 记忆或状态模块：研究阶段状态与数据约束
- 规划器：structured stage decomposition
- 评估器 / verifier：automated review 与 human decision gates
- 人类反馈或专家介入：是
- 实验平台或仿真环境：real datasets for empirical economics

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：否
- 高通量计算：否
- 机器人实验：否
- 湿实验：否
- 临床数据：否
- 真实场景部署：部分是
- 专家评估：部分是

### 5.2 数据、任务与指标

- 数据集 / 实验对象：三套经验经济学数据集
- 任务设置：生成 feasible research questions、执行 econometric analysis、产出 end-to-end manuscripts
- 对比基线：非结构化 LLM research pipeline
- 评价指标：question feasibility、econometric execution quality、manuscript completeness
- 关键结果：系统强调 dataset-aware hypothesis generation 与 empirical execution
- 是否有消融实验：当前摘要级笔记未细写
- 是否有失败案例或负结果：当前摘要级笔记未细写

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：更偏经济学经验研究自动化平台
- 科学贡献是否经过验证：是
- 贡献强度判断：中
- 科学贡献类型：系统平台 / social_science_research
- 证据强度：中高

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：这里直接服务 empirical economics，而非 generic research-agent shell
- 与已有 Agent / 科研智能系统的区别：把 econometric feasibility 与 dataset constraints 放到主流程里
- 与同一科学领域其他 Agent 文献的关系：可与 S-Researcher 一起作为 `11` 中一般社会科学对象研究样本
- 主要创新点：将经验经济学结构化为 dataset-aware multi-agent workflow

## 7. 局限性与风险

- Agent 自主性不足：保留人类决策门，说明完全自治仍有限
- 科学验证不足：当前以经验数据集工作流为主，还不是大规模真实研究部署
- 泛化性不足：经验经济学之外的社会科学外推仍需谨慎
- 工具链依赖：强依赖 econometric workflow 和数据质量
- 数据泄漏或 benchmark 偏差：题目可行性与计量结果都受数据集构造影响
- 成本、可复现性或安全风险：真实政策与经济分析场景有较高误用风险
- 是否仍需进一步全文复核：否

## 8. 对综述写作的价值

- 可放入哪个章节：社会科学对象研究中的 Agent
- 可支撑哪个论点：带 workflow 外观的系统，只要主对象是 empirical economics，就应留在 `11.01`
- 可用于哪个表格或图：`11.01 / 11.07 / 01.04` 边界案例表
- 适合作为代表性案例吗：是
- 推荐引用强度：核心引用
- 需要在正文中特别引用的页码 / 图 / 表：specialized agents 与 dual feedback loops 说明
- 需要与哪些论文并列比较：ASD-0644、ASD-0652、ASD-0658

## 9. 总结

### 9.1 一句话概括

用 HITL 多 Agent 流水线做经验经济学研究。

### 9.2 速记版 pipeline

1. 审计和画像数据集
2. 生成可行研究问题
3. 执行计量分析
4. 起草并审查论文

### 9.3 标注字段汇总

```text
是否纳入：是
主类：11
二级类：11.01
三级类：经验经济学研究自动化
四级专题：empirical economics multi-agent pipelines
Agent 类型：LLM Agent; Multi-Agent System; Human-in-the-loop Agent; Hybrid Agent
科研流程角色：knowledge_extraction_and_organization; scientific_question_formulation; hypothesis_generation; experimental_design; tool_use_and_code_execution; data_analysis; result_interpretation; evidence_assessment_and_validation; paper_writing; end_to_end_research_automation
自主能力：task_decomposition; planning; tool_use; memory_or_state_tracking; feedback_iteration; multi_agent_collaboration; environment_interaction
验证方式：benchmark; expert_evaluation
交叉属性：computation_driven; data_driven
科学贡献类型：system_platform
证据强度：medium_high_primary_abstract
归类置信度：高
纳入置信度：高
推荐引用强度：核心引用
```
