# SageAttention: Accurate 8-Bit Attention for Plug-and-play Inference Acceleration
**作者**: Jintao Zhang, Jia Wei, Pengle Zhang, Jun Zhu, Jianfei Chen | **年份**: 2024 | **arxiv**: 2410.02367

## 0. 摘要翻译
本文提出 SageAttention，一种高效且精确的注意力量化方法。通过将 Q 和 K 量化为 INT8 进行矩阵乘法，并对 softmax 后的 P 和 V 使用 FP16/FP8，SageAttention 在保持精度的同时实现了比 FlashAttention-2 快 2.1 倍的推理速度。后续 SageAttention2 进一步将 Q/K 量化到 INT4，P/V 量化到 FP8，实现 3x+ 加速。SageAttention3 探索了 FP4 微缩放量化。

## 1. 方法动机
a) **为什么**: FlashAttention 通过 IO 优化加速注意力，但未利用低精度计算。现代 GPU（如 H100）的 INT8/FP8 Tensor Core 吞吐量是 FP16 的 2-4 倍。
b) **痛点**: (1) 朴素量化注意力会导致严重精度损失（softmax 对数值敏感）；(2) Q·K^T 的动态范围大，直接 INT8 量化误差大；(3) 需要找到注意力中哪些部分可以安全量化。
c) **假设**: 通过精心设计的量化策略（per-channel 量化 Q/K + 平滑异常值），可以在注意力中安全使用低精度计算。

## 2. 方法设计

### a) SageAttention (v1)
```
标准注意力: S = Q·K^T (FP16) → P = softmax(S) → O = P·V (FP16)
SageAttention: S = Q_int8·K_int8^T (INT8) → P = softmax(S_fp16) → O = P·V (FP16)
```

**Q/K 量化策略**:
- Per-channel 量化（每个 head 维度独立缩放）
- 平滑处理: 减去通道均值以减少异常值影响
- `Q_int8 = round(Q / scale_q)`, `K_int8 = round(K / scale_k)`
- 反量化在 softmax 前完成: `S = scale_q · scale_k · (Q_int8 · K_int8^T)`

**精度保证**:
- Softmax 仍在 FP16/FP32 下计算（对精度最敏感的部分）
- P·V 乘法保持 FP16（P 的值域 [0,1] 量化损失大）
- 只有 Q·K^T 使用 INT8（这部分对量化最鲁棒）

### b) SageAttention2
- Q/K: INT4 量化（4x 加速 QK^T）
- P/V: FP8 量化（2x 加速 PV）
- 总加速: ~3x over FlashAttention-2
- 使用自适应量化粒度（per-warp 或 per-block）

### c) SageAttention3
- 探索 FP4 微缩放（Microscaling）量化
- 利用 Blackwell GPU 的 FP4 Tensor Core
- 目标: 在下一代硬件上实现 5-10x 加速

### d) 关键公式
- INT8 QK^T: `S_ij = s_q · s_k · Σ_d Q_int8[i,d] · K_int8[j,d]`
- 平滑: `Q' = Q - mean(Q, dim=-1)`, `K' = K - mean(K, dim=-1)`
- 误差补偿: `S = S_int8 + correction_term`

## 3. 对比
| 实现 | QK^T 精度 | PV 精度 | 相对 FA2 加速 | 精度损失 |
|------|----------|---------|-------------|---------|
| FlashAttention-2 | FP16 | FP16 | 1x | 0 |
| FlashAttention-3 | FP16/FP8 | FP16/FP8 | 1.5-2x | 极小 |
| SageAttention | INT8 | FP16 | 2.1x | 极小 |
| SageAttention2 | INT4 | FP8 | 3x+ | 小 |

## 4. 实验
- **速度**: SageAttention 在 A100 上比 FA2 快 2.1x，在 RTX 4090 上快 2.7x
- **精度**: 在 Llama-2-7B, Mistral-7B 上，PPL 增加 <0.1（几乎无损）
- **通用性**: 即插即用，无需重训练，适用于任何 Transformer 模型
- **多模态**: 在 Stable Diffusion, DiT 等视觉模型上同样有效
- **SageAttention2**: 在 H100 上达到 ~1.5 PFLOPS（INT4 QK^T + FP8 PV）
- **工业采用**: 被多个推理框架集成

## 5. 总结
a) **一句话**: SageAttention 通过将注意力中的 QK^T 计算量化为 INT8/INT4（利用 Tensor Core 低精度高吞吐），在保持精度的同时实现了 2-3x 的即插即用推理加速。
b) **速记 pipeline**: `Q,K → INT8/INT4 quantize (per-channel, smoothed) → INT8 GEMM(QK^T) → FP16 softmax → FP16/FP8 GEMM(PV) → Output`
