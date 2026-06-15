# GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints
**作者**: Joshua Ainslie, James Lee-Thorp, Michiel de Jong, Yury Zemlyanskiy, Federico Lebron, Sumit Sanghai (Google Research) | **年份**: 2023 | **arxiv**: 2305.13245

## 0. 摘要翻译
多查询注意力（MQA）仅使用单个键值头，大幅加速了解码器推理。然而MQA可能导致质量下降，且从头训练一个单独的MQA模型可能不可取。本文提出：(1) 一种将已有多头注意力（MHA）checkpoint通过少量额外预训练（uptrain）转换为MQA模型的方法；(2) 分组查询注意力（GQA），一种介于MHA和MQA之间的折中方案，使用中间数量的键值头。GQA通过uptrain实现了接近MHA的质量和接近MQA的速度。

## 1. 方法动机
a) **为什么提出**: MQA（单KV头）推理快但质量有损；MHA（多KV头）质量好但推理慢。需要一个灵活的中间方案。
b) **现有痛点**: (1) MQA的单KV头在大模型上可能导致明显的质量下降；(2) 从头训练MQA/GQA模型成本高昂；(3) 推理时KV cache的内存带宽是主要瓶颈，需要减少KV头数量。
c) **研究假设**: 将多个KV头分组共享可以在质量和效率之间取得更好的平衡；且可以从已有MHA模型通过少量训练转换。

## 2. 方法设计
a) **Pipeline**: 将MHA中的$h$个KV头分为$g$组，每组内的query头共享同一组KV头。

b) **模块功能**:
- **分组策略**: 将$h$个query头分为$g$组（$g$整除$h$），每组$h/g$个query头共享1个KV头。
  - $g = h$: 等价于MHA（每个query头有自己的KV头）
  - $g = 1$: 等价于MQA（所有query头共享1个KV头）
  - $1 < g < h$: GQA（折中方案）
- **Uptrain转换**: 从已有MHA checkpoint出发：
  - 将每组内的多个KV头通过均值池化合并为1个KV头
  - 用原始预训练数据的一小部分（约5%的原始训练步数）继续训练
  - 这比从头训练一个GQA模型高效得多
- **KV Cache减少**: KV cache大小从$h \times d_k$减少到$g \times d_k$，减少$h/g$倍

c) **公式解释**:
- MHA: $h$个独立的$(Q_i, K_i, V_i)$对，KV cache = $2 \times h \times d_k \times L$
- GQA-$g$: $h$个$Q_i$，$g$个$(K_j, V_j)$，每$h/g$个query共享一组KV
- KV cache = $2 \times g \times d_k \times L$，减少$h/g$倍
- 推理加速主要来自减少KV cache的内存带宽需求

## 3. 与其他方法对比
| 方面 | GQA | MHA | MQA | MLA |
|------|-----|-----|-----|-----|
| KV头数 | $g$（可调） | $h$ | 1 | 1（压缩潜变量）|
| KV cache大小 | $g \times d_k$ | $h \times d_k$ | $d_k$ | $d_c$（压缩维度）|
| 质量 | 接近MHA | 基准 | 略低 | 接近MHA |
| 推理速度 | 快 | 慢 | 最快 | 快 |
| 转换成本 | 5% uptrain | N/A | 5% uptrain | 需从头训练 |

## 4. 实验表现
- **T5-XXL (uptrained)**: GQA-8从T5-XXL MHA checkpoint uptrain后，质量接近MHA（<0.5%差距），推理速度接近MQA
- **质量排序**: MHA ≥ GQA > MQA（差距随模型增大而缩小）
- **速度排序**: MQA > GQA >> MHA
- **推荐配置**: 对于大模型，GQA-8（8个KV头组）是质量和速度的最佳平衡点
- **实际采用**: Llama 2/3、Mistral等主流开源模型均采用GQA

## 5. 总结
a) **一句话概括**: GQA通过将query头分组共享KV头，提供了MHA和MQA之间的灵活折中，配合uptrain方法可以低成本地从已有MHA模型转换，已成为现代LLM的标准注意力配置。
b) **速记pipeline**: Q(h heads) → 分g组 → 每组共享1个KV头 → 组内各Q独立计算Attention → Concat → Output
