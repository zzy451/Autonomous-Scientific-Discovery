# Anchor Paper Deepening Plan v1

> 目的：把关键论文从“笔记级”升级到“论证级”。  
> 当前材料：98 篇笔记、`taxonomy_v2.md`、`skill_science_evidence_matrix.md`、`review_core_argument.md`、`review_outline_v1.md`。  
> 原则：先深挖 anchor papers，再决定是否定向补文献；不要为了数量继续泛泛扩展。

## 1. 为什么现在要深挖 anchor papers

现在 98 篇已经足够搭结构，但还不足以直接写正式正文。原因不是论文太少，而是正文需要每个核心论点都有“可展开、可核验、可比较”的主证据。

所谓“论证级”笔记，需要比普通笔记多回答：

1. 这篇论文的完整方法流程是什么？
2. 哪些关键数字必须准确引用？
3. 它能支撑综述里的哪个具体论点？
4. 它不能支撑什么过度结论？
5. 它和相邻 anchor papers 之间是什么关系？
6. 它在 `Scientific Workflow × Skill Lifecycle × Cross-cutting Constraints` 中的位置是什么？

## 2. Anchor Paper 分层

### Tier 1：必须深挖，正文会反复引用

| # | Paper | 当前笔记 | 所属主线 | 为什么是 anchor |
|---:|---|---|---|---|
| 1 | Co-Scientist | `Notes/systems/CoScientist_2026.md` | hypothesis generation / scientist-in-the-loop | 最新 Nature，直接连接假设生成、多 agent 辩论、湿实验初步验证 |
| 2 | Robin | `Notes/systems/Robin_2026.md` | lab-in-the-loop discovery | 最新 Nature，连接文献、实验数据分析和候选更新 |
| 3 | CRISPR-GPT | `Notes/systems/CRISPR_GPT_2026.md` | protocol skill / wet-lab automation | 最接近 biological protocol skill 的直接证据 |
| 4 | A-Lab | `Notes/systems/ALab_2023.md` | self-driving lab / materials | 材料 self-driving lab 核心基线，真实物理闭环 |
| 5 | CellVoyager | `Notes/systems/CellVoyager_2026.md` | notebook data analysis | Nature Methods，证明数据分析路径选择也可成为 research skill |
| 6 | SPARK | `Notes/systems/SPARK_Cancer_Pathology_2026.md` | pathology concept-to-code | Nature Medicine，概念生成、参数编码、大队列验证链条完整 |
| 7 | MOSAIC | `Notes/systems/MOSAIC_Chemical_Synthesis_2026.md` | chemical protocol / collective experts | Nature，化学合成知识分区、检索、协议生成和实验验证 |
| 8 | SciAgentGym | `Notes/benchmarks/SciAgentGym_2026.md` | scientific tool-use benchmark | 直接评测多步科学工具链，是 tool-use skill 的主基准 |
| 9 | ChemCost | `Notes/benchmarks/ChemCost_2026.md` | counterexample / resource reasoning | 强反例：有工具和领域知识仍不能可靠做化学成本推理 |
| 10 | RoboChem-Flex | `Notes/systems/RoboChem_Flex_2026.md` | low-cost self-driving lab | 说明 physical grounding 的成本、模块化和可及性 |
| 11 | SafeScientist | `Notes/verification/SafeScientist_2025.md` | safety / governance | 直接把 scientific agents 与风险感知、防御机制绑定 |
| 12 | SPOT-a | `Notes/verification/SPOT_A_2025.md` | verification / error detection | 约束 co-scientist 叙事：自动生成科学文本不等于能检测错误 |

### Tier 2：重要支撑，章节中需要局部深挖

| # | Paper | 当前笔记 | 所属主线 | 为什么重要 |
|---:|---|---|---|---|
| 13 | Kosmos | `Notes/systems/Kosmos_2025.md` | long-horizon AI scientist | world model、长程运行、跨域发现，但 preprint 需谨慎 |
| 14 | Medea | `Notes/systems/Medea_2026.md` | omics therapeutic discovery | verification-aware biomedical analysis |
| 15 | SciToolAgent | `Notes/systems/SciToolAgent_2025.md` | scientific tool infrastructure | KG-driven multi-tool integration |
| 16 | GeneAgent | `Notes/systems/GeneAgent_2025.md` | database-grounded verification | self-verification + biomedical databases |
| 17 | OpenScholar | `Notes/verification/OpenScholar_2025.md` | literature grounding / citation | citation verification 主证据 |
| 18 | PaperBench | `Notes/benchmarks/PaperBench_2025.md` | reproducibility benchmark | scientific closure 的核心约束 |
| 19 | AlphaEvolve | `Notes/systems/AlphaEvolve_2025.md` | code-based discovery loop | generate-test-refine + automated evaluator |
| 20 | MC-NEST | `Notes/systems/MC_NEST_2025.md` | hypothesis search | tree search + self-refinement |
| 21 | RINoBench | `Notes/benchmarks/RINoBench_2026.md` | novelty judgment | idea novelty 边界 |
| 22 | Robot Scientist | `Notes/systems/Robot_Scientist_2004.md` | historical baseline | LLM 之前的自动科学发现闭环 |

