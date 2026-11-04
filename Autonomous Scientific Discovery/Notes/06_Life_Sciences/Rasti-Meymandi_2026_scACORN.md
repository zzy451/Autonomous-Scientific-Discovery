# scACORN: Context-engineered agent orchestration of specialized small language models for single-cell transcriptomic interpretation

**论文信息**

- ID：ASD-0898
- 标题：scACORN: Context-engineered agent orchestration of specialized small language models for single-cell transcriptomic interpretation
- 作者：Arash Rasti-Meymandi; Sepideh Nahali; Eustache Paramithiotis; Angela M. Cheung; Elham Dolatabadi
- 年份：2026
- 来源 / venue：openRxiv (preprint)
- DOI / arXiv / URL：https://doi.org/10.64898/2026.09.10.750801
- 一手阅读来源：https://doi.org/10.64898/2026.09.10.750801
- 来源层级：全文
- 阅读版本：对应缓存来源版本，参见Evidence Log
- 阅读版本题名：scACORN: Context-engineered agent orchestration of specialized small language models for single-cell transcriptomic interpretation
- 原始全文缓存：C:/Users/20683/Desktop/综述/.tmp_asd_pdfs/C_sources/ASD-0898.pdf
- PDF / 本地文件路径：Reference_PDF/06_Life_Sciences/Rasti-Meymandi_2026_scACORN.pdf
- 当前状态：included
- 阅读日期：2026-10-22
- 笔记作者：Codex（读者证据包经主控审核整合）

## Evidence Log

| 判断项 | 结论 / 原文概括 | 证据位置 | 可信度 |
|---|---|---|---|
| 编排Agent执行专家选择与组合 | 固定语言模型Agent按自然语言playbook选择和组合专门化专家模型。 | PDF pp.1–3, Abstract/Results | high |
| 专家模型经两阶段单细胞数据适配 | domain-aligned contrastive adaptation及geometry-preserving specialization。 | PDF pp.3–5, Results; Methods pp.29–31 | high |
| 研究对象是Tabula Sapiens单细胞转录组 | 所有实验以Tabula Sapiens组织数据为共同生物学基底。 | PDF pp.2–5, Abstract/Results | high |
| 方法组合提高具体benchmark指标 | macro-F1 0.356→0.643，Recall@5 0.868→0.970；单细胞注释专家准确率0.89。 | PDF pp.2–6, Abstract/Results | high |
| 文本反馈改善证据支撑 | playbook优化后unsupported gene citations从14.5%降至3.5%。 | PDF pp.2–3、8–9, Abstract/Results | high |

## 0. 摘要翻译

scACORN将专门化小模型与固定编排Agent结合：Agent根据自然语言playbook在推理时选择和组合专家，playbook还通过文本反馈优化。摘要在Tabula Sapiens的10种组织评测，报告macro-F1由0.36升至0.64、Recall@5由0.87升至0.97，专家平均精确匹配标注准确率0.89，优化playbook后无依据基因引用由14.5%降至3.5%。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 当前判断：included；读者建议：included。
bioRxiv v1全文确认固定的编排语言模型Agent在推理时按自然语言playbook选择并组合单细胞专家模型，playbook通过文本反馈优化；系统承担单细胞表达解释而非一次性问答。

### 1.2 排除风险检查

评测对象是多个组织的单细胞转录组解释，归06.03.04；没有疾病诊断/治疗案例证据，不加07。
完整闭环不是纳入门槛；科研目标、多步行动、至少一项Agent能力及明确科研角色须同时成立。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：06
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：06（仅归档，不替代多模块事实）
- 模块内分类路径：06.03.04
- 分类深度：03/04使用二级；06/07使用固定三级；其余沿用现有树。
- 分类状态：原文证据复核

### 2.2 对象优先判定

全文Results pp. 3–9：在10种Tabula Sapiens组织比较domain alignment、专家专门化和编排设置。transfer macro-F1由0.356升至0.643、Recall@5由0.868升至0.970；专家平均exact-match标注准确率0.89；优化playbook后unsupported gene citations由14.5%降至3.5%。各组织和方法细分见正文/Appendix。

### 2.3 容易混淆的边界

评测对象是多个组织的单细胞转录组解释，归06.03.04；没有疾病诊断/治疗案例证据，不加07。

## 3. Agent 系统与科研流程角色

