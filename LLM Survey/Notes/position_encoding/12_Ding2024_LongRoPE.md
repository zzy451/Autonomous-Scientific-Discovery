# LongRoPE: Extending LLM Context to 2M Tokens
**论文**: LongRoPE: Extending LLM Context Window Beyond 2 Million Tokens
**作者**: Yiran Ding, Li Lyna Zhang, Chengruidong Zhang, Yuanyuan Xu, Ning Shang, Jiahang Xu, Fan Yang, Mao Yang
**年份**: 2024
**会议**: ICML 2024 (Microsoft Research)
**arXiv**: 2402.13753

## 核心思想
LongRoPE 通过利用位置插值中的非均匀性（跨 RoPE 维度和 token 位置），结合渐进式扩展策略和短上下文恢复技术，将 LLM 的上下文窗口扩展到 2,048,000 tokens。

## 方法细节

### 三大技术创新

#### 1. 利用非均匀性的搜索
- RoPE 不同维度的最优缩放因子并不相同（PI 假设均匀是次优的）
- 不同 token 位置对插值的敏感度不同
- 通过高效搜索算法（进化搜索）找到每个维度的最优缩放因子
- 无需 fine-tuning 即可实现 8x 扩展

#### 2. 渐进式扩展策略 (Progressive Extension)
两步走策略：
1. **第一步**: Fine-tune 到 256k 上下文长度（使用可获取的长文本）
2. **第二步**: 基于 256k 模型进行第二次位置插值，搜索最优因子，扩展到 2048k

好处：
- 避免了对极长训练文本（2M tokens）的需求
- 分步扩展比一步到位更稳定

#### 3. 短上下文恢复 (Short-Context Recovery)
- 长上下文扩展后，短上下文（如 8k）性能可能下降
- 专门为短长度重新调整缩放因子
- 使用短序列重新搜索最优因子
- 维护两套缩放因子：长上下文和短上下文

### 搜索空间
- 搜索每个 RoPE 维度的独立缩放因子
- 使用困惑度作为搜索目标
- 进化搜索 + 贪心优化

## Position Encoding 维度分析

### 分类
- **类型**: RoPE 扩展方法（搜索优化类）
- **注入方式**: 修改 RoPE 各维度的缩放因子
- **参数量**: 无额外可训练参数（缩放因子通过搜索确定）
- **长度外推**: 迄今最长（2M tokens）

### 与前序工作的关系
| 方法 | 缩放策略 | 最大扩展 | Fine-tuning |
|------|---------|---------|------------|
| PI | 均匀缩放 | ~8x | 需要 |
| NTK-aware | 按频率缩放 | ~8x | 可选 |
| YaRN | 分区域缩放 | ~32x | 需少量 |
| LongRoPE | 逐维度搜索 | ~1000x | 需要 |

### 关键洞察
1. 最优缩放因子的非均匀性是可利用的
2. 搜索方法可以找到比人工设计更好的缩放方案
3. 短上下文恢复是长度扩展中被忽视的重要问题

## 实验结果
- Phi-3 系列模型集成了 LongRoPE
- 2M context passkey retrieval 成功
- 短上下文任务保持原始性能
- 在多个长上下文 benchmark 上 SOTA

## 影响
- 将 RoPE 扩展推向极致（百万级 context）
- 被 Microsoft 的实际产品模型采用
- 表明搜索/自动化方法在 PE 设计中的价值
