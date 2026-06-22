# Liang et al. 2025 - Automating Structural Engineering Workflows with Large Language Model Agents

## 2026-06-23 landed writeback refresh

- `paper_id`: `ASD-0754`
- Accepted relaxed classification: `scientific_object_modules=09`; `object_coverage_mode=single_module`; `primary_module_for_filing=09`; `general_method_bucket=none`
- `classification_confidence`: `high`
- `source_limited`: `no`
- `safety_access_status`: `none`
- First-hand source checked this round: arXiv abstract page `https://arxiv.org/abs/2510.11004`
- PDF / archive status: no local archived PDF was confirmed in this workspace; recommended official PDF URL is `https://arxiv.org/pdf/2510.11004`
- Writeback implication: keep the note anchored in structural-code interpretation, load calculation, capacity verification, and real-world structural-engineering workflow validation

**论文信息**
- 标题：Automating Structural Engineering Workflows with Large Language Model Agents
- 作者：Haoran Liang; Yufa Zhou; Mohammad Talebi Kalaleh; Qipei Mei
- 年份：2025
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2510.11004
- PDF / 本地文件路径：未确认本地归档 PDF；本次写回基于 arXiv abstract page
- 论文类型：研究论文 / structural-engineering multi-agent workflow system
- 当前状态：to_read
- 阅读日期：2026-06-23
- 笔记作者：Codex

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | arXiv abstract | 摘要明确提出 `MASSE`，即 structural engineering 的多 Agent 系统 | 高 |
| 科学对象归类 | `09` | arXiv abstract | 任务围绕 interpreting design codes, executing load calculations, verifying structural capacities | 高 |
| 关键对象证据 | 结构工程工作流对象稳定 | arXiv abstract | 系统直接整合 real-world engineering workflows，而不是抽象科研平台 | 高 |
| 方法流程 | multi-agent workflow automation | arXiv abstract | 训练免调的多 Agent 系统声称可自动化大多数 real-world structural engineering workflows | 高 |
| 实验验证 | real-world case studies | arXiv abstract | comprehensive validation on real-world case studies，并报告从约两小时缩短到数分钟 | 高 |
| 01.04 边界 | 不进入 `01.04` | 对象优先规则 + arXiv abstract | 有明确工程对象、规范解释、荷载计算、承载力校核和案例验证，故不是无对象 general method | 高 |
| PDF / archive 状态 | 未确认本地归档 | workspace 检索 + arXiv abs | 当前工作区未检出本地 PDF；可回溯官方 arXiv PDF 链接 | 高 |

## 0. 摘要翻译

本文提出 `MASSE`，即首个面向结构工程的多智能体系统，将基于大语言模型的 agent 与真实工程工作流有效结合。结构工程是一个基础但长期相对停滞的领域，其核心工作流几十年来变化不大，尽管其经济影响和市场规模都很大。近期 LLM 在复杂推理、长程规划和精确工具使用方面的进展，与结构工程任务高度契合，例如设计规范解释、荷载计算和结构承载力校核。作者给出一个 proof-of-concept，表明大多数真实结构工程工作流都可以通过 training-free 的 LLM 多智能体系统实现自动化。`MASSE` 可直接部署于专业环境中，且在真实案例上的综合验证显示，它可以把专家约两小时的工作缩短到几分钟，同时提高可靠性和准确性。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 是否属于 Agent 文献：是
- 判断依据：存在多 Agent 分工、复杂推理、长程规划、工具调用、工作流决策和结果校核
- 判定置信度：高
- 是否面向明确科研目标：是
- 是否具有多步行动过程：是
- Agent 能力：计划生成、工具调用、反馈迭代、自主决策、多 Agent 协作
- 在科研流程中承担的明确角色：规范解释、荷载计算、结构建模、承载力校核、工作流判定

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
- Primary module for filing 说明：仅用于落盘与展示，不覆盖对象模块事实
- 主展示模块一级类：`09` 工程与工业技术科学
- 主展示模块二级类：`09.05` 土木、建筑与水利工程
- 主展示模块三级类：structural engineering workflow / analysis and verification
- 其他覆盖模块及对应层级路径：无
- 每个模块的对象实验证据：设计规范、荷载计算、承载力校核、真实结构工程案例和专业工作流场景均指向结构工程对象
- 归类理由：论文对象始终是结构工程专业流程及其分析 / 校核任务，而非领域无关科研 Agent 方法
- 归类置信度：高

