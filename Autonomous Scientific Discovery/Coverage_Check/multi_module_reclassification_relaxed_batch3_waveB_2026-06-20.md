# Batch 3 / Wave B relaxed multi-module reclassification audit

> 日期：2026-06-20  
> 范围：`ASD-0674` 到 `ASD-0739` 中当前 confirmed / `to_read` 的 Batch 3 / Wave B 记录。  
> 口径：Notes 只作为定位线索；分类决策优先参考 arXiv / DOI / publisher page / PDF / project page 等一手或权威来源。  
> 主列表说明：本轮仍不直接覆盖 legacy `Main class` / `Secondary class` 字段；high-confidence 事实写入 Notes、审计报告和 `Remarks`。

## 1. 执行概况

| 指标 | 数量 |
|---|---:|
| 本 wave 计划复核 confirmed records | 56 |
| high-confidence relaxed classification changes merged | 15 |
| high-confidence stable / unchanged records | 34 |
| medium / full-text-required queue | 7 |
| 本轮同步更新 Notes | 15 |
| 本轮同步更新主列表 Remarks | 15 |
| 本轮直接修改 legacy `Main class` / `Secondary class` | 0 |

主控合并原则：

- 合并对象必须是 `to_read` confirmed 记录，且有一手来源或权威摘要支撑。
- `background_only` 记录即使有对象覆盖证据，也不计入本轮 confirmed module assignment count；只进入背景或状态复核队列。
- 对 JPL / EO-1 / AEGIS / Europa 等 mission-science 记录，本轮采用 relaxed object-coverage rule：如果原文明确做了 Earth / planetary science event、geology target、geochemical observation 或 planetary environment detection，则在保留 `10` mission autonomy filing 的同时新增 `05`。

## 2. High-confidence 变更

| ID | legacy filing | relaxed modules | primary filing | 主控裁决 |
|---|---|---|---|---|
| `ASD-0693` | `10 / 10.02` | `05;10` | `10` | Europa thermal / compositional / plume event detection 支持 `05`，spacecraft onboard prioritization 支持 `10`。 |
| `ASD-0696` | `10 / 10.02` | `05;10` | `10` | Mars rocks / outcrops / geologic target selection 支持 `05`，rover targeting 支持 `10`。 |
| `ASD-0697` | `10 / 10.02` | `05;10` | `10` | Mars geological materials and ChemCam geochemistry 支持 `05`，rover instrument autonomy 支持 `10`。 |
| `ASD-0702` | `10 / 10.02` | `05;10` | `10` | planetary surface / geologic science features 支持 `05`，rover autonomous science 支持 `10`。 |
| `ASD-0703` | `10 / 10.02` | `05;10` | `10` | Earth science events 支持 `05`，EO-1 / sensor-web autonomy 支持 `10`。 |
| `ASD-0709` | `10 / 10.02` | `05;10` | `10` | Mars rocks / soil / geologic ChemCam surveying 支持 `05`，rover targeting 支持 `10`。 |
| `ASD-0710` | `10 / 10.02` | `05;10` | `10` | Mars SuperCam geological / geochemical targets 支持 `05`，Perseverance instrument autonomy 支持 `10`。 |
| `ASD-0711` | `10 / 10.02` | `05;10` | `10` | MSL rocks / soil / veins / concretions 支持 `05`，autonomous rover science technology 支持 `10`。 |
| `ASD-0719` | `10 / 10.02` | `05;10` | `10` | EO-1 Earth events including land, ice, snow, water, flooding, lava flows 支持 `05`，onboard autonomy 支持 `10`。 |
| `ASD-0721` | `10 / 10.02` | `05;10` | `10` | volcanic activity / flooding / cryosphere events 支持 `05`，integrated spacecraft AI 支持 `10`。 |
| `ASD-0722` | `10 / 10.02` | `05;10` | `05` | autonomous Earth-observing sensorweb 最强对象是 Earth science phenomena；保留 `10` 作为 mission autonomy coverage。 |
| `ASD-0731` | `06 / 06.03` | `03;06;07` | `06` | chemical reactions 支持 `03`，gene-disease / protein localization 支持 `06`，BBB / oral bioavailability / LD50 支持 `07`。 |
| `ASD-0736` | `01 / 01.04` | `01` | `01` | Scientist-Bench / AI research-domain experiments 使其成为 concrete formal-computational research object，不再属于 independent `01.04`。 |
| `ASD-0737` | `01 / 01.04` | `01` | `01` | AI / computational research tasks and chain-of-evidence audits 支持 `01`；medical imaging / 3D perception extra modules 仍进 full-text queue。 |
| `ASD-0739` | `04 / 04.03` | `03;04` | `04` | double perovskite nanoplatelet materials 支持 `04`，reaction inference / mechanistic chemistry 支持 `03`。 |

## 3. 已同步修订 Notes

本轮已向以下 15 个 note 追加 `2026-06-20 relaxed multi-module revision` 段：

