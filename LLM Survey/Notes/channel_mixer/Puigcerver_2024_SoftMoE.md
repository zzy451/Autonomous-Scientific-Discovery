# From Sparse to Soft Mixtures of Experts (Soft MoE)
**作者**: Joan Puigcerver, Carlos Riquelme, Basil Mustafa, Neil Houlsby (Google) | **年份**: 2023 (ICLR 2024) | **arxiv**: 2308.00951

## 0. 摘要翻译
Soft MoE 是一种完全可微分的稀疏 Transformer 架构，通过隐式软分配（implicit soft assignment）解决了传统稀疏 MoE 的训练不稳定、token 丢弃和负载不均等问题。Soft MoE 不是将单个 token 硬路由到专家，而是将所有输入 token 的加权组合传递给每个专家，每个专家处理的是 token 的"软混合"（soft mixture）。在视觉任务上，Soft MoE 在保持稀疏计算优势的同时，显著优于传统 dense Transformer 和 sparse MoE。

## 1. 方法动机
- 传统 sparse MoE（如 Switch Transformer、GShard）使用离散的 top-k 路由，导致：
  - 训练不稳定：路由决策的离散性引入高方差梯度
  - Token 丢弃：当专家容量不足时，部分 token 被丢弃
  - 负载不均：需要额外的 auxiliary loss 来平衡专家负载
  - 不可微分：top-k 操作不可微，需要 straight-through estimator 等技巧
- Soft MoE 的洞察：如果用连续的软权重替代离散路由，所有问题都迎刃而解

## 2. 方法设计（重点：与六维度框架的关联）

### 2.1 核心机制：Dispatch 和 Combine 权重
- **Slot 概念**: 每个专家有固定数量的"slot"（槽位），每个 slot 接收一个输入
- **Dispatch 权重（D）**:
  - 计算方式: `D = softmax(X · Φ)` 沿 token 维度做 softmax
  - X: 输入 token 矩阵 (n × d)，Φ: 可学习的 slot 参数矩阵 (d × (m·p))
  - n = token 数，m = 专家数，p = 每专家 slot 数
  - 每个 slot 的输入 = 所有 token 的加权组合（权重由 D 决定）
- **专家计算**: 每个 slot 的加权输入通过对应专家的 FFN
- **Combine 权重（C）**:
  - 计算方式: `C = softmax(X · Φ)` 沿 slot 维度做 softmax
  - 每个输出 token = 所有 slot 输出的加权组合
- **关键区别**: D 和 C 使用相同的 logits 但在不同维度做 softmax

### 2.2 完全可微分
- 整个路由过程只涉及矩阵乘法和 softmax，完全可微分
- 无需 auxiliary loss、无 token 丢弃、无负载均衡问题
- 梯度可以顺畅地流过路由决策

### 2.3 与传统 MoE 的本质区别
- **Sparse MoE**: 每个 token → 选择 top-k 专家 → 专家处理原始 token
- **Soft MoE**: 所有 token → 软加权混合 → 每个 slot 收到混合 token → 专家处理混合 token → 输出再软加权组合回每个 token 位置

### 与六维度框架的关联
- **Channel Mixer 维度**: Soft MoE 替代标准 FFN，属于 channel mixer 的创新
- **与 sparse MoE 的关系**: 从离散路由到连续路由的范式转变
- **计算效率**: 虽然每个 token 理论上"参与"所有专家，但通过 slot 机制控制每个专家的实际计算量，保持稀疏计算的效率优势
- **局限性**: 由于每个 slot 接收的是 token 混合而非单个 token，Soft MoE 不适合需要 token 级别精确处理的场景（如自回归语言模型的因果性要求）

## 3. 与其他方法对比
| 方法 | 路由方式 | 可微分 | Token 丢弃 | 需要 Aux Loss | 适用场景 |
|------|---------|--------|-----------|-------------|---------|
| Dense Transformer | 无（全连接） | 是 | 无 | 无 | 通用 |
| Switch Transformer | Top-1 硬路由 | 否 | 有 | 需要 | NLP |
| GShard | Top-2 硬路由 | 否 | 有 | 需要 | NLP |
| Expert Choice | 专家选 token | 否 | 有 | 需要 | NLP |
| Soft MoE | 软加权混合 | 完全可微 | 无 | 不需要 | Vision |
| Qwen3 MoE | Top-8 硬路由 | 否 | 有 | 全局批次均衡 | NLP |

## 4. 实验表现
- 在 ImageNet 图像分类上，Soft MoE ViT 显著优于同 FLOPs 的 dense ViT 和 sparse MoE ViT
- 训练稳定性大幅提升，无需调节 auxiliary loss 权重
- 专家利用率天然均匀，无需额外均衡机制
- 在 ViT-S/16 到 ViT-H/14 的多个规模上一致优于基线
- 主要在视觉任务上验证；在自回归语言模型上的应用受限于因果性约束（slot 混合了未来 token）

## 5. 总结
a) Soft MoE 用连续的 dispatch/combine 软权重替代离散 top-k 路由，实现完全可微分的 MoE，消除了 token 丢弃和负载不均问题，但因 token 混合机制在因果语言模型上的应用受限。

b) 速记 pipeline: Input X → D=softmax(X·Φ, dim=token) → slot_input=D^T·X → Expert FFN per slot → slot_output → C=softmax(X·Φ, dim=slot) → Output=C·slot_output
