# Rethinking Attention: Polynomial Alternatives to Softmax in Transformers
**作者**: Hemanth Saratchandran, Jianqiao Zheng, Yiping Ji, Wenbo Zhang, Simon Lucey | **年份**: 2024 | **arxiv**: 2410.18613

## 0. 摘要翻译

本文重新审视了 softmax 在注意力机制中不可替代的传统观点。通过理论分析，作者发现 softmax 的真正价值不在于其产生概率分布的性质（非负性、行归一化、稀疏性），而在于它对注意力矩阵 **Frobenius 范数的隐式正则化**效果。基于这一洞察，作者提出用多项式激活函数替代 softmax，在违反概率分布约束的情况下仍能取得竞争性甚至更优的性能。

## 1. 方法动机

- **传统观点的局限**: 长期以来，softmax 被认为不可替代，因为它产生归一化的概率分布
- **新视角**: 如果 softmax 的优势不在于概率归一化，而在于某种隐式正则化，那么有更简单的替代方案
- **计算瓶颈**: softmax 需要行级全局归一化（计算分母 $\sum_j e^{q_i \cdot k_j}$），限制了并行性和长序列效率
- **核心假设**: softmax 之所以有效，主要是因为它隐式地正则化了注意力矩阵的 Frobenius 范数 $\|A\|_F$，防止注意力权重过大或过小

## 2. 方法设计

### 2.1 理论分析：Softmax 的隐式正则化

标准 softmax 注意力矩阵 $A$ 的每一行满足：
$$\sum_j A_{ij} = 1, \quad A_{ij} \geq 0$$

这隐含了一个 Frobenius 范数上界：
$$\|A\|_F^2 = \sum_{i,j} A_{ij}^2 \leq \sum_i (\sum_j A_{ij})^2 = n$$

即 softmax 自动将 $\|A\|_F$ 限制在 $O(\sqrt{n})$ 量级，防止训练发散。

### 2.2 多项式注意力替代方案

用多项式函数 $p(x)$ 替代 $\text{softmax}(x)$：
$$A_{ij} = p(q_i \cdot k_j / \sqrt{d})$$

常见选择：
- **二次多项式**: $p(x) = x^2$（即 Squared Attention）
- **三次多项式**: $p(x) = x^2 + \alpha x^3$
- **带偏置**: $p(x) = (x + b)^2$

### 2.3 关键性质

多项式注意力**刻意违反** softmax 的三个传统约束：
1. **非负性**: 多项式可以产生负注意力权重 → 允许"负注意力"（抑制某些 token）
2. **行归一化**: 不要求行和为 1 → 允许注意力"总量"随输入变化
3. **稀疏性**: 不自动产生尖锐分布 → 通过多项式阶数控制

但**保留**了 Frobenius 范数正则化效果（通过适当的缩放和多项式设计）。

## 3. 对比

### 3.1 与其他注意力激活函数对比
| 方法 | 激活函数 | 非负性 | 行归一化 | Frobenius 正则化 | 硬件友好 |
|------|---------|:------:|:-------:|:---------------:|:--------:|
| **Softmax** | $e^{x_i}/\sum e^{x_j}$ | 是 | 是 | 隐式 | 需行级 reduce |
| **Sigmoid** (Ramapuram 2024) | $\sigma(x)$ | 是 | 否 | 部分 | 逐元素 |
| **ReLU** | $\max(0, x)$ | 是 | 否 | 弱 | 逐元素 |
| **Squared ReLU** (Primer) | $\text{ReLU}(x)^2$ | 是 | 否 | 中等 | 逐元素 |
| **Polynomial** (本文) | $p(x)$ | **否** | **否** | **显式设计** | 逐元素 |

### 3.2 本文的核心贡献
- 从"softmax 为什么有效"这一根本问题出发，给出了 **Frobenius 范数正则化**的新解释
- 证明了传统三约束（非负、归一化、稀疏）**不是必要的**
- 提供了一个统一框架来理解各种 softmax 替代方案

## 4. 实验

- **图像分类** (ImageNet): 多项式注意力匹配或略超 softmax 基线
- **目标检测 & 实例分割** (COCO): 在 Mask R-CNN 等框架中达到竞争性能
- **文本分类**: 在 NLP 任务上同样有效
- **物理建模**: 在基于物理的模拟任务中表现优异
- **消融**: 验证了 Frobenius 范数控制是性能的关键因素——当移除这一正则化时，所有替代方案（包括多项式）性能均下降

## 5. 总结

### a) 一句话
通过揭示 softmax 的核心优势在于 Frobenius 范数的隐式正则化而非概率归一化，本文为设计注意力激活函数提供了新的理论基础，并证明多项式函数可以作为有效的 softmax 替代方案。

### b) 速记 pipeline
```
Q, K, V → QK^T/√d → Polynomial p(·) [替代 softmax] → × V → Output
                         ↑
          设计 p(·) 使得 ||A||_F 被正则化
          （不需要非负性、不需要归一化）
```

## 6. 与本综述的关联
- 属于 Token Mixer 中 **Different Activation** 子类别
- 与 Sigmoid Attention (Ramapuram 2024) 互补：sigmoid 保留非负性但去除归一化；多项式连非负性也放弃
- 提供了理解"为什么 softmax 有效"的理论工具，有助于设计未来的注意力变体
- 从理论层面统一了 softmax、sigmoid、ReLU、polynomial 等多种注意力激活函数

---
**阅读日期**: 2026-04-06
