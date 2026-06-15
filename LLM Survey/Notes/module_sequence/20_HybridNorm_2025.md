# HybridNorm: Towards Stable and Efficient Transformer Training via Hybrid Normalization
**作者**: (arxiv 2503.04598) | **年份**: 2025 | **arxiv**: 2503.04598 | **链接**: https://arxiv.org/html/2503.04598v3

## 0. 摘要翻译
本文提出 HybridNorm，一种混合归一化策略，在 Transformer 块的不同子层中采用不同的归一化方案。具体而言，HybridNorm 在注意力机制中使用 QKV 归一化（QKV-Norm），在前馈网络（FFN）中使用 Post-Norm。该设计不仅稳定了训练过程，还加速了收敛并提升了最终性能。

## 1. 方法动机
- 注意力机制和 FFN 具有不同的数值特性和梯度行为，统一使用同一种归一化策略并非最优
- 注意力层中 Q、K 向量的尺度直接影响 softmax 的锐度，QKV-Norm 可以有效控制注意力分布
- FFN 层更受益于 Post-Norm 的表示规范化能力
- 需要一种"因地制宜"的归一化策略，针对不同子层的特性选择最合适的归一化方式

## 2. 方法设计

### 注意力层：QKV-Norm
- 对 Query、Key、Value 向量分别施加 LayerNorm / RMSNorm
- 控制注意力分数的尺度，防止 softmax 饱和或过于平坦
- 稳定注意力权重的分布，避免训练初期的注意力熵崩溃（entropy collapse）

### FFN 层：Post-Norm
- FFN 输出经过残差相加后施加 LayerNorm
- 保持 Post-Norm 对 FFN 输出的强表示规范化能力
- FFN 的梯度特性与注意力层不同，Post-Norm 在此处更有效

### 整体块结构
```
x -> QKV-Norm(Q,K,V) -> Attention -> +x -> FFN -> +x -> LN -> output
     (注意力内部归一化)              (残差)        (残差) (Post-Norm)
```

## 3. 与其他方法对比
| 方法 | Attention归一化 | FFN归一化 | 设计理念 |
|------|---------------|----------|---------|
| Pre-Norm | LN在子层前 | LN在子层前 | 统一策略 |
| Post-Norm | LN在残差后 | LN在残差后 | 统一策略 |
| Sandwich-LN | LN在子层前后 | LN在子层前后 | 统一策略 |
| HybridNorm | QKV-Norm | Post-Norm | 分层定制 |

## 4. 实验表现
- 收敛速度快于 Pre-Norm 和 Post-Norm
- 训练稳定性优于纯 Post-Norm，与 Pre-Norm 相当
- 最终性能优于 Pre-Norm，与精调的 Post-Norm 持平或更优
- 理论分析证明 QKV-Norm 可以有效约束注意力层的 Lipschitz 常数

## 5. 总结
a) **一句话概括**：HybridNorm 打破了对 Transformer 块统一归一化的惯例，在注意力层用 QKV-Norm 控制注意力尺度，在 FFN 层用 Post-Norm 保持表示能力，实现了分层定制的归一化策略。

b) **速记 pipeline**：`x -> [QKV-Norm -> Attn -> +x] -> [FFN -> +x -> LN] -> output`（注意力用 QKV-Norm，FFN 用 Post-Norm）
