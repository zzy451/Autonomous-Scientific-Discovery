# RAVA: a robust recurrent active vision agent for plant disease diagnosis under severe environmental noise

**论文信息**

- ID：ASD-1133
- 标题：RAVA: a robust recurrent active vision agent for plant disease diagnosis under severe environmental noise
- 作者：Nima Saeedi; Sana Gholinavaz; Sina Samadi Gharehveran; Kimia Shirini; Adel Taheri Hajivand
- 年份：2026
- 来源 / venue：Scientific Reports
- DOI / arXiv / URL：https://www.nature.com/articles/s41598-026-67160-2
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1133.txt
- PDF / 本地文件路径：Reference_PDF/08_Agricultural_Food_Forestry_Animal_and_Fishery_Sciences/Saeedi_2026_RAVA_a_robust_recurrent_active_vision_agent_for_plant_ASD1133.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 研究对象与任务 | RAVA是面向强噪声环境下植物病害诊断的循环主动视觉代理。代理以PPO学习多步选择图像裁剪和放大观察窗口，将逐步获得的局部线索写入记忆并完成诊断；作者在PlantVillage和更复杂的PlantDoc场景考察严重噪声与环境变化下的鲁棒性。 | 全文TXT第98行；核验TXT行号 98 | lenge of robust decision-making in unconstrained field environments. This section reviews the transition from | 高（一手正文；非独立复现） |
| 系统输入及处理流程 | 每步接收有限图像观察，选择crop/zoom glimpse动作，结合记忆更新病害判断；循环策略根据新观察继续查看或停止并输出类别。 | 全文TXT第411行；核验TXT行号 411 | the competing objectives of classification accuracy, latent structure preservation, and policy entropy without | 高（一手正文；非独立复现） |
| 实验或验证设置 | 每步接收有限图像观察，选择crop/zoom glimpse动作，结合记忆更新病害判断；循环策略根据新观察继续查看或停止并输出类别。 | 全文TXT第669行；核验TXT行号 669 | To quantify the individual contributions of the proposed modules, we conducted an ablation study under the | 高（一手正文；非独立复现） |
| 作者报告的贡献 | 在PlantVillage及包含田间光照、遮挡和背景变化的PlantDoc上评估分类与噪声鲁棒性，对照单次分类及其他视觉方法。 | 全文TXT第790行；核验TXT行号 790 | despite using a lighter CNN backbone, demonstrates superior resilience with an accuracy of 77.0% under heavy | 高（一手正文；非独立复现） |
| 适用范围与边界 | 科学对象为农作物叶片病害诊断，属08农业植物保护。虽观察环境是图像模拟窗口，代理仍执行序贯感知和决策；对象证据明确，建议纳入candidate。 | 全文TXT第979行；核验TXT行号 979 | Table 8 Comparison of model performance (Accuracy and Macro-F1, %) under clean, heavy, and brutal noise for the | 高（一手正文；非独立复现） |

## 0. 摘要翻译

RAVA是面向强噪声环境下植物病害诊断的循环主动视觉代理。代理以PPO学习多步选择图像裁剪和放大观察窗口，将逐步获得的局部线索写入记忆并完成诊断；作者在PlantVillage和更复杂的PlantDoc场景考察严重噪声与环境变化下的鲁棒性。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。RAVA是面向强噪声环境下植物病害诊断的循环主动视觉代理。代理以PPO学习多步选择图像裁剪和放大观察窗口，将逐步获得的局部线索写入记忆并完成诊断；作者在PlantVillage和更复杂的PlantDoc场景考察严重噪声与环境变化下的鲁棒性。
  - 原文位置：全文TXT第98行；核验TXT行号 98；引文：lenge of robust decision-making in unconstrained field environments. This section reviews the transition from
- 多步行动过程：yes。每步接收有限图像观察，选择crop/zoom glimpse动作，结合记忆更新病害判断；循环策略根据新观察继续查看或停止并输出类别。
  - 原文位置：全文TXT第411行；核验TXT行号 411；引文：the competing objectives of classification accuracy, latent structure preservation, and policy entropy without