## 3. 按综述章节分配 anchor papers

| 章节 | 主论点 | Anchor papers | 必须补深什么 |
|---|---|---|---|
| Introduction | 领域正在从 pipeline 转向 research skills，但不是 fully autonomous science | Co-Scientist, Robin, CRISPR-GPT, A-Lab, CellVoyager, SafeScientist | 每篇能支持的“机会”和“边界”各一句 |
| Background | AI for Science、Agents、Skills、SDL 原本分散，现在需要统一框架 | AI Scientist, Agent Laboratory, SkillOS, Voyager, Robot Scientist | 历史脉络和概念区分 |
| Taxonomy | Workflow × Skill Lifecycle × Constraints | SciToolAgent, CellVoyager, CRISPR-GPT, RoboChem-Flex, SPOT-a | 每个标签的代表性例子 |
| Workflow Skills | 每个科学流程阶段都对应不同 research skill | OpenScholar, ResearchAgent, CellVoyager, SPARK, SciAgentGym, PaperBench | 阶段级能力和典型失败 |
| Physical Grounding | 真实发现必须连接仪器、样品、机器人和在线表征 | A-Lab, RoboChem-Flex, Rainbow, AFION, CRISPR-GPT, Robot Scientist | 硬件闭环、优化算法、实验反馈 |
| Tool / Notebook Infrastructure | 工具、notebook、代码是 research skill 的执行面 | SciToolAgent, SciAgentGym, ChemCost, DatawiseAgent, Jupiter, AlphaEvolve | 工具链表示、执行、失败诊断 |
| Hypothesis Generation | 假设生成不是文本生成，而是搜索、评价、验证 | Co-Scientist, ResearchAgent, LiveIdeaBench, RINoBench, MC-NEST, Causal Hypothesis | novelty、feasibility、causal、leakage |
| Verification / Governance | 科学闭环需要引用、复现、错误检测、审稿和安全 | OpenScholar, SciVer, SPOT-a, SafeScientist, Hidden Prompts, AI Responsible Publishing | 证据链、错误类型、治理边界 |
| Open Problems | evolution、transfer、failed-branch reuse、audit logs 仍薄弱 | STELLA, Kosmos, AlphaEvolve, Memory Warning, SkillOS | 哪些只是局部机制，哪些仍未解决 |

## 4. 每篇 anchor paper 的深挖模板

后续升级笔记时，每篇增加一个“论证级补充”小节，不重写全文。

```markdown
## 论证级补充

### 方法流程细化
1. 输入是什么？
2. agent / model / lab / tool 如何处理？
3. 输出是什么？
4. 反馈如何进入下一轮？

### 关键数字核对
| 指标 | 数值 | 原文位置/表格 | 可用于正文的说法 |
|---|---:|---|---|

### 可支撑的论点
- ...

### 不能支撑的过度结论
- ...

### 与其他 anchor papers 的关系
- 互补：
- 对照：
- 反例：

### 框架映射
| 维度 | 标签 |
|---|---|
| Scientific Workflow | ... |
| Skill Lifecycle | ... |
| Evidence Role | ... |
| Cross-cutting Constraints | ... |
```

## 5. 第一批深挖顺序

建议按“最能支撑主线”的顺序，而不是按论文年份。

