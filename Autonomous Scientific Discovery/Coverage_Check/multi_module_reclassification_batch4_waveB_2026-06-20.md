# Batch 4 / Wave B 多模块重分类审计报告

> 日期：2026-06-20  
> 范围：`agent_master_paper_list.md` confirmed 记录序号 396-451。  
> 对应计划：`Coverage_Check/multi_module_reclassification_flat_batch_plan_451_confirmed_2026-06-20.md`。  
> 当前阶段：Reviewer 已完成，主控已合并；本轮不修改主列表。
> 口径提示：本文件为较保守第一轮审计的历史记录。后续执行应以 `classification_policy_relaxation_addendum_2026-06-20.md` 和当前规则文件为准：只要有可识别的具体对象实验、验证、benchmark task、case study 或结果报告，即可记录对应模块，不要求构成核心科学贡献。

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

本轮按当前主列表 confirmed 记录出现顺序抽取序号 396-451。注意：计划表中的 ID 边界只表示 confirmed 顺序范围，不保证连续编号；本报告使用当前主列表解析得到的精确 ID 切片。

| Reviewer | Agent | 记录数 | 分配 ID |
|---|---|---:|---|
| B-Reviewer-1 | Socrates | 14 | `ASD-0805`, `ASD-0806`, `ASD-0807`, `ASD-0808`, `ASD-0809`, `ASD-0810`, `ASD-0811`, `ASD-0812`, `ASD-0813`, `ASD-0814`, `ASD-0815`, `ASD-0816`, `ASD-0817`, `ASD-0818` |
| B-Reviewer-2 | Godel | 14 | `ASD-0819`, `ASD-0820`, `ASD-0821`, `ASD-0822`, `ASD-0826`, `ASD-0827`, `ASD-0828`, `ASD-0829`, `ASD-0824`, `ASD-0825`, `ASD-0830`, `ASD-0831`, `ASD-0832`, `ASD-0833` |
| B-Reviewer-3 | Singer | 14 | `ASD-0838`, `ASD-0839`, `ASD-0840`, `ASD-0844`, `ASD-0845`, `ASD-0848`, `ASD-0849`, `ASD-0850`, `ASD-0851`, `ASD-0852`, `ASD-0853`, `ASD-0854`, `ASD-0855`, `ASD-0856` |
| B-Reviewer-4 | Linnaeus | 14 | `ASD-0857`, `ASD-0858`, `ASD-0859`, `ASD-0860`, `ASD-0861`, `ASD-0862`, `ASD-0863`, `ASD-0864`, `ASD-0866`, `ASD-0867`, `ASD-0868`, `ASD-0869`, `ASD-0870`, `ASD-0871` |

## 三、主控合并口径

本轮原始审计沿用 Batch 1-3 与 Batch 4 / Wave A 校准后的较保守口径；后续复用本段时应按下列新口径理解：

- 分类依据是实际研究、实验、验证、benchmark task、case study 或结果报告覆盖的具体科学对象，不是 Agent 技术、平台名称、venue 或自称通用性。
- 有具体科学对象实验、验证、benchmark task、case study 或结果报告的论文，优先进入对应 `01-11` 对象模块，而不是回收到 `01.04`。
- 只要多个具体科学对象各自有可识别的实验、验证、benchmark task、case study 或结果报告，就建议 multi-module；不要求每个模块构成论文的核心科学贡献。
- 没有任何具体科学对象实验、验证、benchmark task、case study 或结果报告，只提出 ASD / general research-agent 方法或通用 benchmark 的论文，进入独立 `01.04` bucket。
- `03 / 04` 继续按分子、反应、合成、催化 vs 材料组成、结构、相、性能、器件材料对象判断。
- `05 / 10` 继续按自然地球环境对象 vs 航天/任务/载具对象判断。
- `06 / 07` 继续按 biological mechanism / protein / omics vs disease / therapeutic / clinical endpoint 判断。
- `09 / 03` 继续按工程流程、装置、过程系统 vs 化学反应/分子对象判断。
- `11.07 / 01.04` 继续按 scientific knowledge production itself vs general research-agent workflow 判断。
- equation discovery / physics-guided agent 只有在具体物理对象实验明确时才转 `02`；否则按形式/计算对象或独立 `01.04` 判定。

## 四、Reviewer 原始输出

### B-Reviewer-1: Socrates

