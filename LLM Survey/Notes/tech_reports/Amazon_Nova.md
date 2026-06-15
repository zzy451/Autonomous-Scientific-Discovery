# Amazon - Nova 架构分析

## 基本信息
- 论文标题：The Amazon Nova Family of Models
- 参数量：多尺寸系列（Micro/Lite/Pro/Premier）
- 发布时间：2025.04
- arxiv：2504.17788

## 六维度架构选择

| 维度 | 具体选择 | 技术细节 | 创新点 |
|------|----------|----------|--------|
| Token Mixer | GQA | 标准 Grouped-Query Attention | 工业标准 |
| Channel Mixer | Dense FFN (SwiGLU) | 标准三矩阵 SwiGLU FFN | — |
| Normalization | RMSNorm | Pre-Norm | 标准配置 |
| Position Encoding | RoPE | 标准旋转位置编码 | — |
| Residual Connection | 标准残差 | — | — |
| Module Sequence | Pre-Norm | — | — |

## 关键架构创新
1. **多模态原生**：Nova 系列从设计之初就是多模态的（文本/图像/视频理解与生成）
2. **多尺寸系列**：Micro（仅文本）→ Lite（多模态轻量）→ Pro（多模态中型）→ Premier（旗舰），覆盖不同部署场景
3. **AWS 集成**：深度集成到 Amazon Bedrock 平台

## 对本综述的启示
- AWS 作为全球最大云计算平台的 AI 战略核心模型
- 架构选择保守但稳健，完全采用工业共识配置
- 创新集中在多模态能力和企业级部署优化，而非底层架构突破
