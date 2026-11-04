# BioPathfinder: Evidence-guided multi-agent platform enables hypothesis discovery for CAR-T engineering

**论文信息**

- ID：ASD-0896
- 标题：BioPathfinder: Evidence-guided multi-agent platform enables hypothesis discovery for CAR-T engineering
- 作者：Shubing Wang; Yan-Ruide Li; Qian Wang; Youcheng Yang; Xinyuan Shen; Haoran Li; Haochen Nan; Zhoulin Chen; Yichen Zhu; Bo Zhang; Haoyan Ding; Jennifer Soto; Soomin Park; Yi Zheng; Xiangliang Huang; Debiao Li; Song Li
- 年份：2026
- 来源 / venue：openRxiv (preprint)
- DOI / arXiv / URL：https://doi.org/10.64898/2026.07.15.738646
- 一手阅读来源：https://doi.org/10.64898/2026.07.15.738646
- 来源层级：全文
- 阅读版本：bioRxiv v1；主列表题名取当前v2元数据。本文阅读和页码证据对应v1。
- 阅读版本题名：A multi-agent workflow converts CAR-T patient evidence into experimentally testable hypotheses
- 原始全文缓存：C:/Users/20683/Desktop/综述/.tmp_asd_pdfs/C_sources/ASD-0896.pdf
- PDF / 本地文件路径：Reference_PDF/07_Medical_and_Health_Sciences/Wang_2026_BioPathfinder.pdf
- 当前状态：included
- 阅读日期：2026-10-22
- 笔记作者：Codex（读者证据包经主控审核整合）

## Evidence Log

| 判断项 | 结论 / 原文概括 | 证据位置 | 可信度 |
|---|---|---|---|
| 系统有曲线清晰的Agent研究角色 | planner subagent与role-specialized reviewer agents承担机制假设生成、审查及优先排序。 | PDF p.2 Abstract; pp.3–4 Introduction | high |
| Agent分析有临床单细胞和出处追踪的数据资源 | Curator连接CAR-T治疗文献、患者scRNA-seq与临床元数据，并保留provenance。 | PDF pp.3–5, Results | high |
| 系统提出NK样耗竭机制并排序受体基因 | 患者输注后CAR-T细胞中检查NK-like program；虚拟扰动涉及KLRC1、KLRD1、KLRG1。 | PDF pp.5–6, Results | high |
| 由专家审查筛选实验靶点 | 专家选择KLRC1（编码NKG2A）开展实验验证。 | PDF pp.6–7, Results | high |
| NKG2A假设有体外及体内实验跟进 | 慢性刺激诱导NKG2A阳性CD8+ CAR-T表型；NKG2A阻断改善体内抗肿瘤功能/持久性读数。 | PDF pp.7–8, Results; pp.13–14 | high |

## 0. 摘要翻译

BioPathfinder将CAR-T临床研究、患者单细胞RNA测序和临床元数据连接为有来源记录的证据库，并由专门Agent生成、批评和排序可证伪机制假设。摘要追踪NK样转变程序与CAR-T耗竭，优先提出KLRC1/NKG2A靶点；体外和体内慢性刺激模型显示阻断NKG2A可增强抗肿瘤活性及持久性相关功能读数。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 当前判断：included；读者建议：included。
bioRxiv v1全文确认planner subagent与多个专门reviewer/curator agents分工整合来源可追溯的患者单细胞证据、生成并审查机制假设，继而由专家选靶并进入体外/体内验证；Agent角色清楚且有多步科研流程。

### 1.2 排除风险检查

06包含患者单细胞数据、基因和免疫细胞机制；07包含CAR-T肿瘤治疗、临床队列及生物制剂疗法。因疾病治疗目标和CAR-T转化验证，07为主。
完整闭环不是纳入门槛；科研目标、多步行动、至少一项Agent能力及明确科研角色须同时成立。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：06;07
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：07（仅归档，不替代多模块事实）
- 模块内分类路径：06.03.04; 07.02.05
- 分类深度：03/04使用二级；06/07使用固定三级；其余沿用现有树。
- 分类状态：原文证据复核

### 2.2 对象优先判定

全文Results pp. 5–8、13–14、23：患者CAR-T单细胞队列中检查耗竭后细胞的NK-like signature；虚拟扰动比较KLRC1/KLRD1/KLRG1。体外重复肿瘤抗原刺激后NKG2A阳性CD8+ CAR-T比例上升；体内模型中阻断NKG2A提高抗肿瘤功能和持久性相关读数。实验细节/分组见正文，本文证据包未重新计算效应量。

### 2.3 容易混淆的边界

06包含患者单细胞数据、基因和免疫细胞机制；07包含CAR-T肿瘤治疗、临床队列及生物制剂疗法。因疾病治疗目标和CAR-T转化验证，07为主。

## 3. Agent 系统与科研流程角色

bioRxiv v1全文确认planner subagent与多个专门reviewer/curator agents分工整合来源可追溯的患者单细胞证据、生成并审查机制假设，继而由专家选靶并进入体外/体内验证；Agent角色清楚且有多步科研流程。

