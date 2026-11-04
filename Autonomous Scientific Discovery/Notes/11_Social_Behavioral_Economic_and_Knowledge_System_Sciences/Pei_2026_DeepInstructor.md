# DeepInstructor: An Agentic AI Instructor for Experience-Driven Idea Evaluation

**论文信息**

- ID：ASD-0918
- 标题：DeepInstructor: An Agentic AI Instructor for Experience-Driven Idea Evaluation
- 作者：Pei, Rongcan; Guo, Fang; Qi, Qinglin; Zhu, Qi; Luo, Yun; Yan, Jianhao; Zhu, Minjun; Xie, Qiujie; Zheng, Dehong; Zhang, Yue
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2609.22104
- 一手阅读来源：https://arxiv.org/abs/2609.22104
- 来源层级：全文
- 阅读版本：对应缓存来源版本，参见Evidence Log
- 阅读版本题名：DeepInstructor: An Agentic AI Instructor for Experience-Driven Idea Evaluation
- 原始全文缓存：C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/.tmp_asd_pdfs/2609_22104.html
- PDF / 本地文件路径：未归档PDF
- 当前状态：included
- 阅读日期：2026-10-22
- 笔记作者：Codex（读者证据包经主控审核整合）

## Evidence Log

| 判断项 | 结论 / 原文概括 | 证据位置 | 可信度 |
|---|---|---|---|
| 论文研究对象为科学研究构想评价和同行评审经验。 | 作者将研究瓶颈定义为科学构想评估，并以新颖性、意义、可行性作为评估维度。 | Abstract、§1 Introduction | high |
| Experience Graph由大规模科学同行评审经验构造。 | 全文描述从58,607份同行评审抽取任务/方法/评价等结构化经验并构图。 | §3.1 Experience Graph Construction | high |
| Agent执行多步检索和推理。 | ReAct Agent先检索知识实体，再检索关系/证据，基于维度策略生成可追溯评价。 | §3.2 Experience Retriever、§3.3.1 Agentic Retrieval and Reasoning | high |
| 评测基于专家构想评分和控制比较数据。 | 全文包含ExpertEval和DeepInstruct的对齐实验，覆盖novelty/significance/feasibility评分与可行性关注点。 | §4 Datasets、§5.1 Results | high |
| 指标衡量与人类判断的一致性。 | 以Hit@±1/Hit@±2等评分容差命中率和可行性问题覆盖/精度度量。 | §4.2 Evaluation Metrics、Table 1 | high |
| 还评测Agent意见反馈是否影响构想生成。 | 全文设置AI-in-the-loop实验，观察评估建议用于构想生成后的变化。 | §5.3 AI-in-the-loop Experiment及Appendix E | high |

## 0. 摘要翻译

DeepInstructor将科研构想评估建模为基于结构化学术经验的推理任务。系统从58,607份同行评审中构造Experience Graph，使用ReAct Agent检索与具体评估维度有关的证据，再评判研究构想的新颖性、重要性和可行性。作者构建DeepInstruct成对比较数据集，并在ExpertEval和DeepInstruct等设置下与基线比较；摘要报告相对人工评分的Hit@1和Hit@2对齐分别提高24.4%和29.7%。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 当前判断：included；读者建议：included。
Agent面向科学研究构想评估这一科研知识生产环节；系统进行经验图谱检索、关系证据取回、维度化推理及评分，具有工具调用和多步研究评审角色。

### 1.2 排除风险检查

归11.07科学知识生产/同行评审研究对象。容易误归01（Agent/检索系统方法）或某个被评估想法所属自然科学模块；但实验测量的是科学界的构想评审过程，没有某一自然科学对象的独立实验，故01不作为正式对象模块，也不按 idea domain 添加自然科学类。核心强度风险中等：Agent评估而非完整发现流程，但明确承担科研评价工作。
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

- object：科学知识生产中的研究构想评价、同行评审经验与评价标准。
- baselines：论文中的既有评估模型/LLM基线及无经验图谱或不同检索配置；具体配置以表格为准。
- metrics：Hit@±1、Hit@±2与可行性concern的mean coverage/precision；人工判断作为参照。
- results：摘要报告相对基线，Hit@1与Hit@2对齐分别提升24.4%和29.7%；应注意这里是摘要报告的相对提升，未将其改写为百分点。

### 2.3 容易混淆的边界

归11.07科学知识生产/同行评审研究对象。容易误归01（Agent/检索系统方法）或某个被评估想法所属自然科学模块；但实验测量的是科学界的构想评审过程，没有某一自然科学对象的独立实验，故01不作为正式对象模块，也不按 idea domain 添加自然科学类。核心强度风险中等：Agent评估而非完整发现流程，但明确承担科研评价工作。

