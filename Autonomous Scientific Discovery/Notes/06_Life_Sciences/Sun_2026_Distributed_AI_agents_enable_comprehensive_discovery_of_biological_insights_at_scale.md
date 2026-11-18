# Distributed AI agents enable comprehensive discovery of biological insights at scale

**论文信息**

- ID：ASD-0897
- 标题：Distributed AI agents enable comprehensive discovery of biological insights at scale
- 作者：Alexander Sun; Joshua J Park; David DeTomaso; Seoyeon Kim; Amelia Liu; Suyash Shringarpure; Kenny Kim; Patrick C Thompson; Tuo Shi; Yunyun Wang; Eran A Mukamel; Grace XY Zheng; Y Joy Jiao; Xin Jin
- 年份：2026
- 来源 / venue：openRxiv (preprint)
- DOI / arXiv / URL：https://doi.org/10.64898/2026.10.15.759436
- 一手阅读来源：https://doi.org/10.64898/2026.10.15.759436
- 来源层级：全文
- 阅读版本：对应缓存来源版本，参见Evidence Log
- 阅读版本题名：Distributed AI agents enable comprehensive discovery of biological insights at scale
- 原始全文缓存：C:/Users/20683/Desktop/综述/.tmp_asd_pdfs/C_sources/ASD-0897.pdf
- PDF / 本地文件路径：Reference_PDF/06_Life_Sciences/Sun_2026_Distributed_AI_agents_enable_comprehensive_discovery_of_biological_insights_at_scale.pdf
- 当前状态：included
- 阅读日期：2026-10-22
- 笔记作者：Codex（读者证据包经主控审核整合）

## Evidence Log

| 判断项 | 结论 / 原文概括 | 证据位置 | 可信度 |
|---|---|---|---|
| 按扰动给Agent分工并汇总 | one agent assigned to each perturbation and evidence-linked reports synthesized across targets。 | PDF pp.2–3, Abstract/Introduction | high |
| 科学对象是全脑体内CRISPR Perturb-seq | 架构直接用于whole-brain in vivo Perturb-seq atlas。 | PDF pp.2–3, Abstract/Introduction | high |
| 评估隐藏结论后的结果重建 | without access to source manuscript, agents recovered its conclusions。 | PDF pp.2–3, Abstract/Introduction | high |
| 评估留出扰动预测及关系发现 | 预测held-out perturbation effects并识别共享/相反的扰动响应关系。 | PDF pp.2–3, Abstract/Introduction | high |
| 采用盲法专家进行比较评价 | 盲法专家偏好distributed interpretations over single-agent output并支持发现排序。 | PDF p.2 Abstract; Results pp.12–14 | high |

## 0. 摘要翻译

该研究将多个 AI Agent 分配给大型实验的不同分析面，再整合为全局解释。应用于全脑 Perturb-seq atlas，系统在数分钟内并行检查数据、重建来源论文结论、预测留出扰动效应，并识别扰动间共同或相反关系；盲法专家更偏好分布式解释并认可其发现排序。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 当前判断：included；读者建议：included。
bioRxiv v1全文确认每个扰动对应独立Agent，Agent可检查细胞类型差异表达、比较扰动、调用分析工具和文献，并由综合步骤汇总证据报告；系统还评估隐去原论文后的结论恢复、留出效应预测与专家排序。

### 1.2 排除风险检查

对象是脑细胞及其扰动效应，属于生命科学；摘要未以脑病诊断/治疗为研究目标，故不加07医学模块。
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

全文Results pp. 2–4、10–14：使用whole-brain in vivo Perturb-seq atlas；隐藏来源稿件及结论后评估重建，另作扰动响应预测和扰动关系发现，并用盲法专家评价对照distributed与single-agent解释/排序。全文还报告并行Agent处理时间与单Agent文献覆盖比较；需主控审阅具体数值和测试设定。

### 2.3 容易混淆的边界

对象是脑细胞及其扰动效应，属于生命科学；摘要未以脑病诊断/治疗为研究目标，故不加07医学模块。

