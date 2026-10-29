# Online Surrogate Repair: Decoupling High-Fidelity Feedback from Search Length in Closed-Loop Discovery

**论文信息**

- ID：ASD-0968
- 标题：Online Surrogate Repair: Decoupling High-Fidelity Feedback from Search Length in Closed-Loop Discovery
- 作者：Feng, Xiaotang; Torr, Philip; Andreis, Bruno
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2609.07655
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0968.txt
- PDF / 本地文件路径：Reference_PDF/04_Materials_Science/Xiaotang_2026_Online_Surrogate_Repair_Decoupling_High_Fidelity_Feedback_from_Search_ASD0968.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 科学对象 | 论文研究在线代理模型修复如何支持闭环材料发现。 | 本地原文 TXT 第395行；核验TXT行号 395 | We introduce online surrogate repair (OSR), a third feedback regime in which most interactions use inexpensive surrogate feedback while sparse high-fidelity evaluations update it during the optimization process. The AI scientist retains control of proposal generation and design selection, while a separate acquisition rule chooses archived proposals for oracle evaluation and appends the returned labels to the surrogate context used in subsequent episodes (Hollmann et al., 2025; Grinsztajn et al., 2026). Because the purpose of the surrogate is to guide search, repair is evaluated by downstream optimization rather than by global fit alone. | 高（一手正文；非独立复现） |
| 研究方法与Agent行动 | 稀疏oracle查询更新代理模型，采集规则选择历史候选供高保真评估。 | 本地原文 TXT 第435行；核验TXT行号 435 | We show that global prediction error and maximum regret are distinct repair objectives, and identify acquisition rules that substantially improve the surrogate’s optimization performance. | 高（一手正文；非独立复现） |
| 实验任务与验证 | 合成表格世界实验固定查询预算并共享测试条件，以比较代理模型。 | 本地原文 TXT 第1090行；核验TXT行号 1090 | Each acquisition rule repairs the surrogate with Q=32Q=32 oracle queries on 40 synthetically generated tabular worlds, with two independent context draws per world, at both context sizes N=100N=100 and N=1000N=1000, and under two surrogates, TabPFN-3 (Grinsztajn et al., 2026) and TabICLv2 (QU et al., 2026). Different surrogate campaigns share their worlds, contexts and audit samples exactly, so the models are directly comparable. Table 1 reports the final value and the improvement of both measures of Section 3.1. | 高（一手正文；非独立复现） |
| 主要结果 | MADE实验将在线稀疏查询与每轮高保真反馈基线进行对照。 | 本地原文 TXT 第1457行；核验TXT行号 1457 | We evaluate 30 chemical systems with three independent T=300T=300 runs per system under two LLM orchestrators, DeepSeek-V4-Flash and GPT-5.6-Luna. Online EI receives Q=32Q=32 oracle queries on an evenly spaced schedule. Two full feedback baselines receive an oracle query after every episode (Q=300Q=300). Vanilla follows the original MADE agent with MACE candidate scoring, whereas Control adds the TabPFN surrogate to the same stack. | 高（一手正文；非独立复现） |
| 研究贡献或边界 | 结果强调代理全局误差与搜索遗憾不同，并报告减少查询需求。 | 本地原文 TXT 第1747行；核验TXT行号 1747 | We demonstrated that global prediction error and maximum regret are misaligned surrogate objectives. In light of this we introduced online surrogate repair, a novel algorithm that updates the surrogate during a longer agent search with sparse oracle queries. Controlled synthetic experiments show that global predictive accuracy can improve without reducing optimizer-facing regret, while Online EI requires substantially fewer oracle queries than full feedback on both synthetic worlds and MADE. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

论文提出在线代理模型修复方法，试图在闭环搜索中减少高保真查询次数而不牺牲搜索长度。AI Scientist在每轮取得高保真反馈后修正低保真代理，再由不同采集策略选择下一个候选。作者在静态修复、合成世界和材料发现任务上比较查询预算与优化表现。该文研究的是实验设计/优化方法；材料任务提供具体科学对象，但需以任务结果限制领域外推。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。任务面向明确的材料发现目标：在已知化学体系中搜索新的晶体结构。
  - 原文位置：本地全文TXT第1441行；Section 4.3；MADE材料发现任务；核验TXT行号 1441；引文：We further evaluate OSR on MADE (Malik et al., 2026), a closed-loop materials discovery benchmark. Each environment specifies a chemical system and its known phases, and the agent proposes crystal structures over an iterative campaign.
