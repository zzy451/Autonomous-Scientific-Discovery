# ChemGraph-XANES: an agentic framework for XANES simulation and curation

**论文信息**

- ID：ASD-0996
- 标题：ChemGraph-XANES: an agentic framework for XANES simulation and curation
- 作者：Vitor F. Grizzi; Thang Duc Pham; Luke N. Pretzie; Jiayi Xu; Murat Keceli; Cong Liu
- 年份：2026
- 来源 / venue：RSC Advances
- DOI / arXiv / URL：https://pubs.rsc.org/en/content/articlelanding/2026/ra/d6ra06166d
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0996.txt
- PDF / 本地文件路径：Reference_PDF/03_Chemical_Sciences/Grizzi_2026_ChemGraph_XANES_an_agentic_framework_for_XANES_simulation_and_ASD0996.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 纳入与科学目标 | ChemGraph-XANES以LLM Agent编排XANES模拟和数据整理，结合文档检索参数、schema约束工具调用、确定性FDMNES输入生成、Parsl并行执行和带来源的数据整理。系统支持结构文件、组成描述和文档引导三类流程，也能用材料数据库结构并行开展谱计算。 | 摘要；TXT第11行；核验TXT行号 11 | Computational X-ray absorption near-edge structure (XANES) is widely used to interpret local coordination environments, oxidation states, and electronic structure, but large computa- tional campaigns are often limited by workflow complexity. | 高（一手正文；非独立复现） |
| 方法与多步工作流 | 用户提供结构或化学组成，或从材料数据库检索结构；Agent可先从FDMNES文档检索参数，将请求转为受schema约束工具输入，生成FDMNES文件并执行计算，解析卷积谱后与结构和参数出处一起归档。多结构任务由Parsl分发。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。 | 摘要；TXT第13行；核验TXT行号 13 | We present ChemGraph-XANES, a large language model (LLM)-based agentic framework that combines documentation-grounded parameter retrieval via retrieval-augmented generation (RAG), schema-constrained tool execu- tion, deterministic FDMNES input generation, Parsl-backed execution, and provenance-aware data curation. | 高（一手正文；非独立复现） |
| Agent能力与行动 | ChemGraph-XANES: an agentic framework for XANES simulation and curation。系统角色与能力：用户提供结构或化学组成，或从材料数据库检索结构；Agent可先从FDMNES文档检索参数，将请求转为受schema约束工具输入，生成FDMNES文件并执行计算，解析卷积谱后与结构和参数出处一起归档。多结构任务由Parsl分发。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。 | 摘要；TXT第21行；核验TXT行号 21 | We evaluate three workflow modes: documentation-grounded parameter propa- gation, structure-file-based execution, and composition-based execution from a chemistry-level request. | 高（一手正文；非独立复现） |
| 验证与结果 | 重复试验中组成输入流程10/10完成、结构文件流程10/10、文档RAG流程9/10；RAG各次能正确传递能量网格参数，一次失败出现在多结构处理。另从Materials Project取21个TiO2结构并成功完成全部计算。 | 摘要；TXT第26行；核验TXT行号 26 | In a separate task-parallel demonstration, the framework retrieved 21 TiO2 structures from the Materials Project and submitted one FDMNES calculation per structure. | 高（一手正文；非独立复现） |
| 贡献及适用对象 | 支持综述讨论受约束工具调用、文档接地参数和可溯源并行科学计算。 科学贡献与系统贡献按上述证据分别表述。 | 摘要；TXT第30行；核验TXT行号 30 | Together, these results show that ChemGraph-XANES provides a constrained and reproducible orchestration layer for computational spectroscopy, supporting consistent execution of representative tasks, documentation-linked parameter selection, and task-parallel generation of structure-linked XANES collections. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

ChemGraph-XANES以LLM Agent编排XANES模拟和数据整理，结合文档检索参数、schema约束工具调用、确定性FDMNES输入生成、Parsl并行执行和带来源的数据整理。系统支持结构文件、组成描述和文档引导三类流程，也能用材料数据库结构并行开展谱计算。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。ChemGraph-XANES以LLM Agent编排XANES模拟和数据整理，结合文档检索参数、schema约束工具调用、确定性FDMNES输入生成、Parsl并行执行和带来源的数据整理。系统支持结构文件、组成描述和文档引导三类流程，也能用材料数据库结构并行开展谱计算。
  - 原文位置：摘要；TXT第11行；核验TXT行号 11；引文：Computational X-ray absorption near-edge structure (XANES) is widely used to interpret local coordination environments, oxidation states, and electronic structure, but large computa- tional campaigns are often limited by workflow complexity.
- 多步行动过程：yes。用户提供结构或化学组成，或从材料数据库检索结构；Agent可先从FDMNES文档检索参数，将请求转为受schema约束工具输入，生成FDMNES文件并执行计算，解析卷积谱后与结构和参数出处一起归档。多结构任务由Parsl分发。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。
  - 原文位置：摘要；TXT第13行；核验TXT行号 13；引文：We present ChemGraph-XANES, a large language model (LLM)-based agentic framework that combines documentation-grounded parameter retrieval via retrieval-augmented generation (RAG), schema-constrained tool execu- tion, deterministic FDMNES input generation, Parsl-backed execution, and provenance-aware data curation.
