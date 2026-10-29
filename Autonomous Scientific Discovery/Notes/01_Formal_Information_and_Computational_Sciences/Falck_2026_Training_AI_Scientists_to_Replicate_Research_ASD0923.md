# Training AI Scientists to Replicate Research

**论文信息**

- ID：ASD-0923
- 标题：Training AI Scientists to Replicate Research
- 作者：Damon Falck; Samer Sabri; Anja Surina; Thom Foster; Anya Sims; Sam Devlin; Dylan Rogers; Tantum Collins; Kaloyan Aleksiev; Louis Kirsch; Edward Hughes
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2608.13331
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0923.txt
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Falck_2026_Training_AI_Scientists_to_Replicate_Research_ASD0923.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 研究目标/科学问题 | 本文提出 Replica 任务集，并训练 27B 参数的工具型 AI Scientist Faraday 执行论文结果图复现。训练任务取自机器学习论文，测试任务取自 AI for Science 论文；Agent 在图表被遮蔽、受限算力和时限的环境中，通过编码工具开展长程实验复现。作者使用 rubric 奖励训练并比较复现质量，同时讨论复现失败的解释边界。 | 本地全文：ASD-0923中与研究目标/科学问题直接相关的原文句子；核验TXT行号 398 | The replicability of papers is a cornerstone of scientific knowledge, ensuring the reliability of existing results and providing a base for further experiments. The act of replication typically illuminates details that were previously underspecified, and thus requires similar hypothesis-driven exploration to open-ended research. In this work, we develop Replica, a scalable task space for paper replication. To provide reward signal, we introduce an auto-generated rubric-based judge that has low noise and agrees with human assessment of replication quality. We post-train Faraday, a 27B-parameter “AI Scientist” agent that leverages coding agents as tools, surpassing the performance of Claude Opus 4.8 and GPT-5.5 on held-out replication tasks. Qualitative analysis of individual rollouts reveals that Faraday adopts a more scientifically-principled approach. We believe that our results provide a stepping stone towards AI agents capable of long-horizon scientific innovation without requiring complex harnesses. | 高（一手正文；非独立复现） |
| 多步行动/研究流程 | Replica 将论文结果图转换为复现任务；Faraday 阅读未遮蔽内容、规划并调用编码工具，在给定容器和算力预算内运行实验，再按 rubric 评分并用于后训练。 | 本地全文：ASD-0923中与多步行动/研究流程直接相关的原文句子；核验TXT行号 665 | The Replica task space comprises 242242 training tasks and 6868 test tasks drawn from 100100 well-known ML and AI-for-science papers. Each task requires an agent to replicate one results figure from a paper, given the original paper with the figure redacted, a 6060-minute time limit, and a single one-seventh MIG slice of an H200 GPU. The agent is provided with a containerd container to work in with helpful research libraries pre-installed, access to the internet, a system prompt, and a task prompt (Appendix G). Where a paper’s experiment cannot be completed within the given time budget, the prompt asks for the most faithful scaled-down version of the underlying experiment. The training tasks are drawn from ML papers from 1990 to 2026. The test tasks are drawn from AI-for-science papers from 2012 to 2026. We choose well-known papers for ease of human rating (Section 3.3). | 高（一手正文；非独立复现） |
| Agent实现与能力 | Faraday 是经后训练的 27B 工具型 AI Scientist；系统使用 apply_patch、read_file、list_dir、grep_files 和 shell 执行编码、文件检索及实验命令。 | 本地全文：ASD-0923中与Agent实现与能力直接相关的原文句子；核验TXT行号 796 | The agent acts via five function-calling tools: apply_patch, read_file, list_dir, grep_files, and shell. Faraday can detach background processes using the shell tool, allowing it to take many turns while running several commands in parallel. The tool interface is a subset of the Codex CLI schema (OpenAI, 2025), reimplemented in Python. The conversation is a linear, append-only history with no compaction. A turn’s tool calls execute concurrently and their results are appended in call order. Context overflow, exceeding the per-turn 1616K token limits, and inference errors end the rollout, and the partial rollout is judged like any other. A rollout otherwise ends when Faraday replies without tool calls or when its wall-clock time is exhausted. | 高（一手正文；非独立复现） |
| 实验任务与验证设置 | 训练任务来自 1990–2026 年机器学习论文，测试任务来自 2012–2026 年 AI for Science 论文。作者报告与 Claude、Codex 比较，并用人工评审校验 rubric judge。 | 本地全文：ASD-0923中与实验任务与验证设置直接相关的原文句子；核验TXT行号 665 | The training tasks are drawn from ML papers from 1990 to 2026. | 高（一手正文；非独立复现） |
| 作者报告的结果/贡献 | 作者报告 Faraday 在复现任务上优于 Claude 和 Codex；应按论文给出的评测集与 rubric 理解该结果。讨论部分说明仍存在复现失败，不能据此认定原论文结果有误。 科学贡献在于把已发表科学结果的复现作为研究任务来评测；系统贡献在于 Replica 任务生成、rubric 奖励及 Faraday 的工具型长程执行。 | 本地全文中包含该原句的位置；核验TXT行号 474 | Faraday outperforms Claude Opus 4.8 (hereafter, Claude) and GPT-5.5 (hereafter, Codex) on 73%73\% of in-distribution ML tasks, and on 60%60\% of held-out AI-for-science tasks, according to our rubric-based judge. On average, Faraday achieves a 6%6\% improvement over Claude and an 8%8\% improvement over Codex on the test split. Optimising Codex’s prompt only marginally diminishes the gap. Human experts rate Faraday as stronger than Claude and Codex on rollouts for which the rubric judge assesses that Faraday has an advantage. Compared to rollouts from frontier models, Faraday behaves more like a human scientist: it implements the mechanism behind the claim rather than hard-coding outputs, it scales down in a way that remains faithful to the paper’s experimental scope, and it avoids shortcuts that would flatter its own result. In summary, the main contributions of our paper are as follows: | 高（一手正文；非独立复现） |

