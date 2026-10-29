# FUSION: a skill-based research agent for publicly obtainable nuclear-physics codes

**论文信息**

- ID：ASD-1070
- 标题：FUSION: a skill-based research agent for publicly obtainable nuclear-physics codes
- 作者：Lei, Jin
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2609.04742
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1070.txt
- PDF / 本地文件路径：Reference_PDF/02_Physics_Astronomy_and_Cosmic_Sciences/Jin_2026_FUSION_a_skill_based_research_agent_for_publicly_obtainable_ASD1070.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 科研任务 | 核物理代码执行涉及物理约定正确性。 | TXT line 357；核验TXT行号 357 | Figure 4 shows the twenty codes by area: FRESCO [1] with its fitting front end SFRESCO, COLOSS [2], CCFULL [3], pikoe [4], NLAT [5], CNOK [6], SIDES [7] and SWANLOP [8] for reactions and optical models; GSM [9], KSHELL [10], NuclearToolkit.jl [11] and Sky3D [12, 13] for structure; CGMF [14] and TALYS [15] for fission and statistical models; AZURE2 [16] and SkyNet [17] for astrophysics; SMASH [18], GiBUU [19], Thermal-FIST [20] and vHLLE [23] for heavy-ion collisions and the equation of state. | 高（一手正文；非独立复现） |
| Agent技能 | 获取代码、运行解析并记录失败模式。 | TXT line 297；核验TXT行号 297 | A skill is a directory of instructions, examples, and small scripts. It contains no language model. When a request names a supported code or calculation, the agent reads the corresponding skill before acting. Figure 3 shows the FRESCO example. Six things are in each one. | 高（一手正文；非独立复现） |
| 工具范围 | 发布覆盖20个核物理代码。 | TXT line 216；核验TXT行号 216 | Every radius is then 22% too large, but the program still prints a smooth angular distribution and no warning. | 高（一手正文；非独立复现） |
| 验证 | 技能须复现给定基准及容差后才报告。 | TXT line 382；核验TXT行号 382 | A released skill carries the evidence needed to inspect it. The record identifies the upstream revision, pinned where the upstream allows it, the tested platforms, the benchmark, and the tolerance. The checks themselves are mechanical: the code is built on both macOS on ARM and Linux on x86-64 for most skills, with the exceptions stated in their records; the benchmark is reproduced and the agreement stated in significant figures; and each guard is disabled in turn to confirm that exactly its own test fails. A second language model, different from the one that drafted the skill, then goes through it and is allowed to run the code rather than only read it. What it finds is written into the skill and ships with it. | 高（一手正文；非独立复现） |
| 数据资源 | 含离线核物理文献集合。 | TXT line 490；核验TXT行号 490 | EXFOR contains no n+90Zr elastic measurement at 50 MeV. The agent reported that absence as part of the result, repeated the calculation at the two energies that were measured, and produced Fig. 10 with no free parameters: the mean calculate | 高（一手正文；非独立复现） |

## 0. 摘要翻译

FUSION为公开可获得的核物理程序提供技能化研究Agent。技能从公开源获取代码，以验证过的输入运行程序、解析结果并记录已知失效模式；只有复现指定基准及容差才报告结果。当前覆盖20个程序领域和可搜索核物理文献，强调运行成功不等于物理设置正确。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。面向真实核物理计算并强调物理约定正确性。
  - 原文位置：TXT line 195；核验TXT行号 195；引文：A skill obtains the code from its public source, starts from a verified input, runs and parses the calculation, records known failure modes, and must reproduce a stated benchmark to a stated tolerance before reporting a result.
- 多步行动过程：yes。技能获取代码、运行并解析计算、核验基准后报告。
  - 原文位置：TXT line 195；核验TXT行号 195；引文：A skill obtains the code from its public source, starts from a verified input, runs and parses the calculation, records known failure modes, and must reproduce a stated benchmark to a stated tolerance before reporting a result.
- 至少一种Agent能力：yes。能构建程序、生成输入并调用公开核物理代码。
  - 原文位置：TXT line 216；核验TXT行号 216；引文：Language-model agents can compile programs, search manuals, and draft input files.
- 明确科研流程角色：yes。帮助研究者运行核物理数值代码并验证输出。
  - 原文位置：TXT line 195；核验TXT行号 195；引文：Here I describe the design, the checks behind the current release, and one complete calculation from input to comparison with measured data.

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

聚焦核物理数值研究代码与计算，归入02物理科学。

### 2.3 容易混淆的边界

聚焦核物理数值研究代码与计算，归入02物理科学。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

skill_based_coding_agent

### 3.2 科研流程角色

code_execution；scientific_validation

通用编码Agent由代码专属skills约束，包含环境构建、输入生成、程序执行、结果解析和基准校验。

### 3.3 自主能力

能构建程序、生成输入并调用公开核物理代码。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

系统贡献是可复用且带验证门槛的核代码技能库；科学贡献来自通过代码支持开展的具体核物理计算示例。

### 4.2 系统流程与组件

用户提出核物理计算目标；技能获取并编译对应程序，依据已验证输入和代码约定构造输入，运行计算并解析输出，检查已知失效模式，随后对照基准及容差；通过后才报告可追踪结果。 这一工作流的实施细节、输入输出和验证范围均按原文所报告内容理解，不将展示案例外推为普遍能力。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

每项技能需复现声明的基准结果和容差；正文还展示从输入到实验数据比较的完整计算案例。

### 5.2 基线、指标与结果

发布版本覆盖20个代码和61,167页离线文献；论文强调错误物理约定会产生看似合理的输出。

### 5.3 科学贡献与证据强度

系统贡献是可复用且带验证门槛的核代码技能库；科学贡献来自通过代码支持开展的具体核物理计算示例。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

回应通用编码Agent易生成可运行但物理约定错误输入的问题。

## 7. 局限性与风险

- author_stated：代码范围取决于已实现技能及可公开获取的程序；用户凭据和私有注释不进入公开仓库。
- reviewer_inference：平台覆盖领域广度不代表所有代码和物理情形均充分验证。

## 8. 对综述写作的价值

可说明科学软件Agent需验证物理语义而非只确认程序运行成功。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

FUSION以代码专属技能和基准门槛支持可审计核物理计算。

### 9.2 速记版 pipeline

用户提出核物理计算目标；技能获取并编译对应程序，依据已验证输入和代码约定构造输入，运行计算并解析输出，检查已知失效模式，随后对照基准及容差；通过后才报告可追踪结果。 这一工作流的实施细节、输入输出和验证范围均按原文所报告内容理解，不将展示案例外推为普遍能力。

### 9.3 标注字段汇总

```text
paper_id=ASD-1070
inclusion_status=to_read
scientific_object_modules=02
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=02
module_taxonomy_codes=02.02
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`02.02.13` 核物理学；二级：`02.02`。
- 原文位置：PDF p.2。
- 判定：20个核反应、核结构和裂变程序的实际运行，归核物理。
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
