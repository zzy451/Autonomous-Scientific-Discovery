# Batch 4 / Wave A 多模块重分类审计报告

> 日期：2026-06-20  
> 范围：`agent_master_paper_list.md` confirmed 记录序号 340-395。  
> 对应计划：`Coverage_Check/multi_module_reclassification_flat_batch_plan_451_confirmed_2026-06-20.md`。  
> 当前阶段：Reviewer 已完成，主控已合并；本轮不修改主列表。

## 一、基线

本轮开始前主列表状态：

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

## 二、Wave A 分工

本轮按当前主列表 confirmed 记录出现顺序抽取序号 340-395。注意：计划表中的 ID 边界只表示 confirmed 顺序范围，不保证连续编号；本报告使用当前主列表解析得到的精确 ID 切片。

| Reviewer | Agent | 记录数 | 分配 ID |
|---|---|---:|---|
| A-Reviewer-1 | Boole | 14 | `ASD-0740`, `ASD-0741`, `ASD-0742`, `ASD-0743`, `ASD-0744`, `ASD-0745`, `ASD-0747`, `ASD-0748`, `ASD-0749`, `ASD-0750`, `ASD-0751`, `ASD-0752`, `ASD-0753`, `ASD-0754` |
| A-Reviewer-2 | Zeno | 14 | `ASD-0755`, `ASD-0756`, `ASD-0757`, `ASD-0758`, `ASD-0759`, `ASD-0760`, `ASD-0761`, `ASD-0762`, `ASD-0763`, `ASD-0764`, `ASD-0765`, `ASD-0766`, `ASD-0768`, `ASD-0769` |
| A-Reviewer-3 | Heisenberg | 14 | `ASD-0770`, `ASD-0771`, `ASD-0772`, `ASD-0773`, `ASD-0774`, `ASD-0775`, `ASD-0779`, `ASD-0780`, `ASD-0781`, `ASD-0782`, `ASD-0783`, `ASD-0784`, `ASD-0786`, `ASD-0787` |
| A-Reviewer-4 | Hume | 14 | `ASD-0789`, `ASD-0790`, `ASD-0791`, `ASD-0792`, `ASD-0793`, `ASD-0794`, `ASD-0796`, `ASD-0797`, `ASD-0798`, `ASD-0799`, `ASD-0800`, `ASD-0801`, `ASD-0803`, `ASD-0804` |

## 三、主控合并口径

本轮沿用 Batch 1-3 校准后的口径：

- 分类依据是实际研究和实验覆盖的科学对象，不是 Agent 技术、平台名称、venue 或自称通用性。
- 有具体科学对象实验的论文，优先进入对应 `01-11` 对象模块，而不是回收到 `01.04`。
- 只有多个具体科学对象各自有实质实验或结果贡献时，才建议 multi-module。
- 没有任何具体科学对象实验、只提出 ASD / general research-agent 方法或通用 benchmark 的论文，进入独立 `01.04` bucket。
- `03 / 04` 继续按分子、反应、合成、催化 vs 材料组成、结构、相、性能、器件材料对象判断。
- `05 / 10` 继续按自然地球环境对象 vs 航天/任务/载具对象判断。
- `06 / 07` 继续按 biological mechanism / protein / omics vs disease / therapeutic / clinical endpoint 判断。
- `09 / 03` 对 chemical process design 等记录，按工程流程、装置、过程系统 vs 化学反应/分子对象判断。
- `11.07 / 01.04` 继续按 scientific knowledge production itself vs general research-agent workflow 判断。

默认不直接改主列表，除非同时满足：

- Reviewer 证据清楚；
- 主控复核规则一致；
- 不依赖缺失全文；
- 不会造成 schema 迁移半成品。

## 四、Reviewer 原始输出

### A-Reviewer-1: Boole

状态：已返回，14 / 14 条完整覆盖。

主要结论：

