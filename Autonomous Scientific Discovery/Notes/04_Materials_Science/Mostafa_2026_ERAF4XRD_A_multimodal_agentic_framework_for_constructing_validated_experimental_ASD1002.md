# ERAF4XRD: A multimodal agentic framework for constructing validated experimental X-ray diffraction databases from scientific literature

**论文信息**

- ID：ASD-1002
- 标题：ERAF4XRD: A multimodal agentic framework for constructing validated experimental X-ray diffraction databases from scientific literature
- 作者：Afnan Mostafa; William Ratcliff; Simon J. L. Billinge; Niaz Abdolrahim
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2609.18583
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1002.txt
- PDF / 本地文件路径：Reference_PDF/04_Materials_Science/Mostafa_2026_ERAF4XRD_A_multimodal_agentic_framework_for_constructing_validated_experimental_ASD1002.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 纳入与科学目标 | ERAF4XRD是多模态多Agent框架，目标是将文献中的实验XRD图谱、上下文和元数据重建为经过验证的结构化记录。流程下载筛选文档、识别XRD图、提取相关字段并连接原文证据，由独立验证Agent核验输出。作者在273篇文献、3150幅候选图上评估，最终记录具备可追溯的出处。 | 摘要；TXT第16行；核验TXT行号 16 | The scientific literature contains decades of experimental measurements that remain difficult to access as structured data for modern AI and data-driven research. | 高（一手正文；非独立复现） |
| 方法与多步工作流 | 系统先检索/下载论文并由Agent通过PDF搜索、页面查看等工具筛选；随后以栅格和矢量方法提取候选图，识别XRD图并抽取图级元数据，将文本、图表和字段建立关联。独立验证Agent对照来源证据检查记录，保留工具轨迹及最终接受/拒绝判断。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。 | 摘要；TXT第20行；核验TXT行号 20 | , image and text), multi-agent framework that reconstructs validated X-ray diffraction (XRD) records from scien- tific publications. | 高（一手正文；非独立复现） |
| Agent能力与行动 | ERAF4XRD: A multimodal agentic framework for constructing validated experimental X-ray diffraction databases from scientific literature。系统角色与能力：系统先检索/下载论文并由Agent通过PDF搜索、页面查看等工具筛选；随后以栅格和矢量方法提取候选图，识别XRD图并抽取图级元数据，将文本、图表和字段建立关联。独立验证Agent对照来源证据检查记录，保留工具轨迹及最终接受/拒绝判断。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。 | 摘要；TXT第27行；核验TXT行号 27 | 7% recall, with no unsupported metadata observed among 443 evaluated fields. By moving beyond information extraction to the reconstruc- tion and validation of linked experimental records, ERAF4xrd establishes an automated approach for transforming published scientific information into machine-readable experimental datasets for AI and data-driven science. | 高（一手正文；非独立复现） |
| 验证与结果 | 在273篇文献、3150幅候选图基准中，XRD图识别准确率最高98.7%，提取22个字段共1400项元数据；人工评估最终记录精确率98.5%、召回率90.7%，443个审查字段未发现无来源支持的元数据。 | 正文；TXT第24行；核验TXT行号 24 | On a manually curated benchmark of 273 scientific publica- tions containing 3,150 candidate figures, ERAF4xrd achieved up to 98.7% accuracy for XRD figure identification and generated 1,400 metadata values across 22 fields. | 高（一手正文；非独立复现） |
| 贡献及适用对象 | 可支持综述讨论多模态Agent将论文图表转成有上下文、经验证科学数据集的能力。 科学贡献与系统贡献按上述证据分别表述。 | 摘要；TXT第17行；核验TXT行号 17 | Much of this information is distributed across figures, captions, text, and tables, requiring experimental data and their context to be identi- fied, connected, and verified before they can be reused. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

ERAF4XRD是多模态多Agent框架，目标是将文献中的实验XRD图谱、上下文和元数据重建为经过验证的结构化记录。流程下载筛选文档、识别XRD图、提取相关字段并连接原文证据，由独立验证Agent核验输出。作者在273篇文献、3150幅候选图上评估，最终记录具备可追溯的出处。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。ERAF4XRD是多模态多Agent框架，目标是将文献中的实验XRD图谱、上下文和元数据重建为经过验证的结构化记录。流程下载筛选文档、识别XRD图、提取相关字段并连接原文证据，由独立验证Agent核验输出。作者在273篇文献、3150幅候选图上评估，最终记录具备可追溯的出处。
  - 原文位置：摘要；TXT第16行；核验TXT行号 16；引文：The scientific literature contains decades of experimental measurements that remain difficult to access as structured data for modern AI and data-driven research.
- 多步行动过程：yes。系统先检索/下载论文并由Agent通过PDF搜索、页面查看等工具筛选；随后以栅格和矢量方法提取候选图，识别XRD图并抽取图级元数据，将文本、图表和字段建立关联。独立验证Agent对照来源证据检查记录，保留工具轨迹及最终接受/拒绝判断。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。
  - 原文位置：正文；TXT第19行；核验TXT行号 19；引文：Here we introduce ERAF4xrd (Experiment Reader Agentic Framework for X-Ray Diffraction), a fully automated multimodal (i.e., image and text), multi-agent framework that reconstructs validated X-ray diffraction (XRD) records from scien- tific publications.
