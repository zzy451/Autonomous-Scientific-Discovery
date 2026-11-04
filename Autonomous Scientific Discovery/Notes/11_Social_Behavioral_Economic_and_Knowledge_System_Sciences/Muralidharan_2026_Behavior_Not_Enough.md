# Behavior is Not Enough: A Mechanism-Based Evaluation of Social Norm Emergence in LLM Societies

**论文信息**

- ID：ASD-0920
- 标题：Behavior is Not Enough: A Mechanism-Based Evaluation of Social Norm Emergence in LLM Societies
- 作者：Muralidharan, Rasika; Kwak, Haewoon; An, Jisun
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2609.26481
- 一手阅读来源：https://arxiv.org/abs/2609.26481
- 来源层级：全文
- 阅读版本：对应缓存来源版本，参见Evidence Log
- 阅读版本题名：Behavior is Not Enough: A Mechanism-Based Evaluation of Social Norm Emergence in LLM Societies
- 原始全文缓存：C:/Users/20683/Desktop/综述/.tmp_asd_pdfs/source_F/2609.26481.pdf
- PDF / 本地文件路径：Reference_PDF/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Muralidharan_2026_Behavior_Not_Enough.pdf
- 当前状态：included
- 阅读日期：2026-10-22
- 笔记作者：Codex（读者证据包经主控审核整合）

## Evidence Log

| 判断项 | 结论 / 原文概括 | 证据位置 | 可信度 |
|---|---|---|---|
| 概念定义 | 规范由行为及共享期待构成，期待分为经验期待和规范期待。 | Introduction | high |
| 环境规模 | 12个Agent进行20轮PGG，分三组，每人初始10单位，公共贡献乘数1.6。 | Methods: Environment and Interaction Protocol | high |
| 多步互动 | 每轮组内累积讨论后决定贡献，回合结束私下报告两类期待。 | Methods: Interaction Protocol | high |
| 消融设计 | 比较纯baseline、expectation-only、E+SL、E+SS和E+SL+SS。 | Methods: Ablations | high |
| 重复评估 | 四个模型家族，每模型/条件十次独立运行，并进行按run聚类OLS/Wald检验。 | Evaluation and Results | high |
| 发现 | 期待询问提高贡献；social learning稳定行为；social selection能识别合作者但强化有限。 | Evaluation and Results | high |
| 对象边界 | 研究日常社会规范和合作，而不是科学系统或科研知识生产。 | Introduction；Discussion | high |

## 0. 摘要翻译

研究LLM社会中规范形成的机制。12个Agent参与20轮公共物品博弈，逐轮讨论、贡献资源、报告经验/规范期待并经历社会网络群体选择。机制消融显示，期待询问提升合作贡献，社会学习稳定行为；社会选择可识别合作者但没有明显强化贡献。扰动后期待和行为的恢复路径也不同。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 当前判断：included；读者建议：included。
Agent在多轮公共物品博弈中互动、反馈并调整贡献和群体关系，研究其社会行为机制，具备多步行动、互动和明确研究角色。

### 1.2 排除风险检查

研究一般社会行为和社会规范，归11.02；不是科研共同体、科学知识生产或同行评议研究，不归11.07。
完整闭环不是纳入门槛；科研目标、多步行动、至少一项Agent能力及明确科研角色须同时成立。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：11
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：11（仅归档，不替代多模块事实）
- 模块内分类路径：11.02
- 分类深度：03/04使用二级；06/07使用固定三级；其余沿用现有树。
- 分类状态：原文证据复核

### 2.2 对象优先判定

对象为一般社会规范与合作行为。12个Agent、20轮、三组各4人；每人初始10单位、公共贡献乘数1.6。基线含纯baseline、expectation-only、E+SL、E+SS、E+SL+SS；四模型家族，每个模型/条件10次独立运行。测贡献、共享期待、期待—行为对齐及扰动恢复；期待询问提高贡献，社会学习稳定行为，社会选择识别合作者但强化有限。

