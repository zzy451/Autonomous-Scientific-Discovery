# New Reference Works: 2026-06 Update

> 目的：针对学长提出的“5 月 Nature 新工作、药物发现、Erdos 数学题、Google/Meta 等”线索，整理一批需要新增或重点引用的工作。  
> 面向题目：A Survey of Multi- & Evolutionary-Agent Workflow & System on Autonomous Scientific Discovery  
> 日期：2026-06-01  
> 说明：生物医学相关工作仅用于系统架构、multi-agent workflow、human/lab-in-the-loop 和验证闭环叙事，不整理实验操作细节。

## 结论先行

这批资料应分成三类处理：

1. **已有笔记但需要在综述中升格为锚点**：Co-Scientist、Robin、AlphaEvolve、Kosmos。
2. **已完成第一版新增笔记的新工作**：ERA / Empirical Research Assistance、OpenAI unit-distance 数学发现、AlphaProof Nexus、Gemini for Science。
3. **只作引言和背景引用**：Nature News 关于 AI agent team 加速科研、Nature News 关于 80 年数学问题突破，以及 “From AI for Science to Agentic Science” 这类综述。

目前没有核到可靠一手来源能支持“Meta 在 2026 年 5 月解决 Erdos 数学题”这一表述。更可能需要区分为：

- OpenAI：80 年 planar unit distance / Erdos 相关数学问题的 AI-assisted discovery；
- Google DeepMind：AlphaProof Nexus 面向 formal proof search，并覆盖 Erdos 等数学问题；
- Meta：待补题名或链接，暂不写进正文主张。

## A. 已有笔记，应作为新题目的核心锚点

| Work | 当前笔记 | 推荐用法 | 为什么重要 |
|---|---|---|---|
| Accelerating scientific discovery with Co-Scientist | `Notes/systems/CoScientist_2026.md` | Multi-agent hypothesis generation + tournament/evolution 的核心锚点 | 适合支撑“科学发现不是单 agent completion，而是生成、批评、排序、演化的多角色系统” |
| A multi-agent system for automating scientific discovery / Robin | `Notes/systems/Robin_2026.md` | Lab-in-the-loop discovery workflow 的核心锚点 | 适合支撑“文献检索、候选生成、实验数据分析、下一轮候选更新”的闭环 |
| AlphaEvolve: A coding agent for scientific and algorithmic discovery | `Notes/systems/AlphaEvolve_2025.md` | Evolutionary agent workflow 的核心锚点 | 适合支撑“generate-test-refine + automated evaluator”作为可验证发现循环 |
| Kosmos: An AI Scientist for Autonomous Discovery | `Notes/systems/Kosmos_2025.md` | Long-horizon multi-agent / world-model memory 的核心锚点 | 适合支撑“长程运行、文献与代码证据、报告级 auditability” |

处理建议：

- 不必先新增这四篇笔记，已有内容可直接进正文证据链。
- 需要更新 `skill_science_evidence_matrix.md` 时，把这四篇标成主干证据。
- Co-Scientist 与 Robin 的生物医学结果只写系统层贡献，不写实验 protocol。

## B. 应新增笔记的新工作

### ERA / Empirical Research Assistance

| 字段 | 内容 |
|---|---|
| 推荐文件 | `Notes/systems/ERA_2026.md`（已新增） |
| 论文 | An AI system to help scientists write expert-level empirical software |
| 来源 | Nature, 2026-05-19, doi:10.1038/s41586-026-10658-6 |
| 机构线索 | Google / Google Research 系 |
| 核心位置 | scientific software / empirical research assistance |
| Workflow | Experiment Design; Execution; Result Analysis; Synthesis; Verification |
| Skill Lifecycle | code skill; tool-chain execution; human feedback; auditability |
| Evidence Role | Direct + Infrastructure |
| 为什么要加 | 这是 2026-05-19 Nature agentic science 三联信号之一，和 Co-Scientist、Robin 同期发布；它把“AI for science”推进到可执行 empirical software，适合连接 multi-agent scientific discovery 与科研代码生产。 |

写作角度：

- 放在“software-mediated science / executable research skill”小节。
- 和 AI Scientist、Agent Laboratory、SciNav、Jupiter、DatawiseAgent 对照。
- 重点写 empirical software 的专家级辅助、科研代码和人类研究者协作，不夸大为完全自动科学家。

### OpenAI Unit-Distance / Erdos Mathematical Discovery

| 字段 | 内容 |
|---|---|
| 推荐文件 | `Notes/systems/OpenAI_Unit_Distance_2026.md`（已新增） |
| 暂定名称 | OpenAI unit-distance / Erdos mathematics discovery |
| 来源 | OpenAI proof PDF; OpenAI remarks PDF; Nature News, 2026-05-22: AI cracks 80-year-old mathematics challenge |
| 核心位置 | AI-assisted mathematical discovery |
| Workflow | Hypothesis Generation; Search; Verification; Synthesis |
| Skill Lifecycle | reasoning skill; proof/discovery search; verifier-guided refinement |
| Evidence Role | Direct + Boundary |
| 为什么要加 | 学长特别提到“解决 Erdos 数学题”。这条线能把综述从生物/化学/材料扩展到数学发现，说明 agentic science 不只依赖 wet lab，也可以发生在形式化或半形式化搜索空间中。 |

写作角度：

- 放在“mathematical and formal scientific discovery”小节。
- 和 AlphaEvolve、AlphaProof Nexus、LLM Verifier、PaperBench/CORE-Bench 的 verification 叙事连起来。
- 需要谨慎：OpenAI proof PDF 和专家 remarks 可作为一手/验证材料，但系统架构、模型训练和 AI grading pipeline 细节未公开。

### AlphaProof Nexus

