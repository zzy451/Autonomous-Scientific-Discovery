# Agentic AI for Density-Functional Development: Revisiting r2SCAN

**论文信息**

- ID：ASD-1051
- 标题：Agentic AI for Density-Functional Development: Revisiting r2SCAN
- 作者：Santosh Adhikari; Kelsey A. Parker; Etinosa Osaro; Swagata Roy; Dario Rocca
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2609.19419
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1051.txt
- PDF / 本地文件路径：Reference_PDF/03_Chemical_Sciences/Adhikari_2026_Agentic_AI_for_Density_Functional_Development_Revisiting_r2SCAN_ASD1051.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 科学目标 | 工作开展受物理约束的meta-GGA泛函设计。 | Abstract；核验TXT行号 7 | physics-constrained agentic development of a meta-generalized gradient approxi- mation (meta-GGA) functional using a large language model (LLM) to assist the search and optimization of a band-gap-oriented revision of r2SCAN. | 高（一手正文；非独立复现） |
| 搜索方法 | Agent根据约束、知识和搜索反馈提出稀疏交换/相关修正形式。 | Abstract；核验TXT行号 20 | The agent then combined these criteria with its pretrained knowledge and accumulated search feedback to propose and refine sparse forms, prioritizing terms tied to the iso-orbital response | 高（一手正文；非独立复现） |
| 固体对象 | 24种固体的带隙benchmark中MAE由1.26降至0.96 eV。 | Abstract；核验TXT行号 12 | a benchmark comprising 24 solids from 1.26 to 0.96 eV | 高（一手正文；非独立复现） |
| 化学对象 | 329项反应能benchmark的聚合MAE从4.79降至4.42 kcal/mol。 | Abstract；核验TXT行号 13 | 329 reactions from 4.79 to 4.42 kcal/mol. | 高（一手正文；非独立复现） |
| 验证机制 | LLM critic筛查候选，随后确定性程序验证物理约束。 | Abstract；核验TXT行号 22 | a second LLM critic screened proposals before deterministic verification. | 高（一手正文；非独立复现） |
| 主控复核：具体科学对象 | 密度泛函修正分别在固体带隙、分子结构/能量与反应能基准验证；固体材料和分子化学对象均被直接测试。 | TXT line 12；核验TXT行号 12 | r2SCAN+, reduces the band-gap MAE on a benchmark comprising 24 solids from 1.26 to 0.96 eV and the aggregate MAE across a benchmark comprising 329 reactions from 4.79 to 4.42 kcal/mol. To achieve this, we first curated 78 exchange and 90 correlation candidate | 高（一手正文；非独立复现） |

## 0. 摘要翻译

本文以Agent协助改进r2SCAN非经验meta-GGA密度泛函，目标提升固体带隙表现而保留物理约束。作者从78种交换与90种相关修正项构造大搜索空间，用LLM优先排序组合并根据反馈修订，随后进行确定性验证及外部基准评估。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。目标是以非经验约束开发并改进r2SCAN密度泛函。
  - 原文位置：Abstract；核验TXT行号 7；引文：physics-constrained agentic development of a meta-generalized gradient approxi- mation (meta-GGA) functional using a large language model (LLM) to assist the search and optimization of a band-gap-oriented revision of r2SCAN.
- 多步行动过程：yes。Agent提议、筛选并细化修正项，再交系数优化和确定性验证。
  - 原文位置：Abstract / Introduction；核验TXT行号 20；引文：The agent then combined these criteria with its pretrained knowledge and accumulated search feedback to propose and refine sparse forms, prioritizing terms tied to the iso-orbital response
- 至少一种Agent能力：yes。模型利用已积累搜索反馈选择候选表达式，critic筛查后确定性校验。
  - 原文位置：Abstract；核验TXT行号 22；引文：a second LLM critic screened proposals before deterministic verification.
- 明确科研流程角色：yes。Agent参与泛函假设生成、搜索引导和数值优化。
  - 原文位置：Introduction；核验TXT行号 20；引文：The agent then combined these criteria with its pretrained knowledge and accumulated search feedback to propose and refine sparse forms, prioritizing terms tied to the iso-orbital response

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

密度泛函修正分别在固体带隙、分子结构/能量与反应能基准验证；固体材料和分子化学对象均被直接测试。

### 2.3 容易混淆的边界

密度泛函修正分别在固体带隙、分子结构/能量与反应能基准验证；固体材料和分子化学对象均被直接测试。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM Agent；Planning Agent；Tool-using Agent

### 3.2 科研流程角色

hypothesis_generation；experimental_design；tool_use_and_code_execution；data_analysis；evidence_assessment_and_validation

Agent生成和排序稀疏泛函修正；第二个LLM critic审核候选；数值优化与物理约束程序负责确定性检查。科学目标、可接受边界和验收规则由研究者定义。

### 3.3 自主能力

模型利用已积累搜索反馈选择候选表达式，critic筛查后确定性校验。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

化学理论侧改进meta-GGA对分子和反应能的表现；材料侧提升固体带隙基准；系统贡献是将灵活假设搜索与物理约束自动验证结合。

### 4.2 系统流程与组件

从r2SCAN成分构造受限候选表达式空间；Agent结合精确约束、物理规范和目标响应提出修正项；记录评估反馈以调整后续搜索；critic先筛选，再通过确定性验证；外部计算固体、分子及反应基准。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

以24种固体的带隙benchmark，以及分子结构/能量、反应能benchmark验证候选；搜索过程与均匀随机搜索对照，并报告筛选后的外部验证。

### 5.2 基线、指标与结果

首选r2SCAN+将24固体带隙MAE从1.26降至0.96 eV，329项反应聚合MAE从4.79降至4.42 kcal/mol。Agent候选下游拒绝比例报告为0.6%，随机搜索为24.6%；51个候选超过最佳随机搜索响应。

### 5.3 科学贡献与证据强度

化学理论侧改进meta-GGA对分子和反应能的表现；材料侧提升固体带隙基准；系统贡献是将灵活假设搜索与物理约束自动验证结合。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

区别于直接拟合属性的经验参数优化，论文遵循非经验约束路线，并用Agent搜索巨大组合空间、由确定性程序把关。

## 7. 局限性与风险

目前是受研究者目标和边界约束的原型；基准数值提升不等同于所有化学/材料问题普遍更优，仍需扩展体系验证。

## 8. 对综述写作的价值

可用于综述Agent参与科学理论/模型构造时，如何把搜索效率与物理约束、跨对象验证结合。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

物理约束Agent搜索生成r2SCAN修正，并在固体带隙和分子反应基准上验证。

### 9.2 速记版 pipeline

从r2SCAN成分构造受限候选表达式空间；Agent结合精确约束、物理规范和目标响应提出修正项；记录评估反馈以调整后续搜索；critic先筛选，再通过确定性验证；外部计算固体、分子及反应基准。

### 9.3 标注字段汇总

```text
paper_id=ASD-1051
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

- 归档分类：`03.02.11` 理论与计算化学；二级：`03.02`。
- 原文位置：PDF p.1。
- 判定：r2SCAN交换关联泛函的Agent修正与确定性验证，理论计算化学。
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
