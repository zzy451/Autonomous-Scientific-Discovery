# Batch 01 多模块分类 / Note / PDF 全量复核报告

生成日期：`2026-06-21`  
复核范围：主列表平铺位置 `11-30`，对应 `ASD-0012` - `ASD-0035`  
复核模式：`Batch 01`；严格以 `agent_master_paper_list.md` 当前 confirmed core 平铺顺序推进，不以 `Notes/` 反控主流程

## 1. 本轮开始前基线

- confirmed included + classified count：`451`
- needs_review count：`0`
- `08` 类 confirmed count：`3`
- module assignment counts：`528`；对应当前全库重算分布为 `01=20, 02=37, 03=83, 04=110, 05=35, 06=74, 07=70, 08=3, 09=37, 10=24, 11=35`
- independent `01.04` bucket count：全库当前重算为 `18`；本批未新增独立 `01.04` 记录
- 主要边界压力点：`01.04 / 01`、`03 / 04`、`06 / 07`、`04 / 09`、source-limited PDF 获取

## 2. 本轮已落地主列表改动

| ID | 题名 | 原状态 / 原模块或 `01.04` bucket | 新状态 / 新模块或 `01.04` bucket | primary_module_for_filing | 处理结论 | 理由 |
|---|---|---|---|---|---|---|
| ASD-0012 | Large language models for chemistry robotics | `to_read`; legacy `03` | 保持 `03` | `03` | 更新 remarks；不伪造 PDF | Springer HTML 全文和 CLAIRify 官方页已足够支持 chemistry-robotics 对象；本地环境下 Springer PDF 仍被 challenge 阻断 |
| ASD-0013 | The ai scientist-v2: Workshop-level automated scientific discovery via agentic tree search | `to_read`; legacy `01/01.04` | 保持 `01` | `01` | 归档 arXiv PDF；note 去除独立 `01.04` 旧口径 | 机器学习研究任务、代码实验和自动生成 ML manuscript 属于具体 formal/computational research objects |
| ASD-0014 | Spatialagent: An autonomous ai agent for spatial biology | `to_read`; legacy `06` | 保持 `06` | `06` | 更新 note/master；保留 full-text follow-up | Crossref DOI 摘要 + 官方 GitHub README 支持空间生物学 / spatial omics `06`；当前无足够一手证据新增独立 `07` |
| ASD-0016 | An autonomous laboratory for the accelerated synthesis of novel materials | `to_read`; legacy `04` | 保持 `04` | `04` | 归档 author-hosted PDF；重写 note | 一手全文稳定支持材料对象；同时纠正标题，保持 canonical title 为 `An autonomous laboratory for the accelerated synthesis of novel materials` |
| ASD-0017 | Can ai agents design and implement drug discovery pipelines? | `to_read`; legacy `07` | 保持 `07` | `07` | 归档 arXiv PDF；更新 note 头部证据 | 一手全文仍稳定落在药物发现对象，不支持回退 `01.04` 或外扩其他模块 |
| ASD-0018 | Agent laboratory: Using llm agents as research assistants | `to_read`; legacy `01/01.04` | 保持 `01` | `01` | 归档 PDF；清理旧 `01.04` 表述 | 机器学习研究工作流与代码实验支持具体 `01` 对象，不再接受独立 `01.04` 处理 |
| ASD-0019 | Agentrxiv: Towards collaborative autonomous research | `to_read`; legacy `01/01.04` | 保持 `01` | `01` | 归档 PDF；清理旧 `01.04` 表述 | `MedQA` 仅是迁移 benchmark 证据，不足以独立扩为 `07`；主体仍是 formal/computational research workflow |
| ASD-0020 | Biodiscoveryagent: An ai agent for designing genetic perturbation experiments | `to_read`; legacy `06` | 保持 `06` | `06` | 归档 arXiv PDF；补齐 note 头部 PDF 信息 | genetic perturbation experiments 稳定支持生命科学对象 |
| ASD-0022 | Chemgraph: An agentic framework for computational chemistry workflows | `to_read`; legacy `03` | 保持 `03` | `03` | 归档 arXiv PDF；在 remarks 中明确不增 `04` | 当前全文证据仍只稳定支持 computational chemistry `03` |
| ASD-0024 | Large language model agent for modular task execution in drug discovery | `to_read`; legacy `07` | 调整为 `07;03` | `07` | 落地多模块；更新 note/master | 药物发现 pipeline、binding-affinity、protein-ligand 任务支持 `07`；seed-molecule generation、molecular refinement、drug-/lead-likeness 任务独立支持 `03` |
| ASD-0025 | Cactus: Chemistry agent connecting tool usage to science | `to_read`; legacy `03` | 保持 `03` | `03` | 归档本地 PDF；note 同步 PDF 路径 | 当前证据稳定支持 chemistry-agent 对象，不新增其他模块 |
| ASD-0026 | Autonomous microscopy experiments through large language model agents | `to_read`; legacy `04` | 调整为 `04;09` | `04` | 落地多模块；更新 note/master | 材料样品与 AFM 表征支持 `04`；AFMBench 和真实 AFM 仪器操作任务独立支持 `09` |
| ASD-0028 | Drugagent: Automating ai-aided drug discovery programming through llm multi-agent collaboration | `to_read`; legacy `07` | 保持 `07` | `07` | 归档 arXiv PDF；补齐 note 头部 PDF 信息 | 主体仍是 drug discovery programming，对象稳定在 `07` |
| ASD-0029 | Chemhas: Hierarchical agent stacking for enhancing chemistry tools | `to_read`; legacy `03` | 保持 `03` | `03` | 归档 arXiv PDF；保留 title/version 备注 | arXiv PDF 标题为 `ChemAmp`，但当前一手全文仍稳定支持 chemistry `03` |
| ASD-0030 | Rag-enhanced collaborative llm agents for drug discovery | `to_read`; legacy `07` | 调整为 `03;07` | `07` | 落地多模块；更新 note/master | drug-target / biological-activity 任务支持 `07`；molecular captioning 与 MoleculeNet/MLSMR 分子任务支持 `03` |
| ASD-0031 | Llmatdesign: Autonomous materials discovery with large language models | `to_read`; legacy `04` | 保持 `04` | `04` | 归档 arXiv PDF；补齐 note 头部 PDF 信息 | 材料发现对象稳定 |
| ASD-0032 | Codescientist: End-to-end semi-automated scientific discovery with code-based experimentation | `to_read`; legacy `01/01.04` | 保持 `01` | `01` | 归档 PDF；清理 note 中残留 `01.04` 旧口径 | 代码实验、软件工件、任务/指标发现都属于具体 formal/computational 对象 |
| ASD-0033 | Omnicellagent: Towards ai co-scientists for scientific discovery in precision medicine | `to_read`; legacy `06` | 保持 `06` | `06` | 更新 remarks；note 暂不重写 | PMC HTML 全文足以稳定支持 single-cell / omics `06`；precision-medicine 表面 framing 不足以新增 `07` |
| ASD-0034 | Perturboagent: A self-planning agent for boosting sequential perturb-seq experiments | `to_read`; legacy `06` | 保持 `06` | `06` | 成功归档 raw PMLR PDF；note 从 metadata-only 收紧为 PDF-backed | functional genomics / perturbation biology `06` 稳定；当前证据不支持新增 `07` |
| ASD-0035 | Sciagents: automating scientific discovery through bioinspired multi-agent intelligent graph reasoning | `to_read`; legacy `04` | 保持 `04` | `04` | 确认本地 PDF 归档；更新 remarks | biologically inspired materials 仍属材料对象；collagen/amyloid 在此是 biomaterial ingredient / inspiration，不独立支持 `06` |

