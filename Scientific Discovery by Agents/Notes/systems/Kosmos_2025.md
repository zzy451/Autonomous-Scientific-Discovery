# Kosmos 2025

## 基本信息
- **论文**: Kosmos: An AI Scientist for Autonomous Discovery
- **作者**: Ludovico Mitchener et al.
- **年份**: 2025
- **来源**: arXiv:2511.02824v2, submitted 2025-11-04, revised 2025-11-05
- **关键词**: system, ai-scientist, data-driven-discovery, long-horizon-agent, world-model

## 核心思想
数据驱动科学发现需要反复进行文献搜索、假设生成和数据分析。已有 AI research agents 可以自动执行部分科研流程，但常在长程任务中失去 coherence，导致行动次数有限、发现深度不足。

Kosmos 要解决的问题是：能否让 AI scientist 在开放式目标和数据集上长时间运行，并通过结构化 world model 保持跨轮次、跨 agent 的信息一致性，从而产生可追溯的科学发现报告。

## 方法细节
Kosmos 接收 open-ended objective 和 dataset，然后进行最长 12 小时的自动发现循环。它在每轮中并行执行数据分析、文献搜索和假设生成，再把发现综合为 scientific reports；系统主要面向 data-driven discovery，而不是湿实验执行。

核心机制是 structured world model。该 world model 在 data analysis agent 和 literature search agent 之间共享信息，使系统不只是顺序调用工具，而是在长程运行中保留任务状态、已知发现、文献证据和数据分析结果。

论文强调 Kosmos 与已有系统的差异：不是一次性生成论文或执行短流程，而是在大量 agent rollouts 中持续读取文献、运行代码、更新假设，并要求报告中的每个 statement 都由代码或 primary literature 引用支撑。

## 关键结果

1. Kosmos 最长运行 12 小时，进行 parallel data analysis、literature search 和 hypothesis generation cycles。
2. structured world model 在 data analysis agent 和 literature search agent 之间共享状态，支持系统跨 200 个 agent rollouts 保持任务 coherence。
3. 每次运行平均执行约 42,000 行代码，并阅读约 1,500 篇论文。
4. Kosmos 报告中的 statements 都要求用代码或 primary literature 引用支撑。
5. 独立科学家评估认为 Kosmos reports 中 79.4% 的 statements 是 accurate。
6. 合作者报告，一个 20-cycle Kosmos run 平均相当于他们约 6 个月的研究时间；这是合作者主观估计，不是独立时间审计。
7. 论文展示 7 个 discoveries，覆盖 metabolomics、materials science、neuroscience 和 statistical genetics。
8. 其中 3 个 discoveries 独立复现了 Kosmos runtime 未访问的 preprinted 或 unpublished manuscripts 中的发现，4 个被作者描述为对科学文献的新贡献。
9. 作者还报告，valuable findings 数量随 discovery cycles 增加大致线性提升，至少在 20 cycles 以内没有明显饱和。

## 与综述的关联

在 Scientific Workflow 中，Kosmos 覆盖 Knowledge Grounding、Hypothesis Generation、Result Analysis、Synthesis 和 Verification。它尤其重要的是把长程数据分析和文献搜索连成可追溯 discovery loop。

在 Skill Lifecycle 中，它对应：

- Representation：world model 作为跨 agent、跨轮次的研究状态表示；
- Retrieval：文献搜索 agent 读取并整合大量 primary literature；
- Composition：data analysis agent 与 literature search agent 协作；
- Execution：大规模代码执行和数据分析；
- Evolution：多轮循环中持续更新假设和发现；
- Verification：报告 statements 绑定代码或文献引用，并由独立科学家评估。

Evidence Role 应标为 **Direct + Boundary**。Kosmos 是跨域 autonomous discovery 的强候选证据，但目前仍是 arXiv preprint，且“6 个月研究时间”等评价来自合作者报告，需要谨慎使用。它最适合支撑 long-horizon scientific agent 与 world-model memory 的重要性。

## 局限性

Kosmos 不是湿实验平台，主要面向已有 dataset 和文献的 data-driven discovery。论文中的发现质量需要进一步独立复现和同行评议。系统规模较大，每次运行涉及大量代码执行和文献读取，计算成本、失败恢复、安全约束和错误累积风险都需要进一步分析。

## 核心贡献

Kosmos 的核心贡献是提出用 structured world model 支撑长程 AI scientist，使 agent 能在多轮文献搜索、数据分析和假设生成中保持 coherence，并产出带代码和文献证据的跨域发现报告。
