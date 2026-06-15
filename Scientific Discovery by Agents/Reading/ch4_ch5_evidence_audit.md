# 第 4、5 章证据审计：多智能体工作流模式与演化/搜索机制

> 目的：遍历现有 Notes 论文笔记，判断哪些论文支撑第 4 章和第 5 章，并反思这两个章节的分类方式是否合理。  
> 口径：统计对象为 `Notes/` 下 103 篇单篇论文笔记，不包括 `README.md` 和 `matrix_*.md`。  
> 结论：第 4、5 章均有充分文献支撑，但二者不是互斥分类。第 4 章应理解为 **组织层**，第 5 章应理解为 **优化层**。

## 总体判断

现有论文池支持保留第 4 章和第 5 章，但建议调整表述：

- 第 4 章不是“所有多智能体论文的分类箱”，而是回答：**多智能体如何组织科学劳动？**
- 第 5 章不是另一个平行领域，而是回答：**组织起来的多智能体工作流如何通过搜索、反馈和演化改进科学研究产物及其 agentic harness？**

因此，更准确的关系是：

| 章节 | 层次 | 关注点 |
|---|---|---|
| 第 4 章 | 组织层 coordination architecture | 角色如何分工，如何交接，如何批评，如何引入人类/实验室，如何共享记忆与 provenance |
| 第 5 章 | 优化层 search/evolution mechanism | 假设、代码、notebook、证明、实验方案、失败分支和 harness 如何跨迭代改进 |

## 第 4 章证据：科学发现中的多智能体工作流模式

### 数量判断

严格口径下，能直接支撑第 4 章正文主干的论文约 **22 篇**。

如果把 self-driving labs、技能生态、通用 agent memory、治理材料等背景也算入，可扩展到约 **35 篇**，但这些不建议全部进入正文主线。

### 支撑角度一：角色分解与专家分工

这一类论文支撑“科学发现天然需要多角色协作”。

| 论文 | 支撑角度 |
|---|---|
| `Agent_Laboratory_2024` | PhD、Postdoc、ML Engineer、Professor 等角色化科研团队 |
| `Virtual_Lab_2025` | PI、Scientific Critic、领域 scientist agents 的会议式协作 |
| `CoScientist_2026` | Generation、Reflection、Ranking、Evolution、Meta-review 等专门 agent |
| `Robin_2026` | Crow、Falcon、Finch 分别负责文献、评估、数据分析 |
| `AI_Researcher_HKU_2025` | research agent 与 paper agent 的双智能体结构 |
| `AI_Scientist_2024` / `AI_Scientist_Nature_2026` | idea、experiment、write-up、automated review 的阶段化模块 |
| `CRISPR_GPT_2026` | Planner、Executor、Tool provider、User proxy 的 protocol workflow 分工 |
| `Intrinsic_Memory_Agents_2025` | 角色异质记忆，支撑不同角色保持不同专业视角 |

核心锚点：`Virtual_Lab_2025`、`Agent_Laboratory_2024`、`CoScientist_2026`。

### 支撑角度二：协调、通信与交接

这一类论文支撑“多智能体系统的关键不是 agent 数量，而是协调协议和可交接产物”。

| 论文 | 支撑角度 |
|---|---|
| `Agent_Laboratory_2024` | 阶段间交接，实验失败可回溯到早期任务 |
| `CoScientist_2026` | Supervisor 管理任务队列，Elo tournament 驱动假设流转 |
| `Robin_2026` | 文献生成候选、实验执行、数据分析、下一轮候选形成 lab-in-the-loop |
| `Science_Earth_2026` | open task posting、competitive bidding、task ownership negotiation |
| `SciToolAgent_2025` | Planner、tool chain、Summarizer 与失败后重规划 |
| `ARA_2026` | 研究过程结构化为 logic/src/trace/evidence，支持 agent-native 交接 |
| `Mesh_Memory_Protocol_2025` | 跨会话、跨 agent 的语义交换协议 |

核心锚点：`Science_Earth_2026`、`Robin_2026`、`ARA_2026`。

### 支撑角度三：批评、辩论、锦标赛与审稿

这一类论文支撑“多智能体的价值来自独立批评、排序、评审和冲突暴露，而不是多个 agent 重复同一判断”。

