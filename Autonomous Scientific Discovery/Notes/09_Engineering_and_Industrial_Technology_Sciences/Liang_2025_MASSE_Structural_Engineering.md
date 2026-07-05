# Liang et al. 2025 - Automating Structural Engineering Workflows with Large Language Model Agents

**论文信息**
- 标题：Automating Structural Engineering Workflows with Large Language Model Agents
- 作者：Haoran Liang; Yufa Zhou; Mohammad Talebi Kalaleh; Qipei Mei
- 年份：2025
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2510.11004
- PDF / 本地文件路径：`Reference_PDF/09_Engineering_and_Industrial_Technology_Sciences/Liang_2025_MASSE_Structural_Engineering.pdf`
- 论文类型：研究论文 / structural-engineering multi-agent workflow system
- 当前状态：`to_read`
- 阅读日期：2026-07-05
- 笔记作者：Codex

## Phase6FollowupR21 Frozen Adjudication

- Frozen paper id: `ASD-0754`
- Final adjudicated modules: `09`
- `general_method_bucket`: `none`
- Primary module for filing: `09`
- Filing note: 当前目录位置仅用于归档便利，不构成分类依据。
- First-hand source state: 本轮已按本地归档 PDF `Reference_PDF/09_Engineering_and_Industrial_Technology_Sciences/Liang_2025_MASSE_Structural_Engineering.pdf` 进行一手来源确认，不再保留“无本地 PDF / 仅摘要级 / 非全文”表述。
- Frozen judgment: 该文稳定归入工程与工业技术科学 `09`，核心对象是 structural engineering workflows，包括 design-code interpretation、load calculation 与 capacity verification。
- Secondary nuance only: 当前剩余风险主要是 core-strength 与真实部署展开不足，不是分类不稳定。

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | 本地归档 PDF | `MASSE` 是面向 structural engineering 的多 Agent 系统 | 高 |
| 科学对象归类 | `09` | 本地归档 PDF | 任务围绕 interpreting design codes、executing load calculations、verifying structural capacities | 高 |
| 对象证据 | 结构工程流程对象明确 | 本地归档 PDF | 系统直接整合 real-world engineering workflows，而非通用科研平台 | 高 |
| 方法流程 | multi-agent workflow automation | 本地归档 PDF | 多 Agent 自动化大部分真实结构工程工作流 | 高 |
| 实验验证 | real-world case studies | 本地归档 PDF | 论文报告在真实案例中显著压缩专家工作时长 | 高 |
| `01.04` 边界 | 不归 `01.04` | 本地归档 PDF；对象优先规则 | 已有明确工程对象、规范解读、荷载计算、承载力核查与案例验证 | 高 |
| 本地 PDF 状态 | 已确认 | 本地归档路径 | R21 冻结写回包已确认本地归档 PDF | 高 |

## 0. 摘要翻译

本文提出 `MASSE`，将基于大语言模型的 agents 与真实结构工程工作流结合。作者认为，LLM 在复杂推理、长程规划和精确工具使用上的进展，与结构工程任务高度契合，例如设计规范解释、荷载计算和结构承载力校核。论文给出 proof-of-concept，并在真实案例上验证系统可显著缩短专业工作流耗时，同时提高可靠性与准确性。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：存在多 Agent 分工、复杂推理、工具调用、工作流决策和结果校核
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- Agent 能力：计划生成、工具调用、反馈迭代、自主决策、多 Agent 协作
- 在科研流程中承担的明确角色：规范解释、荷载计算、结构建模、承载力核核、工作流判断

### 1.2 排除风险检查

- 是否只是普通 AI for Science / ML / DL 模型：否
- 是否只是单次问答、摘要或分类：否
- 是否缺少行动闭环：否
- 当前排除结论：不排除

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：`09`
- 覆盖模式：单模块
- 是否具有具体科学对象实验、验证、benchmark task、case study 或结果报告：是
- 独立 `01.04` 存放区：`none`
- Primary module for filing：`09`
- Primary module for filing 说明：仅用于归档和展示，不覆盖对象模块事实
- 主展示模块一级类：`09` 工程与工业技术科学
- 主展示模块二级类：`09.05` 土木、建筑与水利工程
- 主展示模块三级类：structural engineering workflow / analysis and verification
- 其他覆盖模块及对应层级路径：无
- 每个模块的对象实验证据：设计规范、荷载计算、承载力核查、真实结构工程案例与专业工作流场景均指向结构工程对象
- 归类理由：论文对象始终是结构工程专业流程及其分析 / 核查任务，而非领域无关科研 Agent 方法
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：结构工程分析、设计规范解读、荷载与承载力校核工作流
- 最终科学问题：如何用多 Agent 自动化真实结构工程工作流
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：multi-agent orchestration 是实现方式，稳定对象仍是 structural engineering

