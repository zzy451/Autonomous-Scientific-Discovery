# PaperOrchestra 2026

## 基本信息

- **论文**: PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing
- **年份**: 2026
- **来源**: arXiv:2604.05018
- **系统名称**: PaperOrchestra
- **关键词**: multi-agent paper writing, automated AI research paper, literature synthesis, LaTeX manuscript, automated evaluation

## 一句话总结

PaperOrchestra 是一个面向 AI research paper writing 的多智能体框架，将 unconstrained pre-writing materials 转换为 LaTeX manuscripts，并通过多角色写作、综合和评价机制支撑 reporting/synthesis。

## 研究问题

ASD 工作流最终需要把中间产物转化为可审阅、可复现、可引用的报告或论文。许多系统覆盖假设、执行和分析，但在 `Z6: Synthesis / Reporting` 上证据较少。PaperOrchestra 可以补这个薄弱环节，但不应被写成完整科学发现系统。

## 系统架构

PaperOrchestra 将论文写作拆解为多个 agent 协作阶段：

| 功能 | 作用 |
|---|---|
| Planning / structuring | 组织论文结构和章节 |
| Literature synthesis | 将相关工作和背景整合进稿件 |
| Writing agents | 生成各部分 manuscript |
| Evaluation agents | 评价稿件质量并触发修正 |
| LaTeX output | 生成结构化论文产物 |

## XYZ 分类

建议分类为：

| 维度 | 标注 | 理由 |
|---|---|---|
| X | `X2` | 多个固定写作/评价角色 |
| Y | `Y1` | 主要是评价与修正，不是明确演化搜索 |
| Z | `Z1,Z6,Z7` | 覆盖文献综合、论文写作和评价 |

建议放入 **ASD 相关系统**，只作为 reporting/synthesis 支撑。

## 对综述的价值

PaperOrchestra 可以补 `X2-Y1-Z6`。它适合放在第 6/7 章讨论 research artifact 的 reporting boundary：论文不是普通文本输出，而是需要结构、引用、评价和审稿接口的 scientific artifact。

## 局限性

- 主要是 paper writing，不应作为自主科学发现主证据。
- 如果输入材料本身不可靠，写作 agent 可能把错误组织得更像论文。
- 自动评价不等同于同行评审或实验复现。

