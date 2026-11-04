# EarthVerse: Benchmarking Scientific Agents Across Dynamic Earth Systems and Natural Hazards

**论文信息**

- ID：ASD-0916
- 标题：EarthVerse: Benchmarking Scientific Agents Across Dynamic Earth Systems and Natural Hazards
- 作者：Cui, Zhiqing; Yin, Xinxiang; Tang, Yihong; Zhang, Xinglang; Hu, Yuanzhe; Zhong, Siru; Tang, Weidong; Liang, Yuxuan; Li, Weijia; Jin, Ming; Pan, Shirui; Kang, Yuhao; Zhuang, Dingyi; Zhao, Jinhua
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2608.23525
- 一手阅读来源：https://arxiv.org/abs/2608.23525
- 来源层级：全文
- 阅读版本：对应缓存来源版本，参见Evidence Log
- 阅读版本题名：EarthVerse: Benchmarking Scientific Agents Across Dynamic Earth Systems and Natural Hazards
- 原始全文缓存：C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/.tmp_asd_pdfs/2608_23525.html
- PDF / 本地文件路径：未归档PDF
- 当前状态：included
- 阅读日期：2026-10-22
- 笔记作者：Codex（读者证据包经主控审核整合）

## Evidence Log

| 判断项 | 结论 / 原文概括 | 证据位置 | 可信度 |
|---|---|---|---|
| benchmark任务覆盖真实地球系统灾害与极端事件。 | 全文报告199个真实灾害/极端事件和405项调查任务。 | Abstract、§3 Benchmark Construction | high |
| 每题要求自行发现多源证据，而不是消费指定图表。 | 事件包来自多种外部来源；任务提示事件和科学决策但不直接给出相关文件，作者报告平均需要约7.26个来源。 | §3.1 Benchmark Construction、§3.2 Task Construction | high |
| 调查包含反复的证据访问、计算与物理解释。 | 全文描述Agent确定事件窗口、区域、危险演变和证据族，随后在定向取证、计算、物理解释之间迭代。 | §3.2 Task Construction: Event-scale scientific iteration | high |
| 评分同时看结论答案单元与研究过程/证据支持。 | 提供可执行ground truth，将答案分解为细粒度单元并以任务rubric评估支持过程；支持多条有效调查路径。 | §3 Benchmark Construction、评分说明 | high |
| 评测有25套模型/Agent系统及明确的端到端可靠性结果。 | 受控工具使用协议评测25个系统；摘要报告最佳平均answer-unit accuracy 84.65%，最高Strict@95 34.81%。 | Abstract、§4 Evaluation | high |
| 作者将错误定位到科研工作流的多个环节。 | 全文分析证据访问、工具选择、记忆、推理、交互、科学执行及轨迹错误。 | Abstract、Appendix D/G | high |

## 0. 摘要翻译

EarthVerse提出地球系统与自然灾害科学Agent benchmark。任务围绕199个真实灾害/极端事件构建405项可复现调查，要求Agent从异质事件资料包中发现证据、执行计算、调和来源差异并保留证据出处。作者在受控工具使用协议下评测25个模型与Agent系统；最佳平均答案单元准确率为84.65%，最高Strict@95为34.81%，显示局部步骤正确不等于完整科学证据链可靠。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 当前判断：included；读者建议：included。
基准明确要求科学Agent围绕自然灾害和动态地球系统问题进行多步证据调查；Agent需选择资料、计算、解释并根据冲突修正结论，工具反馈、规划与迭代角色清晰。

### 1.2 排除风险检查

归05地球环境科学，细分代码取05.03.07（环境风险与环境健康）：具体对象是地球系统、气候/天气/水文灾害过程及地学证据。虽然涉及基础设施、风险决策和跨部门影响，但工程系统并非本benchmark核心研究对象，故不因此加09/11。邻近边界风险低。
完整闭环不是纳入门槛；科研目标、多步行动、至少一项Agent能力及明确科研角色须同时成立。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：05
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：05（仅归档，不替代多模块事实）
- 模块内分类路径：05.03.07
- 分类深度：03/04使用二级；06/07使用固定三级；其余沿用现有树。
- 分类状态：原文证据复核

### 2.2 对象优先判定

- object：地球系统动态过程和自然灾害/极端事件调查，包括天气、气候和水文风险等。
- baselines：评测25种模型/Agent；可比系统细节在主文/附录系统清单中列出，本证据包不臆测具体最佳模型名称。
- metrics：mean answer-unit accuracy；Strict@95；过程rubric/证据支持和轨迹诊断。
- results：摘要报告最佳平均答案单元准确率84.65%，最高Strict@95 34.81%；端到端严格完成度明显低于局部答案单元准确率。

### 2.3 容易混淆的边界

归05地球环境科学，细分代码取05.03.07（环境风险与环境健康）：具体对象是地球系统、气候/天气/水文灾害过程及地学证据。虽然涉及基础设施、风险决策和跨部门影响，但工程系统并非本benchmark核心研究对象，故不因此加09/11。邻近边界风险低。

## 3. Agent 系统与科研流程角色

