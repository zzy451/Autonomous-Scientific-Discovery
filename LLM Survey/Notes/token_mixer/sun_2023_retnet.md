# Sun et al. 2023 - Retentive Network: A Successor to Transformer for Large Language Models (RetNet)

**论文信息**
- 标题: Retentive Network: A Successor to Transformer for Large Language Models
- 作者: Yutao Sun, Li Dong, Shaohan Huang, Shuming Ma, Yuqing Xia, Jilong Xue, Jianyong Wang, Furu Wei
- 年份: 2023
- arXiv: 2307.08621

## 0. 摘要翻译
在本文中，我们提出了Retentive Network (RetNet)作为大语言模型的Transformer后继架构。RetNet同时实现训练并行性、低成本推理和良好性能——解决了语言建模的"不可能三角"。核心是retention机制，支持三种计算范式：并行表示（用于训练）、递归表示（用于推理）、块级递归表示（用于长序列）。

## 1. 方法动机
a) **为什么提出**: 追求"不可能三角"——同时实现训练并行性、低推理成本、强性能
b) **现有方法痛点**: 
   - Transformer: 训练并行+强性能，但推理成本O(N)
   - RNN: 推理O(1)，但训练不并行
   - 线性注意力: 训练并行+推理O(1)，但性能差
c) **研究假设**: 通过结合复数指数衰减和多尺度策略可以同时满足三个要求

## 2. 方法设计
a) **方法流程**:
   - 定义Retention机制: 带复数指数衰减的注意力
   - 三种等价计算形式:
     1. 并行(训练): 类似注意力矩阵，但权重矩阵D带指数衰减
     2. 递归(推理): $s_t = \gamma s_{t-1} + k_t^T v_t$, $o_t = q_t s_t$
     3. 块级递归(长序列): 块内并行，块间递归
   
b) **模块功能**:
   - **Retention**: $\text{Retention}(X) = (QK^T \odot D) V$
   - **衰减矩阵D**: $D_{ij} = \gamma^{i-j}$ when $i \geq j$, 0 otherwise
   - **Multi-Scale Retention**: 不同头使用不同衰减率γ
   - **GroupNorm**: 稳定训练
   
c) **公式解释**:
   - 并行形式: $Y = (QK^T \odot D)V$，D是下三角衰减矩阵
   - 递归形式: $s_n = \gamma s_{n-1} + k_n^T v_n$, $y_n = q_n s_n$
   - γ通常取 $e^{i\theta}$ 的模（复数指数衰减的实部）
   - 不同头使用不同θ实现多尺度记忆

## 3. 与其他方法对比
a) **本质不同**: 用显式的指数衰减替代softmax归一化，实现训练-推理双模式
b) **创新点**: 
   - 三种等价计算范式
   - 多尺度衰减率
   - 理论上的训练-推理等价性
c) **适用场景**: 需要高效推理的LLM场景
d) **对比表格**:

| 特性 | Transformer | RWKV | RetNet |
|------|-------------|------|--------|
| 训练 | 并行 | 并行 | 并行 |
| 推理 | O(N)/step | O(1)/step | O(1)/step |
| 衰减 | 无 | 指数(固定) | 复数指数(多尺度) |
| 三种模式 | 否 | 是 | 是(+块级) |

## 4. 实验表现
a) **验证方式**: 语言建模（规模从1.3B到6.7B）
b) **关键数据**: 6.7B规模上接近Transformer性能；推理速度比Transformer快8.4倍；内存减少70%
c) **优势场景**: 高效推理场景
d) **局限性**: 在小规模模型上可能不如Transformer；指数衰减限制远距离信息

## 5. 学习与应用
a) **开源情况**: Microsoft Research开源
b) **实现细节**: γ使用多尺度（不同head不同γ）
c) **迁移可能性**: 概念影响了后续GLA、RWKV等工作

## 6. 总结
a) **一句话概括**: 通过带复数指数衰减的Retention机制，同时支持并行训练/递归推理/块级计算三种模式，解决语言建模的"不可能三角"
b) **速记版pipeline**: Input → Q,K,V → [并行:QK^T⊙D·V | 递归:γs+kv, qs | 块级:混合] → GroupNorm → Output

**Token Mixer维度**: RNN-Like/Linear Attention方案，指数衰减的线性注意力，训练-推理等价的三模式设计
