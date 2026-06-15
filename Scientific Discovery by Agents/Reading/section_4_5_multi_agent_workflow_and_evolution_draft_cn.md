# 第 4-5 章中文正文草稿：多智能体工作流模式与反馈/搜索/演化机制

> 写作口径：本草稿嵌入 `multi_agent_workflow_survey_outline.md` 的第 4、5 章框架；主要依据 `xyz_explicit_multi_agent_search_evolution_distribution.md` 中 72 篇去除 `X0` 与 `Y0` 后的显式多智能体、且包含反馈/搜索/演化机制的文献。  
> 写作定位：第 4 章回答“科学发现中的多智能体如何被组织”；第 5 章回答“这些工作流如何通过反馈、搜索与演化改进科学产物和 agentic harness”。二者不是并列文献清单，而是一套从组织结构到改进机制的连续分析。

## 4. 科学发现中的多智能体工作流模式

自主科学发现中的多智能体系统并不是把若干 LLM 角色放在同一个对话框中，而是一种面向科学劳动组织的工作流设计。科学发现包含文献 grounding、问题形成、假设生成、实验/仿真/代码/证明设计、执行、结果分析、综合报告、验证评审和长期迭代等环节；这些环节依赖不同工具、证据标准和责任边界。因而，系统设计的关键问题不再是“单个 agent 能否回答问题”，而是“哪些科学任务应被分配给哪些 agent，产物如何交接，错误如何暴露，验证如何独立，最终证据如何闭合”。

基于 72 篇显式多智能体且包含反馈/搜索/演化机制的工作，可以将当前多智能体 ASD 的组织形态概括为四类：固定角色团队、同角色多实例、层级式调度和开放能力网络。它们分别对应 `X2/X3/X4/X5`，也构成本文后续讨论反馈、搜索和演化机制的组织基础。

| 组织形态 | 核心问题 | 典型机制 | 代表系统 | 主要风险 |
|---|---|---|---|---|
| 固定角色多智能体 `X2` | 科学劳动如何分工？ | planner / researcher / coder / executor / analyst / critic / reviewer | Agent Laboratory, MLR-Copilot, MAESTRO, SparksMatter | 角色重叠、接口不清、形式化分工大于实际贡献 |
| 同角色多实例 `X3` | 如何扩大搜索和验证宽度？ | 多 prover、多 verifier、多 critic、多候选分支 | AlphaProof Nexus, BFS-Prover-V2, AccelMat, LLM Verifier | 虚假共识、重复计算、评审偏差相关性 |
| 层级式多智能体 `X4` | 复杂任务如何调度？ | supervisor-worker、planner-executor、orchestrator-specialist | MARS, MASTER, Robin, DREAMS, LeanMarathon | manager bottleneck、上层错误被规模化执行 |
| 开放能力网络 `X5` | 科学能力如何被发现和复用？ | capability discovery、task bidding、artifact exchange、reputation/trust | Science Earth, ScienceClaw Infinite, SCP, AgentRxiv, MACC | 能力认证、开放产物污染、责任归属困难 |

### 4.1 固定角色团队：从“角色提示”到科学劳动分工

固定角色多智能体是当前最密集的证据区。其基本思想是将科学发现拆解为若干职责相对稳定的角色，例如 literature agent 负责检索与 grounding，hypothesis agent 负责提出候选，coder/executor 负责实现和运行，analyst 负责解释结果，critic/reviewer 负责检查和修订。与普通 pipeline 不同，固定角色系统强调每个角色都产生可交接的科学产物，而不是仅在内部传递自然语言上下文。

`Agent_Laboratory_2024` 以 PhD、Postdoc、Engineer、Reviewer 等类科研角色组织文献综述、实验和报告写作；`MLR_Copilot_2024` 通过 IdeaAgent 与 ExperimentAgent 将机器学习研究中的想法生成、实验实现和调试执行分开；`MAESTRO_2026` 使用多个 specialized LLM roles 支撑催化剂设计循环；`SparksMatter_2025` 将材料研究中的 idea generation、experimental workflow design、critique 和 report 组织成固定角色流程。此类系统的共同点是：角色不只是 persona，而是承担不同的输入输出契约。

