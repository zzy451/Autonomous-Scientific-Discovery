# From Sparse to Soft Mixtures of Experts
**作者**: Joan Puigcerver, Carlos Riquelme, Basil Mustafa, Neil Houlsby (Google Research) | **年份**: 2023 (ICLR 2024) | **arxiv**: 2308.00951

## 0. 摘要翻译
Soft MoE 是一种完全可微分的稀疏 Transformer 架构，通过隐式软分配（implicit soft assignment）解决了传统稀疏 MoE 的训练不稳定、token 丢弃和负载不均等问题。与传统 Sparse MoE 将单个 token 硬路由到专家不同，Soft MoE 将所有输入 token 的加权组合传递给每个专家的"槽位"（slot），每个专家处理的是 token 的"软混合"。在视觉任务上，Soft MoE 在保持稀疏计算优势的同时，显著优于 dense Transformer 和 sparse MoE。

## 1. 方法动机
### 1.1 传统 Sparse MoE 的痛点
- **训练不稳定**: 离散 top-k 路由引入高方差梯度，需要 straight-through estimator 等近似技巧
- **Token 丢弃**: 当路由到某个专家的 token 超过容量上限时，超出部分被丢弃，信息损失不可控
- **负载不均衡**: 需要额外的 auxiliary loss（如 Switch Transformer 的负载均衡损失）来防止专家坍缩
- **不可微分**: top-k 操作本身不可微分，梯度无法顺畅流过路由决策

### 1.2 核心洞察
如果用连续的软权重（softmax）替代离散的 top-k 路由，则上述所有问题同时消失：完全可微分、无 token 丢弃、天然负载均衡。

## 2. 方法设计

### 2.1 Slot 机制
Soft MoE 引入"slot"（槽位）概念，是连接 token 与专家之间的中间表示：
- 每个专家拥有 $p$ 个 slot，共 $m$ 个专家，总计 $m \cdot p$ 个 slot
- 每个 slot 不接收单个 token，而是接收所有 token 的加权组合
- slot 的数量决定了计算量（而非专家数量）

### 2.2 Dispatch 权重（分发阶段）
$$D = \text{softmax}_{\text{token}}(X \cdot \Phi)$$
- $X \in \mathbb{R}^{n \times d}$: 输入 token 矩阵（$n$ 个 token，$d$ 维）
- $\Phi \in \mathbb{R}^{d \times (m \cdot p)}$: 可学习的 slot 参数矩阵
- softmax 沿 **token 维度**（列方向）做归一化
- $D_{ij}$ 表示第 $i$ 个 token 对第 $j$ 个 slot 的贡献权重
- 每个 slot 的输入: $\tilde{X}_j = \sum_{i=1}^{n} D_{ij} \cdot X_i$（所有 token 的加权平均）

### 2.3 专家计算
$$Y_{\text{slot}} = \text{Expert}_k(\tilde{X}_j) \quad \text{for slot } j \text{ assigned to expert } k$$
- 每个 slot 的加权输入经过其对应专家的 FFN
- 分配规则: slot $1 \sim p$ 给专家 1，slot $p+1 \sim 2p$ 给专家 2，以此类推

### 2.4 Combine 权重（合并阶段）
$$C = \text{softmax}_{\text{slot}}(X \cdot \Phi)$$
- 使用与 D 相同的 logits $X \cdot \Phi$，但沿 **slot 维度**（行方向）做 softmax
- $C_{ij}$ 表示第 $j$ 个 slot 的输出对第 $i$ 个 token 的贡献权重
- 每个输出 token: $Y_i = \sum_{j=1}^{m \cdot p} C_{ij} \cdot Y_{\text{slot},j}$

### 2.5 完整流程
```
Input X (n×d)
  ↓
Logits = X · Φ                          (n × mp)
  ↓                    ↓
D = softmax(Logits, dim=token)    C = softmax(Logits, dim=slot)
  ↓
Slot inputs = D^T · X                   (mp × d)
  ↓
Expert FFN per slot → Slot outputs       (mp × d)
  ↓
Output = C · Slot outputs               (n × d)
```

