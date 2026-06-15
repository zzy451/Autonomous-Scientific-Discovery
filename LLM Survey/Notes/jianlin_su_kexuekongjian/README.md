# 苏剑林"科学空间"博客 — Transformer 架构相关文章总结

## 作者简介

苏剑林（Jianlin Su），追一科技（ZhuiyiTechnology）研究员，RoPE（Rotary Position Embedding）的发明者。其个人博客"科学空间"（kexue.fm）是中文 NLP/深度学习社区最具影响力的技术博客之一。代表性学术贡献包括：

- **RoPE / RoFormer**：论文 "RoFormer: Enhanced Transformer with Rotary Position Embedding"（Su, Lu, Pan, Wen, Liu），已被 LLaMA、GPT-NeoX、PaLM 等主流大模型广泛采用
- **GAU-alpha**：基于 Gated Attention Unit 的预训练模型实验
- **ReRoPE**：无限长度外推的位置编码方案
- **NTK-RoPE**：将 RoPE 解释为 β 进制编码，启发了社区的 NTK-aware Scaled RoPE 方法
- **HWFA**：Hybrid Window-Full Attention，事前修改类长度外推方案
- **RoPE-Tie**：多模态位置编码的统一方案

英文翻译站点：https://www.tylerromero.com/translations/scientific-spaces/ （部分文章有英文翻译）

---

## "Transformer升级之路"系列文章索引

以下为通过搜索确认的系列文章。该系列从 2021 年开始，截至 2024 年底至少有 17+ 篇。

