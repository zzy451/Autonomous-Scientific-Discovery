# OR-Agent 2026

## 基本信息

- **论文**: OR-Agent: Bridging Evolutionary Search and Structured Research for Automated Algorithm Discovery
- **年份**: 2026
- **来源**: arXiv:2602.13769
- **系统名称**: OR-Agent
- **关键词**: automated algorithm discovery, evolutionary search, structured research, tree-based workflow, multi-agent research framework

## 一句话总结

OR-Agent 将自动算法发现组织为结构化研究流程，把 branching hypothesis generation、systematic backtracking 和 evolutionary-systematic ideation 结合起来，用于补强“层级式多智能体 + artifact evolution”的证据。

## 研究问题

传统 evolutionary search 可以在候选空间中探索，但容易缺乏科学研究中的结构化推理、失败回溯和可解释研究过程。OR-Agent 试图把算法发现从黑箱式优化推进为更接近科研工作流的过程：提出假设、展开分支、执行尝试、保留失败、回溯并继续改进。

## 系统架构

从综述角度，OR-Agent 的重点不是具体算法任务，而是它把研究过程组织为 tree-based workflow：

| 机制 | 作用 |
|---|---|
| Branching hypothesis generation | 从一个研究方向扩展多个候选假设或算法思路 |
| Systematic backtracking | 对失败或低质量分支进行回溯 |
| Evolutionary-systematic ideation | 将演化搜索与结构化研究步骤结合 |
| Evaluation / feedback | 用任务表现和反馈筛选候选 |

如果深读确认其 agent 角色边界明确，建议归为 `X4`；如果多智能体角色不够清楚，则应降级为 `X0/Y4` 或作为第 5 章背景。

## XYZ 分类

暂定分类为：

| 维度 | 标注 | 理由 |
|---|---|---|
| X | `X4` | tree-based research workflow 带有调度和分支管理结构 |
| Y | `Y4` | 明确连接 evolutionary search 与候选 artifact 改进 |
| Z | `Z2,Z3,Z4,Z5,Z7,Z8` | 覆盖问题/假设、算法设计、执行、结果评估、验证和迭代 |

建议放入 **ASD 相关系统**：它更偏 automated algorithm discovery，不一定覆盖完整科学发现闭环。

## 对综述的价值

OR-Agent 可以补 `X4-Y4-*` 稀疏坐标，使层级多智能体中的 artifact evolution 不只依赖 CoScientist_2026。它尤其适合与 CoScientist 对照：

- CoScientist：科学假设 tournament 与 biomedical validation。
- OR-Agent：算法 artifact 的 structured evolutionary research。

## 局限性

- 是否属于严格 ASD 取决于算法发现任务是否产生新的科学/算法贡献，而不只是 benchmark 优化。
- 多智能体角色边界需要深读确认。
- 自动评价指标可能偏向可测 benchmark，而不是科学重要性。

