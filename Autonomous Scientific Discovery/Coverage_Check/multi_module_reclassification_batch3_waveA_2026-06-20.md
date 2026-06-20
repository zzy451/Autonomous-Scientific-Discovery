# Batch 3 / Wave A 多模块重分类审计报告

> 日期：2026-06-20  
> 范围：`agent_master_paper_list.md` confirmed 记录序号 227-283。  
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

本轮按当前主列表 confirmed 记录出现顺序抽取序号 227-283。注意：计划表中的 ID 边界只表示 confirmed 顺序范围，不保证连续编号；本报告使用当前主列表解析得到的精确 ID 切片。

| Reviewer | Agent | 记录数 | 分配 ID |
|---|---|---:|---|
| A-Reviewer-1 | Fermat | 15 | `ASD-0601`, `ASD-0603`, `ASD-0605`, `ASD-0606`, `ASD-0607`, `ASD-0608`, `ASD-0609`, `ASD-0610`, `ASD-0611`, `ASD-0612`, `ASD-0613`, `ASD-0614`, `ASD-0615`, `ASD-0621`, `ASD-0622` |
| A-Reviewer-2 | Sartre | 14 | `ASD-0623`, `ASD-0624`, `ASD-0625`, `ASD-0626`, `ASD-0627`, `ASD-0628`, `ASD-0629`, `ASD-0630`, `ASD-0631`, `ASD-0632`, `ASD-0633`, `ASD-0634`, `ASD-0635`, `ASD-0636` |
| A-Reviewer-3 | Faraday | 14 | `ASD-0637`, `ASD-0644`, `ASD-0645`, `ASD-0647`, `ASD-0648`, `ASD-0649`, `ASD-0650`, `ASD-0651`, `ASD-0652`, `ASD-0653`, `ASD-0654`, `ASD-0655`, `ASD-0656`, `ASD-0658` |
| A-Reviewer-4 | Pasteur | 14 | `ASD-0659`, `ASD-0660`, `ASD-0662`, `ASD-0663`, `ASD-0664`, `ASD-0665`, `ASD-0666`, `ASD-0667`, `ASD-0668`, `ASD-0669`, `ASD-0670`, `ASD-0671`, `ASD-0672`, `ASD-0673` |

## 三、主控合并口径

本轮沿用 Batch 1 与 Batch 2 校准后的口径：

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

### A-Reviewer-1: Fermat

状态：已返回，15 / 15 条完整覆盖。

主要结论：

- `ASD-0601`, `ASD-0603`, `ASD-0605`, `ASD-0607`, `ASD-0609`: 保持 `03` 化学科学；reaction / organic synthesis / pH chemical behavior 对象稳定。
- `ASD-0606`, `ASD-0608`, `ASD-0610`, `ASD-0611`, `ASD-0612`, `ASD-0614`, `ASD-0621`, `ASD-0622`: 保持 `04` 材料科学；MOF、nanoparticle、phase diagram、PXRD、电解质材料对象稳定。
- `ASD-0613`: 保持 `02`，nanoplasmonic physics discovery 是物理对象而非材料组成优化。
- `ASD-0615`: 保持 `09`，mechanical structures / resilience / toughness 是工程对象。
- 本切片未发现足够强的 multi-module assignment。

### A-Reviewer-2: Sartre

状态：已返回，14 / 14 条完整覆盖。

主要结论：

- `ASD-0623`, `ASD-0632`, `ASD-0633`, `ASD-0635`: 保持 `05` 地球与环境科学；climate / geoscientific archives / atmospheric mechanism 对象稳定。
- `ASD-0624`, `ASD-0625`, `ASD-0626`, `ASD-0628`, `ASD-0629`, `ASD-0636`: 保持 `11.07`；peer review、claim attribution、science-of-science 是 scientific knowledge production itself。
- `ASD-0627`: 保持 `10`，deep-space mission science operations 是航天任务科学对象。
- `ASD-0630`, `ASD-0631`: 保持 `04` 材料科学。
- `ASD-0634`: 保持 `08`，plant science / grapevine disease case 支持农业/植物科学应用对象。
- 本切片未发现足够强的 multi-module assignment。

