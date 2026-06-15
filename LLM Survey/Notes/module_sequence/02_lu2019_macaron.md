# Understanding and Improving Transformer From a Multi-Particle Dynamic System Point of View (Macaron Net)
**作者**: Yiping Lu, Zhuohan Li, Jian He, Weize Chen, Zhuo Li, Jie Tang | **年份**: 2019 | **arxiv**: 1906.02762

## 0. 摘要翻译
本文从多粒子动力学系统的角度理解和改进 Transformer。作者将 Transformer 的自注意力子层解释为对流-扩散方程中的"扩散"项（表征粒子间交互），将 FFN 子层解释为"对流"项。标准 Transformer 使用 Lie-Trotter 分裂方案来近似 ODE 求解，而作者提出使用更高阶精度的 Strang-Marchuk 分裂方案，从而得到 FFN-Attention-FFN 的 "Macaron" 结构。

## 1. 方法动机
- Transformer 的理论理解不足，缺乏系统性的数学分析框架
- 标准 Transformer 的 Attn-FFN 交替结构是否最优？是否有数学上更好的排列方式？
- 数值 ODE 领域已有成熟的分裂方案理论，可以借鉴

## 2. 方法设计（重点：模块排列顺序及其理论分析）

### ODE 视角
- 将 Transformer 视为对流-扩散方程的数值求解器
- **自注意力 = 扩散项**：描述 token 之间的信息交互
- **FFN = 对流项**：描述各 token 的独立非线性变换

### 标准 Transformer（Lie-Trotter 分裂）
- 结构：`Attn -> FFN -> Attn -> FFN -> ...`
- 对应一阶精度的 Lie-Trotter 分裂方案
- 局部截断误差较大

### Macaron Net（Strang-Marchuk 分裂）
- 结构：`FFN(1/2) -> Attn -> FFN(1/2) -> FFN(1/2) -> Attn -> FFN(1/2) -> ...`
- 其中 FFN(1/2) 表示"半步" FFN（参数量为完整 FFN 的一半）
- 对应三阶精度的 Strang-Marchuk 分裂方案
- **保持总参数量不变**：两个半步 FFN 的参数量之和等于一个完整 FFN

### 关键设计
- 每个 Macaron 块：`FFN_half -> Attn -> FFN_half`
- 类似"三明治"结构，FFN 夹住 Attention
- 数学上具有更低的局部截断误差

## 3. 与其他方法对比
| 方法 | 结构 | 理论基础 | 精度阶数 |
|------|------|---------|---------|
| 标准 Transformer | Attn-FFN | Lie-Trotter 分裂 | 一阶 |
| Macaron Net | FFN(1/2)-Attn-FFN(1/2) | Strang-Marchuk 分裂 | 三阶 |

- Macaron Net 在参数量相同的条件下获得更好的性能
- 后续被 Conformer（语音识别）等模型采用

## 4. 实验表现
- **机器翻译**：在保持参数量不变的情况下，Macaron Net 始终优于标准 Transformer
- **监督学习与无监督学习任务**：均观察到一致的性能提升
- 改进来源于更精确的 ODE 数值求解，而非简单的参数量增加

## 5. 总结
a) **一句话概括**：从 ODE 数值求解角度推导出 FFN-Attn-FFN 的 "Macaron" 结构，数学上比标准 Attn-FFN 具有更高的近似精度。

b) **速记 pipeline**：`Input -> [FFN_half -> Attn -> FFN_half] x L -> Output`
