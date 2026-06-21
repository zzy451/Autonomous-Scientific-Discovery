# Xiang et al. 2025 - SciReplicate-Bench

**论文信息**
- 标题：SciReplicate-Bench: Benchmarking LLMs in Agent-driven Algorithmic Reproduction from Research Papers
- 作者：Xiang et al.
- 年份：2025
- 来源 / venue：COLM 2025 / arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2504.00255
- PDF / 本地文件路径：`Reference_PDF/01_Formal_Information_and_Computational_Sciences/Xiang_2025_SciReplicate_Bench.pdf`
- First-hand source checked：arXiv abstract；arXiv HTML full text；official benchmark page
- PDF version：official arXiv PDF
- Source-limited status：no
- 论文类型：benchmark / dual-agent scientific reproduction framework
- 当前状态：to_read
- 阅读与复核日期：2026-06-22
- 笔记作者：Codex

## Evidence Log

### 2026-06-22 reaudit writeback revision

- Round decision：将旧的 `01.04` / `11` 漂移结论收束为 `scientific_object_modules=01`。
- Archive sync：已确认并写回本地 PDF 路径 `Reference_PDF/01_Formal_Information_and_Computational_Sciences/Xiang_2025_SciReplicate_Bench.pdf`。
- Source note：本条不是 source-limited 记录；当前写回基于已核对的一手来源，而不是旧 note 推断。
- Policy note：论文虽然与 scientific reproducibility 评测话题相邻，但当前稳定对象是算法复现、代码生成、测试执行与计算研究工作流，因此保留在 `01`；可重复性只作为边界说明，不再作为 `11` 或独立 `01.04` 的最终分类事实。

证据级别：first_hand_full_text

| 判断项 | 结论 | 证据位置 | 证据摘要 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | arXiv abstract；HTML full text | 论文提出 Paper Agent 与 Coding Agent 协同完成 paper-to-code reproduction | 高 |
| 科学对象归类 | `01` | arXiv abstract；方法与 benchmark 描述；official benchmark page | 直接评测算法理解、代码实现、测试执行与计算复现任务，稳定对象是 formal / computational research activity | 中高 |
| 方法流程 | paper understanding -> algorithm decomposition -> code generation -> test execution -> metric evaluation | arXiv HTML full text | 系统围绕科研算法复现而非通用科学工作流展开 | 高 |
| 实验验证 | 36 篇 2024 NLP papers 构成的 100 个 algorithmic reproduction tasks | arXiv abstract；benchmark page | benchmark 以真实论文复现任务为对象，但对象层面仍属于计算 / 算法研究 | 中高 |
| 边界判断 | 不再保留 `11` 或独立 `01.04` | 全部一手来源综合 | reproducibility overlap 存在，但它不是本轮最终对象模块事实，只保留为边界注记 | 中 |

## 0. 摘要概述

SciReplicate-Bench 评测 LLM 在“从科研论文中复现算法实现”这一任务上的能力。作者构建了来自 36 篇 2024 年 NLP 论文的 100 个复现任务，并提出由 Paper Agent 与 Coding Agent 组成的 dual-agent 框架，用 reasoning graph accuracy、test pass rate 等指标衡量论文理解与代码实现质量。当前口径下，它不是“没有具体对象实验的通用 ASD benchmark”，而是一个明确面向算法复现与计算研究任务的 `01` 类记录。

## 1. 是否纳入本综述

- 是否属于 Agent 文献：是
- 判断依据：系统面向明确科研目标，具有多步动作过程，包含工具调用与双 Agent 协作，并在科研流程中承担算法复现角色
- 判定置信度：高
- 科研流程角色：knowledge_extraction_and_organization；tool_use_and_code_execution；evidence_assessment_and_validation

## 2. 科学领域归类

