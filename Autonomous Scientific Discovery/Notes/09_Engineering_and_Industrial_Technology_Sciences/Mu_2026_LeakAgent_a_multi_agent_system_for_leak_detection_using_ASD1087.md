# LeakAgent: a multi-agent system for leak detection using multi-modal large language model coordination in water distribution network

**论文信息**

- ID：ASD-1087
- 标题：LeakAgent: a multi-agent system for leak detection using multi-modal large language model coordination in water distribution network
- 作者：Tianwei Mu; Feiyu Duan; Dan Xue; Mingzhe Yuan; Wenhong Wang; Manhong Huang; Hui Yang; Jun Li; Mashallah Rezakazemi
- 年份：2026
- 来源 / venue：Communications AI &amp; Computing
- DOI / arXiv / URL：https://www.nature.com/articles/s44488-026-00024-w
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1087.txt
- PDF / 本地文件路径：Reference_PDF/09_Engineering_and_Industrial_Technology_Sciences/Mu_2026_LeakAgent_a_multi_agent_system_for_leak_detection_using_ASD1087.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 科研目标 | 目标问题是城市供水管网漏水检测与定位。 | Abstract opening；核验TXT行号 1 | Water distribution networks (WDNs) suffer from severe leakage, yet pinpointing the leaks remains difficult. | 高（一手正文；非独立复现） |
| 多步Agent方法 | HydroSim先生成压力敏感场，为后续网络分区等步骤提供输入。 | Results, Overview of the LeakAgent framework；核验TXT行号 1 | LeakAgent automates this workflow with four specialized agents coordinated by an MLLM (Fig. 1 ). HydroSim computes, by hydraulic simulation, how strongly network pressures respond to a leak at each candidate location; this pressure-sensitivity field underpins every downstream stage. | 高（一手正文；非独立复现） |
| 09水利工程对象 | 用四个基准供水网络和一个真实网络做实验。 | Methods, Benchmark networks and datasets；核验TXT行号 1 | These include four synthetic networks (EXA5, EXA7, KY3, KY5) and a real-world network, City H 44 , 45 . The networks range from 191 to 920 junctions | 高（一手正文；非独立复现） |
| 验证设计 | 不同漏水规模、样本量及平衡漏水/正常情景均被系统比较。 | Methods, experimental design following Benchmark networks and datasets；核验TXT行号 1 | The experimental design spanned eight leak magnitudes (0.5%, 1%, 2%, 3%, 5%, 10%, 15% and 20% of average total demand) | 高（一手正文；非独立复现） |
| 作者报告的结果 | 在五个网络上比较全局及分区检测，并量化准确率。 | Discussion, first paragraph；核验TXT行号 1 | Across five benchmark networks (191 to 920 nodes), the framework achieved 96.0% mean global and regional detection accuracy | 高（一手正文；非独立复现） |

## 0. 摘要翻译

论文提出LeakAgent，将供水管网漏水处理中的水力模拟、管网分区、压力传感器布设和漏水检测整合为由多模态大模型协调的多Agent流程。HydroSim计算漏点引起的压力敏感度，PartitionSim划分水力分区，传感器选址与图模型共同支持漏水存在性及受影响分区判断，协调器可发现并修复运行错误。作者在四个合成网络和City H真实网络上报告约96%的检测准确率，并评估噪声、跨网络迁移及运行效率。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。研究城市供水网络漏水存在性及受影响分区定位。
  - 原文位置：Abstract, opening sentence；核验TXT行号 1；引文：Water distribution networks (WDNs) suffer from severe leakage, yet pinpointing the leaks remains difficult.
- 多步行动过程：yes。执行水力仿真、网络分区、传感器选址、联合检测和故障修复等阶段。
  - 原文位置：Results, Overview of the LeakAgent framework；核验TXT行号 1；引文：LeakAgent automates this workflow with four specialized agents coordinated by an MLLM (Fig. 1 ). HydroSim computes, by hydraulic simulation, how strongly network pressures respond to a leak at each candidate location; this pressure-sensitivity field underpins every downstream stage.
- 至少一种Agent能力：yes。多个专门Agent协作，协调器还可检测并修复执行故障。
  - 原文位置：Abstract, agent workflow description；核验TXT行号 1；引文：the coordinator autonomously detects and repairs its own execution faults.
