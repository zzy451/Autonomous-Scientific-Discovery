# Batch 2 / Wave B 多模块重分类审计报告

> 日期：2026-06-20  
> 范围：`agent_master_paper_list.md` confirmed 记录序号 171-226。  
> 对应计划：`Coverage_Check/multi_module_reclassification_flat_batch_plan_451_confirmed_2026-06-20.md`。  
> 当前阶段：Reviewer 审核进行中；本文档先记录基线、分工和待合并字段，最终主控裁决将在 Reviewer 返回后补入。

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

## 二、Wave B 分工

本轮按当前主列表 confirmed 记录出现顺序抽取序号 171-226。注意：计划表中的 ID 边界只表示 confirmed 顺序范围，不保证连续编号；本报告使用当前主列表解析得到的精确 ID 切片。

| Reviewer | Agent | 记录数 | 分配 ID |
|---|---|---:|---|
| B-Reviewer-1 | James | 14 | `ASD-0524`, `ASD-0525`, `ASD-0526`, `ASD-0528`, `ASD-0529`, `ASD-0530`, `ASD-0531`, `ASD-0535`, `ASD-0536`, `ASD-0537`, `ASD-0538`, `ASD-0539`, `ASD-0540`, `ASD-0541` |
| B-Reviewer-2 | Kuhn | 14 | `ASD-0542`, `ASD-0543`, `ASD-0544`, `ASD-0545`, `ASD-0547`, `ASD-0548`, `ASD-0549`, `ASD-0552`, `ASD-0553`, `ASD-0554`, `ASD-0556`, `ASD-0557`, `ASD-0558`, `ASD-0564` |
| B-Reviewer-3 | Copernicus | 14 | `ASD-0565`, `ASD-0567`, `ASD-0568`, `ASD-0569`, `ASD-0570`, `ASD-0571`, `ASD-0572`, `ASD-0573`, `ASD-0574`, `ASD-0575`, `ASD-0576`, `ASD-0577`, `ASD-0579`, `ASD-0581` |
| B-Reviewer-4 | Erdos | 14 | `ASD-0582`, `ASD-0586`, `ASD-0587`, `ASD-0589`, `ASD-0590`, `ASD-0591`, `ASD-0592`, `ASD-0617`, `ASD-0618`, `ASD-0596`, `ASD-0597`, `ASD-0598`, `ASD-0599`, `ASD-0600` |

## 三、主控合并口径

本轮沿用 Batch 1 与 Batch 2 / Wave A 校准后的口径：

- 分类依据是实际研究和实验覆盖的科学对象，不是 Agent 技术、平台名称、venue 或自称通用性。
- 有具体科学对象实验的论文，优先进入对应 `01-11` 对象模块，而不是回收到 `01.04`。
- 只有多个具体科学对象各自有实质实验或结果贡献时，才建议 multi-module。
- 没有任何具体科学对象实验、只提出 ASD / general research-agent 方法或通用 benchmark 的论文，进入独立 `01.04` bucket。
- `03 / 04` 继续按最终对象判断：反应、分子、合成路线、化学机制归 `03`；纳米晶、薄膜、聚合物、电解质、合金、metasurface 等材料结构/性能对象归 `04`。
- `06 / 07` 继续按 endpoint 判断：gene/protein/enzyme/omics/biofoundry 通常归 `06`；drug discovery、therapeutic discovery、cancer pathology、clinical/biomarker endpoint 通常归 `07`。
- 强平台样论文不自动进入 `01.04`；只有没有具体科学对象实验或对象层贡献时，才保留或移动到独立 `01.04`。

默认不直接改主列表，除非同时满足：

- Reviewer 证据清楚；
- 主控复核规则一致；
- 不依赖缺失全文；
- 不会造成 schema 迁移半成品。

## 四、Reviewer 原始输出

### B-Reviewer-1: James

状态：已返回，14 / 14 条完整覆盖。

主要结论：

- `ASD-0524`, `ASD-0525`, `ASD-0528`, `ASD-0530`: 保持独立 `01.04` general-method bucket；跨域 demo 或通用 SDL 任务不构成多模块对象覆盖。
- `ASD-0526`: 保持 `09` 工程与工业技术科学，constitutive model / mechanics object 稳定。
- `ASD-0529`, `ASD-0535`, `ASD-0538`, `ASD-0539`: 保持 `04` 材料科学；其中 `ASD-0539` 不因 electrolyte-additive 子例硬加 `03`。
- `ASD-0531`, `ASD-0536`, `ASD-0537`, `ASD-0540`: 保持 `07` 医学与健康科学；治疗/药物发现 endpoint 明确。
- `ASD-0541`: 保持 `06` 生命科学，但列为 `06 / 01.04` 平台边界全文复核。
- 本切片未发现足够强的 multi-module assignment。

