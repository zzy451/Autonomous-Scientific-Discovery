# MiniCache: KV Cache Compression in Depth Dimension for Large Language Models
**作者**: Akide Liu, Jing Liu, Zizheng Pan, Yefei He, Gholamreza Haffari, Bohan Zhuang | **年份**: 2024 | **arxiv**: 2405.14366

## 0. 摘要翻译
本文提出 MiniCache，一种在层（深度）维度上压缩 KV cache 的方法。核心发现是：相邻层的 KV cache 在经过适当变换后具有高度相似性。MiniCache 通过跨层合并相似的 KV 状态，并在需要时用低秩残差恢复各层差异，实现了 KV cache 的深度维度压缩。与 token 维度压缩方法（如 SnapKV）正交，可以叠加使用。

## 1. 方法动机
a) **为什么**: 现有 KV cache 压缩主要在 token 维度（选择重要 token）或 head 维度（GQA/MQA），层维度的冗余尚未充分利用。
b) **痛点**: (1) CLA 需要从头训练，无法应用于已有模型；(2) 相邻层的 KV 虽然相似但不完全相同，直接共享会损失质量；(3) 需要一种 training-free 的层维度压缩方法。
c) **假设**: 相邻层的 KV cache 差异可以用低秩矩阵近似，因此可以存储共享部分 + 低秩残差来压缩。

## 2. 方法设计

### a) Pipeline
```
1. 正常 prefill，得到每层的 KV cache
2. 对相邻层 (l, l+1) 的 KV 进行配对
3. 计算每对的合并表示: KV_merged = (KV_l + KV_{l+1}) / 2
4. 计算残差: R_l = KV_l - KV_merged, R_{l+1} = KV_{l+1} - KV_merged
5. 对残差做低秩近似: R ≈ U·S·V^T (只保留 top-r 奇异值)
6. 存储: KV_merged + 低秩残差因子
7. 推理时恢复: KV_l ≈ KV_merged + U_l·S_l·V_l^T
```

### b) 核心模块

**跨层 KV 相似性**:
- 观察: 经过 RMSNorm 后，相邻层的 KV 余弦相似度 >0.9
- 关键: 需要在合适的表示空间中比较（归一化后）
- 相似度随层深度增加而增加（高层更相似）

**合并与低秩恢复**:
- 合并: `M = (KV_l + KV_{l+1}) / 2`
- 残差: `R_l = KV_l - M`
- 低秩近似: `R_l ≈ U_r Σ_r V_r^T` (rank-r SVD)
- 恢复: `KV_l ≈ M + U_r Σ_r V_r^T`
- 存储: 1 份 M + 2 份低秩因子（远小于 2 份完整 KV）

**Token 维度联合压缩**:
- MiniCache 可以与 SnapKV/PyramidKV 等 token 维度方法叠加
- 先做 token 选择，再做层合并
- 双重压缩效果

### c) 关键公式
- 压缩比: 每对层从 2×n×d 压缩到 n×d + 2×r×(n+d)
- 当 r << d 时，接近 2x 压缩
- 总压缩: 层维度 ~2x × token 维度 ~kx = ~2kx

## 3. 对比
| 方法 | 压缩维度 | Training-free | 与 token 压缩兼容 | 压缩比 |
|------|----------|--------------|-------------------|--------|
| GQA/MQA | Head | 否 | 是 | H/G× |
| CLA | Layer | 否(需重训) | 是 | 2× |
| SnapKV | Token | 是 | — | k× |
| MiniCache | Layer | 是 | 是 | ~2× |
| MiniCache+SnapKV | Layer+Token | 是 | — | ~2k× |

## 4. 实验
- **模型**: Llama-2-7B/13B, Llama-3-8B, Mistral-7B
- **长上下文**: LongBench 上 MiniCache (2x 层压缩) 质量损失 <1%
- **叠加压缩**: MiniCache + SnapKV 实现 4-8x 总压缩，质量仍可接受
- **内存节省**: 在 128K 上下文下，KV cache 从 16GB 降至 4-8GB
- **速度**: 恢复操作开销极小（低秩矩阵乘法）
- **低秩**: rank=4-8 即可恢复 >99% 的信息

## 5. 总结
a) **一句话**: MiniCache 利用相邻层 KV cache 的高相似性，通过跨层合并 + 低秩残差恢复实现 training-free 的层维度 KV cache 压缩，可与 token 维度压缩方法叠加。
b) **速记 pipeline**: `Prefill → Pair adjacent layers → Merge KV + Low-rank residual SVD → Store (Merged + U·Σ·V^T) → Restore at inference`
