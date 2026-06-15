# Skill-Driven Agentic Scientific Discovery：53 篇论文证据矩阵

> 目的：把已有 53 篇笔记重新映射到“Scientific Workflow × Skill Lifecycle”框架中，验证 skill lifecycle 是否能作为分析 autonomous scientific discovery agents 的可证实视角。  
> 证据来源：`Notes/` 下已校正论文笔记与五个分矩阵；本表不替代原矩阵，而是作为综述论证骨架。

## 0. 判定标签

| 标签 | 含义 |
|---|---|
| **Direct** | 论文直接研究 skill / skill lifecycle / skill specification / skill evaluation。 |
| **Indirect** | 论文不使用 skill 术语，但包含可复用 workflow、memory、artifact、tool routine 或 verification procedure。 |
| **Boundary** | 论文主要提供评测、限制、反例或能力边界，用来约束 skill-driven 论证。 |

## 1. 总体结论

1. 53 篇中，真正 **Direct skill** 的论文集中在 `skills-ecosystem`、`SkillOS`、`SSL`、`CUHK Survey`、`Perplexity Skills Guide` 与 `Agent Skills Spec`。
2. 核心自动科研系统多为 **pipeline-driven**，不是严格 skill-driven；它们证明了科研 workflow 可以自动化，但尚未证明 workflow 已被沉淀为可检索、可组合、可演化的 skill。
3. 记忆论文提供 skill evolution 的必要基础，但也给出警告：经验压缩为抽象 skill 时必须保留可回溯情景证据。
4. benchmark 与 verification 论文构成约束层：没有复现、引用、审稿、人工评估或任务基准，skill-driven discovery 只能是工程叙事，不能成为科学论证。

## 2. 53 篇逐篇证据矩阵

