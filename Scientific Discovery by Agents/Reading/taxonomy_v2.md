# Taxonomy v2: Skill-Driven Agentic Scientific Discovery

> 目的：固定第二轮文献地图的分类标准。  
> 本文件不改变 `Notes/` 的文件夹结构；它定义的是综述论证用的分析标签。

## 0. 分类层级关系

| 分类 | 回答的问题 | 用途 | 位置 |
|---|---|---|---|
| Notes 文件夹分类 | 这篇论文本身属于什么文献类型？ | 管理单篇笔记 | `Notes/systems`, `Notes/benchmarks`, `Notes/memory` 等 |
| Scientific Workflow | 这篇论文覆盖科学发现流程中的哪一步？ | 构建横轴 | evidence matrix / taxonomy |
| Skill Lifecycle | 这篇论文对应 skill 能力生命周期中的哪一环？ | 构建纵轴 | evidence matrix / taxonomy |
| Evidence Role | 这篇论文在我们的论证中扮演什么角色？ | 判断它如何支持、限制或修正中心框架 | evidence matrix / expanded paper pool |
| Cross-cutting Constraints | 这篇论文是否涉及真实世界落地、人工监督或可审计性？ | 作为横贯约束，防止把能力论证写成无条件自动化 | evidence matrix / stress test |

这五套标签可以同时存在。例如 MIRIX：

| 维度 | 标签 |
|---|---|
| Notes 文件夹 | `memory` |
| Scientific Workflow | `Evolution / memory update` |
| Skill Lifecycle | `Representation / memory skill`, `Retrieval / resource-aware` |
| Evidence Role | `Indirect`, `Infrastructure` |
| Cross-cutting Constraints | `Auditability` |

再例如 RoboChem-Flex：

| 维度 | 标签 |
|---|---|
| Notes 文件夹 | `systems` |
| Scientific Workflow | `Experiment Design`, `Execution`, `Result Analysis`, `Evolution` |
| Skill Lifecycle | `Execution / lab action`, `Evolution / long-horizon learning`, `Verification / real-world validation` |
| Evidence Role | `Infrastructure`, `Direct` |
| Cross-cutting Constraints | `Physical Grounding`, `Human Oversight` |

## 1. Notes 文件夹分类

这是文献管理分类，不作为正文结构。

| 文件夹 | 含义 | 典型论文 |
|---|---|---|
| `systems` | 自动科研系统、Agent 框架、科研 artifact 系统 | AI Scientist, Agent Laboratory, ARA, SkillOS, SSL |
| `benchmarks` | 基准、评测、数据集、能力边界 | PaperBench, ScienceAgentBench, MLE-Bench, BrowseComp |
| `memory` | Agent 记忆、长期状态、协作记忆、记忆协议 | MemGPT, A-MEM, MIRIX, Memory Warning |
| `skills-ecosystem` | skill 生成、存储、检索、复用、评测 | Voyager, AWM, ExpeL, SkillsBench |
| `verification` | 引用验证、审稿、人类研究、轨迹验证 | OpenScholar, LLM Verifier, Stanford Human Study |
| `surveys` | 相关综述和实践性总结 | CUHK Agent Skills Survey, Memory surveys, Osmani |
| `infrastructure` | 工程指南、协议、工具栈、实践框架 | Perplexity Skills Guide, GStack |

## 2. Scientific Workflow 分类

Scientific Workflow 是本综述的横轴，表示论文覆盖科学发现的哪个阶段。

