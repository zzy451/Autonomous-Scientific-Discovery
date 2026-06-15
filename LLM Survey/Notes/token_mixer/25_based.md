# Based: Simple Linear Attention Language Models Balance the Recall-Throughput Tradeoff
**作者**: Simran Arora, Sabri Eyuboglu, Michael Zhang, Aman Timalsina, Frederic Sala, Christopher Ré (Stanford, University of Wisconsin) | **年份**: 2024 | **arxiv**: 2402.18668

## 0. 摘要翻译
本文研究了线性注意力语言模型在召回（recall）和吞吐量（throughput）之间的权衡。作者发现，通过增大循环状态的大小，线性注意力可以显著缩小与softmax注意力在召回密集型任务上的差距。提出Based架构，使用Taylor展开近似的线性注意力核，配合IO感知的CUDA内核实现，在保持亚二次复杂度的同时实现了高质量的语言建模。Based在召回和吞吐量之间取得了比Mamba和标准线性注意力更好的平衡。

## 1. 方法动机
a) **为什么提出**: 线性注意力模型（如Mamba）在需要精确召回的任务上（如从上下文中检索特定信息）明显落后于Transformer，这被称为"召回差距"（recall gap）。
b) **现有痛点**: (1) 线性注意力的循环状态大小有限，无法存储足够的上下文信息；(2) 增大状态会增加计算成本，需要高效的实现；(3) 现有线性注意力核（如elu+1）的近似质量不够好。
c) **研究假设**: (1) 召回能力与循环状态大小直接相关——更大的状态 = 更好的召回；(2) 通过Taylor展开近似softmax核，可以获得更好的特征映射；(3) IO感知的实现可以让大状态的线性注意力在实际中高效运行。

## 2. 方法设计
a) **Pipeline**: 使用Taylor展开的线性注意力核替代softmax注意力，配合滑动窗口注意力处理局部依赖。

b) **模块功能**:
- **Taylor线性注意力核**:
  - softmax核的二阶Taylor展开: $\phi(x) = [1, x_1, ..., x_d, x_1^2, x_1x_2, ..., x_d^2]$
  - 特征维度: 从$d$扩展到$1 + d + d(d+1)/2 \approx O(d^2)$
  - 线性注意力: $o_t = \phi(q_t)^T S_t / (\phi(q_t)^T z_t)$
  - 状态更新: $S_t = S_{t-1} + \phi(k_t) v_t^T$, $z_t = z_{t-1} + \phi(k_t)$
  - 状态大小: $O(d^2) \times d_v$，比标准线性注意力的$d \times d_v$大$O(d)$倍

- **滑动窗口组合**:
  - 线性注意力处理全局依赖（但精度有限）
  - 滑动窗口softmax注意力处理局部依赖（精确）
  - 两者互补: 局部用精确注意力，全局用线性近似

- **IO感知CUDA内核**:
  - 将大矩阵状态$S_t$分块存储在warp寄存器中
  - 避免将大状态写入HBM
  - 使用分块策略: 块内用并行matmul，块间用循环状态传递

c) **公式解释**:
- Taylor核的优势: 比elu+1更好地近似softmax核，保留了二阶交互信息
- 状态大小的权衡: $d^2 \times d_v$的状态提供了更大的记忆容量，但计算成本也更高
- 与Performer的区别: Performer用随机特征近似，Based用确定性的Taylor展开

## 3. 与其他方法对比
| 方面 | Based | Mamba | Linear Attention | Transformer |
|------|-------|-------|-----------------|-------------|
| 核函数 | Taylor展开 | N/A (SSM) | elu+1 | softmax |
| 状态大小 | $O(d^2)$ | $O(dN)$ | $O(d)$ | $O(Ld)$ KV cache |
| 召回能力 | 好 | 中 | 差 | 最好 |
| 吞吐量 | 高 | 高 | 最高 | 低 |
| 局部注意力 | 滑动窗口 | Conv1d | 无 | 全局 |

## 4. 实验表现
- **语言建模**: 在360M参数规模上，Based的PPL优于Mamba和标准线性注意力
- **召回任务**: 在MQAR等召回密集型任务上显著优于Mamba，接近Transformer
- **吞吐量**: prefill阶段比FlashAttention-2快，生成阶段与Mamba竞争
- **Scaling**: 召回能力随状态大小增加而稳步提升
- **实际速度**: IO感知内核使得大状态的线性注意力在实际中可行

## 5. 总结
a) **一句话概括**: Based通过Taylor展开的线性注意力核（$O(d^2)$状态）配合滑动窗口和IO感知CUDA内核，在召回能力和推理吞吐量之间取得了优于Mamba的平衡，证明了大状态线性注意力的潜力。
b) **速记pipeline**: x → Q,K,V → φ(Q),φ(K)(Taylor展开) → S_t = S_{t-1} + φ(k)vᵀ → o = φ(q)ᵀS/φ(q)ᵀz + SlidingWindowAttn → Output
