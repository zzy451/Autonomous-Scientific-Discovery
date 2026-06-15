# 综述骨架：面向自主科学发现的多智能体与演化式工作流系统

> 本骨架围绕自主科学发现中的多智能体工作流系统、演化/搜索机制、科学产物以及验证与评估闭环来组织相关文献。
> 本文与既有 Agentic Science 综述的差异不只是覆盖了更新的工作，而是以 **multi-agent** 作为独立切入点，解释自主科学发现为什么需要多智能体组织，以及“多”在科学发现系统中具体体现为什么。

## 拟定题目

推荐题目：

**A Survey of Multi-Agent Workflow Systems for Autonomous Scientific Discovery**

备选题目：

- **Multi-Agent Workflow Systems for Autonomous Scientific Discovery: Coordination, Artifacts, and Verification**
- **From AI Scientists to Multi-Agent Scientific Workflows: Coordination, Search, and Evidence Closure**
- **Agentic Scientific Discovery as Multi-Agent Workflow Systems: Coordination, Research Artifacts, and Harness Evolution**
- **Multi-Agent and Evolutionary Workflow Systems for Autonomous Scientific Discovery: Artifacts, Harnesses, and Verification**

推荐题目首先突出本文的核心切入点：**multi-agent**。本文不是一般 AI4S 综述，也不是泛化 Agentic Science 综述，而是研究 autonomous scientific discovery 为什么越来越需要被组织为多智能体工作流系统。也就是说，全文主线是多智能体如何分工、协调、交接、批评、验证和接受人类监督。

在这个主线之下，**evolutionary/search-based mechanisms** 是第二层机制，用来解释多智能体工作流如何跨迭代改进。这里的演化对象主要有两类：一类是 **scientific research artifacts**，包括假设、代码、notebook、证明、实验方案、分析结果、论文草稿和失败分支；另一类是 **agentic harness**，即支撑这些产物生成、执行、路由、记忆、评分、验证、交接和治理的系统脚手架。

因此，本文讨论的 evolution 不是 agent 本体的遗传式进化或模型训练，而是多智能体科研工作流中 **科学研究产物** 与 **agentic harness** 在反馈、验证和人类监督下的持续改进。

因此，正式写作中建议避免把题目写成 **evolutionary agents**。更稳妥的表达是 **evolutionary workflow systems**、**artifact evolution** 或 **harness evolution**，这样可以清楚区分本文与一般多智能体系统综述、Agent Skills 综述和泛化 Agentic Science 综述。

## 文章定位

本文继承从 **AI for Science** 到 **Agentic Science** 的宏观转向，但不做一般性的 AI4S 应用综述，也不做泛化的科学智能体综述。本文的重点是系统组织方式：自主科学发现如何通过多个专门化智能体、协调协议、可搜索的科学产物以及验证边界来落地。

| 参照对象 | 主要关注点 | 在本文中的作用 |
|---|---|---|
| From AI for Science to Agentic Science | 从模型中心的 AI4S 走向智能体化科学发现 | 提供“科学发现流程正在被 agent 化”的宏观叙事 |
| AI Scientist 与 autonomous discovery systems | 端到端科研自动化 | 提供与单智能体或 pipeline 式系统对比的基线 |
| Science Earth / EACN | 从固定多智能体团队走向开放 scientific capability network | 帮助本文把 agent 从 LLM prompt role 拉回更经典的主动实体定义，并支撑对 multi-agent 中“多”的扩展定义 |
| Agent skills 与 academic workflow 报告 | 技能、产物、记忆、引用验证与可复用流程 | 为持久运行的多智能体科研工作流提供基础设施视角 |

核心定位：

> 自主科学发现应被理解为多智能体工作流系统的设计问题：科学任务被拆解为不同角色，通过协调协议组织协作，通过搜索与演化机制改进科学研究产物及其 agentic harness，并通过验证、评估与人类监督形成科学闭环。

### 与既有 Agentic Science 综述的区别

`From AI for Science to Agentic Science` 的主要价值在于说明 AI4S 正在从模型中心走向智能体化科学发现。本文在此基础上进一步收窄问题：**如果自主科学发现正在变成 agentic workflow，那么这些 workflow 为什么越来越需要 multi-agent organization？**

因此，本文不是简单补充更新论文，也不是按学科领域重写一遍 Agentic Science 综述，而是把 multi-agent 作为核心分析对象，回答三个更具体的问题：

1. **为什么需要多智能体**：科学发现天然包含不同角色、证据标准、执行环境和验证边界，单个 agent 难以可靠覆盖生成、批评、执行、分析、验证和责任归因。
2. **“多”具体体现在哪里**：多的不只是 agent 数量，也包括角色、同角色候选、层级管理、工具/实验/证明能力、证据标准和开放网络连接。
3. **多智能体如何改变科学发现**：它将科学发现从单次生成转化为多角色协作、产物交接、冲突暴露、搜索演化和证据闭环。

Science Earth 对本文的特殊价值在于，它提醒我们不能把 agent 简化为“一个 LLM 角色”或“一个 prompt persona”。在更经典的定义中，agent 是能够承担任务、感知或接收环境状态、选择行动、调用能力、产生可交接结果并接受评价的主动实体。在科学发现中，这个实体可以是 LLM agent，也可以是证明器、仿真集群、实验机器人、数据分析 pipeline、数据库接口或人类专家。Science Earth 的 EACN 因此不是一个普通新案例，而是帮助本文把 multi-agent 从固定角色团队扩展为开放科学能力网络的概念锚点。