- 至少一种Agent能力：yes。每步接收有限图像观察，选择crop/zoom glimpse动作，结合记忆更新病害判断；循环策略根据新观察继续查看或停止并输出类别。
  - 原文位置：全文TXT第669行；核验TXT行号 669；引文：To quantify the individual contributions of the proposed modules, we conducted an ablation study under the
- 明确科研流程角色：yes。科学对象为农作物叶片病害诊断，属08农业植物保护。虽观察环境是图像模拟窗口，代理仍执行序贯感知和决策；对象证据明确，建议纳入candidate。
  - 原文位置：全文TXT第790行；核验TXT行号 790；引文：despite using a lighter CNN backbone, demonstrates superior resilience with an accuracy of 77.0% under heavy

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：08
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：08（仅归档，不覆盖其他模块）
- 模块内分类路径：08.01.06 植物保护
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

科学对象为农作物叶片病害诊断，属08农业植物保护。虽观察环境是图像模拟窗口，代理仍执行序贯感知和决策；对象证据明确，建议纳入candidate。

### 2.3 容易混淆的边界

科学对象为农作物叶片病害诊断，属08农业植物保护。虽观察环境是图像模拟窗口，代理仍执行序贯感知和决策；对象证据明确，建议纳入candidate。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签



### 3.2 科研流程角色



每步接收有限图像观察，选择crop/zoom glimpse动作，结合记忆更新病害判断；循环策略根据新观察继续查看或停止并输出类别。

### 3.3 自主能力

每步接收有限图像观察，选择crop/zoom glimpse动作，结合记忆更新病害判断；循环策略根据新观察继续查看或停止并输出类别。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

科学对象为农作物叶片病害诊断，属08农业植物保护。虽观察环境是图像模拟窗口，代理仍执行序贯感知和决策；对象证据明确，建议纳入candidate。

### 4.2 系统流程与组件

每步接收有限图像观察，选择crop/zoom glimpse动作，结合记忆更新病害判断；循环策略根据新观察继续查看或停止并输出类别。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

每步接收有限图像观察，选择crop/zoom glimpse动作，结合记忆更新病害判断；循环策略根据新观察继续查看或停止并输出类别。 验证以文中所列任务、数据和对照为准。

### 5.2 基线、指标与结果

在PlantVillage及包含田间光照、遮挡和背景变化的PlantDoc上评估分类与噪声鲁棒性，对照单次分类及其他视觉方法。

### 5.3 科学贡献与证据强度

科学对象为农作物叶片病害诊断，属08农业植物保护。虽观察环境是图像模拟窗口，代理仍执行序贯感知和决策；对象证据明确，建议纳入candidate。

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

RAVA是面向强噪声环境下植物病害诊断的循环主动视觉代理。代理以PPO学习多步选择图像裁剪和放大观察窗口，将逐步获得的局部线索写入记忆并完成诊断；作者在PlantVillage和更复杂的PlantDoc场景考察严重噪声与环境变化下的鲁棒性。

### 9.2 速记版 pipeline

每步接收有限图像观察，选择crop/zoom glimpse动作，结合记忆更新病害判断；循环策略根据新观察继续查看或停止并输出类别。

### 9.3 标注字段汇总

```text
paper_id=ASD-1133
inclusion_status=to_read
scientific_object_modules=08
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=08
module_taxonomy_codes=08.01.06
source_level=first_hand_full_text
fulltext_followup_required=true
```

### 全文后续要求

当前纳入和分类证据已足够；第7节明确的结果/复现细节仍需继续回查。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O2 既定基准 | 植物病害图像分类在预定义数据集上评测 | “PlantVillage和更复杂的PlantDoc” · L29 |
| 验证强度 | V1 基准/内部评测 | 在标准数据集上评估分类准确率，属基准评测 | “在PlantVillage及包含田间光照、遮挡和背景变化的PlantDoc上评估” · L105 |
| 系统自主性 | L2 闭环执行者 | Agent以强化学习自主选择多步观察窗口并更新诊断 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
