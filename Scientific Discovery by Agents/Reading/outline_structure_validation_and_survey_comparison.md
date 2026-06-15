# 综述章节结构验证与优秀综述分类方式对比

> 目的：验证当前综述骨架是否被现有文献池支撑，并对比领域内相关优秀综述的分类方式，判断是否需要调整章节分层。  
> 依据：`Notes/` 下 103 篇单篇论文笔记、`Reading/ch4_ch5_evidence_audit.md`、本地综述笔记，以及外部综述页面。  
> 当前结论：现有章节分层总体成立，但第 4、5 章应明确为同一系统的两个正交层面：第 4 章是 **组织层**，第 5 章是 **优化层**。

## 一、当前章节分层是否被现有文献支撑

### 总体判断

当前 8 章结构整体有文献支撑，尤其是第 3、4、5、7 章支撑最强。需要注意的是，第 4、5 章不是两个互斥的论文分类箱，而是同一类多智能体科学发现系统的两个分析层面。

| 当前章节 | 支撑强度 | 主要证据来源 | 判断 |
|---|---|---|---|
| 1. 引言与背景 | 强 | Agentic Science 综述、Agentic AI for Scientific Discovery 综述、2026 新系统 | 合理，用于建立从 AI4S 到 agentic workflow systems 的宏观转向 |
| 2. 核心概念与分析维度 | 中强 | Science Earth、Agent Skills Survey、Memory surveys、SDL survey | 合理，但应保持概念铺垫定位，不应变成额外 taxonomy |
| 3. 为什么需要多智能体？ | 强 | Co-Scientist、Robin、Virtual Lab、Agent Laboratory、Science Earth、AgentReview、ARA | 是全文差异化核心，应保留 |
| 4. 多智能体工作流模式 | 强 | 严格口径约 22 篇强支撑，扩展口径约 35 篇 | 应改写为“组织架构”，突出角色、协议、交接、批评、记忆、人类检查点 |
| 5. 演化/搜索机制 | 强 | 严格口径约 35 篇正文候选，扩展口径约 55 篇 | 应保留，但标题和小节应突出 artifact evolution + harness evolution |
| 6. 科学产物、执行载体与验证边界 | 中强 | ERA、AlphaEvolve、AlphaProof Nexus、Robin、SDL 系统、OpenScholar、CORE-Bench | 合理，但必须避免写成应用领域列表 |
| 7. 评估、基准与证据闭环 | 强 | 25 篇 benchmark + 9 篇 verification 笔记 | 支撑充分，应突出 multi-agent 专属评估维度 |
| 8. 基础设施、开放问题与结论 | 中强 | memory、skills、infrastructure、governance 材料 | 合理，但写作时需控制篇幅，避免抢主线 |

### 1. 引言与背景

这一章支撑充分。`From AI for Science to Agentic Science` 已经提供宏观叙事：AI for Science 正在从专业模型和工具走向 agentic scientific discovery。`Agentic AI for Scientific Discovery` 则提供了另一种更工程化的综述入口，强调系统、工具、数据集、评估指标和人机协作。

我们的区别不应写成“更新了更多论文”，而应写成：

> 既有综述说明科学发现正在 agent 化；本文进一步追问这些 agentic workflow 为什么越来越需要 multi-agent organization。

### 2. 核心概念与分析维度

这一章有必要，但应保持“概念语言”定位。它不是文章主线，也不是文献分类表。

支撑来源：

- `Science_Earth_2026`：帮助把 agent 从 LLM prompt role 扩展为开放 scientific capability network 中的主动实体。
- `Agent Skills Survey`：支撑 tool、skill、capability、operational layer 的区分。
- `Memory Age Survey` / `Memory Autonomous Survey`：支撑 memory 不是简单上下文，而是持久、可演化、可治理的系统状态。
- `Self-Driving Labs ChemRev`：提醒 scientific agent 必须连接硬件、软件、决策算法和真实实验基础设施。

建议定位：

