# Batch 3 / Wave B 多模块重分类审计报告

> 日期：2026-06-20  
> 范围：`agent_master_paper_list.md` confirmed 记录序号 284-339。  
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

## 二、Wave B 分工

本轮按当前主列表 confirmed 记录出现顺序抽取序号 284-339。注意：计划表中的 ID 边界只表示 confirmed 顺序范围，不保证连续编号；本报告使用当前主列表解析得到的精确 ID 切片。

| Reviewer | Agent | 记录数 | 分配 ID |
|---|---|---:|---|
| B-Reviewer-1 | Avicenna | 14 | `ASD-0674`, `ASD-0675`, `ASD-0676`, `ASD-0677`, `ASD-0678`, `ASD-0679`, `ASD-0680`, `ASD-0681`, `ASD-0682`, `ASD-0683`, `ASD-0684`, `ASD-0687`, `ASD-0688`, `ASD-0691` |
| B-Reviewer-2 | Galileo | 14 | `ASD-0693`, `ASD-0695`, `ASD-0696`, `ASD-0697`, `ASD-0698`, `ASD-0699`, `ASD-0700`, `ASD-0701`, `ASD-0702`, `ASD-0703`, `ASD-0704`, `ASD-0705`, `ASD-0706`, `ASD-0707` |
| B-Reviewer-3 | Archimedes | 14 | `ASD-0708`, `ASD-0709`, `ASD-0710`, `ASD-0711`, `ASD-0712`, `ASD-0713`, `ASD-0714`, `ASD-0715`, `ASD-0716`, `ASD-0717`, `ASD-0719`, `ASD-0721`, `ASD-0722`, `ASD-0723` |
| B-Reviewer-4 | Cicero | 14 | `ASD-0724`, `ASD-0725`, `ASD-0726`, `ASD-0727`, `ASD-0728`, `ASD-0729`, `ASD-0731`, `ASD-0733`, `ASD-0734`, `ASD-0735`, `ASD-0736`, `ASD-0737`, `ASD-0738`, `ASD-0739` |

## 三、主控合并口径

本轮沿用 Batch 1、Batch 2 与 Batch 3 / Wave A 校准后的口径：

- 分类依据是实际研究和实验覆盖的科学对象，不是 Agent 技术、平台名称、venue 或自称通用性。
- 有具体科学对象实验的论文，优先进入对应 `01-11` 对象模块，而不是回收到 `01.04`。
- 只有多个具体科学对象各自有实质实验或结果贡献时，才建议 multi-module。
- 没有任何具体科学对象实验、只提出 ASD / general research-agent 方法或通用 benchmark 的论文，进入独立 `01.04` bucket。
- `05 / 10` 边界继续按自然地球环境对象 vs 航天/任务/载具对象判断。
- `11.07 / 01.04` 边界继续按 scientific knowledge production itself vs general research-agent workflow 判断。
- `06 / 07` 继续按 biological mechanism / protein / omics vs disease / therapeutic / clinical endpoint 判断。

默认不直接改主列表，除非同时满足：

- Reviewer 证据清楚；
- 主控复核规则一致；
- 不依赖缺失全文；
- 不会造成 schema 迁移半成品。

## 四、Reviewer 原始输出

### B-Reviewer-1: Avicenna

状态：已返回，14 / 14 条完整覆盖。

主要结论：

- `ASD-0674` 保持 `04`，biomedical tubing 是应用场景，稳定对象仍是 cross-domain materials design，不加 `07`。
- `ASD-0675`, `ASD-0677`, `ASD-0678`, `ASD-0679` 保持 `07`，drug molecule / therapeutic reasoning / drug discovery endpoint 主导。
- `ASD-0676` 保持独立 `01.04`，AutoSci 是 general full-lifecycle research-agent system。
- `ASD-0680`, `ASD-0681`, `ASD-0682`, `ASD-0683` 保持 `04`，superconductor、lithium halide spinel、solid-state simulation、perovskite materials 对象稳定。
- `ASD-0684` 保持 `03`，organic photocatalyst design rules 是化学对象。
- `ASD-0687` 保持 `02`，particle accelerator physics experiment 对象稳定。
- `ASD-0688` 保持 `09`，computational fluid dynamics automation 是工程仿真对象。
- `ASD-0691` 保持 `10`，rover onboard science autonomy 属航天任务科学对象。
- 本切片未发现足够强的 multi-module assignment。