## 0. 摘要翻译

本文提出 Replica 任务集，并训练 27B 参数的工具型 AI Scientist Faraday 执行论文结果图复现。训练任务取自机器学习论文，测试任务取自 AI for Science 论文；Agent 在图表被遮蔽、受限算力和时限的环境中，通过编码工具开展长程实验复现。作者使用 rubric 奖励训练并比较复现质量，同时讨论复现失败的解释边界。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。本文提出 Replica 任务集，并训练 27B 参数的工具型 AI Scientist Faraday 执行论文结果图复现。训练任务取自机器学习论文，测试任务取自 AI for Science 论文；Agent 在图表被遮蔽、受限算力和时限的环境中，通过编码工具开展长程实验复现。作者使用 rubric 奖励训练并比较复现质量，同时讨论复现失败的解释边界。
  - 原文位置：本地全文：ASD-0923中与研究目标/科学问题直接相关的原文句子；核验TXT行号 398；引文：The replicability of papers is a cornerstone of scientific knowledge, ensuring the reliability of existing results and providing a base for further experiments. The act of replication typically illuminates details that were previously underspecified, and thus requires similar hypothesis-driven exploration to open-ended research. In this work, we develop Replica, a scalable task space for paper replication. To provide reward signal, we introduce an auto-generated rubric-based judge that has low noise and agrees with human assessment of replication quality. We post-train Faraday, a 27B-parameter “AI Scientist” agent that leverages coding agents as tools, surpassing the performance of Claude Opus 4.8 and GPT-5.5 on held-out replication tasks. Qualitative analysis of individual rollouts reveals that Faraday adopts a more scientifically-principled approach. We believe that our results provide a stepping stone towards AI agents capable of long-horizon scientific innovation without requiring complex harnesses.
- 多步行动过程：yes。Replica 将论文结果图转换为复现任务；Faraday 阅读未遮蔽内容、规划并调用编码工具，在给定容器和算力预算内运行实验，再按 rubric 评分并用于后训练。
  - 原文位置：本地全文：ASD-0923中与多步行动/研究流程直接相关的原文句子；核验TXT行号 665；引文：The Replica task space comprises 242242 training tasks and 6868 test tasks drawn from 100100 well-known ML and AI-for-science papers. Each task requires an agent to replicate one results figure from a paper, given the original paper with the figure redacted, a 6060-minute time limit, and a single one-seventh MIG slice of an H200 GPU. The agent is provided with a containerd container to work in with helpful research libraries pre-installed, access to the internet, a system prompt, and a task prompt (Appendix G). Where a paper’s experiment cannot be completed within the given time budget, the prompt asks for the most faithful scaled-down version of the underlying experiment. The training tasks are drawn from ML papers from 1990 to 2026. The test tasks are drawn from AI-for-science papers from 2012 to 2026. We choose well-known papers for ease of human rating (Section 3.3).
