# LLM Verifier 2025

## 基本信息

- **论文**: Multi-Agent Verification: Scaling Test-Time Compute with Multiple Verifiers
- **年份**: 2025
- **来源**: OpenReview
- **系统名称**: BoN-MAV / Multi-Agent Verification
- **关键词**: multi-agent verification, best-of-n, aspect verifiers, test-time compute, verifier ensemble

## 摘要要点

这篇工作提出用多个 verifier agents 在 test-time 对候选答案进行验证与选择。系统将 best-of-n sampling 与 aspect verifiers 结合：先生成多个候选答案，再由不同 verifier 从不同方面检查，最后选择更可靠的输出。论文强调，增加 verifier 数量和类型可以扩展 test-time compute，并带来弱到强泛化和 self-improvement 效果。

在本综述中，它不是 ASD 系统，而是 verification substrate：它说明科学 agent 产出的 hypothesis、proof、code 或 report 可以通过多 verifier 并行检查来提高可信度。

## 方法动机

单个 verifier 容易受到偏差、能力边界和 reward-model mismatch 的影响。对于科学发现，错误可能来自计算、引用、证明、实验设计或解释等多个方面，因此一个统一 verifier 很难覆盖所有风险。Multi-Agent Verification 的核心直觉是：把验证任务拆给多个 aspect verifiers，用多视角检查替代单点判断。

## 方法设计

流程可以概括为：

1. 生成器对同一问题采样得到多个 candidate answers。
2. 多个 verifier agents 分别从不同维度检查候选，如正确性、完整性、推理一致性或任务特定标准。
3. 系统聚合 verifier 信号，对候选答案排序或选择。
4. 通过增加 verifier 数量、类型和验证轮次扩展 test-time compute。

它的“多”不是多角色科研团队，而是同类/相近 verifier 的并行检查，因此对应 `X3`。

## 实验与结果

论文报告 BoN-MAV 随验证计算增加而提升性能，并展示弱 verifier 组合也能帮助更强模型选择更可靠输出。对 ASD 来说，关键结果不是某个单一任务分数，而是“verification compute 可以作为可扩展资源”这一机制。

## 局限性

- 主要面向答案验证，不直接覆盖科学发现全流程。
- verifier 的质量、独立性和聚合方式会影响最终可靠性。
- 对实验、物理验证或形式证明等高要求场景，仍需要领域工具或外部检查器。

## XYZ 分类

| 维度 | 标注 | 理由 |
|---|---|---|
| X | `X3` | 多个 verifier agents 并行评估候选输出 |
| Y | `Y2` | 多候选生成后由 verifier ensemble 选择较优答案 |
| Z | `Z7` | 直接对应验证、检查和 review 阶段 |

## 对综述的价值

LLM Verifier 适合放在第 7 章 verification / evidence closure，说明 ASD 的可信度闭环可以通过多 verifier、多标准、多轮检查扩展，而不是只依赖单一 judge。

