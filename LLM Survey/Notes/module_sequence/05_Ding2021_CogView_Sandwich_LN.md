# CogView: Mastering Text-to-Image Generation via Transformers (Sandwich LayerNorm)

## 基本信息
- **作者**: Ming Ding, Zhuoyi Yang, Wenyi Hong, Wendi Zheng, et al.
- **年份**: 2021 (NeurIPS 2021)
- **arXiv**: 2105.13290
- **关键词**: Sandwich LayerNorm, 训练稳定性, FP16, 文本到图像生成

## 核心贡献（Module Sequence 维度）
提出 Sandwich LayerNorm (Sandwich-LN)，一种在残差分支内额外添加 LayerNorm 的技术。

### 1. 动机
- 训练超大 Transformer（4B-8.3B 参数）时遇到 NaN loss
- 标准 Pre-LN 不足以解决 FP16 训练中的数值爆炸
- 需要更强的激活值控制机制

### 2. Sandwich-LN 机制
- 在标准 Pre-LN 的基础上，在每个残差分支的**末端**再加一个 LayerNorm
- 结构: `x_out = x + LN(Sublayer(LN(x)))`
- 两个 LN 像"三明治"一样夹住子层

### 3. 效果
- 限制了激活值逐层累积爆炸
- 确保每层输入值保持在合理范围内
- 使 FP16 训练大规模模型成为可能
- 对小模型（~500M）收敛速度影响可忽略

### 4. 配套技术
- PB-Relax (Precision Bottleneck Relaxation): 防止注意力机制中的溢出
- 与 Sandwich-LN 协同工作

## 与综述的关联
- 展示了 Module Sequence 中归一化位置的又一种变体
- 与 NormFormer 的"额外归一化"思路类似
- 后续 Gemma 2 采用了类似的"前后双重归一化"策略
- 证明在极端训练条件下（FP16, 超大模型），标准 Pre-Norm 不够用
