# Vaswani et al. 2017 - Attention Is All You Need

**论文信息**
- 标题: Attention Is All You Need
- 作者: Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin
- 年份: 2017
- arXiv: 1706.03762
- 会议: NeurIPS 2017

## 0. 摘要翻译
主流的序列转换模型基于复杂的循环或卷积神经网络，包含编码器和解码器。表现最好的模型还通过注意力机制连接编码器和解码器。我们提出了一种新的简单网络架构——Transformer，完全基于注意力机制，完全摒弃了循环和卷积。在两个机器翻译任务上的实验表明，这些模型在质量上更优，同时更具并行性，训练时间显著减少。

## 1. 方法动机
a) **为什么提出**: RNN（LSTM/GRU）的序列依赖性限制了训练并行化，长距离依赖建模困难
b) **现有方法痛点**: RNN计算本质上是顺序的(sequential)，无法在序列维度并行；CNN虽可并行但捕获长距离依赖需要很多层
c) **研究假设**: 仅使用注意力机制（无循环/卷积）即可建模序列中的全局依赖关系，同时实现高度并行化

## 2. 方法设计
a) **方法流程**: 
   - 输入 → 词嵌入 + 位置编码 → N层编码器堆叠 → 编码表示
   - 编码表示 + 目标输入 → N层解码器堆叠 → 输出概率
   
b) **模块功能**:
   - **Scaled Dot-Product Attention**: $\text{Attention}(Q,K,V) = \text{softmax}(\frac{QK^T}{\sqrt{d_k}})V$
   - **Multi-Head Attention**: 将Q,K,V分别线性投影h次，并行计算注意力后拼接
   - **Position-wise FFN**: 两层全连接 + ReLU，$\text{FFN}(x) = \max(0, xW_1+b_1)W_2+b_2$
   - **残差连接 + LayerNorm**: 每个子层输出 $\text{LayerNorm}(x + \text{Sublayer}(x))$
   
c) **公式解释**:
   - 缩放因子 $\sqrt{d_k}$ 防止点积过大导致softmax梯度消失
   - Multi-Head: $\text{MultiHead}(Q,K,V) = \text{Concat}(head_1,...,head_h)W^O$
   - 每个head: $head_i = \text{Attention}(QW_i^Q, KW_i^K, VW_i^V)$

## 3. 与其他方法对比
a) **本质不同**: 完全去除循环和卷积，仅用注意力建模token间关系
b) **创新点**: 
   - Multi-Head Attention允许模型同时关注不同位置的不同子空间
   - 自注意力使每个位置可以直接与所有其他位置交互（O(1)路径长度）
c) **适用场景**: 适用于所有序列建模任务，尤其是需要长距离依赖的任务
d) **对比表格**:

| 特性 | RNN | CNN | Transformer |
|------|-----|-----|-------------|
| 并行性 | 低（顺序） | 高 | 高 |
| 最大路径长度 | O(N) | O(logN) | O(1) |
| 每层复杂度 | O(N·d²) | O(k·N·d²) | O(N²·d) |

## 4. 实验表现
a) **验证方式**: WMT 2014 英德/英法翻译
b) **关键数据**: EN-DE BLEU 28.4（超过之前最佳），EN-FR BLEU 41.0（SOTA）
c) **优势场景**: 大规模并行训练、长距离依赖建模
d) **局限性**: 自注意力复杂度O(N²)对超长序列不友好

## 5. 学习与应用
a) **开源情况**: 完全开源（tensor2tensor等框架）
b) **实现细节**: base模型：d_model=512, h=8, N=6; big模型：d_model=1024, h=16
c) **迁移可能性**: 已成为NLP/CV/Audio等领域的基础架构

## 6. 总结
a) **一句话概括**: 提出Transformer架构，仅用注意力机制替代RNN/CNN，实现并行化训练和全局依赖建模，奠定了现代LLM的基础
b) **速记版pipeline**: Input → Embedding+PosEnc → [Multi-Head Self-Attention → Add&Norm → FFN → Add&Norm] × N → Output

**Token Mixer维度**: 标准Dot-Product Attention（Scaled），Multi-Head机制允许多子空间并行注意力，复杂度O(N²·d)
