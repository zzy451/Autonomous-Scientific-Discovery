# RealFormer: Transformer Likes Residual Attention

**论文信息**: He, R., Ravula, A., Kanagal, B., Ainslie, J. (Google Research) (2020)
**arXiv**: 2012.11747 | **会议**: Findings of ACL-IJCNLP 2021
**分类**: Depth (注意力残差)

## 核心思想
RealFormer 在 Transformer 的注意力分数上引入残差连接：将前一层的原始注意力分数（pre-softmax logits）直接传递到当前层，与当前层的注意力分数相加。

## 数学公式
标准 Attention: A_l = softmax(Q_l * K_l^T / sqrt(d))
RealFormer: A_l = softmax(Q_l * K_l^T / sqrt(d) + Prev_l-1)

其中 Prev_l-1 是第 l-1 层的 pre-softmax 注意力 logits（残差传递的是注意力分数，而非隐状态）

## 关键机制
- **注意力分数残差**: 不同于标准的隐状态残差，RealFormer 在注意力权重层面建立了跨层连接
- **零额外参数**: 不引入任何新参数或超参数
- **即插即用**: 仅需极少代码修改即可替代标准 Transformer
- **更稀疏的注意力**: 实验发现使用注意力残差后，模型学到的注意力模式更加稀疏

## 实验结果
- 在 MLM、GLUE、SQuAD、NMT 等任务上均显著优于标准 Transformer/BERT
- 开源代码和预训练检查点

## 与 AttnRes (Kimi 2026) 的对比
| 特性 | RealFormer | AttnRes |
|------|------------|---------|
| 残差内容 | pre-softmax 注意力 logits | 隐状态 (via softmax attention over depth) |
| 连接方式 | 加法 (相邻层) | 深度注意力 (所有前层) |
| 额外参数 | 零 | 极少 |
| 年份 | 2020 | 2026 |

## 与综述的关联
属于 **Depth** 维度。是"注意力残差"方向的先驱工作（2020年），启发了后续 AttnRes 等更复杂的跨层注意力设计。特点是极其简洁（零参数），体现了残差思想的普适性。

## 核心贡献
将残差连接从隐状态扩展到注意力分数层面，零参数改进即可提升 Transformer 性能。