科研流程与自主能力以本文实际行动和工具调用为依据：

全文（Results pp. 2–8；Methods pp. 8–10、15–17）显示：Curator agent整理CAR-T临床研究、患者单细胞数据及元数据；planner subagent拆分问题并驱动专门reviewer agents在有出处的知识资源上产生、批判及筛选假设；用患者scRNA-seq及基因集富集分析检查NK样耗竭程序，再对KLRC家族基因做virtual perturbation。研究者/专家选择KLRC1后，以慢性抗原刺激的体外和体内CAR-T模型作实验。

## 4. 方法设计

### 4.1 方法动机与设计

把临床单细胞证据和多 Agent 机制假设生成连接至可检验的CAR-T治疗工程目标，并以实验验证机制靶点。

### 4.2 系统流程与组件

全文（Results pp. 2–8；Methods pp. 8–10、15–17）显示：Curator agent整理CAR-T临床研究、患者单细胞数据及元数据；planner subagent拆分问题并驱动专门reviewer agents在有出处的知识资源上产生、批判及筛选假设；用患者scRNA-seq及基因集富集分析检查NK样耗竭程序，再对KLRC家族基因做virtual perturbation。研究者/专家选择KLRC1后，以慢性抗原刺激的体外和体内CAR-T模型作实验。

## 5. 实验与验证

### 5.1 验证方式、对象及任务

全文Results pp. 5–8、13–14、23：患者CAR-T单细胞队列中检查耗竭后细胞的NK-like signature；虚拟扰动比较KLRC1/KLRD1/KLRG1。体外重复肿瘤抗原刺激后NKG2A阳性CD8+ CAR-T比例上升；体内模型中阻断NKG2A提高抗肿瘤功能和持久性相关读数。实验细节/分组见正文，本文证据包未重新计算效应量。

### 5.2 基线、指标与结果

全文Results pp. 5–8、13–14、23：患者CAR-T单细胞队列中检查耗竭后细胞的NK-like signature；虚拟扰动比较KLRC1/KLRD1/KLRG1。体外重复肿瘤抗原刺激后NKG2A阳性CD8+ CAR-T比例上升；体内模型中阻断NKG2A提高抗肿瘤功能和持久性相关读数。实验细节/分组见正文，本文证据包未重新计算效应量。

### 5.3 科学贡献与证据强度

把临床单细胞证据和多 Agent 机制假设生成连接至可检验的CAR-T治疗工程目标，并以实验验证机制靶点。

证据层级：原始全文支持；作者报告结果不等于独立复现。

## 6. 与已有工作的关系

与CAR-T细胞工程、肿瘤免疫和基于组学的治疗靶点发现相关。与纯单细胞标注/临床预测相比，本文将临床队列证据转成实验验证假设。

## 7. 局限性与风险

已审阅bioRxiv v1全文。候选机制的排序包含专家判断，临床单细胞队列及模型实验外部效度仍有限；全文证据不应解读为Agent自主完成了全部实验或临床治疗开发。

## 8. 对综述写作的价值

可作为从临床组学到体内外验证的多Agent治疗假设案例。

推荐引用强度：普通引用，可在核对原文后用于相应领域案例。

## 9. 总结

### 9.1 一句话概括

多Agent把CAR-T证据转为实验假设

### 9.2 速记版 pipeline

全文（Results pp. 2–8；Methods pp. 8–10、15–17）显示：Curator agent整理CAR-T临床研究、患者单细胞数据及元数据；planner subagent拆分问题并驱动专门reviewer agents在有出处的知识资源上产生、批判及筛选假设；用患者scRNA-seq及基因集富集分析检查NK样耗竭程序，再对KLRC家族基因做virtual perturbation。研究者/专家选择KLRC1后，以慢性抗原刺激的体外和体内CAR-T模型作实验。

### 9.3 标注字段汇总

```text
paper_id=ASD-0896
inclusion_status=included
scientific_object_modules=06;07
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=07
module_taxonomy_codes=06.03.04; 07.02.05
source_level=fulltext
fulltext_followup_required=false
```

### 全文后续要求

本轮已读原始全文并完成对象分类；无需为纳入/分类另做全文补读。具体引用时仍需回查相应原文位置。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O4 需物理检验 | 从患者CAR-T单细胞数据提出KLRC1/NKG2A靶点假设并进行体外慢性刺激和体内模型实验验证，是需物理检验的新治疗工程目标 | “体外重复肿瘤抗原刺激后NKG2A阳性CD8+ CAR-T比例上升” · L89 |
| 验证强度 | V3 物理实验 | 体外慢性刺激诱导NKG2A表型，体内NKG2A阻断改善抗肿瘤功能和持久性读数，有物理实验验证 | “体内模型中阻断NKG2A提高抗肿瘤功能和持久性相关读数” · L89 |
| 系统自主性 | L2 闭环执行者 |  | — |

- 强验证（V3–V4）：是
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
