# NeuroAct: Advancing EEG Analysis and Decoding via Dual-Loop Autonomous Research

**论文信息**

- ID：ASD-1041
- 标题：NeuroAct: Advancing EEG Analysis and Decoding via Dual-Loop Autonomous Research
- 作者：Xiong, Wei; Li, Jiangtong; Zhao, Han; Yang, Linxiao; Li, Jie; Jiang, Changjun
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2610.25211
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1041.txt
- PDF / 本地文件路径：全文已缓存；PDF尚未归档，详见资料清单
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 双环研究流程 | 内环选择分析/干预，外环跨任务提炼、验证并修订条件化建议。 | Section 2；核验TXT行号 414 | NeuroAct implements a dual-loop autonomous research framework: an inner loop selects analyses and interventions from evidence on signal structure, representations, predictor behavior, and training dynamics, while an outer loop distills, validates, and revises conditional recommendations or experiences across research tasks. | 高（一手正文；非独立复现） |
| Agent具体科研行动 | 协调者分派并行问题，依据审阅证据、实验反馈和剩余预算决定后续行动。 | Section 3；核验TXT行号 744 | The inner loop (Sec. 3.1) decomposes a shared objective into parallel questions, with the Coordinator directing specialists in separate contexts and selecting subsequent actions from reviewed evidence, experimental feedback, and remaining budget. | 高（一手正文；非独立复现） |
| 数据集覆盖和疾病对象 | 评测含年龄回归、工作负荷、运动想象、痴呆分类和睡眠分期；ADFTD明确区分两种痴呆及健康对照。 | Section 4 / dataset description；核验TXT行号 2878 | HBN provides pediatric age regression from resting EEG (Alexander et al., 2017; Shirazi et al., 2024); Workload distinguishes mental-arithmetic conditions (Zyma et al., 2019); PhysioMI (Schalk et al., 2004) and BCIC-IV-2a (Tangermann et al., 2012) provide four-class motor imagery; ADFTD distinguishes Alzheimer’s disease, frontotemporal dementia, and healthy controls (Miltiadous et al., 2023); HMC provides five-stage sleep classification (Alvarez-Estevez and Rijsman, 2021). | 高（一手正文；非独立复现） |
| 疾病分类实验 | ADFTD开放研究中，Agent实现类别平衡并尝试新架构，BA由EEGNet结果提高到ShallowFBCSPNet。 | Results / Setting C；核验TXT行号 1486 | On ADFTD, NeuroAct implements class-balanced training and explores a different architecture, improving BA from 54.93% with EEGNet to 71.26% with ShallowFBCSPNet. | 高（一手正文；非独立复现） |
| 跨数据集经验验证 | PhysioMI经验迁移到BCIC-IV-2a后，准确率提高且研究token降低。 | Appendix G / Table 25；核验TXT行号 1878 | The PhysioMI recommendation directs BCIC-IV-2a research toward retaining CBraMod patch information. The first implementation also changes the training recipe, so the Coordinator requests a narrower comparison that preserves the established recipe. | 高（一手正文；非独立复现） |
| 痴呆预测组合结果 | 样本级ADFTD预测器组合达到74.89% BA，并提高额颞叶痴呆召回。 | Appendix G.6；核验TXT行号 5930 | The Coordinator selects the revised router, which reaches 74.89% BA, 0.729 macro-F1, and 0.843 AUROC. BA improves by 3.63 points over the strongest member and 10.45 points over equal weighting. | 高（一手正文；非独立复现） |
| 主控复核：具体科学对象 | 六个EEG数据集和开放研究设置直接涉及脑电、神经活动及神经系统疾病数据；神经生物学与神经病学均有对象证据。 | TXT line 613；核验TXT行号 613 | The evaluation covers six datasets (HBN (Alexander et al., 2017; Shirazi et al., 2024), Workload (Zyma et al., 2019), PhysioMI (Schalk et al., 2004), BCIC-IV-2a (Tangermann et al., 2012), ADFTD (Miltiadous et al., 2023), and HMC (Alvarez-Estevez and Rijsman, 2 | 高（一手正文；非独立复现） |

## 0. 摘要翻译

NeuroAct是面向EEG分析和解码的双环自主研究Agent。内环协调者并行拆解问题，由Researcher提出分析或干预、Developer执行代码与模型训练、Reviewer核查实现和证据；外环把研究结果整理为带适用条件的建议，并在后续任务中验证或修订。论文在六个EEG数据集及四种研究设置上评估，包括年龄回归、工作负荷、运动想象、ADFTD痴呆分类和睡眠分期。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。明确目标是EEG分析与解码，服务于脑机接口、认知评估和睡眠监测。
  - 原文位置：Abstract；核验TXT行号 349；引文：EEG analysis and decoding underpin brain-computer interfaces, cognitive assessment, and sleep monitoring.
- 多步行动过程：yes。研究流程将共享目标分解为并行问题，并依据已审阅证据、实验反馈及剩余预算选择后续行动。
  - 原文位置：Section 3；核验TXT行号 744；引文：The inner loop (Sec. 3.1) decomposes a shared objective into parallel questions, with the Coordinator directing specialists in separate contexts and selecting subsequent actions from reviewed evidence, experimental feedback, and remaining budget.
- 至少一种Agent能力：yes。协调者组织研究、开发和审阅角色，通过可执行分析或模型修改检验竞争假设。
  - 原文位置：Section 2；核验TXT行号 415；引文：Within the inner loop, the Coordinator directs the Researcher, Developer, and Reviewer to test competing diagnostic hypotheses through executable analyses or model changes, with predictive performance, stability, and cost informing the next action for each task.
- 明确科研流程角色：yes。Researcher使用文献、数据集语义和EEG证据形成方案，开发者实施分析，Reviewer检查证据。
  - 原文位置：Section 3.1；核验TXT行号 770；引文：The Researcher investigates an assigned question using literature, dataset semantics, and EEG evidence, then develops a feasible proposal.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：06;07
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：06（仅归档，不覆盖其他模块）
- 模块内分类路径：06.02.07 神经生物学；07.02.06 神经病学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

六个EEG数据集和开放研究设置直接涉及脑电、神经活动及神经系统疾病数据；神经生物学与神经病学均有对象证据。

### 2.3 容易混淆的边界

六个EEG数据集和开放研究设置直接涉及脑电、神经活动及神经系统疾病数据；神经生物学与神经病学均有对象证据。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM Agent；Multi-Agent System；Tool-using Agent

### 3.2 科研流程角色

experimental_design；tool_use_and_code_execution；data_analysis；result_interpretation

系统由Coordinator、Researcher、Developer、Reviewer组成，维护研究证据、实现结果、经验建议及预算。Researcher读取文献、数据集语义和脑电信号证据；Developer提交并执行分析/训练作业；Reviewer检查方法和证据；Coordinator整合意见并选择下一步。

### 3.3 自主能力

协调者组织研究、开发和审阅角色，通过可执行分析或模型修改检验竞争假设。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

EEG研究贡献是对多种脑信号预测任务开展分析、模型优化和跨任务策略评估；Agent系统贡献是将多角色内环研究与条件化经验外环结合，并以真实EEG任务结果检验。

### 4.2 系统流程与组件

首先将共享EEG目标拆成并行诊断问题；Researcher提出候选解释或模型干预，Developer在隔离工作区实现分析或训练；Reviewer审查代码、数据处理和论证；Coordinator综合预测表现、稳定性、成本及预算选择下一轮。外环把源任务的有效行动写成条件化建议，在目标任务中评估适用性，再依据支持或反证保留、收窄、修改或撤回建议。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

在HBN、Workload、PhysioMI、BCIC-IV-2a、ADFTD及HMC六个EEG数据集上评估年龄回归、工作负荷、运动想象、阿尔茨海默/额颞叶痴呆分类及睡眠分期；比较外部Agent和模型基线，另以跨任务经验迁移、模型组合及能力消融检验研究效果。

### 5.2 基线、指标与结果

作者报告Setting A宏平均80.88，高于BrainAgent的63.13；Setting B将EEGPT平衡准确率从47.50升至54.84；Setting C的ADFTD任务由EEGNet 54.93%升至ShallowFBCSPNet 71.26%；Setting D工作负荷准确率由79.69%升至85.02%。PhysioMI经验迁至BCIC-IV-2a后BA由34.66%升至50.81%，研究token由29.21M降至10.51M。

### 5.3 科学贡献与证据强度

EEG研究贡献是对多种脑信号预测任务开展分析、模型优化和跨任务策略评估；Agent系统贡献是将多角色内环研究与条件化经验外环结合，并以真实EEG任务结果检验。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

相较只调用固定分析流程或按奖励搜索的EEG系统，NeuroAct显式分析信号、表征、预测器及训练动态，支持代码和模型干预，并验证跨任务经验的适用条件。

## 7. 局限性与风险

论文评估范围为四种EEG研究设置和六个数据集，结果依赖特定模型、划分、后端和任务；跨任务经验须按条件筛选并由目标侧证据复核。读者应避免把六数据集上的性能优势外推为普适脑电临床效能，特别是ADFTD数据集性能不等于临床部署验证。

## 8. 对综述写作的价值

可支撑对比单环EEG优化Agent与双环经验学习Agent，展示多角色可执行研究和真实疾病分类任务，同时用跨任务数据、准确率、AUROC及成本说明证据强度。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

NeuroAct以多角色内环和经验复用外环执行EEG研究，在ADFTD等脑电任务上验证模型改进。

### 9.2 速记版 pipeline

首先将共享EEG目标拆成并行诊断问题；Researcher提出候选解释或模型干预，Developer在隔离工作区实现分析或训练；Reviewer审查代码、数据处理和论证；Coordinator综合预测表现、稳定性、成本及预算选择下一轮。外环把源任务的有效行动写成条件化建议，在目标任务中评估适用性，再依据支持或反证保留、收窄、修改或撤回建议。

### 9.3 标注字段汇总

```text
paper_id=ASD-1041
inclusion_status=to_read
scientific_object_modules=06;07
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=06
module_taxonomy_codes=06.02.07;07.02.06
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 PDF补齐归档

- 本地PDF：`Reference_PDF/06_Life_Sciences/ASD-1041_NeuroAct_Advancing_EEG_Analysis_and_Decoding_via_Dual_Loop_Autonomous_Research.pdf`，共30页；已核验标题、页面解析和逐页渲染。
- 下载来源：https://arxiv.org/pdf/2610.25211
- 版本：official arXiv preprint PDF; version as downloaded。
- 本轮为来源文件归档，不自动改变既有科学分类或将未决PR意见标记为已结案。