bioRxiv v1全文确认固定的编排语言模型Agent在推理时按自然语言playbook选择并组合单细胞专家模型，playbook通过文本反馈优化；系统承担单细胞表达解释而非一次性问答。

科研流程与自主能力以本文实际行动和工具调用为依据：

全文（Methods pp. 4–11、29–31）描述：先训练表达数据适配的小型cell-to-text专家，再用保持转录几何结构的专门化步骤处理问题条件下的生物学补全；固定编排LLM Agent按自然语言playbook选择/组合专家，playbook基于文本反馈优化，编排器本身不进行梯度更新。所有实验以Tabula Sapiens为共同单细胞数据底座。

## 4. 方法设计

### 4.1 方法动机与设计

以上下文路由和小模型专家组合处理单细胞转录组任务异质性，提升基于基因表达的生物学解释和证据可追溯性。

### 4.2 系统流程与组件

全文（Methods pp. 4–11、29–31）描述：先训练表达数据适配的小型cell-to-text专家，再用保持转录几何结构的专门化步骤处理问题条件下的生物学补全；固定编排LLM Agent按自然语言playbook选择/组合专家，playbook基于文本反馈优化，编排器本身不进行梯度更新。所有实验以Tabula Sapiens为共同单细胞数据底座。

## 5. 实验与验证

### 5.1 验证方式、对象及任务

全文Results pp. 3–9：在10种Tabula Sapiens组织比较domain alignment、专家专门化和编排设置。transfer macro-F1由0.356升至0.643、Recall@5由0.868升至0.970；专家平均exact-match标注准确率0.89；优化playbook后unsupported gene citations由14.5%降至3.5%。各组织和方法细分见正文/Appendix。

### 5.2 基线、指标与结果

全文Results pp. 3–9：在10种Tabula Sapiens组织比较domain alignment、专家专门化和编排设置。transfer macro-F1由0.356升至0.643、Recall@5由0.868升至0.970；专家平均exact-match标注准确率0.89；优化playbook后unsupported gene citations由14.5%降至3.5%。各组织和方法细分见正文/Appendix。

### 5.3 科学贡献与证据强度

以上下文路由和小模型专家组合处理单细胞转录组任务异质性，提升基于基因表达的生物学解释和证据可追溯性。

证据层级：原始全文支持；作者报告结果不等于独立复现。

## 6. 与已有工作的关系

与单细胞大模型/细胞注释模型、专家混合系统及工具/模型路由Agent相关；差异在于上下文编排和文本反馈调整playbook。

## 7. 局限性与风险

已审阅bioRxiv v1全文。评估以Tabula Sapiens组织和特定基因标注/检索任务为主，不能直接等同于新机制发现；结果也依赖专家模型训练与playbook构造。

## 8. 对综述写作的价值

可比较Agent选择/组合专门模型与单一通用模型在单细胞生物学上的作用。

推荐引用强度：普通引用，可在核对原文后用于相应领域案例。

## 9. 总结

### 9.1 一句话概括

Agent协调单细胞注释专家

### 9.2 速记版 pipeline

全文（Methods pp. 4–11、29–31）描述：先训练表达数据适配的小型cell-to-text专家，再用保持转录几何结构的专门化步骤处理问题条件下的生物学补全；固定编排LLM Agent按自然语言playbook选择/组合专家，playbook基于文本反馈优化，编排器本身不进行梯度更新。所有实验以Tabula Sapiens为共同单细胞数据底座。

### 9.3 标注字段汇总

```text
paper_id=ASD-0898
inclusion_status=included
scientific_object_modules=06
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=06
module_taxonomy_codes=06.03.04
source_level=fulltext
fulltext_followup_required=false
```

### 全文后续要求

本轮已读原始全文并完成对象分类；无需为纳入/分类另做全文补读。具体引用时仍需回查相应原文位置。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O2 既定基准 | 在Tabula Sapiens的10种组织上评测单细胞注释和基因检索准确率，属预定义基准 | “在10种Tabula Sapiens组织比较domain alignment、专家专门化和编排设置” · L89 |
| 验证强度 | V1 基准/内部评测 | 报告macro-F1、Recall@5、标注准确率和unsupported gene citations等基准指标 | “transfer macro-F1由0.356升至0.643、Recall@5由0.868升至0.970” · L89 |
| 系统自主性 | L1 任务助手 |  | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
