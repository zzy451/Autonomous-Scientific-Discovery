# 三篇综述精读记录：Skill-driven Agentic Autonomous Scientific Discovery

> 状态：已按 `three_surveys_reading_plan.md` 完成三篇综述的第一轮精读。  
> 目标：不是直接证明“Skill-driven autonomous scientific discovery 已经成立”，而是判断 **skill lifecycle 是否能作为分析 autonomous scientific discovery agents 的可证实框架**。

## 0. 三篇材料的分工

| 文献 | 核心对象 | 它回答的问题 | 对我们综述的作用 | 主要限制 |
|---|---|---|---|---|
| 本地 HTML `research-report.html` / GitHub `Minions-Land/Science-Discovery` | academic workflow 中的 skill 生态、benchmark、memory、web search、long-horizon infrastructure | 如果把 skill 当作 Agent 能力单元，科研工作流需要怎样的工程栈？ | 给出最接近我们主题的立场框架：skill 是科研 Agent 的操作单位，证据链、记忆、搜索、长周期任务是必要基础设施 | 它是 essay/report，不是系统综述；部分生态判断需要继续用论文和仓库核验 |
| `arXiv:2508.14111` From AI for Science to Agentic Science | autonomous scientific discovery / Agentic Science | 科学发现 Agent 应该覆盖哪些科研阶段？自治程度如何分级？关键挑战是什么？ | 给出我们的 **横轴**：Scientific Discovery Workflow | domain/process-oriented，缺少对 skill representation / retrieval / evolution 的细粒度讨论 |
| `arXiv:2605.07358` A Comprehensive Survey on Agent Skills | Agent skill lifecycle | skill 是什么？如何表示、获取、检索、演化？为什么 tool use 还不够？ | 给出我们的 **纵轴**：Skill Lifecycle | general agent survey，不专门讨论科学发现；需要我们完成科研场景映射 |

## 1. 中心问题：读完后的回答

原问题：

> 自动科学发现 Agent 的能力差异，能否被解释为 procedural knowledge 的外化、复用、检索、组合、演化与验证能力差异？

读完后的判断：

**可以作为一个稳健的分析视角，但目前还不能写成强结论。**

更准确的表述是：

> Skill lifecycle offers a verifiable lens for analyzing autonomous scientific discovery agents: current systems automate scientific workflows, but differ sharply in whether their procedural knowledge is represented, acquired, retrieved, composed, evolved, and verified as reusable skills.

也就是说，我们现在能主张的是：

1. 科学发现流程中确实存在可复用的 procedural units，例如文献检索、假设筛选、实验执行、代码复现、引用验证、审稿反馈、记忆更新。
2. Agent Skills 综述说明这些 procedural units 可以被形式化为 reusable procedural artifacts。
3. 本地 HTML 说明如果这些 artifacts 要服务科研，就必须接入 evidence、memory、web retrieval、long-horizon planning 和 verification。
4. 但现有自动科研系统多为 **pipeline-driven**，未必已经是严格的 **skill-driven**。

因此我们应采用稳健命题：

> Current autonomous scientific discovery agents expose a procedural gap, and skill lifecycle provides a useful framework for analyzing and potentially closing that gap.

## 2. `2605.07358` Agent Skills Survey：精读结果

### 2.1 这篇综述具体讲了什么

这篇综述把 LLM Agent 的能力问题从“模型能不能推理”和“工具能不能调用”，转向一个更中间的对象：**agent skills**。

它的基本判断是：

- 现代 Agent 已经能使用 tools、memory、structured interaction。
- 但如果每个任务都从零推理、临时拼接工具调用，系统会低效、脆弱、难维护。
- 因此需要 skill 作为可复用的 procedural artifact。

它给 skill 的核心定义可以概括为：

> agent skills 是可复用的程序性工件，用于在任务约束下协调 tools、memory 和 runtime context。

这直接把 skill 和 tool 区分开：

| 对象 | 解决的问题 | 例子 |
|---|---|---|
| Tool / API / MCP | Agent 能不能访问某种能力 | search API、Python、browser、database |
| Skill | Agent 应该如何可靠地使用能力 | 何时搜索、如何筛选来源、如何验证引用、失败后如何重试 |

