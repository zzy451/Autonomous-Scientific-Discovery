# Code2Math 2026

## 基本信息

- **论文**: Code2Math: Can Your Code Agent Effectively Evolve Math Problems Through Exploration?
- **年份**: 2026
- **来源**: arXiv:2603.03202
- **系统名称**: Code2Math
- **关键词**: mathematical problem generation, code agent, evolutionary exploration, solvability verification, difficulty verification

## 摘要要点

Code2Math 研究 code agent 是否能通过探索和验证来演化数学问题。系统包含 Evolution Agent、Solvability Verification Agent 和 Difficulty Verification Agent，通过代码执行与验证反馈改进数学题目 artifact。它不是严格 ASD 系统，而是 artifact-level evolution 的边界证据：演化对象是数学问题，而非实验假设或自然科学发现。

## 方法动机

数学问题生成常见失败包括：生成的问题不可解、难度不符合目标、解法依赖错误条件，或只是表面改写而缺少有效探索。作者的核心问题是：能否让代码执行成为数学题生成的反馈信号，使问题生成从文本变换升级为可验证的 artifact evolution。

## 方法设计

Code2Math 的方法流程如下：

1. 给定目标类型、主题或难度要求。
2. Evolution Agent 生成初始数学问题，并对问题进行变异或探索。
3. Code agent 将问题中的条件、计算或构造转化为可执行程序。
4. Solvability Verification Agent 检查问题是否有解、约束是否一致。
5. Difficulty Verification Agent 判断题目难度是否符合目标区间。
6. 根据验证反馈继续修改题目，保留更合格的候选。

系统的关键是把 code execution 当作可操作的验证器，让数学题目在多轮探索中逐渐变得可解、可控且有挑战性。

## 与其他方法的区别

| 方法类型 | 特点 | Code2Math 的改进 |
|---|---|---|
| 直接 LLM 生成题目 | 快速但不可控，容易不可解 | 加入可解性和难度验证 |
| 规则模板生成 | 稳定但缺少多样性 | 用 Evolution Agent 扩展候选空间 |
| 纯人工命题 | 质量高但成本高 | 让 agent 进行候选探索和自动检查 |

## 实验与结果

论文围绕数学题生成质量评估 Code2Math，重点检查生成问题的可解性、难度匹配和多样性。其结果表明，加入 verification agents 与 code execution 后，系统比直接生成更能控制题目质量。

## 局限性

- 产物是数学题生成，不等于研究级数学发现。
- 代码验证能检查部分可解性，但不能完全替代数学证明。
- 如果难度评价器本身不可靠，演化方向可能偏离目标。

## XYZ 分类

| 维度 | 标注 | 理由 |
|---|---|---|
| X | `X2` | Evolution、Solvability Verification、Difficulty Verification 是固定角色 |
| Y | `Y4` | 使用 evolution / exploration 改进数学问题 artifact |
| Z | `Z2,Z3,Z4,Z7,Z8` | 覆盖问题生成、可执行表示、代码执行验证和迭代 |

## 对综述的价值

Code2Math 可用于第 5 章说明 artifact evolution 的对象可以是数学问题、代码、证明草图或实验设计，而不只是假设文本。正文中应把它作为 ASD 相关系统和边界案例，而不是严格科学发现系统。

