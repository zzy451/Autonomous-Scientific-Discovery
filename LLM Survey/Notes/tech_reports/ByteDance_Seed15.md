# ByteDance - Seed1.5-LLM 架构分析

## 基本信息
- 论文标题：Seed1.5-LLM Technical Report
- 参数量：未完全公开（推测 MoE 架构，数百B总参数）
- 发布时间：2025
- arxiv：2025 年发布（具体 ID 待确认）

## 六维度架构选择

| 维度 | 具体选择 | 技术细节 | 创新点 |
|------|----------|----------|--------|
| Token Mixer | GQA | 标准 Grouped-Query Attention | 工业标准配置 |
| Channel Mixer | MoE | 细粒度专家设计 | 字节跳动自研 MoE 路由策略 |
| Normalization | RMSNorm | Pre-Norm | 标准配置 |
| Position Encoding | RoPE | 标准旋转位置编码 | — |
| Residual Connection | 标准残差 | — | — |
| Module Sequence | Pre-Norm | — | — |

## 关键架构创新
1. **Thinking Mode (思考模式)**：支持 Long-CoT 推理，类似 DeepSeek-R1 的推理能力
2. **多阶段训练范式**：大规模预训练 → SFT → RLHF → 推理增强
3. **豆包生态集成**：作为字节跳动豆包（Doubao）产品的底层模型

## 对本综述的启示
- 字节跳动作为中国最大的互联网/AI 公司之一，其技术路线选择具有重要参考价值
- 架构上采用工业共识（GQA + RMSNorm + RoPE + SwiGLU），创新集中在训练策略和推理能力
- 与 DeepSeek-R1 形成对比：同样强调推理能力，但底层架构细节公开程度不同
