# Huang et al. 2025 - Biomni: A general-purpose biomedical AI agent

**论文信息**
- 标题：Biomni: A general-purpose biomedical AI agent
- 作者：Huang et al.
- 年份：2025
- 来源 / venue：bioRxiv
- DOI / URL：https://doi.org/10.1101/2025.05.30.656746
- PDF / 本地文件路径：`Reference_PDF/07_Medical_and_Health_Sciences/Huang_2025_Biomni.pdf`
- First-hand source checked：PubMed abstract；official project PDF
- PDF version：official project PDF
- Source-limited：no
- 当前状态：confirmed core；当前落地为 relaxed multi-module `06;07`，主归档模块为 `07`

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| PDF 归档与来源核对 | 已完成 | official project PDF；PubMed abstract | 当前使用项目内 official PDF 作为规范版本 | 高 |
| Agent 纳入 | 是 | PubMed abstract；official PDF | 系统围绕 biomedical research 组织多步任务，具备规划、工具调用、反馈与任务编排能力 | 高 |
| 医学与健康科学覆盖 | `07` | official PDF | 论文包含疾病、药物、临床 / biomedical workflow 等明确医学健康对象任务 | 高 |
| 生命科学覆盖 | `06` | official PDF | 论文同时覆盖 gene、microbiome、molecular cloning、single-cell / ATAC-seq 等生命科学对象案例 | 高 |
| `01.04` 存放区判断 | `none` | official PDF | 尽管系统自称 general-purpose biomedical agent，但其全文包含多个具体生命 / 医学对象任务，不属于独立通用方法存放区 | 高 |

## 1. 是否纳入本综述

- 是否属于 Agent 文献：是。
- 判断依据：系统围绕 biomedical research 执行多步科研工作流，并具备工具调用与任务编排能力。
- 纳入置信度：高。
- 当前口径说明：该文不再写成单一 `07` 记录；其生命科学对象覆盖已足以支持 `06;07` 落地。

## 2. 科学领域归类

- scientific_object_modules：`06;07`
- object_coverage_mode：`multi_module`
- general_method_bucket：`none`
- primary_module_for_filing：`07`
- 归类理由：
  - `07`：面向 biomedical research 的疾病、药物与健康相关任务稳定成立。
  - `06`：gene、microbiome、molecular cloning、single-cell / ATAC-seq 等案例提供明确生命科学对象证据。
- 边界说明：系统的“general-purpose biomedical”表述不能覆盖掉具体 life-science object evidence，因此不应维持旧的单 `07` 写法。

## 3. Agent 系统与科研流程角色

- Agent 类型：LLM Agent；Tool-using Agent；Hybrid Agent。
- 科研流程角色：tool_use_and_code_execution；data_analysis；literature_search_and_reading；evidence_assessment_and_validation。
- 自主能力：planning；tool_use；feedback_iteration；autonomous_decision_making；multi_agent_collaboration。

## 4. 方法设计

1. 接收 biomedical research 问题与上下文。
2. 拆解并编排多步研究任务。
3. 调用外部工具、数据库与分析流程。
4. 根据中间结果迭代修正任务。
5. 输出更高质量的 biomedical / life-science 研究分析结果。

## 5. 实验与验证

- 医学对象案例：疾病、药物与 biomedical workflow 相关任务。
- 生命科学对象案例：gene、microbiome、molecular cloning、single-cell、ATAC-seq。
- 验证方式：benchmark；tool-based task execution；case study。
- 证据强度：first-hand project PDF；source_limited = no。

## 6. 与已有工作的关系

- 与更窄的 biomedical agent 相比，Biomni 的覆盖面更广，但其广覆盖仍建立在具体生命与医学对象任务之上。
- 可与 `Gottweis_2025_Co_Scientist`、`Robin`、`HealthFlow` 等记录对比其 `06;07` 双模块覆盖范围。

## 7. 局限性与风险

- 系统平台叙事较强，但当前不再构成退回 `01.04` 或压缩为单 `07` 的理由。
- 主要剩余风险在任务粒度与模块内细分，而不是 `06;07` 双模块本身。

## 8. 对综述写作的价值

- 适合放在医学与健康科学主节，并在生命科学交叉段落中强调其多对象覆盖。
- 可支撑“biomedical AI agent 已从单类任务工具扩展到生命科学与医学双向覆盖”的论点。
- 推荐引用强度：core。

## 9. 总结

### 9.1 一句话概括

Biomni 以 biomedical research 为主轴，同时覆盖了基因、微生物组、分子克隆与单细胞等生命科学对象。

### 9.2 标注字段汇总

```text
是否纳入：是
scientific_object_modules：06;07
object_coverage_mode：multi_module
general_method_bucket：none
primary_module_for_filing：07
Agent 类型：LLM Agent; Tool-using Agent; Hybrid Agent
科研流程角色：tool_use_and_code_execution; data_analysis; literature_search_and_reading; evidence_assessment_and_validation
验证方式：benchmark; case_study
科学贡献类型：system_platform
证据强度：first_hand_full_text
归类置信度：高
纳入置信度：高
推荐引用强度：core
```
