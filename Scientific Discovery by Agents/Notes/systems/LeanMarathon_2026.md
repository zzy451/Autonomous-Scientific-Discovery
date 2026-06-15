# LeanMarathon 2026

## 基本信息

- **论文**: LeanMarathon: Large-Scale Autoformalization and Theorem Proving for Research Mathematics
- **年份**: 2026
- **来源**: arXiv:2606.05400
- **系统名称**: LeanMarathon
- **关键词**: Lean, autoformalization, proof DAG, orchestrator, construct/audit/prove/repair agents

## 摘要要点

LeanMarathon 面向研究数学的 autoformalization 和 Lean proof production。系统采用 two-stage orchestrator，协调 construct、audit、prove、repair 等 agents，并沿 proof DAG 并行推进证明任务。它不是自然科学发现系统，但能作为 formal proof execution substrate 的强证据。

## 方法动机

研究数学形式化需要把自然语言定义、定理和证明转换成 Lean 代码，并处理大量依赖关系。单个 prover 难以管理整本理论或复杂证明图。LeanMarathon 的目标是把大规模 autoformalization 拆成可调度的 proof DAG，并让专门 agents 分工完成构造、审计、证明和修复。

## 方法设计

流程包括：

1. 将数学材料解析为 definitions、lemmas、theorems 和依赖关系。
2. 构建 proof DAG，确定哪些节点可以并行推进。
3. construct agent 生成形式化定义和证明骨架。
4. audit agent 检查形式化目标是否对应原数学意图。
5. prove agent 尝试生成 Lean proof。
6. repair agent 根据 Lean 错误修复代码。
7. orchestrator 管理节点状态、依赖和 CI-gated verification。

与 `X3` 的同类 prover 并行不同，LeanMarathon 的角色分工和两阶段调度更符合 `X4`。

## 实验与结果

论文展示系统可处理研究数学级别的 autoformalization，并通过 proof DAG 与 CI-gated Lean checking 推进长周期证明工程。其核心实验价值在于证明大规模形式化可以被 agent workflow 管理。

## 局限性

- 只覆盖形式化数学，不代表自然科学实验发现。
- proof DAG 构建和原文语义对齐仍需要审计。
- 成功率依赖 Lean 库、定理分解和模型能力。

## XYZ 分类

| 维度 | 标注 | 理由 |
|---|---|---|
| X | `X4` | two-stage orchestrator 协调 construct/audit/prove/repair agents |
| Y | `Y3` | proof DAG 上的路径搜索和 CI-gated proof discharge |
| Z | `Z3,Z4,Z7,Z8` | 覆盖证明设计、执行、Lean 验证和长周期修复 |

## 对综述的价值

LeanMarathon 可用于强调 ASD 的 execution substrates 包括 formal proof。它也说明层级多智能体可以组织 proof labor，而不只是组织实验室或代码任务。

