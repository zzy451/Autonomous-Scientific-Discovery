# 74 篇核心文献系统笔记完整性审计（2026-06-13）

> 对象：`xyz_explicit_multi_agent_search_evolution_distribution.md` 中去除 `X0` 与 `Y0` 后的 74 篇显式多智能体搜索/演化文献。

## 审计口径

本轮优先处理两类问题：

1. **缺失笔记**：核心矩阵中有文献，但 `Notes/systems/` 下没有对应系统笔记。
2. **明显简略笔记**：字符数低于约 1500，且内容主要只有基本信息、XYZ 分类和一句话用途，无法支撑正文写作。

补全格式参考 `paper_read.md` 的深读模板，但针对综述写作做了压缩，统一采用：

- 基本信息
- 摘要要点
- 方法动机
- 方法设计
- 实验与结果
- 局限性
- XYZ 分类
- 对综述的价值

## 本轮补全结果

| 项目 | 数量 |
|---|---:|
| 核心文献总数 | 74 |
| 缺失笔记 | 0 |
| 低于 1500 字符的明显薄笔记 | 0 |

## 新建笔记

| 文献 | 文件 |
|---|---|
| `AgentReview_2024` | `Notes/systems/AgentReview_2024.md` |
| `LLM_Verifier_2025` | `Notes/systems/LLM_Verifier_2025.md` |

## 重写/补全的短笔记

| 文献 | 补全重点 |
|---|---|
| `MADD_2025` | Decomposer/Orchestrator/Summarizer、hit-identification pipeline、in silico 药物发现边界 |
| `AgentRxiv_2025` | shared preprint server、agent laboratories、开放科研产物网络；明确不强标 `Z7` |
| `El_Agente_Q_2025` | hierarchical memory、quantum chemistry workflow、in situ debugging |
| `DREAMS_2025` | central LLM planner、DFT/HPC/convergence agents、execution-feedback correction |
| `DrugMCTS_2025` | five specialized agents、RAG + MCTS、drug repurposing 推理路径搜索 |
| `GeoEvolve_2025` | outer agentic controller、inner code evolver、GeoKnowRAG、层级演化搜索 |
| `SCP_2025` | Science Context Protocol、Hub + federated servers、开放科学能力网络 |
| `Mozi_2026` | supervisor-worker control plane、stateful skill graphs、HITL checkpoints |
| `AutoResearchClaw_2026` | structured debate、自愈 executor、cross-run evolution |
| `AccelMat_2025` | hypothesis generator、critic ensemble、relevance/novelty/feasibility 筛选 |
| `MA_LoT_2025` | prover/verifier、Lean feedback；收紧为 `Y1` 而非 tree search |
| `Claw_AI_Lab_2026` | hierarchical research lab、Claw-Code Harness、rollback/resume |
| `TopoMAS_2025` | dynamic knowledge graph、memory/harness evolution、DFT validation |
| `BFS_Prover_V2_2025` | planner-enhanced multi-agent tree search、parallel prover agents、proof cache |
| `AGAPI_Agents_2025` | Agent-Planner-Executor-Summarizer、20+ materials APIs、工具编排 |
| `Materealize_2026` | multi-agent deliberation、无机材料候选、合成路线和机制解释 |
| `LeanMarathon_2026` | two-stage orchestrator、construct/audit/prove/repair agents、proof DAG |
| `ScienceClaw_Infinite_2026` | decentralized agents、skill registry、artifact DAG、global index |
| `AtomAgents_2025` | physics-aware multi-agent、LAMMPS simulation、合金候选验证 |
| `eNRRCrew_2025` | orchestrator、GraphRAG、yield/FE predictors、eNRR 催化剂推荐 |
| `RD_Agent_2025` | Researcher/Developer、exploration traces、idea-code-performance evolution |
| `Automatic_Textbook_Formalization_2026` | 30K Claude agents、共享 Lean 代码库、submit/review/merge |
| `Code2Math_2026` | Evolution/Solvability/Difficulty agents、代码执行验证、数学问题 artifact evolution |
| `PANGAEA_GPT_2026` | Supervisor-Worker、data-type-aware routing、sandboxed deterministic code execution |

## 后续可选深挖

本轮只把“明显薄”的笔记补到可支撑综述写作的程度。仍有一些 1500-2000 字左右的旧笔记，已经具备多章节结构，但如果后续正文要把它们作为主证据，可以继续扩展实验细节和对比结果，例如：

- `VirSci_2024`
- `PaperOrchestra_2026`
- `IMPROVE_2025`
- `SAGA_2025`
- `OmniScientist_2025`
- `AScience_ASCollab_2025`
- `MLZero_2025`
- `TAIS_2024`
- `AstroAgents_2025`
- `SciDER_2026`
- `OR_Agent_2026`

这些不是缺失或薄笔记，但若要作为正文 anchor paper，仍建议继续补充原文实验设计、关键数字和图表证据。