- 至少一种Agent能力：yes。Faraday 是经后训练的 27B 工具型 AI Scientist；系统使用 apply_patch、read_file、list_dir、grep_files 和 shell 执行编码、文件检索及实验命令。
  - 原文位置：本地全文：ASD-0923中与Agent实现与能力直接相关的原文句子；核验TXT行号 796；引文：The agent acts via five function-calling tools: apply_patch, read_file, list_dir, grep_files, and shell. Faraday can detach background processes using the shell tool, allowing it to take many turns while running several commands in parallel. The tool interface is a subset of the Codex CLI schema (OpenAI, 2025), reimplemented in Python. The conversation is a linear, append-only history with no compaction. A turn’s tool calls execute concurrently and their results are appended in call order. Context overflow, exceeding the per-turn 1616K token limits, and inference errors end the rollout, and the partial rollout is judged like any other. A rollout otherwise ends when Faraday replies without tool calls or when its wall-clock time is exhausted.
- 明确科研流程角色：yes。训练任务来自 1990–2026 年机器学习论文，测试任务来自 2012–2026 年 AI for Science 论文。作者报告与 Claude、Codex 比较，并用人工评审校验 rubric judge。
  - 原文位置：本地全文：ASD-0923中与实验任务与验证设置直接相关的原文句子；核验TXT行号 665；引文：The training tasks are drawn from ML papers from 1990 to 2026.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：01;11
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：01（仅归档，不覆盖其他模块）
- 模块内分类路径：01.02 计算机科学；11.07 科学系统与知识生产研究
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

对象模块与代码沿用输入审计记录（01, 11；01.02, 11.07）；是否纳入与对象分类分开判断。

### 2.3 容易混淆的边界

对象模块与代码沿用输入审计记录（01, 11；01.02, 11.07）；是否纳入与对象分类分开判断。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

自主科研Agent

### 3.2 科研流程角色

科研问题处理；多步行动或评测

Faraday 是经后训练的 27B 工具型 AI Scientist；系统使用 apply_patch、read_file、list_dir、grep_files 和 shell 执行编码、文件检索及实验命令。

### 3.3 自主能力

Faraday 是经后训练的 27B 工具型 AI Scientist；系统使用 apply_patch、read_file、list_dir、grep_files 和 shell 执行编码、文件检索及实验命令。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

科学贡献在于把已发表科学结果的复现作为研究任务来评测；系统贡献在于 Replica 任务生成、rubric 奖励及 Faraday 的工具型长程执行。

### 4.2 系统流程与组件

Replica 将论文结果图转换为复现任务；Faraday 阅读未遮蔽内容、规划并调用编码工具，在给定容器和算力预算内运行实验，再按 rubric 评分并用于后训练。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

训练任务来自 1990–2026 年机器学习论文，测试任务来自 2012–2026 年 AI for Science 论文。作者报告与 Claude、Codex 比较，并用人工评审校验 rubric judge。

### 5.2 基线、指标与结果

作者报告 Faraday 在复现任务上优于 Claude 和 Codex；应按论文给出的评测集与 rubric 理解该结果。讨论部分说明仍存在复现失败，不能据此认定原论文结果有误。

### 5.3 科学贡献与证据强度

科学贡献在于把已发表科学结果的复现作为研究任务来评测；系统贡献在于 Replica 任务生成、rubric 奖励及 Faraday 的工具型长程执行。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

论文以“Training AI Scientists to Replicate Research”对应的研究任务为对象，具体与哪些既有系统或基准比较，应结合其正文相关工作和实验基线判断；不把工具名称直接视为科学对象。

## 7. 局限性与风险

论文明确讨论复现任务失败及可验证奖励覆盖面的限制；单图复现成绩不能直接代表开放式创新或普遍科研能力。

## 8. 对综述写作的价值

可用于综述“Training AI Scientists to Replicate Research”所涉及的Agent任务、研究流程和验证方式；其证据边界为本论文实际报告的任务集与实验结果。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

Replica 提供论文图表复现任务，Faraday 展示工具型 AI Scientist 的长程复现实验能力。

### 9.2 速记版 pipeline

Replica 将论文结果图转换为复现任务；Faraday 阅读未遮蔽内容、规划并调用编码工具，在给定容器和算力预算内运行实验，再按 rubric 评分并用于后训练。

### 9.3 标注字段汇总

```text
paper_id=ASD-0923
inclusion_status=to_read
scientific_object_modules=01;11
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=01
module_taxonomy_codes=01.02;11.07
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`01.02.13` 机器学习；二级：`01.02`。
- 原文位置：PDF p.1。
- 判定：对机器学习论文复现实验执行进行训练与评估，属于机器学习研究。
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
