# 自主科学发现相关综述的分类方法对比

> 目的：整理现有自主科学发现、Agentic Science、AI Scientist、Human-AI Scientific Discovery 和 Self-Driving Lab 等相关综述的分类标准，判断哪些分类方法可以被本文借鉴，哪些不适合作为本文主线。

## 总体判断

现有相关综述大多从以下角度组织文献：

| 分类方式 | 常见问题意识 | 是否适合作为本文主线 |
|---|---|---|
| 科学发现流程 | AI/agent 参与科学发现的哪些阶段？ | 适合作背景和横向参照，不适合作唯一主线 |
| 自治程度 / 角色层级 | AI 从工具到研究伙伴再到科学家的演进路径是什么？ | 适合作概念引入 |
| AI Scientist 端到端流程 | AI scientist 如何完成从文献到论文的科研 pipeline？ | 适合比较单智能体或 pipeline 式系统 |
| 应用领域 | AI agent 在生物、化学、材料、物理等领域如何应用？ | 不适合作主线，容易变成泛 AI4S 综述 |
| 系统 / 工具 / 数据集 / benchmark | 当前有哪些工具系统和评估资源？ | 适合支撑评估和基础设施章节 |
| Human-AI Collaboration | 人类和 AI 在科学发现中如何分工？ | 适合支撑 human checkpoint 和 lab-in-the-loop |
| Self-Driving Lab 技术栈 | 自主实验室如何由硬件、软件、决策层和实验闭环构成？ | 适合支撑物理实验载体章节 |
| Multi-agent coordination | 多智能体如何组织科学劳动、能力、产物和验证？ | 最适合作为本文差异化主线 |

因此，本文不宜简单复用已有综述的流程式、领域式或工具式分类。更合适的定位是：

> 既有综述多从科学流程、自治程度、应用领域、工具系统或实验室基础设施出发组织文献；本文则进一步把 multi-agent organization 作为自主科学发现的核心分析对象，讨论科学劳动、科学能力、科学产物和验证边界如何通过多智能体工作流被组织起来。

## 1. 按科学发现流程分类

代表综述：

- `From AI for Science to Agentic Science: A Survey on Autonomous Scientific Discovery`

该类综述通常把 agentic scientific discovery 拆成科学发现流程中的若干阶段。

| 阶段 | 含义 |
|---|---|
| Observation and Hypothesis Generation | 观察、文献理解、问题发现和假设生成 |
| Experimental Planning and Execution | 实验规划、实验设计和执行 |
| Data and Result Analysis | 数据分析、结果解释和模式发现 |
| Synthesis, Validation, and Evolution | 综合、验证、迭代和演化 |

该类综述还常把科学 agent 的核心能力拆成：

- reasoning and planning
- tool integration
- memory
- multi-agent collaboration
- optimization and evolution

### 对本文的启发

科学发现流程分类适合作为背景框架，帮助读者理解 agentic science 从哪些科研阶段切入。但它不适合作为本文唯一主线，因为这已经是经典 Agentic Science 综述的核心组织方式。

本文可以继承其宏观叙事，即从模型中心的 AI for Science 转向流程中心的 Agentic Science；但正文应进一步收窄到 multi-agent workflow systems。

参考链接：

- https://arxiv.org/abs/2508.14111

## 2. 按自治程度 / 角色层级分类

代表综述：

- `From Automation to Autonomy: A Survey on Large Language Models in Scientific Discovery`

该类综述把 LLM 或 agent 在科学发现中的角色分为不同自治层级。

| 层级 | 含义 |
|---|---|
| Tool | LLM 作为工具，辅助检索、问答、写作、分析或代码生成 |
| Analyst | LLM 能较独立地完成数据分析、建模、解释和局部科研任务 |
| Scientist | LLM/agent 参与完整科研生命周期，包括提出问题、设计实验、分析结果和形成发现 |

### 对本文的启发