### B-Reviewer-2: Kuhn

状态：已返回，14 / 14 条完整覆盖。

主要结论：

- `ASD-0553`, `ASD-0554`: 保持独立 `01.04` general-method bucket；bioinformatics / translational examples 是 workflow substrate 评测，不是具体对象发现贡献。
- `ASD-0542`, `ASD-0544`, `ASD-0545`, `ASD-0548`, `ASD-0552`, `ASD-0556`, `ASD-0564`: 保持 `07` 医学与健康科学；drug discovery、cancer biomarker、surfaceome、cancer pathology 等对象稳定。
- `ASD-0543`: 暂保持 `06`，但 reviewer 明确建议主控全文复核 `06 / 07` prognosis boundary。
- `ASD-0547`, `ASD-0558`: 保持 `04` 材料科学，metasurface / organic gain-media 是直接优化对象。
- `ASD-0549`: 保持 `02`，inflationary cosmology 是明确物理/宇宙学对象。
- `ASD-0557`: 保持 `03`，azobenzene isomerization mechanism 是化学对象。
- 本切片未发现足够强的 multi-module assignment。

### B-Reviewer-3: Copernicus

状态：已返回，14 / 14 条完整覆盖。

主要结论：

- `ASD-0565`, `ASD-0568`, `ASD-0569`, `ASD-0570`, `ASD-0571`, `ASD-0572`, `ASD-0573`, `ASD-0577`, `ASD-0581`: 保持 `04` 材料科学；其中 `ASD-0570` 是本切片最强 `01.04 / domain` 平台边界样本。
- `ASD-0567`: 保持 `02`，astrophysical equivalent-width measurement 是具体天文对象任务。
- `ASD-0574`, `ASD-0576`: 保持 `06` 生命科学；gene-set analysis 与 biosystems design 对象稳定。
- `ASD-0575`: 保持 `03`，protocell formulation / chemical behavior 是化学对象。
- `ASD-0579`: 保持 `07`，combination drug screens 是医学/药物发现对象；残余风险是 classical-agent strength。
- 本切片未发现足够强的 multi-module assignment。

### B-Reviewer-4: Erdos

状态：已返回，14 / 14 条完整覆盖。

主要结论：

- `ASD-0582`, `ASD-0590`, `ASD-0591`, `ASD-0592`, `ASD-0598`: 保持 `04` 材料科学；engineering apparatus 是执行手段，材料结构/形貌/性能是直接对象。
- `ASD-0586`, `ASD-0587`, `ASD-0589`, `ASD-0597`, `ASD-0600`: 保持 `03` 化学科学；其中 `ASD-0587` 与 `ASD-0600` 是强 `03 / 01.04` 平台边界样本。
- `ASD-0617`, `ASD-0618`, `ASD-0596`, `ASD-0599`: 保持 `06` 生命科学；protein/enzyme engineering 与 cell-free biofoundry 对象稳定。
- `ASD-0597`: 不建议转 `11.07`，因为 scientific literature verification 最终服务于 concrete chemical synthesis execution。
- 本切片未发现足够强的 multi-module assignment。

## 五、主控裁决表

Wave B 共 56 条，全部完成 Reviewer 覆盖。主控裁决如下：