| # | Paper | Note | 论文类型 | Scientific Workflow Stage | Skill Lifecycle Stage | Skill / Procedural Form | 对本综述的证据作用 | 关键限制 |
|---:|---|---|---|---|---|---|---|---|
| 1 | AI Scientist v1 | `systems/AI_Scientist_2024.md` | System | Hypothesis → Experiment → Writing → Review | Execution / weak Evolution | archive-based idea loop + coding + automated review pipeline | **Indirect**：证明端到端科研 workflow 可被 agent pipeline 串起，是 pipeline-driven discovery 的代表 | 缺少显式 skill representation / retrieval；产出质量和安全仍弱 |
| 2 | AI Scientist Nature | `systems/AI_Scientist_Nature_2026.md` | System | End-to-end AI research; workshop validation | Execution / Verification | template-free agentic tree search + VLM check + automated reviewer | **Indirect**：给出真实同行评审验证，支撑 scientific closure 的重要性 | 仅 1/3 workshop 通过；质量与模型/计算为相关性，不是单调证明 |
| 3 | Agent Laboratory | `systems/Agent_Laboratory_2024.md` | System | Literature → Experiment → Report | Execution / Human checkpoint | 5-role agent pipeline + mle-solver + paper-solver | **Indirect**：展示 human-in-the-loop 科研 pipeline，可作为“人类创意 + agent 执行层”的证据 | 不是可复用 skill library；自动审稿显著高估 |
| 4 | AI-Researcher HKU | `systems/AI_Researcher_HKU_2025.md` | System | Idea / Reference → Experiment → Paper | Acquisition / Execution | resource collection + idea generation + Docker experiment + hierarchical writing | **Indirect**：体现从参考文献到实验实现的自动化研究流程 | 创意质量缺大规模盲评；独立同行评审证据不足 |
| 5 | GPT Researcher | `systems/GPT_Researcher_2024.md` | System | Literature search / report synthesis | Retrieval / Synthesis | planner + parallel source crawling + publisher synthesis | **Indirect**：把“深度研究报告”拆成可执行检索与综合流程 | 主要是信息综合，不是实验科学发现 |
| 6 | ARA | `systems/ARA_2026.md` | System / Infrastructure | Synthesis → Reproduction → Verification | Representation / Verification | four-layer Agent-Native Research Artifact + ARA Seal | **Direct-ish**：把科研产物本身转为 agent-readable, evidence-linked artifact，是 scientific skill/artifact 表示层核心证据 | 只能恢复论文中已有信息；湿实验适配不足 |
| 7 | SkillOS | `systems/SkillOS_2026.md` | Skill system | General task execution | Acquisition / Evolution | SkillRepo + RL-trained manager for add/modify/delete | **Direct**：证明 skill management 可以被建模为长期策略学习 | 未测试开放域科研发现；检索仍偏 BM25 |
| 8 | SSL | `systems/SSL_2026.md` | Skill system | Skill routing / execution support | Representation / Retrieval | scheduling-structural-logical 三层 skill graph | **Direct**：证明 skill 表示会影响检索与执行，支撑“技能不是纯文本说明” | 静态归一化，不能保证运行时行为 |
| 9 | GAIA | `benchmarks/GAIA_2023.md` | Benchmark | General assistance / tool use | Verification | multi-step tasks requiring browsing, tools, multimodal reasoning | **Boundary**：说明工具调用与多步推理仍远弱于人类，是 skill routing 的外部压力 | 不测科研流程和过程质量 |
| 10 | HLE | `benchmarks/HLE_2025.md` | Benchmark | Knowledge / reasoning baseline | Verification | expert-authored closed questions + calibration | **Boundary**：证明专业知识仍是瓶颈，约束“agent 可自主科研”的上限 | 封闭问答不等于开放发现 |
| 11 | SimpleQA | `benchmarks/SimpleQA_2024.md` | Benchmark | Factual knowledge / uncertainty | Verification | short-answer factuality + not-attempted calibration | **Boundary**：支撑科学 agent 必须有自知之明和事实校准 | 不测检索、引用和长链科学推理 |
| 12 | BrowseComp | `benchmarks/BrowseComp_2025.md` | Benchmark | Web search / information discovery | Retrieval / Verification | reverse-built hard-to-find web questions | **Boundary**：说明深度浏览是可测能力，信息检索可通过工程显著增强 | 单一短答案，不能代表系统性文献综述 |
| 13 | MLE-Bench | `benchmarks/MLE_Bench_2024.md` | Benchmark | ML experiment / model optimization | Execution / Verification | Kaggle competition environments + medal scoring | **Boundary**：把实验执行能力锚定到人类竞赛标准 | Kaggle 偏调参冲刺，过程不可解释性弱 |
| 14 | MLAgentBench | `benchmarks/MLAgentBench_2024.md` | Benchmark | ML experiment iteration | Execution / Feedback | design-code-run-analyze loop over ML tasks | **Boundary**：检验 agent 是否能进行实验迭代，而不只是一次性写代码 | 任务少，无严格人类基线 |
| 15 | RE-Bench | `benchmarks/RE_Bench_2024.md` | Benchmark | Long-horizon ML R&D | Execution / Time scaling | 7 ML R&D environments + normalized scoring | **Boundary**：揭示长时域工作中 AI 时间扩展弱于人类，是 skill persistence 的关键挑战 | 仅 7 环境，领域偏 ML |
| 16 | IdeaBench | `benchmarks/IdeaBench_2024.md` | Benchmark | Hypothesis / idea generation | Verification | relative idea ranking by dimensions | **Boundary**：把创意生成的新颖性/可行性分开评估 | LLM-as-judge 偏差；不验证实验成败 |
| 17 | ScienceAgentBench | `benchmarks/ScienceAgentBench_2025.md` | Benchmark | Data-driven scientific coding | Execution / Verification | tasks from 44 peer-reviewed papers, executable Python outputs | **Boundary**：对“端到端自动科学发现”形成基础能力约束：先能完成具体科学编码任务 | 仅 Python 数据驱动任务；o1-preview 为另行评估 |
| 18 | PaperBench | `benchmarks/PaperBench_2025.md` | Benchmark | Paper reproduction | Verification | 8,316 rubric leaves + author-designed grading | **Boundary**：为科研 agent 复现能力提供细粒度评估，是 scientific closure 核心基准 | 成本极高，LLM judge 仍有误差 |
| 19 | CORE-Bench | `benchmarks/CORE_Bench_2024.md` | Benchmark | Computational reproducibility | Execution / Verification | run code capsules and extract results | **Boundary**：复现已有研究是自动创造前提 | hard tasks 仍低，视觉/R 任务困难 |
| 20 | SUPER | `benchmarks/SUPER_2024.md` | Benchmark | Repository setup / execution | Execution / Verification | low-star research repos with exact/milestone scoring | **Boundary**：揭示真实科研仓库设置执行是基础瓶颈 | Python/NLP 偏置，外部依赖会漂移 |
| 21 | Paper2Code | `benchmarks/Paper2Code_2025.md` | Benchmark / System | Paper → Code implementation | Composition / Execution | planning → analysis → modular code generation | **Indirect**：体现论文复现可拆成多个可复用 coding procedures | 不是完整端到端复现；数据处理覆盖薄弱 |
| 22 | AutoSurvey | `benchmarks/AutoSurvey_2024.md` | Benchmark / System | Literature review | Retrieval / Synthesis / Verification | large-scale retrieval + outline + citation quality evaluation | **Indirect**：文献综述可被流程化，适合转成 literature-review skills | 批判性分析弱，依赖初始检索覆盖 |
| 23 | ReviewerGPT | `benchmarks/ReviewerGPT_2023.md` | Benchmark | Peer review subskills | Verification | error finding + checklist validation + pairwise judgment | **Indirect**：把审稿拆成可验证子任务，是 review skill 的雏形 | 样本小，生态效度有限 |
| 24 | Reviewer2 | `benchmarks/Reviewer2_2024.md` | Benchmark / Model | Review generation | Acquisition / Execution | aspect prompt generation + review text generation | **Indirect**：把“写审稿”条件化为 aspect-guided generation | 仅 ML/NLP，模型较旧 |
| 25 | PeerRead | `benchmarks/PeerRead_2018.md` | Dataset | Peer review / acceptance prediction | Verification | paper-review-decision dataset + aspect scores | **Boundary**：提供审稿数据基础，支撑 review/rebuttal skill 的训练与评估 | 数据源偏差，不能直接判断论文真实质量 |
| 26 | AgentReview | `benchmarks/AgentReview_2024.md` | Simulation / Benchmark | Peer review dynamics | Verification / Governance | multi-agent simulation of reviewer bias/social influence | **Boundary**：提醒 LLM reviewer 也会携带偏见，约束自动审稿闭环 | 模拟不等于真实评审 |
| 27 | MemGPT | `memory/MemGPT_2023.md` | Memory | Long-context research state | Retrieval / Execution | OS-like main/external context paging | **Indirect**：为长时域科研 agent 提供上下文管理机制 | 内存管理依赖 LLM 自判，可靠性风险 |
| 28 | Generative Agents | `memory/Generative_Agents_2023.md` | Memory | Planning / simulation | Acquisition / Evolution | memory stream + reflection + planning | **Indirect**：反思把经验转为高层推断，是 skill acquisition 的认知前身 | 非科研任务，检索权重固定 |
| 29 | Memory Sandbox | `memory/Memory_Sandbox_2023.md` | Memory / HCI | Memory governance | Representation / Governance | user-visible memory objects | **Indirect**：说明可观察、可编辑记忆对可信科研 agent 必要 | 手工交互不可扩展 |
| 30 | Collaborative Memory | `memory/Collaborative_Memory_2025.md` | Memory | Collaborative research state | Governance / Verification | private/shared memory + dynamic access graph + provenance | **Indirect**：为多人科研团队的权限与溯源提供机制 | 合成实验，冷启动未解决 |
| 31 | Mesh Memory Protocol | `memory/Mesh_Memory_Protocol_2025.md` | Memory protocol | Multi-agent knowledge exchange | Representation / Governance | CAT7 schema + SVAF role-based evaluation + DAG lineage | **Indirect**：多 agent 科研需要语义协议和谱系控制 | 固定 schema 可能限制领域表达 |
| 32 | A-MEM | `memory/A_MEM_2025.md` | Memory | Knowledge organization | Acquisition / Evolution | Zettelkasten-style linked memory notes | **Indirect**：展示经验/记忆可自主组织与动态演化，是 skill library evolution 的相邻证据 | 文本单模态，非科学发现验证 |
| 33 | MIRIX | `memory/MIRIX_2025.md` | Memory | Multi-type research memory | Representation / Retrieval | core/episodic/semantic/procedural/resource/knowledge-vault memories | **Indirect**：procedural/resource memory 直接支持科研 skill 与证据分层 | 记忆类型边界和 agent 协调开销未充分验证 |
| 34 | Intrinsic Memory Agents | `memory/Intrinsic_Memory_Agents_2025.md` | Memory / Multi-agent | Role-specialized collaboration | Evolution / Collaboration | role-specific intrinsic memory updates | **Indirect**：支持“不同科研角色需要不同记忆/skill”的归纳 | token 开销大，非科研真实场景 |
| 35 | Graph Agent Memory | `memory/Graph_Agent_Memory_2025.md` | Survey | Memory infrastructure | Representation / Retrieval / Evolution | graph-memory taxonomy and lifecycle | **Indirect**：为 evidence graph、skill graph、research DAG 提供统一记忆视角 | 综述无原创实验，科学发现讨论不足 |
| 36 | Memory Warning | `memory/Memory_Warning_2026.md` | Memory / Boundary | Long-horizon memory update | Evolution / Verification | episodic traces vs consolidated abstractions | **Boundary**：强烈约束 skill evolution：抽象更新会损害已会能力，必须保留原始情景证据 | 文本 ARC-AGI 设置，非科研实验 |
| 37 | Voyager | `skills-ecosystem/Voyager_2023.md` | Skill system | Open-ended exploration | Acquisition / Retrieval / Composition | executable code skill library + embedding retrieval | **Direct**：经典“经验→代码技能库→复用组合”证据 | Minecraft 环境，非科学发现 |
| 38 | AWM | `skills-ecosystem/AWM_2024.md` | Skill / Workflow memory | Web task execution | Acquisition / Execution | abstract workflow memory from successful trajectories | **Direct**：把轨迹抽象为可复用 workflow，是 skill acquisition 的重要证据 | 动态 UI 中错误 workflow 难纠正 |
| 39 | Reflexion | `skills-ecosystem/Reflexion_2023.md` | Skill / Reflection | Retry-based task solving | Acquisition / Evolution | verbal reflection memory as semantic gradient | **Direct-ish**：失败经验转为自然语言策略，可视为轻量 skill update | 依赖自评估，可能局部最优 |
| 40 | Buffer of Thoughts | `skills-ecosystem/Buffer_of_Thoughts_2024.md` | Skill / Reasoning | Reasoning transfer | Retrieval / Composition | meta-buffer of reusable thought templates | **Direct**：把求解方法论作为可检索模板，支撑 cognitive skill 复用 | 创意任务提升有限 |
| 41 | ExpeL | `skills-ecosystem/ExpeL_2024.md` | Skill / Experience learning | Agent task transfer | Acquisition / Retrieval | experience-derived natural-language insights | **Direct**：证明 agent 可从成功/失败轨迹抽取可迁移经验 | 与 SkillsBench 自生成低收益形成张力 |
| 42 | SkillsBench | `skills-ecosystem/SkillsBench_2025.md` | Skill benchmark | Skill utility evaluation | Verification | curated vs self-generated skills over 86 tasks | **Direct / Boundary**：量化 skill 是否有效，显示精选技能有效、自生成技能近零收益 | 科研技能未纳入，自生成只测单次 |
| 43 | Anthropic Skills Spec | `skills-ecosystem/Anthropic_Skills_Spec_2025.md` | Skill specification | Cross-domain execution | Representation / Retrieval | SKILL.md + scripts/references/assets + progressive disclosure | **Direct**：确立 skill 的文件系统形态和按需加载机制 | 绑定 Claude 生态，依赖人工编写 |
| 44 | Agent Skills Spec | `skills-ecosystem/Agent_Skills_Spec_2026.md` | Skill specification | Cross-platform skills | Representation / Interoperability | open SKILL.md directory convention | **Direct**：支撑“skill 作为跨平台能力单元”的论证 | 执行语义仍不完全标准化 |
| 45 | CUHK Agent Skills Survey | `surveys/CUHK_Agent_Skills_Survey_2026.md` | Survey | General skill lifecycle | Representation / Acquisition / Retrieval / Evolution | formal skill lifecycle taxonomy | **Direct**：给本综述纵轴提供外部综述支撑 | 通用 agent 视角，科学发现垂直映射不足 |
| 46 | Memory in the Age of AI Agents | `surveys/Memory_Age_Survey_2025.md` | Survey | Agent memory landscape | Representation / Dynamics | forms-functions-dynamics taxonomy | **Indirect**：给科研 memory/evidence/experience 层提供通用框架 | 未聚焦科研不确定性与实验证据 |
| 47 | Memory for Autonomous Agents | `surveys/Memory_Autonomous_Survey_2025.md` | Survey | Autonomous agent memory | Acquisition / Retrieval / Evolution | mechanisms, evaluation, future directions | **Indirect**：补充 memory 写入-管理-读取闭环 | 科学发现映射需我们自己完成 |
| 48 | Osmani Agent Skills | `surveys/Osmani_Agent_Skills_2026.md` | Practitioner survey / repo | Software engineering workflow | Representation / Execution / Verification | lifecycle commands + source-driven engineering skills | **Direct-ish**：工程 skill 可迁移为科研代码/验证 discipline | 软件工程场景，非科研 benchmark |
| 49 | Perplexity Skills Guide | `infrastructure/Perplexity_Skills_Guide_2026.md` | Infrastructure guide | Production skill management | Representation / Retrieval / Evaluation | index-load-runtime progressive loading + eval-driven skill design | **Direct**：给技能库工程化、按需加载、评估迭代提供生产证据 | 厂商实践文档，非同行评审论文 |
| 50 | GStack | `infrastructure/GStack_2025.md` | Infrastructure / methodology | Multi-agent engineering workflow | Composition / Execution / Reflection | virtual team + sprint skills + reflect loop | **Indirect**：并行 sprint 可映射多假设科研验证 | 工程团队方法论，科学证据薄 |
| 51 | OpenScholar | `verification/OpenScholar_2025.md` | Verification / System | Literature synthesis / citation verification | Retrieval / Verification | 45M paper corpus + self-feedback retrieval + citation checks | **Indirect**：把引用正确性变成可执行 procedure，是 scientific evidence skill 核心 | 文献层可信，不等于实验发现 |
| 52 | LLM-as-a-Verifier | `verification/LLM_Verifier_2025.md` | Verification | Agent trajectory / task result verification | Verification / Selection | fine-grained scoring + repeated pairwise verification + decomposed criteria | **Indirect**：提供 agent 产出选择与轨迹验证机制 | verifier 不能替代硬证据 |
| 53 | Stanford Human Study | `verification/Stanford_Human_Study_2024.md` | Human study | Idea generation evaluation | Verification / Governance | 100+ NLP researchers blind-review AI vs human ideas | **Boundary**：证明 AI 创意可新颖但可行性/自评不足，限制 autonomous ideation claims | 仅 NLP 创意阶段，非端到端执行 |

