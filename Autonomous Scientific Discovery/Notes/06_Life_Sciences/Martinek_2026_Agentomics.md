# Agentomics: an agentic system that autonomously develops novel state-of-the-art solutions for biomedical machine learning tasks

## 当前分类（2026-11-01 实证复核）

- 当前纳入状态：`included`；主归档：`06`。
- 本块为当前有效结论；后文既有分类、来源限制与审计判断均保留为历史记录，与本块不一致者由本块取代。
- 当前对象模块：`03;06;07`。
- 代表分类每个模块保留一个落点，不表示穷尽全文全部细类。

| 模块 | 二级 | 三级 | 本轮结论 |
|---|---|---|---|
| 03 | 03.04 分子设计与化学空间探索 | 03.04.02 小分子性质优化 | 已落地 |
| 06 | 06.01 生物学基础 | 06.01.13 计算生物学 | 已落地 |
| 07 | 07.04 药学与生物医药 | 07.04.01 药物发现 | 已落地 |

- 模块03：表2实际小分子性质预测指标。
  - 证据：PDF 第 [6] 页；原文：Predict compound solubility from SMILES using standardised ADME protocols.

- 完整裁决：`Coverage_Check/classification_recheck_2026-11-01/`。

## 既有笔记与历史审计记录

**论文信息**

- ID：ASD-0893
- 标题：Agentomics: an agentic system that autonomously develops novel state-of-the-art solutions for biomedical machine learning tasks
- 作者：Vlastimil Martinek; Andrea Gariboldi; Dimosthenis Tzimotoudis; Mark Galea; Elissavet Zacharopoulou; Aitor Alberdi Escudero; Edward Blake; David Čechák; Luke Cassar; Alessandro Balestrucci; Panagiotis Alexiou
- 年份：2026
- 来源 / venue：Bioinformatics (Oxford, England)
- DOI / arXiv / URL：https://doi.org/10.1093/bioinformatics/btag250
- 一手阅读来源：https://www.biorxiv.org/content/biorxiv/early/2026/01/30/2026.01.27.702049.full.pdf
- 来源层级：全文
- 阅读版本：bioRxiv v1 submitted preprint, posted 2026-01-30; DOI 10.64898/2026.01.27.702049, accepted-version location linked by OpenAlex to the Bioinformatics publication DOI.
- 阅读版本题名：Agentomics: an agentic system that autonomously develops novel state-of-the-art solutions for biomedical machine learning tasks
- 原始全文缓存：C:/Users/20683/Desktop/综述/.tmp_asd_pdfs/source_rescue/0893_biorxiv_pdf.pdf
- PDF / 本地文件路径：Reference_PDF/06_Life_Sciences/Martinek_2026_Agentomics.pdf
- 当前状态：included
- 阅读日期：2026-10-22
- 笔记作者：Codex（读者证据包经主控审核整合）

## Evidence Log

| 判断项 | 结论 / 原文概括 | 证据位置 | 可信度 |
|---|---|---|---|
| 身份与来源版本 | 题名Agentomics: An Agentic System that Autonomously Develops Novel State-of-the-art Solutions for Biomedical Machine Learning Tasks，DOI 10.64898/2026.01.27.702049，版本日期2026-01-30；该submitted/accepted manuscript与Bioinformatics DOI 10.1093/bioinformatics/btag250同题，OpenAlex将其作为该期刊记录的accepted version。 | bioRxiv PDF首页 | high |
| Agent工具环境和执行动作 | Agent可使用bash、Python write/run、文件编辑、foundation-model信息及final-result工具访问共享环境；每个实验步骤由独立LLM Agent执行，并可多次探查数据、写代码、运行脚本及观察结果。 | PDF pp. 3–4, “Tools”及“Predefined Steps” | high |
| 明确七步机器学习实验管线 | 逐步执行Data Exploration、Data Splitting、Data Representation、Model Architecture、Training、Inference、Prediction Exploration；每步结构化输出供后续步骤使用。 | PDF pp. 4–5, “Predefined Steps” | high |
| 步骤输出经结构与功能检查并可反馈重试 | JSON输出与各步骤专属功能检查均通过后才继续；失败时错误反馈给Agent并重提，超过retry limit则重启；训练和推理脚本还以不同数据子集运行测试。 | PDF pp. 3–5, Fig. 1说明及Predefined Steps | high |
| 迭代实验、模型选择并隔离测试集 | 每轮产出模型、训练/验证指标和Iteration Summary，Experiment Design LLM用过往摘要制定下一轮指令；按验证分数选输出模型，测试集始终对Agent隐藏并在完成后计算测试指标。 | PDF pp. 5–6, “Iterative Experimentation and Model Selection”及“Evaluation” | high |
| 评测样本、重复数、运行预算与基线 | 20个基准按Protein Engineering N=6、Drug Discovery N=9、Regulatory Genomics N=5划分；每数据集三次、每次8小时，固定GPT-5.1-Codex-Max；与Agent基线和人类leaderboard比较。 | PDF p. 5, “Evaluation” | high |
| 具体蛋白工程对象 | 测试包括SARS-CoV-2 spike RBD ACE2结合适应度、Staphylococcus aureus protein A稳定性、多种人/鼠蛋白多突变或indel稳定性、Shewanella MtrA适应度及光系统I亚基蛋白稳定性。 | PDF Table 2, pp. 6–7 | high |
| 药物发现确有小分子/药理性质对象 | 9项任务涵盖EGFR野生型抑制剂、SMILES预测肝微粒体清除、血浆蛋白结合、溶解度、CYP2D6底物、logP、hERG阻断、BBB穿透和Caco-2肠通透性，支持07药物发现及03.04小分子性质对象。 | PDF Table 2, p. 7 | high |
| 真实专家基准的领域结果 | 对照人类SOTA时Protein Engineering为6/6新SOTA，Drug Discovery为2/9，Regulatory Genomics为4/5持平或超越；严格超过为11/20，另有1项持平。平均leaderboard百分位75.92、34.29、63.85。 | PDF Table 1 p. 5；Table 2 pp. 6–7；Results pp. 5–8 | high |
| 外推与方法边界 | 作者讨论不同领域表现差异及系统局限；药物发现运行测试性能早期停滞且最佳验证迭代不总是最佳测试迭代。结论限定于所用数据集、运行时限和模型配置。 | PDF Discussion, pp. 8–9 | high |

