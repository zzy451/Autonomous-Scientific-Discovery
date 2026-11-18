# AutoSciBench: Autonomous Benchmark Generation for Evaluating Scientific Agents

## 当前分类（2026-11-01 实证复核）

- 当前纳入状态：`included`；主归档：`07`。
- 本块为当前有效结论；后文既有分类、来源限制与审计判断均保留为历史记录，与本块不一致者由本块取代。
- 当前对象模块：`04;06;07`。
- 代表分类每个模块保留一个落点，不表示穷尽全文全部细类。

| 模块 | 二级 | 三级 | 本轮结论 |
|---|---|---|---|
| 04 | 04.01 材料基础 | 04.01.03 材料表征 | 已落地 |
| 06 | 06.03 生物技术相关科学 | 06.03.01 基因组学 | 已落地 |
| 07 | 07.02 临床医学 | 07.02.09 心血管病学 | 已落地 |

- 模块04：实际材料BET表征任务并有薄膜带隙任务。
  - 证据：PDF 第 [6, 7, 24] 页；原文：The question asks the solver to determine the specific surface area of a porous solid from a nitrogen adsorption isotherm using the multi-point BET method.

- 完整裁决：`Coverage_Check/classification_recheck_2026-11-01/`。

## 既有笔记与历史审计记录

**论文信息**

- ID：ASD-0913
- 标题：AutoSciBench: Autonomous Benchmark Generation for Evaluating Scientific Agents
- 作者：Kim, Dongki; Lee, Namkyeong; Nair, Surag; Edwards, Carl; Li, Xiner; De Brouwer, Edward; Collier, Jenna Lynn; Hwang, Sung Ju; Scalia, Gabriele; Hajiramezanali, Ehsan
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2610.05140
- 一手阅读来源：https://arxiv.org/abs/2610.05140
- 来源层级：全文
- 阅读版本：对应缓存来源版本，参见Evidence Log
- 阅读版本题名：AutoSciBench: Autonomous Benchmark Generation for Evaluating Scientific Agents
- 原始全文缓存：C:/Users/20683/Desktop/综述/.tmp_asd_pdfs/source_F/2610.05140.pdf
- PDF / 本地文件路径：Reference_PDF/07_Medical_and_Health_Sciences/Kim_2026_AutoSciBench.pdf
- 当前状态：included
- 阅读日期：2026-10-22
- 笔记作者：Codex（读者证据包经主控审核整合）

## Evidence Log

| 判断项 | 结论 / 原文概括 | 证据位置 | 可信度 |
|---|---|---|---|
| Agent循环 | 流程依次包括concept、recipe、task implementation、solver evaluation和feedback refinement。 | §3.1–3.4 | high |
| 领域 | 三领域的seed benchmark分别为CompBioBench、MatTools和MedCTA。 | §4.1；Appendix A.1 | high |
| 规划能力 | Concept指定科学领域、数据模态和操作；recipe规划任务、数据和求解步骤。 | §3.1–3.3 | high |
| 生物对象任务 | MSI任务使用肿瘤/正常BAM读取，要求提取repeat-length分布并判断体细胞微卫星不稳定。 | Appendix B.4 | high |
| 临床影像对象 | 全文实例包含胸片心胸比计算与心脏MRI水肿/增强区域分析。 | Appendix C.5–C.6 | high |
| 效果 | 生成benchmark在计算生物和材料上更难，三个领域质量评价更高。 | §4.2–4.3 | high |

## 0. 摘要翻译

AutoSciBench使用Agent规划benchmark概念和recipe、实施数据任务、调用solver/judge评测，再依据反馈迭代更新。全文涉及计算生物、材料科学和临床影像；实例包括肿瘤/正常测序数据的微卫星不稳定性判定，以及胸片心胸比和心脏MRI分析。生成任务对solver更具挑战性，质量评价也较高。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 当前判断：included；读者建议：included。
主控与独立边界审稿确认：全文§3明确概念生成、recipe规划、任务实现、solver评价和反馈修订循环；§4.1使用Claude Code/Codex CLI，三领域分别50任务、最多10轮。自动构建科研评测任务属于明确科研角色，benchmark属性本身不是排除理由。

### 1.2 排除风险检查

全文计算生物任务含BAM/MSI，采用06.03.01基因组学；临床任务含心胸比和心脏MRI，07侧主落点07.02.09，肿瘤/MSI对象同时在证据中记录。材料工具任务采用04.01。实际科学对象评测覆盖04/06/07，不进入01.04；生成器满足Agent最低标准。
完整闭环不是纳入门槛；科研目标、多步行动、至少一项Agent能力及明确科研角色须同时成立。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：04;06;07
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：07（仅归档，不替代多模块事实）
- 模块内分类路径：04.01; 06.03.01; 07.02.09
- 分类深度：03/04使用二级；06/07使用固定三级；其余沿用现有树。
- 分类状态：原文证据复核

