# Brainformers: Trading Simplicity for Efficiency
**作者**: Yanqi Zhou, Nan Du, Yanping Huang, Daiyi Peng, Chang Lan, Da Huang, Siamak Shakeri, David So, Andrew Dai, Yonghui Wu, Maxim Krikun, Yanping Huang, Dehao Chen, Quoc V. Le | **年份**: 2023 | **arxiv**: 2306.00008 | **发表**: ICML 2023

## 0. 摘要翻译
Brainformer 提出用**异构的复杂 Transformer 块**替代传统 Transformer 中均匀重复的 Attn-FFN 块。通过进化搜索算法，在包含稀疏门控 FFN (MoE)、密集 FFN、注意力层、各种归一化和激活函数的设计空间中搜索最优的层组合和排列方式。实验表明，8B 激活参数的 Brainformer 比 GLaM 训练收敛快 2 倍，步时间快 5 倍，SuperGLUE 高 3%。

## 1. 方法动机
- 传统 Transformer 使用**均匀重复**的块结构（Attn-FFN-Attn-FFN...），这种设计简单但可能不是最优的
- 不同类型的层（稠密、稀疏、注意力）在不同位置可能有不同的最优配置
- 手工设计异构架构的搜索空间太大
- 利用进化搜索自动发现更高效的块组合

## 2. 方法设计（重点：模块排列顺序及其理论分析）

### 核心思想：异构块设计
- 放弃 Transformer 的"均匀重复"范式
- 每个 Brainformer 块由多种不同类型的层组成
- 搜索空间包括：
  - **稀疏门控 FFN (MoE)**：带路由机制的专家混合层
  - **密集 FFN**：标准前馈网络
  - **注意力层**：不同配置的自注意力
  - **各种归一化**：LayerNorm 等
  - **各种激活函数**

### 搜索维度
1. **层类型选择**：在 MoE、Dense FFN、Attention 中选择
2. **层排列顺序**：确定各类型层的最优排列
3. **层宽度**：不同层可以有不同的隐藏维度
4. **注意力频率**：优化注意力层出现的频率（可以不每层都有注意力）
5. **门控策略**：MoE 层的路由和容量设置

### 关键发现
- 最优块设计是**非均匀**的，包含多种层类型的混合
- 注意力层的频率可以降低（不需要每层都有）
- 不同位置的层宽度应该不同
- 搜索得到的"复杂块"虽然结构复杂，但计算效率更高

## 3. 与其他方法对比
| 方法 | 块设计 | 层类型 | 设计方式 |
|------|-------|-------|---------|
| 标准 Transformer | 均匀 (Attn-FFN) | 2种 | 手工 |
| GLaM | 半均匀 (Dense-MoE 交替) | 3种 | 手工 |
| Primer | 均匀 (修改后的 Attn-FFN) | 2种 | 搜索 |
| Brainformer | 异构（多种层混合） | 多种 | 进化搜索 |

## 4. 实验表现
- **vs GLaM (8B 激活参数)**：
  - 训练收敛速度快 **2 倍**
  - 步时间（step time）快 **5 倍**
  - SuperGLUE 评分高 **3%**
- **扩展性**：
  - GLaM 扩大规模时 example rate 显著下降，Brainformer 保持稳定
  - 训练 perplexity 随规模增大而改善，同时 example rate 基本不变
- **vs 密集模型**：
  - 在相同计算预算下，Brainformer 在 few-shot 和 one-shot 评估中超越密集 Transformer（包括 Primer）
- 近乎完美的对数尺度质量缩放

## 5. 总结
a) **一句话概括**：Brainformer 通过进化搜索发现异构 Transformer 块设计（混合 MoE、Dense FFN 和 Attention），以"牺牲简单性换取效率"的方式大幅超越均匀块设计。

b) **速记 pipeline**：`Input -> [Heterogeneous Block: MoE + Dense + Attn + Norms (搜索得到的最优排列)] x L -> Output`
