# 上海AI实验室 - InternLM2.5 架构分析

## 基本信息
- 论文标题：InternLM2.5 Technical Report
- 参数量：1.8B / 7B / 20B（Dense）
- 上下文长度：1M tokens（通过动态 NTK RoPE 扩展）
- 发布时间：2024.12
- arxiv：2412.15177

## 六维度架构选择

| 维度 | 具体选择 | 技术细节 | 创新点 |
|------|----------|----------|--------|
| Token Mixer | GQA | 标准 Grouped-Query Attention | 工业标准 |
| Channel Mixer | Dense FFN (SwiGLU) | 标准三矩阵 SwiGLU FFN | — |
| Normalization | RMSNorm | Pre-Norm | 标准配置 |
| Position Encoding | RoPE + 动态 NTK 扩展 | 训练 32K → 扩展至 1M | 动态 NTK 缩放实践 |
| Residual Connection | 标准残差 | — | — |
| Module Sequence | Pre-Norm | — | — |

## 关键架构创新
1. **完全开源**：数据、代码、checkpoint 全部公开，可复现性标杆
2. **1M 上下文**：通过动态 NTK RoPE 缩放从 32K 训练长度扩展到 1M 推理长度
3. **多尺寸系列**：1.8B/7B/20B 覆盖不同场景
4. **Conditional Online RLHF (COOL RLHF)**：自研的在线 RLHF 训练策略

## 对本综述的启示
- 中国国家级 AI 实验室的代表性开源模型
- 架构上完全采用工业共识，但在 RoPE 扩展和训练方法上有独到贡献
- 与 OLMo 2 (AI2) 类似，定位为"开源可复现的研究基座"
