# Qwen3: 无 Shared Expert + Global-Batch 负载均衡
**来源**: Alibaba Qwen Team | **年份**: 2025 | **arxiv**: 2505.09388

## 0. 背景
Qwen3 是阿里巴巴通义千问团队发布的新一代大语言模型系列，包含 Dense（0.6B-32B）和 MoE（最大 Qwen3-235B-A22B：235B 总参/22B 激活）两大家族。MoE 版本的核心设计决策包括：(1) 完全移除 shared expert（与 DeepSeek-V2/V3 的设计背道而驰），(2) 采用 128 专家选 8 的细粒度路由策略，(3) 全局批次负载均衡（global-batch load balancing）。这些选择共同构成了对"shared expert 是否必要"这一 MoE 设计核心问题的回答。

## 1. 方法动机
- **Shared expert 的利弊权衡**: DeepSeek-V2/V3 引入 shared expert 的初衷是确保所有 token 都能获得基础通用能力。但 shared expert 占用了固定的计算预算（每个 token 都必须经过 shared expert），降低了整体的稀疏化收益，同时可能削弱 routed expert 的专业化动力（因为基础能力已由 shared expert 覆盖）
- **负载均衡的粒度问题**: 传统 MoE 中的辅助损失（auxiliary loss）在 token 级或 sequence 级计算均衡约束，粒度过细会严重干扰路由学习——路由器被迫在"选最佳专家"和"满足均衡约束"之间妥协
- **Qwen3 的核心假设**: 如果路由策略和负载均衡机制足够好，shared expert 是不必要的。每个 routed expert 都应该既有基础能力又有专业化能力，无需额外的"兜底"专家
- **更多专家 = 更细分工**: 128 个专家（相比 Mixtral 的 8 个）提供了足够细的分工粒度，使得即使没有 shared expert，也有足够多的专家组合来覆盖各类输入模式

## 2. 方法设计（详细）

### 2.1 移除 Shared Expert
**与 DeepSeek 的对比**:
- DeepSeek-V2: 2 个 shared expert + 160 个 routed expert，每 token 选 6 个 routed + 全部 2 个 shared
- DeepSeek-V3: 1 个 shared expert + 256 个 routed expert，每 token 选 8 个 routed + 1 个 shared
- **Qwen3**: 0 个 shared expert + 128 个 routed expert，每 token 选 8 个 routed

**移除 shared expert 的理由**:
1. **计算预算全部用于路由选择**: 没有 shared expert 意味着每个 token 激活的 8 个专家都是路由器精心选择的，专业化程度更高
2. **稀疏化收益最大化**: shared expert 的参数对每个 token 都是"固定开销"，移除后推理效率提升
3. **训练策略替代**: 通过改进的全局批次均衡策略，routed expert 自然能学到基础能力，不需要 shared expert 兜底
4. **实验验证**: 论文报告移除 shared expert 后模型性能不降反升，证实了假设

### 2.2 128 专家选 8 的细粒度路由
- **专家数量**: 128 个 routed expert（对比 DeepSeek-V3 的 256、Mixtral 的 8）
- **每 token 激活数**: Top-8 专家
- **路由机制**: 标准 top-k softmax 路由（对 128 个专家的亲和分数取 top-8，softmax 归一化后加权求和）
- **细粒度优势**: 
  - 128 个专家中的每个都更小但更专精
  - 8/128 = 6.25% 的激活比例提供了很高的稀疏度
  - 组合数 C(128,8) 极大，提供了丰富的专家组合空间
- **与 DeepSeek-V3 的对比**: 
  - DeepSeek-V3: 256选8 + 1 shared = 9 个 FFN 的计算量
  - Qwen3: 128选8 + 0 shared = 8 个 FFN 的计算量（更省）

### 2.3 全局批次负载均衡（Global-Batch Load Balancing）
**传统方法的问题**:
- **Token 级辅助损失**: 在每个 token 上施加均衡约束，直接干扰路由器对最佳专家的选择
- **Sequence 级辅助损失**: 在每个序列上计算均衡，粒度仍然太细，统计不稳定
- **DeepSeek-V3 的 aux-loss-free 方法**: 通过 bias 项隐式均衡，不使用显式辅助损失

**Qwen3 的全局批次均衡**:
- **统计粒度**: 在整个训练全局批次（global batch，包含所有数据并行分组的所有 micro-batch）上计算负载均衡损失
- **均衡指标**: 统计全局批次中每个专家被选中的频率，计算与均匀分布的偏差
- **损失函数**: 对偏离均匀分布的情况施加惩罚（例如 KL 散度或 L2 距离）
- **为什么更好**:
  - 全局批次包含大量 token（通常数十万到数百万），统计更稳定
  - 在宏观层面施加均衡约束，不干扰微观层面（单个 token）的路由决策
  - 效果类似"软约束"：只要全局统计均衡，单个 token 可以自由选择最佳专家
