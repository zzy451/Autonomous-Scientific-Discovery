# Triage-PiEvo: Evidence Admission for Principle-Evolving Scientific Agents

**论文信息**

- ID：ASD-0962
- 标题：Triage-PiEvo: Evidence Admission for Principle-Evolving Scientific Agents
- 作者：Peize Li; Yingming Pu; Xingguo Xu; Yiming Cui; Yuansheng Gao; Tao Lin
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2610.14683
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0962.txt
- PDF / 本地文件路径：Reference_PDF/03_Chemical_Sciences/Li_2026_Triage_PiEvo_Evidence_Admission_for_Principle_Evolving_Scientific_Agents_ASD0962.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 纳入判断：论文直接研究科研Agent或其评测。 | Triage-PiEvo处理科学Agent无法判断异常观测来自新机制还是评价伪象的问题。异常可立即影响搜索，但只有独立验证证据才能改写持久原则，且与留出证据冲突的原则会撤回。 | TXT line 290；核验TXT行号 290 | Large language model (LLM)-based AI Scientists advance scientific discovery, yet they suffer from inefficiencies due to noisy observations. Existing principle-evolving agents act on every anomaly, leaving its source unresolved: a new mechanism or an evaluation artifact, so invalid revisions bias evolution. | 高（一手正文；非独立复现） |
| 对象证据：正文界定科学问题及研究对象。 | 正文在四种具体优化任务上评估Agent：分子生物活性与过渡金属配合物涉及化学对象，纳米螺旋与超导涉及纳米/材料对象；按对象覆盖化学03、材料04及药物发现07。 | TXT line 756；核验TXT行号 756 | on four optimization tasks: Molecular Bio-activity (MBO), Nanohelix (NHO), Superconductor (SPO), and Transition Metal Complex (TMC). | 高（一手正文；非独立复现） |
| 方法证据：全文描述Agent操作或评测流程。 | 作者在四类科学优化任务及三种LLM骨干上测量质量、效率、候选覆盖和成本；另设评价器污染、隐藏异常源、机制反转、代理指标利用等压力测试并作消融。各项比较使用预设的评测条件。 | TXT line 471；核验TXT行号 471 | This separation is implemented as a feedback loop with three components: (a) an evidence-admission layer checks whether an unexpected outcome generalizes to held-out cases (Section 3.2), (b) a search policy proposes experiments from outcomes that have been admitted for exploration (Section 3.3), and (c) a principle manager then updates the principle state accordingly (Section 3.4). | 高（一手正文；非独立复现） |
| 验证证据：实验报告任务、数据与验证设计。 | 系统贡献是分离“异常用于探索”和“异常足以更新知识”，控制持久原则的更新及撤回；任务结果支持该证据门控机制的效用。 | TXT line 743；核验TXT行号 743 | We evaluate Triage-PiEvo along four axes: (1) matched downstream performance across four scientific discovery tasks under three backbone LLMs; (2) search efficiency in optimization speed, candidate coverage, and computational cost; (3) controlled stress tests of the admission gate under evaluator corruption, hidden anomaly sources, mechanism reversal, proxy exploitation, and cross-harness deployment; and (4) ablations isolating search expansion from evidence admission. | 高（一手正文；非独立复现） |
| 结果贡献：正文报告可核查结果和贡献。 | 实际对象为四类科学优化任务，归入03；一般Agent知识更新是方法特点。 | TXT line 1600；核验TXT行号 1600 | An anomalous residual is source-ambiguous: new mechanisms and evaluation artifacts produce identical surprisal. Triage separates the two uses of such evidence: observations steer search immediately, while persistent principles require independent held-out support and are retracted on held-out contradiction. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

Triage-PiEvo处理科学Agent无法判断异常观测来自新机制还是评价伪象的问题。异常可立即影响搜索，但只有独立验证证据才能改写持久原则，且与留出证据冲突的原则会撤回。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。正文提出科学研究或科学评测目标。
  - 原文位置：TXT line 290；核验TXT行号 290；引文：Large language model (LLM)-based AI Scientists advance scientific discovery, yet they suffer from inefficiencies due to noisy observations. Existing principle-evolving agents act on every anomaly, leaving its source unresolved: a new mechanism or an evaluation artifact, so invalid revisions bias evolution.
- 多步行动过程：yes。正文描述多阶段行动及反馈流程。
  - 原文位置：TXT line 292；核验TXT行号 292；引文：To address this, we formulate revision as evidence admission: anomalies steer search immediately, but only independently verified evidence may rewrite persistent principles, and contradicted principles are retracted.
