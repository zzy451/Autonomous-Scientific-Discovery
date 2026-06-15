# Understanding the Difficulty of Training Transformers

## 基本信息
- **作者**: Liyuan Liu, Xiaodong Liu, Jianfeng Gao, Weizhu Chen, Jiawei Han
- **年份**: 2020 (EMNLP 2020)
- **arXiv**: 2004.08249
- **关键词**: 训练稳定性, 梯度消失, Post-Norm, 放大效应

## 核心贡献（Module Sequence 维度）
本文深入分析了 Post-Norm Transformer 的训练困难，超越了简单的"梯度消失"解释。

### 1. "放大效应" (Amplification Effect) 的发现
- Post-Norm 架构中，残差分支的依赖性过强
- 早期训练时，某一层参数的微小更新会通过残差连接被放大
- 导致模型输出产生大幅不稳定波动
- **仅解决梯度消失并不足以完全稳定训练**

### 2. 提出的解决方案
- **Pre-Norm**: 将 LayerNorm 移到残差块输入位置
- **ScaleNorm**: 用单个可学习缩放参数来归一化隐藏状态
- **FixNorm**: 将词嵌入归一化到固定长度
- 这些技术使 Transformer 训练更鲁棒，减少对 warmup 的依赖

### 3. 关键实验发现
- 使用"混合" Transformer（Post-LN encoder + Pre-LN decoder）发现即使部分解决梯度消失，训练仍不稳定
- 证明了问题的根源在于残差分支的放大效应，而非单纯的梯度消失

## 与综述的关联
- 补充了 Xiong et al. 的理论分析，提供了更深入的诊断
- 为后续 ADMIN 初始化、DeepNet 等方法提供了分析基础
- 强调了 Module Sequence 对训练动态的深远影响