## 0. 摘要翻译

全文介绍Agentomics：面向单个生物医学训练数据集的LLM Agent系统，分阶段探索数据表示、模型结构、训练与预测分析；模型脚本和每步工件须通过结构与功能验证，错误会反馈给当前Agent重做，完成后输出可复训模型、推理脚本和报告。评测覆盖Protein Engineering 6项、Drug Discovery 9项、Regulatory Genomics 5项数据集。与4种Agent基线比较，Agentomics在三个领域均有较高人类榜单百分位；在best-of-3模型与人类SOTA对照中，Protein Engineering 6/6达新SOTA，Drug Discovery 2/9达新SOTA，Regulatory Genomics 4/5匹配或超过人类SOTA，严格超过为11/20（另有1项持平）。本文所读为2026-01-30 bioRxiv预印本版本。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 当前判断：included；读者建议：included。
全文详细描述具有科研角色的端到端生物医学ML Agent：按数据集逐步执行数据探索、划分、表示、架构设计、训练、推理和预测探索，反复调用代码工具并接受结构/运行验证反馈，随后在held-out test上评价新模型。任务直接涉及蛋白质工程、药物发现分子/ADME属性和调控基因组学基准，属于真实科学对象的实验建模，而非仅通用编码基准。

### 1.2 排除风险检查

按数据对象多模块分类：Regulatory Genomics中的人类增强子、开放染色质、Drosophila增强子和RNA相互作用任务，以及SARS-CoV-2 spike、Staphylococcus aureus、植物光系统蛋白等蛋白工程任务支持06（06.03.01基因组学、06.03.06蛋白质科学）；9项Drug Discovery数据直接预测EGFR抑制剂分类、药物代谢/清除、血浆蛋白结合、溶解度、CYP2D6底物、logP、hERG、BBB和Caco-2通透性，支持07.04.01药物发现，同时SMILES小分子性质/化学空间任务独立支持03.04分子设计与化学空间探索。故modules为03;06;07，主归档06以覆盖多组学/蛋白科学；不纳入04，亦不把所有数据集笼统称作临床医学。 主控：06模块正式落点采用06.01.13计算生物学，以覆盖基因组与蛋白工程两个对象簇；06.03.01/06.03.06的具体对象保留在证据中。ML是建模工具，本次未据其技术名称额外追加01。
完整闭环不是纳入门槛；科研目标、多步行动、至少一项Agent能力及明确科研角色须同时成立。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：03;06;07
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：06（仅归档，不替代多模块事实）
- 模块内分类路径：03.04; 06.01.13; 07.04.01
- 分类深度：03/04使用二级；06/07使用固定三级；其余沿用现有树。
- 分类状态：原文证据复核

### 2.2 对象优先判定