### 多智能体中的“多”

本文将 autonomous scientific discovery 中的 multi-agent 拆成六个层次：

| “多”的层次 | 含义 | 代表系统 |
|---|---|---|
| 主体形态之多 | agent 不限于 LLM prompt role，也可以是能够承担任务、调用能力、提交产物并接受评价的主动实体 | Science Earth, Robin, AlphaProof Nexus |
| 角色之多 | 一个科学任务被拆成 planner、literature agent、hypothesis agent、critic、executor、analyst、verifier、human PI 等角色 | Co-Scientist, Virtual Lab, Agent Laboratory |
| 实例之多 | 同一类角色可以有多个实例并行探索，例如多个 hypothesis generators、prover subagents、candidate reviewers | Co-Scientist, AlphaProof Nexus, MC-NEST |
| 层级之多 | 一个 coordinator / supervisor / manager agent 可以调度多个 worker agents 或专门模块 | Co-Scientist, Agent Laboratory, Kosmos |
| 能力之多 | 多智能体系统连接的不只是 LLM agent，还包括检索器、代码执行器、仿真器、证明器、数据库、机器人实验室和人类专家 | Robin, AlphaProof Nexus, ERA, Science Earth |
| 证据标准之多 | 不同 agent 或能力产生的结果遵循不同验证边界，需要 citation、code execution、formal proof、human review、physical validation 等多种证据标准互相约束 | OpenScholar, AlphaProof Nexus, Robin, Science Earth |

这个定义使本文的切入点区别于一般“多 agent 工具箱”综述：在科学发现中，多智能体的意义不只是让多个模型聊天，而是把异质科学能力组织成可交接、可冲突、可演化、可验证的发现网络。

## 核心论点

> Autonomous scientific discovery is best understood not as a single AI scientist replacing researchers, but as multi-agent workflow systems that decompose scientific labor, coordinate specialized roles, exchange evidence-bearing research artifacts, evolve both candidate artifacts and the agentic harness that produces them, and close the loop through verification, evaluation, and human oversight.

对应的中文表述：

> 自主科学发现的关键并不是一个“AI 科学家”取代研究者，而是一类多智能体工作流系统：它们将科学劳动拆解为多个专门角色，协调这些角色协作，交换带有证据状态的科学研究产物，对候选产物及其生成、执行、验证和交接 harness 进行搜索与演化，并通过验证、评估和人类监督形成闭环。

在这个视角下，**multi-agent coordination** 解释科学劳动如何分布在文献检索、假设生成、批评、执行、分析、验证和人类决策之间；**evolutionary/search-based mechanisms** 解释科学研究产物以及承载这些产物的 harness 如何随迭代不断改进；**verification and evaluation** 则决定一个输出能否从看似合理的 agent response 变成可信的 scientific artifact。

Science Earth 进一步扩展了这一论点：多智能体不必局限于预设角色的封闭团队，也可以是开放的 scientific capability network。通过 EACN 这样的协议，科学能力可以被发现、竞标任务、协商任务归属，并在不同证据标准之间进行 adjudication。这说明 multi-agent 不只是系统实现细节，而是自主科学发现走向开放、跨学科和长周期协作时的组织原则。

因此，本文中的“演化”不应只理解为 agent 本体的进化，也不应泛化为所有系统组件都在自我训练。本文将演化范围收束为两个对象：

| 演化对象 | 含义 | 代表系统 |
|---|---|---|
| 科学研究产物演化 | 假设、代码、notebook、证明、实验方案、分析结果、论文草稿、失败分支等科学研究产物被生成、执行、评分、选择、改写、归档和复用 | Co-Scientist, AlphaEvolve, ERA, AlphaProof Nexus, MC-NEST, Jupiter, SciNav, ARA |
| Harness 演化 | 生成、执行、检索、路由、协调、记忆、评分、验证和交接科学研究产物的系统脚手架发生更新，包括角色分配、能力选择、工具链、记忆结构、任务拓扑、reputation/trust、verification gates 和 human checkpoints | Science Earth, Kosmos, SkillOS, STELLA, MIRIX, A-MEM, Mesh Memory Protocol, ARA |

## 章节结构

| 章节 | 功能 | 与主线的关系 |
|---|---|---|
| 1. 引言与背景 | 引入从 AI4S 到 agentic workflow systems 的转变 | 说明为什么应从 workflow 层面研究自主科学发现 |
| 2. 核心概念与分析维度 | 定义 agent、tool、capability、harness，并提出理解多智能体科学发现系统的基本维度 | 为全文提供统一术语和分析语言，但不作为并列主线 |
| 3. 为什么需要多智能体？ | 解释多智能体组织的收益、设计原则和风险 | 构成全文的中心论证 |
| 4. 科学发现中的多智能体工作流模式 | 梳理角色分解、交接、批评、人类介入和共享记忆 | 展开主要系统分类 |
| 5. 多智能体工作流中的演化/搜索机制 | 说明搜索与演化如何嵌入多智能体工作流 | 解释科学研究产物和 agentic harness 如何跨迭代改进 |
| 6. 科学产物、执行载体与验证边界 | 比较文献、代码、证明、仿真、实验室和审稿系统 | 说明不同载体如何改变角色、协议、产物和验证方式 |
| 7. 评估、基准与证据闭环 | 区分输出验证和系统评估 | 说明如何评估多智能体/演化式科研工作流 |
| 8. 基础设施、开放问题与结论 | 总结记忆、工具、技能、平台和未解决问题 | 指出持久、可审计科学发现所需的系统条件 |

