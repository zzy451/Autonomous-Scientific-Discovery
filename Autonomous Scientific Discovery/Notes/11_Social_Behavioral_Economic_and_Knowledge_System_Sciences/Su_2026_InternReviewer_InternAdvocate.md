# InternReviewer & InternAdvocate: Objective Reward and Evaluation for Agentic Reinforcement Learning in Peer Review and Rebuttal

**论文信息**

- ID：ASD-0910
- 标题：InternReviewer & InternAdvocate: Objective Reward and Evaluation for Agentic Reinforcement Learning in Peer Review and Rebuttal
- 作者：Su, Xuerui; Guo, Liya; Pei, Qizhi; Guo, Qipeng; Tian, Zhongbo; Wu, Lijun; Chen, Kai; Wang, Zun
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2608.28612
- 一手阅读来源：https://arxiv.org/abs/2608.28612
- 来源层级：全文
- 阅读版本：对应缓存来源版本，参见Evidence Log
- 阅读版本题名：InternReviewer & InternAdvocate: Objective Reward and Evaluation for Agentic Reinforcement Learning in Peer Review and Rebuttal
- 原始全文缓存：C:/Users/20683/Desktop/综述/.tmp_asd_pdfs/source_F/2608.28612.html
- PDF / 本地文件路径：未归档PDF
- 当前状态：included
- 阅读日期：2026-10-22
- 笔记作者：Codex（读者证据包经主控审核整合）

## Evidence Log

| 判断项 | 结论 / 原文概括 | 证据位置 | 可信度 |
|---|---|---|---|
| Agent角色 | InternReviewer和InternAdvocate分别执行评审与作者答辩。 | §1 Introduction；§3 Methods | high |
| 多步交互 | MDP状态会追加搜索结果或文本片段；Agent轨迹由推理动作与工具调用组成。 | §3.1 Problem Formulation | high |
| 数据规模 | 官方OpenReview API来源涵盖ICLR、NeurIPS、ICML，论文报告184,857组评审—答辩数据。 | §3.2 Data Collection and Curation | high |
| 检索工具 | 系统接入arXiv检索，并按投稿时间截断可引用的文献。 | §3.3.1–3.3.2；Appendix A.3 | high |
| 奖励机制 | 复合奖励覆盖语义对齐、结构合规、引用核验和多步工具使用。 | §3.3.3 Objective Reward Function | high |
| 实验结果 | 作者报告提出的专用Agent在多个任务相关指标领先，并另做人类偏好评估。 | §4.3 Main Results；§4.5 | high |

## 0. 摘要翻译

本文训练InternReviewer同行评审Agent和InternAdvocate作者答辩Agent，使用跨会议OpenReview数据、arXiv检索、时间截断与引用核验。任务被形式化为带工具调用和反馈的MDP，并以Agentic RL优化语义对齐、结构合规、引用真实性及工具使用。作者报告专用Agent在格式、工具、引用、幻觉和语义评价等指标领先。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 当前判断：included；读者建议：included。
两种Agent分别承担科研评审和作者答辩角色；其MDP轨迹交错推理与检索工具调用，并依据环境反馈和复合奖励优化，符合四项Agent纳入标准。

### 1.2 排除风险检查

研究对象直接是同行评议与学术答辩，归11.07；虽然使用通用文献检索工具，但科研制度角色明确，不归01.04。
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

对象为学术论文评审、作者答辩和科研论证引用。数据包含ICLR、NeurIPS、ICML的184,857组review-rebuttal pairs。基线为闭源前沿模型及既有训练系统。指标包括Format、Tool、Citation、Hallucination、POLAR及人类偏好；作者报告提出Agent在多项任务指标排名第一，精确表格值未在本证据包转录。

### 2.3 容易混淆的边界

研究对象直接是同行评议与学术答辩，归11.07；虽然使用通用文献检索工具，但科研制度角色明确，不归01.04。

## 3. Agent 系统与科研流程角色

两种Agent分别承担科研评审和作者答辩角色；其MDP轨迹交错推理与检索工具调用，并依据环境反馈和复合奖励优化，符合四项Agent纳入标准。

科研流程与自主能力以本文实际行动和工具调用为依据：

整理OpenReview评审—答辩数据；将任务建模为MDP中的推理与检索动作；接入arXiv搜索并依据投稿时间过滤；使用语义对齐、结构、引用核验和工具行为构造Agentic RL奖励。

## 4. 方法设计

### 4.1 方法动机与设计

将主动文献检索与可验证引用纳入评审/答辩Agent训练，并以客观奖励代替单一主观评价。

### 4.2 系统流程与组件

整理OpenReview评审—答辩数据；将任务建模为MDP中的推理与检索动作；接入arXiv搜索并依据投稿时间过滤；使用语义对齐、结构、引用核验和工具行为构造Agentic RL奖励。

## 5. 实验与验证

### 5.1 验证方式、对象及任务

对象为学术论文评审、作者答辩和科研论证引用。数据包含ICLR、NeurIPS、ICML的184,857组review-rebuttal pairs。基线为闭源前沿模型及既有训练系统。指标包括Format、Tool、Citation、Hallucination、POLAR及人类偏好；作者报告提出Agent在多项任务指标排名第一，精确表格值未在本证据包转录。

### 5.2 基线、指标与结果

对象为学术论文评审、作者答辩和科研论证引用。数据包含ICLR、NeurIPS、ICML的184,857组review-rebuttal pairs。基线为闭源前沿模型及既有训练系统。指标包括Format、Tool、Citation、Hallucination、POLAR及人类偏好；作者报告提出Agent在多项任务指标排名第一，精确表格值未在本证据包转录。

### 5.3 科学贡献与证据强度

将主动文献检索与可验证引用纳入评审/答辩Agent训练，并以客观奖励代替单一主观评价。

证据层级：原始全文支持；作者报告结果不等于独立复现。

## 6. 与已有工作的关系

连接prompt-based AI review、review专用监督训练和强化学习评审系统；本文突出内生检索轨迹与引用真实性。

## 7. 局限性与风险

作者指出数学密集或图表复杂论文会增加MinerU解析及上下文窗口负担；检索来源还可扩展。评估依赖整理后的训练数据与reranker等奖励模型。

## 8. 对综述写作的价值

提供同行评审与答辩Agent的完整工具使用、训练和验证案例，可支撑11.07知识生产流程自动化分析。

推荐引用强度：普通引用，可在核对原文后用于相应领域案例。

## 9. 总结

### 9.1 一句话概括

以证据检索支持审稿与回复

### 9.2 速记版 pipeline

整理OpenReview评审—答辩数据；将任务建模为MDP中的推理与检索动作；接入arXiv搜索并依据投稿时间过滤；使用语义对齐、结构、引用核验和工具行为构造Agentic RL奖励。

### 9.3 标注字段汇总

```text
paper_id=ASD-0910
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

- 本地PDF：`Reference_PDF/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/ASD-0910_InternReviewer_InternAdvocate_Objective_Reward_and_Evaluation_for_Agentic_Reinforcement_Learning_in_Peer_.pdf`，共44页；已核验标题、页面解析和逐页渲染。
- 下载来源：https://arxiv.org/pdf/2608.28612
- 版本：official arXiv preprint PDF; version as downloaded。
- 本轮为来源文件归档，不自动改变既有科学分类或将未决PR意见标记为已结案。
