# Large Knowledge Model: A Knowledge Foundation for Agentic Science at Scale

**论文信息**

- ID：ASD-0873
- 标题：Large Knowledge Model: A Knowledge Foundation for Agentic Science at Scale
- 作者：Huang, Yuan; Hu, Sihan; Gu, Hongyu; Ma, Chao; Zhang, Jiaxing; Zou, Zhiyong; Fan, Caiyu; Xiao, Yan; Xu, Mingjun; Xie, Chenyu; Ju, Mingzhen; Ma, Zhehao; Zhang, Qi; Wang, Baozong; Li, Yu; Yao, Zhiyuan; Liao, Ruoxue; Li, Xinyu; Zhang, Linfeng; Chen, Kun; E, Weinan
- 年份：2026
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2609.27297
- 一手阅读来源：https://arxiv.org/abs/2609.27297
- 来源层级：全文
- 阅读版本：对应缓存来源版本，参见Evidence Log
- 阅读版本题名：Large Knowledge Model: A Knowledge Foundation for Agentic Science at Scale
- 原始全文缓存：C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/.tmp_asd_pdfs/2609.27297.html
- PDF / 本地文件路径：未归档PDF
- 当前状态：included
- 阅读日期：2026-10-22
- 笔记作者：Codex（读者证据包经主控审核整合）

## Evidence Log

| 判断项 | 结论 / 原文概括 | 证据位置 | 可信度 |
|---|---|---|---|
| 科学主张以证据和推理关系表示。 | LKM将主张及支持材料编码为来源可追踪的图对象。 | 全文§1–3 | high |
| 系统保持跨论文对象身份。 | 规范化身份连接重复主张并允许知识基础增量扩展。 | 全文§3.3 | high |
| SciFact-Open用于证据发现。 | 279条主张及460个人工标注正向证据对。 | 全文§5.1 | high |
| 答案流程含多步Agent反馈。 | 明确描述检索、重排、起草、自反馈和引文修复。 | 全文§5.2 | high |
| 科学问答基准测检索效用。 | 固定答题模型分别在ChemBench、PubMedQA、SciBench与无检索比较。 | 全文§5.3 | high |
| 抽取误差有限审计。 | 100篇审计报告0.97% hallucination，但没有测量遗漏。 | 全文Limitations | medium |

## 0. 摘要翻译

论文提出面向多学科科学文献的Large Knowledge Model（LKM），把主张、证据、前提和推理链表示为可追踪图对象，并提供科学检索服务。全文§5.2进一步展示Agent多步执行检索、重排、起草、自我反馈和引文修复。评测覆盖证据发现、引文支持及ChemBench、PubMedQA、SciBench知识问答。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 当前判断：included；读者建议：included。
全文§5.2明确描述Agent执行检索、重排、答案起草、自我反馈与引文修复的多步循环；工具使用与反馈迭代满足Agent最低门槛。

### 1.2 排除风险检查

主模块建议11.07：论文直接构造并检索科学主张、证据及推理链。ChemBench的化学知识任务支持03.01，PubMedQA的医学问答支持07.03.08；不能从PubMedQA推出06。01.04不适用，因为存在科学知识对象级实验。
完整闭环不是纳入门槛；科研目标、多步行动、至少一项Agent能力及明确科研角色须同时成立。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：11;03;07
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：11（仅归档，不替代多模块事实）
- 模块内分类路径：11.07; 03.01; 07.03.08
- 分类深度：03/04使用二级；06/07使用固定三级；其余沿用现有树。
- 分类状态：原文证据复核

### 2.2 对象优先判定

SciFact-Open证据发现；ScholarQABench引文支持；固定答题模型在ChemBench、PubMedQA和SciBench上与无检索对照。作者另抽审100篇文献，报告抽取幻觉率0.97%，未审计漏抽。

### 2.3 容易混淆的边界

主模块建议11.07：论文直接构造并检索科学主张、证据及推理链。ChemBench的化学知识任务支持03.01，PubMedQA的医学问答支持07.03.08；不能从PubMedQA推出06。01.04不适用，因为存在科学知识对象级实验。

## 3. Agent 系统与科研流程角色

全文§5.2明确描述Agent执行检索、重排、答案起草、自我反馈与引文修复的多步循环；工具使用与反馈迭代满足Agent最低门槛。

科研流程与自主能力以本文实际行动和工具调用为依据：

全文§5.2描述检索、重排、起草、自我反馈及引文修复循环；系统将科学文献抽取为主张—证据—推理图，并提供跨论文检索。

## 4. 方法设计

### 4.1 方法动机与设计

把科学论文表示为可追溯、可链接且可增量更新的论证对象，为研究Agent提供证据记忆与检索基础。

### 4.2 系统流程与组件

全文§5.2描述检索、重排、起草、自我反馈及引文修复循环；系统将科学文献抽取为主张—证据—推理图，并提供跨论文检索。

## 5. 实验与验证

### 5.1 验证方式、对象及任务

SciFact-Open证据发现；ScholarQABench引文支持；固定答题模型在ChemBench、PubMedQA和SciBench上与无检索对照。作者另抽审100篇文献，报告抽取幻觉率0.97%，未审计漏抽。

### 5.2 基线、指标与结果

SciFact-Open证据发现；ScholarQABench引文支持；固定答题模型在ChemBench、PubMedQA和SciBench上与无检索对照。作者另抽审100篇文献，报告抽取幻觉率0.97%，未审计漏抽。

### 5.3 科学贡献与证据强度

把科学论文表示为可追溯、可链接且可增量更新的论证对象，为研究Agent提供证据记忆与检索基础。

证据层级：原始全文支持；作者报告结果不等于独立复现。

## 6. 与已有工作的关系

与科学文献检索、claim verification、RAG问答及科学知识图谱相关；贡献重点是推理链与来源追踪。

## 7. 局限性与风险

语言模型漏抽未被量化；图表公式证据可能不完整；同义改写可能保持为不同身份；基准评测尚不能代表完整自主科研。

## 8. 对综述写作的价值

适合讨论Agent记忆/检索基础设施的纳入边界，并检验11.07与01.04的区分。

推荐引用强度：普通引用，可在核对原文后用于相应领域案例。

## 9. 总结

### 9.1 一句话概括

用可追溯知识图支持科学证据检索与写作

### 9.2 速记版 pipeline

全文§5.2描述检索、重排、起草、自我反馈及引文修复循环；系统将科学文献抽取为主张—证据—推理图，并提供跨论文检索。

### 9.3 标注字段汇总

```text
paper_id=ASD-0873
inclusion_status=included
scientific_object_modules=11;03;07
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=11
module_taxonomy_codes=11.07; 03.01; 07.03.08
source_level=fulltext
fulltext_followup_required=false
```

### 全文后续要求

本轮已读原始全文并完成对象分类；无需为纳入/分类另做全文补读。具体引用时仍需回查相应原文位置。


## 2026-10-29 三级分类复核

- 归档分类：`11.07.03` 科学知识网络；二级：`11.07`。
- 原文位置：PDF p.8。
- 判定：论文之间的主张—证据—矛盾链接构成科学知识网络，且有SciFact及检索评估。
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
