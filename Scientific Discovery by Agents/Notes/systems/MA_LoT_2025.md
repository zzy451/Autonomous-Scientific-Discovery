# MA-LoT 2025

## 基本信息

- **论文**: MA-LoT: Multi-Agent Long Chain-of-Thought Framework for Mathematical Reasoning Enhanced by LoT
- **年份**: 2025
- **来源**: arXiv:2503.03205
- **系统名称**: MA-LoT
- **关键词**: multi-agent reasoning, Lean verification, prover, verifier, long chain-of-thought

## 摘要要点

MA-LoT 面向数学推理与形式化验证，将多个 agent / model collaboration 与 Lean4 verifier 结合。系统不是开放式科学发现系统，而是 formal proof execution substrate：它通过 prover / verifier 或 corrector 协作，让推理链在 Lean feedback 下被检查和修正。

## 方法动机

长链式数学推理容易出现局部错误，普通自然语言答案难以保证正确性。形式化证明系统如 Lean 可以提供严格反馈，但 LLM 需要把自然语言推理转成可验证步骤，并根据错误信息修正。MA-LoT 的目标是让多个 agents 分工生成、检查和修复证明。

## 方法设计

可概括为：

1. prover agent 生成初始 Long-CoT 或证明草图。
2. verifier / corrector agent 检查推理步骤或 Lean 代码。
3. Lean4 verifier 返回形式化错误或成功信号。
4. agents 根据反馈修改证明。
5. 多轮循环直到通过验证或达到停止条件。

当前分类中保守标为 `Y1`，因为证据更像 Lean-feedback 修正，而不是明确 MCTS/tree search。

## 实验与结果

论文在数学推理/证明相关任务上展示多 agent collaboration 与 Lean verification 能提升答案可靠性。它的关键价值是把自然语言 reasoning 与 formal verifier 连接起来。

## 局限性

- 不应写成完整 ASD 系统。
- 当前主要是证明/数学推理执行基底，不覆盖文献、实验或结果分析。
- 多轮修正不等同于显式树搜索。

## XYZ 分类

| 维度 | 标注 | 理由 |
|---|---|---|
| X | `X2` | prover 与 verifier/corrector 是固定异质角色 |
| Y | `Y1` | 主要机制是 Lean feedback 下的修正 |
| Z | `Z3,Z4,Z7` | 覆盖证明设计、证明执行和形式验证 |

## 对综述的价值

MA-LoT 可用于第 6 章 formal proof substrate，说明多智能体 ASD 的验证边界可以接入 Lean 这类形式化执行器；但正文中不要把它写成 tree search 或自然科学发现系统。

