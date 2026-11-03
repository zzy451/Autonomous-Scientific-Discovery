# WhatWorkedBench: Benchmarking Experimental Understanding in AI Agents

## 当前分类（2026-11-01 补证复核）

- 当前纳入状态：`to_read`；主归档：`01`。
- 当前对象模块：`01;02;05;07;08;09`。
- 本节为当前结论，取代后文不一致的历史分类；每个模块保留一个有证据支持的代表落点。

| 模块 | 二级 | 三级 | 当前状态 |
|---|---|---|---|
| 01 | 01.02 计算机科学 | 01.02.13 机器学习 | 已确定 |
| 02 | 02.01 天文学与天体物理学 | 02.01.02 太阳物理学 | 已确定 |
| 05 | 05.02 大气、海洋与水文科学 | 05.02.02 气候科学 | 已确定 |
| 07 | 07.02 临床医学 | 07.02.05 肿瘤学 | 已确定 |
| 08 | 08.01 农学 | 08.01.07 种子科学与育种 | 已确定 |
| 09 | 09.05 土木、建筑与水利工程 | 09.05.05 建筑学 | 已确定 |

### 模块08补证

- 原缺项原因：前轮缺少原始数据集标签的品种语义，未裁定作物学与种子科学边界。
- 本轮结论：论文实际执行并冷回放全部native目录任务；UCI原始元数据明确Dry Bean为7个登记品种的种子形态分类，Seeds为Kama/Rosa/Canadian三品种小麦籽粒几何特征。论文以原始类别计算K-means聚类NMI。按更具体的种子形态/品种类别对象归08.01.07种子科学与育种。
- 来源：local PDF；位置：pp.4–6,15–16；原文：K-means fits the feature representation for each mask, and the original class labels enter the external NMI calculation.
- 来源：https://archive.ics.uci.edu/api/dataset?id=602；位置：data.additional_info.summary；原文：A computer vision system was developed to distinguish seven different registered varieties of dry beans with similar features in order to obtain uniform seed classification.
- 来源：https://archive.ics.uci.edu/api/dataset?id=236；位置：data.additional_info.summary；原文：The examined group comprised kernels belonging to three different varieties of wheat: Kama, Rosa and Canadian
- 解释范围：仅指种子形态与品种类别benchmark，不代表种子活力、遗传改良或育种效果验证；两项不属于正文108-episode核心Agent子集，归属依据为已执行native benchmark任务。

- [本轮补证报告](../../Coverage_Check/classification_recheck_2026-11-01/completion_report.md)。

## 既有笔记与历史审计记录

**论文信息**

- ID：ASD-1093
- 标题：WhatWorkedBench: Benchmarking Experimental Understanding in AI Agents
- 作者：Jingjie Ning; Xueqi Li; Yibo Kong; Dongting Li
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2609.27490
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1093.txt
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Ning_2026_WhatWorkedBench_Benchmarking_Experimental_Understanding_in_AI_Agents_ASD1093.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 研究对象与任务 | WhatWorkedBench研究AI研究代理能否从有限测量理解计算实验中组件变化的条件效应。作者构建30个数据源、36种任务条件的基准，覆盖分类、回归、聚类、时间序列预测、图像恢复、检索及心搏检测，并提供穷举计算参考结果。代理检查工作流代码、购买测量、推断响应面并提交预测。 | 全文TXT第897行；核验TXT行号 897 | selection regret maxz⁡ut​(z)−ut​(arg⁡maxz​u^t​(z))\max_{z}u_{t}(z)-u_{t}(\arg\max_{z}\hat{u}_{t}(z)). Prediction ties | 高（一手正文；非独立复现） |
| 系统输入及处理流程 | 代理读取计算工作流、选择并购买预算内测量，利用成对组件效应推断配置分数，最终输出完整响应面及最优配置；作者以穷举原生执行结果评分。基准中可见医学心电、气候水文、太阳黑子、材料/工程及农业等直接任务对象。 | 全文TXT第3591行；核验TXT行号 3591 | Logistic regression uses the LBFGS solver, 3,000 maximum iterations, and random | 高（一手正文；非独立复现） |
| 实验或验证设置 | 代理读取计算工作流、选择并购买预算内测量，利用成对组件效应推断配置分数，最终输出完整响应面及最优配置；作者以穷举原生执行结果评分。基准中可见医学心电、气候水文、太阳黑子、材料/工程及农业等直接任务对象。 | 全文TXT第5392行；核验TXT行号 5392 | Shared fitting passes the exact observed set from an episode to D1, D2, or the | 高（一手正文；非独立复现） |
| 作者报告的贡献 | 正文报告36个任务条件、30个来源、1248条配置记录及4206项数值控制；另评估核心代理回合和新增来源表现。具体模型差值引用表格时须保留统计口径。 | 全文TXT第7115行；核验TXT行号 7115 | uses no new measurements. All eight episodes deliver valid artifacts. | 高（一手正文；非独立复现） |
| 适用范围与边界 | 方法学贡献是可执行的实验理解评测和条件效应数据。对象覆盖不能仅列抽象方法：如MIT-BIH心搏事件检测、CO2/El Niño/Nile及sunspots时间序列预测、混凝土强度/建筑能耗回归、干豆聚类均有明示输入和目标，应增加07、05、02、09、08对象模块；01保留为方法核心。 | 全文TXT第8657行；核验TXT行号 8657 | averages recovery among those exact-choice cases. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

