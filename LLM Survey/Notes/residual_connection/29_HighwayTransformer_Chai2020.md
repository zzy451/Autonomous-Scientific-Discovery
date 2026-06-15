# Highway Transformer: Self-Gating Enhanced Self-Attentive Networks

**论文信息**: Chai, Y., Jin, S., Hou, X. (2020)
**arXiv**: 2004.08178 | **会议**: ACL 2020
**分类**: Control (门控残差连接)

## 核心思想
Highway Transformer 借鉴 Highway Networks 和 LSTM 的门控思想，在 Transformer 的残差连接中引入 **Self-Dependency Units (SDU)**，作为内容依赖的门控机制来调制残差流中的信息传递。

## 数学公式
标准残差: x_{l+1} = x_l + F(x_l)
Highway Transformer: x_{l+1} = g(x_l) * x_l + (1 - g(x_l)) * F(x_l)

其中 g(x_l) 是 SDU 生成的门控信号，类似 LSTM 的 gate:
- g 接近 1: 信息直接通过（highway）
- g 接近 0: 子层输出占主导

## 关键机制
- **Self-Dependency Units (SDU)**: LSTM 风格的门控单元，基于当前输入内容生成门控信号
- **伪信息高速公路**: SDU 创建的门控路径，选择性地让信息通过或被变换
- **内容依赖**: 门控权重不是固定的，而是根据每个 token 的表示动态计算
- **训练收敛加速**: 门控机制帮助模型更快找到优化方向

## 与 Highway Networks 的关系
- Highway Networks (2015): 在 CNN 中引入可学习门控的跳跃连接
- Highway Transformer: 将同一思想迁移到 Transformer 的自注意力架构中
- 增加了"自依赖"维度：门控信号基于输入自身的语义重要性

## 实验结果
- 在机器翻译等 NLP 任务上提升了收敛速度
- 浅层网络中优势更明显（门控帮助早期优化）

## 与综述的关联
属于 **Control** 维度。是门控残差连接在 Transformer 中的典型应用。与 GTrXL 的门控残差思路相似，但 SDU 更偏向 LSTM 风格的门控，而 GTrXL 使用的是 GRU 风格的门控。

## 与其他 Control 方法对比
| 方法 | 控制方式 | 控制粒度 | 额外参数 |
|------|----------|----------|----------|
| ReZero | 标量 alpha | 全局标量 | 1个标量/层 |
| DeepNorm | 固定缩放 | 全局固定 | 0 |
| Highway Transformer | 门控向量 | 逐维度 | 门控网络 |
| GTrXL | 门控向量 | 逐维度 | GRU 门 |

## 核心贡献
将 Highway Network 的门控残差思想引入 Transformer，通过 SDU 实现内容依赖的逐维度残差流控制。
