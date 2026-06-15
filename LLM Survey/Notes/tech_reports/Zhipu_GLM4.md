# 智谱 AI - GLM-4 架构分析

## 基本信息
- 论文标题：ChatGLM: A Family of Large Language Models from GLM-130B to GLM-4 All Tools
- 参数量：GLM-4 系列（旗舰版参数未公开；开源版 GLM-4-9B：9B 参数）
- 层数：GLM-4-9B：40 层
- 隐藏维度：GLM-4-9B：4096
- 注意力头数：GLM-4-9B：32 个 Query 头，2 个 KV 头（GQA）；每头维度 128
- 中间维度：GLM-4-9B：13696
- 上下文长度：GLM-4 旗舰版 128K；GLM-4-9B 8K（实验版 1M）
- 词表大小：151,552
- 训练数据量：约 10T tokens（中英文为主，覆盖 24+ 语言）
- 发布时间：2024 年 6 月
- 论文链接：arXiv:2406.12793

## 六维度架构选择

| 维度 | 具体选择 | 技术细节 | 创新点 |
|------|----------|----------|--------|
| Token Mixer | Grouped Query Attention (GQA) | GLM-4-9B：32 个 Query 头，2 个 KV 头（极端 GQA，16:1 比例）；每头维度 128；使用 FlashAttention 加速 | 极端的 GQA 比例（16:1）大幅压缩 KV cache |
| Channel Mixer | SwiGLU FFN (Dense) | 中间维度 13696；SwiGLU 激活函数 | 标准做法 |
| Normalization | RMSNorm (Pre-Norm) | 在注意力和 FFN 子层之前应用 RMSNorm | 标准做法 |
| Position Encoding | RoPE | 旋转位置编码；支持长上下文扩展至 128K/1M | 标准做法 |
| Residual Connection | Pre-Norm Residual | 标准 Pre-Norm 残差连接 | 标准做法 |
| Module Sequence | Pre-Norm: Norm → Attn → Add → Norm → FFN → Add | 标准 Pre-Norm 序列 | 标准做法 |

## 关键架构创新

1. **GLM 架构演进**：从早期的 GLM（自回归填空预训练）逐步演进为标准因果语言模型架构。GLM-4 系列已基本采用标准 Decoder-only Transformer，放弃了早期 GLM 的双向注意力填空范式。

2. **All Tools 能力**：GLM-4 的核心创新不在底层架构，而在于 All Tools 能力——模型可以自主决定调用网页浏览器、代码解释器、绘图工具等外部工具，实现复杂任务的自动化。

3. **极端 GQA 比例**：GLM-4-9B 使用 32:2 的 Q:KV 头比例（16:1），比常见的 8:1 或 4:1 更激进，进一步压缩 KV cache。

4. **超长上下文**：GLM-4-9B-Chat-1M 实验版支持 1M token 上下文，展示了 RoPE 扩展的极限能力。

## 与前代/同期模型对比

- **vs ChatGLM-6B/ChatGLM2/ChatGLM3**：架构从 GLM 双向填空范式逐步过渡到标准因果 LM；从 LayerNorm 演进到 RMSNorm；引入 GQA 替代 MHA/MQA。
- **vs Llama 3 8B**：相似规模（9B vs 8B），GLM-4-9B 的 GQA 更激进（2 KV 头 vs 8 KV 头），层数更多（40 vs 32）。
- **vs Qwen2.5-7B**：同为中国团队的开源模型，架构选择相似（GQA+SwiGLU+RMSNorm+RoPE），GLM-4 的 GQA 比例更极端。
- **vs Mistral 7B**：GLM-4-9B 无滑动窗口注意力，使用更激进的 GQA 比例。

## 对本综述的启示
- GLM 系列的架构演进（从 GLM 填空到标准因果 LM）反映了社区对 Decoder-only 架构的共识收敛
- 极端 GQA 比例（16:1）是 Token Mixer 维度中 KV cache 压缩的一个极端数据点
- 论文重点在工具调用和对齐，架构细节（尤其旗舰版）公开有限
- 在六维度框架中定位：GQA (Token Mixer) + SwiGLU-Dense (Channel Mixer) + RMSNorm (Norm) + RoPE (PE) + Pre-Norm Residual (Residual) + Standard Pre-Norm Sequence (Module Seq)