| 顺序 | Paper | 深挖重点 |
|---:|---|---|
| 1 | Co-Scientist | 多 agent 假设生成、tournament/refinement、湿实验验证、scientist-in-the-loop 边界 |
| 2 | Robin | 文献搜索、候选生成、实验数据分析、结果反馈、lab-in-the-loop |
| 3 | CRISPR-GPT | protocol skill、state-machine workflow、真实 gene-editing demos、人类监督 |
| 4 | A-Lab | closed-loop materials lab、36/57 target、失败类型、active learning |
| 5 | CellVoyager | CellBench 设计、analysis path prediction、notebook execution、专家评价 |
| 6 | SPARK | idea-to-parameter coding、2,368 parameters、1,115 nonredundant parameters、cohort validation |
| 7 | MOSAIC | 2,498 chemical experts、71% success、35+ compounds、协议生成边界 |
| 8 | SciAgentGym | 1,780 tools、短/长交互差异、SciForge、tool dependency graph |
| 9 | ChemCost | 1,427 reactions、230,775 quotes、50.6% accuracy、阶段级失败诊断 |
| 10 | RoboChem-Flex | low-cost SDL、6 case studies、scale-up validation、human-in-loop |
| 11 | SafeScientist | SciSafetyBench、risk-aware workflow、防御机制、治理边界 |
| 12 | SPOT-a | 83 manuscripts、10 fields、错误检测任务、co-scientist failure |

## 6. 需要定向补文献的潜在薄弱点

这些不是马上扩文献，而是在 anchor 深挖后检查是否仍薄。

| 薄弱点 | 当前证据 | 可能还需补什么 |
|---|---|---|
| Skill versioning / deletion | SkillOS, ARA, Memory Warning | scientific skill version control, lab protocol versioning |
| Failed-branch reuse | ARA, Memory Warning, AlphaEvolve | failed experiment reuse, negative results learning |
| Human oversight | Co-Scientist, Robin, Adaptive AI Decision Interface | human-AI collaboration in wet labs, policy studies |
| Audit logs / provenance | ARA, OpenScholar, Kosmos | W3C PROV, RO-Crate, executable research objects |
| Biofoundry / autonomous biology | CRISPR-GPT, Robot Scientist | autonomous biofoundry, lab automation in synthetic biology |
| Real clinical validation | SPARK, Medea | prospective validation, clinical deployment governance |

## 7. 完成标准

第一批 12 篇 anchor papers 深挖完成后，应能回答：

1. 每个核心章节至少有 2-3 篇强 anchor 论文。
2. 每个 anchor paper 都有方法流程、关键数字、边界和可支撑论点。
3. `review_outline_v1.md` 中每个主论点都能指向具体论文证据。
4. 可以明确哪些章节还需要定向补 30-50 篇文献。
5. 可以开始写 Introduction 和 Taxonomy 初稿。

## 8. 下一步执行

下一步从 Tier 1 的前 4 篇开始：

1. `CoScientist_2026.md`
2. `Robin_2026.md`
3. `CRISPR_GPT_2026.md`
4. `ALab_2023.md`

这 4 篇共同支撑“从假设生成到物理实验闭环”的主线，是整篇综述最核心的一组证据。

## 9. 执行状态（2026-05-27）

按本计划的第一批完成标准，Tier 1 的 12 篇 anchor papers 已全部补充“论证级补充”小节。每篇均已覆盖方法流程、关键数字、可支撑论点、不能支撑的过度结论、与其他 anchor papers 的关系和框架映射。

| # | Paper | 笔记文件 | 状态 |
|---:|---|---|---|
| 1 | Co-Scientist | `Notes/systems/CoScientist_2026.md` | 已完成 |
| 2 | Robin | `Notes/systems/Robin_2026.md` | 已完成 |
| 3 | CRISPR-GPT | `Notes/systems/CRISPR_GPT_2026.md` | 已完成 |
| 4 | A-Lab | `Notes/systems/ALab_2023.md` | 已完成 |
| 5 | CellVoyager | `Notes/systems/CellVoyager_2026.md` | 已完成 |
| 6 | SPARK | `Notes/systems/SPARK_Cancer_Pathology_2026.md` | 已完成 |
| 7 | MOSAIC | `Notes/systems/MOSAIC_Chemical_Synthesis_2026.md` | 已完成 |
| 8 | SciAgentGym | `Notes/benchmarks/SciAgentGym_2026.md` | 已完成 |
| 9 | ChemCost | `Notes/benchmarks/ChemCost_2026.md` | 已完成 |
| 10 | RoboChem-Flex | `Notes/systems/RoboChem_Flex_2026.md` | 已完成 |
| 11 | SafeScientist | `Notes/verification/SafeScientist_2025.md` | 已完成 |
| 12 | SPOT-a | `Notes/verification/SPOT_A_2025.md` | 已完成 |

Tier 2 的 10 篇目前仍作为“章节局部支撑”保留，后续只在写到对应章节时定向深挖，不作为本轮第一批完成标准的一部分。

同时，`review_outline_v1.md` 已新增 `Anchor Claim Map`，把 Tier 1 anchor papers 映射到正文主论点，满足“每个主论点都能指向具体论文证据”的完成标准。
