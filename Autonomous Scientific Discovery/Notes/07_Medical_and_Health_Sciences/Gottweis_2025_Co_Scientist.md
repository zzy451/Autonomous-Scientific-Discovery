# Gottweis et al. 2025 - Towards an AI co-scientist

**论文信息**
- 标题：Towards an AI co-scientist
- 作者：Juraj Gottweis et al.
- 年份：2025
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2502.18864；https://doi.org/10.48550/arXiv.2502.18864
- PDF / 本地文件路径：arXiv PDF；Nature preview page https://www.nature.com/articles/s41586-026-10644-y
- 论文类型：系统论文 / biomedical co-scientist system
- 当前状态：已读摘要级与 journal preview 级证据；主列表当前仍记为 `to_read`
- 阅读日期：2026-06-18
- 笔记作者：Codex

## Evidence Log

记录所有关键判断对应的原文位置，后续写综述时优先回到这里核对。

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | arXiv abstract；Nature abstract | 明确是 multi-agent AI system，执行 hypothesis generation、debate、refinement，并按 scientist-provided objectives 生成待实验验证的假设 | 高 |
| 科学对象归类 | 当前暂保留 `07.04` | arXiv abstract L40-L44；Nature abstract L98-L101 | 虽然系统 framing general-purpose，但现有开发与验证集中在 drug repurposing、novel target discovery、anti-microbial resistance 三类 biomedical applications | 中高 |
| 方法流程 | generate-debate-evolve hypothesis loop | arXiv abstract L40-L43；Nature abstract L98-L100 | 系统采用 multi-agent architecture、asynchronous task execution 与 tournament evolution，自主生成、批评、改写并进化假设 | 高 |
| 实验验证 | real biomedical validation 存在 | arXiv abstract L42-L44；Nature abstract L100-L101 | 报告 acute myeloid leukemia 的 drug repurposing 候选体外验证，以及其他 biomedical discovery 验证案例 | 中高 |
| 边界风险 | `07 / 01.04` 压力仍在 | arXiv abstract L41-L44；Nature abstract L98-L100 | 系统自称 general purpose co-scientist，但目前 strongest evidence 仍主要是 biomedical validation，因此暂不回拉到 `01.04` | 中高 |

## 0. 摘要翻译

论文提出一个 AI co-scientist，多 Agent 系统建立在 Gemini 系列模型之上，目标是在科学家的研究目标和先验证据约束下生成可实验验证的新假设。系统采用 generate、debate、evolve 的假设生成机制，并通过异步任务执行框架与 tournament evolution 过程扩大 test-time compute，从而持续改进假设质量。虽然系统自称 general purpose，但当前开发与验证主要集中在三个 biomedical 场景：drug repurposing、novel target discovery，以及解释 anti-microbial resistance 相关机制。摘要与 Nature preview 均指出系统已在 acute myeloid leukemia 等 biomedical 任务中得到真实实验级验证信号。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：系统明确是 multi-agent AI system，承担 hypothesis generation、evidence-conditioned proposal building、批评辩论、假设演化与面向实验验证的输出
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- 是否具备以下至少一项 Agent 能力：
  - 计划生成：是
  - 工具调用：中等，现有摘要级证据重点在系统流程而非工具细节
  - 反馈迭代：是
  - 自主决策：是
  - 多 Agent 协作：是
- 在科研流程中承担的明确角色：科学问题提出、假设生成、证据约束下的方案形成、候选筛选、实验验证前研究建议形成

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否，至少具备 generate-debate-evolve 的迭代闭环
- 若排除，排除理由：不排除

## 2. 科学领域归类

### 2.1 主科学领域

- 一级类：07
- 二级类：07.04
- 三级类：
- 四级专题：Biomedical co-scientist systems
- 四级专题是否为新增：否
- 归类理由：当前最强、最直接的一手证据来自 biomedical validation；摘要明确把系统验证集中在 drug repurposing、novel target discovery、anti-microbial resistance 三类 biomedical applications，并报告真实 wet-lab / in vitro / organoid 方向验证结果
- 归类置信度：中高

### 2.2 对象优先判定