所以它补上的层就是 **procedural gap**：

> 工具解决“能不能做”，skill 解决“怎么做得可靠、可复用、可维护”。

### 2.2 四阶段 skill lifecycle

| 阶段 | 综述中的含义 | 对科研 Agent 的映射 |
|---|---|---|
| Representation | skill 如何被表示，包括 root instruction、auxiliary resources、applicability conditions；可分 text-backed、code-backed、hybrid skills | 科研 SOP、实验脚本、引用检查流程、ARA artifact、review checklist、`SKILL.md` |
| Acquisition | skill 从哪里来，包括 human-derived、experience-derived、task-derived、corpus-derived | 人写实验协议；从失败实验轨迹提取经验；从论文/代码库挖 workflow；从 benchmark 任务蒸馏 |
| Retrieval / Selection | skill 如何被召回和选择，包括 dense、sparse、generative、structure-aware retrieval，以及 context/cost/composition/feedback-aware selection | 根据科研阶段调用文献检索 skill、代码复现 skill、统计分析 skill、引用验证 skill |
| Evolution | skill 如何更新、验证、接入 policy、治理 skill library | 失败实验更新 protocol；过时数据库/API触发 skill 修订；不可靠 skill 被降权或删除 |

### 2.3 它给我们的直接证据

| Claim | Evidence from 2605 | 我们可用的归纳 | Caveat |
|---|---|---|---|
| skill 是可复用 procedural artifact | 摘要明确把 agent skills 定义为 reusable procedural artifacts | 可以把科研流程中的可复用操作称为 procedural units，但不能把所有 pipeline 都直接叫 skill | 需要确认是否有显式表示、复用、检索、演化机制 |
| skills 与 agents 互补 | 综述认为 agents 负责 high-level reasoning/planning，skills 构成 operational layer | 科研 Agent 的高层规划和底层执行之间需要 skill 层 | 并非所有科研系统都实现了这一层 |
| 四阶段 lifecycle 可作为组织框架 | 综述按 representation/acquisition/retrieval/evolution 组织文献 | 我们可把它作为纵轴 | 这四阶段来自通用 Agent，不是专为科学发现设计 |
| open challenges 包括 quality control、interoperability、safe updating、long-term capability management | 综述结尾明确讨论这些挑战 | 这些挑战可直接映射到科研 skill 的可靠性、跨系统复用、安全更新、长期维护 | 需要结合科研证据链和复现实验扩展 |

### 2.4 对我们主题的限制

这篇综述不能单独证明“科学发现正在 skill-driven 化”，因为它不是 scientific discovery survey。它能证明的是：

1. skill lifecycle 是一个已有外部综述支持的通用框架。
2. 这个框架可以解释 Agent 能力如何从临时推理走向可维护能力库。
3. 但科学场景中的 hypothesis、experiment、reproduction、wet-lab safety、authorship、peer review 等问题，需要我们自己映射和补充。

## 3. `2508.14111` Agentic Science Survey：精读结果

### 3.1 这篇综述具体讲了什么

这篇综述讨论的是 AI for Science 如何走向 **Agentic Science**。

它把 Agentic Science 定位为 AI for Science 的一个新阶段：AI 不只是做预测、生成、辅助分析，而是作为 goal-directed agents 组织科学发现流程。

核心转变是：

> 从 AI 作为科学工具，走向 AI 作为能规划、执行、分析、验证的科学行动者。

### 3.2 自治等级

这篇综述给出的自治等级可以整理为：

| Level | 角色 | 含义 | 对我们综述的意义 |
|---|---|---|---|
| Level 1 | Computational Oracle | AI 是专家调用的模型/工具，完成预测、拟合、生成等局部任务 | 不是 autonomous discovery，只是能力组件 |
| Level 2 | Automated Research Assistant | AI 执行预定义科研子任务，能自动化局部流程 | 对应许多 tool-driven / workflow-driven 系统 |
| Level 3 | Autonomous Scientific Partner | AI 能较自主地提出假设、设计实验、执行、分析和迭代 | 真正接近 agentic scientific discovery |
| Level 4 | Generative Architect | AI 能创造新方法、新工具、新理论框架 | 目前更像远期愿景，不应在综述中过早宣称 |

