# Randomized Positional Encodings
**论文**: Randomized Positional Encodings Boost Length Generalization of Transformers
**作者**: Anian Ruoss, Grégoire Delétang, Tim Genewein, Jordi Grau-Moya, Róbert Csordás, Mehdi Bennani, Shane Legg, Joel Veness
**年份**: 2023
**会议**: ACL 2024 (Google DeepMind)
**arXiv**: 2305.16843

## 核心思想
在训练时随机采样位置索引（而非使用连续的 0,1,2,...），模拟更长序列的位置分布，使模型学习依赖相对顺序而非绝对位置，从而显著提升长度泛化能力。

## 方法细节

### 标准 PE 的长度泛化问题
- 训练时模型只见过 [0, L-1] 的位置索引
- 测试时若序列长度 > L，位置索引进入 OOD（Out-of-Distribution）
- 模型对未见位置的行为不可预测

### 随机化位置编码 (RPE)
1. 设定一个远大于训练长度的"假想最大长度" L_max
2. 对于长度为 n 的训练序列，从 [0, L_max-1] 中随机采样 n 个有序位置
3. 用这些随机位置替代标准的 0,1,...,n-1

### 效果
- 每次训练看到的位置组合不同
- 模型被迫学习位置的相对顺序，而非记忆绝对位置
- 训练时已经"模拟"了长序列的稀疏位置分布
- 测试时遇到长序列不再是 OOD

### 与现有 PE 的兼容性
- 可应用于 Sinusoidal PE
- 可应用于 Learned PE
- 可应用于 RoPE
- 可应用于 ALiBi
- 是一种 meta-strategy，叠加在任何 PE 上

## Position Encoding 维度分析

### 分类
- **类型**: 训练策略（Meta-approach，兼容任意 PE）
- **注入方式**: 修改位置索引的采样方式
- **参数量**: 零额外参数
- **长度外推**: 显著提升，平均准确率提高 12%

### 关键洞察
1. 长度泛化失败的根因是位置索引 OOD
2. 随机采样可以消除 OOD 问题
3. 与具体 PE 方法正交，可组合使用

### 与 CAPE 的对比
| 方面 | CAPE | Randomized PE |
|------|------|--------------|
| 增强对象 | 位置 embedding | 位置索引 |
| 增强方式 | shift/scale/jitter | 随机稀疏采样 |
| 适用编码 | sinusoidal | 任意 |
| 评估任务 | NLP/CV/ASR | 算法推理 |

## 实验结果
- 算法推理任务: 平均 12% 准确率提升
- 在 addition, sorting, multiplication 等任务上测试
- 训练长度 40，测试长度 500+ 时仍保持高准确率

## 影响
- 提供了一种与 PE 设计正交的增强策略
- 对"为什么 Transformer 难以长度泛化"提供了位置 OOD 的解释
- 启发了 Random Float Sampling 等后续方法
