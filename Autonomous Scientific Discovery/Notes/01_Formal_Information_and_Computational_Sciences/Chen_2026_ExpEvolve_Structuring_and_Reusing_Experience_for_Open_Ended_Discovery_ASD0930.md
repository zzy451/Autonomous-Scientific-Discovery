# ExpEvolve: Structuring and Reusing Experience for Open-Ended Discovery

**论文信息**

- ID：ASD-0930
- 标题：ExpEvolve: Structuring and Reusing Experience for Open-Ended Discovery
- 作者：Yongqiang Chen; Chenxi Liu; Deyu Zou; Zhenhao Chen; Tongliang Liu; Bo Han; Kun Zhang
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2610.29303
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0930.txt
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Chen_2026_ExpEvolve_Structuring_and_Reusing_Experience_for_Open_Ended_Discovery_ASD0930.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 研究目标/科学问题 | ExpEvolve 面向开放式程序演化任务，从候选程序中抽取能够解释得分差异的高层 idea factors，并用这些因素引导后续探索与利用。论文分析何种理论条件下此类因素可提高样本效率，并在 11 项开放式数学发现任务上评估，其中九项来自既有 SCS/AlphaEvolve 问题集。 | 本地全文：ASD-0930中与研究目标/科学问题直接相关的原文句子；核验TXT行号 10 | These agents tackle open-ended scientific problems by iteratively improving and evolving programs, leveraging the prior knowledge and reasoning capabilities of LLMs. | 高（一手正文；非独立复现） |
| 多步行动/研究流程 | 系统从不同得分的程序中归纳高层 idea factors，将其转化为搜索控制信息，在演化过程中用于候选生成和搜索资源分配。 | 本地全文：ASD-0930中与多步行动/研究流程直接相关的原文句子；核验TXT行号 132 | Motivated by the analysis, we propose ExpEvolve, which recognizes, structures, and leverages the high-level idea factors from discovery experience (Fig. | 高（一手正文；非独立复现） |
| Agent实现与能力 | ExpEvolve 是带经验抽取和复用机制的演化编码Agent；候选解为程序，显式评价器给出程序及其得分。 | 本地全文：ASD-0930中与Agent实现与能力直接相关的原文句子；核验TXT行号 133 | Specifically, ExpEvolve realizes the discovery of ideas via identifying high-level factors that help explain the program scoring differences. | 高（一手正文；非独立复现） |
| 实验任务与验证设置 | 实验覆盖 11 项开放式数学发现任务，其中九项来自 SCS 所研究并取自 AlphaEvolve 的问题；评价以程序得分和样本效率为主。 | 本地全文：ASD-0930中与实验任务与验证设置直接相关的原文句子；核验TXT行号 146 | We evaluate ExpEvolve on 11 open-ended mathematical discovery tasks with a budget of 200 evaluated programs, using SCS as the backbone and the main baseline (Sec. | 高（一手正文；非独立复现） |
| 作者报告的结果/贡献 | 作者报告 idea-level 抽取与复用可改善开放式演化搜索的样本效率；具体幅度须以任务级表格为准，不外推至任意科学领域。 工作聚焦数学程序搜索中的经验表示与复用，理论分析高层因素何时有助于样本效率，并实现相应的演化Agent。 | 本地全文中包含该原句的位置；核验TXT行号 147 | Under two con- figurations that split the budget into 20 generations of 10 programs and 10 generations of 20 programs, ExpEvolve improves the final performance over SCS and ShinkaEvolve in most settings with smaller budgets up to 5.0×. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

ExpEvolve 面向开放式程序演化任务，从候选程序中抽取能够解释得分差异的高层 idea factors，并用这些因素引导后续探索与利用。论文分析何种理论条件下此类因素可提高样本效率，并在 11 项开放式数学发现任务上评估，其中九项来自既有 SCS/AlphaEvolve 问题集。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。ExpEvolve 面向开放式程序演化任务，从候选程序中抽取能够解释得分差异的高层 idea factors，并用这些因素引导后续探索与利用。论文分析何种理论条件下此类因素可提高样本效率，并在 11 项开放式数学发现任务上评估，其中九项来自既有 SCS/AlphaEvolve 问题集。
  - 原文位置：本地全文：ASD-0930中与研究目标/科学问题直接相关的原文句子；核验TXT行号 10；引文：These agents tackle open-ended scientific problems by iteratively improving and evolving programs, leveraging the prior knowledge and reasoning capabilities of LLMs.
- 多步行动过程：yes。系统从不同得分的程序中归纳高层 idea factors，将其转化为搜索控制信息，在演化过程中用于候选生成和搜索资源分配。
  - 原文位置：本地全文：ASD-0930中与多步行动/研究流程直接相关的原文句子；核验TXT行号 132；引文：Motivated by the analysis, we propose ExpEvolve, which recognizes, structures, and leverages the high-level idea factors from discovery experience (Fig.
- 至少一种Agent能力：yes。ExpEvolve 是带经验抽取和复用机制的演化编码Agent；候选解为程序，显式评价器给出程序及其得分。
  - 原文位置：本地全文：ASD-0930中与Agent实现与能力直接相关的原文句子；核验TXT行号 133；引文：Specifically, ExpEvolve realizes the discovery of ideas via identifying high-level factors that help explain the program scoring differences.
- 明确科研流程角色：yes。实验覆盖 11 项开放式数学发现任务，其中九项来自 SCS 所研究并取自 AlphaEvolve 的问题；评价以程序得分和样本效率为主。
  - 原文位置：本地全文：ASD-0930中与实验任务与验证设置直接相关的原文句子；核验TXT行号 146；引文：We evaluate ExpEvolve on 11 open-ended mathematical discovery tasks with a budget of 200 evaluated programs, using SCS as the backbone and the main baseline (Sec.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：01
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：01（仅归档，不覆盖其他模块）
- 模块内分类路径：01.01 数学；01.02 计算机科学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

对象模块与代码沿用输入审计记录（01；01.01, 01.02）；是否纳入与对象分类分开判断。

### 2.3 容易混淆的边界

对象模块与代码沿用输入审计记录（01；01.01, 01.02）；是否纳入与对象分类分开判断。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

自主科研Agent

### 3.2 科研流程角色

科研问题处理；多步行动或评测

ExpEvolve 是带经验抽取和复用机制的演化编码Agent；候选解为程序，显式评价器给出程序及其得分。

### 3.3 自主能力

ExpEvolve 是带经验抽取和复用机制的演化编码Agent；候选解为程序，显式评价器给出程序及其得分。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

工作聚焦数学程序搜索中的经验表示与复用，理论分析高层因素何时有助于样本效率，并实现相应的演化Agent。

### 4.2 系统流程与组件

系统从不同得分的程序中归纳高层 idea factors，将其转化为搜索控制信息，在演化过程中用于候选生成和搜索资源分配。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

实验覆盖 11 项开放式数学发现任务，其中九项来自 SCS 所研究并取自 AlphaEvolve 的问题；评价以程序得分和样本效率为主。

### 5.2 基线、指标与结果

作者报告 idea-level 抽取与复用可改善开放式演化搜索的样本效率；具体幅度须以任务级表格为准，不外推至任意科学领域。

### 5.3 科学贡献与证据强度

工作聚焦数学程序搜索中的经验表示与复用，理论分析高层因素何时有助于样本效率，并实现相应的演化Agent。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

论文以“ExpEvolve: Structuring and Reusing Experience for Open-Ended Discovery”对应的研究任务为对象，具体与哪些既有系统或基准比较，应结合其正文相关工作和实验基线判断；不把工具名称直接视为科学对象。

## 7. 局限性与风险

结果受数学任务、程序表示和显式评价器所限；不能将程序得分提升直接等同于现实科学发现。

## 8. 对综述写作的价值

可用于综述“ExpEvolve: Structuring and Reusing Experience for Open-Ended Discovery”所涉及的Agent任务、研究流程和验证方式；其证据边界为本论文实际报告的任务集与实验结果。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

ExpEvolve 从已评程序中提炼 idea factors，帮助演化Agent复用搜索经验。

### 9.2 速记版 pipeline

系统从不同得分的程序中归纳高层 idea factors，将其转化为搜索控制信息，在演化过程中用于候选生成和搜索资源分配。

### 9.3 标注字段汇总

```text
paper_id=ASD-0930
inclusion_status=to_read
scientific_object_modules=01
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=01
module_taxonomy_codes=01.01;01.02
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`01.01.12` 离散数学与组合数学；二级：`01.01`。
- 原文位置：PDF p.8, Section 5.1; Table 1 p.9。
- 判定：First-hand evidence supports 01.01.12; Tasks. We evaluate on 11 open-ended mathematical discovery tasks. Nine tasks are the problems studied by SCS (Gideoni et al., 2026), which are taken from AlphaEvolve (Novikov et al., 2025), including the first and second autocorrelation inequalities, the uncertainty inequality, the Erdős minimum overlap problem, sums and differences of sets, the max–min distance ratio, the Heilbronn problem for triangles, the kissing
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
