# A Society of Researchers: Designing Institutions for Populations of Autonomous Research Agents

## 当前分类（2026-11-01 实证复核）

- 当前纳入状态：`to_read`；主归档：`11`。
- 本块为当前有效结论；后文既有分类、来源限制与审计判断均保留为历史记录，与本块不一致者由本块取代。
- 当前对象模块：`01;11`。
- 代表分类每个模块保留一个落点，不表示穷尽全文全部细类。

| 模块 | 二级 | 三级 | 本轮结论 |
|---|---|---|---|
| 01 | 01.02 计算机科学 | 01.02.13 机器学习 | 已落地 |
| 11 | 11.07 科学系统与知识生产研究 | 11.07.04 科研共同体结构 | 已落地 |

- 模块01：语言模型预训练生长三种子对照；复现争议不取消对象覆盖。
  - 证据：PDF 第 [3, 4] 页；原文：17% lower perplexity (lower is better) than the same model trained from scratch

- 完整裁决：`Coverage_Check/classification_recheck_2026-11-01/`。

## 既有笔记与历史审计记录

**论文信息**

- ID：ASD-1100
- 标题：A Society of Researchers: Designing Institutions for Populations of Autonomous Research Agents
- 作者：Ali Asaria; Deep Gandhi; Tony Salomone
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2610.10468
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1100.txt
- PDF / 本地文件路径：Reference_PDF/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Asaria_2026_A_Society_of_Researchers_Designing_Institutions_for_Populations_of_ASD1100.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 实际运行规模及研究任务 | 运行社会包含10,000名研究者，围绕语言模型预训练改善展开；约30%计算节省仍存在实验室间分歧。 | 全文第196行；核验TXT行号 196 | In a running society of ten thousand researchers, asked only to improve the pretraining of language models, one lab reported a way to reach the same quality with about 30% less compute, a result the labs that tested it do not yet agree on. | 高（一手正文；非独立复现） |
| 科研流程闭环 | 作者将自动研究闭环描述为提问、资源分配、执行和评估。 | 全文第541行；核验TXT行号 541 | Automated research is a loop of four steps: propose a question, allocate resources, execute, and evaluate. | 高（一手正文；非独立复现） |
| 科研制度与治理 | PI通过项目申请、独立评审和资助竞争计算资源，人类治理者分配资源但不指定任务。 | 全文第196行；核验TXT行号 196 | Principal investigators compete for compute through requests for proposals, independent review, and grants; | 高（一手正文；非独立复现） |
| 科研对象 | 城市获得的初始研究方向是改善语言模型预训练，不提供预先指定的方法或假设。 | 全文第470行；核验TXT行号 470 | The mayor seeded the city with one direction: improve the pretraining of language models. | 高（一手正文；非独立复现） |
| 结果限制 | 结果需保留作者所述的不一致，不能将单个实验室结果写成稳健共识。 | 全文第196行；核验TXT行号 196 | one lab reported a way to reach the same quality with about 30% less compute, a result the labs that tested it do not yet agree on. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

本文提出并实际运行由一万名持久化研究代理组成的科研社会，研究共享计算资源下如何组织代理研究者。制度包含PI提交项目申请、独立评审、资助竞争及人类市长配置计算资源；运行任务聚焦改善语言模型预训练。一个实验室报告以约30%更少计算达到相同质量，但其他实验室对该结果尚未达成一致。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。代理社会以改善语言模型预训练为明确研究目标，并在实验室中报告计算效率结果。
  - 原文位置：全文第196行；核验TXT行号 196；引文：In a running society of ten thousand researchers, asked only to improve the pretraining of language models, one lab reported a way to reach the same quality with about 30% less compute, a result the labs that tested it do not yet agree on.
- 多步行动过程：yes。研究组织包括提出问题、资源申请、独立审查、拨款、实验执行和结果回报的多阶段闭环。
  - 原文位置：全文第541行；核验TXT行号 541；引文：C6. Governing a loop that improves its own institutions. Automated research is a loop of four steps: propose a question, allocate resources, execute, and evaluate. A society automates proposing and allocating, so with execution and evaluation automated the loop closes through the conference cycle of Section 3. When calls ask the society for better researchers, judges, or tools, the loop becomes the recursive self-improvement long anticipated in the literature (Good, 1965; Clune, 2019), applied to an institution. Our deployment has not run such a call, and we do not claim it would succeed. A society can rewrite text as easily as anything else, so calls, invitations, and review are within its reach; it cannot change the size of the pool. The pool of compute is therefore the one non-textual lever, and the natural point of human control. Some institution must decide the pace, beneficiaries, and cost of a self-improving loop, and it should be explicit and inspectable, unlike the organization the agents in the July incident improvised.
- 至少一种Agent能力：yes。持久化研究代理组成实验室、提出和执行项目；人类市长负责资源分配，不代替代理完成研究任务。
  - 原文位置：全文第196行；核验TXT行号 196；引文：Principal investigators compete for compute through requests for proposals, independent review, and grants; a human governor, the mayor, allocates resources and assigns no tasks.
