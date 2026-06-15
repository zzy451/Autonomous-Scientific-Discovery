# Transformers without Tears: Improving the Normalization of Self-Attention
**作者**: Toan Q. Nguyen, Julian Salazar | **年份**: 2019 | **arxiv**: 1910.05895

## 0. 摘要翻译

我们提出三种互补技术来改善 Transformer 的归一化和训练稳定性。(1) **ScaleNorm**: 用 L2 归一化加单一可学习标量替代 LayerNorm，参数量从 $2d$ 降至 1；(2) **FixNorm**: 对词嵌入向量强制固定 L2 范数，解决权重共享场景下的嵌入范数失控问题；(3) **PreNorm + SmallInit**: 使用 Pre-Norm 配合小初始化值消除对 warmup 的依赖。三种技术结合后在低资源翻译任务上平均提升 1.1 BLEU，且无需 warmup。

## 1. 方法动机

### a) 为什么
LayerNorm 中的均值减法和逐元素仿射参数 ($\gamma, \beta$) 是否必要？如果隐层向量的方向（而非大小和偏移）才是信息的核心载体，那么更简单的 L2 归一化可能就足够了。

### b) 痛点
- **LayerNorm 参数过多**: $2d$ 个可学习参数 ($\gamma, \beta$)，在小模型中比例可观
- **嵌入范数失控**: 使用权重共享 (weight tying) 时，嵌入向量的范数在训练中不受控制，影响 softmax 温度
- **warmup 的脆弱性**: Transformer 训练对 warmup 步数敏感，选择不当导致训练失败
- **归一化的信息几何**: 从信息几何角度，方向比幅度更重要

### c) 假设
隐层向量的**方向**承载了主要信息，**范数**只是一个需要被控制的噪声源。L2 归一化直接将向量映射到超球面，用单一标量 $g$ 控制全局尺度就足够了。

## 2. 方法设计

### a) Pipeline
1. 将 LayerNorm 替换为 ScaleNorm（L2 归一化 + 标量 $g$）
2. 对词嵌入应用 FixNorm（固定 L2 范数）
3. 使用 PreNorm 结构 + SmallInit（小初始化）
4. 移除 warmup

### b) 模块

**ScaleNorm**:
$$\text{ScaleNorm}(x) = g \cdot \frac{x}{\|x\|_2}$$
- $g$: **单一可学习标量**（全局 1 个参数，所有维度共享）
- 将向量映射到半径为 $g$ 的超球面

**FixNorm**:
$$\text{FixNorm}(\mathbf{e}) = c \cdot \frac{\mathbf{e}}{\|\mathbf{e}\|_2}$$
- $c$: **预设固定常数**（如 $c = \sqrt{d}$）
- 应用于词嵌入矩阵的行向量（每个词的嵌入）
- 解决权重共享时嵌入范数的漂移问题

**SmallInit**: 权重从 $\text{Uniform}(-0.01, 0.01)$ 初始化

### c) 公式

**与各归一化方法的参数量对比**:
| 方法 | 操作 | 可学习参数量 |
|------|------|------------|
| LayerNorm | $\gamma \cdot \frac{x-\mu}{\sigma} + \beta$ | $2d$ |
| RMSNorm | $\gamma \cdot \frac{x}{\text{RMS}(x)}$ | $d$ |
| **ScaleNorm** | $g \cdot \frac{x}{\|x\|_2}$ | **1** |

**ScaleNorm 与 RMSNorm 的数学关系**:
- RMSNorm: 除以 $\sqrt{\frac{1}{d}\sum x_i^2}$，即 $\frac{\|x\|_2}{\sqrt{d}}$
- ScaleNorm: 除以 $\|x\|_2$
- 差别仅在 $\sqrt{d}$ 常数因子和参数化方式（逐元素 $\gamma$ vs 全局 $g$）

## 3. 对比

| 特性 | LayerNorm | RMSNorm | ScaleNorm |
|------|-----------|---------|-----------|
| 减均值 | 有 | 无 | 无 |
| 归一化方式 | 除标准差 | 除 RMS | 除 L2 范数 |
| 可学习参数 | $2d$ | $d$ | **1** |
| 输出空间 | 无约束 | 无约束 | 超球面 |
| 简洁度 | 中 | 高 | **最高** |
| 性能 (低资源) | 基线 | 匹配 | **+1.1 BLEU** |
| LLM 主流采用 | GPT-2/3 | LLaMA 等 | **未广泛采用** |

## 4. 实验

- **低资源翻译** (5 个 IWSLT 语言对): ScaleNorm + FixNorm + PreNorm 平均提升 **+1.1 BLEU**
- **IWSLT15 En-Vi**: 达到 32.8 BLEU
- **无 warmup 训练**: 结合 SmallInit 后可以完全去掉 warmup
- **高资源翻译** (WMT14 En-De): ScaleNorm 保持竞争力，但 PreNorm 在大模型上有时退化
- **嵌入分析**: FixNorm 有效防止了权重共享场景下嵌入范数的漂移
- **超球面可视化**: ScaleNorm 后的向量更均匀地分布在超球面上

## 5. 总结

### a) 一句话
ScaleNorm 用 L2 归一化加单一可学习标量替代 LayerNorm（参数量从 $2d$ 降至 1），FixNorm 约束嵌入到固定范数的超球面，两者是归一化极致简化的代表，其超球面思想在 2024 年的 nGPT 中得到了全面发展。

### b) 速记 pipeline
```
ScaleNorm: x → x / ‖x‖₂ → 乘以 g → 输出  (仅 1 个参数!)
FixNorm:   embedding e → c · e / ‖e‖₂      (固定常数 c)
SmallInit: W ~ Uniform(-0.01, 0.01)         (消除 warmup)
```

---
**阅读日期**: 2026-04-06