| 字段 | 内容 |
|---|---|
| 推荐文件 | `Notes/systems/AlphaProof_Nexus_2026.md`（已新增） |
| 论文 | AlphaProof Nexus: Advancing Mathematics Research with AI-Driven Formal Proof Search |
| 来源 | arXiv:2605.22763; Google DeepMind GitHub / results page 待本地下载核验 |
| 核心位置 | formal proof search / mathematical research agent |
| Workflow | Hypothesis Generation; Proof Search; Verification |
| Skill Lifecycle | formal representation; search; automated verification; proof artifact |
| Evidence Role | Direct + Boundary |
| 为什么要加 | 它和 OpenAI unit-distance 共同构成 2026 年 5 月数学发现线：一个偏开放数学发现叙事，一个偏 formal proof search 和可机器验证 artifact。 |

写作角度：

- 放在“verification-first discovery”或“formal science as an auditability extreme”。
- 它尤其适合支撑：当领域有形式验证器时，agentic discovery 的闭环比自然语言科研更清晰。
- 不要把 formal proof 成功泛化成所有科学领域可验证。

### Gemini for Science

| 字段 | 内容 |
|---|---|
| 推荐文件 | `Notes/infrastructure/Gemini_for_Science_2026.md`（已新增） |
| 来源 | Google Blog, 2026-05-20: Introducing Gemini for Science |
| 核心位置 | agentic science product / research infrastructure |
| Workflow | Knowledge Grounding; Experiment Design; Execution; Result Analysis |
| Skill Lifecycle | tool integration; multimodal reasoning; research environment integration |
| Evidence Role | Infrastructure |
| 为什么要加 | 它不是单篇 benchmark 或系统论文，但能说明大厂正在把 agentic science 做成科研基础设施，而不只是论文 prototype。 |

写作角度：

- 作为 infrastructure / ecosystem 例子，不作为强实验发现证据。
- 和 Perplexity Skills、GStack、SciToolAgent、OpenScholar 放在一起看。

## C. 只作引言或背景引用

| Work | 来源 | 用法 |
|---|---|---|
| Teams of AI agents boost speed of research | Nature News, 2026-05-19, doi:10.1038/d41586-026-01596-4 | 引言中说明 Nature 同期把 Co-Scientist、Robin、ERA 放在“AI agent teams accelerate research”的新闻框架下 |
| AI cracks 80-year-old mathematics challenge | Nature News, 2026-05-22, doi:10.1038/d41586-026-01651-0 | 引言中说明数学发现已成为 agentic science 的公众可见案例；正文不能只依赖新闻稿 |
| From AI for Science to Agentic Science: A Survey on Autonomous Scientific Discovery | arXiv:2508.14111 | 叙事结构参考：从 AI4Science 过渡到 Agentic Science，但本文需要突出 Multi-Agent 与 Evolutionary Workflow |

## D. 对新综述题目的整合方式

### 叙事主线

建议把新增工作组织成一句核心判断：

> 2026 年 5 月的一组 Nature / Google / OpenAI 信号表明，autonomous scientific discovery 正在从单点模型能力，转向多智能体协作、可执行科研软件、演化式搜索和可验证数学/实验闭环。

### 按章节嵌入

| 章节位置 | 新工作 |
|---|---|
| Introduction | Nature News 两篇、Co-Scientist、Robin、OpenAI unit-distance、AlphaProof Nexus |
| Multi-Agent Scientific Workflow | Co-Scientist、Robin、ERA、Virtual Lab、Agent Laboratory、MIRIX |
| Evolutionary / Search-Based Discovery | AlphaEvolve、AlphaProof Nexus、MC-NEST、AI Scientist Nature、Kosmos |
| Verification and Auditability | AlphaProof Nexus、OpenAI unit-distance、LLM Verifier、OpenScholar、SciVer、SPOT-a |
| Infrastructure and Ecosystem | Gemini for Science、ERA、SciToolAgent、OpenScholar、Perplexity Skills、GStack |
| Physical / Lab Grounding | Robin、Co-Scientist、A-Lab、Rainbow、RoboChem-Flex、AFION |

## E. 待确认问题

1. **Meta / Erdos 线索待核实**：当前未找到可靠一手来源能确认“Meta 解决 Erdos 数学题”。如果学长给的是内部转述，最好补具体题名、链接或机构新闻稿。
2. **OpenAI unit-distance 已完成第一版笔记**：OpenAI proof PDF 和 expert remarks PDF 已保存到 `Reference_pdf/expanded/`，笔记位于 `Notes/systems/OpenAI_Unit_Distance_2026.md`。
3. **AlphaProof Nexus 已完成第一版笔记**：arXiv PDF 已保存到 `Reference_pdf/expanded/AlphaProof_Nexus_2026_arxiv.pdf`，笔记位于 `Notes/systems/AlphaProof_Nexus_2026.md`；后续可继续核 Google DeepMind results page。
4. **ERA 已完成第一版笔记**：arXiv PDF 已保存到 `Reference_pdf/expanded/ERA_2026_arxiv.pdf`，笔记位于 `Notes/systems/ERA_2026.md`；Nature HTML/PDF 访问受站点 cookie 挑战影响，但 DOI 和正式发表信息已由 Crossref/Google Research/arXiv 互证。

## F. 下一批建议

下一批先做 4 篇非生物或低风险笔记：

1. `ERA_2026.md`（已完成第一版）
2. `OpenAI_Unit_Distance_2026.md`（已完成第一版）
3. `AlphaProof_Nexus_2026.md`（已完成第一版）
4. `Gemini_for_Science_2026.md`（已完成第一版）

完成后再回头更新：

- `Reading/expanded_paper_pool.md`
- `Reading/skill_science_evidence_matrix.md`
- `Reading/review_outline_v1.md`
