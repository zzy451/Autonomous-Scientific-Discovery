# Perturb-ME: Scalable mechanism discovery from phenotype-enriched genome-wide screens

**论文信息**

- ID：ASD-0902
- 标题：Perturb-ME: Scalable mechanism discovery from phenotype-enriched genome-wide screens
- 作者：Hanchen Wang; Jiacheng Gu; Chris J. Frangieh; Michael S. Cuoco; Maryann Zhao; Arindam Sett; Tom Beyer; Kuan Pang; Etzard Stolte; Zihan Xu; Jure Leskovec; Orit Rozenblatt-Rosen; Vivek Natarajan; Kathryn Geiger-Schuller; Pratiksha I. Thakore; Aviv Regev
- 年份：2026
- 来源 / venue：openRxiv (preprint)
- DOI / arXiv / URL：https://doi.org/10.64898/2026.08.17.745330
- 一手阅读来源：https://www.biorxiv.org/content/10.64898/2026.08.17.745330v1.full
- 来源层级：全文
- 阅读版本：bioRxiv v1, DOI 10.64898/2026.08.17.745330；完整HTML正文；补充压缩包未取得，未声称已读。
- 阅读版本题名：Perturb-ME: Scalable mechanism discovery from phenotype-enriched genome-wide screens
- 原始全文缓存：C:/Users/20683/Desktop/综述/.tmp_asd_pdfs/Perturb_ME_full.html
- PDF / 本地文件路径：未归档PDF
- 当前状态：included
- 阅读日期：2026-10-22
- 笔记作者：Codex（读者证据包经主控审核整合）

## Evidence Log

| 判断项 | 结论 / 原文概括 | 证据位置 | 可信度 |
|---|---|---|---|
| 论文身份与来源 | 题名为Perturb-ME: Scalable mechanism discovery from phenotype-enriched genome-wide screens，DOI 10.64898/2026.08.17.745330。 | bioRxiv v1首页与DOI | high |
| 科学对象为黑色素瘤MHC-I表面表达 | 在melanoma细胞比较HLA-low与HLA-high表型，以表面蛋白表达为端点。 | 全文Abstract与Introduction | high |
| 实验结合全基因组CRISPR、表型富集与多模态单细胞测量 | 使用pooled CRISPR、FACS富集，并测量RNA、表面蛋白和guide RNA。 | Introduction、Figure 1图注 | high |
| Agent接收结构化实验模型和筛选结果 | 输入含7个调控模块、9个gene programs代表基因及MAGeCK前100个激活/抑制命中和排名、效应值、模块归属。 | Results，Co-Scientist方法段 | high |
| Agent开展多步机制解释 | 执行模块和gene program标注、文献交叉引用、机制联系提出及候选机制排序。 | Introduction与Results工作流段 | high |
| Agent比较假说并汇总机制框架 | 对竞争机制模型进行tournament，形成HLA Rheostat解释，正文指向Supplementary File 2。 | Results，hypothesis tournament及Extended Data Table 1 | high |
| 实验模型有独立可量化结果 | 模型含221个扰动和18,683个分子特征，识别7模块、9程序并恢复IFNγ–MHC-I轴。 | Results模型结果 | high |
| 明确区分Agent解释与实验验证 | AI输出是供研究者考虑的可检验假说；实验结果来自CRISPR筛选和统计模型。 | Discussion | high |
| 作者提供分析代码和数据材料 | 作者仓库Genentech/PerturbME及Figshare DOI 10.6084/m9.figshare.33264225。 | Code/Data Availability | high |

## 0. 摘要翻译

提出Perturb-ME，将全基因组CRISPR筛选、表型富集和多模态单细胞RNA/表面蛋白/guide测量结合，以黑色素瘤MHC-I为例。模型覆盖221个调控因子和1,998个响应基因，识别7个模块及9个程序；Co-Scientist将模型与文献整合为调控机制假说。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 当前判断：included；读者建议：included。
全文说明Co-Scientist接收实验模型、模块、基因程序与筛选命中，执行文献交叉检索、机制假说提出和排序，再通过假说竞赛比较候选模型并综合出可检验框架。实验和统计模型由作者团队构建，应将Agent解释贡献与湿实验贡献区分。

