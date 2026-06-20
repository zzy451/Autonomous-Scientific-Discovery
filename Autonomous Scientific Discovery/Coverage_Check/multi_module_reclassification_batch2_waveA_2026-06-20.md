# Batch 2 / Wave A 多模块重分类审计报告

> 日期：2026-06-20  
> 范围：`agent_master_paper_list.md` confirmed 记录序号 114-170。  
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

## 二、Wave A 分工

| Reviewer | Agent | 记录数 | 分配 ID |
|---|---|---:|---|
| A-Reviewer-1 | Banach | 15 | `ASD-0155`, `ASD-0156`, `ASD-0158`, `ASD-0179`, `ASD-0186`, `ASD-0189`, `ASD-0254`, `ASD-0276`, `ASD-0280`, `ASD-0290`, `ASD-0333`, `ASD-0357`, `ASD-0370`, `ASD-0379`, `ASD-0381` |
| A-Reviewer-2 | Pauli | 14 | `ASD-0385`, `ASD-0388`, `ASD-0389`, `ASD-0390`, `ASD-0410`, `ASD-0415`, `ASD-0417`, `ASD-0418`, `ASD-0421`, `ASD-0422`, `ASD-0425`, `ASD-0428`, `ASD-0429`, `ASD-0447` |
| A-Reviewer-3 | Halley | 14 | `ASD-0455`, `ASD-0463`, `ASD-0466`, `ASD-0478`, `ASD-0484`, `ASD-0487`, `ASD-0491`, `ASD-0501`, `ASD-0503`, `ASD-0504`, `ASD-0505`, `ASD-0506`, `ASD-0507`, `ASD-0508` |
| A-Reviewer-4 | Feynman | 14 | `ASD-0510`, `ASD-0511`, `ASD-0512`, `ASD-0513`, `ASD-0514`, `ASD-0515`, `ASD-0516`, `ASD-0517`, `ASD-0518`, `ASD-0519`, `ASD-0520`, `ASD-0521`, `ASD-0522`, `ASD-0523` |

## 三、主控合并口径

本轮沿用 Batch 1 校准后的口径：

- 分类依据是实际研究和实验覆盖的科学对象，不是 Agent 技术、平台名称、venue 或自称通用性。
- 只要有具体科学对象实验，优先进入对应 `01-11` 对象模块，而不是回收到 `01.04`。
- 只有多个具体科学对象各自有实质实验或结果贡献时，才建议 multi-module。
- 没有任何具体科学对象实验、只提出 ASD / general research-agent 方法或通用 benchmark 的论文，进入独立 `01.04` bucket。
- drug discovery / target-protein / therapeutic candidate 目标优先 `07`；omics、single-cell、gene editing、protein design 通常保持 `06`。
- 分子、反应、合成、催化、量子化学通常归 `03`；材料组成、结构、性能、器件材料、MOF、metamaterial、alloy 通常归 `04`。
- scientific reproducibility / knowledge production / scientific hypothesis generation 与 `01.04` 的边界需要谨慎记录，不强行改表。

默认不直接改主列表，除非同时满足：

- Reviewer 证据清楚；
- 主控复核规则一致；
- 不依赖缺失全文；
- 不会造成 schema 迁移半成品。

## 四、Reviewer 原始输出

### A-Reviewer-1: Banach

状态：已返回，15 / 15 条完整覆盖。

主要结论：

- `ASD-0254`: 保持独立 `01.04` general-method bucket；这是 biomedical research workflow automation 而非具体 biomedical object 实验。
- `ASD-0155`, `ASD-0156`, `ASD-0379`: 保持 `04` 材料科学。
- `ASD-0158`, `ASD-0179`, `ASD-0280`, `ASD-0290`, `ASD-0333`, `ASD-0381`: 保持 `03` 化学科学；其中 `ASD-0290` 需复核 `03 / 04` 催化材料边界。
- `ASD-0186`: 保持 `11.07`，但需确认 scientific peer review object 而非通用 review workflow。
- `ASD-0189`, `ASD-0276`, `ASD-0370`: 保持 `06` 生命科学。
- `ASD-0357`: 保持 `07` 医学与健康科学。
- 本切片未发现足够强的 multi-module assignment。

### A-Reviewer-2: Pauli

状态：已返回，14 / 14 条完整覆盖。

主要结论：

