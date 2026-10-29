# JANUS: Enhancing Long-Horizon Autonomous Research with Co-Evolving World Models

**论文信息**

- ID：ASD-0933
- 标题：JANUS: Enhancing Long-Horizon Autonomous Research with Co-Evolving World Models
- 作者：Mengdi Liu; Chenghao Jia; Hong Chang; Mingjie He; Shiguang Shan; Xilin Chen
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2610.13194
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0933.txt
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Liu_2026_JANUS_Enhancing_Long_Horizon_Autonomous_Research_with_Co_Evolving_ASD0933.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 研究目标/科学问题 | JANUS 面向长程自主研究，提出由协同演化world model驱动的 Predict-Verify-Evolve 循环。研究Agent提出候选方案，world model预测其价值提升、信息增益和探索效用，据此选择并精炼方案；实验反馈再用于验证和演化模型。作者在包含 30 项任务的 MLS-Bench-Lite 上评估，任务覆盖 12 个领域。 | 本地全文：ASD-0933中与研究目标/科学问题直接相关的原文句子；核验TXT行号 479 | Long-horizon autonomous research has shown promise in accelerating scientific progress through sustained cycles of hypothesis generation, implementation, and validation. However, this Generate-Execute-Feedback paradigm relies on reactive trial-and-error, where costly and time-consuming executions introduce severe feedback delays, throttling evolutionary progress under explosively expanding search space. To address this challenge, we propose JANUS, a framework that unifies future outcomes forecasting and past experience reflection through a Predict-Verify-Evolve loop driven by a co-evolving world model. Within an evolving graph, the research agent proposes candidates while world model scores them by forecasting value improvement, information gain, and exploration utility, then accordingly selects, refines, or prunes branches prior to execution. After receiving ground-truth feedback, JANUS distills experiences into evolving skills: hierarchical skills for research agent, exploration-strategy skills for world model, and their coordination protocols. This mechanism enables continual co-evolution: the research agent sharpens candidate generation while the world model refines its predictive judgment over extended horizons. Extensive evaluations on MLS-Bench-Lite and real research tasks demonstrate that JANUS significantly outperforms state-of-the-art baselines, achieving both higher evolving efficiency and ceiling. | 高（一手正文；非独立复现） |
| 多步行动/研究流程 | Agent生成候选研究方案，world model预测其潜在价值与信息收益并排序；系统执行选中方案、验证预测和结果，再将经验用于演化world model及后续探索。 | 本地全文：ASD-0933中与多步行动/研究流程直接相关的原文句子；核验TXT行号 479 | Within an evolving graph, the research agent proposes candidates while world model scores them by forecasting value improvement, information gain, and exploration utility, then accordingly selects, refines, or prunes branches prior to execution. | 高（一手正文；非独立复现） |
| Agent实现与能力 | JANUS由研究Agent、协同演化world model及Predict-Verify-Evolve循环组成；模型预测候选的价值提升、信息增益和探索效用，并从验证反馈中更新。 | 本地全文：ASD-0933中与Agent实现与能力直接相关的原文句子；核验TXT行号 479 | After receiving ground-truth feedback, JANUS distills experiences into evolving skills: hierarchical skills for research agent, exploration-strategy skills for world model, and their coordination protocols. | 高（一手正文；非独立复现） |
| 实验任务与验证设置 | 主要评估使用 MLS-Bench-Lite 的 30 项研究任务，覆盖 12 个领域；每项任务要求改善机器学习系统的目标组件并检查改进能否跨受控设置泛化。 | 本地全文：ASD-0933中与实验任务与验证设置直接相关的原文句子；核验TXT行号 1390 | We primarily evaluate JANUS on MLS-Bench-Lite Lyu et al. (2026a), comprising 30 research tasks across 12 domains. Each task requires agents to improve one targeted component of an ML system and demonstrate the improvement generalizes across controlled settings. To further examine JANUS’s capacity for end-to-end discovery in real-world research, we consider three additional tasks: nanoGPT training optimization from AutoResearch Karpathy (2026), MinGPT attention kernel optimization from KernelBench Ouyang et al. (2025), and genotype-to-phenotype prediction task from real world. Together, these tasks span algorithm optimization, system design, and scientific discovery. Detailed task descriptions are provided in Appendix C. | 高（一手正文；非独立复现） |
| 作者报告的结果/贡献 | 作者以 MLS-Bench-Lite 比较 JANUS 与多种研究Agent基线，报告提交有效率、胜过基线比例及开发/测试得分。结果须按表1的模型与基线配置解读。 贡献是让Agent显式预测候选的价值、信息增益和探索效用，并通过验证反馈共同演化研究策略与world model。 | 本地全文中包含该原句的位置；核验TXT行号 1471 | We first evaluate JANUS on MLS-Bench-Lite under controlled protocol, with the primary results reported in Table 1. We highlight the following: (1) JANUS outperforms all baselines across six evaluation metrics, demonstrating the superior efficacy of our Predict-Verify-Evolve loop in systematically driving meaningful progress. (2) JANUS achieves 100.0% valid improvements upon its weakest human baseline and surpasses all provided human baselines on 43.3% of tasks, establishing a level of performance that directly rivals human expert standards. (3) JANUS demonstrates robust backbone generality, consistently maintaining its performance advantage across different base model backbones. Moreover, its modular architecture is fully compatible with existing harnesses; when integrating our loop with Codex, the framework achieves a peak score of 49.78. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