固定角色团队的优势在于降低单 agent 同时承担多种认知任务的负担，并使中间结果更容易被审查。文献检索结果、实验计划、代码实现、分析解释和评审意见可以分别进入后续角色，从而形成可追踪的产物链。但这一模式也有边界：如果角色没有独立工具、独立证据来源或明确权限，所谓多智能体可能退化为同一个模型的多轮自我复述。因而，固定角色系统的关键评估问题不是“用了几个角色”，而是“每个角色是否提供了不可替代的边际贡献”。

### 4.2 协调、交接与共享状态：多智能体系统的真正单位是产物

优秀的多智能体 ASD 系统通常不以对话本身为中心，而以科学研究产物为中心。也就是说，系统中的关键对象不是 chat history，而是带有 provenance、执行状态、证据支持和待解决问题的 artifact。一个候选假设、一段代码、一个实验方案、一个数据分析结果、一个 Lean proof、一个论文段落或一个失败分支，都应能被后续 agent 检查、复用、修订或拒绝。

`Kosmos_2025` 通过 structured world model 在 literature-search agent 与 data-analysis agent 之间维护长期状态，并要求报告中的 statement 由代码或 primary literature 支撑。`Robin_2026` 将 literature search、data analysis、hypotheses、experimental directions 和 lab-in-the-loop feedback 连接为迭代药物发现工作流。`MARS_Materials_2026` 通过 19 个 LLM agents 与 16 个领域工具将材料设计、机器人实验、数据分析和优化整合为 closed-loop autonomous materials discovery。

这些系统表明，协调协议的核心不是让 agent 更频繁地通信，而是保证交接发生在可审计对象上。没有 provenance 的共享记忆会污染后续推理；没有 promotion gate 的共享工作区会把错误产物升级为项目事实；没有明确 owner 的中间结果会导致责任扩散。因此，第 4 章中的 coordination 应被写成 artifact-centered coordination，而不是泛泛的 multi-agent communication。

### 4.3 批评、审稿与验证角色：将分歧转化为证据压力

科学发现不同于一般任务求解的关键在于，输出必须经受独立证据标准的约束。多智能体系统中的 critic、reviewer 和 verifier 因此不是辅助模块，而是 evidence closure 的组成部分。它们通过反驳、评分、形式验证、同行评审或专家检查，将生成过程中的不确定性转化为可选择、可淘汰或可修订的信号。

`AgentReview_2024` 和 `Generative_Adversarial_Reviews_2024` 将同行评审过程建模为多角色 agent workflow，覆盖 reviewer assessment、rebuttal、discussion、meta-review 和 final decision。`PaperOrchestra_2026` 面向论文写作，将 pre-writing materials 转化为 LaTeX manuscripts，并通过评价机制检查文本产物。`ResearchAgent_2025` 使用 reviewing agents 对 problem、method 和 experiment design 进行反馈。形式化系统中，`MA_LoT_2025` 将 prover、Lean verifier 和 corrector 连接为 proof draft -> verification feedback -> revised proof 循环；`BFS_Prover_V2_2025` 和 `LeanMarathon_2026` 则将 proof search 与 CI/Lean verifier 结合。

这一类系统的启示是，分歧本身是一种资源。候选之间的评分差异、reviewer 之间的不一致、proof checker 的错误信息、实验结果与预期之间的冲突，都可以触发下一轮搜索或修订。但若 critic 与 generator 共享相同偏差，或者 reviewer 只是复述 generator 的理由，系统会形成虚假共识。因此，验证角色的独立性、评价标准的透明性和反馈到工作流的路径，是多智能体 ASD 的关键设计问题。

### 4.4 同角色多实例：并行探索与独立检查

同角色多实例系统强调多个同类 agent 或同类候选并行工作。它与固定角色团队的区别在于，系统并不主要依靠职责互补，而是利用多个相似角色扩大搜索宽度、产生候选多样性或提高验证稳健性。

