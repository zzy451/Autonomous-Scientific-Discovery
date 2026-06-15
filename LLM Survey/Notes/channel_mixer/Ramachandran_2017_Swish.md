# Searching for Activation Functions (Swish)

**论文**: Searching for Activation Functions
**作者**: Prajit Ramachandran, Barret Zoph, Quoc V. Le
**年份**: 2017
**来源**: arXiv:1710.05941 (Google Brain)
**标签**: [非LLM] 激活函数, 自动搜索, Swish

---

## 0. 摘要
本文通过自动化搜索技术（强化学习+穷举搜索）在候选激活函数空间中发现了 Swish 激活函数：f(x) = x * σ(βx)。实验表明 Swish 在多个深度网络任务上一致优于 ReLU。

## 1. 方法动机
a) ReLU 是当时最常用的激活函数，但不一定是最优的。手动设计激活函数效率低。
b) ReLU 在 x<0 时梯度为零（"死亡神经元"问题），且不光滑。
c) 假设：通过自动化搜索可以发现更好的激活函数。

## 2. 方法设计
a) 搜索流程：
   - 定义搜索空间：由一元和二元操作组成的候选函数
   - 使用强化学习和穷举搜索在 CIFAR-10 代理任务上评估
   - 发现最优候选：Swish = x * σ(βx)

b) Swish 的性质：
   - β=0 时退化为线性函数
   - β→∞ 时逼近 ReLU
   - 光滑、非单调
   - 保持对负值输入的敏感性

c) Swish(x) = x * sigmoid(βx)，其中 β 可以是可学习参数或固定为 1（SiLU）

## 3. 与其他方法对比
| 方法 | 优点 | 缺点 | 改进点 |
|------|------|------|--------|
| ReLU | 简单高效，缓解梯度消失 | 死亡神经元，不光滑 | - |
| GELU | 概率化门控 | 计算略贵 | - |
| **Swish** | **光滑、非单调、自门控** | **比 ReLU 计算稍贵** | **自动搜索发现** |

## 4. 实验表现
- 在 ImageNet、CIFAR 等多个 CV 基准上一致优于 ReLU
- 在机器翻译任务上也有提升
- 深层网络（40+层）提升尤其明显

## 5. 对 Channel Mixer 的意义
Swish（SiLU）是 SwiGLU 的核心组件。Shazeer 2020 将 Swish 与 GLU 结合，创造了 SwiGLU = swish(xW) ⊗ (xV)，成为 LLaMA、PaLM 等主流 LLM 的标准 FFN 激活函数。

## 6. 总结
a) 核心思想：自动搜索发现的自门控光滑激活函数（15字）
b) 速记 pipeline：
   1. 定义激活函数候选搜索空间
   2. 在代理任务上自动评估
   3. 发现 Swish = x * sigmoid(x)
   4. 光滑且自门控，在深层网络中优于 ReLU