### A-Reviewer-3: Faraday

状态：已返回，14 / 14 条完整覆盖。

主要结论：

- `ASD-0637`, `ASD-0652`, `ASD-0655`, `ASD-0656`, `ASD-0658`: 保持 `11.07`；citation networks、research community、peer review、reproducibility 均为 scientific knowledge production object。
- `ASD-0644`: 保持 `11.02`，对象是一般社会行为与社会实验，不是 science-of-science。
- `ASD-0654`: 保持 `11.01`，对象是 empirical economics。
- `ASD-0645`, `ASD-0647`, `ASD-0648`: 保持 `10`，航天器/卫星 mission-science operations 是对象，不按地球观测或天体对象转 `05` / `02`。
- `ASD-0649`, `ASD-0650`, `ASD-0651`, `ASD-0653`: 保持 `05`；其中 `ASD-0651` 是 `05 / 11 / 01.04` 高压边界样本。
- 本切片未发现足够强的 multi-module assignment。

### A-Reviewer-4: Pasteur

状态：已返回，14 / 14 条完整覆盖。

主要结论：

- `ASD-0659`, `ASD-0660`, `ASD-0662`, `ASD-0663`, `ASD-0671`, `ASD-0673`: 保持独立 `01.04` general-method bucket；跨学科 demo / benchmark 不构成多模块对象覆盖。
- `ASD-0664`, `ASD-0665`: 保持 `03` 化学科学；computational catalysis / transition state search 对象稳定。
- `ASD-0666`, `ASD-0667`, `ASD-0668`, `ASD-0672`: 保持 `04` 材料科学；materials / polymer discovery 对象稳定。
- `ASD-0669`: 保持 `06`，bioinformatics / computational-biology model refinement 是对象。
- `ASD-0670`: 保持 `07`，drug discovery stages 是对象。
- 本切片未发现足够强的 multi-module assignment。

## 五、主控裁决表

Wave A 共 57 条，全部完成 Reviewer 覆盖。主控裁决如下：