形式化证明是 `X3` 最清晰的应用场景。`AlphaProof_Nexus_2026` 使用 multiple provers、rating agents、population database 和 Lean-based verification；`BFS_Prover_V2_2025` 将 theorem/subgoal 分解后交给 parallel prover agents，并通过 shared proof cache 组织 multi-agent tree search；`Automatic_Textbook_Formalization_2026` 使用大量 agents 在 shared code base 中并行形式化教材内容，并通过 Pull Request review、merge queue 和 independent reviewers 筛选提交。科学假设和验证场景中，`AccelMat_2025` 使用 multi-LLM critic system 评估材料假设，`LLM_Verifier_2025` 使用多个 verifier models 扩展 test-time verification。

同角色多实例的价值在于将科学探索从单一路径扩展为候选集合或证明分支集合。它适合开放搜索空间、形式证明、候选评审和 verifier ensemble。但它也要求系统具备合并、缓存、去重、评分和冲突处理机制。否则，多实例只会放大 token 成本和重复探索，并不能提高科学可靠性。

### 4.5 层级式多智能体：复杂科研任务的调度与治理

当科学任务跨越文献、数据库、仿真、代码、实验和验证时，平面角色协作往往不足。层级式多智能体引入 coordinator、planner、supervisor、manager 或 orchestrator，对任务进行分解、调度、监控和整合。它的核心是将开放科学目标转换为可执行子任务，并在子任务执行后重新聚合为下一步决策。

材料发现提供了最密集的层级式证据。`MARS_Materials_2026` 使用 hierarchical architecture 调度多个 agents 与领域工具，连接设计、合成、优化和机器人实验。`MASTER_2025` 用 hierarchical agentic reasoning 指导 atomistic simulations。`Robin_2026` 通过多 agent 系统连接 literature search、data analysis、hypotheses、experimental directions 和 lab-in-the-loop feedback。`AGAPI_Agents_2025` 采用 Agent-Planner-Executor-Summarizer architecture，将材料数据库、预测模型、优化接口、衍射分析和逆向设计组织为 API orchestration workflow。

层级结构也出现在其他执行载体中。`DREAMS_2025` 用 central planner 调度结构生成、DFT convergence testing、HPC scheduling 和 error handling；`El_Agente_Q_2025` 面向 quantum chemistry workflows，结合 hierarchical memory、工具选择和 in situ debugging；`PANGAEA_GPT_2026` 通过 Supervisor-Worker topology 支撑地球科学数据发现；`LeanMarathon_2026` 通过 two-stage orchestrator 沿 proof DAG 推进形式化证明。

层级式系统的优势是可扩展和可治理，但风险也更集中。如果上层 planner 错误分解任务，下游 agents 会高效执行错误目标；如果 supervisor 缺乏独立验证，它可能把局部成功误判为科学发现。因此，层级式多智能体必须与执行反馈、验证门槛、日志和人工检查点结合。

### 4.6 开放能力网络：从固定团队到科学能力生态

开放能力网络将多智能体从封闭团队扩展为可注册、可发现、可评价、可复用的科学能力生态。在这里，agent 不一定只是 LLM role，也可以是工具、模型、数据库、仿真集群、物理仪器、证明器、技能包、报告服务器或人类专家。系统关注的是科学能力如何进入网络、如何承接任务、如何交换产物、如何获得信任。

`Science_Earth_2026` 是这一方向的代表。其 EACN 提出 domain-directed discovery、competitive bidding、task ownership negotiation、cross-regime adjudication 和 reputation-weighted trust，使科学任务能够在异质能力节点之间流动。`ScienceClaw_Infinite_2026` 通过 skill registry、artifact DAG、global index 和 persistent memory 组织 distributed discovery。`SCP_2025` 将 tools、models、datasets、physical instruments 和 agents 连接到 Science Context Protocol 中，并强调 provenance 与 reproducibility。`AgentRxiv_2025` 通过 shared preprint server 让多个 agent laboratories 上传、检索和吸收彼此研究。`MACC_2026` 和 `OmniScientist_2025` 则从 shared workspace、collaborative competition、ScienceArena 和 human-AI scientist ecosystem 角度讨论开放科学协作。

开放能力网络的重要性在于，它把 ASD 的组织原则从“一个团队如何完成一个任务”扩展为“科学能力如何组成长期生态”。这对于跨学科、长周期、多证据标准的发现尤其重要。但开放性也带来治理挑战：能力认证、错误声誉更新、恶意节点、产物污染和跨机构责任归属，都将成为未来系统设计的核心问题。