### B-Reviewer-2: Galileo

状态：已返回，14 / 14 条完整覆盖。

主要结论：

- `ASD-0693`, `ASD-0696`, `ASD-0697`, `ASD-0702`, `ASD-0703` 保持 `10`，Europa spacecraft、Mars rover、EO-1 / sensor-web autonomy 属 mission-science / spacecraft operation 对象。
- `ASD-0695` 保持 `08.05`，flavor scientist / food object 支持食品科学低覆盖类。
- `ASD-0698`, `ASD-0699`, `ASD-0700`, `ASD-0701`, `ASD-0704`, `ASD-0705`, `ASD-0706` 保持 `11.07`，paper revision、peer review、reproducibility、AI-generated scientific publishing ecosystem 都是 scientific knowledge production itself。
- `ASD-0707` 保持 `02.02`，fundamental physics from quarks to cosmos 是物理对象；framework-heavy 但不退回 `01.04`。
- 本切片未发现足够强的 multi-module assignment。

### B-Reviewer-3: Archimedes

状态：已返回，14 / 14 条完整覆盖。

主要结论：

- `ASD-0708`, `ASD-0714`, `ASD-0723` 保持 `06`，gene expression analysis、scientific analysis over biological data、cell annotation 是生命科学对象。
- `ASD-0715`, `ASD-0716` 保持 `07`，biomedical hypothesis / CAR-T therapy development 有治疗或医学 endpoint。
- `ASD-0709`, `ASD-0710`, `ASD-0711`, `ASD-0712`, `ASD-0713`, `ASD-0719`, `ASD-0721`, `ASD-0722` 保持 `10`，Mars rover、Europa lander、EO-1、Earth-observing sensorweb 的主对象是航天任务/载具自主科学。
- `ASD-0717` 保持 `11.07`，research discovery and analysis framework 主要面向科学知识生产流程。
- 本切片未发现足够强的 multi-module assignment。

### B-Reviewer-4: Cicero

状态：已返回，14 / 14 条完整覆盖。

主要结论：

- `ASD-0724`, `ASD-0728`, `ASD-0729`, `ASD-0731` 保持 `06`，coral reef biodiversity、virtual cell model、protein discovery、biomedical knowledge extraction 均为生命科学/生物医学知识对象，暂不加其他模块。
- `ASD-0725`, `ASD-0726`, `ASD-0727` 保持 `05`，atmospheric environmental research、climate data science、geospatial reasoning 是地球与环境对象。
- `ASD-0733` 保持 `10`，Mars rover planning / scheduling / execution 是航天任务对象。
- `ASD-0734` 保持 `03`，organic synthesis robot searches new reactivity。
- `ASD-0735`, `ASD-0739` 保持 `04`，quantum dot synthesis 与 double perovskite nanoplatelets 是材料对象。
- `ASD-0736`, `ASD-0737` 保持独立 `01.04`，general research-agent systems；chain-of-evidence / review 组件不足以转 `11.07`。
- `ASD-0738` 保持 formal `01.02`，AI model discovery / AutoSOTA 的对象是计算系统能力，不是 general `01.04`。
- 本切片未发现足够强的 multi-module assignment。

## 五、主控裁决表

Wave B 共 56 条，全部完成 Reviewer 覆盖。主控裁决如下：

