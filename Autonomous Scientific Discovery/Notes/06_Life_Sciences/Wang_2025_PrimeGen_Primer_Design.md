# Wang et al. 2025 - Accelerating Primer Design for Amplicon Sequencing Using Large Language Model-Powered Agents

**论文信息**
- 标题：Accelerating Primer Design for Amplicon Sequencing Using Large Language Model-Powered Agents
- 作者：Wang et al.
- 年份：2025
- 来源 / venue：Nature Biomedical Engineering
- DOI / arXiv / URL：https://doi.org/10.1038/s41551-025-01455-z
- PDF / 本地文件路径：`Reference_PDF/06_Life_Sciences/Wang_2025_PrimeGen_Primer_Design.pdf`
- First-hand source checked：local archived PDF；DOI landing page
- PDF version：publisher PDF archived locally and checked
- Source-limited status：classification `no`；PDF archival `no`
- 论文类型：研究论文 / primer-design agent
- 当前状态：to_read
- 阅读与复核日期：2026-06-22
- 笔记作者：Codex

## Evidence Log

### Frozen Adjudication Writeback - 2026-07-05

- Final adjudication landed: `scientific_object_modules=06;07`; `final_01_04_bucket=none`; `primary_module_for_filing=06`.
- Source status: locally archived PDF checked; authoritative round closes with `source_limited=no`.
- Landed subset note: keep `06` as primary genomics / sequencing-design anchor and preserve the relaxed `07` biomedical validation coverage.

### 2026-07-05 Phase6FollowupR18Approx local PDF recheck

- `first_hand_sources_checked`: local archived PDF `Reference_PDF/06_Life_Sciences/Wang_2025_PrimeGen_Primer_Design.pdf`; DOI `https://doi.org/10.1038/s41551-025-01455-z`.
- Current authoritative classification: keep `scientific_object_modules=06;07`; `object_coverage_mode=multi_module`; `primary_module_for_filing=06`; `general_method_bucket=none`.
- Local-PDF finding: the archived PDF is present and readable. The first-page and early-page full text directly confirm PrimeGen, multi-agent primer design, automated protocol generation, and biomedical targeted-assay validation.
- Round effect: the old PDF-archival source-limited wording is retired; this row now lands with first-hand full-text support.

### 2026-06-22 reaudit writeback revision

- Round decision：更新为 `scientific_object_modules=06;07`，`primary_module_for_filing=06`，`general_method_bucket=none`。
- Archive sync：当前项目内没有合法可归档 PDF；本条必须明确记录为 `PDF unavailable; HTML full text checked`，而不能伪造本地 PDF 路径。
- Source note：分类本身不是 source-limited，因 Nature HTML 正文与补充/源数据已核查；但 PDF 归档状态应记为 source-limited。
- Policy note：`06` 仍是稳定 filing anchor；新增 `07` 只表示其验证和应用场景已触及 biomedical / assay-facing object coverage，不应把整篇论文改写成纯医学诊疗记录。

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | Nature HTML；supplementary / source-data | `PrimeGen` 是 orchestrated multi-agent system，中心控制器负责任务规划与分解，下游含 search / primer / protocol / experiment agents | 高 |
| 科学对象归类 | `06;07` | Nature HTML；supplementary / source-data | 主对象是 primer design for targeted sequencing / genomics workflow，保持 `06` 为 filing anchor；同时其 biomedical assay-facing validation 支撑保守加入 `07` | 中高 |
| 方法流程 | 多 Agent + tool / robot script generation | Nature HTML；supplementary / source-data | 子代理负责数据库检索、引物设计、协议生成、异常监测，protocol agent 可生成可执行机器人脚本 | 高 |
| 实验验证 | 湿实验 + benchmark | Nature HTML；supplementary / source-data | 可处理多达 955 amplicons，并优化扩增均一性与 dimer formation | 高 |
| PDF / source 状态 | HTML full text checked；no archived PDF | Nature site | 项目中无法合法归档 publisher PDF，但 HTML 全文和补充材料已核查 | 高 |

## 0. 摘要概述

本文提出 `PrimeGen`，一个由大语言模型驱动的多 Agent 系统，用于加速扩增子测序中的复杂引物设计任务。系统由中心控制器和多个专职子代理组成，可自动完成任务分解、数据库检索、引物设计、实验协议生成与异常监测，并可为自动化实验平台生成机器人脚本。当前口径下，本记录应以 `06` 生命科学中的 genomics / sequencing design object 为主，同时承认其在 biomedical targeted assay 场景中的 `07` 覆盖，但不应把 `07` 夸大为唯一主对象。

## 1. 是否纳入本综述

- 是否属于 Agent 文献：是
- 判断依据：具备明确科研目标、多 Agent 分工、任务规划、工具调用和实验流程支持
- 判定置信度：高
- 在科研流程中承担的明确角色：knowledge_extraction_and_organization；experimental_design；tool_use_and_code_execution；experiment_execution；evidence_assessment_and_validation
- 是否仍需进一步全文复核：否，HTML 全文与补充材料已足以支撑本轮落地