WhatWorkedBench研究AI研究代理能否从有限测量理解计算实验中组件变化的条件效应。作者构建30个数据源、36种任务条件的基准，覆盖分类、回归、聚类、时间序列预测、图像恢复、检索及心搏检测，并提供穷举计算参考结果。代理检查工作流代码、购买测量、推断响应面并提交预测。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。WhatWorkedBench研究AI研究代理能否从有限测量理解计算实验中组件变化的条件效应。作者构建30个数据源、36种任务条件的基准，覆盖分类、回归、聚类、时间序列预测、图像恢复、检索及心搏检测，并提供穷举计算参考结果。代理检查工作流代码、购买测量、推断响应面并提交预测。
  - 原文位置：全文TXT第897行；核验TXT行号 897；引文：selection regret maxz⁡ut​(z)−ut​(arg⁡maxz​u^t​(z))\max_{z}u_{t}(z)-u_{t}(\arg\max_{z}\hat{u}_{t}(z)). Prediction ties
- 多步行动过程：yes。代理读取计算工作流、选择并购买预算内测量，利用成对组件效应推断配置分数，最终输出完整响应面及最优配置；作者以穷举原生执行结果评分。基准中可见医学心电、气候水文、太阳黑子、材料/工程及农业等直接任务对象。
  - 原文位置：全文TXT第3591行；核验TXT行号 3591；引文：Logistic regression uses the LBFGS solver, 3,000 maximum iterations, and random
- 至少一种Agent能力：yes。代理读取计算工作流、选择并购买预算内测量，利用成对组件效应推断配置分数，最终输出完整响应面及最优配置；作者以穷举原生执行结果评分。基准中可见医学心电、气候水文、太阳黑子、材料/工程及农业等直接任务对象。
  - 原文位置：全文TXT第5392行；核验TXT行号 5392；引文：Shared fitting passes the exact observed set from an episode to D1, D2, or the
- 明确科研流程角色：yes。方法学贡献是可执行的实验理解评测和条件效应数据。对象覆盖不能仅列抽象方法：如MIT-BIH心搏事件检测、CO2/El Niño/Nile及sunspots时间序列预测、混凝土强度/建筑能耗回归、干豆聚类均有明示输入和目标，应增加07、05、02、09、08对象模块；01保留为方法核心。
  - 原文位置：全文TXT第7115行；核验TXT行号 7115；引文：uses no new measurements. All eight episodes deliver valid artifacts.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：01;02;05;07;08;09
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：01（仅归档，不覆盖其他模块）
- 模块内分类路径：01.02.13 机器学习；01.02.17 科学计算与高性能计算；02.01.02 太阳物理学；02.01.04 星系与星系演化；05.02.02 气候科学；05.02.07 水文学；07.02.05 肿瘤学；07.02.09 心血管病学；07.03.08 医学信息学；08.01.01 作物学；09.05.02 结构工程；09.05.05 建筑学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

- sunspots太阳黑子序列预测；Hubble Deep Field图像恢复
- CO2与El Niño气候时间序列预测及Nile水文序列预测
- 乳腺癌诊断分类及MIT-BIH心电心搏检测
- 干豆/种子分类与聚类
- 混凝土强度回归及建筑供暖负荷回归

### 2.3 容易混淆的边界

