# Smbatyan et al. 2025 - Can AI Agents Design and Implement Drug Discovery Pipelines?

**论文信息**
- 标题：Can AI Agents Design and Implement Drug Discovery Pipelines?
- 作者：Khachik Smbatyan, Tsolak Ghukasyan, Tigran Aghajanyan, Hovhannes Dabaghyan, Sergey Adamyan, Aram Bughdaryan, Vahagn Altunyan, Gagik Navasardyan, Aram Davtyan, Anush Hakobyan, Aram Gharibyan, Arman Fahradyan, Artur Hakobyan, Hasmik Mnatsakanyan, Narek Ginoyan, Garik Petrosyan
- 年份：2025
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2504.19912
- PDF / 本地文件路径：临时阅读 `ASD-0017.pdf` / `ASD-0017.txt`
- 论文类型：benchmark + 系统论文
- 当前状态：已读，已纳入
- 阅读日期：2026-06-15
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是，Drug discovery benchmark 中的多 Agent 系统 | PDF p.1-2 Abstract/Introduction | Deep Thought multi-agent system；agents develop, implement, execute strategies；write files, execute code, browse web | 高 |
| 科学对象归类 | `07` 医学与健康科学，药物发现 | PDF p.1-2 | drug discovery；virtual screening；pharmaceutical design | 高 |
| 方法流程 | DO Challenge + Deep Thought 多 Agent 求解 | PDF p.2, contributions；section 3 | identify top molecular structures from 1M library；request 10% labels；3 submissions | 高 |
| 实验验证 | benchmark、竞赛、人类团队/专家对照、消融 | PDF p.2；results lines | Deep Thought 33.5% overlap, top human expert 33.6%, best competition team 16.4%；unrestricted expert 77.8% | 高 |
| 科学贡献 | 提供药物发现 Agent 综合评测和强基线系统 | PDF p.2 contributions | benchmark for strategic decision-making, model selection, code development and execution | 高 |

## 0. 摘要翻译

论文提出 DO Challenge，用于评价 AI Agent 在药物发现中的综合决策能力。任务模拟 virtual screening：Agent 需要在一百万个分子结构中，通过有限标签请求和有限提交机会，独立设计、实现并执行策略，找到高分子得分候选。作者还提出 Deep Thought 多 Agent 系统，能够进行文献回顾、代码开发和执行，在限时设置中达到 33.5% overlap，接近人类专家 33.6%，超过竞赛最佳团队 16.4%，但在不限时设置中仍明显落后于专家 77.8%。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是。
- 判断依据：Deep Thought 是 heterogeneous LLM-based multi-agent system，Agent 之间通信并用工具与环境交互。
- 判定置信度：高。
- 是否面向明确科研目标：是，药物发现 / virtual screening。
- 是否具有多步行动过程：是，探索化学空间、选择模型、请求标签、写代码、执行策略、提交候选。
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是。
  - 工具调用：是，文件写入、代码执行、网页浏览。
  - 反馈迭代：是，有限标签请求和策略调整。
  - 自主决策：是。
  - 多 Agent 协作：是。
- 在科研流程中承担的明确角色：虚拟筛选策略设计者、建模者、代码执行者、候选分子筛选者。

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否，论文核心是 Agent benchmark 与多 Agent 求解系统。
- 是否只是单次问答、摘要或分类：否。
- 是否缺少行动闭环：否。
- 若排除，排除理由：不排除。

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：`07` 医学与健康科学。
- 二级类：`07.04` 药学与生物医药。
- 三级类：`07.04.01` 药物发现。
- 四级专题：Drug discovery / biomedical agents。
- 四级专题是否为新增：否。
- 归类理由：最终任务是药物发现中的分子筛选和候选优先级排序。
- 归类置信度：高。

### 2.2 对象优先判定

- 最终科学研究对象：药物候选分子、分子构象、ADMET 相关 protein target docking score。
- 最终科学问题：Agent 能否在资源受限条件下设计并执行药物筛选 pipeline。
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：多 Agent 和 LLM 是实现，研究对象是 drug discovery。

