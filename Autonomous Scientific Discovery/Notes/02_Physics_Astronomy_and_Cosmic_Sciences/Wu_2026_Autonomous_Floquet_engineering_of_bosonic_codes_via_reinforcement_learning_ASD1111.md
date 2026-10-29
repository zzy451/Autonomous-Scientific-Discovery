# Autonomous Floquet engineering of bosonic codes via reinforcement learning

**论文信息**

- ID：ASD-1111
- 标题：Autonomous Floquet engineering of bosonic codes via reinforcement learning
- 作者：Zheping Wu; Lingzhen Guo; Haobin Shi; Wei-Wei Zhang
- 年份：2026
- 来源 / venue：Communications Physics
- DOI / arXiv / URL：https://doi.org/10.1038/s42005-026-02875-2
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1111.txt
- PDF / 本地文件路径：Reference_PDF/02_Physics_Astronomy_and_Cosmic_Sciences/Wu_2026_Autonomous_Floquet_engineering_of_bosonic_codes_via_reinforcement_learning_ASD1111.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 研究对象与任务 | 本文以强化学习自主设计Floquet控制波形，实现玻色子量子纠错码的制备与稳定。针对连续变量系统中非线性相互作用精确控制、退相干和动态误差等挑战，代理搜索周期驱动控制方案，并以量子态/码空间指标评估制备与抗噪表现。 | 全文TXT第91行；核验TXT行号 91 | errors. The logical code words for any q-fold rotational symmetry code can | 高（一手正文；非独立复现） |
| 系统输入及处理流程 | 强化学习策略与量子系统模拟器交互，迭代提出Floquet控制波形；环境返回制备质量、稳定性及噪声下性能，策略据此更新。 | 全文TXT第367行；核验TXT行号 367 | timescale than the Floquet adiabatic protocol. c The machine-learned driving | 高（一手正文；非独立复现） |
| 实验或验证设置 | 强化学习策略与量子系统模拟器交互，迭代提出Floquet控制波形；环境返回制备质量、稳定性及噪声下性能，策略据此更新。 | 全文TXT第550行；核验TXT行号 550 | our original trained policy. The red dashed-dotted line shows the photon number | 高（一手正文；非独立复现） |
| 作者报告的贡献 | 通过玻色子码制备任务和含噪声条件的数值模拟评估控制波形，并与参考控制策略比较。 | 全文TXT第733行；核验TXT行号 733 | based on the ﬁdelity F with the following formula, | 高（一手正文；非独立复现） |
| 适用范围与边界 | 对象明确为玻色子量子码及Floquet量子控制，属于02物理学；RL代理承担多步自主优化，是可纳入的科学实验设计案例。 | 全文TXT第916行；核验TXT行号 914 | for universal quantum computation. N. J. Phys. 16, 045014 (2014). | 高（一手正文；非独立复现） |

## 0. 摘要翻译

本文以强化学习自主设计Floquet控制波形，实现玻色子量子纠错码的制备与稳定。针对连续变量系统中非线性相互作用精确控制、退相干和动态误差等挑战，代理搜索周期驱动控制方案，并以量子态/码空间指标评估制备与抗噪表现。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。本文以强化学习自主设计Floquet控制波形，实现玻色子量子纠错码的制备与稳定。针对连续变量系统中非线性相互作用精确控制、退相干和动态误差等挑战，代理搜索周期驱动控制方案，并以量子态/码空间指标评估制备与抗噪表现。
  - 原文位置：全文TXT第91行；核验TXT行号 91；引文：errors. The logical code words for any q-fold rotational symmetry code can
- 多步行动过程：yes。强化学习策略与量子系统模拟器交互，迭代提出Floquet控制波形；环境返回制备质量、稳定性及噪声下性能，策略据此更新。
  - 原文位置：全文TXT第367行；核验TXT行号 367；引文：timescale than the Floquet adiabatic protocol. c The machine-learned driving
- 至少一种Agent能力：yes。强化学习策略与量子系统模拟器交互，迭代提出Floquet控制波形；环境返回制备质量、稳定性及噪声下性能，策略据此更新。
  - 原文位置：全文TXT第550行；核验TXT行号 550；引文：our original trained policy. The red dashed-dotted line shows the photon number
- 明确科研流程角色：yes。对象明确为玻色子量子码及Floquet量子控制，属于02物理学；RL代理承担多步自主优化，是可纳入的科学实验设计案例。
  - 原文位置：全文TXT第733行；核验TXT行号 733；引文：based on the ﬁdelity F with the following formula,

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

对象明确为玻色子量子码及Floquet量子控制，属于02物理学；RL代理承担多步自主优化，是可纳入的科学实验设计案例。

### 2.3 容易混淆的边界

对象明确为玻色子量子码及Floquet量子控制，属于02物理学；RL代理承担多步自主优化，是可纳入的科学实验设计案例。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签



### 3.2 科研流程角色



强化学习策略与量子系统模拟器交互，迭代提出Floquet控制波形；环境返回制备质量、稳定性及噪声下性能，策略据此更新。

### 3.3 自主能力

强化学习策略与量子系统模拟器交互，迭代提出Floquet控制波形；环境返回制备质量、稳定性及噪声下性能，策略据此更新。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

对象明确为玻色子量子码及Floquet量子控制，属于02物理学；RL代理承担多步自主优化，是可纳入的科学实验设计案例。

### 4.2 系统流程与组件

强化学习策略与量子系统模拟器交互，迭代提出Floquet控制波形；环境返回制备质量、稳定性及噪声下性能，策略据此更新。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

强化学习策略与量子系统模拟器交互，迭代提出Floquet控制波形；环境返回制备质量、稳定性及噪声下性能，策略据此更新。 验证以文中所列任务、数据和对照为准。

### 5.2 基线、指标与结果

通过玻色子码制备任务和含噪声条件的数值模拟评估控制波形，并与参考控制策略比较。

### 5.3 科学贡献与证据强度

对象明确为玻色子量子码及Floquet量子控制，属于02物理学；RL代理承担多步自主优化，是可纳入的科学实验设计案例。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

与一般LLM代理、科学工作流自动化及该领域既有基准/模型相关；本文的具体差异见上述任务设计和验证设置。

## 7. 局限性与风险

本文结果受其数据、模拟环境、评测指标和实验预算限制；不得将基准或仿真表现直接外推为真实部署成效。

## 8. 对综述写作的价值

可用于综述讨论该类Agent的研究对象、工作流角色和验证边界。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

本文以强化学习自主设计Floquet控制波形，实现玻色子量子纠错码的制备与稳定。针对连续变量系统中非线性相互作用精确控制、退相干和动态误差等挑战，代理搜索周期驱动控制方案，并以量子态/码空间指标评估制备与抗噪表现。

### 9.2 速记版 pipeline

强化学习策略与量子系统模拟器交互，迭代提出Floquet控制波形；环境返回制备质量、稳定性及噪声下性能，策略据此更新。

### 9.3 标注字段汇总

```text
paper_id=ASD-1111
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

- 归档分类：`02.02.06` 量子力学；二级：`02.02`。
- 原文位置：PDF p.1。
- 判定：玻色量子纠错码Floquet控制及态制备，归量子力学。
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
