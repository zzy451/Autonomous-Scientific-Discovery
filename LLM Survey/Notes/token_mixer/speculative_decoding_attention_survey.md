# Speculative Decoding 与 Attention 的关系综述笔记
**主题**: Speculative Decoding 对 Token Mixer 设计的影响 | **年份**: 2023-2025

## 0. 概述
Speculative Decoding（推测解码）是一类通过"先猜后验"加速自回归生成的方法。它与 Token Mixer 的关系体现在：(1) draft model 的设计直接涉及注意力架构选择；(2) 验证阶段利用注意力的并行性；(3) Multi-Token Prediction 头可以作为 draft model。

## 1. 核心思想
```
标准自回归: token₁ → token₂ → token₃ → token₄ (串行，4步)
推测解码:   draft: [token₁,₂,₃,₄] (1步猜测) → verify: 并行验证 (1步) → 接受前3个
            总共 2 步完成 3 个 token → 加速 ~1.5x
```

## 2. 主要方法与 Attention 的关系

### a) 独立 Draft Model 方法
- **Leviathan et al. (2023)** / **Chen et al. (2023)**: 用小 Transformer 作为 draft model
- Draft model 通常用更少的层/更小的 hidden size
- 关键: draft model 的注意力架构影响猜测速度和质量的平衡
- 趋势: draft model 倾向使用更高效的注意力（如 MQA、更少层）

### b) Self-Draft 方法 (无需额外模型)
- **Medusa (Cai et al. 2024)**: 在 LLM 最后一层添加多个并行预测头
  - 每个头是一个小型 FFN，预测第 i 个未来 token
  - 不涉及额外注意力计算
  - 与 Multi-Token Prediction 思想相似
- **EAGLE (Li et al. 2024)**: 用一个轻量 Transformer 层作为 draft head
  - 输入: 当前隐状态 + 上一个 token embedding
  - 自回归地生成 draft tokens
  - 使用简化的注意力（单层、少头）
- **EAGLE-2**: 引入动态 draft tree，根据置信度调整猜测长度

### c) 与 Token Mixer 设计的交叉
- **MTP 作为 Draft**: Multi-Token Prediction 训练的额外头天然可作为 draft model（Gloeckle et al. 2024, DeepSeek-V3）
- **SSM 作为 Draft**: Mamba 等 SSM 模型推理极快（O(1)/step），适合作为 draft model
- **层跳过**: 跳过中间层作为 draft（利用了层间冗余，与 CLA 思想相关）
- **KV Cache 共享**: draft model 和 target model 共享 KV cache 可以减少内存开销

## 3. 对 Attention 设计的启示
- 推测解码的验证阶段天然利用了注意力的**并行前向**能力（一次验证多个 token）
- 这使得注意力（可并行）相比纯 RNN/SSM（必须串行）在验证阶段有优势
- 混合架构（如 Griffin）可以用 RNN 部分快速 draft，用注意力部分并行验证
- 推测解码的存在使得"推理时注意力的并行性"成为架构设计的重要考量

## 4. 关键论文
| 论文 | 年份 | Draft 方法 | 与 Attention 关系 |
|------|------|-----------|------------------|
| Speculative Sampling (Leviathan) | 2023 | 小 Transformer | 独立 draft model |
| Medusa | 2024 | 并行 FFN 头 | 无额外注意力 |
| EAGLE / EAGLE-2 | 2024 | 轻量 Transformer 层 | 简化注意力 draft |
| Multi-Token Prediction | 2024 | 训练时额外头 | 共享主干注意力 |
| Recurrent Drafter | 2024 | RNN draft head | RNN 替代注意力 |

## 5. 总结
a) **一句话**: 推测解码通过"快速猜测+并行验证"加速生成，其 draft model 设计涉及高效注意力架构选择，而验证阶段利用了注意力的并行性，使得注意力在推理加速中仍有不可替代的价值。
b) **与 Token Mixer 综述的关联**: 推测解码是评估不同 Token Mixer 推理效率的重要维度——SSM/RNN 适合做 draft（快），Attention 适合做 verify（并行）。
