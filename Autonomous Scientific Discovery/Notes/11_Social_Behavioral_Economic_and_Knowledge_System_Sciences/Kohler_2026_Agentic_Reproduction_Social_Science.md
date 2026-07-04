# Kohler et al. 2026 - Read the Paper, Write the Code: Agentic Reproduction of Social-Science Results

**论文信息**
- 标题：Read the Paper, Write the Code: Agentic Reproduction of Social-Science Results
- 作者：Benjamin Kohler; David Zollikofer; Johanna Einsiedler; Alexander Hoyle; Elliott Ash
- 年份：2026
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2604.21965
- PDF / 本地文件路径：`Reference_PDF/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Kohler_2026_Agentic_Reproduction_Social_Science.pdf`
- 论文类型：研究论文 / reproducibility agent system
- 当前状态：to_read；2026-07-04 local-PDF full-text writeback completed
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

## Frozen Adjudication Writeback - 2026-07-04

- Final classification: `scientific_object_modules=11`; `object_coverage_mode=single_module`; `primary_module_for_filing=11`; `general_method_bucket=none`.
- Source status: locally archived PDF checked; authoritative round closes with `source_limited=no`.
- Landed subset note: keep the reproducibility-assessment `11.07` reading and do not reopen `11.01`.

## 2026-07-04 Phase6FollowupR15Approx local PDF recheck

- `first_hand_sources_checked`: local archived PDF `Reference_PDF/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Kohler_2026_Agentic_Reproduction_Social_Science.pdf`; arXiv `https://arxiv.org/abs/2604.21965`.
- Current authoritative classification: keep `scientific_object_modules=11`; `object_coverage_mode=single_module`; `primary_module_for_filing=11`; `general_method_bucket=none`.
- Local-PDF finding: the archived PDF is present and readable. The first-page full text directly confirms the title, author block, and reproducibility-assessment framing for social-science results.
- Round effect: the old abstract-led source-limited ceiling is retired; this row now lands with first-hand full-text support while keeping the stable `11.07` reproducibility boundary.

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | abstract / PDF | 系统从 paper methods 提取信息、重写代码、隔离执行并做误差归因 | 高 |
| 科学对象归类 | `11.07` | PDF | 论文明确说关注的是 reproducibility，而不是社会科学内容发现 | 高 |
| 方法流程 | 多步 reproduction pipeline | abstract / PDF | strict information isolation、cell-level comparison、error attribution 构成完整流程 | 高 |
| 评测对象 | 再现性 | PDF | 使用 I4Replication 的 48 篇已验证可重现论文，比较 reproduced outputs 与 original results | 高 |
| 边界判断 | 不应归 `11.01` 或 `01.04` | PDF | 社会科学只是语料来源；真正研究的是 reproducibility diagnosis | 高 |

## 0. 摘要翻译

论文提出一个 paper-to-code 的 agentic reproduction system，目标是在只看方法描述和原始数据、看不到原始代码与结果的条件下，自动重现已发表社会科学论文的结果。系统通过结构化方法抽取、代码重实现、隔离执行与误差归因来判断 reproduction 是否成功。作者强调本文研究的是 reproducibility 本身，而不是经济学或其他社会科学实质内容的发现。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：存在多步结构化 pipeline、工具调用、反馈修正与误差归因
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：部分是
- 在科研流程中承担的明确角色：方法抽取、代码重实现、结果比较、误差归因

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：11
- 二级类：11.07
- 三级类：scientific reproducibility and reproduction diagnostics
- 四级专题：paper-to-code reproduction agents
- 四级专题是否为新增：否
- 归类理由：系统研究对象是 reproducibility / reproduction 这一科学实践本身，而不是社会科学实质问题
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：scientific reproducibility
- 最终科学问题：Agent 能否在严格信息隔离下重现已发表研究结果，并诊断失败来源
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：paper-to-code pipeline 只是方法形式，稳定对象是 reproducibility practice

### 2.3 容易混淆的边界

- 可能误归类到：11.01、01.04
- 最终判定：保留 11.07
- 判定理由：社会科学论文只是测试语料；文章关注的是 reproduction quality、error attribution 与 underspecification
- 是否需要二次复核：否

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：是
- Retrieval-augmented Agent：部分是
- Multi-Agent System：部分是
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：否
- Hybrid Agent：是
- 其他：reproducibility diagnosis pipeline

### 3.2 科研流程角色

