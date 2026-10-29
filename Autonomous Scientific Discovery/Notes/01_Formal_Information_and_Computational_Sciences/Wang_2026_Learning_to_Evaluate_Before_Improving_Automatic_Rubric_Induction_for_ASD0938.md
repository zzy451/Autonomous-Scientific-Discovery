# Learning to Evaluate Before Improving: Automatic Rubric Induction for Automatic Research Agents

**论文信息**

- ID：ASD-0938
- 标题：Learning to Evaluate Before Improving: Automatic Rubric Induction for Automatic Research Agents
- 作者：Xuehai Wang; Haowei Qin; Tongxin Liu; Junkai Li; Buqiang Xu; Jintian Zhang; Yijun Chen; Zirui Xue; Shumin Deng
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2608.31076
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0938.txt
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Wang_2026_Learning_to_Evaluate_Before_Improving_Automatic_Rubric_Induction_for_ASD0938.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 研究目标/科学问题 | AutoSciRub在科研执行前为开放任务诱导任务专属、可执行rubric，并将其用于执行指导、criterion级核验和产物/报告迭代修订。框架把宽泛任务拆成原子科学目标，以相关文献和任务可见数据为依据生成标准。作者在ResearchClawBench的40项任务及AstaBench的20项端到端发现任务上评估。 | 本地全文：ASD-0938中与研究目标/科学问题直接相关的原文句子；核验TXT行号 336 | Autonomous scientific research agents are increasingly applied to end-to-end scientific workflows, including literature review, data analysis, experimentation, and report generation. However, open-ended research tasks often do not clearly specify the analyses, methods, and success criteria required to complete the task. As a result, agents may miss important analyses, use inappropriate methods, or draw conclusions that are insufficiently supported by evidence. To address the problem, we present AutoSciRub, an evaluation-first framework that induces a task-specific executable rubric before research execution, and uses it to guide execution, criterion-level verification as well as iterative revision. AutoSciRub decomposes an underspecified instruction into atomic scientific goals, grounds them in relevant literature and task-visible data, and synthesizes specific, actionable, and verifiable criteria. The resulting rubric makes implicit experimental and evidential requirements explicit, providing guidance for experiments and analyses. During revision, rubric-guided verification identifies unmet criteria and enables targeted refinement of the research report and its supporting artifacts. On ResearchClawBench, AutoSciRub consistently improves all tested configurations, with an average gain of 2.08 points across three backbone LLMs under the fixed Codex harness and 2.95 points across three agent harnesses using a fixed DeepSeek-V4-Flash backbone. On a randomly sampled 20-task subset of AstaBench E2E Discovery, AutoSciRub further achieves an average improvement of 16.8 points across three agent harnesses, while maintaining or increasing the number of successfully completed tasks. These results demonstrate that evaluation-first guidance provides an effective and generalizable control mechanism for autonomous scientific research11 1 The code is available at https://github.com/zjunlp/AutoSciRub.. | 高（一手正文；非独立复现） |
| 多步行动/研究流程 | 系统将不充分指定的指令拆为原子目标，依据文献和任务数据生成criterion；Agent执行研究后逐项验证证据，并据差距迭代修订成果。 | 本地全文：ASD-0938中与多步行动/研究流程直接相关的原文句子；核验TXT行号 559 | Since neither 𝒵i∗\mathcal{Z}_{i}^{*} nor its evaluator is available during execution, AutoSciRub induces an instruction-derived rubric skeleton 𝒢^i\widehat{\mathcal{G}}_{i} and a task-specific executable rubric ℛ^i\widehat{\mathcal{R}}_{i} from the instruction, scientific literature, and task-visible data. The rubric operationalizes the latent specification and guides execution, criterion-level verification, and iterative revision. | 高（一手正文；非独立复现） |
| Agent实现与能力 | AutoSciRub是评价优先的科研Agent框架，先诱导可执行rubric，再用标准控制科研执行、逐项验证及修订。 | 本地全文：ASD-0938中与Agent实现与能力直接相关的原文句子；核验TXT行号 337 | To address the problem, we present AutoSciRub, an evaluation-first framework that induces a task-specific executable rubric before research execution, and uses it to guide execution, criterion-level verification as well as iterative revision. | 高（一手正文；非独立复现） |
| 实验任务与验证设置 | 评估覆盖ResearchClawBench全部40项任务和AstaBench固定的20项端到端科学发现任务，并使用三种骨干LLM比较平均改进。 | 本地全文：ASD-0938中与实验任务与验证设置直接相关的原文句子；核验TXT行号 421 | We evaluate AutoSciRub on all 40 tasks in ResearchClawBench and a fixed subset of 20 end-to-end scientific discovery tasks from AstaBench. On ResearchClawBench, AutoSciRub yields an average improvement of 2.08 points across three backbone LLMs under the fixed Codex harness and 2.95 points across three agent harnesses using the fixed DeepSeek-V4-Flash backbone. On AstaBench, it further improves scores by an average of 16.8 points across three agent systems. These results demonstrate that automatically induced, evidence-grounded rubrics can provide scalable evaluation criteria while also serving as effective guidance for autonomous scientific research. | 高（一手正文；非独立复现） |
| 作者报告的结果/贡献 | 作者报告ResearchClawBench上跨三种骨干LLM平均提升2.08分，并在AstaBench进行泛化评估；分数依赖论文规定的rubric和任务集。 贡献是将任务专属标准生成置于研究执行之前，使Agent能针对缺失分析和证据不足进行过程验证。 | 本地全文中包含该原句的位置；核验TXT行号 422 | On ResearchClawBench, AutoSciRub yields an average improvement of 2.08 points across three backbone LLMs under the fixed Codex harness and 2.95 points across three agent harnesses using the fixed DeepSeek-V4-Flash backbone. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

