# AutoWorldModel-Bench: A State-Centric Benchmark for Automated World-Model Research

**论文信息**

- ID：ASD-0955
- 标题：AutoWorldModel-Bench: A State-Centric Benchmark for Automated World-Model Research
- 作者：Moodi, Marjan; Zhu, Xuankang; Silva, Fernando De Mesentier; Chaput, Harold; Taesiri, Mohammad Reza
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2608.11216
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0955.txt
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Marjan_2026_AutoWorldModel_Bench_A_State_Centric_Benchmark_for_Automated_World_ASD0955.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 纳入核查：文章直接研究自动研究Agent或其基准。 | 纳入核查：文章直接研究自动研究Agent或其基准。 | TXT line 450；核验TXT行号 450 | We introduce AutoWorldModel-Bench, a closed-loop benchmark in which frontier coding agents autonomously improve a provided base world model under a fixed compute budget. | 高（一手正文；非独立复现） |
| 研究对象由正文任务或数据明确界定。 | 研究对象由正文任务或数据明确界定。 | TXT line 451；核验TXT行号 451 | The benchmark spans eight game environments under a unified structured-state representation—ground-truth entity state extracted from each game and consumed through a shared tensor format—which isolates dynamics modeling from perception and enables minutes-per-run iteration. | 高（一手正文；非独立复现） |
| 方法证据包括任务输入与迭代操作。 | 方法证据包括任务输入与迭代操作。 | TXT line 509；核验TXT行号 509 | We define a six-hour compute-bounded closed-loop protocol in which an agent receives a base world model architecture and must autonomously improve it (Sec. 3.5). | 高（一手正文；非独立复现） |
| 验证设计含有对照、多次执行或独立评分。 | 验证设计含有对照、多次执行或独立评分。 | TXT line 1608；核验TXT行号 1608 | Table 2 summarizes the experimental results, showing that both agents improve on the base in the large majority of sessions. Across the 6464 sessions, the agent-produced model exceeds the base on the held-out test split in 6363, with a mean test-score lift of +0.196+0.196 on a [0,1][0,1] scale (median +0.115+0.115). The gains are not uniform: of the 6363 positive sessions, 3333 are substantial (Δ≥+0.10\Delta\geq+0.10), 1010 moderate (+0.05≤Δ<+0.10+0.05\leq\Delta<+0.10), and 2020 marginal (0<Δ<+0.050<\Delta<+0.05), with 1111 of the marginal sessions marginal on both the test and scenario axes. Roughly two-thirds of the improvements are thus meaningful and about a third are marginal but real. The single exception is a Claude Opus 4.6 session on Breakout/D3PM that regresses by 0.0010.001 test score; Codex-5.4 improves the base on every task. The magnitude of the lift tracks base strength: gains concentrate on tasks whose bases are weakest (Fig. G.24), with Asteroids bases averaging 0.2130.213 and reaching 0.6180.618 (+0.405+0.405) while Pong bases begin at 0.7920.792 and reach 0.8950.895 (+0.103+0.103). The table carries per-agent Base columns because base re-runs across sessions produce different step counts and long-horizon rollout behavior despite identical code; platform non-determinism on the shared 88-GPU host is the cause, and Sec. G.9 documents it. | 高（一手正文；非独立复现） |
| 正文报告了可核对结果或系统贡献。 | 正文报告了可核对结果或系统贡献。 | TXT line 1701；核验TXT行号 1701 | The experiments that win each session are predominantly non-trivial; in 5858 of 6464 sessions (91%91\%), the session-best experiment is non-trivial, while the remaining six sessions are won by hyperparameter-only modifications (Tab. G.13). | 高（一手正文；非独立复现） |

## 0. 摘要翻译

论文提出AutoWorldModel-Bench，用统一结构化状态表示支持8种游戏世界模型研究。在固定算力下，编码Agent以迭代实验改进基础世界模型，并在独立held-out集和长轨迹滚动中评测。作者在64个会话中报告63个结果高于基础模型，多数改进来自实质性模型或训练修改。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。正文设定了明确的科学目标或评测问题。
  - 原文位置：TXT line 450；核验TXT行号 450；引文：We introduce AutoWorldModel-Bench, a closed-loop benchmark in which frontier coding agents autonomously improve a provided base world model under a fixed compute budget.
- 多步行动过程：yes。方法需要反复提案、执行和判读结果。
  - 原文位置：TXT line 509；核验TXT行号 509；引文：We define a six-hour compute-bounded closed-loop protocol in which an agent receives a base world model architecture and must autonomously improve it (Sec. 3.5).
- 至少一种Agent能力：yes。系统具有调用工具并根据反馈继续的Agent能力。
  - 原文位置：TXT line 922；核验TXT行号 922；引文：We adopt a closed-loop design in which each task is presented with a self-contained directory with standardized preparation and training scripts [34]. Following Lee et al. [41], we give the agent persistent access to a structured experiment log that records the full history of prior runs, including architectures explored, hyperparameters used, and scores obtained. This setup allows each subsequent decision to be conditioned on all accumulated evidence (Fig. 2).
