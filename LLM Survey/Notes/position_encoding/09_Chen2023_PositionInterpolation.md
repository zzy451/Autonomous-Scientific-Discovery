# Position Interpolation (PI)
**论文**: Extending Context Window of Large Language Models via Positional Interpolation
**作者**: Shouyuan Chen, Sherman Wong, Liangjian Chen, Yuandong Tian
**年份**: 2023
**会议**: arXiv preprint (Meta AI)
**arXiv**: 2306.15595

## 核心思想
通过线性下缩放（interpolation）位置索引，将扩展后的位置范围映射回模型训练时熟悉的范围，从而以极少的 fine-tuning 成本扩展 LLM 的上下文窗口。

## 方法细节

### 外推 (Extrapolation) 的问题
- 直接将 RoPE 的位置索引扩展到训练范围之外
- 产生灾难性的高 attention score
- self-attention 机制崩溃
- 模型性能急剧下降

### 位置插值 (Position Interpolation)
核心修改极其简单：将位置索引线性缩放

$$f'(x, m) = f(x, \frac{mL}{L'})$$

- L: 原始训练长度（如 2048）
- L': 目标长度（如 32768）
- m: 当前位置索引
- 将 [0, L'] 映射到 [0, L]

### 理论分析
- 插值后的位置值都在模型的"已知范围"内
- RoPE 在训练范围内的 attention score 是有界的
- 外推时 attention score 可以任意增长

### Fine-tuning 效率
- 仅需 ~1000 步 fine-tuning
- 使用原始预训练数据的极小子集（~0.1%）
- 即可适应新的上下文长度

## Position Encoding 维度分析

### 分类
- **类型**: RoPE 扩展方法（插值类）
- **注入方式**: 修改 RoPE 的位置索引输入
- **参数量**: 零额外参数（仅改变缩放系数）
- **长度外推**: 通过插值实现"伪外推"

### 关键洞察
1. 插值 vs 外推：前者保持分布内，后者导致 OOD
2. 均匀缩放所有频率维度（这是后续 YaRN 改进的切入点）
3. 极高的效率成本比

### 局限性
1. 均匀缩放损失了高频位置信息的精度
2. 缩放因子过大时仍会退化
3. 需要 fine-tuning（不是完全零成本）

## 实验结果
- LLaMA 7B/13B/33B/65B: 从 2048 扩展到 32768
- Passkey retrieval: 在扩展长度内近乎完美
- 长文档摘要: 保持良好性能
- 短任务: 保持原始性能

## 影响
- 开创了 RoPE 扩展的"插值"范式
- 直接催生了 NTK-aware scaling、YaRN、LongRoPE 等后续工作
- 表明 context length 可以高效扩展
