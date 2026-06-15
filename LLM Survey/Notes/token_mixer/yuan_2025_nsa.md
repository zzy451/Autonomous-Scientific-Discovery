# Yuan et al. 2025 - Native Sparse Attention (NSA)

**论文信息**
- 标题: Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention
- 作者: Jingyang Yuan et al. (DeepSeek)
- 年份: 2025
- arXiv: 2502.11089

## 0. 摘要翻译
长上下文建模是LLM的关键能力，但标准注意力的二次复杂度构成瓶颈。我们提出Native Sparse Attention (NSA)，一种硬件对齐且可原生训练的稀疏注意力机制。NSA通过动态分层稀疏策略，将token压缩、token选择和滑动窗口三种注意力模式组合，在减少计算量的同时保持全注意力的建模能力。

## 1. 方法动机
a) **为什么提出**: 现有稀疏注意力方法（如Longformer）使用固定模式，无法适应数据分布
b) **现有方法痛点**: 
   - 固定模式稀疏（如滑动窗口）可能遗漏重要的远距离依赖
   - 动态稀疏方法（如Reformer的LSH）在GPU上实现效率低
   - 大多数稀疏方法不能端到端训练
c) **研究假设**: 通过硬件对齐的分层稀疏策略，可以在训练中原生支持稀疏注意力

## 2. 方法设计
a) **方法流程**:
   - **压缩分支**: 将KV按块压缩为摘要token，用于粗粒度全局注意力
   - **选择分支**: 基于压缩注意力分数，选择top-k重要块进行细粒度注意力
   - **滑动窗口分支**: 对最近的局部token使用密集注意力
   - 三个分支的输出通过门控聚合

b) **模块功能**:
   - **Token Compression**: 块内KV均值/加权池化→压缩token
   - **Block Selection**: 根据压缩注意力分数选择重要块
   - **Sliding Window**: 固定大小的局部窗口注意力
   - **Gated Aggregation**: $o = g_1 \cdot o_{compress} + g_2 \cdot o_{select} + g_3 \cdot o_{window}$
   
c) **公式解释**:
   - 压缩分支复杂度: O(N/b · d)，b为块大小
   - 选择分支复杂度: O(k · b · d)，k为选择的块数
   - 总复杂度: O(N/b · d + k · b · d + w · d)，远小于O(N²·d)

## 3. 与其他方法对比
a) **本质不同**: 三分支动态稀疏（压缩+选择+局部），而非单一模式
b) **创新点**: 
   - 硬件对齐设计（块对齐GPU内存访问模式）
   - 可端到端训练（不依赖近似梯度）
   - 三种互补的注意力模式
c) **适用场景**: 长上下文LLM（64K+ tokens）
d) **对比表格**:

| 特性 | Full Attention | Longformer | NSA |
|------|---------------|------------|-----|
| 复杂度 | O(N²) | O(N·w) | O(N/b + k·b + w) |
| 全局信息 | 有 | 仅global tokens | 压缩分支 |
| 局部信息 | 有 | 滑窗 | 滑窗 |
| 自适应性 | - | 无 | 动态选择 |

## 4. 实验表现
a) **验证方式**: 语言建模、长上下文检索(NIAH)、多种LLM基准
b) **关键数据**: 64K上下文训练/推理，性能接近full attention，速度提升显著
c) **优势场景**: 超长上下文LLM训练和推理
d) **局限性**: 压缩和选择机制引入额外开销

## 5. 学习与应用
a) **开源情况**: DeepSeek发布
b) **实现细节**: 基于Triton的高效实现
c) **迁移可能性**: 可集成到现有Transformer架构

## 6. 总结
a) **一句话概括**: 通过压缩全局+选择重要块+局部窗口的三分支动态稀疏策略，实现硬件友好且可训练的高效长上下文注意力
b) **速记版pipeline**: Input → [Compress(粗粒度全局) + Select(细粒度重要块) + Window(局部)] → Gated Merge → Output

**Token Mixer维度**: Sparse Attention方案，硬件对齐的动态三分支稀疏注意力，兼顾全局、重要区域和局部
