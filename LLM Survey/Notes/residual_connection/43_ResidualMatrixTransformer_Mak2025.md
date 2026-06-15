# Residual Matrix Transformers: Scaling the Size of the Residual Stream
**作者**: Ethan Mak, Jeffrey Flanigan | **年份**: 2025 (ICML 2025) | **arxiv**: 2506.22696

## 0. 摘要翻译
Transformer 使用"残差流"(residual stream) 作为各层存取信息的记忆总线。然而，残差流的维度与模型隐藏维度绑定，限制了其信息容量的独立扩展。本文提出 Residual Matrix Transformer (RMT)，将残差流从向量替换为外积记忆矩阵 (outer product memory matrix)，使残差流的大小可以独立于模型整体计算量进行扩展。理论分析表明 RMT 具有更高效的残差流扩展能力和更优的方差传播特性。实验表明 RMT 在相同计算预算下达到与标准 Transformer 相当的性能，同时残差流容量显著增大。

## 1. 方法动机
- 标准 Transformer 的残差流是一个 $d$-维向量，其信息容量受限于隐藏维度 $d$
- 增大 $d$ 会同时增加所有层的计算量（注意力和 FFN），导致扩展效率低下
- 残差流本质上是一个"记忆总线"(Elhage et al., 2021)，其容量应该可以独立扩展
- 需要一种机制让残差流容量与计算量解耦

## 2. 方法设计
- **核心思想**: 将残差流从向量 $\mathbf{h} \in \mathbb{R}^d$ 替换为矩阵 $\mathbf{M} \in \mathbb{R}^{d_r \times d_r}$
- **外积记忆矩阵**: 借鉴 Kohonen (1972) 的联想记忆思想，用外积形式存取信息
- **存储操作**: 各子层通过外积 $\mathbf{M} \leftarrow \mathbf{M} + \mathbf{k}\mathbf{v}^T$ 向矩阵写入信息
- **检索操作**: 通过矩阵-向量乘法 $\mathbf{o} = \mathbf{M}\mathbf{q}$ 从矩阵读取信息
- **独立扩展**: $d_r$ 可以独立于注意力/FFN 的维度进行调整
- **方差传播**: 理论证明 RMT 的方差传播比标准残差连接更稳定

## 3. 对比
| 特性 | 标准 Transformer | RMT |
|------|-----------------|-----|
| 残差流形状 | 向量 $\mathbb{R}^d$ | 矩阵 $\mathbb{R}^{d_r \times d_r}$ |
| 残差流容量 | $O(d)$ | $O(d_r^2)$ |
| 容量-计算耦合 | 绑定 | 解耦 |
| 存取机制 | 加法 | 外积写入 / 矩阵乘法读取 |
| 方差传播 | 随深度累积 | 更稳定 |

## 4. 实验
- 在语言建模任务上验证，RMT 在相同 FLOPs 预算下达到与标准 Transformer 相当的困惑度
- 残差流容量可以独立扩展而不增加每层计算量
- 方差传播实验验证了理论分析的预测
- 代码已开源

## 5. 总结
a) 一句话: RMT 将 Transformer 的残差流从向量升级为外积记忆矩阵，实现残差流容量与计算量的解耦扩展。
b) 速记 pipeline: `输入 → [各层通过外积写入/矩阵乘法读取与残差矩阵交互] → 输出`; 残差流: 向量→矩阵, 容量 $O(d^2)$, 存取解耦。
