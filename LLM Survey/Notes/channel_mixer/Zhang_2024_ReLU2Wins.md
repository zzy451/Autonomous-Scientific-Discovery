# ReLU^2 Wins: Discovering Efficient Activation Functions for Sparse LLMs

**论文**: ReLU^2 Wins: Discovering Efficient Activation Functions for Sparse LLMs
**作者**: Zhengyan Zhang, Yixin Song, Guanghui Qi, Zeyu Li, Jiansheng Bai, Xipeng Qiu, Zhiyuan Liu, Maosong Sun
**年份**: 2024
**来源**: arXiv:2402.03804
**标签**: 激活函数, 稀疏性, FFN, 推理加速

---

## 0. 摘要
本文系统评估了多种激活函数（ReLU, SwiGLU, ReGLU, ReLU^2）在 LLM 的 FFN 层中的稀疏性特征，提出广义激活稀疏性定义，发现 ReLU^2（Squared ReLU）在模型性能与激活稀疏性之间取得了最佳平衡，可实现接近 90% 的激活稀疏度且性能损失小于 0.1%。

## 1. 方法动机
a) SwiGLU 虽然在质量上优秀，但其平滑激活函数不产生严格的零输出，不利于推理时的稀疏加速。
b) ReLU 天然产生稀疏激活，但直接用 ReLU 替换 SwiGLU 会损失性能。
c) 假设：存在某种激活函数能同时保持高质量和高稀疏度，使推理可以跳过不活跃神经元。

## 2. 方法设计
a) 核心流程：
   - 定义广义激活稀疏性：不仅看严格为零的神经元，还考虑输出幅度极小的神经元
   - 系统评估 ReLU, GELU, SiLU, SwiGLU, ReGLU, ReLU^2 等激活函数的稀疏性
   - ReLU^2 = max(0, x)^2，即先 ReLU 再平方
   - 分析神经元激活可预测性（predictivity）
   
b) ReLU^2 的优势：
   - 产生高稀疏性（约 90%）
   - 神经元激活模式高度可预测（可以用轻量预测器提前判断）
   - 硬件友好：激活模式利于 GPU 稀疏计算优化

c) 关键公式：ReLU^2(x) = (max(0, x))^2
   - 与 ReLU 相比：平方操作进一步抑制小正值，增强稀疏性
   - 与 SwiGLU 相比：更简单、更稀疏、硬件效率更高

## 3. 与其他方法对比
| 方法 | 优点 | 缺点 | 稀疏度 |
|------|------|------|--------|
| ReLU | 天然稀疏 | 性能略低于 GELU/SwiGLU | ~85% |
| GELU/SiLU | 平滑、性能好 | 无严格零输出，不利于稀疏加速 | ~0% |
| SwiGLU | 当前最佳性能 | 门控结构复杂，不稀疏 | ~0% |
| **ReLU^2** | **高稀疏 + 高性能** | **需要重新训练或微调** | **~90%** |

## 4. 实验表现
- 在多个 LLM 规模上验证，ReLU^2 以极低性能损失（<0.1%）实现约 90% 的激活稀疏度
- 推理时可大幅减少 FLOPs 和内存带宽需求
- 神经元激活可预测性优于其他函数，利于预测式稀疏推理

## 5. 对 Channel Mixer 的意义
这篇论文挑战了 SwiGLU 作为唯一"最优"激活函数的地位，指出在推理效率至关重要的场景下，ReLU^2 是更好的选择。这为 FFN 设计开辟了"性能-效率"权衡的新维度：训练时追求质量，推理时追求稀疏性。

## 6. 总结
a) 核心思想：Squared ReLU 兼顾性能与激活稀疏性（16字）
b) 速记 pipeline：
   1. 定义广义稀疏性度量（含小值神经元）
   2. 系统评估各激活函数的稀疏性和可预测性
   3. 发现 ReLU^2 在稀疏度约 90% 时性能损失最小
   4. 利用可预测性构建轻量预测器跳过不活跃神经元