## 2. 科学领域归类

- 最终科学对象模块：`06;07`
- primary_module_for_filing：`06`
- general_method_bucket：`none`
- 对象覆盖方式：multi-module
- 描述性子方向：genomics / amplicon sequencing design；biomedical targeted assay support
- 最终科学研究对象：amplicon sequencing primer design workflow
- 最终科学问题：如何用 Agent 系统自动完成大规模 targeted NGS 引物设计并提高设计质量
- 容易混淆的边界：`06 / 07`
- 最终判定：保留 `06` 为 filing anchor，并新增 `07`
- 判定理由：直接研究对象仍是引物设计、扩增子测序与基因组学实验流程；`07` 来自其面向 biomedical targeted assay 的验证与应用覆盖，而不是疾病诊疗主叙事

## 3. Agent 系统与科研流程角色

- Agent 类型标签：LLM Agent；Planning Agent；Tool-using Agent；Retrieval-augmented Agent；Multi-Agent System；Hybrid Agent
- 科研流程角色：knowledge_extraction_and_organization；experimental_design；tool_use_and_code_execution；experiment_execution；data_analysis；result_interpretation；evidence_assessment_and_validation；end_to_end_research_automation
- 自主能力：task_decomposition；planning；tool_use；feedback_iteration；autonomous_decision_making；multi_agent_collaboration；environment_interaction；closed_loop_experimentation
- 交叉属性标签：computation_driven；data_driven；experiment_driven；high_throughput_screening；robotic_platform

## 4. 方法设计

1. 输入 targeted NGS / amplicon sequencing design requirements。
2. 中心控制器拆解任务。
3. 调用 search、primer、protocol、experiment agents，并生成机器人脚本。
4. 根据异常检测和设计质量反馈修正流程。
5. 继续优化 primer sets 与 protocol settings。
6. 输出可执行的 primer design 与实验支持方案。

## 5. 实验与验证

- 验证方式：benchmark；robotic_experiment；wet_lab_experiment
- 数据、任务与指标：targeted next-generation sequencing / amplicon sequencing tasks；大规模 primer design 与 protocol support
- 关键结果：支持多达 955 amplicons，并改善扩增均一性与 dimer formation
- 科学贡献类型：design；experimental_optimization；system_platform
- 证据强度：first_hand_html_full_text

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：不是单模型评分，而是端到端组织复杂测序设计工作流。
- 与已有 Agent / 科研智能系统的区别：强调专职代理分工和实验协议 / 机器人脚本生成。
- 与同一科学领域其他 Agent 文献的关系：可与单细胞、multiomics、proteomics Agent 共同构成 `06` 类 workflow agents，同时在 `07` 侧作为 biomedical assay-facing 边界样本出现。

## 7. 局限性与风险

- 目前聚焦 amplicon sequencing，跨任务泛化仍需更多证据。
- `07` 是保守新增模块，不应被表述成“整篇以疾病诊疗为核心”。
- 项目中无法合法归档 PDF，需要持续保留 HTML-full-text checked 的状态记录。

## 8. 对综述写作的价值

- 可放入 `06` 生命科学主章节，并在 `06 / 07` 边界讨论中作为样本。
- 可支撑“Agent 已能承担复杂基因组学实验设计与实验支持任务”这一论点。
- 也适合作为 project-PDF unavailable 的规范示例，说明没有合法 PDF 时应如何保留一手 HTML 证据链。
- 推荐引用强度：core

## 9. 总结

### 9.1 一句话概括

PrimeGen 以 `06` 的基因组学引物设计对象为主，同时因 biomedical targeted assay 覆盖而保守加入 `07`。

### 9.2 速记版 pipeline

1. 输入测序设计目标
2. 控制器拆解任务
3. 子代理检索并设计引物
4. 生成协议和脚本
5. 用实验反馈继续优化

### 9.3 标注字段汇总

```text
是否纳入：to_read
scientific_object_modules：06;07
primary_module_for_filing：06
general_method_bucket：none
object_coverage_mode：multi_module
描述性子方向：genomics / amplicon sequencing design; biomedical targeted assay support
Agent 类型：LLM Agent; Planning Agent; Tool-using Agent; Retrieval-augmented Agent; Multi-Agent System; Hybrid Agent
科研流程角色：knowledge_extraction_and_organization; experimental_design; tool_use_and_code_execution; experiment_execution; data_analysis; result_interpretation; evidence_assessment_and_validation; end_to_end_research_automation
自主能力：task_decomposition; planning; tool_use; feedback_iteration; autonomous_decision_making; multi_agent_collaboration; environment_interaction; closed_loop_experimentation
验证方式：benchmark; robotic_experiment; wet_lab_experiment
交叉属性：computation_driven; data_driven; experiment_driven; high_throughput_screening; robotic_platform
科学贡献类型：design; experimental_optimization; system_platform
证据强度：first_hand_html_full_text
source_limited：no
归类置信度：中高
纳入置信度：高
推荐引用强度：core
```