- `ASD-0740` 保持 `03`，直接搜索对象是有机发射体分子；solid-state laser 应用不足以转 `04`。
- `ASD-0741`, `ASD-0742`, `ASD-0743`, `ASD-0744`, `ASD-0745` 保持 `06`，spatial transcriptomics、kinetic biological models、bioinformatics、life-sciences research 对象稳定。
- `ASD-0747`, `ASD-0749`, `ASD-0752`, `ASD-0753`, `ASD-0754` 保持 `09`，FEA、topology optimization、structural engineering workflows 是工程对象。
- `ASD-0748`, `ASD-0750`, `ASD-0751` 保持 `02`，exoplanet research、particle-physics experiment design、cosmology 对象稳定。
- 本切片未发现应转入 `01.04` 或新增 multi-module 的记录。

### A-Reviewer-2: Zeno

状态：已返回，14 / 14 条完整覆盖。

主要结论：

- `ASD-0755`, `ASD-0756`, `ASD-0757`, `ASD-0758` 保持 `09`，structural analysis / CAD generation / FEA feedback 是工程设计或结构工程对象。
- `ASD-0759`, `ASD-0760`, `ASD-0761`, `ASD-0762`, `ASD-0763`, `ASD-0764` 保持 `02`，physics / quantum physics / quantum sensor / HEP / astronomy 对象明确。
- `ASD-0765` 保持 `05`，CLIMATEAGENT 的任务、API、benchmark 都是 climate-science objects。
- `ASD-0766`, `ASD-0768` 保持 `11.07`，scientific peer review / review disagreement 是 scientific knowledge production itself。
- `ASD-0769` 保持 `07`，medical research / clinical evidence object 稳定；后续可复核二级位点。
- 本切片未发现应转入 `01.04` 或新增 multi-module 的记录。

### A-Reviewer-3: Heisenberg

状态：已返回，14 / 14 条完整覆盖。

主要结论：

- `ASD-0770` 保持 `06`，biological perturbation prediction 是生命科学对象，不因 drug-discovery framing 转 `07`。
- `ASD-0771`, `ASD-0773`, `ASD-0774` 保持 `07`，clinical reasoning、NSCLC biomarker、medical evidence screening 是医学对象。
- `ASD-0772`, `ASD-0783`, `ASD-0784` 保持 `05`，seismology、Earth observation、GIS/geospatial analysis 对象稳定。
- `ASD-0775`, `ASD-0779`, `ASD-0780`, `ASD-0781`, `ASD-0782` 保持 `09`，scientific instrumentation、chemical process / flowsheet simulation、CFD engineering simulation 是工程对象。
- `ASD-0786` 保持 `11.07`，peer review dynamics 是 scientific knowledge production system。
- `ASD-0787` 保持独立 `01.04`，SciToolAgent 是 multitool integration / workflow orchestration；cross-domain demos 不构成对象层多模块。

### A-Reviewer-4: Hume

状态：已返回，14 / 14 条完整覆盖。

主要结论：

- `ASD-0789` 保持 `09`，TEM instrumentation / facility workflow 是工程仪器对象，不因材料场景转 `04`。
- `ASD-0790`, `ASD-0791`, `ASD-0792`, `ASD-0794` 保持 `04`，heterogeneous catalyst / COF / catalyst material / high-throughput material campaign 是材料对象。
- `ASD-0793` 保持 `03`，adsorption configuration / surface chemistry 是化学对象。
- `ASD-0796`, `ASD-0800`, `ASD-0801`, `ASD-0803` 保持 `05`，EO、geospatial retrieval、geothermal/subsurface、social-climate dynamics 以地球环境对象为主；`ASD-0803` 列入 `05 / 11` 边界复核。
- `ASD-0797` 保持 `06`，cell morphology / perturbation phenotypes 是生命科学对象。
- `ASD-0798` 保持 `07`，lead optimization / ADMET 以 drug discovery endpoint 为主。
- `ASD-0799`, `ASD-0804` 保持 `09`，chemical process development / flowsheet generation 是过程工程对象。

## 五、主控裁决表

Wave A 共 56 条，全部完成 Reviewer 覆盖。主控裁决如下：

