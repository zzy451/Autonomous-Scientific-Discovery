# 多模块重分类二轮高风险复核队列

> 日期：2026-06-20  
> 来源：451 篇 confirmed 文献多模块重分类第一轮全库审计。  
> 对应总报告：`Coverage_Check/multi_module_reclassification_full_library_summary_451_confirmed_2026-06-20.md`。  
> 用途：为下一轮全文补强、Note 修订、schema migration 前的重点核验提供队列。  
> 口径：本队列不直接要求改 `agent_master_paper_list.md`；除非全文证据强、规则一致、且不会造成 schema 半迁移，否则继续保持当前 legacy filing。
> 重要更新：本队列生成于较保守的第一轮审计之后；执行时以后续 `classification_policy_relaxation_addendum_2026-06-20.md` 和当前规则文件为准。若文献含可识别的具体对象实验、验证、benchmark task、case study 或结果报告，即可进入对应模块，不要求构成核心科学贡献。

## 一、最高优先级：`01.04` general-method bucket 边界

这些记录需要优先确认是否真的没有具体科学对象实验、验证、benchmark task、case study 或结果报告。cross-domain demo / benchmark 不会因论文自称通用而自动多模块；但只要 demo / benchmark / case study 可明确对应具体科学对象并报告结果，就应按新口径记录对应模块。

| ID | 当前 legacy | 风险点 | 暂定处理 |
|---|---|---|---|
| `ASD-0006` | `06 / 06.03` | DORA AI Scientist 可能更像通用科研/reporting workflow | 暂保持 `06` |
| `ASD-0060` | `01 / 01.04` | cross-domain benchmark 与 general-method tension | 暂保持 `01.04` |
| `ASD-0100` | `01 / 01.04` | scientific reproducibility benchmark 与 `11.07` 强规则冲突 | 暂保持 `01.04` |
| `ASD-0139` | `01 / 01.04` | physics framing 是否包含 substantive physics-object result | 暂保持 `01.04` |
| `ASD-0147` | `01 / 01.04` | idea-generation workflow 证据偏轻 | 暂保持 `01.04` |
| `ASD-0254` | `01 / 01.04` | biomedical research workflow 是否确无具体对象实验 | 暂保持 `01.04` |
| `ASD-0447` | `01 / 01.04` | universal chemical synthesis platform vs concrete chemistry object | 暂保持 `01.04` |
| `ASD-0524` | `01 / 01.04` | SciML benchmark 是否有具体对象层贡献 | 暂保持 `01.04` |
| `ASD-0528` | `01 / 01.04` | 多 demo 是否仅为 framework demonstration | 暂保持 `01.04` |
| `ASD-0530` | `01 / 01.04` | framework-heavy / core-strength | 暂保持 `01.04` |
| `ASD-0553` | `01 / 01.04` | bioinformatics automation substrate 边界 | 暂保持 `01.04` |
| `ASD-0554` | `01 / 01.04` | reproducible translational-bioinformatics workflow 边界 | 暂保持 `01.04` |
| `ASD-0659` | `01 / 01.04` | cross-domain demo 是否有对象层科学贡献 | 暂保持 `01.04` |
| `ASD-0663` | `01 / 01.04` | bio benchmark demo 是否足以转 `06` | 暂保持 `01.04` |
| `ASD-0673` | `01 / 01.04` | AtomisticSkills cross-domain demo weight | 暂保持 `01.04` |
| `ASD-0676` | `01 / 01.04` | AutoSci 是否有足够具体对象实验，或只是 general research-agent system | 暂保持 `01.04` |
| `ASD-0736` | `01 / 01.04` | AI-Researcher 是否有具体对象实验，或仅 general scientific innovation | 暂保持 `01.04` |
| `ASD-0737` | `01 / 01.04` | ScientistOne 的 evidence verification 是否转 `11.07` 或保持 general ASD | 暂保持 `01.04` |
| `ASD-0787` | `01 / 01.04` | cross-domain demos 是否有对象层科学贡献 | 暂保持 `01.04` |
| `ASD-0844` | `01 / 01.04` | Science Earth demos 是否包含可识别的生命科学、复杂系统或物理对象实验 / case study / 结果报告 | legacy 暂保持 `01.04`，新口径下优先复核 `06` 与 `01.03 / 02` |
| `ASD-0845` | `01 / 01.04` | SciDER 是否只是 general data-centric research automation | 暂保持 `01.04` |
| `ASD-0856` | `01 / 01.04` | AutoDiscovery cross-dataset demos 是否仅为 benchmark | 暂保持 `01.04` |
| `ASD-0866` | `01 / 01.04` | cross-domain cases 是否有可识别对象层实验、验证、case study 或结果报告 | 暂保持 `01.04` |
| `ASD-0868` | `01 / 01.04` | physics-guided equation discovery 是否只是方法验证 | 暂保持 `01.04` |
| `ASD-0869` | `01 / 01.04` | symbolic-regression benchmark 是否无具体对象实验 | 暂保持 `01.04` |
| `ASD-0870` | `01 / 01.04` | cross-discipline equation-discovery datasets 是否只是 benchmark | 暂保持 `01.04` |
| `ASD-0871` | `01 / 01.04` | Denario project 是否仍为 general research assistant；`01.04 / 11.07` 边界 | 暂保持 `01.04` |

