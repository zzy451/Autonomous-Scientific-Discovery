# 新增论文原文核对与分类复核

> 目的：对最近加入 XYZ 文献矩阵的论文进行原文摘要/论文主页层面的核对，补全本地论文笔记，并修正不准确的 XYZ 分类。

## 核对范围

本轮重点核对 35 篇最近加入的论文笔记：

- 严格 ASD 候选：SciAgents, SparksMatter, CodeScientist, CycleResearcher, ProtAgents, AutoDiscovery, LLM-SR, EvoSLD, SR-Scientist。
- ASD 相关系统候选：MOOSE-Chem, MOOSE-Chem2, HypER, Open-Domain Hypotheses, Curie, GenoMAS, TAIS, DrugAgent, MLZero, MLR-Copilot, AIDE, KompeteAI, IMPROVE, DS-Agent, DrSR, Nova, Scideator, Sparks of Science, CLAIMCHECK, Generative Adversarial Reviews, DeepReview, AstroAgents, VirSci, GraphEval, ToolUniverse, TxAgent。

所有 35 篇本地笔记已追加 `原文核对与分类复核` 段落。

## 分类修正

| 文献 | 原分类 | 修正后分类 | 原因 |
|---|---|---|---|
| MOOSE_Chem2_2025 | X0-Y2-Z1/Z2/Z3/Z7 | X3-Y3-Z1/Z2/Z3/Z7 | 原文明确是 fine-grained hypothesis discovery via hierarchical search，并讨论 LLM ensemble / repeated instances |
| KompeteAI_2025 | X2-Y2-Z3/Z4/Z5/Z7 | X2-Y3-Z3/Z4/Z5/Z7 | 原文包含 MCTS、dynamic solution-space exploration、candidate merging 和 accelerated debugging |
| DrugAgent_2024 | X2-Y2-Z1/Z3/Z4/Z5/Z7 | X2-Y0-Z1/Z3/Z4/Z5/Z7 | 原文有 Planner / Instructor 多智能体协作，但没有明确搜索、演化或候选筛选机制 |
| SR_Scientist_2026 | X0-Y3-Z3/Z4/Z5/Z7/Z8 | X0-Y1-Z3/Z4/Z5/Z7/Z8 | 更适合归为 agentic equation discovery 中的执行反馈和反思修正，而非明确 tree search |
| CLAIMCHECK_2025 | X0-Y1-Z7 | 移出 XYZ 主矩阵 | 原文是 claim-centric review / verification benchmark，不是 ASD 系统或 ASD 相关系统 |

修正后：

- 严格 ASD 系统：33 篇。
- ASD 相关系统：67 篇。
- XYZ 主矩阵合计：100 篇。

## 分类保持但需注意写作口径

| 文献 | 保持分类 | 写作注意 |
|---|---|---|
| SciAgents_2024 | X2-Y5-Z1/Z2/Z3/Z5/Z7/Z8 | 可作为 multi-agent + in-situ learning / capability evolution 代表，但真实实验闭环有限 |
| SparksMatter_2025 | X2-Y1-Z1/Z2/Z3/Z5/Z6/Z7/Z8 | 摘要声称 full inorganic materials discovery cycle；若正文确认执行实验 workflow，可考虑加入 Z4 |
| CodeScientist_2025 | X0-Y4-Z1-Z8 | 是 artifact-level evolution 的核心案例，尤其适合说明 code-based experimentation |
| CycleResearcher_2024 | X2-Y5-Z1/Z2/Z3/Z6/Z7/Z8 | 重点是 research-review cycle 和 preference-training harness，而非物理实验发现 |
| AutoDiscovery_2025 | X0-Y3-Z2/Z4/Z5/Z7/Z8 | 是 open-ended ASD 的强案例，强调系统自己决定探索哪些问题 |
| ToolUniverse_2025 | X0-Y5-Z1/Z3/Z4/Z5/Z7/Z8 | 不是发现闭环本身，而是 AI scientist 的工具和 capability infrastructure |
| TxAgent_2025 | X0-Y1-Z1/Z3/Z4/Z5/Z7 | 生物医学工具推理系统，适合作基础设施或领域支撑，不应作为多智能体主证据 |
| Sparks_of_Science_2025 | X0-Y2-Z1/Z2/Z7 | 更像 hypothesis generation 数据/训练资源，正文中应作为补充材料 |
| DeepReview_2025 | X0-Y1-Z7 | 是 review system，支撑 verification / review，不应写成发现系统 |
| GraphEval_Idea_2025 | X0-Y2-Z2/Z7 | 是 idea evaluation framework，支撑候选筛选 |

