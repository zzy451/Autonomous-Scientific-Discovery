# CAPE: Continuous Augmented Positional Embeddings
**论文**: CAPE: Encoding Relative Positions with Continuous Augmented Positional Embeddings
**作者**: Tatiana Likhomanenko, Qiantong Xu, Gabriel Synnaeve, Ronan Collobert, Alex Rogozhnikov
**年份**: 2021
**会议**: NeurIPS 2021
**arXiv**: 2106.03143

## 核心思想
通过对绝对位置编码施加数据增强（augmentation），使其兼具绝对编码的简单高效和相对编码的泛化能力，且不需要修改 attention 机制。

## 方法细节

### 连续位置 (Continuous Positions)
- 使用连续实数（而非离散整数）表示位置
- 更适合图像、音频、视频等连续模态
- 基于 sinusoidal 编码的连续扩展

### 位置增强 (Positional Augmentation)
在训练时对位置索引施加三种增强：

1. **全局平移 (Global Shift)**: 对整个序列的位置加一个随机偏移
   - 效果：模型不再依赖绝对位置的具体值
   - 隐式学习相对位置关系

2. **局部抖动 (Local Shift)**: 对每个位置加小的随机扰动
   - 效果：增加位置表示的鲁棒性
   - 减少对精确位置的过拟合

3. **全局缩放 (Global Scaling)**: 对位置序列整体缩放
   - 效果：使模型适应不同分辨率/长度的输入
   - 有助于长度外推

### 关键优势
- 不修改 attention 机制（保持 absolute PE 的计算效率）
- 通过增强间接获得相对位置的泛化能力
- 对训练超参数更稳定

## Position Encoding 维度分析

### 分类
- **类型**: Augmented Absolute Position Encoding
- **注入方式**: 加到输入 embedding（与 sinusoidal 相同）
- **参数量**: 零（如使用 sinusoidal 基础）或少量（如使用 learned 基础）
- **长度外推**: 通过增强策略提升泛化

### 独特定位
- 桥接 absolute PE 和 relative PE 的优势
- "增强式"方法论：不改架构，改数据/训练方式
- 多模态友好（连续位置适合非文本模态）

## 实验结果
- 机器翻译：泛化到训练未见长度时性能提升
- 图像识别：不同分辨率下更稳定
- 语音识别：改善跨长度泛化

## 影响
- 表明位置编码不仅可以从架构层面改进，也可从训练策略层面改进
- 连续位置的思想对多模态 Transformer 有启发
