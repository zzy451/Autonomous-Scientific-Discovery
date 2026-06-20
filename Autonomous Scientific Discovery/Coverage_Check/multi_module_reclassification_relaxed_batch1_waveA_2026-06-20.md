# Batch 1 / Wave A relaxed 多模块重分类审计报告

> 日期：2026-06-20  
> 范围：`agent_master_paper_list.md` confirmed 记录序号 1-57。  
> 对应计划：`Coverage_Check/multi_module_reclassification_relaxed_round_plan_451_confirmed_2026-06-20.md`。  
> 本文件是当前 relaxed 口径下的新一轮审计产物；此前保守试跑结论不再作为本轮分类依据。

## 一、执行口径

本轮采用 relaxed multi-module rule：

- 只要论文对某一科学领域的具体对象做了可识别实验、验证、benchmark task、case study 或结果报告，就可以记录对应 `01-11` 科学对象模块。
- 不要求被记录模块构成论文核心贡献。
- 不因论文自称 general / cross-domain / platform 自动多模块；必须能写出对象层证据。
- `01.04` 只作为独立 general-method bucket，用于没有任何具体科学对象实验、验证、benchmark task、case study 或结果报告的 ASD / general research-agent 方法文献。
- 本 wave 不直接修改 `agent_master_paper_list.md`；原因是主列表 row-level schema migration 尚未完成，当前旧字段仍是 legacy filing display。

## 二、基线与覆盖

本轮开始前主列表头部基线：

| 指标 | 当前值 |
|---|---:|
| `candidate` | 0 |
| `to_read` | 451 |
| `background_only` | 370 |
| `excluded` | 50 |
| `needs_review` | 0 |
| legacy confirmed included-and-classified count | 451 |
| confirmed `08` count | 3 |

Wave A 覆盖情况：

| Reviewer | 记录数 | 分配 ID |
|---|---:|---|
| A-Reviewer-1 | 15 | `ASD-0001`, `ASD-0002`, `ASD-0003`, `ASD-0004`, `ASD-0005`, `ASD-0006`, `ASD-0007`, `ASD-0008`, `ASD-0009`, `ASD-0010`, `ASD-0012`, `ASD-0013`, `ASD-0014`, `ASD-0016`, `ASD-0017` |
| A-Reviewer-2 | 14 | `ASD-0018`, `ASD-0019`, `ASD-0020`, `ASD-0022`, `ASD-0024`, `ASD-0025`, `ASD-0026`, `ASD-0028`, `ASD-0029`, `ASD-0030`, `ASD-0031`, `ASD-0032`, `ASD-0033`, `ASD-0034` |
| A-Reviewer-3 | 14 | `ASD-0035`, `ASD-0036`, `ASD-0037`, `ASD-0038`, `ASD-0040`, `ASD-0041`, `ASD-0044`, `ASD-0045`, `ASD-0046`, `ASD-0047`, `ASD-0048`, `ASD-0049`, `ASD-0051`, `ASD-0052` |
| A-Reviewer-4 | 14 | `ASD-0053`, `ASD-0054`, `ASD-0055`, `ASD-0056`, `ASD-0057`, `ASD-0058`, `ASD-0059`, `ASD-0060`, `ASD-0061`, `ASD-0062`, `ASD-0063`, `ASD-0064`, `ASD-0065`, `ASD-0068` |

四个只读 Reviewer 均已完成，57 / 57 条覆盖。Reviewer 未编辑任何项目文件。

## 三、主控裁决表