这个分级给我们一个重要判断：

> 许多现有系统虽然“自动化”，但仍停留在 Level 2 到 Level 3 之间；是否有 skill lifecycle，决定它们能否从一次性 pipeline 走向可维护科研能力。

### 3.3 科学发现流程

2508 的价值在于给出科学发现的横轴。我们可将其归纳为：

| Scientific workflow stage | 具体能力 | 典型挑战 |
|---|---|---|
| Observation / Knowledge Grounding | 文献检索、知识图谱、事实查证、背景研究 | 知识过期、来源异质、引用幻觉、跨领域关联 |
| Hypothesis / Idea Generation | 提出新颖假设、判断可行性、多样性、因果线索 | novelty 与 feasibility 冲突；LLM 自评不可靠 |
| Experimental Planning | 协议设计、变量控制、资源约束、安全约束 | 成本、安全、物理可行性、实验条件记录 |
| Execution | 代码执行、仿真、机器人实验、工具调用 | 工具选择、环境依赖、错误恢复、长周期执行 |
| Data / Result Analysis | 统计、图表、多模态结果解释、误差分析 | 噪声、偏差、选择性解释、负结果处理 |
| Synthesis / Validation | 写作、审稿、复现、证据综合 | 透明性、可复现性、独立验证、同行评审 |
| Evolution | 根据反馈更新假设、实验策略和知识状态 | 稀疏反馈、错误抽象、长期记忆漂移 |

这就是我们框架里的 **Scientific Workflow 横轴**。

### 3.4 五类 Agent 能力

2508 还总结了 Agentic Science 所需的核心能力。我们可以用更适合本综述的语言整理为：

| Agent ability | 在科学发现中的作用 | 与 skill lifecycle 的关系 |
|---|---|---|
| Planning / Reasoning | 把研究目标拆成子任务，形成实验计划 | 需要 workflow skill / planning skill |
| Tool Use | 调用搜索、代码、数据库、仪器、仿真器 | 需要 execution skill 和 tool-chain composition |
| Memory | 保留文献、实验、失败路径、假设历史 | 支撑 skill acquisition 和 evolution |
| Multi-agent Collaboration | 分工为 planner、coder、critic、reviewer、lab executor | 需要 protocol-mediated composition |
| Optimization / Evolution | 从实验反馈中改进策略 | 对应 skill update、memory consolidation、versioning |

### 3.5 对我们主题的限制

2508 讲的是科学发现流程和领域应用，不是 skill 系统。因此：

- 它能证明我们需要一个科学工作流横轴。
- 它能说明 autonomous science 的挑战包括复现、新颖性、透明性、治理。
- 但它没有充分解释这些流程中的 know-how 如何被表示、复用和维护。

这正是 2605 Agent Skills Survey 可以补上的位置。

## 4. 本地 HTML `research-report.html`：精读结果

### 4.1 这篇报告具体讲了什么

本地 HTML 的主张比两篇 arXiv 更接近我们的主题。它不是普通综述，而是一篇 field report / essay，核心判断是：

> skill 正在成为 AI Agent 能力的基本单位；科研工作流要从 prompt/tool/plugin 走向 skill stack。

它用 AI Scientist、PaperBench、ARA 等材料说明，AI 做研究已经不是简单问答，而是涉及：

- hypothesis
- experiment
- code
- paper
- review
- evidence
- memory
- long-horizon coordination

然后它把这些能力重新组织成 skill / artifact / memory / search / verification 的工程栈。

### 4.2 它如何定义 skill

HTML 中的 skill 是非常工程化的：

| 组成 | 含义 |
|---|---|
| `SKILL.md` | YAML frontmatter + 过程说明 |
| `references/` | 需要时加载的背景资料 |
| `scripts/` | 可执行辅助脚本 |
| `assets/` / templates | 模板、样例、图表、数据等 |

它强调 skill 的属性：

- discoverable：Agent 能自己发现它；
- composable：可以和其他 skill 组合；
- portable：可跨 Agent runtime 使用；
- auditable：过程和来源能被检查。

