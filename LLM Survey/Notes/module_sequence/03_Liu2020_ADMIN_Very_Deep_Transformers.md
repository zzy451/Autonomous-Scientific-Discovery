# Very Deep Transformers for Neural Machine Translation (ADMIN)

## 基本信息
- **作者**: Liyuan Liu, Xiaodong Liu, Jianfeng Gao, Weizhu Chen, Jiawei Han
- **年份**: 2020 (arXiv: 2008.07772)
- **关键词**: ADMIN, 深层Transformer, 初始化策略, Post-Norm

## 核心贡献（Module Sequence 维度）
提出 ADMIN (Adaptive Model Initialization) 方法，使深层 Post-Norm Transformer 可以稳定训练。

### 1. 动机
- Pre-Norm 虽然稳定，但在某些任务上性能不如 Post-Norm
- Post-Norm 难以训练深层模型（>12层）
- 目标：结合 Pre-Norm 的稳定性和 Post-Norm 的性能

### 2. ADMIN 初始化策略
- 在训练早期限制层对残差分支的依赖
- 不引入额外的超参数
- 训练后可以重新参数化为标准 Transformer 架构
- 对半精度训练友好

### 3. 实验结果
- 成功训练了 60 encoder + 12 decoder 的超深 Transformer
- 在 WMT'14 EN-FR 和 EN-DE 上达到 SOTA
- 深层模型一致性地优于标准 6 层基线

## 与综述的关联
- 展示了 Module Sequence（Post-Norm）本身并非不可用，而是需要配合正确的初始化
- 与 DeepNet (Wang et al. 2024) 形成互补：都是让 Post-Norm 深层训练可行的方法
- 说明 Module Sequence 和初始化策略是紧密耦合的设计选择