> 第二章回答“我们用什么概念看这些系统”，而不是回答“论文如何分类”。

### 3. 为什么需要多智能体？

这一章是全文差异化核心，文献池支撑很强。

主要证据：

- 角色专业化：`CoScientist_2026`、`Virtual_Lab_2025`、`Agent_Laboratory_2024`。
- 独立批评与审查：`CoScientist_2026`、`AgentReview_2024`、`LLM_Verifier_2025`。
- 并行探索：`CoScientist_2026`、`AlphaProof_Nexus_2026`、`MC_NEST_2025`。
- 产物交接与 provenance：`ARA_2026`、`Mesh_Memory_Protocol_2025`、`Collaborative_Memory_2025`。
- 开放能力网络：`Science_Earth_2026`。

这章应该明确回答：

> 多智能体不是多个模型聊天，而是科学劳动、科学能力、执行载体和证据标准的组织方式。

### 4. 多智能体工作流模式

第 4 章被现有文献强支撑。`ch4_ch5_evidence_audit.md` 中已经确认，严格口径约 22 篇论文可进入正文主干。

但当前标题“科学发现中的多智能体工作流模式”略宽。建议改为：

> **多智能体科研工作流的组织架构：从固定团队到开放能力网络**

这样更符合文献分布：

- fixed-role teams：`CoScientist_2026`、`Virtual_Lab_2025`、`Agent_Laboratory_2024`、`Robin_2026`。
- coordination and handoff：`ARA_2026`、`SciToolAgent_2025`、`Mesh_Memory_Protocol_2025`。
- critique and review：`AgentReview_2024`、`ReviewerGPT_2023`、`Reviewer2_2024`。
- human/lab loop：`Robin_2026`、`Virtual_Lab_2025`、`CoScientist_2026`。
- shared memory/provenance：`Collaborative_Memory_2025`、`MIRIX_2025`、`ARA_2026`。
- open capability network：`Science_Earth_2026`。

### 5. 演化/搜索机制

第 5 章也有强支撑，严格口径约 35 篇正文候选。它应该作为第 4 章的“优化层”，而不是并列文献分类。

建议标题改为：

> **搜索与演化机制：科学产物演化与 Harness 演化**

文献分布非常清楚：

- hypothesis / idea evolution：`CoScientist_2026`、`MC_NEST_2025`、`ResearchAgent_2025`。
- code / notebook / software evolution：`ERA_2026`、`AlphaEvolve_2025`、`Jupiter_Notebook_Agent_2025`、`SciNav_2026`。
- formal proof search：`AlphaProof_Nexus_2026`。
- experiment / simulation search：`ALab_2023`、`RoboChem_Flex_2026`、`TianJi_2026`、`Robin_2026`。
- failed branch and memory reuse：`ARA_2026`、`Reflexion_2023`、`ExpeL_2024`、`Memory_Warning_2026`。
- harness / capability / network evolution：`Science_Earth_2026`、`SkillOS_2026`、`STELLA_2025`、`Mesh_Memory_Protocol_2025`。

### 6. 科学产物、执行载体与验证边界

这一章有支撑，但风险是写成“应用场景罗列”。它更适合作为横向比较章，回答不同 substrate 如何改变 agent roles、coordination protocol、artifact type 和 verification boundary。

建议保持这一章，但写作时围绕四个问题：

1. 哪些 agent roles 变得必要？
2. 交换什么 scientific artifacts？
3. 使用什么 coordination protocol？
4. 输出如何被验证？

### 7. 评估、基准与证据闭环

这一章支撑非常强。项目已有 25 篇 benchmark 笔记和 9 篇 verification 笔记。

需要突出本文特色：不是只列 benchmark，而是指出当前 benchmark 缺少 multi-agent 专属指标：

- role utility；
- coordination quality；
- artifact handoff quality；
- conflict resolution；
- collective hallucination；
- memory contamination；
- responsibility traceability；
- human checkpoint effectiveness。