### 2.3 容易混淆的边界

- 可能误归类到：`03` 化学科学；`01.04` 通用 Agent benchmark。
- 最终判定：`07`。
- 判定理由：虽然涉及分子和 docking，但目标是药物发现 pipeline 与 pharmaceutical design，不是单纯化学性质探索。
- 是否需要二次复核：否。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是。
- Planning Agent：是。
- Tool-using Agent：是。
- Retrieval-augmented Agent：可能，支持 browsing / literature review。
- Multi-Agent System：是。
- Robot / Embodied Agent：否。
- Human-in-the-loop Agent：否，验证中有专家对照但系统执行不依赖人。
- Hybrid Agent：是。
- 其他：benchmark-solving research agent。

### 3.2 科研流程角色

- 文献检索与阅读：是。
- 知识抽取与组织：部分。
- 科学问题提出：否。
- 假设生成：弱。
- 实验设计：是，计算筛选策略设计。
- 仿真建模：间接，使用 docking-derived benchmark score。
- 工具调用与代码执行：是。
- 实验执行：否。
- 数据分析：是。
- 结果解释：是。
- 证据评估与验证：是。
- 论文写作：否。
- 端到端科研流程自动化：部分，覆盖计算 drug discovery pipeline。

### 3.3 自主能力

- 任务分解：是。
- 计划生成：是。
- 工具调用：是。
- 记忆与状态维护：是，任务执行过程维护状态。
- 反馈迭代：是，标签请求和模型调整。
- 自主决策：是。
- 多 Agent 协作：是。
- 环境交互：是，代码环境、Web、文件系统。
- 闭环实验：计算闭环，不是湿实验闭环。

### 3.4 交叉属性标签

- 计算驱动：是。
- 数据驱动：是。
- 实验驱动：否。
- 仿真驱动：是，docking-derived score。
- 多模态：否。
- 多尺度建模：否。
- 高通量筛选：是，1M molecule library。
- 知识图谱：否。
- 数字孪生：否。
- 机器人平台：否。
- 其他：active learning / virtual screening benchmark。

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：已有 drug discovery benchmark 多评估孤立预测任务，缺少评估 Agent 独立决策、代码开发和 pipeline 执行的综合任务。
- 现有科研流程或方法的痛点：真实药物发现资源受限、目标多、需要策略性探索。
- 核心假设或直觉：一个综合 virtual screening challenge 可以更真实地测试 Agent 的科学决策能力。

### 4.2 系统流程

1. 输入：一百万个分子构象库、隐藏 DO Score、有限标签预算和提交限制。
2. 任务分解 / 规划：Agent 制定探索化学空间、模型选择、采样和提交策略。
3. 工具、数据库、模型或实验平台调用：写代码、执行模型训练/筛选、浏览资料、管理文件。
4. 中间结果反馈：请求最多 10% 真实 DO Score 标签，并根据结果调整策略。
5. 决策或迭代：选择候选集，最多 3 次提交。
6. 输出：预测 top 1000 高分子得分候选结构。

### 4.3 系统组件

- Agent 核心：Claude 3.7 Sonnet、Gemini 2.5 Pro、o3 等主 Agent；GPT-4o、Gemini 2.0 Flash 等辅助角色。
- 工具 / API / 数据库：代码执行、文件系统、网页浏览、benchmark dataset。
- 记忆或状态模块：任务上下文、标签请求历史。
- 规划器：多 Agent 策略规划。
- 评估器 / verifier：benchmark overlap 指标；消融评估。
- 人类反馈或专家介入：无执行介入；有竞赛团队和专家对照。
- 实验平台或仿真环境：DO Challenge benchmark。

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是。
- 仿真验证：是，docking / virtual screening benchmark。
- 高通量计算：是。
- 机器人实验：否。
- 湿实验：否。
- 临床数据：否。
- 真实场景部署：否。
- 专家评估：人类专家参考解。

### 5.2 数据、任务与指标

