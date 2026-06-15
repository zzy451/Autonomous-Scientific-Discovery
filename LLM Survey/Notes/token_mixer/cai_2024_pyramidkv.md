# PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling
**作者**: Zefan Cai, Yichi Zhang, Bofei Gao, Tianyu Liu, Keming Lu, Wayne Xiong, Yue Dong, Baobao Chang, Junjie Hu, Wen Xiao | **年份**: 2024 | **arxiv**: 2406.02069

## 0. 摘要翻译
本文提出 PyramidKV，一种基于"金字塔信息漏斗"观察的动态 KV cache 压缩方法。核心发现是：Transformer 不同层的注意力模式呈金字塔形——底层注意力分散（需要更多 KV），高层注意力集中（只需少量 KV）。PyramidKV 据此为每层分配不同数量的 KV cache 预算，底层多、高层少，在相同总预算下显著优于均匀分配策略。

## 1. 方法动机
a) **为什么**: KV cache 压缩方法（如 SnapKV、H2O）对每层使用相同的压缩比，但不同层的注意力模式差异很大。
b) **痛点**: (1) 底层注意力分散，均匀压缩会丢失大量信息；(2) 高层注意力集中在少数 token，保留过多 KV 是浪费；(3) 需要一种层自适应的 KV 分配策略。
c) **假设**: 根据每层注意力的集中程度动态分配 KV 预算（金字塔形：底多高少），可以在相同总内存下获得更好的质量。

## 2. 方法设计

### a) Pipeline
```
1. 分析注意力模式: 对每层计算注意力的"集中度"
2. 金字塔分配: 底层分配更多 KV 预算，高层分配更少
3. Per-layer 压缩: 每层按分配的预算选择 top-k 重要 KV
4. 推理: 使用层自适应压缩后的 KV cache
```

### b) 核心模块

**注意力模式观察**:
- 底层 (layers 0-10): 注意力分散在多个位置 → 需要保留更多 KV
- 中层 (layers 11-20): 注意力逐渐集中 → 中等 KV 预算
- 高层 (layers 21-31): 注意力高度集中在少数关键 token → 少量 KV 即可
- 这种模式在不同模型和输入上一致出现

**金字塔分配策略**:
- 给定总 KV 预算 B 和 L 层
- 底层每层分配 b_max 个 KV
- 高层每层分配 b_min 个 KV
- 中间层线性插值: `b_l = b_max - (b_max - b_min) · l / L`
- 约束: `Σ_l b_l = B`

**KV 选择**:
- 每层使用类似 SnapKV 的注意力投票方法
- 选择注意力权重最高的 b_l 个位置的 KV
- Per-head 独立选择

### c) 关键公式
- 层预算: `b_l = b_max - (b_max - b_min) · l / (L-1)`
- 总预算约束: `Σ_{l=0}^{L-1} b_l = B`
- 选择: `I_l = argtopk(attention_score_l, b_l)` per head

## 3. 对比
| 方法 | 层分配 | 压缩策略 | 自适应 |
|------|--------|----------|--------|
| SnapKV | 均匀 | Per-head top-k | 否 |
| H2O | 均匀 | 动态淘汰 | 否 |
| PyramidKV | 金字塔(底多高少) | Per-head top-k | 层自适应 |
| StreamingLLM | 均匀(sink+window) | 固定模式 | 否 |

## 4. 实验
- **长上下文基准**: 在 LongBench 上，PyramidKV 在相同总 KV 预算下比 SnapKV 提升 2-5%
- **Needle-in-a-Haystack**: 128K 上下文中检索准确率更高
- **压缩比**: 在 12x 压缩下仍保持 >95% 的原始质量
- **模型**: 在 Llama-2-7B, Llama-3-8B, Mistral-7B 上验证
- **消融**: 金字塔分配 > 均匀分配 > 倒金字塔分配，验证了底层需要更多 KV 的假设

## 5. 总结
a) **一句话**: PyramidKV 发现 Transformer 注意力模式呈金字塔形（底层分散、高层集中），据此为不同层分配不同 KV cache 预算，在相同总内存下优于均匀压缩方法。
b) **速记 pipeline**: `Observe attention patterns → Pyramid budget allocation (bottom-heavy) → Per-layer top-k KV selection → Compressed inference`