## 对综述结构的影响

1. 第 4 章“科学发现中的多智能体工作流模式”仍然成立，但应优先使用 X2-X5 的核心系统：CoScientist、Robin、Virtual Lab、Agent Laboratory、Science Earth、SciAgents、SparksMatter、AstroAgents、GenoMAS、Curie。
2. 第 5 章“演化/搜索机制”应分得更清楚：
   - artifact-level evolution：CodeScientist、AlphaEvolve、LLM-SR、EvoSLD、AI Scientist。
   - tree / trajectory search：ERA、AutoDiscovery、AIDE、KompeteAI、MOOSE-Chem2。
   - harness / capability evolution：Science Earth、Kosmos、CycleResearcher、ToolUniverse、SciAgents。
3. Verification / review 文献中应区分“系统”和“benchmark”。DeepReview、AgentReview、Generative Adversarial Reviews 可以作为 review systems；CLAIMCHECK 更适合作为 benchmark / diagnostic resource。

## 后续阅读优先级

建议下一轮深读优先处理：

1. CodeScientist：决定 artifact evolution 小节的写法。
2. AutoDiscovery：决定 open-ended ASD 和问题形成的写法。
3. SciAgents 与 SparksMatter：决定 materials multi-agent discovery 的写法。
4. MOOSE-Chem / MOOSE-Chem2：决定 hypothesis search 小节的写法。
5. ToolUniverse 与 Science Earth：决定 capability / harness evolution 的写法。

## 第二批近期工作复核

本轮继续核对 19 篇此前已加入矩阵、但尚未写入原文复核段落的近期工作：

- 严格 ASD 候选：EvoScientist, MARS Materials, MOFGen, MASTER, PriM, MAESTRO。
- ASD 相关系统候选：EvoSci, FlowPIE, MAGenIdeas, MatSciAgent, Instrument Agents, BioAgents, Graph2Idea, EvoGens, Deep Research, MACC, CASCADE, Autonomous Materials Computation, PiFlow。

所有 19 篇本地笔记已追加 `原文核对与分类复核` 段落。

### 第二批分类修正

| 文献 | 原分类 | 修正后分类 | 原因 |
|---|---|---|---|
| MatSciAgent_2026 | X4-Y2-Z1/Z3/Z4/Z5/Z7 | X4-Y0-Z1/Z3/Z4/Z5/Z7 | 原文重点是 master agent 调度 task-specific agents 完成多任务材料计算；没有明确候选搜索、筛选或演化机制 |

修正后主矩阵仍为 100 篇：

- 严格 ASD 系统：33 篇。
- ASD 相关系统：67 篇。
- Y0 从 2 篇变为 3 篇，Y2 从 22 篇变为 21 篇。

### 第二批分类保持但需注意写作口径