### 4.7 小结：多智能体组织模式的比较

第 4 章的核心结论是，多智能体 ASD 的“多”并不只有一种含义。`X2` 通过角色分工组织科学劳动，`X3` 通过并行实例扩大搜索和验证宽度，`X4` 通过层级调度治理复杂任务，`X5` 通过开放网络连接异质科学能力。一个成熟的 ASD 系统往往会混合多种模式：例如层级系统中包含固定角色，固定角色系统中包含 reviewer/verifier，多实例证明系统中也需要 manager 和 cache。因而，后续讨论反馈、搜索和演化机制时，必须始终回到这些组织形态：不同的组织形态决定了反馈从哪里来，搜索如何展开，演化对象是什么，以及验证边界在哪里。

## 5. 多智能体工作流中的反馈、搜索与演化机制

第 5 章讨论多智能体工作流如何改进自身输出。这里的“演化”不是泛指 agent 自我进化，也不是将所有迭代都称为 evolution。根据 `Y` 轴，当前文献可以分为五类机制：反思/自我修正 `Y1`、候选生成与筛选 `Y2`、树搜索/轨迹搜索 `Y3`、演化式优化 `Y4`，以及 harness/capability evolution `Y5`。其中 `Y1-Y4` 主要改进科学研究产物，`Y5` 则改进产生、执行和验证这些产物的系统脚手架。

| 机制类型 | 主要对象 | 典型信号 | 代表系统 |
|---|---|---|---|
| 反思/自我修正 `Y1` | 单个或少量产物 | critique, debug, revise, verifier feedback | Agent Laboratory, MAESTRO, MA-LoT, IMPROVE |
| 候选生成与筛选 `Y2` | 候选假设、材料、分子、方案 | ranking, scoring, comparison, review | MOFGen, MOOSE-Chem, MAGenIdeas, MADD |
| 树/轨迹搜索 `Y3` | 多步路径、证明树、代码/实验轨迹 | MCTS, proof DAG, trajectory search | PriM, DrugMCTS, BFS-Prover-V2, LeanMarathon |
| 演化式优化 `Y4` | artifact population | mutation, tournament, Elo, archive, population | CoScientist, SciDER, EvoSci, AlphaProof Nexus |
| harness/capability evolution `Y5` | 工作流、记忆、技能、能力网络 | world model, skill graph, task bidding, reputation | Kosmos, EvoScientist, TopoMAS, Science Earth |

### 5.1 反馈与自我修正：从答案到可修订产物

`Y1` 系统将生成结果置于反馈循环中。反馈可以来自语言 critique，也可以来自编译器、形式验证器、实验约束、工具执行结果、训练指标、专家评价或人类检查点。它们的共同目标是把一次性输出转化为可修订的科学产物。

在固定角色系统中，`Agent_Laboratory_2024`、`MAESTRO_2026`、`SparksMatter_2025`、`MLR_Copilot_2024`、`Curie_2025`、`GenoMAS_2025` 和 `TAIS_2024` 都体现了 generator、executor、analyst 与 reviewer/critic 之间的反馈。`MAESTRO_2026` 通过 autonomous design loop 和 design history 改进催化剂候选；`MLR_Copilot_2024` 将 IdeaAgent 与 ExperimentAgent 连接为 idea-to-execution loop；`GenoMAS_2025` 通过 typed message-passing 和 shared canvas 支持 advance、revise、bypass 或 backtrack。

在执行环境中，反馈更具约束力。`IMPROVE_2025` 使用 real training feedback 对 ML pipeline 逐组件 refinement；`MA_LoT_2025` 使用 Lean4 verifier 反馈修正 proof draft；`CRISPR_GPT_2026` 将 planner、executor、tool provider 与 user proxy 连接到实验设计、guide RNA design、data analysis 和 troubleshooting。由此，`Y1` 的科学价值不在于“模型自我反思”，而在于将外部检查信号引入 agent workflow。

### 5.2 候选生成与筛选：将假设生成转化为选择问题