该分类适合用来解释从工具型 AI 到 autonomous scientific discovery 的演进过程。它能够帮助本文说明：即使单个 agent 的能力从 tool 升级到 analyst 或 scientist，科学发现仍然需要 multi-agent organization，因为科学发现包含异质角色、异质产物和异质验证边界。

因此，该分类适合放在引言或背景中，用于铺垫“为什么单个 AI scientist 叙事不足”。

参考链接：

- https://aclanthology.org/2025.emnlp-main.895/

## 3. 按 AI Scientist 端到端科研流程分类

代表综述：

- `A Survey of AI Scientists`

该类综述通常围绕 AI scientist 如何完成端到端科研 pipeline 展开。

| 阶段 | 含义 |
|---|---|
| Literature Review | 文献检索、文献综述和相关工作整理 |
| Idea Generation | 研究想法、问题和假设生成 |
| Experimental Preparation | 数据、变量、代码、实验协议和资源准备 |
| Experimental Execution | 实验运行、代码执行或仿真实验 |
| Scientific Writing | 结果整理、论文写作和图表生成 |
| Paper Generation | 从研究想法到完整论文草稿的自动化生成 |

该类综述也常区分：

| 类型 | 含义 |
|---|---|
| General AI Scientist Systems | 跨领域、端到端科研自动化系统 |
| Domain-Specific AI Scientist Systems | 面向化学、材料、生物、物理等具体领域的 AI scientist 系统 |

### 对本文的启发

AI Scientist 流程分类适合帮助本文定位 AI Scientist、AI Scientist v2、AI-Researcher、Agent Laboratory 等系统。它也适合作为单智能体或 pipeline 式科研自动化的对照基线。

但该分类主要回答“AI scientist 如何完成科研流程”，没有充分回答“为什么这个流程需要多智能体组织”。因此，它不应成为本文主线。

参考链接：

- https://arxiv.org/html/2510.23045v3

## 4. 按系统、工具、数据集与评估分类

代表综述：

- `Agentic AI for Scientific Discovery`

该类综述更偏工程化，通常按系统资源和评估资源组织。

| 分类标准 | 内容 |
|---|---|
| Systems and Tools | 现有 agentic scientific discovery 系统和工具 |
| Application Fields | chemistry、biology、materials science 等应用领域 |
| Evaluation Metrics | 评估指标、能力测量和任务表现 |
| Implementation Frameworks | Agent 框架、工具调用框架、实验平台 |
| Datasets and Benchmarks | 科学任务数据集、benchmark 和 leaderboard |
| Challenges | 可靠性、文献综述自动化、伦理、人机协作等 |

### 对本文的启发

该分类适合支撑本文的评估、基准和基础设施章节，尤其可以帮助整理当前系统资源、实现框架和 benchmark landscape。

但如果本文按这个方式展开，容易变成系统和工具清单，削弱 multi-agent 主线。因此，它适合做支撑层，不适合作正文主线。

参考链接：

- https://arxiv.org/abs/2503.08979

## 5. 按知识、代码、物理系统和工具链分类

代表综述：

- `Autonomous Agents for Scientific Discovery: Orchestrating Scientists, Language, Code, and Physics`

该类综述强调科学发现中不同类型的执行载体和工具链。

| 分类标准 | 内容 |
|---|---|
| Knowledge Extraction | 文献、知识图谱、多模态科学知识抽取 |
| Hypothesis Generation | 假设生成、问题发现和候选筛选 |
| Experimental Design and Execution | 实验设计、工具调用、仿真或实验执行 |
| Tool Use | 科学数据库、仿真器、代码执行器和工具链 |
| Result Analysis and Refinement | 结果分析、反馈、自我修正和迭代 |
| Domain-Specific Scientific Agents | 生物、化学、材料、物理等领域 agent |

### 对本文的启发

