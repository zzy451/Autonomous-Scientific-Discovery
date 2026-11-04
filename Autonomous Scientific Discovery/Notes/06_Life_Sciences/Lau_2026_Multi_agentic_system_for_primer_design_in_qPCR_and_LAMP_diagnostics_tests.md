# Multi-agentic system for primer design in qPCR and LAMP diagnostics tests

**论文信息**

- ID：ASD-0900
- 标题：Multi-agentic system for primer design in qPCR and LAMP diagnostics tests
- 作者：Kenny J.X. Lau
- 年份：2026
- 来源 / venue：openRxiv (preprint)
- DOI / arXiv / URL：https://doi.org/10.64898/2026.09.15.751771
- 一手阅读来源：https://www.biorxiv.org/content/10.64898/2026.09.15.751771v1.full
- 来源层级：全文
- 阅读版本：对应缓存来源版本，参见Evidence Log
- 阅读版本题名：Multi-agentic system for primer design in qPCR and LAMP diagnostics tests
- 原始全文缓存：C:/Users/20683/Desktop/综述/.tmp_asd_pdfs/source_rescue/primer_pdf.pdf
- PDF / 本地文件路径：Reference_PDF/06_Life_Sciences/Lau_2026_Multi_agentic_system_for_primer_design_in_qPCR_and_LAMP_diagnostics_tests.pdf
- 当前状态：included
- 阅读日期：2026-10-22
- 笔记作者：Codex（读者证据包经主控审核整合）

## Evidence Log

| 判断项 | 结论 / 原文概括 | 证据位置 | 可信度 |
|---|---|---|---|
| 论文身份及版本核验 | 题名 Multi-agentic system for primer design in qPCR and LAMP diagnostics tests；作者Kenny J.X. Lau；DOI 10.64898/2026.09.15.751771；页眉记载bioRxiv版本发表于2026-09-16。PDF签名%PDF-已核验。 | PDF首页 | high |
| 七个专门Agent组成层级流程 | 作者描述qPCR/LAMP双分支及七个specialized sub-agents，从用户指定基因/物种请求和LLM关键词抽取开始。 | PDF Results, “Proposed agentic AI framework for primer design”, pp. 2–3, lines 65–76 | high |
| 第一步进行面向NCBI的序列检索和过滤 | Search Agent标准化16S/ITS或目标基因查询，限定目标物种、排除whole-genome-shotgun记录并为后续比对筛选核酸片段。 | PDF Results, “Optimising search results from NCBI in sub-agent 1: Search Agent”, p. 3, lines 77–96 | high |
| 对外部序列执行多步比对和保守区推断 | Alignment Agent调用EBI Clustal Omega API；Analyst Agent滑窗分析对齐结果，使用长度、简并碱基、>0.7 conservation ratio和GC/Tm规则筛选保守靶区。 | PDF Results, “Aligning short sequences in sub-agent 2”及“Finding consensus region…in sub-agent 3”, pp. 3–4, lines 97–113 | high |
| qPCR与LAMP是不同并行候选设计分支 | Screening/Probe Agent依次组合qPCR引物和TaqMan探针；LAMP Agent按五段距离约束生成六引物组；Report Agent汇总候选并解释Tm、扩增子长度和空间布局。 | PDF Results, “Bifurcation pathways leading to either qPCR or LAMP agents or both”, pp. 4–5, lines 114–142 | high |
| Ganoderma ITS案例输出候选qPCR与LAMP引物 | 正文展示“Design Taqman and LAMP assay for ITS in Ganoderma”；Fig. 2 caption明确图示TaqMan qPCR候选、LAMP候选及选择理由。 | PDF Discussion, pp. 5–6, lines 146–149；Fig. 2 caption, p. 8, lines 211–214 | high |
| Burkholderia recA案例检验微生物序列设计工作流边界 | recA共识区难以满足LAMP全部约束，系统只产出两组qPCR TaqMan候选，没有LAMP候选；该属级序列案例未指定人类病原物种或患者诊断任务。 | PDF Discussion, p. 6, lines 146–149, 169–172；Fig. 3 caption, p. 9, lines 217–219 | high |
| 结果是计算候选设计，不是湿实验性能验证 | 结论称设计并测试软件以识别candidate primers/probes；补充信息提供ITS和recA比对及候选序列。正文所见没有引物合成、扩增实验、敏感度/特异度或患者样本验证。 | PDF Conclusions, p. 7, lines 192–202；Results/Discussion pp. 5–6 | high |
| 方法有可复现入口 | 报告使用GPT-4o或Qwen2.5-1.5B；开源代码和在线应用链接列于结论，支持复核计算工作流。 | PDF Discussion, p. 6, lines 186–189；Conclusions p. 7, lines 192–202 | high |

## 0. 摘要翻译

