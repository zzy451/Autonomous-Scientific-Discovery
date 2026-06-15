# PaperBench 2025

## 基本信息
- **论文**: PaperBench: Evaluating AI's Ability to Replicate AI Research
- **作者**: Giulio Starace, Oliver Jaffe, Dane Sherburn, James Aung, Chan Jun Shern, Leon Maksin, Rachel Dias, Evan Mays, Benjamin Kinsella, Wyatt Thompson, Johannes Heidecke, Amelia Glaese, Tejal Patwardhan (OpenAI)
- **年份**: 2025
- **来源**: arXiv:2504.01848v3
- **关键词**: benchmark, AI research replication, ML engineering, rubric-based evaluation, long-horizon task, LLM judge

## 核心思想
我们提出 PaperBench，一个评估 AI 智能体复制最前沿 AI 研究能力的基准测试。智能体需从零开始复现 20 篇 ICML 2024 Spotlight 和 Oral 论文，包括理解论文贡献、构建代码库、并成功执行实验。为了进行客观评估，我们开发了评分细则（rubrics），将每个复现任务层级化分解为具有明确评分标准的小子任务。PaperBench 总计包含 8,316 个可单独评分的任务。评分细则与每篇 ICML 论文的原作者共同开发以确保准确性与真实性。为实现可规模化的评估，我们还开发了基于 LLM 的评判器来自动依据评分细则对复现尝试进行评分，并通过为评判器创建独立基准来评估其性能。我们在 PaperBench 上评估了多个前沿模型，发现表现最佳的测试智能体——配备开源脚手架（scaffolding）的 Claude 3.5 Sonnet (New)——平均复现得分为 21.0%。最后，我们招募顶尖 ML 博士生尝试 PaperBench 的部分子集，发现模型尚未超越人类基线。我们开源代码以促进未来研究。

## 评测目标
a) 这个基准测什么能力？为什么需要这个基准？
- PaperBench 评测 AI 智能体端到端复制顶会 ML 论文的全部实验贡献的能力，具体涵盖：阅读理解论文方法论、从零构建完整代码库、集成与执行多个交互实验、调试代码和超参数、复现定量实验结果。
- 动机：能自主复制 ML 研究的 AI 系统可能加速机器学习进展，但这同时带来显著的安全与治理风险。PaperBench 被设计为可直接用于 OpenAI Preparedness Framework、Anthropic Responsible Scaling Policy、Google DeepMind Frontier Safety Framework 中的自主能力评估。
- 与 CORE-Bench 的关键区别：CORE-Bench 要求智能体利用已有代码仓库复现论文结果，PaperBench 要求从零开始（不允许使用原作者代码），评估的是完全自主的代码开发与实验执行能力。

b) 现有基准的不足是什么？
- CORE-Bench：评测代码复现（利用已有仓库），但未要求从零编码。
- MLE-bench/MLAgentBench/DSBench：评测 Kaggle 比赛能力，但很多比赛任务已过时，且复杂度远低于复现顶会论文。
- RE-Bench：提出 7 个开放式 ML 研究工程任务，但任务相对自包含，时间跨度和复杂度均远低于 PaperBench。
- 多数现有基准提供"评分函数"作为训练信号，而 PaperBench 的场景中不存在这样的完美信号。

## 基准设计
a) 题目数量、来源、难度分级
- 20 篇 ICML 2024 Spotlight 和 Oral 论文，覆盖 12 个 ICML 主题（深度强化学习、鲁棒性、概率方法、LLM 等）。
- 经严格筛选：排除纯理论论文、需多节点分布式训练的论文、依赖闭源模型的论文、需人类数据收集的论文等。
- 附有两个 NeurIPS 2024 Workshop 论文作为开发集，另有内部保留测试集。
- 评分细则总计 8,316 个叶子节点（可单独评分的最小单元），每个评分细则树的节点数从 94 到 2,551 不等。
- 三种叶子节点类型：Code Development（代码开发，占总节点多数）、Execution（代码执行）、Result Match（结果匹配）。

b) 评分方式（自动/人工/混合）
- 自动 LLM 评判（SimpleJudge）：使用 o3-mini-high 作为评判后端，F1 评分 0.83（vs 人工 gold label）。成本约 $66/篇。
- 评分流程：每个叶子节点进行二元评分（通过/不通过），父节点得分为子节点的加权平均，最终复现得分（Replication Score）为根节点得分（0%-100%）。
- 复现步骤（Reproduction）：智能体的代码被拷贝到全新的 Ubuntu 24.04 VM（配备 A10 GPU），执行 reproduce.sh 最多 12 小时。
- 辅助基准 JudgeEval：包含部分复现提交的人工评分标签，用于校准和评估 LLM 评判器。

c) 人类基线 vs AI 基线（具体数字）
- 人类基线（ML PhD 在读或已毕业，best@3，48 小时）：3 篇论文子集上 41.4%，人类 Code Dev 72.4%、Execution 20.4%、Result Match 8.9%。
- Claude 3.5 Sonnet (New) + BasicAgent：21.0%（主设置最强）
- o1 + BasicAgent：13.2%
- o1 + IterativeAgent（12h）：24.4%
- o1 + IterativeAgent（36h 扩展）：26.0%
- o1 + IterativeAgent 在 3 篇论文子集（同人类）：26.6%（48h 人类 best@3 为 41.4%）
- DeepSeek-R1 + BasicAgent：6.0%
- GPT-4o + BasicAgent：4.1%
- Gemini 2.0 Flash + BasicAgent：3.2%
- o3-mini + BasicAgent：2.6%
- PaperBench Code-Dev（仅代码开发评分）：o1 + IterativeAgent 达 43.4%

