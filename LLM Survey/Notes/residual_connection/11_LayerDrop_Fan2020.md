# Reducing Transformer Depth on Demand with Structured Dropout (LayerDrop)

**论文信息**: Fan, A., Grave, E., Joulin, A. (2020)
**arXiv**: 1909.11556 | **会议**: ICLR 2020
**分类**: Depth (自适应深度/层跳过)

## 核心思想
在训练时随机丢弃整层 Transformer 层 (Structured Dropout / Stochastic Depth)，使模型学会在缺少某些层时仍保持性能。推理时可按需裁剪深度。

## 关键机制
- **训练**: 每个 Transformer 层以概率 p 被丢弃（残差连接直接跳过该层）
- **推理**: 可以裁剪到任意较浅深度，无需重新微调
- 本质上是对残差连接的**随机稀疏化**

## 与残差连接的关系
LayerDrop 的成功**依赖于**残差连接：
- 丢弃一层时，该位置退化为 x_{l+1} = x_l（恒等映射）
- 模型学会不过度依赖任何单一层
- 证明了残差连接提供的冗余性和鲁棒性

## 实验结果
- 20 层编码器训练后可裁剪为更浅模型
- 性能与从头训练浅模型相当甚至更好
- 正则化效果：防止过拟合

## 与综述的关联
属于 **Depth** 维度。LayerDrop 从"训练技巧"角度揭示了残差连接的深层含义：
- 残差连接 = 每层可选的恒等旁路
- 深度可以是弹性的，不是固定的
- 为 Mixture-of-Depths 和 Early Exit 等后续工作奠定基础

## 核心贡献
首次证明残差连接允许 Transformer 实现"深度弹性"，训练和推理时可使用不同深度。