## 3. 从矩阵得到的可写入正文的归纳

### 3.1 现有自动科研系统主要是 pipeline-driven，不是完整 skill-driven

AI Scientist、Agent Laboratory、AI-Researcher HKU 与 GPT Researcher 证明了科研 workflow 可以被拆成阶段并自动执行，但它们大多没有显式的 skill representation、skill retrieval、skill versioning 或 skill retirement。它们是 skill-driven 综述的“前史”和目标对象，而不是充分实现。

### 3.2 真正成熟的 skill 证据来自通用 Agent 领域

Voyager、AWM、ExpeL、Reflexion、Buffer of Thoughts、SkillOS、SSL、Anthropic Skills Spec、Agent Skills Spec 与 Perplexity Skills Guide 共同证明：skill 可以被表示、存储、检索、组合、评估和演化。但这些证据大多来自 Minecraft、Web task、软件工程或通用任务，尚未充分迁移到科学发现。

### 3.3 记忆系统是 skill evolution 的前置条件，但也是风险来源

A-MEM、MIRIX、Graph Agent Memory 等说明经验可以结构化为可检索、可演化的长期知识；Memory Warning 则提醒，持续整合会把有用经验变成错误抽象。因此科研 skill evolution 必须保留 episodic evidence，而不能只保留抽象规则。

