# Deep Learning using Rectified Linear Units (ReLU)

**论文**: Deep Learning using Rectified Linear Units (ReLU)
**作者**: Abien Fred Agarap
**年份**: 2018
**来源**: arXiv:1803.08375
**标签**: [非LLM] 激活函数, ReLU, 深度学习基础

---

## 0. 摘要
本文系统综述了 ReLU 激活函数在深度学习中的应用，并提出将 ReLU 用作分类函数（替代 softmax）的方案。在多个经典模型（DNN、CNN、RNN/GRU）上对比了 ReLU 与 softmax 作为输出层分类函数的表现。

## 1. 方法动机
a) ReLU 是深度学习中最广泛使用的激活函数，但通常仅用于隐藏层，输出层仍使用 softmax。
b) Sigmoid/tanh 在深层网络中存在梯度消失问题，ReLU 通过 max(0, x) 有效缓解。
c) 假设：ReLU 的简洁性和计算效率也可以扩展到分类层。

## 2. 方法设计
a) ReLU 定义：
   f(x) = max(0, x)
   
   性质：
   - x > 0 时梯度恒为 1，不存在梯度消失
   - x ≤ 0 时输出为 0，引入稀疏性
   - 计算极其简单高效

b) ReLU 的已知问题：
   - "死亡神经元"：x < 0 时梯度为 0，神经元可能永久失活
   - 输出无上界，可能导致数值不稳定
   - 不光滑（在 x=0 处不可导）

c) 实验设置：在 DNN、CNN、GRU 上分别用 ReLU 和 softmax 作为分类函数，在 MNIST 和 Fashion-MNIST 上评估。

## 3. 与其他方法对比
| 方法 | 优点 | 缺点 | 改进点 |
|------|------|------|--------|
| Sigmoid | 输出有界 (0,1) | 梯度消失，计算贵 | - |
| Tanh | 零中心化 | 梯度消失 | - |
| **ReLU** | **计算简单，无梯度消失（正区间）** | **死亡神经元，不光滑** | **稀疏激活** |
| Leaky ReLU | 解决死亡神经元 | 引入超参数 | 负区间保留小梯度 |

## 4. 实验表现
- 在 MNIST 上，ReLU 作为分类函数的准确率与 softmax 接近
- 在 Fashion-MNIST 上表现类似
- ReLU 分类函数的计算效率更高
- 但 softmax 在概率解释性上仍有优势

## 5. 对 Channel Mixer 的意义
ReLU 是 Transformer FFN 层最初采用的激活函数（Vaswani et al. 2017 原始 Transformer）。后续研究（Zhang et al. 2024 "ReLU² Wins"）发现 ReLU 及其变体（如 ReLU²）在 LLM 中能产生高度稀疏的激活模式，这对 MoE 和推理加速有重要价值。ReLU 的稀疏激活特性使其成为理解 channel mixer 中信息选择机制的基础。

## 6. 总结
a) 核心思想：用分段线性函数实现高效稀疏激活（14字）
b) 速记 pipeline：
   1. 输入 x 通过 max(0, x) 运算
   2. 正值直通，负值归零
   3. 梯度在正区间恒为 1，训练高效
   4. 天然产生稀疏表示，奠定现代激活函数基础
