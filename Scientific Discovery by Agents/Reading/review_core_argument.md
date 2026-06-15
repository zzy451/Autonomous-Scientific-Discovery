# Review Core Argument v1

> 目的：在正式写正文前，把这篇综述的中心论点、边界和贡献压缩清楚。  
> 状态：结构草案，不是论文正文。

## 1. 综述题目候选

当前最稳的题目方向：

> Skill-Driven Agentic Autonomous Scientific Discovery: Workflows, Research Skills, and Verification Boundaries

更短的题目：

> Skill-Driven Agentic Scientific Discovery

更强调边界的题目：

> From Scientific Workflows to Research Skills: A Survey of Agentic Scientific Discovery

## 2. 中心问题

这篇综述要回答的核心问题不是：

> LLM 是否已经能完全自主做科学发现？

而是：

> 现代 scientific agents 正在把科学发现流程拆解成哪些可复用、可执行、可组合、可验证、可演化的 research skills？这些 skills 在真实科学发现、self-driving lab、工具链、假设生成和治理中分别成立到什么程度？

这个问题的优势是：

1. 避免过度声称“全自动科学家已经实现”。
2. 能同时覆盖 LLM agents、self-driving labs、scientific tool-use、hypothesis generation、verification 和 governance。
3. 能把已有 98 篇材料组织成一个可证实框架，而不是按论文类型堆列表。

## 3. 核心论点

本综述的核心论点可以写成：

> Agentic scientific discovery is shifting from fixed end-to-end pipelines toward reusable research skills embedded in scientific workflows. These skills include literature grounding, hypothesis generation, experiment design, tool-chain execution, lab automation, result analysis, synthesis, verification, and long-horizon evolution. However, such skills become scientifically meaningful only when grounded in physical infrastructure, human oversight, auditable evidence, and governance constraints.

中文版本：

> Agentic scientific discovery 正在从固定端到端 pipeline 转向由可复用 research skills 组织起来的科学 workflow。这些 skills 包括文献 grounding、假设生成、实验设计、工具链执行、实验自动化、结果分析、综合写作、验证和长期演化。但只有当这些 skills 嵌入物理实验基础设施、人工监督、可审计证据和治理边界时，它们才真正具有科学意义。

## 4. 我们与已有综述的区别

| 已有综述常见主线 | 本综述的不同点 |
|---|---|
| AI for Science 按领域分类：biology、chemistry、materials、climate | 我们按 scientific workflow 和 skill lifecycle 分类，领域只是证据来源 |
| Autonomous scientific discovery 按系统能力分类：idea、experiment、paper | 我们追问每个能力是否能成为可复用、可验证、可演化的 research skill |
| Agent skill 综述按通用 agent 技能生命周期分类 | 我们把 skill lifecycle 映射到科学发现，并加入 physical grounding、human oversight、auditability |
| Self-driving lab 综述按硬件/实验平台分类 | 我们把 SDL 看作 physical grounding，是 research skills 进入真实世界的基础设施 |
| Scientific benchmark 综述按任务和分数分类 | 我们把 benchmark 和 verification 作为 scientific closure 的约束层 |

因此，本综述的新意不是“又收集一批 AI scientist 论文”，而是：

> 用 research skill 的生命周期视角，解释 agentic scientific discovery 为什么需要 workflow decomposition、tool/lab infrastructure、verification closure 和 governance constraints。

## 5. 总框架

本综述使用四层框架：

1. **Scientific Workflow**  
   科学发现流程的横轴：Knowledge Grounding、Hypothesis Generation、Experiment Design、Execution、Result Analysis、Synthesis、Verification、Evolution。

2. **Skill Lifecycle**  
   能力形成和维护的纵轴：Representation、Acquisition、Retrieval、Composition、Execution、Evolution、Verification。

3. **Evidence Role**  
   文献在论证中的角色：Direct、Indirect、Boundary、Counterexample、Infrastructure。

4. **Cross-cutting Constraints**  
   横贯约束：Physical Grounding、Human Oversight、Auditability。

这个框架的关键点是：

> Workflow 告诉我们科学发现要做什么；Skill Lifecycle 告诉我们这些能力如何被表示、获取、检索、组合、执行、演化和验证；Evidence Role 告诉我们论文在论证中是支持、约束还是反驳；Cross-cutting Constraints 告诉我们这些能力是否能进入真实科学实践。

## 6. 可以稳妥声称的结论

### 6.1 Scientific agents 正在形成 research skills

可以声称：

- CellVoyager、DatawiseAgent、Jupiter 表明 notebook-based data analysis 可以成为 research skill。
- SPARK 表明 pathology concepts 可以被转成可执行参数并在队列中验证。
- MOSAIC、CRISPR-GPT 表明 chemical / biological protocols 可以被组织为可执行 procedure。
- SciToolAgent、SciAgentGym、BioMedAgent 表明 scientific tool-chain execution 可以被表示、组合和评测。
- MC-NEST、ResearchAgent、Causal Hypothesis 表明 hypothesis generation 正在从 prompt generation 转向 search / refinement / verification。

