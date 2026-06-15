# 演化定义支撑矩阵

> 目的：整理现有论文笔记中可支撑“演化”定义的工作，供综述第 5 章和引言逻辑使用。这里的“演化”范围收束为两类对象：一类是 **scientific research artifacts**，即科学研究产物；另一类是 **agentic harness**，即生成、执行、路由、记忆、验证、交接和治理这些产物的系统脚手架。原先的 agent/capability 演化与 workflow/network 演化统一归入 harness 演化。

## 两类定义

| 演化层次 | 核心含义 | 综述中的作用 |
|---|---|---|
| 科学研究产物演化 scientific research artifact evolution | 假设、代码、notebook、证明、实验方案、报告、失败分支等科学研究产物被生成、执行、评分、选择、改写、归档和复用 | 解释“科学发现为什么不是一次性生成，而是围绕候选产物的搜索与筛选” |
| Harness 演化 agentic harness evolution | agent roles、工具链、技能库、记忆、能力节点、任务拓扑、verifier、promotion gates、human checkpoints、reputation/trust 等系统脚手架根据任务表现、反馈、证据冲突或治理约束被更新 | 解释“系统如何改变产生和验证科学产物的方式，而不只是改变最终输出” |

## 一、科学研究产物演化

这一层证据最强，已有笔记中可以支撑的论文很多。写作时建议把它作为 evolutionary/search-based workflow 的基础层。

| 强度 | 工作 | 演化对象 | 可支撑的论点 | 适合放置位置 |
|---|---|---|---|---|
| 强 | `AlphaEvolve_2025` | 算法代码、可执行程序 | 当候选可以被 evaluator 自动评分时，发现可被建模为 generate-test-refine 的程序演化 | 代码/算法产物演化 |
| 强 | `ERA_2026` | empirical scientific software | 科研软件可以通过 LLM rewriting、sandbox scoring、tree search 和 idea recombination 持续改进 | 代码/软件产物演化 |
| 强 | `AlphaProof_Nexus_2026` | Lean proof sketches、formal proof artifacts | 形式化数学发现可由 prover subagents、rating agents、population database 和 Lean verifier 组成演化搜索闭环 | 证明产物演化；multi-agent 与 evolution 的桥梁 |
| 强 | `CoScientist_2026` | 科学假设、research proposals | 假设可通过 generation、reflection、ranking、Elo tournament、Evolution、Meta-review 迭代改写和排序 | 假设产物演化；multi-agent hypothesis workflow |
| 强 | `MC_NEST_2025` | 科学假设树 | 科学假设生成不是单次 prompt，而是 tree search、自我精炼和多维评价下的搜索过程 | 假设搜索 |
| 强 | `Jupiter_Notebook_Agent_2025` | notebook analysis trajectories | 数据分析路径可在 inference time 被搜索、执行、估值和选择 | notebook 轨迹演化 |
| 强 | `SciNav_2026` | scientific coding solutions | 科学代码任务可被组织为 top-K search、执行反馈和 relative judgment | scientific coding search |
| 中强 | `DatawiseAgent_2025` | notebook cells、分析轨迹 | notebook 作为执行载体，使数据分析过程可逐步生成、执行、修正和保留 | notebook-centric workflow |
| 中强 | `ResearchAgent_2025` | problem、method、experiment design | 文献驱动 idea generation 可通过 ReviewingAgents 反复反馈和改写 | idea / experiment-design refinement |
| 中强 | `Virtual_Lab_2025` | tool scripts、scoring workflow、候选设计 | 多 agent 会议生成工具链和多轮 mutation-selection pipeline，说明实验/设计方案也可迭代筛选 | 多智能体科研团队中的产物演化 |
| 中强 | `Robin_2026` | assay proposal、candidate report、analysis notebook、下一轮候选 | 实验结果分析可反馈到下一轮候选生成，形成 lab-in-the-loop discovery loop | lab-in-the-loop 产物演化 |
| 中 | `AI_Scientist_2024` | idea、代码、实验、论文草稿 | archive-based open-ended iteration 支撑“研究产物进入档案并影响下一轮生成” | 端到端自动科研 baseline |
| 中 | `AI_Scientist_Nature_2026` | 实验节点、论文、review feedback | agentic tree search 和真实 workshop review 支撑研究流程中产物质量随推理计算提升 | 论文级产物演化 |
| 中 | `ARA_2026` | research artifact、exploration graph、dead ends | 失败轨迹和探索 DAG 可作为一等研究产物保存，支持后续 agent 复现和扩展 | 失败分支复用；产物基础设施 |
| 中 | `Robot_Scientist_2004` | 假设、实验选择、知识库 | 早期 robot scientist 已展示 hypothesis -> experiment -> knowledge update 的闭环 | 历史基线 |

可写成一句话：

> Artifact-level evolution is the most mature form of evolutionary scientific workflow: hypotheses, code, proof sketches, notebooks, experimental plans, and even failed branches can be treated as searchable scientific research artifacts when they are paired with execution, scoring, verification, or expert feedback.

## 二、Harness 演化：Agent / Capability 侧