## 3. Agent 系统与科研流程角色

Agent面向科学研究构想评估这一科研知识生产环节；系统进行经验图谱检索、关系证据取回、维度化推理及评分，具有工具调用和多步研究评审角色。

科研流程与自主能力以本文实际行动和工具调用为依据：

从同行评审文本抽取并聚合学术经验图谱；通过实体召回与关系检索寻找相关评价证据；ReAct Agent按评估维度检索、推理，LLM scorer输出分数/风险意见。以专家评价和成对比较集为参照开展评分一致性及AI-in-the-loop实验。

## 4. 方法设计

### 4.1 方法动机与设计

把研究构想评价从仅靠模型参数知识或无结构检索，转向可追溯的学术经验图谱检索与维度化Agent推理；研究对象直接属于科学评价和知识生产系统。

### 4.2 系统流程与组件

从同行评审文本抽取并聚合学术经验图谱；通过实体召回与关系检索寻找相关评价证据；ReAct Agent按评估维度检索、推理，LLM scorer输出分数/风险意见。以专家评价和成对比较集为参照开展评分一致性及AI-in-the-loop实验。

## 5. 实验与验证

### 5.1 验证方式、对象及任务

- object：科学知识生产中的研究构想评价、同行评审经验与评价标准。
- baselines：论文中的既有评估模型/LLM基线及无经验图谱或不同检索配置；具体配置以表格为准。
- metrics：Hit@±1、Hit@±2与可行性concern的mean coverage/precision；人工判断作为参照。
- results：摘要报告相对基线，Hit@1与Hit@2对齐分别提升24.4%和29.7%；应注意这里是摘要报告的相对提升，未将其改写为百分点。

### 5.2 基线、指标与结果

- object：科学知识生产中的研究构想评价、同行评审经验与评价标准。
- baselines：论文中的既有评估模型/LLM基线及无经验图谱或不同检索配置；具体配置以表格为准。
- metrics：Hit@±1、Hit@±2与可行性concern的mean coverage/precision；人工判断作为参照。
- results：摘要报告相对基线，Hit@1与Hit@2对齐分别提升24.4%和29.7%；应注意这里是摘要报告的相对提升，未将其改写为百分点。

### 5.3 科学贡献与证据强度

把研究构想评价从仅靠模型参数知识或无结构检索，转向可追溯的学术经验图谱检索与维度化Agent推理；研究对象直接属于科学评价和知识生产系统。

证据层级：原始全文支持；作者报告结果不等于独立复现。

## 6. 与已有工作的关系

与自动同行评审、研究构想生成/评分及检索增强评价相关；本文强调从真实评审经验中提取结构化证据，并让Agent检索解释其评分。

## 7. 局限性与风险

图谱经验来源和覆盖范围会影响评价；摘要/全文显示来源集中于限定的会议年份语料，外推到不同学科、期刊及真实评审情境需谨慎。评分对齐不是科研构想真实新颖性或可行性最终真值。

## 8. 对综述写作的价值

展示Agent参与科研生命周期中研究构想筛选与评审的方式，可支持11.07与自然科学对象Agent的角色边界讨论。

推荐引用强度：普通引用，可在核对原文后用于相应领域案例。

## 9. 总结

### 9.1 一句话概括

Agent以评审经验评价研究创意

### 9.2 速记版 pipeline

从同行评审文本抽取并聚合学术经验图谱；通过实体召回与关系检索寻找相关评价证据；ReAct Agent按评估维度检索、推理，LLM scorer输出分数/风险意见。以专家评价和成对比较集为参照开展评分一致性及AI-in-the-loop实验。

### 9.3 标注字段汇总

```text
paper_id=ASD-0918
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


## 2026-10-29 PDF补齐归档

- 本地PDF：`Reference_PDF/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/ASD-0918_DeepInstructor_An_Agentic_AI_Instructor_for_Experience_Driven_Idea_Evaluation.pdf`，共28页；已核验标题、页面解析和逐页渲染。
- 下载来源：https://arxiv.org/pdf/2609.22104
- 版本：official arXiv preprint PDF; version as downloaded。
- 本轮为来源文件归档，不自动改变既有科学分类或将未决PR意见标记为已结案。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O3 新实例 | 从学术同行评审经验图谱检索证据评估科研构想，评分维度和标准可由人类判断核对 | “从58,607份同行评审抽取任务/方法/评价等结构化经验” · L26 |
| 验证强度 | V1 基准/内部评测 | 与人类专家评分对齐度量，使用Hit@±1/Hit@±2等指标 | “Hit@1与Hit@2对齐分别提升24.4%和29.7%” · L96 |
| 系统自主性 | L1 任务助手 |  | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
