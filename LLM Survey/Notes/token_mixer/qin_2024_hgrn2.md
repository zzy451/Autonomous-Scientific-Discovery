# Qin et al. 2024 - HGRN2: Gated Linear RNNs with State Expansion

**论文信息**
- 标题: HGRN2: Gated Linear RNNs with State Expansion
- 作者: Zhen Qin, Songlin Yang, Weixuan Sun, Xuyang Shen, Dong Li, Weigao Sun, Yiran Zhong
- 年份: 2024
- arXiv: 2404.07904

## 0. 摘要翻译
门控线性RNN（如Mamba、GLA等）在序列建模中展示了强大的性能，但其递归状态大小通常受限于模型维度。我们提出HGRN2，通过外积(outer product)进行状态扩展，将递归状态从向量扩展到矩阵，显著增加状态容量而不增加参数。同时，这种扩展使HGRN2可以被解释为一种线性注意力，从而利用chunk-wise并行实现高效训练。

## 1. 方法动机
a) **为什么提出**: 原始HGRN的递归状态是向量，容量有限
b) **现有方法痛点**: 
   - 向量状态: 容量为d，无法存储复杂的key-value关联
   - 增加状态维度会增加参数量
   - 需要"免费"的状态扩展方法
c) **研究假设**: 通过外积可以将d维向量状态扩展为d×d矩阵状态，不增加参数

## 2. 方法设计
a) **方法流程**:
   - 基于HGRN的分层门控设计
   - 使用外积将状态从向量扩展到矩阵: $S_t \in \mathbb{R}^{d_k \times d_v}$
   - 状态更新: $S_t = G_t \odot S_{t-1} + k_t \otimes v_t$
   - 可以解释为线性注意力，用chunk-wise并行训练
   
b) **模块功能**:
   - **分层门控**: 低层forget gate下界小（快遗忘），高层下界大（慢遗忘）
   - **状态扩展**: 外积 $k_t \otimes v_t$ 将状态从d扩展到 $d_k \times d_v$
   - **线性注意力解释**: $o_t = q_t^T S_t$，可以用chunk-wise分块训练
   - **下界约束**: $f_t = \sigma(\text{lower\_bound} + \text{raw\_gate})$
   
c) **公式解释**:
   - 状态容量: 从HGRN的d增加到 $d_k \times d_v$（典型地增加d_v倍）
   - 参数量: 外积不需要额外参数（仅需要K、V的投影）
   - 分层下界: 第l层的下界 $b_l = l/L$，确保深层保留更长的记忆

## 3. 与其他方法对比
a) **本质不同**: 外积状态扩展 + 分层门控下界（来自HGRN的核心创新）
b) **创新点**: 
   - "免费"的状态扩展（不增加参数）
   - 线性注意力解释使chunk-wise训练成为可能
   - 分层门控确保多尺度记忆
c) **适用场景**: 需要大状态容量的序列建模
d) **对比表格**:

| 特性 | HGRN | HGRN2 | GLA |
|------|------|-------|-----|
| 状态形状 | 向量(d) | 矩阵(d_k×d_v) | 矩阵(d_k×d_v) |
| 扩展方法 | - | 外积 | 外积 |
| 门控 | 分层下界 | 分层下界 | 数据依赖 |
| 训练 | 扫描 | chunk-wise | chunk-wise |

## 4. 实验表现
a) **验证方式**: 语言建模、长序列基准
b) **关键数据**: 性能与GLA、Mamba相当；训练效率高
c) **优势场景**: 需要多尺度记忆的长序列任务
d) **局限性**: 分层下界是预设的（vs 数据依赖的GLA门控）

## 5. 学习与应用
a) **开源情况**: OpenNLPLab开源
b) **实现细节**: 基于flash-linear-attention库
c) **迁移可能性**: 门控RNN架构的重要进展

## 6. 总结
a) **一句话概括**: 通过外积状态扩展和分层门控下界，以零额外参数将门控RNN的状态容量大幅提升
b) **速记版pipeline**: Input → Q,K,V,Gate → 外积扩展(k⊗v) → 分层门控衰减 → 矩阵状态更新 → Q查询 → Output

**Token Mixer维度**: RNN-Like方案，外积状态扩展+分层门控，兼具线性注意力解释
