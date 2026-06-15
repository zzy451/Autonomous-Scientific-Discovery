# Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention
**作者**: Yuan et al. (DeepSeek) | **年份**: 2025 | **arxiv**: 2502.11089

## 0. 摘要翻译
长上下文建模是大语言模型的核心能力，但标准注意力的二次方复杂度使其在长序列上计算代价极高。现有的稀疏注意力方法多为推理阶段的后处理手段，未能与训练过程原生集成。本文提出 **NSA (Native Sparse Attention)**，一种硬件对齐且可原生训练的稀疏注意力机制。NSA 将注意力分解为三个互补的分支：**压缩粗粒度注意力 (compressed coarse-grained attention)**、**选择性块稀疏注意力 (selected block sparse attention)** 和 **滑动窗口注意力 (sliding window attention)**。该方法在预训练阶段就原生使用稀疏注意力，而非作为推理时的近似。实验表明，NSA 在保持与全注意力相当的建模质量的同时，在 64k token 长度下实现了显著的加速。

## 1. 方法动机
a) **为什么提出这个方法**：现有稀疏注意力方法（如 Longformer, BigBird 等）多采用固定模式或仅在推理时应用稀疏化，无法在训练中获得一致的加速且可能损害模型质量。DeepSeek 团队希望设计一种从预训练起就原生使用的稀疏注意力。

b) **现有方法的痛点**：
- 训练时用全注意力、推理时用稀疏注意力会导致 train-test mismatch
- 现有稀疏模式（如固定局部窗口 + 全局 token）表达能力有限
- 很多稀疏注意力方法不是硬件友好的（memory access pattern 不规律），导致理论 FLOPs 减少但实际速度提升不大

c) **研究假设/直觉**：注意力中的信息可以自然分解为三个层次——全局粗粒度概览、选择性细粒度关注、局部上下文窗口。这三者互补，且每个分支都可以设计为硬件友好的块状计算。

## 2. 方法设计
a) **方法流程 (pipeline)**：
1. 输入 token 序列经过 Q, K, V 投影
2. 并行经过三个注意力分支：
   - **Compressed Attention**：将 KV 按块压缩（平均池化或可学习压缩），用少量压缩 token 捕获全局信息
   - **Selected Block Sparse Attention**：计算 Q 与压缩 K 的相似度，选择 top-k 最相关的 KV 块，只对选中的块做精确注意力
   - **Sliding Window Attention**：对邻近的局部窗口做标准注意力，捕获局部依赖
3. 三个分支输出通过可学习的门控机制（MLP + sigmoid）融合

b) **核心模块功能**：
- **Token Compression**：将长序列 KV 分块，每块压缩为一个代表 token，大幅降低全局注意力的计算量
- **Block Selection**：基于压缩注意力分数选择最相关的块，实现动态稀疏（不同 query 选择不同块）
- **Sliding Window**：保证局部上下文的完整性
- **Gated Fusion**：三个分支的输出通过门控加权求和，门控信号由输入 token 动态生成

c) **关键公式解释**：
- 压缩注意力：K_c = Compress(K, block_size)，Attn_c = softmax(Q K_c^T / √d) V_c
- 块选择：scores = Q · K_c^T，选取 top-k 块索引
- 最终输出：o = g_c ⊙ o_c + g_s ⊙ o_s + g_w ⊙ o_w（三分支门控融合）

## 3. 与其他方法对比
- **与 Longformer/BigBird 的区别**：NSA 使用动态块选择而非固定稀疏模式，且从训练阶段就原生使用
- **与 MoBA 的区别**：MoBA 用 MoE 路由选择块，NSA 用压缩注意力分数选择块；NSA 额外有压缩分支和滑动窗口
- **与推理时稀疏化（如 H2O, StreamingLLM）的区别**：NSA 在训练时就使用稀疏模式，避免 train-test mismatch
- **创新点**：三分支互补设计 + 硬件对齐的块粒度计算 + 原生可训练
- **适用场景**：长上下文预训练（64k+ tokens），尤其适合在 DeepSeek 等大规模模型中应用

## 4. 实验表现
- **关键结果**：
  - 在 64k 长度下，NSA 相比全注意力实现了约 6-8 倍的加速
  - 语言建模困惑度与全注意力基本持平，在长上下文检索任务上甚至优于全注意力
  - 在 "Needle-in-a-Haystack" 任务上保持高精度
- **优势场景**：长文档理解、长上下文问答、大规模预训练
- **局限性**：
  - 块大小和 top-k 数量需要根据具体场景调参
  - 在短序列上相比标准注意力没有优势（稀疏化开销反而可能更大）
  - 硬件实现依赖自定义 CUDA kernel

## 5. 总结
a) **一句话概括（≤20字）**：三分支互补稀疏注意力，训练原生，硬件对齐。

b) **速记 pipeline**：
`Input → Q,K,V → ┌ Compressed Global Attn ┐
                  ├ Selected Block Attn    ├ → Gated Fusion → Output
                  └ Sliding Window Attn    ┘`
