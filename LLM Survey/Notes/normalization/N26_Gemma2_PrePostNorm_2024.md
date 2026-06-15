# Gemma 2: Improving Open Language Models at a Practical Size
**作者**: Gemma Team, Google | **年份**: 2024 | **arxiv**: 2408.00118

## 0. 摘要翻译

Gemma 2 是 Google 推出的新一代开源语言模型系列，提供 2B、9B、27B 三种规模。在架构设计上，Gemma 2 引入了多项改进以提升训练稳定性和最终性能，其中最关键的归一化改进是 **Pre+Post RMSNorm** 策略——在每个 Transformer 子层的输入和输出都应用 RMSNorm。此外还采用了 **QK-Norm**（对 Query 和 Key 进行归一化）和 **logit soft-capping**（约束注意力和最终 logits 的范围）。这些技术共同构成了多层次的归一化保护体系。

## 1. 方法动机

### a) 为什么
从 Gemma 1 到 Gemma 2 的升级中，Google 发现标准 Pre-RMSNorm 在大规模训练中偶尔出现训练不稳定（loss spike）。需要更强的归一化保护来确保数十亿参数模型的稳定训练。

### b) 痛点
- **训练不稳定 (Loss Spikes)**: 大规模训练中偶发的 loss 突增，可能需要回滚和重新训练
- **Pre-Norm 的方差漂移**: 如 Peri-LN 论文所分析，Pre-Norm 的残差路径不受约束
- **注意力 logit 爆炸**: 在大规模模型中，注意力 logits 可能增长到导致 FP16/BF16 溢出
- **输出 logit 过大**: 最终 softmax 前的 logits 过大导致数值问题

### c) 假设
通过在多个层次上施加归一化约束——子层输入/输出的 RMSNorm、注意力 Q/K 的 L2 归一化、logit 的 soft-capping——可以从根本上消除各种数值不稳定的来源。

## 2. 方法设计

### a) Pipeline
1. 在每个子层输入应用 RMSNorm（Pre-Norm，与 Gemma 1 相同）
2. 在每个子层输出、残差连接**之前**新增 RMSNorm（Post-Norm）
3. 在注意力层中对 Q, K 向量应用 L2 归一化（QK-Norm）
4. 对注意力 logits 和最终输出 logits 应用 soft-capping

### b) 模块

**Pre+Post RMSNorm**:
```
Gemma 1 (Pre-Norm only):
  x → [RMSNorm] → [Attention/FFN] → [+x] → output

Gemma 2 (Pre+Post RMSNorm):
  x → [RMSNorm₁] → [Attention/FFN] → [RMSNorm₂] → [+x] → output
```

**QK-Norm** (与 Henry et al. 2020 相同):
$$\hat{Q} = \frac{Q}{\|Q\|_2}, \quad \hat{K} = \frac{K}{\|K\|_2}$$

**Logit Soft-Capping**:
$$\text{logits} = \text{cap} \cdot \tanh\left(\frac{\text{logits}}{\text{cap}}\right)$$
- 注意力 logits cap: 50.0
- 最终 logits cap: 30.0
- 效果: 将 logits 约束在 $(-\text{cap}, +\text{cap})$ 范围内

### c) 公式

**Gemma 2 完整的归一化保护体系**:
1. **层级归一化**: Pre+Post RMSNorm 控制每个子层的输入/输出尺度
2. **注意力输入归一化**: QK-Norm 将 Q·K 点积约束为余弦相似度
3. **注意力输出约束**: logit soft-capping 防止 softmax 前 logit 爆炸
4. **最终输出约束**: 最终 logit soft-capping 防止预测概率极端化

## 3. 对比

| 归一化策略 | Gemma 1 | Gemma 2 |
|-----------|---------|---------|
| RMSNorm 位置 | Pre-Norm only | **Pre+Post Norm** |
| QK-Norm | 无 | **有** |
| Logit Soft-Capping | 无 | **有** |
| 训练稳定性 | 一般 | **更强** |

**与历史方法的对应**:
| 方法 | 年份 | 策略 | 归一化类型 |
|------|------|------|-----------|
| Sandwich-LN (CogView) | 2021 | 子层前+后 | LayerNorm |
| Peri-LN | 2025 | 子层前+输出后(残差前) | LayerNorm |
| **Gemma 2** | 2024 | 子层前+输出后(残差前) | **RMSNorm** |

Gemma 2 的 Pre+Post RMSNorm 本质上是 Sandwich-LN/Peri-LN 的 **RMSNorm 版本**，在工业规模 (27B) 上验证了有效性。

## 4. 实验

- **模型规模**: 2B, 9B, 27B 参数
- **训练数据**: 数万亿 token
- **训练稳定性**: Pre+Post RMSNorm 消除了 loss spikes
- **基准评测**: 在 MMLU、GSM8K、HellaSwag 等基准上达到同规模 SOTA
- **知识蒸馏**: Gemma 2 还使用了从大模型到小模型的蒸馏，但归一化设计是正交的改进
- **与 Llama 3.1 对比**: 在同等参数量下，Gemma 2 性能具有竞争力
- **工业验证**: Google 内部大规模训练验证了该归一化体系的稳健性

## 5. 总结

### a) 一句话
Gemma 2 通过 Pre+Post RMSNorm、QK-Norm 和 logit soft-capping 构建了多层次的归一化保护体系，在工业规模 (27B) 上验证了双重归一化（2021 年 Sandwich-LN 思想的 RMSNorm 版本）的有效性，是现代 LLM 归一化实践的重要参考。

### b) 速记 pipeline
```
层级保护:    x → RMSNorm₁ → Attn/FFN → RMSNorm₂ → +x → output
注意力保护:  Q, K → L2 归一化 → 余弦相似度 → soft-cap(50)
输出保护:    final logits → soft-cap(30) → softmax
（三层归一化保护: 子层级 + 注意力级 + 输出级）
```

---
**阅读日期**: 2026-04-06