这与 2605 的 reusable procedural artifacts 高度一致，但更偏工程落地。

### 4.3 它的章节逻辑

| HTML section | 核心内容 | 对我们有用的地方 |
|---|---|---|
| I-II | AI Scientist / PaperBench / ARA 说明科研任务已变成复杂 agent workflow；skill 被定义为能力单元 | 给出“为什么要 skill-centric” |
| III-IV | skill ecosystem 与 benchmark | 说明 skill 生态不是纸面概念，需要 benchmark 约束 |
| V-VII | ARA、SkillOS、SSL | 分别对应 skill/artifact contains、how skill is born、how skill is found |
| VIII | lifecycle of a skill | 直接和 2605 的 lifecycle 对齐 |
| XI | zero-hallucination evidence | 把 citation、memory、discovery 连接到 evidence graph |
| XII | web search as a tool | 把搜索拆成 query / fetch / synthesize 三层 |
| XIII | long-horizon problem | 把真实科研的难点归纳为 long horizon / large context / high frequency |
| XIV | open questions | 提出 composition、language transfer、skill evolution、evidence web、intra-task learning 等待验证问题 |

### 4.4 它对我们最重要的贡献

HTML 把两篇 arXiv 的抽象框架落到了一个科研工作流基础设施上：

| 来自 2508 的问题 | 来自 2605 的方法 | HTML 的落地方式 |
|---|---|---|
| 科研需要从文献到实验再到验证的闭环 | skill 可表示、获取、检索、演化 | 用 skill stack 管理科研过程 |
| 自动科学发现需要透明性和复现 | skill 需要 verification 和 governance | ARA、citation record、evidence graph |
| Agent 任务长、状态多、反馈稀疏 | skill 需要 retrieval、memory、evolution | long-horizon / large-context / high-frequency 三轴 |
| 工具调用不等于科学能力 | skill 填补 procedural gap | web search query/fetch/synthesize 与 citation-grade retrieval |

### 4.5 对 HTML 的警惕

HTML 不能当作严格系统综述直接引用来证明学术结论，因为：

1. 它是 field report，不是 peer-reviewed survey。
2. 它包含 GitHub star、工具生态、工程实践等动态信息。
3. 它提出的四种 cognitive postures、Carriage thesis 等更像研究假设，需要实验验证。

所以它更适合作为：

- 框架启发来源；
- 工程问题清单；
- 未来方向来源；
- 但不应作为唯一证据。

## 5. 三篇综述如何相互补充

### 5.1 横轴 × 纵轴

最核心的互补关系是：

| 维度 | 来源 | 内容 |
|---|---|---|
| 横轴 | 2508 Agentic Science | scientific discovery workflow |
| 纵轴 | 2605 Agent Skills | skill lifecycle |
| 落地层 | 本地 HTML | academic workflow infrastructure |

因此我们的二维框架不是凭空发明：

> Scientific Discovery Workflow × Skill Lifecycle

### 5.2 2508 提出科学任务，2605 提供操作单位

2508 说科学 Agent 要会：

- 读文献；
- 提假设；
- 设计实验；
- 执行工具；
- 分析结果；
- 写作与验证；
- 根据反馈演化。

2605 则说明这些能力如果要长期可靠，就不能只靠一次性 reasoning，而要变成：

- represented skills；
- acquired skills；
- retrieved skills；
- composed skills；
- evolved skills；
- verified skills。

所以 2605 补的是 2508 的 **procedural layer**。

### 5.3 HTML 把“skill”变成科研基础设施

HTML 进一步说明：如果 skill 要用于科研，它必须连接：

- evidence；
- citation；
- memory；
- artifact；
- web retrieval；
- long-horizon context；
- verification benchmark。

这使我们的综述不只是“Agent Skills 在科研中的应用”，而是：

> 科研 Agent 的可持续自治需要 skill + memory + evidence + verification 的组合基础设施。

## 6. 三篇之间的张力

