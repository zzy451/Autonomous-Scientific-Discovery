# AutoScreen: AI Co-Scientist System for Target Discovery in Functional Genomics

**论文信息**

- ID：ASD-0894
- 标题：AutoScreen: AI Co-Scientist System for Target Discovery in Functional Genomics
- 作者：Yuanhao Qu; Xufeng Liu; Xiaotong Wang; Meitong Chen; Xiao Luo; Luna Lyu; Ming Yin; Jingwen Hui; Di Yin; Ravi Dinesh; Lin Qiu; Kexin Huang; Hanchen Wang; Shangyuan Tong; Henry Cousins; Ricky Runchuan Feng; Oswaldo Martinez; Junze Zhang; Tanming Chen; Russ Altman; Jure Leskovec; Aviv Regev; Mengdi Wang; Le Cong
- 年份：2026
- 来源 / venue：openRxiv (preprint)
- DOI / arXiv / URL：https://doi.org/10.64898/2026.09.06.749678
- 一手阅读来源：https://doi.org/10.64898/2026.09.06.749678
- 来源层级：全文
- 阅读版本：对应缓存来源版本，参见Evidence Log
- 阅读版本题名：AutoScreen: AI Co-Scientist System for Target Discovery in Functional Genomics
- 原始全文缓存：C:/Users/20683/Desktop/综述/.tmp_asd_pdfs/C_sources/ASD-0894.pdf
- PDF / 本地文件路径：Reference_PDF/06_Life_Sciences/Qu_2026_AutoScreen.pdf
- 当前状态：included
- 阅读日期：2026-10-22
- 笔记作者：Codex（读者证据包经主控审核整合）

## Evidence Log

| 判断项 | 结论 / 原文概括 | 证据位置 | 可信度 |
|---|---|---|---|
| AutoScreen含五个专业Agent和可审计证据来源 | Deep Research、信息整理/证据整合、靶点审查等分工；摘要亦报告超过26个数据库并行搜索。 | PDF p.4, Results: “Five specialist agents convert a query into a ranked report” | high |
| 工作流含预筛设计和筛后重排两个步骤 | 自然语言研究问题生成扰动文库；screen后读取统计指标并结合生物上下文重排候选。 | PDF pp.3–4, Methods/Results | high |
| 在320个CRISPR screen上评估，并报告对照基线 | 320项基准；top100恢复率约提升19%；top500同等命中回收所需库规模减少1.2倍。 | PDF pp.4–5, Results; p.17 | high |
| NK细胞案例有实验验证 | MUC1、PDPN、LRRC15排名升至5、44、659，三者在primary human NK cell tumor-killing assay中被验证。 | PDF pp.7–9, Results; pp.18–19 | high |
| Agent输出在独立T细胞杀伤任务上前瞻测试 | 两项cytotoxic T-cell-killing screens中回收77.1% gold-standard hits，较通用LLM Agent基线提升8%。 | PDF pp.8–9, Results | high |

## 0. 摘要翻译

AutoScreen把功能基因组靶点发现分为预筛选设计和筛后分析：由自由文本构建扰动文库，再融合统计分数和生物学证据重排筛选命中。多个专门 Agent 搜索多模态证据、并行访问数据库并审核靶点。摘要报告320个CRISPR筛选基准、NK/T细胞肿瘤杀伤验证及对500多个公共数据集的再分析。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 当前判断：included；读者建议：included。
全文确认五个专门Agent将自然语言问题转为扰动设计或筛后靶点排序，调用文献/数据库和统计工具并保留来源轨迹；基准任务与NK/T细胞验证说明其在功能基因组靶点发现流程中承担多步科研角色。

### 1.2 排除风险检查

06对应基因组规模CRISPR筛选和基因靶点；07对应白血病、肿瘤免疫逃逸及NK/T细胞治疗应用。不能将一般功能基因组分析误归单纯医学，也不能忽略明确癌症治疗验证。
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

全文Results pp. 4–9, 17–19：320个专家整理CRISPR screen benchmark；top-100命中恢复相对最佳Agent baseline提升约19%，top-500同等回收所需文库小1.2倍，MAP高于随机两个数量级以上。NK leukemia案例中MUC1、PDPN、LRRC15从原排名118、81、1384升至5、44、659；primary human NK tumor-killing实验逐个验证三者。两项前瞻T-cell killing screen恢复77.1% gold-standard hits，超过通用LLM Agent baseline 8%。

### 2.3 容易混淆的边界

06对应基因组规模CRISPR筛选和基因靶点；07对应白血病、肿瘤免疫逃逸及NK/T细胞治疗应用。不能将一般功能基因组分析误归单纯医学，也不能忽略明确癌症治疗验证。

## 3. Agent 系统与科研流程角色

