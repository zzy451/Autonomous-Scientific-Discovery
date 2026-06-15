# Attention-Only Transformers and Implementing MLPs with Attention Heads
**作者**: Srinivasan Bhojanapalli, Ayan Chakrabarti, Andreas Veit, Michal Lukasik, Himanshu Jain, Frederick Liu, Yin-Wen Chang, Sanjiv Kumar | **年份**: 2023 | **arxiv**: 2309.08593 | **发表**: ICLR 2024 | **链接**: https://arxiv.org/abs/2309.08593

## 0. 摘要翻译
本文证明了 MLP 神经元可以由一个内部维度为 1 的 masked attention head 实现，前提是 MLP 的激活函数属于一个受限类别（包括 SiLU 及其近似）。这使得可以将标准的 MLP+Attention Transformer 转换为纯 Attention-Only Transformer，代价是大幅增加注意力头的数量。作者还证明注意力头可以执行多项式运算，为 Attention-Only 架构的表达能力提供了理论基础。

## 1. 方法动机
- Transformer 的标准块包含 Attention + FFN 两个子层，但它们的角色是否可以统一？
- 从理论角度探索：Attention 机制是否足以模拟 FFN 的功能？
- 如果可以，意味着 Transformer 的最小必要组件只有 Attention
- 这对理解 Transformer 的计算本质和简化架构设计有重要意义

## 2. 方法设计

### 核心理论：MLP 神经元 = Masked Rank-1 Attention Head
- 一个 MLP 神经元计算 `σ(w^T x + b)` 可以被一个 masked attention head 精确模拟
- 条件：激活函数 σ 属于受限类别（包括 SiLU、GELU 的近似等）
- 每个 attention head 只需内部维度 1（rank-1）
- 转换引入的误差可以任意小

### 转换方法
- 一个 FFN 层有 d_ff 个神经元 → 需要 d_ff 个额外的 rank-1 attention heads
- 标准 Transformer 的 d_ff 通常为 4d，因此 attention heads 数量大幅增加
- 转换后的模型只包含 multi-head attention + residual connections

### Attention 的多项式计算能力
- 证明 attention heads 可以执行多项式运算
- 这为 Attention-Only 架构提供了超越简单线性变换的计算能力

### 相关工作：Attention-Only via Unrolled Subspace Denoising (Wang et al., 2025, ICML)
- 从子空间去噪的迭代展开角度推导出 Attention-Only 架构
- 每层仅包含 self-attention + skip connection
- 在视觉（ImageNet）和语言（GPT-2 级别）任务上接近标准 Transformer 性能

## 3. 与其他方法对比
| 方法 | 组件 | 理论基础 | 实用性 |
|------|------|---------|-------|
| 标准 Transformer | Attn + FFN | 原始设计 | 高 |
| Attention-Only (本文) | 仅 Attn | MLP→Attn 转换 | 理论为主（heads 数量爆炸） |
| FFN-Only (Melas-Kyriazi 2021) | 仅 FFN | 替换 Attn 为 FFN | 性能有差距（74.9% vs 79.9%） |
| Attention-Only (Wang 2025) | 仅 Attn | 子空间去噪展开 | 接近标准性能 |

## 4. 实验表现
- **理论贡献为主**：证明了 MLP→Attention 转换的可行性
- FFN-Only 对比（Melas-Kyriazi 2021）：ViT-Base 在 ImageNet 上 74.9% vs 标准 ViT 77.9%
- Wang et al. 2025 的 Attention-Only：在 GPT-2 和 DeiT 上接近标准 Transformer 性能

## 5. 总结
a) **一句话概括**：理论证明 MLP 神经元可被 rank-1 masked attention head 模拟，Attention-Only Transformer 在理论上与标准 Transformer 等价，但实际转换需要大量额外 heads；后续工作（Wang 2025）从去噪展开角度实现了实用的 Attention-Only 架构。

b) **速记 pipeline**：`x -> [MultiHead Attn (含模拟FFN的rank-1 heads)] -> +x -> ...`（所有计算统一为 attention）
