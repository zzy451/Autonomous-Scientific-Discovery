# 74 篇核心文献系统笔记质量审查（2026-06-13）

## 结论

当前 74 篇显式多智能体搜索/演化文献的系统笔记 **已经足够支撑开始写综述初稿**，尤其足够支撑：

- 第 4 章 multi-agent organization 的组织形态分析；
- 第 5 章 evolution/search mechanisms 的机制分类；
- 材料发现、代码/证明执行、开放能力网络、verification boundary 等证据区的主线搭建；
- XYZ 交叉分布中的逐坐标证据说明。

但这些笔记 **还不等于每篇都达到可直接进入最终正文引用的 anchor-paper 深读标准**。写作时应区分主证据与辅助证据：主证据需要回原文补关键实验数字、图表、限制条件和精确术语；辅助证据可使用现有笔记支持分类和论证。

## 审查结果

| 检查项 | 结果 |
|---|---:|
| 核心文献总数 | 74 |
| 缺失系统笔记 | 0 |
| 缺少方法/流程说明 | 0 |
| 缺少实验/结果/验证说明 | 0 |
| 缺少局限性/边界说明 | 0 |
| 低于 1500 字符的笔记 | 13 |
| 来源表述仍偏粗略的笔记 | 8 |
| 仍带分类/机制不确定提醒的笔记 | 7 |

说明：低于 1500 字符不必然不可用，因为部分 review/verification/substrate 类文献本身只作为边界证据；但若要把它们写成正文主证据，需要继续加深。

## 可直接支撑正文的主证据区

这些笔记质量相对扎实，可以直接支撑章节起草：

- `Agent_Laboratory_2024`
- `AI_Scientist_Nature_2026`
- `AlphaProof_Nexus_2026`
- `CoScientist_2026`
- `CRISPR_GPT_2026`
- `EvoScientist_2026`
- `Kosmos_2025`
- `MARS_Materials_2026`
- `ResearchAgent_2025`
- `Robin_2026`
- `Science_Earth_2026`
- `Virtual_Lab_2025`

这些可以作为正文中的 anchor cases。

## 可用但建议写作前回原文补强的文献

这些笔记结构完整，但如果要在正文中承担主证据，建议补关键实验设置、指标或原文图表：

- `SAGA_2025`
- `SciDER_2026`
- `OR_Agent_2026`
- `PiFlow_2025`
- `AScience_ASCollab_2025`
- `MAESTRO_2026`
- `GeoEvolve_2025`
- `OmniScientist_2025`
- `Mimosa_2026`
- `Instrument_Agents_2026`
- `MAGenIdeas_2026`
- `EvoSci_2026`

## 需要优先精确核对来源的文献

这些笔记的来源字段仍较粗略，或论文身份更像 preprint/project report。它们可以作为辅助证据，但不建议在未回原文前写成强结论：

- `AccelMat_2025`
- `AGAPI_Agents_2025`
- `Automatic_Textbook_Formalization_2026`
- `AutoResearchClaw_2026`
- `BFS_Prover_V2_2025`
- `Claw_AI_Lab_2026`
- `Materealize_2026`
- `TopoMAS_2025`

## 分类仍需谨慎表述的文献

这些文献当前分类可用，但正文中应写得保守，避免把边界案例写成成熟范式：

- `SAGA_2025`：`X4` 取决于外层 goal-evolving agents 的多 agent 组织是否足够明确。
- `AScience_ASCollab_2025`：开放/演化网络证据强，但具体发现闭环需要谨慎。
- `OR_Agent_2026`：自动算法发现与科学发现的边界需要说明。
- `PiFlow_2025`：更偏原则化探索框架，需要结合执行/验证系统。
- `SciDER_2026`：严格 ASD 候选，但最终科学发现强度需看实验任务。
- `MAESTRO_2026`：主要在计算候选发现层面，真实实验验证边界需说明。
- `GeoEvolve_2025`：模型/代码演化证据强，但外部科学有效性需专家解释。

## 是否可以开始写综述

可以。建议采用下面策略：

1. 先用当前笔记写第 4/5 章的结构性初稿。
2. anchor papers 使用上面“可直接支撑正文”的主证据。
3. 边界/辅助文献用于补坐标、补广度，不承担强结论。
4. 写到具体实验数字、claim 或 quote 时，再回原文逐条核对。
5. 不要等 74 篇都达到同等深读标准再开始写；那会拖慢主线形成。

