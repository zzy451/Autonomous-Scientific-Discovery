# MLAgentBench 2024

## 基本信息
- **论文**: MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation
- **作者**: Qian Huang, Jian Vora, Percy Liang, Jure Leskovec
- **年份**: 2024
- **来源**: arXiv:2310.03302
- **关键词**: benchmark, ML experimentation, agent, ReAct, CIFAR-10, BabyLM, ICML 2024

## 核心思想
该文探讨了语言模型驱动的智能体能否有效执行 ML 实验——包括设计与运行实验、分析结果、迭代改进以获得更好性能。作者提出 MLAgentBench，包含 13 个任务，范围从提升 CIFAR-10 模型性能到近期研究问题如 BabyLM。智能体可使用读写文件、执行代码和检查输出等操作。基于 ReAct 框架构建智能体（含 Reflection、Research Plan and Status、Fact Check、Thought 等组件），对 Claude v1.0/v2.1/v3 Opus、GPT-4、GPT-4-turbo、Gemini-Pro 和 Mixtral 共计 7 个模型进行评测。Claude v3 Opus 取得了 37.5% 的平均成功率。性能跨度从经典数据集的 100% 到近期 Kaggle 挑战的 0%。识别出的关键挑战包括长期规划和幻觉减少。发表于 ICML 2024。

## 评测目标
回答基础问题：LLM 智能体能否像人类 ML 研究者一样自主进行实验迭代？具体评测智能体在设计实验方案、编写代码、分析实验结果、根据结果调整策略这一完整闭环中的能力。论文将 MLAgentBench 定位为首个面向该类 ML 实验迭代智能体的基准；现有基准要么只测单步代码生成（HumanEval），要么不涉及实验迭代和结果分析。MLAgentBench 为后续 MLE-Bench、ScienceAgentBench 等方法提供了早期参照。

## 基准设计
- **题目数量/来源/难度分级**：13 个任务，分为 5 类：(1) Canonical Tasks（3 题：CIFAR-10 图像分类、imdb 情感分类、ogbn-arxiv 论文分类）；(2) Classic Kaggle（2 题：house-price 回归、spaceship-titanic 分类）；(3) Kaggle Challenges（4 题：parkinsons-disease、fathomnet、feedback、identify-contrails，均为 2022/08-2023/05 启动，用于检测数据污染）；(4) Recent Research（2 题：CLRS 算法推理、BabyLM 语言模型）；(5) Code Improvement（2 题：llama-inference 加速、vectorization 加速）。覆盖文本、图像、时序、图、表格数据等多种模态。
- **评分方式**：成功率（Success Rate）为核心指标——在起始代码基线基础上性能指标提升 ≥10% 视为成功。每个任务运行 8 次独立实验。同时报告平均性能提升百分比、消耗时间、消耗 tokens 数。智能体最多 50 个动作/5 小时（GPT-4 限制 30 个动作因成本）。
- **人类基线 vs AI 基线**：无受控人类基线。最佳模型 Claude v3 Opus 平均成功率 37.5%（house-price/spaceship-titanic 100%，BabyLM/llama-inference/vectorization 0%）。GPT-4 平均 19.2% 但平均改善幅度更高（41.3% vs Claude v3 Opus 的 26.1%）。GPT-4-turbo 26.0%，Claude v2.1 26.0%，Gemini Pro 18.3%，Claude v1.0 16.3%，Mixtral 3.8%。基线方案（起始代码无改进）10.4%（仅因 identify-contrails 和 CLRS 起始方案就有 40%/42.9% 成功率）。对比框架：LangChain ReAct + Claude v3 Opus 33.7%，AutoGPT + Claude v3 Opus 13.5%。
- **设计原则**：(i) 任务 recency 梯度——从经典任务到 2023 年新发布的任务，用于检测数据污染（训练截止日期后的任务可能反映真实泛化能力）；(ii) 结构化的思维链——Reflection + Research Plan + Fact Check + Thought 的响应格式，强制智能体展示推理过程；(iii) 复合动作设计——Understand File、Edit Script、Edit Script Segment 等高层动作封装多步基础操作；(iv) 注重可解释性——保留完整交互轨迹供分析。

