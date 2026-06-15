# Reducing Transformer Key-Value Cache Size with Cross-Layer Attention

**论文信息**: Brandon, W., Mishra, M., Nrusimha, A., Panda, R., Ragan-Kelley, J. (2024)
**arXiv**: 2405.12981 | **会议**: NeurIPS 2024
**分类**: Depth (跨层信息共享)

## 核心思想
将 KV 共享从"层内"扩展到"跨层"——相邻层共享同一组 KV 头，从而在不显著影响精度的前提下进一步压缩 KV 缓存。

## 关键机制
1. **跨层 KV 共享**: 将多层分组，同一组内的层共享 KV 激活
2. **与 MQA/GQA 互补**: MQA/GQA 在层内共享头；CLA 在层间共享
3. **可与 MQA 叠加**: CLA + MQA 实现更极端的压缩

## 与残差连接的关系
CLA 的有效性隐含了残差连接的一个重要性质：
- 相邻层的输入由残差连接相连，高度相似
- 因此相邻层的 KV 表示也高度冗余
- 残差连接的"平滑性"使跨层共享可行

## 实验结果
- 相比 MQA 进一步减少 **2x** KV 缓存
- 准确率几乎不损失
- 允许更长序列和更大批次推理

## 与综述的关联
属于 **Depth** 维度。CLA 揭示了残差连接的副作用：
- 残差累加使相邻层表示高度相关
- 这种相关性可以被利用来减少冗余
- 与 DenseFormer/MuddFormer 关注跨层连接的增强形成对比：CLA 关注跨层冗余的利用

## 核心贡献
将跨层残差连接的冗余性转化为推理效率优势，开辟了 KV 缓存压缩的新维度。
