# Holtdirk et al. 2026 - Automated Reproducibility Assessments in the Social and Behavioral Sciences

**论文信息**
- 标题：Automated reproducibility assessments in the social and behavioral sciences using large language models
- 作者：Tobias Holtdirk; Pietro Marcolongo; Anna Steinberg Schulten; Felix Henninger; Stefan Rose; Sarah Ball; Bolei Ma; Frauke Kreuter; Markus Weinmann; Stefan Feuerriegel
- 年份：2026
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2606.13670
- PDF / 本地文件路径：当前笔记基于 arXiv PDF 与 arXiv HTML 一手证据整理；当前 note 未记录本地归档 PDF 路径。
- 论文类型：研究论文 / reproducibility assessment workflow
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

## 2026-06-24 adjudicated writeback

```text
scientific_object_modules: 11
object_coverage_mode: single_module
has_concrete_object_experiments: yes
general_method_bucket: none
primary_module_for_filing: 11
first_hand_sources_checked: arXiv PDF
classification_evidence_source_level: first_hand_full_text
source_limited: no
module_assignment_evidence: the paper audits reproducibility of published social and behavioral science studies, re-runs analyses, and compares claims and effect sizes, so the stable object is science-of-science / reproducibility assessment in `11.07`.
multi_module_object_coverage_note: none
note_location_rule: 本 note 落在 `11` 文件夹仅为归档便利，不是分类权威；当前权威对象模块判断是 `11`。
```

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | arXiv abstract | 多步读取上下文、重分析数据、生成 effect size、判断结论一致性 | 中高 |
| 科学对象归类 | `11.07` | arXiv abstract | 对象是 social and behavioral science published studies 的 reproducibility | 高 |
| 方法流程 | 多步执行 | arXiv abstract | 重分析原始数据并与原结果及人工复核比较 | 高 |
| 实验验证 | 有实证样本 | arXiv abstract | `N=76` studies with predefined claims | 高 |
| 边界判断 | 明确留在 `11.07`，不转 `01.04` | arXiv PDF | 目标是对已发表社会与行为科学研究进行 empirical-claims auditing 与 reproducibility assessment，而非通用科研辅助平台。 | 高 |

## 0. 摘要翻译

本文研究如何用大模型自动完成社会与行为科学研究的复现评估。系统读取研究上下文与原始数据，对已发表研究进行自动重分析，并把产生的效应量与定性结论同原文和人工复核结果进行比较，从而支持规模化 reproducibility assessment。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：存在多步分析链、代码/统计执行与结果判断
- 判定置信度：中高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：部分是
  - 工具调用：是
  - 反馈迭代：部分是
  - 自主决策：是
  - 多 Agent 协作：未明确
- 在科研流程中承担的明确角色：复现执行、claim checking、effect-size comparison、quality assessment

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 科学对象模块：11
- 覆盖模式：单模块
- 独立 `01.04` 存放区：none
- Primary module for filing：11（仅用于文件落盘，不覆盖 `11` 模块事实）
- 一级类：11
- 二级类：11.07
- 三级类：reproducibility assessment in social and behavioral sciences
- 四级专题：social and behavioral science reproducibility agents
- 四级专题是否为新增：否
- 归类理由：对象是科学研究结果的自动复核
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：已发表社会与行为科学研究的 empirical claims
- 最终科学问题：如何自动重分析数据并判断结论是否可复现
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：workflow 是手段，稳定对象是科学评估活动本身

### 2.3 容易混淆的边界

- 可能误归类到：01.04
- 最终判定：保留 11.07
- 判定理由：论文本体是 science-of-science / reproducibility assessment，对象是已发表社会与行为科学研究的 empirical claims，而不是无具体对象实验的通用科研平台。
- 是否需要二次复核：否

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：部分是
- Tool-using Agent：是
- Retrieval-augmented Agent：否
- Multi-Agent System：未明确
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：部分是
- Hybrid Agent：是
- 其他：automated reproducibility workflow

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

- 任务分解：中
- 计划生成：部分是
- 工具调用：是
- 记忆与状态维护：中
- 反馈迭代：部分是
- 自主决策：是
- 多 Agent 协作：未明确
- 环境交互：是
- 闭环实验：否

## 4. 方法设计

- 读取 study context 与 predefined claims。
- 自动生成分析并运行原始数据重分析。
- 比较 effect sizes 和 qualitative conclusions，输出 reproducibility judgment。

## 5. 实验与验证

- 样本：76 published studies
- 指标：effect size recovery, qualitative conclusion agreement
- 结果：多数案例与原文定性结论一致

## 6. 与已有工作的关系

- 与 `PaperRepro`、`ARA` 同属 reproducibility automation 方向。
- 比 peer-review generation 更靠近 empirical claim verification。

## 7. 局限性与风险

- 当前以摘要与 arXiv 页面为主要证据来源。
- Agent 结构是否显式多代理仍不如 `PaperRepro` 清楚。
- 主要剩余风险是 core-strength，而非 class direction。

## 8. 对综述写作的价值

- 可支持 `11.07` 中 reproducibility assessment 子脉络。
- 适合与 peer-review、paper evaluation、revision systems 并列。

## 9. 总结

该文稳定属于 `11.07`，因为它研究的是社会与行为科学研究结果的自动复核，而不是通用科研平台。