- 最终科学研究对象：当前证据下更接近 biomedical discovery hypotheses 与 biomedical co-scientist workflow
- 最终科学问题：如何用多 Agent co-scientist 系统在生物医学研究目标约束下提出并演化可实验验证的新假设
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：论文最吸引人的不只是 Gemini-based multi-agent architecture，而是它如何在真实 biomedical discovery 场景中形成并验证假设

### 2.3 容易混淆的边界

- 可能误归类到：01.04
- 最终判定：当前暂保留 07.04
- 判定理由：如果只看标题与系统 framing，它很像 general co-scientist platform；但目前最强的一手证据来自 biomedical validation，因此在 object-first 规则下，现阶段更适合暂留 `07.04`
- 是否需要二次复核：需要。若后续全文显示 biomedical validation 只是 demo，而非 primary object，应重新评估是否回调 `01.04`

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

- LLM Agent：是
- Planning Agent：是
- Tool-using Agent：中等，摘要级证据未充分展开工具链
- Retrieval-augmented Agent：中等，依赖 prior scientific evidence
- Multi-Agent System：是
- Robot / Embodied Agent：否
- Human-in-the-loop Agent：是，系统以 scientist-provided objectives and guidance 为条件
- Hybrid Agent：是
- 其他：co-scientist hypothesis-evolution system

### 3.2 科研流程角色

- 文献检索与阅读：部分是
- 知识抽取与组织：部分是
- 科学问题提出：是
- 假设生成：是
- 实验设计：部分是
- 仿真建模：否
- 工具调用与代码执行：摘要级证据不足
- 实验执行：否，系统本身不是湿实验平台，但输出面向实验验证
- 数据分析：部分是
- 结果解释：是
- 证据评估与验证：是
- 论文写作：否
- 端到端科研流程自动化：中等

### 3.3 自主能力

- 任务分解：是
- 计划生成：是
- 工具调用：中等
- 记忆与状态维护：中等
- 反馈迭代：是
- 自主决策：是
- 多 Agent 协作：是
- 环境交互：中等
- 闭环实验：部分是

### 3.4 交叉属性标签

- 计算驱动：是
- 数据驱动：是
- 实验驱动：部分是
- 仿真驱动：否
- 多模态：摘要级证据不足
- 多尺度建模：否
- 高通量筛选：否
- 知识图谱：摘要级证据不足
- 数字孪生：否
- 机器人平台：否
- 其他：hypothesis-evolution under scientist guidance

## 4. 方法设计

### 4.1 方法动机

- 作者为什么提出该 Agent 系统：科学发现依赖提出新假设并经过严格实验验证，作者希望用 AI co-scientist 增强这一过程
- 现有科研流程或方法的痛点：高质量新假设生成慢，且难以在复杂 biomedical 问题上快速迭代
- 核心假设或直觉：多 Agent debate 与 evolution 机制，叠加更高的 test-time compute，可以持续改进 hypothesis quality

### 4.2 系统流程

按输入到输出写清楚 pipeline：

1. 输入：scientist-provided research objectives、guidance 与 prior scientific evidence
2. 任务分解 / 规划：多个 agents 形成候选 hypotheses
3. 工具、数据库、模型或实验平台调用：在先验证据条件下组织与评估候选方案
4. 中间结果反馈：agents 之间 debate、critique、refine
5. 决策或迭代：通过 tournament evolution 机制推进自改进假设生成
6. 输出：可供实验验证的 novel biomedical hypotheses 与 proposals

### 4.3 系统组件

- Agent 核心：Gemini-based multi-agent architecture
- 工具 / API / 数据库：prior scientific evidence sources；具体工具链待全文复核
- 记忆或状态模块：asynchronous task execution framework
- 规划器：hypothesis generation and evolution process
- 评估器 / verifier：automated evaluations + downstream experimental validation
- 人类反馈或专家介入：scientist-provided objectives and guidance
- 实验平台或仿真环境：下游 biomedical validation environments

## 5. 实验与验证

### 5.1 验证方式

- benchmark：是
- 仿真验证：否
- 高通量计算：摘要级证据不足
- 机器人实验：否
- 湿实验：部分是
- 临床数据：摘要级证据不足
- 真实场景部署：否
- 专家评估：是

### 5.2 数据、任务与指标

