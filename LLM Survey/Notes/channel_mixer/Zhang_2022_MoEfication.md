# MoEfication: Transformer Feed-forward Layers are Mixtures of Experts

**论文**: MoEfication: Transformer Feed-forward Layers are Mixtures of Experts
**作者**: Zhengyan Zhang, Yankai Lin, Zhiyuan Liu, Peng Li, Maosong Sun, Jie Zhou
**年份**: 2022
**来源**: Findings of ACL 2022
**标签**: Dense-to-MoE, FFN, 稀疏化, 推理加速

---

## 0. 摘要
本文提出 MoEfication 方法，将预训练好的密集 Transformer 模型的 FFN 层转换为 MoE 结构。核心发现：密集 FFN 层中的神经元天然地形成功能性分组（clusters），这些分组可以被视为"隐式专家"。通过显式化这种结构并添加路由器，可以在只使用 10-30% FFN 参数的条件下保持 95%+ 的原始性能。

## 1. 方法动机
a) 预训练大型密集模型已经消耗了大量计算资源，从头训练 MoE 模型代价更高。
b) 密集模型的 FFN 层在推理时存在高稀疏性，许多神经元不被激活。
c) 假设：FFN 层中的神经元可以按照共同激活模式分组，形成"天然专家"。

## 2. 方法设计
a) 两阶段流程：
   **阶段一：专家构建（Expert Construction）**
   - 收集大量输入下各神经元的激活统计
   - 使用聚类算法（如 k-means）将神经元按共同激活模式分组
   - 每组神经元构成一个"专家"

   **阶段二：专家选择（Expert Selection）**
   - 训练轻量级路由器（router）
   - 路由器基于输入决定激活哪些专家
   - 使用知识蒸馏或微调恢复性能

b) 关键洞察：
   - FFN 的神经元确实存在明显的功能分组
   - 同一组内的神经元倾向于在相似的输入上共同激活
   - 这与 MoE 中"专家专业化"的直觉一致

## 3. 与其他方法对比
| 方法 | 优点 | 缺点 | 改进点 |
|------|------|------|--------|
| 从头训练 MoE | 充分优化 | 计算代价极高 | - |
| 静态剪枝 | 简单 | 精度损失大 | - |
| Deja Vu | 无需修改模型 | 需要在线预测 | - |
| **MoEfication** | **利用已训练模型** | **需要聚类+微调** | **发现天然专家结构** |

## 4. 实验表现
- 在 BERT 和 GPT-2 等模型上验证
- 使用 10-30% 的 FFN 参数即可保持 95%+ 性能
- 推理速度提升显著（减少 70-90% 的 FFN 计算）
- 验证了"FFN 层本身就是隐式 MoE"的假说

## 5. 对 Channel Mixer 的意义
MoEfication 提供了密集 FFN 和 MoE 之间的桥梁。它证明：
- 密集 FFN 天然具有类 MoE 的内部结构
- MoE 可以被视为"显式化"了密集 FFN 中的隐式专家分组
- 这为理解 Channel Mixer 的本质提供了重要的理论视角

## 6. 总结
a) 核心思想：密集FFN神经元天然分组可转换为MoE结构（20字）
b) 速记 pipeline：
   1. 统计密集 FFN 各神经元的激活模式
   2. 按共同激活模式聚类神经元形成"专家"
   3. 训练路由器动态选择少量专家
   4. 微调恢复性能，实现 70-90% 参数节省
