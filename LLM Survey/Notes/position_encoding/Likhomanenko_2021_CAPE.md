# CAPE: Encoding Relative Positions with Continuous Augmented Positional Embeddings
**作者**: Tatiana Likhomanenko, Qiantong Xu, Gabriel Synnaeve, Ronan Collobert, Alex Rogozhnikov | **年份**: 2021 | **来源**: NeurIPS 2021 | **arXiv**: 2106.03143

## 0. 摘要翻译
本文提出 CAPE（Continuous Augmented Positional Embeddings），一种基于数据增强思想的位置编码方法。CAPE 在训练时对位置索引进行随机扰动（augmentation），使得绝对位置编码隐式地编码相对位置信息。该方法结合了绝对位置编码的简洁性/速度与相对位置编码的泛化优势，在机器翻译、图像识别和语音识别任务上均表现出色。

## 1. 方法动机
a) **为什么提出**: 绝对位置编码（APE）计算简单但泛化性差；相对位置编码（RPE）泛化性好但计算复杂。能否两全其美？
b) **现有痛点**: 
   - 标准 sinusoidal/learned APE 对序列长度敏感，难以泛化
   - 相对位置编码需要修改注意力计算，增加实现复杂度和计算成本
   - 需要一种既简单又具备相对位置泛化能力的方法
c) **研究假设**: 通过在训练时对位置索引进行随机位移和缩放增强，可以使模型学到对绝对位置不敏感但对相对位置敏感的表示。

## 2. 方法设计
a) **pipeline**: 
   1. 位置索引 $p = [0, 1, 2, ..., L-1]$
   2. 训练时：对位置施加随机增强 $p' = \alpha \cdot p + \beta$（$\alpha$ 为缩放，$\beta$ 为位移）
   3. 使用增强后的位置 $p'$ 计算 sinusoidal 位置编码
   4. 将编码加到 word embedding 上（标准 APE 流程）
   5. 推理时：使用原始位置索引（或适当缩放的索引）

b) **模块功能**: 
   - 随机位移：使模型不依赖绝对位置值，学习相对关系
   - 随机缩放：使模型适应不同序列长度的位置间距
   - 连续性：使用连续的 sinusoidal 函数（非离散 learned embedding）以支持任意增强值

c) **公式解释**:
   - 标准 sinusoidal: $PE(p, 2i) = \sin(p / 10000^{2i/d})$
   - CAPE 增强: $PE(p', 2i) = \sin((\alpha p + \beta) / 10000^{2i/d})$
   - 位移增强: $\beta \sim \text{Uniform}(-\delta, \delta)$，使模型对绝对位置不变
   - 缩放增强: $\alpha \sim \text{Uniform}(1-\epsilon, 1+\epsilon)$，使模型适应不同长度
   - 效果：$PE(\alpha p_1 + \beta) - PE(\alpha p_2 + \beta)$ 主要依赖 $\alpha(p_1 - p_2)$

## 3. 与其他方法对比
a) **本质不同**: 
   - 与标准 sinusoidal PE：CAPE 增加训练时增强，迫使模型学习相对位置
   - 与 RoPE：RoPE 在数学上保证相对位置依赖，CAPE 通过数据增强隐式实现
   - 与 relative PE（Shaw, T5）：CAPE 不修改注意力计算，保持 APE 的简洁性
b) **创新点**: 
   - 将数据增强思想引入位置编码（regularization 视角）
   - 在不修改架构的前提下获得相对位置编码的泛化优势
   - 适用于任何使用连续位置编码的 Transformer
c) **适用场景**: 任何使用 sinusoidal APE 的 Transformer；多模态任务（语音、图像、文本）。

## 4. 实验表现
a) **验证方式**: 在 WMT 机器翻译、ImageNet 图像分类、LibriSpeech 语音识别上评估。
b) **关键数据**: 
   - 机器翻译：BLEU 提升约 0.5-1.0（相比标准 sinusoidal PE）
   - 图像分类：DeiT 上 top-1 准确率提升约 0.3%
   - 语音识别：WER 降低约 0.1-0.2%
   - 长度泛化：在超出训练长度的序列上性能退化更平缓
c) **局限性**: 
   - 增强超参数（$\delta, \epsilon$）需要调优
   - 性能提升幅度相对温和
   - 在极端长度外推场景下不如专门设计的方法（如 ALiBi）
   - 随着 RoPE 成为主流，APE 系方法的应用场景缩小

## 5. 总结
a) **一句话概括**: CAPE 通过在训练时对 sinusoidal 位置索引进行随机位移和缩放增强，使绝对位置编码隐式获得相对位置编码的泛化优势，同时保持计算简洁性。
b) **速记 pipeline**: Position Index $p$ → Random Augment ($\alpha p + \beta$) at Train → Sinusoidal PE → Add to Embedding → Standard Transformer