AutoSciRub在科研执行前为开放任务诱导任务专属、可执行rubric，并将其用于执行指导、criterion级核验和产物/报告迭代修订。框架把宽泛任务拆成原子科学目标，以相关文献和任务可见数据为依据生成标准。作者在ResearchClawBench的40项任务及AstaBench的20项端到端发现任务上评估。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。AutoSciRub在科研执行前为开放任务诱导任务专属、可执行rubric，并将其用于执行指导、criterion级核验和产物/报告迭代修订。框架把宽泛任务拆成原子科学目标，以相关文献和任务可见数据为依据生成标准。作者在ResearchClawBench的40项任务及AstaBench的20项端到端发现任务上评估。
  - 原文位置：本地全文：ASD-0938中与研究目标/科学问题直接相关的原文句子；核验TXT行号 336；引文：Autonomous scientific research agents are increasingly applied to end-to-end scientific workflows, including literature review, data analysis, experimentation, and report generation. However, open-ended research tasks often do not clearly specify the analyses, methods, and success criteria required to complete the task. As a result, agents may miss important analyses, use inappropriate methods, or draw conclusions that are insufficiently supported by evidence. To address the problem, we present AutoSciRub, an evaluation-first framework that induces a task-specific executable rubric before research execution, and uses it to guide execution, criterion-level verification as well as iterative revision. AutoSciRub decomposes an underspecified instruction into atomic scientific goals, grounds them in relevant literature and task-visible data, and synthesizes specific, actionable, and verifiable criteria. The resulting rubric makes implicit experimental and evidential requirements explicit, providing guidance for experiments and analyses. During revision, rubric-guided verification identifies unmet criteria and enables targeted refinement of the research report and its supporting artifacts. On ResearchClawBench, AutoSciRub consistently improves all tested configurations, with an average gain of 2.08 points across three backbone LLMs under the fixed Codex harness and 2.95 points across three agent harnesses using a fixed DeepSeek-V4-Flash backbone. On a randomly sampled 20-task subset of AstaBench E2E Discovery, AutoSciRub further achieves an average improvement of 16.8 points across three agent harnesses, while maintaining or increasing the number of successfully completed tasks. These results demonstrate that evaluation-first guidance provides an effective and generalizable control mechanism for autonomous scientific research11 1 The code is available at https://github.com/zjunlp/AutoSciRub..
- 多步行动过程：yes。系统将不充分指定的指令拆为原子目标，依据文献和任务数据生成criterion；Agent执行研究后逐项验证证据，并据差距迭代修订成果。
  - 原文位置：本地全文：ASD-0938中与多步行动/研究流程直接相关的原文句子；核验TXT行号 559；引文：Since neither 𝒵i∗\mathcal{Z}_{i}^{*} nor its evaluator is available during execution, AutoSciRub induces an instruction-derived rubric skeleton 𝒢^i\widehat{\mathcal{G}}_{i} and a task-specific executable rubric ℛ^i\widehat{\mathcal{R}}_{i} from the instruction, scientific literature, and task-visible data. The rubric operationalizes the latent specification and guides execution, criterion-level verification, and iterative revision.
