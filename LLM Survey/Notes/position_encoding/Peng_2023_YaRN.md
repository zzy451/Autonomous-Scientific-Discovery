# YaRN: Efficient Context Window Extension of Large Language Models
**作者**: Bowen Peng, Jeffrey Quesnelle, Honglu Fan, Enrico Shippole | **年份**: 2023 | **来源**: ICLR 2024 | **arXiv**: 2309.00071

## 0. 摘要翻译
本文提出 YaRN（Yet another RoPE extensioN），一种高效的上下文窗口扩展方法，用于基于 RoPE 的大型语言模型。YaRN 结合了 NTK-by-parts 插值和注意力温度缩放两项技术，仅需少量微调数据（约预训练数据的 0.1%）即可将上下文窗口扩展至训练长度的数倍。与之前的方法相比，YaRN 在训练步数上快 10 倍，并支持外推到超出微调长度的序列。

## 1. 方法动机
a) **为什么提出**: RoPE 在预训练上下文长度之外性能急剧下降。现有扩展方法（如 Position Interpolation）效果有限且需要较多微调。
b) **现有痛点**: 
   - 线性位置插值（PI）均匀缩放所有频率维度，导致高频信息丢失
   - NTK-aware 缩放虽改善了高频保持，但仍不够精细
   - 长上下文中注意力分布的熵增导致关注力分散
c) **研究假设**: 通过对不同频率维度采用不同的缩放策略（保留高频、插值低频），并通过温度缩放修正注意力分布，可以高效且准确地扩展上下文窗口。

## 2. 方法设计
a) **pipeline**: 
   1. 分析 RoPE 各维度的波长，将维度分为高频、中频、低频三组
   2. 高频维度：不插值（保持原始）
   3. 低频维度：完全插值
   4. 中频维度：使用 ramp 函数混合插值与不插值
   5. 额外施加注意力温度缩放以修正注意力分布

b) **模块功能**: 
   - NTK-by-parts：根据维度频率选择性插值，保护局部位置分辨率
   - 温度缩放：调整 softmax 前的 logits 温度，防止注意力过于分散

c) **公式解释**:
   - 维度分组标准：按波长 $\lambda_i = 2\pi / \theta_i$ 与训练长度 $L$ 的比值
   - 高频（$\lambda_i < L$）: 不缩放
   - 低频（$\lambda_i > \alpha L$）: 按 $s = L'/L$ 缩放
   - 中频: 使用 ramp 函数 $\gamma(r) = (r - \beta_{low}) / (\beta_{high} - \beta_{low})$ 混合
   - 温度缩放: $\text{softmax}(\frac{q^T k}{t\sqrt{d}})$，其中 $\sqrt{1/t} \approx 0.1 \ln(s) + 1$
   - 实现技巧：温度缩放可直接通过缩放 RoPE 嵌入实现，零额外推理开销

## 3. 与其他方法对比
a) **本质不同**: 
   - 与 PI（线性插值）：PI 均匀缩放所有维度，YaRN 选择性地只缩放低频维度
   - 与 NTK-aware：NTK-aware 改变基频，YaRN 的 NTK-by-parts 更精细地分区处理
   - 与 ALiBi/CoPE：ALiBi/CoPE 是新的 PE 方案，YaRN 是 RoPE 的扩展方法
b) **创新点**: 
   - NTK-by-parts 的精细频率分区策略
   - 注意力温度缩放的引入（首次发现并解决长上下文注意力熵增问题）
   - 通过 RoPE 缩放实现零推理开销的温度调整
c) **适用场景**: 扩展 RoPE-based LLM（如 LLaMA 2/3, Mistral）的上下文窗口；已被多个开源项目和框架采用。

## 4. 实验表现
a) **验证方式**: 在 LLaMA 和 Llama 2 模型上，评估扩展至 64k-128k token 后的困惑度和下游任务性能。
b) **关键数据**: 
   - 在 Llama 2 7B 上，仅 400 步微调即可将 4k 上下文扩展至 64k
   - 比 PI 快约 10 倍达到相同效果
   - 支持外推到微调长度的 2 倍以上
   - Dynamic YaRN（无微调版本）也能实现合理的上下文扩展
c) **局限性**: 
   - 仍需少量微调才能获得最佳效果
   - 极端扩展倍数（>16x）下性能仍会下降
   - 温度缩放参数需要按模型经验调整

## 5. 总结
a) **一句话概括**: YaRN 通过 NTK-by-parts 频率选择性插值和注意力温度缩放两项技术，以极少的微调步数高效扩展 RoPE-based LLM 的上下文窗口，是当前最流行的 RoPE 扩展方案之一。
b) **速记 pipeline**: RoPE Dimensions → Frequency Grouping (High/Mid/Low) → Selective Interpolation (NTK-by-parts) + Attention Temperature Scaling → Extended Context
