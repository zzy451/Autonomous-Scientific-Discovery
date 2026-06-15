# ST-MoE: Designing Stable and Transferable Sparse Expert Models

**论文**: ST-MoE: Designing Stable and Transferable Sparse Expert Models
**作者**: Barret Zoph, Irwan Bello, Sameer Kumar, Nan Du, Yanping Huang, Jeff Dean, Noam Shazeer, William Fedus
**年份**: 2022
**来源**: arXiv:2202.08906 / IEEE IPDPSW 2022
**标签**: MoE, 训练稳定性, 迁移学习

---

## 0. 摘要
ST-MoE 系统性地研究了稀疏 MoE 模型的训练稳定性和微调迁移性问题。提出多种稳定化技术，成功训练了 269B 参数的稀疏模型（ST-MoE-32B），在多个 NLP 任务上达到 SOTA。

## 1. 方法动机
a) 虽然 Switch Transformer 和 GShard 证明了 MoE 的扩展能力，但训练不稳定和微调质量不一致仍是核心问题。
b) MoE 模型在预训练时容易出现损失尖峰（loss spikes），微调时泛化能力不如 dense 模型。
c) 假设：通过系统性的设计指南可以构建既稳定又可迁移的稀疏模型。

## 2. 方法设计
a) 稳定化技术：
   - 移除乘性交互：简化路由器设计
   - 噪声注入策略分析
   - 激活/梯度约束
   - 精度格式选择（路由器使用 float32）

b) 架构设计：
   - 269B 参数稀疏编码器-解码器模型
   - 计算成本等效于 32B dense 模型
   - 每层使用 MoE 替换 FFN

c) 迁移学习优化：
   - 分析 MoE 模型在微调时的行为
   - 提出调整辅助损失系数的策略
   - 确保稀疏模型在下游任务上的迁移质量

## 3. 与其他方法对比
| 方法 | 优点 | 缺点 | 改进点 |
|------|------|------|--------|
| Switch Transformer | 简单高效 | 训练不稳定 | - |
| GShard | 大规模验证 | 微调质量不保证 | - |
| **ST-MoE** | **稳定+可迁移** | **设计规则多** | **系统性设计指南** |

## 4. 实验表现
- SuperGLUE、ARC 等推理基准上达到 SOTA
- 摘要和闭卷问答任务表现优异
- 训练稳定性明显提升，损失尖峰减少

## 5. 对 Channel Mixer 的意义
ST-MoE 提供了实用的 MoE 训练稳定性指南，解决了稀疏模型从预训练到微调的全链路质量问题。其经验性结论（如路由器精度、辅助损失调整等）被后续 MoE 工作广泛采用。

## 6. 总结
a) 核心思想：系统性解决MoE训练稳定性和迁移问题（17字）
b) 速记 pipeline：
   1. 分析 MoE 训练中的不稳定因素
   2. 提出精度控制、噪声策略等稳定化技术
   3. 训练 269B 稀疏模型验证
   4. 在下游任务上验证迁移学习质量