建议写作重心：

| 主题 | 角色 |
|---|---|
| 多智能体工作流系统 | 第一主线 |
| 演化/搜索机制 | 第二主线，嵌入多智能体工作流中；对象包括科学研究产物和 agentic harness |
| 验证、评估与证据闭环 | 科学可信度层 |
| 产物、执行载体、记忆、工具、技能与平台 | 支撑层 |
| 一般 AI4S 背景 | 只作简要引入 |

## 主要贡献

1. **提出一个以多智能体为中心的自主科学发现分析框架**：以 agent、tool、capability、harness 的概念边界为基础，从科学工作流、智能体角色、协调协议、演化机制、科学产物和验证边界等维度解释现有系统。
2. **重新界定自主科学发现中的 agent 与 multi-agent**：借助 Science Earth / EACN 将 agent 从 LLM prompt role 扩展为能够承担任务、调用能力、提交产物并接受评价的主动实体，并区分 agent、tool、capability 和 harness。
3. **定义自主科学发现中 multi-agent 的“多”**：区分主体形态之多、角色之多、实例之多、层级之多、能力之多和证据标准之多，说明多智能体不是简单增加 agent 数量，而是科学劳动、科学能力和验证边界的系统化组织。
4. **明确回答为什么科学发现需要多智能体组织**：将角色专业化、独立批评、并行探索、产物交接、责任边界和人类检查点识别为多智能体系统相对于单智能体 pipeline 的关键优势。
5. **系统讨论多智能体科学发现的特有风险**：包括集体幻觉、虚假共识、协调成本、共享记忆污染、评审偏差、角色坍缩、责任扩散以及提示注入或工作流攻击。
6. **统一理解演化/搜索式发现机制**：将假设搜索、代码演化、形式化证明搜索、基准驱动改进和失败分支复用视为科学研究产物演化；将能力选择、工具链更新、记忆更新、声誉更新、任务涌现和验证门槛调整视为 harness 演化。
7. **从执行载体角度比较验证边界**：分析文献、代码、notebook、形式化证明、仿真、物理实验室、人类实验室和同行评审如何要求不同的角色、产物、协调协议和验证方式。
8. **提出面向多智能体工作流的评估维度**：包括角色效用、协调质量、产物交接质量、冲突解决、集体幻觉率、协调成本、人类检查点有效性和责任可追踪性。

## 核心文献分层

正式写作时不应把所有论文平铺。建议将文献分为三层。

### 第一层：核心锚点系统

这些系统应作为正文中反复使用的核心案例。

| 工作 | 主要用途 |
|---|---|
| Co-Scientist | 多智能体假设生成、批评、排序、锦标赛和演化 |
| Robin | lab-in-the-loop 的多智能体科学发现工作流 |
| Virtual Lab | 通过 PI 和 specialist agents 展示科学角色分解 |
| Agent Laboratory / AI Scientist Nature | 端到端科研工作流，并与单智能体或 pipeline 式自动化对照 |
| AlphaEvolve | 面向可执行科学/算法产物的演化式搜索 |
| ERA | empirical scientific software 搜索、tree search 和 sandbox scoring |
| AlphaProof Nexus | formal verifier-guided proof search 与可机器检查的证明产物 |
| Kosmos | 长周期 world model、记忆和证据链接报告 |
| Science Earth | 从固定多智能体团队推进到开放 scientific capability network，支撑“多”的定义和开放网络协作 |

### 第二层：机制支撑文献

这些工作用于支撑具体机制，应选择性引用。

- AgentReview、Reviewer2、ReviewerGPT、LLM-as-a-Verifier：批评、审稿、评判和重复成对验证。
- MIRIX、A-MEM、Graph Agent Memory、Mesh Memory Protocol：多智能体记忆、共享状态与 provenance。
- MC-NEST、Jupiter、SciNav、DatawiseAgent：假设搜索、notebook 轨迹搜索和科学代码搜索。
- OpenScholar、SciVer、SPOT-a、SafeScientist：证据 grounding、验证、安全和失败检测。
- ARA、PaperBench、CORE-Bench：科研产物、复现和论文级评估。
- Science Earth / EACN：capability discovery、competitive bidding、cross-regime adjudication 和 reputation-weighted trust。

### 第三层：背景与补充证据

这些工作主要用于背景、基础设施或局部补证。

- From AI for Science to Agentic Science。
- Agent Skills Survey。
- 本地 research-report HTML 中关于 skills、artifacts、memory 和 verification 的材料。
- SciToolAgent、Toolformer、ToolLLM、Gemini for Science。
- self-driving lab 综述和机器人实验室系统。
- governance 和 responsible publishing 相关材料。

## 1. 引言与背景

### 开场动机

引言可以从 2026 年的一组信号切入：

- Nature 在同一阶段发表 Co-Scientist、Robin 和 ERA，并将其概括为 AI agent teams 加速科研。
- OpenAI 报告了与 unit-distance 问题相关的 AI 生成反例，随后由人类数学家审查。
- Google DeepMind 的 AlphaProof Nexus 推进了面向数学问题的 formal proof search。
- Gemini for Science 将 agentic science 能力放入科研工具生态，而不是停留在孤立原型。
- Science Earth 提出 planet-scale scientific runtime 和 EACN 协议，展示多智能体科学发现可以从固定团队进一步走向开放能力网络。