### 3.4 Benchmark 与 verification 是 skill-driven discovery 的约束层

PaperBench、CORE-Bench、RE-Bench、ScienceAgentBench、OpenScholar、LLM-as-a-Verifier 与 Stanford Human Study 共同说明：科研 Agent 的 skill 不能只按“任务完成”评估，还要按复现、引用、审稿、人类判断、轨迹验证和成本进行外部约束。

### 3.5 当前最清楚的缺口

1. **科研 skill 表示缺口**：缺少面向 hypothesis、experiment、analysis、review 的统一 `SKILL.md` / artifact schema。
2. **科研 skill acquisition 缺口**：从失败实验、审稿反馈、复现日志中提取 skill 的机制尚不成熟。
3. **科研 skill retrieval 缺口**：现有检索多基于文本相似度，缺少任务阶段、资源约束、证据强度和安全风险感知。
4. **科研 skill evolution 缺口**：长期更新容易产生错误抽象，需要版本、溯源、回滚和证据锚定。
5. **scientific closure 缺口**：多数系统停在论文/代码生成，真实世界实验验证、湿实验闭环和独立复现仍稀缺。

## 4. 第二轮新增精读证据（15 篇）

> 本节把第二轮新增笔记纳入同一套 `Scientific Workflow x Skill Lifecycle x Evidence Role` 标注。它不替换上面的 53 篇矩阵，而是用来检验 v1 框架在真实科学发现、湿实验、科学工具链、假设生成和安全治理上的覆盖能力。

