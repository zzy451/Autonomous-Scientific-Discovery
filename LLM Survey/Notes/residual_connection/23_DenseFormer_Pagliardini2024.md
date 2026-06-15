# DenseFormer: Enhancing Information Flow in Transformers via Depth Weighted Average

**论文信息**: Pagliardini, M., Mohtashami, A., Fleuret, F., Jaggi, M. (2024)
**arXiv**: 2402.02622 | **会议**: NeurIPS 2024
**分类**: Depth (跨层稠密连接)

## 核心思想
DenseFormer 借鉴 DenseNet 的设计思想，将标准 Transformer 的逐层加法残差替换为 **Depth-Weighted Average (DWA)**：每一层的输入不再只是上一层的输出，而是所有前序层输出的加权平均。

## 数学公式
标准残差: x_{l+1} = x_l + F(x_l)
DWA: x_{l+1} = sum_{i=0}^{l} w_{l,i} * h_i, 其中 h_i 是第 i 层的输出
- w_{l,i} 是可学习的标量权重，控制第 l+1 层对第 i 层输出的依赖程度

## 关键机制
- **全局信息聚合**: 每层可以直接访问所有前序层的"原始"输出，避免信息在逐层传递中被稀释
- **可学习标量权重**: 不需要复杂的注意力机制，仅使用标量权重进行线性组合
- **DenseNet 精神**: 类似 DenseNet 的密集连接模式，但用加权平均替代拼接
- **数据效率**: DenseFormer 模型在相同数据量下表现更好

## 与其他方法对比
| 方法 | 聚合方式 | 权重参数 | 计算开销 |
|------|----------|----------|----------|
| 标准残差 | 仅前一层加法 | 无(固定+1) | 无 |
| DenseFormer (DWA) | 所有前层加权平均 | O(L^2) 标量 | 低 |
| MUDDFormer | 动态多路稠密 | 输入依赖 | 中 |
| DCA | 跨层注意力 | GRN 模块 | 中 |

## 实验结果
- 在 perplexity 上显著优于标准 Transformer
- 提供了更好的 速度-内存-性能 权衡
- 数据利用效率更高

## 与综述的关联
属于 **Depth** 维度。是"跨层稠密连接"的经典工作，建立了 DenseNet 思想在 Transformer 中的桥梁。是 MUDDFormer 的重要前驱工作。

## 核心贡献
用可学习的深度加权平均替代简单加法残差，让每层能直接聚合所有前序层的信息。