本文提出面向qPCR和LAMP的多Agent引物/探针设计系统，使用LangGraph、LangChain、Biopython及NCBI/EBI服务串联七个专门Agent：解析用户目标、筛选NCBI序列、Clustal Omega多序列比对、定位保守区，再并行生成qPCR引物/探针或LAMP六引物组合，并汇总候选结果。全文展示Ganoderma ITS和Burkholderia recA案例：前者生成qPCR及LAMP候选，后者仅得到两组TaqMan qPCR候选而无LAMP候选。本文证明的是计算设计与候选产出，不报告湿实验性能验证。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 当前判断：included；读者建议：included。
全文明确展示面向具体微生物基因的七Agent多步系统，先对用户请求解析，再检索NCBI、用Clustal Omega对核酸序列比对、计算保守区并按不同assay分支筛选候选引物；系统给出可下载序列/候选及解释，达到工具使用与领域任务执行的Agent纳入门槛。缺少湿实验不构成排除理由。 主控：摘要已明确专职Agent协调序列获取、比对与引物设计，最低Agent标准原则上可满足；当前待核由全文来源不足驱动，不以无湿实验为排除理由。

### 1.2 排除风险检查

微生物基因（Ganoderma ITS、Burkholderia属recA）是直接计算对象，支持06.02.01微生物学。标题中的diagnostics及作者提及感染诊断用途说明潜在应用，但案例未将Burkholderia具体到人类病原种/感染病诊断，也没有临床样本或患者任务；Ganoderma ITS更不构成人类疾病证据。因此当前只归06，不因诊断措辞加07；如果后续找到全文中明确的病原种诊断实验，再考虑07.01.10医学微生物学或07.02.08感染病学。
完整闭环不是纳入门槛；科研目标、多步行动、至少一项Agent能力及明确科研角色须同时成立。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：06
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：06（仅归档，不替代多模块事实）
- 模块内分类路径：06.02.01
- 分类深度：03/04使用二级；06/07使用固定三级；其余沿用现有树。
- 分类状态：原文证据复核

### 2.2 对象优先判定

正文以真实微生物基因输入展示系统的计算输出。Ganoderma属ITS请求产生TaqMan qPCR候选和LAMP候选；Burkholderia属recA请求因难找到同时满足约束的保守区，返回两组qPCR TaqMan候选、没有LAMP候选。作者还说明不同NCBI检索词和物种序列覆盖度会改变成功率，序列比对及候选引物文件列于补充信息。正文未报告合成引物、扩增实验、灵敏度/特异度或患者样本验证，因此验证层级为计算设计/案例测试。

### 2.3 容易混淆的边界

微生物基因（Ganoderma ITS、Burkholderia属recA）是直接计算对象，支持06.02.01微生物学。标题中的diagnostics及作者提及感染诊断用途说明潜在应用，但案例未将Burkholderia具体到人类病原种/感染病诊断，也没有临床样本或患者任务；Ganoderma ITS更不构成人类疾病证据。因此当前只归06，不因诊断措辞加07；如果后续找到全文中明确的病原种诊断实验，再考虑07.01.10医学微生物学或07.02.08感染病学。

## 3. Agent 系统与科研流程角色

全文明确展示面向具体微生物基因的七Agent多步系统，先对用户请求解析，再检索NCBI、用Clustal Omega对核酸序列比对、计算保守区并按不同assay分支筛选候选引物；系统给出可下载序列/候选及解释，达到工具使用与领域任务执行的Agent纳入门槛。缺少湿实验不构成排除理由。 主控：摘要已明确专职Agent协调序列获取、比对与引物设计，最低Agent标准原则上可满足；当前待核由全文来源不足驱动，不以无湿实验为排除理由。

科研流程与自主能力以本文实际行动和工具调用为依据：

层级系统含七个专门子Agent。用户请求先由LLM抽取organism/gene/目标关键词和参数；Search Agent查询NCBI nucleotide数据库并过滤whole-genome-shotgun、限定短片段；Alignment Agent调用EBI Clustal Omega API做多序列比对；Analyst Agent以20–31 nt滑窗寻找保守序列，去gap后过滤长度<18 nt、N>5的候选，保留保守比例>0.7的区域并计算GC/Tm。之后分支：qPCR Screening Agent找正反向引物，Probe Agent匹配TaqMan探针；LAMP Agent按5段间隔约束组合F3/F2/F1/B1/B2/B3六引物；Report Agent汇总结果。

## 4. 方法设计

### 4.1 方法动机与设计

把核酸数据库检索、序列比对、保守区分析及qPCR/LAMP设计串为可执行的多Agent工作流，并让系统根据序列可用性给出候选或明确失败分支；产物直接面向微生物检测assay设计。

### 4.2 系统流程与组件

