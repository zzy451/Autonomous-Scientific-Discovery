# AgentIdeaBench: Benchmarking Scientific Ideation in the Agent Era

**论文信息**

- ID：ASD-0912
- 标题：AgentIdeaBench: Benchmarking Scientific Ideation in the Agent Era
- 作者：Mo, Yunxiang; Zheng, Tianshi; Gao, Yisen; Wang, Rui; Nam, Newt Nguyen Kim Hue; Tam, Kelvin Kiu Wai; Bai, Jiaxin; Song, Yangqiu; Wong, Ginny; See, Simon
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2609.07611
- 一手阅读来源：https://arxiv.org/abs/2609.07611
- 来源层级：全文
- 阅读版本：对应缓存来源版本，参见Evidence Log
- 阅读版本题名：AgentIdeaBench: Benchmarking Scientific Ideation in the Agent Era
- 原始全文缓存：C:/Users/20683/Desktop/综述/.tmp_asd_pdfs/source_F/2609.07611.pdf
- PDF / 本地文件路径：Reference_PDF/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Mo_2026_AgentIdeaBench.pdf
- 当前状态：included
- 阅读日期：2026-10-22
- 笔记作者：Codex（读者证据包经主控审核整合）

## Evidence Log

| 判断项 | 结论 / 原文概括 | 证据位置 | 可信度 |
|---|---|---|---|
| 实验条件 | Static接收固定文献；Active只给主题和检索工具，须自主找证据后提出假设。 | §3.2 Static and Active Settings | high |
| 领域覆盖 | 计分范围覆盖计算机、物理、生物、化学、医学五学科及40个细分主题。 | §3.1；§4 Experimental Setup | high |
| 工具使用 | Agent调用Semantic Scholar搜索/获取文献，并受固定调用预算约束。 | §3.2；Appendix C | high |
| 结果趋势 | 全文报告Active评分随知识截止年份约+1.16分/年，Static约+0.54分/年。 | §5.1–5.2 | high |
| 评分维度 | Active提高可行性、清晰度和具体性；原创性差−0.14且不显著。 | §5.3 | high |
| 限制 | thought-experiment结果未通过多重比较校正且未胜过compute-matched基线，作者称其尚未证实。 | §6；Limitations | high |

## 0. 摘要翻译

AgentIdeaBench对比静态阅读预先整理文献和主动探索文献两种科学构想生成方式，覆盖计算机、物理、生物、化学和医学五个学科的40个细分主题。Active Agent使用Semantic Scholar工具收集证据后提出可检验假设。结果显示主动设置提升可行性、清晰度和具体性，但测得的原创性没有显著提升。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 当前判断：included；读者建议：included。
Active条件要求Agent主动搜索与获取文献，再形成科研假设，具备工具使用、多步证据收集和明确的科学构想角色，符合Agent标准。

### 1.2 排除风险检查

归11.07：对象是科研知识生产中的假设提出及其相对于既有研究的新颖性，而非某一具体自然科学发现。与01.04通用benchmark相邻，但研究的直接对象是科学构想流程。
完整闭环不是纳入门槛；科研目标、多步行动、至少一项Agent能力及明确科研角色须同时成立。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：11
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：11（仅归档，不替代多模块事实）
- 模块内分类路径：11.07
- 分类深度：03/04使用二级；06/07使用固定三级；其余沿用现有树。
- 分类状态：原文证据复核

### 2.2 对象优先判定

对象为科学假设生成和其相对已有文献的新颖性。覆盖五学科、40细分主题，主分析有33个模型完成配对评估。对照包括静态给定文献、recall-only和主动检索。指标为新颖性、可行性、清晰度、具体性、影响力等评分。按知识截止年份Active/Static评分增长约+1.16/+0.54分/年；Active提高可行性+1.21、清晰度+0.63、具体性+0.58，原创性变化−0.14且不显著。

### 2.3 容易混淆的边界

