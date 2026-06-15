# Universal Transformers

**论文信息**: Dehghani, M., Gouws, S., Vinyals, O., Uszkoreit, J., Kaiser, L. (2019)
**arXiv**: 1807.03819 | **会议**: ICLR 2019
**分类**: Depth (自适应深度/权重共享)

## 核心思想
用**单个共享权重层**迭代处理输入，替代标准 Transformer 的不同层堆叠。结合自适应计算时间(ACT)，实现逐 token 的动态深度。

## 关键机制
1. **权重共享**: 所有"层"使用相同参数，本质上是残差连接的递归应用
2. **自适应停止**: 每个位置独立计算"停止概率"
   - 当概率超过阈值，该 token 停止更新
   - 表示被"冻结"并直接传递
3. **图灵完备**: 递归 + 自适应停止 -> 理论上图灵完备

## 与残差连接的关系
Universal Transformer 本质上是**残差连接的递归版本**：
- 标准: x_{l+1} = x_l + F_l(x_l), 每层不同的 F_l
- UT:   x_{t+1} = x_t + F(x_t), 共享的 F，迭代 t 次
- 残差连接确保迭代精修而非替换

## 实验结果
- 在算法推理任务（如 bAbI）上显著优于标准 Transformer
- 在 NMT 上性能与标准 Transformer 相当

## 与综述的关联
属于 **Depth** 维度。Universal Transformer 是"自适应深度"的先驱：
- 启发了 Mixture-of-Depths (Raposo 2024)
- 体现了残差连接允许"迭代精修"的核心思想
- 后续的 Depth-Adaptive Transformer 和 Early Exit 均受其启发

## 核心贡献
提出了残差连接驱动的递归 Transformer，实现了深度的动态化和自适应。