### 2.6 计算复杂度分析
- **FLOPs 取决于 slot 总数**（而非专家数量）：slot 总数 = $m \times p$
- 若设 slot 总数 = 序列长度 $n$，则与 dense Transformer 的 FLOPs 相当
- 可以大幅增加专家数量（增加参数量）而几乎不增加推理成本
  - 例: Soft MoE ViT-H/14 (128 experts) 有 40x+ 参数量，推理时间仅增加 2%
- 路由计算: $O(n \cdot d \cdot m \cdot p)$ 矩阵乘法 + softmax，无需 top-k/sort 操作
- 硬件友好：全为密集矩阵运算，无需稀疏分发/收集操作

### 2.7 与 Sparse MoE 的本质区别
| 方面 | Sparse MoE | Soft MoE |
|------|-----------|----------|
| 路由 | 离散 top-k，选择 k 个专家 | 连续 softmax 加权 |
| 专家输入 | 原始单个 token | 所有 token 的软混合 |
| 可微分 | 否（需 STE 等技巧） | 完全可微分 |
| Token 丢弃 | 有（容量超限时） | 无 |
| Aux Loss | 需要（负载均衡） | 不需要 |
| 专家利用率 | 不均匀 | 天然均匀 |
| 硬件效率 | 需 sort/top-k | 仅矩阵乘法 |

## 3. 对比
| 方法 | 路由方式 | 可微分 | Token 丢弃 | 需要 Aux Loss | 主要验证场景 |
|------|---------|--------|-----------|-------------|-------------|
| Dense Transformer | 无（全连接） | 是 | 无 | 无 | 通用 |
| Switch Transformer | Top-1 硬路由 | 否 | 有 | 需要 | NLP |
| GShard | Top-2 硬路由 | 否 | 有 | 需要 | NLP |
| Expert Choice | 专家选 token | 否 | 有 | 需要 | NLP |
| V-MoE | Top-k + 容量因子 | 否 | 有 | 需要 | Vision |
| Soft MoE | 软加权混合 | 完全可微 | 无 | 不需要 | Vision |
| Sigma-MoE | Top-k + Sigmoid | 否 | 有 | 改进版 | NLP |

## 4. 实验
### 4.1 图像分类（ImageNet）
- Soft MoE ViT 在所有规模（S/16 到 H/14）上均显著优于同 FLOPs 的 dense ViT
- 与 V-MoE（sparse MoE for ViT）相比：Soft MoE 在精度和训练稳定性上均更优
- Soft MoE-H/14 (128 experts): 40x+ 参数量增长，仅 2% 推理时间增长

### 4.2 训练稳定性
- 无需调节 auxiliary loss 权重（传统 sparse MoE 对此超参数极为敏感）
- 专家利用率天然均匀，无路由坍缩现象
- 训练曲线更平滑，收敛更快

### 4.3 分析实验
- 可视化 dispatch 权重：不同 slot 自然学到关注图像的不同区域
- 专家间的 slot 输入分布多样性高，表明信息有效分配

### 4.4 局限性
- **因果语言模型受限**: slot 机制将所有 token 混合，包括未来 token，违反自回归因果性约束
  - 可通过限制 softmax 范围（仅混合过去 token）缓解，但效果会降低
- **主要在视觉任务验证**: 尚未在大规模语言模型上充分验证
- **Slot 数量选择**: 需要与序列长度匹配，增加了超参数选择的复杂度

## 5. 总结
a) **一句话**: Soft MoE 用连续的 dispatch/combine 软权重替代离散 top-k 路由，实现完全可微分的 MoE，消除了 token 丢弃和负载不均问题，在视觉任务上表现优异，但因 token 混合机制在因果语言模型上的应用受限。

b) **速记 pipeline**: `Input X → Logits=X·Φ → D=softmax(Logits,dim=token) → slot_in=D^T·X → Expert_k(slot_in) → slot_out → C=softmax(Logits,dim=slot) → Output=C·slot_out`
