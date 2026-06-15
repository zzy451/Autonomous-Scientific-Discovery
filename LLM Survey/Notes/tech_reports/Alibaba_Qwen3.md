# Alibaba - Qwen3 架构分析

## 基本信息
- 论文标题：Qwen3 Technical Report
- 参数量：Dense 系列 0.6B / 1.7B / 4B / 8B / 14B / 32B；MoE 系列 30B-A3B（30B 总/3B 激活）、235B-A22B（235B 总/22B 激活）
- 旗舰模型 Qwen3-235B-A22B 配置：
  - 层数：94 层
  - 隐藏维度：4,096
  - FFN 中间维度：12,288
  - 注意力头数：64（Query）/ 4（KV），GQA 比例 16:1
  - 专家数：128 总 / 8 激活
- 上下文长度：128K tokens（32B/14B/8B）；32K tokens（4B/1.7B/0.6B）
- 词表大小：151,669（Byte-level BPE，Qwen 分词器）
- 训练数据量：约 36T tokens（覆盖 119 种语言）
- 发布时间：2025 年 4 月 29 日
- 论文链接：arXiv:2505.09388

## 六维度架构选择

| 维度 | 具体选择 | 技术细节 | 创新点 |
|------|----------|----------|--------|
| Token Mixer | Grouped-Query Attention (GQA) + QK-Norm | 旗舰 235B-A22B: 64 Q 头 / 4 KV 头（16:1 比例）；引入 QK-Norm（对 Q 和 K 矩阵应用归一化）提高训练稳定性；去除了 Qwen2 中的 QKV-bias | QK-Norm 替代传统的 logit softcapping，用更简洁的方式稳定注意力计算 |
| Channel Mixer | MoE-SwiGLU（旗舰）/ Dense-SwiGLU | MoE 版本：128 个专家，Top-8 路由，中间维度 12,288；采用细粒度专家分割（类似 DeepSeekMoE）；不使用共享专家（与 Qwen2.5-MoE 不同） | 细粒度专家分割 + 无共享专家的设计选择；global-batch 负载均衡损失促进专家专精化 |
| Normalization | RMSNorm (Pre-Norm) | 标准 RMSNorm，应用于 Attention 和 FFN 之前 | 标准做法 |
| Position Encoding | RoPE | 旋转位置编码；使用 YaRN 技术扩展上下文长度 | 支持 128K 上下文 |
| Residual Connection | Pre-Norm Residual | 标准 Pre-Norm 残差连接 | 标准做法 |
| Module Sequence | Pre-Norm: Norm -> Attn -> Add -> Norm -> FFN/MoE -> Add | 标准 Pre-Norm Transformer 序列 | 标准做法 |

## 关键架构创新

1. **思考/非思考双模式统一框架**：在单一模型中集成 Thinking Mode（链式推理，适合复杂任务）和 Non-Thinking Mode（快速直接响应），通过 chat template 或用户指令动态切换，无需部署多个模型（如分别部署通用模型和推理模型）。

2. **QK-Norm 替代 Softcapping**：在 Qwen2 基础上移除了 QKV-bias，引入 QK-Norm（对 Query 和 Key 矩阵进行归一化），提高大规模训练稳定性。这是 Gemma 2/3 也采用的趋势。

3. **细粒度 MoE + 无共享专家**：128 个专家的细粒度设计（类似 DeepSeek 系列），但与 Qwen2.5-MoE 和 DeepSeek-V3 不同，Qwen3 MoE 不使用共享专家，所有专家均通过路由选择。

4. **超大规模多语言训练**：36T tokens 训练数据，覆盖 119 种语言，是目前公开报告中最大规模的训练数据之一。

5. **Global-Batch 负载均衡损失**：替代传统的 per-sample 或 per-sequence 辅助损失，在全局 batch 层面鼓励专家负载均衡，减少对模型性能的负面影响。

## 与前代/同期模型对比

- **vs Qwen2.5**：移除 QKV-bias，引入 QK-Norm；MoE 版本移除共享专家；训练数据从约 18T 增至 36T tokens；新增思考/非思考双模式。
- **vs DeepSeek-V3**：同样采用细粒度 MoE，但 Qwen3 专家数 128 vs DeepSeek-V3 的 256+1 共享；Qwen3 无共享专家 vs DeepSeek-V3 有 1 个共享专家；负载均衡策略不同（global-batch loss vs auxiliary-loss-free bias）。
- **vs Llama 3**：Qwen3 旗舰采用 MoE 而非 Dense，参数效率更高（22B 激活 vs 405B 全激活）；GQA 比例更激进（16:1 vs 16:1 for 405B）。
- **vs Gemma 3**：均采用 QK-Norm，但 Qwen3 走 MoE 路线而 Gemma 3 保持 Dense。

## 对本综述的启示
- Qwen3 展示了 MoE 架构从 DeepSeek 系列向更广泛模型家族扩散的趋势
- QK-Norm 的采用（Qwen3 + Gemma 3）表明这已成为 Normalization 维度的新标准做法
- "无共享专家" vs "有共享专家" 的设计选择值得在综述中讨论
- 思考/非思考双模式是推理增强的重要架构趋势
- 在六维度框架中定位：GQA+QK-Norm (Token Mixer) + MoE-SwiGLU (Channel Mixer) + RMSNorm (Norm) + RoPE+YaRN (PE) + Pre-Norm Residual (Residual) + Standard Pre-Norm Sequence (Module Seq)
