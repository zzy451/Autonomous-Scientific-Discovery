# SeisEvo: Evolution of Seismic Data Reconstruction Algorithms by Agents

**论文信息**

- ID：ASD-1057
- 标题：SeisEvo: Evolution of Seismic Data Reconstruction Algorithms by Agents
- 作者：Yingjie Xu; Siwei Yu; Jianwei Ma
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2608.18272
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1057.txt
- PDF / 本地文件路径：Reference_PDF/05_Earth_and_Environmental_Sciences/Xu_2026_SeisEvo_Evolution_of_Seismic_Data_Reconstruction_Algorithms_by_Agents_ASD1057.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 地学任务 | 方法针对地震数据重建，不只优化一次输出。 | Abstract；核验TXT行号 274 | We propose SeisEvo (Seismic Algorithm Evolution), which does not optimize a single reconstruction result but searches for the algorithm that produces it. | 高（一手正文；非独立复现） |
| 程序进化 | Agent搜索从经典重建算法出发并修改开放组件。 | Abstract；核验TXT行号 276 | Starting from a classical reconstruction algorithm, an LLM-driven multi-agent search modifies only the components that the user has opened for editing | 高（一手正文；非独立复现） |
| 插值案例 | Evo-POCS在缺失率30–70%时平均SNR提高3.49 dB。 | Abstract；核验TXT行号 278 | For interpolation without added noise, the search discovered a residual-gated, phase-aligned dip-consistency projection; Evo-POCS improves the SNR over classic POCS by 3.49 dB on average across missing ratios from 30% to 70%. | 高（一手正文；非独立复现） |
| 去噪案例 | Evo-MSSA相较经典MSSA平均重建SNR提高超过7 dB。 | Abstract；核验TXT行号 282 | For simultaneous interpolation and denoising, it discovered a reliability-grouped singular-value shrinkage; Evo-MSSA improves the average reconstruction SNR by more than 7 dB over classic MSSA and by more than 3 dB over a stronger rank-reduction baseline. | 高（一手正文；非独立复现） |
| 留出验证 | 两种算法在未参与搜索的数据上保留收益。 | Abstract；核验TXT行号 285 | Both operators retain their gains on data not used during the search. | 高（一手正文；非独立复现） |
| 主控复核：具体科学对象 | POCS/MSSA算法在野外地震数据插值、去噪和留出数据上验证；地震波重建对象对应地球物理学，建议将05.01细化。算法是工具。 | TXT line 527；核验TXT行号 527 | For interpolation of a field dataset without added synthetic noise, Evo-POCS improves the SNR over classic POCS by 3.49 dB on average across missing ratios from 30% to 70%. For simultaneous interpolation and denoising, Evo-MSSA improves the mean reconstruction | 高（一手正文；非独立复现） |

## 0. 摘要翻译

SeisEvo不是Agent执行时的地震处理系统，而是用LLM多Agent搜索可部署的显式算法。它从经典POCS和MSSA重建算法出发，只修改获准开放的组件，用物理约束筛除候选、以执行得分选择算法，并在未搜索数据上验证。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。目标是为地震数据插值/去噪任务发现可解释重建算法。
  - 原文位置：Abstract；核验TXT行号 274；引文：SeisEvo (Seismic Algorithm Evolution), which does not optimize a single reconstruction result but searches for the algorithm that produces it.
- 多步行动过程：yes。多Agent反复修改允许编辑的算法组件，运行并筛选候选。
  - 原文位置：Abstract；核验TXT行号 276；引文：Starting from a classical reconstruction algorithm, an LLM-driven multi-agent search modifies only the components that the user has opened for editing
- 至少一种Agent能力：yes。无预先规定发现机制，但物理约束不合格的候选被拒绝。
  - 原文位置：Abstract；核验TXT行号 276；引文：Candidates that violate the physical constraints of the task are rejected outright, and the remaining ones are scored by execution.
- 明确科研流程角色：yes。Agent承担地震资料处理算法设计和计算测试。
  - 原文位置：Abstract；核验TXT行号 276；引文：Starting from a classical reconstruction algorithm, an LLM-driven multi-agent search modifies only the components that the user has opened for editing

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：05
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：05（仅归档，不覆盖其他模块）
- 模块内分类路径：05.01.03 地球物理学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

POCS/MSSA算法在野外地震数据插值、去噪和留出数据上验证；地震波重建对象对应地球物理学，建议将05.01细化。算法是工具。

### 2.3 容易混淆的边界

POCS/MSSA算法在野外地震数据插值、去噪和留出数据上验证；地震波重建对象对应地球物理学，建议将05.01细化。算法是工具。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM Agent；Multi-Agent System；Tool-using Agent

### 3.2 科研流程角色

hypothesis_generation；tool_use_and_code_execution；data_analysis；evidence_assessment_and_validation

LLM多Agent分工提出、修改和审查程序；代码执行器运行地震插值/去噪候选；约束检查器剔除违背任务物理条件的算法；最终输出无需Agent推理的白盒算子。

### 3.3 自主能力

无预先规定发现机制，但物理约束不合格的候选被拒绝。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

地震处理侧提出可解释的相位/可靠度门控重建算子；系统侧把程序搜索作为Agent科研任务，最终交付可检查且无推理依赖的独立算法。

### 4.2 系统流程与组件

选择POCS或MSSA基础算法和可编辑部分；Agent生成变体；以物理条件约束筛选；执行候选并评价重建质量；积累结果继续演化；将最佳算子冻结，最后在留出地震数据上测性能。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

两类数值实验：无噪声插值和插值兼去噪。比较经典POCS/MSSA及更强秩约简基线；训练搜索数据之外的留出数据用于检验泛化。

### 5.2 基线、指标与结果

作者报告Evo-POCS相对经典POCS平均SNR提升3.49 dB；Evo-MSSA相对经典MSSA提升超过7 dB，相对更强rank-reduction基线提升超过3 dB；两算法在搜索外数据维持收益。

### 5.3 科学贡献与证据强度

地震处理侧提出可解释的相位/可靠度门控重建算子；系统侧把程序搜索作为Agent科研任务，最终交付可检查且无推理依赖的独立算法。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

与深度网络把规则编码进权重不同，SeisEvo输出可检查、可修改的显式算子；与一次性数据调参相比，直接搜索生成结果的算法机制。

## 7. 局限性与风险

验证限于指定插值与去噪设置、合成/测试地震数据；输出算法部署时不再保留Agent自主性，泛化到不同采集条件仍需单独验证。

## 8. 对综述写作的价值

可用于综述Agent如何通过程序进化而非只优化单次输出，发现地震数据处理算法。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

SeisEvo通过受物理约束的Agent程序搜索发现并留出验证地震重建算子。

### 9.2 速记版 pipeline

选择POCS或MSSA基础算法和可编辑部分；Agent生成变体；以物理条件约束筛选；执行候选并评价重建质量；积累结果继续演化；将最佳算子冻结，最后在留出地震数据上测性能。

### 9.3 标注字段汇总

```text
paper_id=ASD-1057
inclusion_status=to_read
scientific_object_modules=05
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=05
module_taxonomy_codes=05.01.03
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O3 新实例 | 搜索地震数据重建算法并在数值数据验证，答案可由信号处理评分核对 | “field dataset” · L26 |
| 验证强度 | V2 计算/仿真/回顾性 | 在搜索内和留出地震数据上计算SNR验证，无物理采集实验 | “data not used during the search” · L25 |
| 系统自主性 | L2 闭环执行者 | Agent自主搜索修改算法组件并迭代评估，最终交付独立算法 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
