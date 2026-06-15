# N-08: DeepNet / DeepNorm (Wang et al. 2022)

> **论文**: DeepNet: Scaling Transformers to 1,000 Layers
> **作者**: Hongyu Wang, Shuming Ma, Li Dong, Shaohan Huang, Dongdong Zhang, Furu Wei
> **发表**: IEEE TPAMI 2024 (原 arXiv 2022) | arXiv:2203.00555
> **关键词**: DeepNorm, 极深 Transformer, 训练稳定性, 初始化

---

## 核心思想

提出 **DeepNorm**，一种修改残差连接的归一化方法，结合理论推导的初始化策略，成功将 Transformer 缩放到 **1000 层** (2500 个子层)。

## DeepNorm 方法

### 残差连接修改
标准 Post-LN:
$$x_{l+1} = \text{LayerNorm}(x_l + f(x_l))$$

DeepNorm:
$$x_{l+1} = \text{LayerNorm}(\alpha \cdot x_l + f(x_l))$$

其中 $\alpha > 1$ 是一个与深度相关的常数，增大残差路径的权重。

### 初始化策略
- 子层参数使用 $\beta$ 缩放的 Xavier 初始化
- $\alpha$ 和 $\beta$ 的值由理论推导确定，保证模型更新有界

### 理论保证
- 证明了 DeepNorm 使得模型更新在训练初始阶段有界
- 结合了 Post-LN 的**性能优势**和 Pre-LN 的**训练稳定性**

## 关键实验结果

- 成功训练 **1000 层** Transformer (前所未有)
- 200 层 3.2B 参数的 DeepNet 在多语言翻译上超过 48 层 12B 参数的 SOTA 模型 **5 BLEU 点**
- 证明深度是一个高效的缩放维度

## Post-LN vs Pre-LN vs DeepNorm

| 特性 | Post-LN | Pre-LN | DeepNorm |
|------|---------|--------|----------|
| 稳定性 | 差 | 好 | 好 |
| 最终性能 | 高 | 中等 | 高 |
| 可缩放深度 | ~12层 | ~100层 | ~1000层 |
| warmup 需求 | 必需 | 可选 | 可选 |

## 与 MAGNETO/Sub-LN 的关系

DeepNorm 和 MAGNETO 来自同一研究组 (微软):
- **DeepNorm** (2022a): 通过修改残差连接 + 初始化来稳定训练
- **MAGNETO/Sub-LN** (2022b): 通过在子层内部放置 LN 来稳定训练
- 两者共享理论基础，MAGNETO 使用 DeepNet 的初始化策略

## 在综述中的定位

DeepNorm 是"深度缩放"方向的代表性工作，展示了归一化设计与初始化策略的耦合如何突破深度限制。与 Pre-LN vs Post-LN 的讨论紧密相关。

---

**阅读日期**: 2026-04-05
