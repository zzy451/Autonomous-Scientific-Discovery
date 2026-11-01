# Autonomous discovery of new structure-plausibility laws for explainable and rapid crystal diagnosis and screening

**论文信息**

- ID：ASD-0886
- 标题：Autonomous discovery of new structure-plausibility laws for explainable and rapid crystal diagnosis and screening
- 作者：Song, Zhilong; Cheng, Lixue
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2609.01209
- 一手阅读来源：https://arxiv.org/html/2609.01209
- 来源层级：全文
- 阅读版本：对应缓存来源版本，参见Evidence Log
- 阅读版本题名：Autonomous discovery of new structure-plausibility laws for explainable and rapid crystal diagnosis and screening
- 原始全文缓存：C:/Users/20683/Desktop/综述/.tmp_asd_pdfs/2609.01209.html
- PDF / 本地文件路径：未归档PDF
- 当前状态：included
- 阅读日期：2026-10-22
- 笔记作者：Codex（读者证据包经主控审核整合）

## Evidence Log

| 判断项 | 结论 / 原文概括 | 证据位置 | 可信度 |
|---|---|---|---|
| Agent循环 | Agent提出并实现规律，选择阈值并以留出数据及物理检查尝试反驳。 | Results §2.1 | high |
| 规模 | 572项调查，2,037,606个候选评估。 | Methods/Results | high |
| 规律产出 | 最终8条PRIS规律，覆盖五类晶体化学机制。 | Results §2.1 | high |
| 结构验证 | 实验结构满足率82–99%；严格规则识别87.9%的受损结构。 | Abstract | high |
| 对象边界 | 结构合理性不同于热力学稳定性、动力学稳定性和可合成性。 | Discussion | high |

## 0. 摘要翻译

本文提出无机结构合理性规则PRIS。Agent自主提出晶体化学规律、将其转成可检验假设，并以发现集、留出实验结构和人工扰动反例进行检验及反驳。572项调查评估超过200万候选，最终保留8条规律，涉及短程排斥、离子接触与堆积、静电平衡、键价守恒和晶位复杂性。实验晶体满足规则集的比例为82–99%；最严格规则识别87.9%的受损结构。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 当前判断：included；读者建议：included。
全文明确Agent循环提出、实现、检验和反驳假设，并执行大规模数据/物理检验；研究对象是具体晶体结构。

### 1.2 排除风险检查

核心对象为无机晶体结构和晶体化学，归04.02；化学键规律是解释机制，不是独立分子反应任务。
完整闭环不是纳入门槛；科研目标、多步行动、至少一项Agent能力及明确科研角色须同时成立。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：04
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：04（仅归档，不替代多模块事实）
- 模块内分类路径：04.02
- 分类深度：03/04使用二级；06/07使用固定三级；其余沿用现有树。
- 分类状态：原文证据复核

### 2.2 对象优先判定

572项调查、2,037,606个候选评估，最终8条PRIS规律；实验结构满足率82–99%；严格规则损伤检测率87.9%，距离阈值1.6–3.2%。

### 2.3 容易混淆的边界

核心对象为无机晶体结构和晶体化学，归04.02；化学键规律是解释机制，不是独立分子反应任务。

## 3. Agent 系统与科研流程角色

全文明确Agent循环提出、实现、检验和反驳假设，并执行大规模数据/物理检验；研究对象是具体晶体结构。

科研流程与自主能力以本文实际行动和工具调用为依据：

Agent提议可证伪规律；程序统计描述符并搜索阈值；以发现集提出规律、留出集测试、结构扰动生成反例并做物理检查；失败结论留存供下一轮。

## 4. 方法设计

### 4.1 方法动机与设计

自主发现晶体结构合理性可解释规律，提供独立于稳定性和可合成性的筛选层。

### 4.2 系统流程与组件

Agent提议可证伪规律；程序统计描述符并搜索阈值；以发现集提出规律、留出集测试、结构扰动生成反例并做物理检查；失败结论留存供下一轮。

## 5. 实验与验证

### 5.1 验证方式、对象及任务

572项调查、2,037,606个候选评估，最终8条PRIS规律；实验结构满足率82–99%；严格规则损伤检测率87.9%，距离阈值1.6–3.2%。

### 5.2 基线、指标与结果

572项调查、2,037,606个候选评估，最终8条PRIS规律；实验结构满足率82–99%；严格规则损伤检测率87.9%，距离阈值1.6–3.2%。

### 5.3 科学贡献与证据强度

自主发现晶体结构合理性可解释规律，提供独立于稳定性和可合成性的筛选层。

证据层级：原始全文支持；作者报告结果不等于独立复现。

## 6. 与已有工作的关系

与晶体生成/材料筛选系统相邻；本文产出可解释、可证伪结构规律而非单纯生成器。

## 7. 局限性与风险

规律结果依赖数据、扰动方式和阈值搜索；正文记录11项早先通过的结论后来被反驳；筛选分不能替代稳定性分析。

## 8. 对综述写作的价值

压测材料结构合理性与可合成性边界，并展示Agent科学规律发现。

推荐引用强度：普通引用，可在核对原文后用于相应领域案例。

## 9. 总结

### 9.1 一句话概括

Agent审查晶体结构合理性规则

### 9.2 速记版 pipeline

Agent提议可证伪规律；程序统计描述符并搜索阈值；以发现集提出规律、留出集测试、结构扰动生成反例并做物理检查；失败结论留存供下一轮。

### 9.3 标注字段汇总

```text
paper_id=ASD-0886
inclusion_status=included
scientific_object_modules=04
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=04
module_taxonomy_codes=04.02
source_level=fulltext
fulltext_followup_required=false
```

### 全文后续要求

本轮已读原始全文并完成对象分类；无需为纳入/分类另做全文补读。具体引用时仍需回查相应原文位置。


## 2026-10-29 PDF补齐归档

- 本地PDF：`Reference_PDF/04_Materials_Science/ASD-0886_Autonomous_discovery_of_new_structure_plausibility_laws_for_explainable_and_rapid_crystal_diagnosis_and_s.pdf`，共27页；已核验标题、页面解析和逐页渲染。
- 下载来源：https://arxiv.org/pdf/2609.01209
- 版本：official arXiv preprint PDF; version as downloaded。
- 本轮为来源文件归档，不自动改变既有科学分类或将未决PR意见标记为已结案。
