# iRoPE: Interleaved RoPE (Llama 4)
**作者**: Meta AI (Llama Team) | **年份**: 2025 | **arxiv**: 2601.11659

## 0. 摘要翻译
Llama 4 是 Meta 于 2025 年 4 月发布的基础模型系列，包括 Scout（16 专家）和 Maverick（128 专家）。其核心位置编码创新为 iRoPE（interleaved Rotary Position Embedding），通过交替使用带 RoPE 的注意力层和不带位置编码（NoPE）的注意力层，实现了高达 10M token 的上下文窗口，同时保持模型在短上下文任务上的性能。

## 1. 方法动机
- 标准 RoPE 在所有层施加相对位置编码，导致长距离 token 间的注意力分数因高频旋转而快速衰减，限制了有效上下文长度
- 纯 NoPE（无位置编码）模型虽然理论上不受位置限制，但缺乏位置感知能力，在需要精确位置信息的任务上表现不佳
- iRoPE 的核心洞察：并非每一层都需要位置信息。部分层可以作为"语义层"自由地关注全局上下文，而其他层负责提供位置感知

## 2. 方法设计（重点：与六维度框架的关联）

### 架构设计
- **交替策略**: 在 Transformer 的层堆叠中，交替使用 RoPE 层和 NoPE 层
  - RoPE 层：使用标准 RoPE 旋转位置编码，配合局部注意力掩码（local attention mask），关注局部上下文
  - NoPE 层：不施加任何位置编码，使用全局注意力掩码（global attention mask），可自由关注整个上下文窗口中的所有 token
- **注意力温度缩放**: NoPE 层引入推理时温度缩放因子（inference-time temperature scaling），在推理阶段对注意力 logits 进行缩放，以适应训练时未见过的超长序列长度
- **渐进式上下文扩展**: 训练分阶段进行，逐步增加上下文长度（如从 256K 扩展到 10M），每阶段微调 iRoPE 的温度参数

### 与六维度框架的关联
- **位置编码维度**: iRoPE 是 RoPE 的直接演进，属于相对位置编码的混合变体
- **Token Mixer 维度**: NoPE 层的全局注意力 + RoPE 层的局部注意力构成了一种隐式的混合注意力模式，类似于 local-global attention 的设计思路
- **长度外推**: 通过 NoPE 层消除位置编码对长度的硬约束，配合温度缩放实现训练-推理长度的解耦

### 关键超参数（Scout 模型）
- 总参数: 109B（17B 激活），16 专家
- 上下文窗口: 10M tokens
- 层数: 80 层，交替 RoPE/NoPE

## 3. 与其他方法对比
| 方法 | 位置编码 | 最大上下文 | 长度外推策略 |
|------|---------|-----------|-------------|
| RoPE (Llama 3) | 全层 RoPE | 128K | 频率缩放 |
| ALiBi | 线性偏置 | ~8K | 天然外推但性能有限 |
| YaRN | 修改 RoPE 频率 | ~128K | NTK-aware 插值 |
| iRoPE (Llama 4) | 交替 RoPE+NoPE | 10M | NoPE 全局注意力 + 温度缩放 |

- 相比纯 RoPE 扩展方法（PI、NTK、YaRN），iRoPE 从架构层面解决问题，而非仅修改频率参数
- 相比 LongRoPE 等方法，iRoPE 更简洁，不需要搜索每个维度的缩放因子

## 4. 实验表现
- Scout（10M 上下文）在 RULER 等长上下文基准上表现优异，能有效利用超长上下文
- 在标准短上下文基准（MMLU、HumanEval 等）上，iRoPE 不损害模型性能
- Maverick（128 专家，1M 上下文）在多模态和文本任务上达到同级别模型的领先水平
- 推理时温度缩放使得模型可以在不重新训练的情况下适应不同长度的输入

## 5. 总结
a) iRoPE 通过交替 RoPE 和 NoPE 层，让部分层自由关注全局上下文，配合推理时温度缩放，实现了 10M token 的上下文窗口。

b) 速记 pipeline: Input → [RoPE Layer (local attn) ↔ NoPE Layer (global attn)] × N → temperature scaling at inference → 10M context
