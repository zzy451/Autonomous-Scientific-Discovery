# AutoResearch: Insight In, Hallucination Out

**论文信息**

- ID：ASD-0952
- 标题：AutoResearch: Insight In, Hallucination Out
- 作者：Liu, Xiang; Sun, Qumeng; Bruno; Zhang, Xiao; Li, Jiahao; Zhang, Haoyang
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2608.17906
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0952.txt
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Xiang_2026_AutoResearch_Insight_In_Hallucination_Out_ASD0952.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 纳入判断依据：目标是研究而非通用产品应用。 | 纳入判断依据：目标是研究而非通用产品应用。 | TXT line 240；核验TXT行号 240 | Autonomous research systems are increasingly capable of executing long research workflows, yet automation alone does not ensure that the resulting process remains scientifically grounded. | 高（一手正文；非独立复现） |
| 科学对象或研究任务由正文明确指出。 | 科学对象或研究任务由正文明确指出。 | TXT line 243；核验TXT行号 243 | In Idea Execution, coordinated agents decompose these plans into experiments, iteratively implement and diagnose them, and employ independent evidence-based review before accepting research conclusions. | 高（一手正文；非独立复现） |
| 方法包含任务路由、执行和结果处理。 | 方法包含任务路由、执行和结果处理。 | TXT line 452；核验TXT行号 452 | As illustrated in Figure 1, the Idea Generation stage transforms heterogeneous research signals and accumulated domain knowledge into a grounded hypothesis and an executable research plan. | 高（一手正文；非独立复现） |
| 作者设置了对照或独立验证。 | 作者设置了对照或独立验证。 | TXT line 523；核验TXT行号 523 | Candidate hypotheses are subjected to independent cross-validation before they become research commitments. | 高（一手正文；非独立复现） |
| 正文报告可核对的结果或系统贡献。 | 正文报告可核对的结果或系统贡献。 | TXT line 634；核验TXT行号 634 | Crucially, critical evaluation is performed by a fresh-context agent that does not inherit the producer’s reasoning trajectory. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

论文提出AutoResearch双阶段框架，先将外部研究信号与域内知识组合为可测试的研究计划，再以协调Agent执行、诊断并独立复核。实验覆盖跨模态检索、系统优化和机器学习。作者报告RSICD上Recall提高且审计发现问题事件较少，也以矩阵乘法案例演示不稳定测量如何被纠正。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。论文设定了可检验的科研目标或学术问题。
  - 原文位置：TXT line 241；核验TXT行号 241；引文：We introduce AutoResearch, a two-stage system that connects Idea Generation with Idea Execution to address both how research ideas are formed and how they are reliably established through experimentation.
- 多步行动过程：yes。正文实例显示Agent进行了多步任务路径。
  - 原文位置：TXT line 245；核验TXT行号 245；引文：For example, on RSICD benchmark, an AutoResearch-generated idea improves mean Recall from 32.8432.84 to 34.6934.69, while recording only 55 audit-confirmed issue events compared with 1111–2727 for other autonomous research systems.
- 至少一种Agent能力：yes。系统使用工具、计划、反馈或多Agent中明确能力。
  - 原文位置：TXT line 452；核验TXT行号 452；引文：As illustrated in Figure 1, the Idea Generation stage transforms heterogeneous research signals and accumulated domain knowledge into a grounded hypothesis and an executable research plan.
- 明确科研流程角色：yes。系统在科研流程中承担研究者、执行者或审查者角色。
  - 原文位置：TXT line 523；核验TXT行号 523；引文：Candidate hypotheses are subjected to independent cross-validation before they become research commitments.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：01
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：01（仅归档，不覆盖其他模块）
- 模块内分类路径：01.02 计算机科学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

此文不仅是通用Agent模式；RSICD遥感检索和深度实验是可指认研究任务，但当前证据不能支持新加专业领域分类，保留01。

### 2.3 容易混淆的边界

此文不仅是通用Agent模式；RSICD遥感检索和深度实验是可指认研究任务，但当前证据不能支持新加专业领域分类，保留01。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM research agent

### 3.2 科研流程角色

研究协调；实验执行

系统中的Agent角色为 AutoResearch: Insight In, Hallucination Out; 从研究目标构建信号池和域知识库，多模型生成与交叉评审产生可执行假设；任务被分解成实现、试验、消融、诊断等单元，执行Agent对工作区产生文件与运行实验；批评Agent独立评判结果支持继续、修改或停止。

### 3.3 自主能力

系统使用工具、计划、反馈或多Agent中明确能力。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

科学方法贡献是把机制假设与可验证实验链接，并设置不足证据时的独立否决。系统贡献是两阶段Agent组织与审计机制。

### 4.2 系统流程与组件

从研究目标构建信号池和域知识库，多模型生成与交叉评审产生可执行假设；任务被分解成实现、试验、消融、诊断等单元，执行Agent对工作区产生文件与运行实验；批评Agent独立评判结果支持继续、修改或停止。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

包含RSICD双向图文检索，矩阵乘法正确性和计时稳定性实验，另对生成实验轨迹做审计，与AI Scientist、Agent Laboratory、R&D-Agent、AutoResearchClaw比较。

### 5.2 基线、指标与结果

作者报告RSICD mR由32.84提升到34.69，并有55个审计确认问题事件；矩阵乘法实验经定位计时错误后重跑建立3.4 ms基线。

### 5.3 科学贡献与证据强度

科学方法贡献是把机制假设与可验证实验链接，并设置不足证据时的独立否决。系统贡献是两阶段Agent组织与审计机制。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

正文在相关工作中将本系统放入自动研究Agent及其评测背景；与相邻自动化研究工作相比，本文主要增加了对应方法或监督机制。

## 7. 局限性与风险

作者限制或讨论中明示的证据见原文结论；阅读者推断是评测任务较窄或规模有限，不宜外推至广泛自主科学发现。

## 8. 对综述写作的价值

科学方法贡献是把机制假设与可验证实验链接，并设置不足证据时的独立否决。系统贡献是两阶段Agent组织与审计机制。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

论文提出AutoResearch双阶段框架，先将外部研究信号与域内知识组合为可测试的研究计划，再以协调Agent执行、诊断并独立复核。实验覆盖跨模态检索、系统优化和机器学习。作者报告RSICD上Recall提高且审计发现问题事件较少，也以矩阵乘法案例演示不稳定测量如何被纠正。

### 9.2 速记版 pipeline

从研究目标构建信号池和域知识库，多模型生成与交叉评审产生可执行假设；任务被分解成实现、试验、消融、诊断等单元，执行Agent对工作区产生文件与运行实验；批评Agent独立评判结果支持继续、修改或停止。

### 9.3 标注字段汇总

```text
paper_id=ASD-0952
inclusion_status=to_read
scientific_object_modules=01
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=01
module_taxonomy_codes=01.02
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O2 既定基准 | 在预定义检索和优化任务上评测 | “RSICD” · L29 |
| 验证强度 | V1 基准/内部评测 | 基准指标和审计检查 | “55个审计确认问题事件” · L105 |
| 系统自主性 | L2 闭环执行者 | 系统自主执行并独立复核实验 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