- `ASD-0447`: 保持独立 `01.04` general-method bucket；多类合成 demo 是通用 synthesis platform 展示，不是具体对象发现贡献。
- `ASD-0385`, `ASD-0388`, `ASD-0389`, `ASD-0390`, `ASD-0410`, `ASD-0415`, `ASD-0417`, `ASD-0421`, `ASD-0425`: 保持 `04` 材料科学；其中 `ASD-0388` 需复核 confirmed-core strength。
- `ASD-0418`, `ASD-0422`, `ASD-0428`: 保持 `03` 化学科学。
- `ASD-0429`: 保持 `09` 工程与工业技术科学，增材制造工艺参数是核心对象。
- 本切片未发现足够强的 multi-module assignment。

### A-Reviewer-3: Halley

状态：已返回，14 / 14 条完整覆盖。

主要结论：

- `ASD-0455`, `ASD-0466`, `ASD-0478`, `ASD-0484`, `ASD-0487`, `ASD-0491`, `ASD-0503`, `ASD-0505`: 保持 `04` 材料科学；其中 `ASD-0466` 需复核 Agent/autonomy 强度，`ASD-0478` 是 `04 / 01.04` 高压平台边界。
- `ASD-0463`, `ASD-0506`, `ASD-0507`, `ASD-0508`: 保持 `03` 化学科学。
- `ASD-0501`: 保持 `06` 生命科学。
- `ASD-0504`: 保持 `09` 工程与工业技术科学。
- 本切片未发现足够强的 multi-module assignment。

### A-Reviewer-4: Feynman

状态：已返回，14 / 14 条完整覆盖。

主要结论：

- `ASD-0510`: 保持 `08` 农业科学；plant phenotyping 对象稳定，但 full text 可补强。
- `ASD-0511`: 保持 `09` 工程与工业技术科学；advanced scientific instruments / facility operation 是对象。
- `ASD-0512`, `ASD-0523`: 保持正式 `01`；其中 `ASD-0523` 需复核是否 benchmark-heavy。
- `ASD-0513`, `ASD-0514`, `ASD-0515`, `ASD-0516`, `ASD-0517`, `ASD-0520`, `ASD-0522`: 保持 `04` 材料科学；其中 `ASD-0516`, `ASD-0520`, `ASD-0522` 有 `04 / 09` 或 Agent-strength 边界。
- `ASD-0518`, `ASD-0521`: 保持 `06` 生命科学。
- `ASD-0519`: 保持 `03` 化学科学，但需确认 Agent minimum beyond automation。
- 本切片未发现足够强的 multi-module assignment。

## 五、主控裁决表

Wave A 共 57 条，全部完成 Reviewer 覆盖。主控裁决如下：

