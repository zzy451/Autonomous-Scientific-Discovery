# Batch 2 多模块重分类审计汇总

> Transitional note 2026-06-20：本文件保留为早期多模块审计记录。当前重新开审时，以 `multi_module_reclassification_relaxed_round_plan_451_confirmed_2026-06-20.md` 为优先口径；不能用“主对象 / 核心贡献 / 只是 demo”排除模块，必须逐项检查具体科学对象实验、验证、benchmark task、case study 或结果报告。

> 日期：2026-06-20  
> 范围：`agent_master_paper_list.md` confirmed 记录序号 114-226。  
> 对应批次：`Coverage_Check/multi_module_reclassification_flat_batch_plan_451_confirmed_2026-06-20.md` 的 Batch 2。  
> 子报告：`multi_module_reclassification_batch2_waveA_2026-06-20.md` 与 `multi_module_reclassification_batch2_waveB_2026-06-20.md`。  

## 一、批次基线

Batch 2 开始前主列表状态：

- master list total records: 871
- confirmed record-level count: 451
- `needs_review`: 0
- confirmed `08`: 3
- legacy confirmed `01.04`: 46

legacy confirmed 主类分布：

| Legacy main class | Count |
|---|---:|
| `01` | 52 |
| `02` | 29 |
| `03` | 60 |
| `04` | 95 |
| `05` | 23 |
| `06` | 51 |
| `07` | 51 |
| `08` | 3 |
| `09` | 34 |
| `10` | 23 |
| `11` | 30 |

## 二、执行覆盖

| Wave | Reviewed records | Reviewer-covered records | 主控状态 |
|---|---:|---:|---|
| Wave A | 57 | 57 | 已合并 |
| Wave B | 56 | 56 | 已合并 |
| Batch 2 total | 113 | 113 | 已完成 |

本批所有分配记录均已由只读 Reviewer 覆盖，且均已完成主控裁决。子 Agent 均未编辑主列表。

## 三、主控落地结论

本批不修改 `agent_master_paper_list.md`。原因是：

- 未发现高置信、证据充分、且不依赖 schema 迁移的即时改表项。
- Reviewer 建议的潜在变更多属于全文补强、Agent-strength 复核或平台边界复核。
- 当前主列表仍处于 legacy filing 字段过渡期；本轮目标优先是审计与口径稳定，不强行做半成品 schema 迁移。

| Metric | Count |
|---|---:|
| reviewed records | 113 |
| unchanged by 主控 | 113 |
| add_module | 0 |
| move_primary | 0 |
| move_to_01.04 | 0 |
| demote/background-review candidate | 0 |
| main-control / full-text follow-up queue | 36 |
| records with `full_text_required=yes` from Reviewer output | 33 |

主列表 record-level confirmed count 仍为 `451`，`needs_review` 仍为 `0`，confirmed `08` 仍为 `3`。

## 四、边界校准

Batch 2 的关键校准结论如下：

1. `01.04` 独立 bucket 的使用更加清晰。`ASD-0254`, `ASD-0447`, `ASD-0524`, `ASD-0525`, `ASD-0528`, `ASD-0530`, `ASD-0553`, `ASD-0554` 等记录都显示：只有没有具体对象层科学贡献、主要是 general research-agent workflow / platform / benchmark 时，才保留 `01.04`。
2. 平台感强但对象实验明确时，不退回 `01.04`。`ASD-0540`, `ASD-0570`, `ASD-0587`, `ASD-0600` 等记录需要全文复核，但当前对象实验仍支持其对应领域。
3. 本批未发现高置信 multi-module assignment。跨工具、跨数据源、跨 demo、跨材料家族或跨实验设备不等于跨一级科学对象模块。
4. `03 / 04` 继续按最终对象而非实验手段处理。反应、分子、合成路线、化学机制和 chemical synthesis execution 归 `03`；纳米晶、电池电解质、聚合物、薄膜、metasurface、合金、MOF 等材料结构/性能对象归 `04`。
5. `06 / 07` 继续按 endpoint 判断。Gene/protein/enzyme/omics/biofoundry 通常归 `06`；drug discovery、therapeutic discovery、cancer pathology、cancer biomarker、clinical/biomarker endpoint 归 `07`。
6. `04 / 09` 继续按“材料对象 vs 工程工艺/设备对象”判断。设备、reactor、robotic platform、beamline、biofoundry 通常是执行手段；只有工程系统或工艺本身成为研究对象时才优先 `09`。
7. `11.07` 不应泛化为所有处理 scientific literature 的论文入口。若文献处理最终服务于 chemical synthesis execution，仍按 `03` 处理。
8. 当前没有足够证据支持重构一级分类，问题主要集中在边界解释、全文证据强弱和 Agent minimum strength，而不是 `01-11` 顶层 taxonomy 失稳。

## 五、Batch 2 后续复核队列

