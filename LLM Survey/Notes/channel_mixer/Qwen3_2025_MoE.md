# Qwen3: 无 Shared Expert 的 MoE 与全局批次均衡
**作者**: Alibaba Qwen Team | **年份**: 2025 | **arxiv**: 2505.09388

## 0. 摘要翻译
Qwen3 是阿里巴巴通义千问团队发布的新一代大语言模型系列，包含 Dense（0.6B-32B）和 MoE（最大 235B 总参/22B 激活）两大家族。MoE 版本的核心创新包括：移除 shared expert（与 DeepSeek-V2/V3 的设计相反）、采用 128 专家选 8 的细粒度路由策略、以及全局批次负载均衡（global-batch load balancing）损失函数，在保持训练稳定性的同时显著提升了专家利用率和模型性能。

## 1. 方法动机
- DeepSeek-V2/V3 引入 shared expert 的初衷是确保所有 token 都能获得基础能力，但 shared expert 占用了固定的计算预算，降低了专家的专业化程度
- 传统的 token 级或 sequence 级负载均衡损失（auxiliary loss）会干扰路由学习，导致专家坍缩或利用率不均
- Qwen3 的洞察：如果路由和均衡策略足够好，shared expert 是不必要的——每个专家都应该既有基础能力又有专业化能力
- 全局批次均衡在更大的统计粒度上施加均衡约束，减少对单个 token 路由决策的干扰

## 2. 方法设计（重点：与六维度框架的关联）

### 2.1 移除 Shared Expert
- **与 DeepSeek 的对比**: DeepSeek-V2/V3 使用 1-2 个 shared expert + N 个 routed expert 的架构，shared expert 处理所有 token
- **Qwen3 的选择**: 完全移除 shared expert，所有 128 个专家均为 routed expert
- **理由**: 
  - shared expert 的计算预算固定，限制了模型的稀疏化收益
  - 通过更好的训练策略（全局批次均衡），routed expert 自然能学到基础能力
  - 移除 shared expert 后，每个 token 激活的 8 个专家都是通过路由选择的，专业化程度更高

### 2.2 128 专家选 8 的细粒度路由
- **专家数量**: 128 个 routed expert（对比 DeepSeek-V3 的 256 专家选 8）
- **激活数量**: 每个 token 选择 top-8 专家
- **路由机制**: 标准 top-k softmax 路由
- **细粒度优势**: 更多专家意味着更细的专业化分工，每个专家更小但更专精

### 2.3 全局批次负载均衡（Global-Batch Load Balancing）
- **传统方法的问题**: 
  - Token 级 auxiliary loss: 在每个 token 上施加均衡约束，严重干扰路由学习
  - Sequence 级 auxiliary loss: 在每个序列上均衡，粒度仍然太细
- **全局批次均衡**:
  - 在整个训练批次（global batch）的粒度上计算负载均衡损失
  - 统计全局批次中每个专家被选中的频率，对偏离均匀分布的情况施加惩罚
  - 由于全局批次包含大量 token，统计更稳定，对单个 token 的路由决策干扰更小
- **效果**: 几乎是"免费午餐"——在不损害模型性能的前提下实现专家负载均衡

### 与六维度框架的关联
- **Channel Mixer 维度**: MoE 是 FFN 层的稀疏化替代，属于 channel mixer 的核心创新
- **与 DeepSeek MoE 的对比**: Qwen3 证明了 shared expert 并非必需，挑战了 DeepSeek 系列的设计范式
- **训练稳定性**: 全局批次均衡是 MoE 训练工程的重要进展，解决了长期困扰 MoE 的负载不均问题

### 关键超参数（Qwen3-235B-A22B）
- 总参数: 235B，激活参数: 22B
- 专家数: 128，每 token 激活: 8
- 无 shared expert
- 支持 thinking/non-thinking 双模式推理

## 3. 与其他方法对比
| 方法 | Shared Expert | 专家数/激活数 | 均衡策略 | 总参/激活参 |
|------|-------------|-------------|---------|-----------|
| Switch Transformer | 无 | N/1 | Auxiliary loss | - |
| GShard | 无 | N/2 | Auxiliary loss | - |
| DeepSeek-V2 | 2 shared | 160/6 | Token 级 | 236B/21B |
| DeepSeek-V3 | 1 shared | 256/8 | 无 aux loss (bias) | 671B/37B |
| Qwen3-235B | 无 | 128/8 | 全局批次均衡 | 235B/22B |

## 4. 实验表现
- Qwen3-235B-A22B 在多项基准上达到开源模型领先水平
- 在 MMLU、HumanEval、GSM8K 等标准基准上与更大的 dense 模型竞争
- 全局批次均衡显著改善了专家利用率的均匀性
- thinking/non-thinking 双模式使模型在推理任务和快速响应之间灵活切换
- 移除 shared expert 后模型性能不降反升，验证了设计假设

## 5. 总结
a) Qwen3 MoE 移除 shared expert、采用 128 专家选 8 的细粒度路由和全局批次负载均衡，证明了在足够好的训练策略下 shared expert 并非必需，全局批次均衡几乎是提升 MoE 训练的"免费午餐"。

b) 速记 pipeline: Input → Router(softmax top-8 of 128 experts, no shared) → 8 Expert FFNs parallel → weighted sum → Output; 训练时 global-batch load balance loss