- 明确科研流程角色：yes。系统直接组织科研项目与研究共同体，并在语言模型预训练任务上运行，覆盖科研管理和实际研究执行。
  - 原文位置：全文第470行；核验TXT行号 470；引文：The mayor seeded the city with one direction: improve the pretraining of language models. The call named no technique and no hypothesis.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：01;11
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：11（仅归档，不覆盖其他模块）
- 模块内分类路径：01.02.12 人工智能；11.07.04 科研共同体结构；11.07.05 科学政策与科研管理
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

- 语言模型预训练方法与计算效率
- 大规模科研共同体、科研项目评审、资助和计算资源配置制度

### 2.3 容易混淆的边界

贡献包括科研代理群体的制度设计，以及围绕语言模型预训练改善的实际运行研究。前者涉及科研共同体结构和科研管理，后者提供AI/机器学习对象上的实验案例；因此同时支持11.07.04/11.07.05与01.02.12。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签



### 3.2 科研流程角色



研究代理在实验室结构中提出和执行研究方向，制度层负责征集问题、同行评审、分配经费/算力和汇集结果；人类市长负责资源配置但不替代理指定具体研究方法。运行示例从改善语言模型预训练这一宽泛目标出发，代理实验室通过文献研究收敛到模型growth方案。

### 3.3 自主能力

持久化研究代理组成实验室、提出和执行项目；人类市长负责资源分配，不代替代理完成研究任务。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

贡献包括科研代理群体的制度设计，以及围绕语言模型预训练改善的实际运行研究。前者涉及科研共同体结构和科研管理，后者提供AI/机器学习对象上的实验案例；因此同时支持11.07.04/11.07.05与01.02.12。

### 4.2 系统流程与组件

研究代理在实验室结构中提出和执行研究方向，制度层负责征集问题、同行评审、分配经费/算力和汇集结果；人类市长负责资源配置但不替代理指定具体研究方法。运行示例从改善语言模型预训练这一宽泛目标出发，代理实验室通过文献研究收敛到模型growth方案。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

实际部署一万人研究者社会，跟踪项目申请、独立评审、资助和实验室研究；预训练growth案例由实验室开展并报告计算效率结果，作者同时记录结果分歧。

### 5.2 基线、指标与结果

一万人研究者社会围绕语言模型预训练改善运行。实验室提出从较小已训练模型扩展模型的growth方法；一个实验室报告相同质量下计算量约减少30%，作者明确说明测试该方案的实验室对结果仍有分歧，故该数字应作为初步且存在争议的案例结果。

### 5.3 科学贡献与证据强度

贡献包括科研代理群体的制度设计，以及围绕语言模型预训练改善的实际运行研究。前者涉及科研共同体结构和科研管理，后者提供AI/机器学习对象上的实验案例；因此同时支持11.07.04/11.07.05与01.02.12。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

本文把多Agent科研从单项目协作扩展到资源受限的科研社会，结合科研资助、评审与代理实验室运行；预训练growth项目提供实际研究案例。

## 7. 局限性与风险

约30%计算节省是实验室报告且存在实验室间分歧；制度运行样例不能证明所有组织机制长期有效，也不应把争议结果概括为已确证结论。

## 8. 对综述写作的价值

可支持综述讨论大规模科研Agent组织、资源治理与实际机器学习研究案例。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

本文提出并实际运行由一万名持久化研究代理组成的科研社会，研究共享计算资源下如何组织代理研究者。制度包含PI提交项目申请、独立评审、资助竞争及人类市长配置计算资源；运行任务聚焦改善语言模型预训练。一个实验室报告以约30%更少计算达到相同质量，但其他实验室对该结果尚未达成一致。

### 9.2 速记版 pipeline

研究代理在实验室结构中提出和执行研究方向，制度层负责征集问题、同行评审、分配经费/算力和汇集结果；人类市长负责资源配置但不替代理指定具体研究方法。运行示例从改善语言模型预训练这一宽泛目标出发，代理实验室通过文献研究收敛到模型growth方案。

### 9.3 标注字段汇总

```text
paper_id=ASD-1100
inclusion_status=to_read
scientific_object_modules=01;11
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=11
module_taxonomy_codes=01.02.12;11.07.04;11.07.05
source_level=first_hand_full_text
fulltext_followup_required=true
```

### 全文后续要求

当前纳入和分类证据已足够；第7节明确的结果/复现细节仍需继续回查。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O5 开放数学 | 预训练改进目标事先未知需计算验证 | “improve the pretraining of language models” · L61 |
| 验证强度 | V2 计算/仿真/回顾性 | 实验室报告结果但存在分歧 | “a result the labs that tested it do not yet agree on” · L55 |
| 系统自主性 | L3 自主研究者 | PI自主提出研究问题并推动实验 | — |

- 强验证（V3–V4）：否
- 置信度：low；需全文复核：是；争议记录：无
- 复核状态：待专家复核：低置信度；需全文复核