### 8. 基础设施、开放问题与结论

这一章有必要，但应避免展开成独立技能/工具综述。它应该服务于 multi-agent workflow：

- memory 支撑长期项目状态；
- skills 支撑能力复用；
- tools 支撑执行；
- artifact protocols 支撑交接和审计；
- platforms 支撑部署。

建议后续正式写作时，如果篇幅允许，可以把第 8 章拆成：

1. Infrastructure for persistent multi-agent science。
2. Open problems and conclusion。

但在 outline 阶段合并是可以的。

## 二、领域内优秀综述的分类方式

本节继续扩展可借鉴的综述分类法。总体来看，相关综述大致分为六类：科学流程型、领域应用型、多智能体协作型、Agent 架构型、能力生命周期型、实验室基础设施型。我们的综述可以吸收它们的局部分类，但不应直接照搬任何一种。

### 1. From AI for Science to Agentic Science

来源：arXiv:2508.14111。

它的分类方式可以概括为：

| 分类层 | 内容 |
|---|---|
| 宏观叙事 | 从 AI for Science 到 Agentic Science |
| 能力层 | LLM、多模态系统、工具调用、规划、记忆、平台 |
| 流程层 | hypothesis generation、experimental design、execution、analysis、iterative refinement |
| 领域层 | life sciences、chemistry、materials、physics |
| 挑战层 | reliability、reproducibility、governance、evaluation |

它的优点是范围大、叙事完整，适合定义 Agentic Science。局限是 multi-agent coordination、artifact handoff、harness evolution 不是它的中心。

对本文启发：

> 我们可以继承它的宏观转向和科学流程，但不能重复它的领域式综述。本文应收窄到 multi-agent workflow systems。

### 2. Agentic AI for Scientific Discovery

来源：arXiv:2503.08979。

它的分类方式可以概括为：

| 分类层 | 内容 |
|---|---|
| 系统与工具 | existing systems and tools |
| 领域应用 | chemistry、biology、materials science 等 |
| 评估层 | metrics、datasets、benchmarks |
| 实现层 | frameworks and implementation tools |
| 挑战层 | reliability、literature review automation、ethics、human-AI collaboration |

它更像一篇“领域进展 + 工具/系统/评估”综述。优点是工程覆盖广，局限是分类仍以系统和领域为主，对 multi-agent 的组织机制不够细。

对本文启发：

> 我们应吸收它对 evaluation metrics、implementation frameworks 和 human-AI collaboration 的重视，但正文主线不要按领域应用展开。

### 3. LLM-based Multi-Agent Systems: workflow / construction 型分类

代表综述：

- `Large Language Model based Multi-Agents: A Survey of Progress and Challenges`
- `A survey on LLM-based multi-agent systems: workflow, infrastructure, and challenges`

这些综述通常从多智能体系统的构成模块出发分类。典型结构包括：

| 分类层 | 内容 |
|---|---|
| Agent profile | 角色、身份、目标、persona、能力描述 |
| Perception | agent 如何获得环境、任务、文献、工具反馈 |
| Self-action | 单个 agent 的推理、规划、记忆、行动 |
| Mutual interaction | agent 间通信、协作、协商、辩论 |
| Evolution | 反思、经验积累、能力增长 |
| Application | problem-solving 与 world simulation |
| Challenges | 通信成本、协调失败、评估、可靠性 |

对本文启发：

> 这类分类非常适合支持我们的第 4 章。尤其是 profile / mutual interaction / evolution 三个模块，可以映射为本文的角色定义、协调协议和 harness evolution。但我们不能完全照搬，因为它们面向通用 LLM-MAS，不处理科学产物、实验验证和科学证据边界。

### 4. Multi-Agent Collaboration Mechanisms: actors / type / structure / strategy / protocol

来源：arXiv:2501.06322。

这篇综述专门从协作机制角度组织 LLM-based MAS，分类维度包括：

