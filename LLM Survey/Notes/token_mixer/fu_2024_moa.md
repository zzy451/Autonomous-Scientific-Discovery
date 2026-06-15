# Mixture of Sparse Attention for Automatic Large Language Model Compression (MoA)
**作者**: Tianyu Fu, Haofeng Huang, Xuefei Ning, Genghan Zhang, Boju Chen, Tianqi Wu, Hongyi Wang, Zhekai Zhang, Zhihang Yuan, Qiang Xu, Shu-Tao Xia, Yu Wang | **年份**: 2024 | **arxiv**: 2406.14909

## 0. 摘要翻译
本文提出 Mixture of Attention (MoA)，一种自动为 LLM 不同层和不同注意力头分配最优稀疏注意力模式的方法。MoA 构建了一个包含多种注意力模式（全注意力、滑动窗口、局部+全局、稀疏等）及其随序列长度的缩放规则的搜索空间，通过 profiling 和搜索自动找到每层每头的最优配置，实现了在保持质量的同时大幅压缩注意力计算。

## 1. 方法动机
a) **为什么**: 不同层、不同头的注意力模式差异很大——有些头关注局部，有些关注全局，有些几乎是稀疏的。用统一的注意力模式（如全部用滑动窗口）是次优的。
b) **痛点**: (1) 手动为每层每头设计注意力模式不可行；(2) 现有稀疏注意力方法（如 Longformer）对所有层使用相同模式；(3) 需要一种自动化的异构注意力分配方法。
c) **假设**: 通过自动搜索，为每个注意力头分配最适合其功能的稀疏模式，可以在大幅减少计算的同时保持模型质量。

## 2. 方法设计

### a) Pipeline
```
1. 定义搜索空间: 多种注意力模式 × 缩放规则
2. Profiling: 在校准数据上分析每层每头的注意力特征
3. 搜索: 在给定计算预算下，为每层每头选择最优模式
4. 部署: 使用异构注意力配置进行推理
```

### b) 注意力模式搜索空间
- **Full Attention**: 标准全注意力（最贵但最强）
- **Sliding Window**: 固定窗口大小的局部注意力
- **Local + Global**: 滑动窗口 + 少量全局 token
- **Block Sparse**: 块级稀疏注意力
- **Static Sparse**: 固定稀疏模式
- 每种模式有不同的窗口大小/稀疏度参数

### c) 自动搜索
- 对每个头计算不同模式下的注意力近似误差
- 使用进化搜索或贪心算法在预算约束下最小化总误差
- 结果: 每层每头一个注意力模式配置
- 典型发现: 底层需要更多全注意力，高层可以更稀疏

## 3. 对比
| 方法 | 模式分配 | 自动化 | 异构 |
|------|----------|--------|------|
| Longformer | 全局统一 | 手动 | 否 |
| BigBird | 全局统一 | 手动 | 否 |
| NSA | 全局统一 | 学习 | 否 |
| MoA | Per-head | 自动搜索 | 是 |

## 4. 实验
- **模型**: Llama-2-7B, Llama-2-13B
- **压缩效果**: 在保持 <1% 质量损失的情况下，注意力计算减少 50-70%
- **长上下文**: 在 LongBench 上，MoA 优于均匀稀疏化方法
- **发现**: 不同层的最优模式确实差异很大，验证了异构分配的必要性
- **推理加速**: 配合稀疏注意力 kernel，实现 1.5-2x 推理加速

## 5. 总结
a) **一句话**: MoA 通过自动搜索为 LLM 每层每头分配最优的稀疏注意力模式，实现了异构注意力压缩，在保持质量的同时大幅减少注意力计算。
b) **速记 pipeline**: `Profile attention patterns → Search space (Full/SW/Sparse per head) → Evolutionary search under budget → Deploy heterogeneous attention`