| ID | Legacy filing | Reviewer suggestion | 主控裁决 | 是否改主列表 | 备注 |
|---|---|---|---|---|---|
| `ASD-0601` | `03 / 03.03` | `03` | 保持 `03` | 否 | flow photocatalysis reaction optimization |
| `ASD-0603` | `03 / 03.03` | `03` | 保持 `03` | 否 | diverse chemical reaction optimization |
| `ASD-0605` | `03 / 03.04` | `03` | 保持 `03` | 否 | oil-droplet chemical formulation behavior |
| `ASD-0606` | `04 / 04.03` | `04` | 保持 `04` | 否 | MOF/ZIF crystallinity and material quality |
| `ASD-0607` | `03 / 03.03` | `03` | 保持 `03` | 否 | robotic organic synthesis |
| `ASD-0608` | `04 / 04.04` | `04` | 保持 `04` | 否 | battery electrolyte materials optimization |
| `ASD-0609` | `03 / 03.03` | `03` | 保持 `03`，列入全文补强 | 否 | chemical pH behavior；second-level nuance 可后续补强 |
| `ASD-0610` | `04 / 04.03` | `04` | 保持 `04` | 否 | nanoparticle spectral-shape / morphology matching |
| `ASD-0611` | `04 / 04.04` | `04` | 保持 `04` | 否 | nonequilibrium phase diagrams |
| `ASD-0612` | `04 / 04.04` | `04` | 保持 `04` | 否 | quaternary oxides / battery materials synthesis |
| `ASD-0613` | `02 / 02.02` | `02` | 保持 `02`，列入 `02 / 04` 全文补强 | 否 | nanoplasmonic physics discovery |
| `ASD-0614` | `04 / 04.01` | `04` | 保持 `04`，列入 autonomy-depth 复核 | 否 | solid-state PXRD materials characterization |
| `ASD-0615` | `09 / 09.02` | `09` | 保持 `09` | 否 | additively manufactured mechanical structures |
| `ASD-0621` | `04 / 04.04` | `04` | 保持 `04` | 否 | electrolyte formulation discovery |
| `ASD-0622` | `04 / 04.04` | `04` | 保持 `04` | 否 | electrolyte solvent screening |
| `ASD-0623` | `05 / 05.02` | `05` | 保持 `05`，列入 withdrawn/core-strength 复核 | 否 | climate-science benchmark and tools |
| `ASD-0624` | `11 / 11.07` | `11.07` | 保持 `11.07` | 否 | science-of-science workflow support |
| `ASD-0625` | `11 / 11.07` | `11.07` | 保持 `11.07`，列入全文补强 | 否 | academic peer review |
| `ASD-0626` | `11 / 11.07` | `11.07` | 保持 `11.07`，列入全文补强 | 否 | proactive scientific peer review |
| `ASD-0627` | `10 / 10.02` | `10` | 保持 `10` | 否 | deep-space mission science operations |
| `ASD-0628` | `11 / 11.07` | `11.07` | 保持 `11.07`，列入全文补强 | 否 | automated peer review |
| `ASD-0629` | `11 / 11.07` | `11.07` | 保持 `11.07` | 否 | scientific claim attribution / citation grounding |
| `ASD-0630` | `04 / 04.01` | `04` | 保持 `04` | 否 | PXRD materials characterization |
| `ASD-0631` | `04 / 04.04` | `04` | 保持 `04`，列入全文补强 | 否 | polymer electrolyte formulation |
| `ASD-0632` | `05 / 05.04` | `05` | 保持 `05` | 否 | geoscientific data archives |
| `ASD-0633` | `05 / 05.02` | `05` | 保持 `05` | 否 | climate-science workflow |
| `ASD-0634` | `08 / 08.01` | `08` | 保持 `08`，列入全文补强 | 否 | plant science / grapevine case；不因低覆盖而放宽 |
| `ASD-0635` | `05 / 05.02` | `05` | 保持 `05` | 否 | atmospheric mechanisms / WRF verification |
| `ASD-0636` | `11 / 11.07` | `11.07` | 保持 `11.07`，列入全文补强 | 否 | evidence-grounded scientific peer review |
| `ASD-0637` | `11 / 11.07` | `11.07` | 保持 `11.07` | 否 | citation-network science-of-science simulation |
| `ASD-0644` | `11 / 11.02` | `11.02` | 保持 `11.02` | 否 | social behavior experiments / social-science automation |
| `ASD-0645` | `10 / 10.02` | `10` | 保持 `10` | 否 | EO-1 spacecraft mission-science autonomy |
| `ASD-0647` | `10 / 10.02` | `10` | 保持 `10` | 否 | small-body science operations |
| `ASD-0648` | `10 / 10.02` | `10` | 保持 `10`，列入 core-strength 复核 | 否 | Earth-observing satellite autonomy under spacecraft constraints |
| `ASD-0649` | `05 / 05.02` | `05` | 保持 `05` | 否 | CMIP/ESGF climate workflows |
| `ASD-0650` | `05 / 05.04` | `05` | 保持 `05` | 否 | Earth observation tool creation / EO tasks |
| `ASD-0651` | `05 / 05.02` | `main_control_review` | 保持 `05`，列入 `05 / 11 / 01.04` 全文复核 | 否 | heatwave risk with bio-ecological/economic mediation |
| `ASD-0652` | `11 / 11.07` | `11.07` | 保持 `11.07` | 否 | research community simulation |
| `ASD-0653` | `05 / 05.04` | `05` | 保持 `05` | 否 | Earth observation agent |
| `ASD-0654` | `11 / 11.01` | `11.01` | 保持 `11.01` | 否 | empirical economics |
| `ASD-0655` | `11 / 11.07` | `11.07` | 保持 `11.07` | 否 | scientific peer review |
| `ASD-0656` | `11 / 11.07` | `11.07` | 保持 `11.07`，列入全文补强 | 否 | AAAI-26 AI review pilot |
| `ASD-0658` | `11 / 11.07` | `11.07` | 保持 `11.07` | 否 | scientific reproducibility / paper-to-code reproduction |
| `ASD-0659` | `01 / 01.04` | `01.04` | 保持独立 `01.04`，列入 demo 权重全文复核 | 否 | artifact-exchange scientific-agent ecosystem |
| `ASD-0660` | `01 / 01.04` | `01.04` | 保持独立 `01.04` | 否 | multidisciplinary benchmark 不构成多模块对象覆盖 |
| `ASD-0662` | `01 / 01.04` | `01.04` | 保持独立 `01.04` | 否 | evolving general scientific-agent system |
| `ASD-0663` | `01 / 01.04` | `01.04` | 保持独立 `01.04`，列入 demo 权重全文复核 | 否 | self-organizing team mechanism；bio benchmarks 暂不转 `06` |
| `ASD-0664` | `03 / 03.03` | `03` | 保持 `03`，列入 `03 / 04 / 01.04` 全文复核 | 否 | computational catalysis / catalyst mechanism |
| `ASD-0665` | `03 / 03.03` | `03` | 保持 `03` | 否 | transition-state and catalytic mechanism search |
| `ASD-0666` | `04 / 04.04` | `04` | 保持 `04` | 否 | materials exploration workflows |
| `ASD-0667` | `04 / 04.04` | `04` | 保持 `04`，列入全文补强 | 否 | materials candidates / stability evaluation |
| `ASD-0668` | `04 / 04.04` | `04` | 保持 `04` | 否 | polymer property prediction / design |
| `ASD-0669` | `06 / 06.03` | `06` | 保持 `06` | 否 | bioinformatics / computational-biology model refinement |
| `ASD-0670` | `07 / 07.04` | `07` | 保持 `07` | 否 | drug discovery stages |
| `ASD-0671` | `01 / 01.04` | `01.04` | 保持独立 `01.04`，列入 core-strength 复核 | 否 | general autonomous research system |
| `ASD-0672` | `04 / 04.04` | `04` | 保持 `04` | 否 | polymer design |
| `ASD-0673` | `01 / 01.04` | `01.04` | 保持独立 `01.04`，列入 demo 权重全文复核 | 否 | atomistic-research harness；cross-domain demos 不足以多模块 |