| ID | Legacy filing | Reviewer suggestion | 主控裁决 | 是否改主列表 | 备注 |
|---|---|---|---|---|---|
| `ASD-0674` | `04 / 04.04` | `04` | 保持 `04` | 否 | materials design object；biomedical tubing 不是医学 endpoint |
| `ASD-0675` | `07 / 07.04` | `07` | 保持 `07` | 否 | drug molecule evaluation / screening / optimization |
| `ASD-0676` | `01 / 01.04` | `01.04` | 保持独立 `01.04`，列入全文补强 | 否 | memory-centric full-lifecycle general research-agent system |
| `ASD-0677` | `07 / 07.04` | `07` | 保持 `07` | 否 | therapeutic reasoning over historical medical texts |
| `ASD-0678` | `07 / 07.04` | `07` | 保持 `07` | 否 | lab-validated de novo drug design |
| `ASD-0679` | `07 / 07.04` | `07` | 保持 `07` | 否 | small molecule drug discovery operating system |
| `ASD-0680` | `04 / 04.04` | `04` | 保持 `04` | 否 | superconductor discovery |
| `ASD-0681` | `04 / 04.04` | `04` | 保持 `04` | 否 | lithium halide spinel conductors |
| `ASD-0682` | `04 / 04.01` | `04` | 保持 `04`，列入全文补强 | 否 | solid-state simulations；平台感强但对象是固体材料 |
| `ASD-0683` | `04 / 04.04` | `04` | 保持 `04` | 否 | perovskite material discovery |
| `ASD-0684` | `03 / 03.04` | `03` | 保持 `03` | 否 | organic photocatalyst design rules |
| `ASD-0687` | `02 / 02.02` | `02` | 保持 `02` | 否 | particle accelerator physics experiment |
| `ASD-0688` | `09 / 09.01` | `09` | 保持 `09` | 否 | computational fluid dynamics engineering simulation |
| `ASD-0691` | `10 / 10.02` | `10` | 保持 `10` | 否 | onboard rover science autonomy |
| `ASD-0693` | `10 / 10.02` | `10` | 保持 `10` | 否 | Europa Clipper spacecraft onboard event detection |
| `ASD-0695` | `08 / 08.05` | `08` | 保持 `08`，列入全文补强 | 否 | flavor scientist / food science low-coverage boundary |
| `ASD-0696` | `10 / 10.02` | `10` | 保持 `10` | 否 | MER Opportunity rover automated science targeting |
| `ASD-0697` | `10 / 10.02` | `10` | 保持 `10` | 否 | ChemCam / Mars Science Laboratory autonomous targeting |
| `ASD-0698` | `11 / 11.07` | `11.07` | 保持 `11.07`，列入全文补强 | 否 | paper revision and evaluation system |
| `ASD-0699` | `11 / 11.07` | `11.07` | 保持 `11.07`，列入全文补强 | 否 | reproducibility assessment for peer review |
| `ASD-0700` | `11 / 11.07` | `11.07` | 保持 `11.07`，列入全文补强 | 否 | peer review process / mechanism design |
| `ASD-0701` | `11 / 11.07` | `11.07` | 保持 `11.07`，列入全文补强 | 否 | computational reproducibility in social science |
| `ASD-0702` | `10 / 10.02` | `10` | 保持 `10` | 否 | rover-based autonomous science |
| `ASD-0703` | `10 / 10.02` | `10` | 保持 `10` | 否 | autonomous science agents and sensor webs |
| `ASD-0704` | `11 / 11.07` | `11.07` | 保持 `11.07` | 否 | reproducibility assessment for social science papers |
| `ASD-0705` | `11 / 11.07` | `11.07` | 保持 `11.07`，列入全文补强 | 否 | reproducibility assessments in social and behavioral sciences |
| `ASD-0706` | `11 / 11.07` | `11.07` | 保持 `11.07`，列入全文补强 | 否 | open-access ecosystem / AI-generated scientific discovery |
| `ASD-0707` | `02 / 02.02` | `02` | 保持 `02`，列入全文补强 | 否 | fundamental physics from quarks to cosmos |
| `ASD-0708` | `06 / 06.03` | `06` | 保持 `06` | 否 | gene expression analysis |
| `ASD-0709` | `10 / 10.02` | `10` | 保持 `10` | 否 | MSL rover ChemCam targeting |
| `ASD-0710` | `10 / 10.02` | `10` | 保持 `10` | 否 | Mars 2020 SuperCam autonomous targeting |
| `ASD-0711` | `10 / 10.02` | `10` | 保持 `10` | 否 | MSL rover mission autonomous science technology |
| `ASD-0712` | `10 / 10.02` | `10` | 保持 `10` | 否 | rover dynamic planning and scheduling |
| `ASD-0713` | `10 / 10.02` | `10` | 保持 `10` | 否 | Europa Lander mission autonomy prototype |
| `ASD-0714` | `06 / 06.03` | `06` | 保持 `06`，列入全文补强 | 否 | automated scientific analysis over biological data |
| `ASD-0715` | `07 / 07.04` | `07` | 保持 `07`，列入全文补强 | 否 | biomedical hypothesis generation with temporal evaluation |
| `ASD-0716` | `07 / 07.04` | `07` | 保持 `07` | 否 | CAR-T therapy development |
| `ASD-0717` | `11 / 11.07` | `11.07` | 保持 `11.07`，列入全文补强 | 否 | research discovery and analysis framework |
| `ASD-0719` | `10 / 10.02` | `10` | 保持 `10` | 否 | Earth Observing-1 onboard autonomy |
| `ASD-0721` | `10 / 10.02` | `10` | 保持 `10` | 否 | Autonomous Sciencecraft on Earth Observing One |
| `ASD-0722` | `10 / 10.02` | `10` | 保持 `10`，列入全文补强 | 否 | autonomous Earth-observing sensorweb；`05 / 10` 边界 |
| `ASD-0723` | `06 / 06.03` | `06` | 保持 `06` | 否 | automated and interpretable cell annotation |
| `ASD-0724` | `06 / 06.02` | `06` | 保持 `06` | 否 | coral reef biodiversity hotspots |
| `ASD-0725` | `05 / 05.02` | `05` | 保持 `05`，列入全文补强 | 否 | atmospheric environmental research |
| `ASD-0726` | `05 / 05.02` | `05` | 保持 `05`，列入全文补强 | 否 | climate data science |
| `ASD-0727` | `05 / 05.04` | `05` | 保持 `05`，列入全文补强 | 否 | autonomous geospatial reasoning |
| `ASD-0728` | `06 / 06.01` | `06` | 保持 `06`，列入全文补强 | 否 | virtual cell models |
| `ASD-0729` | `06 / 06.03` | `06` | 保持 `06`，列入全文补强 | 否 | protein discovery and directed evolution |
| `ASD-0731` | `06 / 06.03` | `06` | 保持 `06`，列入全文补强 | 否 | biomedical knowledge at scale；`06 / 07` 边界 |
| `ASD-0733` | `10 / 10.02` | `10` | 保持 `10` | 否 | Mars rover planning, scheduling and execution |
| `ASD-0734` | `03 / 03.03` | `03` | 保持 `03` | 否 | organic synthesis robot / new reactivity |
| `ASD-0735` | `04 / 04.03` | `04` | 保持 `04` | 否 | quantum dot synthesis |
| `ASD-0736` | `01 / 01.04` | `01.04` | 保持独立 `01.04`，列入全文补强 | 否 | autonomous scientific innovation system |
| `ASD-0737` | `01 / 01.04` | `01.04` | 保持独立 `01.04`，列入全文补强 | 否 | chain-of-evidence general research system |
| `ASD-0738` | `01 / 01.02` | `01` | 保持 `01.02`，列入全文补强 | 否 | AI model discovery object；not general `01.04` |
| `ASD-0739` | `04 / 04.04` | `04` | 保持 `04` | 否 | double perovskite nanoplatelets |

