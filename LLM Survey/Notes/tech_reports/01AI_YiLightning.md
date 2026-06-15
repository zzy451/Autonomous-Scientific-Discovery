# 01.AI - Yi-Lightning 架构分析

## 基本信息
- 论文标题：Yi-Lightning Technical Report
- 参数量：未公开具体数值（MoE 架构）
- 层数：未公开
- 隐藏维度：未公开
- 上下文长度：64K tokens（训练时扩展）
- 训练数据量：未公开
- 发布时间：2024 年 12 月
- 论文链接：arXiv:2412.01253

## 六维度架构选择

| 维度 | 具体选择 | 技术细节 | 创新点 |
|------|----------|----------|--------|
| Token Mixer | 混合注意力（Full Attention + Sliding Window） | 混合注意力块设计：部分层使用全局注意力，部分层使用局部滑动窗口注意力；跨层 KV cache 共享 | 混合注意力模式 + 跨层 KV 共享，兼顾全局建模与推理效率 |
| Channel Mixer | 细粒度 MoE | FFN 专家被分割为更小的功能单元（细粒度专家分割）；具体专家数量未公开；分组负载均衡路由 | 细粒度专家分割提升参数利用率和训练吞吐量 |
| Normalization | 未明确公开（推测 RMSNorm） | 遵循现代 Transformer 标准实践 | — |
| Position Encoding | 未明确公开（推测 RoPE） | 支持 64K 上下文 | — |
| Residual Connection | Pre-Norm Residual（推测） | 标准做法 | — |
| Module Sequence | Pre-Norm（推测） | 标准 Pre-Norm 序列 | — |

## 关键架构创新

1. **细粒度专家分割**：将 FFN 专家进一步分割为更小的专精功能单元，提升参数利用效率和训练吞吐量，类似 DeepSeek 系列的超细粒度 MoE 思路。

2. **混合注意力 + 跨层 KV 共享**：结合全局注意力层和滑动窗口注意力层，并在层间共享 KV cache，大幅降低推理时内存占用。

3. **分组负载均衡路由**：采用分组导向的负载均衡机制，配合辅助损失函数确保专家利用率均匀。

4. **FP8 量化优化**：架构设计专门针对 FP8 量化和 NVIDIA Hopper 架构硬件优化，最大化训练和推理效率。

5. **RAISE 安全框架**：集成四组件安全引擎，贯穿预训练、后训练和服务阶段。

## 与前代/同期模型对比

- **vs Yi-34B/Yi-1.5**：从 Dense 架构演进为 MoE，引入细粒度专家分割和混合注意力设计。
- **vs DeepSeek-V2/V3**：共享细粒度 MoE 的设计理念；Yi-Lightning 的混合注意力（Full+SWA）vs DeepSeek 的 MLA，两种不同的 KV cache 优化路线。
- **vs Hunyuan-Large**：两者都采用跨层 KV cache 共享，但 Yi-Lightning 还结合了滑动窗口注意力。
- **vs Mixtral 8x7B**：Yi-Lightning 的细粒度专家分割 vs Mixtral 的 8 个大专家，代表 MoE 设计的不同粒度选择。

## 对本综述的启示
- 该报告侧重训练方法论和系统优化，具体架构超参数未公开，限制了精确的架构对比
- 混合注意力（Full+SWA）+ 跨层 KV 共享是 Token Mixer 维度的重要组合策略
- FP8 量化友好的架构设计反映了硬件-软件协同设计的趋势
- 在六维度框架中定位：Hybrid Attention (Token Mixer) + Fine-grained MoE (Channel Mixer) + RMSNorm (Norm, 推测) + RoPE (PE, 推测) + Pre-Norm Residual (Residual) + Pre-Norm Sequence (Module Seq)