这些例子共同服务于一个中心判断：

> Agentic science 的可见前沿正在从孤立的 AI scientist 转向协调式工作流系统。在这类系统中，多个智能体、搜索过程、工具、验证器和人类共同生产科学产物。

### 从 AI4S 到 Agentic Workflow Systems

传统 AI for Science 往往以模型为中心：模型预测、生成、优化、分类或加速某个特定科学任务。Agentic Science 改变了分析单位：智能体能够规划、搜索文献、调用工具、编写并执行代码、设计实验、检查输出、修订计划，并与人类专家交互。

本文进一步关注下一层系统组织问题：

> Agentic Science 说明 AI 可以参与科学工作流；本文研究这些工作流如何被组织为多智能体系统。

### 研究缺口

现有综述和讨论通常存在以下不足：

- 关注 AI4S 的模型能力，但弱化 workflow organization 和 multi-agent coordination。
- 将自主科学发现视为端到端 pipeline，但没有充分解释角色分解、批评、审稿和产物交接。
- 强调 LLM hypothesis generation，但不足以解释 AlphaEvolve、ERA、AlphaProof Nexus 等搜索/演化系统。
- 将 verification 和 governance 视为后处理问题，而不是科学闭环的必要条件。
- 缺少同时覆盖 self-driving laboratories、formal mathematics、computational discovery、scientific software 和 peer review 的统一系统视角。

### 研究问题

1. 自主科学发现中 multi-agent 的“多”具体指什么？
2. 为什么自主科学发现应被组织为多智能体工作流系统，而不是单智能体 pipeline？
3. 科学发现工作流如何被拆解为不同的专门化智能体角色？
4. 多智能体系统如何协调生成、批评、排序、执行、记忆和综合？
5. 演化/搜索机制如何在这些工作流内部改进科学研究产物，并调整生成、执行、验证和交接这些产物的 harness？
6. 不同执行载体如何塑造智能体角色、协调协议、产物类型和验证边界？
7. 多智能体和演化式科学工作流应如何被验证、评估和治理？

## 2. 核心概念与分析维度

本章提供全文写作所需的基本概念和分析语言。它并不是与后续章节并列的另一套分类体系，而是为后文讨论具体系统提供共同问题意识：一个系统中的 agent 是什么，它们如何协作，操作什么科学产物，如何在反馈中改进，以及输出如何被验证。

**图 1：Multi-Agent Scientific Discovery Workflow System**

建议图中包含以下层次：

- 人类目标与科学监督。
- 科学工作流阶段。
- 智能体角色。
- 协调协议。
- 演化/搜索循环。
- 科学产物与执行载体。
- 验证、评估、provenance 和治理。

### Agent、Tool、Capability 与 Harness

为了避免把 multi-agent 误解为“多个 LLM 角色互相聊天”，本文需要先明确四个概念边界。Science Earth / EACN 提供了一个有用参照：在开放科学发现网络中，参与者不一定都是 LLM agent，而是能够被发现、承接任务、提交产物、接受评价并与其他能力节点协作的科学能力实体。

| 概念 | 本文定义 | 在科学发现中的例子 |
|---|---|---|
| Agent | 能够承担任务、选择行动、调用工具或能力、产生可交接产物并接受验证或评价的主动实体 | planner agent, hypothesis agent, verifier agent, proof-search agent, human expert |
| Tool | 被 agent 调用的相对被动接口，本身通常不负责目标分解和责任承担 | search API, code interpreter, database, simulator endpoint, lab instrument interface |
| Capability | 可完成某类科学操作的能力节点，可以由 agent、tool chain、模型、实验平台或人类专家构成 | theorem proving capability, wet-lab assay capability, simulation capability, data-analysis pipeline |
| Harness | 组织 agent、tool、capability、memory、artifact store、verifier、human checkpoint 和 governance rule 的系统脚手架 | EACN, Co-Scientist orchestration, ERA sandbox/tree-search harness, ARA artifact protocol |

在这个定义下，multi-agent 的“多”不是简单增加 LLM 数量，而是把多个主动实体、能力节点、证据标准和执行载体组织成能够协作、竞争、交接、验证和演化的 scientific discovery network。Science Earth 的重要性正在于它把 fixed-role agent team 推进到 open capability network：能力可以被发现，任务可以被竞标，任务归属可以协商，不同证据标准之间可以 adjudicate，声誉和信任也会影响后续任务分配。

### 系统分析维度

以下维度用于刻画多智能体科学发现系统的基本结构。正式写作时，每个核心系统不需要机械地逐项展开，但应能够在正文或对比表中回应这些问题。

| 分析维度 | 核心问题 | 示例 |
|---|---|---|
| 科学工作流阶段 | 系统自动化或辅助科学发现的哪一步？ | grounding, hypothesis, design, execution, analysis, synthesis, verification, iteration |
| 智能体角色 | 科学劳动如何被分工？ | planner, literature agent, hypothesis agent, critic, executor, analyst, verifier, human PI |
| 协调协议 | 智能体如何合作、分歧、交接和决策？ | pipeline, hierarchy, debate, tournament, review, shared blackboard, human checkpoint |
| 搜索/演化机制 | 候选科学研究产物及其 agentic harness 如何被改进？ | generate-test-refine, tree search, MCTS, population, mutation, verifier-guided search, capability bidding, reputation update, emergent task decomposition |
| 科学产物/执行载体 | 系统操作的科学对象是什么？ | citation, code, notebook, proof, simulation, experiment, review |
| 验证边界 | 输出如何成为可信证据？ | citation support, code execution, formal proof, expert review, physical validation |

