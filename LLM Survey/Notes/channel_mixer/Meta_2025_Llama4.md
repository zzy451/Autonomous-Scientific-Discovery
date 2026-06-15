# Llama 4: Architecture, Training, Evaluation, and Deployment Notes

**论文**: The Llama 4 Herd of Models
**作者**: Meta AI
**年份**: 2025
**来源**: arXiv:2601.11659
**标签**: MoE, 原生多模态, 早融合, 超长上下文

---

## 0. 摘要
Llama 4 是 Meta 于 2025 年 4 月发布的多模态 MoE 模型系列，包括 Scout（16专家）、Maverick（128专家）和 Behemoth（预览）。首次在 Llama 系列中采用 MoE 架构，支持原生多模态（文本+图像）早融合，Scout 支持高达 1000 万 token 的上下文窗口。

## 1. 方法动机
a) Llama 3 是纯 Dense 架构，推理成本随参数量线性增长。
b) 需要原生多模态能力而非后接适配器。
c) 超长上下文（10M tokens）需要高效的架构支撑。

## 2. 方法设计（Channel Mixer 相关）
a) MoE 配置：
   - **Scout**: 109B 总参，17B 激活，16 个专家
   - **Maverick**: 400B 总参，17B 激活，128 个专家
   - 每个 token 激活 1 个共享专家 + 1 个路由专家

b) 架构特点：
   - 交替使用 Dense 层和 MoE 层（非每层都是 MoE）
   - 共享专家处理所有 token 的通用特征
   - 路由专家处理专业化特征

c) 多模态早融合：
   - 图像 token 直接与文本 token 在同一序列中处理
   - 不需要额外的跨模态适配器

d) 激活函数：SwiGLU

## 3. 与其他 MoE 模型对比
| 模型 | 总参/激活参 | 专家数 | 共享专家 | 多模态 | 最大上下文 |
|------|------------|--------|---------|--------|-----------|
| DeepSeek-V3 | 671B/37B | 256 | 有 | 无 | 128K |
| Qwen3 MoE | 235B/22B | 128 | 无 | 无 | - |
| **Llama 4 Scout** | **109B/17B** | **16** | **有** | **原生** | **10M** |
| **Llama 4 Maverick** | **400B/17B** | **128** | **有** | **原生** | **1M** |

## 4. 对 Channel Mixer 的意义
Llama 4 展示了 MoE 与多模态早融合的结合方式。交替 Dense/MoE 层的设计是一种折中方案，在效率和表达能力之间取得平衡。iRoPE（交替 RoPE/NoPE）配合 MoE 实现了 10M 级别的超长上下文。

## 5. 总结
a) 核心思想：MoE+原生多模态早融合+交替Dense/MoE层（18字）
b) 速记 pipeline：共享专家+路由专家 → Dense/MoE交替 → 多模态早融合 → 10M上下文
