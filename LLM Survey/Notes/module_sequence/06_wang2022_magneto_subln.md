# Foundation Transformers (MAGNETO / Sub-LayerNorm)
**作者**: Hongyu Wang, Shuming Ma, Shaohan Huang, Li Dong, Wenhui Wang, Zhiliang Peng, Yu Wu, Payal Bajaj, Saksham Singhal, Alon Benhaim, Barun Patra, Zhun Liu, Vishrav Chaudhary, Xia Song, Furu Wei | **年份**: 2022 | **arxiv**: 2210.06423

## 0. 摘要翻译
本文提出 "Foundation Transformer"（MAGNETO），旨在提供一个统一的 Transformer 架构，能够在不同模态（语言、视觉、语音、多模态）上都保持训练稳定性和强劲性能。核心创新是 Sub-LayerNorm (Sub-LN) 归一化方案，配合基于 DeepNet 理论推导的初始化策略，实现了跨模态的"开箱即用"架构。

## 1. 方法动机
- 不同任务使用不同的 Transformer 变体：BERT 用 Post-LN，GPT/ViT 用 Pre-LN
- 缺乏一个统一的"基座"架构，适用于所有模态
- Pre-LN 训练稳定但表达能力有限（表示坍塌），Post-LN 表达能力强但训练不稳定
- 需要兼顾二者优势的新方案

## 2. 方法设计（重点：模块排列顺序及其理论分析）

### Sub-LayerNorm (Sub-LN) 结构
在每个子层内部应用**双重 LayerNorm**：

#### 自注意力子层
```
LN -> Q,K,V 投影 -> Attention -> LN -> 输出投影 -> Add
```

#### FFN 子层
```
LN -> 输入投影 (FC1) -> 激活 -> LN -> 输出投影 (FC2) -> Add
```

### 关键区别
- **Pre-LN**：仅在子层输入端有 LN
- **Post-LN**：仅在残差连接后有 LN
- **Sub-LN**：在子层的输入投影前和输出投影前各有一个 LN
- Sub-LN 增强了子模块的独立性，防止表示坍塌

### 初始化策略（基于 DeepNet 理论）
- 分析 Sub-LN 结构的"期望模型更新量"
- 推导出特定的权重初始化要求，使得模型更新量与网络深度无关
- 避免对 Q、K 投影权重进行缩放（与 vanilla 初始化不同）
- 确保任意深度的模型都能稳定训练

### 完整模块结构
```
Post-LN:  x + LN(Attn(x))
Pre-LN:   x + Attn(LN(x))
Sub-LN:   x + OutProj(LN(Attn(LN(x))))    -- 子层内双 LN
```

## 3. 与其他方法对比
| 方法 | LN 位置 | 训练稳定性 | 表达能力 | 统一性 |
|------|---------|-----------|---------|-------|
| Post-LN | 残差后 | 差 | 强 | BERT 专用 |
| Pre-LN | 子层前 | 好 | 中（表示坍塌） | GPT/ViT |
| Sub-LN (MAGNETO) | 子层内双 LN | 好 | 强 | 全模态通用 |
| Sandwich-LN | 残差分支两端 | 好 | 中 | 大模型训练 |

## 4. 实验表现
- **语言建模（BERT）**：超越 Post-LN 和 Pre-LN 基线
- **语言建模（GPT）**：超越 Pre-LN 基线，支持更大学习率
- **视觉预训练（BEiT）**：超越标准 ViT
- **语音识别**：优于标准 Transformer
- **多模态预训练（BEiT-3）**：提供统一的基座架构
- **深度扩展**：借助 DeepNet 初始化，支持 1000 层 Transformer 的稳定训练
- 实现代码集成在 Microsoft TorchScale 库中

## 5. 总结
a) **一句话概括**：MAGNETO 通过 Sub-LN（子层内双重 LayerNorm）和基于 DeepNet 的初始化策略，提供了跨语言、视觉、语音、多模态的统一 Transformer 基座架构。

b) **速记 pipeline**：`x + OutProj(LN(Attn(LN(x)))) -> x + FC2(LN(Act(FC1(LN(x)))))`