`Y2` 将科学发现组织为候选集合上的选择问题。系统先生成多个 hypotheses、ideas、molecules、materials、plans 或 reviews，再通过 ranking、scoring、review、comparison 或 selection 选择较优候选。这类机制在文献驱动假设生成、材料发现、蛋白质设计和药物发现中尤为常见。

在知识和假设层面，`MOOSE_Chem_2024` 将 background、inspirations 和 hypothesis 组织为化学假设发现流程，并使用 ranking 评估候选；`MAGenIdeas_2026` 将 research idea generation 组织为 generate、evaluate 和 refine；`AI_Researcher_HKU_2025` 使用 divergent-convergent discovery，从多个研究方向中筛选 idea；`ResearchAgent_2025` 通过 ReviewingAgents 对 problem、method 和 experiment design 提供反馈。

在材料与药物执行载体中，候选筛选更接近科学实验前的决策门槛。`MOFGen_2025` 组合 LLM、diffusion model、quantum mechanical agents 和 synthetic-feasibility agents 生成并过滤 MOF 候选。`AtomAgents_2025` 结合 knowledge retrieval、multi-modal data integration 和 physics-based simulations 支撑 alloy design。`Materealize_2026` 使用 multi-agent debate、structure generation、property prediction、synthesizability prediction 和 synthesis planning 支撑无机材料候选设计。`MADD_2025` 将 drug discovery query 拆成 de novo generation、screening、prediction 和 docking evaluation 等子任务。

因此，`Y2` 的关键不是“多生成”，而是“可选择”。候选必须能被评价、比较和进入下一步执行。评价信号可以来自 agent review、物理仿真、docking score、synthetic feasibility、实验数据比较、novelty/plausibility 评分或专家判断。候选生成与筛选是连接问题形成和执行验证的中间层。

### 5.3 树搜索与轨迹搜索：保留探索过程本身

`Y3` 机制比候选筛选更强调过程结构。系统不只是生成候选列表，而是显式维护搜索树、证明 DAG、代码轨迹、实验路径或 reasoning trajectory。这样，失败节点、局部成功、分支选择和回溯过程都可以成为后续搜索的资源。

`PriM_2025` 将 principle-inspired material discovery 与 MCTS/structured search 结合，用科学原则约束材料假设和实验验证。`DrugMCTS_2025` 将 RAG、多 agent 协作和 Monte Carlo Tree Search 用于 drug repurposing。`PiFlow_2025` 将自动发现理解为 structured uncertainty reduction。`KompeteAI_2025` 在 AutoML pipeline 生成中结合 dynamic solution space exploration、MCTS、candidate merging 和 accelerated debugging。

形式证明提供了更硬的搜索边界。`BFS_Prover_V2_2025` 将 theorem/subgoal 分解后交给 parallel prover agents，并通过 shared proof cache 进行 multi-agent tree search。`LeanMarathon_2026` 沿 proof DAG 组织 Blueprinter、Target-Reviewer、Worker 和 Refiner，所有提交经 CI verifier 检查。`MOOSE_Chem2_2025` 将细粒度化学假设发现形式化为 hypothesis space 上的 hierarchical search。

树搜索与轨迹搜索的价值在于，它使探索过程可回溯。科学发现中的失败分支、局部证明、被淘汰候选和中间实验结果都可能包含知识。多智能体系统通过 planner、generator、executor、critic、verifier 和 manager 的分工，将这些路径转化为可管理的搜索结构。

### 5.4 演化式优化：从候选列表到产物种群

`Y4` 系统显式使用 mutation、recombination、population、Elo、tournament、archive、elite selection 或 parallel exploration traces。其核心对象是 scientific research artifacts 的种群，而不是单个候选。

`CoScientist_2026` 通过 generate、debate、rank 和 evolve approach 组织 biomedical hypothesis tournament。`SciDER_2026` 使用 four specialized sub-agents 和 Evolutionary Idea Search，将 ideation、data analysis、experimentation 与 critic 连接为 data-centric discovery workflow。`EvoSci_2026` 将 seed ideas、evolutionary iterations、reviewer/meta-reviewer 和 tournament ranking 结合，推动 scientific idea evolution。`RD_Agent_2025` 通过 Researcher/Developer 双 agent、多条 parallel exploration traces、runnable solution 和 performance feedback 推进数据科学研发。

