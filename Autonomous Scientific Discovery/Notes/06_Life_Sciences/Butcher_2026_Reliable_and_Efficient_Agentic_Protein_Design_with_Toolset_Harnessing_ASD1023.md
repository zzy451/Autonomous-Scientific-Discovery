# Reliable and Efficient Agentic Protein Design with Toolset Harnessing

**论文信息**

- ID：ASD-1023
- 标题：Reliable and Efficient Agentic Protein Design with Toolset Harnessing
- 作者：Jasper Butcher; Jie Chen; Andrew Hunt; Cyrus M. Haas; Wenzhao Dai; Shajesh Sharma; Raktim Mitra; Saman Salike; Jeremy Koob; Aiko Muraishi; Zhe Li; Harley Pyles; Michael D. Tyka; Magnus S. Bauer; Rafi I. Brent; Anant Mittal; Neil P. King; David Baker
- 年份：2026
- 来源 / venue：bioRxiv preprint
- DOI / arXiv / URL：https://doi.org/10.64898/2026.10.19.759896
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1023.txt
- PDF / 本地文件路径：Reference_PDF/06_Life_Sciences/Butcher_2026_Reliable_and_Efficient_Agentic_Protein_Design_with_Toolset_Harnessing_ASD1023.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 科学目标 | 论文在九项生物分子设计任务上评估蛋白设计工具协调框架。 | Full text, local TXT line 23；核验TXT行号 23 | nine biomolecular design tasks | 高（一手正文；非独立复现） |
| 多步科研流程 | 框架支持复杂、长时程设计工作流中的反复迭代和设计空间探索。 | Full text, local TXT line 22；核验TXT行号 22 | rapid iteration and scalable exploration of complex | 高（一手正文；非独立复现） |
| Agent能力 | Harness把序列设计、结构预测及评价工具接入统一的Agent工作接口。 | Full text, local TXT line 18；核验TXT行号 18 | sequence design, structure prediction, and evaluation tools | 高（一手正文；非独立复现） |
| 验证结果 | 九项任务报告token和GPU成本下降，并提升计算设计通过率。 | Full text, local TXT line 23；核验TXT行号 23 | reduces total token usage relative to baseline agents by 86 | 高（一手正文；非独立复现） |
| 限制与边界 | cortisol结果是特定端到端设计活动的报告结果，不能推广到全部设计任务。 | Full text, local TXT line 26；核验TXT行号 26 | low nanomolar binders to cortisol zero shot | 高（一手正文；非独立复现） |

## 0. 摘要翻译

本文介绍Chaperone蛋白设计工具harness，将RFdiffusion3与ProteinMPNN、AlphaFold3及50余种工具连接，并支持高性能计算并行执行。作者建立九类生物分子设计任务评测，报告相较基线Agent更低的token和GPU开销及更高的计算设计通过率，并展示cortisol binder等应用。平台扩展了Agent可调用的蛋白设计工具范围；各任务的实验验证深度不同，计算通过不能一概解释为实测功能。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。评估对象为多种生物分子设计任务，具有明确的蛋白/分子研究目标。
  - 原文位置：Full text, local TXT line 23；核验TXT行号 23；引文：nine biomolecular design tasks
- 多步行动过程：yes。框架支持复杂长周期设计工作流迭代。
  - 原文位置：Full text, local TXT line 22；核验TXT行号 22；引文：rapid iteration and scalable exploration of complex
- 至少一种Agent能力：yes。Agent harness提供多工具接口并支持并行执行与结果编排。
  - 原文位置：Full text, local TXT line 18；核验TXT行号 18；引文：sequence design, structure prediction, and evaluation tools
- 明确科研流程角色：yes。论文通过九项设计任务和具体binder/组装体案例验证框架效用。
  - 原文位置：Full text, local TXT line 23；核验TXT行号 23；引文：reduces total token usage relative to baseline agents by 86

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：06
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：06（仅归档，不覆盖其他模块）
- 模块内分类路径：06.03.06 蛋白质科学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

归入蛋白质设计对象模块；多类分子设计结果应逐项依据来源判断证据等级，不能将工具套件覆盖面当成实验验证覆盖面。

### 2.3 容易混淆的边界

归入蛋白质设计对象模块；多类分子设计结果应逐项依据来源判断证据等级，不能将工具套件覆盖面当成实验验证覆盖面。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM Agent；Tool-using Agent

### 3.2 科研流程角色

tool_use_and_code_execution；data_analysis；evidence_assessment_and_validation

Chaperone为Agent提供统一工具接口和并行高性能计算执行环境，连接ProteinMPNN、AlphaFold3及50余种蛋白设计/评估工具，支持不同分子设计任务。

### 3.3 自主能力

Agent harness提供多工具接口并支持并行执行与结果编排。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

贡献是构建面向蛋白设计Agent的工具套件harness和评测框架，使Agent可调用成熟生物分子模型并利用HPC并行执行。

### 4.2 系统流程与组件

论文建立覆盖多靶点和多类任务的de novo蛋白设计评测套件，并展示Chaperone对蛋白binder、纳米材料及蛋白复合物linker等任务的工具编排；Agent通过标准接口提出和运行设计步骤。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

验证结合设计任务基准与案例，包括cortisol binder设计活动及计算结构/序列筛选；论文报告纳摩尔级binder相关结果。需区分计算筛选和实际结合实验的证据层级。

### 5.2 基线、指标与结果

标准化工具编排能支持大规模并行设计，论文报告纳摩尔级cortisol binder相关设计结果，并展示多个任务的可复用执行能力；结论依赖各专用工具的评估标准。

### 5.3 科学贡献与证据强度

贡献是构建面向蛋白设计Agent的工具套件harness和评测框架，使Agent可调用成熟生物分子模型并利用HPC并行执行。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

相较定制一个蛋白设计Agent，Chaperone提供可组合工具接口，让Agent连接已有生成、结构预测与评价程序；评测关注工具harness效率和任务覆盖。

## 7. 局限性与风险

设计质量仍依赖外部模型及结构评价器；不同任务的验证深度不一，计算成功不能推定所有binder、纳米材料或linker均经实验确认。

## 8. 对综述写作的价值

可用于分析蛋白设计工具harness如何扩大Agent工具覆盖，以及不同任务结果的验证深度差异。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

Chaperone以统一接口连接蛋白生成、序列设计、结构预测和评价工具，并在九类任务中测试Agent工具编排。报告的效率及计算筛选收益说明其可扩展性，但不同设计成果仍需分别核对实验验证。

### 9.2 速记版 pipeline

论文建立覆盖多靶点和多类任务的de novo蛋白设计评测套件，并展示Chaperone对蛋白binder、纳米材料及蛋白复合物linker等任务的工具编排；Agent通过标准接口提出和运行设计步骤。

### 9.3 标注字段汇总

```text
paper_id=ASD-1023
inclusion_status=to_read
scientific_object_modules=06
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=06
module_taxonomy_codes=06.03.06
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O4 需物理检验 | 设计需实验验证的生物分子包括cortisol binder | “nine biomolecular design tasks” · L21 |
| 验证强度 | V2 计算/仿真/回顾性 | 报告纳摩尔级binder相关结果但验证深度不一 | “low nanomolar binders to cortisol” · L25 |
| 系统自主性 | L1 任务助手 | 工具套件支持设计任务但由人决定研究流程 | — |

- 强验证（V3–V4）：否
- 置信度：medium；需全文复核：是；争议记录：无
- 复核状态：待专家复核：需全文复核
