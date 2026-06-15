# Benchmarking SDL 2026

## 基本信息
- **论文**: Benchmarking Self-Driving Labs
- **作者**: Adedire D. Adesiji, Jiashuo Wang, Cheng-Shu Kuo, Keith A. Brown
- **年份**: 2026
- **来源**: Digital Discovery 5:14-27, doi:10.1039/D5DD00337G
- **关键词**: benchmark, self-driving-lab, autonomous-experimentation, evaluation

## 核心思想
这篇论文系统讨论 self-driving laboratories 如何被横向比较。SDL 文献中常报告不同任务、不同硬件、不同优化目标和不同成本，但如果没有共同 benchmark，很难判断一个系统是否真正比另一个系统更高效。论文重点梳理 acceleration factor (AF) 和 enhancement factor (EF) 两个指标：AF 衡量达到同等目标时减少了多少实验次数，EF 衡量固定实验预算下结果提升多少。

## 评测目标
这篇论文讨论 self-driving laboratories 如何被横向比较。SDL 文献中常报告不同任务、不同硬件、不同优化目标和不同成本，但如果没有共同 benchmark，很难判断一个系统是否真正比另一个系统更高效。

评测目标是建立一套可比较的 SDL benchmarking 思路，使不同 closed-loop experimental systems 能围绕效率、搜索空间、实验次数和优化性能进行更透明的比较。

## 基准设计
论文关注 SDL benchmark 的指标化表达，尤其讨论 acceleration factor (AF) 和 enhancement factor (EF) 等可以跨研究提取的指标。

其核心设计思想包括：

- 从已发表 SDL studies 中提取可比较信息：作者用 "Bayesian optimization" + "benchmark" 在 Scopus 中检索到 4,245 篇文献，又用 "self-driving lab" 检索到 111 项研究，其中只有 40% 明确报告了 benchmark；
- 用 search space dimension、实验次数、优化目标和结果改进度描述系统；
- 区分 experimental、retrospective、computational 三类 benchmark，以及 random sampling、Latin hypercube sampling、grid-based sampling、human-directed sampling、algorithmic baseline 等 reference campaign；
- 提醒 benchmark 不能只看最终最优结果，还要看成本、吞吐、可复现性和任务难度。
- 通过模拟 Bayesian optimization campaigns 分析 property space 的统计性质如何影响 EF 与 AF：EF 受目标空间 contrast 等性质影响，AF 更受搜索空间复杂度和噪声影响。

## 关键数字

| 指标 | 说明 |
|---|---|
| Scopus 检索 | "Bayesian optimization" + "benchmark" 得到 4,245 篇 |
| SDL 检索 | "self-driving lab" 得到 111 项研究 |
| 明确报告 benchmark 的 SDL 研究 | 约 40% |
| AF / acceleration factor | 达到同等目标时相对 baseline 减少实验次数，表征"快多少" |
| EF / enhancement factor | 固定实验预算下相对 baseline 的结果提升，表征"好多少" |
| search-space dimension | 衡量优化问题复杂度 |
| number of experiments | 衡量闭环系统的实验成本 |
| 文献元分析趋势 | AF 中位数约为 6；EF 常在每个维度 10-20 次实验附近达到峰值 |

## 设计哲学

论文的设计哲学是：SDL 不能只靠单个炫目的发现案例证明有效。要让自动实验成为科学基础设施，就必须能说明“在哪类任务、什么成本、什么搜索空间、什么 baseline 下快了多少、好多少”。因此，benchmark 必须同时报告目标函数、参数空间维度、reference campaign、实验预算、失败实验和收敛过程。

## 局限性

SDL benchmark 面临高度异质的实验领域，统一指标可能忽略任务本身差异。许多已发表 SDL 工作没有完整报告可复现的成本、失败实验、搜索空间定义和 baseline，因此现阶段 benchmark 仍受文献报告质量限制。论文中的 BO 模拟是启发式分析，主要用于解释 AF/EF 变化趋势，不能覆盖多目标优化、强约束实验、硬件故障、实验室吞吐瓶颈等全部 SDL 情形。

## 核心贡献
Benchmarking SDL 2026 的核心贡献是把 self-driving lab 的"加速发现"主张转化为可比较的 benchmark 问题，系统梳理 AF/EF 指标、reference campaign 类型和 SDL 文献报告现状，并用模拟解释不同参数空间下 benchmark 数值为何会变化。

## 与综述的关联

在 Scientific Workflow 中，它主要覆盖 Verification 和 Evolution，因为它评估闭环实验系统是否真的提高了探索效率。

在 Skill Lifecycle 中，它对应 Verification / benchmark 和 Evolution / long-horizon learning。Evidence Role 应标为 **Infrastructure + Boundary**。它为 self-driving lab 证据链提供横向评价约束，防止我们只把单个成功案例当成普遍规律。
