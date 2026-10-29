# Demonstration of a Structured Agentic Workflow for Applied Quantum Computing Research

**论文信息**

- ID：ASD-1055
- 标题：Demonstration of a Structured Agentic Workflow for Applied Quantum Computing Research
- 作者：Dikshant Dulal; Maxence Grandadam; Maciej Koch-Janusz; Mykola Maksymenko
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2610.05304
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1055.txt
- PDF / 本地文件路径：Reference_PDF/03_Chemical_Sciences/Dulal_2026_Demonstration_of_a_Structured_Agentic_Workflow_for_Applied_Quantum_ASD1055.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 科学目标 | QAOS被用于量子化学原型任务。 | Abstract；核验TXT行号 210 | We demonstrate QAOS on a quantum chemistry prototyping task | 高（一手正文；非独立复现） |
| 化学对象 | 案例要求建立质子转移问题的最小模型。 | Abstract；核验TXT行号 210 | a minimal model for a proton-transfer problem | 高（一手正文；非独立复现） |
| 计算方法 | 实现SQD并与FCI、DFT等经典参考方法并用。 | Abstract；核验TXT行号 210 | using sample-based quantum diagonalization (SQD), together with classical reference methods such as FCI (exact diagonalization) and density functional theory (DFT). | 高（一手正文；非独立复现） |
| Agent组织 | 非线性工作流图将项目拆为受控、沙箱化多Agent任务。 | Abstract；核验TXT行号 210 | It decomposes a complex research project into sandboxed multi-agent tasks executed under constraints from the project graph, task-relevant methodologies, and necessary verification steps. | 高（一手正文；非独立复现） |
| 基线观察 | 基线Agent会遗漏明确指令且多次运行差异较大。 | Abstract；核验TXT行号 210 | In contrast to QAOS, the baseline agents silently ignore explicit instructions, and the runs show large variability. | 高（一手正文；非独立复现） |
| 主控复核：具体科学对象 | 量子化学案例将质子转移问题建成最小模型并比较SQD与FCI/DFT参考解；研究对象是化学过程。量子算法和计算框架为方法，不单独归01。 | TXT line 210；核验TXT行号 210 | proton-transfer problem and to implement its solution using sample-based quantum diagonalization (SQD), together with classical reference methods such as FCI (exact diagonalization) and density functional theory (DFT). We compare the QAOS solution to those obt | 高（一手正文；非独立复现） |

## 0. 摘要翻译

QAOS是用于量子与计算研发的结构化Agent系统，以非线性工作流图控制不同Agent节点的上下文和计算资源。作者以质子转移量子化学任务展示从问题拆解、最小模型构建到SQD实现及经典方法核验，并与代码型基线Agent比较。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。目标是把质子转移化学问题形式化为可执行的量子化学算法。
  - 原文位置：Abstract；核验TXT行号 210；引文：a minimal model for a proton-transfer problem
- 多步行动过程：yes。QAOS以工作流图拆解项目为隔离子任务，并安排计算和验证。
  - 原文位置：Abstract；核验TXT行号 210；引文：It decomposes a complex research project into sandboxed multi-agent tasks executed under constraints from the project graph, task-relevant methodologies, and necessary verification steps.
- 至少一种Agent能力：yes。异构多Agent受图结构约束分工，调用计算资源并执行核验。
  - 原文位置：Abstract；核验TXT行号 210；引文：It decomposes a complex research project into sandboxed multi-agent tasks executed under constraints from the project graph, task-relevant methodologies, and necessary verification steps.
- 明确科研流程角色：yes。系统承担计算化学问题的建模、算法实现和结果检查。
  - 原文位置：Abstract；核验TXT行号 210；引文：We demonstrate QAOS on a quantum chemistry prototyping task

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：03
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：03（仅归档，不覆盖其他模块）
- 模块内分类路径：03.02 基础化学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

量子化学案例将质子转移问题建成最小模型并比较SQD与FCI/DFT参考解；研究对象是化学过程。量子算法和计算框架为方法，不单独归01。

### 2.3 容易混淆的边界

量子化学案例将质子转移问题建成最小模型并比较SQD与FCI/DFT参考解；研究对象是化学过程。量子算法和计算框架为方法，不单独归01。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM Agent；Multi-Agent System；Tool-using Agent

### 3.2 科研流程角色

task_decomposition；tool_use_and_code_execution；simulation_modeling；data_analysis；evidence_assessment_and_validation

QAOS由异构多Agent节点构成，项目图限制子任务的上下文、方法和验证要求。科研问题拆解、量子算法实现和核验任务分别交给隔离子Agent，人类研究者编排目标与检查。

### 3.3 自主能力

异构多Agent受图结构约束分工，调用计算资源并执行核验。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

计算化学贡献是完成质子转移问题的量子算法原型；系统贡献是以项目图和受控上下文管理复杂研发任务，并显式加入验证节点。

### 4.2 系统流程与组件

将质子转移问题转为最小模型；规划SQD实现及参考解计算；把实现、理论/算法核验和代码检查拆分为沙箱任务；执行并合并结果；对照FCI和DFT结果审阅；比较基线Agent是否遵守原始要求。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

采用质子转移量子化学原型案例，构造模型并实现sample-based quantum diagonalization，参考方法包括FCI精确对角化和DFT；以基线代码Agent对照任务遵循度及结果一致性。

### 5.2 基线、指标与结果

作者指出基线Claude Sonnet 5/Claude Code运行会静默忽略显式指令且结果波动较大；摘要未给出QAOS与基线的统一误差统计，因此不扩写数值性能结论。

### 5.3 科学贡献与证据强度

计算化学贡献是完成质子转移问题的量子算法原型；系统贡献是以项目图和受控上下文管理复杂研发任务，并显式加入验证节点。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

区别于可直接编码的通用Agent，QAOS以项目级依赖图控制粒度任务、方法约束和核验过程；用量子化学案例检验而非只展示抽象工作流。

## 7. 局限性与风险

仅为单一质子转移原型任务；论文未声称量子硬件实验或新化学发现。基线结果的随机性/指令遵从比较也不能替代全面算法benchmark。

## 8. 对综述写作的价值

可用于综述结构化多Agent如何管理计算化学项目分解、代码实现与方法学核验。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

QAOS以图式多Agent工作流完成质子转移量子化学原型并与经典方法对照。

### 9.2 速记版 pipeline

将质子转移问题转为最小模型；规划SQD实现及参考解计算；把实现、理论/算法核验和代码检查拆分为沙箱任务；执行并合并结果；对照FCI和DFT结果审阅；比较基线Agent是否遵守原始要求。

### 9.3 标注字段汇总

```text
paper_id=ASD-1055
inclusion_status=to_read
scientific_object_modules=03
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=03
module_taxonomy_codes=03.02
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`03.02.11` 理论与计算化学；二级：`03.02`。
- 原文位置：PDF p.2。
- 判定：水分子质子转移量子化学模型与电子相关能垒，归理论计算化学。
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
