# Mamba-3: Improved Sequence Modeling using State Space Principles
**作者**: Albert Gu, Tri Dao | **年份**: 2025 | **arxiv**: 2603.15569

## 0. 摘要翻译
Mamba-3 是 Mamba 系列的第三代，通过三个关键改进提升了 SSM 的序列建模能力：(1) 指数梯形离散化（Exponential-Trapezoidal Discretization）恢复复数值动态的表达能力；(2) 复数值 SSM 在实数参数化下的高效实现；(3) 多输入多输出（MIMO）SSM 增强通道间交互。Mamba-3 在推理效率上设立了新的 Pareto 前沿，超越 Mamba-2 和强 Transformer 基线。

## 1. 方法动机
a) **为什么**: Mamba-2 通过 SSD 框架统一了 SSM 和注意力，但为了计算效率限制在实数对角 SSM，丢失了 S4 中复数值动态的表达能力。
b) **痛点**: (1) 实数对角 SSM 只能建模指数衰减，无法建模振荡模式；(2) Mamba-2 的 SISO（单输入单输出）结构限制了通道间交互；(3) 离散化方法（ZOH）在选择性 SSM 中不是最优的。
c) **假设**: 通过更好的离散化方法恢复复数值动态，并引入 MIMO 结构增强通道交互，可以在保持 Mamba-2 效率的同时显著提升质量。

## 2. 方法设计

### a) 指数梯形离散化 (Exponential-Trapezoidal)
- Mamba-1/2 使用零阶保持（ZOH）离散化: `Ā = exp(ΔA)`
- 问题: ZOH 对选择性（输入依赖的 Δ）SSM 不是最优的
- Mamba-3 使用指数梯形规则:
  - `Ā_t = exp(Δ_t · A)`
  - `B̄_t = (exp(Δ_t · A) - I) · A^{-1} · B_t` (梯形近似)
- 这使得复数值 A 的振荡模式可以被正确离散化

### b) 复数值 SSM 的实数实现
- A 矩阵使用复数值（共轭对形式）: `a + bi`
- 状态 x 也是复数值
- 但通过共轭对技巧，所有计算可以用实数运算完成
- 存储: 只需存储实部和虚部，不需要复数运算库
- 复数值恢复了 S4 的振荡建模能力

### c) MIMO SSM
- Mamba-1/2: 每个通道独立的 SISO SSM
- Mamba-3: 引入通道间交互的 MIMO SSM
  - 状态更新: `x_t = Ā_t x_{t-1} + B̄_t u_t` (B 是矩阵，不是向量)
  - 输出: `y_t = C_t x_t` (C 也是矩阵)
- 增强了不同特征通道间的信息交换

### d) 关键公式
- 连续 SSM: `dx/dt = Ax + Bu`, `y = Cx`
- 指数梯形离散化: `x_t = exp(Δ_t A) x_{t-1} + (exp(Δ_t A) - I)A^{-1} B_t u_t`
- 复数 A: `A = diag(a_1 + b_1 i, a_1 - b_1 i, a_2 + b_2 i, ...)` (共轭对)
- MIMO: B ∈ R^{N×D}, C ∈ R^{D×N} (N=状态维度, D=通道数)

## 3. 对比
| 模型 | 离散化 | 值域 | 通道交互 | 振荡建模 |
|------|--------|------|----------|----------|
| S4 | 双线性 | 复数 | SISO | 是 |
| Mamba | ZOH | 实数 | SISO | 否 |
| Mamba-2 | ZOH | 实数 | SISO | 否 |
| Mamba-3 | 指数梯形 | 复数(实数实现) | MIMO | 是 |

## 4. 实验
- **语言建模**: Mamba-3 在同参数量下超越 Mamba-2，缩小与 Transformer 的差距
- **长程依赖**: 在需要振荡模式的任务上（如周期性序列）显著优于 Mamba-2
- **推理效率**: 保持 Mamba-2 的线性推理复杂度，实际速度相当
- **Scaling**: 在 1B-7B 参数范围验证了改进的一致性
- **Pareto 前沿**: 在质量-效率权衡上超越 Mamba-2 和同规模 Transformer

## 5. 总结
a) **一句话**: Mamba-3 通过指数梯形离散化恢复复数值 SSM 的振荡建模能力，并引入 MIMO 结构增强通道交互，在保持线性推理效率的同时设立了新的质量-效率 Pareto 前沿。
b) **速记 pipeline**: `Input → Selective SSM(Complex A, Exp-Trapezoidal Discretize, MIMO B/C) → Gate ⊙ Output | Recurrent: O(d) per step`
