# Longformer: The Long-Document Transformer
**作者**: Iz Beltagy, Matthew E. Peters, Arman Cohan | **年份**: 2020 | **arxiv**: 2004.05150

## 0. 摘要翻译
基于Transformer的模型由于自注意力操作（与序列长度成二次方缩放）无法处理长序列。为解决这一限制，本文提出Longformer，其注意力机制与序列长度成线性关系，使得处理长文档变得简单。Longformer的注意力机制是标准自注意力的一种替代方案，结合了局部滑动窗口注意力和针对任务的全局注意力。在字符级语言建模上的评估表明Longformer取得了与先前方法一致或更好的性能。

## 1. 方法动机
a) **为什么提出**: 许多NLP任务涉及长文档（如问答、文档摘要），但标准Transformer受限于512或1024 token的上下文窗口。
b) **现有痛点**: (1) 标准注意力的$O(n^2)$内存限制了最大序列长度；(2) 简单截断长文档会丢失关键信息；(3) 之前的稀疏注意力方法（如Sparse Transformer）缺乏灵活的全局信息聚合能力。
c) **研究假设**: 自然语言处理中的大多数注意力交互是局部的，全局信息只需在少量特定位置聚合。

## 2. 方法设计
a) **Pipeline**: 混合使用三种注意力模式构建稀疏注意力矩阵。

b) **模块功能**:
- **滑动窗口注意力 (Sliding Window)**: 每个token只关注其左右各$w/2$个token，复杂度$O(n \times w)$。通过堆叠$l$层，感受野可达$l \times w$个token。
- **扩张滑动窗口 (Dilated Sliding Window)**: 类似空洞卷积，窗口内token之间有间隔$d$，使得感受野扩大到$l \times d \times w$，同时不增加计算量。
- **全局注意力 (Global Attention)**: 在特定位置（如[CLS]token、问题token）设置全局注意力，这些位置与所有其他位置交互。全局注意力使用单独的$Q_g, K_g, V_g$投影矩阵。

c) **公式解释**:
- 总体复杂度: $O(n \times w)$，其中$w$是窗口大小（通常$w=256$或$w=512$）
- 全局注意力: 假设有$g$个全局token，额外复杂度为$O(g \times n)$，$g \ll n$时可忽略
- 实际实现使用TVM实现自定义CUDA核以高效处理稀疏模式

## 3. 与其他方法对比
| 方面 | Longformer | Transformer | Reformer | Sparse Transformer |
|------|-----------|-------------|----------|-------------------|
| 复杂度 | $O(n \cdot w)$ | $O(n^2)$ | $O(n\log n)$ | $O(n\sqrt{n})$ |
| 注意力模式 | 局部+全局 | 全局 | LSH近似 | 固定稀疏 |
| 任务适应性 | 全局位置可配置 | 固定 | 固定 | 固定 |
| 长文档支持 | 最长4096+ | 512 | 64K+ | 中等 |

## 4. 实验表现
- **字符级语言建模（text8、enwiki8）**: 与full attention性能相当，text8上达到1.10 bpc
- **长文档问答（TriviaQA、WikiHop）**: 显著优于使用截断的RoBERTa baseline
- **文档分类（IMDB、Hyperpartisan）**: 优于之前的长文档方法
- **共指消解（OntoNotes）**: 新的SOTA
- **支持序列长度**: 预训练时4,096 tokens，微调时最长可扩展

## 5. 总结
a) **一句话概括**: Longformer通过结合滑动窗口局部注意力和可配置的全局注意力，以$O(n)$复杂度高效处理长文档任务，同时保持灵活的信息聚合能力。
b) **速记pipeline**: Input → [Sliding-Window-Attn(w) + Optional-Global-Attn(g positions) → FFN] × N → Output
