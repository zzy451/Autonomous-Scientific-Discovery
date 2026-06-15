# Beltagy et al. 2020 - Longformer: The Long-Document Transformer

**论文信息**
- 标题: Longformer: The Long-Document Transformer
- 作者: Iz Beltagy, Matthew E. Peters, Arman Cohan
- 年份: 2020
- arXiv: 2004.05150

## 0. 摘要翻译
Transformer基础模型无法处理长序列，因为自注意力机制的复杂度随序列长度二次增长。为解决此限制，我们引入Longformer，其注意力机制随序列长度线性增长，使其易于处理长文档。Longformer的注意力机制是局部窗口注意力与任务驱动的全局注意力的组合。

## 1. 方法动机
a) **为什么提出**: BERT等模型限制在512 tokens，无法处理长文档
b) **现有方法痛点**: 全注意力O(N²)导致长文档必须截断或分块处理，丢失全局信息
c) **研究假设**: 大多数token只需与局部邻域交互，少数特殊token（如[CLS]）需要全局视野

## 2. 方法设计
a) **方法流程**:
   - 每个token与固定窗口大小w内的邻居计算局部注意力
   - 选定的特殊token（如[CLS]）与所有token计算全局注意力
   - 可选：增加空洞（dilated）窗口扩大感受野

b) **模块功能**:
   - **Sliding Window Attention**: 每个token关注前后w/2个token，复杂度O(N·w)
   - **Dilated Sliding Window**: 间隔d的窗口扩展，有效窗口大小w×d
   - **Global Attention**: 特定位置与所有token交互（task-specific，如分类时的[CLS]）
   
c) **公式解释**:
   - 局部注意力: 每个位置i只与 $[i-w/2, i+w/2]$ 范围内的token交互
   - 多层堆叠后感受野: L层 × w窗口 = L·w 的有效感受野
   - 总复杂度: O(N·w) + O(N·g)，g为全局token数

## 3. 与其他方法对比
a) **本质不同**: 混合局部固定模式和任务驱动的全局注意力
b) **创新点**: 将稀疏注意力与下游任务需求结合（global token可学习）
c) **适用场景**: 长文档理解（QA、分类、摘要）
d) **对比表格**:

| 特性 | BERT | Longformer | BigBird |
|------|------|------------|---------|
| 最大长度 | 512 | 4096+ | 4096+ |
| 注意力 | 全局 | 局部+全局 | 局部+全局+随机 |
| 复杂度 | O(N²) | O(N·w) | O(N·w) |

## 4. 实验表现
a) **验证方式**: 长文档任务：WikiHop, TriviaQA, HotpotQA, arXiv分类
b) **关键数据**: 在所有长文档任务上超过RoBERTa（截断版）
c) **优势场景**: 长文档理解和分类
d) **局限性**: 固定窗口大小可能不适合所有任务；主要面向编码器

## 5. 学习与应用
a) **开源情况**: AllenAI开源，HuggingFace集成
b) **实现细节**: 窗口大小通常256-512；底层窗口小、高层窗口大
c) **迁移可能性**: 滑窗注意力思想被Mistral等LLM采用

## 6. 总结
a) **一句话概括**: 结合滑动窗口局部注意力和任务驱动全局注意力，实现线性复杂度的长文档处理
b) **速记版pipeline**: Input → Sliding Window Attention(local) + Global Attention(special tokens) → FFN → Output

**Token Mixer维度**: Sparse Attention方案，固定模式的局部窗口+少量全局token，复杂度O(N·w)
