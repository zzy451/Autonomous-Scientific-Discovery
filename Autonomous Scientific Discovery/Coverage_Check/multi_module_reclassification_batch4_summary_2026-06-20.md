# Batch 4 多模块重分类审计汇总报告

> 日期：2026-06-20  
> 范围：`agent_master_paper_list.md` confirmed 记录序号 340-451。  
> 对应计划：`Coverage_Check/multi_module_reclassification_flat_batch_plan_451_confirmed_2026-06-20.md`。  
> 覆盖报告：`multi_module_reclassification_batch4_waveA_2026-06-20.md` 与 `multi_module_reclassification_batch4_waveB_2026-06-20.md`。  
> 当前阶段：Batch 4 已完成 Reviewer 审核与主控合并；本批不修改主列表。
> 口径提示：本批次生成于较保守的第一轮审计中，以下结论保留为历史基线。后续执行应以 `classification_policy_relaxation_addendum_2026-06-20.md` 和当前规则文件为准：只要有可识别的具体对象实验、验证、benchmark task、case study 或结果报告，即可记录对应模块，不要求构成核心科学贡献。

## 一、批次基线

Batch 4 开始前主列表状态：

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

## 二、完成情况

| Wave | Reviewed records | Reviewer-covered records | 主控状态 |
|---|---:|---:|---|
| Wave A | 56 | 56 | 已完成 |
| Wave B | 56 | 56 | 已完成 |
| Batch 4 total | 112 | 112 | 已完成 |

本批 112 条均已由只读 Reviewer 覆盖，并由主控按统一口径合并。Reviewer 均未编辑 `agent_master_paper_list.md`。

## 三、本批已落地主列表改动

本批无已落地主列表改动。

| Change type | Count |
|---|---:|
| add_module | 0 |
| move_primary | 0 |
| move_to_01.04 | 0 |
| demote/background-review candidate | 0 |

原因：本批潜在变更主要属于全文证据补强、二级位点复核、平台 demo 权重、Note / master trace 冲突，或需等待 row-level schema migration 后统一处理，不满足直接改表条件。

## 四、批次统计

| Metric | Count |
|---|---:|
| reviewed records | 112 |
| unchanged by 主控 | 112 |
| add_module | 0 |
| move_primary | 0 |
| move_to_01.04 | 0 |
| demote/background-review candidate | 0 |
| main-control / full-text follow-up queue | 33 |
| records with `full_text_required=yes` from Reviewer output | 32 |

本批不修改 `agent_master_paper_list.md`。批次后主列表 record-level confirmed count 仍为 `451`，`needs_review` 仍为 `0`，confirmed `08` 仍为 `3`。

## 五、Batch 4 主要口径校准

1. 本批在当时较保守口径下未发现高置信 multi-module assignment。跨领域 benchmark、platform demo、多工具 workflow、跨数据集验证不会因系统自称通用而自动多模块；但若其中某项 demo / benchmark / case study 可明确对应具体科学对象并报告结果，后续应按新口径记录对应模块。
2. `01.04` 在 Batch 4 中继续作为独立 general-method bucket。Science Earth、SciDER、AutoDiscovery、goal-evolving agents、equation-discovery agents 和 Denario 等记录在本批历史审计中暂保持 `01.04`；后续需按新口径重新检查其是否包含具体对象实验、验证、benchmark task、case study 或结果报告。
3. `03 / 07` 是 Batch 4 最强边界之一。通用分子优化、synthetic pathway、chemical language model 保持 `03`；drug response、drug lead optimization、target-pocket / protein-conditioned drug design 保持 `07`。
4. `03 / 04` 边界继续按对象处理。organic emitters、continuous-flow chemistry、adsorption configuration 保持 `03`；semiconductor mobility、redox-flow-battery negolyte、COF、heterogeneous catalyst material 保持 `04`。
5. `05 / 10` 再次验证：rover mission operations / Mars rover autonomous science 保持 `10`；EO-1 火山、冰冻圈、洪水监测以地球环境过程为对象，保持 `05`。
6. `11.07 / 01.04` 边界保持稳定。paper writing、peer review、scientific evaluation、scientific ecosystem、phenotype ontology curation 是 scientific knowledge production；general research assistant 或 equation-discovery benchmark 不自动转 `11.07`。
7. equation discovery 需分开：formal systems / governing-law recovery 可保留 `01.03`，无具体对象实验的 general equation-discovery frameworks 继续留 `01.04`。
8. 当前没有足够证据支持重构一级分类，问题主要集中在边界解释与低覆盖类稀缺性判断。