归11.07：对象是科研知识生产中的假设提出及其相对于既有研究的新颖性，而非某一具体自然科学发现。与01.04通用benchmark相邻，但研究的直接对象是科学构想流程。

## 3. Agent 系统与科研流程角色

Active条件要求Agent主动搜索与获取文献，再形成科研假设，具备工具使用、多步证据收集和明确的科学构想角色，符合Agent标准。

科研流程与自主能力以本文实际行动和工具调用为依据：

为Static和Active设置配对任务；Active条件调用Semantic Scholar search/fetch工具并受固定调用预算约束；以prior-art critic评估假设；额外探索thought-experiment反馈修订。

## 4. 方法设计

### 4.1 方法动机与设计

把科学构想评测扩展为Agent主动控制文献检索，并在配对条件下比较静态信息和主动探索。

### 4.2 系统流程与组件

为Static和Active设置配对任务；Active条件调用Semantic Scholar search/fetch工具并受固定调用预算约束；以prior-art critic评估假设；额外探索thought-experiment反馈修订。

## 5. 实验与验证

### 5.1 验证方式、对象及任务

对象为科学假设生成和其相对已有文献的新颖性。覆盖五学科、40细分主题，主分析有33个模型完成配对评估。对照包括静态给定文献、recall-only和主动检索。指标为新颖性、可行性、清晰度、具体性、影响力等评分。按知识截止年份Active/Static评分增长约+1.16/+0.54分/年；Active提高可行性+1.21、清晰度+0.63、具体性+0.58，原创性变化−0.14且不显著。

### 5.2 基线、指标与结果

对象为科学假设生成和其相对已有文献的新颖性。覆盖五学科、40细分主题，主分析有33个模型完成配对评估。对照包括静态给定文献、recall-only和主动检索。指标为新颖性、可行性、清晰度、具体性、影响力等评分。按知识截止年份Active/Static评分增长约+1.16/+0.54分/年；Active提高可行性+1.21、清晰度+0.63、具体性+0.58，原创性变化−0.14且不显著。

### 5.3 科学贡献与证据强度

把科学构想评测扩展为Agent主动控制文献检索，并在配对条件下比较静态信息和主动探索。

证据层级：原始全文支持；作者报告结果不等于独立复现。

## 6. 与已有工作的关系

连接静态idea-generation benchmark、科学假设生成和端到端AI scientist研究；聚焦科研流程中的构想子任务。

## 7. 局限性与风险

Active与Static差异还包括多轮交互和工具能力，未完全拆解单一检索因素；评分依赖LLM critic；thought-experiment附加收益尚未确认。

## 8. 对综述写作的价值

为科学构想Agent和文献探索提供跨学科评估证据，同时展示Agent检索可提升假设落地性但不必然提升原创性。

推荐引用强度：普通引用，可在核对原文后用于相应领域案例。

## 9. 总结

### 9.1 一句话概括

评测科研创意生成与原创性

### 9.2 速记版 pipeline

为Static和Active设置配对任务；Active条件调用Semantic Scholar search/fetch工具并受固定调用预算约束；以prior-art critic评估假设；额外探索thought-experiment反馈修订。

### 9.3 标注字段汇总

```text
paper_id=ASD-0912
inclusion_status=included
scientific_object_modules=11
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=11
module_taxonomy_codes=11.07
source_level=fulltext
fulltext_followup_required=false
```

### 全文后续要求

本轮已读原始全文并完成对象分类；无需为纳入/分类另做全文补读。具体引用时仍需回查相应原文位置。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O3 新实例 | Agent主动检索文献后提出科学假设，假设新颖性由评分器相对已有文献评判，答案可知 | “Active Agent使用Semantic Scholar工具收集证据后提出可检验假设” · L34 |
| 验证强度 | V1 基准/内部评测 | 使用LLM critic评分新颖性、可行性等维度，与静态条件配对比较 | “Active提高可行性+1.21、清晰度+0.63、具体性+0.58” · L90 |
| 系统自主性 | L2 闭环执行者 |  | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