| 张力 | 表现 | 对我们写综述的影响 |
|---|---|---|
| process vs skill | 2508 讲科学流程，2605 讲通用 skill 生命周期 | 我们不能把 2508 的每个 workflow step 都自动称为 skill |
| essay vs evidence | HTML 观点强，但不全是同行评审证据 | HTML 的 thesis 要用 53 篇笔记和后续新论文验证 |
| autonomy vs reliability | Agentic Science 追求更高自治，Skills Survey 强调可维护执行 | 我们应突出“自治越高，越需要 skill reliability 和 verification” |
| evolution vs evidence preservation | skill/memory evolution 听起来积极，但 Memory Warning 等材料提示错误抽象风险 | 我们不能把 evolution 写成单向进步，要强调 trace、rollback、episodic evidence |
| general skill vs scientific closure | 通用 skill benchmark 不等于科学发现成功 | 需要引入 PaperBench、CORE-Bench、OpenScholar、human review、real-world validation |

## 7. 读完后三个原始问题的完整回答

### Q1：科研流程中的哪些步骤已经被 skill 化？

部分已经 skill 化，尤其是：

| 科研步骤 | 已有 skill 化证据 | 代表论文/系统 |
|---|---|---|
| 文献检索与综合 | search / retrieval / synthesis workflow | GPT Researcher, AutoSurvey, OpenScholar |
| 引用验证 | citation check procedure | OpenScholar, LLM Verifier |
| 代码执行与复现 | code execution / reproduction workflow | PaperBench, CORE-Bench, SUPER, Paper2Code |
| 审稿与反馈 | review checklist / aspect prompt / reviewer simulation | ReviewerGPT, Reviewer2, AgentReview |
| 经验沉淀 | reflection / workflow memory / code skill | Voyager, Reflexion, AWM, ExpeL |
| skill 管理 | add/modify/delete / structured representation | SkillOS, SSL, Agent Skills Spec |
| 记忆组织 | procedural/resource/episodic memory | MIRIX, A-MEM, Graph Agent Memory |

但还没有充分 skill 化的包括：

- wet-lab protocol execution；
- robotic experimentation；
- causal hypothesis testing；
- failed-branch reuse；
- long-horizon scientific project management；
- peer-reviewed real-world discovery validation。

### Q2：哪些系统只是 pipeline/tool-driven，而不是 skill-driven？

| 系统 | 判断 | 原因 |
|---|---|---|
| AI Scientist | pipeline-driven | 有端到端科研 pipeline，但没有显式 skill library / skill retrieval / skill evolution |
| Agent Laboratory | pipeline/tool-driven | 角色分工和工具执行明确，但可复用 skill 层弱 |
| AI-Researcher HKU | pipeline-driven | 自动化研究流程强，但 skill 表示和治理弱 |
| GPT Researcher | retrieval/synthesis-driven | 信息综合流程明确，但不做科学实验闭环 |
| Paper2Code | workflow-driven | 规划-分析-编码很适合 skill 化，但论文系统本身不一定维护 skill library |

这些系统的价值是证明 **科学工作流可被自动化**；它们的不足是尚未证明 **工作流可被维护为长期 skill infrastructure**。

### Q3：科研 Agent 的评估是否必须同时看 scientific closure 和 skill reliability？

答案是必须。

原因：

| 只看什么 | 会漏掉什么 |
|---|---|
| 只看最终论文 | 不知道引用是否真实、实验是否可复现、失败路径是否被隐藏 |
| 只看 skill 调用成功率 | 不知道科学结论是否可靠 |
| 只看 benchmark score | 不知道系统是否能迁移到真实科研 |
| 只看 human review | 成本高且审稿本身有偏差 |

因此我们需要双层评价：

1. **Skill reliability**：skill 是否可检索、可执行、可组合、可更新、可回滚？
2. **Scientific closure**：产出的假设、实验、引用、代码、结论是否可验证、可复现、可审计？

这正是我们综述区别于普通 Agent Skills 综述和普通 Agentic Science 综述的地方。

## 8. 完整证据表

