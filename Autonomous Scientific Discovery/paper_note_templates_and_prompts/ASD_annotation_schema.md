# ASD Annotation Schema

本文件定义后续文献标注时建议使用的受控字段和值。它的作用是减少同义词、自由写法和口径漂移。

## 1. Inclusion Status

| 字段值 | 含义 |
|---|---|
| `candidate` | 候选论文，尚未判断是否纳入 |
| `to_read` | 需要精读 |
| `included` | 已纳入综述 |
| `excluded` | 已排除 |
| `needs_review` | 归类或纳入判断需要复核 |
| `background_only` | 仅作背景引用，不进入核心统计 |

## 2. Agent Inclusion Criteria

每篇正式纳入论文必须同时满足：

1. 面向明确科研目标。
2. 具有多步行动过程。
3. 至少具备计划生成、工具调用、反馈迭代、自主决策、多 Agent 协作中的一项。
4. 在科研流程中承担明确角色。

建议记录：

| 字段 | 可选值 |
|---|---|
| `is_agent_paper` | `yes` / `no` / `uncertain` |
| `has_scientific_goal` | `yes` / `no` / `uncertain` |
| `has_multistep_action` | `yes` / `no` / `uncertain` |
| `has_agent_capability` | `yes` / `no` / `uncertain` |
| `has_research_workflow_role` | `yes` / `no` / `uncertain` |
| `inclusion_confidence` | `high` / `medium` / `low` |

## 3. Main Domain Codes

| Code | 中文类名 | English Directory |
|---|---|---|
| `01` | 形式、信息与计算科学 | `01_Formal_Information_and_Computational_Sciences` |
| `02` | 物理学、天文学与宇宙科学 | `02_Physics_Astronomy_and_Cosmic_Sciences` |
| `03` | 化学科学 | `03_Chemical_Sciences` |
| `04` | 材料科学 | `04_Materials_Science` |
| `05` | 地球与环境科学 | `05_Earth_and_Environmental_Sciences` |
| `06` | 生命科学 | `06_Life_Sciences` |
| `07` | 医学与健康科学 | `07_Medical_and_Health_Sciences` |
| `08` | 农业、食品、林业、畜牧与渔业科学 | `08_Agricultural_Food_Forestry_Animal_and_Fishery_Sciences` |
| `09` | 工程与工业技术科学 | `09_Engineering_and_Industrial_Technology_Sciences` |
| `10` | 航空、航天、海洋与交通科学 | `10_Aerospace_Marine_and_Transportation_Sciences` |
| `11` | 社会、行为、经济与知识系统科学 | `11_Social_Behavioral_Economic_and_Knowledge_System_Sciences` |

特别规则：

- 领域无关型科研智能系统归入 `01.04`。
- 一般系统、复杂性与网络规律归入 `01.03`。
- 科学系统与知识生产研究归入 `11.07`。
- 只要论文有具体科学对象，就优先按具体科学对象归入对应领域。

## 4. Agent Type Tags

可多选：

- `LLM Agent`
- `Planning Agent`
- `Tool-using Agent`
- `Retrieval-augmented Agent`
- `Multi-Agent System`
- `Robot / Embodied Agent`
- `Human-in-the-loop Agent`
- `Hybrid Agent`
- `Classical Agent`
- `Symbolic Agent`
- `Reinforcement Learning Agent`

## 5. Research Workflow Role Tags

可多选：

- `literature_search_and_reading`
- `knowledge_extraction_and_organization`
- `scientific_question_formulation`
- `hypothesis_generation`
- `experimental_design`
- `simulation_modeling`
- `tool_use_and_code_execution`
- `experiment_execution`
- `data_analysis`
- `result_interpretation`
- `evidence_assessment_and_validation`
- `paper_writing`
- `end_to_end_research_automation`

## 6. Autonomy Capability Tags

可多选：

- `task_decomposition`
- `planning`
- `tool_use`
- `memory_or_state_tracking`
- `feedback_iteration`
- `autonomous_decision_making`
- `multi_agent_collaboration`
- `environment_interaction`
- `closed_loop_experimentation`

## 7. Validation Type Tags

可多选：

- `benchmark`
- `simulation_validation`
- `high_throughput_computation`
- `robotic_experiment`
- `wet_lab_experiment`
- `clinical_data`
- `real_world_deployment`
- `expert_evaluation`

## 8. Cross Attribute Tags

可多选：

- `computation_driven`
- `data_driven`
- `experiment_driven`
- `simulation_driven`
- `multimodal`
- `multiscale_modeling`
- `high_throughput_screening`
- `knowledge_graph`
- `digital_twin`
- `robotic_platform`

注意：`digital_twin` 不决定主类。地球系统数字孪生归 `05`，工业系统数字孪生归 `09`，交通系统数字孪生归 `10`，医学数字孪生归 `07`。

## 9. Scientific Contribution Type

可多选：

- `hypothesis`
- `design`
- `prediction`
- `explanation`
- `experimental_discovery`
- `system_platform`
- `benchmark`
- `taxonomy`
- `negative_result`

## 10. Evidence Strength

| 字段值 | 含义 |
|---|---|
| `benchmark_only` | 仅 benchmark 支持 |
| `simulation_supported` | 有仿真支持 |
| `computationally_validated` | 有计算验证 |
| `experimentally_validated` | 有实验验证 |
| `real_world_deployment` | 有真实场景部署 |
| `expert_confirmed` | 有专家确认 |

## 11. Citation Priority

| 字段值 | 含义 |
|---|---|
| `core` | 核心引用，适合作为代表性论文 |
| `standard` | 普通引用 |
| `background` | 背景引用 |
| `do_not_cite` | 暂不引用 |

## 12. File Naming

论文笔记建议使用英文文件名：

```text
FirstAuthor_Year_ShortTitle.md
```

示例：

```text
Boiko_2023_ChemCrow.md
Bran_2024_Augmenting_Large_Language_Models_with_Chemistry_Tools.md
```

如果一篇论文有多个版本，以最终引用版本的年份为准。