JANUS 面向长程自主研究，提出由协同演化world model驱动的 Predict-Verify-Evolve 循环。研究Agent提出候选方案，world model预测其价值提升、信息增益和探索效用，据此选择并精炼方案；实验反馈再用于验证和演化模型。作者在包含 30 项任务的 MLS-Bench-Lite 上评估，任务覆盖 12 个领域。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。JANUS 面向长程自主研究，提出由协同演化world model驱动的 Predict-Verify-Evolve 循环。研究Agent提出候选方案，world model预测其价值提升、信息增益和探索效用，据此选择并精炼方案；实验反馈再用于验证和演化模型。作者在包含 30 项任务的 MLS-Bench-Lite 上评估，任务覆盖 12 个领域。
  - 原文位置：本地全文：ASD-0933中与研究目标/科学问题直接相关的原文句子；核验TXT行号 479；引文：Long-horizon autonomous research has shown promise in accelerating scientific progress through sustained cycles of hypothesis generation, implementation, and validation. However, this Generate-Execute-Feedback paradigm relies on reactive trial-and-error, where costly and time-consuming executions introduce severe feedback delays, throttling evolutionary progress under explosively expanding search space. To address this challenge, we propose JANUS, a framework that unifies future outcomes forecasting and past experience reflection through a Predict-Verify-Evolve loop driven by a co-evolving world model. Within an evolving graph, the research agent proposes candidates while world model scores them by forecasting value improvement, information gain, and exploration utility, then accordingly selects, refines, or prunes branches prior to execution. After receiving ground-truth feedback, JANUS distills experiences into evolving skills: hierarchical skills for research agent, exploration-strategy skills for world model, and their coordination protocols. This mechanism enables continual co-evolution: the research agent sharpens candidate generation while the world model refines its predictive judgment over extended horizons. Extensive evaluations on MLS-Bench-Lite and real research tasks demonstrate that JANUS significantly outperforms state-of-the-art baselines, achieving both higher evolving efficiency and ceiling.
- 多步行动过程：yes。Agent生成候选研究方案，world model预测其潜在价值与信息收益并排序；系统执行选中方案、验证预测和结果，再将经验用于演化world model及后续探索。
  - 原文位置：本地全文：ASD-0933中与多步行动/研究流程直接相关的原文句子；核验TXT行号 479；引文：Within an evolving graph, the research agent proposes candidates while world model scores them by forecasting value improvement, information gain, and exploration utility, then accordingly selects, refines, or prunes branches prior to execution.
- 至少一种Agent能力：yes。JANUS由研究Agent、协同演化world model及Predict-Verify-Evolve循环组成；模型预测候选的价值提升、信息增益和探索效用，并从验证反馈中更新。
  - 原文位置：本地全文：ASD-0933中与Agent实现与能力直接相关的原文句子；核验TXT行号 479；引文：After receiving ground-truth feedback, JANUS distills experiences into evolving skills: hierarchical skills for research agent, exploration-strategy skills for world model, and their coordination protocols.
