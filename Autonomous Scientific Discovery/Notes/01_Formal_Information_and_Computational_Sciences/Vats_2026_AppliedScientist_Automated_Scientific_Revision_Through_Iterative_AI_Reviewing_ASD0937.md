# AppliedScientist: Automated Scientific Revision Through Iterative AI Reviewing

**论文信息**

- ID：ASD-0937
- 标题：AppliedScientist: Automated Scientific Revision Through Iterative AI Reviewing
- 作者：Vidushee Vats; Karun Sharma; Shengzhi Li; Shichao Pei
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2609.14738
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0937.txt
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Vats_2026_AppliedScientist_Automated_Scientific_Revision_Through_Iterative_AI_Reviewing_ASD0937.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 研究目标/科学问题 | AppliedScientist把自主科学家与AI审稿人组成闭环，对被拒稿进行迭代修订；修订Agent可以访问先前稿件版本，而每轮审查独立生成以减少前序判断偏差。数据包含 25 篇被拒和 5 篇边缘接收的ICLR论文，且均有公开评审及代码。 | 本地全文：ASD-0937中与研究目标/科学问题直接相关的原文句子；核验TXT行号 328 | Automated reviewing systems are increasingly evaluated based on the quality of the reviews they produce. Yet a review is only useful if acting on it leads to a measurable improvement in the paper. We present AppliedScientist, a closed-loop system that couples an autonomous AI scientist with an AI reviewer, and evaluate it by iteratively revising rejected papers from a range of research subfields. To mirror how human authors build on earlier drafts, the AI scientist has access to its previous versions during revision. To avoid bias from prior judgments, however, each review is generated independently, with the reviewer having no memory of earlier feedback or scores. We compare three revision settings: one initialized with the original venue reviews, one initialized with AI-generated reviews, and autonomous self-revision using the same fixed prompt in every round. Because the reviewer both guides and evaluates the revision, we also assess the human-initialized revisions using Stanford Reviewer as an independent evaluator. Reviewer-guided revision consistently improves more than fixed-prompt self-revision, and Stanford Reviewer also assigns higher scores to later revisions. AppliedScientist resolves 128 of 150 execution-related weaknesses (85.3%), but only 2 of 18 idea-related weaknesses (11.1%), suggesting that iterative revision is effective at improving experiments and implementation, but rarely changes concerns about novelty or significance. | 高（一手正文；非独立复现） |
| 多步行动/研究流程 | 系统读取稿件、评审意见及可用代码，定位执行或研究构想问题并修订；新一轮审查不沿用旧裁决，比较稿件迭代前后的改进。 | 本地全文：ASD-0937中与多步行动/研究流程直接相关的原文句子；核验TXT行号 328 | We present AppliedScientist, a closed-loop system that couples an autonomous AI scientist with an AI reviewer, and evaluate it by iteratively revising rejected papers from a range of research subfields. | 高（一手正文；非独立复现） |
| Agent实现与能力 | AppliedScientist由负责修改论文的自主科学家Agent和独立AI reviewer组成，形成反复评审、修订与再评审的闭环。 | 本地全文：ASD-0937中与Agent实现与能力直接相关的原文句子；核验TXT行号 328 | To avoid bias from prior judgments, however, each review is generated independently, with the reviewer having no memory of earlier feedback or scores. | 高（一手正文；非独立复现） |
| 实验任务与验证设置 | 评测集包括25篇拒稿和5篇边缘接收的ICLR论文，跨多个研究领域；原文同时提供公开评审及代码以支持分析。 | 本地全文：ASD-0937中与实验任务与验证设置直接相关的原文句子；核验TXT行号 390 | We evaluate AppliedScientist on 25 rejected and 5 borderline-accepted ICLR papers spanning multiple research domains. Reviewer-guided revision improves substantially more than autonomous self-revision, while Stanford Reviewer also assigns higher scores to later human-initialized versions. The effect depends strongly on the type of weakness: AppliedScientist resolves 128 of 150 execution-related weaknesses (85.3%), but only 2 of 18 idea-related weaknesses (∼11.1%\sim 11.1\%). Iterative revision can therefore strengthen the implementation, experimental evidence, and presentation of an existing contribution, but it rarely resolves concerns about the novelty or significance of the contribution itself | 高（一手正文；非独立复现） |
| 作者报告的结果/贡献 | 作者评估闭环修订是否解决论文中的执行与构想缺陷；结论受30篇样本及AI评审评价方式影响，不能等同于真实重投结果。 贡献是把AI评审意见接入自主科研修订循环，并用真实投稿材料研究迭代修稿能力。 | 本地全文中包含该原句的位置；核验TXT行号 328 | AppliedScientist resolves 128 of 150 execution-related weaknesses (85.3%), but only 2 of 18 idea-related weaknesses (11.1%), suggesting that iterative revision is effective at improving experiments and implementation, but rarely changes concerns about novelty or significance. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

