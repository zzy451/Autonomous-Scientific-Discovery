# Peng et al. 2025 - RWKV-7 "Goose" with Expressive Dynamic State Evolution

**论文信息**
- 标题: RWKV-7 "Goose" with Expressive Dynamic State Evolution
- 作者: Bo Peng et al.
- 年份: 2025
- arXiv: 2503.14456

## 0. 摘要翻译
我们提出RWKV-7（代号Goose），引入动态状态演化机制。核心创新包括：广义Delta规则用于状态更新、向量值门控、上下文内学习率、以及松弛值替换规则。这些改进使RWKV-7在保持线性复杂度的同时，显著提升了表达能力和在上下文学习(ICL)方面的能力。

## 1. 方法动机
a) **为什么提出**: RWKV-6的状态更新（简单的外积加法）表达能力仍有限
b) **现有方法痛点**: 
   - 简单的additive外积更新不够灵活
   - 线性RNN模型在ICL（in-context learning）上弱于Transformer
   - 需要更强的状态更新规则
c) **研究假设**: Delta规则（从联想记忆理论而来）可以提供更精确的状态更新

## 2. 方法设计
a) **方法流程**:
   - 使用广义Delta规则进行状态更新
   - Delta规则先"擦除"旧的关联再"写入"新的，比简单外积加法更精确
   - 向量值门控控制每个维度的衰减
   - 上下文内学习率(in-context learning rate)

b) **模块功能**:
   - **广义Delta规则**: $S_t = S_{t-1} - \alpha_t (S_{t-1} k_t - v_t) k_t^T$
     - 先用 $S_{t-1} k_t$ 读取旧值
     - 计算误差 $S_{t-1} k_t - v_t$
     - 按学习率 $\alpha_t$ 更新
   - **向量值门控**: 衰减向量而非标量，每个维度独立衰减
   - **In-context learning rate**: $\alpha_t$ 由输入动态生成
   
c) **公式解释**:
   - Delta规则来自Widrow-Hoff学习规则，是联想记忆的最优更新
   - 相比外积加法: 外积加法→干扰叠加; Delta规则→最小干扰更新
   - 状态作为key-value联想记忆矩阵

## 3. 与其他方法对比
a) **本质不同**: 使用Delta规则的状态更新（vs RWKV-6的简单外积加法; vs Gated Delta Networks的类似思想）
b) **创新点**: 
   - 广义Delta规则 + 松弛值替换
   - 向量值门控（比标量门控更精细）
   - 上下文内学习率
c) **适用场景**: 需要强ICL能力的线性复杂度模型
d) **对比表格**:

| 特性 | RWKV-6 | RWKV-7 | GDN |
|------|--------|--------|-----|
| 状态更新 | 外积加法 | Delta规则 | Delta规则 |
| 门控 | 标量 | 向量 | 矩阵(Householder) |
| ICL能力 | 中等 | 强 | 强 |

## 4. 实验表现
a) **验证方式**: 语言建模、ICL任务、长上下文任务
b) **关键数据**: 在ICL和语言建模上大幅超过RWKV-6
c) **优势场景**: 需要ICL的任务、长序列
d) **局限性**: 实现复杂度增加

## 5. 学习与应用
a) **开源情况**: 完全开源
b) **实现细节**: 基于Triton的高效实现
c) **迁移可能性**: RWKV系列最新版，社区持续支持

## 6. 总结
a) **一句话概括**: 通过广义Delta规则实现更精确的状态更新，结合向量门控和上下文内学习率，大幅提升线性RNN的表达能力和ICL能力
b) **速记版pipeline**: Input → 投影R,K,V,α → Delta Rule状态更新(擦除+写入) → 向量门控衰减 → Output

**Token Mixer维度**: RNN-Like方案，基于Delta规则的动态状态演化，RWKV系列最新进展
