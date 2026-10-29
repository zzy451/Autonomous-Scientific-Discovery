# AEcroscopyWave: Towards Self-Driving Characterization Platforms for Agentic AI

**论文信息**

- ID：ASD-0994
- 标题：AEcroscopyWave: Towards Self-Driving Characterization Platforms for Agentic AI
- 作者：Yongtao Liu; Jawad Chowdhury; Ganesh Narasimha; Ralph Bulanadi; Liam Collins; Ruben Millan Solsona; Marti Checa; Asraful Haque; Sumner B. Harris; Stephen Jesse; Rama Vasudevan
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2607.22975
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0994.txt
- PDF / 本地文件路径：Reference_PDF/04_Materials_Science/Liu_2026_AEcroscopyWave_Towards_Self_Driving_Characterization_Platforms_for_Agentic_AI_ASD0994.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 纳入与科学目标 | AEcroscopyWave是面向Agent的自驱动电子材料表征平台，提供扫描探针显微镜及外围设备统一控制接口。论文讨论如何将异构仪器能力组织成可发现、可组合工具，并用MCP使支持该协议的LLM调用平台函数；预验证工作流可注册后由Agent按名称执行。数字孪生和审批队列用于降低直接控制物理仪器的风险。 | 摘要；TXT第16行；核验TXT行号 16 | The characterization of electronic materials has traditionally been stratified into two distinct regimens: industry-scale automated systems to inspect materials for defects and ensure quality (such as in the semiconductor industry), and highly customized, operator-driven systems requiring human experts. | 高（一手正文；非独立复现） |
| 方法与多步工作流 | 自然语言请求经规划端转成工作流或脚本，先在数字孪生中运行验证，再进入人工审批队列；获批后通过云端服务、作业队列和MCP工具调用显微仪器。平台返回图像、光谱和元数据供Agent及用户查看。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。 | 摘要；TXT第20行；核验TXT行号 20 | Recent advances in “self-driving” characterization tools offer the potential to bridge the two stratified regimes, by the creation of application program interfaces (APIs) that can control hardware, and the integration of AI methods to incorporate autonomy into the process. | 高（一手正文；非独立复现） |
| Agent能力与行动 | AEcroscopyWave: Towards Self-Driving Characterization Platforms for Agentic AI。系统角色与能力：自然语言请求经规划端转成工作流或脚本，先在数字孪生中运行验证，再进入人工审批队列；获批后通过云端服务、作业队列和MCP工具调用显微仪器。平台返回图像、光谱和元数据供Agent及用户查看。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。 | 摘要；TXT第27行；核验TXT行号 27 | The benefits of making heterogeneous scientific instruments accessible, composable and usable by agents is demonstrated by test cases. | 高（一手正文；非独立复现） |
| 验证与结果 | 以平台构建及测试案例展示工具调用、预定义工作流、数字孪生预检和人工审批机制。该文主要验证平台可组合性与控制架构，具体材料发现能力有限，需与实验结果区分。 | 摘要；TXT第19行；核验TXT行号 19 | The former offers high throughput but limited flexibility, whereas the latter is heavily bandwidth-limited but provides research-grade discovery capabilities. | 高（一手正文；非独立复现） |
| 贡献及适用对象 | 可支持综述讨论物理仪器暴露给Agent时的接口、数字孪生验证和人工审批设计。 科学贡献与系统贡献按上述证据分别表述。 | 摘要；TXT第23行；核验TXT行号 23 | Here, we discuss our latest developments in AEcroscopyWave, a custom-built characterization platform for the agentic-AI era, that provides unified control of scanning probe microscopes with programmable peripheral instrumentation, highlighting the design choices that are necessary for maximizing the capability of the system and the ease of use for both human and AI agents. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

AEcroscopyWave是面向Agent的自驱动电子材料表征平台，提供扫描探针显微镜及外围设备统一控制接口。论文讨论如何将异构仪器能力组织成可发现、可组合工具，并用MCP使支持该协议的LLM调用平台函数；预验证工作流可注册后由Agent按名称执行。数字孪生和审批队列用于降低直接控制物理仪器的风险。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。AEcroscopyWave是面向Agent的自驱动电子材料表征平台，提供扫描探针显微镜及外围设备统一控制接口。论文讨论如何将异构仪器能力组织成可发现、可组合工具，并用MCP使支持该协议的LLM调用平台函数；预验证工作流可注册后由Agent按名称执行。数字孪生和审批队列用于降低直接控制物理仪器的风险。
  - 原文位置：摘要；TXT第16行；核验TXT行号 16；引文：The characterization of electronic materials has traditionally been stratified into two distinct regimens: industry-scale automated systems to inspect materials for defects and ensure quality (such as in the semiconductor industry), and highly customized, operator-driven systems requiring human experts.
- 多步行动过程：yes。自然语言请求经规划端转成工作流或脚本，先在数字孪生中运行验证，再进入人工审批队列；获批后通过云端服务、作业队列和MCP工具调用显微仪器。平台返回图像、光谱和元数据供Agent及用户查看。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。
  - 原文位置：正文；TXT第23行；核验TXT行号 23；引文：Here, we discuss our latest developments in AEcroscopyWave, a custom-built characterization platform for the agentic-AI era, that provides unified control of scanning probe microscopes with programmable peripheral instrumentation, highlighting the design choices that are necessary for maximizing the capability of the system and the ease of use for both human and AI agents.
