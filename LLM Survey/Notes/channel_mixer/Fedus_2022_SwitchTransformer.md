# Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity

**论文**: Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity
**作者**: William Fedus, Barret Zoph, Noam Shazeer
**年份**: 2022
**来源**: JMLR 2022 (arXiv:2101.03961)
**标签**: MoE, Top-1 路由, 万亿参数

---

## 0. 摘要
Switch Transformer 简化了 MoE 路由策略，证明 Top-1 路由（每个 token 只选择 1 个专家）即可取得优异表现，无需 Top-2。该简化降低了通信开销、简化了实现，并成功将模型扩展到万亿参数规模。

## 1. 方法动机
a) 之前的 MoE 工作（GShard, Shazeer 2017）使用 Top-2 或更多专家，增加了通信和计算开销。
b) MoE 模型训练不稳定是阻碍其广泛使用的主要因素。
c) 假设：将路由简化为 Top-1 可以在降低复杂度的同时保持甚至提升性能。

## 2. 方法设计
a) Switch 层（替换 FFN）：
   - 输入 token x → 路由器计算每个专家的得分
   - 选择得分最高的 1 个专家（Top-1）
   - 仅该专家处理 token，输出乘以路由器权重

b) 关键设计：
   - 容量因子（Capacity Factor）：控制每个专家的缓冲区大小
   - 溢出 token 通过残差连接直接传递（token dropping）
   - 简化的负载均衡损失：L_balance = α * N * Σ f_i * P_i

c) 训练稳定性技巧：
   - 使用 bfloat16 精度
   - 路由器计算使用 float32 确保精度
   - 专家 dropout
   - 初始化方案调整

## 3. 与其他方法对比
| 方法 | 优点 | 缺点 | 改进点 |
|------|------|------|--------|
| GShard Top-2 | 每个 token 有2个专家冗余 | 通信开销大 | - |
| Dense Transformer | 训练稳定 | 参数和计算耦合 | - |
| **Switch (Top-1)** | **最简单的稀疏路由** | **单专家无冗余** | **7x 预训练加速** |

## 4. 实验表现
- 与 T5-Base 相比，预训练速度提升 7 倍
- 万亿参数模型成功训练
- 在多个 NLP 基准上超越 T5-XXL
- 下游微调表现稳定

## 5. 对 Channel Mixer 的意义
Switch Transformer 证明了 Top-1 路由的可行性和效率优势，大幅简化了 MoE 的设计范式。其提出的负载均衡损失公式 L = α * N * Σ f_i * P_i 成为后续工作的标准参考。

## 6. 总结
a) 核心思想：Top-1路由简化MoE实现万亿参数扩展（16字）
b) 速记 pipeline：
   1. FFN 替换为多个专家 FFN
   2. 路由器为每个 token 选择 1 个最佳专家
   3. 容量因子控制专家负载上限
   4. 辅助损失保证负载均衡
   5. 混合精度训练保障稳定性