| 文献 | 保持分类 | 写作注意 |
|---|---|---|
| EvoScientist_2026 | X2-Y5-Z1/Z2/Z3/Z4/Z5/Z7/Z8 | 直接支撑 harness evolution；重点是 persistent memory 与 self-evolution |
| EvoSci_2026 | X2-Y4-Z1/Z2/Z7/Z8 | 支撑 multi-agent idea evolution；不宜写成完整实验闭环 |
| FlowPIE_2026 | X0-Y4-Z1/Z2/Z7/Z8 | 同时有 flow-guided MCTS 和 test-time idea evolution，正文可放在 idea artifact evolution |
| MAGenIdeas_2026 | X2-Y2-Z1/Z2/Z7/Z8 | 支撑 multi-agent research idea generation, evaluation, and refinement；当前证据不足以严格归入 tree / trajectory search |
| Instrument_Agents_2026 | X2-Y5-Z1/Z3/Z4/Z5/Z7/Z8 | 支撑仪器操作中的 on-the-job learning 和 capability evolution |
| BioAgents_2025 | X2-Y1-Z1/Z5/Z7 | 支撑生物信息分析与结果验证，不是完整 ASD 系统 |
| Graph2Idea_2026 | X0-Y2-Z1/Z2/Z7 | 支撑 graph-structured literature contexts for idea generation |
| EvoGens_2026 | X0-Y4-Z1/Z2/Z7/Z8 | 典型 population-based idea evolution |
| MARS_Materials_2026 | X4-Y2-Z1/Z2/Z3/Z4/Z5/Z7/Z8 | 多智能体 + 机器人材料实验闭环，是严格 ASD 的核心材料案例 |
| MOFGen_2025 | X2-Y2-Z2/Z3/Z4/Z5/Z7/Z8 | 支撑多能力 agent 组合生成、优化、过滤和验证 MOF |
| MASTER_2025 | X4-Y2-Z2/Z3/Z4/Z5/Z7/Z8 | 支撑 hierarchical multi-agent reasoning + atomistic simulation |
| PriM_2025 | X2-Y2-Z2/Z3/Z5/Z7/Z8 | 支撑 principle-guided multi-agent material discovery |
| MAESTRO_2026 | X2-Y1-Z2/Z3/Z4/Z5/Z7/Z8 | 支撑 multi-agent reflection 和 design history in catalyst discovery |
| Deep_Research_2026 | X2-Y5-Z1/Z2/Z3/Z4/Z5/Z7/Z8 | 支撑 interactive multi-agent workflow 与 persistent world state |
| MACC_2026 | X5-Y5-Z2/Z3/Z6/Z7/Z8 | 可与 Science Earth 一起支撑开放协作/竞争架构 |
| CASCADE_2025 | X0-Y5-Z1/Z3/Z4/Z5/Z7/Z8 | 支撑 skill / harness evolution，不是多智能体主案例 |
| Autonomous_Materials_Computation_2025 | X0-Y1-Z1/Z3/Z4/Z5/Z7 | 支撑可靠材料计算执行，不是完整发现闭环 |
| PiFlow_2025 | X2-Y3-Z1/Z2/Z3/Z5/Z7/Z8 | 支撑 principle-aware multi-agent structured uncertainty reduction |

### 对章节写作的新增启发

1. **材料发现是当前严格 ASD 文献最密集的证据区**：MARS、MOFGen、MASTER、PriM、MAESTRO、SparksMatter、SciAgents 可以组成一个强小节。
2. **演化对象需要继续区分 artifact 与 harness**：FlowPIE、EvoGens 偏 scientific idea artifacts；EvoScientist、CASCADE、Instrument Agents、Deep Research 偏 harness/capability evolution。
3. **多智能体不必总是搜索机制**：MatSciAgent 说明有些强多智能体系统主要贡献是任务分解、工具调用和仿真执行，而不是搜索/演化。

## 深读笔记升级记录

为便于后续正文写作，已将近期新增的 54 篇系统笔记升级到接近 `MARS_Materials_2026.md` 的深读标准。

### 升级范围

- 第一批 35 篇：SciAgents, MOOSE-Chem, MOOSE-Chem2, HypER, Open-Domain Hypotheses, ProtAgents, SparksMatter, Curie, CodeScientist, CycleResearcher, GenoMAS, TAIS, DrugAgent, MLZero, MLR-Copilot, AIDE, KompeteAI, IMPROVE, DS-Agent, LLM-SR, DrSR, EvoSLD, SR-Scientist, AutoDiscovery, Nova, Scideator, Sparks of Science, CLAIMCHECK, Generative Adversarial Reviews, DeepReview, AstroAgents, VirSci, GraphEval, ToolUniverse, TxAgent。
- 第二批 19 篇：EvoScientist, EvoSci, FlowPIE, MAGenIdeas, MatSciAgent, Instrument Agents, BioAgents, Graph2Idea, EvoGens, MARS Materials, MOFGen, MASTER, PriM, MAESTRO, Deep Research, MACC, CASCADE, Autonomous Materials Computation, PiFlow。

### 统一补充内容

每篇笔记已补充或保留以下内容：

- 研究问题。
- 系统架构 / 工作流。
- 关键机制。
- 实验验证与证据。
- 局限性补充。
- XYZ 分类逐项解释。
- 综述写作用法。
- 原文核对与分类复核。

### 当前状态

- 54/54 篇近期新增笔记已包含 `深读补充（按 MARS 标准）` 或等价的完整深读结构。
- XYZ 主矩阵保持 100 篇口径。
- `CLAIMCHECK_2025` 不进入 XYZ 主矩阵，但保留为 verification / benchmark 补充材料。
