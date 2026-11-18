# An immune world model for multiscale forecasting and therapeutic hypothesis generation

**论文信息**

- ID：ASD-0967
- 标题：An immune world model for multiscale forecasting and therapeutic hypothesis generation
- 作者：Cui, Taoyong; Wang, Xi; Li, Zonghang; Ding, Jinchao; You, Lingsen; Xu, Yuzhi; Xu, Wanghan; Wu, Fang; Ying, Kejun; Ouyang, Wanli; Heng, Pheng Ann; Yang, Ling; Yin, Zhenfei; Wu, Yingcheng
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2609.14709
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0967.txt
- PDF / 本地文件路径：Reference_PDF/06_Life_Sciences/Taoyong_2026_An_immune_world_model_for_multiscale_forecasting_and_therapeutic_ASD0967.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 科学对象 | 对象是跨细胞、组织和个体尺度的免疫状态预测及干预假设。 | 本地原文 TXT 第246行；核验TXT行号 246 | Immune therapies act across cell-intrinsic programs, tissue ecosystems, and patient-specific immune states, yet most predictors address these scales separately. We used a governed evolutionary AI Scientist to construct the Immune World Model, an action-conditioned model that learns how interventions move immune states across cellular, tissue, and individual levels. The Immune World Model–building Scientist searched candidate architectures and workflows, and the resulting world model was frozen before independent confirmation. The frozen model generalized to unseen interventions and biological contexts, recovered intervention-specific cellular programs, integrated cell and tissue information to improve ecosystem and patient-response prediction, and forecast unseen perturbation combinations. Immune World Model–guided analysis then combined measured perturbations with cross-axis inference to nominate IL-36γ\gamma plus SIRPα\alpha inhibition as a complementary-axis therapeutic hypothesis, whereas a governed self-correction audit rejected every screened cytokine pair. The Immune World Model provides a framework for multiscale immune simulation that connects AI Scientist-driven model construction, intervention forecasting, and the generation of prospectively testable therapeutic hypotheses. | 高（一手正文；非独立复现） |
| 研究方法与Agent行动 | 受治理的AI Scientist演化候选模型与工作流，模型冻结后进入独立确认。 | 本地原文 TXT 第297行；核验TXT行号 297 | AI Scientist systems can organize evidence, select analytical tools, execute computational analyses, and evaluate intermediate results,12, 14 and language-model agents have been applied to laboratory planning, automation, and prospective molecular design.6, 41 We used Agent Genesis, a governed evolutionary AI Scientist, to construct the Immune World Model by evolving candidate Scientist workflows and immune-world-model configurations under versioned data manifests and prespecified evaluation gates. Here, Agent Genesis denotes the governed development framework, the Immune World Model denotes the learned biological model, and the Immune World Model Research Scientist denotes the fixed post-freeze workflow. The resulting Immune World Model configuration was frozen before independent confirmation and then evaluated on withheld interventions and contexts, cross-scale World Model Rollout, and action composition. Immune World Model–guided analysis further identified complementary immune axes and prioritized IL-36γ\gamma plus SIRPα\alpha inhibition as a therapeutic hypothesis for prospective experimental evaluation. | 高（一手正文；非独立复现） |
| 实验任务与验证 | 模型将细胞、组织和个体背景整合为状态，并将干预编码为动作。 | 本地原文 TXT 第325行；核验TXT行号 325 | Within this architecture, multiscale immune data, perturbation and intervention data, patient-derived data with clinical annotations, and prior knowledge enter a structured encoder (Figure 1B). Cellular state ZcellZ_{\mathrm{cell}}, tissue immune context ZtmeZ_{\mathrm{tme}}, and individual context ZpatientZ_{\mathrm{patient}} are combined into the structured state StS_{t}, while the intervention under evaluation is encoded independently as AtA_{t}. Treatment information within the individual context denotes baseline or prior treatment history rather than the action being predicted. The state and action jointly parameterize the transition | 高（一手正文；非独立复现） |
| 主要结果 | 作者通过能力评估和消融比较结构解码器、动作动态等组件的作用。 | 本地原文 TXT 第374行；核验TXT行号 374 | To determine which components were required for this multiscale transition model, we evaluated seven capabilities and performed complementary module- and representation-level ablations (Figures 1C–1E). The capability analysis covered gene-program fidelity, cellular state, tissue context, individual response, action-conditioned dynamics, cross-context transfer, and mechanistic or counterfactual analysis. Comparator models addressed different subsets of these tasks, with scFoundation providing a pretrained single-cell representation reference.17 Omitting the structured decoder produced a 0.14 loss in composite score, and omitting action-conditioned dynamics produced a 0.10 loss. Substitution of the action representation, multiscale encoder, or immune-adapted cell encoder lowered the score by 0.07, 0.08, and 0.06, respectively. At the representation level, the structured orthogonal state reached 0.748 balanced accuracy on the held-out rheumatoid arthritis (RA) out-of-distribution (OOD) task, versus 0.616, 0.586, and 0.521 for progressively less structured alternatives. The gated residual action model reached an unseen-context Δ​cos\Delta\cos score of 0.388, compared with 0.369 for an orthogonal residual, 0.296 for a context mean, and 0.248 for a raw action vector. Together, these ablations identified distinct contributions from state organization, action encoding, and biological decoding. | 高（一手正文；非独立复现） |
| 研究贡献或边界 | 治疗假设由实测扰动与模型推断共同产生，文中明确其为候选假设。 | 本地原文 TXT 第523行；核验TXT行号 523 | To move from forecasting to hypothesis generation, we combined measured perturbations with model inference to identify complementary immune axes as candidate therapeutic hypotheses. In the surface-knockout screen, CD47 was among the strongest druggable shifts toward a hot or inflamed state (Figure 4A). CD47 is an established self-recognition signal whose blockade can promote tumor-cell phagocytosis and link myeloid uptake to adaptive antitumor responses.30, 47, 21, 44, 2 CD47 knockout supplied evidence for the innate-checkpoint arm; because SIRPα\alpha is the cognate inhibitory receptor of CD47, SIRPα\alpha inhibition served as the therapeutic counterpart of that perturbation. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

