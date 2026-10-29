# Hierarchical automation of scanning probe microscopy through agentic orchestration and algorithmic control

**论文信息**

- ID：ASD-0986
- 标题：Hierarchical automation of scanning probe microscopy through agentic orchestration and algorithmic control
- 作者：Boris N. Slautin; Sheryl L. Sanchez; Aidan Swanger; Yu Liu; Gerd Duscher; Vladimir V. Shvartsman; Mahshid Ahmadi; Sergei V. Kalinin
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2609.04015
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0986.txt
- PDF / 本地文件路径：Reference_PDF/04_Materials_Science/Slautin_2026_Hierarchical_automation_of_scanning_probe_microscopy_through_agentic_orchestration_ASD0986.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 纳入与科学目标 | 论文提出扫描探针显微镜分层自动化架构，把意图解释、实验表征构建、证据评估和高层决策交给Agent，把数值分析、坐标选取、验证及仪器执行交给确定性算法。系统用于压电响应力显微镜，围绕局部畴结构与极化翻转关系开展测量，并依据证据决定适应波形、选择局部测点及停止实验。 | 摘要；TXT第16行；核验TXT行号 16 | Rapid advances in agentic artificial intelligence enable scientific systems to interpret open- ended objectives, combine heterogeneous information, invoke specialized tools, and revise experimental strategies as evidence accumulates. | 高（一手正文；非独立复现） |
| 方法与多步工作流 | Agent接收关于局部畴结构与极化翻转的开放问题，构造空间描述并选择后续测量；确定性算法负责图像数值处理、坐标定位、波形/动作验证和仪器执行。新测量结果返回Agent更新判断，若新增测量不再提供新证据则终止。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。 | 摘要；TXT第22行；核验TXT行号 22 | Here, we introduce a hierarchical architecture for autonomous experimentation that separates these roles. | 高（一手正文；非独立复现） |
| Agent能力与行动 | Hierarchical automation of scanning probe microscopy through agentic orchestration and algorithmic control。系统角色与能力：Agent接收关于局部畴结构与极化翻转的开放问题，构造空间描述并选择后续测量；确定性算法负责图像数值处理、坐标定位、波形/动作验证和仪器执行。新测量结果返回Agent更新判断，若新增测量不再提供新证据则终止。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。 | 摘要；TXT第34行；核验TXT行号 34 | These results demonstrate a route toward scientific autonomy in which agents determine what evidence is required while algorithms determine how that evidence is acquired reproducibly and within validated physical constraints. | 高（一手正文；非独立复现） |
| 验证与结果 | 案例为压电响应力显微镜中的局部滞回测量与适应性实验路径。作者报告发现极化状态与畴壁距离的混杂关系，并识别所需对比在当前视野中无法独立表示；重点验证安全、可复现的层级控制。 | 摘要；TXT第18行；核验TXT行号 18 | However, physical experimentation also contains many tasks for which agentic reasoning provides little advantage and can reduce reliability. | 高（一手正文；非独立复现） |
| 贡献及适用对象 | 支持综述讨论Agent与算法分工、科学实验中的物理约束及何时应停止采集。 科学贡献与系统贡献按上述证据分别表述。 | 摘要；TXT第20行；核验TXT行号 20 | Quantitative analysis, optimization, spatial targeting, validation, and instrument execution are often better posed as deterministic or algorithmic operations with explicit objectives and verifiable outputs. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

论文提出扫描探针显微镜分层自动化架构，把意图解释、实验表征构建、证据评估和高层决策交给Agent，把数值分析、坐标选取、验证及仪器执行交给确定性算法。系统用于压电响应力显微镜，围绕局部畴结构与极化翻转关系开展测量，并依据证据决定适应波形、选择局部测点及停止实验。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。论文提出扫描探针显微镜分层自动化架构，把意图解释、实验表征构建、证据评估和高层决策交给Agent，把数值分析、坐标选取、验证及仪器执行交给确定性算法。系统用于压电响应力显微镜，围绕局部畴结构与极化翻转关系开展测量，并依据证据决定适应波形、选择局部测点及停止实验。
  - 原文位置：摘要；TXT第16行；核验TXT行号 16；引文：Rapid advances in agentic artificial intelligence enable scientific systems to interpret open- ended objectives, combine heterogeneous information, invoke specialized tools, and revise experimental strategies as evidence accumulates.
- 多步行动过程：yes。Agent接收关于局部畴结构与极化翻转的开放问题，构造空间描述并选择后续测量；确定性算法负责图像数值处理、坐标定位、波形/动作验证和仪器执行。新测量结果返回Agent更新判断，若新增测量不再提供新证据则终止。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。
  - 原文位置：摘要；TXT第22行；核验TXT行号 22；引文：Here, we introduce a hierarchical architecture for autonomous experimentation that separates these roles.
- 至少一种Agent能力：yes。Hierarchical automation of scanning probe microscopy through agentic orchestration and algorithmic control。系统角色与能力：Agent接收关于局部畴结构与极化翻转的开放问题，构造空间描述并选择后续测量；确定性算法负责图像数值处理、坐标定位、波形/动作验证和仪器执行。新测量结果返回Agent更新判断，若新增测量不再提供新证据则终止。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。
  - 原文位置：摘要；TXT第34行；核验TXT行号 34；引文：These results demonstrate a route toward scientific autonomy in which agents determine what evidence is required while algorithms determine how that evidence is acquired reproducibly and within validated physical constraints.
