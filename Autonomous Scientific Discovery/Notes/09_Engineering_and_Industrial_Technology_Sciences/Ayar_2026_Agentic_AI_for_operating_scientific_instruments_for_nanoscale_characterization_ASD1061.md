# Agentic AI for operating scientific instruments for nanoscale characterization

**论文信息**

- ID：ASD-1061
- 标题：Agentic AI for operating scientific instruments for nanoscale characterization
- 作者：Zahra Ayar; Marcos Penedo; Mahdi Mehdikhani; Nahid Hosseini; Prabhu Prasad Swain; Georg E. Fantner
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2608.26198
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1061.txt
- PDF / 本地文件路径：Reference_PDF/09_Engineering_and_Industrial_Technology_Sciences/Ayar_2026_Agentic_AI_for_operating_scientific_instruments_for_nanoscale_characterization_ASD1061.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 研究目标 | 框架操作AFM工作流。 | TXT lines 22-24；核验TXT行号 22 | controllers, or trained machine-learning models. Here we present an agentic-AI framework that operates the executable part of the AFM workflow using a general-purpose, tool-augmented large language model connected to instrument functions through the Model Context Protocol (MCP). The framework consists | 高（一手正文；非独立复现） |
| Agent角色 | 三Agent分工明确。 | TXT lines 24-28；核验TXT行号 24 | connected to instrument functions through the Model Context Protocol (MCP). The framework consists of three MCP-based agents: AFM Messenger converts natural-language instructions into checked instrument commands; AFM Pilot assesses image quality through a large language model (LLM) and, if necessary, adapts imaging parameters; and AFM Doctor diagnoses image artifacts and applies transparent post-processing from a pre-approved tool set. Because the language model performs image assessment | 高（一手正文；非独立复现） |
| 安全机制 | 执行前歧义检查。 | TXT line 30；核验TXT行号 30 | types and imaging modes without specific retraining. Safe hardware operation is enforced through an | 高（一手正文；非独立复现） |
| 验证 | 比较受控执行前后的错误命令。 | TXT lines 31-33；核验TXT行号 31 | ambiguity check layer before execution. Benchmarking against fine-tuned and off-the-shelf tool-using models shows that this guarded execution layer, rather than model capability alone, reduces wrong- command execution to zero. In live experiments on different samples, AFM Pilot matched expert | 高（一手正文；非独立复现） |
| 现场结果 | 与专家在多个指标上比较。 | TXT lines 33-35；核验TXT行号 33 | command execution to zero. In live experiments on different samples, AFM Pilot matched expert operators in image quality, iteration count, and tuning time, with no significant difference. These results demonstrate a safe route to agentic operation of scientific instruments, where experimental intent | 高（一手正文；非独立复现） |

## 0. 摘要翻译

本文介绍工具增强语言模型操作原子力显微镜的Agent框架。三个MCP Agent分别将自然语言转成校验命令、判断图像质量并调参、诊断伪影和后处理。作者报告真实样品实验中Pilot与专家表现相当，安全层将错误命令执行降为零。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。在真实AFM上完成纳米尺度成像实验。
  - 原文位置：TXT lines 22-24；核验TXT行号 22；引文：controllers, or trained machine-learning models. Here we present an agentic-AI framework that operates the executable part of the AFM workflow using a general-purpose, tool-augmented large language model connected to instrument functions through the Model Context Protocol (MCP). The framework consists
- 多步行动过程：yes。命令生成、质量评估、调参与后处理形成行动链。
  - 原文位置：TXT lines 24-28；核验TXT行号 24；引文：connected to instrument functions through the Model Context Protocol (MCP). The framework consists of three MCP-based agents: AFM Messenger converts natural-language instructions into checked instrument commands; AFM Pilot assesses image quality through a large language model (LLM) and, if necessary, adapts imaging parameters; and AFM Doctor diagnoses image artifacts and applies transparent post-processing from a pre-approved tool set. Because the language model performs image assessment
- 至少一种Agent能力：yes。具备命令检查、图像评估、调参与伪影处理能力。
  - 原文位置：TXT lines 26-27；核验TXT行号 26；引文：instrument commands; AFM Pilot assesses image quality through a large language model (LLM) and, if necessary, adapts imaging parameters; and AFM Doctor diagnoses image artifacts and applies transparent
- 明确科研流程角色：yes。执行AFM工作流中的仪器操作和数据质量处理。
  - 原文位置：TXT lines 33-35；核验TXT行号 33；引文：command execution to zero. In live experiments on different samples, AFM Pilot matched expert operators in image quality, iteration count, and tuning time, with no significant difference. These results demonstrate a safe route to agentic operation of scientific instruments, where experimental intent

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：09
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：09（仅归档，不覆盖其他模块）
- 模块内分类路径：09.03.08 传感器与仪器科学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

对象为AFM纳米表征和仪器操作，归入09仪器测量。

### 2.3 容易混淆的边界

对象为AFM纳米表征和仪器操作，归入09仪器测量。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

tool_augmented_llm；multi_agent

### 3.2 科研流程角色

instrument_operation；image_analysis；postprocessing

Messenger、Pilot、Doctor调用MCP仪器函数、图像评估及预批准后处理工具；执行前设置歧义检查。

### 3.3 自主能力

具备命令检查、图像评估、调参与伪影处理能力。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

系统贡献是安全连接LLM与真实显微仪器；科学贡献是验证纳米表征流程中的操作Agent能力。

### 4.2 系统流程与组件

研究者提供实验意图；Messenger转换为受检查命令，Pilot观察图像并迭代调整参数，Doctor诊断伪影并处理，最终输出成像结果及流程记录。 这一工作流的实施细节、输入输出和验证范围均按原文所报告内容理解，不将展示案例外推为普遍能力。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

模型基准对照和不同样品现场AFM实验，以图像质量、迭代数、调参时间及错误命令执行评估。

### 5.2 基线、指标与结果

作者报告安全层将错误命令降至零，Pilot与专家在三项现场指标无显著差异。

### 5.3 科学贡献与证据强度

系统贡献是安全连接LLM与真实显微仪器；科学贡献是验证纳米表征流程中的操作Agent能力。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

相较硬编码自动化及任务专用控制器，框架以通用模型控制工具并读图反馈。

## 7. 局限性与风险

- author_stated：实验意图仍由人类定义，Agent操作工作流的可执行部分。
- reviewer_inference：样品范围、长期稳定性和跨仪器泛化仍需检验。

## 8. 对综述写作的价值

可讨论科研仪器Agent的命令安全、视觉反馈和人工定义实验意图。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

AFM多Agent通过安全命令与图像反馈辅助显微实验，并与专家比较。

### 9.2 速记版 pipeline

研究者提供实验意图；Messenger转换为受检查命令，Pilot观察图像并迭代调整参数，Doctor诊断伪影并处理，最终输出成像结果及流程记录。 这一工作流的实施细节、输入输出和验证范围均按原文所报告内容理解，不将展示案例外推为普遍能力。

### 9.3 标注字段汇总

```text
paper_id=ASD-1061
inclusion_status=to_read
scientific_object_modules=09
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=09
module_taxonomy_codes=09.03.08
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O2 既定基准 | AFM成像参数调优在预定义图像质量指标下评估 | “image quality, iteration count, and tuning time” · L25 |
| 验证强度 | V1 基准/内部评测 | 与专家操作比较图像质量等指标，未报告核心科学发现的物理检验 | “matched expert operators in image quality” · L25 |
| 系统自主性 | L2 闭环执行者 | Agent自主评估图像并调整参数闭环，人定义实验意图 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
