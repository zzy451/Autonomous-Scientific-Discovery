# Hunyuan-Large: An Open-Source MoE Model with 52 Billion Activated Parameters by Tencent

**论文**: Hunyuan-Large: An Open-Source MoE Model with 52 Billion Activated Parameters by Tencent
**作者**: Tencent
**年份**: 2024
**来源**: arXiv:2411.02265
**标签**: MoE, 共享专家, expert-specific学习率, 大规模开源

---

## 0. 摘要
Hunyuan-Large 是腾讯推出的开源 MoE 模型，总参数 389B，激活参数 52B。采用共享专家 + Top-K 路由专家的架构，引入了 expert-specific 学习率等训练技巧。在发布时是最大的开源 Transformer-based MoE 模型。

## 1. 方法动机
a) 开源社区缺乏大规模 MoE 模型。
b) MoE 训练中专家利用率不均和训练不稳定是核心挑战。
c) 需要探索大规模 MoE 的训练技巧和最佳实践。

## 2. 方法设计（Channel Mixer 相关）
a) MoE 配置：
   - 389B 总参数，52B 激活参数
   - 共享专家 + Top-K 路由专家
   - 遵循 DeepSeekMoE 的细粒度专家设计

b) 训练技巧：
   - Expert-specific 学习率：不同专家使用不同的学习率，根据其利用率动态调整
   - 改进的负载均衡损失
   - 大规模分布式训练优化

c) 激活函数：SwiGLU

## 3. 与其他 MoE 模型对比
| 模型 | 总参/激活参 | 特色 |
|------|------------|------|
| DeepSeek-V2 | 236B/21B | MLA + 细粒度MoE |
| Mixtral 8x7B | 47B/13B | 简洁的8选2 |
| **Hunyuan-Large** | **389B/52B** | **Expert-specific LR, 最大开源MoE** |

## 4. 对 Channel Mixer 的意义
Hunyuan-Large 的 expert-specific 学习率是一个有价值的训练技巧，说明不同专家的优化动态可能不同，统一学习率可能不是最优的。这为 MoE 训练方法论提供了新的思路。

## 5. 总结
a) 核心思想：大规模开源MoE配合专家级学习率优化（17字）
b) 速记 pipeline：389B/52B MoE → 共享+路由专家 → expert-specific LR → 开源