全文确认五个专门Agent将自然语言问题转为扰动设计或筛后靶点排序，调用文献/数据库和统计工具并保留来源轨迹；基准任务与NK/T细胞验证说明其在功能基因组靶点发现流程中承担多步科研角色。

科研流程与自主能力以本文实际行动和工具调用为依据：

全文（Methods pp. 3–6, 11）描述五个专门Agent：Deep Research Agent按研究问题进行多轮文献检索和证据抽取，Evidence Integration Agent构建证据图/排序依据，Target Review Agent复核；预筛模式将自然语言描述转为可测试基因的CRISPR库，筛后模式读取MAGeCK/DESeq2统计量并结合生物上下文重排。Agent检索可调用超过26个数据库；文献和数据来源写入provenance。

## 4. 方法设计

### 4.1 方法动机与设计

将面向功能基因组筛选的科研问题转成扰动设计、候选靶点优先级和可追溯验证链，并以NK/T细胞实验连接发现与治疗应用。

### 4.2 系统流程与组件

全文（Methods pp. 3–6, 11）描述五个专门Agent：Deep Research Agent按研究问题进行多轮文献检索和证据抽取，Evidence Integration Agent构建证据图/排序依据，Target Review Agent复核；预筛模式将自然语言描述转为可测试基因的CRISPR库，筛后模式读取MAGeCK/DESeq2统计量并结合生物上下文重排。Agent检索可调用超过26个数据库；文献和数据来源写入provenance。

## 5. 实验与验证

### 5.1 验证方式、对象及任务

全文Results pp. 4–9, 17–19：320个专家整理CRISPR screen benchmark；top-100命中恢复相对最佳Agent baseline提升约19%，top-500同等回收所需文库小1.2倍，MAP高于随机两个数量级以上。NK leukemia案例中MUC1、PDPN、LRRC15从原排名118、81、1384升至5、44、659；primary human NK tumor-killing实验逐个验证三者。两项前瞻T-cell killing screen恢复77.1% gold-standard hits，超过通用LLM Agent baseline 8%。

### 5.2 基线、指标与结果

全文Results pp. 4–9, 17–19：320个专家整理CRISPR screen benchmark；top-100命中恢复相对最佳Agent baseline提升约19%，top-500同等回收所需文库小1.2倍，MAP高于随机两个数量级以上。NK leukemia案例中MUC1、PDPN、LRRC15从原排名118、81、1384升至5、44、659；primary human NK tumor-killing实验逐个验证三者。两项前瞻T-cell killing screen恢复77.1% gold-standard hits，超过通用LLM Agent baseline 8%。

### 5.3 科学贡献与证据强度

将面向功能基因组筛选的科研问题转成扰动设计、候选靶点优先级和可追溯验证链，并以NK/T细胞实验连接发现与治疗应用。

证据层级：原始全文支持；作者报告结果不等于独立复现。

## 6. 与已有工作的关系

与CRISPR screen分析、Agent协同假设发现及癌症免疫治疗靶点研究相关；本文以生物对象筛选及治疗靶点验证为主。

## 7. 局限性与风险

已审阅bioRxiv v1全文。本文基准和验证集中于特定癌症免疫筛选，效能不能直接外推其他领域；对大规模公开数据资源的抽取/重分析覆盖也不等同于无人工监督的完全自主发现。

## 8. 对综述写作的价值

适合作为 Agent 将基因扰动筛选扩展为可实验验证的肿瘤免疫靶点发现案例。

推荐引用强度：普通引用，可在核对原文后用于相应领域案例。

## 9. 总结

### 9.1 一句话概括

Agent从CRISPR筛选发现机制

### 9.2 速记版 pipeline

全文（Methods pp. 3–6, 11）描述五个专门Agent：Deep Research Agent按研究问题进行多轮文献检索和证据抽取，Evidence Integration Agent构建证据图/排序依据，Target Review Agent复核；预筛模式将自然语言描述转为可测试基因的CRISPR库，筛后模式读取MAGeCK/DESeq2统计量并结合生物上下文重排。Agent检索可调用超过26个数据库；文献和数据来源写入provenance。

### 9.3 标注字段汇总

```text
paper_id=ASD-0894
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

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O3 新实例 | 在320个CRISPR screen基准上评估靶点排序能力；NK/T细胞案例虽有实验验证但核心评测是已知筛选数据上的候选重排 | “320个专家整理CRISPR screen benchmark” · L89 |
| 验证强度 | V3 物理实验 | NK细胞案例中MUC1、PDPN、LRRC15经primary human NK tumor-killing实验验证，T细胞杀伤任务有前瞻测试，覆盖核心科学结论 | “primary human NK tumor-killing实验逐个验证三者” · L89 |
| 系统自主性 | L2 闭环执行者 |  | — |

- 强验证（V3–V4）：是
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
