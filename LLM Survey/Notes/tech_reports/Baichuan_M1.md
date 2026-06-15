# Baichuan - Baichuan-M1 架构分析

## 基本信息
- 论文标题：Baichuan-M1: Pushing the Medical Capability of Large Language Models
- 参数量：14B（Baichuan-M1-14B，开源版本；Dense 模型）
- 层数：32
- 隐藏维度：4096（MLP 中间维度 22016）
- 注意力头数：32 个 Query 头，32 个 KV 头（MHA）；全局层头维度 256
- 上下文长度：32,768 tokens（32K）
- 词表大小：133,120（通用 + 医疗混合词表）
- RoPE base：1,000,000（支持长上下文）
- 训练数据量：20T tokens（医疗 + 通用数据，三阶段课程学习）
- 发布时间：2025 年 2 月
- 论文链接：arXiv:2502.12671

## 六维度架构选择

| 维度 | 具体选择 | 技术细节 | 创新点 |
|------|----------|----------|--------|
| Token Mixer | MHA + Short Convolution + 部分层 Sliding Window Attention | 32 Q 头 × 32 KV 头（标准 MHA）；全局层头维度增至 256；计算 Key/Value 时引入 Short Convolution 操作；部分层采用滑动窗口注意力以降低 KV cache 内存 | Short Convolution 减少对 induction heads 的依赖，增强上下文模式捕获；混合全局/局部注意力层 |
| Channel Mixer | SwiGLU FFN (Dense) | 中间维度 22016；SiLU 激活的门控线性单元 | 标准做法 |
| Normalization | RMSNorm (Pre-Norm) | 在注意力和 FFN 子层之前应用 RMSNorm | 标准做法 |
| Position Encoding | RoPE (base=1,000,000) | 旋转位置编码，base 设为 1M 以支持 32K 上下文 | 高 base 值设计适配长上下文医疗文档 |
| Residual Connection | Pre-Norm Residual | 标准 Pre-Norm 残差连接 | 标准做法 |
| Module Sequence | Pre-Norm: Norm → Attn → Add → Norm → FFN → Add | 基于 LLaMA 框架的标准 Pre-Norm 序列 | 标准做法 |

## 关键架构创新

1. **Short Convolution on K/V**：在计算 Key 和 Value 时引入短卷积操作，减少模型对 induction heads 的依赖，增强对重复模式和上下文依赖的捕获能力。这是架构层面的独特设计。

2. **混合全局/滑动窗口注意力**：部分层使用滑动窗口注意力以降低 KV cache 内存占用，提升长序列推理效率；其余层保持全局注意力以维持远距离依赖建模能力。

3. **全局层头维度增大至 256**：相比常见的 128 维头维度，全局注意力层将头维度提升至 256，增强每个注意力头的表达能力。

4. **超大医疗混合词表**：词表大小 133,120，专门设计了通用 + 医疗术语的混合 tokenizer，减少医疗专业术语的 token 碎片化。

5. **三阶段课程学习**：训练分为通用知识增强 → 医疗基础知识 → 医疗高级知识三个阶段，20T tokens 从头训练。

6. **20+ 医疗科室专精建模**：针对 20 多个医疗科室进行细粒度专业化建模，而非将医疗作为单一领域处理。

## 与前代/同期模型对比

- **vs Baichuan 2-13B**：Baichuan-M1 从头训练（而非微调），训练数据从 2.6T 增至 20T tokens，专注医疗领域。
- **vs Med-PaLM 2 / GPT-4 Medical**：Baichuan-M1 是开源的医疗专用模型，而 Med-PaLM 2 和 GPT-4 为闭源通用模型的医疗应用。
- **vs Qwen2.5-14B / Phi-4**：相同参数规模（14B），但 Baichuan-M1 专注医疗领域，训练数据量更大（20T vs 18T/9.8T）。

## 对本综述的启示
- Short Convolution on K/V 是 Token Mixer 维度的独特创新，在注意力计算中引入卷积操作，值得在综述中作为"混合注意力机制"的案例
- 混合全局/滑动窗口注意力层的设计与 Gemma 2 类似，体现了"异构层"的趋势
- 全局层头维度 256 是少见的设计选择，展示了头维度作为可调超参数的潜力
- 超大医疗混合词表（133K）展示了领域专用 tokenizer 设计的重要性
- 在六维度框架中定位：MHA+ShortConv+SWA (Token Mixer) + SwiGLU-Dense (Channel Mixer) + RMSNorm (Norm) + RoPE-1M (PE) + Pre-Norm Residual (Residual) + Standard Pre-Norm Sequence (Module Seq)