- 至少一种Agent能力：yes。正文显示Agent使用工具、状态或证据进行决策。
  - 原文位置：TXT line 471；核验TXT行号 471；引文：This separation is implemented as a feedback loop with three components: (a) an evidence-admission layer checks whether an unexpected outcome generalizes to held-out cases (Section 3.2), (b) a search policy proposes experiments from outcomes that have been admitted for exploration (Section 3.3), and (c) a principle manager then updates the principle state accordingly (Section 3.4).
- 明确科研流程角色：yes。系统承担科研执行、理论发现或科研评价角色。
  - 原文位置：TXT line 743；核验TXT行号 743；引文：We evaluate Triage-PiEvo along four axes: (1) matched downstream performance across four scientific discovery tasks under three backbone LLMs; (2) search efficiency in optimization speed, candidate coverage, and computational cost; (3) controlled stress tests of the admission gate under evaluator corruption, hidden anomaly sources, mechanism reversal, proxy exploitation, and cross-harness deployment; and (4) ablations isolating search expansion from evidence admission.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：03;04;07
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：03（仅归档，不覆盖其他模块）
- 模块内分类路径：03.02 基础化学；03.04 分子设计与化学空间探索；04.01 材料基础；04.03 软物质与功能材料；04.04 能源、电子与器件材料；07.04.01 药物发现
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

MBO对应分子活性/药物发现（03.04、07.04.01）；TMC对应化学配位/过渡金属对象（03.02）；Nanohelix对应纳米材料（04.03）；Superconductor对应材料物理及能源电子材料（04.01、04.04）。方法的证据门控是副属性，不替代这些任务对象模块。

### 2.3 容易混淆的边界

MBO对应分子活性/药物发现（03.04、07.04.01）；TMC对应化学配位/过渡金属对象（03.02）；Nanohelix对应纳米材料（04.03）；Superconductor对应材料物理及能源电子材料（04.01、04.04）。方法的证据门控是副属性，不替代这些任务对象模块。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

科学发现Agent；语言模型Agent

### 3.2 科研流程角色

实验设计；证据验证；知识更新

系统包含证据准入层、实验搜索策略和原则管理器；主历史保存供探索的观测，验证历史记录独立检查。候选原则须获留出案例支持才可接受。

### 3.3 自主能力

正文显示Agent使用工具、状态或证据进行决策。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

相较一般自我纠错，本文将独立留出验证绑定到持久科学原则的更新权限。

### 4.2 系统流程与组件

作者在四类科学优化任务及三种LLM骨干上测量质量、效率、候选覆盖和成本；另设评价器污染、隐藏异常源、机制反转、代理指标利用等压力测试并作消融。各项比较使用预设的评测条件。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

摘要报告四任务三骨干平均质量较最强基线高7.5%至11.8%；构造测试未接纳受污染或利用型证据且未漏掉植入机制，接入三个框架后错误准入下降超过60%。

### 5.2 基线、指标与结果

系统贡献是分离“异常用于探索”和“异常足以更新知识”，控制持久原则的更新及撤回；任务结果支持该证据门控机制的效用。

### 5.3 科学贡献与证据强度

相较一般自我纠错，本文将独立留出验证绑定到持久科学原则的更新权限。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

评测依赖构造压力测试、特定优化任务和指定模型；跨框架结果不足以证明对所有科学领域均有效。

## 7. 局限性与风险

实际对象为四类科学优化任务，归入03；一般Agent知识更新是方法特点。

## 8. 对综述写作的价值

Triage-PiEvo在科学优化Agent中将异常搜索和原则更新分开治理，并以多任务对照及压力测试检验证据准入。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

Triage-PiEvo在科学优化Agent中将异常搜索和原则更新分开治理，并以多任务对照及压力测试检验证据准入。

### 9.2 速记版 pipeline

作者在四类科学优化任务及三种LLM骨干上测量质量、效率、候选覆盖和成本；另设评价器污染、隐藏异常源、机制反转、代理指标利用等压力测试并作消融。各项比较使用预设的评测条件。

### 9.3 标注字段汇总

```text
paper_id=ASD-0962
inclusion_status=to_read
scientific_object_modules=03;04;07
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=03
module_taxonomy_codes=03.02;03.04;04.01;04.03;04.04;07.04.01
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`03.02.07` 配位化学；二级：`03.02`。
- 原文位置：PDF pp.6,7,8。
- 判定：Concrete experiment/task evidence supports 03.02.07 (配位化学). we evaluate TRIAGE-PIEVO on four optimization tasks ... Transition Metal Complex (TMC); Table 1 ... Triage-PiEvo ... TMC 81.50±4.02
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