| 论文 | 支撑角度 |
|---|---|
| `CoScientist_2026` | Reflection、Ranking、Meta-review 形成 generate-critique-rank-evolve |
| `AI_Scientist_2024` / `AI_Scientist_Nature_2026` | automated reviewer 进入端到端科研闭环 |
| `Agent_Laboratory_2024` | 3-reviewer NeurIPS-style evaluation，同时暴露自动评审高估问题 |
| `Virtual_Lab_2025` | Scientific Critic 参与 team / individual meeting |
| `ResearchAgent_2025` | ReviewingAgents 对 problem、method、experiment design 迭代精炼 |
| `AgentReview_2024` | 将同行评审建模为多智能体社会过程 |
| `ReviewerGPT_2023` / `Reviewer2_2024` | 支撑审稿任务可被拆解为错误识别、方面提示、具体意见生成 |
| `LLM_Verifier_2025` | 多轮验证、轨迹奖励和 verifier 机制 |
| `OpenScholar_2025` | 文献与引用支持的验证 |
| `Stanford_Human_Study_2024` | AI 自评不可靠，需要人类专家校准 |

核心锚点：`CoScientist_2026`、`AgentReview_2024`、`AI_Scientist_Nature_2026`。

### 支撑角度四：Human-in-the-loop 与 Lab-in-the-loop

这一类论文支撑“人类介入不是自主性的失败，而是科学可信度和合法性的组成部分”。

| 论文 | 支撑角度 |
|---|---|
| `Robin_2026` | 人类实验室执行实验，agent 分析数据并推动下一轮 |
| `CoScientist_2026` | scientist-in-the-loop hypothesis validation |
| `Virtual_Lab_2025` | 人类给目标、agenda、审阅和调试，实验验证由人类实验室完成 |
| `CRISPR_GPT_2026` | co-pilot 模式，真实实验由人类执行 |
| `Coscientist_2023` | LLM planner 连接实验自动化接口，部分物理动作仍需人类 |
| `Adaptive_AI_Decision_Interface_2025` | 人类-AI 材料发现界面 |
| `OpenAI_Unit_Distance_2026` | AI 生成数学输出由人类数学家和外部专家验证 |

核心锚点：`Robin_2026`、`CoScientist_2026`、`Virtual_Lab_2025`。

### 支撑角度五：共享记忆、Provenance 与产物管理

这一类论文支撑“多智能体科研系统需要共享状态、证据链和可审计交接，而不是无差别共享聊天记录”。

| 论文 | 支撑角度 |
|---|---|
| `Collaborative_Memory_2025` | 多用户多 agent 共享记忆、动态访问控制和不可变溯源 |
| `Mesh_Memory_Protocol_2025` | CAT7、SVAF、lineage、remix，支撑跨 agent 语义记忆交换 |
| `ARA_2026` | claims、code、trace、evidence 跨层绑定，保留失败轨迹 |
| `MIRIX_2025` | 多类型记忆和 Meta Memory Manager |
| `Intrinsic_Memory_Agents_2025` | 角色私有记忆，避免专业视角被同质化 |
| `Memory_Sandbox_2023` | 记忆透明化和人类可干预 |

核心锚点：`Collaborative_Memory_2025`、`Mesh_Memory_Protocol_2025`、`ARA_2026`。

### 支撑角度六：开放能力网络与生态化协作

这一类论文支撑“multi-agent 不只是固定团队，也可以是开放 scientific capability network”。

| 论文 | 支撑角度 |
|---|---|
| `Science_Earth_2026` | 从 fixed-role team 推进到 open capability network；能力发现、任务竞标、跨证据裁决、声誉信任 |
| `Agent_Skills_Spec_2026` | 技能可包装、可发现、可跨平台复用 |
| `Anthropic_Skills_Spec_2025` | SKILL.md 和渐进式披露支撑能力封装 |
| `Gemini_for_Science_2026` | 平台化趋势，将多种科研 agentic 能力放入工作台入口 |

核心锚点：`Science_Earth_2026`。

### 第 4 章最强核心锚点

建议正文围绕以下 8 篇反复展开：

