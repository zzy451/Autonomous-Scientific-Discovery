# Beyond Execution: Auditing Experimental Fidelity in LLM-Driven Scientific Research

**论文信息**

- ID：ASD-0925
- 标题：Beyond Execution: Auditing Experimental Fidelity in LLM-Driven Scientific Research
- 作者：Lezhi Yu; Xiaogang Xu; Yuhua Zhou; Shuibing He; Aimin Pan
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2608.26753
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0925.txt
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Yu_2026_Beyond_Execution_Auditing_Experimental_Fidelity_in_LLM_Driven_Scientific_ASD0925.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 研究目标/科学问题 | 本文提出 ABE-Ralph，用于审计 LLM 驱动科研系统是否忠实执行论文实验。基准包含来自机器学习、计算物理和生物信息学的 30 项复现任务，并采用八步实验工作流以及定量、定性和代码层验证。论文还报告 NatureBench 的 23 项发现任务，其中 5 项达到或超过相应最先进水平；该结果应理解为特定基准上的报告。 | 本地全文：ASD-0925中与研究目标/科学问题直接相关的原文句子；核验TXT行号 534 | We introduce ABE-Ralph (Auto Baseline Experiment), an automated scientific auditing framework that monitors, binds, and verifies the experimental lifecycle of AI-driven research, treating scientific reproduction as a reference-anchored process. Before implementation, ABE-Ralph structures paper claims, architectural components, datasets, baselines, metrics, and resource bounds into declarative YAML contracts. An 8-step workflow guides model construction and protocol execution. During execution, a Triple-Verification pipeline checks quantitative metric alignment, qualitative semantic logic, and structural code fidelity. These checks intercept deceptive model shortcuts and guarantee methodological fidelity and auditability. | 高（一手正文；非独立复现） |
| 多步行动/研究流程 | 每项任务围绕论文中的主张制定复现和审计步骤；系统依次实现、执行并检查实验，以定量结果、定性判断和代码级证据核验实验忠实度。 | 本地全文：ASD-0925中与多步行动/研究流程直接相关的原文句子；核验TXT行号 534 | During execution, a Triple-Verification pipeline checks quantitative metric alignment, qualitative semantic logic, and structural code fidelity. | 高（一手正文；非独立复现） |
| Agent实现与能力 | ABE-Ralph 将 Ralph 循环式编码Agent与 claim-anchored 审计协议结合，追踪论文主张、实现、运行结果及代码证据。 | 本地全文：ASD-0925中与Agent实现与能力直接相关的原文句子；核验TXT行号 469 | LLM agents used for scientific experimentation must do more than generate executable code: they must implement the reference method faithfully, design experiments that test the paper’s claims, and provide evidence supporting those claims. We show that agents often produce methodological hallucinations: silently reducing datasets or training budgets, replacing failed learning or generative components with lookup or oracle functions, or drawing conclusions from resource-limited settings where a method’s claimed advantage disappears. To detect these failures, we introduce ABE-Ralph, a reference-anchored auditing framework that represents claims, protocols, required components, baselines, and metrics as structured experimental constraints, guides implementation through an 8-step workflow, and performs quantitative, qualitative, and code-level verification. Across 30 long-horizon reproduction runs covering 12 machine learning domains, ABE-Ralph achieves a 93% robust execution rate and identifies five scientific failure modes. In 23 NatureBench discovery tasks, ABE-Ralph matches or exceeds state-of-the-art performance on 5 tasks. These results show that reliable evaluation of AI scientists must assess whether the experimental design faithfully tests the intended claim and whether the resulting evidence supports it, rather than treating code execution or plausible metrics as evidence of scientific success. | 高（一手正文；非独立复现） |
| 实验任务与验证设置 | 基准由机器学习、计算物理和生物信息学的 30 项复现任务构成；另在 23 项 NatureBench 科学发现任务上评估，并报告达到或超过 SOTA 的任务数。 | 本地全文：ASD-0925中与实验任务与验证设置直接相关的原文句子；核验TXT行号 1426 | We construct a benchmark consisting of 30 distinct reproduction tasks derived from classic ML, computational physics, and bio-informatics domains (e.g., implementing architecture variants of U-Net, training ResNet pipelines under resource constraints, and optimizing multi-objective scientific solvers). Each task is mapped to a ground-truth specification containing canonical data flows, hyperparameter baselines, and reference metrics. | 高（一手正文；非独立复现） |
| 作者报告的结果/贡献 | 作者报告 NatureBench 的 23 项发现任务中有 5 项达到或超过 SOTA。复现任务用于检查实验实现忠实度，不能把基准成绩推广为全面科研能力。 科学贡献是将实验忠实度作为科研Agent的重要评价对象；系统贡献是八步审计流程及多层验证协议。 | 本地全文中包含该原句的位置；核验TXT行号 1803 | Table 4 summarizes the results. ABE-Ralph achieves or exceeds the state-of-the-art baseline on 5 of 23 tasks, demonstrating that the constraint-anchored optimization framework can effectively navigate open-ended scientific search spaces. On the remaining 18 tasks, ABE-Ralph produces valid solutions within the constraint boundaries but falls short of the best-known results, indicating that the discovery mode provides a sound foundation for further optimization through extended search or multi-agent collaboration. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