### 2.2 对象优先判定

对象任务包括计算生物的肿瘤/正常BAM测序与MSI判别、材料数据和工具分析、临床影像任务。种子基线为CompBioBench、MatTools、MedCTA。指标包括solver accuracy与benchmark质量评分。作者报告计算生物和材料生成任务更难，三个领域的平均质量评价较高；此处未转录表中具体数值。

### 2.3 容易混淆的边界

全文计算生物任务含BAM/MSI，采用06.03.01基因组学；临床任务含心胸比和心脏MRI，07侧主落点07.02.09，肿瘤/MSI对象同时在证据中记录。材料工具任务采用04.01。实际科学对象评测覆盖04/06/07，不进入01.04；生成器满足Agent最低标准。

## 3. Agent 系统与科研流程角色

主控与独立边界审稿确认：全文§3明确概念生成、recipe规划、任务实现、solver评价和反馈修订循环；§4.1使用Claude Code/Codex CLI，三领域分别50任务、最多10轮。自动构建科研评测任务属于明确科研角色，benchmark属性本身不是排除理由。

科研流程与自主能力以本文实际行动和工具调用为依据：

Concept规划领域、数据模态和分析操作；recipe规划问题与数据需求；Agent实施任务，solver分析数据，judge评估并给反馈；依据反馈修改benchmark难度及后续任务概念。

## 4. 方法设计

### 4.1 方法动机与设计

将科学Agent benchmark构建做成具有高低层计划、数据任务实施、solver反馈和迭代改进的自动化流程，并覆盖三个科学领域。

### 4.2 系统流程与组件

Concept规划领域、数据模态和分析操作；recipe规划问题与数据需求；Agent实施任务，solver分析数据，judge评估并给反馈；依据反馈修改benchmark难度及后续任务概念。

## 5. 实验与验证

### 5.1 验证方式、对象及任务

对象任务包括计算生物的肿瘤/正常BAM测序与MSI判别、材料数据和工具分析、临床影像任务。种子基线为CompBioBench、MatTools、MedCTA。指标包括solver accuracy与benchmark质量评分。作者报告计算生物和材料生成任务更难，三个领域的平均质量评价较高；此处未转录表中具体数值。

### 5.2 基线、指标与结果

对象任务包括计算生物的肿瘤/正常BAM测序与MSI判别、材料数据和工具分析、临床影像任务。种子基线为CompBioBench、MatTools、MedCTA。指标包括solver accuracy与benchmark质量评分。作者报告计算生物和材料生成任务更难，三个领域的平均质量评价较高；此处未转录表中具体数值。

### 5.3 科学贡献与证据强度

将科学Agent benchmark构建做成具有高低层计划、数据任务实施、solver反馈和迭代改进的自动化流程，并覆盖三个科学领域。

证据层级：原始全文支持；作者报告结果不等于独立复现。

## 6. 与已有工作的关系

与自动benchmark生成及科学Agent能力评测相关，强调科学任务须包含信息获取、数据分析与间接证据推理。

## 7. 局限性与风险

生成质量依赖LLM solver、judge和人工种子任务；benchmark难度或质量评价不等于真实科研发现效益。材料任务的对象细分类别还需核对。

## 8. 对综述写作的价值

适合作为benchmark生成Agent与科学对象覆盖交叉的边界样本；主控可决定其核心地位，具体对象实验依据已提取。

推荐引用强度：普通引用，可在核对原文后用于相应领域案例。

## 9. 总结

### 9.1 一句话概括

Agent迭代生成科学评测任务

### 9.2 速记版 pipeline

Concept规划领域、数据模态和分析操作；recipe规划问题与数据需求；Agent实施任务，solver分析数据，judge评估并给反馈；依据反馈修改benchmark难度及后续任务概念。

### 9.3 标注字段汇总

```text
paper_id=ASD-0913
inclusion_status=included
scientific_object_modules=04;06;07
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=07
module_taxonomy_codes=04.01; 06.03.01; 07.02.09
source_level=fulltext
fulltext_followup_required=false
```

### 全文后续要求

本轮已读原始全文并完成对象分类；无需为纳入/分类另做全文补读。具体引用时仍需回查相应原文位置。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O2 既定基准 | Agent自动生成计算生物、材料和医学影像benchmark任务，种子来自已有CompBioBench、MatTools、MedCTA | “三领域的seed benchmark分别为CompBioBench、MatTools和MedCTA” · L46 |
| 验证强度 | V1 基准/内部评测 | 评估生成任务上solver准确率和benchmark质量评分 | “计算生物和材料生成任务更难，三个领域的平均质量评价较高” · L110 |
| 系统自主性 | L2 闭环执行者 |  | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