### 与章节结构的关系

| 后续章节 | 与这些分析维度的关系 |
|---|---|
| 第 3 章：为什么需要多智能体？ | 从角色、协议、验证边界解释单智能体为何难以覆盖完整科学发现 |
| 第 4 章：多智能体工作流模式 | 重点展开智能体角色与协调协议 |
| 第 5 章：演化/搜索机制 | 重点展开科学产物、搜索/演化机制和 harness |
| 第 6 章：科学产物与验证边界 | 重点展开执行载体与验证边界 |
| 第 7 章：评估与基准 | 将这些维度转化为 role utility、coordination quality、handoff quality、verification cost 等评估指标 |
| 第 8 章：基础设施与开放问题 | 讨论哪些工具、记忆、技能和平台条件能支撑这些维度长期稳定运行 |

## 3. 为什么需要多智能体？收益、设计原则与失败模式

本章提供采用多智能体视角的核心理由。

### 相比单智能体 pipeline 的收益

| 收益 | 对科学发现的意义 | 代表性证据 |
|---|---|---|
| 角色专业化 | 文献检索、假设生成、实验设计、代码执行、分析和验证可由不同角色承担 | Co-Scientist, Robin, Virtual Lab, Agent Laboratory |
| 独立批评 | critic、reviewer 或 verifier agents 可用独立标准检查 generator 的输出 | AgentReview, LLM-as-a-Verifier, Co-Scientist |
| 并行探索 | 可同时探索多个假设、实验分支、代码实现或证明路径 | Co-Scientist, AlphaProof Nexus, MC-NEST |
| 产物交接 | 中间输出可被后续智能体检查、复用、修订和验证 | ARA, Kosmos, ERA, PaperBench |
| 责任边界 | 可区分生成、验证、批准和执行责任 | Robin, OpenAI Unit Distance, AI Responsible Publishing |
| 人类/实验室检查点 | 可在关键位置插入人类专家、实验室、审稿和安全审批 | Robin, Co-Scientist, AI Scientist Nature |

### 设计原则

- **明确角色，而不是模糊 persona**：每个智能体应有清晰输入、输出、权限和失败行为。
- **围绕产物协作，而不是围绕聊天记录协作**：多智能体协作应以可检查科学产物为中心，而不是依赖非结构化对话历史。
- **交接必须携带证据状态**：角色之间的每次交接都应包含 provenance、support status 和 unresolved questions。
- **验证路径应保持独立**：verifier 不应只是复述 generator 的理由。
- **设置 promotion gates**：假设、结果、引用和实验分支进入 shared project state 前应经过检查。
- **进行角色消融**：系统应测试每个角色的边际贡献，而不是默认 agent 越多越好。

### 多智能体科学发现的特有失败模式

| 失败模式 | 描述 | 影响 |
|---|---|---|
| 集体幻觉 | 多个智能体共同强化同一个无支撑 claim | 共识不等于证据 |
| 虚假共识 | debate 或 review 看似收敛，但依赖同一个有问题来源 | 一致性会制造虚假的可靠感 |
| 协调成本过高 | 通信、交接和审查成本超过角色分解带来的收益 | 多智能体系统可能不如单智能体基线高效 |
| 共享记忆污染 | 错误摘要进入共享记忆并影响后续角色 | 错误会沿工作流传播 |
| judge bias / role collapse | critic、judge 或 reviewer 没有保持独立性 | 评估机制退化为自我确认 |
| 责任扩散 | 难以追踪谁生成、检查、批准或执行了某个动作 | 问责变得困难 |
| 安全与提示攻击 | 共享文档、审稿流程和工具调用引入新的攻击面 | 削弱治理与可信交互 |

## 4. 科学发现中的多智能体工作流模式

本章梳理系统模式，重点应放在机制上，而不是逐篇论文罗列。

### 角色专门化的研究团队

核心论点：

> 多智能体科学系统的能力来自对科学发现任务的角色化拆解，但角色分离只有在具备明确接口、科学产物和验证门槛时才真正有效。

核心论文：

- Co-Scientist：generation、reflection、ranking、evolution 和 meta-review。
- Robin：Crow、Falcon、Finch agents 以及 lab-in-the-loop workflow。
- Virtual Lab：PI 和 specialist scientist roles。
- Agent Laboratory：PhD、Postdoc、ML Engineer 和 Professor 风格角色。
- AgentReview：reviewer、author 和 area-chair simulation。

### 协调、通信与交接

典型机制：

- sequential handoff。
- hierarchical delegation。
- role-based pipeline。
- shared artifact store。
- task-state tracking。
- conflict resolution。
- human checkpointing。
- lab-in-the-loop handoff。

关键观点：

多智能体科学发现不应只通过最终输出评估，还应评估中间产物是否可检查、可转移、可复用，并且是否绑定证据。

### 批评、辩论、锦标赛与审稿

典型机制：

- pairwise comparison。
- Elo tournament。
- reviewer-style critique。
- meta-review。
- round-robin verifier。
- judge consistency。

代表性论文：