AppliedScientist把自主科学家与AI审稿人组成闭环，对被拒稿进行迭代修订；修订Agent可以访问先前稿件版本，而每轮审查独立生成以减少前序判断偏差。数据包含 25 篇被拒和 5 篇边缘接收的ICLR论文，且均有公开评审及代码。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。AppliedScientist把自主科学家与AI审稿人组成闭环，对被拒稿进行迭代修订；修订Agent可以访问先前稿件版本，而每轮审查独立生成以减少前序判断偏差。数据包含 25 篇被拒和 5 篇边缘接收的ICLR论文，且均有公开评审及代码。
  - 原文位置：本地全文：ASD-0937中与研究目标/科学问题直接相关的原文句子；核验TXT行号 328；引文：Automated reviewing systems are increasingly evaluated based on the quality of the reviews they produce. Yet a review is only useful if acting on it leads to a measurable improvement in the paper. We present AppliedScientist, a closed-loop system that couples an autonomous AI scientist with an AI reviewer, and evaluate it by iteratively revising rejected papers from a range of research subfields. To mirror how human authors build on earlier drafts, the AI scientist has access to its previous versions during revision. To avoid bias from prior judgments, however, each review is generated independently, with the reviewer having no memory of earlier feedback or scores. We compare three revision settings: one initialized with the original venue reviews, one initialized with AI-generated reviews, and autonomous self-revision using the same fixed prompt in every round. Because the reviewer both guides and evaluates the revision, we also assess the human-initialized revisions using Stanford Reviewer as an independent evaluator. Reviewer-guided revision consistently improves more than fixed-prompt self-revision, and Stanford Reviewer also assigns higher scores to later revisions. AppliedScientist resolves 128 of 150 execution-related weaknesses (85.3%), but only 2 of 18 idea-related weaknesses (11.1%), suggesting that iterative revision is effective at improving experiments and implementation, but rarely changes concerns about novelty or significance.
- 多步行动过程：yes。系统读取稿件、评审意见及可用代码，定位执行或研究构想问题并修订；新一轮审查不沿用旧裁决，比较稿件迭代前后的改进。
  - 原文位置：本地全文：ASD-0937中与多步行动/研究流程直接相关的原文句子；核验TXT行号 328；引文：We present AppliedScientist, a closed-loop system that couples an autonomous AI scientist with an AI reviewer, and evaluate it by iteratively revising rejected papers from a range of research subfields.
- 至少一种Agent能力：yes。AppliedScientist由负责修改论文的自主科学家Agent和独立AI reviewer组成，形成反复评审、修订与再评审的闭环。
  - 原文位置：本地全文：ASD-0937中与Agent实现与能力直接相关的原文句子；核验TXT行号 328；引文：To avoid bias from prior judgments, however, each review is generated independently, with the reviewer having no memory of earlier feedback or scores.