- 明确科研流程角色：yes。承担供水基础设施水力建模、传感器布设与漏水诊断。
  - 原文位置：Abstract, method/result sentence；核验TXT行号 1；引文：A single hydraulic pressure-sensitivity field, computed once, informs network zoning, sensor placement and detection; a dual-branch graph model then determines leak presence and the affected partition jointly

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：09
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：09（仅归档，不覆盖其他模块）
- 模块内分类路径：09.05.07 水利工程
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

对象是供水网络这一工程基础设施，归09.05.07水利工程。漏水诊断涉及传感器和机器学习，但它们是方法组件，不构成01或医疗/环境对象。

### 2.3 容易混淆的边界

对象是供水网络这一工程基础设施，归09.05.07水利工程。漏水诊断涉及传感器和机器学习，但它们是方法组件，不构成01或医疗/环境对象。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM Agent；Multi-Agent System；Tool-using Agent

### 3.2 科研流程角色

simulation_modeling；experimental_design；data_analysis；tool_use_and_code_execution

四个专门Agent分别负责水力仿真、管网分区、传感器布设和漏水检测，由多模态LLM协调；图模型联合输出漏水存在性与影响分区。

### 3.3 自主能力

多个专门Agent协作，协调器还可检测并修复执行故障。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

科学/工程结果是水力敏感性可作为分区、选址及检测的共享基础；系统贡献是把传统分离的供水管网运维分析阶段组成协作Agent工作流。

### 4.2 系统流程与组件

输入为供水网络拓扑、需求状态和传感器数据；HydroSim对候选漏点运行水力模拟并产生压力敏感场。该场与网络拓扑供PartitionSim形成DMA，再由SensorPlacement优化监测点，LeakDetection用双分支图模型联合分类和定位。协调器检查各步运行状态，发生故障时生成修复并重跑，最终输出检测与分区结果。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

五个网络（EXA5、EXA7、KY3、KY5、City H），覆盖191–920节点；以多漏水幅度、多个训练样本量、需求/传感器噪声和跨网测试评估；包含组件消融和协调策略比较。

### 5.2 基线、指标与结果

作者报告：在4000训练情景、漏水幅度为平均总需求20%时，五网平均全局和区域检测准确率96.0%；自动错误恢复率98.18%，总处理时间减少16.38%。

### 5.3 科学贡献与证据强度

科学/工程结果是水力敏感性可作为分区、选址及检测的共享基础；系统贡献是把传统分离的供水管网运维分析阶段组成协作Agent工作流。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

相较先前将漏水存在性与区域定位分开处理的管网检测方法，本文尝试联合建模，并以LLM协调仿真与数据驱动模块。

## 7. 局限性与风险

主要证据来自合成漏水情景与一个真实网络，尚不能证明不同城市实际部署中的长期可靠性；高检测分数受训练情景和漏水幅度设定影响。

## 8. 对综述写作的价值

可支撑综述中工程Agent把物理仿真、感知布点和诊断模型串成多阶段工作流的案例。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

多Agent协作完成供水管网漏水模拟、布点与定位。

### 9.2 速记版 pipeline

输入为供水网络拓扑、需求状态和传感器数据；HydroSim对候选漏点运行水力模拟并产生压力敏感场。该场与网络拓扑供PartitionSim形成DMA，再由SensorPlacement优化监测点，LeakDetection用双分支图模型联合分类和定位。协调器检查各步运行状态，发生故障时生成修复并重跑，最终输出检测与分区结果。

### 9.3 标注字段汇总

```text
paper_id=ASD-1087
inclusion_status=to_read
scientific_object_modules=09
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=09
module_taxonomy_codes=09.05.07
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O3 新实例 | 供水管网漏水检测答案可由模拟验证 | “Water distribution networks (WDNs) suffer from severe leakage” · L21 |
| 验证强度 | V2 计算/仿真/回顾性 | 合成及真实网络水力仿真评估 | “four synthetic networks (EXA5, EXA7, KY3, KY5) and a real-world network” · L23 |
| 系统自主性 | L2 闭环执行者 | 从水力仿真到分区检测的自主闭环 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
