# Shah et al. 2026 - Automating Computational Reproducibility in Social Science

**论文信息**
- 标题：Automating Computational Reproducibility in Social Science: Comparing Prompt-Based and Agent-Based Approaches
- 作者：Syed Mehtab Hussain Shah; Frank Hopfgartner; Arnim Bleier
- 年份：2026
- 来源 / venue：arXiv / The Web Conference 2026 workshop
- DOI / arXiv / URL：https://arxiv.org/abs/2602.08561
- PDF / 本地文件路径：当前笔记基于 arXiv 摘要与 workshop 接收信息；未保存本地 PDF
- 论文类型：系统论文 / scientific reproducibility Agent
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | arXiv abstract | 明确比较 prompt-based 与 agent-based workflows，后者会检查文件、修改代码、重复运行分析 | 高 |
| 科学对象归类 | `11.07` | arXiv abstract | 核心对象是 social science computational reproducibility，而不是社会科学现象本身 | 高 |
| 方法流程 | 多步闭环 | arXiv abstract | 在 Docker 环境中接收失败复现实例，诊断错误，修复代码，再次运行 | 高 |
| 实验验证 | 有受控验证 | arXiv abstract | 基于 five fully reproducible R-based social science studies 做故障注入与修复测试 | 中高 |
| 边界判断 | 不归 `01.04` | object-first reading | 论文研究的是 scientific reproducibility / post-publication verification，本体是知识生产过程 | 高 |

## 0. 摘要翻译

本文比较两类自动化计算复现流程在社会科学中的表现：一类是直接 prompt 驱动的大模型流程，另一类是具有文件检查、代码修改和重复执行能力的 agent-based 流程。作者在干净的 Docker 环境中对若干可复现的 R 语言社会科学研究进行故障注入测试，评估系统是否能够自动诊断并修复复现失败。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：存在明确科研目标、多步执行链、代码与文件操作、失败反馈后的自主修复
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：部分是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：未明确
- 在科研流程中承担的明确角色：复现执行、错误诊断、代码修复、证据评估

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：11
- 二级类：11.07
- 三级类：computational reproducibility in social science
- 四级专题：social-science reproducibility agents
- 四级专题是否为新增：否
- 归类理由：稳定对象是 scientific reproducibility 与 post-publication verification
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：已发表社会科学研究的计算可复现性
- 最终科学问题：Agent 能否自动诊断、修复并重新执行复现失败的研究代码
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：agent 只是手段，论文真正研究的是科学知识生产中的复现审查

### 2.3 容易混淆的边界

- 可能误归类到：01.04
- 最终判定：保留 11.07
- 判定理由：目标不是通用科研工作流，而是科学复现这一知识生产过程本身
- 是否需要二次复核：需要更强 full text 证据，但当前主类方向稳定

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：部分是
- Tool-using Agent：是
- Retrieval-augmented Agent：否
- Multi-Agent System：未明确
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：否
- Hybrid Agent：是
- 其他：reproducibility repair agent

### 3.2 科研流程角色

- 文献检索与阅读：是
- 知识抽取与组织：否
- 科学问题提出：否
- 假设生成：否
- 实验设计：否
- 仿真建模：否
- 工具调用与代码执行：是
- 实验执行：否
- 数据分析：是
- 结果解释：是
- 证据评估与验证：是
- 论文写作：否
- 端到端科研流程自动化：部分是

### 3.3 自主能力

- 任务分解：部分是
- 计划生成：部分是
- 工具调用：是
- 记忆与状态维护：中
- 反馈迭代：是
- 自主决策：是
- 多 Agent 协作：未明确
- 环境交互：是
- 闭环实验：否

## 4. 方法设计

- 输入是带有复现失败的研究代码、文件和环境信息。
- 系统读取错误线索后执行文件检查、代码编辑和重复运行。
- 通过执行结果反馈判断是否修复成功，形成复现修复闭环。

## 5. 实验与验证

- 验证方式：controlled reproducibility benchmark
- 对象：five fully reproducible R-based social science studies
- 关键结果：agent-based workflow 比 prompt-only workflow 更能处理复杂复现故障
- 证据强度判断：abstract-level strong, full-text still desirable

## 6. 与已有工作的关系

- 相比通用代码助手，这篇论文把对象限定在 scientific reproducibility。
- 相比一般科研平台论文，它更像 knowledge-production / evaluation 系统。
- 可与 `PaperRepro`、`ARA`、peer-review automation 记录并列讨论。

## 7. 局限性与风险

- 当前核心证据仍主要来自摘要级信息。
- 样本规模不大，且为受控故障注入环境。
- 主要剩余风险是 core-strength，而不是顶层分类方向。

## 8. 对综述写作的价值

- 可作为 `11.07` 中 reproducibility automation 的代表样本。
- 能支持“Agent 不只做发现，也进入科学审查与知识生产质量控制”的论点。

## 9. 总结

这是一篇稳定的 `11.07` 文献：论文对象是社会科学研究的计算复现审查，而不是通用科研 Agent 平台。