| 维度 | 含义 |
|---|---|
| Actors | 参与协作的 agents 是谁 |
| Types | cooperation、competition、coopetition 等关系类型 |
| Structures | peer-to-peer、centralized、distributed 等组织结构 |
| Strategies | role-based、model-based 等协作策略 |
| Coordination protocols | 具体通信和协调协议 |

对本文启发：

> 这是最适合借鉴到第 4 章的分类方式。我们可以把第 4 章从“角色分解、交接、批评、人类介入、共享记忆”进一步整理为：actors / interaction type / structure / strategy / protocol / memory-provenance。这样第 4 章会更像机制综述，而不是案例堆叠。

可吸收进本文的表达：

- actors：scientist agents、critics、verifiers、tool executors、human experts、lab interfaces；
- interaction types：cooperation、competition、critique、adjudication；
- structures：fixed-role team、coordinator-worker hierarchy、open capability network；
- protocols：meeting、tournament、review、task bidding、artifact handoff、memory protocol。

### 5. LLM-based Multi-Agent System: application-purpose 型分类

代表综述：`A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application`。

该综述按应用目的把 LLM-MAS 分为：

| 类型 | 含义 |
|---|---|
| Solving complex tasks | 多智能体用于任务分解、协作求解复杂任务 |
| Simulating specific scenarios | 多智能体作为社会、经济、游戏或领域场景模拟器 |
| Evaluating generative agents | 多智能体用于动态评估和交互式评价 |

对本文启发：

> 这类分类不适合作为我们的主线，因为我们不是泛化 LLM-MAS 应用综述。但它提醒我们可以在第 7 章讨论“multi-agent as evaluator”，例如 AgentReview、ReviewerGPT、LLM-as-a-Verifier、AI Scientist automated reviewer 等。

### 6. Autonomous LLM Agents: construction / application / evaluation

代表综述：`A Survey on Large Language Model based Autonomous Agents`。

它的基本分类方式是：

| 分类层 | 内容 |
|---|---|
| Agent construction | agent 的 profile、memory、planning、action、tool use |
| Applications | social science、natural science、engineering 等 |
| Evaluation | agent 能力、任务表现、环境交互等评估 |
| Challenges | grounding、long-horizon planning、memory、safety、alignment |

对本文启发：

> 这类综述适合作为基础 agent 概念参考，但不应主导本文。我们可以借鉴 construction / evaluation 的二分：第 4、5、6 章讲 construction and operation，第 7 章讲 evaluation and evidence closure。

### 7. Cognitive Architectures for Language Agents: memory / action / decision-making

来源：CoALA, `Cognitive Architectures for Language Agents`。

这篇综述借鉴认知科学和符号 AI，提出语言 agent 的三个核心组成：

| 组成 | 含义 |
|---|---|
| Modular memory | 工作记忆、长期记忆、外部记忆等 |
| Structured action space | 与内部记忆、外部工具、环境交互的动作空间 |
| Generalized decision-making process | 选择行动、规划、反馈更新的决策过程 |

对本文启发：

> CoALA 的价值在于帮助我们严肃定义 agent，而不是把 agent 写成 prompt persona。它支持第 2 章中 agent / tool / capability / harness 的概念区分，也支持第 6 章把不同 execution substrates 看作不同 action spaces。

### 8. LLM Agent architecture surveys: reasoning / planning / tool calling / reflection

代表综述：

- `The Landscape of Emerging AI Agent Architectures for Reasoning, Planning, and Tool Calling`
- `Large Language Model Agent: A Survey on Methodology, Applications and Challenges`
- `A Review of Prominent Paradigms for LLM-Based Agents: Tool Use, Planning, and Feedback Learning`

这些综述的分类方式通常围绕 agent 能力模块：

| 分类层 | 内容 |
|---|---|
| Tool use / RAG | 搜索、API、数据库、工具链 |
| Planning | task decomposition、plan selection、external module、memory-augmented planning |
| Feedback learning | reflection、self-correction、experience learning |
| Multi-agent collaboration | communication、role division、leadership、coordination |
| Architecture pattern | single-agent、multi-agent、leader-worker、team-based、hybrid |

