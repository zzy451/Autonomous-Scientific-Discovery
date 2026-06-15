# MiniMax-01: Scaling Foundation Models with Lightning Attention

**论文**: MiniMax-01: Scaling Foundation Models with Lightning Attention
**作者**: MiniMax
**年份**: 2025
**来源**: arXiv:2501.08313
**标签**: MoE, Lightning Attention, 混合注意力, 超长上下文

---

## 0. 摘要
MiniMax-01 是首个大规模部署线性注意力（Lightning Attention）的生产级 LLM。采用 456B 总参/45.9B 激活的 MoE 架构，配合 Lightning Attention 和 Softmax Attention 的混合设计，支持训练时 1M、推理时 4M token 的超长上下文。

## 1. 方法动机
a) 标准 Softmax Attention 的 O(N^2) 复杂度限制了超长上下文。
b) 纯线性注意力在精确检索任务上表现不佳。
c) 需要在效率和质量之间找到平衡。

## 2. 方法设计（Channel Mixer 相关）
a) MoE 配置：
   - 456B 总参数，45.9B 激活参数
   - 32 个专家
   - 标准 Top-K 路由

b) 混合注意力架构：
   - Lightning Attention（线性）与 Softmax Attention 以 7:1 比例交替
   - Lightning Attention 处理大部分层（高效长距离建模）
   - Softmax Attention 在关键层保持精确检索能力

c) 激活函数：SwiGLU

## 3. 与其他 MoE 模型对比
| 模型 | 总参/激活参 | 专家数 | 注意力类型 | 最大上下文 |
|------|------------|--------|-----------|-----------|
| DeepSeek-V3 | 671B/37B | 256 | Softmax | 128K |
| Llama 4 Scout | 109B/17B | 16 | Softmax+iRoPE | 10M |
| **MiniMax-01** | **456B/45.9B** | **32** | **Lightning+Softmax 7:1** | **4M** |

## 4. 对 Channel Mixer 的意义
MiniMax-01 的核心创新在 Token Mixer（混合注意力），但其 MoE 配置（32专家）展示了 MoE 与非标准注意力机制的结合。这说明 Channel Mixer（MoE）和 Token Mixer（注意力变体）的设计是可以独立优化的，验证了 survey 中"正交维度"的框架。

## 5. 总结
a) 核心思想：线性注意力与MoE结合实现超长上下文LLM（18字）
b) 速记 pipeline：32专家MoE → Lightning+Softmax 7:1混合 → 4M上下文 → 456B/45.9B