## 六、Wave B 口径校准结论

基于 56 条完整结果，本轮形成以下校准结论：

1. Batch 3 / Wave B 未发现高置信 multi-module assignment。跨平台、跨任务链、跨示例或应用场景并不自动构成多科学对象模块。
2. `01.04` 的使用继续收窄到 general ASD / general research-agent system。`ASD-0676`, `ASD-0736`, `ASD-0737` 保持独立 `01.04`；`ASD-0738` 则因对象是 AI model discovery 保持 `01.02`。
3. 平台感强但对象实验明确时，不退回 `01.04`。`ASD-0682`, `ASD-0707`, `ASD-0725`, `ASD-0726`, `ASD-0727` 都按具体对象模块保留。
4. `05 / 10` 边界继续稳定：Mars rover、Europa spacecraft、EO-1、Earth-observing sensorweb 的主对象是航天/载具/任务自主科学，归 `10`；atmospheric、climate、geospatial reasoning 归 `05`。
5. `11.07 / 01.04` 边界继续按对象判定。paper revision、peer review、reproducibility、scientific publishing ecosystem 属 scientific knowledge production itself，归 `11.07`。
6. `06 / 07` 边界继续按生命机制/生物对象 vs 疾病/治疗 endpoint 判定。gene expression、cell annotation、protein discovery 保持 `06`；drug discovery、therapeutic reasoning、CAR-T therapy 保持 `07`。
7. `08` 仍不为平衡数量而放宽。`ASD-0695` 保持 `08.05` 是因为对象为 flavor / food science，而不是为了补足低覆盖类。
8. 当前没有足够证据支持重构一级分类，问题主要集中在边界解释与低覆盖类稀缺性判断。

