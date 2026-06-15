# DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model

**论文**: DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model
**作者**: DeepSeek-AI
**年份**: 2024
**来源**: arXiv:2405.04434
**标签**: MoE, 共享专家, 多头潜在注意力

---

## 0. 摘要
DeepSeek-V2 是 DeepSeek 系列的第二代 MoE 模型，结合了多头潜在注意力（MLA）和 DeepSeekMoE 架构。在保持高性能的同时，训练成本节省 42.5%，KV Cache 减少 93.3%，推理吞吐量提升 5.76 倍。

## 1. 方法动机
a) DeepSeek 67B（dense）的训练和推理成本过高。
b) 传统注意力的 KV Cache 是长上下文推理的内存瓶颈。
c) 假设：MoE（节省计算）+ MLA（节省内存）的组合可以大幅降低全链路成本。

## 2. 方法设计
a) MoE 架构（继承 DeepSeekMoE）：
   - 细粒度专家分割：大量小专家
   - 共享专家隔离：1-2个共享专家始终激活
   - 路由专家通过 Top-K 选择

b) 多头潜在注意力（MLA）[注：属于 Token Mixer 范畴]：
   - 将 KV 压缩为低秩潜在向量
   - 推理时只缓存压缩后的潜在向量
   - KV Cache 压缩 93.3%

c) Channel Mixer 维度的核心贡献：
   - 继承并验证了 DeepSeekMoE 的细粒度+共享专家设计在更大规模上的有效性
   - 证明了 MoE 不仅能降低训练成本，还能大幅优化推理效率

## 3. 与其他方法对比
| 方法 | 训练成本 | 推理成本 | 性能 |
|------|----------|----------|------|
| DeepSeek 67B (dense) | 基线 | 基线 | 基线 |
| Mixtral 8x7B | 低 | 低 | 略低于 DeepSeek 67B |
| **DeepSeek-V2** | **-42.5%** | **5.76x 吞吐** | **更好** |

## 4. 实验表现
- 在多个中英文基准上超越 DeepSeek 67B
- 与 Mixtral 8x7B 相当或更好
- 支持 128K 上下文
- 极大降低了服务成本

## 5. 对 Channel Mixer 的意义
DeepSeek-V2 是 DeepSeekMoE 设计哲学的大规模验证，证明了细粒度专家+共享专家在百亿参数级别的有效性。该架构直接演进为 DeepSeek-V3，后者在综述中已引用。

## 6. 总结
a) 核心思想：MoE+MLA双管齐下大幅降低训练推理成本（18字）
b) 速记 pipeline：
   1. FFN 使用 DeepSeekMoE（细粒度+共享专家）
   2. 注意力使用 MLA 压缩 KV Cache
   3. 训练成本节省 42.5%
   4. 推理吞吐提升 5.76 倍
