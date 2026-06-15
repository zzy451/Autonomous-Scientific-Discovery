# N-32: UnitNorm — Rethinking Normalization for Transformers in Time Series (2024)

> **论文**: UnitNorm: Rethinking Normalization for Transformers in Time Series
> **arXiv**: 2405.15903
> **年份**: 2024
> **发表**: NeurIPS 2024 (OpenReview)
> **关键词**: UnitNorm, 时序归一化, token shift, attention shift, 稀疏注意力

---

## 核心思想

传统归一化方法（BatchNorm、LayerNorm）在时序 Transformer 中会引发三个特有问题：**token shift**（归一化改变 token 间的相对关系）、**attention shift**（注意力分布被扭曲）、**sparse attention**（注意力过度集中）。UnitNorm 提出一种极简方案：**仅按向量的 L2 范数缩放输入，将所有向量投影到单位超球面上**，不做均值中心化，不引入可学习的仿射参数。

## 方法

### 三个问题的诊断

1. **Token Shift**: LayerNorm 的均值中心化操作改变了不同时间步 token 之间的相对距离，破坏了时序信号中的趋势和周期信息
2. **Attention Shift**: 归一化后 token 表示的变化导致注意力权重分布偏移，模型关注错误的时间步
3. **Sparse Attention**: LayerNorm 的缩放操作可能放大某些维度，导致注意力过度集中在少数 token 上

### UnitNorm 定义

$$\text{UnitNorm}(x) = \frac{x}{\|x\|_2}$$

- 无均值中心化（保留时序偏移信息）
- 无方差缩放（仅归一化范数）
- 无可学习的 $\gamma, \beta$（零额外参数）
- 将所有向量映射到单位超球面 $S^{d-1}$

### 与 LayerNorm 的关键区别

| 操作 | LayerNorm | UnitNorm |
|------|-----------|----------|
| 均值中心化 | 有 $x - \mu$ | 无 |
| 方差缩放 | 有 $/ \sigma$ | 无 |
| 范数归一化 | 隐式 | 显式 $/ \|x\|_2$ |
| 可学习参数 | $\gamma, \beta$ | 无 |
| 输出空间 | $\mathbb{R}^d$ | $S^{d-1}$ (单位超球面) |

### 为什么有效

- 保留了 token 间的**角度关系**（余弦相似度不变）
- 消除了范数差异带来的注意力偏差
- 不破坏时序数据中的趋势和偏移信息
- 注意力计算退化为余弦相似度，分布更均匀

## 实验

- **长期预测**: 在 ETTh1/h2, ETTm1/m2, Weather, Electricity, Traffic 等标准 benchmark 上测试
- **分类**: 在 UEA 多变量时序分类 benchmark 上测试
- **异常检测**: 在 SMD, MSL, SMAP 等数据集上测试
- **结果**: UnitNorm 替换 LayerNorm 后，在多个 Transformer 变体（PatchTST, iTransformer, FEDformer 等）上一致提升性能
- **注意力可视化**: UnitNorm 产生更分散、更合理的注意力模式

## 与其他方法的关系

| 方法 | 领域 | 归一化方式 | 超球面约束 |
|------|------|-----------|-----------|
| LayerNorm (N-02) | 通用 | 均值+方差 | 无 |
| RMSNorm (N-09) | 通用 | RMS 缩放 | 无 |
| QK-Norm (N-10) | 注意力 | Q,K 的 L2 归一化 | Q,K 在超球面 |
| nGPT (N-25) | 全架构 | 全面 L2 归一化 | 所有向量在超球面 |
| RevIN | 时序 | 可逆实例归一化 | 无 |
| **UnitNorm** | **时序** | **L2 范数缩放** | **所有 token 在超球面** |

## 局限

1. 仅在时序 Transformer 上验证，未扩展到 NLP/CV
2. 无可学习参数可能在某些任务上限制表达力
3. 与 nGPT 的思路高度相似（都是超球面投影），但独立提出且聚焦不同领域

## 在综述中的定位

UnitNorm 是**时序领域对归一化的反思**，揭示了 LayerNorm 在时序数据上的特有缺陷（token shift, attention shift）。其方法本质上与 nGPT (N-25) 的超球面思想一脉相承，但从时序数据的实际问题出发独立得出相似结论，形成了有趣的跨领域呼应。

---

**阅读日期**: 2026-04-06
