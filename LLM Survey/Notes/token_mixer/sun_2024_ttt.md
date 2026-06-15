# Learning to (Learn at Test Time): RNNs with Expressive Hidden States (TTT)
**作者**: Yu Sun, Xinhao Li, Karan Dalal, Jiarui Xu, Arjun Vikram, Genghan Zhang, Yann Dubois, Xinlei Chen, Xiaolong Wang, Sanmi Koyejo, Tatsunori Hashimoto, Carlos Guestrin | **年份**: 2024 | **arxiv**: 2407.04620

## 0. 摘要翻译
本文提出 TTT (Test-Time Training) 层，一种新的序列建模层，其隐状态本身是一个机器学习模型，更新规则是一步自监督学习。由于隐状态在测试序列上也通过训练来更新，故称"测试时训练"。提出两个实例：TTT-Linear（隐状态为线性模型）和 TTT-MLP（隐状态为两层 MLP）。TTT-Linear 在质量上匹配 Transformer 同时保持线性复杂度，TTT-MLP 在长上下文上进一步超越。

## 1. 方法动机
a) **为什么**: RNN 的核心限制是隐状态的表达能力——固定大小的向量/矩阵难以压缩任意长的历史。如果隐状态本身是一个模型（有更多参数和非线性），表达能力就不再受限。
b) **痛点**: (1) 线性注意力/SSM 的矩阵状态容量有限（O(d²)）；(2) 简单的累加更新规则（如外积）容易被新信息覆盖旧信息；(3) 需要一种更有表达力的隐状态和更智能的更新规则。
c) **假设**: 将隐状态定义为一个模型的参数，将更新规则定义为梯度下降，可以获得理论上无限的表达能力——模型越大，记忆越多。

## 2. 方法设计

### a) 核心思想
```
传统 RNN:  h_t = f(h_{t-1}, x_t)     — h 是固定大小向量
TTT 层:    W_t = W_{t-1} - η∇L(W; x_t) — W 是模型参数，通过 SGD 更新
```

### b) 两个实例

**TTT-Linear (隐状态 = 线性模型)**:
- 隐状态: W ∈ R^{d×d}（线性投影矩阵）
- 自监督任务: 重建被遮蔽的 token
- 更新: `W_t = W_{t-1} - η · (W_{t-1} k_t - v_t) k_t^T`
- 输出: `o_t = W_t q_t`
- 这本质上就是 delta rule / 线性注意力的一种形式
- 复杂度: O(d²) per step

**TTT-MLP (隐状态 = 两层 MLP)**:
- 隐状态: θ = {W1, b1, W2, b2}（两层 MLP 的参数）
- 自监督任务: `L = ||f_θ(k_t) - v_t||²`
- 更新: `θ_t = θ_{t-1} - η · ∇_θ L(θ; k_t, v_t)`
- 输出: `o_t = f_{θ_t}(q_t)`
- 非线性记忆，容量更大
- 需要计算二阶梯度（训练时）

### c) Mini-batch TTT
- 不逐 token 更新，而是每 mini-batch (如 16 tokens) 更新一次
- 减少更新频率，提高训练效率
- 类似于 chunk-wise 处理

### d) 关键公式
- 自监督损失: `L(W; x_t) = ||f_W(k_t) - v_t||²`
- 参数更新: `W_t = W_{t-1} - η ∇_W L(W_{t-1}; x_t)`
- TTT-Linear 展开: `W_t = W_{t-1} - η(W_{t-1}k_t - v_t)k_t^T` = delta rule
- TTT-MLP 输出: `o_t = MLP_{θ_t}(q_t)`

## 3. 对比
| 模型 | 隐状态 | 更新规则 | 表达能力 | 复杂度/step |
|------|--------|----------|----------|------------|
| LSTM | 向量 h | 门控 | O(d) | O(d) |
| Linear Attn | 矩阵 W | 外积累加 | O(d²) | O(d²) |
| DeltaNet | 矩阵 W | Delta rule | O(d²) | O(d²) |
| TTT-Linear | 矩阵 W | SGD (=delta rule) | O(d²) | O(d²) |
| TTT-MLP | MLP 参数 θ | SGD | O(|θ|) 可扩展 | O(|θ|) |
| Titans | 神经网络 θ | SGD + 惊喜门控 | O(|θ|) 可扩展 | O(|θ|) |

- TTT-Linear ≈ DeltaNet（数学等价）
- TTT-MLP 和 Titans 思想相似，Titans 增加了惊喜门控和多种混合方式

## 4. 实验
- **语言建模**: TTT-Linear (1.3B) 匹配 Transformer 和 Mamba 质量
- **TTT-MLP**: 在 8K+ 上下文长度上超越 TTT-Linear 和 Mamba
- **Scaling**: TTT 层的 scaling law 与 Transformer 相当
- **长上下文**: 在 32K 上下文的 book 数据上，TTT-MLP 困惑度持续下降
- **效率**: TTT-Linear 推理速度与 Mamba 相当；TTT-MLP 因需要 MLP 前向/反向传播，稍慢
- **训练**: 需要二阶梯度，训练开销比标准 Transformer 大约 1.5-2x

## 5. 总结
a) **一句话**: TTT 层将 RNN 的隐状态定义为一个模型的参数，将更新规则定义为自监督学习的梯度下降，统一了线性注意力（TTT-Linear = delta rule）并通过非线性扩展（TTT-MLP）获得了更强的长程记忆能力。
b) **速记 pipeline**: `Input x_t → (k_t, v_t, q_t) → Update: W_t = W_{t-1} - η∇L(W; k_t, v_t) → Output: o_t = f_{W_t}(q_t) | TTT-Linear: f=linear, TTT-MLP: f=MLP`