该分类与本文的“科学产物、执行载体与验证边界”章节高度相关。它提醒我们，科学发现 agent 操作的不只是自然语言，还包括代码、仿真、数据库、证明系统、实验仪器和物理世界。

本文可以吸收这一点，但需要进一步从 multi-agent 视角追问：不同执行载体会要求哪些角色、哪些协调协议、哪些中间产物和哪些验证边界。

参考链接：

- https://arxiv.org/html/2510.09901v1

## 6. 按 Human-AI Collaboration 分类

代表综述：

- `A Survey of Human-AI Collaboration for Scientific Discovery`

该类综述通常从人类和 AI 在科学发现流程中的分工关系出发。

| 分类标准 | 内容 |
|---|---|
| 科学发现阶段 | observation、hypothesis、experiment 等 |
| 人与 AI 的角色 | 人类主导、AI 辅助；AI 生成、人类验证；人机共同迭代 |
| 协作模式 | 人类监督、AI 建议、共同决策、实验室执行和专家审查 |

### 对本文的启发

该分类适合支撑 human-in-the-loop、lab-in-the-loop 和 human checkpoint 的论证。它尤其有助于强调：人类监督并不只是自主性的不足，在科学发现中，人类专家、实验室和同行评审往往正是可信闭环的一部分。

本文可以将其纳入多智能体工作流：human scientist、domain expert、lab operator 和 reviewer 都可以被视为 multi-agent workflow 中的异质参与者或检查点。

参考链接：

- https://www.preprints.org/manuscript/202601.0405

## 7. 按 Self-Driving Lab 技术栈分类

代表综述：

- `Self-Driving Laboratories for Chemistry and Materials Science`

该类综述通常按自主实验室的技术栈组织。

| 层级 | 内容 |
|---|---|
| Hardware | 机器人、仪器、自动化反应器和表征设备 |
| Software | 调度系统、数据管理、设备通信和实验控制 |
| Decision Layer | Bayesian optimization、active learning、实验设计算法 |
| Application Layer | drug discovery、materials science、chemistry、genomics 等 |
| Automation Level | 从局部自动化到闭环 autonomous lab |

### 对本文的启发

该分类适合支撑本文第 6 章中的 physical / robotic lab 部分。它提醒我们，真实实验闭环不仅依赖 LLM agent，也依赖硬件、传感、调度、数据质量、成本和实验安全。

本文不应把 self-driving lab 简化为“一个 agent 调用实验工具”，而应将其视为包含硬件、软件、决策层、人类监督和验证边界的复杂执行载体。

参考链接：

- https://doi.org/10.1021/acs.chemrev.4c00055

## 8. 按 Multi-agent coordination 分类

这一类分类方法最接近本文的差异化主线。需要注意的是，在“自主科学发现”同领域综述中，真正把 multi-agent coordination 作为主分类轴的工作还不多；更多综述只是把 multi-agent collaboration 作为科学 agent 的一种能力、系统形态或案例现象。因此，本文可以借鉴这些综述的分类语言，但需要进一步将其科学发现化。

### 8.1 同领域综述：MAS for scientific discovery

代表综述：

- `Collective Intelligence: On the Promise and Reality of Multi-Agent Systems for AI-Driven Scientific Discovery`

这类综述已经直接讨论 multi-agent systems 在 AI-driven scientific discovery 中的作用。其分类方式通常仍然沿用科学流程，将 MAS 映射到不同科研阶段。

| 分类轴 | 内容 |
|---|---|
| Literature Review | 多智能体用于文献检索、阅读、摘要、证据组织 |
| Hypothesis Generation | 多智能体用于提出、比较、批评和筛选假设 |
| Experimental Planning | 多智能体用于实验设计、方案讨论和资源规划 |
| Experimental Execution | 多智能体用于工具调用、实验执行或实验室交接 |
| Peer Review | 多智能体用于评审、批评、仲裁和质量控制 |

### 对本文的启发