基准明确要求科学Agent围绕自然灾害和动态地球系统问题进行多步证据调查；Agent需选择资料、计算、解释并根据冲突修正结论，工具反馈、规划与迭代角色清晰。

科研流程与自主能力以本文实际行动和工具调用为依据：

从事件调查中构造任务包和答案单元，将事件名/科学决策需求作为提示而不指定答案文件；Agent通过工具在候选证据中检索、计算、核对单位与尺度、形成解释并保留来源。用细粒度答案单元与过程rubric评分，并执行轨迹、错误路径和干预分析。

## 4. 方法设计

### 4.1 方法动机与设计

把自然灾害地球科学分析建模为事件尺度的动态证据调查任务，评估多源检索、量纲/尺度绑定、可追溯计算和机制解释能否在同一Agent轨迹中保持一致。

### 4.2 系统流程与组件

从事件调查中构造任务包和答案单元，将事件名/科学决策需求作为提示而不指定答案文件；Agent通过工具在候选证据中检索、计算、核对单位与尺度、形成解释并保留来源。用细粒度答案单元与过程rubric评分，并执行轨迹、错误路径和干预分析。

## 5. 实验与验证

### 5.1 验证方式、对象及任务

- object：地球系统动态过程和自然灾害/极端事件调查，包括天气、气候和水文风险等。
- baselines：评测25种模型/Agent；可比系统细节在主文/附录系统清单中列出，本证据包不臆测具体最佳模型名称。
- metrics：mean answer-unit accuracy；Strict@95；过程rubric/证据支持和轨迹诊断。
- results：摘要报告最佳平均答案单元准确率84.65%，最高Strict@95 34.81%；端到端严格完成度明显低于局部答案单元准确率。

### 5.2 基线、指标与结果

- object：地球系统动态过程和自然灾害/极端事件调查，包括天气、气候和水文风险等。
- baselines：评测25种模型/Agent；可比系统细节在主文/附录系统清单中列出，本证据包不臆测具体最佳模型名称。
- metrics：mean answer-unit accuracy；Strict@95；过程rubric/证据支持和轨迹诊断。
- results：摘要报告最佳平均答案单元准确率84.65%，最高Strict@95 34.81%；端到端严格完成度明显低于局部答案单元准确率。

### 5.3 科学贡献与证据强度

把自然灾害地球科学分析建模为事件尺度的动态证据调查任务，评估多源检索、量纲/尺度绑定、可追溯计算和机制解释能否在同一Agent轨迹中保持一致。

证据层级：原始全文支持；作者报告结果不等于独立复现。

## 6. 与已有工作的关系

与遥感问答、地理空间推理和地球科学工具Agent基准有关；EarthVerse从预先选定数据/图像进一步推进到开放事件资料包中的证据发现和研究过程评估。

## 7. 局限性与风险

benchmark任务仍依赖作者构建和审计的事件包、评分单元及工具协议；严格评分低也可能反映任务链长和来源异质性。它测量基准任务能力，不能等同真实灾害现场部署成效。

## 8. 对综述写作的价值

是05类最直接的科学Agent基准之一，可用于讨论从单项地学问答迈向可追溯、多源、事件尺度研究流程的评测差距。

推荐引用强度：普通引用，可在核对原文后用于相应领域案例。

## 9. 总结

### 9.1 一句话概括

在地球灾害任务中评测科学Agent

### 9.2 速记版 pipeline

从事件调查中构造任务包和答案单元，将事件名/科学决策需求作为提示而不指定答案文件；Agent通过工具在候选证据中检索、计算、核对单位与尺度、形成解释并保留来源。用细粒度答案单元与过程rubric评分，并执行轨迹、错误路径和干预分析。

### 9.3 标注字段汇总

```text
paper_id=ASD-0916
inclusion_status=included
scientific_object_modules=05
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=05
module_taxonomy_codes=05.03.07
source_level=fulltext
fulltext_followup_required=false
```

### 全文后续要求

本轮已读原始全文并完成对象分类；无需为纳入/分类另做全文补读。具体引用时仍需回查相应原文位置。


## 2026-10-29 PDF补齐归档

- 本地PDF：`Reference_PDF/05_Earth_and_Environmental_Sciences/ASD-0916_EarthVerse_Benchmarking_Scientific_Agents_Across_Dynamic_Earth_Systems_and_Natural_Hazards.pdf`，共46页；已核验标题、页面解析和逐页渲染。
- 下载来源：https://arxiv.org/pdf/2608.23525v1
- 版本：official arXiv preprint PDF; version as downloaded。
- 本轮为来源文件归档，不自动改变既有科学分类或将未决PR意见标记为已结案。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O3 新实例 | 针对199个真实灾害事件的调查任务，要求从事件包中发现证据、执行计算并解释，答案可由ground truth验证 | “199个真实灾害/极端事件和405项调查任务” · L25 |
| 验证强度 | V2 计算/仿真/回顾性 | 提供可执行ground truth和细粒度答案单元，评估过程rubric和证据支持，属计算验证 | “提供可执行ground truth，将答案分解为细粒度单元” · L28 |
| 系统自主性 | L2 闭环执行者 |  | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