层级系统含七个专门子Agent。用户请求先由LLM抽取organism/gene/目标关键词和参数；Search Agent查询NCBI nucleotide数据库并过滤whole-genome-shotgun、限定短片段；Alignment Agent调用EBI Clustal Omega API做多序列比对；Analyst Agent以20–31 nt滑窗寻找保守序列，去gap后过滤长度<18 nt、N>5的候选，保留保守比例>0.7的区域并计算GC/Tm。之后分支：qPCR Screening Agent找正反向引物，Probe Agent匹配TaqMan探针；LAMP Agent按5段间隔约束组合F3/F2/F1/B1/B2/B3六引物；Report Agent汇总结果。

## 5. 实验与验证

### 5.1 验证方式、对象及任务

正文以真实微生物基因输入展示系统的计算输出。Ganoderma属ITS请求产生TaqMan qPCR候选和LAMP候选；Burkholderia属recA请求因难找到同时满足约束的保守区，返回两组qPCR TaqMan候选、没有LAMP候选。作者还说明不同NCBI检索词和物种序列覆盖度会改变成功率，序列比对及候选引物文件列于补充信息。正文未报告合成引物、扩增实验、灵敏度/特异度或患者样本验证，因此验证层级为计算设计/案例测试。

### 5.2 基线、指标与结果

正文以真实微生物基因输入展示系统的计算输出。Ganoderma属ITS请求产生TaqMan qPCR候选和LAMP候选；Burkholderia属recA请求因难找到同时满足约束的保守区，返回两组qPCR TaqMan候选、没有LAMP候选。作者还说明不同NCBI检索词和物种序列覆盖度会改变成功率，序列比对及候选引物文件列于补充信息。正文未报告合成引物、扩增实验、灵敏度/特异度或患者样本验证，因此验证层级为计算设计/案例测试。

### 5.3 科学贡献与证据强度

把核酸数据库检索、序列比对、保守区分析及qPCR/LAMP设计串为可执行的多Agent工作流，并让系统根据序列可用性给出候选或明确失败分支；产物直接面向微生物检测assay设计。

证据层级：原始全文支持；作者报告结果不等于独立复现。

## 6. 与已有工作的关系

与生物信息学分析流程和分子诊断引物设计工具相关；是否超出工作流自动化，需查看全文算法与实验。

## 7. 局限性与风险

候选输出依赖NCBI现有序列的数量和检索词；Burkholderia recA案例无LAMP候选，显示目标序列保守性/约束会限制作业覆盖。本文是bioRxiv预印本，所见证据为计算案例与补充序列，未见湿实验扩增、分析性能或临床样本验证。Ganoderma ITS并未指向人类病原；Burkholderia案例只到属级recA，未指定人类病原物种或感染病诊断场景，因此目前不足以增加07。

## 8. 对综述写作的价值

适合评估分子诊断Agent的最低Agent标准及从生物序列分析到医学诊断的分类阈值。

推荐引用强度：普通引用，可在核对原文后用于相应领域案例。

## 9. 总结

### 9.1 一句话概括

多Agent协作设计微生物引物

### 9.2 速记版 pipeline

层级系统含七个专门子Agent。用户请求先由LLM抽取organism/gene/目标关键词和参数；Search Agent查询NCBI nucleotide数据库并过滤whole-genome-shotgun、限定短片段；Alignment Agent调用EBI Clustal Omega API做多序列比对；Analyst Agent以20–31 nt滑窗寻找保守序列，去gap后过滤长度<18 nt、N>5的候选，保留保守比例>0.7的区域并计算GC/Tm。之后分支：qPCR Screening Agent找正反向引物，Probe Agent匹配TaqMan探针；LAMP Agent按5段间隔约束组合F3/F2/F1/B1/B2/B3六引物；Report Agent汇总结果。

### 9.3 标注字段汇总

```text
paper_id=ASD-0900
inclusion_status=included
scientific_object_modules=06
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=06
module_taxonomy_codes=06.02.01
source_level=fulltext
fulltext_followup_required=false
```

### 全文后续要求

本轮已读原始全文并完成对象分类；无需为纳入/分类另做全文补读。具体引用时仍需回查相应原文位置。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O3 新实例 | 为Ganoderma ITS和Burkholderia recA设计qPCR/LAMP引物候选，答案可由序列比对、Tm和约束条件计算验证 | “Ganoderma属ITS请求产生TaqMan qPCR候选和LAMP候选” · L93 |
| 验证强度 | V1 基准/内部评测 | 展示计算设计输出和候选序列，无湿实验扩增、灵敏度/特异度或患者样本验证 | “正文未报告合成引物、扩增实验、灵敏度/特异度或患者样本验证” · L93 |
| 系统自主性 | L2 闭环执行者 |  | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