| 一级阶段 | 二级能力 | 判断标准 | 典型证据 |
|---|---|---|---|
| Knowledge Grounding | literature search | 是否检索、筛选、组织文献 | AutoSurvey, GPT Researcher |
| Knowledge Grounding | citation verification | 是否检查引用存在性、相关性、claim 支撑 | OpenScholar |
| Knowledge Grounding | knowledge graph | 是否构建领域知识图谱或图记忆 | Graph Agent Memory, A-MEM |
| Knowledge Grounding | factuality | 是否评估事实准确性、自知之明、检索事实能力 | SimpleQA, HLE, BrowseComp |
| Hypothesis Generation | novelty | 是否生成/评估新颖研究想法 | IdeaBench, Stanford Human Study |
| Hypothesis Generation | feasibility | 是否评估创意可行性、实现风险 | Stanford Human Study |
| Hypothesis Generation | diversity | 是否衡量创意多样性或避免模式坍缩 | Stanford Human Study |
| Hypothesis Generation | analogy | 是否用跨领域类比或概念迁移生成假设 | 候选论文待补 |
| Hypothesis Generation | causal reasoning | 是否构造因果假设或干预机制 | 候选论文待补 |
| Experiment Design | protocol design | 是否生成实验协议或研究计划 | Agent Laboratory, AI Scientist |
| Experiment Design | variable control | 是否显式控制变量、实验条件、消融 | AI Scientist Nature, PaperBench |
| Experiment Design | resource planning | 是否考虑算力、成本、数据、实验材料约束 | Agent Laboratory, ScienceAgentBench |
| Experiment Design | safety constraints | 是否处理实验安全、伦理约束、危险操作 | 候选论文待补 |
| Execution | code execution | 是否执行科研代码、训练、调试、复现 | CORE-Bench, SUPER, MLE-Bench |
| Execution | simulation | 是否运行仿真、模型、科学模拟 | MLE-Bench, AgenticSciML 候选 |
| Execution | lab automation | 是否控制实验室设备或自动实验平台 | 候选论文待补 |
| Execution | robotic experimentation | 是否包含机器人实验、self-driving lab | 候选论文待补 |
| Result Analysis | statistics | 是否做统计分析、显著性、误差估计 | PaperBench, ScienceAgentBench |
| Result Analysis | visualization | 是否生成/解释图表 | AI Scientist, PaperBench |
| Result Analysis | error analysis | 是否分析失败模式、调试结果 | RE-Bench, Memory Warning |
| Result Analysis | multimodal interpretation | 是否处理图像、谱图、截图、实验图表 | MIRIX, ScienceAgentBench |
| Synthesis | paper writing | 是否生成论文、报告、综述 | AI Scientist, GPT Researcher, AutoSurvey |
| Synthesis | artifact construction | 是否构建结构化研究 artifact | ARA, Paper2Code |
| Synthesis | review response | 是否生成 rebuttal 或审稿回应 | Reviewer2, Osmani/GStack 候选 |
| Verification | reproduction | 是否复现论文/代码/结果 | PaperBench, CORE-Bench |
| Verification | peer review | 是否生成或模拟同行评审 | ReviewerGPT, Reviewer2, AgentReview |
| Verification | citation checking | 是否验证引用与 claim | OpenScholar |
| Verification | benchmark grading | 是否提供任务评分、rubric、自动评测 | PaperBench, SkillsBench |
| Evolution | memory update | 是否更新长期记忆或经验库 | A-MEM, MIRIX, MemGPT |
| Evolution | skill update | 是否修改、增加、删除 skill | SkillOS |
| Evolution | failed-branch reuse | 是否保留并复用失败路径 | ARA, Memory Warning |
| Evolution | long-horizon learning | 是否跨长时间任务持续改进 | RE-Bench, long-horizon 候选 |

## 3. Skill Lifecycle 分类

Skill Lifecycle 是本综述的纵轴，表示 procedural knowledge 如何成为可维护能力。

