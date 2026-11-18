# LaMET-Agent: An Agent Framework for Large-Momentum Effective Theory Analysis

**论文信息**

- ID：ASD-1056
- 标题：LaMET-Agent: An Agent Framework for Large-Momentum Effective Theory Analysis
- 作者：Jinchen He; Xiangyu Jiang; Fei Yao; Dian-Jun Zhao
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2609.32225
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1056.txt
- PDF / 本地文件路径：Reference_PDF/02_Physics_Astronomy_and_Cosmic_Sciences/He_2026_LaMET_Agent_An_Agent_Framework_for_Large_Momentum_Effective_ASD1056.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 研究对象 | LaMET用于从格点QCD计算光锥部分子分布。 | Abstract；核验TXT行号 309 | Large-momentum effective theory (LaMET) provides a first-principles framework for computing the xx dependence of light-cone parton distributions from lattice QCD. | 高（一手正文；非独立复现） |
| 分析步骤 | Agent实现关联函数分析、重整化、变换、微扰匹配及外推。 | Abstract；核验TXT行号 312 | The present release supports collinear quark distributions and implements correlator analysis, renormalization, Fourier transformation, perturbative matching, continuum, physical pion mass and infinite-momentum extrapolations, and automated result review. | 高（一手正文；非独立复现） |
| 案例数量 | 四项端到端分析验证LaMET-Agent。 | Abstract；核验TXT行号 313 | We validate it on four end-to-end analyses | 高（一手正文；非独立复现） |
| 粒子对象 | 案例包含π介子PDF及π、K介子分布振幅。 | Abstract；核验TXT行号 313 | pion parton distribution functions in the gauge-invariant and Coulomb-gauge formulations, and pion and kaon distribution amplitudes | 高（一手正文；非独立复现） |
| 结果核对 | 作者报告与已发表计算结果一致。 | Abstract；核验TXT行号 313 | obtaining results consistent with the published calculations. | 高（一手正文；非独立复现） |
| 主控复核：具体科学对象 | 四项端到端案例计算π介子部分子分布和π/K介子分布振幅，属于格点QCD和强相互作用物理；建议细化至粒子物理学。 | TXT line 402；核验TXT行号 402 | four end-to-end LaMET analyses: pion PDFs in both the gauge-invariant and Coulomb-gauge formalisms, and pion and kaon DAs. These examples provide systematic reproductions of established analyses and validate the framework across distinct observables and formul | 高（一手正文；非独立复现） |

## 0. 摘要翻译

LaMET-Agent将大动量有效理论下格点QCD的部分子分布计算整理为可执行、可复现和可检查的管线。当前版本依次覆盖关联函数分析、重整化、傅里叶变换、微扰匹配及连续极限、物理π质量和无限动量外推，并自动审阅结果。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。目标是自动执行格点QCD中的LaMET部分子分布计算流程。
  - 原文位置：Abstract；核验TXT行号 311；引文：We present lamet-agent, an open-source large language model (LLM) agent framework that organizes this workflow into an executable, reproducible, and inspectable analysis pipeline.
- 多步行动过程：yes。管线包含关联函数、重整化、傅里叶变换、匹配及多种外推。
  - 原文位置：Abstract；核验TXT行号 312；引文：The present release supports collinear quark distributions and implements correlator analysis, renormalization, Fourier transformation, perturbative matching, continuum, physical pion mass and infinite-momentum extrapolations, and automated result review.
- 至少一种Agent能力：yes。Agent编排完整、可检查的计算阶段并自动审阅结果。
  - 原文位置：Abstract；核验TXT行号 311；引文：We present lamet-agent, an open-source large language model (LLM) agent framework that organizes this workflow into an executable, reproducible, and inspectable analysis pipeline.
- 明确科研流程角色：yes。Agent承担强子部分子分布和分布振幅数据分析工作。
  - 原文位置：Abstract；核验TXT行号 313；引文：pion parton distribution functions in the gauge-invariant and Coulomb-gauge formulations, and pion and kaon distribution amplitudes

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：02
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：02（仅归档，不覆盖其他模块）
- 模块内分类路径：02.02.14 粒子物理学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

四项端到端案例计算π介子部分子分布和π/K介子分布振幅，属于格点QCD和强相互作用物理；建议细化至粒子物理学。

### 2.3 容易混淆的边界

四项端到端案例计算π介子部分子分布和π/K介子分布振幅，属于格点QCD和强相互作用物理；建议细化至粒子物理学。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM Agent；Tool-using Agent；Planning Agent

### 3.2 科研流程角色

task_decomposition；tool_use_and_code_execution；data_analysis；result_interpretation；evidence_assessment_and_validation

LLM Agent承载任务阶段编排和结果审阅；底层格点QCD程序执行关联函数、重整化、变换与匹配等数值步骤；manifest记录工作计划和运行状态。

### 3.3 自主能力

Agent编排完整、可检查的计算阶段并自动审阅结果。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

粒子物理侧支持强子内部夸克分布的第一原理数值分析；系统侧把专家操作的多阶段计算固化成可复现管线。

### 4.2 系统流程与组件

计划模式生成阶段清单；运行阶段读取格点关联函数并执行重整化、傅里叶变换和微扰匹配；用系统学分析和多极限外推生成PDF/DA；审阅阶段检查计算设置与结果，汇总可复用分析产物。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

四个端到端格点QCD分析：规范不变与库仑规范下的π介子PDF，以及π和K介子分布振幅；与已发表计算结果比较。

### 5.2 基线、指标与结果

作者报告四项分析结果与已发表计算一致。论文未在摘要提供统一误差指标；其他TMD、GPD与胶子分布功能仍在计划扩展中。

### 5.3 科学贡献与证据强度

粒子物理侧支持强子内部夸克分布的第一原理数值分析；系统侧把专家操作的多阶段计算固化成可复现管线。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

相较单一LaMET数值研究，系统贡献在于可复用执行与审阅基础设施；相比通用代码Agent，工作流阶段与系统误差检查针对格点强子物理专门化。

## 7. 局限性与风险

目前功能限于共线夸克分布；四个验证案例均为计算分析，与实验数据的关系由格点QCD理论及既有发表结果提供。

## 8. 对综述写作的价值

可作为高能理论物理中Agent自动化多阶段数值分析并保留系统学审查的案例。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

LaMET-Agent将强子部分子分布计算组织为可检查的格点QCD分析管线。

### 9.2 速记版 pipeline

计划模式生成阶段清单；运行阶段读取格点关联函数并执行重整化、傅里叶变换和微扰匹配；用系统学分析和多极限外推生成PDF/DA；审阅阶段检查计算设置与结果，汇总可复用分析产物。

### 9.3 标注字段汇总

```text
paper_id=ASD-1056
inclusion_status=to_read
scientific_object_modules=02
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=02
module_taxonomy_codes=02.02.14
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O3 新实例 | 复现已发表格点QCD部分子分布计算，答案可由已知方法核对 | “four end-to-end analyses” · L23 |
| 验证强度 | V2 计算/仿真/回顾性 | 与已发表计算结果一致性比较，属计算验证 | “obtaining results consistent with the published calculations” · L25 |
| 系统自主性 | L1 任务助手 | Agent执行已定义LaMET分析流程各阶段，人决定研究流程 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
