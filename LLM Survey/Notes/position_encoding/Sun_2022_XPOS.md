# A Length-Extrapolatable Transformer (XPOS)
**作者**: Yutao Sun, Li Dong, Barun Patra, Shuming Ma, Shaohan Huang, Al-Rashid Benber, Vishrav Chaudhary, Xia Song, Furu Wei | **年份**: 2022 | **来源**: Microsoft Research / arXiv (后收录于 ACL 2023) | **arXiv**: 2212.10554

## 0. 摘要翻译
本文提出 XPOS（Extrapolatable Position Embedding），一种系统性的长度外推方法。XPOS 在 RoPE 的基础上引入指数衰减因子，使注意力分数随 token 距离增大而自然衰减。通过将衰减因子分别分配给 query 和 key（一方乘以正指数、另一方乘以负指数），XPOS 在保持 RoPE 相对位置编码优势的同时，显著提升了长度外推能力。

## 1. 方法动机
a) **为什么提出**: RoPE 虽然编码了相对位置，但缺乏随距离衰减的归纳偏置，在长度外推时注意力分数可能变得不稳定。
b) **现有痛点**: 
   - RoPE 在训练长度之外性能显著下降
   - ALiBi 虽有距离衰减但采用加性偏置，与 RoPE 的乘性编码不兼容
   - 需要一种在 RoPE 框架内引入衰减的方法
c) **研究假设**: 在 RoPE 的旋转矩阵上乘以指数衰减因子，可以在保留相对位置编码的同时，引入有利于长度外推的距离衰减特性。

## 2. 方法设计
a) **pipeline**: 
   1. 计算标准 RoPE 旋转矩阵 $R_{\Theta,m}$
   2. 对每个频率维度 $i$，计算指数衰减因子 $\gamma_i$
   3. Query 乘以 $\gamma_i^m$（正幂），Key 乘以 $\gamma_i^{-n}$（负幂）
   4. 计算注意力分数时，衰减因子组合为 $\gamma_i^{m-n}$

b) **模块功能**: 指数衰减因子为注意力施加了位置相关的缩放，使远距离 token 对的注意力权重自然减小。

c) **公式解释**:
   - 标准 RoPE 内积: $q_m^T k_n = x_m^T R_{\Theta,m-n} x_n$
   - XPOS 修改: $q_m^T k_n = x_m^T \Lambda^m R_{\Theta,m-n} \Lambda^{-n} x_n$
   - 其中 $\Lambda = \text{diag}(\gamma_1, \gamma_2, ..., \gamma_{d/2})$
   - $\gamma_i = (i/d + \epsilon)^{1/d}$（或类似形式），使不同维度有不同衰减速率
   - 高频维度衰减较快（关注局部），低频维度衰减较慢（关注全局）

## 3. 与其他方法对比
a) **本质不同**: 
   - 与 RoPE：XPOS = RoPE + 指数衰减，增加了距离衰减归纳偏置
   - 与 ALiBi：ALiBi 用加性线性偏置，XPOS 用乘性指数衰减，且保留了旋转编码
   - 与 PI/YaRN：PI/YaRN 是 RoPE 的后处理扩展，XPOS 是 RoPE 的架构修改
b) **创新点**: 
   - 将 ALiBi 的距离衰减思想与 RoPE 的旋转编码统一在乘法框架中
   - 通过将衰减因子分配给 Q 和 K（正负幂），保持了内积形式
   - 每个频率维度有不同的衰减率，形成多尺度注意力
c) **适用场景**: 需要长度外推的场景；新模型预训练时可替代 RoPE。

## 4. 实验表现
a) **验证方式**: 在语言建模任务上评估，训练 1024 token 后测试更长序列的困惑度。
b) **关键数据**: 
   - 在 4096 token（4x 训练长度）上的困惑度显著优于 RoPE
   - 外推稳定性优于 ALiBi 和 RoPE
   - 在 blockwise causal attention 场景下也有效
c) **局限性**: 
   - 尚未在大规模 LLM 训练中被广泛采用（主流仍是 RoPE + PI/YaRN）
   - 指数衰减可能导致对非常长距离信息的过度抑制
   - 衰减因子的具体设置需要经验调整

## 5. 总结
a) **一句话概括**: XPOS 在 RoPE 旋转矩阵上叠加指数衰减因子，将乘性距离衰减融入旋转位置编码框架，显著提升了 Transformer 的长度外推能力。
b) **速记 pipeline**: Q/K Linear → RoPE Rotation × Exponential Decay ($\gamma^{m-n}$ per dim) → Distance-Decayed Rotary Attention
