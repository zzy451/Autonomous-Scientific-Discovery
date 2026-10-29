# TruthInsightBench: An Evidence-Grounded Benchmark for Automated Evaluation of Open-Ended Scientific Discovery Agents

**论文信息**

- ID：ASD-0949
- 标题：TruthInsightBench: An Evidence-Grounded Benchmark for Automated Evaluation of Open-Ended Scientific Discovery Agents
- 作者：Zhibo Yang; Chen Zhang; Yuewei Zhang; Hao Wang
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2609.05079
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0949.txt
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Yang_2026_TruthInsightBench_An_Evidence_Grounded_Benchmark_for_Automated_Evaluation_of_ASD0949.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 研究目标/科学问题 | TruthInsightBench包含来自10个科学领域、40篇同行评审研究的40项盲测任务。Agent只获得中性的科学目标和冻结数据，不提供原研究结论、预期数值或分析路径，必须自行确定主张、选择分析并形成证据支持的发现报告，以检验开放式科学发现能力。 | 本地全文：ASD-0949中与研究目标/科学问题直接相关的原文句子；核验TXT行号 39 | The second is the capacity for open-ended scientific inquiry: to examine raw data without a known answer, determine which phenomena merit a claim, separate a genuine effect from a numerical ∗Correspondence: TruthInsightBench@163.com. | 高（一手正文；非独立复现） |
| 多步行动/研究流程 | 从10个学科的40项同行评审研究构建任务；仅提供中性目标与冻结数据，使用证据约束的评分标准检查Agent提出的主张及分析过程。 | 本地全文：ASD-0949中与多步行动/研究流程直接相关的原文句子；核验TXT行号 42 | 1 arXiv:2609.05079v2 [cs.AI] 8 Sep 2026 or modeling artifact, formulate falsifiable hypotheses, adjudicate between competing explanations, test controls and robustness, establish that a result holds on independent data, delimit the scope within which a conclusion holds, and revise that conclusion when counter-evidence arrives. | 高（一手正文；非独立复现） |
| Agent实现与能力 | 本文提出评价基准，受测编码Agent在隐藏原结论、目标数值和分析路径的盲任务中自主分析冻结数据并撰写发现报告。 | 本地全文：ASD-0949中与Agent实现与能力直接相关的原文句子；核验TXT行号 1016 | Where reproduction-oriented benchmarks organize a task, its data, and its rubric around a hidden target study, TruthInsightBench gives an agent only a neutral scientific objective and frozen data, hides all source conclusions and evaluation as- sets, and scores the evidentiary maturity of the agent’s own claims along six dimensions and 29 artifact-grounded items. | 高（一手正文；非独立复现） |
| 实验任务与验证设置 | 基准包含40项盲任务，来源于40项同行评审研究、覆盖10个科学领域；评价报告与原始证据及科学结论的对应关系。 | 本地全文：ASD-0949中与实验任务与验证设置直接相关的原文句子；核验TXT行号 82 | TruthInsightBench contains 40 blind tasks derived from 40 peer-reviewed studies published between 2018 and 2024 and spanning 10 scientific domains. | 高（一手正文；非独立复现） |
| 作者报告的结果/贡献 | 论文报告不同Agent在证据支持、结论正确性等指标上的基准表现；结果是基准评测，不等同于独立完成并发表新发现。 贡献是用真实研究数据和证据标准构造无特权答案的开放发现评测，而不是以已知目标值直接判分。 | 本地全文中包含该原句的位置；核验TXT行号 99 | The results reveal a consistent and, we argue, informative pattern: • All four systems fall within a narrow interval of 58.4 to 60.3 (of 100), and no system is reliably superior to another at the task level. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

TruthInsightBench包含来自10个科学领域、40篇同行评审研究的40项盲测任务。Agent只获得中性的科学目标和冻结数据，不提供原研究结论、预期数值或分析路径，必须自行确定主张、选择分析并形成证据支持的发现报告，以检验开放式科学发现能力。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。TruthInsightBench包含来自10个科学领域、40篇同行评审研究的40项盲测任务。Agent只获得中性的科学目标和冻结数据，不提供原研究结论、预期数值或分析路径，必须自行确定主张、选择分析并形成证据支持的发现报告，以检验开放式科学发现能力。
  - 原文位置：本地全文：ASD-0949中与研究目标/科学问题直接相关的原文句子；核验TXT行号 39；引文：The second is the capacity for open-ended scientific inquiry: to examine raw data without a known answer, determine which phenomena merit a claim, separate a genuine effect from a numerical ∗Correspondence: TruthInsightBench@163.com.
- 多步行动过程：yes。从10个学科的40项同行评审研究构建任务；仅提供中性目标与冻结数据，使用证据约束的评分标准检查Agent提出的主张及分析过程。
  - 原文位置：本地全文：ASD-0949中与多步行动/研究流程直接相关的原文句子；核验TXT行号 42；引文：1 arXiv:2609.05079v2 [cs.AI] 8 Sep 2026 or modeling artifact, formulate falsifiable hypotheses, adjudicate between competing explanations, test controls and robustness, establish that a result holds on independent data, delimit the scope within which a conclusion holds, and revise that conclusion when counter-evidence arrives.