- Co-Scientist：hypothesis tournament and evolution。
- Robin：LLM-judged candidate ranking。
- LLM-as-a-Verifier：repeated pairwise verification。
- AgentReview、Reviewer2、ReviewerGPT：review-agent evidence。
- Stanford Human Study：AI idea evaluation 的边界。

### Human-in-the-Loop 与 Lab-in-the-Loop

核心论点：

> 人类监督并不只是自主性的不足。在科学场景中，人类专家、实验室和审稿机制往往正是 agentic workflow 获得合法性和可信度的方式。

代表性论文：

- Robin：人类实验室执行实验并上传结果。
- Co-Scientist：scientist-in-the-loop hypothesis validation。
- Adaptive AI Decision Interface：human-AI material discovery interface。
- AI Scientist Nature：真实 workshop peer review。
- OpenAI Unit Distance：人类数学家和外部专家验证 AI 生成的数学输出。

### 共享记忆、Provenance 与产物管理

代表性论文：

- Kosmos：structured world model 和 evidence-linked reports。
- MIRIX：multi-type memory。
- A-MEM、Graph Agent Memory、Mesh Memory Protocol。
- ARA：agent-native research artifacts。

关键观点：

多智能体科学发现不应使用无差别的共享记忆池，而应区分 role-private memory、shared project memory、evidence memory 和 promotion gates。

## 5. 多智能体工作流中的演化/搜索机制

演化与搜索方法应被理解为多智能体工作流内部的优化机制，而不是另一个平行的综述主题。这里的演化范围限定为两类对象：一类是 **scientific research artifacts**，即科学研究过程中被生成、执行、验证和复用的产物；另一类是 **agentic harness**，即承载这些产物生成、路由、执行、记忆、验证、交接和治理的系统脚手架。

### 两类演化对象

核心论点：

> 演化/搜索式工作流将科学发现视为对科学研究产物和 agentic harness 的联合优化过程。系统不仅可以搜索更好的假设、代码、证明、实验方案和报告，也可以调整用于产生这些产物的角色分配、工具链、记忆结构、评分器、验证门槛和协作拓扑。

第一类是 **scientific research artifact evolution**，即科学研究产物被生成、执行、评分、选择、变异、重组、归档，并重新引入多智能体工作流。可演化产物包括：

- 假设。
- 代码实现。
- notebooks。
- proof sketches。
- 实验方案。
- 分析结果和数据解释。
- reports / paper drafts。
- failed branches。

第二类是 **harness evolution**，即系统根据任务表现、confidence、reputation、memory、skill update、execution feedback 或 human feedback，调整产生科学研究产物的脚手架。这里的 harness 包括：

- agent roles 和 role assignment。
- coordinator / supervisor / worker 的层级关系。
- tool chains、code sandbox、proof assistant、simulation environment 和 lab interface。
- memory、artifact store、provenance record 和 failed-branch archive。
- ranking / scoring / verifier / reviewer。
- promotion gates、human checkpoints 和 safety/governance constraints。
- capability registry、task bidding、reputation-weighted trust 和 open capability network。

Science Earth 的 EACN 是 harness evolution 的代表：capability 可以被发现、竞标任务、协商任务归属，并通过 reputation-weighted trust 累积或失去后续任务机会；新的 sub-task 也可以由不同结果之间的冲突、失败、异常或 evidence mismatch 触发。SkillOS、STELLA、A-MEM、MIRIX、Mesh Memory Protocol 和 ARA 则分别从技能管理、工具池、记忆更新、跨 agent 语义交换和研究产物协议层面支撑 harness 的演化。

### 假设搜索与候选选择

代表性论文：

- Co-Scientist：hypothesis generation、ranking 和 evolution。
- MC-NEST：Monte Carlo tree search over hypotheses。
- ResearchAgent：iterative idea generation。
- Sparks of Science：structured hypothesis data。
- RINoBench、AI Idea Bench、LiveIdeaBench：novelty 和 idea evaluation boundaries。

关键观点：

假设生成应被理解为在新颖性、可行性、因果合理性、证据和验证约束下的搜索过程。

### 代码与 Notebook 中心的演化

代表性论文：

- AlphaEvolve：generate-test-refine algorithmic discovery。
- ERA：通过 LLM rewriting、tree search 和 sandbox scoring 生成 empirical software。
- Jupiter：value-guided notebook trajectory search。
- SciNav：scientific coding search。
- DatawiseAgent：notebook-centric data science automation。

关键对比：

AI Scientist 生成论文；ERA 和 AlphaEvolve 演化可执行科学产物。

### 形式化证明搜索

代表性论文：

- AlphaProof Nexus：Lean proof sketches、prover subagents、AlphaProof tool、rating agents 和 population database。
- OpenAI Unit Distance：AI-generated counterexample with human verification。
- LLM Verifier：general verification framework。

关键对比：

- AlphaProof Nexus 是 verification-first 系统，其形式化证明产物可被机器检查。
- OpenAI Unit Distance 是开放数学发现案例，系统细节较少公开，更依赖人类数学共同体验证。

### Harness 演化与失败分支复用

代表性论文：

- Kosmos：long-running AI scientist with world model。
- TianJi：atmospheric mechanism discovery。
- Climate Self-Evolving Agent。
- Science Earth：open capability network, reputation-weighted trust, emergent task decomposition。
- SkillOS、STELLA、MIRIX、A-MEM、Mesh Memory Protocol 和 Memory Warning。
- ARA、PaperBench 和 RE-Bench 中关于 failure traces 的证据。

核心论点：