不能声称：

- 所有这些系统都显式使用 skill library。
- 它们已经实现跨领域通用科研技能。
- 它们能替代科学家完成完整发现闭环。

### 6.2 Self-driving lab 是 skill-driven science 的硬基础设施

可以声称：

- A-Lab、RoboChem-Flex、Rainbow、AFION、Coscientist、CRISPR-GPT 显示 scientific skills 需要实验设备、机器人、在线表征和实验反馈。
- ChemRev SDL 和 Benchmarking SDL 说明 SDL 已经形成独立技术谱系和评价需求。
- Robot Scientist 说明自动假设生成与实验闭环早于 LLM，LLM agent 应放入更长历史中理解。

不能声称：

- LLM agents 单独构成 self-driving lab。
- 实验执行可以被 prompt 或 tool-call 完全替代。
- 所有 SDL 都具有开放式发现能力。

### 6.3 Verification and governance 是科学闭环，不是附录

可以声称：

- OpenScholar、GeneAgent、SciVer、SPOT-a、PaperBench 显示 scientific outputs 需要 citation、claim、database、multimodal 和 replication-level verification。
- SafeScientist、Hidden Prompts、AI Responsible Publishing、Risks of AI Scientists 显示 scientific agents 需要安全、对抗鲁棒性、出版责任和审稿治理。

不能声称：

- 自动 verifier 可替代专家审查。
- LLM reviewer 已经足以承担同行评审。
- 只要有 benchmark，科学发现就可靠。

## 7. 不能写过头的地方

以下表述应避免：

1. “AI agents can autonomously conduct scientific discovery end-to-end.”
2. “Skill-driven agents have solved scientific research automation.”
3. “LLMs can generate reliable scientific hypotheses.”
4. “Self-driving labs are just tool-use extensions of LLM agents.”
5. “Automated peer review can replace human peer review.”
6. “More memory and more skills necessarily improve long-horizon discovery.”

更稳的替代表述：

1. “AI agents increasingly automate subskills within scientific workflows.”
2. “Research skills are emerging as reusable units of agentic scientific work.”
3. “Hypothesis generation requires novelty, feasibility, causal plausibility, and leakage-aware verification.”
4. “Physical grounding is required for claims about real-world discovery.”
5. “Verification and governance define the boundary of credible autonomy.”
6. “Skill evolution remains an open problem due to degradation, provenance, and validation challenges.”

## 8. 论文的预期贡献

这篇综述可以主张四个贡献：

1. **A workflow-skill taxonomy**  
   将 scientific workflow 与 skill lifecycle 结合，用于分析 agentic scientific discovery。

2. **A role-aware evidence map**  
   将 98 篇论文标注为 Direct、Indirect、Boundary、Counterexample、Infrastructure，避免只收集支持性证据。

3. **A physical and governance-aware framing**  
   将 Physical Grounding、Human Oversight、Auditability 作为横贯约束，连接 LLM agents、self-driving labs 和 scientific verification。

4. **A research agenda**  
   指出 future work 应集中在 skill evolution、failed-branch reuse、cross-domain transfer、real-world validation、audit logs 和 governance protocols。

## 9. Anchor papers：后续必须深挖的主证据

正文写作前，以下论文需要升级到“可写正文级”精读：

| 方向 | Anchor papers |
|---|---|
| End-to-end / co-scientist systems | AI Scientist Nature, Co-Scientist, Robin, Agent Laboratory, Kosmos |
| Biomedical / pathology discovery | CellVoyager, SPARK, Medea, GeneAgent, BioMedAgent |
| Chemical / biological protocol skill | MOSAIC, CRISPR-GPT, Coscientist |
| Self-driving labs | A-Lab, RoboChem-Flex, Rainbow, AFION, Robot Scientist |
| Scientific tool-use | SciToolAgent, SciAgentGym, ChemCost, ToolLLM |
| Hypothesis generation | ResearchAgent, LiveIdeaBench, RINoBench, MC-NEST, Causal Hypothesis |
| Verification / auditability | OpenScholar, SciVer, SPOT-a, PaperBench, ARA |
| Governance | SafeScientist, Risks of AI Scientists, Hidden Prompts, AI Responsible Publishing |

这些 anchor papers 应优先补：

- 方法流程细节；
- 关键数字；
- 消融实验；
- failure modes；
- 作者承认的局限；
- 我们能用它支撑的具体论点；
- 不能用它支撑的过度论点。

## 10. 下一步任务

1. 根据本文件写 `review_outline_v1.md`。
2. 按 outline 选出每章 anchor papers。
3. 回头升级 anchor notes，而不是继续无边界扩文献。
4. 再开始写引言和相关工作草稿。