| ID | Legacy filing | 本轮建议模块 / bucket | 主控裁决 | 证据摘要 | 置信度 | 是否需全文 |
|---|---|---|---|---|---|---|
| `ASD-0001` | `04 / 04.04` | `04` | 保持 `04` | crystal structures, bandgap, stability, materials datasets | high | no |
| `ASD-0002` | `07 / 07.04` | `07` | 保持 `07` | EHR / clinical / healthcare research tasks | high | no |
| `ASD-0003` | `03 / 03.04` | `03;04` | 记录 `04` add-module 候选，不改表 | chemistry tasks plus materials-tool / pymatgen benchmark evidence | medium | no |
| `ASD-0004` | `01 / 01.04` | `01` | 记录离开 `01.04` 候选，不改表 | AI / computational research tasks with code experiments and results | medium | no |
| `ASD-0005` | `03 / 03.04` | `03` | 保持 `03` | robotic chemistry experiments / autonomous chemical workflow | medium | yes |
| `ASD-0006` | `06 / 06.03` | uncertain / possible `01.04` | 主控复核队列 | local evidence does not verify concrete biology object experiments | low | yes |
| `ASD-0007` | `04 / 04.04` | `04` | 保持 `04` | materials hypotheses from material design goals and constraints | high | no |
| `ASD-0008` | `07 / 07.04` | `07;03` | 记录 `03` add-module 候选，不改表 | DMTA / drug discovery plus synthesis and HPLC chemistry workflow | medium | no |
| `ASD-0009` | `04 / 04.04` | `04` | 保持 `04` | MOFs, solid-state impurity doping, materials literature datasets | high | no |
| `ASD-0010` | `03 / 03.04` | `03` | 保持 `03` | molecules, pKa, excited states, lanthanoid complex, QC calculations | high | no |
| `ASD-0012` | `03 / 03.04` | `03` | 保持 `03` | robot-executed solubility and recrystallization chemistry experiments | high | no |
| `ASD-0013` | `01 / 01.04` | `01` | 记录离开 `01.04` 候选，不改表 | ML / AI research code experiments and workshop-level automated discovery | medium | no |
| `ASD-0014` | `06 / 06.03` | `06`, possible `07` | 保持 `06`，列入 `06/07` 低强度复核 | spatial transcriptomics, tissue niches, cell-cell communication | medium | yes |
| `ASD-0016` | `04 / 04.04` | `04` | 保持 `04` | autonomous lab for accelerated materials synthesis | high | yes |
| `ASD-0017` | `07 / 07.04` | `07` | 保持 `07` | pharmaceutical virtual screening / drug discovery pipeline | high | no |
| `ASD-0018` | `01 / 01.04` | `01.04` bucket | 保持独立 `01.04` | general research assistant workflow; MLE-Bench is capability validation | high | no |
| `ASD-0019` | `01 / 01.04` | `01.04` bucket | 保持独立 `01.04` | collaborative autonomous research platform; reasoning benchmarks not object experiments | high | no |
| `ASD-0020` | `06 / 06.03` | `06` | 保持 `06` | genes, genetic perturbations, cellular phenotypes | high | no |
| `ASD-0022` | `03 / 03.04` | `03` | 保持 `03` | molecules, reactions, thermochemistry, atomistic simulations | high | no |
| `ASD-0024` | `07 / 07.04` | `07` | 保持 `07` | drug candidates, target proteins, ADMET / lead-like properties | high | no |
| `ASD-0025` | `03 / 03.04` | `03` | 保持 `03` | small molecules, descriptors, ADME / drug-likeness filters as cheminformatics tasks | high | no |
| `ASD-0026` | `04 / 04.04` | `04` | 保持 `04` | graphene, HOPG, AFM images, material surface / mechanical properties | high | no |
| `ASD-0028` | `07 / 07.04` | `07` | 保持 `07` | ADMET, DTI, HTS drug-discovery ML tasks | high | no |
| `ASD-0029` | `03 / 03.04` | `03` | 保持 `03` | molecular design, captioning, reaction prediction, property prediction | high | no |
| `ASD-0030` | `07 / 07.04` | `07` | 保持 `07` | drug-target prediction, biological activity prediction | high | no |
| `ASD-0031` | `04 / 04.04` | `04` | 保持 `04` | inorganic / crystal materials, band gap, formation energy | high | no |
| `ASD-0032` | `01 / 01.04` | uncertain: `01` vs `01.04` | 主控复核队列 | code experiments in agents / virtual environments may be formal-computational object evidence | medium | yes |
| `ASD-0033` | `06 / 06.03` | `06`, possible `07` | 保持 `06`，低优先复核 `07` | single-cell omics, DEGs, pathways, disease mechanisms | medium-high | no |
| `ASD-0034` | `06 / 06.03` | `06` | 保持 `06`，列入全文补证 | Perturb-seq, genes, cell phenotypes, RNA profiles | medium | yes |
| `ASD-0035` | `04 / 04.04` | `04` | 保持 `04`，列入额外对象复核 | bioinspired materials and materials-discovery hypotheses | medium | yes |
| `ASD-0036` | `03 / 03.03` | `03` | 保持 `03` | solubility, pH, recrystallization, quinone redox / electrochemistry | high | no |
| `ASD-0037` | `03 / 03.03` | `03` | 保持 `03`，列入全文补证 | robotic exploratory synthetic chemistry | medium | yes |
| `ASD-0038` | `03 / 03.04` | `03` | 保持 `03` | chemical reaction extraction benchmark with reactants, products, yields | high | no |
| `ASD-0040` | `01 / 01.04` | `01.04` bucket | 保持独立 `01.04` | general research idea generation; no concrete object experiment | high | no |
| `ASD-0041` | `07 / 07.04` | `07` | 保持 `07` | clinically relevant protein targets and small-molecule drug candidates | high | no |
| `ASD-0044` | `02 / 02.01` | `02` | 保持 `02` | cosmological simulations, galaxy formation, large-scale structure parameters | high | no |
| `ASD-0045` | `04 / 04.04` | `04` | 保持 `04` | materials-science QA and materials-specific tool / knowledge tasks | high | no |
| `ASD-0046` | `04 / 04.04` | `04` | 保持 `04` | topological materials, crystal structures, SrSbO3, DFT validation | high | no |
| `ASD-0047` | `09 / 09.01` | `09` | 保持 `09` | CFD / OpenFOAM engineering simulation workflows | high | no |
| `ASD-0048` | `01 / 01.04` | `01` | 记录离开 `01.04` 候选，不改表 | ML / AI benchmark tasks and closed-loop code experiments with results | medium | no |
| `ASD-0049` | `06 / 06.03` | `06` | 保持 `06`，列入全文补证 | scRNA-seq data and bioinformatics workflow evidence | medium | yes |
| `ASD-0051` | `06 / 06.03` | `06` | 保持 `06` | gene sets, gene functions, biological processes, melanoma gene sets | high | no |
| `ASD-0052` | `09 / 09.01` | `09` | 保持 `09` | finite element analysis / linear elasticity engineering simulation | high | no |
| `ASD-0053` | `01 / 01.04` | `01.04` bucket | 保持独立 `01.04` | toy ML hypothesis-verification task; no concrete science object | high | no |
| `ASD-0054` | `07 / 07.04` | `07;06` | 记录 `06` add-module 候选，不改表 | SARS-CoV-2 nanobody therapeutic candidates with wet-lab binding validation | medium-high | no |
| `ASD-0055` | `06 / 06.03` | `06`, possible `07` | 保持 `06`，列入全文补证 | omics modalities and automated bioinformatics workflow tasks | medium | yes |
| `ASD-0056` | `03 / 03.04` | `03;04` | 记录 `04` add-module 候选，不改表 | organic laser emitters combine molecular chemistry and optoelectronic material-performance evidence | medium | yes |
| `ASD-0057` | `09 / 09.04` | `09` | 保持 `09` | chemical manufacturing process, PFD / PID, simulator-validated process cases | high | no |
| `ASD-0058` | `02 / 02.01` | `02` | 保持 `02` | meteorites, sample-return / soil mass spectra, astrobiological hypotheses | high | no |
| `ASD-0059` | `01 / 01.04` | `01.04` bucket | 保持独立 `01.04` | generic hypothesis-quality benchmark; no object-level scientific result | high | no |
| `ASD-0060` | `01 / 01.04` | `04;06` | 记录离开 `01.04` 与新增 `04/06` 候选，不改表 | nanomaterials, biomolecules and superconductors benchmark / evaluator tasks | medium | yes |
| `ASD-0061` | `03 / 03.04` | `03` | 保持 `03` | QM9 molecules and quantum-chemistry molecular-property benchmarks | high | no |
| `ASD-0062` | `01 / 01.04` | uncertain: `01.04` vs `04/02` | 主控复核队列 | materials / astronomy case studies may be substrate demos or object-level results | medium | yes |
| `ASD-0063` | `01 / 01.02` | `01` | 保持正式 `01` | algorithms, programs, matrix multiplication, constructive mathematics | high | no |
| `ASD-0064` | `06 / 06.03` | `06;07` | 记录 `07` add-module 候选，不改表 | spatial transcriptomics plus cancer clinical-phenotype / tumor microenvironment cases | medium | no |
| `ASD-0065` | `04 / 04.04` | `04` | 保持 `04` | energy-storage ceramics and solid-state sintering / materials workflow | high | no |
| `ASD-0068` | `04 / 04.04` | `04` | 保持 `04` | photonic metamaterials and all-dielectric metasurface inverse design | high | no |

