# Mixture-of-Experts with Expert Choice Routing

**论文**: Mixture-of-Experts with Expert Choice Routing
**作者**: Yanqi Zhou, Tao Lei, Hanxiao Liu, Nan Du, Yanping Huang, Vincent Zhao, Andrew Dai, Zhifeng Chen, Quoc Le, James Laudon
**年份**: 2022
**来源**: NeurIPS 2022 (arXiv:2202.09368)
**标签**: MoE, 路由策略, Expert Choice

---

## 0. 摘要
本文提出"专家选择"（Expert Choice）路由策略：不再让 token 选择专家，而是让专家选择 token。这从根本上保证了负载均衡，同时允许不同 token 被不同数量的专家处理（异质路由），训练收敛速度比 Switch Transformer 和 GShard 快 2 倍以上。

## 1. 方法动机
a) 传统 Token-Choice 路由（token 选专家）天然导致负载不均：热门专家过载，冷门专家闲置。
b) 辅助损失虽然缓解了负载问题，但会干扰主任务的梯度信号。
c) 假设：如果让专家主动选择自己要处理的 token，负载均衡可以被结构性地保证。

## 2. 方法设计
a) Expert Choice 路由流程：
   - 计算所有 (token, expert) 对的亲和力得分矩阵
   - 每个专家从所有 token 中选择 top-k 个（k = 专家容量 = 总token数 / 专家数 * 容量因子）
   - 保证每个专家处理固定数量的 token → 完美负载均衡

b) 异质性优势：
   - 某些"重要"token 可能被多个专家选中 → 获得更多计算
   - 某些"简单"token 可能不被任何专家选中 → 仅通过残差连接
   - 自然实现了计算资源的自适应分配

c) 无需辅助损失：负载均衡是结构性保证的，不需要额外损失函数

## 3. 与其他方法对比
| 方法 | 优点 | 缺点 | 改进点 |
|------|------|------|--------|
| Top-1 (Switch) | 简单 | 负载不均，需辅助损失 | - |
| Top-2 (GShard) | 冗余性 | 通信开销大 | - |
| **Expert Choice** | **完美负载均衡+异质路由** | **无法用于自回归（因果性）** | **专家选 token** |

## 4. 实验表现
- 训练收敛速度比 Switch Transformer 提升 2x 以上
- 同计算量下在 GLUE/SuperGLUE 上性能更高
- 甚至超越了同规模的 T5 dense 模型（7/11任务）

## 5. 对 Channel Mixer 的意义
Expert Choice 是路由策略设计的重要创新，提出了"谁选谁"的新范式。但它主要适用于编码器或非自回归场景，在 decoder-only LLM（需保持因果性）中直接使用有困难。后续工作如 DeepSeek 系列在此基础上发展了更灵活的路由方案。

## 6. 总结
a) 核心思想：让专家选择token实现结构性负载均衡（16字）
b) 速记 pipeline：
   1. 计算所有 token-专家 亲和力矩阵
   2. 每个专家选择自己最匹配的 k 个 token
   3. 负载均衡自动保证，无需辅助损失
   4. 重要 token 可被多个专家处理（异质路由）