| Source | Claim | Evidence Location | Supports Our Framework? | Caveat |
|---|---|---|---|---|
| 2605 Agent Skills Survey | skills 是 reusable procedural artifacts | Abstract / Introduction | 支持 skill lifecycle 作为纵轴 | 通用 Agent 视角，不专门讨论科研 |
| 2605 Agent Skills Survey | skills 协调 tools、memory、runtime context | Abstract | 支持“tool use 不等于 skill” | 需要在科研系统中逐篇判断是否真的有 skill |
| 2605 Agent Skills Survey | lifecycle 包括 representation、acquisition、retrieval、evolution | Abstract / survey organization | 直接支持我们的四阶段/多阶段 skill 分类 | 还缺 scientific closure |
| 2605 Agent Skills Survey | open challenges 包括 quality control、interoperability、safe updating、long-term capability management | Conclusion / challenges | 支持我们讨论 skill governance | 没有给出科学发现专用 benchmark |
| 2508 Agentic Science Survey | Agentic Science 是 AI for Science 从辅助走向 full scientific agency 的阶段 | Abstract / Introduction | 支持 autonomous scientific discovery 横轴 | 对 skill 层展开不足 |
| 2508 Agentic Science Survey | 科学发现可被组织为闭环 workflow | Introduction / workflow sections | 支持 Knowledge → Hypothesis → Experiment → Analysis → Validation | 不等于这些环节已被 skill 化 |
| 2508 Agentic Science Survey | 关键挑战包括 reliability、reproducibility、novelty、transparency、governance | challenges sections | 支持我们强调 verification/evidence | 需要具体系统和 benchmark 补证据 |
| 2508 Agentic Science Survey | Agentic Science 涉及 tool use、memory、multi-agent collaboration、evolution | method capability sections | 支持将 memory 和 skill evolution 纳入综述 | 它主要是领域综述，不给 skill schema |
| 本地 HTML | skill 是 Agent 能力单元，而不是 prompt/tool/plugin | Section II | 支持 skill-centric 立场 | essay/report，需论文证据校准 |
| 本地 HTML | ARA、SkillOS、SSL 可读作同一 skill lifecycle 的不同阶段 | Section VIII | 支持我们把 representation / acquisition / retrieval / evolution 连起来 | 三者原论文未必互引，需要谨慎写成“我们归纳” |
| 本地 HTML | citation、memory、evidence graph 是 zero-hallucination discovery 的基础 | Section XI | 支持 evidence-centered skill-driven discovery | 仍需 OpenScholar、Memory Warning 等论文支撑 |
| 本地 HTML | web retrieval 应拆成 query / fetch / synthesize | Section XII | 支持 Knowledge Grounding 细分 | 工具生态变化快，需要更新 |
| 本地 HTML | long-horizon 难点来自 long horizon / large context / high frequency | Section XIII | 支持未来补 long-horizon 科研 Agent 文献 | 仍是框架分析，不是单一实验结论 |
| 本地 HTML | open questions 包括 composition、skill evolution、evidence web、intra-task learning | Section XIV | 支持后续论文池扩展方向 | 需要新论文验证 |

## 9. 我们自己的二维归纳框架：读完后的正式版

### 9.1 横轴：Scientific Discovery Workflow

| 一级阶段 | 二级能力 | 当前证据状态 |
|---|---|---|
| Knowledge Grounding | literature search, citation verification, knowledge graph, factuality | 证据较多：BrowseComp、AutoSurvey、OpenScholar、SimpleQA、HLE |
| Hypothesis Generation | novelty, feasibility, diversity, analogy, causal reasoning | 证据中等：IdeaBench、Stanford Human Study；实验验证不足 |
| Experiment Design | protocol design, variable control, resource planning, safety constraints | 证据偏弱：多数系统只做计算实验，湿实验不足 |
| Execution | code execution, simulation, lab automation, robotic experimentation | 计算执行证据多：MLE-Bench、ScienceAgentBench、CORE-Bench；lab automation 缺 |
| Result Analysis | statistics, visualization, error analysis, multimodal interpretation | 分散在系统论文中，缺统一基准 |
| Synthesis | paper writing, artifact construction, review response | 证据较多：AI Scientist、Paper2Code、ARA、Reviewer2 |
| Verification | reproduction, peer review, citation checking, benchmark grading | 证据强：PaperBench、CORE-Bench、OpenScholar、LLM-Verifier |
| Evolution | memory update, skill update, failed-branch reuse, long-horizon learning | 证据正在形成：SkillOS、A-MEM、Memory Warning、MIRIX |

