# Evidence Matrix Addendum: 2026-06 New Anchors

> 目的：补充 2026 年 6 月新增的数学发现、计算发现和科研基础设施锚点。  
> 这些条目是 `skill_science_evidence_matrix.md` 的增量，不替代原矩阵。

| Paper | Note | Scientific Workflow Stage | Skill Lifecycle Stage | Skill / Procedural Form | 对本综述的证据作用 | 关键限制 |
|---|---|---|---|---|---|---|
| ERA | `systems/ERA_2026.md` | Experiment Design / Execution / Result Analysis / Verification / Evolution | Representation / Execution / Composition / Evolution / Verification | research idea summaries + code mutation + sandbox scoring + tree search | **Direct + Infrastructure**：把 empirical scientific software 写作转化为可评分、可搜索、可重组的计算发现闭环，是 evolutionary workflow 的强证据 | 依赖 scorable tasks；不等于开放式科学问题全自动解决；需要人类检查 method fidelity |
| AlphaProof Nexus | `systems/AlphaProof_Nexus_2026.md` | Hypothesis / Proof Search / Execution / Verification / Evolution | Representation / Execution / Composition / Evolution / Verification | Lean theorem sketch + prover subagents + AlphaProof tool + rating agents + population database | **Direct + Boundary**：展示 formal verification 下的 multi-agent/evolutionary discovery；9/353 Erdos problems 和 44/492 OEIS conjectures 是强案例 | 仅适用于可形式化问题；Lean statement fidelity 仍需人类确认 |
| OpenAI Unit Distance | `systems/OpenAI_Unit_Distance_2026.md` | Hypothesis Generation / Mathematical Construction / Verification / Synthesis | Search / Execution / Verification / Synthesis | AI-generated proof + AI grading + human/expert verification + human-edited exposition | **Direct + Boundary**：展示 AI-generated research-level mathematical discovery，并与 AlphaProof Nexus 形成“开放创意 vs 形式验证”对照 | 系统细节未公开；最终进入科学记录依赖人类数学家和外部专家验证 |
| Gemini for Science | `infrastructure/Gemini_for_Science_2026.md` | Knowledge Grounding / Hypothesis Generation / Execution / Result Analysis / Synthesis | Representation / Retrieval / Composition / Execution / Verification | Hypothesis Generation + Computational Discovery + Literature Insights + Science Skills | **Infrastructure**：说明 Co-Scientist、AlphaEvolve、ERA、NotebookLM 正在被整合为科研平台和工作台 | 产品发布，不是 peer-reviewed benchmark；partner preview 不能当作独立验证结果 |

## 写作含义

这四篇/项把综述的新题目进一步推向 **Multi- & Evolutionary-Agent Workflow**：

- Co-Scientist / Gemini Hypothesis Generation 提供 multi-agent idea tournament。
- ERA / AlphaEvolve 提供 code-centered evolutionary search。
- AlphaProof Nexus 提供 multi-agent + evolutionary proof search，并用 Lean 形成硬验证闭环。
- OpenAI Unit Distance 提供开放数学发现案例，但也暴露出系统透明度和人类验证边界。

正文中可把它们组织成一句判断：

> 2026 年 5 月之后，agentic science 的前沿证据不再只来自湿实验或自动论文写作，而是同时出现在可评分科研软件、形式化数学证明、开放数学反例和平台化科研工作台中。