状态：已返回，14 / 14 条完整覆盖。

主要结论：

- `ASD-0805`, `ASD-0806`, `ASD-0807`, `ASD-0809` 保持 `09`，turbomachinery、optofluidic assembly、power-electronics control、battery system parameter estimation 都是工程对象。
- `ASD-0808`, `ASD-0811` 保持 `04`，2D semiconductor mobility / battery negolyte 属材料或能源材料对象；`ASD-0811` 列入 `03 / 04` 全文确认。
- `ASD-0810`, `ASD-0818` 保持 `03`，molecular design / broad molecular optimization 是化学对象；`ASD-0818` 保留 `03 / 07` 边界标记。
- `ASD-0812`, `ASD-0814`, `ASD-0815`, `ASD-0816`, `ASD-0817` 保持 `07`，translational medicine、medical neuroimaging、digital health biomarkers、target safety、structure-based drug design 都是医学/药物对象。
- `ASD-0813` 保持 `06`，single-cell genomics 是生命科学对象。
- 本切片未发现应转 `01.04` 或新增 multi-module 的记录。

### B-Reviewer-2: Godel

状态：已返回，14 / 14 条完整覆盖。

主要结论：

- `ASD-0819`, `ASD-0820`, `ASD-0821`, `ASD-0832` 保持 `03`，molecular optimization、chemical language models、catalyst discovery 是化学对象；`ASD-0820` 为最高风险 `03 / 07` 边界。
- `ASD-0822`, `ASD-0824`, `ASD-0825`, `ASD-0826`, `ASD-0827`, `ASD-0828` 保持 `07`，drug response、drug lead optimization、computational pathology 都是医学/药物对象。
- `ASD-0829`, `ASD-0830` 保持 `02`，astroparticle physics / BESIII physics analysis 对象稳定。
- `ASD-0831` 保持 `11.07`，phenotype ontology curation 是 scientific knowledge organization / knowledge production。
- `ASD-0833` 保持 `06`，virtual cells / perturbation biology / mechanistic reasoning 是生命科学对象。
- 本切片未发现应新增 `01.04` 或 multi-module 的记录。

### B-Reviewer-3: Singer

状态：已返回，14 / 14 条完整覆盖。

主要结论：

- `ASD-0838` 保持 `03`，continuous-flow chemistry 是化学反应/合成对象。
- `ASD-0839`, `ASD-0840` 保持 `02`，Einstein Telescope / gravitational-wave analysis 与 cosmological perturbation-theory module 是物理/天文对象。
- `ASD-0844`, `ASD-0845`, `ASD-0856` 在本轮历史审计中保持独立 `01.04`；后续需按新口径逐项检查其跨领域 demo / benchmark 是否包含可识别的具体对象实验、验证、case study 或结果报告。
- `ASD-0848`, `ASD-0849`, `ASD-0855` 保持 `11.07`，scientific manuscript production、scientific ecosystem、peer review / scientific evaluation 属 scientific knowledge production itself。
- `ASD-0850` 保持 `01.02`，algorithm discovery 是 formal/computational object；但 Note 与主列表存在痕迹冲突，列入后续修订队列。
- `ASD-0851` 保持 `05`，geospatial model discovery 对象稳定。
- `ASD-0852`, `ASD-0853`, `ASD-0854` 保持 `10`，rover mission-science autonomy 是航天任务对象，不因火星地质目标转 `05`。

### B-Reviewer-4: Linnaeus

状态：已返回，14 / 14 条完整覆盖。

主要结论：

- `ASD-0857` 保持 `01.03`，governing equation / scientific-law recovery 是 formal systems / law discovery object。
- `ASD-0858` 保持 `10`，AEGIS / MSL rover mission-science operations 是航天任务对象。
- `ASD-0859`, `ASD-0860`, `ASD-0861` 保持 `05`，volcanism、cryosphere、flood monitoring 是地球环境对象，卫星只是平台。
- `ASD-0862`, `ASD-0863`, `ASD-0864` 保持 `02`，HEP analysis / workflows / simulation campaign 是物理对象；`ASD-0864` 列入 support-tooling/core-strength 复核。
- `ASD-0866`, `ASD-0868`, `ASD-0869`, `ASD-0870`, `ASD-0871` 保持独立 `01.04`，goal-evolving agents、equation-discovery agents、general deep-knowledge agents 无具体对象实验。
- `ASD-0867` 保持 `06`，protein sequence design with experimental validation 是生命科学对象。