## 六、Wave A 口径校准结论

基于 57 条完整结果，本轮形成以下校准结论：

1. Batch 3 / Wave A 未发现高置信 multi-module assignment。跨对象族、跨工具、跨 benchmark、跨实验平台或跨任务链不等于跨一级科学对象模块。
2. `03 / 04` 边界继续稳定：化学反应、合成执行、transition-state search、catalytic mechanism 归 `03`；MOF、nanoparticle、电解质、polymer、phase diagram、materials characterization 归 `04`。
3. `02 / 04` 边界以研究问题为准。`ASD-0613` 研究 nanoplasmonic physics discovery，因此保留 `02`，不因 STEM / nanostructure 外观转为材料科学。
4. `05 / 10` 边界进一步明确：Earth-observing satellite、EO-1、small-body mission science operations 归 `10`；climate science、Earth observation analysis、geoscientific archives 归 `05`。
5. `11.07 / 01.04` 边界继续按对象判定。peer review、citation attribution、research community simulation、scientific reproducibility 属 scientific knowledge production itself，归 `11.07`，不是通用 `01.04`。
6. `11.01–11.02 / 11.07` 边界也较稳定。`ASD-0644` 是一般社会行为研究，`ASD-0654` 是经验经济学；二者不因使用科研自动化 agent 而转 `11.07`。
7. 独立 `01.04` 在本轮主要处理 general / multidisciplinary scientific-agent framework。跨学科 demo 或 benchmark 不自动形成 `03/04/06/07` 多模块，除非全文证明每个对象都有实质对象层贡献。
8. 当前没有足够证据支持重构一级分类，问题主要集中在全文证据强弱、Agent minimum strength、以及平台 demo 权重，而不是 `01-11` 顶层 taxonomy 失稳。

