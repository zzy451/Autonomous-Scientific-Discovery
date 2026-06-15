# RWKV-7 Goose with Expressive Dynamic State Evolution
**作者**: Bo Peng, Ruichong Zhang, Daniel Goldstein, et al. (RWKV Foundation) | **年份**: 2025 | **arxiv**: 2503.14456

## 0. 摘要翻译
本文提出RWKV-7（代号Goose），引入"表达性动态状态演化"机制，使用广义Delta规则（Generalized Delta Rule）来更新状态。与之前版本的简单衰减+累加不同，RWKV-7的状态更新可以执行"先删后写"操作，显著提升了模型的记忆精度和表达能力。RWKV-7在多个基准上超越了之前的线性复杂度模型，在部分任务上接近甚至匹配Transformer。

## 1. 方法动机
a) **为什么提出**: RWKV-6的状态更新仍然是"衰减+累加"模式（$S_t = wS_{t-1} + kv^T$），无法精确修改已存储的特定记忆。
b) **现有痛点**: (1) 累加式更新导致旧记忆与新记忆干扰；(2) 对角衰减只能全局遗忘，无法针对性删除；(3) 在关联记忆任务（如MQAR）上仍落后于Transformer。
c) **研究假设**: 广义Delta规则可以实现"查询旧值→计算差异→定向更新"的精确记忆管理，突破线性注意力/RNN的表达能力瓶颈。

## 2. 方法设计
a) **Pipeline**: 与RWKV-6结构类似，但状态更新规则从简单衰减+累加升级为广义Delta规则。

b) **模块功能**:
- **广义Delta规则状态更新**:
  - RWKV-6: $S_t = \text{diag}(w_t) S_{t-1} + k_t v_t^T$
  - RWKV-7: $S_t = \text{diag}(w_t) S_{t-1} + k_t (a_t \odot v_t + b_t \odot (k_t^T S_{t-1}))^T$
  - 其中$a_t$和$b_t$是输入依赖的门控向量
  - 当$a_t = 1, b_t = -1$时退化为标准Delta规则: $S_t = wS_{t-1} + k_t(v_t - k_t^T S_{t-1})^T$
  - $k_t^T S_{t-1}$: 用当前key查询旧状态中存储的值
  - $v_t - k_t^T S_{t-1}$: 计算新值与旧值的差异
  - 更新只修正差异部分，避免重复写入

- **增强的Token Shift**: 使用更灵活的数据依赖插值
- **改进的归一化**: 使用改进的GroupNorm稳定训练

c) **公式解释**:
- Delta规则的直觉: 类似Hopfield网络的学习规则，但更精确
- $a_t, b_t$提供了灵活性: 模型可以学习何时用Delta规则（精确更新）、何时用简单累加（快速写入）
- 与Gated Delta Networks的关系: 类似的思想，但RWKV-7在RWKV框架内实现，有不同的参数化

## 3. 与其他方法对比
| 方面 | RWKV-7 | RWKV-6 | Gated Delta Net | Mamba-2 |
|------|--------|--------|----------------|---------|
| 状态更新 | 广义Delta规则 | 衰减+累加 | Delta规则 | 选择性衰减+累加 |
| 记忆精度 | 高 | 中 | 高 | 中 |
| 参数化 | $a_t, b_t$门控 | 无 | $\beta_t$学习率 | $\Delta_t$步长 |
| MQAR | 接近Transformer | 落后 | 接近Transformer | 落后 |
| 框架 | RWKV | RWKV | Mamba2 | Mamba |

## 4. 实验表现
- **语言建模**: 在多个规模上超越RWKV-6和Mamba-2
- **关联记忆 (MQAR)**: 显著提升，接近Transformer水平
- **多语言基准**: 在100+语言上表现优异
- **长序列**: 保持线性复杂度和恒定推理内存
- **与Transformer对比**: 在部分任务上匹配同规模Transformer
- **训练效率**: 训练速度与RWKV-6相当

## 5. 总结
a) **一句话概括**: RWKV-7通过广义Delta规则实现"先查后改"的精确状态更新，突破了线性RNN的记忆精度瓶颈，在保持线性复杂度的同时显著缩小与Transformer的性能差距。
b) **速记pipeline**: x → TokenShift(data-dep) → R,K,V,w,a,b → S_t = diag(w)S_{t-1} + k·(a⊙v + b⊙(kᵀS_{t-1}))ᵀ → o = Sᵀr → Output
