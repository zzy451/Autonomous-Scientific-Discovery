# DrugMCTS 2025

## 基本信息

- **论文**: DrugMCTS: a drug repurposing framework combining multi-agent, RAG and Monte Carlo Tree Search
- **年份**: 2025
- **来源**: arXiv:2507.07426
- **系统名称**: DrugMCTS
- **关键词**: drug repurposing, multi-agent, RAG, Monte Carlo Tree Search, molecular and protein information

## 摘要要点

DrugMCTS 将 RAG、多智能体协作和 Monte Carlo Tree Search 结合，用于 drug repurposing / repositioning。系统包含五个 specialized agents，负责检索和分析 molecular / protein information，并通过结构化、迭代式推理选择药物重定位候选。论文报告无需领域微调即可让 Qwen2.5-7B-Instruct 在 DrugBank 和 KIBA 数据集上超过更强通用模型。

## 方法动机

药物重定位需要结合药物、靶点、蛋白、相互作用和文献证据。普通 LLM 受限于预训练知识，RAG 又可能只是被动补充上下文，难以进行系统性候选路径搜索。DrugMCTS 的动机是把检索、专业 agent 分工和 MCTS 搜索结合起来，增强结构化科学推理。

## 方法设计

流程包括：

1. 输入 drug repurposing 查询。
2. RAG 模块检索药物、蛋白和相关科学数据。
3. 五个 specialized agents 分别处理不同信息源或分析任务。
4. MCTS 在候选推理路径上进行选择、扩展、评估和回传。
5. 系统根据搜索反馈逐步收敛到更有希望的药物-靶点候选。
6. 输出候选及其证据链和推理依据。

这里的核心 Y 机制是 MCTS，而不是普通候选排序。

## 实验与结果

论文在 DrugBank 和 KIBA 上评估 DrugMCTS，报告 Qwen2.5-7B-Instruct 在该框架下超过 Deepseek-R1 20% 以上，并在 recall 和 robustness 上优于通用 LLM 与深度学习 baselines。作者强调 structured reasoning、agent collaboration 和 feedback-driven search 对药物发现任务很重要。

## 局限性

- 主要是 in silico drug repurposing，不包含湿实验验证。
- 检索质量和数据库覆盖会影响候选可靠性。
- MCTS 的 reward / scoring 设计决定搜索质量。

## XYZ 分类

| 维度 | 标注 | 理由 |
|---|---|---|
| X | `X2` | 五个 specialized agents 形成固定角色协作 |
| Y | `Y3` | Monte Carlo Tree Search 是核心候选推理机制 |
| Z | `Z1,Z2,Z5,Z7,Z8` | 覆盖知识检索、候选推理、结果分析、验证和迭代 |

## 对综述的价值

DrugMCTS 可作为第 5 章 tree/MCTS search 在生物医药场景中的证据，说明 multi-agent ASD 的搜索对象不只是假设或代码，也可以是药物重定位推理路径。

