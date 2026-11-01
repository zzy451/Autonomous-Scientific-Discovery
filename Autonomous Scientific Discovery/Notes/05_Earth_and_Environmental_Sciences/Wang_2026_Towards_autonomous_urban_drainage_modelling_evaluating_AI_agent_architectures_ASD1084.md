# Towards autonomous urban drainage modelling: evaluating AI agent architectures for automated SWMM calibration

## 当前分类（2026-11-01 实证复核）

- 当前纳入状态：`to_read`；主归档：`05`。
- 本块为当前有效结论；后文既有分类、来源限制与审计判断均保留为历史记录，与本块不一致者由本块取代。
- 当前对象模块：`05;09`。
- 代表分类每个模块保留一个落点，不表示穷尽全文全部细类。

| 模块 | 二级 | 三级 | 本轮结论 |
|---|---|---|---|
| 05 | 05.03 环境科学 | 05.03.03 水环境科学 | 已落地 |
| 09 | 09.05 土木、建筑与水利工程 | 09.05.07 水利工程 | 已落地 |

- 模块09：实际城市排水模型准备建模校准验证。
  - 证据：PDF 第 [1, 3] 页；原文：completed the automated SWMM calibration task

- 完整裁决：`Coverage_Check/classification_recheck_2026-11-01/`。

## 既有笔记与历史审计记录

**论文信息**

- ID：ASD-1084
- 标题：Towards autonomous urban drainage modelling: evaluating AI agent architectures for automated SWMM calibration
- 作者：Jian Wang; Shuming Liu; Guangtao Fu; Dragan Savic
- 年份：2026
- 来源 / venue：npj Clean Water
- DOI / arXiv / URL：https://www.nature.com/articles/s41545-026-00638-8
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1084.txt
- PDF / 本地文件路径：Reference_PDF/05_Earth_and_Environmental_Sciences/Wang_2026_Towards_autonomous_urban_drainage_modelling_evaluating_AI_agent_architectures_ASD1084.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 研究对象 | 以SWMM模型进行城市排水校准。 | TXT lines 559-562；核验TXT行号 559 | The benchmark system used in this study was based on Case 1 reported by Huang et al25., a synthetic SWMM model derived from the ﬁrst illustrative example in the SWMM manual4. The system comprises 8 subcatchments, 14 nodes and 13 links (Fig. S8), covers 0.287 km2, and was implemented in | 高（一手正文；非独立复现） |
| 数据验证 | 一个降雨事件校准，另一个独立验证。 | TXT lines 572-579；核验TXT行号 572 | Two rainfall events from 29 June 2012 in Bellinge, Denmark41 were selected to test whether a parameter set calibrated for one event remained applicable to a contrasting event. Event 1,with a mean intensity 5.5 mm/h, a peak intensity108 mm/h and a durationof 210 min,was usedforparameter screening and calibration. Event 2, with a mean intensity 7.7 mm/h, a peak intensity 36 mm/h and a duration of 50 min, was withheld for independent validation. The corresponding rainfall hyetographs are shown in Fig. S9. This separation assessed cross-event applicability and prevented informa- | 高（一手正文；非独立复现） |
| 方法链 | 检查数据、生成INP、筛参、校准和验证。 | TXT lines 73-74；核验TXT行号 73 | sation in water distribution networks12, and broader perspectives have highlighted the potential of LLM technologies for hydrological data man- | 高（一手正文；非独立复现） |
| 架构比较 | 三种架构均完成任务但鲁棒性与资源消耗不同。 | TXT lines 417-422；核验TXT行号 417 | This study shows that agent architecture is a central design decision in agentic engineering automation. Under the same SWMM calibration task setting,the three architectures allreached thetargettaskoutcome,butdid so through different execution patterns, with corresponding differences in robustness, token consumption and model dependence. These differences were evident across workﬂow completion, repeated execution, token con- | 高（一手正文；非独立复现） |
| 对象分类 | 校准同时包含城市排水和Agent工程架构评估。 | TXT lines 429-432；核验TXT行号 429 | among architectural choices under realistic task conditions32. Urban drai- nage calibration places further demands on physical-model coupling, intermediate artefact management and hydrological result interpretation, making execution coherence even more consequential33. Recent hydro- | 高（一手正文；非独立复现） |

## 0. 摘要翻译

