# SolutionsX: supergravity theories/solutions as code, with an agentic workflow for machine-verifiable physics

**论文信息**

- ID：ASD-1052
- 标题：SolutionsX: supergravity theories/solutions as code, with an agentic workflow for machine-verifiable physics
- 作者：Vasil Dimitrov
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2609.07826
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1052.txt
- PDF / 本地文件路径：Reference_PDF/02_Physics_Astronomy_and_Cosmic_Sciences/Dimitrov_2026_SolutionsX_supergravity_theories_solutions_as_code_with_an_agentic_ASD1052.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 研究对象 | 论文以超引力论文中的场方程解作为理论物理案例。 | Abstract；核验TXT行号 246 | A supergravity solution in the literature is an artifact that cannot be verified without re-deriving it | 高（一手正文；非独立复现） |
| 计算系统 | SolutionsX将xAct环境和解打包为机器可验证记录。 | Abstract；核验TXT行号 246 | SolutionsX is a Mathematica package that turns an xAct environment, whatever physics it may describe, into a stored, machine-verifiable record | 高（一手正文；非独立复现） |
| 案例核验 | 沿一项已发表解完整执行工作流，并与xAct组件引擎比较。 | Abstract；核验TXT行号 246 | We follow one published solution through the entire workflow, benchmark the package’s component engine against xAct’s | 高（一手正文；非独立复现） |
| Agent试验 | 三次盲测编码近期论文，均由AI coding agent完成。 | Abstract；核验TXT行号 246 | report on three blind runs of an agentic workflow in which an AI coding agent, given the package and a small toolkit, correctly codified a recent paper in under three hours. | 高（一手正文；非独立复现） |
| 即时验证 | 理论主张在形成时即可由Mathematica kernel核验。 | Abstract；核验TXT行号 246 | a claim is checked in the kernel before it is made. | 高（一手正文；非独立复现） |
| 主控复核：具体科学对象 | 案例编码和验证的是超引力及其他理论物理张量解；建议把宽泛的02.02细化为02.02.01理论物理学。 | TXT line 246；核验TXT行号 246 | three blind runs of an agentic workflow in which an AI coding agent, given the package and a small toolkit, correctly codified a recent paper in under three hours. A database of such records is useful to researchers today and gives agents worked examples to le | 高（一手正文；非独立复现） |

## 0. 摘要翻译

SolutionsX把超引力及其他xAct可描述的张量/微分形式/自旋量理论解，组织为可重放且含验证的代码记录。论文比较组件计算引擎，并以AI coding agent从近期论文中编码超引力解，展示Agent在计算过程中调用机器验证。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。目标是将超引力理论解转为可重放、机器可验证的计算记录。
  - 原文位置：Abstract；核验TXT行号 246；引文：SolutionsX is a Mathematica package that turns an xAct environment, whatever physics it may describe, into a stored, machine-verifiable record
- 多步行动过程：yes。Agent调用符号计算工具编码论文解，之后运行校验与保存。
  - 原文位置：Abstract；核验TXT行号 246；引文：report on three blind runs of an agentic workflow in which an AI coding agent, given the package and a small toolkit, correctly codified a recent paper in under three hours.
- 至少一种Agent能力：yes。系统在Agent推理期间调用kernel检查物理/代数主张。
  - 原文位置：Abstract；核验TXT行号 246；引文：a claim is checked in the kernel before it is made.
- 明确科研流程角色：yes。Agent承担从论文中提取并编码理论物理解的工作。
  - 原文位置：Abstract；核验TXT行号 246；引文：report on three blind runs of an agentic workflow in which an AI coding agent, given the package and a small toolkit, correctly codified a recent paper in under three hours.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：02
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：02（仅归档，不覆盖其他模块）
- 模块内分类路径：02.02.01 理论物理学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

案例编码和验证的是超引力及其他理论物理张量解；建议把宽泛的02.02细化为02.02.01理论物理学。

### 2.3 容易混淆的边界

案例编码和验证的是超引力及其他理论物理张量解；建议把宽泛的02.02细化为02.02.01理论物理学。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM Agent；Tool-using Agent；Hybrid Agent

### 3.2 科研流程角色

literature_search_and_reading；tool_use_and_code_execution；data_analysis；evidence_assessment_and_validation

AI coding agent在研究者给定小型工具包后读取理论论文，编写Mathematica/SolutionsX记录；包将可执行代码、约定和验证留存在数据库，xAct负责张量代数与计算。

### 3.3 自主能力

系统在Agent推理期间调用kernel检查物理/代数主张。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

理论物理侧展示已有超引力结果的可复算封装；软件侧提供含约定、可回放代码和内部检查的知识资产。

### 4.2 系统流程与组件

选定已发表的超引力解；研究者提供包和工具；Agent识别约定、构造解的可执行表示并添加验证；在fresh kernel回放；对包组件引擎与xAct进行基准对比；通过盲测记录完成度和耗时。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

一个已发表理论物理解的端到端重编码案例、SolutionsX组件引擎与xAct基准比较，以及Agent对近期论文的3次盲测。验证聚焦代码可运行、计算等式可机核，不覆盖全部物理解释。

### 5.2 基线、指标与结果

作者报告三次盲测中Agent均在三小时内正确编码近期论文；单案例用于展示工作流。本文未声称独立发现新超引力解。

### 5.3 科学贡献与证据强度

理论物理侧展示已有超引力结果的可复算封装；软件侧提供含约定、可回放代码和内部检查的知识资产。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

相比通用符号计算包，SolutionsX面向物理解的可追溯封装与Agent辅助编码；相比Agent数学证明器，重点在张量/超引力计算工作流。

## 7. 局限性与风险

单篇解的完整跟踪和三次盲测规模有限；机器验证只能确认编码表达式的计算一致性，不能替代理论前提和物理解读审查。

## 8. 对综述写作的价值

可支持综述介绍Agent如何把文献中的理论物理解转换为可执行、可机核的研究记录。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

SolutionsX让Agent编码并机器验证超引力计算，将理论结果保存为可重放记录。

### 9.2 速记版 pipeline

选定已发表的超引力解；研究者提供包和工具；Agent识别约定、构造解的可执行表示并添加验证；在fresh kernel回放；对包组件引擎与xAct进行基准对比；通过盲测记录完成度和耗时。

### 9.3 标注字段汇总

```text
paper_id=ASD-1052
inclusion_status=to_read
scientific_object_modules=02
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=02
module_taxonomy_codes=02.02.01
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O3 新实例 | 编码已发表超引力解并机器验证计算一致性，答案可由符号计算核对 | “three blind runs” · L43 |
| 验证强度 | V2 计算/仿真/回顾性 | 以Mathematica kernel机器验证张量等式计算一致性，非物理实验 | “a claim is checked in the kernel before it is made” · L41 |
| 系统自主性 | L1 任务助手 | Agent执行已发表解的编码任务，人给定论文和验证目标 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
