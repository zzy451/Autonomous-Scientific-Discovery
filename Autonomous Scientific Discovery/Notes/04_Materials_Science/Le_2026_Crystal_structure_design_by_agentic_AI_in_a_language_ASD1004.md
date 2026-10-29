# Crystal-structure design by agentic AI in a language of motifs

**论文信息**

- ID：ASD-1004
- 标题：Crystal-structure design by agentic AI in a language of motifs
- 作者：Dinh-Khiet Le; Minh-Quyet Ha; Hong-Phuc Vu-Dinh; Viet-Cuong Nguyen; Huan Tran; Truyen Tran; Takashi Miyake; Hiori Kino; Hieu-Chi Dam
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2608.15900
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1004.txt
- PDF / 本地文件路径：Reference_PDF/04_Materials_Science/Le_2026_Crystal_structure_design_by_agentic_AI_in_a_language_ASD1004.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 纳入与科学目标 | 论文研究Agentic AI以motif语言设计晶体结构，关注如何把结构设计任务表示为可组合的结构单元并由Agent迭代探索。现有来源摘要未在抽取文本中可靠定位，故本稿仅依题名及正文中的结构设计流程线索作初步归纳；性能、稳定性筛选、实验合成验证和具体案例必须由主控复核后再定稿。 | 摘要；TXT第19行；核验TXT行号 19 | Data-driven materials discovery interpolates more reliably than it extrapolates and seldom reveals new structure types. | 高（一手正文；非独立复现） |
| 方法与多步工作流 | 初步按正文工作流理解为：用户给出目标材料/性质，Agent在motif表示空间提出结构方案，调用结构构建和计算工具检查候选，再根据结果修正结构并输出候选。由于当前抽取摘要缺失，关于规划策略、反馈信号、验证计算与合成环节仍属待核信息，不应视为已证实的闭环。 | 摘要；TXT第20行；核验TXT行号 20 | We present MatEvolve, an agentic-AI framework that designs crystals in an interpretable language of motifs, in which each crystal is written as a motif profile that describes the recurring geometric patterns—the motifs—composing the crystal. | 高（一手正文；非独立复现） |
| Agent能力与行动 | Crystal-structure design by agentic AI in a language of motifs。系统角色与能力：初步按正文工作流理解为：用户给出目标材料/性质，Agent在motif表示空间提出结构方案，调用结构构建和计算工具检查候选，再根据结果修正结构并输出候选。由于当前抽取摘要缺失，关于规划策略、反馈信号、验证计算与合成环节仍属待核信息，不应视为已证实的闭环。 | 摘要；TXT第26行；核验TXT行号 26 | It is applied to the design of rare-earth-lean permanent- magnet compounds and finds novel (meta)stable crystals that are both new structural prototypes and magnet compounds; under an equal validation budget, it does so an order of magnitude more often than generative models. | 高（一手正文；非独立复现） |
| 验证与结果 | 需要从正文结果段确认motif设计覆盖的体系、结构弛豫/能量或稳定性判据、比较基线及是否有实验验证。现阶段不录入未经核验的数值，建议保持needs_review。 | 摘要；TXT第29行；核验TXT行号 29 | Beyond design, analyzing the human-readable profiles of the discovered crystals reveals their structure–property relationships. | 高（一手正文；非独立复现） |
| 贡献及适用对象 | 可能支持综述讨论以结构motif作为Agent生成语言的材料设计路线；需补读全文验证具体科学贡献。 科学贡献与系统贡献按上述证据分别表述。 | 摘要；TXT第22行；核验TXT行号 22 | The motif profile serves not merely as a description of a material but as the medium for material design: the agent edits the profile with a stated rationale and constructs a crystal from the modified one; the most promising candidates are then validated by first-principles calculations. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

论文研究Agentic AI以motif语言设计晶体结构，关注如何把结构设计任务表示为可组合的结构单元并由Agent迭代探索。现有来源摘要未在抽取文本中可靠定位，故本稿仅依题名及正文中的结构设计流程线索作初步归纳；性能、稳定性筛选、实验合成验证和具体案例必须由主控复核后再定稿。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。论文研究Agentic AI以motif语言设计晶体结构，关注如何把结构设计任务表示为可组合的结构单元并由Agent迭代探索。现有来源摘要未在抽取文本中可靠定位，故本稿仅依题名及正文中的结构设计流程线索作初步归纳；性能、稳定性筛选、实验合成验证和具体案例必须由主控复核后再定稿。
  - 原文位置：摘要；TXT第19行；核验TXT行号 19；引文：Data-driven materials discovery interpolates more reliably than it extrapolates and seldom reveals new structure types.
- 多步行动过程：yes。初步按正文工作流理解为：用户给出目标材料/性质，Agent在motif表示空间提出结构方案，调用结构构建和计算工具检查候选，再根据结果修正结构并输出候选。由于当前抽取摘要缺失，关于规划策略、反馈信号、验证计算与合成环节仍属待核信息，不应视为已证实的闭环。
  - 原文位置：摘要；TXT第20行；核验TXT行号 20；引文：We present MatEvolve, an agentic-AI framework that designs crystals in an interpretable language of motifs, in which each crystal is written as a motif profile that describes the recurring geometric patterns—the motifs—composing the crystal.
