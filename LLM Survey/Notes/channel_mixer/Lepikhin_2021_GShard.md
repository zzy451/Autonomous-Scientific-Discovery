# GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding

**论文**: GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding
**作者**: Dmitry Lepikhin, HyoukJoong Lee, Yuanzhong Xu, Dehao Chen, Orhan Firat, Yanping Huang, Maxim Krikun, Noam Shazeer, Zhifeng Chen
**年份**: 2021
**来源**: ICLR 2021
**标签**: MoE, 分布式训练, Top-2 路由

---

## 0. 摘要
GShard 提出了一套轻量级注解 API 与 XLA 编译器集成的方案，实现大规模 MoE 模型的自动分片（sharding）。使用 Top-2 专家选择策略和 SPMD 编程模型，成功训练了 6000 亿参数的多语言机器翻译模型。

## 1. 方法动机
a) 大规模模型训练需要跨多设备分片，但手工编写并行代码极其困难。
b) 现有分片方案缺乏灵活性，无法自动处理条件计算（MoE）中的不规则通信模式。
c) 假设：通过编译器级别的自动分片+MoE 条件计算，可以让研究者用简单的注解就实现超大规模训练。

## 2. 方法设计
a) 系统架构：
   - 研究者在模型代码中添加轻量级分片注解
   - XLA 编译器根据注解自动生成 SPMD 并行代码
   - MoE 层使用 Top-2 路由：每个 token 选择 2 个专家

b) MoE 路由机制：
   - 门控网络输出 softmax 概率
   - 每个 token 选择概率最高的 2 个专家
   - 输出是这 2 个专家输出的加权和
   - 使用容量因子（capacity factor）限制每个专家的最大负载

c) 负载均衡：辅助损失促进均匀分配，超出容量的 token 被丢弃（token dropping）

## 3. 与其他方法对比
| 方法 | 优点 | 缺点 | 改进点 |
|------|------|------|--------|
| Shazeer 2017 MoE | 证明稀疏可行 | 工程实现复杂 | - |
| 手工模型并行 | 灵活 | 开发成本极高 | - |
| **GShard** | **自动分片+MoE** | **Top-2 仍有负载不均** | **编译器自动化** |

## 4. 实验表现
- 6000亿参数模型在 2048 TPU v3 上仅用 4 天训练完成
- 多语言翻译（100语言到英语）显著超越之前 SOTA
- 验证了自动分片对超大规模训练的实用性

## 5. 对 Channel Mixer 的意义
GShard 确立了 Top-2 路由作为 MoE 的标准范式，引入了容量因子和 token dropping 的概念。同时展示了 MoE 在工业级系统中的工程实现路径，影响了后续 Switch Transformer 和 Mixtral 等工作。

## 6. 总结
a) 核心思想：编译器自动分片实现超大规模MoE训练（17字）
b) 速记 pipeline：
   1. 研究者在模型中添加分片注解
   2. XLA 编译器自动生成并行代码
   3. MoE 层 Top-2 路由选专家
   4. 容量因子限制负载，辅助损失促均衡