- 至少一种Agent能力：yes。AutoSciRub是评价优先的科研Agent框架，先诱导可执行rubric，再用标准控制科研执行、逐项验证及修订。
  - 原文位置：本地全文：ASD-0938中与Agent实现与能力直接相关的原文句子；核验TXT行号 337；引文：To address the problem, we present AutoSciRub, an evaluation-first framework that induces a task-specific executable rubric before research execution, and uses it to guide execution, criterion-level verification as well as iterative revision.
- 明确科研流程角色：yes。评估覆盖ResearchClawBench全部40项任务和AstaBench固定的20项端到端科学发现任务，并使用三种骨干LLM比较平均改进。
  - 原文位置：本地全文：ASD-0938中与实验任务与验证设置直接相关的原文句子；核验TXT行号 421；引文：We evaluate AutoSciRub on all 40 tasks in ResearchClawBench and a fixed subset of 20 end-to-end scientific discovery tasks from AstaBench. On ResearchClawBench, AutoSciRub yields an average improvement of 2.08 points across three backbone LLMs under the fixed Codex harness and 2.95 points across three agent harnesses using the fixed DeepSeek-V4-Flash backbone. On AstaBench, it further improves scores by an average of 16.8 points across three agent systems. These results demonstrate that automatically induced, evidence-grounded rubrics can provide scalable evaluation criteria while also serving as effective guidance for autonomous scientific research.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：01
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：01（仅归档，不覆盖其他模块）
- 模块内分类路径：01.02 计算机科学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

对象模块与代码沿用输入审计记录（01；01.02）；是否纳入与对象分类分开判断。

### 2.3 容易混淆的边界

对象模块与代码沿用输入审计记录（01；01.02）；是否纳入与对象分类分开判断。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

自主科研Agent

### 3.2 科研流程角色

科研问题处理；多步行动或评测

AutoSciRub是评价优先的科研Agent框架，先诱导可执行rubric，再用标准控制科研执行、逐项验证及修订。

### 3.3 自主能力

AutoSciRub是评价优先的科研Agent框架，先诱导可执行rubric，再用标准控制科研执行、逐项验证及修订。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

贡献是将任务专属标准生成置于研究执行之前，使Agent能针对缺失分析和证据不足进行过程验证。

### 4.2 系统流程与组件

系统将不充分指定的指令拆为原子目标，依据文献和任务数据生成criterion；Agent执行研究后逐项验证证据，并据差距迭代修订成果。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

评估覆盖ResearchClawBench全部40项任务和AstaBench固定的20项端到端科学发现任务，并使用三种骨干LLM比较平均改进。

### 5.2 基线、指标与结果

作者报告ResearchClawBench上跨三种骨干LLM平均提升2.08分，并在AstaBench进行泛化评估；分数依赖论文规定的rubric和任务集。

### 5.3 科学贡献与证据强度

贡献是将任务专属标准生成置于研究执行之前，使Agent能针对缺失分析和证据不足进行过程验证。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

论文以“Learning to Evaluate Before Improving: Automatic Rubric Induction for Automatic Research Agents”对应的研究任务为对象，具体与哪些既有系统或基准比较，应结合其正文相关工作和实验基线判断；不把工具名称直接视为科学对象。

## 7. 局限性与风险

自动rubric会继承文献抽取和标准生成错误；基准分数不代表所有开放式任务都能被充分形式化。

## 8. 对综述写作的价值

可用于综述“Learning to Evaluate Before Improving: Automatic Rubric Induction for Automatic Research Agents”所涉及的Agent任务、研究流程和验证方式；其证据边界为本论文实际报告的任务集与实验结果。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

AutoSciRub先生成可执行评价标准，再指导Agent研究、验证和迭代修订。

### 9.2 速记版 pipeline

系统将不充分指定的指令拆为原子目标，依据文献和任务数据生成criterion；Agent执行研究后逐项验证证据，并据差距迭代修订成果。

### 9.3 标注字段汇总

```text
paper_id=ASD-0938
inclusion_status=to_read
scientific_object_modules=01
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=01
module_taxonomy_codes=01.02
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`01.02.12` 人工智能；二级：`01.02`。
- 原文位置：PDF p.1。
- 判定：研究Agent的可执行rubric诱导及对照实验直接测量AI研究能力。
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