| # | Paper | Note | Scientific Workflow Stage | Skill Lifecycle Stage | Evidence Role | 关键证据 | 对框架的含义 |
|---:|---|---|---|---|---|---|---|
| 54 | AI Co-Scientist | `systems/CoScientist_2026.md` | Knowledge Grounding / Hypothesis Generation / Experiment Design / Verification / Evolution | Literature-derived acquisition / multi-agent composition / human review / real-world validation | **Indirect + Boundary** | 多 agent 生成、批判、排序和演化生物医学假设，并连接药物重定位、靶点发现和机制解释的湿实验初步验证 | 说明科学发现 agent 的核心过程可被组织成可批判、可排序、可演化的 procedure；但仍依赖专家选择和实验资源，不应被写成全自动发现 |
| 55 | Robin | `systems/Robin_2026.md` | Knowledge Grounding / Hypothesis Generation / Experiment Design / Execution interface / Result Analysis / Verification / Evolution | Tool-chain composition / multi-agent composition / result-driven memory update | **Indirect + Infrastructure** | Crow、Falcon、Finch 等 agent 连接文献、assay 选择、实验数据分析与下一轮候选生成，并提出 ripasudil 作为 dAMD 药物重定位候选 | 强化 lab-in-the-loop 证据：skill-driven science 不能只看文本生成，还要看实验结果如何反馈到下一轮任务 |
| 56 | Virtual Lab | `systems/Virtual_Lab_2025.md` | Knowledge Grounding / Experiment Design / Execution by computational workflow / Result Analysis / Verification / Synthesis | Multi-agent composition / workflow skill / code skill / human review | **Indirect + Infrastructure** | 多 agent 会议设计 ESM、AlphaFold-Multimer、Rosetta workflow，产生 92 个实验验证的 SARS-CoV-2 nanobody 突变体 | 证明多 agent 科研协作可以形成可执行 workflow skill；边界是合成和实验仍由人类完成 |
| 57 | CRISPR-GPT | `systems/CRISPR_GPT_2026.md` | Experiment Design / Execution / Result Analysis / Verification | Protocol skill / tool-chain composition / supervised execution / real-world validation | **Direct + Infrastructure** | 面向 22 类 gene-editing 任务、4 种实验模态和 3 种工作模式，生成 CRISPR 实验设计、协议和分析流程，并完成 A549 knockout 与 A375 activation 湿实验 | 是目前最接近“实验 protocol skill”的直接证据：把已知生物实验能力封装为可组合、可监督、可验证的 agentic workflow |
| 58 | Coscientist | `systems/Coscientist_2023.md` | Experiment Design / Execution / Result Analysis / Evolution | Tool use / lab action / tool-chain composition / feedback update | **Infrastructure + Boundary** | GPT-4 agent 使用 web search、文档检索、代码执行和实验自动化 API，规划并执行交叉偶联反应和条件优化 | 把 LLM agent 接到物理实验接口，是 execution skill 的重要底座；但安全、自动化程度和发现闭环仍有限 |
| 59 | A-Lab | `systems/ALab_2023.md` | Experiment Design / Execution / Result Analysis / Verification / Evolution | Literature-derived acquisition / lab action / closed-loop optimization / real-world validation | **Infrastructure + Boundary** | 计算筛选、文献学习 recipe、机器人合成、XRD 自动分析和 active learning 闭环，在 17 天内合成 36/57 个无机材料 target | 证明真实 self-driving lab 的闭环可行；也提醒 skill-driven LLM 视角必须纳入传感、样品处理和材料表征等物理基础设施 |
| 60 | ResearchAgent | `systems/ResearchAgent_2025.md` | Knowledge Grounding / Hypothesis Generation / Experiment Design / limited Verification | Literature-derived acquisition / reflection / human or LLM review | **Direct + Boundary** | citation graph、entity-centric knowledge augmentation 和 ReviewingAgents 迭代精炼研究想法 | 支持 hypothesis-generation skill 的流程化；边界是 idea 质量评价不能替代真实实验和同行评议 |
| 61 | LiveIdeaBench | `benchmarks/LiveIdeaBench_2026.md` | Hypothesis Generation / Verification | Benchmark-derived verification | **Boundary** | 以 1,180 个近期论文关键词构造 live idea-generation benchmark，发现模型 general intelligence 与研究创意表现相关性有限 | 直接约束“会推理就会科研创意”的假设，提示 hypothesis skill 需要独立评测 |
| 62 | Toolformer | `skills-ecosystem/Toolformer_2023.md` | Execution / Knowledge Grounding / Result Analysis | Tool-use acquisition / tool execution | **Direct + Infrastructure** | 从少量示例自监督生成和过滤 API-call 数据，使语言模型学习何时、如何调用 QA、calculator、search、MT、calendar 等工具 | 为 scientific tool-use skill 提供通用机制来源，但不直接证明科学发现 |
| 63 | ToolLLM | `skills-ecosystem/ToolLLM_2024.md` | Execution | Tool representation / retrieval / composition / execution / benchmark verification | **Direct + Infrastructure** | ToolBench 覆盖 16,464 个真实 API；系统包含 retriever、DFSDT 规划和 ToolEval 评测 | 证明大规模工具技能可以被检索、组合、执行和评测，可迁移为 scientific tools 生态的底层蓝图 |
| 64 | SciVer | `verification/SciVer_2025.md` | Verification / Result Analysis | Evidence retrieval / multimodal interpretation / benchmark verification | **Boundary** | 3k 多模态科学 claim-verification 样本；o4-mini 约 77.7，仍低于人类约 93.8，并暴露图表理解和细粒度证据匹配错误 | 说明 scientific verification skill 是当前瓶颈，尤其是多模态证据与 claim 对齐 |
| 65 | Risks of AI Scientists | `verification/Risks_AI_Scientists_2025.md` | Experiment Design / Execution / Verification / Governance | Safety verification / human regulation / environmental feedback | **Counterexample + Boundary** | 提出 human regulation、agent alignment、environmental feedback 三元治理框架和 AI scientists 风险分类 | 防止框架把“能自动执行”误写成“应自动执行”；skill 必须包含安全、权限和责任边界 |
| 66 | BioMedAgent | `systems/BioMedAgent_2026.md` | Execution / Result Analysis / Synthesis | Tool-aware execution / multi-agent composition / memory retrieval | **Direct** | BioMed-AQA 覆盖 327 个任务；系统接入 65 个 bioinformatics tools，在自然语言驱动生物医学分析中优于通用 LLM agent | 说明科学 skill 不只是假设生成，也包括面向数据分析的工具链规划、执行和报告生成 |
| 67 | GeneAgent | `systems/GeneAgent_2025.md` | Knowledge Grounding / Result Analysis / Verification | Database retrieval / self-verification / answer modification | **Direct** | 连接 18 个生物医学数据库和 4 个 API，构建 claim-level self-verification，显著降低 gene set 分析幻觉 | 强化“可靠 scientific skill = 数据库证据 + 可追溯验证 + 修正机制”，不是单纯 LLM 解释 |
| 68 | SciToolAgent | `systems/SciToolAgent_2025.md` | Knowledge Grounding / Execution / Result Analysis / Verification | Tool representation / KG retrieval / tool-chain composition / safety checking | **Direct + Infrastructure** | SciToolKG 集成 500+ 科学工具，SciToolEval 含 531 个任务，支持 chain-of-tools 规划、顺序执行和安全检查 | 是 scientific tool-chain skill 的最直接基础设施证据之一，补上 v1 中科学工具生态不足的缺口 |