对本文启发：

> 这些分类适合支持第 5 章的 search / iteration / feedback 边界。尤其是 tool use、planning、feedback learning 三分法，可以作为我们解释 artifact evolution 的底层机制：先规划候选，调用工具执行，再用反馈更新。

### 9. Agent Memory Surveys: forms / functions / dynamics 与 write / manage / read

本地已有两篇记忆综述笔记：

| 综述 | 分类方式 |
|---|---|
| Memory in the Age of AI Agents | Forms / Functions / Dynamics |
| Memory for Autonomous LLM Agents | Write / Manage / Read loop + time range / substrate / control strategy |

可借鉴分类：

| 分类层 | 对本文的意义 |
|---|---|
| Forms | 科学记忆以文本、图、层级、参数化或潜空间方式存在 |
| Functions | 科学记忆承担事实、经验、工作状态、程序技能等功能 |
| Dynamics | 科学记忆如何形成、演化、检索、遗忘 |
| Write / Manage / Read | 多智能体工作流中的证据写入、共享治理和任务时检索 |

对本文启发：

> 第 4 章的共享记忆小节可以借鉴 memory surveys 的分类，但要科学化：role-private memory、shared project memory、evidence memory、failed-branch archive、provenance graph。第 5 章 harness evolution 也应强调 memory evolution 的风险：持续整合不等于进步。

### 10. Self-Driving Laboratories: hardware / software / decision / application / automation level

来源：Chemical Reviews 2024。

SDL 综述的分类方式是技术栈与自动化层级：

| 层次 | 内容 |
|---|---|
| Hardware | 自动反应器、机器人平台、分析仪器 |
| Software | 调度、实验控制、数据管理、设备通信 |
| Decision layer | Bayesian optimization、active learning、实验设计 |
| Application layer | drug discovery、materials、chemistry、genomics |
| Automation level | partial automation 到 closed-loop autonomy |

对本文启发：

> 第 6 章讨论 physical / robotic labs 时，应借鉴 SDL 的 stack，而不是只把它们当作“实验场景”。这能防止我们把 LLM agent 的推理能力误写成真实实验闭环的全部。

## 三、可借鉴分类方法汇总

| 外部分类方法 | 是否适合做本文主线 | 最适合放入本文哪里 | 理由 |
|---|---|---|---|
| Scientific workflow | 不适合作唯一主线 | 引言、第 2 章、第 6 章 | 已被 Agentic Science 综述使用，适合作背景横轴 |
| Domain/application taxonomy | 不适合 | 只作例子分布 | 会让本文变成普通 AI4S / Agentic Science 综述 |
| Agent construction modules | 部分适合 | 第 2、4 章 | 可帮助定义 agent、role、memory、action |
| Multi-agent collaboration dimensions | 很适合 | 第 4 章 | actors、interaction types、structures、strategies、protocols 正好服务 multi-agent 主线 |
| Tool use / planning / feedback learning | 适合 | 第 5 章 | 可解释 search/evolution 的底层机制 |
| Skill lifecycle | 不适合作主线 | 第 5、8 章 | 支撑 harness evolution 和 skill infrastructure |
| Memory lifecycle | 不适合作主线 | 第 4、5、8 章 | 支撑 shared memory、provenance、memory governance |
| SDL technology stack | 局部适合 | 第 6 章 | 支撑 physical grounding 和真实实验闭环 |
| Evaluation benchmark taxonomy | 适合 | 第 7 章 | 用于组织 benchmark 与 multi-agent 专属评估缺口 |

## 四、对当前 outline 的进一步建议

### 建议一：第 4 章吸收 multi-agent collaboration survey 的分类语言

当前第 4 章可以从：

> 角色分解、交接、批评、人类介入、共享记忆

进一步书面化为：

> actors、interaction structures、coordination protocols、artifact handoff、human/lab checkpoints、shared memory and provenance。

