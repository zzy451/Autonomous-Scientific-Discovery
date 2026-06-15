# Eagle and Finch: RWKV with Matrix-Valued States and Dynamic Recurrence (RWKV v5/v6)
**作者**: Bo Peng, Daniel Goldstein, Quentin Anthony, Alon Albalak, Eric Alcaide, Stella Biderman, Eugene Cheah, Xingjian Du, Teddy Ferdinan, Haowen Hou, Przemyslaw Kazienko, Kranthi Kiran GV, Jan Kocon, Bartlomiej Koptyra, Satyapriya Krishna, Ronald McClelland Jr., Jiaju Lin, Niklas Muennighoff, Fares Obeid, Atsushi Saito, Guangyu Song, Haoqin Tu, Stanislaw Wozniak, Ruichong Zhang, Bingchen Zhao, Qihang Zhao, Peng Zhou, Jian Zhu, Rui-Jie Zhu | **年份**: 2024 | **arxiv**: 2404.05892

## 0. 摘要翻译
本文介绍RWKV架构的两个重要更新版本：RWKV-5（Eagle）和RWKV-6（Finch）。Eagle引入了矩阵值状态（multi-headed matrix-valued states），将标量状态扩展为矩阵，显著增加了模型的表达能力和记忆容量。Finch在Eagle基础上进一步引入了数据依赖的动态循环（dynamic recurrence），使得时间衰减和token shift参数依赖于输入，类似于Mamba的选择性机制。两个版本均在多语言和多任务基准上取得了与同规模Transformer竞争的性能。

## 1. 方法动机
a) **为什么提出**: RWKV-4的标量状态（每个通道一个标量）限制了记忆容量；固定的时间衰减参数无法根据输入内容动态调整。
b) **现有痛点**: (1) RWKV-4的状态维度为$d$（向量），记忆容量有限；(2) 固定的$w$衰减参数无法适应不同上下文；(3) 固定的token shift插值系数$\mu$限制了灵活性。
c) **研究假设**: 矩阵值状态（$d_k \times d_v$矩阵）可以大幅增加记忆容量；数据依赖的参数可以提升模型的上下文适应能力。

## 2. 方法设计
a) **Pipeline**: 与RWKV-4结构类似，但Time-Mixing模块进行了重大升级。

b) **模块功能**:
- **RWKV-5 (Eagle) 改进**:
  - **矩阵值状态**: 状态从向量$s_t \in \mathbb{R}^d$扩展为矩阵$S_t \in \mathbb{R}^{d_k \times d_v}$
  - **多头结构**: 引入多个头，每个头维护独立的状态矩阵
  - 更新: $S_t^{(h)} = \text{diag}(w^{(h)}) S_{t-1}^{(h)} + k_t^{(h)} v_t^{(h)T}$
  - 输出: $o_t^{(h)} = S_t^{(h)T} r_t^{(h)}$（receptance门控读取）
  - 记忆容量从$O(d)$提升到$O(H \times d_k \times d_v)$

- **RWKV-6 (Finch) 额外改进**:
  - **数据依赖的时间衰减**: $w_t = w_0 + \text{tanh}(W_w \cdot x_t')$，衰减率随输入变化
  - **数据依赖的Token Shift**: $\mu_t = \sigma(W_\mu \cdot x_t)$，插值系数也随输入变化
  - **LoRA式参数化**: 部分投影使用低秩分解减少参数量
  - 更新: $S_t^{(h)} = \text{diag}(w_t^{(h)}) S_{t-1}^{(h)} + k_t^{(h)} v_t^{(h)T}$（$w_t$现在是输入依赖的）

c) **公式解释**:
- Eagle的矩阵状态: 类似线性注意力的$S = \sum k_i v_i^T$，但带衰减$w$
- Finch的动态衰减: 类似Mamba的选择性——模型可以根据输入决定"记住"还是"遗忘"
- 与Mamba的区别: RWKV用对角衰减矩阵$\text{diag}(w_t)$，Mamba用标量$\Delta_t$控制全局衰减

## 3. 与其他方法对比
| 方面 | RWKV-6 (Finch) | RWKV-4 | Mamba | RetNet |
|------|----------------|--------|-------|--------|
| 状态类型 | 矩阵$d_k \times d_v$ | 向量$d$ | 向量$N$ per channel | 矩阵$d \times d$ |
| 衰减 | 输入依赖 | 固定 | 输入依赖$\Delta$ | 固定$\gamma$ |
| Token Shift | 输入依赖 | 固定 | N/A（用Conv1d）| N/A |
| 多头 | 是 | 否 | 否（多通道）| 是（多尺度）|
| 记忆容量 | $H \times d_k \times d_v$ | $d$ | $d \times N$ | $d \times d$ |

## 4. 实验表现
- **语言建模**: Eagle-7B和Finch-7B在多个基准上接近Llama2-7B和Mistral-7B
- **多语言**: 在多语言基准上表现优异（训练数据包含100+语言）
- **长序列**: 推理时内存恒定，支持任意长度
- **Finch vs Eagle**: Finch在大多数任务上优于Eagle（动态衰减的优势）
- **训练规模**: Eagle训练了1.1T tokens，Finch训练了1.4T tokens
- **效率**: 推理速度与RWKV-4相当，远快于Transformer

## 5. 总结
a) **一句话概括**: RWKV-5(Eagle)通过矩阵值多头状态大幅提升记忆容量，RWKV-6(Finch)进一步引入输入依赖的动态衰减和token shift，使RWKV系列在保持线性复杂度的同时达到与同规模Transformer竞争的性能。
b) **速记pipeline**: x → DataDep-TokenShift → R,K,V,w(x) → S_t = diag(w_t)·S_{t-1} + k·vᵀ → o = Sᵀ·r → Output
