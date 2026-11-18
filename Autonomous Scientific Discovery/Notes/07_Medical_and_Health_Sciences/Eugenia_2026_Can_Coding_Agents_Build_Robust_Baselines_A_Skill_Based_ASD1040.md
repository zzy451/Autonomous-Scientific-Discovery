# Can Coding Agents Build Robust Baselines? A Skill-Based Approach for Automating the Medical Imaging Model-Development Pipeline

**论文信息**

- ID：ASD-1040
- 标题：Can Coding Agents Build Robust Baselines? A Skill-Based Approach for Automating the Medical Imaging Model-Development Pipeline
- 作者：Moris, Eugenia; Orlando, José Ignacio
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2608.23336
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1040.txt
- PDF / 本地文件路径：Reference_PDF/07_Medical_and_Health_Sciences/Eugenia_2026_Can_Coding_Agents_Build_Robust_Baselines_A_Skill_Based_ASD1040.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 研究目标 | 自动开发医疗影像领域的模型baseline。 | Abstract；核验TXT行号 219 | competitive deep learning baselines for medical imaging | 高（一手正文；非独立复现） |
| Agent方法 | 组合文献导向推理、自动代码生成和假设驱动实验。 | Abstract；核验TXT行号 219 | literature-guided reasoning, automated code generation, and hypothesis-driven experimentation | 高（一手正文；非独立复现） |
| 流程反馈 | 持久实验树记录正负结果并驱动迭代实验。 | Abstract；核验TXT行号 252 | A persistent experiment tree records both positive and negative experimental evidence | 高（一手正文；非独立复现） |
| 对象覆盖 | 四个挑战涉及分割、分类和目标检测。 | Section 3.2；核验TXT行号 427 | four benchmark tasks derived from three public medical imaging challenges covering semantic segmentation, multiclass classification, and object detection | 高（一手正文；非独立复现） |
| 数据验证 | PUMA、MILK10k、MIDOG25使用组级或图像级划分和隐藏测试。 | Section 3.2 / Table 1；核验TXT行号 427 | The proposed workflow was evaluated on four benchmark tasks | 高（一手正文；非独立复现） |
| 结果 | PUMA两个track第6名，MILK10k第31名，MIDOG25跨扫描仪/肿瘤类型泛化较强。 | Results；核验TXT行号 219 | Across all tasks, the Experimentation Pipeline consistently improves validation performance, achieving competitive leaderboard results, including 6th place on both PUMA tracks (15 teams) and 31st place on MILK10k (125 teams). | 高（一手正文；非独立复现） |
| 主控复核：具体科学对象 | 公开挑战涵盖组织/细胞图像分割、肿瘤检测及病理影像分类；病理影像模型开发支持07.01.04。Coding agent只是方法，不因其编程工具另归01。 | TXT line 219；核验TXT行号 219 | four public benchmarks spanning segmentation, classification, and detection. Across all tasks, the Experimentation Pipeline consistently improves validation performance, achieving competitive leaderboard results, including 6th place on both PUMA tracks (15 tea | 高（一手正文；非独立复现） |

## 0. 摘要翻译

本文提出技能驱动的AI Scientist工作流，自动开发医疗影像模型基线。系统在四个公开挑战任务上完成分割、分类和检测，并取得有竞争力的榜单/保留测试结果。 论文以四个公开医疗影像挑战任务检验工作流，覆盖分割、分类和检测，并记录实验方案树和最终名次。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。目标是以科研Agent流程为医疗影像任务建立竞争性模型基线。
  - 原文位置：Abstract；核验TXT行号 219；引文：Developing competitive deep learning baselines for medical imaging
- 多步行动过程：yes。流程包含文献调研、实现、实验和基于结果的模型改进。
  - 原文位置：Abstract；核验TXT行号 219；引文：combines literature-guided reasoning, automated code generation, and hypothesis-driven experimentation
- 至少一种Agent能力：yes。技能流程记录实验树并选择、执行、分析实验。
  - 原文位置：Figure 1 caption；核验TXT行号 266；引文：iteratively select, execute, and analyze experiments while maintaining a persistent experiment plan and tree
- 明确科研流程角色：yes。Agent承担医学影像分割、分类和检测模型开发。
  - 原文位置：Section 3.2 / Table 1；核验TXT行号 427；引文：four benchmark tasks derived from three public medical imaging challenges

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：07
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：07（仅归档，不覆盖其他模块）
- 模块内分类路径：07.01.04 病理学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

公开挑战涵盖组织/细胞图像分割、肿瘤检测及病理影像分类；病理影像模型开发支持07.01.04。Coding agent只是方法，不因其编程工具另归01。

### 2.3 容易混淆的边界

公开挑战涵盖组织/细胞图像分割、肿瘤检测及病理影像分类；病理影像模型开发支持07.01.04。Coding agent只是方法，不因其编程工具另归01。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM Agent；Tool-using Agent；Hybrid Agent；Human-in-the-loop Agent

### 3.2 科研流程角色

literature_search_and_reading；tool_use_and_code_execution；experimental_design；data_analysis

Coding agents结合文献检索、模型构建和实验skills，在人类逐阶段审阅下执行。

### 3.3 自主能力

技能流程记录实验树并选择、执行、分析实验。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

科学贡献是医疗影像模型开发实证；系统贡献是可复用的文献引导、代码生成和实验树工作流。

### 4.2 系统流程与组件

整理任务和数据；检索SOTA知识；生成可运行建模管线；校准学习率、增强和模型设置；迭代运行与分析实验；持久记录实验计划和正负结果。 Agent持久维护实验计划树，从文献线索提出架构或训练假设，运行代码和训练作业、比较验证结果，再决定下一轮模型修改。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

四项benchmark任务来自PUMA、MILK10k、MIDOG25等公开挑战；患者/样本/切片分组划分；使用Dice、Macro-F1、检测F1及隐藏测试/leaderboard。

### 5.2 基线、指标与结果

同一流程在无任务特定重设计下适配异质任务；报告PUMA两个track第6名、MILK10k第31名及MIDOG25跨扫描仪和肿瘤类型泛化。

### 5.3 科学贡献与证据强度

科学贡献是医疗影像模型开发实证；系统贡献是可复用的文献引导、代码生成和实验树工作流。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

相较仅自动化超参搜索，该工作覆盖文献理解、代码和假设驱动实验全过程。

## 7. 局限性与风险

仍需研究者调用各技能并审查/运行所提实验；任务数和挑战集有限，榜单表现不等同于临床部署。

## 8. 对综述写作的价值

可支撑医疗影像AI Scientist、基线开发和实验可复现性论点。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

技能化Agent可跨多个公开医疗影像任务迭代构建模型基线。

### 9.2 速记版 pipeline

整理任务和数据；检索SOTA知识；生成可运行建模管线；校准学习率、增强和模型设置；迭代运行与分析实验；持久记录实验计划和正负结果。 Agent持久维护实验计划树，从文献线索提出架构或训练假设，运行代码和训练作业、比较验证结果，再决定下一轮模型修改。

### 9.3 标注字段汇总

```text
paper_id=ASD-1040
inclusion_status=to_read
scientific_object_modules=07
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=07
module_taxonomy_codes=07.01.04
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O2 既定基准 | 在四个公开医疗影像挑战基准上评估 | “four benchmark tasks derived from three public” · L44 |
| 验证强度 | V2 计算/仿真/回顾性 | 隐藏测试集和排行榜为基准评测 | “leaderboard results” · L27 |
| 系统自主性 | L2 闭环执行者 | 文献引导推理和假设驱动实验迭代 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