| ID | Legacy filing | Reviewer suggestion | 主控裁决 | 是否改主列表 | 备注 |
|---|---|---|---|---|---|
| `ASD-0740` | `03 / 03.04` | `03` | 保持 `03` | 否 | organic emitter molecules；solid-state laser application 不触发 `04` |
| `ASD-0741` | `06 / 06.03` | `06` | 保持 `06` | 否 | spatial transcriptomics / hPSC-pancreas maturation |
| `ASD-0742` | `06 / 06.01` | `06` | 保持 `06`，列入全文补强 | 否 | kinetic biological models / systems biology |
| `ASD-0743` | `06 / 06.03` | `06` | 保持 `06`，列入全文补强 | 否 | spatial transcriptomics framework |
| `ASD-0744` | `06 / 06.03` | `06` | 保持 `06`，列入全文补强 | 否 | automated bioinformatics tasks；abstract-level evidence |
| `ASD-0745` | `06 / 06.03` | `06` | 保持 `06` | 否 | autonomous life sciences research / biological foundation models |
| `ASD-0747` | `09 / 09.01` | `09` | 保持 `09`，列入 core-strength 复核 | 否 | automated FEA / engineering mechanics |
| `ASD-0748` | `02 / 02.01` | `02` | 保持 `02` | 否 | exoplanet atmospheric characterization |
| `ASD-0749` | `09 / 09.02` | `09` | 保持 `09`，列入 core-strength 复核 | 否 | topology optimization engineering design |
| `ASD-0750` | `02 / 02.02` | `02` | 保持 `02` | 否 | particle-physics experiment design |
| `ASD-0751` | `02 / 02.01` | `02` | 保持 `02`，列入全文补强 | 否 | cosmology autonomous discovery preliminary evidence |
| `ASD-0752` | `09 / 09.05` | `09` | 保持 `09`，列入 core-strength 复核 | 否 | automated structural analysis |
| `ASD-0753` | `09 / 09.05` | `09` | 保持 `09` | 否 | 2D frame structural analysis multi-agent system |
| `ASD-0754` | `09 / 09.05` | `09` | 保持 `09`，列入 deployment/safety-depth 复核 | 否 | structural engineering workflows |
| `ASD-0755` | `09 / 09.05` | `09` | 保持 `09` | 否 | multi-platform structural analysis |
| `ASD-0756` | `09 / 09.05` | `09` | 保持 `09` | 否 | 3D frame structural analysis |
| `ASD-0757` | `09 / 09.02` | `09` | 保持 `09` | 否 | CAD generation with geometric validation |
| `ASD-0758` | `09 / 09.02` | `09` | 保持 `09` | 否 | CAD generation with FEA feedback |
| `ASD-0759` | `02 / 02.02` | `02` | 保持 `02`，列入全文补强 | 否 | autonomous AI physicist；platform-heavy physics object |
| `ASD-0760` | `02 / 02.02` | `02` | 保持 `02` | 否 | autonomous quantum physics research |
| `ASD-0761` | `02 / 02.02` | `02` | 保持 `02` | 否 | variational quantum circuit design |
| `ASD-0762` | `02 / 02.02` | `02` | 保持 `02` | 否 | quantum sensor / cold-atom experiment |
| `ASD-0763` | `02 / 02.02` | `02` | 保持 `02` | 否 | BSM collider searches and limits |
| `ASD-0764` | `02 / 02.01` | `02` | 保持 `02` | 否 | gravitational-wave counterpart association |
| `ASD-0765` | `05 / 05.02` | `05` | 保持 `05` | 否 | climate data-science workflows |
| `ASD-0766` | `11 / 11.07` | `11.07` | 保持 `11.07`，列入全文补强 | 否 | review substantiveness / peer-review quality |
| `ASD-0768` | `11 / 11.07` | `11.07` | 保持 `11.07`，列入全文补强 | 否 | contradiction analysis in scientific peer reviews |
| `ASD-0769` | `07 / 07.04` | `07` | 保持 `07`，列入二级位点复核 | 否 | medical research / clinical evidence；`07.03 / 07.04` secondary boundary |
| `ASD-0770` | `06 / 06.03` | `06` | 保持 `06`，列入 core-strength 复核 | 否 | biological perturbation prediction |
| `ASD-0771` | `07 / 07.02` | `07` | 保持 `07` | 否 | clinical genetics / rare-disease reasoning |
| `ASD-0772` | `05 / 05.01` | `05` | 保持 `05` | 否 | seismology physical reasoning |
| `ASD-0773` | `07 / 07.02` | `07` | 保持 `07` | 否 | NSCLC transcriptomic biomarker medical endpoint |
| `ASD-0774` | `07 / 07.03` | `07` | 保持 `07` | 否 | medical evidence screening |
| `ASD-0775` | `09 / 09.01` | `09` | 保持 `09` | 否 | scientific instrumentation / instrument-control workflow |
| `ASD-0779` | `09 / 09.04` | `09` | 保持 `09` | 否 | chemical process design / flowsheet simulation |
| `ASD-0780` | `09 / 09.04` | `09` | 保持 `09` | 否 | model-based process design |
| `ASD-0781` | `09 / 09.04` | `09` | 保持 `09` | 否 | chemical process simulations |
| `ASD-0782` | `09 / 09.01` | `09` | 保持 `09` | 否 | CFD engineering simulation |
| `ASD-0783` | `05 / 05.04` | `05` | 保持 `05` | 否 | Earth observation / remote sensing |
| `ASD-0784` | `05 / 05.04` | `05` | 保持 `05` | 否 | GIS / geospatial analysis |
| `ASD-0786` | `11 / 11.07` | `11.07` | 保持 `11.07`，列入全文补强 | 否 | peer-review dynamics |
| `ASD-0787` | `01 / 01.04` | `01.04` | 保持独立 `01.04`，列入 demo 权重全文复核 | 否 | multitool integration general scientific agent |
| `ASD-0789` | `09 / 09.01` | `09` | 保持 `09` | 否 | TEM instrumentation / facility workflow |
| `ASD-0790` | `04 / 04.04` | `04` | 保持 `04` | 否 | heterogeneous catalyst material discovery |
| `ASD-0791` | `04 / 04.04` | `04` | 保持 `04` | 否 | durable photocatalytic COF materials |
| `ASD-0792` | `04 / 04.04` | `04` | 保持 `04` | 否 | heterogeneous catalyst material / digital twin as method |
| `ASD-0793` | `03 / 03.03` | `03` | 保持 `03` | 否 | adsorption configuration / surface chemistry |
| `ASD-0794` | `04 / 04.04` | `04` | 保持 `04` | 否 | high-throughput material campaigns |
| `ASD-0796` | `05 / 05.04` | `05` | 保持 `05` | 否 | Earth observation meta-planner |
| `ASD-0797` | `06 / 06.03` | `06` | 保持 `06` | 否 | cellular morphological profiling |
| `ASD-0798` | `07 / 07.04` | `07` | 保持 `07` | 否 | molecular lead optimization / ADMET endpoint |
| `ASD-0799` | `09 / 09.04` | `09` | 保持 `09` | 否 | automated chemical process development |
| `ASD-0800` | `05 / 05.04` | `05` | 保持 `05` | 否 | geospatial data retrieval |
| `ASD-0801` | `05 / 05.01` | `05` | 保持 `05` | 否 | geothermal / subsurface geophysics |
| `ASD-0803` | `05 / 05.02` | `05` | 保持 `05`，列入 `05 / 11` 边界复核 | 否 | social-climate dynamics with policy/socioeconomic variables |
| `ASD-0804` | `09 / 09.04` | `09` | 保持 `09` | 否 | process-engineering flowsheet generation |