## 5. 第二轮证据对 v1 框架的修正

1. **Direct 证据开始从通用 agent 迁移到科学场景**：CRISPR-GPT、BioMedAgent、GeneAgent、SciToolAgent 已经不只是通用 skill 类比，而是直接把 protocol、biomedical data analysis、database-grounded verification、scientific tool-chain 组织成可执行能力。
2. **Wet-lab 与 self-driving lab 不能只放在 Execution**：Co-Scientist、Robin、CRISPR-GPT、Coscientist 和 A-Lab 说明真实科学发现还涉及实验资源、人工监督、物理传感、失败反馈和安全权限，应同时标注为 Infrastructure 或 Boundary。
3. **Hypothesis Generation 需要独立边界层**：ResearchAgent 和 LiveIdeaBench 说明 idea generation 可被流程化和评测，但创意、可行性和真实发现之间不能划等号。
4. **Tool skill 是连接 skill lifecycle 与 scientific workflow 的关键桥**：Toolformer、ToolLLM、SciToolAgent 和 BioMedAgent 把 `Representation / Retrieval / Composition / Execution` 具体化为工具文档、工具图谱、工具检索、工具链规划和运行反馈。
5. **Verification 应从单一阶段升级为横贯约束**：SciVer、GeneAgent、Risks of AI Scientists 显示 verification 不只是最后打分，还包括证据检索、claim 对齐、数据库核查、安全检查和人类责任边界。

## 6. 当前最稳的阶段性判断

Skill-driven 视角可以继续保留，但应写成一个**分析框架**，而不是声称现有 autonomous scientific discovery agents 已经全面 skill-driven。更稳的表述是：

> 现有系统正在把科学发现从一次性 pipeline 推向由可复用 research skills 组成的 agentic workflow；但完整的 skill lifecycle，尤其是自主 acquisition、可靠 retrieval、跨实验 composition、长期 evolution 与 real-world verification，仍只在局部场景中成立。

## 7. 第三轮新增精读证据（30 篇）

> 本节把第三轮新增 30 篇笔记纳入同一套框架。第三轮证据的主要作用是：补齐真实科学发现、self-driving lab、科学工具链、hypothesis generation、governance/safety 和历史基线。