## 四、Wave A 统计

| Metric | Count |
|---|---:|
| reviewed records | 57 |
| Reviewer-covered records | 57 |
| high / medium stable single-module or bucket records | 38 |
| relaxed add-module candidates | 6 |
| `01.04` exit candidates | 4 |
| uncertain `01.04` / object-module boundary cases | 3 |
| records with `full_text_required=yes` | 13 |
| direct master-list edits | 0 |

按本轮建议模块展开统计如下。此表是 Wave A 审计建议，不是当前主列表正式计数。

| Suggested module / bucket | Wave A count |
|---|---:|
| `01` | 4 |
| `02` | 2 |
| `03` | 13 |
| `04` | 14 |
| `06` | 10 |
| `07` | 9 |
| `09` | 3 |
| independent `01.04` bucket, high-confidence | 5 |
| uncertain: `01.04` / object-module boundary | 3 |

说明：`ASD-0006`, `ASD-0032`, `ASD-0062` 暂不纳入模块展开计数，因为证据不足以稳定判定；它们进入主控复核队列。

## 五、关键变化相对前一轮保守试跑

此前保守试跑在这一切片上基本没有记录新增模块或离开 `01.04` 的迁移压力；在当前 relaxed 口径下，这个结论不再可作为本轮判断依据。