## 二、`11.07` scientific knowledge production 边界

这些记录需要确认研究对象是否真是科学知识生产系统本身，而不是通用 research-agent workflow 或某一具体学科文献处理任务。

| ID | 当前 legacy | 风险点 | 暂定处理 |
|---|---|---|---|
| `ASD-0140` | `11 / 11.07` | scientific hypothesis generation 是 knowledge-production object 还是 general benchmark | 暂保持 `11.07` |
| `ASD-0186` | `11 / 11.07` | scientific peer review object vs generic review workflow | 暂保持 `11.07` |
| `ASD-0625` | `11 / 11.07` | ReviewBench / benchmark-heavy peer-review strength | 暂保持 `11.07` |
| `ASD-0626` | `11 / 11.07` | proactive review agent evidence depth | 暂保持 `11.07` |
| `ASD-0628` | `11 / 11.07` | ScholarPeer full-text evidence depth | 暂保持 `11.07` |
| `ASD-0636` | `11 / 11.07` | EGTR-Review evidence depth / duplicate pressure | 暂保持 `11.07` |
| `ASD-0656` | `11 / 11.07` | AAAI AI Review Pilot full-text evidence | 暂保持 `11.07` |
| `ASD-0698` | `11 / 11.07` | APRES 是否属于 scientific knowledge production core 或偏工具化 | 暂保持 `11.07` |
| `ASD-0699` | `11 / 11.07` | reproducibility assessment / peer-review support 的 Agent 强度 | 暂保持 `11.07` |
| `ASD-0700` | `11 / 11.07` | peer-review mechanism design 的实证与 Agent role 强度 | 暂保持 `11.07` |
| `ASD-0701` | `11 / 11.07` | social-science reproducibility 与一般 social science 方法边界 | 暂保持 `11.07` |
| `ASD-0706` | `11 / 11.07` | aiXiv ecosystem 是否更像 knowledge-production system 或 general ASD platform | 暂保持 `11.07` |
| `ASD-0717` | `11 / 11.07` | Paper Circle 是否是 scientific knowledge production object 或 general research framework | 暂保持 `11.07` |
| `ASD-0766` | `11 / 11.07` | ReviewGrounder evidence depth / peer-review core strength | 暂保持 `11.07` |
| `ASD-0768` | `11 / 11.07` | peer-review contradiction analysis full-text evidence | 暂保持 `11.07` |
| `ASD-0786` | `11 / 11.07` | AgentReview 的 peer-review dynamics evidence depth | 暂保持 `11.07` |
| `ASD-0831` | `11 / 11.07` | phenotype ontology curation 的 `11.07 / 06` 边界证据补强 | 暂保持 `11.07` |
| `ASD-0855` | `11 / 11.07` | peer-review framework 实证强度 | 暂保持 `11.07` |

## 三、`03 / 04` 与催化、材料、能源材料边界

这些记录需要优先用全文判断直接对象是分子/反应/合成，还是材料结构/性能/器件材料。