- 明确科研流程角色：yes。系统在文中承担科研Agent的实验、研发或评价角色。
  - 原文位置：TXT line 1608；核验TXT行号 1608；引文：Table 2 summarizes the experimental results, showing that both agents improve on the base in the large majority of sessions. Across the 6464 sessions, the agent-produced model exceeds the base on the held-out test split in 6363, with a mean test-score lift of +0.196+0.196 on a [0,1][0,1] scale (median +0.115+0.115). The gains are not uniform: of the 6363 positive sessions, 3333 are substantial (Δ≥+0.10\Delta\geq+0.10), 1010 moderate (+0.05≤Δ<+0.10+0.05\leq\Delta<+0.10), and 2020 marginal (0<Δ<+0.050<\Delta<+0.05), with 1111 of the marginal sessions marginal on both the test and scenario axes. Roughly two-thirds of the improvements are thus meaningful and about a third are marginal but real. The single exception is a Claude Opus 4.6 session on Breakout/D3PM that regresses by 0.0010.001 test score; Codex-5.4 improves the base on every task. The magnitude of the lift tracks base strength: gains concentrate on tasks whose bases are weakest (Fig. G.24), with Asteroids bases averaging 0.2130.213 and reaching 0.6180.618 (+0.405+0.405) while Pong bases begin at 0.7920.792 and reach 0.8950.895 (+0.103+0.103). The table carries per-agent Base columns because base re-runs across sessions produce different step counts and long-horizon rollout behavior despite identical code; platform non-determinism on the shared 88-GPU host is the cause, and Sec. G.9 documents it.

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

任务对象为实际游戏世界动力建模与游戏规则，是AI/计算科学内对象并可计入01.02。

### 2.3 容易混淆的边界

任务对象为实际游戏世界动力建模与游戏规则，是AI/计算科学内对象并可计入01.02。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

语言模型Agent

### 3.2 科研流程角色

科研执行；实验评估

AutoWorldModel-Bench: A State-Centric Benchmark for Automated World-Model Research?输入包含游戏世界的真值实体状态、基础模型、训练数据和评估代码；Agent读取结构化任务包，提出修改、改训练流程并交付实验；每次运行结束后看实验日志和多水平模型误差，为下一次提案选择针对性变更，以外部held-out评分判定提升。

### 3.3 自主能力

系统具有调用工具并根据反馈继续的Agent能力。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

科学贡献是上文实验任务中可复核的结果与对照；系统贡献是论文提出的Agent架构、迭代流程和评估方法。

### 4.2 系统流程与组件

输入包含游戏世界的真值实体状态、基础模型、训练数据和评估代码；Agent读取结构化任务包，提出修改、改训练流程并交付实验；每次运行结束后看实验日志和多水平模型误差，为下一次提案选择针对性变更，以外部held-out评分判定提升。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

八种游戏环境、两类编码Agent、基础模型与计算相同的多种搜索基线比较；用teacher-forced一步预测、h=10/20长时轨迹和游戏规则probe三种held-out测试。

### 5.2 基线、指标与结果

作者报告63/64会话超越基础模型，58/64（91%）会话最佳迭代为非平凡模型或训练改变；提升集中在长轨迹预测。

### 5.3 科学贡献与证据强度

科学贡献是上文实验任务中可复核的结果与对照；系统贡献是论文提出的Agent架构、迭代流程和评估方法。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

论文在自动研究Agent及长程轨迹研究的背景下与已有系统和评测基准比较，具体差异体现于上文所述的新监督、证据记忆或任务评价策略。

## 7. 局限性与风险

作者承认的局限以全文limitations段为准；读者风险：任务集和评分器不能代表全部真实研究环境，结果需按作者所设定的任务范围解读。

## 8. 对综述写作的价值

任务对象为实际游戏世界动力建模与游戏规则，是AI/计算科学内对象并可计入01.02。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

论文提出AutoWorldModel-Bench，用统一结构化状态表示支持8种游戏世界模型研究。在固定算力下，编码Agent以迭代实验改进基础世界模型，并在独立held-out集和长轨迹滚动中评测。作者在64个会话中报告63个结果高于基础模型，多数改进来自实质性模型或训练修改。

### 9.2 速记版 pipeline

输入包含游戏世界的真值实体状态、基础模型、训练数据和评估代码；Agent读取结构化任务包，提出修改、改训练流程并交付实验；每次运行结束后看实验日志和多水平模型误差，为下一次提案选择针对性变更，以外部held-out评分判定提升。

### 9.3 标注字段汇总

```text
paper_id=ASD-0955
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


## 2026-10-29 三级分类复核

- 归档分类：`01.02.13` 机器学习；二级：`01.02`。
- 原文位置：PDF p.2。
- 判定：实际改进世界模型架构与训练，在8个游戏环境作持出评估。
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
