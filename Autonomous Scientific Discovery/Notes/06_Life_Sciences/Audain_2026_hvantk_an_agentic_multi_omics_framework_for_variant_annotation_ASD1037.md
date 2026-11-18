# hvantk: an agentic multi-omics framework for variant annotation and analysis

**论文信息**

- ID：ASD-1037
- 标题：hvantk: an agentic multi-omics framework for variant annotation and analysis
- 作者：Enrique Audain; Yasset Perez-Riverol; Marc-Phillip Hitz
- 年份：2026
- 来源 / venue：bioRxiv preprint
- DOI / arXiv / URL：https://doi.org/10.64898/2026.10.19.760196
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1037.txt
- PDF / 本地文件路径：Reference_PDF/06_Life_Sciences/Audain_2026_hvantk_an_agentic_multi_omics_framework_for_variant_annotation_ASD1037.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| Agent行为 | AI coding agent可以新增数据提供者或驱动workflow。 | Abstract；核验TXT行号 200 | can update a data provider or add a new one | 高（一手正文；非独立复现） |
| 框架资源 | 整合21个公开多组学数据提供者。 | Abstract；核验TXT行号 43 | hvantk agentically integrates 21 public | 高（一手正文；非独立复现） |
| 多队列对象 | 使用CHD、Epi25与SCHEMA病例对照队列。 | Abstract / Results；核验TXT行号 66 | developmental and epileptic encephalopathy (Epi25) 26 and schizophrenia (SCHEMA). | 高（一手正文；非独立复现） |
| 分析任务 | 联合遗传负担统计与生物注释得到逐基因排序。 | Abstract；核验TXT行号 220 | combining burden statistics with biological annotations to generate a ranked per-gene 90 score. | 高（一手正文；非独立复现） |
| 定量结果 | 多组学加入后AUC在三个队列提升。 | Results；核验TXT行号 68 | Re-ranking of gene-based burden testing results using 27 multi-omic annotations improved the recovery of curated disease genes from 26% to 28 49% in CHD, 40% to 48% in Epi25 and 51% to 54% in SCHEMA, among the top decile 29 re-ranked genes. | 高（一手正文；非独立复现） |
| Agent边界 | 分析runtime确定性运行且不依赖LLM。 | Results / Framework；核验TXT行号 208 | runtime itself remains deterministic and independent of large language models (LLMs). | 高（一手正文；非独立复现） |
| 主控复核：具体科学对象 | 三队列为癫痫性脑病、精神分裂症和先天性心脏病；07.03.02生物统计学是分析方法，不是被研究对象。保留06基因组学，并将07细化到神经病、精神病和心血管病对象。 | TXT line 522；核验TXT行号 522 | We analysed three cohorts: the developmental and epileptic 205 encephalopathy collection (Epi25) [8], the SCHEMA schizophrenia meta-analysis [9], 206 and a congenital heart disease (CHD) cohort [10]. CHD is the study primary cohort, 207 since it is run t | 高（一手正文；非独立复现） |

## 0. 摘要翻译

hvantk为大规模遗传变异注释和多组学分析提供统一数据模型、资源插件与Agent skills。AI coding agent可新增数据源并编排分析；作者在先心病、发育性癫痫性脑病和精神分裂症队列中验证多组学特征对疾病基因排序的贡献。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。研究目标是多队列遗传变异分析和疾病候选基因排序。
  - 原文位置：Abstract / Results；核验TXT行号 216；引文：We integrate 21 public resources and apply hvantk to per-sample gVCFs
- 多步行动过程：yes。Agent skills帮助添加注释资源并编排分析工作流。
  - 原文位置：Abstract；核验TXT行号 200；引文：can update a data provider or add a new one
- 至少一种Agent能力：yes。AI coding agent开发资源插件时必须遵循schema并通过验证。
  - 原文位置：Results / Framework；核验TXT行号 290；引文：AI coding agent adds a provider
- 明确科研流程角色：yes。联合遗传负担与生物注释生成基因排序。
  - 原文位置：Abstract / Results；核验TXT行号 220；引文：combining burden statistics with biological annotations to generate a ranked per-gene

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：06;07
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：06（仅归档，不覆盖其他模块）
- 模块内分类路径：06.03.01 基因组学；07.02.06 神经病学；07.02.07 精神病学；07.02.09 心血管病学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

三队列为癫痫性脑病、精神分裂症和先天性心脏病；07.03.02生物统计学是分析方法，不是被研究对象。保留06基因组学，并将07细化到神经病、精神病和心血管病对象。

### 2.3 容易混淆的边界

三队列为癫痫性脑病、精神分裂症和先天性心脏病；07.03.02生物统计学是分析方法，不是被研究对象。保留06基因组学，并将07细化到神经病、精神病和心血管病对象。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM Agent；Tool-using Agent；Hybrid Agent

### 3.2 科研流程角色

tool_use_and_code_execution；data_analysis；result_interpretation

框架平台与AI coding agent skills协作；Agent用于插件开发和分析编排，统计runtime本身确定性执行。

### 3.3 自主能力

AI coding agent开发资源插件时必须遵循schema并通过验证。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

科学贡献是三疾病遗传队列的疾病基因排序分析；系统贡献是可追溯多组学平台与Agent插件/编排能力。

### 4.2 系统流程与组件

输入病例对照队列及多组学数据；使用Hail/AnnData数据模型并保存版本来源；执行队列分析、负担检验、注释整合及基因重排；schema验证插件。 系统按用户目标加载多组学provider并运行基因负担分析；结合表达、蛋白和变异注释形成每基因评分，再通过外部疾病队列和既有标签评估排序。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

CHD、Epi25、SCHEMA三队列；接入21公共资源；对比基线和加入组学特征的AUC及疾病基因top-decile恢复率。

### 5.2 基线、指标与结果

作者报告加入多组学后ΔAUC分别+0.089、+0.054、+0.028；已知疾病基因恢复率分别26→49%、40→48%、51→54%；表达特征贡献最大。

### 5.3 科学贡献与证据强度

科学贡献是三疾病遗传队列的疾病基因排序分析；系统贡献是可追溯多组学平台与Agent插件/编排能力。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

与全自主LLM基因组分析不同，本文Agent承担资源扩展与流程驱动，核心运算独立于LLM。

## 7. 局限性与风险

作者指出真值基因集合不完整、CHD阳性较少；不能视为临床变异判读或新机制确证。

## 8. 对综述写作的价值

可支撑多组学整合、可追溯变异分析和Agent辅助生物信息基础设施。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

多组学注释提升三个疾病队列的候选基因排序。

### 9.2 速记版 pipeline

输入病例对照队列及多组学数据；使用Hail/AnnData数据模型并保存版本来源；执行队列分析、负担检验、注释整合及基因重排；schema验证插件。 系统按用户目标加载多组学provider并运行基因负担分析；结合表达、蛋白和变异注释形成每基因评分，再通过外部疾病队列和既有标签评估排序。

### 9.3 标注字段汇总

```text
paper_id=ASD-1037
inclusion_status=to_read
scientific_object_modules=06;07
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=06
module_taxonomy_codes=06.03.01;07.02.06;07.02.07;07.02.09
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O3 新实例 | 在已知队列上重新排序疾病基因候选 | “combining burden statistics with biological annotations” · L44 |
| 验证强度 | V2 计算/仿真/回顾性 | 与已知疾病基因恢复率比较为回顾性验证 | “recovery of curated disease genes” · L25 |
| 系统自主性 | L1 任务助手 | Agent可新增数据源并编排分析 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
