# DeepNet: Scaling Transformers to 1,000 Layers

**论文信息**: Wang, H., Ma, S., Dong, L., Huang, S., Zhang, D., Wei, F. (2022)
**arXiv**: 2203.00555 | **机构**: Microsoft Research
**分类**: Control (残差缩放 + 初始化)

## 核心思想
DeepNorm 通过修改残差连接的缩放因子和权重初始化，解决超深 Transformer 的训练不稳定问题（"爆炸模型更新"）。

## 数学公式
标准残差: x_{l+1} = LN(x_l + f(x_l))  (Post-LN)
DeepNorm:  x_{l+1} = LN(alpha * x_l + f(x_l))

其中:
- alpha 为残差连接的常数缩放因子（依赖于架构深度）
- 残差分支内的权重 theta_l 按常数 beta 缩放初始化
- alpha 和 beta 的取值由理论推导得出，保证模型更新有界

## 关键创新
1. **理论保证**: 证明选择合适的 alpha 和 beta 后，模型更新量被常数约束
2. **结合 Pre-LN 和 Post-LN 优势**: Post-LN 的高性能 + Pre-LN 的训练稳定性
3. **极端深度**: 成功训练 **1000 层** (2500 子层) Transformer

## 实验结果
- 200层 3.2B 参数 DeepNet 在 7482 个翻译方向上超过 48层 12B 参数 SOTA 模型 **5 BLEU**
- 深度比此前最深 Transformer 增大一个数量级

## 与综述的关联
属于 **Control** 维度的重要工作。代表了残差缩放控制的成熟阶段：
- 不再是简单的零初始化（ReZero），而是基于深度的精确数学缩放
- 为工业级超深 Transformer 提供了可靠方案

## 核心贡献
首次实现 1000 层 Transformer 的稳定训练，建立了深度与残差缩放的理论联系。
