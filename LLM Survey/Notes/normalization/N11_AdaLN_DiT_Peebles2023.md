# Scalable Diffusion Models with Transformers (DiT)
**作者**: William Peebles, Saining Xie | **年份**: 2023 | **arxiv**: 2212.09748

## 0. 摘要翻译

本文探索了一类基于 Transformer 架构的扩散模型——Diffusion Transformers (DiTs)。通过将标准扩散模型中的 U-Net 骨干替换为在隐空间 (latent space) 上操作的 Transformer，我们分析了不同设计选择对图像生成质量的影响。其中，**Adaptive Layer Normalization (adaLN)** 被发现是最有效的条件化机制。我们进一步提出 adaLN-Zero 变体，通过零初始化使每个 DiT block 在初始化时等效为恒等函数。DiT-XL/2 模型在 class-conditional ImageNet 256x256 和 512x512 上达到了 SOTA 的 FID 分数。

## 1. 方法动机

### a) 为什么
扩散模型需要将条件信号（时间步 $t$、类别标签 $c$）注入网络。在 U-Net 架构中通常使用 cross-attention 或 FiLM 等方式。当骨干网络切换为 Transformer 时，需要寻找最高效的条件注入方式。

### b) 痛点
- **Cross-attention 计算量大**: 为条件信号添加专门的 cross-attention 层增加了大量参数和计算
- **In-context conditioning 效果一般**: 将条件 token 与图像 token 拼接并通过自注意力处理，效果不如预期
- **标准 LayerNorm 是"静态"的**: 其 $\gamma, \beta$ 对所有输入共享，无法根据条件信号动态调整

### c) 假设
归一化层可以作为轻量级的条件信号注入点：通过让条件信号动态生成归一化层的仿射参数 $\gamma, \beta$，以最小的计算开销实现高效条件化。

## 2. 方法设计

### a) Pipeline
1. 将条件信号 $t$（时间步）和 $c$（类别标签）分别嵌入并相加
2. 通过 MLP 从条件嵌入回归出 $\gamma, \beta, \alpha$ 参数
3. 在每个 DiT block 中用回归出的 $\gamma, \beta$ 替换 LayerNorm 的固定参数
4. 使用 $\alpha$ 在残差连接前对子层输出进行缩放

### b) 模块

**标准 LayerNorm（静态参数）**:
$$y = \gamma \cdot \frac{x - \mu}{\sqrt{\sigma^2 + \epsilon}} + \beta$$

**adaLN（动态参数）**:
$$\gamma, \beta = \text{MLP}(\text{embed}(t) + \text{embed}(c))$$
$$y = \gamma \cdot \frac{x - \mu}{\sqrt{\sigma^2 + \epsilon}} + \beta$$

**adaLN-Zero（动态参数 + 零初始化门控）**:
$$\gamma, \beta, \alpha = \text{MLP}(\text{embed}(t) + \text{embed}(c))$$
$$\text{output} = x + \alpha \cdot \text{SubLayer}(\gamma \cdot \hat{x} + \beta)$$
- $\alpha$ 的 MLP 输出层初始化为零向量
- 初始状态下每个 block 等效于恒等函数

### c) 公式
- 条件嵌入: $\mathbf{c} = \text{embed}(t) + \text{embed}(c)$
- 参数回归: $[\gamma_1, \beta_1, \alpha_1, \gamma_2, \beta_2, \alpha_2] = \text{MLP}(\mathbf{c})$（每个 block 6 组参数：注意力层和 FFN 层各需 $\gamma, \beta, \alpha$）
- 所有 block 共享同一个 MLP（按层分 block，但 MLP 结构共享）

## 3. 对比

| 条件化方法 | 额外参数 | 计算开销 | FID (ImageNet 256) |
|-----------|---------|---------|-------------------|
| In-context conditioning | 少 | 低 | 较高（较差） |
| Cross-attention | 多 | 高 | 中等 |
| **adaLN** | **少** | **最低** | **较低（较好）** |
| **adaLN-Zero** | **少** | **最低** | **最低（最好）** |

**与其他归一化条件化的对比**:
| 方法 | 年份 | 领域 | 条件化方式 |
|------|------|------|-----------|
| FiLM | 2018 | 视觉QA | $\gamma \cdot x + \beta$ |
| AdaNorm (Xu 2019) | 2019 | NLP | 条件化 LayerNorm 的 scale |
| **adaLN (DiT)** | 2023 | 扩散模型 | 条件化 $\gamma, \beta, \alpha$ |

## 4. 实验

- **ImageNet 256x256**: DiT-XL/2 + adaLN-Zero 达到 FID=2.27（当时 SOTA）
- **ImageNet 512x512**: 同样达到 SOTA
- **缩放律**: DiT 遵循清晰的缩放律——更大的模型和更多的计算稳定提升 FID
- **设计消融**: adaLN-Zero 显著优于 cross-attention、in-context 等其他条件化方式
- **后续影响**: Stable Diffusion 3 (MMDiT), Flux, Sora 等均采用 DiT + adaLN 架构

## 5. 总结

### a) 一句话
DiT 中的 adaLN/adaLN-Zero 展示了归一化层可以作为轻量级的条件信号注入载体，通过动态生成 $\gamma, \beta, \alpha$ 参数实现高效条件化，已成为扩散 Transformer 的标准设计。

### b) 速记 pipeline
```
条件信号 (t, c) → embed → MLP → (γ, β, α)
                                    ↓
输入 x → LN(用动态 γ, β) → SubLayer → × α → + x → 输出
（adaLN-Zero: α 初始化为 0，初始 block = 恒等函数）
```

---
**阅读日期**: 2026-04-06