- 数据集 / 实验对象：biomedical discovery applications，包括 drug repurposing、novel target discovery、anti-microbial resistance mechanism explanation
- 任务设置：在 scientist-specified goals 与 prior evidence 下生成并进化 hypotheses
- 对比基线：automated evaluations over hypothesis quality；具体基线待全文复核
- 评价指标：hypothesis quality 随 test-time compute 扩展而提升；并有真实 biomedical validation 结果
- 关键结果：报告 AML drug repurposing 候选及组合疗法的 in vitro validation；并报告其他 biomedical discovery validation
- 是否有消融实验：摘要级证据不足
- 是否有失败案例或负结果：摘要级证据不足

### 5.3 科学贡献

- 是否发现新知识、新机制、新分子、新材料、新假设或新实验结果：是，至少在摘要级证据上指向真实 biomedical hypotheses 和验证
- 科学贡献是否经过验证：是，摘要与 Nature preview 均指向实验级 biomedical validation
- 贡献强度判断：中到强
- 科学贡献类型：假设；系统平台
- 证据强度：实验验证

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单任务预测模型，而是多 Agent hypothesis-generation and evolution system
- 与已有 Agent / 科研智能系统的区别：强调 scientist guidance、test-time compute scaling 和 debate/evolve 假设机制
- 与同一科学领域其他 Agent 文献的关系：既可与 `Biomni`、`Robin`、`HealthFlow` 等 biomedical agents 比较，也可与 `CycleResearcher`、`The AI Scientist` 等通用 research-agent systems 做边界对照
- 主要创新点：用多 Agent 异步框架和 tournament evolution 机制提升 biomedical hypothesis generation，并连接到真实实验验证

## 7. 局限性与风险

- Agent 自主性不足：仍依赖 scientist-provided objectives and guidance
- 科学验证不足：虽然已有 biomedical validation，但目前本地可获取证据仍以摘要和 journal preview 为主，全文细节尚未完全压实
- 泛化性不足：general-purpose framing 是否真正稳固，仍需全文核验
- 工具链依赖：依赖 Gemini-based multi-agent architecture 与 test-time compute scaling
- 数据泄漏或 benchmark 偏差：自动评估部分可能有偏差
- 成本、可复现性或安全风险：高计算成本、多 Agent debate 复杂性与 biomedical hypothesis 误导风险

## 8. 对综述写作的价值

- 可放入哪个章节：07.04 biomedical discovery agents；同时可在 `07 / 01.04` 边界讨论中重点提及
- 可支撑哪个论点：Agent systems 已从 benchmark-only hypothesis generation 走向真实 biomedical validation；但 general co-scientist 与 domain-specific biomedical object 的边界仍需谨慎解释
- 可用于哪个表格或图：medical / biomedical Agent representative case table；boundary-case table
- 适合作为代表性案例吗：适合
- 推荐引用强度：核心引用
- 需要在正文中特别引用的页码 / 图 / 表：当前可优先引用 arXiv / Nature abstract；正文页码待后续全文补强
- 需要与哪些论文并列比较：`Biomni`、`HealthFlow`、`Robin`、`The AI Scientist`、`CycleResearcher`

## 9. 总结

### 9.1 一句话概括

面向生物医学发现的多 Agent co-scientist 假设生成系统。

### 9.2 速记版 pipeline

1. 输入科学家目标和证据
2. 多 Agent 生成候选假设
3. debate / critique / refine
4. tournament evolution 迭代筛选
5. 输出可实验验证的 biomedical hypotheses

### 9.3 标注字段汇总

```text
是否纳入：是
主类：07
二级类：07.04
三级类：
四级专题：Biomedical co-scientist systems
Agent 类型：LLM Agent; Planning Agent; Retrieval-augmented Agent; Multi-Agent System; Human-in-the-loop Agent; Hybrid Agent
科研流程角色：scientific_question_formulation; hypothesis_generation; evidence_assessment_and_validation; result_interpretation
自主能力：task_decomposition; planning; feedback_iteration; autonomous_decision_making; multi_agent_collaboration
验证方式：benchmark; wet_lab_experiment; expert_evaluation
交叉属性：computation_driven; data_driven; experiment_driven
科学贡献类型：hypothesis; system_platform
证据强度：experimentally_validated
归类置信度：中高
纳入置信度：高
推荐引用强度：core
```