基准含20个任务：Protein Engineering 6项、Drug Discovery 9项、Regulatory Genomics 5项。每任务重复三次，每次8小时；训练/验证与测试数据隔离，作者计算ACC/AUPRC/AUROC或MAE/Pearson/Spearman等适配指标，同时报告运行完成率。相对人类榜单，Agentomics平均百分位分别为Protein Engineering 75.92、Drug Discovery 34.29、Regulatory Genomics 63.85；与其他Agent比较，在所有已测领域表现领先。best-of-3模型在Protein Engineering 6/6数据集超过人类SOTA，Drug Discovery 2/9达到新SOTA，Regulatory Genomics 4/5匹配或超过人类SOTA，严格超过为11/20（另有1项持平）。作者还报告验证-测试分数相关性总体中位数0.964；Regulatory Genomics均值0.986、Protein Engineering 0.746、Drug Discovery 0.807。注意各结果取决于运行时限、重复次数和对应数据集leaderboard定义。

### 2.3 容易混淆的边界

按数据对象多模块分类：Regulatory Genomics中的人类增强子、开放染色质、Drosophila增强子和RNA相互作用任务，以及SARS-CoV-2 spike、Staphylococcus aureus、植物光系统蛋白等蛋白工程任务支持06（06.03.01基因组学、06.03.06蛋白质科学）；9项Drug Discovery数据直接预测EGFR抑制剂分类、药物代谢/清除、血浆蛋白结合、溶解度、CYP2D6底物、logP、hERG、BBB和Caco-2通透性，支持07.04.01药物发现，同时SMILES小分子性质/化学空间任务独立支持03.04分子设计与化学空间探索。故modules为03;06;07，主归档06以覆盖多组学/蛋白科学；不纳入04，亦不把所有数据集笼统称作临床医学。 主控：06模块正式落点采用06.01.13计算生物学，以覆盖基因组与蛋白工程两个对象簇；06.03.01/06.03.06的具体对象保留在证据中。ML是建模工具，本次未据其技术名称额外追加01。

## 3. Agent 系统与科研流程角色

全文详细描述具有科研角色的端到端生物医学ML Agent：按数据集逐步执行数据探索、划分、表示、架构设计、训练、推理和预测探索，反复调用代码工具并接受结构/运行验证反馈，随后在held-out test上评价新模型。任务直接涉及蛋白质工程、药物发现分子/ADME属性和调控基因组学基准，属于真实科学对象的实验建模，而非仅通用编码基准。

科研流程与自主能力以本文实际行动和工具调用为依据：

系统输入单个训练集、可选数据说明/验证/测试集及运行约束。LLM Agent依序完成七个预定义步骤：数据探索、数据划分、数据表示、模型架构、训练、推理、预测探索；每步有独立上下文Agent，可反复使用bash、Python写入/运行、文件编辑、foundation-model信息及结构化结果工具。每步输出须通过JSON结构检查和对应的功能检查，失败信息反馈并重试，超过重试上限则重启该步骤/流程。每次完整迭代产生训练/验证指标和结构化摘要，Experiment Design LLM结合前序迭代、剩余资源和得分生成下一轮策略；依验证集指标选择最终迭代，测试集一直对Agent隐藏，最终对输出模型统一计算测试指标。评测使用GPT-5.1-Codex-Max，每数据集三次8小时运行；Protein Engineering和Drug Discovery沿BioML-bench协议与AIDE、MLAgentBench、STELLA及人类榜单比较，Regulatory Genomics与Biomni等系统比较。

## 4. 方法设计

### 4.1 方法动机与设计

把生物医学模型研发拆成带接口、工件与验证门槛的七步Agent实验流程，并通过迭代设计、真实运行与隐藏测试完成模型开发；公开结果显示系统可在蛋白质工程、分子药物发现和调控基因组多类任务上生成可复训/推理模型，并在部分专家基准超过既有SOTA。

### 4.2 系统流程与组件

系统输入单个训练集、可选数据说明/验证/测试集及运行约束。LLM Agent依序完成七个预定义步骤：数据探索、数据划分、数据表示、模型架构、训练、推理、预测探索；每步有独立上下文Agent，可反复使用bash、Python写入/运行、文件编辑、foundation-model信息及结构化结果工具。每步输出须通过JSON结构检查和对应的功能检查，失败信息反馈并重试，超过重试上限则重启该步骤/流程。每次完整迭代产生训练/验证指标和结构化摘要，Experiment Design LLM结合前序迭代、剩余资源和得分生成下一轮策略；依验证集指标选择最终迭代，测试集一直对Agent隐藏，最终对输出模型统一计算测试指标。评测使用GPT-5.1-Codex-Max，每数据集三次8小时运行；Protein Engineering和Drug Discovery沿BioML-bench协议与AIDE、MLAgentBench、STELLA及人类榜单比较，Regulatory Genomics与Biomni等系统比较。

## 5. 实验与验证

### 5.1 验证方式、对象及任务

