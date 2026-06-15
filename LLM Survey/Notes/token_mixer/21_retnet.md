# Retentive Network: A Successor to Transformer for Large Language Models (RetNet)
**作者**: Yutao Sun, Li Dong, Shaohan Huang, Shuming Ma, Yuqing Xia, Jilong Xue, Jianyong Wang, Furu Wei (Microsoft Research, Tsinghua) | **年份**: 2023 | **arxiv**: 2307.08621

## 0. 摘要翻译
本文提出RetNet作为大语言模型的基础架构，同时实现训练并行性、低成本推理和良好性能，达成"不可能三角"。RetNet引入多尺度保留机制（multi-scale retention）来替代多头注意力。该机制支持三种等价的计算范式：(1) 并行表示用于高效训练；(2) 循环表示用于低成本$O(1)$推理；(3) 分块循环表示用于高效的长序列推理。实验表明RetNet在语言建模上取得了与Transformer相当的结果，同时推理成本显著降低。

## 1. 方法动机
a) **为什么提出**: 现有架构无法同时满足三个目标——训练并行性（Transformer有，RNN无）、$O(1)$推理（RNN有，Transformer无）、良好性能（Transformer有，线性模型差）。
b) **现有痛点**: (1) Transformer推理时KV cache线性增长，每步$O(L)$；(2) RNN训练无法并行；(3) 线性注意力性能不足；(4) 需要一种统一的框架同时支持并行训练和循环推理。
c) **研究假设**: 通过在复数域引入指数衰减（retention），可以设计一种同时具有并行和循环表示的机制，兼顾训练效率和推理效率。

## 2. 方法设计
a) **Pipeline**: 用Retention层替代Self-Attention层，其余架构（FFN、残差连接等）保持不变。

b) **模块功能**:
- **Retention机制**: 
  核心公式（循环形式）: $s_t = \gamma s_{t-1} + k_t^T v_t$, $o_t = q_t s_t$
  其中$\gamma \in (0, 1)$是衰减因子。
  
- **三种等价表示**:
  1. **并行表示（训练用）**: $\text{Retention}(Q,K,V) = (QK^T \odot D) V$，其中$D_{ij} = \gamma^{i-j}$（$i \geq j$时），$D_{ij} = 0$（$i < j$时）。本质是带指数衰减掩码的线性注意力。
  2. **循环表示（推理用）**: $s_t = \gamma s_{t-1} + k_t^T v_t$, $o_t = q_t s_t$。每步$O(d^2)$，状态大小$O(d^2)$。
  3. **分块循环表示（长序列推理）**: 块内用并行表示，块间用循环传递状态。平衡了并行性和内存效率。

- **多尺度Retention (Multi-Scale)**:
  - 不同头使用不同的衰减率$\gamma_h$
  - $\gamma_h = 1 - 2^{-5-h}$（如$\gamma_1=0.96875, \gamma_2=0.984375, ...$）
  - 不同头捕获不同时间尺度的依赖关系
  
- **复数域表示**: 使用$e^{i\theta}$引入位置信息（类似RoPE），$\gamma$实际为$|\gamma|e^{i\theta}$。

c) **公式解释**:
- 并行形式中$D$矩阵的作用: 类似因果掩码+指数衰减，近期token权重大、远期token权重指数衰减
- 与线性注意力的区别: 线性注意力无衰减（$\gamma=1$），Retention有衰减（$\gamma<1$），衰减提供了遗忘机制
- 与Transformer的区别: 无softmax归一化，用衰减替代

## 3. 与其他方法对比
| 方面 | RetNet | Transformer | RWKV | Mamba | Linear Attn |
|------|--------|-------------|------|-------|-------------|
| 训练 | 并行$O(L^2d)$ | 并行$O(L^2d)$ | 并行$O(Ld)$ | scan$O(LdN)$ | 并行$O(Ld^2)$ |
| 推理 | 循环$O(d^2)$/步 | $O(Ld)$/步 | $O(d)$/步 | $O(dN)$/步 | $O(d^2)$/步 |
| 衰减 | 指数$\gamma^{i-j}$ | 无 | 指数$e^{-w}$ | 选择性$\Delta$ | 无 |
| 多尺度 | 不同$\gamma_h$ | 无 | 单一$w$ | 输入依赖 | 无 |

## 4. 实验表现
- **语言建模**: 在1.3B-6.7B规模上，PPL与Transformer相当（差距<0.5）
- **推理速度**: 比Transformer快约8.4倍（循环模式），内存减少约70%
- **训练速度**: 与Transformer相当（并行模式）
- **长序列**: 分块循环模式可高效处理长序列
- **下游任务**: 在多个zero-shot基准上与Transformer竞争
- **Scaling**: 在不同规模上scaling行为与Transformer一致

## 5. 总结
a) **一句话概括**: RetNet通过多尺度指数衰减的retention机制，实现了并行训练（类注意力）、循环推理（类RNN）和分块长序列处理三种等价计算范式，打破了训练并行性、推理效率和模型质量的"不可能三角"。
b) **速记pipeline**: 训练: Q,K,V → (QKᵀ⊙D_γ)V（并行）| 推理: s_t = γs_{t-1} + kᵀv → o = qs（循环）
