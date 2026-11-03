# EvoCast: Reliable Autonomous Research Agents for Iterative Forecasting Architecture Evolution

**论文信息**

- ID：ASD-0972
- 标题：EvoCast: Reliable Autonomous Research Agents for Iterative Forecasting Architecture Evolution
- 作者：Xu, Kaipeng; Yan, Xianli; Wang, Yan; Liu, Xiang; Liu, Shan
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2610.04517
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0972.txt
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Kaipeng_2026_EvoCast_Reliable_Autonomous_Research_Agents_for_Iterative_Forecasting_Architecture_ASD0972.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 科学对象 | 研究对象是面向具体时间序列预测任务的架构研发。 | 本地原文 TXT 第455行；核验TXT行号 455 | We evaluate EvoCast through three research questions. RQ1 studies implementation reliability and efficiency, asking whether EvoCast can translate forecasting architecture ideas into executable, semantically correct, and protocol-compliant code with higher success and lower agent-side token/time cost. RQ2 studies end-to-end forecasting utility, asking whether EvoCast can develop task-specific architectures that outperform selected baselines, strong forecasting models, and agent baselines in three real-world forecasting cases. RQ3 studies orchestration and authority design, asking which parts of cognition-authority separation are necessary for reliable autonomous architecture research. | 高（一手正文；非独立复现） |
| 研究方法与Agent行动 | LLM生成研究意图与代码，程序权限独立控制构建、评估和晋升。 | 本地原文 TXT 第480行；核验TXT行号 480 | We introduce cognition-authority separation for reliable autonomous research. This design assigns hypothesis generation and source implementation to LLM agents, and deterministic authorities control source validity, runtime evaluation, model promotion, and state updates. | 高（一手正文；非独立复现） |
| 实验任务与验证 | 候选及基线共享数据划分、指标、训练策略和评估路径。 | 本地原文 TXT 第711行；核验TXT行号 711 | where the metric direction follows the formal evaluation setting. In the experiments of this paper, lower error indicates a stronger model. The selected single baseline anchors all later candidate comparisons and also serves as the execution starting point for mechanism diagnosis. Under this design, the canonical evaluator reuses the same dataset split, metric, training policy, and evaluation path for baselines, ablations, and promoted candidates, thereby fixing one comparison surface throughout the run. | 高（一手正文；非独立复现） |
| 主要结果 | 实现评测显示EvoCast提高成功率和修复表现并降低资源成本。 | 本地原文 TXT 第1285行；核验TXT行号 1285 | Table 1 reports the overall results. EvoCast achieves the highest success rate while maintaining perfect fidelity and the strongest repair performance, and it is also more time- and cost-efficient than the other agent baselines. Direct Independent Edit is the cheapest method, but it also has the lowest success rate; the remaining agent baselines outperform direct editing but still fall clearly behind EvoCast. These results show that EvoCast improves success rate, efficiency, and stability together when implementing complex deep-learning architecture changes. As tasks move from local edits to cross-module integration and novel module insertion, cognition-authority separation more reliably turns research intent into valid implementations. Appendix D.1 reports the complexity-level and backbone-level analysis. | 高（一手正文；非独立复现） |
| 研究贡献或边界 | 真实预测案例在统一协议下显示误差下降，支持其任务级效用。 | 本地原文 TXT 第1867行；核验TXT行号 1867 | Table 3 reports the final formal forecasting results on the three real cases. EvoCast reduces the selected-baseline error on all three tasks. It achieves the lowest MSE on all three tasks and the lowest MAE on two of them. These results show that the fixed EvoCast loop can develop stronger task-specific architectures under one unchanged evaluator, task protocol, and final-artifact evaluation rule. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

EvoCast提出面向时间序列预测架构演化的自主研究Agent。系统建立基线、诊断误差机制、提出候选修改，并将提出候选的认知角色与执行和晋级权限分开；只有通过受控实验的结果才能更新研究状态。论文在统一预测基准上检查实现可靠性、端到端效用和权限设计。对象是预测方法和研究流程，具体数据领域需要按任务清单确认。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。基准以10种预测骨干网络和三类预设改动复杂度构造30项预测架构设计任务。
  - 原文位置：TXT 第1271行；原文引文；核验TXT行号 1271；引文：We construct a controlled idea-to-code benchmark with 30 tasks from 10 forecasting backbones and three predefined idea-complexity levels: local modification, cross-module integration, and novel module insertion.