本文比较三种Agent架构用于自动SWMM城市排水校准，覆盖GIS数据检查、模型输入生成、参数筛选、校准、独立验证及结果报告。三个架构均达到目标结果，但执行模式、鲁棒性、token成本和模型依赖不同。研究以一个降雨事件校准、另一事件独立验证，突出架构对长流程可靠性的影响。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。校准SWMM城市排水模型并检验跨降雨事件表现。
  - 原文位置：TXT lines 559-562；核验TXT行号 559；引文：The benchmark system used in this study was based on Case 1 reported by Huang et al25., a synthetic SWMM model derived from the ﬁrst illustrative example in the SWMM manual4. The system comprises 8 subcatchments, 14 nodes and 13 links (Fig. S8), covers 0.287 km2, and was implemented in
- 多步行动过程：yes。检查GIS和降雨数据、建模、筛参、校准、验证和报告。
  - 原文位置：TXT lines 73-74；核验TXT行号 73；引文：sation in water distribution networks12, and broader perspectives have highlighted the potential of LLM technologies for hydrological data man-
- 至少一种Agent能力：yes。Agent跨阶段执行工具并据中间结果调整后续动作。
  - 原文位置：TXT lines 54-58；核验TXT行号 54；引文：Large language models (LLMs) have recently introduced a different form of automation. Unlike conventional scripts that execute a ﬁxed sequence of predeﬁned operations, LLMs can interpret natural-language task descriptions, generate and execute code, assess intermediate outputs and adjust subsequent actions when unexpected results arise8,9. When
- 明确科研流程角色：yes。比较三种Agent架构对完整SWMM科研建模流程的作用。
  - 原文位置：TXT line 417；核验TXT行号 417；引文：This study shows that agent architecture is a central design decision in

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：05;09
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：05（仅归档，不覆盖其他模块）
- 模块内分类路径：05.03.03 水环境科学；09.05.07 水利工程
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

05对应城市水文/排水对象，09对应科研软件SWMM及Agent工程架构；两类均有实证依据。

### 2.3 容易混淆的边界

05对应城市水文/排水对象，09对应科研软件SWMM及Agent工程架构；两类均有实证依据。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

skill_based；tool_based；multi_agent

### 3.2 科研流程角色

model_calibration；data_processing；validation

比较技能式、工具式和多Agent架构，均调用SWMM、GIS及优化工具并生成工作流工件。

### 3.3 自主能力

Agent跨阶段执行工具并据中间结果调整后续动作。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

科学贡献是城市排水模型跨事件校准案例；系统贡献是同任务条件下比较技能式、工具式和多Agent架构。

### 4.2 系统流程与组件

输入GIS、降雨和观测数据；Agent生成SWMM基准输入，进行Morris敏感性筛选和参数校准，以事件1拟合并将事件2留作独立验证；分析水文图表并写报告，架构之间比较执行稳定性和资源使用。 这一工作流的实施细节、输入输出和验证范围均按原文所报告内容理解，不将展示案例外推为普遍能力。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

合成SWMM案例，两个Bellinge降雨事件；事件1用于校准，事件2独立验证，比较三种Agent架构的目标结果、重复执行、鲁棒性和token成本。

### 5.2 基线、指标与结果

作者报告三种架构均达到目标校准结果，但鲁棒性、资源消耗和模型依赖存在差异。

### 5.3 科学贡献与证据强度

科学贡献是城市排水模型跨事件校准案例；系统贡献是同任务条件下比较技能式、工具式和多Agent架构。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

拓展既有水文模型Agent参数调节研究，转向完整SWMM校准工作流协同。

## 7. 局限性与风险

- author_stated：技能式架构依赖正确选择技能，工具式易受上下文累积影响，多Agent存在交接开销和失败。
- reviewer_inference：合成模型和两场降雨事件的结果不能直接代表真实城市长期运行。

## 8. 对综述写作的价值

可支撑Agent架构本身对完整工程科学工作流鲁棒性的比较论点。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

三类Agent架构完成SWMM校准但在稳定性和资源消耗上各有差异。

### 9.2 速记版 pipeline

输入GIS、降雨和观测数据；Agent生成SWMM基准输入，进行Morris敏感性筛选和参数校准，以事件1拟合并将事件2留作独立验证；分析水文图表并写报告，架构之间比较执行稳定性和资源使用。 这一工作流的实施细节、输入输出和验证范围均按原文所报告内容理解，不将展示案例外推为普遍能力。

### 9.3 标注字段汇总

```text
paper_id=ASD-1084
inclusion_status=to_read
scientific_object_modules=05;09
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=05
module_taxonomy_codes=05.03.03;09.05.07
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。
