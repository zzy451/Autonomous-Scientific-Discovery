# Gaussian Error Linear Units (GELUs)

**论文**: Gaussian Error Linear Units (GELUs)
**作者**: Dan Hendrycks, Kevin Gimpel
**年份**: 2016
**来源**: arXiv:1606.08415
**标签**: [非LLM] 激活函数, GELU, 概率门控, BERT/GPT 基础

---

## 0. 摘要
本文提出高斯误差线性单元（GELU）激活函数：GELU(x) = x · Φ(x)，其中 Φ(x) 是标准高斯分布的累积分布函数。GELU 将非线性变换与随机正则化（dropout）的思想统一起来，在 CV 和 NLP 任务上均优于 ReLU 和 ELU。

## 1. 方法动机
a) ReLU 通过符号函数（sign）对输入进行硬门控：正值通过，负值归零。这种硬阈值缺乏平滑性。
b) Dropout 随机将神经元置零，是一种随机正则化手段，但与激活函数是分离的。
c) 假设：可以设计一种激活函数，将非线性和随机正则化统一起来——根据输入值的大小（而非仅符号）来概率性地决定是否保留该输入。

## 2. 方法设计
a) 核心公式：
   GELU(x) = x · Φ(x) = x · P(X ≤ x)，X ~ N(0, 1)
   
   直觉：输入 x 越大，被保留的概率越高；输入越小（负值），越可能被置零。

b) 与 dropout 的联系：
   - Dropout：以固定概率 p 随机将输入置零
   - GELU：以输入值决定的概率 Φ(x) 保留输入
   - GELU 是"自适应 dropout"的期望值

c) 近似计算：
   - 精确计算需要 erf 函数
   - 快速近似：GELU(x) ≈ 0.5x(1 + tanh[√(2/π)(x + 0.044715x³)])
   - 另一近似：GELU(x) ≈ x · σ(1.702x)，与 Swish 形式相似

d) 性质：
   - 光滑、非单调
   - x → +∞ 时趋近恒等函数
   - x → -∞ 时趋近零
   - 在 x ≈ -0.17 处有一个小的负值区域

## 3. 与其他方法对比
| 方法 | 优点 | 缺点 | 改进点 |
|------|------|------|--------|
| ReLU | 简单高效 | 硬阈值，死亡神经元 | - |
| ELU | 负值区域光滑 | 计算较贵 | - |
| **GELU** | **概率门控，光滑，自适应** | **计算比 ReLU 贵** | **统一非线性与正则化** |
| Swish | 自门控，光滑 | 无概率解释 | 与 GELU 近似等价 |

## 4. 实验表现
- 在 MNIST、CIFAR-10/100、SVHN 等 CV 基准上优于 ReLU 和 ELU
- 在 Twitter POS 标注、TIMIT 语音识别等 NLP 任务上也有提升
- 后被 BERT、GPT-2/3、ViT 等里程碑模型广泛采用

## 5. 对 Channel Mixer 的意义
GELU 是 BERT 和 GPT 系列模型 FFN 层的标准激活函数，直接定义了 Transformer channel mixer 的非线性特性。GELU 的概率门控思想（按值大小而非符号决定信息通过量）影响了后续 GeGLU（GELU + GLU）的设计。在 Shazeer 2020 的 GLU 变体实验中，GeGLU 是表现最好的变体之一。

## 6. 总结
a) 核心思想：用高斯概率门控实现自适应平滑激活（15字）
b) 速记 pipeline：
   1. 输入 x 计算高斯 CDF Φ(x)
   2. 输出 = x · Φ(x)，按值大小概率性保留
   3. 光滑非单调，统一非线性与正则化
   4. 成为 BERT/GPT FFN 层标准激活函数
