# Ma 2026 - DeepRoot: A KG-Coordinated Multi-Agent System for Therapeutic Reasoning over Historical Medical Texts

**论文信息**
- 标题：DeepRoot: A KG-Coordinated Multi-Agent System for Therapeutic Reasoning over Historical Medical Texts
- 作者：Zijian Carl Ma; Sean J. Wang; Sijbren Manuel Kramer; Li Erran Li
- 年份：2026
- 来源 / venue：arXiv / OpenReview GenBio 2026 Poster
- DOI / arXiv / URL：https://arxiv.org/abs/2606.15931 ; https://openreview.net/forum?id=q6uNEM1Xru
- PDF / 本地文件路径：当前笔记基于 OpenReview abstract、arXiv search snippet 与 reviewer 一手 PDF 证据整理
- 论文类型：系统论文 / therapeutic reasoning agent
- 当前状态：to_read
- 阅读日期：2026-06-19
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | OpenReview abstract L22-L25 | 论文明确提出 multi-agent LLM system，并联合构建和使用 verified KG | 高 |
| 科学对象归类 | `07.04` | OpenReview abstract L22-L25；reviewer PDF evidence | 最终目标是把历史医药文本转成 verifiable drug-discovery leads | 高 |
| 方法流程 | KG-grounded therapeutic reasoning | OpenReview abstract L22-L25 | grounding 与 reasoning 被分离再组合，服务于 therapeutic reasoning | 高 |
| 科学验证 | lead recovery + reasoning audit | OpenReview abstract L23-L25 | 在 held-out compound-disease treatment pairs 上 R@20=47.6%，且 hallucination 率显著低于 tool-using baselines | 高 |
| 边界判断 | 不转 `11.07` 或 `06` | OpenReview abstract；reviewer PDF evidence | 历史文本与 KG 只是入口，最终对象是 therapeutic leads 与 treatment recovery | 高 |

## 0. 摘要翻译

论文指出，历史医药档案和传统医学知识仍是现代药物开发的重要来源，但前本体化文本和不一致的分类体系阻碍了它们进入现代生物医药流程。作者提出 DeepRoot，一个多 Agent LLM 系统，能够联合构建并使用经验证的知识图谱，把 grounding 与 reasoning 作为可组合的两个轴，用于 therapeutic reasoning。应用在《神农本草经》上时，DeepRoot 在 held-out compound-disease treatment pairs 上达到 R@20 47.6%，明显优于 raw corpus LLM 和随机基线，同时显著降低 hallucinated evidence 比例。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：具有多 Agent 结构、KG 构建与利用、外部 API 查询、推理与验证闭环
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：是
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：是
- 在科研流程中承担的明确角色：知识组织、治疗线索发现、证据核验、推理整合

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：07
- 二级类：07.04
- 三级类：
- 四级专题：Therapeutic reasoning and lead-discovery agents
- 四级专题是否为新增：否
- 归类理由：尽管入口是历史医学文本和 KG，但论文最终要输出的是可核验 drug-discovery leads
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：therapeutic lead discovery / treatment recovery
- 最终科学问题：如何从历史医学文本中系统挖掘可验证的治疗线索
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：KG 和文本现代化只是手段，目标仍是生物医药转化线索

### 2.3 容易混淆的边界

- 可能误归类到：11.07；06
- 最终判定：保留 07.04
- 判定理由：系统不研究 scientific knowledge production itself，也不是一般生物文本挖掘；它直接面向 therapeutic reasoning 和 leads
- 是否需要二次复核：否，主类方向较稳

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：部分是
- Tool-using Agent：是
- Retrieval-augmented Agent：是
- Multi-Agent System：是
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：未明确
- Hybrid Agent：是
- 其他：KG-coordinated reasoning system

### 3.2 科研流程角色

- 文献检索与阅读：是
- 知识抽取与组织：是
- 科学问题提出：部分是
- 假设生成：是
- 实验设计：否
- 仿真建模：否
- 工具调用与代码执行：是
- 实验执行：否
- 数据分析：是
- 结果解释：是
- 证据评估与验证：是
- 论文写作：否
- 端到端科研流程自动化：是

### 3.3 自主能力

- 任务分解：是
- 计划生成：部分是
- 工具调用：是
- 记忆与状态维护：是
- 反馈迭代：是
- 自主决策：是
- 多 Agent 协作：是
- 环境交互：是
- 闭环实验：否

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 实验驱动：否
- 仿真驱动：否
- 多模态：否
- 多尺度建模：否
- 高通量筛选：否
- 知识图谱：是
- 数字孪生：否
- 机器人平台：否
- 其他：historical medical text modernization

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：历史医学文本蕴含药物发现线索，但难标准化进入现代 biomedical pipelines
- 现有科研流程或方法的痛点：无现有 agent 能把这类文本大规模转成 verifiable drug-discovery leads
- 核心假设或直觉：把 grounding 与 reasoning 分离再组合，可让知识图谱和 LLM 各自发挥优势