### 2.3 容易混淆的边界

- 可能误归类到：`01.04`
- 最终判定：保持 `09`
- 判定理由：任务、知识源、评价与案例都直接围绕具体结构工程对象和专业流程
- 多模块覆盖说明：当前没有独立非工程对象证据支持额外模块
- 01.04 判定说明：已有明确工程对象 case studies，故 `general_method_bucket=none`
- 是否需要二次复核：当前分类无需二次复核

## 3. Agent 系统与科研流程角色

- Agent 类型：LLM Agent; Tool-using Agent; Multi-Agent System; Hybrid Agent
- 科研流程角色：knowledge_extraction_and_organization; simulation_modeling; tool_use_and_code_execution; data_analysis; result_interpretation; evidence_assessment_and_validation; end_to_end_research_automation
- 自主能力：task_decomposition; planning; tool_use; feedback_iteration; autonomous_decision_making; multi_agent_collaboration
- 交叉属性：computation_driven; simulation_driven

## 4. 方法设计

### 4.1 方法动机

- 结构工程核心流程长期高度依赖专家人工执行，自动化程度低
- 作者认为 LLM 在长程规划、复杂推理和工具使用上的进展已足以支撑专业工作流自动化

### 4.2 系统流程

1. 输入工程任务、规范与技术文档。
2. 多 Agent 分工解释设计规范与分析要求。
3. 系统执行荷载计算、结构分析与工具调用。
4. 对承载力和 adequacy 做校核与判断。
5. 汇总工作流结论并输出专业工程结果。

## 5. 实验与验证

- 验证方式：case_study; real_world_workflow_validation; expert_workload_comparison
- 数据 / 对象：real-world structural engineering case studies
- 任务设置：自动化规范解释、荷载计算、结构分析与 capacity verification
- 关键结果：论文报告可将专家级工作从约两小时压缩到几分钟级别
- 证据强度判断：当前已是本地 PDF 支撑下的工程对象分类证据

## 6. 与已有工作的关系

- 与通用科研 Agent 不同：本文直接嵌入真实结构工程工作流
- 与其他结构分析 Agent 的关系：比单点脚本生成更强调 professional workflow integration
- 主要创新点：把规范解读、荷载计算、结构分析和承载力核查整合到 training-free multi-agent system

## 7. 局限性与风险

- 科学贡献更偏工程工作流自动化，而非新的工程理论发现
- 真实部署细节、失败案例和安全边界仍需更细页码级证据展开
- 当前主要风险是 core-strength 与部署细节展开不足，不是 `09` 与 `01.04` 之间的分类不稳定

## 8. 对综述写作的价值

- 可放入章节：`09` 工程与工业技术科学中的 structural-engineering workflow agents
- 可支撑论点：只要工作流对象稳定落在结构工程，就不应因“通用 workflow”外观而回收到 `01.04`
- 推荐引用强度：standard

## 9. 总结

### 9.1 一句话概括

多 Agent 把真实结构工程工作流压缩成可自动执行流程。

### 9.2 标注字段汇总

```text
paper_id: ASD-0754
scientific_object_modules: 09
object_coverage_mode: single_module
primary_module_for_filing: 09
general_method_bucket: none
classification_confidence: high
source_limited: no
safety_access_status: none
first_hand_sources_checked: local archived PDF (`Reference_PDF/09_Engineering_and_Industrial_Technology_Sciences/Liang_2025_MASSE_Structural_Engineering.pdf`); official arXiv record (`https://arxiv.org/abs/2510.11004`)
pdf_archive_status: local archived PDF confirmed
canonical_local_pdf_path: Reference_PDF/09_Engineering_and_Industrial_Technology_Sciences/Liang_2025_MASSE_Structural_Engineering.pdf
official_pdf_url: https://arxiv.org/pdf/2510.11004
```