| ID | Legacy filing | Reviewer suggestion | 主控裁决 | 是否改主列表 | 备注 |
|---|---|---|---|---|---|
| `ASD-0524` | `01 / 01.04` | `01.04` | 保持独立 `01.04`，列入边界复核 | 否 | SciML discovery capability / benchmark，不是单一具体科学对象 |
| `ASD-0525` | `01 / 01.04` | `01.04` | 保持独立 `01.04` | 否 | chemistry/materials demos 不足以压过通用 dual-agent framework |
| `ASD-0526` | `09 / 09.01` | `09` | 保持 `09` | 否 | constitutive model / engineering mechanics object |
| `ASD-0528` | `01 / 01.04` | `01.04` | 保持独立 `01.04`，列入全文复核 | 否 | projectile / Ising / nanophotonics 为 framework demos |
| `ASD-0529` | `04 / 04.03` | `04` | 保持 `04` | 否 | interfacial formulation / wettability optimization |
| `ASD-0530` | `01 / 01.04` | `01.04` | 保持独立 `01.04`，列入 core-strength 复核 | 否 | hierarchical AI scientist system，framework/taxonomy-heavy |
| `ASD-0531` | `07 / 07.04` | `07` | 保持 `07` | 否 | therapeutic peptide / membrane / wet-lab feedback |
| `ASD-0535` | `04 / 04.04` | `04` | 保持 `04` | 否 | inorganic crystalline materials design |
| `ASD-0536` | `07 / 07.04` | `07` | 保持 `07`，列入 core-strength 复核 | 否 | TCM / network pharmacology / herbal medicine discovery |
| `ASD-0537` | `07 / 07.04` | `07` | 保持 `07` | 否 | omics evidence serves therapeutic discovery endpoint |
| `ASD-0538` | `04 / 04.01` | `04` | 保持 `04` | 否 | materials simulation agent |
| `ASD-0539` | `04 / 04.04` | `04` | 保持 `04` | 否 | materials-discovery workflow；electrolyte additive subcase 不足以加 `03` |
| `ASD-0540` | `07 / 07.04` | `07` | 保持 `07` | 否 | dry AMD therapeutic/mechanism discovery with wet-lab validation |
| `ASD-0541` | `06 / 06.03` | `06` | 保持 `06`，列入 `06 / 01.04` 复核 | 否 | PromptBio platform pressure 较强 |
| `ASD-0542` | `07 / 07.04` | `07` | 保持 `07` | 否 | MADD drug hit identification / drug discovery |
| `ASD-0543` | `06 / 06.03` | `main_control_review` | 暂保持 `06`，列入 `06 / 07` 全文复核 | 否 | prognostic gene discovery 可能转向 clinical prognosis endpoint |
| `ASD-0544` | `07 / 07.01` | `07` | 保持 `07` | 否 | cancer biomarker discovery |
| `ASD-0545` | `07 / 07.01` | `07` | 保持 `07` | 否 | immunotherapy biomarker / surfaceome discovery |
| `ASD-0547` | `04 / 04.04` | `04` | 保持 `04`，列入 `04 / 09` 全文复核 | 否 | metasurface design object stable but evidence detail weak |
| `ASD-0548` | `07 / 07.04` | `07` | 保持 `07` | 否 | biomedical discovery cases anchor classification |
| `ASD-0549` | `02 / 02.01` | `02` | 保持 `02` | 否 | inflationary cosmology model discovery |
| `ASD-0552` | `07 / 07.04` | `07` | 保持 `07` | 否 | AD drug-combination hypotheses with in vitro validation |
| `ASD-0553` | `01 / 01.04` | `01.04` | 保持独立 `01.04`，列入边界复核 | 否 | bioinformatics automation substrate，非具体 gene/protein discovery |
| `ASD-0554` | `01 / 01.04` | `01.04` | 保持独立 `01.04`，列入边界复核 | 否 | reproducible translational-bioinformatics workflow infrastructure |
| `ASD-0556` | `07 / 07.04` | `07` | 保持 `07` | 否 | drug-discovery task library and case studies |
| `ASD-0557` | `03 / 03.02` | `03` | 保持 `03` | 否 | azobenzene isomerization mechanism / spectra |
| `ASD-0558` | `04 / 04.04` | `04` | 保持 `04` | 否 | organic gain-media / laser material |
| `ASD-0564` | `07 / 07.01` | `07` | 保持 `07` | 否 | cancer pathology concepts / biomarkers |
| `ASD-0565` | `04 / 04.04` | `04` | 保持 `04`，列入 Agent-strength 全文复核 | 否 | radiation-tolerant high-entropy alloys |
| `ASD-0567` | `02 / 02.01` | `02` | 保持 `02` | 否 | equivalent-width measurement on astrophysical spectra |
| `ASD-0568` | `04 / 04.04` | `04` | 保持 `04` | 否 | zinc-ion battery electrolyte material |
| `ASD-0569` | `04 / 04.03` | `04` | 保持 `04` | 否 | nanocrystal doping material object |
| `ASD-0570` | `04 / 04.04` | `main_control_review` | 保持 `04`，列入 `01.04 / domain` 全文复核 | 否 | MARS platform-heavy but visible validation is concrete materials |
| `ASD-0571` | `04 / 04.01` | `04` | 保持 `04` | 否 | materials crystal-structure / phase mapping |
| `ASD-0572` | `04 / 04.03` | `04` | 保持 `04` | 否 | polymer blend formulation；protein stabilization is assay objective |
| `ASD-0573` | `04 / 04.03` | `04` | 保持 `04` | 否 | lead-free perovskite nanocrystals / PLQY |
| `ASD-0574` | `06 / 06.03` | `06` | 保持 `06` | 否 | gene-set biological function / pathway knowledge |
| `ASD-0575` | `03 / 03.04` | `03` | 保持 `03` | 否 | protocell formulation / chemical behavior |
| `ASD-0576` | `06 / 06.03` | `06` | 保持 `06` | 否 | lycopene biosynthetic pathway / biosystems design |
| `ASD-0577` | `04 / 04.04` | `04` | 保持 `04` | 否 | perovskite nanocrystal materials optimization |
| `ASD-0579` | `07 / 07.04` | `07` | 保持 `07` | 否 | combination drug screens；classical-agent strength 留意 |
| `ASD-0581` | `04 / 04.03` | `04` | 保持 `04` | 否 | nanoparticle morphology/size/spectra optimization |
| `ASD-0582` | `04 / 04.04` | `04` | 保持 `04` | 否 | electronic polymer thin-film processing / properties |
| `ASD-0586` | `03 / 03.03` | `03` | 保持 `03` | 否 | organic / enzymatic synthesis route planning |
| `ASD-0587` | `03 / 03.03` | `03` | 保持 `03`，列入 `03 / 01.04` 全文复核 | 否 | collective-intelligence chemical synthesis platform |
| `ASD-0589` | `03 / 03.03` | `03` | 保持 `03` | 否 | self-optimizing chemical reaction engine |
| `ASD-0590` | `04 / 04.03` | `04` | 保持 `04` | 否 | colloidal nanocrystal synthesis / morphology-property control |
| `ASD-0591` | `04 / 04.03` | `04` | 保持 `04` | 否 | quantum-dot / nanoparticle material quality |
| `ASD-0592` | `04 / 04.04` | `04` | 保持 `04` | 否 | Nb-doped TiO2 thin-film property optimization |
| `ASD-0617` | `06 / 06.03` | `06` | 保持 `06`，列入全文补强 | 否 | programmable protein evolution |
| `ASD-0618` | `06 / 06.03` | `06` | 保持 `06` | 否 | protein evolution with automatic biofoundry |
| `ASD-0596` | `06 / 06.03` | `06` | 保持 `06`，列入 Agent-strength 全文复核 | 否 | cell-free protein synthesis / biofoundry operation |
| `ASD-0597` | `03 / 03.03` | `03` | 保持 `03` | 否 | chemical literature verification leads to chemical synthesis execution, not `11.07` |
| `ASD-0598` | `04 / 04.04` | `04` | 保持 `04` | 否 | nano / advanced materials synthesis |
| `ASD-0599` | `06 / 06.03` | `06` | 保持 `06`，列入全文补强 | 否 | enzyme / polymerase engineering |
| `ASD-0600` | `03 / 03.03` | `03` | 保持 `03`，列入 `03 / 01.04` 全文复核 | 否 | universal chemputation system，但 demos 是 concrete chemical syntheses |