这类综述说明，multi-agent 已经被看作科学发现的重要组织形态。但它的主线仍然偏“MAS 用在哪些科研阶段”。本文可以在此基础上进一步推进：不只讨论 MAS 在科研流程中的应用位置，而是讨论 **多智能体如何组织科学劳动、科学能力、科学产物和验证边界**。

参考链接：

- https://www.preprints.org/manuscript/202508.1640/v1

### 8.2 Agentic Science 综述：multi-agent 作为核心能力之一

代表综述：

- `From AI for Science to Agentic Science: A Survey on Autonomous Scientific Discovery`

该综述的主线不是 multi-agent，而是从 AI4S 到 Agentic Science 的宏观转向。它将 scientific agents 的能力组织为若干模块，其中 multi-agent collaboration 是重要能力之一。

| 能力模块 | 含义 |
|---|---|
| Reasoning and Planning | 任务分解、推理和规划 |
| Tool Integration | 调用外部工具、数据库、代码环境和科学软件 |
| Memory | 保存任务状态、经验、知识和长期上下文 |
| Multi-agent Collaboration | 多个 agent 通过任务分配、信息综合和协作解决复杂科学问题 |
| Optimization and Evolution | 通过搜索、反馈和迭代改进产物 |

### 对本文的启发

该综述已经承认 multi-agent collaboration 是 Agentic Science 的核心能力之一，但没有把它作为全文组织主线。本文可以承接它的宏观叙事，并进一步说明：当科学发现从单点任务走向长周期、跨工具、跨证据边界的工作流时，multi-agent organization 不只是一个能力模块，而是组织科学发现的系统原则。

参考链接：

- https://arxiv.org/abs/2508.14111

### 8.3 Agentic AI for Scientific Discovery：multi-agent 作为系统形态

代表综述：

- `Agentic AI for Scientific Discovery: A Survey of Progress, Challenges, and Future Directions`

该综述会区分 single-agent 和 multi-agent 系统。multi-agent 通常被理解为一种系统形态：多个 agents 通过不同角色、工具或 persona 协作完成科学任务。

| 分类角度 | 内容 |
|---|---|
| Single-agent systems | 一个 agent 独立规划、调用工具和完成任务 |
| Multi-agent systems | 多个 agents 分担角色、工具、领域知识或评估职责 |
| Human-AI collaboration | 人类专家参与监督、反馈、验证或决策 |
| Systems and tools | 不同 agentic scientific discovery 工具和平台 |
| Evaluation and benchmarks | 用数据集、指标和任务评价系统能力 |

### 对本文的启发

该类综述适合帮助本文说明 single-agent 与 multi-agent 是 agentic scientific discovery 中不同的系统形态。但它对 multi-agent 内部的组织机制展开不够。本文应进一步细化：角色如何定义，任务如何分配，产物如何交接，分歧如何解决，验证如何独立，责任如何追踪。

参考链接：

- https://arxiv.org/abs/2503.08979

### 8.4 AI Scientist 综述：multi-agent 作为端到端科研系统的实现机制

代表综述：

- `A Survey of AI Scientists`

这类综述主要按 AI scientist 的端到端科研流程组织文献，但会将 multi-agent roles、agentic tree search、tool use 和 reviewer agents 作为重要方法机制。

| 分类轴 | multi-agent 的位置 |
|---|---|
| Literature Review | 多个阅读、检索或综述 agents |
| Idea Generation | 多个 idea generators、critics 或 rankers |
| Experimental Preparation | planner、coder、tool executor 等角色分工 |
| Experimental Execution | 执行、调试、分析角色之间的交接 |
| Scientific Writing | writer、reviewer、editor agents |
| Paper Generation / Review | 自动论文生成、审稿和元评审 |

### 对本文的启发

该范式适合作为单智能体或 pipeline 式 AI scientist 的对照。它说明 multi-agent 经常出现在端到端科研自动化系统中，但它通常仍服务于“完成科研流程”这一叙事。本文需要突出的是：multi-agent 不只是端到端流程中的实现技巧，而是科学劳动分工、独立审查、产物交接和证据闭环的组织方式。

