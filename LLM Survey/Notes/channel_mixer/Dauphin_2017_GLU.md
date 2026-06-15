# Language Modeling with Gated Convolutional Networks

**论文**: Language Modeling with Gated Convolutional Networks
**作者**: Yann N. Dauphin, Angela Fan, Michael Auli, David Grangier
**年份**: 2017
**来源**: ICML 2017
**标签**: [非LLM] GLU, 激活函数, 门控机制

---

## 0. 摘要
本文提出了门控线性单元（Gated Linear Unit, GLU），并将其应用于卷积语言模型中。GLU 通过线性路径和 sigmoid 门控实现信息选择性传递，在语言建模任务上取得了当时的 SOTA 结果。

## 1. 方法动机
a) 当时语言建模主要依赖 RNN/LSTM，计算无法并行化，训练效率低。
b) RNN 的顺序处理本质限制了并行训练的可能性。
c) 假设：卷积网络配合门控机制可以在保持序列建模能力的同时实现并行计算。

## 2. 方法设计
a) GLU 的核心公式：
   GLU(X) = (X * W + b) ⊗ σ(X * V + c)
   
   其中：
   - X * W + b 是线性投影（信息通道）
   - σ(X * V + c) 是 sigmoid 门控（选择信号）
   - ⊗ 是逐元素乘法

b) 与传统门控（如 LSTM）的区别：GLU 的一半是线性的，提供了梯度直通路径，缓解了深层网络的梯度消失问题。

c) 架构：堆叠多层门控卷积，捕获不同尺度的上下文特征。

## 3. 与其他方法对比
| 方法 | 优点 | 缺点 | 改进点 |
|------|------|------|--------|
| LSTM 门控 | 自然处理序列 | 无法并行 | - |
| 纯 ReLU/tanh | 简单 | 无门控选择能力 | - |
| GTU (σ(X*W) ⊗ tanh(X*V)) | 有门控 | 两路都非线性，梯度弱 | - |
| **GLU** | **线性梯度路径+门控选择** | **卷积受限感受野** | **梯度传播更好** |

## 4. 实验表现
- WikiText-103 上达到当时 SOTA
- Google Billion Word 基准上结果有竞争力
- 比 LSTM 基线训练速度更快

## 5. 对 Channel Mixer 的意义
GLU 是后续 SwiGLU、GeGLU、ReGLU 等变体的基础。Shazeer 2020 将 GLU 思想引入 Transformer FFN 层，用不同激活函数替换 sigmoid 门控，形成了现代 LLM 中广泛使用的 FFN 设计（如 LLaMA, PaLM 等均使用 SwiGLU）。

## 6. 总结
a) 核心思想：用线性门控实现信息选择性传递（14字）
b) 速记 pipeline：
   1. 输入同时通过两个线性变换
   2. 一路做 sigmoid 门控
   3. 两路逐元素相乘实现信息筛选
   4. 线性路径保证梯度流畅
