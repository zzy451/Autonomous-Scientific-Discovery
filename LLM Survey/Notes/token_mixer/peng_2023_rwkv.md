# Peng et al. 2023 - RWKV: Reinventing RNNs for the Transformer Era

**论文信息**
- 标题: RWKV: Reinventing RNNs for the Transformer Era
- 作者: Bo Peng, Eric Alcaide, Quentin Anthony, Alon Albalak, et al.
- 年份: 2023
- arXiv: 2305.13048
- 会议: EMNLP 2023 Findings

## 0. 摘要翻译
我们提出RWKV (Receptance Weighted Key Value)，一种结合了RNN和Transformer优点的新型模型架构。RWKV利用线性注意力机制实现了类似Transformer的并行训练，同时保持了RNN的O(1)推理复杂度。我们将RWKV扩展到140亿参数，展示了其在性能上与同规模Transformer相当。

## 1. 方法动机
a) **为什么提出**: 希望结合Transformer的训练效率和RNN的推理效率
b) **现有方法痛点**: 
   - Transformer推理时KV cache随序列增长
   - 传统RNN无法并行训练
   - 需要"训练时并行、推理时递归"的模型
c) **研究假设**: 通过改进的线性注意力机制可以实现"两全其美"

## 2. 方法设计
a) **方法流程**:
   - Time Mixing（替代自注意力）: 使用WKV机制
   - Channel Mixing（替代FFN）: 使用类似的门控混合
   - 支持并行训练和递归推理双模式
   
b) **模块功能**:
   - **Token Shift**: $\bar{x}_t = \mu \cdot x_t + (1-\mu) \cdot x_{t-1}$（混合当前和前一token）
   - **Receptance (R)**: 门控信号，控制信息接收
   - **WKV计算**: $wkv_t = \frac{\sum_{i=1}^{t-1} e^{-(t-1-i)w+k_i} v_i + e^{u+k_t} v_t}{\sum_{i=1}^{t-1} e^{-(t-1-i)w+k_i} + e^{u+k_t}}$
   - **输出**: $o_t = W_o \cdot (\sigma(r_t) \odot wkv_t)$
   
c) **公式解释**:
   - w: 时间衰减因子（channel-wise，不依赖输入）
   - u: 当前token的bonus（强调当前信息）
   - 分子分母结构类似于softmax注意力的指数加权平均
   - 可改写为递归形式: 状态 $(a_t, b_t)$ 递归更新

## 3. 与其他方法对比
a) **本质不同**: 线性注意力的变体，带有指数衰减和门控
b) **创新点**: 
   - WKV机制结合了指数衰减和当前token加成
   - Receptance门控控制信息流
   - 真正的双模式：并行训练+递归推理
c) **适用场景**: 长序列生成、推理效率敏感的场景
d) **对比表格**:

| 特性 | Transformer | RNN | RWKV |
|------|-------------|-----|------|
| 训练并行 | 是 | 否 | 是 |
| 推理复杂度 | O(N) per step | O(1) per step | O(1) per step |
| 内存 | O(N) KV cache | O(1) 固定状态 | O(1) 固定状态 |
| 长距离建模 | 全局 | 困难 | 指数衰减 |

## 4. 实验表现
a) **验证方式**: The Pile语言建模，多种NLP基准
b) **关键数据**: RWKV-14B性能接近同规模Transformer
c) **优势场景**: 推理效率要求高、长序列生成
d) **局限性**: 指数衰减限制了远距离信息保持；在检索密集任务上弱于Transformer

## 5. 学习与应用
a) **开源情况**: 完全开源，活跃社区维护
b) **实现细节**: CUDA优化的WKV核；支持多种规模（0.1B-14B）
c) **迁移可能性**: 后续版本v5(Eagle)/v6(Finch)/v7(Goose)持续改进

## 6. 总结
a) **一句话概括**: 通过WKV机制和Receptance门控实现"训练时并行、推理时O(1)"的RNN-Transformer混合架构
b) **速记版pipeline**: Input → Token Shift → [R,W,K,V投影] → WKV(指数衰减加权) → R门控 → Output

**Token Mixer维度**: RNN-Like方案，线性注意力变体，指数衰减+门控实现O(1)递归推理