保留01计算方法模块；Appendix B/C明确列出可执行的领域任务。sunspots属于02.01.02太阳物理，Hubble Deep Field恢复作为02.01.04天文学任务；CO2与El Niño预测属05.02.02气候科学，Nile流量预测属05.02.07水文学；乳腺诊断分类属07.02.05，心搏检测属07.02.09并可作为07.03.08医学信息学任务；干豆/种子属08.01.01；混凝土强度及建筑供暖负荷分别对应09.05.02结构工程和09.05.05建筑学。各对象由公开任务输入及预测/分类目标直接体现，不要求benchmark产生新领域知识。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签



### 3.2 科研流程角色



代理读取计算工作流、选择并购买预算内测量，利用成对组件效应推断配置分数，最终输出完整响应面及最优配置；作者以穷举原生执行结果评分。基准中可见医学心电、气候水文、太阳黑子、材料/工程及农业等直接任务对象。

### 3.3 自主能力

代理读取计算工作流、选择并购买预算内测量，利用成对组件效应推断配置分数，最终输出完整响应面及最优配置；作者以穷举原生执行结果评分。基准中可见医学心电、气候水文、太阳黑子、材料/工程及农业等直接任务对象。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

方法学贡献是可执行的实验理解评测和条件效应数据。对象覆盖不能仅列抽象方法：如MIT-BIH心搏事件检测、CO2/El Niño/Nile及sunspots时间序列预测、混凝土强度/建筑能耗回归、干豆聚类均有明示输入和目标，应增加07、05、02、09、08对象模块；01保留为方法核心。

### 4.2 系统流程与组件

代理读取计算工作流、选择并购买预算内测量，利用成对组件效应推断配置分数，最终输出完整响应面及最优配置；作者以穷举原生执行结果评分。基准中可见医学心电、气候水文、太阳黑子、材料/工程及农业等直接任务对象。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

代理读取计算工作流、选择并购买预算内测量，利用成对组件效应推断配置分数，最终输出完整响应面及最优配置；作者以穷举原生执行结果评分。基准中可见医学心电、气候水文、太阳黑子、材料/工程及农业等直接任务对象。 验证以文中所列任务、数据和对照为准。

### 5.2 基线、指标与结果

正文报告36个任务条件、30个来源、1248条配置记录及4206项数值控制；另评估核心代理回合和新增来源表现。具体模型差值引用表格时须保留统计口径。

### 5.3 科学贡献与证据强度

方法学贡献是可执行的实验理解评测和条件效应数据。对象覆盖不能仅列抽象方法：如MIT-BIH心搏事件检测、CO2/El Niño/Nile及sunspots时间序列预测、混凝土强度/建筑能耗回归、干豆聚类均有明示输入和目标，应增加07、05、02、09、08对象模块；01保留为方法核心。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

与一般LLM代理、科学工作流自动化及该领域既有基准/模型相关；本文的具体差异见上述任务设计和验证设置。

## 7. 局限性与风险

本文结果受其数据、模拟环境、评测指标和实验预算限制；不得将基准或仿真表现直接外推为真实部署成效。

## 8. 对综述写作的价值

可用于综述讨论该类Agent的研究对象、工作流角色和验证边界。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

WhatWorkedBench研究AI研究代理能否从有限测量理解计算实验中组件变化的条件效应。作者构建30个数据源、36种任务条件的基准，覆盖分类、回归、聚类、时间序列预测、图像恢复、检索及心搏检测，并提供穷举计算参考结果。代理检查工作流代码、购买测量、推断响应面并提交预测。

### 9.2 速记版 pipeline

代理读取计算工作流、选择并购买预算内测量，利用成对组件效应推断配置分数，最终输出完整响应面及最优配置；作者以穷举原生执行结果评分。基准中可见医学心电、气候水文、太阳黑子、材料/工程及农业等直接任务对象。

### 9.3 标注字段汇总

```text
paper_id=ASD-1093
inclusion_status=to_read
scientific_object_modules=01;02;05;07;08;09
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=01
module_taxonomy_codes=01.02.13;01.02.17;02.01.02;02.01.04;05.02.02;05.02.07;07.02.05;07.02.09;07.03.08;08.01.01;09.05.02;09.05.05
source_level=first_hand_full_text
fulltext_followup_required=true
```

### 全文后续要求

当前纳入和分类证据已足够；第7节明确的结果/复现细节仍需继续回查。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O2 既定基准 | 36种任务条件的固定基准，带穷举计算参考结果 | “30个数据源、36种任务条件的基准” · L57 |
| 验证强度 | V1 基准/内部评测 | 以穷举原生执行结果评分，属基准评测 | “作者以穷举原生执行结果评分” · L133 |
| 系统自主性 | L1 任务助手 | Agent执行委派的配置选择和测量购买任务 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
