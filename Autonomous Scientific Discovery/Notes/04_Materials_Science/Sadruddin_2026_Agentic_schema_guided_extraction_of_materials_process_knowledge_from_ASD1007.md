# Agentic schema-guided extraction of materials process knowledge from scientific literature

**论文信息**

- ID：ASD-1007
- 标题：Agentic schema-guided extraction of materials process knowledge from scientific literature
- 作者：Sameer Sadruddin; Jennifer D'Souza
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2610.06322
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1007.txt
- PDF / 本地文件路径：全文已缓存；PDF尚未归档，详见资料清单
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 评估语料包括176篇ZnO和IGZO原子层沉积论文及专家标注子集。 | 评估语料包括176篇ZnO和IGZO原子层沉积论文及专家标注子集。 | Results；核验TXT行号 231 | We evaluate the framework on 176 atomic-layer-deposition papers describing zinc oxide (ZnO) and indium–gallium–zinc oxide (IGZO), together with an expert-annotated full-schema subset. PubChem normalization improves exact-match extraction F1 for every | 高（一手正文；非独立复现） |
| 实体规范化和Agent核验共同将材料文献转成机器可处理的实验知识。 | 实体规范化和Agent核验共同将材料文献转成机器可处理的实验知识。 | Methods/Results；核验TXT行号 231 | chemical canonicalization and targeted agentic verification provide complementary controls for converting complex materials literature into reusable, machine-actionable experimental knowledge. keywordsmaterials informatics, scientific informati | 高（一手正文；非独立复现） |
| 作者报告ZnO最佳F1由直接规范化抽取0.591提升至Agent refinement后的0.805，IGZO最佳F1为0.344。 | 作者报告ZnO最佳F1由直接规范化抽取0.591提升至Agent refinement后的0.805，IGZO最佳F1为0.344。 | Results；核验TXT行号 231 | PubChem normalization improves exact-match extraction F1 for every tested model. For ZnO, the best F1 increases from 0.591 for direct normalized extraction to 0.805 with agentic refinement, whereas the best IGZO result is 0.344, revealing the greater | 高（一手正文；非独立复现） |
| 深层schema金标准仅覆盖两篇论文和13个由文本抽取的工艺实例。 | 深层schema金标准仅覆盖两篇论文和13个由文本抽取的工艺实例。 | Limitations；核验TXT行号 924 | The deep-schema gold standard covers two representative papers and thirteen text-derived process instances, although each instance contains many property–value decisions. Expanding expert annotation across more materials and deposition chemistries wo | 高（一手正文；非独立复现） |
| 作者建议扩大专家标注材料与沉积化学范围以获得更可靠误差分析。 | 作者建议扩大专家标注材料与沉积化学范围以获得更可靠误差分析。 | Limitations；核验TXT行号 924 | Expanding expert annotation across more materials and deposition chemistries would support stronger variance estimates and property-level error analysis. The transfer experiments demonstrate portability of the orchestration but are not intended as st | 高（一手正文；非独立复现） |

## 0. 摘要翻译

论文构建schema引导的Agent流程，从原子层沉积文献抽取材料、工艺步骤和测量属性。流程结合化学实体规范化及Agent核验，在176篇ZnO和IGZO论文上评估，并以专家标注深层schema检查工艺片段。深层金标准规模仍有限。正文同时报告了任务设置、方法验证及适用边界，相关结论应结合所引原文和论文实验结果理解。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。研究目标是从ZnO和IGZO原子层沉积文献中抽取材料、工艺及测量知识，构造成可复用结构化记录。
  - 原文位置：Results；核验TXT行号 231；引文：We evaluate the framework on 176 atomic-layer-deposition papers describing zinc oxide (ZnO) and indium–gallium–zinc oxide (IGZO), together with an expert-annotated full-schema subset. PubChem normalization improves exact-match extraction F1 for every
- 多步行动过程：yes。流程包含schema字段抽取、化学实体规范化、Agent针对性核验和结果评估，而非单次文本问答。
  - 原文位置：Methods/Results；核验TXT行号 231；引文：chemical canonicalization and targeted agentic verification provide complementary controls for converting complex materials literature into reusable, machine-actionable experimental knowledge. keywordsmaterials informatics, scientific informati