本文提出 ABE-Ralph，用于审计 LLM 驱动科研系统是否忠实执行论文实验。基准包含来自机器学习、计算物理和生物信息学的 30 项复现任务，并采用八步实验工作流以及定量、定性和代码层验证。论文还报告 NatureBench 的 23 项发现任务，其中 5 项达到或超过相应最先进水平；该结果应理解为特定基准上的报告。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。本文提出 ABE-Ralph，用于审计 LLM 驱动科研系统是否忠实执行论文实验。基准包含来自机器学习、计算物理和生物信息学的 30 项复现任务，并采用八步实验工作流以及定量、定性和代码层验证。论文还报告 NatureBench 的 23 项发现任务，其中 5 项达到或超过相应最先进水平；该结果应理解为特定基准上的报告。
  - 原文位置：本地全文：ASD-0925中与研究目标/科学问题直接相关的原文句子；核验TXT行号 534；引文：We introduce ABE-Ralph (Auto Baseline Experiment), an automated scientific auditing framework that monitors, binds, and verifies the experimental lifecycle of AI-driven research, treating scientific reproduction as a reference-anchored process. Before implementation, ABE-Ralph structures paper claims, architectural components, datasets, baselines, metrics, and resource bounds into declarative YAML contracts. An 8-step workflow guides model construction and protocol execution. During execution, a Triple-Verification pipeline checks quantitative metric alignment, qualitative semantic logic, and structural code fidelity. These checks intercept deceptive model shortcuts and guarantee methodological fidelity and auditability.
- 多步行动过程：yes。每项任务围绕论文中的主张制定复现和审计步骤；系统依次实现、执行并检查实验，以定量结果、定性判断和代码级证据核验实验忠实度。
  - 原文位置：本地全文：ASD-0925中与多步行动/研究流程直接相关的原文句子；核验TXT行号 534；引文：During execution, a Triple-Verification pipeline checks quantitative metric alignment, qualitative semantic logic, and structural code fidelity.
- 至少一种Agent能力：yes。ABE-Ralph 将 Ralph 循环式编码Agent与 claim-anchored 审计协议结合，追踪论文主张、实现、运行结果及代码证据。
  - 原文位置：本地全文：ASD-0925中与Agent实现与能力直接相关的原文句子；核验TXT行号 469；引文：LLM agents used for scientific experimentation must do more than generate executable code: they must implement the reference method faithfully, design experiments that test the paper’s claims, and provide evidence supporting those claims. We show that agents often produce methodological hallucinations: silently reducing datasets or training budgets, replacing failed learning or generative components with lookup or oracle functions, or drawing conclusions from resource-limited settings where a method’s claimed advantage disappears. To detect these failures, we introduce ABE-Ralph, a reference-anchored auditing framework that represents claims, protocols, required components, baselines, and metrics as structured experimental constraints, guides implementation through an 8-step workflow, and performs quantitative, qualitative, and code-level verification. Across 30 long-horizon reproduction runs covering 12 machine learning domains, ABE-Ralph achieves a 93% robust execution rate and identifies five scientific failure modes. In 23 NatureBench discovery tasks, ABE-Ralph matches or exceeds state-of-the-art performance on 5 tasks. These results show that reliable evaluation of AI scientists must assess whether the experimental design faithfully tests the intended claim and whether the resulting evidence supports it, rather than treating code execution or plausible metrics as evidence of scientific success.