## 五、主控裁决表

Wave B 共 56 条，全部完成 Reviewer 覆盖。主控裁决如下：

| ID | Legacy filing | Reviewer suggestion | 主控裁决 | 是否改主列表 | 备注 |
|---|---|---|---|---|---|
| `ASD-0805` | `09 / 09.02` | `09` | 保持 `09` | 否 | turbomachinery aerodynamic design |
| `ASD-0806` | `09 / 09.03` | `09` | 保持 `09` | 否 | optofluidic assembly / engineering control |
| `ASD-0807` | `09 / 09.03` | `09` | 保持 `09` | 否 | power-electronics control design |
| `ASD-0808` | `04 / 04.04` | `04` | 保持 `04` | 否 | 2D semiconductor mobility materials |
| `ASD-0809` | `09 / 09.06` | `09` | 保持 `09` | 否 | battery system parameter estimation / digital twin |
| `ASD-0810` | `03 / 03.04` | `03` | 保持 `03` | 否 | synthetic-pathway molecular design |
| `ASD-0811` | `04 / 04.04` | `04` | 保持 `04`，列入全文补强 | 否 | redox-flow-battery negolytes；`03 / 04` 边界 |
| `ASD-0812` | `07 / 07.04` | `07` | 保持 `07` | 否 | translational medicine |
| `ASD-0813` | `06 / 06.03` | `06` | 保持 `06`，列入 core-strength 复核 | 否 | single-cell genomics |
| `ASD-0814` | `07 / 07.01` | `07` | 保持 `07` | 否 | clinical neuroimaging biomarkers |
| `ASD-0815` | `07 / 07.03` | `07` | 保持 `07` | 否 | wearable digital health biomarkers |
| `ASD-0816` | `07 / 07.04` | `07` | 保持 `07` | 否 | therapeutic target safety |
| `ASD-0817` | `07 / 07.04` | `07` | 保持 `07` | 否 | structure-based drug design |
| `ASD-0818` | `03 / 03.04` | `03` | 保持 `03`，列入 `03 / 07` 复核 | 否 | broad molecular optimization benchmark |
| `ASD-0819` | `03 / 03.04` | `03` | 保持 `03` | 否 | molecular optimization |
| `ASD-0820` | `03 / 03.04` | `03` | 保持 `03`，列入高风险 `03 / 07` 复核 | 否 | synthesizable lead optimization；drug-lead pressure |
| `ASD-0821` | `03 / 03.04` | `03` | 保持 `03` | 否 | molecular design and synthesis |
| `ASD-0822` | `07 / 07.04` | `07` | 保持 `07` | 否 | colorectal cancer drug response |
| `ASD-0826` | `07 / 07.04` | `07` | 保持 `07` | 否 | multi-objective drug discovery |
| `ASD-0827` | `07 / 07.01` | `07` | 保持 `07` | 否 | computational pathology diagnosis |
| `ASD-0828` | `07 / 07.01` | `07` | 保持 `07` | 否 | pathology biomarker discovery |
| `ASD-0829` | `02 / 02.02` | `02` | 保持 `02` | 否 | astroparticle physics |
| `ASD-0824` | `07 / 07.04` | `07` | 保持 `07` | 否 | drug lead optimization |
| `ASD-0825` | `07 / 07.04` | `07` | 保持 `07` | 否 | de novo drug design |
| `ASD-0830` | `02 / 02.02` | `02` | 保持 `02`，列入全文补强 | 否 | BESIII real-world physics analysis |
| `ASD-0831` | `11 / 11.07` | `11.07` | 保持 `11.07`，列入全文补强 | 否 | phenotype ontology curation / knowledge organization |
| `ASD-0832` | `03 / 03.03` | `03` | 保持 `03`，列入全文补强 | 否 | CO2 reduction catalyst discovery |
| `ASD-0833` | `06 / 06.03` | `06` | 保持 `06`，列入全文补强 | 否 | virtual cells / mechanistic reasoning |
| `ASD-0838` | `03 / 03.03` | `03` | 保持 `03`，列入全文补强 | 否 | continuous-flow chemistry |
| `ASD-0839` | `02 / 02.01` | `02` | 保持 `02` | 否 | Einstein Telescope / gravitational-wave analysis |
| `ASD-0840` | `02 / 02.02` | `02` | 保持 `02` | 否 | cosmological perturbation-theory software |
| `ASD-0844` | `01 / 01.04` | `01.04` | legacy 暂保持 `01.04`，新口径下优先复核 `06` 与 `01.03 / 02` | 否 | Science Earth platform demos 需按具体对象实验 / case study / 结果报告重新判断 |
| `ASD-0845` | `01 / 01.04` | `01.04` | 保持独立 `01.04` | 否 | general data-centric end-to-end researcher |
| `ASD-0848` | `11 / 11.07` | `11.07` | 保持 `11.07` | 否 | scientific manuscript production |
| `ASD-0849` | `11 / 11.07` | `11.07` | 保持 `11.07` | 否 | human-AI scientist ecosystem / knowledge production |
| `ASD-0850` | `01 / 01.02` | `01` | 保持 `01.02`，列入 Note / master trace conflict 复核 | 否 | algorithm discovery object |
| `ASD-0851` | `05 / 05.04` | `05` | 保持 `05` | 否 | geospatial model discovery |
| `ASD-0852` | `10 / 10.02` | `10` | 保持 `10` | 否 | ExoMars-like rover mission science |
| `ASD-0853` | `10 / 10.02` | `10` | 保持 `10` | 否 | onboard rover science |
| `ASD-0854` | `10 / 10.02` | `10` | 保持 `10` | 否 | Mars rover mission autonomy |
| `ASD-0855` | `11 / 11.07` | `11.07` | 保持 `11.07`，列入全文补强 | 否 | peer review / scientific evaluation |
| `ASD-0856` | `01 / 01.04` | `01.04` | 保持独立 `01.04`，列入 demo 权重复核 | 否 | open-ended discovery workflow / cross-dataset demos |
| `ASD-0857` | `01 / 01.03` | `01` | 保持 `01.03` | 否 | governing equation / scientific-law recovery |
| `ASD-0858` | `10 / 10.02` | `10` | 保持 `10` | 否 | MSL rover mission operations |
| `ASD-0859` | `05 / 05.04` | `05` | 保持 `05` | 否 | active volcanism monitoring |
| `ASD-0860` | `05 / 05.04` | `05` | 保持 `05` | 否 | cryospheric change monitoring |
| `ASD-0861` | `05 / 05.04` | `05` | 保持 `05` | 否 | flood detection and monitoring |
| `ASD-0862` | `02 / 02.02` | `02` | 保持 `02` | 否 | experimental high-energy physics |
| `ASD-0863` | `02 / 02.02` | `02` | 保持 `02`，列入细节补强 | 否 | HEP workflows |
| `ASD-0864` | `02 / 02.02` | `02` | 保持 `02`，列入 support-tooling / core-strength 复核 | 否 | MadGraph / HEP simulation workflow |
| `ASD-0866` | `01 / 01.04` | `01.04` | legacy 暂保持 `01.04`，列入全文补强 | 否 | autonomous goal-evolving agents；按新口径检查 cross-domain cases 是否有具体对象实验 / case study / 结果报告 |
| `ASD-0867` | `06 / 06.03` | `06` | 保持 `06` | 否 | protein sequence design with experimental validation |
| `ASD-0868` | `01 / 01.04` | `01.04` | 保持独立 `01.04` | 否 | physics-guided equation-discovery method, not `02` |
| `ASD-0869` | `01 / 01.04` | `01.04` | 保持独立 `01.04` | 否 | automatic equation-discovery framework |
| `ASD-0870` | `01 / 01.04` | `01.04` | 保持独立 `01.04` | 否 | cross-domain equation-discovery agent benchmark |
| `ASD-0871` | `01 / 01.04` | `01.04` | 保持独立 `01.04`，列入全文补强 | 否 | general deep-knowledge research assistant |