- 文献检索与阅读：是
- 知识抽取与知识组织：是
- 科学问题提出：否
- 假设生成：否
- 实验设计：是
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
- 多 Agent 协作：部分是
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
- 其他：strict information isolation

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：自动 reproduction 能帮助理解 scientific reporting 与 reproducibility 的真实边界
- 现有科研流程或方法的痛点：普通 code generation 难以处理方法描述中的模糊性与缺漏
- 核心假设或直觉：若在严格信息隔离下让 Agent 重建分析流程，就能更清楚识别失败来自 agent 还是论文描述不足

### 4.2 系统流程

1. 输入：paper methods description 与 original data
2. 任务分解 / 规划：抽取步骤、重建分析计划
3. 工具、数据库、模型或实验平台调用：执行代码重实现与隔离运行
4. 中间结果反馈：对 reproduced outputs 做 deterministic cell-level comparison
5. 决策或迭代：根据差异追踪 root causes
6. 输出：reproduction result 与 discrepancy diagnosis

### 4.3 系统组件

- Agent 核心：agentic reproduction system
- 工具 / API / 数据库：code execution environment、comparison pipeline
- 记忆或状态模块：reproduction state 与 discrepancy records
- 规划器：paper-to-code decomposition
- 评估器 / verifier：cell-level deterministic comparison
- 人类反馈或专家介入：无
- 实验平台或仿真环境：I4Replication paper set

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：否
- 高通量计算：否
- 机器人实验：否
- 湿实验：否
- 临床数据：否
- 真实场景部署：否
- 专家评估：是

### 5.2 数据、任务与指标

- 数据集 / 实验对象：I4Replication 的 48 篇社会科学论文
- 任务设置：在 strict information isolation 下重现 original results
- 对比基线：不同 reproduction settings
- 评价指标：deterministic cell-level match、error attribution、failure sources
- 关键结果：论文区分了 agent errors 与 paper underspecification
- 是否有消融实验：当前摘要级笔记未细写
- 是否有失败案例或负结果：有，且是核心分析内容

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：更偏 reproducibility diagnosis 平台
- 科学贡献是否经过验证：是
- 贡献强度判断：中高
- 科学贡献类型：system_platform / reproducibility_analysis
- 证据强度：中高

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：最终对象不是社会科学问题，而是已发表结果的再现性
- 与已有 Agent / 科研智能系统的区别：强调 strict information isolation 和 discrepancy root-cause attribution
- 与同一科学领域其他 Agent 文献的关系：可与 CiteME、TreeReview、APRES 一起构成 `11.07` scholarly evaluation / reproducibility 分支
- 主要创新点：把 paper-to-code reproduction 与 scientific reproducibility diagnosis 一起实现

## 7. 局限性与风险

- Agent 自主性不足：受方法描述质量和 LLM coding 能力限制
- 科学验证不足：当前集中在社会科学语料
- 泛化性不足：不同学科的再现性难度可能差异很大
- 工具链依赖：代码执行与对比流水线必须稳定
- 数据泄漏或 benchmark 偏差：reproducible subset 的选择会影响结论
- 成本、可复现性或安全风险：自动重现错误分析有较高工程与解释成本
- 是否仍需进一步全文复核：否

## 8. 对综述写作的价值

- 可放入哪个章节：scientific reproducibility agents
- 可支撑哪个论点：如果论文研究的是 reproducibility itself，应归 `11.07`，即便语料来自社会科学
- 可用于哪个表格或图：reproducibility / peer-review / citation attribution agents 对照表
- 适合作为代表性案例吗：是
- 推荐引用强度：核心引用
- 需要在正文中特别引用的页码 / 图 / 表：strict information isolation 与 root-cause attribution 说明
- 需要与哪些论文并列比较：ASD-0629、ASD-0655

## 9. 总结

### 9.1 一句话概括

在严格隔离下自动重现社会科学论文结果并诊断差异。

### 9.2 速记版 pipeline

1. 读论文方法描述
2. 重建代码与分析步骤
3. 跑结果并逐单元比对
4. 追踪失败根因

### 9.3 标注字段汇总

```text
是否纳入：是
主类：11
二级类：11.07
三级类：scientific reproducibility and reproduction diagnostics
四级专题：paper-to-code reproduction agents
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Hybrid Agent
科研流程角色：literature_search_and_reading; knowledge_extraction_and_organization; experimental_design; tool_use_and_code_execution; data_analysis; result_interpretation; evidence_assessment_and_validation; end_to_end_research_automation
自主能力：task_decomposition; planning; tool_use; memory_or_state_tracking; feedback_iteration; autonomous_decision_making; environment_interaction
验证方式：benchmark; expert_evaluation
交叉属性：computation_driven; data_driven
科学贡献类型：system_platform
证据强度：medium_high_primary_abstract
归类置信度：高
纳入置信度：高
推荐引用强度：核心引用
```
