# DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models

**论文**: DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models
**作者**: Damai Dai, Chengqi Deng, Chenggang Zhao, R.X. Xu, Huazuo Gao, et al.
**年份**: 2024
**来源**: ACL 2024 (arXiv:2401.06066)
**标签**: MoE, 细粒度专家, 共享专家

---

## 0. 摘要
DeepSeekMoE 提出两个核心策略来提升 MoE 专家的专业化程度：细粒度专家分割（Fine-Grained Expert Segmentation）和共享专家隔离（Shared Expert Isolation）。DeepSeekMoE 16B 用约 40% 的计算量达到了 DeepSeek 7B / LLaMA2 7B 的性能水平。

## 1. 方法动机
a) 传统 MoE 使用少量大专家，每个专家承载的知识过于混杂（knowledge hybridity），难以专业化。
b) 不同专家独立学习相同的共性知识，导致参数冗余（knowledge redundancy）。
c) 假设：将专家切分得更细+隔离出共享专家可以同时解决上述两个问题。

## 2. 方法设计
a) 细粒度专家分割：
   - 不用少量大专家（如 8 个），而是将 FFN 中间维度切分为大量小专家（如 64 个）
   - 每个 token 仍然激活相同总计算量（如选择 8 个小专家 = 1 个大专家的计算量）
   - 更多小专家 → 组合更灵活 → 知识分解更精细

b) 共享专家隔离：
   - 划出一部分专家作为"共享专家"，对所有 token 始终激活
   - 共享专家负责捕获和巩固各类输入的共性知识
   - 剩余的路由专家专注于学习特定、差异化的知识
   - 减少了路由专家间的知识冗余

c) 路由机制：
   - 对路由专家使用标准 Top-K 路由
   - 共享专家始终参与计算（不经过路由选择）
   - 最终输出 = 共享专家输出 + 路由专家加权输出

## 3. 与其他方法对比
| 方法 | 专家数 | 共享专家 | 知识冗余 | 专业化程度 |
|------|--------|----------|----------|------------|
| GShard | 少（如8） | 无 | 高 | 低 |
| Switch | 少~中 | 无 | 中 | 中 |
| Mixtral | 8 | 无 | 中 | 中 |
| **DeepSeekMoE** | **多（如64）** | **有** | **低** | **高** |

## 4. 实验表现
- DeepSeekMoE 16B（2.8B 活跃参数）≈ DeepSeek 7B / LLaMA2 7B 的性能
- 仅用约 40% 的计算量
- 在知识密集型任务上表现尤其好（专家更专业化）
- 145B 规模验证也一致

## 5. 对 Channel Mixer 的意义
DeepSeekMoE 的两大创新（细粒度专家 + 共享专家）被直接继承到 DeepSeek-V2 和 DeepSeek-V3，成为 DeepSeek 系列的核心架构特色。DBRX 也采用了类似的细粒度专家设计（16专家选4）。这两个思想是2024年 MoE 领域最有影响力的设计贡献之一。

## 6. 总结
a) 核心思想：细粒度小专家+共享专家提升MoE专业化（18字）
b) 速记 pipeline：
   1. 将大 FFN 专家拆分为大量小专家
   2. 隔离出始终激活的共享专家
   3. 路由专家通过 Top-K 选择
   4. 共享专家捕获通用知识，路由专家专攻差异化知识
