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

## 3. Scientific Object Module Codes

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

说明：

- `01` 到 `11` 表示按科学研究对象划分的正式模块集合。
- 同一篇论文可进入一个或多个具体科学模块，只要论文确实对多个具体科学对象做了可识别的实验、验证、benchmark task、case study 或结果报告；不要求每个模块都构成论文的核心科学贡献。
- 不再要求所有纳入文献只能归入一个主类；是否单模块或多模块，应由论文实际覆盖的科学对象决定。
- 若论文提出通用 ASD / research-agent 方法，但没有做任何具体科学对象实验、验证、benchmark task、case study 或结果报告，则不要把它当作正式 `01` 主模块论文处理，而应放入下文的 `01.04` 专用存放区。

特别规则：

- 一般系统、复杂性与网络规律归入 `01.03`。
- 科学系统与知识生产研究归入 `11.07`。
- 只要论文有面向具体科学对象的可识别实验、验证、benchmark task、case study 或结果报告，就优先按具体科学对象归入对应模块；如同时覆盖多个具体对象模块，可多选记录。

### 3A. Special Bucket: `01.04`

`01.04` 不再作为正式主类入口，而是单独摘出的专用存放区，仅用于以下文献：

- 提出 ASD / general research-agent / general scientific workflow 方法；
- 没有做任何具体科学对象实验、验证、benchmark task、case study 或结果报告；
- 其验证主要停留在通用能力演示、流程框架、benchmark、抽象任务或领域无关评测。

执行规则：

- 只要论文出现了面向具体科学对象的可识别实验、验证、benchmark task、case study 或结果报告，就不要放入 `01.04`，而应按具体科学对象模块记录到 `01`-`11` 中的一个或多个模块。
- `01.04` 可与方法标签并存，但不应替代具体科学对象模块记录。
- `01.04` 适合作为综述中的“general ASD methods without concrete object experiments”存放区，而不是具体科学模块统计口径的一部分。

### 3B. Suggested Classification Fields

建议新增或统一使用以下字段，以承载 `general ASD methods without concrete object experiments` 和 `multi-module object coverage`：

| 字段 | 建议值 | 用途 |
|---|---|---|
| `scientific_object_modules` | `01`-`11` 中一个或多个代码 | 记录论文实际覆盖的具体科学对象模块；允许多选 |
| `object_coverage_mode` | `single_module` / `multi_module` / `general_method_without_concrete_object_experiments` | 快速标记是单模块、多模块，还是仅属于通用方法存放区 |
| `has_concrete_object_experiments` | `yes` / `no` / `uncertain` | 判断是否存在具体科学对象实验、验证、benchmark task、case study 或结果报告 |
| `general_method_bucket` | `none` / `01.04_general_asd_methods_without_concrete_object_experiments` | 单独标记是否进入 `01.04` 专用存放区 |
| `module_assignment_evidence` | 自由文本或要点列表 | 简要记录每个模块归类所依赖的对象实验依据 |
| `primary_module_for_filing` | `01`-`11` 中一个代码，或留空 | 仅用于笔记落盘、排序或表格展示时指定一个首要展示模块；不覆盖多模块事实 |
| `multi_module_object_coverage_note` | 自由文本 | 说明同一论文为何跨多个具体科学模块 |

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

注意：`digital_twin` 不决定科学对象模块。地球系统数字孪生归 `05`，工业系统数字孪生归 `09`，交通系统数字孪生归 `10`，医学数字孪生归 `07`。

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

## 13. Source Verification and Note Revision Fields

用于本轮 relaxed multi-module reclassification 和后续 note 更新时记录证据来源，避免只依赖旧单模块笔记。

| 字段 | 建议值 | 用途 |
|---|---|---|
| `first_hand_sources_checked` | `pdf` / `arxiv` / `doi_page` / `publisher_abstract` / `supplementary_material` / `official_project_page` / `official_benchmark_page` / `notes_only` / 自由文本组合 | 记录分类判断实际核对过哪些一手或权威来源；若只看了本地 note，必须写 `notes_only` 并降低置信度。 |
| `note_revision_required` | `yes` / `no` / `uncertain` | 标记现有 note 是否仍保留旧单主类、旧 `01.04` 或与原文证据不一致的分类表述。 |
| `classification_evidence_source_level` | `first_hand_full_text` / `first_hand_abstract_or_landing_page` / `project_or_benchmark_page` / `local_note_only` / `source_limited` | 标记分类证据强度和来源层级。 |

执行规则：

- `local_note_only` 或 `notes_only` 不能支撑高置信多模块新增；最多作为待全文复核线索。
- 如果原文证据支持多个对象模块，而 note 仍写作单模块或单主类，应把 `note_revision_required` 标为 `yes`。
- 若原文证据不足以确认模块，但 note 暗示可能跨模块，应记录为 `source_limited`，并在审计报告中进入 full-text follow-up queue。
