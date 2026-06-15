# Scaling Vision Transformers to 22 Billion Parameters (ViT-22B)
**作者**: Mostafa Dehghani, Josip Djolonga, Basil Mustafa, Piotr Padlewski, Jonathan Heek, Justin Gilmer, Andreas Steiner, Mathilde Caron, Robert Geirhos, Ibrahim Alabdulmohsin, et al. | **年份**: 2023 | **arxiv**: 2302.05442 | **发表**: ICML 2023

## 0. 摘要翻译
ViT-22B 是当时最大的密集 Vision Transformer 模型，拥有 220 亿参数。为了在如此规模下实现稳定高效的训练，作者对标准 ViT 进行了多项架构修改，包括**并行层**（Attention 和 MLP 并行执行）、**QK 归一化**（防止注意力 logit 爆炸）和**省略偏置项**等。这些修改解决了超过 8B 参数时出现的训练发散问题。

## 1. 方法动机
- 将 ViT 扩展到 >8B 参数时观察到严重的训练不稳定性
- 训练发散的具体表现：注意力 logit 值异常增大，导致注意力权重接近 one-hot
- 注意力熵趋近于零，模型表示坍塌
- 需要找到既能稳定训练又能保持效率的架构修改

## 2. 方法设计（重点：模块排列顺序及其理论分析）

### 1) 并行层（Parallel Layers）
```
标准 ViT: y = x + MLP(LN(x + Attn(LN(x))))
并行 ViT: y = x + MLP(LN(x)) + Attn(LN(x))
```
- Attention 和 MLP 共享同一个 LayerNorm 的输出
- QKV 投影和 MLP 第一层可以融合为一次矩阵乘法
- Attention 输出投影和 MLP 第二层也可以融合
- 训练速度提升约 15%（与 PaLM 的发现一致）

### 2) QK 归一化（Query-Key Normalization）
```
标准 Attention: softmax(QK^T / sqrt(d))
QK-Norm:       softmax(LN(Q) * LN(K)^T / sqrt(d))
```
- 在计算点积注意力之前，对 Query 和 Key 施加 LayerNorm
- 防止注意力 logit 值的无控制增长
- 确保注意力权重保持合理的熵（不会退化为 one-hot）
- 这是解决 >8B 参数训练发散的**关键技术**

### 3) 省略偏置
- QKV 投影和 LayerNorm 中不使用偏置项
- MLP Dense 层保留偏置（对质量有帮助）
- TPU 利用率提升约 3%

### 完整的 ViT-22B 块结构
```
y = x + Attn(QK-Norm, LN(x)) + MLP(LN(x))
   并行执行 + QK 归一化 + 无偏置
```

## 3. 与其他方法对比
| 方法 | 并行层 | QK Norm | 规模 | 目标 |
|------|-------|---------|------|------|
| 标准 ViT | 否 | 否 | <1B | 视觉基线 |
| PaLM | 是 | 否 | 540B | 语言模型 |
| ViT-22B | 是 | 是 | 22B | 视觉模型 |
| MAGNETO | 否 | 否（用 Sub-LN） | 通用 | 多模态 |

- QK 归一化是 ViT-22B 的独特贡献，后续被广泛采用（如 Gemma 等）
- 并行层设计验证了 PaLM 的发现在视觉领域同样适用

## 4. 实验表现
- **训练稳定性**：解决了 >8B 参数 ViT 的训练发散问题
- **硬件利用率**：MFU（Model FLOPs Utilization）达到 54.9%
- **图像分类**：在 ImageNet 等基准上达到 SOTA
- **Frozen Feature**：作为特征提取器表现优异
- **鲁棒性**：对分布偏移和对抗样本的鲁棒性更强
- **人类对齐**：形状偏差（shape bias）更接近人类视觉

## 5. 总结
a) **一句话概括**：ViT-22B 通过并行层+QK 归一化解决了超大 Vision Transformer（>8B 参数）的训练发散问题，其中 QK 归一化是防止注意力 logit 爆炸的关键。

b) **速记 pipeline**：`y = x + Attn(LN(Q), LN(K), V; LN(x)) + MLP(LN(x))`（并行 + QK-Norm）
