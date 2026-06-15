# T-Fixup: Improving Transformer Optimization Through Better Initialization

**论文信息**: Huang, X.S., Perez, F., Ba, J., Volkovs, M. (2020)
**arXiv**: 1910.05449 | **会议**: ICML 2020
**分类**: Control (初始化方案)

## 核心思想
T-Fixup 提出一种专门针对 Transformer 的权重初始化方案，通过根据网络深度 N 仔细缩放权重矩阵，使得 SGD 更新的幅度在训练过程中保持有界。这使得深层 Transformer 可以在不需要学习率 warmup 和 Layer Normalization 的情况下稳定训练。

## 数学公式
核心初始化规则:
- 编码器中 Attention 的 V, 输出投影 和 FFN 第二层: 乘以 (9N)^{-1/4} 缩放因子
- 解码器中相应层: 类似但考虑解码器深度
- 输入嵌入: Xavier 初始化后乘以 d^{-1/2}

这些缩放确保了:
- 前向传播中信号幅度保持稳定
- 反向传播中梯度幅度保持稳定
- 参数更新幅度与深度无关

## 关键机制
- **去除 LayerNorm**: T-Fixup 证明了正确初始化可以替代 LayerNorm 的稳定化作用
- **去除学习率 warmup**: 不再需要传统 Transformer 训练中必须的 warmup 阶段
- **深度缩放**: 初始化缩放因子与层数 N 相关，自动适应不同深度
- **理论保证**: 提供了关于模型更新幅度有界的理论分析

## 与 Fixup 的关系
- **Fixup** (Zhang 2019): 最初为 ResNet/CNN 设计的无归一化初始化方案
- **T-Fixup**: 将 Fixup 思想适配到 Transformer 架构
- T-Fixup 还解决了 Adam 优化器二阶动量带来的额外不稳定性

## 实验结果
- 可训练多达 200 层的 Transformer（无 LayerNorm、无 warmup）
- 在机器翻译任务上达到与标准 Transformer 相当的性能
- 训练动态更加稳定

## 与其他 Control 方法对比
| 方法 | 核心策略 | 是否去LN | 是否去warmup | 额外参数 |
|------|----------|----------|--------------|----------|
| Fixup | 权重缩放+偏置 | 是 | 是 | 偏置 |
| T-Fixup | 权重缩放(深度相关) | 是 | 是 | 无 |
| ReZero | 零初始化标量 | 是(可选) | 是 | 标量 |
| SkipInit | 零初始化标量 | 是 | 是 | 标量 |
| Admin | 自适应向量 | 否(改进Post-LN) | 是 | 向量 |

## 与综述的关联
属于 **Control** 维度。与 Fixup、ReZero、SkipInit 共同构成 2019-2020 年"通过初始化控制残差连接"的研究浪潮。核心洞察一致：如果控制好残差分支的初始信号幅度，就可以去除归一化层和 warmup，大幅简化训练过程。

## 核心贡献
为 Transformer 设计深度感知的初始化方案，证明正确初始化可替代 LayerNorm 和 warmup。
