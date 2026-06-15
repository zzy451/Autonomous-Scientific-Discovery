# CLAIMCHECK 2025

## 基本信息
- **论文**: CLAIMCHECK: How Grounded are LLM Critiques of Scientific Papers?
- **作者**: Jiefu Ou, William Gantt Walden, Kate Sanders, Zhengping Jiang, Kaiser Sun, Jeffrey Cheng, William Jurayj, Miriam Wanner, Shaobo Liang, Candice Morgan, Seunghoon Han, Weiqi Wang, Chandler May, Hannah Recknor, Daniel Khashabi, Benjamin Van Durme
- **年份**: 2025
- **来源**: arXiv:2503.21717; EMNLP Findings 2025
- **关键词**: claim-verification, peer-review, scientific-critique, grounding

## 核心思想
CLAIMCHECK 关注 LLM 科学论文 critique 是否真正 grounded in paper claims。

## 方法细节
数据集将 review weakness statements 与被质疑的 paper claims 对齐，并支持 claim-centric verification tasks。

## 关键结果
论文显示前沿 LLM 在 grounded critique 和 claim verification 上仍显著落后于专家。

## 局限性
主要是评测资源和验证任务，不是 discovery system。

## 核心贡献
为科学审稿和声明验证提供 claim-grounded 评估基础。

## 与综述的关联
不再放入 XYZ 主矩阵；适合作为第 7 章 verification / benchmark 的补充材料，说明 LLM critique 的 groundedness 仍需独立评估。

## 原文核对与分类复核
- **原文核对**：原文是 CLAIMCHECK 数据集和 benchmark，评估 LLM critique 是否 grounded in paper claims。
- **机制判断**：它不是 ASD 系统，而是 claim-centric review / verification benchmark。
- **分类复核**：已从 XYZ 主矩阵中移出；仍可作为第 7 章 verification / benchmark 的补充引用。
- **写作用途**：用于说明 LLM critique 仍弱于人类专家，不能作为多智能体系统主证据。

## 深读补充（按 MARS 标准）

### 研究问题
CLAIMCHECK 关注 LLM 自动生成的科学论文 critique 是否真正 grounded in paper claims。自动审稿看似合理，但可能没有对应具体 claim。

### 系统架构 / 工作流
论文构建 NeurIPS submission/review 数据集，标注 review weakness statements、被质疑的 paper claims，以及 validity、objectivity 和 type 标签。

### 关键机制
核心是 claim-centric verification benchmark，而不是发现系统。任务包括关联 weakness 与 claim、预测标签、重写 weakness、验证 paper claims。

### 实验验证与证据
原文显示前沿 LLM 在多个 claim-grounding 任务上仍弱于人类专家。

### 局限性补充
它不是 ASD 系统，也不是 ASD 相关 workflow；但对 verification / review 章节非常重要。

### XYZ 分类逐项解释
- 已移出 XYZ 主矩阵。
- 可作为 `Z7` verification benchmark 补充材料。

### 综述写作用法
用于提醒：critic/reviewer agents 的输出必须做 claim grounding，不能把 review text 当作可靠验证。
