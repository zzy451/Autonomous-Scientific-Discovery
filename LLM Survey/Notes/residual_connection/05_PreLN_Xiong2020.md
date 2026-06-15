# On Layer Normalization in the Transformer Architecture

**论文信息**: Xiong, R., Yang, Y., He, J., Zheng, K., Zheng, S., Xing, C., Zhang, H., Lan, Y., Wang, L., Liu, T.-Y. (2020)
**arXiv**: 2002.04745 | **会议**: ICML 2020
**分类**: Control (残差连接中的归一化位置)

## 核心思想
系统性分析 Pre-LN vs Post-LN 对 Transformer 训练稳定性的影响。这是理解残差连接结构最重要的基础论文之一。

## 两种架构
**Post-LN** (原始 Transformer):
  Output = LayerNorm(x + SubLayer(x))
  - 归一化在残差加法之后
  - 梯度需穿过归一化层，深层不稳定
  - 需要 warm-up 学习率

**Pre-LN** (现代标准):
  Output = x + SubLayer(LayerNorm(x))
  - 归一化在子层之前
  - 残差路径为"干净"的恒等映射
  - 梯度直接流动，训练稳定

## 关键理论贡献
1. 证明 Post-LN 初始化时梯度在深层趋向零
2. 证明 Pre-LN 保持梯度稳定，不需要 warm-up
3. Pre-LN 的代价：可能导致"表示坍缩"（深层特征过于相似）

## 与综述的关联
属于 **Control** 维度的基础理论工作。LayerNorm 位置本质上决定了残差连接的信息流结构：
- Pre-LN: 残差路径为纯恒等映射 -> 梯度流优先
- Post-LN: 残差路径经过归一化 -> 表示多样性优先
后续的 ResiDual、DeepNorm 等工作都是在解决这两者的权衡

## 核心贡献
为 Transformer 残差连接设计提供了理论基础，解释了 Pre-LN 为何成为 LLM 的事实标准。
