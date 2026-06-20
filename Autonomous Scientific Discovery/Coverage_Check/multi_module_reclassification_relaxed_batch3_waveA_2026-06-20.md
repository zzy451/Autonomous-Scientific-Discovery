# Batch 3 / Wave A relaxed multi-module reclassification audit

> 日期：2026-06-20  
> 范围：`ASD-0601` 到 `ASD-0673` 中当前 confirmed / `to_read` 的 Batch 3 / Wave A 记录。  
> 口径：本轮不把旧 Notes 当作最终依据；旧 note 只作为定位线索。分类判断优先参考 arXiv / DOI / publisher abstract / PDF / project page 等一手或权威来源。  
> 主列表说明：`agent_master_paper_list.md` 仍处于 legacy schema 阶段，本轮不直接覆盖 `Main class` / `Secondary class` 字段；已确认事实写入 Notes、审计报告和 `Remarks`。

## 1. 执行概况

| 指标 | 数量 |
|---|---:|
| 本 wave 计划复核 confirmed records | 57 |
| high-confidence relaxed classification changes | 3 |
| high-confidence stable / unchanged records | 45 |
| medium / full-text-required queue | 9 |
| 本轮同步更新 Notes | 3 |
| 本轮同步更新 Batch 3 / Wave A 主列表 Remarks | 3 |
| 顺手补写 Batch 2 / Wave A 主列表 Remarks | 6 |
| 本轮直接修改 legacy `Main class` / `Secondary class` | 0 |

主控合并原则：

- 只合并有一手来源或权威摘要支持、且与当前 relaxed object-coverage rule 一致的 high-confidence 变更。
- `notes_only`、metadata-only、或仍依赖 full text 的候选变更不强行写入分类事实，只进入后续复核队列。
- high-confidence 分类变化同步写入对应 Notes；medium / low-confidence 记录不抢先修改 note。

## 2. High-confidence 变更

| ID | 题名 | legacy filing | relaxed modules | primary filing | 结论 | note |
|---|---|---|---|---|---|---|
| `ASD-0663` | AutoScientists: Self-Organizing Agent Teams for Long-Running Scientific Experimentation | `01 / 01.04` | `01;06;07` | `06` | arXiv abstract 报告 LM-training optimization、BioML-Bench、ProteinGym、biomedical imaging、protein engineering、single-cell omics、drug discovery 等具体任务；不能继续仅作为 independent `01.04`。 | updated |
| `ASD-0669` | MARBLE: Multi-Agent Reasoning for Bioinformatics Learning and Evolution | `06 / 06.03` | `06;07` | `06` | spatial transcriptomics / bioinformatics model-refinement 支持 `06`，drug-target interaction 和 drug-response prediction 支持 `07`。 | updated |
| `ASD-0673` | Harnessing AtomisticSkills for Agentic Atomistic Research | `01 / 01.04` | `03;04;07` | `04` | abstract 明确列出 Li-ion electrolytes、MOFs for CO2 capture、drug virtual screening、XRD/materials tasks、Fe-oxide OER catalyst campaigns；平台感不能覆盖具体对象实验。 | updated |

## 3. 已同步修订 Notes

| ID | Note path | 修订内容 |
|---|---|---|
| `ASD-0663` | `Notes/01_Formal_Information_and_Computational_Sciences/Unknown_2026_AutoScientists.md` | 新增 `2026-06-20 relaxed multi-module revision`，记录 `scientific_object_modules=01;06;07`、`primary_module_for_filing=06`、`general_method_bucket=none`。 |
| `ASD-0669` | `Notes/06_Life_Sciences/Kim_2026_MARBLE.md` | 新增 relaxed 多模块修订，记录 `scientific_object_modules=06;07`，保留 `06` 为 primary filing。 |
| `ASD-0673` | `Notes/01_Formal_Information_and_Computational_Sciences/Deng_2026_AtomisticSkills.md` | 新增 relaxed 多模块修订，记录 `scientific_object_modules=03;04;07`、`primary_module_for_filing=04`、`general_method_bucket=none`。 |

## 4. 待 full-text / 主控复核队列

| ID | 当前倾向 | 队列原因 |
|---|---|---|
| `ASD-0609` | possible `03;09` | pH adjustment / process-control 可能触发工程过程模块，但需要 full-text 确认对象层证据。 |
| `ASD-0651` | possible `05;06;11` | heatwave bio-ecological / socioeconomic cascading risk 可能跨环境、生命和社会风险对象，需 full-text。 |
| `ASD-0659` | possible `04;06;07` | 当前证据不足以确认每个对象模块均有可识别任务。 |
| `ASD-0660` | possible `03;04;06` | S1-NexusAgent abstract 提到 BioMini-Eval、ChemBench、MatSciBench，但具体对象任务和结果仍需 full text。 |
| `ASD-0662` | keep `01.04` for now | abstract 未给出足够 concrete object experiments；暂不迁出 independent `01.04`。 |
| `ASD-0664` | possible add `04` to `03` | computational catalysis / MatBench / materials foundation 边界需要 full-text 支撑。 |
| `ASD-0665` | possible `03;04` | 化学 / 材料双对象证据仍不足以 high-confidence 合并。 |
| `ASD-0668` | possible `04;06` | 材料与生物对象是否均构成实验覆盖需继续核对。 |
| `ASD-0671` | keep `01.04` for now | abstract 缺少具体对象实验细节；暂不迁出 independent `01.04`。 |

## 5. 主列表与统计更新

本轮已在 `agent_master_paper_list.md` 做两类更新：

1. 为 `ASD-0663`、`ASD-0669`、`ASD-0673` 追加 `RelaxedMultiModule2026-06-20` 备注。
2. 回填 Batch 2 / Wave A 中已确认但尚未写入主列表备注的 `ASD-0254`、`ASD-0385`、`ASD-0447`、`ASD-0510`、`ASD-0522`、`ASD-0523`。

顶部统计新增 partial overlay，不覆盖 legacy filing counts：

| Scientific object module | Expanded assignment count |
|---|---:|
| `01` | 46 |
| `02` | 29 |
| `03` | 64 |
| `04` | 98 |
| `05` | 23 |
| `06` | 61 |
| `07` | 58 |
| `08` | 3 |
| `09` | 35 |
| `10` | 23 |
| `11` | 31 |

| Relaxed-counting metric | Count |
|---|---:|
| Record-level confirmed included-and-classified count | 451 |
| Expanded module assignment count | 471 |
| Independent `01.04` general-method bucket count after accepted relaxed migrations | 40 |

## 6. 主控结论

Batch 3 / Wave A 的关键校准点是：平台型、通用型或 cross-domain agentic system 只要在原文摘要或全文中给出了具体科学对象任务、benchmark task、case study 或结果报告，就不能继续仅凭“通用平台”叙事留在 independent `01.04`。但 medium/full-text 队列仍不能因为标题或跨域表述而强行多模块化，必须等到对象层证据足够清楚再修 note 和主列表。

