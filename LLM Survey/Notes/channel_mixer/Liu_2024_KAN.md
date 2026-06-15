# KAN: Kolmogorov-Arnold Networks

**论文**: KAN: Kolmogorov-Arnold Networks
**作者**: Ziming Liu, Yixuan Wang, Sachin Vaidya, Fabian Ruehle, James Halverson, Marin Soljacic, Thomas Y. Hou, Max Tegmark
**年份**: 2024
**来源**: arXiv:2404.19756
**标签**: FFN 替代方案, 可学习激活函数, Kolmogorov-Arnold 定理

---

## 0. 摘要
本文提出 KAN（Kolmogorov-Arnold Networks）作为 MLP 的替代方案。与 MLP 在节点上使用固定激活函数不同，KAN 在边（连接权重）上使用可学习的激活函数（参数化为 B-spline）。KAN 在特定任务上以更少的参数达到更好的精度和可解释性。

## 1. 方法动机
a) 传统 MLP 基于万能近似定理（Universal Approximation Theorem），需要大量参数来逼近复杂函数。
b) Kolmogorov-Arnold 表示定理提供了另一种理论框架：任何多变量连续函数都可以用一元函数的组合来表示。
c) 假设：将可学习的一元函数放在网络的边上（而非节点上），可以获得更好的表达能力和可解释性。

## 2. 方法设计
a) 核心思路对比：
   - **MLP**: y = W_2 * sigma(W_1 * x + b_1) + b_2（固定激活函数 sigma 在节点上）
   - **KAN**: y = sum_i phi_i(x_i)（可学习激活函数 phi 在边上，使用 B-spline 参数化）

b) B-spline 参数化：
   - 每条边上的激活函数由 B-spline 基函数的线性组合表示
   - B-spline 的控制点是可学习参数
   - 网格可以自适应细化以提高精度

c) 网络结构：
   - 类似 MLP 的分层结构
   - 但每层的计算是对输入各维度分别应用一元可学习函数，然后求和
   - 不需要标准的矩阵乘法 + 固定激活的模式

## 3. 与其他方法对比
| 方法 | 优点 | 缺点 | 适用场景 |
|------|------|------|----------|
| MLP/FFN | GPU 高效，训练成熟 | 参数多，可解释性差 | 大规模 LLM |
| **KAN** | **参数高效，可解释** | **GPU 效率低，难大规模** | **科学计算，小规模任务** |
| GLU 变体 | 动态门控，性能好 | 仍是固定激活函数 | LLM FFN |

## 4. 实验表现
- 在函数拟合、PDE 求解等任务上，KAN 以更少参数超越 MLP
- 可解释性显著优于 MLP：可以直观看到每条边学到了什么函数
- 局限：
  - B-spline 计算不利于 GPU 并行
  - 大规模 Transformer 中直接替换 FFN 面临计算效率瓶颈
  - 参数量扩展不如 MLP 线性可控

## 5. 对 Channel Mixer 的意义
KAN 代表了一种根本不同的 Channel Mixer 设计思路：从"固定激活+可学习权重"到"可学习激活+结构化连接"。但在当前 LLM 规模下，KAN 的计算效率问题限制了其实际应用。后续工作（如 KAT, Rational KAN）试图解决效率问题。KAN 更可能在科学计算或小规模特定领域找到应用，而非直接替代大规模 LLM 的 FFN。

## 6. 总结
a) 核心思想：将可学习激活函数放在边上替代固定激活MLP（20字）
b) 速记 pipeline：
   1. 基于 Kolmogorov-Arnold 定理设计网络结构
   2. 每条边使用 B-spline 参数化的可学习一元函数
   3. 网格自适应细化提升逼近精度
   4. 以更少参数达到高精度但 GPU 效率受限