## 六、Wave B 口径校准结论

基于 56 条完整结果，本轮形成以下校准结论：

1. Batch 2 / Wave B 未发现高置信 multi-module assignment。跨工具、跨数据源、跨实验平台、跨材料家族不等于跨一级科学对象模块。
2. `01.04` 独立 bucket 的边界进一步稳定：`ASD-0524`, `ASD-0525`, `ASD-0528`, `ASD-0530`, `ASD-0553`, `ASD-0554` 均因缺少具体对象层科学贡献而保留 `01.04`。
3. “平台外观不等于 `01.04`”同样被反向验证：`ASD-0540`, `ASD-0570`, `ASD-0587`, `ASD-0600` 等虽平台感很强，但只要对象实验明确，暂按对应领域保留。
4. `03 / 04` 边界继续按最终对象判定。合成路线、反应机制、chemical synthesis execution 归 `03`；纳米晶、薄膜、聚合物、电解质、合金、metasurface 等材料结构/性能对象归 `04`。
5. `06 / 07` 边界继续按 endpoint 判定。Gene/protein/enzyme/biosystems/biofoundry 归 `06`；drug discovery、therapeutic discovery、cancer biomarker、cancer pathology、clinical/biomarker endpoint 归 `07`。
6. `11.07` 不能泛化为所有“处理科学文献”的论文入口。`ASD-0597` 与 `ASD-0600` 的 scientific literature digitization / verification 最终对象是 chemical synthesis execution，因此暂不转 `11.07`。
7. 当前没有足够证据支持重构一级分类。问题主要集中在 `01.04` bucket、平台型对象论文和 Agent-strength 复核，而不是 `01-11` 顶层 taxonomy 失稳。

## 七、待主控复核队列

Wave B 暂列以下记录为主控复核或后续全文复核：

| ID | 当前 legacy | 初步问题 | 暂定处理 |
|---|---|---|---|
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
| records with `full_text_required=yes` from Reviewer output | 11 |

本轮不修改 `agent_master_paper_list.md`。主列表 record-level confirmed count 仍为 `451`，`needs_review` 仍为 `0`，confirmed `08` 仍为 `3`。
