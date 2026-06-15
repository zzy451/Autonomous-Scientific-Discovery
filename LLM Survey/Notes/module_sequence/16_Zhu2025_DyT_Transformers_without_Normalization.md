# Transformers without Normalization (Dynamic Tanh / DyT)

## 基本信息
- **作者**: Jiachen Zhu, Xinlei Chen, Kaiming He, Yann LeCun, Zhuang Liu
- **年份**: 2025 (CVPR 2025)
- **arXiv**: 2503.10622
- **机构**: Meta AI (FAIR), MIT, NYU
- **关键词**: Dynamic Tanh, DyT, 无归一化, LayerNorm替代, 激活压缩

## 核心贡献（Module Sequence 维度）
本文提出 Dynamic Tanh (DyT)，一种简洁的**逐元素操作**，可以完全替代 Transformer 中的归一化层（LayerNorm/RMSNorm）。挑战了"Transformer 必须有归一化层"的基本假设。

### 1. 关键观察：归一化层的实际行为
- 在已训练好的 Transformer 中，LayerNorm 层的输入-输出映射呈现**S 形曲线**
- 这个 S 形类似于 $\tanh$ 函数
- LayerNorm 的实际作用：**压缩极端值** + **重新缩放/偏移**
- 这并不需要计算批次/层的统计量（均值、方差）

### 2. DyT 机制
$$\text{DyT}(x) = \gamma \cdot \tanh(\alpha \cdot x) + \beta$$

- $\alpha$: 可学习标量参数，控制输入缩放（决定 tanh 的"陡峭程度"）
- $\gamma$: 可学习的逐通道缩放参数
- $\beta$: 可学习的逐通道偏移参数
- 整体是一个**逐元素操作**，无需计算统计量

### 3. DyT vs LayerNorm 的对比
| 属性 | LayerNorm | DyT |
|------|-----------|-----|
| 操作类型 | 需要全局统计量 | 逐元素操作 |
| 计算复杂度 | $O(d)$ 规约操作 | $O(1)$ 逐元素 |
| 跨样本依赖 | 无（不像 BN） | 无 |
| 参数量 | $2d$ ($\gamma, \beta$) | $2d + 1$ ($\gamma, \beta, \alpha$) |
| 核心机制 | 均值归零+方差归一 | 激活值压缩 |

### 4. 实验验证（跨领域）
- **视觉**: 分类 (ViT)、自监督学习 (MAE, DINO)、扩散模型 (DiT)
- **语言**: 语言建模 (GPT-2 级别)
- **语音**: 语音识别
- 在所有任务上 DyT 的表现与 LayerNorm/RMSNorm **持平或更优**
- 通常**不需要大量超参数调优**即可替换

## 与综述的关联
- **Module Sequence 中归一化组件的根本性挑战**：
  - 从 Post-LN → Pre-LN → RMSNorm → DyT，归一化一直在简化
  - DyT 代表了"归一化不是必需的"这一极端立场
- 与 De & Smith 2020 的理论互补：
  - De & Smith 证明 BN 的主要作用是缩放残差分支
  - DyT 证明归一化的主要作用是压缩极端激活值
  - 两者都表明：归一化的**副作用**才是其真正价值
- 与 Noci et al. 2023 (Shaped Transformer) 的关系：
  - 两者都试图构建"无归一化"的 Transformer
  - Shaped Transformer 从注意力机制入手，DyT 从归一化替代入手
- **对 Module Sequence 设计的启示**：标准 Transformer 块中的 LN 可能可以用更简单的操作替代

## 关键公式
- DyT: $\text{DyT}(x) = \gamma \cdot \tanh(\alpha \cdot x) + \beta$
- 对比 LayerNorm: $\text{LN}(x) = \gamma \cdot \frac{x - \mu}{\sigma} + \beta$
- 对比 RMSNorm: $\text{RMSNorm}(x) = \gamma \cdot \frac{x}{\text{RMS}(x)}$

## 局限性
- 在超大规模 LLM（100B+）上的验证有限
- tanh 的饱和区域可能在某些场景下导致梯度消失
- $\alpha$ 的初始化可能需要根据模型深度调整
- 目前主流训练框架（Megatron, DeepSpeed）对 DyT 的支持和优化不如 LayerNorm 成熟
- 是否能在长时间训练（数万亿 token）中保持稳定尚需验证
