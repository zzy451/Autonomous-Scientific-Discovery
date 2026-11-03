# An Open-Source Hardware and Software Toolkit to Enable Agentic RHEED-Guided Thin-Film Synthesis

**论文信息**

- ID：ASD-0885
- 标题：An Open-Source Hardware and Software Toolkit to Enable Agentic RHEED-Guided Thin-Film Synthesis
- 作者：Haque, Asraful; Rouleau, Christopher M.; Vasudevan, Rama K.; Harris, Sumner B.
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2609.15922
- 一手阅读来源：https://arxiv.org/abs/2609.15922
- 来源层级：全文
- 阅读版本：对应缓存来源版本，参见Evidence Log
- 阅读版本题名：An Open-Source Hardware and Software Toolkit to Enable Agentic RHEED-Guided Thin-Film Synthesis
- 原始全文缓存：C:/Users/20683/Desktop/综述/.tmp_asd_pdfs/2609.15922.pdf
- PDF / 本地文件路径：Reference_PDF/04_Materials_Science/Haque_2026_Agentic_RHEED_Thin_Film_Toolkit.pdf
- 当前状态：included
- 阅读日期：2026-10-22
- 笔记作者：Codex（读者证据包经主控审核整合）

## Evidence Log

| 判断项 | 结论 / 原文概括 | 证据位置 | 可信度 |
|---|---|---|---|
| 实验对象 | RHEED监测薄膜生长中的演化表面。 | PDF p.2 Abstract | high |
| 设备/采集 | 在PLD系统演示程序化电子光学控制、自动束流对准和rocking-curve采集。 | PDF p.2 Abstract | high |
| 工具接口 | 分析核心可由GUI或MCP server驱动。 | PDF p.10 Methods: Auto-RHEED | high |
| Agent演示 | SrTiO3薄膜上，Agent按自然语言请求顺序调用八个工具，定位峰、配置ROI并检查返回图像。 | PDF pp.14–15 Fig.4 | high |
| 边界 | 文章定位为支持未来自主生长控制的工具基础；当前演示为Agent表征分析，未做生长闭环决策。 | PDF p.2 Abstract; pp.14–15 | high |

## 0. 摘要翻译

全文提出开放硬件与软件工具包，使RHEED控制和定量分析可供操作员及AI Agent使用。PLD演示包括电子光学控制、自动束流对准、rocking-curve采集及训练自由的晶体方位对准；Auto-RHEED通过GUI、程序接口和MCP服务器提取结构与生长观测量。另一片SrTiO3薄膜的Agent演示中，自然语言请求触发连续工具调用以自动定位衍射峰、配置ROI、跟踪图像序列并核验峰识别。文章提供的是表征/分析工具基础，不是Agent自主闭环控制生长。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 当前判断：included；读者建议：included。
全文有自然语言驱动的Agent分析演示：多步选择工具、配置和执行RHEED定量分析，承担材料表征/数据分析角色；Agent自主性较弱但满足工具使用标准。

### 1.2 排除风险检查

薄膜材料生长及原位表面/晶相表征归04.02；仪器控制是科研工具角色，不单列09。
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

在PLD薄膜系统演示测量和分析功能；在SrTiO3薄膜RHEED序列中完成agent-driven analysis。没有完整材料发现campaign或Agent性能基准。

### 2.3 容易混淆的边界

薄膜材料生长及原位表面/晶相表征归04.02；仪器控制是科研工具角色，不单列09。

## 3. Agent 系统与科研流程角色

全文有自然语言驱动的Agent分析演示：多步选择工具、配置和执行RHEED定量分析，承担材料表征/数据分析角色；Agent自主性较弱但满足工具使用标准。

科研流程与自主能力以本文实际行动和工具调用为依据：

FPGA/程序化电子光学与PLD接口；自动束斑对准、rocking-curve采集、晶体方位识别；auto-RHEED经GUI、API/MCP开放分析；Agent读取自然语言意图，顺序调用八个工具进行峰定位、ROI选择、图像核验和时间序列跟踪。

## 4. 方法设计

### 4.1 方法动机与设计

把RHEED采集/分析工具化、标准化并开放给Agent，建立未来表面反馈控制基础。

### 4.2 系统流程与组件

FPGA/程序化电子光学与PLD接口；自动束斑对准、rocking-curve采集、晶体方位识别；auto-RHEED经GUI、API/MCP开放分析；Agent读取自然语言意图，顺序调用八个工具进行峰定位、ROI选择、图像核验和时间序列跟踪。

## 5. 实验与验证

### 5.1 验证方式、对象及任务

在PLD薄膜系统演示测量和分析功能；在SrTiO3薄膜RHEED序列中完成agent-driven analysis。没有完整材料发现campaign或Agent性能基准。

### 5.2 基线、指标与结果

在PLD薄膜系统演示测量和分析功能；在SrTiO3薄膜RHEED序列中完成agent-driven analysis。没有完整材料发现campaign或Agent性能基准。

### 5.3 科学贡献与证据强度

把RHEED采集/分析工具化、标准化并开放给Agent，建立未来表面反馈控制基础。

证据层级：原始全文支持；作者报告结果不等于独立复现。

## 6. 与已有工作的关系

与ASD-0806合成Agent不同；与ASD-0630粉末XRD平台邻近，但本文聚焦原位RHEED和薄膜表征。

## 7. 局限性与风险

Agent演示只处理数据分析，没有自主选择生长参数或闭环控制合成；工具包能力强于Agent实验证据。

## 8. 对综述写作的价值

说明Agent可在实验工作流中承担表征分析角色；完整自驱闭环不是纳入门槛。

推荐引用强度：普通引用，可在核对原文后用于相应领域案例。

## 9. 总结

### 9.1 一句话概括

以Agent选择并执行薄膜衍射分析

### 9.2 速记版 pipeline

FPGA/程序化电子光学与PLD接口；自动束斑对准、rocking-curve采集、晶体方位识别；auto-RHEED经GUI、API/MCP开放分析；Agent读取自然语言意图，顺序调用八个工具进行峰定位、ROI选择、图像核验和时间序列跟踪。

### 9.3 标注字段汇总

```text
paper_id=ASD-0885
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

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O3 新实例 | 分析RHEED数据识别衍射峰，答案可由分析核对 | “SrTiO3薄膜RHEED序列中完成agent-driven analysis” · L61 |
| 验证强度 | V1 基准/内部评测 | 工具演示，agent只做数据分析未闭环控制合成 | “Agent演示只处理数据分析” · L107 |
| 系统自主性 | L1 任务助手 | agent按请求调用工具分析数据，未自主控制生长 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
