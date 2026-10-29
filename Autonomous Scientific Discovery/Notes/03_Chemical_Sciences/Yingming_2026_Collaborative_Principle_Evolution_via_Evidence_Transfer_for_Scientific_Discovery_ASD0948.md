# Collaborative Principle Evolution via Evidence Transfer for Scientific Discovery

**论文信息**

- ID：ASD-0948
- 标题：Collaborative Principle Evolution via Evidence Transfer for Scientific Discovery
- 作者：Pu, Yingming; Chen, Hongyu; Lin, Tao
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2609.35315
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0948.txt
- PDF / 本地文件路径：Reference_PDF/03_Chemical_Sciences/Yingming_2026_Collaborative_Principle_Evolution_via_Evidence_Transfer_for_Scientific_Discovery_ASD0948.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 研究目标/科学问题 | COEVOLVE将协作科学发现表述为并行 principle-evolution 分支之间的证据传递。协调核心汇集各分支测量、去重和折扣证据，再通过价值信息门控路由及上下文折扣似然注入，帮助目标分支更新principle posterior，同时保持分支后验相互独立。作者在六项科学发现任务上进行匹配评价。 | 本地全文：ASD-0948中与研究目标/科学问题直接相关的原文句子；核验TXT行号 15 | To address this, we formulate collaborative scientific discovery as evidence transfer between parallel principle-evolution branches. | 高（一手正文；非独立复现） |
| 多步行动/研究流程 | 分支保留各自原则后验；协调核心汇总、去重并折扣证据，按value-of-information门控路由，并以上下文折扣似然更新目标分支。 | 本地全文：ASD-0948中与多步行动/研究流程直接相关的原文句子；核验TXT行号 76 | A coordination core collects branch-level evidence, deduplicates and discounts each record, and routes them to the target branch for principle posterior updates. | 高（一手正文；非独立复现） |
| Agent实现与能力 | COEVOLVE以多个并行分支分别演化研究原则，由协调核心收集证据并决定是否以及向哪个分支传递。 | 本地全文：ASD-0948中与Agent实现与能力直接相关的原文句子；核验TXT行号 18 | By integrating value-of-information-gated routing and context-discounted likelihood injection, COEVOLVE enables branches to collaborate through shared measurements while keeping their principle posteriors separate. | 高（一手正文；非独立复现） |
| 实验任务与验证设置 | 作者在六项科学发现任务上与匹配评价设置比较，覆盖生物活性、抗菌肽、启动子表达等任务。 | 本地全文：ASD-0948中与实验任务与验证设置直接相关的原文句子；核验TXT行号 373 | We evaluate COEVOLVE on six scientific tasks, spanning Molecular Bio-activity Opti- mization (MBO) (Gaulton et al., 2011), Antimicrobial Peptide Design (AMP) (Santos-Junior et al., 2020), Promoter Expression Optimization (Promoter) (de Almeida et al., 2022) in biology, Nanohelix Optimization (NHO) (Wu et al., 2025) and Transition-Metal-Complex Design (TMC) (Song et al., 2025) in materials science, and Superconductor Critical-Temperature Optimization (SPO) (Hamidieh, 2018) in physics. | 高（一手正文；非独立复现） |
| 作者报告的结果/贡献 | 论文报告跨六项任务的匹配评价结果，考察证据转移对发现效率和结果质量的影响；具体效应需结合任务逐项数据。 贡献是允许并行研究分支共享证据，同时保留分支各自的原则后验，减少重复测量并扩大探索。 | 本地全文中包含该原句的位置；核验TXT行号 21 | Across six scientific-discovery tasks under a matched evaluation budget, COEVOLVE attains a mean solution quality of 66.5% versus 57.0% for single-branch principle evolution, with a 1.80× mean wall-clock speedup on the GPT-5.6-Terra backbone; on five auto-research tasks delegated to an autonomous research harness, it is the only arm whose mean stays above the published SOTA anchor on every task. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

COEVOLVE将协作科学发现表述为并行 principle-evolution 分支之间的证据传递。协调核心汇集各分支测量、去重和折扣证据，再通过价值信息门控路由及上下文折扣似然注入，帮助目标分支更新principle posterior，同时保持分支后验相互独立。作者在六项科学发现任务上进行匹配评价。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。COEVOLVE将协作科学发现表述为并行 principle-evolution 分支之间的证据传递。协调核心汇集各分支测量、去重和折扣证据，再通过价值信息门控路由及上下文折扣似然注入，帮助目标分支更新principle posterior，同时保持分支后验相互独立。作者在六项科学发现任务上进行匹配评价。
  - 原文位置：本地全文：ASD-0948中与研究目标/科学问题直接相关的原文句子；核验TXT行号 15；引文：To address this, we formulate collaborative scientific discovery as evidence transfer between parallel principle-evolution branches.
