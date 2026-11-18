# Auto-MD-bench: Evaluating Autoresearch Agents for Real-World Medical Tasks

**论文信息**

- ID：ASD-1038
- 标题：Auto-MD-bench: Evaluating Autoresearch Agents for Real-World Medical Tasks
- 作者：Zhou, Shenqi; Zou, Qiran; Zhao, Wenhao; Liao, Zhenyu; Liu, Dianbo
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2610.25069
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1038.txt
- PDF / 本地文件路径：Reference_PDF/07_Medical_and_Health_Sciences/Shenqi_2026_Auto_MD_bench_Evaluating_Autoresearch_Agents_for_Real_World_ASD1038.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 对象与目标 | 评估主指标之外的风险校准和人群稳健性。 | Abstract；核验TXT行号 482 | medical ML models should also provide well-calibrated risk estimates and remain robust across patient populations | 高（一手正文；非独立复现） |
| 任务覆盖 | 基准包含15项真实医疗任务。 | Abstract / Table 8；核验TXT行号 486 | a benchmark of 15 real-world medical tasks | 高（一手正文；非独立复现） |
| Agent行动 | autoresearch agent检查数据、建模、验证并反复修改。 | Introduction；核验TXT行号 504 | from data inspection and model selection to implementation, validation, and iterative refinement | 高（一手正文；非独立复现） |
| 系统比较 | 评估AIDE、AI Scientist v2、Codex和Autoresearch。 | Abstract；核验TXT行号 488 | We evaluate four agents: AIDE, AI Scientist v2, Codex, and Autoresearch. | 高（一手正文；非独立复现） |
| 多维验证 | 除预测性能外还测风险校准、外部验证及亚组表现。 | Section 3.3; Tables 3–5；核验TXT行号 4296 | With AUROC and ECE as objectives, mean ECE falls from 0.172±0.2110.172\pm 0.211 in A to 0.016±0.0230. | 高（一手正文；非独立复现） |
| 主要结果 | 较强Agent主分数有竞争力但风险校准逊于简单基线。 | Abstract；核验TXT行号 489 | The strongest agents achieve competitive primary scores, yet their predicted risks are less calibrated than those of the simple baseline models | 高（一手正文；非独立复现） |
| 主控复核：具体科学对象 | 基准的15项任务来自10个临床数据集，涵盖生存、分类、序列预测和跨医院验证；医疗信息学是合适的对象索引。 | TXT line 486；核验TXT行号 486 | 15 real-world medical tasks from 10 clinical datasets, spanning survival analysis, classification and sequential prediction, with external validation across cohorts, hospitals and time periods. We evaluate four agents: AIDE, AI Scientist v2, Codex, and Autores | 高（一手正文；非独立复现） |

## 0. 摘要翻译

Auto-MD-bench以15项真实医疗任务评估autoresearch agents。基准除预测性能外还检查风险校准、跨人群泛化、亚组差异和规则遵循。作者发现Agent可取得有竞争力的主指标，但概率校准和人群迁移仍有风险。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。检验真实医疗预测中单一主指标是否足以引导模型开发。
  - 原文位置：Abstract / Introduction；核验TXT行号 485；引文：are these objectives sufficient to guide agents toward models that meet the broader requirements of real-world medical use?
- 多步行动过程：yes。Agent从数据检查到模型选择、实现、验证和迭代改进。
  - 原文位置：Introduction；核验TXT行号 504；引文：from data inspection and model selection to implementation, validation, and iterative refinement
- 至少一种Agent能力：yes。比较四种autoresearch agents并观察其模型搜索。
  - 原文位置：Abstract；核验TXT行号 488；引文：We evaluate four agents: AIDE, AI Scientist v2, Codex, and Autoresearch.
- 明确科研流程角色：yes。基准评估15项真实医疗任务上的模型研发过程。
  - 原文位置：Abstract；核验TXT行号 486；引文：a benchmark of 15 real-world medical tasks

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：07
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：07（仅归档，不覆盖其他模块）
- 模块内分类路径：07.03.08 医学信息学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

基准的15项任务来自10个临床数据集，涵盖生存、分类、序列预测和跨医院验证；医疗信息学是合适的对象索引。

### 2.3 容易混淆的边界

基准的15项任务来自10个临床数据集，涵盖生存、分类、序列预测和跨医院验证；医疗信息学是合适的对象索引。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM Agent；Tool-using Agent；Hybrid Agent

### 3.2 科研流程角色

data_analysis；tool_use_and_code_execution；evidence_assessment_and_validation

多个自主模型开发Agent在受限代码环境中迭代构建医疗预测模型。

### 3.3 自主能力

比较四种autoresearch agents并观察其模型搜索。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

科学贡献为医疗模型开发Agent的真实任务评估；系统贡献为多维benchmark。

### 4.2 系统流程与组件

Agent检查数据、选择特征/预处理/模型、运行训练验证、记录实验并保留改进；最终以独立测试、校准和人群外部验证复评。 每项任务要求Agent查看真实医学指南/论文与临床数据代码，生成并执行多步分析，再按任务要求输出统计证据及临床解释。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

15任务、10个临床数据集，涵盖生存分析、分类和序列预测；比较简单基线，三次重复，评估主分数、ECE、外部与亚组性能。

### 5.2 基线、指标与结果

作者报告强Agent的主任务分数有竞争力，但风险校准低于简单基线；相近主分数模型可有不同校准表现，人口迁移时性能变化明显。

### 5.3 科学贡献与证据强度

科学贡献为医疗模型开发Agent的真实任务评估；系统贡献为多维benchmark。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

拓展只看AUROC等单指标的Agent评估，强调校准和人群稳健性。

## 7. 局限性与风险

benchmark结果不能代替临床部署验证；任务和数据覆盖有限，结论依赖给定目标函数。

## 8. 对综述写作的价值

可支撑医疗Agent评估、目标错配和临床部署前验证论点。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

医疗模型开发Agent的高主分数并不保证风险校准和人群稳健。

### 9.2 速记版 pipeline

Agent检查数据、选择特征/预处理/模型、运行训练验证、记录实验并保留改进；最终以独立测试、校准和人群外部验证复评。 每项任务要求Agent查看真实医学指南/论文与临床数据代码，生成并执行多步分析，再按任务要求输出统计证据及临床解释。

### 9.3 标注字段汇总

```text
paper_id=ASD-1038
inclusion_status=to_read
scientific_object_modules=07
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=07
module_taxonomy_codes=07.03.08
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O2 既定基准 | 15项医疗任务基准，有标准评估指标 | “a benchmark of 15 real-world medical tasks” · L44 |
| 验证强度 | V1 基准/内部评测 | 基准测试与校准分析，无真实临床部署验证 | “The strongest agents achieve competitive primary scores” · L26 |
| 系统自主性 | L2 闭环执行者 | Agent自主完成数据检查到迭代修改的建模闭环 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
