# Zhang et al. 2026 - PaperRepro

**论文信息**
- 标题：PaperRepro: Automated Computational Reproducibility Assessment for Social Science Papers
- 作者：Linhao Zhang; Tong Xia; Jinghua Piao; Lizhen Cui; Yong Li
- 年份：2026
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2603.00058
- PDF / 本地文件路径：`Reference_PDF/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Zhang_2026_PaperRepro.pdf`
- 论文类型：系统论文 / reproducibility assessment agent
- 当前状态：to_read；2026-07-04 local-PDF full-text writeback completed
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

## Frozen Adjudication Writeback - 2026-07-04

- Final classification: `scientific_object_modules=11`; `object_coverage_mode=single_module`; `primary_module_for_filing=11`; `general_method_bucket=none`.
- Source status: locally archived PDF checked; authoritative round closes with `source_limited=no`.
- Landed subset note: keep the social-science reproducibility-assessment `11.07` reading and do not reopen `01.04`.

## 2026-07-04 Phase6FollowupR15Approx local PDF recheck

- `first_hand_sources_checked`: local archived PDF `Reference_PDF/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Zhang_2026_PaperRepro.pdf`; arXiv `https://arxiv.org/abs/2603.00058`.
- Current authoritative classification: keep `scientific_object_modules=11`; `object_coverage_mode=single_module`; `primary_module_for_filing=11`; `general_method_bucket=none`.
- Local-PDF finding: the archived PDF is present and readable. The first-page full text directly confirms the PaperRepro title, author block, and social-science reproducibility-assessment framing.
- Round effect: the old abstract-only source-limited ceiling is retired; this row now lands with first-hand full-text support while keeping the stable `11.07` reproducibility boundary.

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | arXiv abstract | two-stage multi-agent approach | 高 |
| 科学对象归类 | `11.07` | arXiv abstract | social science papers 的 reproducibility assessment | 高 |
| 方法流程 | 多步闭环 | arXiv abstract | 执行阶段运行 reproduction package 并改代码；评估阶段基于显式证据判断 | 高 |
| 实验验证 | benchmark 支持 | arXiv abstract | 在 REPRO-Bench / REPRO-Bench-S 上提升明显 | 中高 |
| 边界判断 | 不转 `01.04` | object-first reading | 研究对象是 peer-review / reproducibility-quality control 范畴 | 高 |

## 0. 摘要翻译

PaperRepro 提出一套两阶段多 Agent 流程，用于自动评估社会科学论文的计算可复现性。第一阶段执行复现实验并在必要时修改代码以抓取复现结果，第二阶段基于显式证据判断论文是否可复现，并在 REPRO-Bench 上优于现有基线。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：存在多 Agent 分工、代码执行、证据收集和评估闭环
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：部分是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：是
- 在科研流程中承担的明确角色：复现实验执行、结果抓取、证据判断、reproducibility assessment

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：11
- 二级类：11.07
- 三级类：scientific reproducibility assessment
- 四级专题：social-science reproducibility-assessment agents
- 四级专题是否为新增：否
- 归类理由：最终对象是 scientific reproducibility assessment
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：社会科学论文的计算可复现性
- 最终科学问题：如何自动执行、抓取并评估论文复现结果
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：multi-agent 只是方法，论文真正研究的是 scientific evaluation 过程

### 2.3 容易混淆的边界

- 可能误归类到：01.04
- 最终判定：保留 11.07
- 判定理由：这不是通用科研平台，而是 scientific knowledge production quality control
- 是否需要二次复核：需要 full text 细化，但主类稳定

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：部分是
- Tool-using Agent：是
- Retrieval-augmented Agent：否
- Multi-Agent System：是
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：否
- Hybrid Agent：是
- 其他：reproducibility assessment agents

### 3.2 科研流程角色

- 文献检索与阅读：是
- 知识抽取与组织：部分是
- 科学问题提出：否
- 假设生成：否
- 实验设计：否
- 仿真建模：否
- 工具调用与代码执行：是
- 实验执行：否
- 数据分析：是
- 结果解释：是
- 证据评估与验证：是
- 论文写作：否
- 端到端科研流程自动化：部分是

### 3.3 自主能力

- 任务分解：是
- 计划生成：部分是
- 工具调用：是
- 记忆与状态维护：中
- 反馈迭代：是
- 自主决策：是
- 多 Agent 协作：是
- 环境交互：是
- 闭环实验：否

## 4. 方法设计

- 执行阶段运行 reproduction package 并在必要时做代码修补。
- 评估阶段读取显式执行证据并判断复现状态。
- 两阶段结合形成面向 scientific papers 的自动 reproducibility assessment。

## 5. 实验与验证

- 验证方式：benchmark evaluation
- 基准：REPRO-Bench / REPRO-Bench-S
- 关键结果：相对最强基线有明显提升

## 6. 与已有工作的关系

- 与 `ARA`、`Automating Computational Reproducibility in Social Science` 同属 reproducibility 方向。
- 相比通用 research workflow agent，这篇更稳定落在 `11.07`。

## 7. 局限性与风险

- 当前仍以 arXiv-level evidence 为主。
- 主要风险是 core-strength 与 full-text depth，不是 top-level misclassification。

## 8. 对综述写作的价值

- 可作为 `11.07` 中 scientific reproducibility automation 的核心样本。
- 适合和 peer-review automation 共同构成“科学知识生产与审查”小节。

## 9. 总结

PaperRepro 是稳定的 `11.07` 记录，主对象是 scientific reproducibility assessment，而不是领域无关科研 Agent 平台。
