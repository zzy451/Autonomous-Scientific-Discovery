# Stabilizing Transformers for Reinforcement Learning (GTrXL)

**论文信息**: Parisotto, E., Song, H.F., et al. (2019/2020)
**arXiv**: 1910.06764 | **会议**: ICML 2020
**分类**: Control (门控残差连接)

## 核心思想
将标准残差连接替换为 **GRU 风格的门控机制**，以解决 Transformer 在强化学习中的训练不稳定问题。

## 两个关键修改
1. **修改 LayerNorm 位置**: 仅对残差块的输入流（非 shortcut 流）做归一化
   - 原始输入可以无损流过网络
2. **门控残差连接**: 用 GRU 门控替代简单加法
   - r = sigmoid(W_r * y + U_r * x)
   - z = sigmoid(W_z * y - b)  (b 为偏置, 使初始时倾向于通过)
   - h_hat = tanh(W_h * y + U_h * (r * x))
   - g(x, y) = (1-z) * x + z * h_hat

## 与简单标量控制的区别
- ReZero/SkipInit: 单个标量控制
- GTrXL: 基于输入内容的**向量级门控**，可以逐维度控制信息流
- 门控偏置初始化使网络初始倾向于恒等映射

## 实验结果
- 在 DMLab-30 多任务 RL 基准上达到 SOTA
- 超越 LSTM 基线，即使在不需要记忆的"反应式"环境中也稳定

## 与综述的关联
属于 **Control** 维度。GTrXL 代表了残差控制从"标量"到"门控"的演进：
- Highway Networks: 原始的门控残差
- GTrXL: 将 GRU 门控引入 Transformer 残差
- 比 Highway Transformer (Chai2020) 更早在 Transformer 上实现门控

## 核心贡献
证明了复杂门控机制在残差连接中的价值，尤其在训练不稳定的场景中。
