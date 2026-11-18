# Bringing Agentic Search to Earth Observation Data Discovery

**论文信息**

- ID：ASD-0908
- 标题：Bringing Agentic Search to Earth Observation Data Discovery
- 作者：Yu, Minghan; Sun, Youran; Yi, Chugang; Wen, Yixin; Yang, Haizhao
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2607.02387
- 一手阅读来源：https://arxiv.org/abs/2607.02387
- 来源层级：全文
- 阅读版本：对应缓存来源版本，参见Evidence Log
- 阅读版本题名：Bringing Agentic Search to Earth Observation Data Discovery
- 原始全文缓存：C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/.tmp_asd_pdfs/2607_02387.html
- PDF / 本地文件路径：未归档PDF
- 当前状态：included
- 阅读日期：2026-10-22
- 笔记作者：Codex（读者证据包经主控审核整合）

## Evidence Log

| 判断项 | 结论 / 原文概括 | 证据位置 | 可信度 |
|---|---|---|---|
| 目标是帮助地球科学研究者发现数据集和工具。 | 论文以自然语言研究问题作为输入，返回匹配的地球科学数据资源和工具。 | §1 Introduction、§5.1 Problem Formulation | high |
| benchmark基于NASA地球观测知识图谱。 | 全文说明NASA EO-KG派生NASA-EO-Bench，包含47k query-dataset pairs及21k task-based queries。 | §3 Benchmark / §3.1 Data Source and Construction | high |
| 系统采用多阶段检索和重排。 | 方法分为NASA官方工具检索、混合检索和Agentic reranking阶段。 | §5 Method，尤其§5.1 | high |
| Agent使用工具且可进行自主检索。 | 全文描述自主web与arXiv工具使用，并报告其在已有检索流程上增加收益。 | §5.6 Agentic Reranking with Autonomous Tool Use | high |
| 有基线和多项检索指标验证。 | 比较cosine、BM25、微调神经评分与融合/重排方案，指标含Recall@10、MRR等。 | §4 Evaluation Metrics、§6 Experiments | high |
| 版本元数据显示v2对应CIKM 2026会议稿。 | 全文首页标记arXiv:2607.02387v2，CIKM ’26会议出版信息和DOI 10.1145/3799682.3841109。 | 全文首页与arXiv v2标记 | high |

## 0. 摘要翻译

论文提出面向地球科学研究的数据集与工具搜索框架，将自然语言研究问题映射到NASA地球观测数据资源。作者从NASA Earth Observation Knowledge Graph构造NASA-EO-Bench（47k查询—数据集对，含21k任务型查询），并评测神经排序、BM25融合、零样本重排和Agent自主网页/arXiv工具使用。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 当前判断：included；读者建议：included。
面向明确的地球观测科研资料发现目标；流程包括研究查询解析、NASA工具检索、候选排序、Agent重排及自主网页/arXiv工具使用，是科研工作流中的数据/工具发现Agent。

### 1.2 排除风险检查

应归05，因为benchmark对象和返回资源是NASA Earth Observation地球科学数据与工具。可能被误放01信息检索；但IR算法只是方法，任务对象及科研使用场景是地球观测数据发现。若主控将科研数据发现视为通用检索能力而非具体科学任务，需复核Agent边界，分类风险低、角色范围风险中。
完整闭环不是纳入门槛；科研目标、多步行动、至少一项Agent能力及明确科研角色须同时成立。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：05
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：05（仅归档，不替代多模块事实）
- 模块内分类路径：05.04.04
- 分类深度：03/04使用二级；06/07使用固定三级；其余沿用现有树。
- 分类状态：原文证据复核

### 2.2 对象优先判定

- object：NASA地球观测数据集、科学数据检索任务与数据/工具发现
- baselines：cosine similarity、BM25、单独监督神经排序及其融合方案。
- metrics：Recall@10、MRR、MAP及LLM-as-a-Judge Precision@K；报告paired bootstrap等显著性检验。
- results：摘要报告融合检索的Recall@10与MRR超过未适配cosine基线5倍；零样本重排使MRR再升16%；自主web/arXiv使用带来额外收益。

### 2.3 容易混淆的边界