| ID | Legacy filing | Reviewer suggestion | 主控裁决 | 是否改主列表 | 备注 |
|---|---|---|---|---|---|
| `ASD-0155` | `04 / 04.04` | `04` | 保持 `04` | 否 | freeform dielectric metasurfaces / nanophotonic structure-performance design |
| `ASD-0156` | `04 / 04.01` | `04` | 保持 `04` | 否 | EM-to-materials analysis，工具链不是工程对象 |
| `ASD-0158` | `03 / 03.03` | `03` | 保持 `03` | 否 | organic compounds / flow synthesis routes |
| `ASD-0179` | `03 / 03.03` | `03` | 保持 `03`，列入全文补强 | 否 | reaction-condition recommendation 方向稳定 |
| `ASD-0186` | `11 / 11.07` | `11` | 保持 `11.07`，列入全文复核 | 否 | scientific peer review object 与 generic review workflow 边界 |
| `ASD-0189` | `06 / 06.03` | `06` | 保持 `06`，列入全文补强 | 否 | proteomics / proteins / biological hypotheses |
| `ASD-0254` | `01 / 01.04` | `01.04` | 保持独立 `01.04`，列入边界复核 | 否 | biomedical research workflow automation，无具体疾病/药物/蛋白对象实验 |
| `ASD-0276` | `06 / 06.03` | `06` | 保持 `06`，列入全文补强 | 否 | multiomics / biological entity relationships；clinical data source 不足以转 `07` |
| `ASD-0280` | `03 / 03.03` | `03` | 保持 `03` | 否 | chemical synthesis development / reaction screening / kinetics |
| `ASD-0290` | `03 / 03.02` | `03` | 保持 `03`，列入 `03 / 04` 复核 | 否 | quantum-chemical catalyst feedback，需确认是否有独立 materials contribution |
| `ASD-0333` | `03 / 03.04` | `03` | 保持 `03`，列入全文补强 | 否 | chemistry-specific hypothesis benchmark，不是 general `01.04` |
| `ASD-0357` | `07 / 07.04` | `07` | 保持 `07`，列入全文补强 | 否 | therapeutic target discovery / disease cases |
| `ASD-0370` | `06 / 06.03` | `06` | 保持 `06` | 否 | protein fitness landscape / enzyme variants |
| `ASD-0379` | `04 / 04.04` | `04` | 保持 `04` | 否 | palladium films / material-property Pareto optimization |
| `ASD-0381` | `03 / 03.03` | `03` | 保持 `03`，列入全文补强 | 否 | rhodium-catalyzed hydroformylation / catalysis Pareto fronts |
| `ASD-0385` | `04 / 04.04` | `04` | 保持 `04` | 否 | semiconductor nanoparticle shell-growth route |
| `ASD-0388` | `04 / 04.01` | `04` | 保持 `04`，列入 core-strength 复核 | 否 | crystallography / XRD phase identification for materials discovery |
| `ASD-0389` | `04 / 04.04` | `04` | 保持 `04` | 否 | chiral inorganic perovskite nanocrystals |
| `ASD-0390` | `04 / 04.04` | `04` | 保持 `04` | 否 | adhesive formulations / bond strength |
| `ASD-0410` | `04 / 04.04` | `04` | 保持 `04` | 否 | phase-change materials / beamline closed-loop materials discovery |
| `ASD-0415` | `04 / 04.03` | `04` | 保持 `04` | 否 | polymer formulations / material properties |
| `ASD-0417` | `04 / 04.04` | `04` | 保持 `04` | 否 | Li-ion battery electrolytes / material formulation performance |
| `ASD-0418` | `03 / 03.03` | `03` | 保持 `03` | 否 | stereoselective Suzuki-Miyaura coupling / reaction conditions |
| `ASD-0421` | `04 / 04.04` | `04` | 保持 `04` | 否 | superconducting compounds / Zr-In-Ni system |
| `ASD-0422` | `03 / 03.03` | `03` | 保持 `03` | 否 | molecular electrochemistry mechanism |
| `ASD-0425` | `04 / 04.03` | `04` | 保持 `04` | 否 | CNT growth / nanomaterial growth rate |
| `ASD-0428` | `03 / 03.03` | `03` | 保持 `03` | 否 | new reactions / new molecules / reactivity modes |
| `ASD-0429` | `09 / 09.02` | `09` | 保持 `09`，列入 core-strength 复核 | 否 | autonomous additive manufacturing / 3D-printing process optimization |
| `ASD-0447` | `01 / 01.04` | `01.04` | 保持独立 `01.04`，列入边界复核 | 否 | universal chemical synthesis platform，多对象 demo 不构成具体对象发现贡献 |
| `ASD-0455` | `04 / 04.04` | `04` | 保持 `04` | 否 | photocatalyst mixtures / hydrogen-evolution performance |
| `ASD-0463` | `03 / 03.03` | `03` | 保持 `03` | 否 | organic molecules / synthesis routes |
| `ASD-0466` | `04 / 04.03` | `main_control_review` | 保持 `04`，列入 Agent/autonomy 复核 | 否 | CNT wall selectivity 方向稳定，但需压实自主决策强度 |
| `ASD-0478` | `04 / 04.04` | `main_control_review` | 保持 `04`，列入 `04 / 01.04` 平台边界复核 | 否 | NIMS-OS 是 materials closed-loop orchestration，平台贡献偏强 |
| `ASD-0484` | `04 / 04.03` | `04` | 保持 `04` | 否 | silver nanoparticles / optical response |
| `ASD-0487` | `04 / 04.04` | `04` | 保持 `04` | 否 | battery electrolytes / electrochemical stability window |
| `ASD-0491` | `04 / 04.04` | `04` | 保持 `04` | 否 | perovskite thin films / PCE and stability |
| `ASD-0501` | `06 / 06.03` | `06` | 保持 `06` | 否 | yeast gene function / functional genomics |
| `ASD-0503` | `04 / 04.04` | `04` | 保持 `04` | 否 | thin-film materials / optoelectronic properties |
| `ASD-0504` | `09 / 09.02` | `09` | 保持 `09` | 否 | mechanical structures / additive-manufacturing design |
| `ASD-0505` | `04 / 04.04` | `04` | 保持 `04` | 否 | solid-state materials / phase selection |
| `ASD-0506` | `03 / 03.03` | `03` | 保持 `03` | 否 | donor-acceptor molecules / photostability |
| `ASD-0507` | `03 / 03.03` | `03` | 保持 `03` | 否 | reaction conditions / reaction-class generality |
| `ASD-0508` | `03 / 03.04` | `03` | 保持 `03` | 否 | dye-like molecules / multiproperty molecular discovery |
| `ASD-0510` | `08 / 08.01` | `08` | 保持 `08`，列入全文补强 | 否 | automated plant phenotyping，`08` 低覆盖但不放宽也不回收 |
| `ASD-0511` | `09 / 09.03` | `09` | 保持 `09` | 否 | scientific instruments / facility operation |
| `ASD-0512` | `01 / 01.01` | `01` | 保持正式 `01` | 否 | cap set / extremal combinatorics，不是 `01.04` |
| `ASD-0513` | `04 / 04.04` | `04` | 保持 `04`，列入 core-strength 复核 | 否 | networked autonomous materials exploration systems |
| `ASD-0514` | `04 / 04.03` | `04` | 保持 `04` | 否 | gold nanoparticles / phase mapping |
| `ASD-0515` | `04 / 04.04` | `04` | 保持 `04` | 否 | alloy thin films / anomalous-Hall functional materials |
| `ASD-0516` | `04 / 04.04` | `04` | 保持 `04`，列入 `04 / 09` 复核 | 否 | PVD equipment-heavy，但对象仍为 silver thin-film material properties |
| `ASD-0517` | `04 / 04.03` | `04` | 保持 `04` | 否 | plasmonic nanoparticles / optical properties |
| `ASD-0518` | `06 / 06.03` | `06` | 保持 `06` | 否 | enzyme/protein engineering |
| `ASD-0519` | `03 / 03.02` | `03` | 保持 `03`，列入 Agent-strength 复核 | 否 | electrochemistry discovery 对象稳定，但 autonomy depth uncertain |
| `ASD-0520` | `04 / 04.04` | `04` | 保持 `04`，列入 Agent-strength / `04 / 03` 复核 | 否 | low-Ir OER electrocatalyst material performance |
| `ASD-0521` | `06 / 06.03` | `06` | 保持 `06` | 否 | CRISPR gene-editing experiment design |
| `ASD-0522` | `04 / 04.01` | `04` | 保持 `04` | 否 | AFM materials characterization |
| `ASD-0523` | `01 / 01.02` | `01` | 保持正式 `01`，列入全文复核 | 否 | AI research automation 是 formal-computational object，不是 general `01.04` |