- 明确科研流程角色：yes。Agent接收关于局部畴结构与极化翻转的开放问题，构造空间描述并选择后续测量；确定性算法负责图像数值处理、坐标定位、波形/动作验证和仪器执行。新测量结果返回Agent更新判断，若新增测量不再提供新证据则终止。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。
  - 原文位置：正文；TXT第26行；核验TXT行号 26；引文：We implement this architecture in piezoresponse force microscopy. Starting from a broad scientific question concerning the relation between local domain structure and polarization switching, the system constructs spatial descriptors from multichannel imaging, selects and analyzes local hysteresis measurements, adapts the spectroscopy waveform, and terminates the experiment when additional measurements cease to provide new evidence.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：04
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：04（仅归档，不覆盖其他模块）
- 模块内分类路径：04.03 软物质与功能材料
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

对象是铁电材料局域畴结构和显微实验设计，属04.03实验过程控制/优化。Agent做高层“要什么证据”的决定，确定性算法负责可验证执行。

### 2.3 容易混淆的边界

对象是铁电材料局域畴结构和显微实验设计，属04.03实验过程控制/优化。Agent做高层“要什么证据”的决定，确定性算法负责可验证执行。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM科研Agent

### 3.2 科研流程角色

计算/数据分析

Hierarchical automation of scanning probe microscopy through agentic orchestration and algorithmic control。系统角色与能力：Agent接收关于局部畴结构与极化翻转的开放问题，构造空间描述并选择后续测量；确定性算法负责图像数值处理、坐标定位、波形/动作验证和仪器执行。新测量结果返回Agent更新判断，若新增测量不再提供新证据则终止。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 3.3 自主能力

Hierarchical automation of scanning probe microscopy through agentic orchestration and algorithmic control。系统角色与能力：Agent接收关于局部畴结构与极化翻转的开放问题，构造空间描述并选择后续测量；确定性算法负责图像数值处理、坐标定位、波形/动作验证和仪器执行。新测量结果返回Agent更新判断，若新增测量不再提供新证据则终止。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

支持综述讨论Agent与算法分工、科学实验中的物理约束及何时应停止采集。 科学贡献与系统贡献按上述证据分别表述。

### 4.2 系统流程与组件

Agent接收关于局部畴结构与极化翻转的开放问题，构造空间描述并选择后续测量；确定性算法负责图像数值处理、坐标定位、波形/动作验证和仪器执行。新测量结果返回Agent更新判断，若新增测量不再提供新证据则终止。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

案例为压电响应力显微镜中的局部滞回测量与适应性实验路径。作者报告发现极化状态与畴壁距离的混杂关系，并识别所需对比在当前视野中无法独立表示；重点验证安全、可复现的层级控制。

### 5.2 基线、指标与结果

案例为压电响应力显微镜中的局部滞回测量与适应性实验路径。作者报告发现极化状态与畴壁距离的混杂关系，并识别所需对比在当前视野中无法独立表示；重点验证安全、可复现的层级控制。

### 5.3 科学贡献与证据强度

支持综述讨论Agent与算法分工、科学实验中的物理约束及何时应停止采集。 科学贡献与系统贡献按上述证据分别表述。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

作者将Agent推理与扫描探针显微镜的确定性算法控制相结合，回应完全脚本自动化难理解开放问题、完全Agent控制难保证数值和物理可靠性的两端局限。

## 7. 局限性与风险

作者及读者可确认的适用边界：实证集中在PFM畴结构与极化切换这一实验问题；分层架构的有效性仍需在不同仪器、样品与科学目标中检验。

## 8. 对综述写作的价值

支持综述讨论Agent与算法分工、科学实验中的物理约束及何时应停止采集。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

论文提出扫描探针显微镜分层自动化架构，把意图解释、实验表征构建、证据评估和高层决策交给Agent，把数值分析、坐标选取、验证及仪器执行交给确定性算法。

### 9.2 速记版 pipeline

Agent接收关于局部畴结构与极化翻转的开放问题，构造空间描述并选择后续测量；确定性算法负责图像数值处理、坐标定位、波形/动作验证和仪器执行。新测量结果返回Agent更新判断，若新增测量不再提供新证据则终止。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 9.3 标注字段汇总

```text
paper_id=ASD-0986
inclusion_status=to_read
scientific_object_modules=04
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=04
module_taxonomy_codes=04.03
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`04.03.04` 智能材料；二级：`04.03`。
- 原文位置：PDF pp.11。
- 判定：Concrete experiment/task evidence supports 04.03.04 (智能材料). in the end-to-end autonomous experiment The complete workflow was evaluated on a PLZT relaxor ferroelectric with a single instruction – determine how local domain structure affects polarization switching dynamics. The context stated that this was a DART-PFM measurement on PLZT with complex domain structure. No spatial criteria, measurement locations, spectroscopy waveform, experimental trajectory, or stopping rule we
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
