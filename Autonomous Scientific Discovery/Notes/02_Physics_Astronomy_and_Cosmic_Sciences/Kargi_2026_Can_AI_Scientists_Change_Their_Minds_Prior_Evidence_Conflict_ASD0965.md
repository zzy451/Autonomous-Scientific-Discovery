# Can AI Scientists Change Their Minds? Prior-Evidence Conflict in Synthetic Universes

**论文信息**

- ID：ASD-0965
- 标题：Can AI Scientists Change Their Minds? Prior-Evidence Conflict in Synthetic Universes
- 作者：Chauhan, Kargi
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2609.36726
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0965.txt
- PDF / 本地文件路径：Reference_PDF/02_Physics_Astronomy_and_Cosmic_Sciences/Kargi_2026_Can_AI_Scientists_Change_Their_Minds_Prior_Evidence_Conflict_ASD0965.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 科学对象 | 配对经典与扭曲机制的合成世界构成该文的科学评测对象。 | 本地原文 TXT 第321行；核验TXT行号 321 | Can a scientific agent distinguish a law it inferred from evidence from one it merely recognizes? We introduce Synthetic Universes, a controlled benchmark that pairs canonical famous worlds with matched twisted twins governed by nearby noncanonical mechanisms. We evaluate each reported law twice: by executing it on held-out continuations and transfer settings, and by independently checking whether it recovers the generating mechanism. In the current checkpoint of a pre-specified 60-cell study, 22 trials were graded and one additional run ended in infrastructure failure. Among 20 twin trials, 8 pass predictive verification while 5 recover the generator. The dissociation is bidirectional: six parsable outputs predict successfully while missing the mechanism, whereas three recover the mechanism but fail predictive rollout. Drag exhibits the first pattern (5/5 predictive pass, 1/5 mechanism recovery); Gravity exhibits the second (1/5 predictive pass, 4/5 mechanism recovery). Because matched famous controls, the corrected identifiability sweep, and the Evidence Ladder remain incomplete, we do not claim a confirmatory causal prior-conflict effect. Instead, the completed runs establish a narrower verification result: predictive adequacy and mechanism recovery are distinct scientific claims and require distinct tests. | 高（一手正文；非独立复现） |
| 研究方法与Agent行动 | Agent在隐藏机制条件下提交可执行定律，评测器独立检查预测与机制恢复。 | 本地原文 TXT 第349行；核验TXT行号 349 | Instance freshness alone is insufficient. A newly generated trajectory can still have a centuries-old answer strongly represented in pretraining. Synthetic Universes therefore turns prior–evidence agreement into an experimental variable. Every domain contains a canonical famous world and a nearby twisted twin. The interface stays fixed while the generating law changes. In Gravity, for example, r−2r^{-2} is paired with r−2.3r^{-2.3}. The familiar hypothesis remains plausible, but it is wrong. Fresh or dynamically generated evaluations reduce reuse of particular benchmark items, but they do not remove a model’s prior over canonical scientific answers (White et al., 2025; Li et al., 2024; Xu et al., 2024; Sainz et al., 2023). | 高（一手正文；非独立复现） |
| 实验任务与验证 | 作者说明预注册复制矩阵的完成进度，并将未完成部分排除在确认性结论之外。 | 本地原文 TXT 第394行；核验TXT行号 394 | Our benchmark asks three questions: (i) does a scientific agent behave differently when familiar knowledge conflicts with the observations; (ii) when it fails, did the experiment contain enough information to discriminate the alternative; and (iii) what additional evidence would be sufficient to move the agent away from a familiar explanation? The present submission reports the benchmark, the frozen verification taxonomy, and the completed subset of the pre-specified replication. It does not treat the unfinished matrix or planned interventions as completed confirmatory evidence. | 高（一手正文；非独立复现） |
| 主要结果 | 当前结果区分预测成功和机制识别，且样本不平衡只支持描述性报告。 | 本地原文 TXT 第744行；核验TXT行号 744 | The benchmark is model-agnostic, but the present empirical checkpoint evaluates one instantiation: a fresh tool-augmented Claude Code sub-agent with Bash, Python, NumPy, SciPy, and pandas, following the broader tool-using/experiment-agent paradigm (Schick et al., 2023; Huang et al., 2024). The single-agent design is intentional at this stage: it isolates evidence updating before introducing social dynamics from debate, critic, or consensus pipelines. The agent receives a self-contained task and observation table and may create scratch analyses. Ground-truth law metadata, graders, simulator source, and prior results are not placed in the run workspace. Because Bash executes on a shared host, this is task-level content isolation, not an OS security sandbox. Raw responses and tool traces are retained for audit. | 高（一手正文；非独立复现） |
| 研究贡献或边界 | 该段界定了先验冲突评测的问题及其当前证据边界。 | 本地原文 TXT 第830行；核验TXT行号 830 | At submission time, 23/60 headline cells had been attempted: 22 produced graded trial records and one remained a current infrastructure failure; 37 were not yet run. Two of the 22 graded records were unparseable under the frozen evaluator. The completed scientific matrix is highly imbalanced (2 famous, 20 twin), so the rates below are descriptive. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

