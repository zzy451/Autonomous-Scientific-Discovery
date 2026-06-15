# N-33: Outlier-Driven Rescaling is Essential for Transformer Training (2026)

> **论文**: Outlier-Driven Rescaling is Essential for Transformer Training
> **arXiv**: 2601.22966
> **年份**: 2026
> **关键词**: 异常值驱动重缩放, attention sink, residual sink, massive activation, RMSNorm, softmax

---

## 核心思想

Transformer 训练中会自发涌现两类异常值：**attention sink**（注意力集中在 BOS 等特殊 token 上）和 **residual sink / massive activation**（隐状态中出现极大幅值的维度）。本文揭示了一个关键洞察：**这些异常值不是 bug，而是 feature**——它们与归一化层（RMSNorm、softmax）协同工作，执行"异常值驱动的重缩放 (outlier-driven rescaling)"，这是 Transformer 有效训练的必要机制。

## 关键发现

### 发现 1: 异常值与归一化共生

- **移除归一化** → 异常值消失，但训练稳定性和性能下降
- **保留归一化但裁剪异常值** → 性能同样下降
- **结论**: 异常值和归一化是一个不可分割的功能单元

### 发现 2: 两类异常值的机制

**Attention Sink (注意力汇聚)**:
- BOS/特殊 token 获得不成比例的高注意力权重
- 机制: softmax 归一化将极大 logit 转化为近似 one-hot 分布
- 功能: 提供一个"默认注意力目标"，当没有强语义匹配时，注意力流向 sink token
- 与 softmax 的交互: softmax 的归一化特性使得 sink token 能有效"吸收"多余的注意力概率质量

**Residual Sink / Massive Activation (残差汇聚/巨大激活)**:
- 隐状态的某些维度出现极大值（比其他维度大 100-1000 倍）
- 机制: RMSNorm 将这些极大值转化为对其他维度的缩放效应
- 功能: 通过 RMSNorm 的除法操作，massive activation 实际上控制了非异常维度的有效尺度

### 发现 3: 重缩放机制

$$\text{RMSNorm}(x) = \frac{x}{\text{RMS}(x)} \cdot \gamma$$

当 $x$ 中存在 massive activation $x_k \gg x_i$ (对 $i \neq k$) 时:
$$\text{RMS}(x) \approx \frac{|x_k|}{\sqrt{d}}$$

因此非异常维度被缩放为:
$$\hat{x}_i \approx \frac{x_i \cdot \sqrt{d}}{|x_k|} \cdot \gamma_i$$

即 **massive activation 的幅值 $|x_k|$ 控制了所有其他维度的有效尺度**。

## 实验

1. **消融实验**: 分别移除归一化、裁剪异常值、同时操作，验证共生关系
2. **训练动态追踪**: 追踪异常值的涌现时间线，发现它们在训练早期就出现
3. **跨模型验证**: 在不同规模的 LLM 上验证现象的普遍性
4. **与 DyT/Derf 的关系**: 无归一化方法（DyT, Derf）通过 tanh/erf 的有界性提供了替代的重缩放机制，但机制不同

## 与已有方法的关系

| 方法 | 对异常值的态度 | 归一化角色 |
|------|--------------|-----------|
| 标准 Transformer | 被动接受 | 隐式利用 |
| SmoothQuant | 消除（迁移到权重） | 不变 |
| TWEO | 抑制（正则化损失） | 不变 |
| DyT/Derf (N-16/17) | 不产生（无归一化） | 替代为有界函数 |
| **本文** | **理解为必要机制** | **与异常值共生** |

## 对量化/低精度的启示

- 异常值是 FP8/INT8 量化的主要障碍
- 但本文表明异常值对训练是必要的
- 因此量化方案需要**保留异常值的功能**而非简单消除
- 这解释了为什么 FOG (N-34) 需要专门的架构设计来兼容 FP8

## 在综述中的定位

本文是归一化研究中的**机制解释性工作**，首次系统阐明了归一化层与涌现异常值之间的共生关系。这一发现对多个方向有深远影响：(1) 解释了为什么简单移除归一化（如早期 Fixup）效果有限；(2) 为 DyT/Derf 的成功提供了新视角（它们用有界函数替代了异常值-归一化的重缩放机制）；(3) 为低精度训练中的归一化设计提供了理论指导。

---

**阅读日期**: 2026-04-06
