# Better & Faster Large Language Models via Multi-token Prediction
**作者**: Fabian Gloeckle, Badr Youbi Idrissi, Baptiste Rozière, David Lopez-Paz, Gabriel Synnaeve | **年份**: 2024 | **arxiv**: 2404.19737

## 0. 摘要翻译
本文提出多 token 预测（Multi-Token Prediction, MTP）训练目标：在每个位置同时预测未来 k 个 token，而非仅预测下一个。通过共享 Transformer 主干 + k 个独立的输出头实现。MTP 训练的模型在标准自回归推理中质量更好（尤其在代码任务上），且天然支持 speculative decoding 加速推理（用额外头作为 draft model）。

## 1. 方法动机
a) **为什么**: 标准 next-token prediction 目标可能导致模型过度关注局部统计模式（如高频 n-gram），而忽略更长程的规划和语义结构。
b) **痛点**: (1) 教师强制（teacher forcing）导致训练时缺乏对未来的规划；(2) 推理时自回归逐 token 生成速度慢；(3) 需要一种既能提升质量又能加速推理的训练方法。
c) **假设**: 同时预测多个未来 token 迫使模型学习更好的内部表示（需要编码更多关于未来的信息），同时额外的预测头可以直接用于 speculative decoding。

## 2. 方法设计

### a) Pipeline
```
Input tokens: [x1, x2, x3, ..., xn]
                    ↓
        Shared Transformer Backbone
                    ↓
            Hidden states: [h1, h2, ..., hn]
           ↙     ↓      ↓      ↘
      Head_1   Head_2  Head_3  Head_4
      (next)  (+2nd)  (+3rd)  (+4th)
        ↓       ↓       ↓       ↓
      x_{t+1} x_{t+2} x_{t+3} x_{t+4}
```

### b) 核心模块

**共享主干 + 独立头**:
- 一个共享的 Transformer 编码器处理输入
- k 个独立的输出头（每个是一个小型 Transformer 层 + LM head）
- Head_i 预测位置 t 处的第 i 个未来 token
- 训练损失: `L = Σ_{i=1}^{k} L_CE(Head_i(h_t), x_{t+i})`

**内存高效实现**:
- 朴素实现需要 k 倍内存（k 个 logit 矩阵）
- 解决方案: 顺序计算每个头的损失，不同时存储所有 logit
- 实际内存开销仅增加约 (k-1)/k × 一个头的参数量

**对注意力/表示的影响**:
- MTP 迫使隐状态 h_t 编码更多关于未来的信息
- 这隐式地改善了注意力模式——模型需要关注更广泛的上下文来预测多步未来
- 实验表明 MTP 训练的模型在 probing 任务中表示质量更好

### c) 关键公式
- 标准 NTP 损失: `L_NTP = -Σ_t log P(x_{t+1} | x_{≤t})`
- MTP 损失: `L_MTP = -Σ_t Σ_{i=1}^{k} log P_i(x_{t+i} | x_{≤t})`
- 每个头: `P_i(· | x_{≤t}) = softmax(W_i · TransformerHead_i(h_t))`

## 3. 对比
| 训练目标 | 预测范围 | 推理加速 | 表示质量 |
|----------|----------|----------|----------|
| Next-token | 1 step | 无 | 基线 |
| Multi-token (k=4) | 4 steps | Spec. decoding ~3x | 更好 |
| BERT MLM | 双向 | 不适用于生成 | 好(理解) |

## 4. 实验
- **代码生成**: 在 HumanEval/MBPP 上，MTP (k=4) 比 NTP 提升 12-17%（代码任务受益最大）
- **语言建模**: 在自然语言任务上也有 1-3% 的稳定提升
- **Scaling**: 在 7B 参数规模上，MTP 的优势随模型增大而增加
- **Speculative Decoding**: 用 Head_2/3/4 作为 draft model，推理加速 2-3x，无质量损失
- **最优 k**: k=4 是最佳平衡点，k>4 收益递减
- **工业采用**: Meta Llama 4 和 DeepSeek-V3 均采用了 MTP 训练

## 5. 总结
a) **一句话**: 多 token 预测通过在每个位置同时预测未来 k 个 token，迫使模型学习更好的内部表示，同时额外预测头可直接用于 speculative decoding 加速推理。
b) **速记 pipeline**: `Input → Shared Transformer → k Independent Heads → Predict (x_{t+1}, ..., x_{t+k}) | Inference: Head_1 generates, Head_2-k draft for speculation`