- 至少一种Agent能力：yes。本文提出评价基准，受测编码Agent在隐藏原结论、目标数值和分析路径的盲任务中自主分析冻结数据并撰写发现报告。
  - 原文位置：本地全文：ASD-0949中与Agent实现与能力直接相关的原文句子；核验TXT行号 1016；引文：Where reproduction-oriented benchmarks organize a task, its data, and its rubric around a hidden target study, TruthInsightBench gives an agent only a neutral scientific objective and frozen data, hides all source conclusions and evaluation as- sets, and scores the evidentiary maturity of the agent’s own claims along six dimensions and 29 artifact-grounded items.
- 明确科研流程角色：yes。基准包含40项盲任务，来源于40项同行评审研究、覆盖10个科学领域；评价报告与原始证据及科学结论的对应关系。
  - 原文位置：本地全文：ASD-0949中与实验任务与验证设置直接相关的原文句子；核验TXT行号 82；引文：TruthInsightBench contains 40 blind tasks derived from 40 peer-reviewed studies published between 2018 and 2024 and spanning 10 scientific domains.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：01;02;03;04;05;06;09
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：01（仅归档，不覆盖其他模块）
- 模块内分类路径：01.01 数学；01.02 计算机科学；02.01 天文学与天体物理学；02.02 物理学；03.02 基础化学；03.03 合成、反应与催化；04.01 材料基础；05.01 地球科学基础；05.02 大气、海洋与水文科学；06.02.07 神经生物学；09.06 能源工程
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

对象模块与代码沿用输入审计记录（01, 02, 03, 04, 05, 06, 09；01.01, 01.02, 02.01, 02.02, 03.02, 03.03, 04.01, 05.01, 05.02, 06.02.07, 09.06）；是否纳入与对象分类分开判断。

### 2.3 容易混淆的边界

对象模块与代码沿用输入审计记录（01, 02, 03, 04, 05, 06, 09；01.01, 01.02, 02.01, 02.02, 03.02, 03.03, 04.01, 05.01, 05.02, 06.02.07, 09.06）；是否纳入与对象分类分开判断。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

自主科研Agent

### 3.2 科研流程角色

科研问题处理；多步行动或评测

本文提出评价基准，受测编码Agent在隐藏原结论、目标数值和分析路径的盲任务中自主分析冻结数据并撰写发现报告。

### 3.3 自主能力

本文提出评价基准，受测编码Agent在隐藏原结论、目标数值和分析路径的盲任务中自主分析冻结数据并撰写发现报告。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

贡献是用真实研究数据和证据标准构造无特权答案的开放发现评测，而不是以已知目标值直接判分。

### 4.2 系统流程与组件

从10个学科的40项同行评审研究构建任务；仅提供中性目标与冻结数据，使用证据约束的评分标准检查Agent提出的主张及分析过程。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

基准包含40项盲任务，来源于40项同行评审研究、覆盖10个科学领域；评价报告与原始证据及科学结论的对应关系。

### 5.2 基线、指标与结果

论文报告不同Agent在证据支持、结论正确性等指标上的基准表现；结果是基准评测，不等同于独立完成并发表新发现。

### 5.3 科学贡献与证据强度

贡献是用真实研究数据和证据标准构造无特权答案的开放发现评测，而不是以已知目标值直接判分。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

论文以“TruthInsightBench: An Evidence-Grounded Benchmark for Automated Evaluation of Open-Ended Scientific Discovery Agents”对应的研究任务为对象，具体与哪些既有系统或基准比较，应结合其正文相关工作和实验基线判断；不把工具名称直接视为科学对象。

## 7. 局限性与风险

任务来源限于40项研究和10个领域；评分标准及冻结数据仍影响可评内容，不能覆盖所有科学发现过程。

## 8. 对综述写作的价值

可用于综述“TruthInsightBench: An Evidence-Grounded Benchmark for Automated Evaluation of Open-Ended Scientific Discovery Agents”所涉及的Agent任务、研究流程和验证方式；其证据边界为本论文实际报告的任务集与实验结果。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

TruthInsightBench以40项盲任务评估Agent能否从真实科学数据提出证据支持的发现。

### 9.2 速记版 pipeline

从10个学科的40项同行评审研究构建任务；仅提供中性目标与冻结数据，使用证据约束的评分标准检查Agent提出的主张及分析过程。

### 9.3 标注字段汇总

```text
paper_id=ASD-0949
inclusion_status=to_read
scientific_object_modules=01;02;03;04;05;06;09
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=01
module_taxonomy_codes=01.01;01.02;02.01;02.02;03.02;03.03;04.01;05.01;05.02;06.02.07;09.06
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`01.01.06` 微分方程；二级：`01.01`。
- 原文位置：PDF pp.26?27。
- 判定：Concrete experiment/task evidence supports 01.01.06 (微分方程). Table 7: Math_01 governing equation disc.; Math_02 compositional invariants (PDF p.26); Math_03 ode parameter geometry; Math_04 anomalous diffusion cps (PDF p.27).
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
