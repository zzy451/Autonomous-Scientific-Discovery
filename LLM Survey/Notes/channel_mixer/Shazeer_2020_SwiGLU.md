# GLU Variants Improve Transformer

**论文**: GLU Variants Improve Transformer
**作者**: Noam Shazeer
**年份**: 2020
**来源**: arXiv:2002.05202 (Google)
**标签**: SwiGLU, GeGLU, ReGLU, GLU 变体, Transformer FFN

---

## 0. 摘要
本文将门控线性单元（GLU）的思想引入 Transformer FFN 层，用不同激活函数替换原始 GLU 中的 sigmoid 门控，提出了多种 GLU 变体：ReGLU、GEGLU、SwiGLU 等。实验表明这些 GLU 变体在机器翻译和语言建模任务上一致优于标准 Transformer FFN（ReLU/GELU），其中 SwiGLU 和 GEGLU 表现最佳。

## 1. 方法动机
a) 标准 Transformer FFN 为两层 MLP：FFN(x) = act(xW₁)W₂，其中 act 通常为 ReLU 或 GELU。
b) Dauphin et al. 2017 提出的 GLU 使用 sigmoid 门控实现信息选择，但未在 Transformer 中系统测试。
c) 假设：将 GLU 的门控机制引入 Transformer FFN，并用更强的激活函数替换 sigmoid，可以提升模型性能。

## 2. 方法设计
a) 标准 FFN vs GLU 变体：
   - 标准 FFN：FFN(x, W₁, W₂) = act(xW₁) · W₂
   - GLU 变体：GLU(x, W, V, W₂) = (act(xW) ⊗ xV) · W₂
   
   关键区别：GLU 变体引入第三个权重矩阵 V，输入同时通过两路线性变换，一路经激活函数后与另一路逐元素相乘。

b) 具体变体（按激活函数分类）：
   - GLU：σ(xW) ⊗ xV（原始 sigmoid 门控）
   - ReGLU：ReLU(xW) ⊗ xV
   - GEGLU：GELU(xW) ⊗ xV
   - SwiGLU：Swish(xW) ⊗ xV = (xW · σ(xW)) ⊗ xV

c) 参数量调整：
   - GLU 变体有 3 个矩阵（W, V, W₂），标准 FFN 有 2 个（W₁, W₂）
   - 为公平对比，将 GLU 变体的隐藏维度从 4d 缩减为 8d/3 ≈ 2.67d
   - 保持总参数量大致相同

## 3. 与其他方法对比
| 方法 | 公式 | 参数矩阵数 | 性能 |
|------|------|------------|------|
| FFN-ReLU | ReLU(xW₁)W₂ | 2 | 基线 |
| FFN-GELU | GELU(xW₁)W₂ | 2 | 略优于 ReLU |
| ReGLU | (ReLU(xW) ⊗ xV)W₂ | 3 | 优于 FFN |
| GEGLU | (GELU(xW) ⊗ xV)W₂ | 3 | 优于 FFN |
| **SwiGLU** | **(Swish(xW) ⊗ xV)W₂** | **3** | **最优之一** |

## 4. 实验表现
- 在 T5 架构上进行实验（encoder-decoder Transformer）
- 机器翻译（WMT）和语言建模（C4 数据集）任务
- SwiGLU 和 GEGLU 在困惑度上一致优于 ReLU/GELU 基线
- 即使在参数量匹配的条件下，GLU 变体仍有明显优势
- 作者坦言"没有理论解释为什么这些变体更好"

## 5. 对 Channel Mixer 的意义
本文是现代 LLM FFN 设计的奠基性工作。SwiGLU 已成为事实上的标准 channel mixer 激活方案，被 LLaMA、PaLM、Mistral、Qwen、DeepSeek 等几乎所有主流 LLM 采用。GLU 变体的核心思想——用门控机制让网络学习"选择性传递信息"——定义了当代 channel mixer 的基本范式。三矩阵结构（W, V, W₂）配合 8d/3 隐藏维度也成为标准配置。

## 6. 总结
a) 核心思想：用激活函数变体门控实现 FFN 信息选择（16字）
b) 速记 pipeline：
   1. 输入 x 同时通过两个线性变换 xW 和 xV
   2. 一路经激活函数（Swish/GELU/ReLU）
   3. 两路逐元素相乘实现门控选择
   4. 结果通过输出投影 W₂，SwiGLU 成为 LLM 标准 FFN