- 明确科研流程角色：yes。基准由机器学习、计算物理和生物信息学的 30 项复现任务构成；另在 23 项 NatureBench 科学发现任务上评估，并报告达到或超过 SOTA 的任务数。
  - 原文位置：本地全文：ASD-0925中与实验任务与验证设置直接相关的原文句子；核验TXT行号 1426；引文：We construct a benchmark consisting of 30 distinct reproduction tasks derived from classic ML, computational physics, and bio-informatics domains (e.g., implementing architecture variants of U-Net, training ResNet pipelines under resource constraints, and optimizing multi-objective scientific solvers). Each task is mapped to a ground-truth specification containing canonical data flows, hyperparameter baselines, and reference metrics.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：01;02;06;11
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：01（仅归档，不覆盖其他模块）
- 模块内分类路径：01.02 计算机科学；02.02 物理学；06.01.12 生物信息学；11.07 科学系统与知识生产研究
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

对象模块与代码沿用输入审计记录（01, 02, 06, 11；01.02, 02.02, 06.01.12, 11.07）；是否纳入与对象分类分开判断。

### 2.3 容易混淆的边界

对象模块与代码沿用输入审计记录（01, 02, 06, 11；01.02, 02.02, 06.01.12, 11.07）；是否纳入与对象分类分开判断。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

自主科研Agent

### 3.2 科研流程角色

科研问题处理；多步行动或评测

ABE-Ralph 将 Ralph 循环式编码Agent与 claim-anchored 审计协议结合，追踪论文主张、实现、运行结果及代码证据。

### 3.3 自主能力

ABE-Ralph 将 Ralph 循环式编码Agent与 claim-anchored 审计协议结合，追踪论文主张、实现、运行结果及代码证据。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

科学贡献是将实验忠实度作为科研Agent的重要评价对象；系统贡献是八步审计流程及多层验证协议。

### 4.2 系统流程与组件

每项任务围绕论文中的主张制定复现和审计步骤；系统依次实现、执行并检查实验，以定量结果、定性判断和代码级证据核验实验忠实度。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

基准由机器学习、计算物理和生物信息学的 30 项复现任务构成；另在 23 项 NatureBench 科学发现任务上评估，并报告达到或超过 SOTA 的任务数。

### 5.2 基线、指标与结果

作者报告 NatureBench 的 23 项发现任务中有 5 项达到或超过 SOTA。复现任务用于检查实验实现忠实度，不能把基准成绩推广为全面科研能力。

### 5.3 科学贡献与证据强度

科学贡献是将实验忠实度作为科研Agent的重要评价对象；系统贡献是八步审计流程及多层验证协议。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

论文以“Beyond Execution: Auditing Experimental Fidelity in LLM-Driven Scientific Research”对应的研究任务为对象，具体与哪些既有系统或基准比较，应结合其正文相关工作和实验基线判断；不把工具名称直接视为科学对象。

## 7. 局限性与风险

基准规模和所含学科限制了结论外推范围；复现实验与开放式科学发现衡量不同能力。

## 8. 对综述写作的价值

可用于综述“Beyond Execution: Auditing Experimental Fidelity in LLM-Driven Scientific Research”所涉及的Agent任务、研究流程和验证方式；其证据边界为本论文实际报告的任务集与实验结果。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

ABE-Ralph 用多层审计协议检查科研Agent复现实验的忠实度。

### 9.2 速记版 pipeline

每项任务围绕论文中的主张制定复现和审计步骤；系统依次实现、执行并检查实验，以定量结果、定性判断和代码级证据核验实验忠实度。

### 9.3 标注字段汇总

```text
paper_id=ASD-0925
inclusion_status=to_read
scientific_object_modules=01;02;06;11
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=01
module_taxonomy_codes=01.02;02.02;06.01.12;11.07
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`01.02.13` 机器学习；二级：`01.02`。
- 原文位置：PDF p.1。
- 判定：30次复现覆盖12个机器学习领域，具具体执行和忠实性验证。
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