| 一级阶段 | 二级机制 | 判断标准 | 典型证据 |
|---|---|---|---|
| Representation | prompt skill | skill 主要是自然语言指令、prompt、checklist | Anthropic Skills, Agent Skills Spec |
| Representation | code skill | skill 以可执行代码、函数、脚本存在 | Voyager, Paper2Code |
| Representation | workflow skill | skill 是多步程序、任务流程或 SOP | AWM, GStack, Agent Laboratory |
| Representation | artifact skill | skill/研究成果被结构化为机器可消费 artifact | ARA |
| Representation | memory skill | skill 以内化记忆、经验、procedure memory 存在 | MIRIX, A-MEM |
| Representation | protocol skill | skill 以协议、schema、跨 agent 规范存在 | MMP, Agent Skills Spec |
| Acquisition | human-written | skill 由人类专家手写 | Anthropic Skills, Agent Skills Spec |
| Acquisition | trajectory-derived | 从成功/失败轨迹提取 skill | Voyager, AWM, ExpeL |
| Acquisition | literature-derived | 从论文、文档、语料中抽取 workflow | AutoSurvey, Paper2Code 候选 |
| Acquisition | failure-derived | 从失败、审稿意见、debug trace 中提取经验 | Reflexion, Memory Warning |
| Acquisition | benchmark-derived | 从 benchmark/rubric/task 中形成可复用 procedure | SkillsBench, PaperBench |
| Retrieval | keyword | BM25、关键词、metadata 匹配 | SkillOS |
| Retrieval | embedding | 向量相似度检索 | Voyager, AWM |
| Retrieval | structure-aware | 利用结构化字段、图、schema 检索 | SSL, Graph Agent Memory |
| Retrieval | stage-aware | 根据科研阶段选择 skill | taxonomy 目标；候选待补 |
| Retrieval | resource-aware | 根据工具、数据、成本、安全约束选择 | Perplexity Skills Guide, ScienceAgentBench |
| Composition | sequential | 多个 skill 顺序串联 | Agent Laboratory, GStack |
| Composition | hierarchical | 高层 plan 调用低层 skill | AI Scientist, Agent Skills Spec |
| Composition | multi-agent | 不同 Agent 分工调用/维护 skill | Agent Laboratory, Intrinsic Memory Agents |
| Composition | tool-chain | skill 组织一组工具/API/脚本 | GPT Researcher, OpenScholar |
| Composition | protocol-mediated | 通过协议/artifact 跨 agent 组合 | ARA, MMP |
| Execution | tool use | 使用浏览器、搜索、数据库、MCP、API | GPT Researcher, BrowseComp |
| Execution | code run | 运行代码、测试、调试、训练 | CORE-Bench, MLE-Bench |
| Execution | web search | query / fetch / synthesize | BrowseComp, OpenScholar |
| Execution | lab action | 控制实验设备或湿实验操作 | 候选待补 |
| Execution | simulation | 科学仿真、模型实验、虚拟实验 | AgenticSciML 候选 |
| Evolution | reflection | 自然语言反思更新策略 | Reflexion, ExpeL |
| Evolution | RL curator | 强化学习管理 skill 增改删 | SkillOS |
| Evolution | memory consolidation | 记忆整合与抽象更新 | A-MEM, Generative Agents |
| Evolution | versioning | 版本、 lineage、变更记录 | ARA, Agent Skills Spec 候选 |
| Evolution | deletion | 删除、淘汰、降权过时 skill | SkillOS |
| Verification | unit test | 代码级或任务级测试 | Voyager, Paper2Code |
| Verification | benchmark | 基准评分、rubric、pass rate | SkillsBench, PaperBench |
| Verification | citation check | 文献存在性与 claim 支撑 | OpenScholar |
| Verification | human review | 人类评审、专家标注、作者反馈 | Stanford Human Study, Paper2Code |
| Verification | replication | 复现实验和结果匹配 | PaperBench, CORE-Bench |
| Verification | real-world validation | 真实科学发现、湿实验、真实同行评审 | AI Scientist Nature；更多候选待补 |

## 4. Cross-cutting Constraints 横贯约束

Cross-cutting Constraints 不是第三条轴，也不替代 Workflow / Lifecycle。它用于标记一篇论文是否触及真实世界科学部署中的关键约束：物理落地、人工监督和可审计性。

| Constraint | 含义 | 判断标准 | 典型证据 |
|---|---|---|---|
| Physical Grounding | 是否连接真实世界物理对象、仪器、机器人、样品、实验室或在线表征 | 如果系统不只是文本/代码，而是能影响或读取真实实验过程，就标记此项 | A-Lab, Coscientist, RoboChem-Flex, Rainbow, AFION, CRISPR-GPT |
| Human Oversight | 是否明确人类在目标设定、实验选择、安全审查、结果解释、同行评审或责任承担中的角色 | 如果系统依赖 scientist-in-the-loop、human-in-the-loop、专家评价或出版责任，就标记此项 | Co-Scientist, Robin, Adaptive AI Decision Interface, Stanford Human Study, AI Responsible Publishing |
| Auditability | 是否提供证据链、日志、引用、版本、错误检测、可回滚记录或可追溯 artifact | 如果系统输出可被检查、复现、追踪、纠错或归责，就标记此项 | ARA, OpenScholar, Kosmos, SPOT-a, GeneAgent, SciVer, PaperBench |

### 4.1 Physical Grounding

Physical Grounding 用来约束“agent 能输出实验建议”与“agent 能参与真实科学发现”之间的距离。

典型问题：

- 是否控制真实实验设备？
- 是否处理真实样品、试剂、细胞、材料或传感器数据？
- 是否包含在线表征、机器人执行、自动采样或实验安全约束？
- 是否有真实实验结果反馈到下一轮决策？

这个标签对 self-driving lab 和 wet-lab agent 尤其重要。RoboChem-Flex、Rainbow、AFION、A-Lab 说明，真实科学 skill 需要硬件、传感、分析设备、实验成本和安全流程支撑。

### 4.2 Human Oversight

Human Oversight 用来避免把 human-in-the-loop 系统误写成 fully autonomous discovery。

典型问题：

- 人类是否定义了目标、搜索空间或 precursor library？
- 人类是否选择最终候选、批准实验或解释结果？
- 人类专家是否参与评价、审稿、署名、披露或安全审查？
- 系统是否显式保留 scientist-in-the-loop 或 human-in-the-loop？

这个标签不表示系统“不够自动化”，而是说明人类监督本身是可信 scientific workflow 的组成部分。

### 4.3 Auditability