参考链接：

- https://arxiv.org/html/2510.23045v3

### 8.5 通用 LLM-MAS 综述：coordination taxonomy 的主要来源

代表综述：

- `Multi-Agent Collaboration Mechanisms: A Survey of LLMs`
- `Large Language Model based Multi-Agents: A Survey of Progress and Challenges`
- `A survey on LLM-based multi-agent systems: workflow, infrastructure, and challenges`

这些综述不专门研究科学发现，但提供了最成熟的 multi-agent coordination 分类语言。

| 通用 MAS 分类维度 | 含义 | 可迁移到科学发现的表述 |
|---|---|---|
| Actors | 参与协作的 agents 是谁 | literature agent、hypothesis agent、critic、executor、analyst、verifier、human PI |
| Interaction Types | agents 之间是什么关系 | cooperation、competition、critique、adjudication |
| Structures | 系统组织结构是什么 | fixed-role team、coordinator-worker hierarchy、peer network、open capability network |
| Strategies | 如何进行协作 | role specialization、parallel exploration、debate、review、task bidding |
| Coordination Protocols | 如何通信、分配任务和决策 | tournament、peer review、artifact handoff、human checkpoint、EACN |
| Memory and State | 如何共享上下文和状态 | shared project memory、evidence memory、failed-branch archive、provenance graph |
| Evaluation | 如何评估多智能体系统 | role utility、coordination quality、conflict resolution、collective hallucination |

### 对本文的启发

这类综述最适合支撑本文第 4 章的组织语言。本文可以吸收 actors、structures、strategies、protocols 等概念，但必须将它们科学发现化：多智能体协作的对象不是一般任务输出，而是带有证据状态、执行记录和验证边界的 scientific artifacts。

参考链接：

- https://arxiv.org/abs/2501.06322

### 本文可形成的差异化表述

现有自主科学发现综述已经注意到 multi-agent collaboration，但通常将其作为科学 agent 的一种能力、系统实现方式或应用案例。本文进一步把 multi-agent organization 提升为核心分析主线，系统讨论科学劳动、科学能力、科学产物和验证边界如何通过多智能体工作流被组织、协调、演化和评估。

## 9. 对本文结构的直接建议

综合以上综述分类，本文最适合采用的总框架是：

> Multi-agent organization × Search/evolution mechanism × Scientific artifact/substrate × Verification/evaluation boundary

具体对应关系如下：

| 本文部分 | 可借鉴的外部分类 |
|---|---|
| 引言与背景 | AI4S -> Agentic Science；Tool -> Analyst -> Scientist |
| 核心概念与分析维度 | agent architecture、capability、tool、memory、harness |
| 为什么需要多智能体 | multi-agent coordination、Human-AI Collaboration |
| 多智能体科研工作流组织架构 | actors、roles、interaction structures、coordination protocols |
| 搜索与演化机制 | planning、execution、feedback learning、artifact evolution、harness evolution |
| 科学产物、执行载体与验证边界 | language、code、proof、simulation、physical lab、peer review |
| 评估、基准与证据闭环 | system evaluation、process evaluation、output verification、governance |
| 基础设施与开放问题 | memory、skills、tools、platforms、SDL stack |

## 最终写作立场

本文可以在引言中明确写出与已有综述的差异：

> 既有综述多从科学流程、自治程度、应用领域、工具系统或实验室基础设施出发组织文献；本文则进一步把 multi-agent organization 作为自主科学发现的核心分析对象，讨论科学劳动、科学能力、科学产物和验证边界如何通过多智能体工作流被组织起来。

这样可以避免本文被理解为“又一篇 autonomous scientific discovery 综述”，而是突出本文真正的切入点：**多智能体不是实现细节，而是自主科学发现的组织原则。**