建议第 4 章小节改为：

1. **Actors and roles: from fixed-role teams to heterogeneous capability nodes**
2. **Interaction structures: hierarchy, peer collaboration, tournament, review, and open networks**
3. **Coordination protocols and artifact handoff**
4. **Critique, adjudication, and review**
5. **Human/lab checkpoints and responsibility boundaries**
6. **Shared memory, provenance, and open capability networks**

### 建议二：第 5 章吸收 tool-use / planning / feedback-learning 分类

当前第 5 章可继续保留 artifact evolution + harness evolution，但在开头补一个机制层：

| 机制 | 说明 |
|---|---|
| Planning | 生成候选假设、代码路径、实验计划、证明草图 |
| Execution | 运行代码、notebook、仿真、证明器、实验 |
| Feedback | benchmark score、compiler error、Lean verifier、实验结果、人类评审 |
| Selection | ranking、Elo、tree search、MCTS、BO、review-based filtering |
| Memory / Archive | 保存成功、失败、分支、技能、trust 和 provenance |
| Harness update | 更新角色、工具链、验证门槛、reputation、checkpoints |

这样第 5 章不仅讲“演化对象”，也讲“演化是如何发生的”。

### 建议三：第 6 章借鉴 SDL stack 和 CoALA action-space 思想

第 6 章不要按领域写，而应按 execution substrate 写：

- literature / citation；
- code / notebook；
- formal proof；
- simulation；
- robotic lab；
- human lab / peer review。

同时每个 substrate 都问：

1. action space 是什么？
2. artifact 是什么？
3. coordination protocol 是什么？
4. verification boundary 是什么？

### 建议四：第 7 章吸收 evaluation-oriented MAS taxonomy

第 7 章可以区分：

- output verification：claim、code、proof、experiment 是否可信；
- system evaluation：multi-agent workflow 是否比 single-agent / fixed pipeline 更好；
- process evaluation：coordination、handoff、memory、role utility 是否有效；
- governance evaluation：authorship、safety、responsibility、prompt injection。

这比单纯按 benchmark 名称分类更强。

## 五、最终结论

继续查阅更多综述后，当前结构仍然成立，但可以更成熟地吸收外部分类语言：

1. **不要按领域应用分类**：这会和 Agentic Science / Agentic AI for Scientific Discovery 重复。
2. **不要按通用 Agent 或 Skill lifecycle 分类**：这会冲淡 multi-agent 主线。
3. **第 4 章应吸收 multi-agent collaboration 综述的 actors / structures / strategies / protocols。**
4. **第 5 章应吸收 agent architecture 综述的 planning / execution / feedback / selection / memory。**
5. **第 6 章应吸收 SDL 与 CoALA 的 substrate / action-space 思想。**
6. **第 7 章应吸收 benchmark / evaluation taxonomy，但突出 multi-agent 专属指标。**

因此，本文最合适的分类方式不是照搬任何已有综述，而是融合为：

> Multi-agent organization × Search/evolution mechanism × Scientific artifact/substrate × Verification/evaluation boundary.

这套分类既能继承已有优秀综述的成熟术语，又能保留本文最重要的差异化：**自主科学发现中的 multi-agent 不是实现细节，而是组织科学劳动、科学能力和科学证据的核心机制。**


来源：arXiv:2605.07358。

它的分类方式是非常清晰的 lifecycle：

| 阶段 | 含义 |
|---|---|
| Representation | skill 如何表示 |
| Acquisition | skill 如何获得 |
| Retrieval / Selection | skill 如何被召回和选择 |
| Evolution | skill 如何被修改、验证、治理和更新 |

它的优点是机制清楚，特别适合解释可复用 procedural knowledge。局限是它不是科学发现综述。

对本文启发：

> 技能生命周期适合放在 infrastructure / harness evolution 层，而不应成为全文主线。本文主线仍是 multi-agent organization。

### 4. Agent Memory Surveys

