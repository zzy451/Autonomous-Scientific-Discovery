# Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer

**论文**: Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer
**作者**: Noam Shazeer, Azalia Mirhoseini, Krzysztof Maziarz, Andy Davis, Quoc Le, Geoffrey Hinton, Jeff Dean
**年份**: 2017
**来源**: ICLR 2017
**标签**: MoE, 条件计算, 稀疏门控

---

## 0. 摘要
本文将 MoE 思想引入深度学习大规模训练，提出稀疏门控 MoE 层。通过可训练的门控网络动态选择少量专家处理每个输入，实现模型容量（参数量）的大幅扩展而不显著增加计算成本。在语言建模和机器翻译任务上展示了高达 1370 亿参数的模型。

## 1. 方法动机
a) 神经网络的吸收能力（capacity）受限于参数量，但增加参数量通常意味着计算量线性增长。
b) 条件计算（Conditional Computation）的思想很早就有，但之前缺乏实际可行的大规模实现。
c) 假设：通过门控网络只激活少数专家，可以在参数量（容量）和计算量之间解耦。

## 2. 方法设计
a) MoE 层的核心流程：
   - 输入 token 表示 x
   - 门控网络 G(x) 计算每个专家的权重（使用 softmax + 噪声 + top-k 选择）
   - 只有权重非零的专家（top-k）被实际激活
   - 输出 y = Σ_{i∈top-k} G(x)_i * E_i(x)

b) 门控设计关键：
   - 加入可训练噪声以增加探索
   - 使用 top-k 选择（论文中 k=2 或 k=4）实现稀疏性
   - 辅助损失函数（auxiliary loss）鼓励负载均衡

c) 辅助损失：引入 importance loss 和 load loss，防止门控网络只偏好少数专家（"赢者通吃"问题）

## 3. 与其他方法对比
| 方法 | 优点 | 缺点 | 改进点 |
|------|------|------|--------|
| Dense Transformer | 训练稳定 | 参数和计算线性相关 | - |
| Jacobs 1991 MoE | 理论优雅 | 规模小，所有专家都激活 | - |
| **稀疏门控 MoE** | **参数量与计算量解耦** | **负载不均衡、训练不稳定** | **辅助损失+噪声门控** |

## 4. 实验表现
- 在语言建模上，MoE 模型以更少的计算量超越了当时最大的 LSTM 模型
- 在机器翻译上，1370亿参数 MoE 模型以同样计算成本大幅超过 dense 基线
- 验证了稀疏激活的可行性和有效性

## 5. 对 Channel Mixer 的意义
这是将 MoE 引入现代深度学习的里程碑论文。核心创新：
- 稀疏门控（Sparse Gating）使大规模 MoE 可行
- 辅助损失（Auxiliary Loss）解决负载均衡
- 为后续所有 MoE 工作（GShard, Switch Transformer, Mixtral, DeepSeek 系列）奠定基础

## 6. 总结
a) 核心思想：稀疏门控只激活少数专家以解耦容量与计算量（20字）
b) 速记 pipeline：
   1. 门控网络为每个输入计算专家权重
   2. 加噪声 + top-k 选择实现稀疏激活
   3. 只计算被选中的少数专家
   4. 辅助损失保证各专家均匀使用
