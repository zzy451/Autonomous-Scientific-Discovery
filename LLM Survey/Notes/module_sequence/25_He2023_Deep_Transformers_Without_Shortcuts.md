# Deep Transformers without Shortcuts: Modifying Self-attention for Faithful Signal Propagation
**作者**: Bobby He, James Martens, Guodong Zhang, Aleksandar Botev, Andrew Brock, Samuel L. Smith, Yee Whye Teh | **年份**: 2023 (ICLR 2023) | **arxiv**: 2302.10322

## 0. 摘要翻译
跳跃连接和归一化层是训练深度神经网络的两个标准架构组件，但其精确作用尚不清楚。近期方法（如 Deep Kernel Shaping）利用宽网络核理论的洞察改善了无跳跃/无归一化的普通 DNN 的信号传播，但这些方法不兼容 Transformer 中的自注意力层——自注意力的核本质上是输入依赖的。本文设计了多种方法，通过参数初始化、偏置矩阵和位置相关的重缩放的组合，在自注意力层中实现忠实的信号传播。在 WikiText-103 和 C4 上的实验表明，这些方法使无归一化的深层 Transformer 达到与标准对应物匹配的训练速度，并使无跳跃连接的深层 vanilla Transformer 达到标准 Transformer 的性能水平。

## 1. 方法动机
- 跳跃连接和归一化层对训练深层网络至关重要，但它们是"必需品"还是"权宜之计"？
- Deep Kernel Shaping 等方法已能在 MLP/CNN 中实现无 skip/无 norm 训练
- 但自注意力层的核是**输入依赖的**（data-dependent kernel），现有信号传播理论不直接适用
- 需要专门针对自注意力设计信号传播修正方案
- 目标：理解并移除 Transformer 对跳跃连接和归一化的依赖

## 2. 方法设计
- **信号传播分析**: 分析自注意力层中前向/反向信号的传播特性
  - 标准 Softmax 注意力导致表示坍缩（秩退化）
  - 注意力矩阵的行和为 1 的约束导致信号传播偏差
- **三种修正方案**:
  1. **Value-Skip (V-Skip)**: 在 Value 投影中加入跳跃连接
     - $\text{Attn}(Q,K,V) = \text{Softmax}(QK^T/\sqrt{d}) \cdot V + V$
     - 确保即使注意力矩阵退化，信息仍可通过 skip 传递
  2. **Centered Attention**: 将注意力矩阵中心化
     - 移除注意力矩阵的均值分量，保留有意义的差异信号
  3. **位置相关重缩放**: 根据序列位置调整注意力权重
     - 补偿因果掩码导致的不同位置接收不同数量注意力的问题
- **参数初始化**: 配合上述修改，精心设计权重初始化以确保信号传播的忠实性

## 3. 对比
| 方法 | 目标 | 适用架构 | 可移除组件 |
|------|------|---------|-----------|
| Deep Kernel Shaping | 信号传播 | MLP/CNN | Skip + Norm |
| Shaped Transformer (Noci 2023) | 秩坍缩理论 | Transformer | Skip + Norm (理论) |
| 本文 | 自注意力信号传播 | Transformer | Skip 和/或 Norm |
| SkipInit (De & Smith 2020) | 恒等偏置 | ResNet | Norm |

## 4. 实验
- **任务**: 语言建模 (WikiText-103, C4)
- **关键结果**:
  - **无归一化**: 修改后的深层 Transformer 训练速度匹配标准 Pre-LN Transformer
  - **无跳跃连接**: vanilla Transformer（无 skip）达到标准 Transformer 的性能水平
  - **完全无 skip 无 norm**: 也能训练，但性能有一定差距
  - V-Skip 是最有效的单一修改
- **深度扩展**: 在不同深度（6层到48层）上验证，深层网络改进更显著
- **与 Shaped Transformer 的关系**: 共享作者 (Bobby He)，理论互补——Shaped 提供极限理论，本文提供实用方案

## 5. 总结
a) 一句话: 通过 Value-Skip、中心化注意力和位置重缩放等修改，使深层 Transformer 在无归一化甚至无跳跃连接的情况下实现忠实的信号传播和有效训练。
b) 速记 pipeline: `分析自注意力信号传播缺陷 → 提出 V-Skip / Centered Attn / 位置重缩放 → 配合初始化 → 无 Norm 匹配标准速度, 无 Skip 匹配标准性能`; 核心: 自注意力的信号传播可以被显式修正。
