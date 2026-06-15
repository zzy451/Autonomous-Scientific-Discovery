# DeepSeek - DeepSeek-R1 架构分析

## 基本信息
- 论文标题：DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning
- 参数量：671B 总参数（MoE 架构，与 DeepSeek-V3 相同基座）
- 层数：61 层（继承 DeepSeek-V3）
- 隐藏维度：7168（继承 DeepSeek-V3）
- 注意力头数：128（继承 DeepSeek-V3）
- 上下文长度：128K tokens
- 训练数据量：基于 DeepSeek-V3 基座模型进行 RL 训练
- 发布时间：2025 年 1 月
- 论文链接：arXiv:2501.12948
- 蒸馏版本：1.5B/7B/8B/14B/32B/70B（基于 Qwen 和 Llama 架构）

## 六维度架构选择

| 维度 | 具体选择 | 技术细节 | 创新点 |
|------|----------|----------|--------|
| Token Mixer | Multi-head Latent Attention (MLA) | 继承 DeepSeek-V3：128 个注意力头，每头维度 128；KV 压缩维度 512，Query 压缩维度 1536；解耦 RoPE | 架构继承自 V3，无新变化 |
| Channel Mixer | DeepSeekMoE (SwiGLU) | 继承 DeepSeek-V3：256 个路由专家 + 1 个共享专家；Top-8 路由；SwiGLU 激活 | 架构继承自 V3，无新变化 |
| Normalization | RMSNorm (Pre-Norm) | 继承 DeepSeek-V3 | 标准做法 |
| Position Encoding | Decoupled RoPE | 继承 DeepSeek-V3 | 标准做法 |
| Residual Connection | Pre-Norm Residual | 继承 DeepSeek-V3 | 标准做法 |
| Module Sequence | Pre-Norm: Norm → Attn → Add → Norm → MoE → Add | 继承 DeepSeek-V3 | 标准做法 |

## 关键架构创新

注：DeepSeek-R1 的核心创新在 RL 训练方法，而非模型架构。底层架构完全继承 DeepSeek-V3。

1. **纯 RL 推理涌现（R1-Zero）**：直接在基座模型上进行纯 RL 训练（无 SFT），发现复杂推理行为（自我反思、多步验证、"aha moment"）可自然涌现。这是首次大规模验证纯 RL 可激发推理能力。

2. **多阶段训练流程（R1）**：
   - Cold Start：少量长 CoT 数据提供初始格式
   - 大规模 RL：使用 GRPO（Group Relative Policy Optimization）优化推理能力
   - Rejection Sampling + SFT：精炼推理数据质量
   - 最终 RL：全场景人类偏好对齐

3. **GRPO（Group Relative Policy Optimization）**：无需独立价值函数的策略优化方法，通过组内相对奖励估计基线，简化 RL 训练流程。

4. **推理能力蒸馏**：将 R1 的推理能力蒸馏到 1.5B-70B 的小模型中，蒸馏版在推理任务上显著优于同规模直接 RL 训练的模型。

## 与前代/同期模型对比

- **vs DeepSeek-V3**：架构完全相同（671B MoE），区别在于 R1 经过多阶段 RL 训练获得强推理能力。
- **vs OpenAI o1**：R1 在 AIME 2024、MATH-500 等推理基准上达到 o1 级别性能，但采用开源方案。
- **vs Kimi k1.5**：两者都是 RL 驱动的推理模型。R1 使用 GRPO + 多阶段流程；Kimi k1.5 使用 Online Mirror Descent + 长上下文 RL。
- **vs Llama 3 405B**：R1 以 MoE 架构（37B 激活）在推理任务上超越 405B Dense 模型。

## 对本综述的启示
- R1 的底层架构完全继承 V3（MLA+DeepSeekMoE），证明了该架构的通用性和可扩展性
- RL 训练方法（而非架构变化）可显著改变模型能力特征，这对"架构决定性能"的观点提出了补充
- 推理能力蒸馏表明架构选择（Dense vs MoE）对蒸馏效果有影响
- 在六维度框架中：与 DeepSeek-V3 完全相同，该论文更适合作为"训练方法"的参考