- 至少一种Agent能力：yes。Crystal-structure design by agentic AI in a language of motifs。系统角色与能力：初步按正文工作流理解为：用户给出目标材料/性质，Agent在motif表示空间提出结构方案，调用结构构建和计算工具检查候选，再根据结果修正结构并输出候选。由于当前抽取摘要缺失，关于规划策略、反馈信号、验证计算与合成环节仍属待核信息，不应视为已证实的闭环。
  - 原文位置：摘要；TXT第26行；核验TXT行号 26；引文：It is applied to the design of rare-earth-lean permanent- magnet compounds and finds novel (meta)stable crystals that are both new structural prototypes and magnet compounds; under an equal validation budget, it does so an order of magnitude more often than generative models.
- 明确科研流程角色：yes。需要从正文结果段确认motif设计覆盖的体系、结构弛豫/能量或稳定性判据、比较基线及是否有实验验证。现阶段不录入未经核验的数值，建议保持needs_review。
  - 原文位置：摘要；TXT第29行；核验TXT行号 29；引文：Beyond design, analyzing the human-readable profiles of the discovered crystals reveals their structure–property relationships.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：04
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：04（仅归档，不覆盖其他模块）
- 模块内分类路径：04.02 结构材料与无机材料；04.04 能源、电子与器件材料
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

纳入Agent研究。科学对象是晶体结构及稀土贫化永磁材料，准确分类为04.02.05晶体材料和04.04.06磁性材料；两者均有对象级候选生成/计算验证证据。主模块04。新候选由第一性原理筛选，不能表述为已合成或实验测得磁性能。

### 2.3 容易混淆的边界

纳入Agent研究。科学对象是晶体结构及稀土贫化永磁材料，准确分类为04.02.05晶体材料和04.04.06磁性材料；两者均有对象级候选生成/计算验证证据。主模块04。新候选由第一性原理筛选，不能表述为已合成或实验测得磁性能。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM科研Agent

### 3.2 科研流程角色

计算/数据分析

Crystal-structure design by agentic AI in a language of motifs。系统角色与能力：初步按正文工作流理解为：用户给出目标材料/性质，Agent在motif表示空间提出结构方案，调用结构构建和计算工具检查候选，再根据结果修正结构并输出候选。由于当前抽取摘要缺失，关于规划策略、反馈信号、验证计算与合成环节仍属待核信息，不应视为已证实的闭环。

### 3.3 自主能力

Crystal-structure design by agentic AI in a language of motifs。系统角色与能力：初步按正文工作流理解为：用户给出目标材料/性质，Agent在motif表示空间提出结构方案，调用结构构建和计算工具检查候选，再根据结果修正结构并输出候选。由于当前抽取摘要缺失，关于规划策略、反馈信号、验证计算与合成环节仍属待核信息，不应视为已证实的闭环。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

可能支持综述讨论以结构motif作为Agent生成语言的材料设计路线；需补读全文验证具体科学贡献。 科学贡献与系统贡献按上述证据分别表述。

### 4.2 系统流程与组件

初步按正文工作流理解为：用户给出目标材料/性质，Agent在motif表示空间提出结构方案，调用结构构建和计算工具检查候选，再根据结果修正结构并输出候选。由于当前抽取摘要缺失，关于规划策略、反馈信号、验证计算与合成环节仍属待核信息，不应视为已证实的闭环。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

需要从正文结果段确认motif设计覆盖的体系、结构弛豫/能量或稳定性判据、比较基线及是否有实验验证。现阶段不录入未经核验的数值，建议保持needs_review。

### 5.2 基线、指标与结果

需要从正文结果段确认motif设计覆盖的体系、结构弛豫/能量或稳定性判据、比较基线及是否有实验验证。现阶段不录入未经核验的数值，建议保持needs_review。

### 5.3 科学贡献与证据强度

可能支持综述讨论以结构motif作为Agent生成语言的材料设计路线；需补读全文验证具体科学贡献。 科学贡献与系统贡献按上述证据分别表述。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

作者对照第一性原理计算、数据驱动代理/生成模型和演化或粒子群结构搜索，提出以motif作为可解释设计语言支持超出已知结构的晶体生成。

## 7. 局限性与风险

作者及读者可确认的适用边界：候选结构经第一性原理计算筛选，未报告实际合成验证；motif设计对元素范围、结构表示和所用计算近似的依赖限制了当前证据外推。

## 8. 对综述写作的价值

可能支持综述讨论以结构motif作为Agent生成语言的材料设计路线；需补读全文验证具体科学贡献。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

论文研究Agentic AI以motif语言设计晶体结构，关注如何把结构设计任务表示为可组合的结构单元并由Agent迭代探索。

### 9.2 速记版 pipeline

初步按正文工作流理解为：用户给出目标材料/性质，Agent在motif表示空间提出结构方案，调用结构构建和计算工具检查候选，再根据结果修正结构并输出候选。由于当前抽取摘要缺失，关于规划策略、反馈信号、验证计算与合成环节仍属待核信息，不应视为已证实的闭环。

### 9.3 标注字段汇总

```text
paper_id=ASD-1004
inclusion_status=to_read
scientific_object_modules=04
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=04
module_taxonomy_codes=04.02;04.04
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`04.02.05` 晶体材料；二级：`04.02`。
- 原文位置：PDF p.1。
- 判定：晶体结构中的基元设计与结构性质优化。
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