长周期科学发现需要可演化 harness：系统必须保存记忆、分支历史、工具链状态、角色分工、能力选择记录和验证门槛。但不受控制的记忆整合、未筛选的失败轨迹、错误的 reputation/trust 更新和缺乏 provenance 的能力复用，也可能损害后续搜索。

## 6. 科学产物、执行载体与验证边界

本章不应写成应用领域列表，而应说明不同执行载体如何改变智能体角色、协调协议、产物类型和验证边界。

### 执行载体比较

| 执行载体 | 产物类型 | 典型智能体角色 | 协调协议 | 验证边界 |
|---|---|---|---|---|
| 文献 / 引用 | claim, citation, synthesis | literature agent, verifier, writer | retrieval -> claim support -> synthesis | source existence, metadata match, claim support |
| 代码 / notebook | script, notebook, result table | coder, executor, analyst, reviewer | generate -> execute -> debug -> score | reproducible execution, benchmark score |
| 形式化数学 | proof sketch, Lean proof | proposer, prover, verifier, rater | sketch -> prove -> check -> select | machine-checkable proof |
| 仿真 | model, parameter setting, run result | planner, simulator, analyst, domain critic | design -> simulate -> analyze -> revise | executable simulation plus physical/domain plausibility |
| 物理 / 机器人实验室 | experiment plan, measurement, lab record | experiment designer, lab interface, analyst, human supervisor | propose -> approve -> execute -> measure | physical validation, safety approval |
| 人类实验室 / 同行评审 | expert feedback, review, approval | reviewer, author, area chair, human expert | submit -> review -> revise -> decide | expert validation, institutional accountability |

### 写作规则

讨论每类执行载体时，应回答四个问题：

1. 哪些智能体角色变得必要？
2. 交换了哪些中间科学产物？
3. 使用了什么协调协议？
4. 哪种验证边界使输出可信？

### 各载体的代表性论文

- 文献：OpenScholar、GPT Researcher、AutoSurvey、BrowseComp、SimpleQA/HLE、SciToolAgent。
- 代码 / notebook：ERA、AlphaEvolve、Jupiter、DatawiseAgent、SciNav、CORE-Bench、PaperBench。
- 形式化数学：AlphaProof Nexus、OpenAI Unit Distance。
- 仿真：TianJi、Climate Self-Evolving Agent、SciAgentGym、MLE-Bench。
- 物理 / 机器人 / 人类实验室：Robot Scientist、A-Lab、Coscientist、RoboChem-Flex、Rainbow、AFION、MOSAIC、Robin。
- 生物医学系统：Co-Scientist、Robin、Virtual Lab、CellVoyager、SPARK、Medea、GeneAgent、BioMedAgent。这些工作只从系统工作流层面使用，不展开 protocol-level 细节。

## 7. 评估、基准与证据闭环

本章区分两个问题：

- **验证**：一个生成的 claim、代码结果、证明、实验或报告如何成为科学证据？
- **评估**：如何衡量一个多智能体/演化式工作流是否优于替代方案？

### 输出验证类型

| 验证类型 | 检查什么 | 示例论文 | 局限 |
|---|---|---|---|
| Citation verification | claim 是否被文献支持 | OpenScholar, SciVer | 引用支持不等于真理 |
| Benchmark score | 任务表现 | PaperBench, CORE-Bench, SciAgentGym | benchmark leakage 和任务狭窄性 |
| Code execution | 可复现执行 | CORE-Bench, SUPER, Paper2Code | 环境配置脆弱 |
| Formal proof | 逻辑正确性 | AlphaProof Nexus | formalization bottleneck |
| Human expert review | 科学合理性 | Stanford Study, Robin, OpenAI Unit Distance | 专家成本与偏差 |
| Physical validation | 真实世界 grounding | A-Lab, Robin, Rainbow | 安全、成本、可扩展性 |
| Governance audit | 安全与科研诚信 | SafeScientist, Hidden Prompts, AI Responsible Publishing | 政策碎片化 |

### 当前基准类型

- 通用浏览与事实性：SimpleQA、BrowseComp、HLE。
- ML 与代码执行：MLE-Bench、RE-Bench、CORE-Bench、SUPER。
- 论文复现：PaperBench、Paper2Code。
- 科学工具使用：SciAgentGym。
- idea generation：IdeaBench、RINoBench、LiveIdeaBench、AI Idea Bench。
- 验证：SciVer、SPOT-a、OpenScholar。
- self-driving labs：Benchmarking SDL。

### 多智能体专属评估维度

| 指标 | 问题 |
|---|---|
| Role utility | 每个角色是否相对 monolithic agent 改善了最终质量？ |
| Coordination quality | 各角色输出是否连贯、及时且可被其他角色使用？ |
| Artifact handoff quality | 中间产物是否可检查、完整且绑定证据？ |
| Conflict resolution | 分歧是否改善了决策，还是只是增加噪声？ |
| Collective hallucination rate | 多个智能体是否放大了无支撑 claim？ |
| Memory contamination | 错误是否进入共享状态并继续传播？ |
| Coordination cost | 协调增加了多少 token、时间、工具或人类成本？ |
| Human checkpoint effectiveness | 人类审批是否在正确阶段捕获重要错误？ |
| Role robustness | 某个角色失败或移除时，系统是否能平稳退化？ |
| Responsibility traceability | 是否能追踪谁生成、检查、批准和执行了每一步？ |

### 当前基准缺失什么