- 至少一种Agent能力：yes。用户提供结构或化学组成，或从材料数据库检索结构；Agent可先从FDMNES文档检索参数，将请求转为受schema约束工具输入，生成FDMNES文件并执行计算，解析卷积谱后与结构和参数出处一起归档。多结构任务由Parsl分发。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。
  - 原文位置：正文；TXT第133行；核验TXT行号 133；引文：pipeline begins with either user-provided structures or structures retrieved from a ma- terials database, converts them into a unified atomistic representation, generates FDMNES input files, executes the calculations, parses the resulting convolution spectra, and stores the spectra back alongside the originating structures for downstream analysis.
- 明确科研流程角色：yes。重复试验中组成输入流程10/10完成、结构文件流程10/10、文档RAG流程9/10；RAG各次能正确传递能量网格参数，一次失败出现在多结构处理。另从Materials Project取21个TiO2结构并成功完成全部计算。
  - 原文位置：摘要；TXT第26行；核验TXT行号 26；引文：In a separate task-parallel demonstration, the framework retrieved 21 TiO2 structures from the Materials Project and submitted one FDMNES calculation per structure.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：03;04
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：03（仅归档，不覆盖其他模块）
- 模块内分类路径：03.02 基础化学；04.01 材料基础
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

对象为XANES局部配位/氧化态/电子结构模拟，兼具03.02材料电子结构任务及04.01科学计算工作流。确定性光谱引擎承担计算，Agent负责编排和文档接地参数选择。

### 2.3 容易混淆的边界

对象为XANES局部配位/氧化态/电子结构模拟，兼具03.02材料电子结构任务及04.01科学计算工作流。确定性光谱引擎承担计算，Agent负责编排和文档接地参数选择。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM科研Agent

### 3.2 科研流程角色

计算/数据分析

ChemGraph-XANES: an agentic framework for XANES simulation and curation。系统角色与能力：用户提供结构或化学组成，或从材料数据库检索结构；Agent可先从FDMNES文档检索参数，将请求转为受schema约束工具输入，生成FDMNES文件并执行计算，解析卷积谱后与结构和参数出处一起归档。多结构任务由Parsl分发。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 3.3 自主能力

用户提供结构或化学组成，或从材料数据库检索结构；Agent可先从FDMNES文档检索参数，将请求转为受schema约束工具输入，生成FDMNES文件并执行计算，解析卷积谱后与结构和参数出处一起归档。多结构任务由Parsl分发。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

支持综述讨论受约束工具调用、文档接地参数和可溯源并行科学计算。 科学贡献与系统贡献按上述证据分别表述。

### 4.2 系统流程与组件

用户提供结构或化学组成，或从材料数据库检索结构；Agent可先从FDMNES文档检索参数，将请求转为受schema约束工具输入，生成FDMNES文件并执行计算，解析卷积谱后与结构和参数出处一起归档。多结构任务由Parsl分发。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

重复试验中组成输入流程10/10完成、结构文件流程10/10、文档RAG流程9/10；RAG各次能正确传递能量网格参数，一次失败出现在多结构处理。另从Materials Project取21个TiO2结构并成功完成全部计算。

### 5.2 基线、指标与结果

重复试验中组成输入流程10/10完成、结构文件流程10/10、文档RAG流程9/10；RAG各次能正确传递能量网格参数，一次失败出现在多结构处理。另从Materials Project取21个TiO2结构并成功完成全部计算。

### 5.3 科学贡献与证据强度

支持综述讨论受约束工具调用、文档接地参数和可溯源并行科学计算。 科学贡献与系统贡献按上述证据分别表述。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

本文沿用FDMNES XANES模拟和材料数据库流程，新增文档接地参数检索、schema约束Agent调用及可溯源并行执行。

## 7. 局限性与风险

作者及读者可确认的适用边界：工作流依赖FDMNES与当前schema/参数文档；重复任务中仍出现一次多结构处理失败，广泛规模化表现尚未评估。

## 8. 对综述写作的价值

支持综述讨论受约束工具调用、文档接地参数和可溯源并行科学计算。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

ChemGraph-XANES以LLM Agent编排XANES模拟和数据整理，结合文档检索参数、schema约束工具调用、确定性FDMNES输入生成、Parsl并行执行和带来源的数据整理。

### 9.2 速记版 pipeline

用户提供结构或化学组成，或从材料数据库检索结构；Agent可先从FDMNES文档检索参数，将请求转为受schema约束工具输入，生成FDMNES文件并执行计算，解析卷积谱后与结构和参数出处一起归档。多结构任务由Parsl分发。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 9.3 标注字段汇总

```text
paper_id=ASD-0996
inclusion_status=to_read
scientific_object_modules=03;04
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=03
module_taxonomy_codes=03.02;04.01
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`03.02.03` 分析化学；二级：`03.02`。
- 原文位置：PDF p.1。
- 判定：TiO2局域配位与氧化态的XANES谱分析，归分析化学。
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
