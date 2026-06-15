# Hierarchically Gated Recurrent Neural Network for Sequence Modeling (HGRN)
**作者**: Zhen Qin, Songlin Yang, Yiran Zhong | **年份**: 2023 | **arxiv**: 2311.04823

## 0. 摘要翻译
本文提出 HGRN（Hierarchically Gated Recurrent Neural Network），一种门控线性 RNN 模型。核心思想是为遗忘门设置可学习的下界，并在不同层强制下界单调递增——底层遗忘门下界低（更多遗忘，捕捉短程依赖），高层下界高（更少遗忘，捕捉长程依赖）。这种层次化的门控设计使模型在语言建模上与 Transformer 竞争力相当，同时保持线性推理复杂度。

## 1. 方法动机
a) **为什么**: 线性 RNN（如 S4、LRU）虽然推理高效，但缺乏数据依赖的门控，表达能力有限。传统 LSTM 的门控有效但训练不可并行。
b) **痛点**: (1) 线性 RNN 的固定衰减率无法适应不同时间尺度的依赖；(2) 浅层和深层应该关注不同尺度的依赖，但现有模型未显式建模这种层次结构；(3) 需要一种既有门控灵活性又可并行训练的 RNN。
c) **假设**: 通过层次化的遗忘门下界（底层短记忆、高层长记忆），可以让不同层自然分工，捕捉不同时间尺度的依赖。

## 2. 方法设计

### a) Pipeline
```
Input x_t
  → Linear projection → (gate input, value)
  → Forget gate: f_t = σ(w_f · x_t + b_f), 下界为 λ_l (层相关)
  → 实际遗忘率: f̃_t = λ_l + (1 - λ_l) · f_t
  → 状态更新: h_t = f̃_t · h_{t-1} + (1 - f̃_t) · v_t
  → Output gate → output
```

### b) 核心模块

**层次化遗忘门 (Hierarchical Forget Gate)**:
- 每层 l 有一个可学习的下界 λ_l
- 约束: 0 ≤ λ_1 ≤ λ_2 ≤ ... ≤ λ_L ≤ 1（单调递增）
- 底层 λ 小 → 遗忘门可以很低 → 短程记忆
- 高层 λ 大 → 遗忘门至少为 λ → 长程记忆
- 实现: `f̃_t = λ_l + (1 - λ_l) · σ(w_f · x_t + b_f)`

**门控线性循环**:
- 状态更新: `h_t = f̃_t ⊙ h_{t-1} + i_t ⊙ v_t`
- 其中 `i_t = 1 - f̃_t`（输入门与遗忘门互补）
- 这是对角线性 RNN + 数据依赖门控
- 可通过 parallel scan 并行训练

### c) 关键公式
- 遗忘门: `f̃_t^{(l)} = λ_l + (1 - λ_l) · σ(W_f^{(l)} x_t + b_f^{(l)})`
- 状态更新: `h_t = f̃_t ⊙ h_{t-1} + (1 - f̃_t) ⊙ v_t`
- 层次约束: `λ_l = σ(α_l)`, 其中 α_1 ≤ α_2 ≤ ... ≤ α_L`
- 隐状态维度: O(d) per layer

## 3. 对比
| 模型 | 门控 | 层次化 | 状态大小 | 并行训练 |
|------|------|--------|----------|----------|
| LSTM | sigmoid 门 | 否 | O(d) | 否 |
| S4/LRU | 固定/可学习衰减 | 否 | O(d) | 是 |
| Mamba | 选择性(数据依赖) | 否 | O(d·N) | 是(scan) |
| HGRN | 下界约束门控 | 是(单调递增) | O(d) | 是(scan) |
| HGRN2 | 下界约束+外积 | 是 | O(d²) | 是(chunk) |

## 4. 实验
- **语言建模**: 在 WikiText-103 和 The Pile 上，HGRN 匹配同规模 Transformer
- **Long Range Arena**: 平均准确率优于 S4 和 Transformer
- **训练速度**: 与 Transformer 相当（parallel scan 实现）
- **推理速度**: O(1) per step，显著快于 Transformer
- **后续**: HGRN2 通过引入矩阵值状态（外积更新）将状态容量从 O(d) 提升到 O(d²)

## 5. 总结
a) **一句话**: HGRN 通过层次化的遗忘门下界约束（底层短记忆、高层长记忆），让门控线性 RNN 自然分工捕捉多尺度依赖，是 HGRN2 和后续门控线性 RNN 工作的基础。
b) **速记 pipeline**: `Input → [ForgetGate(lower_bound=λ_l↑) → h_t = f̃·h_{t-1} + (1-f̃)·v_t] × L layers (λ monotonically increasing) → Output`
