# Mix-LN: Mixing Pre-LN and Post-LN for Better Training Stability

## 基本信息
- **作者**: Pixeli Chen et al.
- **年份**: 2024
- **arXiv**: 2412.13795
- **关键词**: Mix-LN, 混合归一化, 梯度分布均衡

## 核心贡献（Module Sequence 维度）
提出混合使用 Pre-LN 和 Post-LN 的策略，解决深层 Transformer 的梯度不均衡问题。

### 1. 问题分析
- **Pre-LN 的局限**：深层的梯度范数显著下降，使深层变得"无效"
- **Post-LN 的局限**：浅层的梯度消失，加上训练不稳定
- 两种方法各有缺陷，都无法保证所有层均匀训练

### 2. Mix-LN 方案
- **浅层使用 Post-LN**（稳定性较好，浅层的梯度问题较轻）
- **深层使用 Pre-LN**（保证深层的梯度流通）
- 关键超参数 $\alpha = 0.25$：前 25% 的层用 Post-LN，后 75% 用 Pre-LN

### 3. 效果
- 梯度范数在整个网络中更均匀
- 浅层和深层都能有效参与训练
- 在多种模型规模上表现优异
- 实现简单，只需修改不同层的归一化位置

### 4. 与其他方法的比较
- 比纯 Pre-LN 和纯 Post-LN 都更好
- 与 NormFormer 的"额外归一化"思路不同——Mix-LN 不增加归一化层，而是混合两种位置
- 与 MAGNETO/Sub-LN 正交——可以结合使用

## 与综述的关联
- 代表了 Module Sequence 研究的**最新趋势**：混合策略
- 打破了"整个网络用同一种归一化位置"的假设
- 是 Pre-Norm vs Post-Norm 辩论的最新解答：**不是非此即彼，而是混合使用**
- 2024年末的工作，反映了该领域的前沿方向
