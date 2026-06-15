# Peri-LN: Revisiting Normalization Layer in the Transformer Architecture
**作者**: (匿名/多作者) | **年份**: 2025 | **arxiv**: 2501.12948

## 0. 摘要翻译

LayerNorm 的放置位置（Pre-LN vs Post-LN）是 Transformer 架构设计中的关键选择。Pre-LN 提供良好的训练稳定性但存在隐状态方差随深度指数增长的问题，Post-LN 保持方差稳定但梯度流受阻。本文提出 **Peri-LN (Peripheral LayerNorm)**，在子层的输入和输出都放置归一化层，形成"外围"归一化。Peri-LN 同时获得了 Pre-LN 的梯度流优势和 Post-LN 的方差控制优势，并通过理论分析和实验验证了其在最大 3.2B 参数模型上的有效性。

## 1. 方法动机

### a) 为什么
Pre-LN 虽然是当前最广泛使用的 LN 位置，但存在一个被忽视的隐患：残差路径上的值不经过任何归一化约束，导致隐状态方差随深度**指数增长**。这种方差增长可能导致"massive activations"（巨大激活值）现象。

### b) 痛点
- **Pre-LN 的方差增长**: $\text{Var}(x_L) \sim O(L)$ 或更差，深层时激活值尺度不可控
- **Post-LN 的梯度消失**: 归一化在残差连接之后，阻断了梯度高速公路
- **Massive Activations 问题**: 少数维度上的激活值远大于其他维度，影响量化和推理
- **现有方案的折中**: Sandwich-LN、Sub-LN 等虽有改善但各有局限

### c) 假设
在子层的输入**和**输出（但在残差连接**之前**）都放置 LN，可以：(1) 保持 Pre-LN 的梯度高速公路（残差连接仍直接连接），(2) 通过输出端 LN 约束子层输出的方差，防止方差累积增长。

## 2. 方法设计

### a) Pipeline
1. 分析 Pre-LN 和 Post-LN 的方差增长和梯度流特性
2. 设计 Peri-LN：在子层输入和输出各放一个 LN
3. 关键: 输出端 LN 放在残差连接**之前**（区别于 Post-LN 和 Sandwich-LN）
4. 理论证明方差增长受控

### b) 模块

**各种 LN 位置的结构对比**:
```
Pre-LN:      x → [LN] → [SubLayer] → [+x] → output
Post-LN:     x → [SubLayer] → [+x] → [LN] → output
Sandwich-LN: x → [LN₁] → [SubLayer] → [LN₂] → [+x] → [LN₃?] → output  (含残差后LN)
Peri-LN:     x → [LN₁] → [SubLayer] → [LN₂] → [+x] → output
```

**Peri-LN 的关键区别**:
- 与 Sandwich-LN 的区别: LN₂ 在残差连接**之前**，残差之后无 LN
- 与 Post-LN 的区别: 残差连接之后无 LN，保持梯度高速公路
- 与 Pre-LN 的区别: 多了输出端 LN₂，约束子层输出的尺度

### c) 公式
**Pre-LN**:
$$x_{l+1} = x_l + f(\text{LN}(x_l))$$
方差: $\text{Var}(x_{l+1}) = \text{Var}(x_l) + \text{Var}(f(\text{LN}(x_l)))$（累积增长）

**Peri-LN**:
$$x_{l+1} = x_l + \text{LN}_2(f(\text{LN}_1(x_l)))$$
- LN₂ 将 $f(\text{LN}_1(x_l))$ 的方差约束为 $O(1)$
- 残差路径仍直连: 梯度可直接回传
- 方差增长: $\text{Var}(x_{l+1}) \approx \text{Var}(x_l) + O(1)$（线性增长，受控）

## 3. 对比

| 特性 | Pre-LN | Post-LN | Sandwich-LN | Peri-LN |
|------|--------|---------|-------------|---------|
| 方差增长 | 指数/线性（不受控） | 稳定 | 受控 | **受控** |
| 梯度流 | 好 | 差 | 中 | **好** |
| 训练稳定性 | 好 | 差 | 好 | **最好** |
| warmup 依赖 | 低 | 高 | 低 | **低** |
| LN 数量 (per block) | 2 | 2 | 4 | **4** |
| 残差路径归一化 | 无 | 有 | 部分 | **输出端有** |
| 首次提出年份 | 2018 | 2017 | 2021 | 2025 |

## 4. 实验

- **语言建模**: 在最大 3.2B 参数的模型上验证
- **方差分析**: Peri-LN 的隐状态方差增长显著低于 Pre-LN
- **梯度流**: 梯度范数在各层间更均匀分布
- **收敛稳定性**: 优于 Pre-LN 和 Post-LN
- **与 Gemma 2 的对应**: 类似于 Gemma 2 的 Pre+Post RMSNorm 理念（验证了双重归一化的有效性）
- **与 OLMo 的对应**: OLMo 也采用了非传统的归一化位置

## 5. 总结

### a) 一句话
Peri-LN 在子层的输入和输出（残差连接前）各放一个 LayerNorm，同时获得 Pre-LN 的梯度流优势和 Post-LN 的方差控制优势，是 LN 位置研究的最新进展，完成了 Post-LN -> Pre-LN -> Sandwich-LN -> Sub-LN -> Peri-LN 的演进谱系。

### b) 速记 pipeline
```
x → LN₁ → SubLayer(Attn/FFN) → LN₂ → + x → output
                                  ↑
                            关键: LN₂ 在残差加法之前
                            效果: 约束子层输出方差，不阻断梯度高速公路
```

---
**阅读日期**: 2026-04-06