### 2.2 对象优先判定

- 最终科学研究对象：结构工程分析、设计规范解释、荷载与承载力校核工作流
- 最终科学问题：如何用多 Agent 自动化真实结构工程工作流
- 为什么不按 Agent 技术、模型方法或发表 venue 归类：multi-agent orchestration 是实现方式，稳定对象仍是 structural engineering

### 2.3 容易混淆的边界

- 可能误归类到：`01.04`
- 最终判定：保持 `09`
- 判定理由：摘要中的任务、知识源、评价与案例都直接围绕具体结构工程对象和专业流程
- 多模块覆盖说明：当前没有独立非工程对象实验支撑额外模块
- 01.04 判定说明：已有明确工程对象 case studies，故 `general_method_bucket=none`
- 是否需要二次复核：当前分类无需二次复核；若后续要提炼更细的案例和评估指标，可补读 PDF

## 3. Agent 系统与科研流程角色

- Agent 类型：LLM Agent; Tool-using Agent; Multi-Agent System; Hybrid Agent
- 科研流程角色：knowledge_extraction_and_organization; simulation_modeling; tool_use_and_code_execution; data_analysis; result_interpretation; evidence_assessment_and_validation; end_to_end_research_automation
- 自主能力：task_decomposition; planning; tool_use; feedback_iteration; autonomous_decision_making; multi_agent_collaboration
- 交叉属性：computation_driven; simulation_driven

## 4. 方法设计

### 4.1 方法动机

- 结构工程核心流程长期高度依赖专家人工执行，自动化程度低
- 作者认为 LLM 在长程规划、复杂推理与工具使用上的进展已足以支撑专业工作流自动化

### 4.2 系统流程

1. 输入工程任务、规范与技术文档。
2. 多 Agent 分工解释设计规范与分析要求。
3. 系统执行荷载计算、结构分析与相关工具调用。
4. 对承载力和 adequacy 做校核与判断。
5. 汇总工作流结论并输出专业工程结果。

## 5. 实验与验证

- 验证方式：case_study; real_world_workflow_validation; expert_workload_comparison
- 数据 / 对象：real-world structural engineering case studies
- 任务设置：自动化规范解释、荷载计算、结构分析与 capacity verification
- 关键结果：专家工作量从约两小时缩短到几分钟，并声称可靠性与准确性提高
- 证据强度判断：当前一手 abstract 已足以稳定 `09` 分类；若要拆解具体 case 或 benchmark 名称，仍可补读 PDF

## 6. 与已有工作的关系

- 与通用科研 Agent 不同：本文直接嵌入真实结构工程工作流
- 与其他结构分析 Agent 的关系：比单点结构分析脚本生成更强调 professional workflow integration
- 主要创新点：把规范解释、荷载计算、结构分析和承载力校核整合到 training-free multi-agent system

## 7. 局限性与风险

- 当前未确认本地归档 PDF，后续如做精细引文建议补档
- 科学贡献更偏工程工作流自动化，而非新的工程理论发现
- 真实部署细节、失败案例和安全边界仍需更强全文证据展开
- 当前主要风险是 core-strength 与部署风险细化，不是对象分类风险

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
first_hand_sources_checked: arXiv abstract page
pdf_archive_status: no local archived PDF confirmed
recommended_pdf_url: https://arxiv.org/pdf/2510.11004
```