- 至少一种Agent能力：yes。AEcroscopyWave: Towards Self-Driving Characterization Platforms for Agentic AI。系统角色与能力：自然语言请求经规划端转成工作流或脚本，先在数字孪生中运行验证，再进入人工审批队列；获批后通过云端服务、作业队列和MCP工具调用显微仪器。平台返回图像、光谱和元数据供Agent及用户查看。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。
  - 原文位置：摘要；TXT第27行；核验TXT行号 27；引文：The benefits of making heterogeneous scientific instruments accessible, composable and usable by agents is demonstrated by test cases.
- 明确科研流程角色：yes。AEcroscopyWave: Towards Self-Driving Characterization Platforms for Agentic AI。系统角色与能力：自然语言请求经规划端转成工作流或脚本，先在数字孪生中运行验证，再进入人工审批队列；获批后通过云端服务、作业队列和MCP工具调用显微仪器。平台返回图像、光谱和元数据供Agent及用户查看。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。
  - 原文位置：正文；TXT第254行；核验TXT行号 254；引文：Furthermore, we provide a ‘digital twin’ interface for some available backends (such as the DriveAFM and Cypher tools), to validate custom scripts before running on the instrument.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：04
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：04（仅归档，不覆盖其他模块）
- 模块内分类路径：04.01 材料基础；04.04 能源、电子与器件材料
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

对象为电子材料表征仪器平台和扫描探针显微镜工作流，归04.01/04.04。重点在仪器基础设施和Agent可访问性，不是材料性质发现算法。

### 2.3 容易混淆的边界

对象为电子材料表征仪器平台和扫描探针显微镜工作流，归04.01/04.04。重点在仪器基础设施和Agent可访问性，不是材料性质发现算法。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM科研Agent

### 3.2 科研流程角色

计算/数据分析

AEcroscopyWave: Towards Self-Driving Characterization Platforms for Agentic AI。系统角色与能力：自然语言请求经规划端转成工作流或脚本，先在数字孪生中运行验证，再进入人工审批队列；获批后通过云端服务、作业队列和MCP工具调用显微仪器。平台返回图像、光谱和元数据供Agent及用户查看。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 3.3 自主能力

AEcroscopyWave: Towards Self-Driving Characterization Platforms for Agentic AI。系统角色与能力：自然语言请求经规划端转成工作流或脚本，先在数字孪生中运行验证，再进入人工审批队列；获批后通过云端服务、作业队列和MCP工具调用显微仪器。平台返回图像、光谱和元数据供Agent及用户查看。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

可支持综述讨论物理仪器暴露给Agent时的接口、数字孪生验证和人工审批设计。 科学贡献与系统贡献按上述证据分别表述。

### 4.2 系统流程与组件

自然语言请求经规划端转成工作流或脚本，先在数字孪生中运行验证，再进入人工审批队列；获批后通过云端服务、作业队列和MCP工具调用显微仪器。平台返回图像、光谱和元数据供Agent及用户查看。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

以平台构建及测试案例展示工具调用、预定义工作流、数字孪生预检和人工审批机制。该文主要验证平台可组合性与控制架构，具体材料发现能力有限，需与实验结果区分。

### 5.2 基线、指标与结果

以平台构建及测试案例展示工具调用、预定义工作流、数字孪生预检和人工审批机制。该文主要验证平台可组合性与控制架构，具体材料发现能力有限，需与实验结果区分。

### 5.3 科学贡献与证据强度

可支持综述讨论物理仪器暴露给Agent时的接口、数字孪生验证和人工审批设计。 科学贡献与系统贡献按上述证据分别表述。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

本文关联自驱显微镜和MCP工具生态，重点讨论如何将异构仪器能力变成Agent可发现、预检并复用的工作流。

## 7. 局限性与风险

作者及读者可确认的适用边界：论文主要以平台设计及测试案例展示仪器可组合性；预批准工作流和数字孪生并不能自动验证所有自定义脚本在真实仪器上的科学有效性。

## 8. 对综述写作的价值

可支持综述讨论物理仪器暴露给Agent时的接口、数字孪生验证和人工审批设计。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

AEcroscopyWave是面向Agent的自驱动电子材料表征平台，提供扫描探针显微镜及外围设备统一控制接口。

### 9.2 速记版 pipeline

自然语言请求经规划端转成工作流或脚本，先在数字孪生中运行验证，再进入人工审批队列；获批后通过云端服务、作业队列和MCP工具调用显微仪器。平台返回图像、光谱和元数据供Agent及用户查看。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 9.3 标注字段汇总

```text
paper_id=ASD-0994
inclusion_status=to_read
scientific_object_modules=04
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=04
module_taxonomy_codes=04.01;04.04
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`04.01.03` 材料表征；二级：`04.01`。
- 原文位置：PDF p.3。
- 判定：扫描探针显微镜的实际仪器闭环，归材料表征。
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
