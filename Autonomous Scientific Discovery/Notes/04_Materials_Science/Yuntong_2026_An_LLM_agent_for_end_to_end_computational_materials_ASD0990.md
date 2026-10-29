# An LLM agent for end-to-end computational materials discovery

**论文信息**

- ID：ASD-0990
- 标题：An LLM agent for end-to-end computational materials discovery
- 作者：Chen Yuntong; Huang Ju; Liu Yu; Zhao Dan; Sun Mingqi; Ju Chentian; Liu Yanbing; Huang Lijiang; Zhao Guobin
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2608.20434
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0990.txt
- PDF / 本地文件路径：Reference_PDF/04_Materials_Science/Yuntong_2026_An_LLM_agent_for_end_to_end_computational_materials_ASD0990.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 纳入与科学目标 | MAESTRO将LLM Agent用于金属有机框架（MOF）端到端计算材料发现。系统从文献提取材料信息并关联晶体结构，整理成可计算数据库，再用逐渐增加计算成本的筛选策略分析材料，寻找湿烟道气条件下的分离候选。作者强调跨越文献整理、结构关联、模拟和筛选的多阶段协调。 | 摘要；TXT第23行；核验TXT行号 23 | The coordination of multi-scale tasks is an effective strategy for computational materials discovery, yet the repeated application of diverse algorithms and tools renders it challenging. | 高（一手正文；非独立复现） |
| 方法与多步工作流 | 输入为MOF研究目标及文献/结构数据；Agent检索和解析论文，将材料记录与晶体结构关联并整理为计算数据库。筛选管线逐级调用成本上升的计算工具，比较候选分离性能并更新候选集合，最终输出湿烟道气分离的高性能MOF候选及出处。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。 | 摘要；TXT第24行；核验TXT行号 24 | We report MAESTRO, a large language model (LLM) agent system capable of executing the entire screening pipeline for metal-organic frameworks (MOFs). | 高（一手正文；非独立复现） |
| Agent能力与行动 | An LLM agent for end-to-end computational materials discovery。系统角色与能力：输入为MOF研究目标及文献/结构数据；Agent检索和解析论文，将材料记录与晶体结构关联并整理为计算数据库。筛选管线逐级调用成本上升的计算工具，比较候选分离性能并更新候选集合，最终输出湿烟道气分离的高性能MOF候选及出处。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。 | 摘要；TXT第26行；核验TXT行号 26 | It processes a large body of MOF literature, links relevant publications to their crystal structures, and curates the results into a computation-ready database, which is then screened through a strategy of progressively increasing computational cost. | 高（一手正文；非独立复现） |
| 验证与结果 | 验证包含文献数据与结构链接、逐级计算筛选及湿烟道气分离候选评估。摘要称最终候选来自彼此独立的研究。具体性能指标和基线需从结果表核对。 | 摘要；TXT第28行；核验TXT行号 28 | The promising candidates identified for separation under wet flue-gas conditions all originate from unrelated studies. | 高（一手正文；非独立复现） |
| 贡献及适用对象 | 可支持综述讨论Agent连接文献数据、结构数据库与多尺度计算的端到端研究价值。 科学贡献与系统贡献按上述证据分别表述。 | 摘要；TXT第29行；核验TXT行号 29 | By connecting the heterogeneous stages of computational materials discovery, the LLM-based agents of MAESTRO can operate across application domains and uncover high-performance materials that conventional screening approaches would be unlikely to consider. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

MAESTRO将LLM Agent用于金属有机框架（MOF）端到端计算材料发现。系统从文献提取材料信息并关联晶体结构，整理成可计算数据库，再用逐渐增加计算成本的筛选策略分析材料，寻找湿烟道气条件下的分离候选。作者强调跨越文献整理、结构关联、模拟和筛选的多阶段协调。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。MAESTRO将LLM Agent用于金属有机框架（MOF）端到端计算材料发现。系统从文献提取材料信息并关联晶体结构，整理成可计算数据库，再用逐渐增加计算成本的筛选策略分析材料，寻找湿烟道气条件下的分离候选。作者强调跨越文献整理、结构关联、模拟和筛选的多阶段协调。
  - 原文位置：摘要；TXT第23行；核验TXT行号 23；引文：The coordination of multi-scale tasks is an effective strategy for computational materials discovery, yet the repeated application of diverse algorithms and tools renders it challenging.
- 多步行动过程：yes。输入为MOF研究目标及文献/结构数据；Agent检索和解析论文，将材料记录与晶体结构关联并整理为计算数据库。筛选管线逐级调用成本上升的计算工具，比较候选分离性能并更新候选集合，最终输出湿烟道气分离的高性能MOF候选及出处。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。
  - 原文位置：摘要；TXT第24行；核验TXT行号 24；引文：We report MAESTRO, a large language model (LLM) agent system capable of executing the entire screening pipeline for metal-organic frameworks (MOFs).