### 1.2 排除风险检查

三级代码为06.03.01基因组学（全基因组CRISPR扰动）及07.02.05肿瘤学（黑色素瘤及肿瘤MHC-I表型）。真实肿瘤功能基因组数据支持06与07；不属于01.04通用方法。主要风险是Agent结论强度，而非对象分类。
完整闭环不是纳入门槛；科研目标、多步行动、至少一项Agent能力及明确科研角色须同时成立。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：06;07
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：06（仅归档，不替代多模块事实）
- 模块内分类路径：06.03.01; 07.02.05
- 分类深度：03/04使用二级；06/07使用固定三级；其余沿用现有树。
- 分类状态：原文证据复核

### 2.2 对象优先判定

测序277,152个细胞；命中guide覆盖最多约提高20倍；模型含221个扰动因子和1,998个响应基因，并恢复已知IFNγ–MHC-I轴。Agent提出的机制假说是研究者可继续检验的解释，不等同于独立实验验证。

### 2.3 容易混淆的边界

三级代码为06.03.01基因组学（全基因组CRISPR扰动）及07.02.05肿瘤学（黑色素瘤及肿瘤MHC-I表型）。真实肿瘤功能基因组数据支持06与07；不属于01.04通用方法。主要风险是Agent结论强度，而非对象分类。

## 3. Agent 系统与科研流程角色

全文说明Co-Scientist接收实验模型、模块、基因程序与筛选命中，执行文献交叉检索、机制假说提出和排序，再通过假说竞赛比较候选模型并综合出可检验框架。实验和统计模型由作者团队构建，应将Agent解释贡献与湿实验贡献区分。

科研流程与自主能力以本文实际行动和工具调用为依据：

基于HLA-I高低表达进行表型富集CRISPR screen，利用Perturb-CITE-seq获取RNA、13种表面蛋白及guide。正则化模型分析221种扰动及18,683个分子特征，分解为7模块和9个gene programs。Co-Scientist接收结构化结果和筛选命中，完成文献交叉分析及机制假说比较。

## 4. 方法设计

### 4.1 方法动机与设计

提出表型富集的多模态全基因组扰动筛选，并以AI co-scientist将扰动结果和文献整合为机制假说。

### 4.2 系统流程与组件

基于HLA-I高低表达进行表型富集CRISPR screen，利用Perturb-CITE-seq获取RNA、13种表面蛋白及guide。正则化模型分析221种扰动及18,683个分子特征，分解为7模块和9个gene programs。Co-Scientist接收结构化结果和筛选命中，完成文献交叉分析及机制假说比较。

## 5. 实验与验证

### 5.1 验证方式、对象及任务

测序277,152个细胞；命中guide覆盖最多约提高20倍；模型含221个扰动因子和1,998个响应基因，并恢复已知IFNγ–MHC-I轴。Agent提出的机制假说是研究者可继续检验的解释，不等同于独立实验验证。

### 5.2 基线、指标与结果

测序277,152个细胞；命中guide覆盖最多约提高20倍；模型含221个扰动因子和1,998个响应基因，并恢复已知IFNγ–MHC-I轴。Agent提出的机制假说是研究者可继续检验的解释，不等同于独立实验验证。

### 5.3 科学贡献与证据强度

提出表型富集的多模态全基因组扰动筛选，并以AI co-scientist将扰动结果和文献整合为机制假说。

证据层级：原始全文支持；作者报告结果不等于独立复现。

## 6. 与已有工作的关系

与Perturb-seq、Perturb-CITE-seq、CRISPR功能基因组学及AI辅助组学解释相关。

## 7. 局限性与风险

