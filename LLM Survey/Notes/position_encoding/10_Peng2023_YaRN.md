# YaRN: Yet Another RoPE Extension
**论文**: YaRN: Efficient Context Window Extension of Large Language Models
**作者**: Bowen Peng, Jeffrey Quesnelle, Honglu Fan, Enrico Shippole
**年份**: 2023
**会议**: ICLR 2024
**arXiv**: 2309.00071

## 核心思想
YaRN 改进了 Position Interpolation (PI) 的均匀缩放策略，提出 **NTK-by-parts** 插值法，对 RoPE 的不同频率维度施加不同的缩放策略，在保留局部高频信息的同时外推全局低频关系。

## 方法细节

### PI 的问题
Position Interpolation 对所有 RoPE 维度均匀缩放：
- 高频维度（编码近距离关系）被过度压缩
- 局部位置分辨率下降
- 需要更多 fine-tuning 来恢复

### NTK-aware Scaling（前置工作，来自社区）
- 由 Reddit 用户 bloc97 提出（2023.06）
- 调整 RoPE 的 base frequency（从 10000 增大）
- 基于 Neural Tangent Kernel 理论
- 高频缩放少、低频缩放多
- 但仍是全局统一策略

### YaRN: NTK-by-parts 插值
将 RoPE 的频率维度分为三个区域：

1. **高频区域（维度 i 较大）**: 不做缩放（保留局部精确位置信息）
2. **中频区域**: 线性插值（在不缩放和完全缩放之间过渡）
3. **低频区域（维度 i 较小）**: 完全按 PI 方式缩放（外推全局结构）

分区标准基于波长与目标上下文长度的比值。

### 额外技术
- **Attention Scaling**: 在 softmax 之前对 attention logits 乘以温度系数
  - 补偿因插值导致的 attention 分布"散化"
  - 等效于调整 softmax 温度

### Dynamic-YaRN
- 根据推理时的实际序列长度动态调整缩放因子
- 无需 fine-tuning 即可实现上下文扩展
- 适合不确定输入长度的推理场景

## Position Encoding 维度分析

### 分类
- **类型**: RoPE 扩展方法（改进插值类）
- **注入方式**: 修改 RoPE 频率的缩放策略
- **参数量**: 无额外可训练参数
- **长度外推**: 显著优于 PI，需极少 fine-tuning

### 效率
- 比 SOTA 方法少 10x tokens
- 比 SOTA 方法少 2.5x training steps
- 仅需原始预训练数据的 ~0.1%

### 关键创新
1. 频率分区策略：不同频率不同处理
2. Attention scaling 补偿
3. Dynamic scaling 无需 fine-tuning

## 实验结果
- LLaMA 模型: 从 4k 扩展到 128k+
- 在 passkey retrieval、长文档 QA 上表现优异
- 短上下文任务保持原始性能

## 影响
- 成为 RoPE 长度扩展的主流方法
- 被多个开源模型采用
- NTK-by-parts 的思想被 LongRoPE 等进一步发展