- 最终科学对象模块：`01`
- primary_module_for_filing：`01`
- general_method_bucket：`none`
- 对象覆盖方式：single-module
- 描述性子方向：algorithmic reproduction / paper-to-code scientific benchmarking
- 最终科学研究对象：算法描述、代码实现、测试执行与计算研究复现
- 最终科学问题：Agent 能否从研究论文中稳定恢复可运行的算法实现

### 边界讨论

- 容易混淆的边界：`01.04` general benchmark；`11.07` scientific reproducibility / knowledge-production evaluation
- 最终判定：稳定保留 `01`
- 判定理由：当前 relaxed 规则要求按具体对象与验证任务归类。本文的实验对象不是 scientific knowledge production itself，也不是无对象的通用 scientific-agent workflow，而是具体的算法复现与代码执行任务。
- 备注：可重复性话题保留为边界注记，不再写成最终 `11` 模块事实。

## 3. Agent 系统与科研流程角色

- Agent 类型标签：LLM Agent；Tool-using Agent；Multi-Agent System；Hybrid Agent
- 科研流程角色：knowledge_extraction_and_organization；tool_use_and_code_execution；evidence_assessment_and_validation
- 自主能力：task_decomposition；planning；tool_use；feedback_iteration；multi_agent_collaboration；environment_interaction
- 交叉属性标签：computation_driven；benchmark

## 4. 方法设计

1. 读取论文与参考实现上下文。
2. 由 Paper Agent 解析算法逻辑与实现要求。
3. 由 Coding Agent 生成代码并调用测试环境。
4. 用 reasoning graph accuracy、test pass rate 等指标衡量理解与实现质量。
5. 输出算法复现结果与 benchmark 评测。

## 5. 实验与验证

- 验证方式：benchmark
- 数据与任务：100 个来自 36 篇 2024 NLP 论文的 algorithmic reproduction tasks
- 关键结果：论文指出模型在“理解算法”与“正确实现代码”之间仍存在明显落差
- 科学贡献类型：benchmark；system_platform
- 证据强度：first_hand_full_text

## 6. 与已有工作的关系

- 与一般 coding benchmark 的区别：这里的任务入口是科研论文中的算法复现，而不是普通编程题。
- 与通用 scientific-agent 平台的区别：本文重点是 paper-to-code reproduction benchmark，不是无对象的科研工作流总框架。
- 对当前综述的价值：可作为 `01` 模块中“计算研究对象上的 Agent 复现与评测”代表样本。

## 7. 局限性与风险

- benchmark 主要来自 NLP / algorithmic papers，领域覆盖仍偏窄。
- 论文贡献主要是评测与复现框架，不是新科学发现。
- 与 scientific reproducibility 议题存在邻接性，容易被旧口径误写为 `11`；本轮已收束为边界说明而非最终分类。

## 8. 对综述写作的价值

- 适合放入 `01` 形式、信息与计算科学章节。
- 可支持“Agent 已能承担计算研究对象上的算法复现与证据评估任务”这一论点。
- 也适合在 benchmark 小节中与 CodeScientist、ResearchCodeAgent 等记录并列比较。

## 9. 总结

### 9.1 一句话概括

SciReplicate-Bench 是一个面向科研论文算法复现的 Agent benchmark，当前稳定归入 `01`，不再保留 `01.04` 或 `11` 漂移表述。

### 9.2 速记字段

```text
是否纳入：是
scientific_object_modules：01
primary_module_for_filing：01
general_method_bucket：none
object_coverage_mode：single_module
描述性子方向：algorithmic reproduction / paper-to-code scientific benchmarking
Agent 类型：LLM Agent; Tool-using Agent; Multi-Agent System; Hybrid Agent
科研流程角色：knowledge_extraction_and_organization; tool_use_and_code_execution; evidence_assessment_and_validation
自主能力：task_decomposition; planning; tool_use; feedback_iteration; multi_agent_collaboration; environment_interaction
验证方式：benchmark
科学贡献类型：benchmark; system_platform
证据强度：first_hand_full_text
source_limited：no
归类置信度：medium
纳入置信度：high
推荐引用强度：core
```
