# MoE Expert Pruning: 专家级稀疏化与压缩

**综述方向**: MoE Expert Pruning / Dropping / Sparsification
**核心论文**:
- Lu et al., 2024, "Not All Experts are Equal: Efficient Expert Pruning and Skipping for MoE LLMs" (arXiv:2402.14800)
- CDSP-MoE, 2024, "Gradient Conflict-Driven Subspace Topology Pruning" (arXiv:2512.20291)
- SEER-MoE, 2024, "Sparse Expert Efficiency through Regularization" (arXiv:2404.05089)
- Finding Fantastic Experts, 2025, "A Unified Study for Expert Dropping Strategies" (arXiv:2504.05586)
**标签**: MoE 压缩, 专家剪枝, 推理加速, 部署优化

---

## 0. 摘要
MoE 模型虽然激活参数少，但总参数量巨大（如 DeepSeek-V3 的 671B），导致显存占用和部署成本极高。Expert Pruning 通过识别并移除不重要的专家来压缩 MoE 模型，在保持性能的同时大幅减少参数量和显存需求。2024-2025 年涌现了多种专家剪枝策略，从 post-training 到 training-aware，从 task-agnostic 到 domain-specific。

## 1. 方法动机
a) MoE 的"双重惩罚"（Double Penalty）：训练时高效（稀疏激活），但推理时所有专家参数都需驻留显存。
b) 实际部署中，许多专家的利用率极低——部分专家可能仅处理 <1% 的 token。
c) 不同下游任务/领域只需要专家的一个子集。
d) 假设：可以安全地移除低利用率或低贡献的专家，以显著降低部署成本。

## 2. 主要方法分类

### 2.1 基于路由统计的剪枝
- 统计每个专家在校准数据上的激活频率（heavy-hitter counting）
- 移除激活频率最低的专家
- 简单有效，但可能遗漏"低频但关键"的专家
- 代表：SEER-MoE 第一阶段

### 2.2 基于重要性评分的剪枝
- 计算每个专家对输出的实际贡献（如路由权重 × 输出范数）
- 考虑专家间的冗余性（相似专家可以合并或移除）
- 代表：Not All Experts are Equal（结合频率和贡献度）

### 2.3 Expert Skipping（动态跳过）
- 不永久移除专家，而是在推理时动态决定是否跳过某些专家
- 基于输入的路由分数：如果所有专家的分数都低于阈值，跳过整个 MoE 层
- 可以与 Early Exit 结合：简单 token 跳过更多专家层

### 2.4 Domain-Specific Pruning
- 针对特定领域（如医疗、法律），仅保留该领域最相关的专家
- EASY-EP（2025）：用少量领域示例识别关键专家
- 可将 256 专家压缩到 32-64 个，性能损失 <2%

### 2.5 结构化剪枝 + 微调恢复
- SEER-MoE 两阶段方案：先剪枝（heavy-hitter 指导），再正则化微调恢复精度
- CDSP-MoE：基于梯度冲突检测专家间的功能重叠，剪枝冗余子空间

## 3. 关键发现（Finding Fantastic Experts, 2025）
- 统一评估了多种剪枝策略，发现：
  - 路由频率是最可靠的单一指标
  - 结合频率 + 输出范数的混合指标略优
  - 剪枝 50% 专家后性能下降通常 <5%
  - 不同层的专家冗余度不同：浅层冗余高，深层冗余低
  - 微调恢复（即使很少的 token）可以显著弥补剪枝损失

## 4. 与其他压缩方法对比
| 方法 | 压缩目标 | 压缩比 | 性能保持 | 需要微调 |
|------|----------|--------|----------|----------|
| 量化（INT4/FP8） | 权重精度 | 2-4x | 高 | 可选 |
| 知识蒸馏 | 模型规模 | 任意 | 中 | 必须 |
| **Expert Pruning** | **专家数量** | **2-8x** | **中-高** | **推荐** |
| Expert Merging | 专家数量 | 2-4x | 中-高 | 推荐 |

## 5. 对 Channel Mixer 的意义
Expert Pruning 是 MoE 从训练到部署的关键桥梁。大规模 MoE（如 256 专家）在训练时提供了丰富的容量，但部署时可以通过剪枝大幅压缩。这形成了一种"训练时过参数化，部署时精简化"的范式。与 Mixture-of-Depths 的 token 级跳过不同，Expert Pruning 是专家级的结构化稀疏，两者可以正交组合。

## 6. 总结
a) 核心思想：移除低利用率/低贡献专家，压缩 MoE 部署成本（20字）
b) 速记 pipeline：
   1. 在校准数据上统计专家激活频率和贡献度
   2. 按重要性排序，移除底部 N% 的专家
   3. 可选：少量数据微调恢复精度
   4. 部署时仅加载保留的专家子集
