# Griffin & Hawk: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models
**作者**: Soham De, Samuel L. Smith, Anushan Fernando, Aleksandar Botev, George Cristian-Muraru, Albert Gu, Ruba Haroun, Leonard Berrada, Yutian Chen, Srivatsan Srinivasan, Guillaume Desjardins, Arnaud Doucet, David Budden, Yee Whye Teh, Razvan Pascanu, Nando De Freitas, Caglar Gulcehre | **年份**: 2024 | **arxiv**: 2402.19427

## 0. 摘要翻译
RNN 推理快且在长序列上扩展高效，但训练困难且难以扩展。本文提出 Hawk（带门控线性循环的 RNN）和 Griffin（将门控线性循环与局部注意力混合的模型）。Hawk 和 Griffin 在下游任务上分别超越 Mamba 和 Llama-2，同时训练效率与 Transformer 相当。Griffin 在长序列外推方面表现优异，可扩展至 14B 参数。

## 1. 方法动机
a) **为什么**: Transformer 的二次复杂度限制了长序列处理；现有 RNN 替代方案（如 S4、Mamba）虽然推理高效，但训练吞吐量和扩展性仍有差距。
b) **痛点**: 纯 RNN 模型在 recall-intensive 任务上弱于 Transformer；纯注意力模型推理成本随序列长度线性增长。
c) **假设**: 将门控线性循环（高效序列建模）与局部注意力（精确局部信息检索）混合，可以兼得两者优势。

## 2. 方法设计

### a) Pipeline
- **Hawk**: 纯 RNN 架构，交替堆叠 RG-LRU 循环块和 MLP 块
- **Griffin**: 混合架构，交替堆叠 [RG-LRU + 局部注意力] 混合块和 MLP 块

### b) 核心模块：Real-Gated Linear Recurrent Unit (RG-LRU)
RG-LRU 是本文的核心创新，基于 Linear Recurrent Unit (LRU) 改进：
- 输入门: `i_t = σ(W_i x_t + b_i)`
- 循环门: `a_t = σ(W_a x_t + b_a)`
- 循环权重: `r_t = diag(exp(-8 · softplus(ν) · a_t²))` — 其中 ν 是可学习参数
- 状态更新: `h_t = r_t ⊙ h_{t-1} + √(1 - r_t²) · (i_t ⊙ x_t)`

### c) 关键公式
- 循环块结构（类似 Mamba 的选择性门控）:
  - 两个分支: 一支经过 Conv1D → RG-LRU，另一支经过 GeLU 激活
  - 两支逐元素相乘后经线性投影输出
- 局部注意力: 使用固定窗口大小的滑动窗口注意力（如 1024 tokens）
- Griffin 中 RG-LRU 层和局部注意力层交替排列

## 3. 对比
| 模型 | 类型 | 训练效率 | 推理效率 | 长序列 |
|------|------|----------|----------|--------|
| Transformer (Llama-2) | 全注意力 | 高 | 低(KV cache) | 受限 |
| Mamba | 选择性 SSM | 中 | 高 | 好 |
| Hawk | 纯 RG-LRU | 高 | 高 | 好 |
| Griffin | RG-LRU + 局部注意力 | 高 | 高 | 最好 |

- Griffin vs Llama-2: 同等参数下质量更好，推理更快
- Hawk vs Mamba: 训练吞吐量更高，下游任务更强

## 4. 实验
- **规模**: 100M → 14B 参数，在 300B tokens 上训练
- **语言建模**: Griffin-14B 在 MMLU 等基准上匹配 Llama-2 质量
- **长序列**: 在 4096 tokens 训练后可外推至 16K+ tokens（copy/retrieval 任务）
- **训练效率**: Griffin 训练吞吐量与同规模 Transformer 相当（得益于硬件友好的循环设计）
- **推理效率**: 在长序列上推理延迟显著低于 Transformer（无需 KV cache 线性增长）
- **RecurrentGemma**: Google 基于 Griffin 架构发布了 RecurrentGemma-2B/9B 开源模型

## 5. 总结
a) **一句话**: Griffin 通过将新颖的 RG-LRU 门控线性循环与局部滑动窗口注意力混合，在保持 Transformer 级训练效率的同时实现了高效推理和长序列外推。
b) **速记 pipeline**: `Input → [RMSNorm → (Conv1D → RG-LRU) ⊙ GeLU → Linear] 交替 [RMSNorm → Local SWA] → MLP → Output`