形式化与数学任务中，`AlphaProof_Nexus_2026` 使用 multiple provers、rating agents、population database 和 Lean-based verification；`Code2Math_2026` 将已有数学问题演化为更复杂且可验证的变体。材料、生物和算法发现中，`Virtual_Lab_2025` 通过 mutation、weighted score 和 top-candidate selection 优化 nanobody candidates；`GeoEvolve_2025` 通过 outer agentic controller 与 inner code evolver 形成地理空间算法发现的层级演化搜索；`OR_Agent_2026` 使用 structured tree-based workflow 和 Idea/Code/Experiment agents 进行算法发现。

演化式优化相对于 `Y2` 的不同在于，候选不会在一次排序后退出系统，而是进入 archive、population database 或 exploration trace，被变异、重组、评分、淘汰或复用。它适合开放搜索空间和长期探索，但也要求执行反馈和验证门槛足够严格，否则演化机制可能只是将错误候选更高效地扩散。

### 5.5 Harness 与能力演化：当工作流本身成为对象

`Y5` 是本文第二主线的关键。它关注的不是单个 hypothesis、code、proof 或 experiment plan 的改进，而是 agentic harness 的更新：角色分配、工作流拓扑、工具链、记忆结构、skill graph、scoring functions、verifier、promotion gates、capability registry 和 trust/reputation。

固定角色系统中的 harness evolution 常表现为 memory、world state 和 research strategy 的更新。`EvoScientist_2026` 通过 persistent memory and self-evolution 改进 idea generation 和 experimental execution。`Kosmos_2025` 通过 structured world model 在 literature search、hypothesis generation 和 data analysis 之间维护长期状态。`SciAgents_2024` 通过 in-situ learning、知识图谱和 critique 改进材料科学假设。`Instrument_Agents_2026` 将 on-the-job learning 引入真实科学仪器操作，使 interaction memory 成为后续实验任务的能力来源。

层级系统中的 harness evolution 更强调 workflow、skill graph 和 objective function。`TopoMAS_2025` 通过 self-evolving knowledge graph 将材料检索、理论推理、结构生成和 first-principles validation 的结果写回知识系统。`Mimosa_2026` 自动合成 task-specific multi-agent workflows，并通过工具发现、meta-orchestrator、LLM judge、执行日志和归档 workflow 支撑可审计演化。`Mozi_2026` 使用 Supervisor-Worker Hierarchical Agent System 和 Composable Stateful Skill Graphs 治理药物发现长流程。`SAGA_2025` 的 outer loop of LLM agents 更新目标和 computable scoring functions，说明目标函数本身也可以成为演化对象。

开放能力网络将 harness evolution 扩展到生态层。`Science_Earth_2026` 中，EACN 通过 capability discovery、competitive bidding、cross-regime adjudication 和 reputation-weighted trust 调整能力网络。`ScienceClaw_Infinite_2026` 通过 scientific skills、artifact DAG 和 global index 组织 distributed discovery。`SCP_2025` 将 tools、models、datasets、physical instruments 和 agents 连接成 global web of autonomous scientific agents。`AgentRxiv_2025` 让多个 agent laboratories 通过 shared preprint server 上传、检索并基于彼此报告迭代。此时，演化对象已经从单个科学产物转向能力网络本身。

### 5.6 小结：组织形态与演化机制的耦合

第 4 章和第 5 章应被共同阅读。多智能体组织决定反馈和搜索如何发生，反馈和搜索又反过来要求更清晰的角色、交接、验证和记忆结构。`X2` 适合稳定科研流程中的角色分工，`X3` 适合并行证明、验证和候选评审，`X4` 适合复杂任务调度，`X5` 适合开放能力组合和长期协作。相应地，`Y1-Y4` 主要改进科学研究产物，`Y5` 则改进产生这些产物的 harness。

由此可以形成本文的中心判断：自主科学发现不是一个孤立 AI scientist 的能力展示，而是多智能体组织、反馈/搜索/演化机制和验证边界共同构成的工作流系统。只有当科学产物可交接、搜索路径可追踪、演化对象可验证、harness 更新可审计时，多智能体输出才可能从 agent response 转化为可信的 scientific discovery artifact。