1. `Science_Earth_2026`
2. `CoScientist_2026`
3. `Virtual_Lab_2025`
4. `Robin_2026`
5. `Agent_Laboratory_2024`
6. `ARA_2026`
7. `Collaborative_Memory_2025`
8. `AgentReview_2024`

### 第 4 章弱支撑或不宜正文展开的材料

- 单点能力基准：`GAIA_2023`、`HLE_2025`、`SimpleQA_2024`、`BrowseComp_2025`、`MLE_Bench_2024`、`ScienceAgentBench_2025`、`PaperBench_2025` 等。它们更适合评估章节。
- 通用记忆但非多主体协作核心：`MemGPT_2023`、`A_MEM_2025`、`Graph_Agent_Memory_2025`、`Memory_Warning_2026`。可作背景或边界。
- 技能生态材料：`Toolformer_2023`、`ToolLLM_2024`、`Voyager_2023`、`AWM_2024`、`ExpeL_2024`、`Buffer_of_Thoughts_2024`、`SkillsBench_2025`。更适合第 5 章或基础设施章节。
- Self-driving lab 系统：`AFION_Plasmonic_SDL_2025`、`ALab_2023`、`Rainbow_Perovskite_2025`、`RoboChem_Flex_2026`、`Robot_Scientist_2004`。它们支撑物理闭环，但不是第 4 章多智能体组织主线。
- 治理风险材料：`AI_Responsible_Publishing_2026`、`Hidden_Prompts_Peer_Review_2025`、`Risks_AI_Scientists_2025`、`SafeScientist_2025`。更适合治理或开放问题。

## 第 5 章证据：多智能体工作流中的演化/搜索机制

### 数量判断

严格口径下，能支撑第 5 章正文的论文约 **35 篇**。

如果把基准、综述、平台入口、纯基础设施和边界材料也纳入，可扩展到约 **55 篇**，但很多只适合作脚注、边界或评估支撑。

### 支撑角度一：假设 / Idea 演化

| 论文 | 支撑角度 |
|---|---|
| `CoScientist_2026` | generate、reflect、rank、Elo tournament、Evolution agent、Meta-review |
| `MC_NEST_2025` | 假设生成即 tree search / self-refining trees |
| `ResearchAgent_2025` | 文献驱动 idea generation，经 ReviewingAgents 反复反馈和改写 |
| `Robin_2026` | 实验结果反馈到下一轮候选生成 |
| `AI_Scientist_2024` | idea、实验、论文草稿进入 archive-based open-ended iteration |
| `AI_Scientist_Nature_2026` | agentic tree search 和 workshop review 支撑论文级产物改进 |
| `AI_Researcher_HKU_2025` | 从参考文献或研究思路到算法设计和论文生成 |
| `Robot_Scientist_2004` | 假设、实验、知识库更新的历史基线 |

核心锚点：`CoScientist_2026`、`MC_NEST_2025`、`ResearchAgent_2025`、`Robin_2026`。

### 支撑角度二：代码 / Notebook / 软件产物演化

| 论文 | 支撑角度 |
|---|---|
| `ERA_2026` | empirical scientific software 的 tree search、sandbox scoring、idea recombination |
| `AlphaEvolve_2025` | 代码 artifact 的 generate-test-refine / evolutionary search |
| `Jupiter_Notebook_Agent_2025` | notebook 轨迹的 value-guided search |
| `SciNav_2026` | scientific coding solution 的 top-K search 和执行反馈 |
| `DatawiseAgent_2025` | notebook cells 和分析轨迹逐步生成、执行、修正 |
| `CellVoyager_2026` | notebook/data-analysis agent 作为可执行科学分析轨迹 |
| `SPARK_Cancer_Pathology_2026` | biological concept / parameter 从生成、编码到验证 |
| `AI_Scientist_Nature_2026` | 实验节点和论文产物随推理计算提升 |

核心锚点：`ERA_2026`、`AlphaEvolve_2025`、`Jupiter_Notebook_Agent_2025`、`SciNav_2026`。

### 支撑角度三：形式化证明搜索

