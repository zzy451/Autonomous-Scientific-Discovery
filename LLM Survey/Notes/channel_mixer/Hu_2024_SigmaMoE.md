# Sigma-MoE-Tiny Technical Report

**论文**: Sigma-MoE-Tiny Technical Report
**作者**: Qingguo Hu, Zhenghao Lin, Ziyue Yang, Yucheng Ding, Xiao Liu, Yuting Jiang, Ruizhe Wang, Tianyu Chen, Zhongxin Guo, Yifan Xiong, Rui Gao, Lei Qu, Jinsong Su, Peng Cheng, Yeyun Gong
**年份**: 2024
**来源**: arXiv:2512.16248
**标签**: MoE, sigmoid 门控, 超稀疏, 负载均衡, 细粒度专家

---

## 0. 摘要
Sigma-MoE-Tiny 是一个超稀疏 MoE 语言模型，总参数 20B，每 token 仅激活 0.5B 参数（40:1 稀疏比）。每层最多 96 个专家，每 token 仅路由到 1 个专家。采用 sigmoid 门控函数替代传统 softmax 门控，配合细粒度专家分割和专门的负载均衡策略，在极端稀疏条件下实现了有竞争力的语言建模性能。

## 1. 方法动机
a) 传统 MoE 使用 softmax 门控，专家权重之间存在竞争关系（零和博弈），限制了路由灵活性。
b) 超稀疏场景（top-1 路由 + 大量专家）下，softmax 门控的负载均衡问题更加严重，需要辅助损失来缓解。
c) 假设：sigmoid 门控允许每个专家独立评分，打破专家间的竞争耦合，在超稀疏 MoE 中可以获得更好的路由质量和负载均衡。

## 2. 方法设计
a) 核心架构：
   - 56 层 decoder-only Transformer
   - 隐藏维度 d=1536，GQA（16 头），QK-Norm，RMSNorm
   - 每层 96 个细粒度专家，每 token 激活 1 个（top-1 路由）

b) Sigmoid 门控机制：
   - 路由分数 g_i = σ(x · w_i)，每个专家独立计算 sigmoid 分数
   - 选择分数最高的 1 个专家
   - 与 softmax 不同：各专家分数不需要归一化求和为 1
   - 优势：消除专家间的竞争耦合，允许更灵活的路由决策

c) 负载均衡：
   - 采用 per-token FP32 路由精度保证路由稳定性
   - 专门的负载均衡策略应对 96 专家 top-1 的极端稀疏场景

## 3. 与其他方法对比
| 方法 | 门控函数 | 专家数/激活数 | 稀疏比 | 特点 |
|------|----------|---------------|--------|------|
| Switch Transformer | softmax top-1 | 少量专家 | 低 | 需要辅助损失 |
| Mixtral | softmax top-2 | 8/2 | 4:1 | 标准稀疏 |
| DeepSeek-V3 | sigmoid + top-K | 256/8 | 高 | 也用 sigmoid |
| **Sigma-MoE-Tiny** | **sigmoid top-1** | **96/1** | **40:1** | **超稀疏，独立评分** |

## 4. 实验表现
- 20B 总参数，0.5B 激活参数
- 在极端稀疏比（40:1）下仍保持有竞争力的语言建模性能
- Sigmoid 门控在超稀疏场景下比 softmax 门控表现更稳定
- 细粒度专家分割（96 专家）有效提升了模型容量利用率

## 5. 对 Channel Mixer 的意义
Sigma-MoE 代表了 MoE 门控函数从 softmax 向 sigmoid 演进的重要趋势。sigmoid 门控允许专家独立评分，打破了 softmax 的零和约束，这一思路也被 DeepSeek-V3 等模型采用。在超稀疏 MoE 场景下，sigmoid 门控展现出更好的路由质量和负载均衡特性，是 MoE channel mixer 设计的重要方向。

## 6. 总结
a) 核心思想：sigmoid 独立门控实现超稀疏 MoE 路由（15字）
b) 速记 pipeline：
   1. 每层设置 96 个细粒度专家
   2. 用 sigmoid 独立计算每个专家的路由分数
   3. 选择分数最高的 1 个专家处理 token
   4. 打破 softmax 零和约束，提升超稀疏场景路由质量