- 多步行动过程：yes。算法在多轮候选提议、归档、低成本代理反馈、定期oracle测量和状态更新之间循环，构成实验设计子任务的多步行动。
  - 原文位置：本地全文TXT第682行；Section 3.2；在线修复流程；核验TXT行号 682；引文：Every emitted candidate is recorded in an append-only archive 𝒜t\mathcal{A}_{t}
- 至少一种Agent能力：yes。Agent每轮提出候选并使用当前代理反馈选择设计；高保真oracle标签修复代理后影响后续episode，体现工具/模型调用与反馈迭代能力。
  - 原文位置：本地全文TXT第758行；Algorithm 1；Agent候选提议与反馈；核验TXT行号 758；引文：agent emits candidates CtC_{t} and selects xx
- 明确科研流程角色：yes。论文提出嵌入科学Agent研究循环的实验/查询分配组件，用有限高保真测量改进后续搜索；该局部实验设计角色足以构成科研工作流任务，不要求论文提供完整自动发现系统。
  - 原文位置：本地全文TXT第422行；Contributions；在线查询分配与代理修复；核验TXT行号 422；引文：We formulate online surrogate repair, in which a scientific agent operates under inexpensive surrogate feedback while a separate acquisition rule allocates a limited number of oracle queries to update the surrogate during the search.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：04
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：04（仅归档，不覆盖其他模块）
- 模块内分类路径：04.01 材料基础
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

- Closed-loop design optimization with high-fidelity evaluations, including possible wet-lab or simulation feedback; application domain requires task-list review.

### 2.3 容易混淆的边界

04.01方法覆盖代理修复和高保真查询分配；MADE任务在30种化学体系上提出晶体结构，提供材料对象验证。论文贡献为科学Agent工作流中的实验设计局部方法，不要求完整闭环发现。保留既有模块代码。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

多Agent/科研工作流Agent

### 3.2 科研流程角色

科学问题提出；实验设计；工具调用与代码执行；结果分析与验证

闭环AI Scientist由代理模型、修复器和采集策略构成；Agent根据高保真观测更新代理并选择后续候选，形成实验设计反馈循环。

### 3.3 自主能力

Agent每轮提出候选并使用当前代理反馈选择设计；高保真oracle标签修复代理后影响后续episode，体现工具/模型调用与反馈迭代能力。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

提出将代理修复插入主动搜索闭环的方法；科学贡献依赖基准任务，主要贡献为实验设计/优化方法。

### 4.2 系统流程与组件

输入为低保真数据、稀疏高保真查询和目标函数；用在线代理修复校准预测；比较Random、UQ、Peak、Q90-UCB、G2P及EI等采集策略；将选点送入仿真/高保真oracle；以新反馈更新代理并迭代。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

静态代理修复实验、合成世界与MADE多极值材料发现基准；每种方法多次重复并比较查询预算、目标值和命中情况。不是材料实验室验证。

### 5.2 基线、指标与结果

作者报告EI在线修复能在较少查询条件下保持目标搜索表现；MADE部分方法和控制组有90次运行等设置，具体数值应按表格对方法分别引用。

### 5.3 科学贡献与证据强度

提出将代理修复插入主动搜索闭环的方法；科学贡献依赖基准任务，主要贡献为实验设计/优化方法。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

连接多保真贝叶斯优化、主动学习与科研Agent；关键区别是利用反馈修复代理并分析查询数与搜索长度的关系。

## 7. 局限性与风险

结果依赖合成世界、基准oracle和代理假设；特定采集策略的收益不代表所有实验任务；真实实验成本估算不是已完成湿实验。

## 8. 对综述写作的价值

可用于综述比较主动学习/代理修复如何作为Agent科研循环中的实验规划组件。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

在线修复代理模型，以更少高保真反馈支持闭环搜索。

### 9.2 速记版 pipeline

输入为低保真数据、稀疏高保真查询和目标函数；用在线代理修复校准预测；比较Random、UQ、Peak、Q90-UCB、G2P及EI等采集策略；将选点送入仿真/高保真oracle；以新反馈更新代理并迭代。

### 9.3 标注字段汇总

```text
paper_id=ASD-0968
inclusion_status=to_read
scientific_object_modules=04
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=04
module_taxonomy_codes=04.01
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`04.01.04` 材料计算与材料信息学；二级：`04.01`。
- 原文位置：PDF p.2。
- 判定：材料代理模型修复与高精度计算反馈的实验支持材料计算。
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