| # | Paper | Note | Scientific Workflow Stage | Skill Lifecycle Stage | Evidence Role | 关键证据 | 对框架的含义 |
|---:|---|---|---|---|---|---|---|
| 69 | CellVoyager | `systems/CellVoyager_2026.md` | Result Analysis / Hypothesis Generation / Synthesis | Notebook execution / analysis path selection / expert review | **Direct** | CellBench 覆盖 76 篇 scRNA-seq 论文；CellVoyager 在预测论文分析路径上最高提升 23%，并在 3 个 case study 中生成专家认可的新洞见 | 科学 skill 不只是假设和实验，也包括数据分析路径选择、notebook 执行和结果解释 |
| 70 | SPARK Cancer Pathology | `systems/SPARK_Cancer_Pathology_2026.md` | Hypothesis Generation / Execution / Result Analysis / Verification | Concept-to-code representation / parameter verification / cohort validation | **Direct** | 18 个队列、5 类癌症、超过 5,400 名患者；从 475 个 ideas 生成 2,368 个 parameters，并得到 1,115 个 nonredundant parameters | 把 biological concepts 转成可执行 pathology parameters，是 scientific skill representation 的强证据 |
| 71 | MOSAIC Chemical Synthesis | `systems/MOSAIC_Chemical_Synthesis_2026.md` | Knowledge Grounding / Experiment Design / Execution / Verification | Expert retrieval / protocol generation / real-world validation | **Direct + Infrastructure** | 2,498 个 specialized chemical experts；实验验证成功率 71%，合成 35+ 新化合物 | 支持“科学技能可分区、检索和组合”，尤其是化学合成 protocol skill |
| 72 | Medea | `systems/Medea_2026.md` | Knowledge Grounding / Result Analysis / Hypothesis Generation / Verification | Tool-chain composition / intermediate verification / abstention | **Direct** | 5,679 个 open-ended omics analyses；target identification、synthetic lethality、immunotherapy prediction 均有提升 | 强化 verification-aware long-horizon biomedical agent，说明中间步骤验证是科学 skill 的核心 |
| 73 | Kosmos | `systems/Kosmos_2025.md` | Knowledge Grounding / Hypothesis Generation / Result Analysis / Synthesis / Verification | World-model memory / long-horizon execution / evidence-linked reporting | **Direct + Boundary** | 12 小时运行、约 200 个 rollouts、平均 42,000 行代码和 1,500 篇论文；79.4% statements 被评为 accurate | 补足跨域长程 AI scientist；但 preprint 和高成本提醒不能过度声称成熟 |
| 74 | SciAgentGym | `benchmarks/SciAgentGym_2026.md` | Execution / Verification | Tool dependency graph / tool-chain execution / benchmark grading | **Direct + Boundary** | 1,780 个科学工具；GPT-5 短交互成功率 60.6%，长交互成功率 30.9% | 证明 scientific tool-use 可被系统评测，也显示长程工具链仍是瓶颈 |
| 75 | ChemCost | `benchmarks/ChemCost_2026.md` | Knowledge Grounding / Result Analysis / Verification | Resource-aware retrieval / procurement reasoning / arithmetic verification | **Counterexample + Boundary** | 1,427 个反应、2,261 个化学品、230,775 个报价；最强 agent 在 25% relative error 内仅 50.6% | 强反例：有工具和化学知识不等于会科学资源推理 |
| 76 | RoboChem-Flex | `systems/RoboChem_Flex_2026.md` | Experiment Design / Execution / Result Analysis / Verification / Evolution | Low-cost lab action / BO curator / scale-up validation | **Infrastructure + Direct** | 6 个 case studies；human-in-loop 入口配置约 US$5,000；多个反应完成 microscale optimization 与 scale-up | 说明 self-driving lab 的可及性、模块化和成本也是 scientific skill 落地条件 |
| 77 | Adaptive AI Decision Interface | `systems/Adaptive_AI_Decision_Interface_2025.md` | Experiment Design / Execution / Result Analysis / Verification | Human-AI decision skill / real-time monitoring / characterization | **Direct + Infrastructure** | 64 次 autonomous trials；发现提高 volumetric capacitance 的结构因素和此前未知 polymer polymorph | 强化 human-in-the-loop：科学 skill 可以是实时决策界面，不必等于全自动 |
| 78 | Rainbow Perovskite SDL | `systems/Rainbow_Perovskite_2025.md` | Experiment Design / Execution / Result Analysis / Evolution / Verification | Multi-robot orchestration / BO update / Pareto-front discovery | **Infrastructure + Direct** | 四机器人平台，6D input / 3D output parameter space，绘制 MHP nanocrystal PLQY-FWHM Pareto fronts | 补足 physical lab skill：机器人、在线表征和多目标优化共同构成实验技能 |
| 79 | AFION Plasmonic SDL | `systems/AFION_Plasmonic_SDL_2025.md` | Experiment Design / Execution / Result Analysis / Evolution | Microfluidic lab action / online spectroscopy / multi-objective optimization | **Infrastructure + Direct** | 七维反应条件空间；微流控光化学合成 + in-line spectrometer + Gryffin/Chimera 闭环 | 证明 flow/microfluidic SDL 是 wet-lab skill 的重要实现形态 |
| 80 | Benchmarking SDL | `benchmarks/Benchmarking_SDL_2026.md` | Verification / Benchmarking / Evolution | Benchmark design / acceleration factor / comparability | **Infrastructure + Boundary** | 讨论 acceleration factor、search-space dimension、number of experiments 等 SDL 横向指标 | 防止把单个 SDL 成功案例写成普遍结论，要求成本和任务难度可比 |
| 81 | Self-Driving Labs ChemRev | `surveys/Self_Driving_Labs_ChemRev_2024.md` | Experiment Design / Execution / Result Analysis / Evolution | Lab action / protocol skill / autonomous planning | **Infrastructure** | 系统梳理 chemistry/materials SDL 的硬件、软件、决策层和应用 | 给 wet-lab / robotic lab 章节提供权威技术地图 |
| 82 | SafeScientist | `verification/SafeScientist_2025.md` | Experiment Design / Execution / Verification / Governance | Risk-aware execution / safety benchmark / guardrail | **Boundary + Infrastructure** | 提出 risk-aware scientific agent 和 SciSafetyBench | 明确 skill 必须包含不可执行、需审查、需升级给人类的条件 |
| 83 | SPOT-a | `verification/SPOT_A_2025.md` | Verification / Reproducibility | Error detection benchmark / post-hoc checking | **Counterexample + Boundary** | 83 篇 manuscripts、10 个科学领域，用于检测科学研究错误 | 约束 co-scientist 乐观叙事：生成科学文本不等于能发现错误 |
| 84 | Hidden Prompts Peer Review | `verification/Hidden_Prompts_Peer_Review_2025.md` | Verification / Peer Review / Governance | Adversarial document parsing / prompt-injection defense | **Counterexample** | 发现 18 篇 arXiv manuscripts 含 hidden prompts，并归纳 4 类攻击 | 说明自动审稿和 verifier skill 会被 manuscript 操纵，治理必须考虑对抗面 |
| 85 | AI Responsible Publishing | `verification/AI_Responsible_Publishing_2026.md` | Synthesis / Peer Review / Governance | Disclosure protocol / accountability / confidentiality | **Infrastructure + Boundary** | Nature Methods editorial 明确 AI 写作、审稿、署名和披露边界 | 给 AI-generated research artifact 的出版制度边界 |
| 86 | RINoBench | `benchmarks/RINoBench_2026.md` | Hypothesis Generation / Verification | Novelty judgment benchmark / human-gold evaluation | **Boundary** | 1,381 个 research ideas 和 9 个 automated metrics | 约束 idea novelty skill：解释像人不等于 novelty judgment 准确 |
| 87 | Causal Hypothesis LLM | `systems/Causal_Hypothesis_LLM_2025.md` | Hypothesis Generation / Verification | Causal hypothesis representation / expert-data validation | **Direct + Boundary** | 将 LLM 定义为 imperfect probabilistic expert，需与数据和专家结合 | 补 taxonomy 中 causal reasoning 子能力，同时限制 LLM 因果真理主张 |
| 88 | MC-NEST | `systems/MC_NEST_2025.md` | Hypothesis Generation / Verification / Evolution | Tree search / self-refinement / rubric evaluation | **Direct** | 用 Monte Carlo tree search + Nash equilibrium inspired refinement 优化科学假设 | 证明 hypothesis skill 可以是搜索、评估、精炼和选择过程 |
| 89 | Sparks of Science | `benchmarks/Sparks_of_Science_2025.md` | Knowledge Grounding / Hypothesis Generation / Verification | Structured paper data / hypothesis schema | **Infrastructure** | HypoGen、Bit-Flip-Spark schema 和 chain-of-reasoning | 给 literature-derived hypothesis skill 提供结构化数据和表示基础 |
| 90 | AI Idea Bench 2025 | `benchmarks/AI_Idea_Bench_2025.md` | Hypothesis Generation / Verification | Leakage-aware benchmark / grounded comparison | **Boundary + Infrastructure** | 聚焦 AI research idea generation 的 leakage-aware evaluation | 提醒 idea skill 必须控制文献泄漏和时间泄漏 |
| 91 | STELLA | `systems/STELLA_2025.md` | Knowledge Grounding / Execution / Result Analysis / Evolution | Dynamic tool pool / template library / self-evolution | **Direct** | Dynamic Tool Ocean + evolving template library | 补足 scientific skill evolution：工具池和模板库可随任务经验更新 |
| 92 | DatawiseAgent | `systems/DatawiseAgent_2025.md` | Execution / Result Analysis / Synthesis | Notebook cell execution / sequential workflow / runtime feedback | **Direct + Infrastructure** | notebook-centric data science agent | Notebook 是科研数据分析 skill 的真实执行载体 |
| 93 | Jupiter | `systems/Jupiter_Notebook_Agent_2025.md` | Execution / Result Analysis / Verification | Value-guided trajectory search / notebook execution | **Direct** | notebook + inference-time value-guided search | 说明数据分析 skill 可以在运行时搜索多条分析轨迹 |
| 94 | AlphaEvolve | `systems/AlphaEvolve_2025.md` | Hypothesis Generation / Execution / Verification / Evolution | Code artifact generation / automated evaluator / evolutionary refinement | **Direct + Indirect** | generate-test-refine loop，用 automated evaluator 进化候选算法 | 对可验证 discovery loop 很关键：有 evaluator 的领域更容易形成稳定 skill evolution |
| 95 | SciNav | `systems/SciNav_2026.md` | Execution / Result Analysis / Verification | Scientific code skill / top-K tree search / relative judgment | **Direct** | scientific coding tasks 中的 relative-judgment-guided search | 补足科学编码这一中间层：介于工具调用和完整科学发现之间 |
| 96 | TianJi | `systems/TianJi_2026.md` | Knowledge Grounding / Hypothesis Generation / Simulation / Verification | Numerical-model operation / mechanism search / physical consistency | **Direct** | autonomous AI meteorologist 用文献、假设、数值实验探索大气机制 | 把 agentic discovery 扩展到 earth science 和 simulation-based science |
| 97 | Climate Self-Evolving Agent | `systems/Climate_Self_Evolving_Agent_2025.md` | Result Analysis / Hypothesis Generation / Evolution | Code execution / physical reasoning / self-evolution | **Direct + Boundary** | climate science agent，含 Atlantic Niño 前兆发现案例 | 补非生物医学长程任务，但仍需独立气候学验证 |
| 98 | Robot Scientist | `systems/Robot_Scientist_2004.md` | Hypothesis Generation / Experiment Design / Execution / Verification / Evolution | Rule-based hypothesis / robotic experiment / knowledge update | **Infrastructure + Historical Baseline** | 2004 年 functional genomics 中生成、测试、更新假设的机器人科学家 | 说明 autonomous scientific discovery 有 LLM 之前的闭环历史，避免框架短视 |