本轮新增的主要迁移压力如下：

| 类型 | ID | 当前判断 |
|---|---|---|
| `03 -> 03;04` | `ASD-0003`, `ASD-0056` | materials / optoelectronic material-performance evidence 需要纳入候选模块 |
| `07 -> 07;03` | `ASD-0008` | DMTA 中的 synthesis / HPLC chemistry workflow 需要主控确认是否足以记录 `03` |
| `07 -> 07;06` | `ASD-0054` | SARS-CoV-2 nanobody design 同时有 biomedical therapeutic 和 protein / biological-object evidence |
| `06 -> 06;07` | `ASD-0064` | cancer phenotype / tumor microenvironment case 支持医学模块候选 |
| `01.04 -> 01` | `ASD-0004`, `ASD-0013`, `ASD-0048` | code / ML / AI computational experiments 可能构成正式 `01` 对象证据 |
| `01.04 -> 04;06` | `ASD-0060` | nanomaterials / biomolecules benchmark tasks 在 relaxed 口径下构成对象层候选证据 |

## 六、待复核队列

| ID | 当前 legacy | 复核问题 | 建议下一步 |
|---|---|---|---|
| `ASD-0003` | `03 / 03.04` | materials benchmark split 是否足以新增 `04` | 看 note / full text 中 materials task 是否有独立对象结果 |
| `ASD-0004` | `01 / 01.04` | general InternAgent 是否已有 formal / computational research-object experiments | 复核 12 个 research tasks 是否是 `01` 对象实验还是 workflow demo |
| `ASD-0006` | `06 / 06.03` | DORA AI Scientist 的生命科学对象证据不足 | 若无具体对象 case，应迁入 independent `01.04` bucket |
| `ASD-0008` | `07 / 07.04` | DMTA 中 synthesis / HPLC 是否构成 `03` 实验覆盖 | 复核 chemistry workflow 是否有对象层结果 |
| `ASD-0013` | `01 / 01.04` | AI Scientist-v2 的 ML / code experiments 是否足以记录正式 `01` | 复核实验对象是否是 AI / computational research itself |
| `ASD-0014` | `06 / 06.03` | spatial biology 中疾病 / 临床转化证据是否足以新增 `07` | 低优先级全文复核 |
| `ASD-0032` | `01 / 01.04` | CodeScientist 是 formal-computational object study 还是 general ASD workflow | 主控全文复核 |
| `ASD-0033` | `06 / 06.03` | precision medicine framing 是否足以新增 `07` | 暂保持 `06`，低优先复核 |
| `ASD-0034` | `06 / 06.03` | Perturb-seq 轮次与指标需补证 | 保持 `06`，补全文证据 |
| `ASD-0035` | `04 / 04.04` | SciAgents 是否除材料外还有生物对象 case | 保持 `04`，全文复核额外模块 |
| `ASD-0037` | `03 / 03.03` | synthetic chemistry full-text evidence pending | 保持 `03`，补全文证据 |
| `ASD-0048` | `01 / 01.04` | Dolphin 是否应从 independent `01.04` 转正式 `01` | 复核 ML / AI benchmark 是否是对象层实验而非通用 demo |
| `ASD-0049` | `06 / 06.03` | BIA 的 scRNA-seq / bioinformatics case 需全文确认 | 保持 `06` 倾向 |
| `ASD-0054` | `07 / 07.04` | 是否应新增 `06` protein / nanobody design module | 复核 wet-lab validation 的 biological-object framing |
| `ASD-0055` | `06 / 06.03` | BioMaster 是否含 clinical / patient omics 场景 | 保持 `06`，全文复核是否加 `07` |
| `ASD-0056` | `03 / 03.04` | organic laser emitters 的材料性能对象是否足以新增 `04` | `03/04` 边界重点复核 |
| `ASD-0060` | `01 / 01.04` | PiFlow 的 nanomaterials / biomolecules benchmark 是否应使其离开 `01.04` | 高优先级复核，旧口径残留风险高 |
| `ASD-0062` | `01 / 01.04` | federated workflow case studies 是否报告 concrete object results | 若只是 substrate demo，保留 `01.04`；若有对象结果，记录 `04/02` |
| `ASD-0064` | `06 / 06.03` | cancer phenotype / clinical metadata 是否足以新增 `07` | `06/07` 边界复核 |

## 七、主控结论

Batch 1 / Wave A 已按 relaxed multi-module 口径完成新一轮复核。与旧保守报告相比，本轮明确发现多个 add-module 与 `01.04` exit 候选，但由于主列表 schema 尚未迁移，本 wave 只写入审计报告，不直接改旧 `Main class / Secondary class` 字段。

本 wave 不支持重构 `01-11` 一级体系；真正需要处理的是 row-level schema migration，以及把 `01.04` 从 legacy filing 解释中彻底拆出。
