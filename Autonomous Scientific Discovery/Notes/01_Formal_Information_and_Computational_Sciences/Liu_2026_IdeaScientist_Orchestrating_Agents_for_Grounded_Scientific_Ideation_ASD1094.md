# IdeaScientist: Orchestrating Agents for Grounded Scientific Ideation

## 当前分类（2026-11-01 实证复核）

- 当前纳入状态：`to_read`；主归档：`01`。
- 本块为当前有效结论；后文既有分类、来源限制与审计判断均保留为历史记录，与本块不一致者由本块取代。
- 当前对象模块：`01`。
- 代表分类每个模块保留一个落点，不表示穷尽全文全部细类。

| 模块 | 二级 | 三级 | 本轮结论 |
|---|---|---|---|
| 01 | 01.02 计算机科学 | 01.02.12 人工智能 | 已落地 |

- 模块11：评价机器学习方案生成的新颖性和质量；未形成独立科学系统对象；保留既有01计算研究对象。
  - 证据：PDF 第 [6, 7] 页；原文：Proposal quality measures the research proposal on six criteria commonly used in conference peer review

- 完整裁决：`Coverage_Check/classification_recheck_2026-11-01/`。

## 既有笔记与历史审计记录

**论文信息**

- ID：ASD-1094
- 标题：IdeaScientist: Orchestrating Agents for Grounded Scientific Ideation
- 作者：Jiarui Liu; Renjie Tao; Yiwei Liao; Chuanyang Jin; Kai Sun; Xiao Yang; Xinyuan Zhang; Xilun Chen; Zhuangqun Huang; Lechen Zhang; Yongjin Yang; Yinghui He; Weihao Xuan; Rakesh Wanga; Anuj Kumar; Mona T. Diab; Wen-tau Yih; Xin Luna Dong
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2610.04074
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1094.txt
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Liu_2026_IdeaScientist_Orchestrating_Agents_for_Grounded_Scientific_Ideation_ASD1094.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 机器学习研究案例 | 附录说明四个案例比较人工、IdeaScientist及七种外部系统，并控制问题、模型设置、输入和期望输出。 | 全文第4944行；核验TXT行号 4944 | The four cases below compare the human method, IdeaScientist-Base, IdeaScientist-Trained, and seven external systems under the same problem definition, model setting, inputs, and desired output. | 高（一手正文；非独立复现） |
| 研究问题与方法比较 | 推理RL案例将问题设定为在固定计算预算下选择题目接受追加rollout的方式并组织训练数据；这是构思评估用任务设定。 | 全文第5207行；核验TXT行号 5207 | The goal is to improve the student’s reasoning accuracy under a fixed compute budget by deciding which questions receive additional rollouts and how their samples contribute to training. GRPO calculates advantages by comparing rewards within each question’s rollout group. The baseline objective also includes a KL penalty to limit deviation from a reference policy. | 高（一手正文；非独立复现） |
| 多模态AI研究案例 | 多模态推测解码案例明确大模型作为目标、轻量模型作为草稿模型，并以图像、文本和已接受token为输入来构思自适应方法。 | 全文第5656行；核验TXT行号 5656 | A large vision and language model is the target whose answer we want to produce; a cheaper model is the drafter that proposes several tokens at a time. Given the image, the text prompt, and the tokens already accepted, a method chooses how to draft the next block of tokens. The target checks that block in one verificat | 高（一手正文；非独立复现） |
| 跨领域发现评测 | 作者使用时间截断文献评估生成方向与15K后续人类论文的关系。 | 全文第494行；核验TXT行号 494 | Our evaluation restricts access to literature available before a cutoff date and assesses how closely proposed directions align with those later explored in 15K papers authored by human researchers. | 高（一手正文；非独立复现） |
| 对象分类边界 | 子代理能力拒答案例的任务要求是：根据请求、可用工具和权限决定返回任务结果或指明具体原因的拒答。这是论文构思评估中的AI研究问题，并未报告相应生产部署实验。 | 全文第5433行；核验TXT行号 5433 | A coordinator sends a user request qq to a specialized sub-agent. The sub-agent receives the request, its task context, and information about its available tools, data, and permissions. It must return either a valid task result yy, such as a customer segmentation query, or a structured abstention aa. The abstention states the fa | 高（一手正文；非独立复现） |

## 0. 摘要翻译

IdeaScientist将科学研究构思拆分为研究缺口发现、跨问题情境机制迁移和方案撰写，并以强化学习训练专门代理。评测使用时间截断的文献语料和15K篇后续人类论文，比较生成方向与真实后续研究的关联；附录还以可组合安全对齐、推理强化学习rollout分配、子代理拒答及多模态推测解码四项机器学习问题作案例，直接检验具体AI研究方案的构思能力。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。研究构思案例具体包含可组合的安全对齐任务：根据用户请求和激活规则生成符合规则的答案。这是构思评测中的问题定义，不表示作者实际执行了该模型训练。
  - 原文位置：全文第4955行；核验TXT行号 4955；引文：Table 13: Case study on composable safety alignment. Every method receives a user question xx and a set SS of safety rules enabled for that request and must produce an answer that follows those rules. The language model’s existing weights remain frozen.
- 多步行动过程：yes。推理RL构思案例比较各方案如何先为问题生成rollout组，再按优先级分配余下计算预算并构造GRPO训练数据；这是被评价的构思方案内容，而非本文实际执行该训练实验。
  - 原文位置：全文第5267行；核验TXT行号 5267；引文：Mechanism. Generate an initial group per question, repeatedly assign the remaining budget to the highest upper-confidence score, and train GRPO on the resulting variable-size whole-question groups; no teacher model is required.
