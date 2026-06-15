# Cohere - Command A 架构分析

## 基本信息
- 论文标题：Cohere Command A: An Enterprise-Ready LLM
- 参数量：111B 总参数 / 23B 激活参数（MoE）
- 上下文长度：256K tokens
- 发布时间：2025.04
- arxiv：2504.00698

## 六维度架构选择

| 维度 | 具体选择 | 技术细节 | 创新点 |
|------|----------|----------|--------|
| Token Mixer | GQA | Grouped-Query Attention | 工业标准 |
| Channel Mixer | MoE | 稀疏 MoE，111B/23B active | 企业级 MoE 部署 |
| Normalization | RMSNorm | Pre-Norm | 标准配置 |
| Position Encoding | RoPE | 标准旋转位置编码 | — |
| Residual Connection | 标准残差 | — | — |
| Module Sequence | Pre-Norm | — | — |

## 关键架构创新
1. **企业级 RAG 优化**：专为检索增强生成场景优化的架构和训练
2. **工具调用能力**：原生支持函数调用和多步工具使用
3. **多语言能力**：23 种语言支持，企业级多语言部署
4. **MoE 高效部署**：111B 总参数但仅 23B 激活，单机可部署

## 对本综述的启示
- 代表了面向企业部署的 MoE 设计路线
- 与 DeepSeek-V3（研究导向）和 Mixtral（开源导向）形成互补
- 256K 上下文 + RAG 优化展示了长上下文在企业场景的实际需求
