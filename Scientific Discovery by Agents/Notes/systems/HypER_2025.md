# HypER 2025

## 基本信息
- **论文**: HypER: Literature-grounded Hypothesis Generation and Distillation with Provenance
- **作者**: Rosni Vasu, Chandrayee Basu, Bhavana Dalvi Mishra, Cristina Sarasua, Peter Clark, Abraham Bernstein
- **年份**: 2025
- **来源**: arXiv:2506.12937; EMNLP 2025
- **关键词**: hypothesis-generation, provenance, literature-grounding, reasoning-chain

## 核心思想
HypER 关注假设生成中的证据链和 provenance，避免只生成听起来合理但不可追踪的想法。

## 方法细节
系统训练小语言模型区分有效和无效科学推理链，并生成 evidence-grounded hypotheses。

## 关键结果
论文报告 HypER 在 reasoning-chain discrimination 和 evidence-grounded hypothesis quality 上优于基线。

## 局限性
不覆盖实验执行和结果分析，主要支撑早期假设形成。

## 核心贡献
将 provenance 和 reasoning validation 引入 literature-grounded hypothesis generation。

## 与综述的关联
适合放入 `X0-Y1-Z1/Z2/Z7`，支撑证据绑定的假设生成。

## 原文核对与分类复核
- **原文核对**：原文关注 literature-grounded hypothesis generation，强调 explanation、reasoning、provenance，而不是只生成最终假设。
- **机制判断**：系统支撑的是 ASD 的早期知识 grounding、假设形成和证据链构造。
- **分类复核**：保持 `ASD 相关系统`；`X0` 正确；`Y1` 可保留，因为它通过 reasoning / distillation 改善假设过程；`Z1,Z2,Z7` 正确。
- **写作用途**：支撑“假设必须携带 provenance，而不是裸生成”。

## 深读补充（按 MARS 标准）

### 研究问题
HypER 关注科学假设生成中缺少 provenance 和 reasoning trace 的问题。很多系统只输出最终假设，却无法说明假设由哪些证据和推理链支持。

### 系统架构 / 工作流
系统训练小语言模型进行 literature-guided reasoning 和 evidence-based hypothesis generation，在多任务设置中学习区分有效和无效 scientific reasoning chains。

### 关键机制
核心是 hypothesis generation with explanation and reasoning。它强调假设本身必须绑定证据来源和 reasoning process。

### 实验验证与证据
原文围绕 literature-grounded hypothesis generation 评估输出质量和 provenance，可作为假设 grounding 的证据。

### 局限性补充
HypER 主要覆盖假设形成与证据链，不处理实验执行或材料/生物学验证。

### XYZ 分类逐项解释
- `X0`：非显式多智能体。
- `Y1`：通过 reasoning / distillation 改善假设生成过程。
- `Z1,Z2,Z7`：覆盖文献 grounding、假设和验证边界。

### 综述写作用法
适合说明 ASD 中的 hypothesis artifact 必须携带 provenance，而不是裸 claim。