## 六、Wave A 口径校准结论

基于 57 条完整结果，本轮形成以下校准结论：

1. Batch 2 / Wave A 未发现高置信 multi-module assignment。材料、化学、生命、医学、工程和 `01.04` 样本均可按单对象模块稳定处理。
2. `ASD-0254` 与 `ASD-0447` 是本轮最关键的独立 `01.04` 校准样本：前者是 biomedical research workflow automation，后者是 universal chemical synthesis platform。二者虽带有生物医学或化学语境，但 Reviewer 未发现具体对象层科学实验贡献。
3. `03 / 04` 继续按最终对象而非实验手段处理：反应、分子、合成路线、分子电化学归 `03`；纳米材料、电池电解液、聚合物、钙钛矿、CNT、薄膜、超导材料等材料结构/性能对象归 `04`。
4. `04 / 09` 边界继续按“材料对象 vs 工程工艺/设备对象”判断。PVD、AFM、beamline 等设备通常是方法；additive manufacturing process optimization 和 scientific instrument operation 可归 `09`。
5. `06 / 07` 仍按 endpoint 判断。omics、proteomics、protein/enzyme engineering、CRISPR gene editing 归 `06`；therapeutic target discovery 和 disease-case validation 归 `07`。
6. 正式 `01` 与独立 `01.04` 的边界继续稳定：数学发现、AI research automation 等有明确 formal-computational object 的记录保留正式 `01`；无具体对象实验的通用科研工作流保留独立 `01.04`。
7. 当前没有足够证据支持重构一级分类，问题主要集中在边界解释与低覆盖类稀缺性判断。

## 七、待主控复核队列

Wave A 暂列以下记录为主控复核或后续全文复核：

| ID | 当前 legacy | 初步问题 | 暂定处理 |
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

## 八、本轮统计

| Metric | Count |
|---|---:|
| reviewed records | 57 |
| Reviewer-covered records | 57 |
| unchanged by主控 | 57 |
| add_module | 0 |
| move_primary | 0 |
| move_to_01.04 | 0 |
| demote/background-review candidate | 0 |
| main-control / full-text follow-up queue | 20 |
| records with `full_text_required=yes` from Reviewer output | 22 |

本轮不修改 `agent_master_paper_list.md`。主列表 record-level confirmed count 仍为 `451`，`needs_review` 仍为 `0`，confirmed `08` 仍为 `3`。