## 六、Batch 4 后续复核队列

Batch 4 暂列以下 33 条为后续全文或主控复核队列，均暂不改表。

| ID | 当前 legacy | 主要复核点 | 暂定处理 |
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
| `ASD-0811` | `04 / 04.04` | battery negolyte 的 `03 / 04` 边界与全文证据 | 暂保持 `04` |
| `ASD-0813` | `06 / 06.03` | ELISA agent-threshold / core-strength | 暂保持 `06` |
| `ASD-0818` | `03 / 03.04` | broad molecular optimization 的 `03 / 07` 边界 | 暂保持 `03` |
| `ASD-0820` | `03 / 03.04` | synthesizable lead optimization 的高风险 `03 / 07` 边界 | 暂保持 `03` |
| `ASD-0830` | `02 / 02.02` | BESIII real-world physics analysis 细节补强 | 暂保持 `02` |
| `ASD-0831` | `11 / 11.07` | phenotype ontology curation 的 `11.07 / 06` 边界证据补强 | 暂保持 `11.07` |
| `ASD-0832` | `03 / 03.03` | catalyst discovery evidence based on abstract/note package | 暂保持 `03` |
| `ASD-0833` | `06 / 06.03` | virtual-cell mechanistic reasoning evidence depth | 暂保持 `06` |
| `ASD-0838` | `03 / 03.03` | continuous-flow chemistry full-text/source strength | 暂保持 `03` |
| `ASD-0844` | `01 / 01.04` | Science Earth demos 是否包含可识别的生命科学、复杂系统或物理对象实验 / case study / 结果报告 | legacy 暂保持 `01.04`，新口径下优先复核 `06` 与 `01.03 / 02` |
| `ASD-0850` | `01 / 01.02` | OR-Agent Note 与主列表 trace 冲突；需统一证据记录 | 暂保持 `01.02` |
| `ASD-0855` | `11 / 11.07` | peer-review framework 实证强度 | 暂保持 `11.07` |
| `ASD-0856` | `01 / 01.04` | AutoDiscovery cross-dataset demos 是否仅为 benchmark | 暂保持 `01.04` |
| `ASD-0863` | `02 / 02.02` | HEP workflow detail | 暂保持 `02` |
| `ASD-0864` | `02 / 02.02` | support-tooling / discovery-strength boundary | 暂保持 `02` |
| `ASD-0866` | `01 / 01.04` | cross-domain cases 是否有可识别对象层实验、验证、case study 或结果报告 | 暂保持 `01.04` |
| `ASD-0871` | `01 / 01.04` | Denario project 是否仍为 general research assistant；`01.04 / 11.07` 边界 | 暂保持 `01.04` |

## 七、批次后状态

Batch 4 结束后，主列表未发生行级修改：

- confirmed record-level count: 451
- `needs_review`: 0
- confirmed `08`: 3
- legacy confirmed `01.04`: 46
- legacy confirmed 主类分布仍保持本报告第一节所列基线

由于本轮仍未进行 row-level schema migration，`scientific_object_modules` 的正式 assignment count 暂不写入主列表；后续应在 451 条全部复核完成后，统一从审计报告与迁移字段生成模块 assignment count。
