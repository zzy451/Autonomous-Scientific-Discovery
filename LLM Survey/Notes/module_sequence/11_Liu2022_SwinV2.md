# Swin Transformer V2: Scaling Up Capacity and Resolution

## 基本信息
- **作者**: Ze Liu, Han Hu, Yutong Lin, Zhuliang Yao, Zhenda Xie, Yixuan Wei, Jia Ning, Yue Cao, Zheng Zhang, Li Dong, Furu Wei, Baining Guo
- **年份**: 2022 (CVPR 2022)
- **arXiv**: 2111.09883
- **关键词**: res-post-norm, 缩放余弦注意力, 视觉Transformer

## 核心贡献（Module Sequence 维度）
提出 res-post-norm 归一化配置，解决大规模视觉 Transformer 的训练不稳定性。

### 1. 问题
- 原始 Swin Transformer 使用 Pre-Norm
- 扩展到 3B 参数时，深层的激活值急剧增大
- Pre-Norm 中残差路径的累积导致激活值爆炸

### 2. Res-Post-Norm
- 将 LayerNorm 从残差单元的开头移到末尾（回到 Post-Norm 位置）
- 与标准 Post-Norm 不同：这里是在 Swin 的特定窗口注意力上下文中
- 产生更温和的激活值分布
- 显著改善深层网络的训练稳定性

### 3. 配套技术
- **Scaled Cosine Attention**: 用余弦相似度替代点积注意力，不依赖输入幅度
- 防止注意力值进入极端值
- 两者协同解决扩展问题

### 4. 成果
- 成功扩展到 3B 参数
- 支持高分辨率输入（1536 x 1536）

## 与综述的关联
- 虽然是视觉领域的工作，但其 Module Sequence 洞察具有通用性
- 说明 Pre-Norm 并非在所有场景下都最优——极深模型中可能需要回到 Post-Norm
- 与 DeepNet 的发现一致：Post-Norm + 特定技术可以实现更好的训练稳定性
- 注意：此工作主要面向 ViT，LLM 领域的直接应用较少