基准含20个任务：Protein Engineering 6项、Drug Discovery 9项、Regulatory Genomics 5项。每任务重复三次，每次8小时；训练/验证与测试数据隔离，作者计算ACC/AUPRC/AUROC或MAE/Pearson/Spearman等适配指标，同时报告运行完成率。相对人类榜单，Agentomics平均百分位分别为Protein Engineering 75.92、Drug Discovery 34.29、Regulatory Genomics 63.85；与其他Agent比较，在所有已测领域表现领先。best-of-3模型在Protein Engineering 6/6数据集超过人类SOTA，Drug Discovery 2/9达到新SOTA，Regulatory Genomics 4/5匹配或超过人类SOTA，严格超过为11/20（另有1项持平）。作者还报告验证-测试分数相关性总体中位数0.964；Regulatory Genomics均值0.986、Protein Engineering 0.746、Drug Discovery 0.807。注意各结果取决于运行时限、重复次数和对应数据集leaderboard定义。

### 5.2 基线、指标与结果

基准含20个任务：Protein Engineering 6项、Drug Discovery 9项、Regulatory Genomics 5项。每任务重复三次，每次8小时；训练/验证与测试数据隔离，作者计算ACC/AUPRC/AUROC或MAE/Pearson/Spearman等适配指标，同时报告运行完成率。相对人类榜单，Agentomics平均百分位分别为Protein Engineering 75.92、Drug Discovery 34.29、Regulatory Genomics 63.85；与其他Agent比较，在所有已测领域表现领先。best-of-3模型在Protein Engineering 6/6数据集超过人类SOTA，Drug Discovery 2/9达到新SOTA，Regulatory Genomics 4/5匹配或超过人类SOTA，严格超过为11/20（另有1项持平）。作者还报告验证-测试分数相关性总体中位数0.964；Regulatory Genomics均值0.986、Protein Engineering 0.746、Drug Discovery 0.807。注意各结果取决于运行时限、重复次数和对应数据集leaderboard定义。

### 5.3 科学贡献与证据强度

把生物医学模型研发拆成带接口、工件与验证门槛的七步Agent实验流程，并通过迭代设计、真实运行与隐藏测试完成模型开发；公开结果显示系统可在蛋白质工程、分子药物发现和调控基因组多类任务上生成可复训/推理模型，并在部分专家基准超过既有SOTA。

证据层级：原始全文支持；作者报告结果不等于独立复现。

## 6. 与已有工作的关系

与AutoML及生物医学基础模型建模相接；原文与AIDE、MLAgentBench、STELLA、Biomni及人类榜单对照，区别在带工件检查和运行反馈的多轮建模流程。

## 7. 局限性与风险

证据来自bioRxiv预印本v1，未据此声称期刊版所有细节一致。不同领域和基准规模不均（6/9/5），Drug Discovery平均专家榜单百分位明显低于Protein Engineering，且best-of-3只在2/9药物发现数据集超过人类SOTA；运行使用GPT-5.1-Codex-Max、每次最多8小时及特定硬件，不能直接外推其他模型/预算。测试集指标仅用于事后评估；Agent设计和基准本身仍受数据集质量、指标与专家榜单覆盖限制。系统做的是计算模型实验，不等同于药物候选的实验/临床验证。

## 8. 对综述写作的价值

适合比较通用 ML Agent 在多个生物医学对象上的实验设计、验证与绩效。

推荐引用强度：普通引用，可在核对原文后用于相应领域案例。

## 9. 总结

### 9.1 一句话概括

Agent迭代构建生物医学学习模型

### 9.2 速记版 pipeline

系统输入单个训练集、可选数据说明/验证/测试集及运行约束。LLM Agent依序完成七个预定义步骤：数据探索、数据划分、数据表示、模型架构、训练、推理、预测探索；每步有独立上下文Agent，可反复使用bash、Python写入/运行、文件编辑、foundation-model信息及结构化结果工具。每步输出须通过JSON结构检查和对应的功能检查，失败信息反馈并重试，超过重试上限则重启该步骤/流程。每次完整迭代产生训练/验证指标和结构化摘要，Experiment Design LLM结合前序迭代、剩余资源和得分生成下一轮策略；依验证集指标选择最终迭代，测试集一直对Agent隐藏，最终对输出模型统一计算测试指标。评测使用GPT-5.1-Codex-Max，每数据集三次8小时运行；Protein Engineering和Drug Discovery沿BioML-bench协议与AIDE、MLAgentBench、STELLA及人类榜单比较，Regulatory Genomics与Biomni等系统比较。

### 9.3 标注字段汇总

```text
paper_id=ASD-0893
inclusion_status=included
scientific_object_modules=03;06;07
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=06
module_taxonomy_codes=03.04; 06.01.13; 07.04.01
source_level=fulltext
fulltext_followup_required=false
```

### 全文后续要求

本轮已读原始全文并完成对象分类；无需为纳入/分类另做全文补读。具体引用时仍需回查相应原文位置。