- 数据集 / 实验对象：1M unique molecular conformations；4 protein targets including ADMET-related proteins；DEKOIS2 / DUD-E 相关训练和验证背景。
- 任务设置：从隐藏标签分子库中找 top DO Score 结构；最多请求 100,000 标签，最多 3 次提交。
- 对比基线：DO Challenge 2025 human teams、人类 domain experts、不同 LLM 和系统消融。
- 评价指标：top 1000 overlap percentage；限时/不限时设置。
- 关键结果：限时 Deep Thought 33.5%，接近专家 33.6%，超过最佳参赛团队 16.4%；不限时专家 77.8% 明显领先。
- 是否有消融实验：是。
- 是否有失败案例或负结果：有，系统高不稳定，且弱于专家不限时方案。

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：主要不是发现新药，而是提出可评估 Agent 药物筛选能力的 benchmark 和强基线系统。
- 科学贡献是否经过验证：benchmark 验证充分。
- 贡献强度判断：中。
- 科学贡献类型：benchmark / 系统平台。
- 证据强度：benchmark + 人类对照 + 消融。

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不只预测分子性质，而要求 Agent 自主规划、编码、采样和提交。
- 与已有 Agent / 科研智能系统的区别：提供药物发现场景下资源受限、目标综合的评测环境。
- 与同一科学领域其他 Agent 文献的关系：可与 AgentD、DrugAgent、LIDDIA 等药物发现 Agent 比较；本篇偏 benchmark 和系统评估。
- 主要创新点：把 drug discovery 的 multi-objective virtual screening 转化为 Agent 能力评测。

## 7. 局限性与风险

- Agent 自主性不足：强，但仍依赖 benchmark 环境，不覆盖真实湿实验。
- 科学验证不足：没有真实药物候选实验验证。
- 泛化性不足：DO Score 是构造指标，未必代表真实药物开发全部复杂性。
- 工具链依赖：依赖代码执行和模型环境。
- 数据泄漏或 benchmark 偏差：公开 benchmark 后需防止训练污染。
- 成本、可复现性或安全风险：多模型 Agent 运行成本和随机性可能较高。

## 8. 对综述写作的价值

- 可放入哪个章节：医学与健康科学 / 药物发现 Agent；也可在 benchmark 章节引用。
- 可支撑哪个论点：科学 Agent 评测应从孤立预测走向策略规划、资源分配和执行能力。
- 可用于哪个表格或图：药物发现 Agent 验证方式表；Agent vs human benchmark 对照表。
- 适合作为代表性案例吗：适合，尤其代表 benchmark-driven drug discovery Agent。
- 推荐引用强度：核心引用。
- 需要在正文中特别引用的页码 / 图 / 表：PDF p.1-2 Abstract/Introduction；benchmark section；结果表/图需进一步提取具体编号。
- 需要与哪些论文并列比较：Ock 2025 AgentD、LIDDIA、DrugAgent、RAG-enhanced drug discovery agents。

## 9. 总结

### 9.1 一句话概括

药物发现 Agent 综合评测。

### 9.2 速记版 pipeline

1. 给出百万级分子库和隐藏得分。
2. Agent 制定筛选策略。
3. 请求有限标签并训练/选择模型。
4. 迭代筛选候选分子。
5. 用 top overlap 与人类团队/专家比较。

### 9.3 标注字段汇总

```text
是否纳入：是
主类：07 医学与健康科学
二级类：07.04 药学与生物医药
三级类：07.04.01 药物发现
四级专题：Drug discovery / biomedical agents
Agent 类型：LLM Agent；Planning Agent；Tool-using Agent；Multi-Agent System；Hybrid Agent
科研流程角色：实验设计；仿真建模；工具调用与代码执行；数据分析；证据评估与验证
自主能力：任务分解；计划生成；工具调用；记忆与状态维护；反馈迭代；自主决策；多 Agent 协作
验证方式：benchmark；仿真验证；高通量计算；专家评估
交叉属性：计算驱动；数据驱动；仿真驱动；高通量筛选
科学贡献类型：benchmark；系统平台
证据强度：全文 PDF 高
归类置信度：高
纳入置信度：高
推荐引用强度：核心引用
```
