# LATHE: LAnguage-driven Toolkit for Hypothesis-based crystal Editing

**论文信息**

- ID：ASD-1005
- 标题：LATHE: LAnguage-driven Toolkit for Hypothesis-based crystal Editing
- 作者：Qianyu Zheng; Shuyi Jia; Victor Fung
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2610.02671
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1005.txt
- PDF / 本地文件路径：Reference_PDF/04_Materials_Science/Zheng_2026_LATHE_LAnguage_driven_Toolkit_for_Hypothesis_based_crystal_Editing_ASD1005.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| LATHE把七类晶体几何/结构性质表示为可优化目标。 | LATHE把七类晶体几何/结构性质表示为可优化目标。 | Abstract；核验TXT行号 322 | We present LATHE, a geometric toolkit that closes this gap by expressing seven classes of crystallographic properties — bond length, bond angle, dihedral angle, coordination environment, lattice parameters, cell volume, and space group, as differenti | 高（一手正文；非独立复现） |
| 假设Agent把语言提出的结构修改交由LATHE配置为梯度优化，并依据目标性质评估结构。 | 假设Agent把语言提出的结构修改交由LATHE配置为梯度优化，并依据目标性质评估结构。 | Methods；核验TXT行号 360 | Hypothesis Agent proposes geometric modifications in natural language and the LATHE-equipped Agent translates each proposal into a configuration for gradient-based optimization; the resulting structure is evaluated for the target property, and the (h | 高（一手正文；非独立复现） |
| 作者在操作与设计两种约束设置下评估带隙优化。 | 作者在操作与设计两种约束设置下评估带隙优化。 | Results；核验TXT行号 658 | We evaluate band-gap optimization under two settings of increasing physical constraints: manipulation and design. The manipulation setting is a test of whether the agentic system can simply find a configuration of atomic positions and lattice paramet | 高（一手正文；非独立复现） |
| 实验以直接生成CIF和Claude Code作为替代方案比较。 | 实验以直接生成CIF和Claude Code作为替代方案比较。 | Results；核验TXT行号 841 | we evaluated the performance of two alternative approaches. (1) Direct CIF generation: we instruct the LLM (gpt-4o) to directly generate the CIF representation of the transformed structure given the input CIF and the task prompt. (2) Claude Code: we | 高（一手正文；非独立复现） |
| 作者指出可行性预筛选可提前发现互不兼容的几何或对称约束。 | 作者指出可行性预筛选可提前发现互不兼容的几何或对称约束。 | Discussion；核验TXT行号 1135 | Future work could add a feasibility pre-screening step, for instance using cheap geometric or symmetry-based heuristics to flag jointly unsatisfiable constraint sets before optimization begins, or to suggest relaxed targets when a strict combination | 高（一手正文；非独立复现） |

## 0. 摘要翻译

论文提出LATHE晶体几何编辑工具，将键长、键角、二面角、配位、晶格参数、晶胞体积和空间群编码为可微优化目标。假设Agent提出修改，LATHE Agent执行优化并依据结构与目标性质反馈继续迭代。作者以带隙设计任务评估，并与直接CIF生成等方法比较。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。研究目标是按指定约束编辑晶体几何和带隙等材料性质，作者以受约束带隙设计任务评估LATHE。
  - 原文位置：Abstract；核验TXT行号 322；引文：We present LATHE, a geometric toolkit that closes this gap by expressing seven classes of crystallographic properties — bond length, bond angle, dihedral angle, coordination environment, lattice parameters, cell volume, and space group, as differenti
- 多步行动过程：yes。假设Agent先提出自然语言几何改动，LATHE工具将其配置为梯度优化，系统检查生成结构与目标性质后迭代。
  - 原文位置：Methods；核验TXT行号 360；引文：Hypothesis Agent proposes geometric modifications in natural language and the LATHE-equipped Agent translates each proposal into a configuration for gradient-based optimization; the resulting structure is evaluated for the target property, and the (h
- 至少一种Agent能力：yes。Agent可调用LATHE将结构修改转为几何/晶格参数优化，并在操作与设计两种物理约束设置下完成设计任务。
  - 原文位置：Results；核验TXT行号 658；引文：We evaluate band-gap optimization under two settings of increasing physical constraints: manipulation and design. The manipulation setting is a test of whether the agentic system can simply find a configuration of atomic positions and lattice paramet
- 明确科研流程角色：yes。系统承担材料设计流程中的晶体结构编辑和性质优化；作者还将其与直接CIF生成和Claude Code方案比较。
  - 原文位置：Results；核验TXT行号 841；引文：we evaluated the performance of two alternative approaches. (1) Direct CIF generation: we instruct the LLM (gpt-4o) to directly generate the CIF representation of the transformed structure given the input CIF and the task prompt. (2) Claude Code: we

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：04
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：04（仅归档，不覆盖其他模块）
- 模块内分类路径：04.02 结构材料与无机材料；04.04 能源、电子与器件材料
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

保留候选并按晶体结构设计归入04.02，带隙导向的功能材料设计也支持04.04；结论限于计算闭环与所测约束，不据此声称发现了实验验证的新材料。

### 2.3 容易混淆的边界

保留候选并按晶体结构设计归入04.02，带隙导向的功能材料设计也支持04.04；结论限于计算闭环与所测约束，不据此声称发现了实验验证的新材料。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM Agent；Tool-using Agent；Multi-Agent System

### 3.2 科研流程角色

tool_use_and_code_execution；data_analysis；evidence_assessment_and_validation

LATHE把晶体图表示、可微几何性质和优化算法封装为工具；Hypothesis Agent提出自然语言结构—性质假设，LATHE Agent将其转成优化配置并执行，结果再供下一轮假设修订。

### 3.3 自主能力

Agent可调用LATHE将结构修改转为几何/晶格参数优化，并在操作与设计两种物理约束设置下完成设计任务。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

主要贡献是把多类晶体几何属性统一成可微、可调用的编辑目标，并将其接入语言假设驱动的闭环结构设计；Agent负责提出与协调，数值优化器负责可验证的结构更新。

### 4.2 系统流程与组件

系统从输入CIF建立晶体图，对键长、键角、二面角、配位、对称性、晶格参数、体积及势能等量构造目标；Agent选择编辑目标和约束，梯度式优化生成结构，再由结构/性质计算返回反馈。多目标情形需同时权衡性质与可行性。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

作者分别测试结构操纵与受约束设计，并对比LATHE-equipped Agent、直接由LLM生成CIF和Claude Code方案；评估集中在论文构造的带隙优化任务及结构约束满足情况，属于计算验证。

### 5.2 基线、指标与结果

结果显示工具化几何编辑能把语言假设落实为可执行晶体修改；在带隙目标下，LATHE流程能在约束下搜索结构。直接文本生成CIF作为基线，体现了显式结构优化的作用。具体性能依赖任务约束与优化设置。

### 5.3 科学贡献与证据强度

主要贡献是把多类晶体几何属性统一成可微、可调用的编辑目标，并将其接入语言假设驱动的闭环结构设计；Agent负责提出与协调，数值优化器负责可验证的结构更新。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

相较于让生成模型直接输出晶体或CIF，LATHE将语言推理与显式几何参数化、梯度优化相连；论文也与常规结构优化及代码型Agent作任务级比较。

## 7. 局限性与风险

研究以带隙设计案例展示方法，计算结果不能代替合成与实验测量；几何可行并不自动保证热力学稳定或可合成。作者指出可增加廉价几何/对称性预筛，以避免不现实候选消耗优化预算。

## 8. 对综述写作的价值

可用于比较语言假设如何借助可微晶体编辑落地，以及结构约束下计算设计与实验验证之间的距离。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

论文提出LATHE晶体几何编辑工具，将键长、键角、二面角、配位、晶格参数、晶胞体积和空间群编码为可微优化目标。假设Agent提出修改，LATHE Agent执行优化并依据结构与目标性质反馈继续迭代。作者以带隙设计任务评估，并与直接CIF生成等方法比较。

### 9.2 速记版 pipeline

系统从输入CIF建立晶体图，对键长、键角、二面角、配位、对称性、晶格参数、体积及势能等量构造目标；Agent选择编辑目标和约束，梯度式优化生成结构，再由结构/性质计算返回反馈。多目标情形需同时权衡性质与可行性。

### 9.3 标注字段汇总

```text
paper_id=ASD-1005
inclusion_status=to_read
scientific_object_modules=04
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=04
module_taxonomy_codes=04.02;04.04
source_level=first_hand_full_text
fulltext_followup_required=true
```

### 全文后续要求

当前纳入和分类证据已足够；第7节明确的结果/复现细节仍需继续回查。


## 2026-10-29 三级分类复核

- 归档分类：`04.02.05` 晶体材料；二级：`04.02`。
- 原文位置：PDF p.1。
- 判定：七类晶体几何约束及带隙逆设计，归晶体材料。
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