bioRxiv预印本；Co-Scientist内部推理轨迹和工具调用细节并不完整。补充材料页面可读，但附件下载连接重置。假说未逐条由独立实验验证。

## 8. 对综述写作的价值

真实科学实验与多步Agent解释相结合的跨06/07案例，须区分实验、统计建模和Agent解释贡献。

推荐引用强度：普通引用，可在核对原文后用于相应领域案例。

## 9. 总结

### 9.1 一句话概括

以多模态扰动筛选探索细胞机制

### 9.2 速记版 pipeline

基于HLA-I高低表达进行表型富集CRISPR screen，利用Perturb-CITE-seq获取RNA、13种表面蛋白及guide。正则化模型分析221种扰动及18,683个分子特征，分解为7模块和9个gene programs。Co-Scientist接收结构化结果和筛选命中，完成文献交叉分析及机制假说比较。

### 9.3 标注字段汇总

```text
paper_id=ASD-0902
inclusion_status=included
scientific_object_modules=06;07
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=06
module_taxonomy_codes=06.03.01; 07.02.05
source_level=fulltext
fulltext_followup_required=false
```

### 全文后续要求

本轮已读原始全文并完成对象分类；无需为纳入/分类另做全文补读。具体引用时仍需回查相应原文位置。


## 2026-10-29 PR剩余差异复核

- 来源深度：`verified_official_pdf_fulltext`。本轮涉及4条差异，其中4条已判定，0条待核。摘要或图注支持的判定不代表全文已逐页核验。

- 原1664行号 `1141`：`reject_pr`。Genome-wide CRISPR screening with matched RNA and guide measurements directly supports genomics (06.03.01); reverting to 06.01 would lose the actual research-object specificity.
  - 位置：PDF p.2; p.5 hypothesis tournament; p.21 Extended Data Table 1；来源：https://doi.org/10.64898/2026.08.17.745330

- 原1664行号 `1142`：`reject_pr`。The current taxonomy defines 06.03.01 genomics, and the genome-wide perturbation experiments support it. Clearing this code is unwarranted.
  - 位置：PDF p.2; p.5 hypothesis tournament; p.21 Extended Data Table 1；来源：https://doi.org/10.64898/2026.08.17.745330

- 原1664行号 `1143`：`reject_pr`。The experiments concern MHC-I regulation in A375 melanoma cells and resistance to checkpoint immunotherapy. This is concrete oncology evidence supporting 07.02.05.
  - 位置：PDF p.2; p.5 hypothesis tournament; p.21 Extended Data Table 1；来源：https://doi.org/10.64898/2026.08.17.745330

- 原1664行号 `1144`：`retain_current`。The complete PDF establishes the scientific goal of explaining MHC-I regulation, multiple steps from module inputs through literature cross-checking to mechanistic hypotheses, Co-Scientist hypothesis-tournament capabilities, and a mechanistic interpretation/hypothesis-generation role. Retain modules 06 and 07. The agent is not credited with performing the entire wet-laboratory workflow.
  - 位置：PDF p.2; p.5 hypothesis tournament; p.21 Extended Data Table 1；来源：https://doi.org/10.64898/2026.08.17.745330

逐条引文、来源文件和限制见 `Coverage_Check/pr1_82_recheck_2026-10-29/final_review.json`。保留现有分类不等于全部分类边界已消除。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O3 新实例 | 表型富集CRISPR筛选测序数据，模型识别调控模块和程序，恢复已知IFNγ–MHC-I轴，答案可由数据和文献核对 | “模型含221个扰动因子和1,998个响应基因，并恢复已知IFNγ–MHC-I轴” · L65 |
| 验证强度 | V2 计算/仿真/回顾性 | 测序277,152个细胞并构建统计模型，Co-Scientist提出机制假说供研究者检验，不是独立实验验证 | “Agent提出的机制假说是研究者可继续检验的解释” · L93 |
| 系统自主性 | L1 任务助手 |  | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
