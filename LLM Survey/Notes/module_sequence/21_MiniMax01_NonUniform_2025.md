# MiniMax-01: Non-Uniform Hybrid Attention with Lightning Attention (7:1 Ratio)
**作者**: MiniMax AI | **年份**: 2025 | **arxiv**: 2501.08313 | **链接**: https://arxiv.org/abs/2501.08313

## 0. 摘要翻译
MiniMax-01 是一个 456B 参数的 MoE 语言模型（45.9B 激活参数），其核心架构创新在于非均匀的混合注意力层设计：每 8 层 Transformer 中，7 层使用 Lightning Attention（线性注意力），1 层使用传统 Softmax Attention。这种 7:1 的异构层比例使模型在训练时支持 1M token 上下文，推理时可扩展至 4M token，同时保持与全 Softmax 模型可比的质量。

## 1. 方法动机
- 标准 Softmax Attention 的 O(n²) 复杂度在超长上下文（>100K token）下计算成本极高
- 纯线性注意力模型虽然高效，但在精确检索和局部模式匹配上不如 Softmax Attention
- 需要在效率和质量之间找到最优的层级配比
- 关键洞察：并非每一层都需要全精度的 Softmax Attention，大部分层可以用线性注意力替代

## 2. 方法设计

### 非均匀层设计（7:1 比例）
- **Lightning Attention 层（7/8）**：线性复杂度 O(n)，负责大部分序列建模
  - 基于线性注意力机制，去除 softmax 操作
  - 高效处理超长序列，内存占用与序列长度线性相关
- **Softmax Attention 层（1/8）**：二次复杂度 O(n²)，负责精确的全局信息聚合
  - 每隔 7 层插入一层标准 Softmax Attention
  - 提供精确的 token 间交互，弥补线性注意力的表达力不足

### 层排列模式
```
[Lightning] x 7 -> [Softmax] -> [Lightning] x 7 -> [Softmax] -> ...
```
共 80 层，其中 70 层 Lightning Attention + 10 层 Softmax Attention

### 其他架构特点
- 采用 DeepNorm 归一化策略
- MoE 结构：部分层使用 Mixture-of-Experts
- 64 个注意力头，头维度 128
- WSD（Warmup-Stable-Decay）学习率调度

## 3. 与其他方法对比
| 模型 | 注意力类型 | 层比例 | 最大上下文 | 参数量 |
|------|-----------|-------|-----------|-------|
| GPT-4 | 全 Softmax | 均匀 | 128K | ~1.8T (推测) |
| Gemma 2 | SWA + Full Attn | 1:1 交替 | 8K | 27B |
| Gemma 3 | SWA + Full Attn | 5:1 | 128K | 27B |
| MiniMax-01 | Lightning + Softmax | 7:1 | 4M | 456B (45.9B活) |
| Jamba | Mamba + Attn | 7:1 | 256K | 52B (12B活) |

### 非均匀设计的趋势
- Gemma 3 采用 5:1 的滑动窗口/全局注意力比例
- MiniMax-01 采用 7:1 的线性/Softmax 注意力比例
- Jamba 采用约 7:1 的 Mamba/Attention 比例
- 共同趋势：少量精确注意力层 + 大量高效层

## 4. 实验表现
- 支持 1M token 训练上下文，4M token 推理上下文
- 在标准 LLM 基准上与同规模全 Softmax 模型性能可比
- 长上下文任务（NIAH、长文档QA）上表现优异
- 训练使用约 2000 张 H800 GPU，约 12T token 数据

## 5. 总结
a) **一句话概括**：MiniMax-01 通过 7:1 的 Lightning/Softmax 非均匀层设计，证明了绝大多数层可以用线性注意力替代，仅需少量 Softmax 层即可维持模型质量，同时将上下文长度扩展至百万级别。

b) **速记 pipeline**：`[Lightning Attn + FFN] x7 -> [Softmax Attn + FFN] x1 -> 重复 x10`（80层，7:1 异构比例）
