# Gu & Dao 2024 - Mamba: Linear-Time Sequence Modeling with Selective State Spaces

**论文信息**
- 标题: Mamba: Linear-Time Sequence Modeling with Selective State Spaces
- 作者: Albert Gu, Tri Dao
- 年份: 2024 (arXiv 2023.12)
- arXiv: 2312.00752

## 0. 摘要翻译
基础模型（如LLM）的核心是序列建模。尽管Transformer及其核心注意力层无处不在，但它在序列长度上存在O(N²)的计算瓶颈。我们提出Mamba，一种新的架构，它引入了选择性状态空间模型(selective SSM)，能够基于输入内容动态调整SSM参数，从而实现内容感知的信息传播。Mamba结合了硬件感知的扫描算法，实现了线性时间复杂度的序列建模。

## 1. 方法动机
a) **为什么提出**: SSM（如S4）虽然是线性复杂度，但参数不依赖输入内容，无法进行内容感知的选择
b) **现有方法痛点**: 
   - 传统SSM（S4、H3）使用时不变参数，无法选择性地传播或遗忘信息
   - Transformer虽然能内容感知但O(N²)
   - 现有高效序列模型在语言建模上远落后于Transformer
c) **研究假设**: 让SSM的参数(B, C, Δ)依赖于输入可以实现选择性信息流

## 2. 方法设计
a) **方法流程**:
   - 输入x → 线性投影 → 通过选择性SSM处理 → 输出
   - SSM参数(B, C, Δ)由输入x动态生成（选择性机制）
   - 使用硬件感知的并行扫描算法高效计算
   
b) **模块功能**:
   - **Selective SSM**: 
     - $h_t = \bar{A}h_{t-1} + \bar{B}x_t$
     - $y_t = Ch_t$
     - $B = \text{Linear}_B(x)$, $C = \text{Linear}_C(x)$, $\Delta = \text{softplus}(\text{Linear}_\Delta(x))$
   - **离散化**: $\bar{A} = \exp(\Delta A)$, $\bar{B} = (\Delta A)^{-1}(\exp(\Delta A) - I) \cdot \Delta B$
   - **硬件感知扫描**: 在GPU SRAM中执行扫描，避免HBM访问
   - **Mamba Block**: 类似于H3，使用线性投影+SSM+门控
   
c) **公式解释**:
   - Δ大 → $\bar{A}$接近0 → 遗忘历史，关注当前输入
   - Δ小 → $\bar{A}$接近1 → 保持历史状态
   - 选择性通过输入依赖的Δ实现"何时记住、何时遗忘"

## 3. 与其他方法对比
a) **本质不同**: 时变SSM参数（选择性机制），而非时不变的线性系统
b) **创新点**: 
   - 选择性机制（input-dependent Δ, B, C）
   - 硬件感知的并行扫描实现
   - 简化架构（无注意力、无MLP，单一SSM块堆叠）
c) **适用场景**: 长序列语言建模、DNA序列分析、音频
d) **对比表格**:

| 特性 | Transformer | S4 | Mamba |
|------|-------------|----|----- |
| 复杂度 | O(N²) | O(N) | O(N) |
| 内容感知 | 是 | 否 | 是 |
| 推理 | KV cache | 递归 | 递归 |
| 推理状态 | O(N) | O(d_state) | O(d_state) |
| 训练 | 并行 | 卷积/并行 | 并行扫描 |

## 4. 实验表现
a) **验证方式**: 语言建模(The Pile)、合成任务、DNA、音频
b) **关键数据**: 
   - Mamba-3B匹配Transformer-3B（开创性结果）
   - 推理吞吐比Transformer高5倍
   - 线性扩展到百万token长度
c) **优势场景**: 长序列建模、推理效率要求高的场景
d) **局限性**: 在某些需要精确检索的任务上不如注意力；并行扫描实现复杂

## 5. 学习与应用
a) **开源情况**: 完全开源（GitHub: state-spaces/mamba）
b) **实现细节**: 状态维度N=16; 扩展因子E=2; CUDA扫描核
c) **迁移可能性**: 已衍生出Mamba-2、Jamba等后续工作

## 6. 总结
a) **一句话概括**: 通过让SSM参数依赖输入内容实现选择性信息传播，以线性复杂度在语言建模上首次匹配Transformer
b) **速记版pipeline**: Input → Linear Proj → [Selective SSM: x→Δ,B,C + 离散化 + 并行扫描] → Gate → Output

**Token Mixer维度**: RNN-Like/SSM方案，选择性状态空间模型，线性复杂度的内容感知序列建模