| ID | Note path |
|---|---|
| `ASD-0693` | `Notes/10_Aerospace_Marine_and_Transportation_Sciences/Wagstaff_2019_Europa_Clipper_Onboard_Detection.md` |
| `ASD-0696` | `Notes/10_Aerospace_Marine_and_Transportation_Sciences/Estlin_2012_AEGIS_Opportunity_Rover.md` |
| `ASD-0697` | `Notes/10_Aerospace_Marine_and_Transportation_Sciences/Francis_2017_AEGIS_ChemCam_MSL.md` |
| `ASD-0702` | `Notes/10_Aerospace_Marine_and_Transportation_Sciences/Gallant_2013_Rover_Autonomous_Science.md` |
| `ASD-0703` | `Notes/10_Aerospace_Marine_and_Transportation_Sciences/Sherwood_2006_EO1_Autonomous_Science_Agents.md` |
| `ASD-0709` | `Notes/10_Aerospace_Marine_and_Transportation_Sciences/Estlin_2014_ChemCam_Automated_Targeting.md` |
| `ASD-0710` | `Notes/10_Aerospace_Marine_and_Transportation_Sciences/Francis_2024_AEGIS_SuperCam.md` |
| `ASD-0711` | `Notes/10_Aerospace_Marine_and_Transportation_Sciences/Estlin_2015_Autonomous_Science_Technology_MSL.md` |
| `ASD-0719` | `Notes/10_Aerospace_Marine_and_Transportation_Sciences/Rabideau_2006_EO1_Mission_Operations_Onboard_Autonomy.md` |
| `ASD-0721` | `Notes/10_Aerospace_Marine_and_Transportation_Sciences/Chien_2006_Integrated_AI_in_Space_EO1.md` |
| `ASD-0722` | `Notes/10_Aerospace_Marine_and_Transportation_Sciences/Chien_2005_Autonomous_Earth_Observing_Sensorweb.md` |
| `ASD-0731` | `Notes/06_Life_Sciences/Jones_2026_Self_Driving_Datasets.md` |
| `ASD-0736` | `Notes/01_Formal_Information_and_Computational_Sciences/Wang_2025_AI_Researcher.md` |
| `ASD-0737` | `Notes/01_Formal_Information_and_Computational_Sciences/Unknown_2026_ScientistOne.md` |
| `ASD-0739` | `Notes/04_Materials_Science/Sharma_2026_Double_Perovskite_Nanoplatelets.md` |

## 4. Medium / full-text 队列

| ID | 队列原因 |
|---|---|
| `ASD-0676` | AutoSci 仍保留 independent `01.04`；需 full text 确认是否有 concrete scientific-object case studies。 |
| `ASD-0682` | El Agente Solido 保持 `04`，但 solid-state case 深度需 full text。 |
| `ASD-0694` | background_only；可能 `05;10`，但需 full text 和 metadata correction 后再决定是否提升。 |
| `ASD-0700` | 保持 `11.07`，但 confirmed-core strength 偏弱，需 full-text / status 复核。 |
| `ASD-0712` | 可能添加 `05`，但 Mars Yard / rover science scenario 对象证据不够。 |
| `ASD-0713` | Europa lander mission autonomy 可能触发 `05` 或 `06`，需要 scenario 级证据。 |
| `ASD-0715` | BioDisco 保持 `07`，但是否新增 `06` 需 full text 判断生物机制覆盖。 |
| `ASD-0718` | background_only status boundary；若后续提升为 core，应保持 `11.07` 并补 note。 |
| `ASD-0720` | background_only；Earth science event evidence 支持 `05;10`，但不计入 confirmed overlay。 |
| `ASD-0732` | background_only；EO-1 lineage record 可能 `05;10`，但不计入本轮 confirmed overlay。 |
| `ASD-0737` | 已迁出 `01.04` 到 `01`；medical imaging / 3D perception 是否额外触发 `07` / `09` 需 full text。 |

## 5. 主列表统计更新

本轮 accepted changes 对 partial overlay 的影响：

- `05`: +11
- `03`: +2
- `07`: +1
- independent `01.04` bucket: -2

更新后的 partial overlay：

| Scientific object module | Expanded assignment count |
|---|---:|
| `01` | 46 |
| `02` | 29 |
| `03` | 66 |
| `04` | 98 |
| `05` | 34 |
| `06` | 61 |
| `07` | 59 |
| `08` | 3 |
| `09` | 35 |
| `10` | 23 |
| `11` | 31 |

| Relaxed-counting metric | Count |
|---|---:|
| Record-level confirmed included-and-classified count | 451 |
| Expanded module assignment count | 485 |
| Independent `01.04` general-method bucket count after accepted relaxed migrations | 38 |

## 6. 主控结论

Batch 3 / Wave B 的核心口径校准是：mission autonomy 和 scientific object coverage 可以并存。过去为了避免把 spacecraft / rover / sensorweb 误写成地球科学或行星科学，我们把很多 JPL lineage records 稳定放在 `10`；本轮 relaxed rule 下，只要原文明确报告 Earth science events、planetary geology targets、geochemical observations 或 planetary-environment event detection，就应在不覆盖 `10` 的前提下新增 `05`。同时，AI-research automation records 若已有 concrete AI research benchmark / experiment，不再留在 independent `01.04`。

