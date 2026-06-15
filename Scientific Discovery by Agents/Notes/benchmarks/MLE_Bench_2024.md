# MLE Bench 2024

## 基本信息
- **论文**: MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering
- **作者**: Jun Shern Chan, Neil Chowdhury, Oliver Jaffe, James Aung, Dane Sherburn, Evan Mays, Giulio Starace, Kevin Liu, Leon Maksin, Tejal Patwardhan, Lilian Weng, Aleksander Mądry
- **年份**: 2024
- **来源**: arXiv:2410.07095
- **关键词**: benchmark, ML engineering, Kaggle, agent scaffolding, ICLR 2025

## 核心思想
该文提出 MLE-bench，用于评估 AI 智能体在机器学习工程任务上的端到端表现。作者从 Kaggle 精选了 75 个 ML 工程相关竞赛，覆盖模型训练、数据集准备和实验执行等任务。使用开源智能体框架搭配多个前沿大语言模型评测，发现最佳配置——OpenAI o1-preview + AIDE 框架——在 16.9% 的竞赛中达到了至少 Kaggle 铜牌水平。工作还研究了智能体的资源扩展效应及预训练数据污染问题。代码已开源，发表于 ICLR 2025。

## 评测目标
评估 AI 智能体在真实世界 ML 工程任务上的端到端能力——从数据准备、特征工程、模型训练到超参数调优的完整流程。现有基准要么太简单（如 HumanEval 单步代码生成，已接近饱和），要么太人工（合成任务不反映真实挑战）。MLE-bench 填补了这一空白，直接对标 Kaggle 人类竞赛排名，为 AI 自动化 ML 工程师的进度提供了可量化标尺。多个 AI 开发者（OpenAI Preparedness Framework、Anthropic RSP、Google DeepMind Frontier Safety Framework）将此类能力评估列为安全治理关键。

## 基准设计
- **题目数量/来源/难度分级**：75 道来自 Kaggle 的竞赛题目，从 5673 个已完成竞赛中经历多轮人工筛选得到（排除社区竞赛、不可复现评分的竞赛、滥用数据集等）。人工标注复杂度：Low（30%，22 题，资深 ML 工程师 <2h 可产出合理方案）、Medium（50%，38 题，2-10h）、High（20%，15 题，>10h）。覆盖 15 个问题类别：表格数据、图像分类/NLP/信号处理/目标检测/时序预测等。另含 7 题开发集。
- **评分方式**：使用 Kaggle 奖牌体系与原始竞赛 Private Leaderboard 对比：100 队以下按 top 40%/20%/10% 给铜/银/金，100-249 队金牌取 top 10，250 队以上铜牌/银牌改用固定名额或比例规则，金牌为 top 10 + 0.2%（每增加 500 队阈值加 1）。核心指标为"获得任何奖牌的比例"。同时报告原始分数、Above Median 比例。允许智能体 24 小时内多次提交，主实验用 3 个随机种子重复。
- **人类基线 vs AI 基线**：人类基线为 Kaggle 排行榜真实数据。仅 9 人曾在 75 个不同竞赛中获牌。AI 最佳：o1-preview + AIDE 获 16.9% 奖牌率（含 9.4% 金牌），GPT-4o + AIDE 为 8.7%，Claude 3.5 Sonnet 为 7.6%，Llama 3.1 405B 仅 3.0%。GPT-4o + MLAB 仅 0.8%，OpenHands 为 4.4%。pass@8 下 o1-preview 奖牌率翻倍至 34.1%。
- **设计原则**：(i) 任务来自真实 Kaggle 竞赛，具有实际价值（总奖金池 ~$1.95M）；(ii) 可直接与人类排行榜成绩对比；(iii) 框架无关——只需提交 CSV 文件；(iv) 规则检测与抄袭检测机制（Dolos 代码相似度 >60% 标记）。

## 关键数字
| 指标 | 值 |
|------|-----|
| 竞赛题目数 | 75（+7 开发集）|
| 问题类别数 | 15 |
| 复杂度分布 | Low 30% / Medium 50% / High 20% |
| 最佳模型 | o1-preview + AIDE |
| 铜牌以上奖牌率（o1-preview）| 16.9% |
| 金牌率（o1-preview）| 9.4%（平均 7 枚金牌）|
| GPT-4o + AIDE 奖牌率 | 8.7% |
| o1-preview pass@8 奖牌率 | 34.1% |
| GPT-4o 100h 奖牌率 | 11.8%（24h 为 8.7%）|
| 人类 Grandmaster 要求 | 5 枚金牌（o1-preview 平均约 7 枚）|
| 每个种子硬件 | 36 vCPU, 440GB RAM, 1×A10 GPU |
| 每个种子 API 消耗 | o1-preview: 127.5M 输入 + 15.0M 输出 tokens |
| 总 GPU 小时（75 竞赛×24h）| 1800 GPU-hours |

## 设计哲学
- **与人类可比的真实排名**：选择 Kaggle 奖牌而非人工主观评分，直接对标人类竞赛生态。这是该基准最强的设计决策——使得"AI 超越人类"的宣称有了客观锚点。
- **任务多样性而非规模**：75 题不算多，但每题都是真实竞赛，覆盖 15 个领域和 3 个复杂度层级。
- **规则与防作弊**：禁止智能体直接写入预测值或浏览在线解答，提供 GPT-4o 驱动的日志分析工具检测违规。设立抄袭检测（Dolos 工具，相似度 >60% 标记），最终未发现抄袭案例。
- **框架无关性与可访问性权衡**：仅需提交 CSV 的设计使任何智能体框架都可参与，但 1800 GPU-hours 的运行成本极高，制约了学术界的广泛复现。
- **安全治理工具的定位**：明确将 MLE-bench 定位为 AI 安全评估工具（OpenAI Preparedness Framework 等引用），反映了该工作对 ML R&D 加速风险的关注。

## 局限性
- Kaggle 竞赛偏向"调参冲刺"风格，有清晰的问题陈述、干净的标注数据和明确的评估指标，不反映真实 ML R&D 中"问题定义模糊、数据和指标需要自行梳理"的探索性工作。
- 数据污染风险难以彻底排除——部分竞赛在模型训练截止日期前已公开，GPT-4 base 模型可逐行复现 Titanic 数据集内容。虽通过熟悉度分析和描述混淆实验给出初步信号，但无法保证未来模型不受污染。
- 仅评估结果指标，不评估过程的合理性、代码质量、可解释性。
- 人类基线是排行榜数据而非受控实验，不与 AI 在相同硬件和时间内完成，可比性有限。
- 奖牌体系对高参与度竞赛的金牌阈值极严格（1000+ 队伍时金牌仅限 top 10），增加低样本下的统计方差。

## 核心贡献
MLE Bench 2024 的核心贡献是把 ML engineering agent 的能力评估锚定到 75 个真实离线 Kaggle 竞赛和人类奖牌体系上，使数据准备、模型训练、特征工程、调参、提交与资源扩展等端到端 ML 工程能力可以与真实人类排行榜结果进行比较。

## 与综述的关联
MLE-Bench 是目前 ML 工程领域最具代表性的智能体基准之一，衡量的是智能体执行完整数据科学工作流的能力。在本综述的 benchmark 章节中，它代表"ML 工程自动化"任务方向，与 RE-Bench（研究工程，关注开放式探索和人类对标）、MLAgentBench（实验迭代，较早期设计但奠定性地位）、ScienceAgentBench（科学发现编码，多学科且强调科学真实性）构成互补评估矩阵。其 ICLR 2025 的接收也表明学术界的认可。