这一部分说明 harness 的第一类变化：参与发现的角色、工具、技能、记忆和能力节点会根据反馈被选择、更新、降权、复用或删除。

| 强度 | 工作 | 演化对象 | 可支撑的论点 | 适合放置位置 |
|---|---|---|---|---|
| 强 | `Science_Earth_2026` | scientific capability nodes、任务承接权、reputation、trust | EACN 通过 capability discovery、competitive bidding、task ownership negotiation、cross-regime adjudication 和 reputation-weighted trust，使能力节点可被动态选择和更新 | open capability-network evolution |
| 强 | `SkillOS_2026` | SkillRepo、skill curator、insert/update/delete 操作 | agent 能通过长期任务反馈学习如何管理技能库，能力增长表现为技能插入、更新、删除和结构化管理 | skill/capability evolution |
| 强 | `STELLA_2025` | Dynamic Tool Ocean、Tool Creation Agent、template library | 科研 agent 能维护动态工具池，并从任务经验中沉淀可复用模板 | tool/capability evolution |
| 强 | `Voyager_2023` | executable skill library | 代码技能可由环境反馈、自我验证和任务课程持续积累，并在新任务中复用 | 技能库增长的原型证据 |
| 中强 | `AWM_2024` | workflow memory、抽象操作例程 | 成功轨迹可被归纳为可复用 workflow，并在流式任务中持续扩展 | workflow-as-skill evolution |
| 中强 | `ExpeL_2024` | natural-language insights、experience pool | agent 可从成功/失败经验中提取可迁移洞察，无需参数更新即可改善后续任务 | 经验到能力的转化 |
| 中强 | `Reflexion_2023` | verbal reflection memory | 失败轨迹可被转化为自然语言反思，作为后续策略改进的语义梯度 | failure-driven capability update |
| 中强 | `Buffer_of_Thoughts_2024` | thought templates、meta-buffer | 推理方法论可被蒸馏、检索、实例化和动态入库，支持认知技能演化 | reasoning capability evolution |
| 中强 | `A_MEM_2025` | linked memory network、memory attributes | 新记忆触发旧记忆上下文、关键词和标签更新，支持知识网络持续精炼 | memory-level capability evolution |
| 中强 | `Intrinsic_Memory_Agents_2025` | role-private memory | 每个 agent 的专属记忆从自身输出中内在更新，使角色能力随对话和任务持续变化 | role-specific capability evolution |
| 中 | `MIRIX_2025` | 多类型记忆管理能力 | Meta Memory Manager 和 6 类 Memory Managers 说明能力演化需要类型化记忆路由，而不是单一记忆池 | capability memory infrastructure |
| 中 | `Graph_Agent_Memory_2025` | graph memory lifecycle | Graph memory 综述将 Extraction -> Storage -> Retrieval -> Evolution 作为生命周期，提供记忆演化的通用分类 | 记忆演化综述支撑 |
| 边界 | `SkillsBench_2025` | 自生成技能、精选技能 | 自生成技能平均无收益甚至负收益，说明 capability evolution 必须经过验证和筛选，不能默认越自动越好 | 能力演化的反例/边界 |
| 边界 | `Memory_Warning_2026` | continuously consolidated memories | 持续整合记忆可能把有用经验变成错误抽象，说明能力演化需要原始轨迹、门控和回滚 | memory/capability evolution 的风险 |

可写成一句话：

> Harness evolution shifts the focus from improving candidate outputs to improving the scaffold that produces them: tools, skills, memories, templates, capability nodes, role assignments, and trust relations become objects of selection, update, deletion, or reuse.

## 三、Harness 演化：Workflow / Network 侧

这一部分说明 harness 的第二类变化：任务分解、角色组合、能力连接、协作拓扑、子任务和检查点会随冲突、失败、证据不一致或新目标动态变化。