本地两篇记忆综述分别使用：

| 综述 | 分类方式 |
|---|---|
| Memory in the Age of AI Agents | Forms / Functions / Dynamics |
| Memory for Autonomous LLM Agents | Write / Manage / Read loop + time range / substrate / control strategy |

它们的优点是抓住了记忆系统的生命周期和治理问题，而不是只按记忆类型罗列。

对本文启发：

> 共享记忆不应只写成“有 memory 模块”，而要写成多智能体工作流中的状态管理、provenance、权限、冲突合并和长期演化问题。

### 5. Self-Driving Laboratories for Chemistry and Materials Science

来源：Chemical Reviews 2024。

它的分类方式是技术栈 + 自动化层级：

| 层次 | 内容 |
|---|---|
| Hardware | reactor、robotics、analysis instruments |
| Software | scheduling、control、data management |
| Decision layer | Bayesian optimization、active learning、experimental design |
| Application layer | chemistry、materials、drug discovery 等 |
| Automation level | partial automation 到 closed-loop autonomy |

对本文启发：

> 当我们讨论 physical / robotic lab 时，不能只说 agent 决策，还要考虑硬件、软件、数据、优化算法和自动化层级。

## 三、对比后得到的结构建议

### 当前结构的优点

当前结构相对于已有综述有三个差异化优势：

1. **更聚焦 multi-agent**：不是泛泛讨论 autonomous scientific discovery。
2. **更强调组织机制**：角色、协议、交接、批评、记忆、人类检查点。
3. **更强调演化对象**：不仅是 artifact evolution，也包括 harness evolution。

### 当前结构的风险

| 风险 | 表现 | 修改建议 |
|---|---|---|
| 第 4、5 章重复 | Co-Scientist、Robin、Science Earth、ARA 会同时出现 | 明确第 4 章是组织层，第 5 章是优化层 |
| 第 6 章发散 | 容易变成不同应用领域列表 | 每个 substrate 都回扣 roles、protocols、artifacts、verification |
| 第 8 章过宽 | memory、skills、tools、platforms 都可能抢主线 | 只写对 multi-agent workflow 有直接作用的基础设施 |
| skills 线复燃 | 可能又变成 skill lifecycle survey | skills 只放在 harness / infrastructure 中 |
| evolution 过度泛化 | 把所有 iteration 都叫 evolution | 只有存在选择、评分、反馈、记忆、更新、归档或拓扑重组时才称强演化 |

### 建议后的章节结构

建议保留 8 章结构，但对第 4、5 章标题进行修正：

| 章节 | 建议标题 | 作用 |
|---|---|---|
| 1 | 引言与背景 | 从 AI4S / Agentic Science 转向 Multi-Agent Workflow Systems |
| 2 | 核心概念与分析维度 | 定义 agent、tool、capability、harness |
| 3 | 为什么需要多智能体？ | 回答本文差异化问题 |
| 4 | 多智能体科研工作流的组织架构：从固定团队到开放能力网络 | 组织层 |
| 5 | 搜索与演化机制：科学产物演化与 Harness 演化 | 优化层 |
| 6 | 科学产物、执行载体与验证边界 | 横向比较不同 substrate |
| 7 | 评估、基准与证据闭环 | 评价系统和输出可信度 |
| 8 | 基础设施、开放问题与结论 | 长期运行条件和未来问题 |

## 四、最终判断

现有文献池能够支撑当前章节分层逻辑，但需要把章节关系讲清楚：

> 第 4 章解释多智能体科学发现系统如何被组织；第 5 章解释这些组织起来的系统如何通过搜索、反馈和演化改进科学研究产物及其 agentic harness。

与现有优秀综述相比，本文不应按领域应用分类，也不应按通用 skill lifecycle 分类。最合适的差异化结构是：

> 以 autonomous scientific discovery 为应用背景，以 multi-agent coordination 为核心切入点，以 artifact/harness evolution 为第二机制，以 verification and infrastructure 为可信闭环。
