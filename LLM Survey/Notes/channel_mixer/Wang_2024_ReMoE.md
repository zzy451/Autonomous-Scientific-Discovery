# ReMoE: Fully Differentiable Mixture-of-Experts with ReLU Routing

**论文**: ReMoE: Fully Differentiable Mixture-of-Experts with ReLU Routing
**作者**: Ziteng Wang, Jianfei Chen, Jun Zhu (清华大学)
**年份**: 2024 (ICLR 2025)
**来源**: arXiv:2412.14711
**标签**: MoE, 全可微, ReLU 路由, TopK 替代

---

## 0. 摘要
ReMoE 提出用 ReLU 激活函数替代传统的 TopK+Softmax 路由机制，实现全可微的 MoE 架构。ReLU 天然产生稀疏输出（负值归零），无需离散的 Top-K 选择即可实现稀疏专家激活。ReMoE 是传统 TopK MoE 的简单 drop-in 替代，在多种规模和专家数量下一致优于 vanilla TopK 路由，并展现出更好的专家数量扩展性。

## 1. 方法动机
a) TopK+Softmax 路由的核心问题：Top-K 操作是不可微的，梯度只能流过被选中的专家，未被选中的专家得不到梯度信号。
b) 这导致"富者愈富"现象：被频繁选中的专家持续优化，不被选中的专家停滞，最终导致专家坍缩。
c) 辅助损失虽然缓解了负载不均，但引入了与主任务冲突的梯度干扰。
d) 假设：ReLU 天然产生稀疏输出，可以替代 Top-K 实现稀疏路由，同时保持全可微性。

## 2. 方法设计
a) 核心路由机制：
   - 传统: g(x) = TopK(Softmax(x · W_r))  — 不可微
   - ReMoE: g(x) = ReLU(x · W_r)  — 全可微
   - ReLU 自然将负值置零 → 对应专家不被激活 → 实现稀疏性
   - 正值专家的路由权重直接作为加权系数

b) 稀疏性控制（关键挑战）：
   - 纯 ReLU 路由无法精确控制激活专家数量（可能太多或太少）
   - 引入可学习的 bias 项: g(x) = ReLU(x · W_r + b)
   - 通过动态调整 bias 控制平均激活专家数量接近目标值 K
   - 类似于 Aux-Loss-Free 的 bias 调整策略

c) 负载均衡：
   - ReLU 路由天然比 TopK 更均衡（梯度流向所有专家）
   - 仍可选择性地加入轻量级均衡约束
   - 实验表明即使不加辅助损失，ReMoE 的负载均衡也优于 TopK+aux loss

## 3. 与其他方法对比
| 方法 | 路由函数 | 可微性 | 稀疏性 | 负载均衡 |
|------|----------|--------|--------|----------|
| TopK+Softmax | 离散选择 | 不可微 | 精确 K 个 | 需辅助损失 |
| Soft MoE | 软加权 | 全可微 | 无稀疏 | 天然 |
| Lory | 参数合并 | 全可微 | 无稀疏 | 天然 |
| **ReMoE** | **ReLU** | **全可微** | **近似 K 个** | **天然较好** |

## 4. 实验表现
- 在 1B-7B 参数规模上，ReMoE 一致优于 TopK MoE（perplexity 降低 0.3-0.8）
- 专家扩展性：从 8 到 64 专家，ReMoE 的性能增益持续增长，而 TopK MoE 在 32+ 专家时趋于饱和
- 无需辅助损失即可实现良好的负载均衡
- 训练稳定性优于 TopK MoE（无路由坍缩现象）
- 推理时可将 ReLU 路由转换为近似 TopK 以获得精确的稀疏性

## 5. 对 Channel Mixer 的意义
ReMoE 提供了一个极其简洁的全可微 MoE 方案：仅将 TopK+Softmax 替换为 ReLU，就同时解决了可微性、负载均衡和专家坍缩问题。与 Soft MoE（需要 slot 机制）和 Lory（需要参数合并）相比，ReMoE 的改动最小、最容易集成到现有 MoE 框架中。其与 ReLU² 稀疏性工作的联系也值得注意：ReLU 在路由层面和激活层面都展现出稀疏性的优势。

## 6. 总结
a) 核心思想：用 ReLU 替代 TopK 路由，实现全可微稀疏 MoE（19字）
b) 速记 pipeline：
   1. 路由分数 = ReLU(x · W_r + b)
   2. ReLU 天然置零负值 → 稀疏激活
   3. 动态调整 bias 控制平均激活专家数
   4. 全可微，无需辅助损失，扩展性优于 TopK
