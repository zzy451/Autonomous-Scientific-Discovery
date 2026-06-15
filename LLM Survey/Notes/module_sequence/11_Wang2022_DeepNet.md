# DeepNet: Scaling Transformers to 1,000 Layers

## 基本信息
- **作者**: Hongyu Wang, Shuming Ma, Li Dong, Shaohan Huang, Dongdong Zhang, Furu Wei
- **年份**: 2022 (arXiv: 2203.00555)
- **机构**: Microsoft Research
- **关键词**: DeepNorm, 超深Transformer, 残差缩放, Post-LN, 训练稳定性

## 核心贡献（Module Sequence 维度）
本文提出 DeepNorm，一种新的归一化和初始化方案，成功将 Transformer 扩展到**1000层**。在 Module Sequence 维度上，这是 Post-LN 深度扩展的终极解决方案。

### 1. 问题定义
- Post-LN Transformer 在深度增加时训练极不稳定
- 模型更新（model update）随深度指数级增长
- 现有方法（Pre-LN, ADMIN）只能部分缓解，或牺牲性能
- 目标：在保持 Post-LN 性能优势的同时，实现极深模型训练

### 2. DeepNorm 机制
**修改残差连接的缩放方式：**
$$x_{l+1} = \text{LN}(\alpha \cdot x_l + G_l(x_l, \theta_l))$$

- $\alpha > 1$ 是一个与模型深度相关的常数，用于放大残差连接
- $G_l$ 是第 $l$ 层的子层函数（Attention 或 FFN）
- 配合特定的初始化方案：将子层参数按 $\beta$ 缩放（$\beta < 1$）

### 3. 理论保证
- **证明了模型更新的上界是常数**，不随深度增长
- 结合了 Post-LN 的良好性能和 Pre-LN 的训练稳定性
- 理论推导了 $\alpha$ 和 $\beta$ 的最优值：
  - 对于 encoder-decoder: $\alpha = (2N)^{1/4}$, $\beta = (8N)^{-1/4}$（$N$ 为层数）
  - 对于 decoder-only: $\alpha = (2N)^{1/4}$, $\beta = (8N)^{-1/4}$

### 4. 实验成就
- 成功训练了 **1000 层** Transformer（2500 个子层）
- 200 层 3.2B 参数模型在多语言基准上**超越** 48 层 12B 参数的 SOTA 模型
- 说明"更深"可以比"更宽"更高效
- 被 GLM-130B 等大模型采用

### 5. 实现简洁性
- 仅需修改残差连接的缩放因子和初始化
- 代码改动极少（几行代码）
- 无需引入额外的可学习参数

## 与综述的关联
- **Post-LN 深度扩展的集大成者**：证明 Post-LN 配合正确的缩放可以无限深
- 与 ADMIN (Liu et al. 2020) 形成互补：ADMIN 关注初始化，DeepNorm 关注残差缩放
- 与 Pre-LN 的比较：DeepNorm 结合两者优势，是 Module Sequence 设计的重要进展
- 理论贡献：提供了分析 Module Sequence 对训练动态影响的数学框架
- 后续影响：启发了更多关于残差连接缩放的研究

## 关键公式
- DeepNorm: $x_{l+1} = \text{LN}(\alpha \cdot x_l + G_l(x_l, \theta_l))$
- 初始化: $\theta_l \sim \mathcal{N}(0, \beta^2)$
- 缩放因子: $\alpha = (2N)^{1/4}$, $\beta = (8N)^{-1/4}$

## 局限性
- 理论分析基于初始化时刻，对训练过程中的动态分析有限
- 超参数 $\alpha$, $\beta$ 的最优值在实际应用中可能需要微调
- 对于 decoder-only LLM 的验证相对有限（主要在 encoder-decoder 上实验）
- 深度增加的收益在某个点后会递减
