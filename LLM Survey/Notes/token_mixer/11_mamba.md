# Mamba: Linear-Time Sequence Modeling with Selective State Spaces
**作者**: Albert Gu, Tri Dao | **年份**: 2023 | **arxiv**: 2312.00752

## 0. 摘要翻译
基础模型（特别是Transformer及其核心注意力层）在深度学习的多个领域推动了重大进展。同时，许多亚二次时间复杂度的架构（如线性注意力、门控卷积/循环模型和结构化状态空间模型SSM）被开发来解决Transformer在长序列上的计算效率问题，但在语言等重要模态上尚未追上注意力的性能。本文提出的选择性状态空间模型通过引入输入依赖的选择机制解决了这一问题。Mamba结合了选择性SSM与硬件感知的并行算法，在语言建模上首次实现了与Transformer相当的性能，同时保持了线性时间复杂度。

## 1. 方法动机
a) **为什么提出**: 之前的SSM（如S4、H3）使用固定参数（不依赖输入），导致在需要内容感知推理的任务上表现不佳（如选择性复制、感应头等）。
b) **现有痛点**: (1) 线性时间模型（RNN/SSM）在语言建模上显著落后于Transformer；(2) 固定参数SSM无法根据输入内容动态调整信息保留策略；(3) 输入依赖的SSM破坏了高效的卷积计算模式。
c) **研究假设**: 通过让SSM的参数依赖于输入（即选择性），模型可以学会在相关信息出现时"记住"、在无关信息出现时"忘记"，从而弥补与注意力的性能差距。

## 2. 方法设计
a) **Pipeline**: Mamba block = 线性投影扩展 → 卷积 → 选择性SSM → 线性投影回原维度。不使用注意力层。

b) **模块功能**:
- **选择性SSM (Selective State Space Model)**: 
  连续时间SSM: $h'(t) = Ah(t) + Bx(t)$, $y(t) = Ch(t)$
  离散化后: $h_t = \bar{A}h_{t-1} + \bar{B}x_t$, $y_t = Ch_t$
  **选择性**: 参数$B$、$C$和步长$\Delta$均依赖于输入$x$：
  - $B = \text{Linear}_B(x)$, $C = \text{Linear}_C(x)$, $\Delta = \text{softplus}(\text{Linear}_\Delta(x))$
  - $\bar{A} = \exp(\Delta A)$, $\bar{B} = (\Delta A)^{-1}(\exp(\Delta A) - I) \cdot \Delta B$（简化为$\bar{B} \approx \Delta B$）
- **硬件感知算法**: 
  - 由于参数输入依赖，无法使用FFT卷积。改用扫描（scan）算法并行计算。
  - 关键优化：将SSM状态保持在GPU SRAM中（而非HBM），减少内存IO。
  - 使用kernel fusion将离散化、扫描和输出计算合并在一个GPU kernel中。
- **Mamba Block架构**: 
  $x → \text{Linear}(\uparrow D) → [\text{Conv1d} → \text{SiLU} → \text{SSM}] \otimes [\text{SiLU}] → \text{Linear}(\downarrow D)$
  使用门控机制（类似GLU），一条路径经过Conv+SSM，另一条直接激活后做门控。

c) **公式解释**:
- $\Delta$控制"时间步长"：大$\Delta$表示关注当前输入、重置状态；小$\Delta$表示忽略当前输入、保持状态
- 选择性让模型学会：遇到重要token时增大$\Delta$（写入状态），遇到无关token时减小$\Delta$（保持不变）
- 复杂度: $O(L \cdot D \cdot N)$，其中$N$是状态维度（如16），线性于序列长度$L$

## 3. 与其他方法对比
| 方面 | Mamba | Transformer | S4 (SSM) | RWKV | H3 |
|------|-------|-------------|----------|------|-----|
| 复杂度 | $O(LDN)$ | $O(L^2D)$ | $O(L\log L \cdot D)$ | $O(LD)$ | $O(LDN)$ |
| 参数依赖 | 输入依赖 | 输入依赖 | 固定 | 部分 | 部分 |
| 推理模式 | 循环（常数时间/步）| 需KV cache | 循环 | 循环 | 循环 |
| 语言建模 | 匹配Transformer | 基准 | 明显落后 | 接近 | 接近 |
| 训练并行 | scan并行 | 完全并行 | FFT并行 | 并行 | 并行 |

## 4. 实验表现
- **语言建模**: Mamba-3B在多个zero-shot评估上匹配甚至超越Transformer-3B（在相同token数训练下）
- **选择性复制**: 在合成的选择性复制任务上完美解决，而固定SSM失败
- **感应头 (Induction Heads)**: 成功学习感应头模式，固定SSM无法学习
- **音频建模 (SC09)**: 超越所有baseline包括S4和Transformer
- **DNA建模**: 在基因组学任务上达到新SOTA
- **推理效率**: 推理时每步$O(1)$（相对于序列长度），生成速度比Transformer快约5倍
- **训练效率**: 在A100 GPU上训练吞吐量接近Transformer（得益于硬件感知算法）

## 5. 总结
a) **一句话概括**: Mamba通过让SSM参数（$B$、$C$、$\Delta$）依赖输入实现选择性，配合硬件感知的scan并行算法，首次让线性时间序列模型在语言建模上匹配Transformer性能。
b) **速记pipeline**: x → Linear↑ → [Conv1d → SiLU → SelectiveSSM(B(x),C(x),Δ(x))] ⊗ SiLU(gate) → Linear↓ → output
