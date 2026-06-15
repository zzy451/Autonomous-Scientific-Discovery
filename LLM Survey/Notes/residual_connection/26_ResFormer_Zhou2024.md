# Value Residual Learning (ResFormer / SVFormer)

**论文信息**: Zhou, Z., Wu, T., Jiang, Z., Obeid, F., Lan, Z. (2024)
**arXiv**: 2410.17897 | **会议**: ACL 2025
**分类**: Depth (值残差连接)

## 核心思想
提出在注意力机制的 Value (V) 向量上添加跨层残差连接，解决深层 Transformer 中的"注意力集中"问题（attention concentration）。核心思想是将第一层的 V 矩阵残差传递到所有后续层。

## 数学公式
标准 Attention: U_n = A_n * V_n
ResFormer: U_n = (1/2) * A_n * (V_n + V_1)

其中:
- A_n: 第 n 层的注意力权重矩阵
- V_n: 第 n 层计算的 Value 矩阵
- V_1: 第 1 层的 Value 矩阵（跨层残差）

SVFormer (Single-layer Value):
- 所有层共享第一层的 Value 嵌入: U_n = A_n * V_1
- KV cache 减少约 50%

## 关键机制
- **V 残差而非 hidden state 残差**: 创新点在于残差连接不是在主残差流上，而是专门在注意力机制内部的 V 上
- **近似跨层注意力**: 从数学上证明了 V 残差近似于跨层注意力
- **注意力集中问题**: 深层 Transformer 的注意力模式趋于集中，V 残差帮助保持早期的 token 级别信息
- **SVFormer 变体**: 极端情况下所有层共享 V_1，大幅减少 KV cache

## 实验结果
- 等效验证损失下减少约 16% 参数
- SVFormer 将 KV cache 减少近 50%
- 在 ACL 2025 发表

## 与其他方法对比
| 方法 | 残差位置 | 信息来源 | KV cache 影响 |
|------|----------|----------|---------------|
| 标准残差 | hidden state | 前一层 | 无 |
| DenseFormer/DCA | hidden state | 所有前层 | 无 |
| ResFormer | Value 向量 | 第一层 V | 无 |
| SVFormer | Value 向量 | 第一层 V (共享) | 减少 ~50% |

## 与综述的关联
属于 **Depth** 维度。独特之处在于残差连接不在传统的 hidden state 残差流上，而是在注意力机制内部的 Value 路径上。为 KV cache 优化提供了新视角。

## 核心贡献
在注意力机制的 Value 向量上引入跨层残差，同时解决注意力集中问题和 KV cache 效率问题。