- 多步行动过程：yes。分支保留各自原则后验；协调核心汇总、去重并折扣证据，按value-of-information门控路由，并以上下文折扣似然更新目标分支。
  - 原文位置：本地全文：ASD-0948中与多步行动/研究流程直接相关的原文句子；核验TXT行号 76；引文：A coordination core collects branch-level evidence, deduplicates and discounts each record, and routes them to the target branch for principle posterior updates.
- 至少一种Agent能力：yes。COEVOLVE以多个并行分支分别演化研究原则，由协调核心收集证据并决定是否以及向哪个分支传递。
  - 原文位置：本地全文：ASD-0948中与Agent实现与能力直接相关的原文句子；核验TXT行号 18；引文：By integrating value-of-information-gated routing and context-discounted likelihood injection, COEVOLVE enables branches to collaborate through shared measurements while keeping their principle posteriors separate.
- 明确科研流程角色：yes。作者在六项科学发现任务上与匹配评价设置比较，覆盖生物活性、抗菌肽、启动子表达等任务。
  - 原文位置：本地全文：ASD-0948中与实验任务与验证设置直接相关的原文句子；核验TXT行号 373；引文：We evaluate COEVOLVE on six scientific tasks, spanning Molecular Bio-activity Opti- mization (MBO) (Gaulton et al., 2011), Antimicrobial Peptide Design (AMP) (Santos-Junior et al., 2020), Promoter Expression Optimization (Promoter) (de Almeida et al., 2022) in biology, Nanohelix Optimization (NHO) (Wu et al., 2025) and Transition-Metal-Complex Design (TMC) (Song et al., 2025) in materials science, and Superconductor Critical-Temperature Optimization (SPO) (Hamidieh, 2018) in physics.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：03;04;06;07
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：03（仅归档，不覆盖其他模块）
- 模块内分类路径：03.04 分子设计与化学空间探索；04.03 软物质与功能材料；04.04 能源、电子与器件材料；06.01.11 合成生物学；06.03.06 蛋白质科学；07.04.01 药物发现
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

对象模块与代码沿用输入审计记录（03, 04, 06, 07；03.04, 04.03, 04.04, 06.01.11, 06.03.06, 07.04.01）；是否纳入与对象分类分开判断。

### 2.3 容易混淆的边界

对象模块与代码沿用输入审计记录（03, 04, 06, 07；03.04, 04.03, 04.04, 06.01.11, 06.03.06, 07.04.01）；是否纳入与对象分类分开判断。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

自主科研Agent

### 3.2 科研流程角色

科研问题处理；多步行动或评测

COEVOLVE以多个并行分支分别演化研究原则，由协调核心收集证据并决定是否以及向哪个分支传递。

### 3.3 自主能力

COEVOLVE以多个并行分支分别演化研究原则，由协调核心收集证据并决定是否以及向哪个分支传递。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

贡献是允许并行研究分支共享证据，同时保留分支各自的原则后验，减少重复测量并扩大探索。

### 4.2 系统流程与组件

分支保留各自原则后验；协调核心汇总、去重并折扣证据，按value-of-information门控路由，并以上下文折扣似然更新目标分支。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

作者在六项科学发现任务上与匹配评价设置比较，覆盖生物活性、抗菌肽、启动子表达等任务。

### 5.2 基线、指标与结果

论文报告跨六项任务的匹配评价结果，考察证据转移对发现效率和结果质量的影响；具体效应需结合任务逐项数据。

### 5.3 科学贡献与证据强度

贡献是允许并行研究分支共享证据，同时保留分支各自的原则后验，减少重复测量并扩大探索。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

论文以“Collaborative Principle Evolution via Evidence Transfer for Scientific Discovery”对应的研究任务为对象，具体与哪些既有系统或基准比较，应结合其正文相关工作和实验基线判断；不把工具名称直接视为科学对象。

## 7. 局限性与风险

证据去重、折扣和路由质量决定传递效用；六个任务仍不足以证明所有科学问题都适合该协作机制。

## 8. 对综述写作的价值

可用于综述“Collaborative Principle Evolution via Evidence Transfer for Scientific Discovery”所涉及的Agent任务、研究流程和验证方式；其证据边界为本论文实际报告的任务集与实验结果。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

COEVOLVE在独立并行研究分支之间按信息价值传递证据。

### 9.2 速记版 pipeline

分支保留各自原则后验；协调核心汇总、去重并折扣证据，按value-of-information门控路由，并以上下文折扣似然更新目标分支。

### 9.3 标注字段汇总

```text
paper_id=ASD-0948
inclusion_status=to_read
scientific_object_modules=03;04;06;07
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=03
module_taxonomy_codes=03.04;04.03;04.04;06.01.11;06.03.06;07.04.01
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`03.04.02` 小分子性质优化；二级：`03.04`。
- 原文位置：PDF pp.6,7,33。
- 判定：Concrete experiment/task evidence supports 03.04.02 (小分子性质优化). MBO searches the space of drug-like small molecules, represented as SMILES strings, for the highest predicted bio-activity; quantified by maximizing its predicted pChEMBL value
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
