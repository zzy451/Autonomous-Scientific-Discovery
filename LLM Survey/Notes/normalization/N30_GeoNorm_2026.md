# N-30: GeoNorm — Unify Pre-Norm and Post-Norm with Geodesic Optimization (2026)

> **论文**: Unify Pre-Norm and Post-Norm with Geodesic Optimization
> **arXiv**: 2601.22095
> **年份**: 2026
> **关键词**: GeoNorm, 测地线优化, 流形, Pre-Norm, Post-Norm, 归一化调度

---

## 核心思想

GeoNorm 提出用**流形上的测地线更新 (geodesic updates)** 替代传统的归一化层，从几何视角统一 Pre-Norm 和 Post-Norm。核心洞察：归一化本质上是将表示投影回流形表面，而测地线更新可以在流形上直接进行，无需显式的归一化-投影循环。此外，类比学习率调度，GeoNorm 引入**归一化调度 (normalization schedule)**，在训练过程中动态调整归一化强度。

## 方法

### 几何视角的统一

- **Pre-Norm 的几何解释**: 先投影到流形表面，再做变换 → 变换发生在切空间
- **Post-Norm 的几何解释**: 先做变换，再投影回流形 → 变换可能偏离流形
- **GeoNorm**: 直接在流形上沿测地线方向更新，无需显式归一化层

### 测地线更新

传统残差连接:
$$h_{l+1} = h_l + f(h_l)$$

GeoNorm 测地线更新:
$$h_{l+1} = \text{Exp}_{h_l}(\alpha_l \cdot v_l)$$

其中 $\text{Exp}$ 是流形上的指数映射 (exponential map)，$v_l$ 是切空间中的更新方向，$\alpha_l$ 是步长。

### 归一化调度 (Normalization Schedule)

类比学习率调度的思想：
- 训练初期：较强的归一化约束（类似 Post-Norm 的稳定性）
- 训练后期：逐渐放松约束（类似 Pre-Norm 的表达力）
- 实现方式：动态调整测地线步长 $\alpha_l$ 的范围

## 与已有方法的关系

| 方法 | 归一化位置 | 几何解释 | 统一性 |
|------|-----------|---------|--------|
| Pre-Norm | 子层输入 | 切空间变换 | 稳定但性能受限 |
| Post-Norm | 子层输出 | 投影回流形 | 性能好但不稳定 |
| PeriLN (N-21) | 子层两侧 | 双重投影 | 折中方案 |
| nGPT (N-25) | 全局超球面 | 超球面约束 | 极端几何约束 |
| **GeoNorm** | **无显式归一化** | **测地线更新** | **几何统一** |

## 关键发现

1. **一致性超越**: GeoNorm 在多个 Transformer 任务上一致超过 Pre-Norm 和 Post-Norm
2. **无缝集成**: 可以直接替换标准 Transformer 中的归一化层，无需大幅修改架构
3. **归一化调度有效**: 动态调整归一化强度比固定策略更优
4. **统一框架**: Pre-Norm 和 Post-Norm 可以被视为测地线更新的特殊情况

## 局限

1. 测地线计算（指数映射）的额外开销
2. 流形选择（超球面 vs Stiefel vs Oblique）对性能的影响需要进一步研究
3. 超大规模模型上的验证尚不充分

## 在综述中的定位

GeoNorm 代表了归一化研究的**几何统一方向**：不再争论 Pre-Norm vs Post-Norm，而是从流形几何的角度提供统一框架。与 nGPT (N-25) 的超球面约束思路相关，但 GeoNorm 更灵活——不要求所有向量严格在超球面上，而是通过测地线更新隐式保持几何一致性。归一化调度的概念也是新颖的贡献，将归一化从静态设计推向动态策略。

---

**阅读日期**: 2026-04-06