## 关键数字
| 指标 | 值 |
|------|-----|
| 任务数 | 13（5 类）|
| 最佳模型（成功率）| Claude v3 Opus: 37.5% |
| 最佳模型（平均改善）| GPT-4: 41.3% |
| 经典任务最高成功率 | 100%（house-price, spaceship-titanic）|
| 近期 Kaggle 任务最低成功率 | 0%（parkinsons-disease, fathomnet）|
| BabyLM 成功率 | 0%（所有模型）|
| 对比模型数 | 7 |
| 对比智能体框架数 | 3（Ours, AutoGPT, LangChain ReAct）|
| 最大动作数/时间 | 50 动/5h（GPT-4: 30 动）|
| 典型失败模式 | 长期规划不足、幻觉式声称进展、调试中卡住 |
| GPT-4-turbo 运行总成本 | ~$60（6M tokens）|
| 人类基线 | 无（主要局限）|

## 设计哲学
- **Recency 作为污染检测代理**：最独特的设计选择——通过引入训练截止日期后的任务（2022/08-2023/05），自然形成"已知 vs 未知"的对比。结果清晰：经典任务 100%，近期 Kaggle 0%，暗示 LLM 在"熟悉领域"的高表现可能源于记忆而非泛化。这一设计方法被后续 MLE-Bench 和 ScienceAgentBench 引用。
- **过程可解释性 > 最终结果**：要求的四段式响应格式（Reflection-Plan-FactCheck-Thought）将智能体的推理过程显式化，这些痕迹成为重要的分析素材。Claude v3 Opus 相比 GPT-4 的 Fact Check 更好地抑制了幻觉。
- **高层动作的权衡**：复合动作（Understand File、Edit Script）封装了一层 LLM 调用，减少了主智能体的认知负担和上下文消耗。这种设计揭示了"微调用 vs 主智能体推理"的架构权衡。
- **轻量级设计的刻意选择**：13 个任务、代码执行仅需分钟级，使全基准可在 $60 内运行。这种轻量设计降低进入门槛但牺牲了统计稳健性。

## 局限性
- 任务数量少（13），统计意义有限，单个任务 8 次运行不足以得出稳健结论。
- 成功率作为二值指标（10% 改善阈值），无法反映部分进展。平均改善百分比在表 4 中因个别极端值（identify-contrails 143.3%）而扭曲。
- 实验环境相对封闭——智能体无法获取外部知识、文献或网页信息，不反映真实研究者的信息获取能力。
- 无人类受控基线对比，无法回答"AI 离人类水平有多远"的问题。
- ReAct 框架已略显过时，后续基准（MLE-Bench AIDE、ScienceAgentBench self-debug）采用了更丰富的工具和策略。
- Claude v3 Opus 虽然成功率高但开销也高（平均 tokens 和耗时最多），效率-性能的权衡未被深入分析。
- 10% 改善阈值在某些任务上可能偏低（CIFAR-10 起始方案差），在其他任务上偏高。

## 核心贡献
MLAgentBench 2024 的核心贡献是较早将语言模型 agent 放入真实 ML 实验迭代闭环中评测，用 13 个任务检验 agent 读写代码、运行实验、分析结果、调整方案和保持长期计划的能力，并通过任务新旧差异暴露泛化与数据污染风险。

## 与综述的关联
MLAgentBench 是该领域较早（2023 年 10 月发布、ICML 2024 接收）的系统性 ML 智能体基准之一，在本综述 benchmark 章节中具有奠基性地位。它的 13 个任务从简单到前沿的设计、ReAct + Reflexion 的智能体架构、以及数据污染分析（通过引入训练截止日期后的任务发现 LLM 记忆效应的清晰证据），为后续基准（MLE-Bench、ScienceAgentBench、RE-Bench）提供了方法论参考。特别有价值的是其 Fact Check 机制——直接回应了科学发现中最致命的问题（幻觉），该思想被后续工作以不同形式继承。