| 论文 | 支撑角度 |
|---|---|
| `AlphaProof_Nexus_2026` | prover subagents、rating agents、population database、Lean compiler 验证 |
| `OpenAI_Unit_Distance_2026` | AI-generated mathematical discovery，但系统细节较少公开，人类专家验证为主 |

核心锚点：`AlphaProof_Nexus_2026`。

边界案例：`OpenAI_Unit_Distance_2026`。

### 支撑角度四：实验 / 仿真搜索

| 论文 | 支撑角度 |
|---|---|
| `Robot_Scientist_2004` | hypothesis -> experiment -> knowledge update 闭环 |
| `ALab_2023` | 真实材料实验闭环，实验结果更新后续路线 |
| `AFION_Plasmonic_SDL_2025` | 在线表征和多目标优化 |
| `Rainbow_Perovskite_2025` | 多机器人、多目标 Bayesian optimization |
| `RoboChem_Flex_2026` | 模块化 SDL 中的 Bayesian optimization 闭环 |
| `Coscientist_2023` | LLM planner 连接化学实验自动化接口 |
| `TianJi_2026` | 文献、假设、数值实验、物理解释组成仿真发现流程 |
| `Climate_Self_Evolving_Agent_2025` | 气候科学 agent 通过失败和反馈更新分析策略 |
| `Virtual_Lab_2025` | 多轮 mutation-selection pipeline |
| `Robin_2026` | lab-in-the-loop 候选、实验、分析、下一轮候选 |

核心锚点：`ALab_2023`、`RoboChem_Flex_2026`、`TianJi_2026`、`Robin_2026`。

### 支撑角度五：失败分支与记忆复用

| 论文 | 支撑角度 |
|---|---|
| `ARA_2026` | dead ends、exploration graph、trace 和 evidence 作为一等研究产物 |
| `Reflexion_2023` | 失败轨迹转化为自然语言反思，指导后续重试 |
| `ExpeL_2024` | 成功/失败轨迹归纳为可迁移 insight |
| `Voyager_2023` | executable skill library 随任务反馈积累 |
| `A_MEM_2025` | 新记忆触发旧记忆上下文和标签更新 |
| `Memory_Warning_2026` | 持续整合记忆可能退化，强调原始轨迹和门控 |
| `SkillOS_2026` | SkillRepo 的 insert/update/delete 和长期技能管理 |
| `SciToolAgent_2025` | 工具链失败后重新规划 |

核心锚点：`ARA_2026`、`Reflexion_2023`、`ExpeL_2024`。

边界锚点：`Memory_Warning_2026`。

### 支撑角度六：Harness / Capability / Network 演化

| 论文 | 支撑角度 |
|---|---|
| `Science_Earth_2026` | open capability network、capability discovery、task bidding、reputation-weighted trust |
| `SkillOS_2026` | SkillRepo 的长期 RL 管理，技能插入、更新、删除 |
| `STELLA_2025` | Dynamic Tool Ocean、Tool Creation Agent、template library |
| `SciToolAgent_2025` | 科学工具图谱、chain-of-tools planning、失败后重规划 |
| `Voyager_2023` | 任务反馈驱动的 executable skill library |
| `AWM_2024` | 成功轨迹归纳为 workflow memory |
| `A_MEM_2025` | 记忆网络持续组织和更新 |
| `Intrinsic_Memory_Agents_2025` | role-private memory 随任务内在更新 |
| `MIRIX_2025` | 多类型记忆和 Meta Memory Manager |
| `Mesh_Memory_Protocol_2025` | 跨 agent 认知状态交换、lineage 和 remix |
| `Collaborative_Memory_2025` | 用户-agent-resource 动态访问图 |
| `MOSAIC_Chemical_Synthesis_2026` | 能力/专家分区、检索与组合，作为 collective intelligence 支撑 |

核心锚点：`Science_Earth_2026`、`SkillOS_2026`、`STELLA_2025`、`Mesh_Memory_Protocol_2025`。

### 第 5 章弱支撑或边界材料

