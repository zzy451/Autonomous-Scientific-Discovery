# KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache
**作者**: Zirui Liu, Jiayi Yuan, Hongye Jin, Shaochen Zhong, Zhaozhuo Xu, Vladimir Braverman, Beidi Chen, Xia Hu | **年份**: 2024 | **arxiv**: 2402.02750

## 0. 摘要翻译
高效服务大语言模型（LLM）需要对大量请求进行批处理以降低单请求成本。然而，更大的批量和更长的上下文长度会导致 KV cache 显著膨胀，成为内存瓶颈。量化是一种潜在的解决方案，但此前缺乏对 KV cache 元素分布的深入研究。本文对 key cache 和 value cache 的元素分布进行了系统分析，发现：key cache 应按通道（per-channel）量化，value cache 应按 token（per-token）量化。基于此发现，本文提出 KIVI，一种无需微调的非对称 2bit KV cache 量化算法，可即插即用地应用于现有 LLM，在几乎不损失质量的前提下将 KV cache 内存压缩至原来的 ~2.6 倍，并支持更大的批量大小。

## 1. 方法动机
a) **为什么**: LLM 推理中 KV cache 是主要内存瓶颈。以 Llama-2-7B 为例，batch=128、seq_len=4096 时 KV cache 占用约 64GB（FP16），远超模型参数本身。
b) **痛点**: (1) 直接对 KV cache 做 per-tensor 或 per-token 量化会导致严重质量损失，因为 key cache 中存在跨 token 的通道级离群值（outlier channels）；(2) 现有量化方法多针对权重设计，未考虑 KV cache 的独特分布特性；(3) 需要一种无需重新训练、即插即用的方案。
c) **假设**: key 和 value 的元素分布具有不同的统计特性，应采用不同的量化粒度策略（非对称量化）。

## 2. 方法设计

### a) 核心观察

**Key cache 分布特性**:
- 存在显著的通道级离群值：某些通道的数值范围远大于其他通道
- 离群值在不同 token 间保持一致（同一通道始终偏大或偏小）
- 因此应按通道（per-channel）量化：沿 channel 维度分组，每组共享量化参数

**Value cache 分布特性**:
- 无明显通道级离群值，数值分布在 token 间变化较大
- 因此应按 token（per-token）量化：每个 token 的 value 向量独立量化

### b) 量化公式
对于一组元素 x，2bit 均匀量化：
```
x_q = round((x - x_min) / Δ)，Δ = (x_max - x_min) / (2^b - 1)
x_dequant = x_q * Δ + x_min
```
- Key cache: 按 channel 维度计算 x_min, x_max（即每个 head 的每个 channel 维度共享一组量化参数）
- Value cache: 按 token 维度计算 x_min, x_max（即每个 token 的 value 向量独立量化）

### c) 流式量化（Streaming Quantization）
由于自回归生成中 KV cache 逐 token 增长：
- **Value cache**: 每生成一个新 token，直接对其 value 向量做 per-token 量化并追加，无需重新量化历史
- **Key cache**: per-channel 量化需要知道整个通道的统计量。解决方案：
  - 保留最近 r 个 token 的 key 为全精度（FP16 residual）
  - 当 residual 缓冲区满时，将其整体做 per-channel 量化并合并到已量化的 key cache 中
  - 注意力计算时：`Attn = softmax(Q · [K_quant; K_residual]^T) · [V_quant; V_residual]`

### d) Pipeline
```
新 token → 计算 K, V
         → V: per-token 2bit 量化 → 追加到 V_quant
         → K: 追加到 K_residual (FP16)
         → 若 |K_residual| ≥ r: per-channel 2bit 量化 → 合并到 K_quant
         → Attention: Q × [K_quant | K_residual]^T → softmax → × [V_quant | V_residual]
```

## 3. 对比
| 方法 | 量化位宽 | Key 策略 | Value 策略 | 需要微调 | 内存压缩 |
|------|---------|---------|-----------|---------|---------|
| FP16 (baseline) | 16bit | - | - | - | 1x |
| KIVI | 2bit | per-channel | per-token | 否 | ~2.6x |
| KVQuant | 2-4bit | per-channel + 离群值保护 | per-token | 否 | ~2-4x |
| H2O | - | 驱逐不重要token | 驱逐不重要token | 否 | 可变 |
| SnapKV | - | 压缩 prefix | 压缩 prefix | 否 | 可变 |
| FlexGen | 4bit | per-tensor | per-tensor | 否 | ~4x |

## 4. 实验
- **模型**: Llama-2 (7B/13B/70B), Falcon-7B, Mistral-7B
- **质量评估**:
  - CoQA (阅读理解): 2bit KIVI 在 Llama-2-7B 上 F1 仅下降 ~0.5（从 77.8 到 77.3）
  - GSM8K (数学推理): 几乎无损
  - LongBench (长文本): 在 4k-16k 长度上保持接近 FP16 的性能
  - Perplexity: WikiText-2 上 PPL 增加 < 0.2（Llama-2-7B）
- **内存节省**: KV cache 内存减少约 2.6 倍（2bit + 量化参数开销）
- **吞吐量**: 在相同 GPU 内存下，batch size 可增大 2-4 倍，吞吐量相应提升
- **消融实验**: 验证了 per-channel (key) + per-token (value) 的非对称策略显著优于对称策略（per-token-only 或 per-channel-only）

## 5. 总结
a) **一句话**: KIVI 发现 key cache 和 value cache 具有不同的元素分布特性，提出非对称量化策略（key per-channel + value per-token）实现 2bit 无微调 KV cache 压缩，几乎无损地将内存压缩 2.6 倍。
b) **速记 pipeline**: `KV生成 → Key: residual buffer → 满时 per-channel 2bit 量化 | Value: 逐token per-token 2bit 量化 → 混合精度 Attention([Q_fp16] × [K_2bit; K_fp16]) → Output`
