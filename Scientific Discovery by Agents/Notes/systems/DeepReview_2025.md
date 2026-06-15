# DeepReview 2025

## 基本信息
- **论文**: DeepReview: Improving LLM-based Paper Review with Human-like Deep Thinking Process
- **作者**: Minjun Zhu, Yixuan Weng, Linyi Yang, Yue Zhang
- **年份**: 2025
- **来源**: arXiv:2503.08569; ACL 2025
- **关键词**: paper-review, structured-review, evidence-based-argumentation

## 核心思想
DeepReview 用结构化多阶段流程提升 LLM-based paper review 的可靠性。

## 方法细节
系统结合 structured analysis、literature retrieval 和 evidence-based argumentation，并训练 DeepReviewer。

## 关键结果
论文报告 DeepReviewer 在与 GPT-o1 和 DeepSeek-R1 的评估中取得高 win rates。

## 局限性
审稿质量不等于科学发现验证，仍是评审辅助。

## 核心贡献
将 evidence-based structured review 引入自动科学评估。

## 与综述的关联
适合放入 `X0-Y1-Z7`，支撑 verification / review layer。

## 原文核对与分类复核
- **原文核对**：原文提出 multi-stage framework，模拟 expert reviewers 的 structured analysis、literature retrieval 和 evidence-based argumentation。
- **机制判断**：这是科学评审系统，支撑 ASD 输出进入 review / validation，而不是发现系统本身。
- **分类复核**：保持 `ASD 相关系统`；`X0` 正确；`Y1` 正确；`Z7` 正确。
- **写作用途**：适合作为科学输出审查和 evidence-based review 的系统案例。

## 深读补充（按 MARS 标准）

### 研究问题
DeepReview 关注 LLM-based paper review 缺乏领域深度、推理幻觉和结构化评价不足的问题。

### 系统架构 / 工作流
系统采用 multi-stage framework，模拟 expert reviewers 的 structured analysis、literature retrieval 和 evidence-based argumentation。

### 关键机制
核心是 human-like deep thinking process 和 evidence-based review。

### 实验验证与证据
原文构建 DeepReview-13K，并训练 DeepReviewer-14B，在多个评审对比中取得较高 win rate。

### 局限性补充
DeepReview 是 review system，不是 discovery system；评审质量仍需 claim grounding 和人类专家校准。

### XYZ 分类逐项解释
- `X0`：非显式多智能体。
- `Y1`：structured critique / review 属于反思修正。
- `Z7`：支撑科学输出验证和评审。

### 综述写作用法
适合 verification / review 小节。
