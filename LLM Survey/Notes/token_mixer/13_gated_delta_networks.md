# Gated Delta Networks: Improving Mamba2 with Delta Rule
**作者**: Songlin Yang, Jan Kautz, Ali Hatamizadeh (NVIDIA) | **年份**: 2024 | **arxiv**: 2412.06464

## 0. 摘要翻译
本文提出Gated Delta Networks，将delta rule（一种经典的在线学习规则）引入线性注意力/状态空间模型框架。Delta rule通过减去旧的键值关联再加入新的关联来更新记忆状态，实现了比简单累加更精确的记忆管理。结合门控机制，Gated Delta Networks在语言建模和下游任务上显著超越Mamba2和其他线性循环模型，接近甚至匹配Transformer的性能。

## 1. 方法动机
a) **为什么提出**: 线性注意力和SSM模型的状态更新本质是累加式的（$S_t = S_{t-1} + k_t v_t^T$），无法精确修改或删除已存储的信息，导致记忆容量受限。
b) **现有痛点**: (1) 线性注意力的累加更新会导致记忆干扰——新信息与旧信息混合；(2) Mamba的选择性遗忘是全局的（通过$\Delta$缩放整个状态），无法针对性地修改特定记忆；(3) 在需要精确关联记忆的任务（如MQAR）上，线性模型远落后于Transformer。
c) **研究假设**: Delta rule（$S_t = S_{t-1} - \beta_t k_t (k_t^T S_{t-1}) + \beta_t k_t v_t^T$）可以实现"先删后写"的精确记忆更新，显著提升线性模型的记忆能力。

## 2. 方法设计
a) **Pipeline**: 在Mamba2的框架上，将状态更新规则从简单累加改为delta rule，并增加门控机制。

b) **模块功能**:
- **Delta Rule状态更新**:
  - 标准线性注意力: $S_t = S_{t-1} + k_t v_t^T$（只能写入）
  - Delta rule: $S_t = S_{t-1} + \beta_t k_t (v_t - k_t^T S_{t-1})^T$
  - 展开: $S_t = (I - \beta_t k_t k_t^T) S_{t-1} + \beta_t k_t v_t^T$
  - 含义: 先用$k_t$查询旧状态得到$k_t^T S_{t-1}$，计算与新值$v_t$的差异，然后更新
- **门控机制 (Gating)**:
  - 输出门控: $o_t = \alpha_t \odot (q_t^T S_t)$，$\alpha_t$是输入依赖的门控
  - 短路连接: 类似GRU的设计，允许信息绕过状态直接传递
- **与Mamba2的结合**:
  - 使用Mamba2的矩阵值状态（multi-head结构）
  - 保留Mamba2的硬件高效scan算法
  - $\beta_t$（学习率）是输入依赖的，通过sigmoid激活

c) **公式解释**:
- Delta rule的直觉: 如果$k_t$对应的旧值$k_t^T S_{t-1}$已经等于$v_t$，则不更新；否则修正差异
- $\beta_t$控制更新强度: $\beta_t \to 0$保持旧记忆，$\beta_t \to 1$完全覆盖
- 复杂度: 与Mamba2相同，$O(LdN)$，但常数因子略大

## 3. 与其他方法对比
| 方面 | Gated Delta Net | Mamba2 | Linear Attention | Transformer |
|------|----------------|--------|-----------------|-------------|
| 状态更新 | Delta rule（先删后写）| 选择性衰减+累加 | 纯累加 | 无状态（KV cache）|
| 记忆精度 | 高 | 中 | 低 | 精确（存储所有KV）|
| MQAR性能 | 接近Transformer | 明显落后 | 很差 | 基准 |
| 复杂度 | $O(LdN)$ | $O(LdN)$ | $O(Ld^2)$ | $O(L^2d)$ |
| 门控 | 输入依赖 | 通过$\Delta$ | 无 | 无 |

## 4. 实验表现
- **MQAR (Multi-Query Associative Recall)**: 显著超越Mamba2和所有线性模型，接近Transformer
- **语言建模**: 在相同参数量和训练数据下，PPL优于Mamba2约0.3-0.5点
- **下游任务**: 在多个zero-shot基准上超越Mamba2，接近Transformer
- **长序列**: 保持线性复杂度的优势
- **规模实验**: 从370M到7B参数均有验证，优势一致

## 5. 总结
a) **一句话概括**: Gated Delta Networks将delta rule引入线性注意力框架，通过"先查旧值、再算差异、最后更新"的精确记忆管理机制，显著提升线性模型的关联记忆能力，缩小与Transformer的差距。
b) **速记pipeline**: x → Q,K,V,β,α → S_t = (I-βkk^T)S_{t-1} + βkv^T → o = α⊙(q^TS_t) → Output