### 2.3 容易混淆的边界

研究一般社会行为和社会规范，归11.02；不是科研共同体、科学知识生产或同行评议研究，不归11.07。

## 3. Agent 系统与科研流程角色

Agent在多轮公共物品博弈中互动、反馈并调整贡献和群体关系，研究其社会行为机制，具备多步行动、互动和明确研究角色。

科研流程与自主能力以本文实际行动和工具调用为依据：

重复公共物品博弈；Agent在每轮先讨论再贡献资源，私下报告期待，之后社会网络更新；设置五种机制消融与扰动实验，覆盖四模型家族。

## 4. 方法设计

### 4.1 方法动机与设计

把规范形成拆分为行为、共享期待和社会学习/选择机制，避免仅凭行为趋同推断社会规范。

### 4.2 系统流程与组件

重复公共物品博弈；Agent在每轮先讨论再贡献资源，私下报告期待，之后社会网络更新；设置五种机制消融与扰动实验，覆盖四模型家族。

## 5. 实验与验证

### 5.1 验证方式、对象及任务

对象为一般社会规范与合作行为。12个Agent、20轮、三组各4人；每人初始10单位、公共贡献乘数1.6。基线含纯baseline、expectation-only、E+SL、E+SS、E+SL+SS；四模型家族，每个模型/条件10次独立运行。测贡献、共享期待、期待—行为对齐及扰动恢复；期待询问提高贡献，社会学习稳定行为，社会选择识别合作者但强化有限。

### 5.2 基线、指标与结果

对象为一般社会规范与合作行为。12个Agent、20轮、三组各4人；每人初始10单位、公共贡献乘数1.6。基线含纯baseline、expectation-only、E+SL、E+SS、E+SL+SS；四模型家族，每个模型/条件10次独立运行。测贡献、共享期待、期待—行为对齐及扰动恢复；期待询问提高贡献，社会学习稳定行为，社会选择识别合作者但强化有限。

### 5.3 科学贡献与证据强度

把规范形成拆分为行为、共享期待和社会学习/选择机制，避免仅凭行为趋同推断社会规范。

证据层级：原始全文支持；作者报告结果不等于独立复现。

## 6. 与已有工作的关系

连接行为经济学公共物品博弈、LLM社会模拟和规范涌现研究。

## 7. 局限性与风险

LLM社会模拟不等同真实人类规范；作者把期待报告作为操作化测量，并不宣称它是人类心理状态。结论依赖博弈参数、提示和模型。

## 8. 对综述写作的价值

提供有明确机制、对照条件和多轮Agent互动的社会行为实验样本，支持11.02分类。

推荐引用强度：普通引用，可在核对原文后用于相应领域案例。

## 9. 总结

### 9.1 一句话概括

以机制检验模拟社会中的规范

### 9.2 速记版 pipeline

重复公共物品博弈；Agent在每轮先讨论再贡献资源，私下报告期待，之后社会网络更新；设置五种机制消融与扰动实验，覆盖四模型家族。

### 9.3 标注字段汇总

```text
paper_id=ASD-0920
inclusion_status=included
scientific_object_modules=11
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=11
module_taxonomy_codes=11.02
source_level=fulltext
fulltext_followup_required=false
```

### 全文后续要求

本轮已读原始全文并完成对象分类；无需为纳入/分类另做全文补读。具体引用时仍需回查相应原文位置。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O3 新实例 | 在公共物品博弈中测试社会规范形成机制，答案可由Agent行为、期待报告和扰动响应计算验证 | “12个Agent参与20轮公共物品博弈” · L35 |
| 验证强度 | V2 计算/仿真/回顾性 | 多次独立运行并聚类OLS/Wald检验，测量贡献、期待和期待-行为对齐，属计算实验 | “每模型/条件十次独立运行，并进行按run聚类OLS/Wald检验” · L29 |
| 系统自主性 | L1 任务助手 |  | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