## 六、Wave B 口径校准结论

基于 56 条完整结果，本轮形成以下校准结论：

1. Batch 4 / Wave B 在当时较保守口径下未发现高置信 multi-module assignment。跨领域 benchmark、跨数据集 demo、platform cases 和工具链复用不会自动形成多模块；但若可明确对应具体科学对象并报告结果，后续应按新口径记录对应模块。
2. `01.04` 在最后一批中继续作为独立 general-method bucket。`ASD-0844`, `ASD-0845`, `ASD-0856`, `ASD-0866`, `ASD-0868`, `ASD-0869`, `ASD-0870`, `ASD-0871` 在本轮历史审计中暂保持 `01.04`；后续需按新口径复核是否存在具体对象实验、验证、benchmark task、case study 或结果报告。
3. `Science Earth` (`ASD-0844`) 是新口径下的优先复核样本：如果 complex systems / Kuramoto 与 pan-cancer single-cell 案例确认为具体对象 case study 或结果报告，则不应只保留 `01.04`，应记录 `06` 与 `01.03 / 02` 等对应模块。
4. equation discovery 边界进一步清楚：`ASD-0857` 是 formal systems / governing-law object，保持 `01.03`；`ASD-0868-0870` 是 general equation-discovery method / benchmark，保持独立 `01.04`。
5. `03 / 07` 边界仍是高压区。`ASD-0820` 最不稳定，暂保留 `03`，后续按 lead optimization 是否绑定 therapeutic target / translational endpoint 复核。
6. `05 / 10` 边界再次验证：rover mission operations 保持 `10`；EO-1 火山、冰冻圈、洪水监测以地球环境过程为对象，保持 `05`。
7. `11.07 / 01.04` 边界保持稳定。paper writing、scientific ecosystem、peer review、ontology curation 属 scientific knowledge production itself；general research assistant / equation-discovery benchmark 不转 `11.07`。
8. 当前没有足够证据支持重构一级分类，问题主要集中在边界解释与低覆盖类稀缺性判断。

