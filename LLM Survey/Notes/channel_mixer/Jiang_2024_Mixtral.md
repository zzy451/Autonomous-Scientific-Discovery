# Mixtral of Experts

**论文**: Mixtral of Experts
**作者**: Albert Q. Jiang, Alexandre Sablayrolles, Antoine Roux, et al. (Mistral AI)
**年份**: 2024
**来源**: arXiv:2401.04088
**标签**: MoE, 开源LLM, Top-2 路由

---

## 0. 摘要
Mixtral 8x7B 是基于 Mistral 7B 架构的稀疏 MoE 模型，每层有 8 个 FFN 专家，每个 token 激活 2 个。总参数 47B，活跃参数仅 13B，在多个基准上超越 LLaMA 2 70B 和 GPT-3.5。

## 1. 方法动机
a) Dense 模型扩展需要成比例增加计算量，成本过高。
b) 之前的开源 MoE LLM 较少，社区缺乏高质量开源 MoE 基线。
c) 假设：在已验证的高质量 dense 架构（Mistral 7B）基础上引入 MoE，可以以较低成本获得更大模型的性能。

## 2. 方法设计
a) 架构：
   - Decoder-only Transformer
   - 每个 Transformer 层的 FFN 替换为 8 个 FFN 专家
   - 路由器选择 Top-2 专家
   - 输出是 2 个被选专家输出的加权和

b) 路由器：
   - 线性层 + softmax
   - Top-2 选择 + 归一化权重
   - 无明确提及特殊的负载均衡策略

c) 其他设计：
   - 32K 上下文窗口
   - Sliding Window Attention
   - SwiGLU 激活函数
   - 分组查询注意力（GQA）

## 3. 与其他方法对比
| 方法 | 总参数 | 活跃参数 | 性能 |
|------|--------|----------|------|
| LLaMA 2 70B | 70B | 70B | 基线 |
| GPT-3.5 | ~175B | ~175B | 参考 |
| **Mixtral 8x7B** | **47B** | **13B** | **超越两者** |

## 4. 实验表现
- 在大部分基准上超越 LLaMA 2 70B（数学、代码、多语言尤其突出）
- 推理速度比 LLaMA 2 70B 快 6 倍
- 在法语、德语等多语言任务上表现优异
- Apache 2.0 开源许可

## 5. 对 Channel Mixer 的意义
Mixtral 是第一个广泛使用的开源 MoE LLM，验证了 MoE 在 decoder-only LLM 中的实际效果。它的成功推动了 MoE 在开源社区的普及，影响了 DBRX、OLMoE 等后续工作。Top-2 路由+8专家的设计成为行业参考配置。

## 6. 总结
a) 核心思想：8专家Top-2路由实现高效大模型推理（15字）
b) 速记 pipeline：
   1. 基于 Mistral 7B 架构
   2. FFN 替换为 8 个 FFN 专家
   3. 路由器选 Top-2 专家加权输出
   4. 47B 总参数仅 13B 活跃，超越 70B dense 模型
