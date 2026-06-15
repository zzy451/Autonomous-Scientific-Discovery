# The Curse of Depth in Large Language Models

**论文信息**: Sun, L., et al. (2025)
**arXiv**: 2502.05795 | **会议**: NeurIPS 2025 (submitted)
**分类**: Control (深度缩放/残差方差控制)

## 核心思想
揭示了 Pre-LN Transformer 的"深度诅咒"：深层的贡献远小于浅层。原因是 Pre-LN 导致激活方差随深度指数增长，使深层的残差路径主导信号，子层输出被淹没。

## 问题分析
1. **方差爆炸**: Pre-LN 中，x_{l+1} = x_l + SubLayer(LN(x_l))，残差累加使方差随层数指数增长
2. **恒等映射退化**: 方差过大时，Jacobian 趋近恒等矩阵，深层实际不做有意义计算
3. **经验验证**: Llama、Mistral、DeepSeek、Qwen 等主流 LLM 均存在此现象

## 解决方案: LayerNorm Scaling (LNS)
公式: 将第 l 层 LayerNorm 输出缩放 1/sqrt(l)

- **简单实现**: 无超参数、无额外可学习参数
- **效果**: 抑制方差指数增长，使深层有效贡献
- **注意**: 建议移除 Scaled Initialization 以避免干扰

## 实验结果
- 从 130M 到 7B 参数模型均有效
- 预训练性能一致提升
- SFT 后性能优势保持

## 与综述的关联
属于 **Control** 维度的最新工作。直接回应了 Pre-LN 的隐患：
- Xiong2020 推广了 Pre-LN 因其稳定性
- Sun2025 指出 Pre-LN 的代价——深层无效
- LNS 是对 Pre-LN 的"修补"，保持稳定性同时恢复深层功能

## 核心贡献
诊断并量化了 Pre-LN 残差连接的深层退化问题，提供了极简修复方案。