## 3. Agent 系统与科研流程角色

bioRxiv v1全文确认每个扰动对应独立Agent，Agent可检查细胞类型差异表达、比较扰动、调用分析工具和文献，并由综合步骤汇总证据报告；系统还评估隐去原论文后的结论恢复、留出效应预测与专家排序。

科研流程与自主能力以本文实际行动和工具调用为依据：

全文（Methods pp. 4–9、11–12）描述分布式生物学推理架构：将全脑体内CRISPR Perturb-seq数据按扰动分配给专门Agent，各Agent在不读取原论文/原结论的条件下产生带文献证据的解释，再由综合Agent跨扰动汇总；包含结论重建、留出扰动响应预测和发现排序。

## 4. 方法设计

### 4.1 方法动机与设计

以按实验方面分布式协作的Agent扩展大型单细胞扰动实验的解释吞吐量，并提出后续研究优先级。

### 4.2 系统流程与组件

全文（Methods pp. 4–9、11–12）描述分布式生物学推理架构：将全脑体内CRISPR Perturb-seq数据按扰动分配给专门Agent，各Agent在不读取原论文/原结论的条件下产生带文献证据的解释，再由综合Agent跨扰动汇总；包含结论重建、留出扰动响应预测和发现排序。

## 5. 实验与验证

### 5.1 验证方式、对象及任务

全文Results pp. 2–4、10–14：使用whole-brain in vivo Perturb-seq atlas；隐藏来源稿件及结论后评估重建，另作扰动响应预测和扰动关系发现，并用盲法专家评价对照distributed与single-agent解释/排序。全文还报告并行Agent处理时间与单Agent文献覆盖比较；需主控审阅具体数值和测试设定。

### 5.2 基线、指标与结果

全文Results pp. 2–4、10–14：使用whole-brain in vivo Perturb-seq atlas；隐藏来源稿件及结论后评估重建，另作扰动响应预测和扰动关系发现，并用盲法专家评价对照distributed与single-agent解释/排序。全文还报告并行Agent处理时间与单Agent文献覆盖比较；需主控审阅具体数值和测试设定。

### 5.3 科学贡献与证据强度

以按实验方面分布式协作的Agent扩展大型单细胞扰动实验的解释吞吐量，并提出后续研究优先级。

证据层级：原始全文支持；作者报告结果不等于独立复现。

## 6. 与已有工作的关系

与Perturb-seq、单细胞扰动生物学、文献增强数据解释相关；区别于单模型直接分析完整数据，强调多Agent并行分工和结果整合。

## 7. 局限性与风险

已审阅bioRxiv v1全文。证据来自单一whole-brain Perturb-seq研究及其扰动集合；结论重建、预测和盲评表现不等于已证明跨实验平台通用，也不表示Agent取代实验验证。

## 8. 对综述写作的价值

有利于讨论多Agent扩大组学解释能力及其对实验后续假设排序的价值。

推荐引用强度：普通引用，可在核对原文后用于相应领域案例。

## 9. 总结

### 9.1 一句话概括

分布式Agent解释大规模生物扰动

### 9.2 速记版 pipeline

全文（Methods pp. 4–9、11–12）描述分布式生物学推理架构：将全脑体内CRISPR Perturb-seq数据按扰动分配给专门Agent，各Agent在不读取原论文/原结论的条件下产生带文献证据的解释，再由综合Agent跨扰动汇总；包含结论重建、留出扰动响应预测和发现排序。

### 9.3 标注字段汇总

```text
paper_id=ASD-0897
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
| 问题开放度 | O3 新实例 | 在whole-brain Perturb-seq atlas数据上重建来源论文结论、预测留出扰动效应，答案可由数据集和原文核对 | “隐藏来源稿件及结论后评估重建” · L89 |
| 验证强度 | V2 计算/仿真/回顾性 | 与来源论文结论、专家评价和held-out扰动预测比对，属回顾性数据分析验证 | “盲法专家偏好distributed interpretations over single-agent output” · L29 |
| 系统自主性 | L1 任务助手 |  | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
