# MOBA: Mixture of Block Attention
**作者**: Enzhe Lu, Zhejun Jiang, Jingyuan Liu, Yulun Du, Tao Jiang, Chao Hong, Shaowei Chen, Weiran He, Enming Yuan, Yuzhi Wang, Zhiqi Huang (MoonShot AI / Kimi) | **年份**: 2025 | **arxiv**: 2502.13189

## 0. 摘要翻译
本文提出MOBA（Mixture of Block Attention），一种将混合专家（MoE）思想应用于注意力机制的方法。MOBA允许每个query token动态选择最相关的KV block来参与注意力计算，而不是关注所有token。该方法可以无缝集成到现有的full-attention模型中，通过continue-training即可获得高效的稀疏注意力能力。MOBA在Kimi的长上下文模型中已得到实际部署。

## 1. 方法动机
a) **为什么提出**: 长上下文LLM（如支持128K-1M token）的推理成本极高，需要高效的稀疏注意力来降低KV cache访问和计算开销。
b) **现有痛点**: (1) 全注意力在超长上下文上不可持续；(2) 固定稀疏模式（如滑动窗口）无法适应不同query的需求；(3) 推理阶段的事后稀疏会导致质量损失。
c) **研究假设**: 借鉴MoE中"路由到最相关专家"的思想，每个query应该被路由到最相关的KV block，类似于token选择自己最需要的"注意力专家"。

## 2. 方法设计
a) **Pipeline**: 将KV序列分为固定大小的block，每个query通过路由机制选择top-k个block，仅在选中的block上计算注意力。

b) **模块功能**:
- **Block划分**: 将长度为$L$的KV序列等分为$L/B$个block，每个block包含$B$个连续token。
- **路由机制 (Router)**: 对每个query $q_i$，计算与每个block的相关性分数。使用block内所有key的均值（或可学习的block表示）来计算路由分数：$s_{i,j} = q_i \cdot \bar{k}_j$。
- **Top-k选择**: 选择得分最高的$k$个block（加上当前token附近的局部block），仅在这些block上计算标准注意力。
- **局部窗口**: 始终保留当前位置附近的block（类似滑动窗口），确保局部信息不丢失。
- **与FlashAttention兼容**: 可以基于FlashAttention的block-level计算范式高效实现。

c) **公式解释**:
- 路由: $\mathcal{S}_i = \text{top-k}(\{q_i \cdot \bar{k}_j\}_{j=1}^{L/B})$
- 注意力: $o_i = \text{Attn}(q_i, K_{\mathcal{S}_i}, V_{\mathcal{S}_i})$，只在选中的$k$个block上计算
- 复杂度: $O(L \cdot k \cdot B)$，当$k \cdot B \ll L$时远小于$O(L^2)$

## 3. 与其他方法对比
| 方面 | MOBA | NSA | Full Attention | Longformer |
|------|------|-----|---------------|------------|
| 稀疏类型 | 动态block选择 | 多路径融合 | 密集 | 固定窗口+全局 |
| 路由方式 | MoE式top-k | 压缩+选择 | N/A | 预设位置 |
| 训练方式 | continue-training | 从头训练 | 标准 | 标准 |
| 部署验证 | Kimi实际部署 | DeepSeek | 通用 | 学术 |

## 4. 实验表现
- **长上下文基准**: 在Needle-in-a-Haystack, RULER等长上下文评测上接近或匹配全注意力
- **通用基准**: 在标准NLP基准上与全注意力模型差距极小
- **效率**: 在128K+上下文长度上实现显著的计算和内存节省
- **实际部署**: 已在Kimi的产品中验证，证明了方法的实用性
- **兼容性**: 可以从已有全注意力checkpoint通过continue-training获得

## 5. 总结
a) **一句话概括**: MOBA将MoE的动态路由思想引入注意力机制，让每个query选择最相关的KV block进行注意力计算，实现了可从现有模型continue-training的高效稀疏注意力。
b) **速记pipeline**: KV → 分Block → 每个Q路由选top-k Block → 在选中Block上FlashAttn → Output