- **效果**: 几乎是"免费午餐"——在不损害模型性能的前提下实现专家负载均衡，显著改善专家利用率的均匀性

### 2.4 与六维度框架的关联
- **Channel Mixer 维度**: MoE 是 FFN 层的稀疏化替代，是 channel mixer 的核心创新方向
- **与 DeepSeek MoE 的范式之争**: Qwen3 证明了 shared expert 并非必需，直接挑战 DeepSeek 系列的设计范式。这一"有无 shared expert"的分歧可能是 MoE 设计中最重要的架构选择之一
- **训练工程维度**: 全局批次均衡不仅是算法创新，也涉及分布式训练的通信设计——全局统计需要跨所有数据并行分组聚合

### 2.5 其他关键特性
- **Thinking/Non-thinking 双模式**: 支持在推理任务（使用思维链）和快速响应之间灵活切换
- **激活函数**: SwiGLU（与主流一致）
- **Dense 系列**: 同时提供 0.6B、1.7B、4B、8B、14B、30B、32B 的 Dense 模型

## 3. 与其他方法对比

| 方法 | Shared Expert | 专家数/激活数 | 均衡策略 | 总参/激活参 | 有效 FFN 计算 |
|------|-------------|-------------|---------|-----------|-------------|
| Switch Transformer | 无 | N/1 | Auxiliary loss | - | 1 FFN |
| GShard | 无 | N/2 | Auxiliary loss | - | 2 FFN |
| Mixtral 8x7B | 无 | 8/2 | Auxiliary loss | 47B/13B | 2 FFN |
| DeepSeek-V2 | 2 shared | 160/6 | Token 级 aux loss | 236B/21B | 6+2=8 FFN |
| DeepSeek-V3 | 1 shared | 256/8 | Aux-loss-free (bias) | 671B/37B | 8+1=9 FFN |
| **Qwen3-235B** | **无** | **128/8** | **全局批次均衡** | **235B/22B** | **8 FFN** |

**关键洞察**:
- Qwen3 与 DeepSeek-V3 形成鲜明对比：一个移除 shared expert，一个保留 shared expert
- 两者都取得了顶级性能，说明 shared expert 的有无可能不是决定性因素，路由策略和训练方法可能更重要
- Qwen3 的 128 选 8 无 shared 设计比 DeepSeek-V3 的 256 选 8 + 1 shared 设计更简洁高效

## 4. 实验/工程验证
- **基准性能**: Qwen3-235B-A22B 在 MMLU、HumanEval、GSM8K 等多项标准基准上达到开源模型领先水平
- **与 Dense 模型竞争**: 以 22B 激活参数量与更大的 dense 模型（如 70B+）竞争
- **专家利用率**: 全局批次均衡显著改善了专家利用率的均匀性，几乎所有专家都被均等使用
- **移除 shared expert 的验证**: 性能不降反升，验证了"在足够好的训练策略下 shared expert 非必需"的假设
- **双模式推理**: thinking mode 在数学、编程等推理任务上表现突出；non-thinking mode 在常规对话中提供快速响应
- **规模验证**: Dense 系列（0.6B-32B）+ MoE 系列（30B-A3B、235B-A22B）在多个规模上验证了架构选择的一致性

## 5. 对本综述的启示
- **Shared Expert 的争论**: Qwen3 vs DeepSeek 形成了 MoE 设计中最重要的架构争论之一。综述中应以对比分析的形式呈现双方的论点和实验证据
- **负载均衡的演进路线**: Token级 → Sequence级 → Global-batch级 的均衡粒度演进清晰地展示了 MoE 训练工程的进步
- **简洁性原则**: Qwen3 证明了"更简单的设计 + 更好的训练策略"可能优于"更复杂的架构设计"，这对综述的结论部分有重要参考价值
- **MoE 的设计空间**: shared expert 的有无、专家数量、激活数量、均衡策略构成了 MoE 的多维设计空间，综述应系统梳理这些选择的权衡
- **训练与架构的交互**: 全局批次均衡是一个训练工程创新，但它使得特定的架构选择（移除 shared expert）成为可能，说明架构创新和训练创新不可割裂分析

## 6. 总结
Qwen3 MoE 采用 128 专家选 8 的纯路由设计（无 shared expert），配合全局批次负载均衡策略，证明了在足够好的训练方法下 shared expert 并非必需。全局批次均衡在不干扰单个 token 路由决策的前提下实现了专家负载均衡，几乎是 MoE 训练的"免费午餐"。这一设计直接挑战了 DeepSeek 系列的 shared expert 范式，是 MoE 架构演进中的重要里程碑。

**速记 pipeline**: Input → Router(softmax top-8 of 128 experts, NO shared expert) → 8 Routed Expert FFNs parallel → weighted sum → Output; 训练时 global-batch load balance loss（跨所有数据并行分组聚合统计）