## 六、Wave A 口径校准结论

基于 56 条完整结果，本轮形成以下校准结论：

1. Batch 4 / Wave A 未发现高置信 multi-module assignment。平台型、benchmark-heavy、多 Agent、多工具、跨子任务均不足以触发多模块，除非每个具体对象都有独立实质结果。
2. 本轮只有 `ASD-0787` 稳定留在独立 `01.04`。它的 biology / chemistry / materials demos 主要支持 tool integration / workflow orchestration，不构成对象层科学贡献。
3. `03 / 04` 催化边界继续需要逐条判断。`ASD-0790`, `ASD-0792` 是 catalyst material candidate discovery，保留 `04`；`ASD-0793` 的对象是 adsorption configuration / surface chemistry，保留 `03`。
4. `09 / 03` 边界在 process / flowsheet records 中稳定。`ASD-0779`, `ASD-0780`, `ASD-0781`, `ASD-0799`, `ASD-0804` 均以 process engineering / flowsheet simulation 为对象，保留 `09`，不按分子化学转 `03`。
5. `06 / 07` 继续按 biological object vs medical endpoint 判定。`ASD-0770`, `ASD-0797` 保持 `06`；`ASD-0771`, `ASD-0773`, `ASD-0774`, `ASD-0798` 保持 `07`。
6. `11.07 / 01.04` 边界继续按对象判定。`ASD-0766`, `ASD-0768`, `ASD-0786` 研究 peer review / review dynamics，归 `11.07`；不是通用科研 Agent bucket。
7. `digital twin`、scientific instrumentation、workflow orchestration 不决定主类。`ASD-0792` 保持 `04`，`ASD-0801` 保持 `05`，`ASD-0789` 保持 `09`。
8. `ASD-0803` 是本轮最强 `05 / 11` 边界样本：当前保留 `05.02`，但如果全文证明社会政策、经济或不平等对象有独立实质实验，可在二轮考虑 `11` 或 `05+11`。
9. 当前没有足够证据支持重构一级分类，问题主要集中在边界解释与低覆盖类稀缺性判断。