d) 题目设计原则和独特之处
- 作者合作开发评分细则：每篇论文的评分细则均与原论文作者共同反复修改、签字确认，以确保评分标准准确且代表论文的核心贡献。
- 层级化分解：从最高层"论文核心贡献被复现"逐级分解到 "gpt2-xl 的某一具体超参数配置" 级别，每层有明确权重。
- 三类型叶子节点：Code Dev 给"写了正确代码"以部分分，Execution 给"代码成功运行"以部分分，Result Match 给"产出结果与论文匹配"以满分。这种渐进式评分使部分复现也有区分度。
- 反作弊：作者代码仓库和已知在线复现均被列入黑名单，使用后将提交分数设为 0。

## 关键数字
| 指标 | 人类 | 最佳AI | 年份 | 备注 |
|------|------|--------|------|------|
| 主设置平均复现得分 | — | 21.0% (Claude 3.5 Sonnet) | 2025 | BasicAgent, 20篇论文 |
| o1 IterativeAgent (12h) | — | 24.4% | 2025 | 强制全程工作 |
| o1 IterativeAgent (36h) | — | 26.0% | 2025 | 扩展时间限制 |
| 3篇论文子集 (best@3, 48h) | 41.4% | 26.6% (o1) | 2025 | 人类为ML PhD |
| Code-Dev 变体 | — | 43.4% (o1) | 2025 | 仅评代码质量 |
| JudgeEval F1 评分 | 1.0 (gold) | 0.83 (o3-mini) | 2025 | 评判器校准基准 |
| 总叶子节点数 | — | 8,316 | 2025 | 20篇论文合计 |
| 单次rollout成本 | — | ~$400 | 2025 | o1 API费用/篇 |

## 设计哲学
a) 这个基准的独特设计选择反映了什么价值观？
- "从零开始"的硬核承诺：不允许使用原作者代码库，评测的是 AI 系统完全自主的从论文阅读到代码实现的端到端能力，而非代码复现/适配。
- 评分细则（Rubric）作为核心方法论：将"复制一篇论文"这个极度开放、模糊的任务分解为数千个二元可判定的子任务，既保留任务复杂性又保证评分的客观性。
- 多级渐进评分：用 Code Development → Execution → Result Match 三个层次追踪一个复现从"写了代码"到"跑通代码"再到"结果匹配"的完整进展，避免单一评判导致信息丢失。
- 安全治理工具定位：明确将 PaperBench 定位为前沿 AI 安全框架（OpenAI/Anthropic/DeepMind）中的自主能力度量工具，而非纯学术 benchmark。

b) 和其他基准（如 MLE-Bench, RE-Bench, AutoSurvey）有什么本质不同？
- vs MLE-Bench/RE-Bench：任务复杂度与时间跨度远超。单篇 PaperBench 论文的复现工作量（人类专家至少数天）远大于单个 Kaggle 比赛或 RE-Bench 任务。
- vs CORE-Bench：核心区别是 CORE-Bench 评测代码复现（给定代码仓库），PaperBench 评测从零复制（无代码仓库）。CORE-Bench 验证可信度，PaperBench 评测自主开发能力。
- vs GAIA：GAIA 评测通用助手的日常信息处理，PaperBench 评测专业 AI 研究者的科研能力。维度正交。
- vs AutoSurvey：PaperBench 不局限于文献综述，而是覆盖 ML 研究全流程（代码+实验+结果分析）。

## 局限性
a) 什么重要的能力没有被测到？
- 研究创意/新颖性：只评测复制（replicate），不评测提出新假设或原创实验设计。
- 论文撰写：不评测将实验结果整理成学术论文的能力。
- 长时程策略规划：当前智能体在 12 小时后出现明显平台（plateau），反映无法有效利用更多时间进行全局策略规划。
- 仅评测代码复现路径：未评估智能体是否能理解和批判论文方法论中的潜在缺陷。
- 不包含需要多机分布式训练的论文，硬件需求被有意限制在单 GPU。

b) 基准本身的缺陷
- 规模有限（20 篇论文）：构建评分细则极其耗时（每篇需作者配合数周），难以快速扩展。
- LLM 评判器不确定性：o3-mini 评判器非确定性，且 F1=0.83 意味着约 17% 的评分误差。
- 数据污染风险：原作者代码库已公开存在于网络上，未来模型可能被预训练数据污染。
- 成本高：论文估计 o1 IterativeAgent 12 小时单篇 rollout 约 $400 API 费用，20 篇论文单次完整评估约 $8,000，加上 GPU 执行环境；若做多次重复，费用会进一步增加。
- PaperBench Code-Dev 与完整版的相关性仅 r=0.48，作为轻量代理可能误导。
- 评分细则依赖单个作者判断：不同作者对同一论文的"复制标准"可能不同，存在主体间偏差。

## 核心贡献
a) 一句话核心定位（不超过20字）
评测 AI 从零自主复现顶会 ML 论文的全栈能力。

## 与综述的关联
- 适用章节："Benchmarks for AI Research Automation"（AI 研究自动化基准章节）
- 可支持论点：PaperBench 是评测 AI 科学发现能力时较严格、较全面的基准之一——它要求端到端的研究复制（读论文 → 写代码 → 跑实验 → 匹配结果），而非单一技能切片。其 2025 年的结果（最强 AI 仅 21.0%）表明当前 AI 系统在该受控复现设置中仍落后于人类博士基线。该基准的评分细则（rubric）方法论也为本综述中"如何评测开放式科研任务"这一核心问题提供了重要参考方案。
- 可对比视角：与 MLE-Bench（评测 ML 工程）、RE-Bench（评测科研子任务）、GAIA（评测通用助手）共同构成 AI 科研能力的递进式评测矩阵：通用信息查找 → 专项工程 → 完整科研复现。
