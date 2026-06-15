# Alibaba - Qwen2.5 架构分析

## 基本信息
- 论文标题：Qwen2.5 Technical Report
- 参数量：Dense 系列 0.5B/1.5B/3B/7B/14B/32B/72B；MoE 系列（Turbo/Plus，闭源）
- 层数：Qwen2.5-72B：80 层
- 隐藏维度：Qwen2.5-72B：8,192
- 注意力头数：Qwen2.5-72B：64 个 Query 头，8 个 KV 头（GQA）
- 上下文长度：Dense 模型 128K tokens；Turbo 1M tokens
- 训练数据量：18T tokens
- 发布时间：2024 年 9 月
- 论文链接：arXiv:2412.15115

## 六维度架构选择

| 维度 | 具体选择 | 技术细节 | 创新点 |
|------|----------|----------|--------|
| Token Mixer | Grouped Query Attention (GQA) | Qwen2.5-72B：64 Q 头，8 KV 头（8:1 比例）；支持 128K 上下文 | 标准 GQA 实现 |
| Channel Mixer | SwiGLU FFN (Dense) / MoE (闭源版) | Dense 版使用标准 SwiGLU FFN；MoE 版（Turbo/Plus）使用 Top-K 路由专家 | Dense 开源 + MoE 闭源的双轨策略 |
| Normalization | RMSNorm (Pre-Norm) | 在注意力和 FFN 子层之前应用 RMSNorm | 标准做法 |
| Position Encoding | RoPE (ABF 扩展) | 旋转位置编码；通过 Adaptive Base Frequency (ABF) 将 base 从 10,000 扩展至 1,000,000，支持长上下文 | ABF 频率调整是 RoPE 长度扩展的实用方法 |
| Residual Connection | Pre-Norm Residual | 标准 Pre-Norm 残差连接 | 标准做法 |
| Module Sequence | Pre-Norm: Norm → Attn → Add → Norm → FFN → Add | 标准 Pre-Norm 序列 | 标准做法 |

## 关键架构创新

1. **大规模高质量预训练数据**：18T tokens 的训练数据量在同期开源模型中领先，数据质量和多样性是 Qwen2.5 性能提升的核心驱动力。

2. **多阶段上下文扩展**：训练从 4096 token 上下文开始，逐步扩展至 32K，最终通过 ABF 调整 RoPE base frequency 支持 128K。Turbo 版进一步扩展至 1M。

3. **全尺寸覆盖**：从 0.5B 到 72B 的 7 个 Dense 模型尺寸，覆盖从边缘设备到数据中心的全场景需求。

4. **数据质量优先**：相比 Qwen2（7T tokens），Qwen2.5 将训练数据扩展至 18T tokens，同时通过更精细的数据过滤和合成数据提升质量。

## 与前代/同期模型对比

- **vs Qwen2**：训练数据从 7T 增至 18T tokens；架构基本不变，性能提升主要来自数据规模和质量。
- **vs Llama 3.1 70B**：相似规模（72B vs 70B），架构选择高度相似（GQA+SwiGLU+RMSNorm+RoPE），Qwen2.5 训练数据更多（18T vs 15T）。
- **vs DeepSeek-V2**：Qwen2.5 开源版为 Dense 架构 vs DeepSeek-V2 的 MoE；GQA vs MLA；标准 RoPE vs 解耦 RoPE。
- **vs GLM-4-9B**：相似架构选择，Qwen2.5 的 GQA 比例更温和（8:1 vs 16:1），训练数据更多（18T vs 10T）。

## 对本综述的启示
- Qwen2.5 代表了"标准架构 + 大规模高质量数据"的路线，架构创新有限但工程执行出色
- ABF 频率调整是 Position Encoding 维度中 RoPE 长度扩展的重要实践方法
- Dense 开源 + MoE 闭源的策略反映了 Channel Mixer 选择的商业考量
- 在六维度框架中定位：GQA (Token Mixer) + SwiGLU-Dense (Channel Mixer) + RMSNorm (Norm) + RoPE-ABF (PE) + Pre-Norm Residual (Residual) + Standard Pre-Norm Sequence (Module Seq)