## 3. 本轮重点复核但暂不改动

| ID | 题名 | 当前 scientific_object_modules / `01.04` bucket | 暂不改动原因 | 是否建议后续复核 |
|---|---|---|---|---|
| ASD-0012 | Large language models for chemistry robotics | `03` | Springer HTML 全文已足够支持分类；当前问题主要是 PDF challenge，不是模块不稳 | 是，后续可继续补合法 PDF |
| ASD-0014 | Spatialagent: An autonomous ai agent for spatial biology | `06` | 当前最佳一手来源仍是 DOI 摘要 + 官方仓库；`06/07` 边界已先收口，但全文 PDF 仍缺 | 是，后续优先补 bioRxiv 全文 |
| ASD-0022 | Chemgraph: An agentic framework for computational chemistry workflows | `03` | 当前一手全文不足以支持新增 `04`；先保持稳定单模块 | 低优先 |
| ASD-0029 | Chemhas: Hierarchical agent stacking for enhancing chemistry tools | `03` | 当前主要风险是 `ChemHAS` / `ChemAmp` 标题版本差异，而不是对象模块漂移 | 是，后续可继续做元数据统一 |
| ASD-0033 | Omnicellagent: Towards ai co-scientists for scientific discovery in precision medicine | `06` | PMC HTML 全文已足够支持 `06`；当前缺的是本地 PDF，不是 `06/07` 结论 | 是，后续可继续补合法 PDF |