应归05，因为benchmark对象和返回资源是NASA Earth Observation地球科学数据与工具。可能被误放01信息检索；但IR算法只是方法，任务对象及科研使用场景是地球观测数据发现。若主控将科研数据发现视为通用检索能力而非具体科学任务，需复核Agent边界，分类风险低、角色范围风险中。

## 3. Agent 系统与科研流程角色

面向明确的地球观测科研资料发现目标；流程包括研究查询解析、NASA工具检索、候选排序、Agent重排及自主网页/arXiv工具使用，是科研工作流中的数据/工具发现Agent。

科研流程与自主能力以本文实际行动和工具调用为依据：

基于NASA EO知识图谱构建检索评测集；采用词项与任务适配语义评分的混合检索，再由LLM重排。Agent阶段可自主调用网页和arXiv工具补充证据并对候选数据集重排。

## 4. 方法设计

### 4.1 方法动机与设计

提供大规模地球观测科研数据发现benchmark，并展示知识图谱、监督排序与Agent工具检索互补。

### 4.2 系统流程与组件

基于NASA EO知识图谱构建检索评测集；采用词项与任务适配语义评分的混合检索，再由LLM重排。Agent阶段可自主调用网页和arXiv工具补充证据并对候选数据集重排。

## 5. 实验与验证

### 5.1 验证方式、对象及任务

- object：NASA地球观测数据集、科学数据检索任务与数据/工具发现
- baselines：cosine similarity、BM25、单独监督神经排序及其融合方案。
- metrics：Recall@10、MRR、MAP及LLM-as-a-Judge Precision@K；报告paired bootstrap等显著性检验。
- results：摘要报告融合检索的Recall@10与MRR超过未适配cosine基线5倍；零样本重排使MRR再升16%；自主web/arXiv使用带来额外收益。

### 5.2 基线、指标与结果

- object：NASA地球观测数据集、科学数据检索任务与数据/工具发现
- baselines：cosine similarity、BM25、单独监督神经排序及其融合方案。
- metrics：Recall@10、MRR、MAP及LLM-as-a-Judge Precision@K；报告paired bootstrap等显著性检验。
- results：摘要报告融合检索的Recall@10与MRR超过未适配cosine基线5倍；零样本重排使MRR再升16%；自主web/arXiv使用带来额外收益。

### 5.3 科学贡献与证据强度

提供大规模地球观测科研数据发现benchmark，并展示知识图谱、监督排序与Agent工具检索互补。

证据层级：原始全文支持；作者报告结果不等于独立复现。

## 6. 与已有工作的关系

与地理空间数据发现、Earth science LLM和检索增强系统相关；不同于仅在已给定影像/数据层上问答的地球科学benchmark，本文关注检索研究所需的证据资源。

## 7. 局限性与风险

检索到相关数据集不等于找到完整或正确的科学证据；论文讨论流行度偏差、潜在标签泄漏和评测范围/有效性限制。其科研Agent作用集中于数据发现/检索，不负责后续地球科学假说或实地验证。

## 8. 对综述写作的价值

可作为研究Agent前端文献发现/数据获取的地学实例，与端到端科学发现Agent形成角色对比。

推荐引用强度：普通引用，可在核对原文后用于相应领域案例。

## 9. 总结

### 9.1 一句话概括

Agent检索地球观测科研资源

### 9.2 速记版 pipeline

基于NASA EO知识图谱构建检索评测集；采用词项与任务适配语义评分的混合检索，再由LLM重排。Agent阶段可自主调用网页和arXiv工具补充证据并对候选数据集重排。

### 9.3 标注字段汇总

```text
paper_id=ASD-0908
inclusion_status=included
scientific_object_modules=05
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=05
module_taxonomy_codes=05.04.04
source_level=fulltext
fulltext_followup_required=false
```

### 全文后续要求

本轮已读原始全文并完成对象分类；无需为纳入/分类另做全文补读。具体引用时仍需回查相应原文位置。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O2 既定基准 | 在NASA-EO-Bench（47k查询-数据集对）上评测数据发现检索系统，属预定义基准 | “从NASA Earth Observation Knowledge Graph构造NASA-EO-Bench” · L34 |
| 验证强度 | V1 基准/内部评测 | 报告Recall@10、MRR、MAP等检索指标，与baseline比较 | “融合检索的Recall@10与MRR超过未适配cosine基线5倍” · L96 |
| 系统自主性 | L1 任务助手 |  | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
