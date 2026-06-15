# Attention Residuals (AttnRes)

**论文信息**: Kimi Team (Moonshot AI) (2026)
**arXiv**: 2603.15031
**分类**: Depth (深度注意力残差)

## 核心思想
AttnRes 用 **depth-wise softmax attention** 替代标准的固定权重残差累加。每一层对之前所有层的输出进行注意力加权聚合（而非简单相加），实现动态的、输入依赖的跨层信息选择。

## 问题诊断: PreNorm Dilution
- 标准 PreNorm 以固定单位权重累积所有层的输出：x_L = x_0 + sum F_l(x_l)
- 随着深度增加：(1) 隐状态幅度不受控增长；(2) 早期层的贡献被稀释
- 这就是 "PreNorm Dilution" 问题

## 数学公式
标准 PreNorm: x_{l+1} = x_l + F(LN(x_l))  （固定权重 1）
AttnRes: x_{l+1} = sum_{i=0}^{l} alpha_i * h_i, 
  其中 alpha_i = softmax(q_l^T * k_i / sqrt(d))

## Block AttnRes (实用版本)
- Full AttnRes 的计算复杂度 O(L^2)，内存 O(Ld)
- **Block AttnRes**: 将 L 层分成 N 个 block，block 内使用标准残差，block 间使用注意力聚合
- 内存开销从 O(Ld) 降至 O(Nd)

## 关键机制
- **动态选择性聚合**: 每层通过注意力权重选择性地利用前序层的输出
- **幅度控制**: softmax 归一化天然约束了权重总和为 1，防止隐状态爆炸
- **Block 分层**: 在 Full 和 None 之间取折中，平衡性能与效率
- **梯度均匀化**: 更均匀的梯度分布有助于深层模型的优化

## 实验结果
- 集成到 Kimi Linear (48B参数, 3B激活) 模型中
- 在 1.4T token 上训练，推理/编程/长上下文基准上一致提升
- 约 1.25x 计算效率增益
- 隐状态幅度保持有界，梯度分布更均匀

## 与综述的关联
属于 **Depth** 维度的最新进展。代表了"注意力残差"方向的工业级实践，解决了 PreNorm Dilution 这一长期存在的问题。Block AttnRes 的分层策略是一个重要的工程贡献。

## 核心贡献
用深度softmax注意力替代固定权重残差累加，从根本上解决 PreNorm 稀释问题，并通过 Block 策略实现实用化。
