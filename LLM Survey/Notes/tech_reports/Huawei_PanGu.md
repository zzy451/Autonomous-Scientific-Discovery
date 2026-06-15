# Huawei - PanGu-Sigma 架构分析

## 基本信息
- 论文标题：PanGu-Σ: Towards Trillion Parameter Language Model with Sparse Heterogeneous Computing
- 参数量：1.085T（万亿参数）
- 层数：混合结构：下层 M 层为 Dense，上层 N 层为 Sparse（具体数值未完全公开）
- 隐藏维度：未明确公开
- 上下文长度：未明确公开
- 训练数据量：329B tokens（40+ 自然语言和编程语言）
- 训练硬件：512 个 Ascend 910 AI 加速器，约 100 天
- 训练框架：MindSpore
- 发布时间：2023 年 3 月
- 论文链接：arXiv:2303.10845

## 六维度架构选择

| 维度 | 具体选择 | 技术细节 | 创新点 |
|------|----------|----------|--------|
| Token Mixer | 标准自注意力（继承 PanGu-α） | 继承 PanGu-α 的 Decoder-only Transformer 注意力机制 | 无显著创新 |
| Channel Mixer | Random Routed Experts (RRE) | 上层使用 RRE 替代标准 FFN；两级路由：Level 1 按领域映射到候选专家组，Level 2 在组内随机选择 1 个专家；路由映射随机初始化且每层独立 | RRE 是独特的路由机制：基于哈希的随机路由替代可学习路由，确保负载均衡 |
| Normalization | 未明确公开（推测 LayerNorm，继承 PanGu-α） | — | — |
| Position Encoding | 未明确公开（推测学习式位置编码，继承 PanGu-α） | — | — |
| Residual Connection | 标准残差连接 | — | — |
| Module Sequence | Dense 下层 + Sparse 上层 | 下层 M 层为标准 Dense Transformer（跨领域共享）；上层 N 层使用 RRE 的 Sparse Transformer | 异构层结构：Dense 底层 + Sparse 顶层 |

## 关键架构创新

1. **Random Routed Experts (RRE)**：核心创新。受 Hash Layers 启发，使用随机（非可学习）路由将 token 分配给专家。两级路由机制：
   - Level 1：根据 token 所属领域映射到候选专家组
   - Level 2：在候选组内通过随机映射选择具体专家
   - 路由映射随机初始化，每层独立，确保计算均衡

2. **Expert Computation and Storage Separation (ECSS)**：将专家的计算和存储分离，实现 6.3 倍训练吞吐量提升。解决了传统 MoE 中通信开销大的问题。

3. **异构 Dense-Sparse 层结构**：下层为 Dense（共享通用知识），上层为 Sparse（领域专精）。这种设计基于"底层特征通用、高层特征专精"的直觉。

4. **参数继承**：从预训练的 PanGu-α Dense 模型继承参数，再扩展为 Sparse 模型，减少从头训练的成本。

5. **Ascend 原生训练**：在华为 Ascend 910 + MindSpore 框架上训练，是非 NVIDIA 硬件上训练万亿参数模型的早期实践。

## 与前代/同期模型对比

- **vs PanGu-α**：从 Dense 扩展为 Sparse（RRE），参数从 200B 级别增至 1.085T；继承底层参数。
- **vs Switch Transformer**：Switch 使用可学习路由 + Top-1，PanGu-Σ 使用随机路由（RRE）；Switch 全层 MoE vs PanGu-Σ 仅上层 MoE。
- **vs Mixtral 8x7B**：Mixtral 使用可学习 Top-2 路由，PanGu-Σ 使用随机路由；Mixtral 全层 MoE vs PanGu-Σ 异构结构。
- **vs DeepSeek-V2/V3**：DeepSeek 使用可学习路由 + 超细粒度专家，PanGu-Σ 使用随机路由 + 领域导向专家分组。

## 对本综述的启示
- RRE 是 Channel Mixer 维度中独特的路由策略，与可学习路由形成对比
- Dense 底层 + Sparse 顶层的异构设计是 Module Sequence 维度的重要变体
- ECSS 展示了系统优化对 MoE 训练效率的关键作用
- 训练数据量相对较小（329B tokens），反映了早期万亿参数模型的数据限制
- 在六维度框架中定位：Standard Attention (Token Mixer) + RRE-MoE (Channel Mixer) + LayerNorm (Norm, 推测) + Learned PE (PE, 推测) + Standard Residual (Residual) + Heterogeneous Dense-Sparse Sequence (Module Seq)