作者使用受治理的演化式AI Scientist构建免疫世界模型，用于个体背景下的免疫状态预测及治疗假设生成。系统迭代选择分析工作流，整合多种免疫数据并以留出情境、扰动和独立数据评估。研究对象同时包含免疫细胞/组织系统与疾病患者反应。结果支持跨数据集预测并提出免疫靶点假设，但并非治疗实验验证。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。研究对象是细胞内程序、组织生态环境和个体免疫状态之间的预测与干预关系。
  - 原文位置：TXT 第246行；原文引文；核验TXT行号 246；引文：Immune therapies act across cell-intrinsic programs, tissue ecosystems, and patient-specific immune states, yet most predictors address these scales separately.
- 多步行动过程：yes。Agent Genesis在版本化数据清单和预设评估门下演化候选Scientist工作流及免疫世界模型配置。
  - 原文位置：TXT 第297行；原文引文；核验TXT行号 297；引文：We used Agent Genesis, a governed evolutionary AI Scientist, to construct the Immune World Model by evolving candidate Scientist workflows and immune-world-model configurations under versioned data manifests and prespecified evalu
- 至少一种Agent能力：yes。系统搜索并比较候选工作流和模型配置，再冻结选定模型以供独立确认。
  - 原文位置：TXT 第297行；原文引文；核验TXT行号 297；引文：evolving candidate Scientist workflows and immune-world-model configurations under versioned data manifests and prespecified evaluation gates.
