# GPT-J-6B: Parallel Attention + FFN

## 基本信息
- **作者**: Ben Wang, Aran Komatsuzaki (EleutherAI)
- **年份**: 2021
- **来源**: Mesh Transformer JAX (技术文档/GitHub)
- **关键词**: Parallel Layers, GPT-J, 分布式训练效率

## 核心贡献（Module Sequence 维度）
GPT-J-6B 是首个大规模采用 Parallel Attention + FFN 结构的开源模型。

### 1. 并行结构设计
- **标准串行**:
  ```
  Output = Input + Attention(LayerNorm(Input))
  Final = Output + FeedForward(LayerNorm(Output))
  ```
- **GPT-J 并行**:
  ```
  Final = Input + Attention(LayerNorm(Input)) + FeedForward(LayerNorm(Input))
  ```

### 2. 关键优势
- 减少分布式训练中的通信次数
- Attention 和 FFN 的结果可以先本地合并，再做一次 all-reduce
- 训练吞吐量提升约 15%
- 模型收敛不受显著影响

### 3. 设计意义
- 打破了"FFN 必须接收 Attention 输出"的假设
- 两个子层接收相同的输入（经过 LayerNorm 后）
- 实质上假设 Attention 和 FFN 的功能是相对独立的

## 与综述的关联
- 并行 Attention+FFN 的**首创工作**（在大规模模型中）
- 被 PaLM 引用并在更大规模验证
- 代表了 Module Sequence 设计中从"串行"到"并行"的范式转变
- 后续影响了多个模型的架构选择（PaLM, Cerebras-GPT, etc.）