- 至少一种Agent能力：yes。Agent refinement与PubChem规范化可提升ZnO抽取效果；IGZO结果较低，显示不同材料术语的难度差异。
  - 原文位置：Results；核验TXT行号 231；引文：PubChem normalization improves exact-match extraction F1 for every tested model. For ZnO, the best F1 increases from 0.591 for direct normalized extraction to 0.805 with agentic refinement, whereas the best IGZO result is 0.344, revealing the greater
- 明确科研流程角色：yes。该Agent在科研流程中承担材料工艺文献知识抽取和核验，为后续材料研究提供机器可读实验信息。
  - 原文位置：Limitations；核验TXT行号 924；引文：The deep-schema gold standard covers two representative papers and thirteen text-derived process instances, although each instance contains many property–value decisions. Expanding expert annotation across more materials and deposition chemistries wo

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

归入04.02，研究对象是材料制备过程知识及薄膜材料；这是从文献构建机器可读记录，不等同于Agent亲自执行ALD实验。

### 2.3 容易混淆的边界

归入04.02，研究对象是材料制备过程知识及薄膜材料；这是从文献构建机器可读记录，不等同于Agent亲自执行ALD实验。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM Agent；Tool-using Agent

### 3.2 科研流程角色

tool_use_and_code_execution；data_analysis；evidence_assessment_and_validation

SciKGExtract以预定义schema约束文献解析，配合化学实体规范化和定向Agent核验，目标是把ALD论文中的材料、沉积过程及测量属性整理成结构化记录。

### 3.3 自主能力

Agent refinement与PubChem规范化可提升ZnO抽取效果；IGZO结果较低，显示不同材料术语的难度差异。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

论文提供面向材料工艺知识的schema抽取与核验流程，并以ALD文献说明实体规范化和定向复核如何改善结构化知识质量。

### 4.2 系统流程与组件

系统对论文文本抽取schema字段，再将化学名称规范化；Agent依据字段和上下文检查疑难条目并修订。评估语料含176篇ZnO与IGZO原子层沉积论文，并单独构建深层工艺schema的专家标注样本。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

作者报告不同模型与提取策略的字段级比较、规范化前后精确匹配F1，以及专家对深层schema结果的评估；另有跨材料/任务迁移测试。深层金标准仅含两篇代表性论文和13个工艺片段。

### 5.2 基线、指标与结果

化学规范化提升各测试模型的精确匹配F1；Agent修订有帮助，但增加Agent数量不必然改进。深层实验重建仍困难，说明词项抽取成绩不能等同于完整复原实验方法。

### 5.3 科学贡献与证据强度

论文提供面向材料工艺知识的schema抽取与核验流程，并以ALD文献说明实体规范化和定向复核如何改善结构化知识质量。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

相较通用科学实体抽取，本文要求字段遵循领域schema并追踪沉积步骤；它也把LLM提取与化学本体规范化、人工专家评估组合起来。

## 7. 局限性与风险

专家深层标注规模很小，语料集中于ZnO/IGZO及ALD，迁移结果不足以证明对其他化学体系普遍有效。抽取字段的准确也不保证缺失上下文中的完整实验复现。

## 8. 对综述写作的价值

可用于比较材料文献结构化抽取的schema、实体规范化、Agent复核和专家金标准覆盖范围。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

论文构建schema引导的Agent流程，从原子层沉积文献抽取材料、工艺步骤和测量属性。流程结合化学实体规范化及Agent核验，在176篇ZnO和IGZO论文上评估，并以专家标注深层schema检查工艺片段。深层金标准规模仍有限。正文同时报告了任务设置、方法验证及适用边界，相关结论应结合所引原文和论文实验结果理解。

### 9.2 速记版 pipeline

系统对论文文本抽取schema字段，再将化学名称规范化；Agent依据字段和上下文检查疑难条目并修订。评估语料含176篇ZnO与IGZO原子层沉积论文，并单独构建深层工艺schema的专家标注样本。

### 9.3 标注字段汇总

```text
paper_id=ASD-1007
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

- 归档分类：`04.04.04` 半导体材料；二级：`04.04`。
- 原文位置：PDF p.1。
- 判定：176篇ZnO/IGZO原子层沉积论文中的工艺与测量知识，归半导体材料；须由04.02对齐04.04。
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
