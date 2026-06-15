# Understanding the Difficulty of Training Transformers (Admin)

**论文信息**: Liu, L., Liu, X., Gao, J., Chen, W., Han, J. (2020)
**arXiv**: 2004.08249 | **会议**: EMNLP 2020
**分类**: Control (自适应初始化)

## 核心思想
发现 Transformer 训练困难的根源——"放大效应" (Amplification Effect)：残差分支对参数更新的依赖过强时，小的参数变化被放大导致训练不稳定。提出 Admin (Adaptive Model Initialization) 解决。

## Admin 方法
- **训练初期**: 降低层对残差分支的依赖 -> 确保稳定性
- **训练后期**: 增强残差分支的依赖 -> 释放模型潜力
- **可重参数化**: 训练完成后可重新参数化为标准 Transformer 架构

## 关键发现
1. 深层 Transformer 中，残差分支的贡献被层数"放大"
2. 放大效应导致梯度爆炸和训练发散
3. Admin 通过自适应调节残差权重来平衡稳定性和表达能力

## 实验结果
- 稳定训练深达 **200 层**的 Transformer
- 在 WMT'14 机器翻译基准上收敛更快、性能更优

## 与综述的关联
属于 **Control** 维度。与 ReZero/SkipInit 的"一刀切"零初始化不同，Admin 是**自适应**的：
- 初期抑制、后期释放残差分支
- 不改变最终模型架构
- 提供了"放大效应"的理论解释

## 核心贡献
首次理论分析残差分支在 Transformer 中的"放大效应"，并提出自适应初始化方案。