- Idea 评估基准：`IdeaBench_2024`、`AI_Idea_Bench_2025`、`LiveIdeaBench_2026`、`RINoBench_2026`。它们评估 idea generation，但不是演化工作流本身。
- 代码/复现评估基准：`ScienceAgentBench_2025`、`MLAgentBench_2024`、`MLE_Bench_2024`、`RE_Bench_2024`、`PaperBench_2025`、`Paper2Code_2025`、`CORE_Bench_2024`、`SUPER_2024`。它们可支撑为什么需要可执行搜索，但不是机制主锚点。
- 信息检索基准：`BrowseComp_2025`。支撑 persistent search，但偏信息检索。
- 方法或背景：`Causal_Hypothesis_LLM_2025` 支撑因果假设生成，但缺少完整 agentic search 系统。
- 技能规范与工程材料：`SSL_2026`、`Anthropic_Skills_Spec_2025`、`Agent_Skills_Spec_2026`、`SkillsBench_2025`、`Perplexity_Skills_Guide_2026`。可作 skill 表示、评估和工程规范，弱于 `SkillOS_2026` / `STELLA_2025`。
- 平台材料：`Gemini_for_Science_2026`、`GStack_2025`。适合说明生态趋势，不宜作为论文级机制证据。

## 对第 4、5 章分类方式的反思

### 现有分类的优点

现有第 4、5 章切法基本合理，因为论文池确实呈现两条强信号：

1. 大量系统将科学发现组织为多角色、多协议、多证据边界的协作流程。
2. 大量系统将科学发现建模为对假设、代码、notebook、证明、实验方案、失败分支和 harness 的搜索与改进。

这说明第 4 章和第 5 章都不是空设章节。

### 主要风险

第 4、5 章不是互斥分类，而是交叉维度。同一篇论文经常同时支撑两章：

| 论文 | 第 4 章支撑 | 第 5 章支撑 |
|---|---|---|
| `CoScientist_2026` | 多 agent 批评、排序、meta-review | 假设 evolution、Elo tournament、candidate refinement |
| `Robin_2026` | lab-in-the-loop 工作流 | 实验反馈进入下一轮候选 |
| `Science_Earth_2026` | open capability network | harness / network evolution |
| `ARA_2026` | provenance、artifact handoff | dead ends、exploration graph、失败分支复用 |
| `SkillOS_2026` | 多 agent 技能管理基础设施 | SkillRepo evolution |
| `MIRIX_2025` | 多类型记忆支持协作 | memory / harness evolution |

因此，如果第 4 章写成“多智能体论文分类”，第 5 章写成“演化论文分类”，会产生重复和割裂。

### 推荐理解

更稳妥的理解是：

> 第 4 章写多智能体科研系统的 **coordination architecture**，第 5 章写这些系统内部的 **search/evolution mechanism**。

也就是：

- 第 4 章：谁和谁协作，如何协作。
- 第 5 章：协作系统如何通过反馈改进产物和 harness。

### 建议标题与小节调整

建议将第 4 章标题调整为：

**多智能体科研工作流的组织架构：从固定团队到开放能力网络**

建议小节：

1. 固定角色团队：PI、specialist、critic、generator、reviewer。
2. 协调协议与产物交接：pipeline、handoff、artifact store、ARA。
3. 批评、辩论、锦标赛与审稿：critic、judge、reviewer 的独立性。
4. Human-in-the-loop 与 Lab-in-the-loop。
5. 共享记忆、provenance、权限与责任归因。
6. 从 fixed-role team 到 open capability network：Science Earth / EACN。

建议将第 5 章标题调整为：

**搜索与演化机制：科学产物演化与 Harness 演化**

建议小节：

1. Search、Iteration 与 Evolution 的边界。
2. 假设与研究想法搜索。
3. 代码、Notebook 与软件产物演化。
4. 形式证明与可机器验证产物。
5. 实验方案、失败分支与探索图。
6. Harness evolution：roles、tools、skills、memory、reputation、verification gates。
7. 风险与边界：虚假优化、错误抽象、缺少 rollback。

## 最终建议

保留第 4、5 章，但在写作中明确二者关系：

> 第 4 章是组织层，解释多智能体如何把科学劳动拆成角色、协议、交接、批评、记忆和人类检查点；第 5 章是优化层，解释这些工作流如何通过搜索、反馈、验证和记忆改进科学研究产物及其 agentic harness。

这样既能保留当前 outline 的结构优势，又能避免把两章写成重复的论文清单。