## 七、待主控复核队列

Wave A 暂列以下记录为主控复核或后续全文复核：

| ID | 当前 legacy | 初步问题 | 暂定处理 |
|---|---|---|---|
| `ASD-0742` | `06 / 06.01` | Talk2Biomodels 的 autonomy depth 与 biological-model contribution strength | 暂保持 `06` |
| `ASD-0743` | `06 / 06.03` | spatial transcriptomics framework 的 biological case depth | 暂保持 `06` |
| `ASD-0744` | `06 / 06.03` | BioGAIP abstract-level / core-strength evidence | 暂保持 `06` |
| `ASD-0747` | `09 / 09.01` | VFEAgent 的 discovery-core strength vs workflow automation | 暂保持 `09` |
| `ASD-0749` | `09 / 09.02` | TopOptAgents 的 topology optimization object 与 core-strength | 暂保持 `09` |
| `ASD-0751` | `02 / 02.01` | cosmology autonomous-discovery evidence depth | 暂保持 `02` |
| `ASD-0752` | `09 / 09.05` | structural-analysis automation 的 Agent / discovery strength | 暂保持 `09` |
| `ASD-0754` | `09 / 09.05` | deployment/safety-depth and engineering workflow strength | 暂保持 `09` |
| `ASD-0759` | `02 / 02.02` | PhysMaster platform-heavy physics object evidence | 暂保持 `02` |
| `ASD-0766` | `11 / 11.07` | ReviewGrounder evidence depth / peer-review core strength | 暂保持 `11.07` |
| `ASD-0768` | `11 / 11.07` | peer-review contradiction analysis full-text evidence | 暂保持 `11.07` |
| `ASD-0769` | `07 / 07.04` | medical evidence-based research 的 `07.03 / 07.04` secondary boundary | 暂保持 `07` |
| `ASD-0770` | `06 / 06.03` | perturbation prediction 的 core-strength / drug-discovery framing | 暂保持 `06` |
| `ASD-0786` | `11 / 11.07` | AgentReview 的 peer-review dynamics evidence depth | 暂保持 `11.07` |
| `ASD-0787` | `01 / 01.04` | cross-domain demos 是否有对象层科学贡献 | 暂保持 `01.04` |
| `ASD-0803` | `05 / 05.02` | social-climate dynamics 的 `05 / 11` 边界与多模块可能性 | 暂保持 `05` |

## 八、本轮统计

| Metric | Count |
|---|---:|
| reviewed records | 56 |
| Reviewer-covered records | 56 |
| unchanged by 主控 | 56 |
| add_module | 0 |
| move_primary | 0 |
| move_to_01.04 | 0 |
| demote/background-review candidate | 0 |
| main-control / full-text follow-up queue | 16 |
| records with `full_text_required=yes` from Reviewer output | 15 |

本轮不修改 `agent_master_paper_list.md`。主列表 record-level confirmed count 仍为 `451`，`needs_review` 仍为 `0`，confirmed `08` 仍为 `3`。