论文提出在合成科学世界中检验AI Scientist是否能在先验知识与新证据冲突时修正观点。作者把预测能力与机制恢复分开评估，构造匹配世界、执行式预测验证和可识别性检查，并报告当前复制实验仍未完成。因此目前能支持的是评测设计及预测—机制可能分离，尚不能把先验冲突造成的效应写成已确认结论。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。基准将经典机制世界与邻近的改变机制世界配对，用于检验科学定律推断。
  - 原文位置：TXT 第321行；原文引文；核验TXT行号 321；引文：We introduce Synthetic Universes, a controlled benchmark that pairs canonical famous worlds with matched twisted twins governed by nearby noncanonical mechanisms.
- 多步行动过程：yes。受测科学Agent调用Claude Code及Python等工具分析并执行候选科学定律。
  - 原文位置：TXT 第744行；原文引文；核验TXT行号 744；引文：tool-augmented Claude Code sub-agent with Bash, Python, NumPy, SciPy, and pandas, following the broader tool-using/experiment-agent paradigm (Schick et al.
- 至少一种Agent能力：yes。Agent提交可执行定律；系统在留出延续和迁移情境中执行预测，并独立核验机制是否恢复。
  - 原文位置：TXT 第321行；原文引文；核验TXT行号 321；引文：We evaluate each reported law twice: by executing it on held-out continuations and transfer settings, and by independently checking whether it recovers the generating mechanism.
- 明确科研流程角色：yes。该单Agent流程承担计算实验角色，使用代码与数值工具检验推断出的规律。
  - 原文位置：TXT 第744行；原文引文；核验TXT行号 744；引文：tool-augmented Claude Code sub-agent with Bash, Python, NumPy, SciPy, and pandas, following the broader tool-using/experiment-agent paradigm (Schick et al.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：02
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：02（仅归档，不覆盖其他模块）
- 模块内分类路径：02.02 物理学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

- Synthetic controlled universes with held-out predictions and independent checks of generated mechanisms; current results are explicitly an incomplete checkpoint, not a confirmatory causal study.

### 2.3 容易混淆的边界

02.02对应合成物理规律、动力学方程及机制验证。该对象是基准中的科学规律，不是研究AI Agent本身；没有足够证据扩展到11方法模块。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

单Agent

### 3.2 科研流程角色

科学问题提出；实验设计；工具调用与代码执行；结果分析与验证

AI Scientist在合成世界中提出并检验机制解释；评测器分别检查未见数据预测、生成机制恢复和证据干预下的可识别性。

### 3.3 自主能力

Agent提交可执行定律；系统在留出延续和迁移情境中执行预测，并独立核验机制是否恢复。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

提出可执行的两轴科研推理评测方案；当前主要贡献是benchmark与验证方法，尚非已确立的实验科学发现。

### 4.2 系统流程与组件

输入为匹配的合成世界与隐藏规律；Agent依据候选规律进行预测并尝试恢复生成机制；执行代码验证预测与机制；评估器冻结后对正确性、可识别性及失败模式分开记分；预注册控制仍待完成。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

六类合成基准世界；可执行的外推预测和机制恢复检查；另审计基准是否可区分候选规律。当前复制与控制条件尚未全部完成。

### 5.2 基线、指标与结果

作者报告预测成功与机制正确可能双向分离，并给出错误机制仍能预测、正确规律预测失效的审计案例。关于先验—证据冲突的定量归因仍待未完成控制。

### 5.3 科学贡献与证据强度

提出可执行的两轴科研推理评测方案；当前主要贡献是benchmark与验证方法，尚非已确立的实验科学发现。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

将AI Scientist评估从答案复现推进到预测与机制解释分别验证；与方程发现、科学基准审计及模型先验研究相连。

## 7. 局限性与风险

作者明确标注复制/控制未完成，Conservation/Coupling生成器尚待非退化性审计；不可将当前观察写成因果结论。

## 8. 对综述写作的价值

可用于综述讨论科学Agent评估应将预测准确性与机制正确性分离，并报告基准可识别性及实验未完成状态。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

以合成世界检验科学Agent能否区分预测成功与机制正确。

### 9.2 速记版 pipeline

输入为匹配的合成世界与隐藏规律；Agent依据候选规律进行预测并尝试恢复生成机制；执行代码验证预测与机制；评估器冻结后对正确性、可识别性及失败模式分开记分；预注册控制仍待完成。

### 9.3 标注字段汇总

```text
paper_id=ASD-0965
inclusion_status=to_read
scientific_object_modules=02
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=02
module_taxonomy_codes=02.02
source_level=first_hand_full_text
fulltext_followup_required=true
```

### 全文后续要求

当前纳入和分类证据已足够；第7节明确的结果/复现细节仍需继续回查。


## 2026-10-29 三级分类复核

- 归档分类：`02.02.03` 经典力学；二级：`02.02`。
- 原文位置：PDF p.3。
- 判定：扭曲引力定律的轨道数据验证，支持经典力学；其他合成物理环境另标签。
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
