# AI2 - OLMo 2 架构分析

## 基本信息
- 论文标题：2 OLMo 2 Furious
- 参数量：7B / 13B / 32B（三个尺寸）
- 层数：7B：32 层；13B：40 层（推测）；32B：未明确
- 隐藏维度：7B：4096；13B：5120（推测）
- 注意力头数：7B：32 头（推测）
- 上下文长度：4096 tokens
- 训练数据量：7B：4.05T tokens；13B：5.6T tokens
- 发布时间：2025 年 1 月
- 论文链接：arXiv:2501.00656

## 六维度架构选择

| 维度 | 具体选择 | 技术细节 | 创新点 |
|------|----------|----------|--------|
| Token Mixer | 标准注意力（推测 MHA 或 GQA） | QKV Clipping（受 DBRX 启发）防止注意力值过大；上下文 4096 | QKV Clipping 增强训练稳定性 |
| Channel Mixer | SwiGLU FFN (Dense) | SwiGLU 激活函数 | 标准做法 |
| Normalization | RMSNorm（Reordered/Post-Norm 变体） | 无 bias 的 RMSNorm；应用于注意力和 FFN 子层的输出（而非输入），即 Post-Norm 或 Reordered-Norm | 从标准 Pre-Norm 改为 Post-Norm/Reordered-Norm，提升训练稳定性 |
| Position Encoding | RoPE | 旋转位置编码 | 标准做法 |
| Residual Connection | Post-Norm Residual | 与 Reordered-Norm 配合的残差连接 | 非标准的 Post-Norm 残差 |
| Module Sequence | Reordered-Norm: Attn → Norm → Add → FFN → Norm → Add | 先计算子层输出，再归一化，再残差连接；与标准 Pre-Norm 顺序不同 | Reordered-Norm 序列是对 Pre-Norm/Post-Norm 的折中方案 |

## 关键架构创新

1. **Reordered Norm（重排归一化）**：将 RMSNorm 从子层输入移至子层输出（即 Attn→Norm→Add 而非 Norm→Attn→Add）。这种"后归一化"变体在 OLMo 2 中被证明能显著提升训练稳定性，减少损失尖峰。

2. **QKV Clipping**：受 DBRX 启发，对 Query、Key、Value 向量进行裁剪，防止注意力计算中出现极端值，进一步增强训练稳定性。

3. **两阶段训练**：
   - 预训练阶段：大规模网络数据（7B 用 3.9T tokens，13B 用 5T tokens）
   - 中期训练/退火阶段：使用 Dolmino Mix 1124 数据集，上采样最高质量网络文档、策划的非网络数据源和合成数学推理数据

4. **完全开源**：模型权重、完整训练数据、训练代码和配方、训练日志全部公开，是开源 LLM 的标杆。

5. **无 Bias 设计**：所有层均不使用 bias 参数，减少参数量并简化架构。

## 与前代/同期模型对比

- **vs OLMo 1**：从非参数化 LayerNorm 改为 RMSNorm；从 Pre-Norm 改为 Reordered-Norm；引入 QKV Clipping；MMLU 提升 9 个百分点。
- **vs Llama 3 8B**：OLMo 2 使用 Reordered-Norm vs Llama 3 的标准 Pre-Norm；OLMo 2 完全开源（含数据）vs Llama 3 仅开放权重。
- **vs Mistral 7B**：OLMo 2 无滑动窗口注意力；使用 Reordered-Norm vs Pre-Norm。
- **vs Phi-4**：两者都强调数据质量，但 OLMo 2 的架构创新（Reordered-Norm）更显著。

## 对本综述的启示
- Reordered-Norm 是 Normalization 和 Module Sequence 维度的重要变体，介于 Pre-Norm 和 Post-Norm 之间
- QKV Clipping 是 Token Mixer 维度中训练稳定性的实用技巧
- OLMo 2 的完全开源特性使其成为架构消融实验的理想参考
- 在六维度框架中定位：Attention+QKV-Clip (Token Mixer) + SwiGLU-Dense (Channel Mixer) + RMSNorm-Reordered (Norm) + RoPE (PE) + Post-Norm Residual (Residual) + Reordered-Norm Sequence (Module Seq)
