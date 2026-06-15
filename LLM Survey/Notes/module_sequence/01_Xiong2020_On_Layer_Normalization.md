# On Layer Normalization in the Transformer Architecture

## 基本信息
- **作者**: Ruibin Xiong, Yunchang Yang, Angela He, Shishir Kolathaya, et al.
- **年份**: 2020 (ICML 2020)
- **arXiv**: 2002.04745
- **关键词**: Pre-Norm, Post-Norm, Layer Normalization, 梯度分析

## 核心贡献（Module Sequence 维度）
本文是 Pre-Norm vs Post-Norm 理论分析的**奠基性工作**，用均场理论 (mean-field theory) 严格分析了 LayerNorm 位置对梯度行为的影响。

### 1. Post-Norm 的问题
- 原始 Transformer 使用 Post-Norm: `x_out = LayerNorm(x + Sublayer(x))`
- 在初始化时，靠近输出层的参数梯度非常大
- 这导致**必须使用 learning rate warmup** 才能稳定训练
- 梯度在反向传播时被 LayerNorm 层"阻断"，没有干净的恒等路径

### 2. Pre-Norm 的解决方案
- Pre-Norm 将 LayerNorm 移到子层之前: `x_out = x + Sublayer(LayerNorm(x))`
- 残差路径保持"干净"——梯度可以通过恒等连接直接回传
- 在初始化时梯度行为良好
- **不需要 warmup** 即可稳定训练

### 3. 理论证明
- 通过均场理论证明 Pre-Norm 在初始化时的梯度范数是有界的
- Post-Norm 的梯度范数随层数增加会快速增长或消失
- 这为后续所有 Pre-Norm 架构（GPT-2, LLaMA, etc.）提供了理论依据

## 与综述的关联
- **Module Sequence 核心论文**：定义了 Pre-Norm vs Post-Norm 的理论基础
- 解释了为什么现代 LLM 几乎全部采用 Pre-Norm（或其变体 RMSNorm）
- 后续工作（DeepNet, MAGNETO, Mix-LN）都基于此文的分析框架

## 关键公式
- Post-Norm: $y = \text{LN}(x + F(x))$
- Pre-Norm: $y = x + F(\text{LN}(x))$

## 局限性
- 分析主要基于初始化时刻，对训练过程中的动态变化分析有限
- 没有讨论 Pre-Norm 可能导致的"表示坍缩"问题（后续研究指出）
