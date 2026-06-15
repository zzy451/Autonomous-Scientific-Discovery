# N-27: Re-Introducing LayerNorm (Gupta et al. 2024)

> **论文**: Re-Introducing LayerNorm: Geometric Meaning, Irreversibility and a Comparative Study with RMSNorm
> **作者**: Akshat Gupta, Atahan Ozdemir, Gopala Krishna Anumanchipalli
> **发表**: arXiv:2409.12951 (2024)
> **关键词**: LayerNorm, RMSNorm, 几何解释, 不可逆性, 均匀向量

---

## 核心思想

从几何角度重新审视 LayerNorm，揭示其本质是将隐藏表示投影到与"均匀向量" $\mathbf{1} = [1, 1, \dots, 1]^T$ 正交的子空间上，并证明此操作具有不可逆性——丢失的信息无法通过可学习参数恢复。实验表明 RMSNorm（不做均值减除）的模型自然学到了与均匀向量正交的表示，证明 LayerNorm 的均值减除步骤实际上是冗余的。

## 方法

### LayerNorm 的三步几何解释

1. **移除均匀分量**: 减去均值等价于移除输入向量在均匀向量 $\mathbf{1}$ 方向上的投影
2. **归一化**: 将剩余向量归一化到单位长度
3. **缩放**: 乘以 $\sqrt{d}$（d 为维度）

**几何结果**: 经过 LayerNorm 后，所有隐藏向量被约束在与 $\mathbf{1}$ 正交、范数为 $\sqrt{d}$ 的子空间上。

### 不可逆性 (Irreversibility)

LayerNorm 具有**不可逆性**——均值减除步骤显式地丢弃了输入在均匀向量方向上的所有信息。后续的可学习参数 $\gamma$ 和 $\beta$ **无法恢复**这些被丢弃的信息。换言之，LayerNorm 不能学习恒等变换 (identity transformation)。

### 与 RMSNorm 的对比

| 特性 | LayerNorm | RMSNorm |
|------|-----------|---------|
| 均匀分量移除 | 显式（减均值） | 无 |
| 信息丢失 | 丢失均匀方向信息 | 不丢失 |
| 不可逆性 | 是 | 否（可学恒等） |
| 模型表示分布 | 强制正交于 $\mathbf{1}$ | **自然学到**正交于 $\mathbf{1}$ |
| 计算效率 | 需要均值计算 | 更高效 |

## 关键发现

1. **均值减除是冗余的**: 使用 RMSNorm 训练的 LLM（如 LLaMA）自然地将内部表示对齐到与均匀向量正交的方向上，说明模型会自发学到这种几何结构
2. **隐藏状态的稳定性**: LayerNorm 和 RMSNorm 都在稳定残差流向量的范数方面起作用，但 RMSNorm 更高效
3. **实际等价**: 在大规模 LLM 中，LayerNorm 和 RMSNorm 产生几乎相同的隐藏表示几何分布

## 实验

- 分析了多个预训练 LLM 的隐藏状态分布
- 验证 RMSNorm 模型的表示自然与 $\mathbf{1}$ 正交
- 对比 LayerNorm 和 RMSNorm 模型的下游性能
- 结论：RMSNorm 在理论和实践上都是更优的选择

## 在综述中的定位

本文为 RMSNorm 取代 LayerNorm 提供了**几何层面的理论解释**。Zhang & Sennrich (2019) 在实验上证明了 re-centering 不重要，而本文从几何角度解释了**为什么不重要**：因为模型会自然学到与均匀向量正交的表示。这为 LLaMA 等现代 LLM 选择 RMSNorm 提供了事后理论支持。

---

**阅读日期**: 2026-04-05
