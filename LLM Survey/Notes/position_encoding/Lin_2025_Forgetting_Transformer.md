# Forgetting Transformer: Softmax Attention with a Forget Gate (FoX)
**作者**: Zhixuan Lin, Xu Owen He, Tien-Dung Le, Jiaxin Shi, Yaniv Shmueli, Yoon Kim, Dale Schuurmans | **年份**: 2025 | **来源**: ICLR 2025 (Spotlight) | **arXiv**: 2503.02130

## 0. 摘要翻译
本文提出 Forgetting Transformer（FoX），通过在标准 softmax 注意力中加入遗忘门（forget gate），使模型能够以数据依赖的方式遗忘历史信息。遗忘门在注意力 logits 上施加累积的对数遗忘因子，实现了可学习的、数据依赖的注意力衰减。FoX 在长上下文语言建模、长度外推和短上下文下游任务上均优于标准 Transformer，且无需显式位置编码。

## 1. 方法动机
a) **为什么提出**: 现代循环序列模型（Mamba-2, HGRN2 等）通过遗忘门有效管理信息流，但标准 Transformer 缺乏这种机制。需要将遗忘门的优势引入 Transformer。
b) **现有痛点**: 
   - 标准 Transformer 对所有历史 token 给予平等的初始注意力机会，缺乏时序衰减
   - ALiBi 的固定线性衰减是数据无关的，无法根据内容调整
   - RoPE 等位置编码不直接控制信息的保留/遗忘
   - Transformer 和循环模型之间存在未桥接的架构鸿沟
c) **研究假设**: 通过在 softmax 注意力中引入数据依赖的遗忘门，可以在保持 Transformer 全局注意力优势的同时，获得循环模型选择性遗忘的能力。

## 2. 方法设计
a) **pipeline**: 
   1. 对每个 token $x_t$，计算遗忘门值 $f_t = \sigma(w_f^T x_t + b_f)$
   2. 计算累积对数遗忘因子 $d_{ij} = \sum_{l=j+1}^{i} \log f_l$
   3. 将遗忘因子加入注意力 logits: $a_{ij} = q_i^T k_j + d_{ij}$
   4. 经 softmax 得到注意力权重

b) **模块功能**: 
   - 遗忘门：为每个 token 计算一个 $\in (0,1)$ 的遗忘因子
   - 累积因子：将 token $j$ 到 token $i$ 之间所有遗忘因子相乘（对数空间求和）
   - 效果：远距离 token 被累积衰减，近距离 token 衰减较少

c) **公式解释**:
   - 遗忘门: $f_t = \sigma(w_f^T x_t + b_f)$，$\sigma$ 为 sigmoid
   - 累积因子: $d_{ij} = \sum_{l=j+1}^{i} \log f_l$
   - 修改后的注意力: $o_i = \frac{\sum_j \exp(q_i^T k_j + d_{ij}) v_j}{\sum_j \exp(q_i^T k_j + d_{ij})}$
   - 与 ALiBi 的关系: 如果 $f_t = f$（常数），则 $d_{ij} = (i-j) \log f$，退化为 ALiBi
   - FoX = 数据依赖的、可学习的 ALiBi 推广

## 3. 与其他方法对比
a) **本质不同**: 
   - 与 ALiBi：ALiBi 用固定线性偏置，FoX 用数据依赖的累积遗忘因子
   - 与 RoPE：RoPE 编码位置到 Q/K 中，FoX 通过遗忘门隐式编码位置
   - 与 CoPE：CoPE 用门控决定"什么算一个位置"，FoX 用门控决定"遗忘多少"
   - 与 Mamba/HGRN：FoX 在注意力（而非循环）框架中引入遗忘门
b) **创新点**: 
   - 首次在 softmax 注意力中成功加入遗忘门
   - 无需显式位置编码即可工作（遗忘门本身提供位置信息）
   - 与 FlashAttention 兼容的高效实现
   - FoX (Pro) 变体进一步整合了循环模型的架构组件
c) **适用场景**: 长上下文语言建模；需要长度外推的场景；作为 RoPE 的替代方案。

## 4. 实验表现
a) **验证方式**: 在语言建模（1B/3B 参数）、Needle-in-a-Haystack、下游任务上评估。
b) **关键数据**: 
   - 1B 模型在 32k 上下文的困惑度优于标准 Transformer + RoPE
   - 长度外推能力显著优于 RoPE（无外推退化）
   - Needle-in-a-Haystack 测试通过（保持全局检索能力）
   - 短上下文下游任务性能与标准 Transformer 可比或略优
   - FoX Pro 在多个基准上进一步提升
c) **局限性**: 
   - 遗忘门引入额外参数（虽然很少）
   - 在超长上下文场景下可能过度遗忘
   - 尚未在 >10B 参数模型上大规模验证
   - 与 RoPE 生态的兼容性需要进一步探索

## 5. 总结
a) **一句话概括**: FoX 通过在 softmax 注意力中加入数据依赖的遗忘门，实现了可学习的注意力衰减，无需显式位置编码即可获得优于标准 Transformer 的长上下文建模能力，是 ALiBi 的数据依赖推广。
b) **速记 pipeline**: Token $x_t$ → Forget Gate $f_t = \sigma(w^T x + b)$ → Cumulative Log $d_{ij} = \sum \log f$ → Attention Logits + $d_{ij}$ → Softmax → Output