| 强度 | 工作 | 演化对象 | 可支撑的论点 | 适合放置位置 |
|---|---|---|---|---|
| 强 | `Science_Earth_2026` | open scientific capability network、任务拓扑、子任务生成 | EACN 中问题分解不是预设 pipeline，而是在能力竞标、冲突、cross-regime adjudication 和失败中涌现 | workflow/network evolution 的核心锚点 |
| 强 | `Kosmos_2025` | structured world model、long-running discovery loop | structured world model 支持跨 agent、跨轮次保持状态，使文献搜索、数据分析、假设更新形成长周期 discovery loop | long-horizon workflow evolution |
| 强 | `ARA_2026` | exploration graph、dead ends、research artifact protocol | 研究过程可被表示为含 question、decision、experiment、dead_end、pivot 的探索 DAG，支持失败分支复用和后续扩展 | workflow artifact / failure branch reuse |
| 中强 | `Mesh_Memory_Protocol_2025` | agent-to-agent cognitive state network、lineage DAG | CAT7、SVAF、lineage 和 remix 让多 agent 之间的认知状态可选择性接受、追踪谱系和跨会话延续 | cross-agent memory/network evolution |
| 中强 | `Collaborative_Memory_2025` | 用户-agent-resource 动态二分图 | 访问图随时间授予或撤销边，说明多主体协作网络需要动态权限、provenance 和可审计共享 | collaboration network governance |
| 中强 | `Graph_Agent_Memory_2025` | graph memory topology | 图记忆把事件、概念、关系和时序结构组织为可演化拓扑，适合科学知识网络更新 | knowledge network evolution |
| 中强 | `Climate_Self_Evolving_Agent_2025` | climate analysis procedure、knowledge/tool/data libraries | 气候科学 agent 通过失败和反馈更新分析策略并复用 procedure，说明科学 workflow 可以跨任务演化 | domain workflow evolution |
| 中强 | `TianJi_2026` | atmospheric mechanism discovery workflow | meta-planner + worker agents 将文献、假设、数值实验和物理解释组织成可更新的机制发现流程 | simulation workflow evolution |
| 中 | `Agent_Laboratory_2024` | research stages、mle-solver program pool、paper-solver review loop | 多角色研究流程能在实验和写作阶段回溯、重做和稳定化，但整体更接近预设 pipeline | staged workflow evolution |
| 中 | `AI_Scientist_Nature_2026` | agentic tree search over experimental stages | 四阶段实验管理和 tree search 展示 workflow 可随推理计算扩展，但主要仍在 ML paper generation 场景 | end-to-end workflow baseline |
| 中 | `Virtual_Lab_2025` | team meetings、individual meetings、tool workflow | PI、specialists 和 critic 通过会议生成并修订 workflow，属于固定团队内的协作结构演化 | fixed-team workflow evolution |
| 中 | `Robin_2026` | literature -> assay -> experiment -> analysis -> next candidate loop | 真实实验数据反馈进入下一轮候选生成，是 lab-in-the-loop workflow 演化 | lab-in-the-loop workflow |
| 中 | `SciToolAgent_2025` | chain-of-tools planning | Planner-Executor-Summarizer 和失败后重新规划支持工具链 workflow 调整 | tool-chain workflow evolution |
| 中 | `RoboChem_Flex_2026` | closed-loop lab optimization workflow | BO agent、设备控制和分析反馈形成实验条件选择的闭环优化网络 | physical workflow evolution |
| 中 | `Rainbow_Perovskite_2025` | multi-robot DBTL loop | 多机器人 self-driving lab 中 surrogate model 和 classifier 每轮更新，支持合成-表征-优化 workflow | physical network/workflow evolution |
| 中 | `AFION_Plasmonic_SDL_2025` | closed-loop microfluidic synthesis workflow | 在线表征和多目标优化让下一轮实验条件随反馈变化 | self-driving lab workflow |

可写成一句话：

> Harness evolution treats the organization of discovery itself as adaptive: task decomposition, role assignment, memory sharing, access rights, tool chains, verifier gates, and capability links can change as evidence accumulates, conflicts arise, or failed branches reveal new subproblems.

## 推荐正文使用方式

### 第 5 章的组织建议

第 5 章可以不再只按“假设、代码、证明、长期系统”平铺，而是先提出三层演化对象，再分别用代表系统展开：

1. **科学研究产物演化**：Co-Scientist、MC-NEST、AlphaEvolve、ERA、Jupiter、SciNav、AlphaProof Nexus。
2. **Harness 演化**：Science Earth、SkillOS、STELLA、Voyager、AWM、A-MEM、Intrinsic Memory Agents、Kosmos、ARA、MMP、Collaborative Memory、Robin、TianJi、self-driving labs。

### 写作时的主次关系

| 层次 | 建议权重 | 写法 |
---|---:|---|
| 科学研究产物演化 | 高 | 最容易被读者理解，也是 AlphaEvolve / ERA / AlphaProof Nexus 等新工作的主线 |
| Harness 演化 | 高 | 这是本文区别于一般 evolutionary search 综述的关键，必须和 multi-agent 主线绑定；用 Science Earth 引出，再用 SkillOS / STELLA / Voyager / AWM / Kosmos / ARA / MMP 支撑 |

### 可放入引言的差异化句子

> Compared with prior Agentic Science surveys, this survey treats evolution not only as the optimization of scientific research artifacts, but also as the adaptation of the agentic harness that generates, routes, executes, verifies, and governs those artifacts.

中文可写为：

> 与既有 Agentic Science 综述相比，本文中的“演化”不只指科学研究产物被优化，还包括生成、路由、执行、验证和治理这些产物的 agentic harness 被持续调整。

## 边界提醒

- 不要把所有“迭代”都写成强演化。只有当系统有明确的选择、评分、反馈、记忆、更新、归档或拓扑重组机制时，才适合作为演化证据。
- 不要把 `evolutionary agents` 写成所有 agent 本体都在训练或遗传进化。更稳妥的表达是 `evolutionary/search-based workflow systems`。
- 对 `Science_Earth_2026` 应强调它是开放 capability network 的组织升级证据，但当前主要来自 live runs，不是大规模 benchmark sweep。
- 对 `SkillsBench_2025` 和 `Memory_Warning_2026` 应作为边界文献使用：能力演化需要验证、门控和原始轨迹，而不是无条件自动整合。
