# BFS Prover V2 2025

## 基本信息

- **论文**: BFS-Prover-V2: Scaling Formal Theorem Proving with Planner-Enhanced Multi-Agent Tree Search
- **年份**: 2025
- **来源**: arXiv / formal theorem proving preprint
- **系统名称**: BFS-Prover-V2
- **关键词**: formal theorem proving, Lean, multi-agent tree search, planner, proof cache

## 摘要要点

BFS-Prover-V2 面向 Lean 形式化定理证明，提出 planner-enhanced multi-agent tree search。系统将定理分解为子目标，由多个并行 prover agents 推进证明搜索，并共享 proof cache。它是形式证明 execution substrate 中较清晰的 `X3-Y3` 证据。

## 方法动机

形式化证明搜索空间巨大，单个 prover 容易陷入局部路径。传统 BFS/DFS 或单模型生成无法充分利用并行计算和中间证明缓存。BFS-Prover-V2 的直觉是：让多个 prover agents 并行探索 proof tree，并由 planner 组织子目标，可以提高搜索覆盖率和证明效率。

## 方法设计

流程包括：

1. 输入 Lean theorem。
2. planner 将目标拆解为 proof subgoals 或搜索节点。
3. 多个 prover agents 并行尝试证明不同节点。
4. proof cache 保存已解决子目标、中间 lemma 和失败路径。
5. 搜索策略根据当前 proof tree 状态选择下一批节点。
6. Lean checker 验证候选证明，成功后合并到完整 proof。

其 `X3` 来自多个同类 prover agents 并行探索，`Y3` 来自显式 tree search。

## 实验与结果

论文在 Lean theorem proving benchmarks 上评估系统，展示 planner、multi-agent parallelism 和 proof cache 对证明成功率和搜索效率的帮助。关键贡献是把 tree search 与 agent parallelism 结合。

## 局限性

- 任务集中在形式化数学证明，不覆盖自然科学实验。
- proof search 的成功依赖 theorem decomposition 和 Lean feedback。
- 并行搜索会增加计算成本。

## XYZ 分类

| 维度 | 标注 | 理由 |
|---|---|---|
| X | `X3` | 多个同类 prover agents 并行搜索证明 |
| Y | `Y3` | planner-enhanced tree search 是核心机制 |
| Z | `Z3,Z4,Z7,Z8` | 覆盖证明设计、执行、Lean 验证和迭代修复 |

## 对综述的价值

BFS-Prover-V2 可用于说明 formal proof 是 ASD 的一种 execution substrate，并且多智能体中的“多”可以表现为同类 prover 并行扩展 proof search breadth。

