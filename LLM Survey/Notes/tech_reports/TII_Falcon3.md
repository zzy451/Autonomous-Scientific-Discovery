# TII (Technology Innovation Institute) - Falcon 3 架构分析

## 基本信息
- 论文标题：Falcon 3 (TII 官方发布)
- 参数量：1B / 3B / 7B / 10B
- 上下文长度：32K tokens（多模态版本）
- 词表大小：131K tokens（Falcon 2 的两倍）
- 训练数据量：14T tokens
- 发布时间：2024 年 12 月
- 论文链接：无正式 arXiv 论文

## 六维度架构选择

| 维度 | 具体选择 | 技术细节 | 创新点 |
|------|----------|----------|--------|
| Token Mixer | Grouped Query Attention (GQA) + Flash Attention 2 | GQA 降低 KV cache；Flash Attention 2 加速计算 | 标准做法 |
| Channel Mixer | Dense FFN | 标准 FFN 层 | 标准做法 |
| Normalization | 未明确公开（推测 RMSNorm） | — | — |
| Position Encoding | 未明确公开（推测 RoPE） | Llama 兼容架构 | 标准做法 |
| Residual Connection | 未明确公开（推测 Pre-Norm） | — | — |
| Module Sequence | 未明确公开（推测标准 Pre-Norm） | — | — |

## 关键架构创新

1. **Llama 兼容架构**：Falcon 3 采用了 Llama 兼容的架构设计，便于利用 Llama 生态的推理框架和工具链。这反映了架构收敛的趋势——即使不同公司也倾向于采用相同的架构选择。

2. **超大词表**：131K token 词表（是 Falcon 2 的两倍），增强了多语言和特殊字符的编码效率。

3. **极致量化支持**：支持 GGUF、AWQ、GPTQ 等多种量化格式，包括 1.58-bit BitNet 量化，使模型可在消费级硬件（如笔记本）上运行。

4. **大规模训练数据**：14T tokens 的训练数据对于 1B-10B 规模的模型而言非常充分，体现了"小模型 + 大数据"的趋势。

## 与前代/同期模型对比

- **vs Falcon 1/2**：从 ALiBi 位置编码转向 Llama 兼容架构（推测 RoPE），词表从 65K 扩展至 131K。
- **vs Llama 3 8B**：相似架构（Llama 兼容），Falcon 3 侧重小模型（1B-10B）和量化部署。
- **vs Phi-4**：同为中等规模 Dense 模型，但 Falcon 3 更强调边缘部署和量化支持。
- **vs Gemma 3**：两者都有小模型版本（1B-4B），Gemma 3 有更多架构创新（交替注意力、双基频 RoPE）。

## 对本综述的启示
- Falcon 系列从 ALiBi 转向 Llama 兼容架构是"架构收敛"的有力证据——即使曾有不同选择的团队也在向主流标准靠拢
- 极致量化支持（1.58-bit BitNet）展示了架构设计与部署效率的关系
- 架构本身无显著创新，但作为"架构收敛"现象的案例有价值
- 在六维度框架中定位：GQA (Token Mixer) + Dense FFN (Channel Mixer) + RMSNorm (Norm, 推测) + RoPE (PE, 推测) + Pre-Norm Residual (Residual, 推测) + Standard Pre-Norm Sequence (Module Seq, 推测)