- 多步行动过程：yes。EvoCast先运行基线诊断和机制消融，再依据证据提出研究方向并迭代实现候选架构。
  - 原文位置：TXT 第403行；原文引文；核验TXT行号 403；引文：EvoCast first establishes and diagnoses a task-specific baseline through executed mechanism ablations, then generates evidence-grounded research directions from dataset characteristics, diagnostic results, prior rounds, and failur
- 至少一种Agent能力：yes。LLM Agent负责开放式假设生成和代码实现；程序权限控制代码有效性、统一评估、晋升与状态更新。
  - 原文位置：TXT 第448行；原文引文；核验TXT行号 448；引文：LLM agents handle open-ended hypothesis generation, source implementation, and report narration, while deterministic program authorities control source validity, canonical evaluation, metric comparison, model promotion, and state
- 明确科研流程角色：yes。EvoCast被设计为自主研究系统，用于迭代演进面向预测任务的架构。
  - 原文位置：TXT 第403行；原文引文；核验TXT行号 403；引文：introduce EvoCast, a fully autonomous research-agent system for iterative forecasting architecture evolution.

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

- Task-specific time-series forecasting architecture evolution; dataset/domain list needs full-paper inspection.

### 2.3 容易混淆的边界

01.02适用于研究Agent及计算方法开发；若任务只测通用预测性能且缺少特定领域科学问题，则暂不增加其他对象模块或11。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

多Agent/科研工作流Agent

### 3.2 科研流程角色

科学问题提出；实验设计；工具调用与代码执行；结果分析与验证

EvoCast包含研究Agent、受控执行器和证据状态更新流程；Agent生成候选，权限层负责运行固定协议及验证，避免Agent自行宣布改进。

### 3.3 自主能力

LLM Agent负责开放式假设生成和代码实现；程序权限控制代码有效性、统一评估、晋升与状态更新。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

提出具有显式权限控制和证据状态更新的预测架构研究Agent；科学贡献主要是基准上的方法改进评估。

### 4.2 系统流程与组件

输入为预测任务与基线；诊断预测误差并形成机制假设；提出架构/代码候选；在统一TFB协议下运行对照；验证改动并按规则晋级，保存证据承载的研究状态。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

TFB统一基准；三个问题覆盖实现可靠性、端到端研究效用和编排/权限设计；含消融及追加分析。需把不同任务域与统计量依结果表逐项引用。

### 5.2 基线、指标与结果

作者报告受控协议和认知—权限分离改善实验执行可靠性，并评估Agent迭代搜索对预测表现的效用；不应把基准表现泛化到所有科学领域。

### 5.3 科学贡献与证据强度

提出具有显式权限控制和证据状态更新的预测架构研究Agent；科学贡献主要是基准上的方法改进评估。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

结合时间序列AutoML、LLM架构搜索和自主研究Agent；区别在于固定基准协议、候选晋级权限和证据记录。

## 7. 局限性与风险

受TFB任务集、代理模型和预算限制；数据领域是否构成具体科学对象需根据实验任务而非预测通用性判断；尚无外部领域验证。

## 8. 对综述写作的价值

适合讨论自主研究系统中实验权限、可复现协议和证据状态管理。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

EvoCast用权限分离和证据状态管理执行时间序列架构研究。

### 9.2 速记版 pipeline

输入为预测任务与基线；诊断预测误差并形成机制假设；提出架构/代码候选；在统一TFB协议下运行对照；验证改动并按规则晋级，保存证据承载的研究状态。

### 9.3 标注字段汇总

```text
paper_id=ASD-0972
inclusion_status=to_read
scientific_object_modules=01
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=01
module_taxonomy_codes=01.02
source_level=first_hand_full_text
fulltext_followup_required=true
```

### 全文后续要求

当前纳入和分类证据已足够；第7节明确的结果/复现细节仍需继续回查。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O2 既定基准 | TFB时间序列预测基准为预定义任务集 | “TFB统一基准；三个问题覆盖实现可靠性、端到端研究效用和编排/权限设计” · L101 |
| 验证强度 | V1 基准/内部评测 | 基准评分和可靠性指标，无独立复现 | “含消融及追加分析。需把不同任务域与统计量依结果表逐项引用” · L101 |
| 系统自主性 | L2 闭环执行者 | Agent自主诊断误差机制并提出架构改进 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
