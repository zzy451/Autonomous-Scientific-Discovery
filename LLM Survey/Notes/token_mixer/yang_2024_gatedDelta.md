# Yang et al. 2024 - Gated Delta Networks: Improving Mamba2 with Delta Rule

**论文信息**
- 标题: Gated Delta Networks: Improving Mamba2 with Delta Rule
- 作者: Songlin Yang, Jan Kautz, Ali Hatamizadeh (NVIDIA)
- 年份: 2024
- arXiv: 2412.06464

## 0. 摘要翻译
线性Transformer和状态空间模型使用固定大小的递归状态实现恒定的推理开销。然而，当新的key-value关联与已存储的信息冲突时，简单的additive外积更新会导致记忆退化。我们提出Gated Delta Networks，结合Delta规则的精确记忆更新和门控机制，在Mamba2框架上实现显著的性能提升。

## 1. 方法动机
a) **为什么提出**: 线性Transformer/SSM的外积加法状态更新（$S_t = \alpha S_{t-1} + k_t v_t^T$）会导致灾难性遗忘
b) **现有方法痛点**: 
   - 当新的kv对与旧的kv对的key相似但value不同时，简单累加会导致干扰
   - Mamba2虽快但状态更新缺乏精确性
   - 检索任务上线性模型远弱于Transformer
c) **研究假设**: Delta规则可以"先擦除旧关联再写入新关联"，解决记忆冲突

## 2. 方法设计
a) **方法流程**:
   - 在Mamba2的SSD框架上替换状态更新规则
   - 使用Delta规则: $S_t = S_{t-1} - \beta_t (S_{t-1} k_t - v_t) k_t^T$
   - 添加门控机制和短卷积
   - 利用广义Householder变换实现高效并行训练
   
b) **模块功能**:
   - **Delta Rule**: 
     - 读取: $\hat{v}_t = S_{t-1} k_t$（用当前key查旧状态）
     - 误差: $e_t = v_t - \hat{v}_t$
     - 更新: $S_t = S_{t-1} + \beta_t e_t k_t^T$
   - **门控**: 输出门 $o_t = \text{sigmoid}(W_o x_t) \odot y_t$
   - **并行化**: 将Delta规则重写为矩阵值RNN，利用广义Householder变换的compact WY表示实现并行
   
c) **公式解释**:
   - Delta规则等价于在线梯度下降更新联想记忆
   - β_t: 数据依赖的"学习率"
   - Householder变换: $H = I - \beta k k^T$，Delta规则的状态转移可表示为Householder矩阵乘积

## 3. 与其他方法对比
a) **本质不同**: 将Delta规则整合到Mamba2的SSD框架中，实现精确记忆更新
b) **创新点**: 
   - 首次将Delta规则与现代SSM框架结合
   - 通过Householder变换实现高效并行训练
   - 显著提升检索和ICL能力
c) **适用场景**: 需要精确记忆/检索的任务
d) **对比表格**:

| 特性 | Mamba | Mamba2 | GDN |
|------|-------|--------|-----|
| 状态更新 | 选择性衰减+加法 | SSD(标量衰减+加法) | Delta规则 |
| 记忆冲突 | 干扰叠加 | 干扰叠加 | 先擦后写 |
| 并行化 | 扫描 | 块matmul | Householder WY |
| 检索能力 | 弱 | 弱 | 强 |

## 4. 实验表现
a) **验证方式**: 语言建模、合成检索任务、标准基准
b) **关键数据**: 
   - 1.3B模型在100B tokens上训练
   - 显著超过Mamba和Mamba2
   - 在检索密集任务上接近Transformer
c) **优势场景**: 检索密集任务（MQAR, ICL）
d) **局限性**: 并行化实现复杂

## 5. 学习与应用
a) **开源情况**: NVIDIA开源
b) **实现细节**: 基于flash-linear-attention库
c) **迁移可能性**: 可直接替换Mamba2层

## 6. 总结
a) **一句话概括**: 通过在Mamba2框架中引入Delta规则替代外积加法更新，实现"先擦后写"的精确记忆，显著提升线性模型的检索能力
b) **速记版pipeline**: Input → 投影K,V → Delta Rule(读取旧值→计算误差→更新状态) → 门控输出

**Token Mixer维度**: RNN-Like/SSM方案，Delta规则实现精确联想记忆更新，解决线性模型的记忆冲突问题
