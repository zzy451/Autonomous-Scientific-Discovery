# PaLM: Scaling Language Modeling with Pathways
**作者**: Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung, Charles Sutton, Sebastian Gehrmann, et al. | **年份**: 2022 | **arxiv**: 2204.02311

## 0. 摘要翻译
PaLM 是 Google 推出的 5400 亿参数语言模型，使用 Pathways 系统在 6144 个 TPU v4 芯片上训练。在架构设计上，PaLM 采用了多项关键修改，其中最突出的是**并行层（Parallel Layers）**设计——将注意力和 FFN 并行执行而非串行。此外还使用了 SwiGLU 激活、RoPE 位置编码、Multi-Query Attention 等技术，在多项基准上达到当时最优水平。

## 1. 方法动机
- 标准 Transformer 串行执行 Attention 和 FFN，存在不必要的计算依赖
- 大规模训练中，硬件利用率和吞吐量至关重要
- 需要在保持模型质量的前提下提升训练速度
- 同时引入最新的组件设计（SwiGLU、RoPE 等）提升模型质量

## 2. 方法设计（重点：模块排列顺序及其理论分析）

### 并行层（Parallel Formulation）
```
标准串行:  x' = x + Attn(LN(x))
           y  = x' + FFN(LN(x'))      -- FFN 的输入依赖 Attn 的输出

并行:      y  = x + Attn(LN(x)) + FFN(LN(x))   -- Attn 和 FFN 共享同一输入
```

#### 关键优势
- **计算效率**：Attn 和 FFN 的输入投影矩阵可以融合为一次矩阵乘法
- 输出投影也可以融合
- 训练速度提升约 **15%**
- **信息**：PaLM 的实验表明，在大规模（8B+ 参数）下，并行层不损失模型质量

#### 理论分析
- 在大规模模型中，Attn 和 FFN 的更新量相对于残差连接较小
- 因此串行 vs 并行的差异被残差主路径主导
- GPT-J (6B) 首先采用此设计，PaLM 在 540B 规模上验证

### 其他关键组件
- **SwiGLU 激活**：`Swish(xW) * (xV)`，比 ReLU/GeLU 效果更好
- **RoPE 位置编码**：旋转位置编码，更好地捕获相对位置信息
- **Multi-Query Attention**：K、V 投影跨头共享，加速自回归解码
- **无偏置**：所有 Dense 层和 LayerNorm 不使用偏置项，提升训练稳定性
- **共享 Embedding**：输入和输出 Embedding 矩阵共享

### 完整的 PaLM 块结构
```
y = x + Attn(LN(x)) + FFN(LN(x))
其中 Attn 使用 Multi-Query + RoPE
     FFN 使用 SwiGLU 激活
     LN 无偏置
```

## 3. 与其他方法对比
| 方法 | Attn/FFN 关系 | 训练速度 | 质量影响 |
|------|-------------|---------|---------|
| 标准 Transformer | 串行 | 基线 | - |
| GPT-J (6B) | 并行 | +15% | 基本无损 (6B) |
| PaLM (540B) | 并行 | +15% | 基本无损 (大规模) |
| Macaron Net | FFN-Attn-FFN | 无加速 | 略有提升 |

- 并行设计在小规模（<8B）可能有轻微质量损失
- 在大规模（>8B）下质量差异消失，但速度优势持续

## 4. 实验表现
- **训练效率**：并行层带来约 15% 的训练速度提升
- **语言建模**：540B 模型在多项基准上达到 SOTA
- **推理任务**：在 BIG-bench 等复杂推理基准上表现突出
- **few-shot 学习**：多项任务上超越 GPT-3
- 验证了并行层设计在超大规模下的可行性

## 5. 总结
a) **一句话概括**：PaLM 采用并行 Attention+FFN 设计（共享输入，输出相加），在 540B 规模上验证了该设计不损失质量但提升 15% 训练速度的可行性。

b) **速记 pipeline**：`y = x + Attn(LN(x)) + SwiGLU_FFN(LN(x))` （并行，非串行）