| ID | 当前 legacy | 风险点 | 暂定处理 |
|---|---|---|---|
| `ASD-0056` | `03 / 03.04` | organic laser emitters 处于 `03 / 04` 边界 | 暂保持 `03` |
| `ASD-0117` | `03 / 03.04` | OSDA molecule 与 zeolite/material performance 边界 | 暂保持 `03` |
| `ASD-0290` | `03 / 03.02` | catalyst / material structure-property 边界 | 暂保持 `03` |
| `ASD-0381` | `03 / 03.03` | catalysis Pareto-front mapping 细节需补强 | 暂保持 `03` |
| `ASD-0516` | `04 / 04.04` | equipment-heavy PVD system 的 `04 / 09` nuance | 暂保持 `04` |
| `ASD-0520` | `04 / 04.04` | Agent minimum 与 `04 / 03` catalyst boundary | 暂保持 `04` |
| `ASD-0547` | `04 / 04.04` | metasurface design 的 `04 / 09` 细节 | 暂保持 `04` |
| `ASD-0587` | `03 / 03.03` | collective-intelligence synthesis 的 `03 / 01.04` 边界 | 暂保持 `03` |
| `ASD-0600` | `03 / 03.03` | universal chemputation system 的 `03 / 01.04` 边界 | 暂保持 `03` |
| `ASD-0664` | `03 / 03.03` | computational catalysis 的 `03 / 04 / 01.04` 边界 | 暂保持 `03` |
| `ASD-0682` | `04 / 04.01` | El Agente Solido 的平台性与 solid-state 对象贡献强弱 | 暂保持 `04` |
| `ASD-0790` | `04 / 04.04` | heterogeneous catalyst material vs reaction/catalysis chemistry | 暂保持 `04` |
| `ASD-0793` | `03 / 03.03` | adsorption configuration 是否仍是化学对象而非材料候选发现 | 暂保持 `03` |
| `ASD-0811` | `04 / 04.04` | battery negolyte 的 `03 / 04` 边界与全文证据 | 暂保持 `04` |
| `ASD-0832` | `03 / 03.03` | catalyst discovery evidence based on abstract/note package | 暂保持 `03` |

## 四、`03 / 07` 与药物、分子优化边界

这些记录需要确认是否有明确 disease / target / therapeutic / translational endpoint。

| ID | 当前 legacy | 风险点 | 暂定处理 |
|---|---|---|---|
| `ASD-0112` | `07 / 07.04` | drug molecule optimization 是否由 therapeutic objective 主导 | 暂保持 `07` |
| `ASD-0357` | `07 / 07.04` | therapeutic target discovery validation 细节需补强 | 暂保持 `07` |
| `ASD-0536` | `07 / 07.04` | TCM-Agent core-strength 与平台感 | 暂保持 `07` |
| `ASD-0579` | `07 / 07.04` | classical active-learning Agent-strength | 暂保持 `07` |
| `ASD-0675` | `07 / 07.04` | drug molecule evaluation / screening endpoint | 暂保持 `07` |
| `ASD-0715` | `07 / 07.04` | BioDisco 的 therapeutic / biomedical endpoint 与生命科学机制边界 | 暂保持 `07` |
| `ASD-0798` | `07 / 07.04` | molecular lead optimization 是否由 drug endpoint 主导 | 暂保持 `07` |
| `ASD-0818` | `03 / 03.04` | broad molecular optimization 的 `03 / 07` 边界 | 暂保持 `03` |
| `ASD-0820` | `03 / 03.04` | synthesizable lead optimization 的高风险 `03 / 07` 边界 | 暂保持 `03` |
| `ASD-0824` | `07 / 07.04` | drug lead optimization endpoint | 暂保持 `07` |
| `ASD-0825` | `07 / 07.04` | protein-conditioned de novo drug design | 暂保持 `07` |
| `ASD-0826` | `07 / 07.04` | multi-objective drug discovery endpoint | 暂保持 `07` |

## 五、`06 / 07` 与生命机制、医学 endpoint 边界

这些记录需要确认 biological mechanism / omics / protein object 与 clinical / disease / therapeutic endpoint 的优先级。

| ID | 当前 legacy | 风险点 | 暂定处理 |
|---|---|---|---|
| `ASD-0034` | `06 / 06.03` | Perturb-seq 对象稳定，但系统细节和实验轮次需全文确认 | 暂保持 `06` |
| `ASD-0189` | `06 / 06.03` | proteomics hypothesis validation 细节需补强 | 暂保持 `06` |
| `ASD-0276` | `06 / 06.03` | clinical multiomics source 是否改变 endpoint | 暂保持 `06` |
| `ASD-0543` | `06 / 06.03` | prognostic gene discovery 的 `06 / 07` endpoint | 暂保持 `06` |
| `ASD-0714` | `06 / 06.03` | K-Dense Analyst 的 biological object evidence 与 general analysis workflow 边界 | 暂保持 `06` |
| `ASD-0728` | `06 / 06.01` | virtual cell model 的生命科学对象贡献与 framework-heavy 风险 | 暂保持 `06` |
| `ASD-0731` | `06 / 06.03` | biomedical knowledge extraction 的 `06 / 07 / 11.07` 边界 | 暂保持 `06` |
| `ASD-0770` | `06 / 06.03` | perturbation prediction 的 core-strength / drug-discovery framing | 暂保持 `06` |
| `ASD-0773` | `07 / 07.02` | NSCLC transcriptomic biomarker medical endpoint | 暂保持 `07` |
| `ASD-0813` | `06 / 06.03` | ELISA agent-threshold / core-strength | 暂保持 `06` |
| `ASD-0833` | `06 / 06.03` | virtual-cell mechanistic reasoning evidence depth | 暂保持 `06` |
| `ASD-0867` | `06 / 06.03` | protein sequence design with experimental validation | 暂保持 `06` |