- 明确科研流程角色：yes。评测集包括25篇拒稿和5篇边缘接收的ICLR论文，跨多个研究领域；原文同时提供公开评审及代码以支持分析。
  - 原文位置：本地全文：ASD-0937中与实验任务与验证设置直接相关的原文句子；核验TXT行号 390；引文：We evaluate AppliedScientist on 25 rejected and 5 borderline-accepted ICLR papers spanning multiple research domains. Reviewer-guided revision improves substantially more than autonomous self-revision, while Stanford Reviewer also assigns higher scores to later human-initialized versions. The effect depends strongly on the type of weakness: AppliedScientist resolves 128 of 150 execution-related weaknesses (85.3%), but only 2 of 18 idea-related weaknesses (∼11.1%\sim 11.1\%). Iterative revision can therefore strengthen the implementation, experimental evidence, and presentation of an existing contribution, but it rarely resolves concerns about the novelty or significance of the contribution itself

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：01;11
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：01（仅归档，不覆盖其他模块）
- 模块内分类路径：01.02 计算机科学；11.07 科学系统与知识生产研究
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

对象模块与代码沿用输入审计记录（01, 11；01.02, 11.07）；是否纳入与对象分类分开判断。

### 2.3 容易混淆的边界

对象模块与代码沿用输入审计记录（01, 11；01.02, 11.07）；是否纳入与对象分类分开判断。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

自主科研Agent

### 3.2 科研流程角色

科研问题处理；多步行动或评测

AppliedScientist由负责修改论文的自主科学家Agent和独立AI reviewer组成，形成反复评审、修订与再评审的闭环。

### 3.3 自主能力

AppliedScientist由负责修改论文的自主科学家Agent和独立AI reviewer组成，形成反复评审、修订与再评审的闭环。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

贡献是把AI评审意见接入自主科研修订循环，并用真实投稿材料研究迭代修稿能力。

### 4.2 系统流程与组件

系统读取稿件、评审意见及可用代码，定位执行或研究构想问题并修订；新一轮审查不沿用旧裁决，比较稿件迭代前后的改进。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

评测集包括25篇拒稿和5篇边缘接收的ICLR论文，跨多个研究领域；原文同时提供公开评审及代码以支持分析。

### 5.2 基线、指标与结果

作者评估闭环修订是否解决论文中的执行与构想缺陷；结论受30篇样本及AI评审评价方式影响，不能等同于真实重投结果。

### 5.3 科学贡献与证据强度

贡献是把AI评审意见接入自主科研修订循环，并用真实投稿材料研究迭代修稿能力。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

论文以“AppliedScientist: Automated Scientific Revision Through Iterative AI Reviewing”对应的研究任务为对象，具体与哪些既有系统或基准比较，应结合其正文相关工作和实验基线判断；不把工具名称直接视为科学对象。

## 7. 局限性与风险

样本仅含ICLR论文且规模有限；AI reviewer的判断不等同于真实审稿人，也不能保证修订后的科学主张成立。

## 8. 对综述写作的价值

可用于综述“AppliedScientist: Automated Scientific Revision Through Iterative AI Reviewing”所涉及的Agent任务、研究流程和验证方式；其证据边界为本论文实际报告的任务集与实验结果。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

AppliedScientist在拒稿和边缘接收论文上测试AI审查反馈驱动的迭代修订。

### 9.2 速记版 pipeline

系统读取稿件、评审意见及可用代码，定位执行或研究构想问题并修订；新一轮审查不沿用旧裁决，比较稿件迭代前后的改进。

### 9.3 标注字段汇总

```text
paper_id=ASD-0937
inclusion_status=to_read
scientific_object_modules=01;11
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=01
module_taxonomy_codes=01.02;11.07
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`01.02.13` 机器学习；二级：`01.02`。
- 原文位置：PDF pp.4。
- 判定：Concrete experiment/task evidence supports 01.02.13 (机器学习). We curate 30 ICLR papers spanning five research domains and retain only papers with publicly available source code that can be reproduced on a single GPU within our VRAM budget.
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