### 4.2 系统流程

1. 输入：historical medical texts
2. 任务分解 / 规划：构建并验证知识图谱
3. 工具、数据库、模型或实验平台调用：查询 APIs、构建 KG、执行 reasoning
4. 中间结果反馈：核验 claims 与 evidence fidelity
5. 决策或迭代：更新 therapeutic plausibility judgement
6. 输出：drug-discovery leads 与 treatment recovery results

### 4.3 系统组件

- Agent 核心：DeepRoot multi-agent LLM system
- 工具 / API / 数据库：verified KG + external biomedical APIs
- 记忆或状态模块：KG state
- 规划器：多 Agent 协调
- 评估器 / verifier：LLM-as-judge reasoning audit
- 人类反馈或专家介入：有 qualitative expert-oriented evaluation
- 实验平台或仿真环境：文本 / KG / API reasoning environment

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：否
- 高通量计算：否
- 机器人实验：否
- 湿实验：否
- 临床数据：否
- 真实场景部署：否
- 专家评估：是

### 5.2 数据、任务与指标

- 数据集 / 实验对象：Shen Nong Ben Cao Jing
- 任务设置：held-out compound-disease treatment pair recovery + reasoning audit
- 对比基线：raw corpus LLM、random、tool-using LLM、graph-only inference
- 评价指标：R@20、hallucinated evidence rate、reasoning quality
- 关键结果：R@20 47.6%；tool-using LLM hallucination 87%，DeepRoot 7-10%
- 是否有消融实验：有，摘要比较了 KG-only、LLM-only、KG+LLM
- 是否有失败案例或负结果：graph-only 0 hallucination 但 reasoning coherence 最低

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：更偏 therapeutic leads 与 historical knowledge repurposing
- 科学贡献是否经过验证：是
- 贡献强度判断：中到强
- 科学贡献类型：system_platform; drug_discovery
- 证据强度：medium_high_primary_abstract

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单纯文本挖掘，而是 lead-oriented therapeutic reasoning system
- 与已有 Agent / 科研智能系统的区别：把 grounding 和 reasoning 作为可分离但可组合的两轴
- 与同一科学领域其他 Agent 文献的关系：可与 Mozi、MolClaw、Latent-Y、Rhizome OS-1 对照
- 主要创新点：把历史医疗文本现代化为可核验的药物发现线索

## 7. 局限性与风险

- Agent 自主性不足：主要仍停留在文本 / KG 推理环境
- 科学验证不足：缺乏更下游湿实验验证
- 泛化性不足：当前主要场景是历史医学文本
- 工具链依赖：高度依赖 KG 与 API 质量
- 数据泄漏或 benchmark 偏差：待全文核对 held-out split 设计
- 成本、可复现性或安全风险：医学线索解释需谨慎
- 是否仍需进一步全文复核：否；当前证据已足以支持纳入和主类判断

## 8. 对综述写作的价值

- 可放入哪个章节：07.04 药物发现 / therapeutic reasoning agents
- 可支撑哪个论点：以文本与 KG 为入口的系统，只要输出是治疗线索，仍应归在 `07`
- 可用于哪个表格或图：text/KG-driven therapeutic reasoning comparison
- 适合作为代表性案例吗：适合作为非实验型药物发现边界样本
- 推荐引用强度：core
- 需要在正文中特别引用的页码 / 图 / 表：R@20 47.6%、7-10% hallucination、87% tool-call hallucination
- 需要与哪些论文并列比较：Mozi、MolClaw、Latent-Y、OriGene

## 9. 总结

### 9.1 一句话概括

把历史医学文本转成可核验治疗线索的多 Agent 系统。

### 9.2 速记版 pipeline

1. 读取历史医药文本
2. 构建并验证知识图谱
3. 多 Agent 做治疗推理
4. 对证据与结论打分
5. 输出药物发现线索

### 9.3 标注字段汇总

```text
是否纳入：是
主类：07
二级类：07.04
三级类：
四级专题：Therapeutic reasoning and lead-discovery agents
Agent 类型：LLM Agent; Tool-using Agent; Retrieval-augmented Agent; Multi-Agent System; Hybrid Agent
科研流程角色：literature_search_and_reading; hypothesis_generation; evidence_assessment_and_validation; feedback_iteration
自主能力：task_decomposition; tool_use; memory_or_state_tracking; feedback_iteration; autonomous_decision_making; multi_agent_collaboration
验证方式：benchmark; expert_evaluation
交叉属性：computation_driven; data_driven; knowledge_graph
科学贡献类型：system_platform; drug_discovery
证据强度：medium_high_primary_abstract
归类置信度：高
纳入置信度：高
推荐引用强度：core
```