## 六、`05 / 10` 与地球环境、航天任务边界

这些记录用于二轮继续校准“平台/载具”和“自然对象”的优先级。

| ID | 当前 legacy | 风险点 | 暂定处理 |
|---|---|---|---|
| `ASD-0648` | `10 / 10.02` | EO satellite autonomy 的 scientific core strength | 暂保持 `10` |
| `ASD-0651` | `05 / 05.02` | heatwave risk 的 `05 / 11 / 01.04` 边界 | 暂保持 `05` |
| `ASD-0703` | `10 / 10.02` | sensor-web / EO-1 mission-science boundary | 暂保持 `10` |
| `ASD-0722` | `10 / 10.02` | Earth-observing sensorweb 的 `05 / 10` 归属与 scientific object weight | 暂保持 `10` |
| `ASD-0783` | `05 / 05.04` | Earth observation benchmark-heavy but object-specific | 暂保持 `05` |
| `ASD-0803` | `05 / 05.02` | social-climate dynamics 的 `05 / 11` 边界与多模块可能性 | 暂保持 `05` |
| `ASD-0852` | `10 / 10.02` | ExoMars-like rover mission science vs Mars environmental object | 暂保持 `10` |
| `ASD-0858` | `10 / 10.02` | AEGIS / MSL rover mission operations | 暂保持 `10` |
| `ASD-0859` | `05 / 05.04` | EO-1 platform vs active volcanism object | 暂保持 `05` |
| `ASD-0860` | `05 / 05.04` | EO-1 platform vs cryosphere change object | 暂保持 `05` |
| `ASD-0861` | `05 / 05.04` | EO-1 platform vs flood monitoring object | 暂保持 `05` |

## 七、`08` 低覆盖类复核

这些记录用于确认低覆盖 `08` 是否确为农业/食品对象，而不是人为扩类。

| ID | 当前 legacy | 风险点 | 暂定处理 |
|---|---|---|---|
| `ASD-0510` | `08 / 08.01` | plant phenotyping 方向稳定，但 evidence strength 需补强 | 暂保持 `08` |
| `ASD-0634` | `08 / 08.01` | plant-science object evidence and low-coverage `08` pressure | 暂保持 `08` |
| `ASD-0695` | `08 / 08.05` | flavor scientist 的食品科学对象证据与低覆盖 `08` 压力 | 暂保持 `08` |

## 八、形式、计算、算法对象与 `01.04` 的边界

这些记录需要确认是 formal/computational object，还是 general ASD method bucket。

| ID | 当前 legacy | 风险点 | 暂定处理 |
|---|---|---|---|
| `ASD-0523` | `01 / 01.02` | AI research automation 是否 benchmark-heavy | 暂保持 `01.02` |
| `ASD-0738` | `01 / 01.02` | AutoSOTA 的 AI model discovery 是否仍稳定为 formal/computational object | 暂保持 `01.02` |
| `ASD-0850` | `01 / 01.02` | OR-Agent Note 与主列表 trace 冲突；需统一证据记录 | 暂保持 `01.02` |
| `ASD-0857` | `01 / 01.03` | governing equation / law discovery 与 generic equation-discovery method 边界 | 暂保持 `01.03` |

## 九、执行建议

下一轮建议按以下顺序处理：

1. 先处理 `01.04` 最高优先级队列，尤其 `ASD-0844`, `ASD-0868`, `ASD-0869`, `ASD-0870`, `ASD-0871`。
2. 同步处理 `11.07 / 01.04`，防止 general research-agent workflow 与 scientific knowledge production object 混淆。
3. 再处理 `03 / 07` 与 `03 / 04`，因为这些最可能影响未来 module assignment count。
4. 最后处理 `05 / 10`、`06 / 07`、低覆盖 `08` 和 formal `01.02 / 01.03` 边界。

执行时仍应遵守：只在证据强、规则一致、且 schema 迁移方案明确时才改主列表；否则先更新 Note 或审计报告，不做 legacy filing 半迁移。