## 七、待主控复核队列

Wave B 暂列以下记录为主控复核或后续全文复核：

| ID | 当前 legacy | 初步问题 | 暂定处理 |
|---|---|---|---|
| `ASD-0676` | `01 / 01.04` | AutoSci 是否有足够具体对象实验，或只是 full-lifecycle general research-agent system | 暂保持 `01.04` |
| `ASD-0682` | `04 / 04.01` | El Agente Sólido 的平台性与 solid-state 对象贡献强弱 | 暂保持 `04` |
| `ASD-0695` | `08 / 08.05` | flavor scientist 的食品科学对象证据与低覆盖 `08` 压力 | 暂保持 `08` |
| `ASD-0698` | `11 / 11.07` | APRES 是否属于 scientific knowledge production core 或偏工具化 | 暂保持 `11.07` |
| `ASD-0699` | `11 / 11.07` | reproducibility assessment / peer-review support 的 Agent 强度 | 暂保持 `11.07` |
| `ASD-0700` | `11 / 11.07` | peer-review mechanism design 的实证与 Agent role 强度 | 暂保持 `11.07` |
| `ASD-0701` | `11 / 11.07` | social-science reproducibility 与一般 social science 方法边界 | 暂保持 `11.07` |
| `ASD-0705` | `11 / 11.07` | LLM reproducibility assessment 是否满足 Agent 最低标准 | 暂保持 `11.07` |
| `ASD-0706` | `11 / 11.07` | aiXiv ecosystem 是否更像 knowledge-production system 或 general ASD platform | 暂保持 `11.07` |
| `ASD-0707` | `02 / 02.02` | ArgoLOOM framework-heavy physics object evidence | 暂保持 `02` |
| `ASD-0714` | `06 / 06.03` | K-Dense Analyst 的 biological object evidence 与 general analysis workflow 边界 | 暂保持 `06` |
| `ASD-0715` | `07 / 07.04` | BioDisco 的 therapeutic / biomedical endpoint 与生命科学机制边界 | 暂保持 `07` |
| `ASD-0717` | `11 / 11.07` | Paper Circle 是否是 scientific knowledge production object 或 general research framework | 暂保持 `11.07` |
| `ASD-0722` | `10 / 10.02` | Earth-observing sensorweb 的 `05 / 10` 归属与 scientific object weight | 暂保持 `10` |
| `ASD-0725` | `05 / 05.02` | atmospheric environmental research 的具体对象实验与平台强度 | 暂保持 `05` |
| `ASD-0726` | `05 / 05.02` | Climate Data Science Agentic AI 的对象贡献强度 | 暂保持 `05` |
| `ASD-0727` | `05 / 05.04` | GeoAgentic-RAG 的 geospatial reasoning 是否足够对象层 | 暂保持 `05` |
| `ASD-0728` | `06 / 06.01` | virtual cell model 的生命科学对象贡献与 framework-heavy 风险 | 暂保持 `06` |
| `ASD-0729` | `06 / 06.03` | protein discovery / directed evolution 的实验或结果证据 | 暂保持 `06` |
| `ASD-0731` | `06 / 06.03` | biomedical knowledge extraction 的 `06 / 07 / 11.07` 边界 | 暂保持 `06` |
| `ASD-0736` | `01 / 01.04` | AI-Researcher 是否有具体对象实验，或仅 general scientific innovation | 暂保持 `01.04` |
| `ASD-0737` | `01 / 01.04` | ScientistOne 的 evidence verification 是否转 `11.07` 或保持 general ASD | 暂保持 `01.04` |
| `ASD-0738` | `01 / 01.02` | AutoSOTA 的 AI model discovery 是否仍稳定为 formal/computational object | 暂保持 `01.02` |

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
| main-control / full-text follow-up queue | 23 |
| records with `full_text_required=yes` from Reviewer output | 23 |

本轮不修改 `agent_master_paper_list.md`。主列表 record-level confirmed count 仍为 `451`，`needs_review` 仍为 `0`，confirmed `08` 仍为 `3`。