## 七、待主控复核队列

Wave B 暂列以下记录为主控复核或后续全文复核：

| ID | 当前 legacy | 初步问题 | 暂定处理 |
|---|---|---|---|
| `ASD-0811` | `04 / 04.04` | battery negolyte 的 `03 / 04` 边界与全文证据 | 暂保持 `04` |
| `ASD-0813` | `06 / 06.03` | ELISA agent-threshold / core-strength | 暂保持 `06` |
| `ASD-0818` | `03 / 03.04` | broad molecular optimization 的 `03 / 07` 边界 | 暂保持 `03` |
| `ASD-0820` | `03 / 03.04` | synthesizable lead optimization 的高风险 `03 / 07` 边界 | 暂保持 `03` |
| `ASD-0830` | `02 / 02.02` | BESIII real-world physics analysis 细节补强 | 暂保持 `02` |
| `ASD-0831` | `11 / 11.07` | phenotype ontology curation 的 `11.07 / 06` 边界证据补强 | 暂保持 `11.07` |
| `ASD-0832` | `03 / 03.03` | catalyst discovery evidence based on abstract/note package | 暂保持 `03` |
| `ASD-0833` | `06 / 06.03` | virtual-cell mechanistic reasoning evidence depth | 暂保持 `06` |
| `ASD-0838` | `03 / 03.03` | continuous-flow chemistry full-text/source strength | 暂保持 `03` |
| `ASD-0844` | `01 / 01.04` | Science Earth demos 是否包含具体对象实验 / case study / 结果报告 | legacy 暂保持 `01.04`，新口径下优先复核 `06` 与 `01.03 / 02` |
| `ASD-0850` | `01 / 01.02` | OR-Agent Note 与主列表 trace 冲突；需统一证据记录 | 暂保持 `01.02` |
| `ASD-0855` | `11 / 11.07` | peer-review framework 实证强度 | 暂保持 `11.07` |
| `ASD-0856` | `01 / 01.04` | AutoDiscovery cross-dataset demos 是否仅为 benchmark | 暂保持 `01.04` |
| `ASD-0863` | `02 / 02.02` | HEP workflow detail | 暂保持 `02` |
| `ASD-0864` | `02 / 02.02` | support-tooling / discovery-strength boundary | 暂保持 `02` |
| `ASD-0866` | `01 / 01.04` | cross-domain cases 是否有可识别对象层实验、验证、case study 或结果报告 | 暂保持 `01.04` |
| `ASD-0871` | `01 / 01.04` | Denario project 是否仍为 general research assistant；`01.04 / 11.07` 边界 | 暂保持 `01.04` |

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
| main-control / full-text follow-up queue | 17 |
| records with `full_text_required=yes` from Reviewer output | 17 |

本轮不修改 `agent_master_paper_list.md`。主列表 record-level confirmed count 仍为 `451`，`needs_review` 仍为 `0`，confirmed `08` 仍为 `3`。