- 多智能体协调质量。
- 每个角色的边际价值。
- 冲突解决与虚假共识。
- 长周期研究连续性。
- 失败分支复用。
- 跨领域迁移。
- 真实实验成本。
- 安全感知的任务拒绝。
- provenance preservation。
- 人类信任校准。
- formalization quality。
- 超出 benchmark 分布的新颖性。

## 8. 基础设施、开放问题与结论

基础设施在本文中是支撑层。它解释多智能体工作流如何持久运行、复用流程、保存证据并安全执行，但不应喧宾夺主。

### 支撑持久多智能体科学发现的基础设施

| 基础设施层 | 在多智能体工作流中的作用 | 代表性证据 |
|---|---|---|
| 工具基础设施 | 让智能体访问搜索、数据库、代码、仿真和仪器 | SciToolAgent, SciAgentGym, Toolformer, ToolLLM, ChemCost |
| 记忆基础设施 | 保存私有记忆、共享项目状态、证据记录和失败分支 | Kosmos, MIRIX, A-MEM, Graph Agent Memory, Mesh Memory Protocol |
| 产物基础设施 | 将 claim、code、trace、evidence 和 dead ends 转化为机器可读对象 | ARA, PaperBench, CORE-Bench |
| 技能基础设施 | 提供可复用流程，但必须从属于科学证据和验证 | Anthropic Skills Spec, Agent Skills Spec, SkillOS, SSL, GStack |
| 平台基础设施 | 推动原型系统走向科研工作台 | Gemini for Science, NotebookLM, Google Cloud/Labs tools |

关键观点：

科学多智能体系统需要能保存 provenance、失败分支、证据链接、版本化产物和角色特定记忆的基础设施。技能库只有在连接证据、权限和验证门槛时才真正有用。

### 开放问题

- **动态角色分配**：科学角色应如何在项目过程中被创建、合并、退休或重新分配？
- **角色消融与边际价值**：哪些智能体角色真正提升了发现质量？
- **冲突解决**：如何让分歧改善证据，而不是制造噪声？
- **集体幻觉**：如何防止多个智能体收敛到同一个无支撑 claim？
- **共享记忆治理**：谁可以写入、提升、编辑或删除项目记忆？
- **责任归因**：谁生成、检查、批准并执行了每个科学动作？
- **面向科学重要性的搜索**：产物演化如何优化新颖性、可行性和重要性，而不只是优化 benchmark score？
- **Harness 演化治理**：角色分配、工具链、记忆、verifier、reputation 和 human checkpoints 应在什么条件下被更新或回滚？
- **失败分支复用**：哪些失败应被保存？何时失败轨迹会反过来约束后续搜索？
- **形式系统之外的验证**：没有 proof assistant 的经验科学 claim 如何变得 audit-ready？
- **人类检查点设计**：人类应在哪些位置介入，才能最大化科学价值和安全价值？

### 结论立场

结论不应宣称完全自主的 AI 科学家已经到来。更稳健的表述是：

> Agentic scientific discovery 最强的证据并不来自一个模型取代科学家，而来自一类工作流系统：它们协调专门化智能体，演化可执行或可验证的科学研究产物，同时调整生成、执行和验证这些产物的 harness，并将人类、证据和基础设施保留在闭环之中。

收束观点：

- 多智能体工作流提供科学劳动分工。
- 协调协议决定角色专门化是否真正有效。
- 演化/搜索机制同时改进科学研究产物和 agentic harness。
- 验证与评估将 plausible outputs 转化为 scientific artifacts。
- 基础设施决定这些工作流能否被复用、审计和治理。

## 建议图表

### 图 1

Multi-Agent Scientific Discovery Workflow System。

建议层次：

- 人类目标与科学监督。
- 科学工作流阶段。
- 智能体角色。
- 协调协议。
- 演化/搜索循环：科学研究产物演化与 harness 演化。
- 科学产物与执行载体。
- 验证、评估、provenance 和治理。

### 图 2

Why Multi-Agent? Benefit-risk matrix。

行：role specialization、critique、parallel exploration、artifact handoff、responsibility boundary、human checkpoint。  
列：benefit、representative systems、failure mode、mitigation。

### 图 3

多智能体工作流中的演化/搜索循环：

Generate artifact -> Execute/Test -> Score/Verify -> Select -> Mutate/Recombine -> Archive -> Handoff -> Harness update -> Repeat。

### 表 1

核心文献分层：

- Tier 1：core anchor systems。
- Tier 2：mechanism support。
- Tier 3：background and supporting evidence。

### 表 2

Agent roles、coordination protocols、artifacts 和 verification checkpoints。

### 表 3

执行载体比较：artifact type、roles、coordination protocol、verification boundary。

### 表 4

Multi-agent/evolutionary evaluation metrics and benchmark gaps。

## 写作优先级

1. 围绕 AI4S -> Agentic Science -> Multi-Agent Workflow Systems 的转变撰写引言。
2. 先完成核心概念、系统分析维度和图 1，再展开系统章节。
3. 将第 3 章作为全文差异化核心：为什么需要多智能体，它带来什么，也引入什么风险。
4. 将第 4 章写成篇幅最大的系统章节。
5. 将演化/搜索机制写成多智能体工作流内部的双对象优化循环：科学研究产物演化 + harness 演化。
6. 所有关于执行载体、验证、基准和基础设施的讨论，都要回扣角色、协议、产物和验证边界。
