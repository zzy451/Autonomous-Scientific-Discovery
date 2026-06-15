# N-29: Enhanced QKNorm with Lp Norm (Lopez-Rubio et al. 2026)

> **论文**: Enhanced QKNorm normalization for neural transformers with the Lp norm
> **作者**: Ezequiel Lopez-Rubio, Javier Montes-Perez, Esteban Jose Palomo
> **发表**: arXiv:2602.05006 (2026)
> **关键词**: QKNorm, Lp 范数, 注意力归一化, 非欧几何, nanoGPT

---

## 核心思想

将 QK-Norm (Henry et al. 2020) 中的标准 L2 归一化推广为 **Lp 归一化**，探索不同 p 值对注意力几何和模型性能的影响。实验表明 Transformer 的注意力机制不一定需要欧几里得 (L2) 归一化，不同的 p 值可以产生不同的收敛速度和验证损失。

## 方法

### 从 QK-Norm 到 Lp-QK-Norm

**标准 QK-Norm (Henry 2020)**:
$$\hat{Q} = \frac{Q}{\|Q\|_2}, \quad \hat{K} = \frac{K}{\|K\|_2}$$

**Enhanced QKNorm (本文)**:
$$\hat{Q} = \frac{Q}{\|Q\|_p}, \quad \hat{K} = \frac{K}{\|K\|_p}$$

其中 $\|x\|_p = \left(\sum_i |x_i|^p\right)^{1/p}$

### 设计动机

- QK-Norm 通过将 Q, K 归一化来解耦幅度与方向，控制注意力分数的动态范围
- L2 归一化只是一种特殊选择，不同的 p 值定义了不同的注意力几何
- 探索 p 值对训练稳定性和性能的影响

### 实验设置

| 配置项 | 值 |
|--------|-----|
| 框架 | nanoGPT (Karpathy) |
| 架构 | Decoder-only, Pre-Norm |
| 层数 | 6 |
| 注意力头 | 6 |
| 嵌入维度 | 384 |
| Dropout | 0.2 |
| 上下文长度 | 256 |
| 数据集 | Tiny Shakespeare (65 字符词表) |
| p 值 | {1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0} |

## 关键发现

1. **L2 非唯一选择**: 欧几里得归一化 (p=2) 不是注意力机制成功运行的必要条件
2. **连续行为变化**: 随着 p 值变化，模型行为连续平滑变化，表明 Lp 归一化是一个稳定的设计空间
3. **潜在改进**: 某些 p 值可以产生比标准 L2 更好的验证损失和收敛速度
4. **几何多样性**: 不同 p 值对应不同的注意力空间几何，为架构设计提供了新的自由度

## 局限

1. **小规模实验**: 仅在 nanoGPT/Tiny Shakespeare 上验证，缺乏大规模 LLM 验证
2. **单一任务**: 仅语言建模任务，未覆盖翻译、分类等下游任务
3. **工程意义有限**: 当前结论对大规模工业应用的指导价值待验证
4. **缺乏理论分析**: 为什么某些 p 值更优缺乏理论解释

## 在综述中的定位

本文是 QK-Norm 方向的**前沿探索性工作**，将注意力归一化的设计空间从固定的 L2 扩展到 Lp 族。虽然实验规模有限，但其核心贡献在于指出：注意力归一化的几何选择不是唯一的，Lp 范数提供了一个连续的设计谱。

与 Henry 2020 (N-10) 的关系：N-10 提出 QK-Norm 概念，本文将其推广到非欧几何。
与 nGPT (N-25) 的关系：nGPT 也探讨了归一化的几何含义，但聚焦于全面 L2 归一化。

---

**阅读日期**: 2026-04-05