| ID | 当前 legacy | 边界问题 | 暂定处理 |
|---|---|---|---|
| `ASD-0179` | `03 / 03.03` | reaction condition coverage 需全文补强 | 暂保持 `03` |
| `ASD-0186` | `11 / 11.07` | scientific peer review object vs generic review workflow | 暂保持 `11.07` |
| `ASD-0189` | `06 / 06.03` | proteomics hypothesis validation 细节需补强 | 暂保持 `06` |
| `ASD-0254` | `01 / 01.04` | biomedical research workflow 是否确无具体对象实验 | 暂保持 `01.04` |
| `ASD-0276` | `06 / 06.03` | clinical multiomics source 是否改变 endpoint | 暂保持 `06` |
| `ASD-0290` | `03 / 03.02` | catalyst / material structure-property 边界 | 暂保持 `03` |
| `ASD-0333` | `03 / 03.04` | chemistry hypothesis benchmark 的 confirmed-core strength | 暂保持 `03` |
| `ASD-0357` | `07 / 07.04` | therapeutic target discovery validation 细节需补强 | 暂保持 `07` |
| `ASD-0381` | `03 / 03.03` | catalysis Pareto-front mapping 细节需补强 | 暂保持 `03` |
| `ASD-0388` | `04 / 04.01` | crystallography companion 的 confirmed-core strength | 暂保持 `04` |
| `ASD-0429` | `09 / 09.02` | additive manufacturing record 的 core strength | 暂保持 `09` |
| `ASD-0447` | `01 / 01.04` | universal chemical synthesis platform vs concrete chemistry object | 暂保持 `01.04` |
| `ASD-0466` | `04 / 04.03` | CNT automated experimentation 的 Agent/autonomy 强度 | 暂保持 `04` |
| `ASD-0478` | `04 / 04.04` | NIMS-OS orchestration software 是否平台贡献过强 | 暂保持 `04` |
| `ASD-0510` | `08 / 08.01` | plant phenotyping 方向稳定，但 evidence strength 需补强 | 暂保持 `08` |
| `ASD-0513` | `04 / 04.04` | networked autonomous materials exploration core-strength | 暂保持 `04` |
| `ASD-0516` | `04 / 04.04` | equipment-heavy PVD system 的 `04 / 09` nuance | 暂保持 `04` |
| `ASD-0519` | `03 / 03.02` | Agent minimum beyond automation 需全文确认 | 暂保持 `03` |
| `ASD-0520` | `04 / 04.04` | Agent minimum 与 `04 / 03` catalyst boundary | 暂保持 `04` |
| `ASD-0523` | `01 / 01.02` | AI research automation 是否 benchmark-heavy | 暂保持正式 `01` |
| `ASD-0524` | `01 / 01.04` | SciML benchmark 是否有具体对象层贡献 | 暂保持 `01.04` |
| `ASD-0528` | `01 / 01.04` | 多 demo 是否仅为 framework demonstration | 暂保持 `01.04` |
| `ASD-0530` | `01 / 01.04` | framework-heavy / core-strength | 暂保持 `01.04` |
| `ASD-0536` | `07 / 07.04` | TCM-Agent core-strength 与平台感 | 暂保持 `07` |
| `ASD-0541` | `06 / 06.03` | PromptBio 平台型 bioinformatics 是否应转 `01.04` | 暂保持 `06` |
| `ASD-0543` | `06 / 06.03` | prognostic gene discovery 的 `06 / 07` endpoint | 暂保持 `06` |
| `ASD-0547` | `04 / 04.04` | metasurface design 的 `04 / 09` 细节 | 暂保持 `04` |
| `ASD-0553` | `01 / 01.04` | bioinformatics automation substrate 边界 | 暂保持 `01.04` |
| `ASD-0554` | `01 / 01.04` | reproducible translational-bioinformatics workflow 边界 | 暂保持 `01.04` |
| `ASD-0565` | `04 / 04.04` | metadata-limited Agent-strength | 暂保持 `04` |
| `ASD-0570` | `04 / 04.04` | MARS platform-heavy `01.04 / domain` 边界 | 暂保持 `04` |
| `ASD-0579` | `07 / 07.04` | classical active-learning Agent-strength | 暂保持 `07` |
| `ASD-0587` | `03 / 03.03` | collective-intelligence synthesis 的 `03 / 01.04` 边界 | 暂保持 `03` |
| `ASD-0596` | `06 / 06.03` | LLM role 是否只是 workflow-code generation | 暂保持 `06` |
| `ASD-0599` | `06 / 06.03` | preprint / evidence completeness | 暂保持 `06` |
| `ASD-0600` | `03 / 03.03` | universal chemputation system 的 `03 / 01.04` 边界 | 暂保持 `03` |

## 六、下一步

下一步按计划进入 Batch 3 / Wave A，仍采用四个只读 Reviewer、每人约 14-15 篇的 micro-batch 设计。Batch 3 不按风险优先抽样，继续按 confirmed 记录出现顺序平铺推进。
