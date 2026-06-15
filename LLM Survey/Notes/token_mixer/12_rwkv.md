# RWKV: Reinventing RNNs for the Transformer Era
**作者**: Bo Peng, Eric Alcaide, Quentin Anthony, Alon Albalak, Samuel Arcadinho, Huanqi Cao, Xin Cheng, Michael Chung, Matteo Grella, Kranthi Kiran GV, Xuzheng He, Haowen Hou, Przemyslaw Kazienko, Jan Kocon, Jiaming Kong, Bartlomiej Koptyra, Hayden Lau, Krishna Sri Ipsit Mantri, Ferdinand Mom, Atsushi Saito, Xiangru Tang, Bolun Wang, Johan S. Wind, Stansilaw Wozniak, Ruichong Zhang, Zhenyuan Zhang, Qihang Zhao, Peng Zhou, Jian Zhu, Rui-Jie Zhu | **年份**: 2023 | **arxiv**: 2305.13048

## 0. 摘要翻译
Transformer在NLP任务中占据主导地位，但由于自注意力机制的二次复杂度，在处理长序列时面临内存和计算挑战。本文提出RWKV（Receptance Weighted Key Value），一种结合了RNN和Transformer优势的新型架构。RWKV利用线性注意力机制实现高效的线性缩放，同时保持Transformer的表达能力和训练并行性。该方法通过"token shift"时间混合和"channel mixing"通道混合来捕获时序和通道维度的信息。

## 1. 方法动机
a) **为什么提出**: 需要一种既能像Transformer一样高效并行训练，又能像RNN一样高效推理（常数内存、常数时间/步）的架构。
b) **现有痛点**: (1) Transformer推理时KV cache随序列长度线性增长；(2) RNN训练时无法并行化；(3) 之前的线性注意力方法性能不足。
c) **研究假设**: 通过精心设计的线性注意力变体（WKV机制）和时间衰减，可以在保持RNN推理效率的同时实现Transformer级别的训练并行性和模型质量。

## 2. 方法设计
a) **Pipeline**: 交替堆叠Time-Mixing（token mixer）和Channel-Mixing（channel mixer）模块，每个模块前都有LayerNorm。

b) **模块功能**:
- **Token Shift**: 将当前token的表示与前一个token的表示进行线性插值：$x_t' = \mu \odot x_t + (1-\mu) \odot x_{t-1}$，其中$\mu$是可学习参数。这为模型提供了相邻token的信息。
- **Time-Mixing (WKV机制)**:
  - $r_t = W_r \cdot x_t'$（receptance，类似gate）
  - $k_t = W_k \cdot x_t'$（key）
  - $v_t = W_v \cdot x_t'$（value）
  - WKV计算: $wkv_t = \frac{\sum_{i=1}^{t-1} e^{-(t-1-i)w+k_i} v_i + e^{u+k_t} v_t}{\sum_{i=1}^{t-1} e^{-(t-1-i)w+k_i} + e^{u+k_t}}$
  - 输出: $o_t = W_o \cdot (\sigma(r_t) \odot wkv_t)$
  - $w$是时间衰减参数（每个通道不同），$u$是当前token的bonus参数
- **Channel-Mixing**:
  - $r_t = W_r \cdot x_t'$, $k_t = W_k \cdot x_t'$
  - $o_t = \sigma(r_t) \odot (W_v \cdot \max(k_t, 0)^2)$
  - 使用squared ReLU激活，receptance门控

c) **公式解释**:
- WKV本质是带指数衰减的加权平均：越近的token权重越大（通过$w$衰减），但key值大的token也能获得高权重
- 可以写成RNN形式：$a_t = e^{-w} a_{t-1} + e^{k_t} v_t$, $b_t = e^{-w} b_{t-1} + e^{k_t}$, $wkv_t = a_t/b_t$
- 训练时可以并行计算（类似线性注意力的chunk-wise并行）

## 3. 与其他方法对比
| 方面 | RWKV | Transformer | Mamba | Linear Attention |
|------|------|-------------|-------|-----------------|
| 训练复杂度 | $O(Ld)$ | $O(L^2d)$ | $O(LdN)$ | $O(Ld^2)$ |
| 推理复杂度 | $O(d)$/step | $O(Ld)$/step | $O(dN)$/step | $O(d^2)$/step |
| 状态大小 | $O(d)$ | $O(Ld)$ KV cache | $O(dN)$ | $O(d^2)$ |
| 选择性 | 通过$k$值 | 完全动态 | 输入依赖$\Delta,B,C$ | 无 |
| 训练并行 | 是 | 是 | scan并行 | 是 |

## 4. 实验表现
- **语言建模**: RWKV-14B在多个zero-shot基准上接近同规模Transformer（如Pythia-12B）
- **长序列**: 推理时内存恒定，可处理任意长度序列
- **多语言**: 在多语言基准上表现良好
- **训练效率**: 训练速度接近Transformer（线性注意力的并行计算）
- **推理效率**: 生成速度恒定，不随上下文长度增加而变慢
- **规模验证**: 从169M到14B参数均有验证，scaling行为良好

## 5. 总结
a) **一句话概括**: RWKV通过WKV线性注意力机制（带指数时间衰减和receptance门控）实现了"训练像Transformer、推理像RNN"的架构，在保持线性复杂度的同时接近Transformer的语言建模性能。
b) **速记pipeline**: x → TokenShift(x,x_{t-1}) → [R=σ(Wr·x'), WKV=ExpDecayAttn(K,V,w)] → R⊙WKV → Output