- 明确科研流程角色：yes。主要评估使用 MLS-Bench-Lite 的 30 项研究任务，覆盖 12 个领域；每项任务要求改善机器学习系统的目标组件并检查改进能否跨受控设置泛化。
  - 原文位置：本地全文：ASD-0933中与实验任务与验证设置直接相关的原文句子；核验TXT行号 1390；引文：We primarily evaluate JANUS on MLS-Bench-Lite Lyu et al. (2026a), comprising 30 research tasks across 12 domains. Each task requires agents to improve one targeted component of an ML system and demonstrate the improvement generalizes across controlled settings. To further examine JANUS’s capacity for end-to-end discovery in real-world research, we consider three additional tasks: nanoGPT training optimization from AutoResearch Karpathy (2026), MinGPT attention kernel optimization from KernelBench Ouyang et al. (2025), and genotype-to-phenotype prediction task from real world. Together, these tasks span algorithm optimization, system design, and scientific discovery. Detailed task descriptions are provided in Appendix C.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：01;06
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：01（仅归档，不覆盖其他模块）
- 模块内分类路径：01.02 计算机科学；06.01.06 遗传学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

对象模块与代码沿用输入审计记录（01, 06；01.02, 06.01.06）；是否纳入与对象分类分开判断。

### 2.3 容易混淆的边界

对象模块与代码沿用输入审计记录（01, 06；01.02, 06.01.06）；是否纳入与对象分类分开判断。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

自主科研Agent

### 3.2 科研流程角色

科研问题处理；多步行动或评测

JANUS由研究Agent、协同演化world model及Predict-Verify-Evolve循环组成；模型预测候选的价值提升、信息增益和探索效用，并从验证反馈中更新。

### 3.3 自主能力

JANUS由研究Agent、协同演化world model及Predict-Verify-Evolve循环组成；模型预测候选的价值提升、信息增益和探索效用，并从验证反馈中更新。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

贡献是让Agent显式预测候选的价值、信息增益和探索效用，并通过验证反馈共同演化研究策略与world model。

### 4.2 系统流程与组件

Agent生成候选研究方案，world model预测其潜在价值与信息收益并排序；系统执行选中方案、验证预测和结果，再将经验用于演化world model及后续探索。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

主要评估使用 MLS-Bench-Lite 的 30 项研究任务，覆盖 12 个领域；每项任务要求改善机器学习系统的目标组件并检查改进能否跨受控设置泛化。

### 5.2 基线、指标与结果

作者以 MLS-Bench-Lite 比较 JANUS 与多种研究Agent基线，报告提交有效率、胜过基线比例及开发/测试得分。结果须按表1的模型与基线配置解读。

### 5.3 科学贡献与证据强度

贡献是让Agent显式预测候选的价值、信息增益和探索效用，并通过验证反馈共同演化研究策略与world model。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

论文以“JANUS: Enhancing Long-Horizon Autonomous Research with Co-Evolving World Models”对应的研究任务为对象，具体与哪些既有系统或基准比较，应结合其正文相关工作和实验基线判断；不把工具名称直接视为科学对象。

## 7. 局限性与风险

world model预测质量依赖任务分布和已积累经验；MLS-Bench-Lite 的任务范围不能代表无界开放式科学发现。

## 8. 对综述写作的价值

可用于综述“JANUS: Enhancing Long-Horizon Autonomous Research with Co-Evolving World Models”所涉及的Agent任务、研究流程和验证方式；其证据边界为本论文实际报告的任务集与实验结果。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

JANUS 用协同演化world model预测研究候选效用，并在MLS-Bench-Lite 30项任务上评估。

### 9.2 速记版 pipeline

Agent生成候选研究方案，world model预测其潜在价值与信息收益并排序；系统执行选中方案、验证预测和结果，再将经验用于演化world model及后续探索。

### 9.3 标注字段汇总

```text
paper_id=ASD-0933
inclusion_status=to_read
scientific_object_modules=01;06
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=01
module_taxonomy_codes=01.02;06.01.06
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`01.02.13` 机器学习；二级：`01.02`。
- 原文位置：PDF pp.7。
- 判定：Concrete experiment/task evidence supports 01.02.13 (机器学习). Table 1: Overall performance on MLS-Bench-Lite. Beat Any, Beat Median, and Beat All denote the percentages of tasks that outperform at least one, the median-performing, and all provided human baselines, respectively.
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
