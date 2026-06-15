# Lu et al. 2025 - MOBA: Mixture of Block Attention

**论文信息**
- 标题: MoBA: Mixture of Block Attention for Long-Context LLM
- 作者: Enzhe Lu et al. (MoonShot AI / Kimi)
- 年份: 2025
- arXiv: 2502.13189

## 0. 摘要翻译
我们提出MoBA (Mixture of Block Attention)，一种受混合专家(MoE)启发的稀疏注意力方法。MoBA将KV cache分成块，每个Query token通过路由机制选择最相关的KV块进行注意力计算。该方法可以无缝集成到现有Transformer中，在全注意力和稀疏注意力之间灵活切换。

## 1. 方法动机
a) **为什么提出**: 长上下文LLM（如Kimi的128K+）需要高效注意力机制
b) **现有方法痛点**: 
   - 全注意力O(N²)不可扩展
   - 固定模式稀疏注意力无法适应不同任务和数据分布
   - 需要与全注意力模型无缝兼容
c) **研究假设**: 类比MoE的路由机制，可以让每个Query选择最相关的KV块

## 2. 方法设计
a) **方法流程**:
   - 将KV cache均匀分成B个块
   - 每个Query token通过路由器选择top-k个最相关的KV块
   - 在选中的块内执行标准注意力
   - 保留因果滑动窗口确保局部信息

b) **模块功能**:
   - **Block Partitioning**: 将长度N的KV分成B个块，每块N/B个token
   - **Router**: 计算Query与每个块的相关性分数（如Q与块均值K的点积）
   - **Top-k Selection**: 选择分数最高的k个块
   - **Block Attention**: 在选中的块内计算标准注意力
   - **Causal Window**: 始终保留当前位置附近的局部窗口
   
c) **公式解释**:
   - 路由分数: $s_i = \text{score}(q, \bar{k}_i)$，$\bar{k}_i$为第i个块的key均值
   - 选择: 取top-k个分数最高的块
   - 复杂度: O(N·k·(N/B)·d) = O(k·N²/(B·d))，当k和B适当时远小于O(N²)

## 3. 与其他方法对比
a) **本质不同**: 用MoE思想进行注意力路由，数据驱动的稀疏选择
b) **创新点**: 
   - MoE → MoA（Mixture of Attention）的类比
   - 可以与全注意力无缝混合（训练时部分层用MoBA，部分层用全注意力）
   - 与现有训练好的模型兼容
c) **适用场景**: 超长上下文LLM（128K+ tokens）
d) **对比表格**:

| 特性 | Full Attention | NSA | MoBA |
|------|---------------|-----|------|
| 路由方式 | 无 | 压缩+选择 | MoE-style路由 |
| 块级/token级 | token | 块+token | 块 |
| 与全注意力兼容 | - | 需要训练 | 无缝切换 |

## 4. 实验表现
a) **验证方式**: 长上下文任务、NIAH测试、标准基准
b) **关键数据**: 在128K上下文上性能接近全注意力，计算量显著减少
c) **优势场景**: 超长上下文LLM推理
d) **局限性**: 路由机制的额外开销；块大小选择需要调参

## 5. 学习与应用
a) **开源情况**: Kimi团队发布
b) **实现细节**: 块大小通常1024-4096 tokens
c) **迁移可能性**: 可集成到任何Transformer-based LLM

## 6. 总结
a) **一句话概括**: 借鉴MoE的路由思想，让每个Query选择最相关的KV块进行注意力计算，实现数据驱动的稀疏注意力
b) **速记版pipeline**: KV → Block分割 → Router(Q与块均值K) → Top-k选择 → Block Attention → Output

**Token Mixer维度**: Sparse Attention方案，基于MoE路由的块级动态稀疏注意力