## 8. 第三轮证据对框架的修正

1. **真实科学发现证据显著增强**：CellVoyager、SPARK、MOSAIC、Medea、Kosmos、TianJi 和 Climate Agent 说明 agentic discovery 已经从 AI/CS benchmark 扩展到 biology、medicine、chemistry、materials 和 earth science。
2. **Self-driving lab 成为独立主线**：RoboChem-Flex、Rainbow、AFION、Benchmarking SDL 和 ChemRev SDL 表明，wet-lab / robotic lab 不能只是 Execution 子项，而应作为 infrastructure-rich scientific workflow 讨论。
3. **Hypothesis Generation 从“生成文本”升级为“搜索与验证”**：RINoBench、Causal Hypothesis、MC-NEST、Sparks 和 AI Idea Bench 说明 hypothesis skill 需要 novelty judgment、causal constraints、search/refinement、structured paper data 和 leakage control。
4. **Tool-use 的边界更清楚**：SciAgentGym 证明科学工具链可以评测，ChemCost 则证明工具访问和领域知识仍不足以保证 resource-aware reasoning。
5. **Governance 不再只是附录**：SafeScientist、SPOT-a、Hidden Prompts 和 AI Responsible Publishing 说明 autonomous scientific discovery 必须把安全、错误检测、对抗文档和出版责任写成横贯约束。
6. **历史基线必须补入正文**：Robot Scientist 说明“自动生成假设并做实验”不是 LLM 时代才出现，本综述需要把 LLM agent 放入 robot scientist / self-driving lab 的长期脉络。

## 9. v2 阶段性判断

第三轮 30 篇证据使 `skill-driven` 视角更稳，但也迫使它更克制：

> Skill-driven agentic scientific discovery 不应被定义为“LLM 自主完成科学发现”，而应被定义为：科学发现 workflow 正在被拆解为可表示、可执行、可组合、可验证，并在部分场景中可演化的 research skills；这些 skills 必须嵌入实验基础设施、领域工具、证据系统和治理边界之中。

与 v1 相比，v2 可以更有把握地写：

1. 科学场景中已经出现 direct skill evidence，不再只是通用 agent skill 的类比。
2. wet-lab 与 self-driving lab 是 skill-driven science 的硬基础设施，不是外围案例。
3. verification/governance 是框架的横贯层，而不是最后一个章节。
4. long-horizon evolution 仍是弱项，但 STELLA、Kosmos、AlphaEvolve、Jupiter、RoboChem-Flex 等已经提供了局部机制。
