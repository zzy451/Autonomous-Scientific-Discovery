# SWE-bench Science: Can Coding Agents Resolve Engineering Tasks in Science?

**论文信息**

- ID：ASD-0878
- 标题：SWE-bench Science: Can Coding Agents Resolve Engineering Tasks in Science?
- 作者：Xu, Zhipeng; Lu, Jiahao; Zheng, Yining; Wang, Yuxin; Qiu, Xipeng
- 年份：2026
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2608.19799
- 一手阅读来源：https://arxiv.org/abs/2608.19799
- 来源层级：全文
- 阅读版本：对应缓存来源版本，参见Evidence Log
- 阅读版本题名：SWE-bench Science: Can Coding Agents Resolve Engineering Tasks in Science?
- 原始全文缓存：C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/.tmp_asd_pdfs/2608.19799.pdf
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Xu_2026_SWEBenchScience.pdf
- 当前状态：included
- 阅读日期：2026-10-22
- 笔记作者：Codex（读者证据包经主控审核整合）

## Evidence Log

| 判断项 | 结论 / 原文概括 | 证据位置 | 可信度 |
|---|---|---|---|
| 基准含119项科学软件任务。 | 任务来自98个仓库并覆盖20个领域。 | 全文摘要及§2 | high |
| 任务有三种工程范式。 | Issue-driven、Expert-exploratory和Engineering-integration。 | 全文摘要与任务分类 | high |
| Agent在真实仓库执行修复。 | 任务要求检索、修改并测试科学软件。 | 全文实验设置 | high |
| 最佳Agent通过率仍低于一半。 | Claude Code with Opus-5(max) pass@1 <50%。 | 全文摘要及结果 | high |
| 科学指导的效果依质量而变。 | 可靠信息改善平均表现或效率，偏离任务的指导可能诱发anchoring。 | 全文配对消融 | high |
| 跨领域比较受任务量限制。 | 每个领域样本少，科学知识如何起作用仍待研究。 | 全文§7 Limitations | medium |

## 0. 摘要翻译

SWE-bench Science收录98个科学软件仓库的119项工程任务，覆盖20个科学领域，并按任务驱动、专家探索与工程集成分组。Coding Agent须在仓库环境中探索、修复和测试代码；报告的最佳pass@1低于50%，显式科学指导的效用依其质量而变。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 当前判断：included；读者建议：included。
原文§2–3评测Agent检视真实科学代码仓库、定位缺陷并多步修改/运行测试，具有工具行动和明确科学软件维护角色，满足四项最低标准。科研流程支持不要求产出新的自然科学发现。

### 1.2 排除风险检查

科学程序和软件缺陷是实际评测对象，归01.02；不因仓库来自20个学科就自动添加全部自然科学模块，也不因不是新发现而排除。独立边界审稿与主控均确认纳入。
完整闭环不是纳入门槛；科研目标、多步行动、至少一项Agent能力及明确科研角色须同时成立。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：01
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：01（仅归档，不替代多模块事实）
- 模块内分类路径：01.02
- 分类深度：03/04使用二级；06/07使用固定三级；其余沿用现有树。
- 分类状态：原文证据复核

### 2.2 对象优先判定

119项任务，来自98个仓库、20个科学领域；最强报告Agent pass@1低于50%。可靠科学指导可改善平均表现或token效率，误导指导可能导致anchoring。

### 2.3 容易混淆的边界

科学程序和软件缺陷是实际评测对象，归01.02；不因仓库来自20个学科就自动添加全部自然科学模块，也不因不是新发现而排除。独立边界审稿与主控均确认纳入。

## 3. Agent 系统与科研流程角色

原文§2–3评测Agent检视真实科学代码仓库、定位缺陷并多步修改/运行测试，具有工具行动和明确科学软件维护角色，满足四项最低标准。科研流程支持不要求产出新的自然科学发现。

科研流程与自主能力以本文实际行动和工具调用为依据：

repository-level benchmark覆盖Issue-driven、Expert-exploratory、Engineering-integration任务；Agent在仓库中探索并执行修复，另有配对消融移除显式科学指导。

## 4. 方法设计

### 4.1 方法动机与设计

建立科学软件工程Agent基准，评估科学知识、探索、修复覆盖和系统集成相关失败。

### 4.2 系统流程与组件

repository-level benchmark覆盖Issue-driven、Expert-exploratory、Engineering-integration任务；Agent在仓库中探索并执行修复，另有配对消融移除显式科学指导。

## 5. 实验与验证

### 5.1 验证方式、对象及任务

119项任务，来自98个仓库、20个科学领域；最强报告Agent pass@1低于50%。可靠科学指导可改善平均表现或token效率，误导指导可能导致anchoring。

### 5.2 基线、指标与结果

119项任务，来自98个仓库、20个科学领域；最强报告Agent pass@1低于50%。可靠科学指导可改善平均表现或token效率，误导指导可能导致anchoring。

### 5.3 科学贡献与证据强度

建立科学软件工程Agent基准，评估科学知识、探索、修复覆盖和系统集成相关失败。

证据层级：原始全文支持；作者报告结果不等于独立复现。

## 6. 与已有工作的关系

扩展SWE-bench式仓库级coding-agent评测至科学代码仓库，并分析科学指导作用。

## 7. 局限性与风险

每个领域任务数有限；科学知识如何被利用的分析较初步；软件修复成功不等同科学发现能力。

## 8. 对综述写作的价值

用于判定科研基础设施和科学软件Agent是否纳入综述，以及科学软件归类边界。

推荐引用强度：普通引用，可在核对原文后用于相应领域案例。

## 9. 总结

### 9.1 一句话概括

评测科学软件修复Agent

### 9.2 速记版 pipeline

repository-level benchmark覆盖Issue-driven、Expert-exploratory、Engineering-integration任务；Agent在仓库中探索并执行修复，另有配对消融移除显式科学指导。

### 9.3 标注字段汇总

```text
paper_id=ASD-0878
inclusion_status=included
scientific_object_modules=01
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=01
module_taxonomy_codes=01.02
source_level=fulltext
fulltext_followup_required=false
```

### 全文后续要求

本轮已读原始全文并完成对象分类；无需为纳入/分类另做全文补读。具体引用时仍需回查相应原文位置。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O2 既定基准 | 在119项科学软件工程任务的基准上评测 | “119项任务，来自98个仓库、20个科学领域” · L90 |
| 验证强度 | V1 基准/内部评测 | 基准评测，最佳agent通过率低于50% | “最强报告Agent pass@1低于50%” · L62 |
| 系统自主性 | L1 任务助手 | agent在真实仓库执行修复但成功率有限 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
