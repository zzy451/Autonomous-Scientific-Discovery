# RecurrentGemma: Moving Past Transformers for Efficient Open Language Models
**作者**: Botev et al. (Google DeepMind) | **年份**: 2024 | **arxiv**: 2404.07839

## 0. 摘要翻译
RecurrentGemma 是 Google 基于 Griffin 架构发布的开源语言模型（2B 和 9B 参数）。它使用 RG-LRU（Real-Gated Linear Recurrent Unit）与局部滑动窗口注意力的混合架构，在保持与 Gemma-2B 相当质量的同时，实现了固定大小的状态（不随序列长度增长的内存占用），使得长序列推理更加高效。

## 1. 方法动机
a) **为什么**: Gemma 系列需要一个高效推理的变体，特别是在设备端和长序列场景下。Griffin 架构已在研究中证明了其有效性，需要将其产品化。
b) **痛点**: (1) 标准 Transformer 的 KV cache 随序列长度线性增长；(2) 设备端部署对内存敏感；(3) 需要一个开源的、经过充分训练的循环式 LLM。
c) **假设**: Griffin 架构（RG-LRU + 局部注意力）经过大规模训练后可以匹配同规模 Transformer 的质量。

## 2. 方法设计

### a) 架构
RecurrentGemma 直接采用 Griffin 架构:
```
Block 类型交替:
  Recurrent Block: RMSNorm → [Conv1D → RG-LRU] ⊙ [GeLU] → Linear
  Attention Block: RMSNorm → Local SWA (window=2048) → Linear
  MLP Block: RMSNorm → GeGLU FFN

堆叠模式 (26 层):
  [Recurrent, Recurrent, Attention, Recurrent, Recurrent, Attention, ...] + MLP after each
```

### b) 核心模块

**RG-LRU (Real-Gated Linear Recurrent Unit)**:
- 与 Griffin 论文相同
- 输入门 + 循环门控制状态更新
- 固定大小状态: O(d) per layer（不随序列长度增长）
- 训练时可并行（通过 parallel scan）

**局部滑动窗口注意力**:
- 窗口大小 2048
- 只关注最近 2048 个 token
- KV cache 大小固定为 2048（不增长）
- 提供精确的局部信息检索

**推理时的固定状态**:
- RG-LRU 层: 固定大小隐状态 h ∈ R^d
- 注意力层: 固定大小 KV cache (window=2048)
- 总推理内存: O(d + w·d) per layer — 与序列长度无关

### c) 训练细节
- 训练数据: 2T tokens (RecurrentGemma-2B), 与 Gemma 使用相同数据
- 使用 JAX/Flax 实现
- 支持 SFI (Supervised Fine-tuning) 和 RLHF

## 3. 对比
| 模型 | 架构 | 推理状态大小 | 长序列推理 |
|------|------|-------------|-----------|
| Gemma-2B | Transformer | O(L·n·d) 增长 | KV cache 瓶颈 |
| RecurrentGemma-2B | Griffin (RG-LRU+SWA) | O(L·(d+w·d)) 固定 | 高效 |
| Mamba-2.8B | SSM | O(L·N·d) 固定 | 高效 |
| RWKV-3B | Linear RNN | O(L·d²) 固定 | 高效 |

## 4. 实验
- **质量**: RecurrentGemma-2B 在 MMLU, HellaSwag, PIQA 等基准上与 Gemma-2B 相当
- **推理效率**: 在长序列上内存恒定，吞吐量不随序列长度下降
- **指令遵循**: RecurrentGemma-2B-it 经过 SFT+RLHF 后聊天质量良好
- **开源**: 权重在 Kaggle 和 Hugging Face 上公开发布
- **局限**: 在某些需要精确长程检索的任务上略弱于纯 Transformer（RG-LRU 的压缩记忆有损）

## 5. 总结
a) **一句话**: RecurrentGemma 是 Google 基于 Griffin 架构（RG-LRU + 局部注意力混合）发布的开源循环式语言模型，以固定推理状态实现了与同规模 Transformer 相当的质量。
b) **速记 pipeline**: `Input → [RG-LRU Block × 2 → Local SWA Block × 1] × N_groups → GeGLU MLP → Output | State: fixed O(d+w·d) per layer`