### 9.2 纵轴：Skill Lifecycle

| 一级阶段 | 二级机制 | 当前证据状态 |
|---|---|---|
| Representation | prompt skill, code skill, workflow skill, artifact skill, memory skill, protocol skill | 较强：Anthropic Skills, Agent Skills Spec, SSL, ARA |
| Acquisition | human-written, trajectory-derived, literature-derived, failure-derived, benchmark-derived | 中等：Voyager、AWM、ExpeL、Reflexion；科研场景不足 |
| Retrieval | keyword, embedding, structure-aware, stage-aware, resource-aware | 较强：SSL、Perplexity guide、Voyager、OpenScholar |
| Composition | sequential, hierarchical, multi-agent, tool-chain, protocol-mediated | 中等：Agent Laboratory、GStack、MMP；严格评估不足 |
| Execution | tool use, code run, web search, lab action, simulation | 计算场景较强，lab action 弱 |
| Evolution | reflection, RL curator, memory consolidation, versioning, deletion | 早期：SkillOS、A-MEM、Memory Warning；版本治理不足 |
| Verification | unit test, benchmark, citation check, human review, replication, real-world validation | 较强但分散：SkillsBench、PaperBench、OpenScholar、Stanford Human Study |

## 10. 可以写进未来综述的核心判断

### 判断 1：现有自动科研系统多为 pipeline-driven，而不是完整 skill-driven

AI Scientist、Agent Laboratory、AI-Researcher 等证明端到端科研流程可以被 agent pipeline 组织，但它们通常没有显式 skill 表示、检索、组合、演化和淘汰机制。因此它们是 skill-driven discovery 的重要前置证据，而不是充分实现。

### 判断 2：Agent Skills 综述补上了 Agentic Science 缺失的 procedural layer

2508 告诉我们科学发现要覆盖哪些阶段；2605 告诉我们这些阶段中的操作性知识如何变成 reusable procedural artifacts。两者结合后，才形成可证实的 “Scientific Workflow × Skill Lifecycle” 框架。

### 判断 3：科研 skill 必须绑定 evidence，否则只是更复杂的 prompt

本地 HTML 的 zero-hallucination evidence、OpenScholar 的引用验证、PaperBench 的复现评分、Memory Warning 的情景痕迹警告共同说明：科研 skill 不能只保存抽象步骤，还必须保存证据、上下文、失败路径和验证记录。

### 判断 4：skill evolution 是未来重点，但也是风险点

SkillOS、A-MEM、ExpeL、Reflexion 支持从经验中更新能力；Memory Warning 则提示持续整合会造成错误抽象。因此 evolution 不能写成单向进步，必须包含 validation、rollback、versioning、episodic trace preservation。

### 判断 5：下一轮文献扩展应围绕缺口，而不是泛读

最明显缺口是：

- wet-lab / robotic lab autonomous discovery；
- real-world biomedical / chemistry / materials discovery；
- scientific hypothesis generation with experimental validation；
- skill composition benchmark；
- long-horizon scientific project benchmark；
- governance / authorship / safety / peer-review policy。

## 11. 最终定位

这三篇读完后，我们的综述不应定位为：

> 又一篇 autonomous scientific discovery survey。

也不应定位为：

> 又一篇 agent skills survey。

更合适的定位是：

> A survey that uses the agent skill lifecycle to analyze the procedural infrastructure of agentic autonomous scientific discovery.

中文可以写成：

> 本综述从 skill lifecycle 视角重新审视自动科学发现 Agent，关注科研流程中的操作性知识如何被表示、获取、检索、组合、执行、演化和验证。

这个定位是稳健的，因为：

1. 2508 提供科学发现流程；
2. 2605 提供 skill 生命周期；
3. 本地 HTML 提供 academic workflow infrastructure；
4. 我们已有 53 篇笔记可以作为初始 evidence base；
5. 后续新增论文可以继续检验、扩展或修正这个框架。