## 七、待主控复核队列

Wave A 暂列以下记录为主控复核或后续全文复核：

| ID | 当前 legacy | 初步问题 | 暂定处理 |
|---|---|---|---|
| `ASD-0609` | `03 / 03.03` | pH adjustment 的 second-level / evidence completeness | 暂保持 `03` |
| `ASD-0613` | `02 / 02.02` | nanoplasmonic physics vs materials characterization | 暂保持 `02` |
| `ASD-0614` | `04 / 04.01` | autonomy depth and workflow evidence | 暂保持 `04` |
| `ASD-0623` | `05 / 05.02` | withdrawn-status / core-strength | 暂保持 `05` |
| `ASD-0625` | `11 / 11.07` | ReviewBench / benchmark-heavy peer-review strength | 暂保持 `11.07` |
| `ASD-0626` | `11 / 11.07` | proactive review agent evidence depth | 暂保持 `11.07` |
| `ASD-0628` | `11 / 11.07` | ScholarPeer full-text evidence depth | 暂保持 `11.07` |
| `ASD-0631` | `04 / 04.04` | polymer electrolyte experiment/autonomy detail | 暂保持 `04` |
| `ASD-0634` | `08 / 08.01` | plant-science object evidence and low-coverage `08` pressure | 暂保持 `08` |
| `ASD-0636` | `11 / 11.07` | EGTR-Review evidence depth / duplicate pressure | 暂保持 `11.07` |
| `ASD-0648` | `10 / 10.02` | EO satellite autonomy 的 scientific core strength | 暂保持 `10` |
| `ASD-0651` | `05 / 05.02` | heatwave risk 的 `05 / 11 / 01.04` 边界 | 暂保持 `05` |
| `ASD-0656` | `11 / 11.07` | AAAI AI Review Pilot full-text evidence | 暂保持 `11.07` |
| `ASD-0659` | `01 / 01.04` | cross-domain demo 是否有对象层科学贡献 | 暂保持 `01.04` |
| `ASD-0663` | `01 / 01.04` | bio benchmark demo 是否足以转 `06` | 暂保持 `01.04` |
| `ASD-0664` | `03 / 03.03` | computational catalysis 的 `03 / 04 / 01.04` 边界 | 暂保持 `03` |
| `ASD-0667` | `04 / 04.04` | materials candidate novelty / evidence chain | 暂保持 `04` |
| `ASD-0671` | `01 / 01.04` | general research system core-strength | 暂保持 `01.04` |
| `ASD-0673` | `01 / 01.04` | AtomisticSkills cross-domain demo weight | 暂保持 `01.04` |

## 八、本轮统计

| Metric | Count |
|---|---:|
| reviewed records | 57 |
| Reviewer-covered records | 57 |
| unchanged by 主控 | 57 |
| add_module | 0 |
| move_primary | 0 |
| move_to_01.04 | 0 |
| demote/background-review candidate | 0 |
| main-control / full-text follow-up queue | 19 |
| records with `full_text_required=yes` from Reviewer output | 20 |

本轮不修改 `agent_master_paper_list.md`。主列表 record-level confirmed count 仍为 `451`，`needs_review` 仍为 `0`，confirmed `08` 仍为 `3`。