- 明确科研流程角色：yes。固定后的模型用于预测未见干预和生物背景，并支持治疗假设生成。
  - 原文位置：TXT 第246行；原文引文；核验TXT行号 246；引文：the resulting world model was frozen before independent confirmation. The frozen model generalized to unseen interventions and biological contexts, recovered intervention-specific cellular programs, integrated cell and tissue info

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：06;07
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：06（仅归档，不覆盖其他模块）
- 模块内分类路径：06.03.04 单细胞生物学；07.04.01 药物发现
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

- Immune-cell programs and states, tissue ecosystems, patient response, perturbation combinations, and IL-36?/SIRP? inhibition hypothesis.

### 2.3 容易混淆的边界

06.03.04支持免疫细胞及组织层级对象；07.04.01由疾病患者响应和治疗假设支持。跨模块应分别保留细胞机制与疾病情境证据。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

多Agent/科研工作流Agent

### 3.2 科研流程角色

科学问题提出；实验设计；工具调用与代码执行；结果分析与验证

Agent Genesis通过治理的工作流搜索生成免疫分析系统；Scientist工作流选择建模方法，工具执行数据分析，评估阶段比较预测及扰动假设。

### 3.3 自主能力

系统搜索并比较候选工作流和模型配置，再冻结选定模型以供独立确认。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

科学贡献是统一免疫数据预测并提出可检验治疗候选；系统贡献是演化式选择和运行Agent工作流。

### 4.2 系统流程与组件

输入包括免疫细胞状态、疾病队列和扰动数据；系统选择/组合细胞状态表示、响应预测及上下文条件；在留出供体或疾病情境评估；将表面蛋白敲除、细胞因子交互和肿瘤表达分析用于治疗候选排序。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

多疾病/年龄背景数据、扰动及肿瘤表达数据；报告个体情境预测，并用匹配评估单元避免重复样本。属于回顾性计算验证。

### 5.2 基线、指标与结果

作者报告多个疾病和疫苗响应数据集支持个体上下文预测，并从免疫扰动及表达数据提出治疗假设；没有临床干预试验。

### 5.3 科学贡献与证据强度

科学贡献是统一免疫数据预测并提出可检验治疗候选；系统贡献是演化式选择和运行Agent工作流。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

面向跨模态免疫预测，区别于仅在单一数据集训练的细胞响应模型；与单细胞建模、免疫系统生物学及计算药物假设生成相关。

## 7. 局限性与风险

候选假设尚未实验或临床验证；跨数据集的测量差异与评估切分可能影响外推；不得把论文结果写成疗效证据。

## 8. 对综述写作的价值

可支撑免疫学Agent跨尺度预测与疾病治疗假设生成的案例，并展示计算候选到实验验证之间的证据断层。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

演化式科研Agent构建免疫世界模型并生成疾病情境治疗假设。

### 9.2 速记版 pipeline

输入包括免疫细胞状态、疾病队列和扰动数据；系统选择/组合细胞状态表示、响应预测及上下文条件；在留出供体或疾病情境评估；将表面蛋白敲除、细胞因子交互和肿瘤表达分析用于治疗候选排序。

### 9.3 标注字段汇总

```text
paper_id=ASD-0967
inclusion_status=to_read
scientific_object_modules=06;07
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=06
module_taxonomy_codes=06.03.04;07.04.01
source_level=first_hand_full_text
fulltext_followup_required=true
```

### 全文后续要求

当前纳入和分类证据已足够；第7节明确的结果/复现细节仍需继续回查。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O3 新实例 | 免疫状态预测在留出数据集上可计算检验 | “多疾病/年龄背景数据、扰动及肿瘤表达数据；报告个体情境预测” · L101 |
| 验证强度 | V2 计算/仿真/回顾性 | 回顾性计算验证和留出数据评估，无临床试验 | “并用匹配评估单元避免重复样本。属于回顾性计算验证” · L101 |
| 系统自主性 | L2 闭环执行者 | AI Scientist演化模型架构并自主验证假设 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