- 至少一种Agent能力：yes。An LLM agent for end-to-end computational materials discovery。系统角色与能力：输入为MOF研究目标及文献/结构数据；Agent检索和解析论文，将材料记录与晶体结构关联并整理为计算数据库。筛选管线逐级调用成本上升的计算工具，比较候选分离性能并更新候选集合，最终输出湿烟道气分离的高性能MOF候选及出处。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。
  - 原文位置：摘要；TXT第26行；核验TXT行号 26；引文：It processes a large body of MOF literature, links relevant publications to their crystal structures, and curates the results into a computation-ready database, which is then screened through a strategy of progressively increasing computational cost.
- 明确科研流程角色：yes。验证包含文献数据与结构链接、逐级计算筛选及湿烟道气分离候选评估。摘要称最终候选来自彼此独立的研究。具体性能指标和基线需从结果表核对。
  - 原文位置：摘要；TXT第28行；核验TXT行号 28；引文：The promising candidates identified for separation under wet flue-gas conditions all originate from unrelated studies.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：04
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：04（仅归档，不覆盖其他模块）
- 模块内分类路径：04.02 结构材料与无机材料；04.03 软物质与功能材料；04.04 能源、电子与器件材料
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

对象是MOF晶体材料及气体分离性质，归04.02；文献抽取是材料发现工作流的输入准备环节，分类重心仍是计算材料发现。

### 2.3 容易混淆的边界

对象是MOF晶体材料及气体分离性质，归04.02；文献抽取是材料发现工作流的输入准备环节，分类重心仍是计算材料发现。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM科研Agent

### 3.2 科研流程角色

计算/数据分析

An LLM agent for end-to-end computational materials discovery。系统角色与能力：输入为MOF研究目标及文献/结构数据；Agent检索和解析论文，将材料记录与晶体结构关联并整理为计算数据库。筛选管线逐级调用成本上升的计算工具，比较候选分离性能并更新候选集合，最终输出湿烟道气分离的高性能MOF候选及出处。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 3.3 自主能力

An LLM agent for end-to-end computational materials discovery。系统角色与能力：输入为MOF研究目标及文献/结构数据；Agent检索和解析论文，将材料记录与晶体结构关联并整理为计算数据库。筛选管线逐级调用成本上升的计算工具，比较候选分离性能并更新候选集合，最终输出湿烟道气分离的高性能MOF候选及出处。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

可支持综述讨论Agent连接文献数据、结构数据库与多尺度计算的端到端研究价值。 科学贡献与系统贡献按上述证据分别表述。

### 4.2 系统流程与组件

输入为MOF研究目标及文献/结构数据；Agent检索和解析论文，将材料记录与晶体结构关联并整理为计算数据库。筛选管线逐级调用成本上升的计算工具，比较候选分离性能并更新候选集合，最终输出湿烟道气分离的高性能MOF候选及出处。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

验证包含文献数据与结构链接、逐级计算筛选及湿烟道气分离候选评估。摘要称最终候选来自彼此独立的研究。具体性能指标和基线需从结果表核对。

### 5.2 基线、指标与结果

验证包含文献数据与结构链接、逐级计算筛选及湿烟道气分离候选评估。摘要称最终候选来自彼此独立的研究。具体性能指标和基线需从结果表核对。

### 5.3 科学贡献与证据强度

可支持综述讨论Agent连接文献数据、结构数据库与多尺度计算的端到端研究价值。 科学贡献与系统贡献按上述证据分别表述。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

本文把以往分散的MOF文献提取、晶体结构链接、数据整理和多保真计算筛选连成单一MAESTRO研究活动。

## 7. 局限性与风险

作者及读者可确认的适用边界：候选发现来自MOF湿烟道气分离的计算筛选；计算候选还需实验吸附/分离验证，不能把筛选结果当成已实现的材料性能。

## 8. 对综述写作的价值

可支持综述讨论Agent连接文献数据、结构数据库与多尺度计算的端到端研究价值。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

MAESTRO将LLM Agent用于金属有机框架（MOF）端到端计算材料发现。

### 9.2 速记版 pipeline

输入为MOF研究目标及文献/结构数据；Agent检索和解析论文，将材料记录与晶体结构关联并整理为计算数据库。筛选管线逐级调用成本上升的计算工具，比较候选分离性能并更新候选集合，最终输出湿烟道气分离的高性能MOF候选及出处。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 9.3 标注字段汇总

```text
paper_id=ASD-0990
inclusion_status=to_read
scientific_object_modules=04
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=04
module_taxonomy_codes=04.02;04.03;04.04
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`04.03.05` 多孔材料；二级：`04.03`。
- 原文位置：PDF p.1。
- 判定：MOF材料的湿烟气吸附分离，归多孔材料；须由04.02对齐04.03。
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