## 4. 边界问题清单

`ASD-0014`
这是本批最典型的 `06 / 07` source-limited 样本。当前可访问的一手来源把对象稳定锚定在 spatial biology、spatial transcriptomics 和 human/mouse spatial-omics datasets，上述证据足以支持 `06`。但在没有拿到 bioRxiv 全文之前，不继续细化其临床层面是否存在独立 `07` 对象实验。

`ASD-0024`
这是药物发现论文在 relaxed rule 下接受 `07;03` 的代表样本。主目标当然是 drug discovery，但原文也确实报告了分子生成、性质约束和 molecular refinement 结果，因此不能再因为主展示模块是 `07` 就抹掉 `03`。

`ASD-0026`
这是 `04 / 09` 边界样本。旧口径容易把这类论文全部压回材料科学；本轮按“具体科学对象实验覆盖”重新判断后，材料样品与表征对象支持 `04`，而 AFM benchmark 与真实仪器操作任务又独立支持 `09`，因此接受多模块更符合当前规则。

`ASD-0033`
这是 precision-medicine surface framing 与 single-cell / omics 实际对象之间的边界样本。PMC HTML 全文显示主体仍是单细胞 / omics 数据检索、DEG 分析、通路/疾病关联富集与文献综合，尚不足以独立扩成 `07`。

`ASD-0035`
这是 `04 / 06` 边界样本。虽然材料设计中使用了 collagen、amyloid 等生物启发对象，但它们在原文里承担的是 biomaterial ingredient / inspiration 角色，而不是独立生命科学实验模块，因此不接受外扩 `06`。

## 5. 本轮后统计

- 本批处理记录数：`20`
- 本批成功归档本地 PDF 数：`17`
- 本批无本地 PDF 但完成一手 HTML / landing-page 核对数：`3`（`ASD-0012`, `ASD-0014`, `ASD-0033`）
- 本批 `source_limited=yes` 数：`1`（`ASD-0014`）
- 本批 note 更新数：`17`
- 本批 note 已核对但未重写数：`3`（`ASD-0012`, `ASD-0033`, `ASD-0035`）
- 本批 master-list row 更新数：`20`
- 本批落地多模块记录数：`3`（`ASD-0024`, `ASD-0026`, `ASD-0030`）
- 本批独立 `01.04` 新增数：`0`
- confirmed included + classified count：`451`
- needs_review count：`0`
- `08` 类 confirmed count：`3`
- module assignment counts：全库当前重算为 `528`；模块分布为 `01=20, 02=37, 03=83, 04=110, 05=35, 06=74, 07=70, 08=3, 09=37, 10=24, 11=35`。本批内部最终分布为 `01 x5`、`03 x6`、`04 x4`、`06 x5`、`07 x4`、`09 x1`，其中多模块叠加 `3` 篇
- independent `01.04` bucket count：全库当前重算为 `18`；本批无新增，且 `ASD-0013`、`0018`、`0019`、`0032` 继续维持“legacy secondary class 仍写 `01.04`，但当前 relaxed authoritative fact 已改为 `01`”的过渡状态
- legacy confirmed class 分布（如仍需兼容旧表）：本批未改 legacy `Main class` 主展示位，只通过 remarks / note 收口当前多模块事实
- 当前主要边界压力点：`01.04 / 01` 旧口径清理、`06 / 07` source-limited 样本、`03 / 04` 与 `04 / 09` 多模块接受阈值、PDF 合法归档完整率

## 6. 结论

`当前没有足够证据支持重构一级分类，问题主要集中在边界解释与低覆盖类稀缺性判断。`

补充说明：本批最重要的实质性收口不是“又多看了 20 篇”，而是把这 20 条记录重新拉回到一手来源上，清理了多篇 note 里残留的旧单模块 / 独立 `01.04` 表述，并把 `ASD-0024`、`ASD-0026`、`ASD-0030` 这 3 篇多模块事实正式落到主列表与 note 中。下一批仍应继续沿 `agent_master_paper_list.md` 的当前平铺顺序推进，不回退到按 `Notes/` 平铺管理。
