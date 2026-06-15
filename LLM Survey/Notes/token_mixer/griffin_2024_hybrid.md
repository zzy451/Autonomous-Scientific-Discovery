# Griffin: Mixing Gated Linear Recurrences with Local Attention
**作者**: Soham De, Samuel L. Smith, Anushan Fernando, Aleksandar Botev, et al. (Google DeepMind) | **年份**: 2024 | **arxiv**: 2402.19427

## 0. 摘要翻译
Griffin 是 Google DeepMind 提出的混合架构模型，将门控线性循环（Gated Linear Recurrence）与局部注意力（Local Attention）相结合。论文同时提出了 Hawk（纯循环模型）和 Griffin（混合模型）。Griffin 的核心组件是 RG-LRU（Real-Gated Linear Recurrent Unit），一种新型的门控线性循环单元。Griffin 在保持 RNN 高效推理优势的同时，通过局部注意力弥补了纯循环模型在精确检索任务上的不足。RecurrentGemma 是基于 Griffin 架构的开源模型。

## 1. 方法动机
- Transformer 的全局注意力具有 O(n^2) 的序列长度复杂度，在长序列推理时效率低下
- 传统 RNN（LSTM、GRU）训练困难且难以扩展到大规模
- 线性循环模型（如 S4、Mamba）展示了 RNN 可以高效训练，但纯循环模型在需要精确 token 检索的任务上仍有不足
- Griffin 的洞察：混合架构可以兼得两者优势——循环层处理长程依赖，局部注意力处理精确检索

## 2. 方法设计（重点：与六维度框架的关联）

### 2.1 RG-LRU（Real-Gated Linear Recurrent Unit）
- **核心创新**: 在实数域上的门控线性循环单元
- **循环公式**:
  - `x_t = a_t ⊙ x_{t-1} + (1 - a_t) ⊙ (b_t ⊙ u_t)`
  - 其中 `a_t = σ(W_a · input_t)` 是循环门控（recurrence gate），控制历史信息的保留比例
  - `b_t` 是输入门控
  - 运算在实数域进行（区别于 S4 的复数域），简化实现
- **与 LRU 的区别**: 加入了输入门控和循环门控，增强了选择性遗忘能力
- **与 Mamba 的区别**: Mamba 使用选择性 SSM（输入依赖的 A 矩阵），RG-LRU 使用门控线性循环（更简洁）
- **训练**: 支持并行扫描（parallel scan）算法，可在 GPU 上高效训练

### 2.2 Griffin 混合架构
- **层交替策略**: 
  - 循环层（RG-LRU）：处理大部分层，负责长程序列建模
  - 局部注意力层：每隔若干循环层插入一个，使用滑动窗口注意力（window size 通常为 1024）
- **每个残差块的结构**:
  1. RMSNorm
  2. 分支 1: 线性投影 → RG-LRU → 线性投影
  3. 分支 2: 线性投影 → GeLU
  4. 两分支逐元素相乘（gated）
  5. 线性投影输出
- **Hawk 变体**: 纯 RG-LRU，不含任何注意力层

### 与六维度框架的关联
- **Token Mixer 维度**: Griffin 是典型的混合 token mixer——RG-LRU（线性循环）+ Local Attention（滑动窗口注意力）
- **与 Mamba/Jamba 的关系**: 
  - Jamba（AI21）也是循环+注意力混合，但使用 Mamba 作为循环组件
  - Griffin 使用 RG-LRU，更简洁且在实数域操作
- **效率特性**: 固定大小的循环状态 → 推理时内存恒定，不随序列长度增长

## 3. 与其他方法对比
| 方法 | 循环组件 | 注意力组件 | 状态大小 | 训练方式 |
|------|---------|-----------|---------|---------|
| Transformer | 无 | 全局注意力 | O(n) KV cache | 并行 |
| Mamba | 选择性 SSM | 无 | 固定 | 并行扫描 |
| Jamba | Mamba | 全局注意力 | 混合 | 并行 |
| RWKV | WKV 机制 | 无 | 固定 | 并行 |
| Griffin | RG-LRU | 局部注意力 | 固定+局部窗口 | 并行扫描 |
| Hawk | RG-LRU | 无 | 固定 | 并行扫描 |

## 4. 实验表现
- Griffin 在语言建模上匹配同规模 Transformer 的性能（1B-7B 参数范围）
- 在长序列外推上显著优于 Transformer（训练 2K，测试 8K+ 仍保持低困惑度）
- 在复制和检索任务上，Griffin（有局部注意力）显著优于 Hawk（纯循环）
- 推理吞吐量比 Transformer 高 2-4 倍（长序列场景）
- RecurrentGemma（2B/9B）在实际部署中验证了 Griffin 架构的可行性

## 5. 总结
a) Griffin 通过将 RG-LRU（实数域门控线性循环）与局部滑动窗口注意力交替堆叠，在保持 RNN 高效推理的同时弥补了纯循环模型在精确检索上的不足，是混合架构的代表性工作。

b) 速记 pipeline: Input → [RG-LRU Block (gated linear recurrence) ↔ Local Attention Block (sliding window)] × N → Output; 固定状态 + 局部窗口
