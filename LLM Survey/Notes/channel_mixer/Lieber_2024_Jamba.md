# Jamba: A Hybrid Transformer-Mamba Language Model

**论文**: Jamba: A Hybrid Transformer-Mamba Language Model
**作者**: Opher Lieber, Barak Lenz, Hofit Bata, et al. (AI21 Labs)
**年份**: 2024
**来源**: arXiv:2403.19887
**标签**: MoE, 混合架构, Mamba+Transformer

---

## 0. 摘要
Jamba 是一个混合架构模型，将 Transformer 层、Mamba 层（状态空间模型）和 MoE 层三者结合。通过交错使用不同类型的层，在保持高质量的同时大幅降低内存占用和提升推理吞吐量，支持 256K 上下文窗口。

## 1. 方法动机
a) 纯 Transformer 在长上下文场景下 KV Cache 内存占用巨大。
b) 纯 Mamba/SSM 在某些推理任务上表现不如 Transformer。
c) 假设：混合三种架构可以取长补短——Transformer 提供推理质量，Mamba 提供内存效率，MoE 提供参数效率。

## 2. 方法设计
a) 层类型交错：
   - 模型由 Transformer Block 和 Mamba Block 交替组成
   - Transformer 层提供精确的注意力机制
   - Mamba 层以线性复杂度处理序列
   - 比例可调（如每隔几个 Mamba 层插入一个 Transformer 层）

b) MoE 集成：
   - 部分层（通常是 Transformer 层中的 FFN）使用 MoE 替换
   - 增加参数量但不增加计算量

c) Jamba 1.5 Large：
   - 总参数 398B，活跃参数 94B
   - 支持 256K 上下文
   - 可在单 80GB GPU 上运行

## 3. 与其他方法对比
| 方法 | 序列处理 | 内存效率 | 参数效率 |
|------|----------|----------|----------|
| 纯 Transformer | 注意力 | 低（KV Cache 大） | 低（dense） |
| 纯 Mamba | SSM | 高 | 低（dense） |
| **Jamba** | **混合** | **高** | **高（MoE）** |

## 4. 实验表现
- 长上下文任务（256K）表现优异
- KV Cache 大幅减少
- 吞吐量显著优于同参数级别的纯 Transformer
- 在多个标准 NLP 基准上与 Mixtral 8x7B 竞争

## 5. 对 Channel Mixer 的意义
Jamba 展示了 MoE 不仅可以在纯 Transformer 中使用，也可以与 SSM/Mamba 等非注意力架构结合。这拓展了 Channel Mixer 的设计空间——FFN/MoE 层可以出现在任何类型的 Token Mixer 之后。

## 6. 总结
a) 核心思想：Transformer+Mamba+MoE三合一混合架构（17字）
b) 速记 pipeline：
   1. 交错使用 Transformer 和 Mamba 层
   2. 部分 FFN 层替换为 MoE
   3. 组合获得注意力精度+线性内存+参数效率
   4. 支持 256K 上下文，单 GPU 可部署