Auditability 用来标记 scientific agent 的输出是否可检查、可追踪、可复现和可问责。

典型问题：

- 输出是否绑定 citation、database evidence、代码、实验日志或 primary literature？
- 是否保留版本、lineage、失败路径或回滚机制？
- 是否能检测错误、隐藏 prompt、数据泄漏或 hallucination？
- 是否支持人类或外部系统复核？

Auditability 是把 agent output 从“看起来合理”变成“可进入科学记录”的关键约束。

## 5. Evidence Role 分类

Evidence Role 标记论文在我们论证中的角色。每篇论文至少有一个主角色，可以有一个副角色。

| Role | 含义 | 适用标准 | 例子 |
|---|---|---|---|
| Direct | 直接研究 skill / skill lifecycle / skill evaluation | 论文明确使用 skill、skill library、skill representation、skill acquisition、skill retrieval、skill evolution 或 skill benchmark | SkillOS, SSL, SkillsBench, Voyager, Agent Skills Spec |
| Indirect | 不使用 skill 术语，但包含可复用 procedure / workflow / artifact / routine | 可被映射为 procedural unit，但不是显式 skill 系统 | AI Scientist, Agent Laboratory, OpenScholar, MIRIX |
| Boundary | 给框架设边界，说明能力不足或评估约束 | 主要贡献是 benchmark、失败模式、human baseline、可靠性约束 | PaperBench, RE-Bench, ScienceAgentBench, HLE |
| Counterexample | 反例或削弱某个乐观假设 | 显示 skill 自动生成/记忆整合/自动审稿等机制可能无效或有害 | SkillsBench self-generated skills, Memory Warning, AgentReview |
| Infrastructure | 提供实现 skill-driven discovery 所需底座 | 协议、artifact、memory store、retrieval stack、citation database、工程指南、实验平台 | ARA, MMP, OpenScholar, Perplexity Skills Guide, RoboChem-Flex, ChemRev SDL |

## 6. 标签使用规则

1. **不要用 Notes 文件夹分类替代 Workflow / Lifecycle 标签。**  
   `memory/MIRIX` 仍然放在 memory 文件夹，但在证据矩阵中可标为 `Evolution / memory update` 与 `Representation / memory skill`。

2. **Direct 不等于重要，Boundary 也不等于次要。**  
   PaperBench 是 Boundary，但对综述很关键，因为它约束“自动科研”的可信度。

3. **Indirect 论文不能被过度改写成 skill-driven。**  
   AI Scientist 可以说是 pipeline-driven，不能说已经完整实现 skill lifecycle。

4. **Counterexample 要保留。**  
   反例是综述可信度的重要来源，例如自生成 skill 低收益、记忆整合退化、LLM reviewer 偏见。

5. **新增论文必须填三类标签。**  
   以后扩展论文池时，每篇至少填写：
   - Scientific Workflow stage
   - Skill Lifecycle stage
   - Evidence Role

6. **第三轮以后，新增论文建议额外填写 Cross-cutting Constraints。**  
   不要求每篇都必须有横贯标签，但如果论文涉及真实实验、人工监督或可审计证据，应明确标记：
   - Physical Grounding
   - Human Oversight
   - Auditability

7. **Physical Grounding 不能被 tool-use 替代。**  
   SciToolAgent 这样的工具链论文可以是 `Execution / tool use`，但只有连接真实仪器、实验样品、机器人或在线表征时，才标记 `Physical Grounding`。

8. **Human Oversight 不是缺点标签。**  
   Co-Scientist、Robin、Adaptive AI Decision Interface 等系统中的人类参与，是可信科研流程的一部分，应作为约束和设计特征记录。

9. **Auditability 是进入科学记录的门槛。**  
   没有引用、代码、日志、实验记录、版本或错误检测的 agent 输出，只能作为候选想法，不能作为 scientific closure。

## 7. 候选论文初筛标准

新增论文进入 `expanded_paper_pool.md` 前，至少满足以下一项：

1. 补足当前 53 篇的明显缺口，例如 wet-lab、robotic lab、chemistry、biology、materials、real-world discovery。
2. 对 skill lifecycle 某一环有更细机制，例如 skill composition、skill transfer、skill evolution、skill verification。
3. 提供强边界条件，例如失败模式、benchmark、人类研究、治理政策。
4. 提供基础设施，例如 lab automation platform、scientific data connector、citation/reproduction framework。

不优先纳入：

- 只有泛泛 LLM 应用，没有 agentic workflow 的论文；
- 只有普通工具调用，没有可复用 procedure 或科学发现关联的论文；
- 只有新闻/博客且无可核验技术细节的材料；
- 与 scientific discovery 或 agent skill 两边都关系弱的论文。
