# CLEX: Continuous Length Extrapolation for Large Language Models
**作者**: Guanzheng Chen, Xin Li, Zaiqiao Meng, Shangsong Liang, Lidong Bing
**年份**: 2023/2024 | **arxiv**: 2310.16450 | **venue**: ICLR 2024

## 0. 摘要翻译
CLEX 将位置编码的缩放方法推广为关于长度缩放因子的常微分方程（ODE），通过神经 ODE 建模 RoPE 频率随上下文长度的连续动态变化，从而克服现有离散缩放方法的局限性。实验表明 CLEX 可将上下文窗口有效扩展到训练长度的 4 倍甚至 8 倍，且性能无明显退化。

## 1. 方法动机
- 现有 RoPE 缩放方法（PI、NTK-aware、YaRN）都是针对特定目标长度设计的离散缩放策略
- 这些方法在训练长度和目标长度之间缺乏平滑过渡，导致中间长度性能不稳定
- 不同长度需要不同的缩放因子，但现有方法无法自适应调整
- 核心问题：能否将离散的缩放策略统一为连续的动态过程？

## 2. 核心方法

### 2.1 ODE 建模框架
将 RoPE 频率的缩放过程建模为关于长度缩放因子 $t$ 的 ODE：
$$\frac{d\boldsymbol{\theta}(t)}{dt} = f_\phi(\boldsymbol{\theta}(t), t)$$
其中：
- $\boldsymbol{\theta}(t)$ 是在缩放因子 $t$ 下的 RoPE 频率向量
- $f_\phi$ 是由神经网络参数化的动态函数
- $t=1$ 对应原始训练长度，$t>1$ 对应扩展长度

### 2.2 连续外推
- 初始条件 $\boldsymbol{\theta}(1)$ 为原始 RoPE 频率
- 通过 ODE 求解器（如 Euler、RK4）积分到任意目标 $t$
- 神经网络 $f_\phi$ 学习频率随长度变化的连续规律
- 训练时只需少量长度点，推理时可外推到任意长度

### 2.3 统一视角
CLEX 将现有方法统一为 ODE 的特殊情况：
- **Position Interpolation**: $f_\phi = -\boldsymbol{\theta}/t$（线性缩放）
- **NTK-aware**: 对不同频率维度施加不同缩放速率
- **YaRN**: 分段线性缩放策略
- CLEX 通过学习 $f_\phi$ 自动发现最优的连续缩放路径

## 3. 实验结果
- 基于 LLaMA-2-7B 和 CodeLLaMA-7B 验证
- 训练长度 4K → 有效扩展到 16K（4x）甚至 32K（8x）
- 在 LongBench 上超越 PI、NTK-aware、YaRN
- Perplexity 在扩展长度范围内保持平稳
- 在 passkey retrieval 任务上达到近乎完美的准确率
- 参数开销极小（仅 ODE 网络的少量参数）

## 4. 关键优势
1. **连续性**：任意长度都有对应的最优频率配置，无需离散跳变
2. **泛化性**：训练少量长度点即可外推到更长序列
3. **统一性**：将现有方法纳入统一框架，便于理论分析
4. **轻量级**：ODE 网络参数量极小，几乎不增加模型大小

## 5. 与本综述的关联
- 提供了 RoPE 缩放方法的统一理论框架（ODE 视角）
- 连续外推思想对后续工作（LongRoPE2 等）有重要启发
- 展示了将离散方法连续化的一般性研究范式
- 与 NTK-aware、YaRN 等方法形成方法论对比

## 6. 标签
`#RoPE` `#长度外推` `#ODE` `#连续缩放` `#神经ODE` `#ICLR2024`
