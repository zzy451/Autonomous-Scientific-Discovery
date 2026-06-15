# Jiang et al. 2023 - Mistral 7B (Sliding Window Attention)

**论文信息**
- 标题: Mistral 7B
- 作者: Albert Q. Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh Chaplot, Diego de las Casas, Florian Bressand, Gianna Lengyel, Guillaume Lample, Lucile Saulnier, Lélio Renard Lavaud, Marie-Anne Lachaux, Pierre Stock, Teven Le Scao, Thibaut Lavril, Thomas Wang, Timothée Lacroix, William El Sayed
- 年份: 2023
- arXiv: 2310.06825

## 0. 摘要翻译
我们介绍Mistral 7B，一个70亿参数的语言模型，在所有评估基准上超过了Llama 2 13B，在许多基准上接近Llama 1 34B。Mistral 7B使用分组查询注意力(GQA)加速推理，并结合滑动窗口注意力(SWA)有效处理任意长度的序列，同时降低推理成本。

## 1. 方法动机
a) **为什么提出**: 需要一个在质量和效率之间取得最优平衡的开源模型
b) **现有方法痛点**: 全注意力在长序列上成本过高；需要实用的注意力效率优化
c) **研究假设**: 滑动窗口注意力+GQA的组合可以在不损失质量的前提下显著提升效率

## 2. 方法设计
a) **方法流程**:
   - 使用滑动窗口注意力(SWA): 每个token只关注前W个token
   - 使用GQA: 减少KV头数
   - 多层堆叠: 每层窗口W，L层后有效感受野W×L
   
b) **模块功能**:
   - **Sliding Window Attention**: 
     - 每个token在每层关注前W个token（W=4096）
     - L层后，理论感受野 = W × L
     - 32层 × 4096 = 131,072 tokens的理论感受野
   - **GQA**: 8个KV头, 32个Query头
   - **Rolling Buffer KV Cache**: 固定大小W的KV cache，循环覆盖旧token
   
c) **公式解释**:
   - 每层注意力范围: $[i-W, i]$
   - L层后任意token可通过W×L距离的信息传播
   - KV cache大小固定为W（不随序列长度增长）

## 3. 与其他方法对比
a) **本质不同**: 将SWA作为实用的LLM注意力方案（之前主要用于编码器如Longformer）
b) **创新点**: 
   - Rolling buffer KV cache: 固定大小的循环KV cache
   - SWA+GQA的实用组合
   - Pre-fill和chunked pre-fill优化
c) **适用场景**: 通用LLM推理
d) **对比表格**:

| 特性 | Full Attention | SWA(Mistral) |
|------|---------------|--------------|
| 每层范围 | 全局 | 局部W |
| KV cache | O(N) | O(W)固定 |
| 有效感受野 | N | W×L |
| 推理内存 | 随N增长 | 固定 |

## 4. 实验表现
a) **验证方式**: MMLU, HellaSwag, ARC, GSM8K等
b) **关键数据**: Mistral 7B超过Llama 2 13B；在代码和推理任务上接近Llama 1 34B
c) **优势场景**: 高效推理、固定内存预算
d) **局限性**: 单层内只有局部信息；窗口大小需要调参

## 5. 学习与应用
a) **开源情况**: 完全开源（Mistral AI）
b) **实现细节**: W=4096, GQA 8KV头, 32层
c) **迁移可能性**: SWA+GQA已成为很多模型的标准配置

## 6. 总结
a) **一句话概括**: 结合滑动窗口注意力和GQA，在7B参数下实现高效且强大的语言模型，固定大小KV cache支持任意长序列
b) **速记版pipeline**: Input → SWA(窗口W=4096) + GQA(8KV头) → Rolling Buffer KV Cache → Output

**Token Mixer维度**: Sparse Attention的实用变体——滑动窗口注意力+GQA的工程组合，固定KV cache大小
