# Lv et al. 2024 - CogAttention: More Expressive Attention with Negative Weights

**论文信息**
- 标题: Cog Attention: More Expressive Attention with Negative Weights  
- 作者: Chaojun Lv et al.
- 年份: 2024
- arXiv: 2410.07105

## 0. 摘要翻译
传统注意力机制使用softmax归一化，限制了注意力权重为非负值。这意味着模型无法直接表达"抑制"某些token的信息。我们提出Cog Attention，通过允许负注意力权重来增强注意力的表达能力。方法通过移除softmax的非负约束，使用修改后的注意力计算来支持负权重。

## 1. 方法动机
a) **为什么提出**: softmax的非负输出限制了注意力机制的表达能力
b) **现有方法痛点**: 
   - softmax强制所有注意力权重非负，无法表达"不相关"或"排斥"关系
   - 标准注意力只能做加权求和（所有权重同号），无法做对比/差分
c) **研究假设**: 允许负权重可以让模型更精确地控制信息流

## 2. 方法设计
a) **方法流程**:
   - 设计支持负权重的注意力计算方式
   - 保持计算效率与标准注意力相当
   - 与现有模型架构兼容
   
b) **模块功能**:
   - 修改注意力权重计算，允许产生负值
   - 保持归一化稳定性
   - 负权重用于抑制不相关或冲突信息
   
c) **公式解释**:
   - 标准: $\text{Attn}(Q,K,V) = \text{softmax}(QK^T/\sqrt{d})V$（权重 ≥ 0）
   - CogAttention: 允许权重 < 0，通过修改归一化方式实现

## 3. 与其他方法对比
a) **本质不同**: 直接修改注意力权重的符号约束（vs Differential Transformer用两个softmax的差）
b) **创新点**: 
   - 更直接的负权重实现方式
   - 与Differential Transformer互补的设计哲学
c) **适用场景**: 需要精细信息控制的任务
d) **对比表格**:

| 特性 | Standard Attn | Diff Transformer | CogAttention |
|------|--------------|-------------------|--------------|
| 负权重 | 否 | 是（差分） | 是（直接） |
| 实现方式 | softmax | 双路softmax差 | 修改归一化 |
| 计算开销 | 基线 | 约2x | 约1x |

## 4. 实验表现
a) **验证方式**: 语言建模、下游任务
b) **关键数据**: 在多个任务上超过标准注意力
c) **优势场景**: 信息抑制重要的任务
d) **局限性**: 训练稳定性需要注意

## 5. 学习与应用
a) **开源情况**: 论文公开
b) **实现细节**: 实现相对简单，修改注意力计算即可
c) **迁移可能性**: 可替换任何标准注意力

## 6. 总结
a) **一句话概括**: 通过允许负注意力权重增强注意力表达能力，使模型能够显式地抑制不相关信息
b) **速记版pipeline**: Input → Q,K,V → 支持负权重的Attention → Output

**Token Mixer维度**: Attention with Negative——直接允许负注意力权重，增强表达能力
