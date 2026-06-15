# Jamba: A Hybrid Transformer-Mamba Language Model
**作者**: AI21 Labs (Opher Lieber, Barak Lenz, Horace He, et al.) | **年份**: 2024 | **arxiv**: 2403.19887 | **链接**: https://arxiv.org/abs/2403.19887

## 0. 摘要翻译
Jamba 是一种混合架构语言模型，交替排列 Transformer 层和 Mamba（结构化状态空间模型, SSM）层，并在部分层中加入 Mixture-of-Experts (MoE)。这种交替设计结合了 Transformer 的高精度上下文检索能力和 Mamba 的线性复杂度序列建模效率。Jamba 拥有 52B 总参数（12B 激活），支持 256K 上下文长度，可在单张 80GB GPU 上运行。

## 1. 方法动机
- Transformer 的 Attention 机制在精确检索（recall）方面表现优异，但 O(n²) 复杂度限制了长序列效率
- Mamba/SSM 具有 O(n) 线性复杂度，擅长长序列建模，但在精确检索任务上不如 Attention
- 纯 Mamba 模型在需要精确 token 匹配的任务（如 NIAH）上表现较弱
- 关键洞察：两种机制互补，交替排列可以兼得两者优势

## 2. 方法设计

### 交替层设计
- 基本单元为"Jamba block"，每个 block 包含交替的 Mamba 层和 Attention 层
- 典型比例：每 8 层中 7 层 Mamba + 1 层 Attention（约 7:1）
- Attention 层提供精确的全局信息检索
- Mamba 层提供高效的序列状态压缩和传递

### 层排列模式
```
[Mamba] -> [Mamba] -> ... -> [Mamba] -> [Attention] -> 重复
          (7 层 Mamba)                  (1 层 Attn)
```

### MoE 集成
- 部分层（Mamba 和 Attention 均可）使用 MoE 替代标准 FFN
- 增加模型总容量而不增加激活参数
- 52B 总参数，仅 12B 在每个 token 上激活

### 关键设计决策
- **比例选择**：通过消融实验确定 7:1 为最优比例
  - 纯 Mamba：长序列高效但检索弱
  - 1:1 交替：性能好但效率提升有限
  - 7:1：最佳效率-质量平衡点
- **Attention 层位置**：均匀间隔分布，确保信息定期被精确聚合

## 3. 与其他方法对比
| 模型 | 层类型 | 交替比例 | 复杂度 | 上下文 | 参数 |
|------|-------|---------|-------|-------|------|
| Llama 2 | 全 Attention | 均匀 | O(n²) | 4K | 70B |
| Mamba | 全 SSM | 均匀 | O(n) | 长 | 2.8B |
| Jamba | Mamba+Attn | ~7:1 | 近线性 | 256K | 52B(12B活) |
| MiniMax-01 | Lightning+Softmax | 7:1 | 近线性 | 4M | 456B(46B活) |
| Gemma 3 | SWA+Global Attn | 5:1 | 亚二次 | 128K | 27B |

### 交替架构的共同模式
- Jamba (Mamba:Attn ≈ 7:1)、MiniMax-01 (Linear:Softmax = 7:1)、Gemma 3 (SWA:Global = 5:1)
- 共同趋势：高效层占绝大多数，精确层少量但均匀分布
- 精确层的作用类似"信息同步点"，定期整合全局信息

## 4. 实验表现
- 在标准 LLM 基准上与同规模 Transformer 模型（Llama 2 70B、Mixtral）性能可比
- 长上下文任务上显著优于纯 Transformer（得益于 Mamba 的线性复杂度）
- 吞吐量：在 256K 上下文下比同规模纯 Transformer 快 3x+
- 内存：可在单张 80GB GPU 上运行 256K 上下文（纯 Transformer 无法做到）

## 5. 总结
a) **一句话概括**：Jamba 通过约 7:1 的 Mamba/Attention 交替层设计，结合 MoE，实现了线性复杂度的长序列建模与精确检索的平衡，开创了异构层交替排列的实用范式。

b) **速记 pipeline**：`[Mamba+FFN/MoE] x7 -> [Attn+FFN/MoE] x1 -> 重复`（52B 总参数，12B 激活，256K 上下文）