- 至少一种Agent能力：yes。拒答案例展示一个被评价的子代理能力检查方案：拆解任务所需能力并与实时清单核对，条件不足则输出结构化拒答。这是研究构思评估中呈现的方案，不是本文实际部署验证。
  - 原文位置：全文第5517行；核验TXT行号 5517；引文：Mechanism. Compare the LLM-extracted requirements with a live structured inventory; execute only if all checks pass, otherwise return a typed abstention naming the missing or prohibited capability. The basic version needs no training.
- 明确科研流程角色：yes。系统参与问题定义、研究方案构思和文献时间截断评估；15K人类后续论文是评估对象，不代表模型在这些论文中执行了实验。
  - 原文位置：全文第494行；核验TXT行号 494；引文：Our evaluation restricts access to literature available before a cutoff date and assesses how closely proposed directions align with those later explored in 15K papers authored by human researchers.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：01;11
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：01（仅归档，不覆盖其他模块）
- 模块内分类路径：01.02.12 人工智能；11.07.10 学科演化与跨学科发现机制
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

- 机器学习研究任务：可组合安全对齐、推理强化学习自适应rollout分配、子代理能力边界与拒答、多模态推测解码
- 跨学科研究构思及后续人类论文中的学科间机制迁移

### 2.3 容易混淆的边界

贡献是面向机器学习研究任务的多阶段科研构思Agent，以及以15K后续论文评测跨问题情境的机制迁移。具体实验对象支持01.02.12人工智能；对跨学科发现机制的评测支持11.07.10。该文有具体领域案例，不属于01.04通用桶。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签



### 3.2 科研流程角色



gap finder检索相关工作并识别方法缺口，innovator从不同问题情境提取可迁移机制，report writer整合依据并生成可执行方案；角色通过阶段匹配的参考产物和评分规则进行强化学习训练。附录I进一步在四个具体机器学习研究问题上并列比较人工方法、IdeaScientist及外部系统。

### 3.3 自主能力

拒答案例展示一个被评价的子代理能力检查方案：拆解任务所需能力并与实时清单核对，条件不足则输出结构化拒答。这是研究构思评估中呈现的方案，不是本文实际部署验证。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

贡献是面向机器学习研究任务的多阶段科研构思Agent，以及以15K后续论文评测跨问题情境的机制迁移。具体实验对象支持01.02.12人工智能；对跨学科发现机制的评测支持11.07.10。该文有具体领域案例，不属于01.04通用桶。

### 4.2 系统流程与组件

gap finder检索相关工作并识别方法缺口，innovator从不同问题情境提取可迁移机制，report writer整合依据并生成可执行方案；角色通过阶段匹配的参考产物和评分规则进行强化学习训练。附录I进一步在四个具体机器学习研究问题上并列比较人工方法、IdeaScientist及外部系统。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

主评测按文献截止日期隔离可用材料，以15K后续人类论文评估构思方向；另外报告四个机器学习问题上的案例比较，并在多个模型/Agent基线上比较构思分数。

### 5.2 基线、指标与结果

作者在Qwen3.6-27B上报告IdeaScientist总体分数较最强开源autoresearch基线高14.0%；同一骨干上较Claude Code SDK与Claude-4.8-Opus高5.9%，较Codex SDK与GPT-5.4高5.1%。评测另以15K后续人类论文检查研究方向关联，附录I报告四个AI研究案例。

### 5.3 科学贡献与证据强度

贡献是面向机器学习研究任务的多阶段科研构思Agent，以及以15K后续论文评测跨问题情境的机制迁移。具体实验对象支持01.02.12人工智能；对跨学科发现机制的评测支持11.07.10。该文有具体领域案例，不属于01.04通用桶。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

本文将端到端autoresearch中的构思阶段单独抽出训练，区别于把方案、实现、实验和写作合并评分的系统；附录案例覆盖具体AI研究任务。

## 7. 局限性与风险

后续论文相关性和评审模型分数是构思质量代理指标，不等于方案已被实施或产生真实科学发现；附录案例也不替代实验验证。

## 8. 对综述写作的价值

可支持综述讨论AI科研构思Agent、跨问题情境机制迁移及后续论文对照评测。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

IdeaScientist将科学研究构思拆分为研究缺口发现、跨问题情境机制迁移和方案撰写，并以强化学习训练专门代理。评测使用时间截断的文献语料和15K篇后续人类论文，比较生成方向与真实后续研究的关联；附录还以可组合安全对齐、推理强化学习rollout分配、子代理拒答及多模态推测解码四项机器学习问题作案例，直接检验具体AI研究方案的构思能力。

### 9.2 速记版 pipeline

gap finder检索相关工作并识别方法缺口，innovator从不同问题情境提取可迁移机制，report writer整合依据并生成可执行方案；角色通过阶段匹配的参考产物和评分规则进行强化学习训练。附录I进一步在四个具体机器学习研究问题上并列比较人工方法、IdeaScientist及外部系统。

### 9.3 标注字段汇总

```text
paper_id=ASD-1094
inclusion_status=to_read
scientific_object_modules=01;11
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=01
module_taxonomy_codes=01.02.12;11.07.10
source_level=first_hand_full_text
fulltext_followup_required=true
```

### 全文后续要求

当前纳入和分类证据已足够；第7节明确的结果/复现细节仍需继续回查。