| # | 标题 | 链接 | 对应综述维度 | 核心贡献 |
|---|------|------|-------------|---------|
| 1 | Sinusoidal位置编码追根溯源 | [kexue.fm/archives/8130](https://kexue.fm/archives/8130) | Position Encoding | 对原始 Sinusoidal 位置编码的深入数学分析，为后续 RoPE 推导奠基 |
| 2 | 博采众长的旋转式位置编码 | [kexue.fm/archives/8265](https://kexue.fm/archives/8265) | Position Encoding | **RoPE 原始推导**：从内积不变性出发推导旋转位置编码，兼具绝对编码的实现简洁性和相对编码的理论优势 |
| 3 | 从Performer到线性Attention | [kexue.fm/archives/8338](https://kexue.fm/archives/8338) | Token Mixer | 分析 Performer 的核方法逼近 Softmax Attention 的思路，探讨线性 Attention 的本质 |
| 4 | 二维位置的旋转式位置编码 | [kexue.fm/archives/8397](https://kexue.fm/archives/8397)（推测） | Position Encoding | 将 RoPE 推广到二维位置（如图像），探索 Vision Transformer 中的位置编码 |
| 5 | GAU与Flash Attention的关联 | [kexue.fm/archives/8513](https://kexue.fm/archives/8513)（推测） | Token Mixer / Efficiency | 分析 Gated Attention Unit 的设计思想，探讨 Attention 与 FFN 的融合 |
| 6 | 旋转位置编码的完备性分析 | kexue.fm/archives/8620（推测） | Position Encoding | 对 RoPE 的理论完备性进行更深入的数学分析 |
| 7 | 长度外推性与局部注意力 | kexue.fm/archives/9431（推测） | Position Encoding / Efficiency | 长度外推问题的统一视角：系统分析长度外推问题，提出局部注意力与外推性的关系框架 |
| 8 | 长度外推性与位置鲁棒性 | kexue.fm/archives/9444（推测） | Position Encoding | 提出 even pairs 任务验证全局依赖能力，分析位置鲁棒性与外推性的关系 |
| 9 | 一种全局长度外推的新思路 | [kexue.fm/archives/9603](https://kexue.fm/archives/9603) | Position Encoding | 提出全局长度外推方案，在 even pairs 任务上实现 100% 外推准确率 |
| 10 | RoPE是一种β进制编码 | [kexue.fm/archives/9675](https://kexue.fm/archives/9675) | Position Encoding | NTK-RoPE 理论基础：将 RoPE 解释为 β 进制编码，通过转换进制实现长度外推 |
| 11 | 将β进制位置进行到底 | kexue.fm/archives/9693（推测） | Position Encoding | 引入混合进制思路，进一步推广 NTK-aware Scaled RoPE |
| 12 | 无限外推的ReRoPE？ | [kexue.fm/archives/9708](https://kexue.fm/archives/9708) | Position Encoding | ReRoPE：基于窗口内外不同位置编码策略的无限长度外推方案 |
| 13 | 逆用Leaky ReRoPE | kexue.fm/archives/9756（推测） | Position Encoding | ReRoPE 的改进版本，通过 Leaky 机制优化外推效果 |
| 14 | 当HWFA遇见ReRoPE | kexue.fm/archives/9790（推测） | Token Mixer / Position Encoding | HWFA（Hybrid Window-Full Attention）与 ReRoPE 的结合 |
| 15 | Key归一化助力长度外推 | [kexue.fm/archives/9859](https://kexue.fm/archives/9859) | Position Encoding / Normalization | Key 归一化 + log n 缩放因子改善长度外推 |
| 16 | "复盘"长度外推技术 | [kexue.fm/archives/9948](https://kexue.fm/archives/9948) | Position Encoding | 系统复盘长度外推研究，指出局部注意力方法的局限性 |
| 17 | 多模态位置编码的简单思考 | [kexue.fm/archives/10040](https://kexue.fm/archives/10040) | Position Encoding / Multimodal | RoPE-Tie：多模态场景下的统一位置编码方案 |

> **注**：标注"推测"的链接为根据 archive 编号规律推测，未经直接验证。已确认链接均来自搜索结果。

### 系列之外的重要相关文章

| 标题 | 链接 | 对应综述维度 | 核心贡献 |
|------|------|-------------|---------|
| 线性Attention的探索：Attention必须有个Softmax吗？ | kexue.fm（具体链接待确认） | Token Mixer | 质疑 Softmax 在 Attention 中的必要性，探索去 Softmax 的线性 Attention |
| 线性注意力简史：从模仿、创新到反哺 | kexue.fm（2025年6月发表） | Token Mixer | 系统回顾线性 Attention 的发展历程 |
| 从熵不变性看Attention的Scale操作 | kexue.fm（具体链接待确认） | Token Mixer / Normalization | 从信息论角度分析 Attention 的 Scale 因子 |
| DeepNet相关分析 | kexue.fm（具体链接待确认） | Normalization / Residual | 分析 DeepNet 的尺度分析方法和深层 Transformer 训练 |

---

## 关键文章详细摘要

### 1. RoPE 原始推导（Transformer升级之路：2）

**链接**：https://kexue.fm/archives/8265
**对应论文**：Su et al., "RoFormer: Enhanced Transformer with Rotary Position Embedding", arXiv

**核心推导**：
- 从"通过绝对位置编码实现相对位置编码"的目标出发
- 设定核心约束：内积 `<f(q,m), f(k,n)>` 仅依赖于 q, k 和相对位置 m-n
- 在二维情形下求解该函数方程，得到旋转矩阵形式的解
- 推广到高维：将 d 维向量两两分组，每组应用不同频率的旋转

**关键公式**：
- 对位置 m 处的向量 x，RoPE 编码为：将 x 的每两个分量 (x_{2i}, x_{2i+1}) 乘以旋转矩阵 R(m*theta_i)
- theta_i = 10000^{-2i/d}，与 Sinusoidal 编码的频率设计相通
- 内积自然包含相对位置信息：R(m*theta)^T * R(n*theta) = R((m-n)*theta)

**独到见解**：
- RoPE 不依赖泰勒展开，比 Sinusoidal 编码更严谨
- RoPE 是"目前唯一一种可用于线性 Attention 的相对位置编码"
- 具有良好的长度外推性

**对综述 Section 4（Position Encoding）的补充价值**：
- 提供了从函数方程角度推导位置编码的范式，不同于传统的启发式设计
- 是当前主流 LLM 位置编码的理论基础

### 2. NTK-RoPE：β 进制编码视角（Transformer升级之路：10）

**链接**：https://kexue.fm/archives/9675

**核心思想**：
- 将 RoPE 的位置编码解释为 β 进制数的表示
- 每个频率分量对应 β 进制的一个"位"，低频分量是高位，高频分量是低位
- 长度外推等价于"进制溢出"问题：训练长度内的位置可以用当前进制表示，超出则溢出

**关键洞察**：
- 转换进制（改变 base）可以扩展表示范围，且模型可能无需微调即可适应
- 因为模型学到的是"比较大小"的规则（如 875 > 874），这个规则与进制无关
- 每个维度稍微往外推一些是可行的，因为模型有一定泛化能力
- 这一视角直接启发了社区的 NTK-aware Scaled RoPE 方法

**对综述的补充价值**：
- 提供了理解 RoPE 长度外推的全新数学视角
- β 进制编码框架统一了多种外推方法的理论解释

### 3. ReRoPE：无限外推（Transformer升级之路：12）

**链接**：https://kexue.fm/archives/9708

**核心方法**：
- 在 NTK-RoPE 系列方法达到效果上限后，另辟蹊径
- 对窗口内和窗口外的 token 使用不同的位置编码策略
- 窗口内保持原始 RoPE，窗口外使用压缩/截断的位置编码
- 理论上可实现无限长度外推

**实验结果**：
- 在 1 亿参数 GAU 架构小模型上验证
- 训练长度 512，外推到 4096
- 相比 Baseline、PI-RoPE、NTK-RoPE 等方法有显著提升

**对综述的补充价值**：
- 代表了"事后修改"类长度外推方法的前沿
- 与 HWFA 等"事前修改"方法形成互补

### 4. 线性 Attention 分析（Transformer升级之路：3 及相关文章）

**链接**：https://kexue.fm/archives/8338

**核心分析**：
- 从 Performer 的核方法出发，分析线性 Attention 逼近标准 Attention 的思路
- 提出关键问题："标准 Attention 有什么好的？哪里值得大家向它对齐？"
- 探讨 Softmax 在 Attention 中的真正作用

**相关文章**：
- "线性Attention的探索：Attention必须有个Softmax吗？"——质疑 Softmax 的必要性
- "线性注意力简史：从模仿、创新到反哺"（2025年6月）——系统回顾线性 Attention 发展

**对综述 Section 1（Token Mixer）的补充价值**：
- 提供了从"为什么需要 Softmax"角度理解 Attention 变体的框架
- 线性 Attention 的分析对理解 SSM、Mamba 等替代架构也有参考价值

### 5. Key 归一化与长度外推（Transformer升级之路：15）

**链接**：https://kexue.fm/archives/9859

**核心贡献**：
- 将长度外推技术分为两大类：
  - **事后修改**：NTK-RoPE、YaRN、ReRoPE 等，无需微调但无法保持训练长度内恒等性
  - **事前修改**：ALiBi、KERPLE、XPOS、HWFA 等，需要训练前引入但可直接外推
- 提出 Key 归一化方案，结合 log n 缩放因子
- 在 GAU 架构上实验验证

**对综述的补充价值**：
- 事后/事前修改的分类框架对综述的长度外推部分有直接参考价值
- Key 归一化连接了 Normalization 和 Position Encoding 两个维度

### 6. 长度外推技术复盘（Transformer升级之路：16）

**链接**：https://kexue.fm/archives/9948

**核心观点**：
- 回顾从第 7 篇到第 15 篇连续 9 篇围绕长度外推的研究
- 指出"这个问题远不像一开始想象那么简单"
- 很多基于局部注意力的工作"不总是有效"，暗示旧的分析未触及问题核心
- 提到 PoSE 等社区工作

**对综述的补充价值**：
- 提供了长度外推研究的一手反思和经验总结

### 7. 多模态位置编码 RoPE-Tie（Transformer升级之路：17）

**链接**：https://kexue.fm/archives/10040

**核心思想**：
- 多模态模型（文本+图像+音频等）中，不同模态的 token 如何共享位置编码
- RoPE-Tie 方案：将不同模态的位置编码"绑定"到统一的 RoPE 框架中
- 简洁优雅地解决多模态位置编码问题

**对综述 Section 4（Position Encoding）的补充价值**：
- 将位置编码从单模态扩展到多模态，是重要的前沿方向

---

## 对综述各 Section 的补充建议

### Section 1 (Token Mixer)

- **线性 Attention 分析**（系列第 3 篇及相关文章）：苏剑林对"Softmax 在 Attention 中是否必要"的深入探讨，可补充到 Token Mixer 的 Attention 变体分析中。他从 Performer 的核方法出发，质疑了"逼近标准 Attention"这一目标本身的合理性。
- **GAU（Gated Attention Unit）**：苏剑林在系列中多次使用 GAU 架构做实验（如第 12、15 篇），GAU 将 Attention 和 FFN 融合为单一模块，是 Token Mixer 设计的重要变体。对应论文为 Google 的 "Transformer Quality in Linear Time"（2022），苏剑林的实验提供了独立验证。
- **HWFA（Hybrid Window-Full Attention）**（系列第 14 篇）：混合窗口-全局注意力机制，是一种事前修改的高效 Attention 方案。

### Section 2 (Channel Mixer)

- GAU 的设计将 Attention 和 FFN 融合，模糊了 Token Mixer 和 Channel Mixer 的边界，值得在综述中讨论这种融合趋势。

### Section 3 (Normalization)

- **Key 归一化**（系列第 15 篇）：提出对 Attention 中的 Key 进行归一化以助力长度外推，连接了 Normalization 和 Position Encoding 两个维度。
- **从熵不变性看 Attention 的 Scale 操作**：从信息论角度分析 Attention 的缩放因子，对理解 LayerNorm/RMSNorm 在 Attention 中的作用有参考价值。
- **DeepNet 分析**：苏剑林对 DeepNet（Scaling Transformers to 1,000 Layers）的尺度分析进行了独立推导和修正，对理解深层 Transformer 的归一化和初始化方案有重要参考价值。

### Section 4 (Position Encoding) — 最核心的补充

- **RoPE 原始推导**（系列第 2 篇）：**必须引用**。这是当前主流 LLM 位置编码的理论基础，从函数方程角度推导，比启发式设计更严谨。
- **NTK-RoPE 的 β 进制编码视角**（系列第 10 篇）：独到的理论贡献，将位置编码与数制理论联系，启发了社区的 NTK-aware Scaled RoPE。
- **ReRoPE 的无限外推方案**（系列第 12 篇）：代表事后修改类方法的前沿。
- **长度外推的两类方法分类**（系列第 15、16 篇）：事后修改 vs 事前修改的分类框架，对综述的组织结构有直接参考价值。
- **RoPE-Tie 多模态位置编码**（系列第 17 篇）：将位置编码扩展到多模态场景。
- **Sinusoidal 位置编码追根溯源**（系列第 1 篇）：对原始位置编码的深入分析，可作为综述的历史背景补充。

### Section 5 (Residual Connection)

- DeepNet 的分析中涉及残差连接的尺度分析，指出"增量爆炸"是深模型训练的根本困难。

---

## 关键引用信息

### 学术论文
```bibtex
@article{su2024roformer,
  title={RoFormer: Enhanced Transformer with Rotary Position Embedding},
  author={Su, Jianlin and Lu, Yu and Pan, Shengfeng and Murtadha, Ahmed and Wen, Bo and Liu, Yunfeng},
  journal={Neurocomputing},
  volume={568},
  pages={127063},
  year={2024},
  publisher={Elsevier}
}
```

### GitHub 仓库
- RoFormer: https://github.com/ZhuiyiTechnology/roformer
- GAU-alpha: https://github.com/ZhuiyiTechnology/GAU-alpha

### 博客主页
- 科学空间: https://kexue.fm
- 英文翻译: https://www.tylerromero.com/translations/scientific-spaces/

---

## 数据收集说明

- 本文档基于 2026 年 4 月的网络搜索结果编制
- kexue.fm 域名在爬取时被安全策略阻止，部分文章内容基于搜索摘要和已知信息整理
- 标注"推测"的链接为根据 archive 编号规律推测，建议后续手动验证
- 系列可能还有第 18 篇及之后的文章（2024 年底至 2025 年），建议后续补充