- 至少一种Agent能力：yes。ERAF4XRD: A multimodal agentic framework for constructing validated experimental X-ray diffraction databases from scientific literature。系统角色与能力：系统先检索/下载论文并由Agent通过PDF搜索、页面查看等工具筛选；随后以栅格和矢量方法提取候选图，识别XRD图并抽取图级元数据，将文本、图表和字段建立关联。独立验证Agent对照来源证据检查记录，保留工具轨迹及最终接受/拒绝判断。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。
  - 原文位置：正文；TXT第22行；核验TXT行号 22；引文：ERAF4xrd downloads and screens documents, identifies XRD figures, extracts and links metadata to the corresponding experimental data, and validates outputs against source evidence using an independent validation agent.
- 明确科研流程角色：yes。在273篇文献、3150幅候选图基准中，XRD图识别准确率最高98.7%，提取22个字段共1400项元数据；人工评估最终记录精确率98.5%、召回率90.7%，443个审查字段未发现无来源支持的元数据。
  - 原文位置：正文；TXT第26行；核验TXT行号 26；引文：Independent manual assessment of the final validated records yielded 98.5% precision and 90.7% recall, with no unsupported metadata observed among 443 evaluated fields. By moving beyond information extraction to the reconstruc- tion and validation of linked experimental records, ERAF4xrd establishes an automated approach for transforming published scientific information into machine-readable experimental datasets for AI and data-driven science.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：04
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：04（仅归档，不覆盖其他模块）
- 模块内分类路径：04.01 材料基础；04.02 结构材料与无机材料
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

对象是实验XRD数据及实验数据库构建，归04.01/04.02。科学文献是数据来源，重点在实验数据重建和独立证据核验。

### 2.3 容易混淆的边界

对象是实验XRD数据及实验数据库构建，归04.01/04.02。科学文献是数据来源，重点在实验数据重建和独立证据核验。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM科研Agent

### 3.2 科研流程角色

计算/数据分析

ERAF4XRD: A multimodal agentic framework for constructing validated experimental X-ray diffraction databases from scientific literature。系统角色与能力：系统先检索/下载论文并由Agent通过PDF搜索、页面查看等工具筛选；随后以栅格和矢量方法提取候选图，识别XRD图并抽取图级元数据，将文本、图表和字段建立关联。独立验证Agent对照来源证据检查记录，保留工具轨迹及最终接受/拒绝判断。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 3.3 自主能力

ERAF4XRD: A multimodal agentic framework for constructing validated experimental X-ray diffraction databases from scientific literature。系统角色与能力：系统先检索/下载论文并由Agent通过PDF搜索、页面查看等工具筛选；随后以栅格和矢量方法提取候选图，识别XRD图并抽取图级元数据，将文本、图表和字段建立关联。独立验证Agent对照来源证据检查记录，保留工具轨迹及最终接受/拒绝判断。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

可支持综述讨论多模态Agent将论文图表转成有上下文、经验证科学数据集的能力。 科学贡献与系统贡献按上述证据分别表述。

### 4.2 系统流程与组件

系统先检索/下载论文并由Agent通过PDF搜索、页面查看等工具筛选；随后以栅格和矢量方法提取候选图，识别XRD图并抽取图级元数据，将文本、图表和字段建立关联。独立验证Agent对照来源证据检查记录，保留工具轨迹及最终接受/拒绝判断。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

在273篇文献、3150幅候选图基准中，XRD图识别准确率最高98.7%，提取22个字段共1400项元数据；人工评估最终记录精确率98.5%、召回率90.7%，443个审查字段未发现无来源支持的元数据。

### 5.2 基线、指标与结果

在273篇文献、3150幅候选图基准中，XRD图识别准确率最高98.7%，提取22个字段共1400项元数据；人工评估最终记录精确率98.5%、召回率90.7%，443个审查字段未发现无来源支持的元数据。

### 5.3 科学贡献与证据强度

可支持综述讨论多模态Agent将论文图表转成有上下文、经验证科学数据集的能力。 科学贡献与系统贡献按上述证据分别表述。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

本文承接科学文献抽取和XRD数据库建设，进一步利用多模态图表识别并把元数据与原文证据连接，再由独立Agent验证。

## 7. 局限性与风险

作者及读者可确认的适用边界：基准覆盖273篇文献及特定XRD图表/字段；文献格式、图像质量和元数据规范变化可能影响抽取与验证效果。

## 8. 对综述写作的价值

可支持综述讨论多模态Agent将论文图表转成有上下文、经验证科学数据集的能力。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

ERAF4XRD是多模态多Agent框架，目标是将文献中的实验XRD图谱、上下文和元数据重建为经过验证的结构化记录。

### 9.2 速记版 pipeline

系统先检索/下载论文并由Agent通过PDF搜索、页面查看等工具筛选；随后以栅格和矢量方法提取候选图，识别XRD图并抽取图级元数据，将文本、图表和字段建立关联。独立验证Agent对照来源证据检查记录，保留工具轨迹及最终接受/拒绝判断。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 9.3 标注字段汇总

```text
paper_id=ASD-1002
inclusion_status=to_read
scientific_object_modules=04
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=04
module_taxonomy_codes=04.01;04.02
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`04.01.03` 材料表征；二级：`04.01`。
- 原文位置：PDF p.5。
- 判定：XRD图谱的提取及测量元数据重建，归材料表征。
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
