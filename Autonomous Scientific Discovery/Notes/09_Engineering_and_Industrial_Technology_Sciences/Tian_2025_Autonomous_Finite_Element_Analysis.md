# Tian et al. 2025 - Optimizing collaboration of large language model based agents for autonomous finite element analysis

## 2026-06-22 carry-forward closeout / archive sync

- Canonical PDF path: `Reference_PDF/09_Engineering_and_Industrial_Technology_Sciences/Tian_2025_Autonomous_Finite_Element_Analysis.pdf`
- Current closeout sources checked: SSRN abstract page; DOI redirect / metadata check; arXiv abstract page (`2408.13406`)
- PDF version: approved arXiv fallback PDF archived locally; `%PDF` header verified
- `source_limited`: yes
- Accepted relaxed classification: `scientific_object_modules=09`; `object_coverage_mode=single_module`; `primary_module_for_filing=09`; `general_method_bucket=none`.
- Note implication: keep the paper stably anchored in finite-element engineering analysis; this note's folder location is filing convenience, not classification authority.

**论文信息**
- 标题：Optimizing collaboration of large language model based agents for autonomous finite element analysis
- 作者：Tian et al.
- 年份：2025
- 来源 / venue：SSRN；approved arXiv fallback available
- DOI / arXiv / URL：https://doi.org/10.2139/ssrn.5107557；https://arxiv.org/abs/2408.13406
- PDF / 本地文件路径：`Reference_PDF/09_Engineering_and_Industrial_Technology_Sciences/Tian_2025_Autonomous_Finite_Element_Analysis.pdf`（approved arXiv fallback archive copy；本轮 closeout 仍保持 `source_limited=yes`）
- 论文类型：系统论文 / engineering-analysis agent
- 当前状态：`to_read`（confirmed core；2026-06-22 carry-forward closeout refreshed）
- 阅读日期：2026-06-22
- 笔记作者：Codex

## Evidence Log

**2026-06-22 source refresh**: the current closeout checked the SSRN abstract, DOI redirect / metadata status, and arXiv abstract page; an approved arXiv fallback PDF is now archived locally, but the note remains `source_limited=yes` because official SSRN full text stayed blocked in this environment.

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | SSRN abstract; arXiv abstract | 基于 AutoGen 的多代理框架，含 Engineer / Executor / Expert 等角色 | 高 |
| 科学对象归类 | `09` | SSRN abstract; arXiv abstract | 对象稳定锚定在线弹性有限元工程分析流程，而非通用科研平台 | 高 |
| 方法流程 | 多代理协作 + 求解执行 | SSRN abstract; arXiv abstract | 代理负责规划、执行、纠错与结果求解 | 高 |
| 实验验证 | 工程仿真比较 | SSRN abstract; arXiv abstract | 对不同协作配置进行了多次随机试验比较，评估成功率与稳健性 | 高 |
| 边界判断 | `general_method_bucket=none`，不归 `01.04` | SSRN abstract; DOI redirect / metadata check; arXiv abstract | 已有具体 FEM 工程分析对象级证据，因此不应回收到通用方法桶 | 高 |
| 来源状态 / 归档 | 保持 `source_limited=yes`；本地已归档 arXiv fallback PDF | DOI redirect / metadata check; local archive verification | 官方 SSRN 全文在本环境仍 blocked，但 approved arXiv fallback PDF 已成功归档供后续复核 | 高 |

## 0. 摘要翻译

本文研究如何优化 LLM 多代理在有限元分析中的协作方式。系统通过不同角色分工自动完成线弹性问题的工程求解，并比较不同协作配置的稳定性和成功率。核心贡献不是一般 scientific-agent benchmark，而是面向具体工程仿真对象的 Agent 协作优化。

## 1. 是否纳入本综述

- 是否属于 Agent 文献：是
- 判断依据：有明确科研目标、多步行动、多代理协作、代码执行与结果校验
- 判定置信度：高
- 在科研流程中承担的明确角色：simulation_modeling；tool_use_and_code_execution；evidence_assessment_and_validation
- 是否仍需进一步全文复核：是；本轮 closeout 仅核对 SSRN 摘要、DOI 跳转状态与 arXiv 摘要。虽然 approved arXiv fallback PDF 已归档，本环境中的官方 SSRN 全文仍 blocked，因此继续保持 `source_limited=yes`

## 2. 科学领域归类

- 科学对象模块：`09`
- 覆盖模式：`single_module`
- `primary_module_for_filing`：`09`
- `general_method_bucket`：`none`
- 归档细分标签：finite element analysis / engineering simulation；Engineering/scientific workflow agents
- 最终科学研究对象：有限元工程分析与线弹性问题求解
- 最终科学问题：如何通过多代理协作提高工程仿真求解流程自动化与稳健性
- 容易混淆的边界：`01.04`
- 最终判定：保留稳定单模块 `09`
- 判定理由：对象级验证任务始终是具体 FEM 工程分析，不是通用科研能力平台；当前 note 位于 `09` 目录仅为 filing convenience，不是分类权威来源

## 3. Agent 系统与科研流程角色

- Agent 类型标签：LLM Agent；Multi-Agent System；Tool-using Agent
- 科研流程角色：simulation_modeling；tool_use_and_code_execution；evidence_assessment_and_validation
- 自主能力：planning；tool_use；feedback_iteration；multi_agent_collaboration
- 交叉属性标签：computation_driven；simulation_driven

## 4. 方法设计

1. 输入工程分析任务与边界条件。
2. 多代理分担建模、执行、检查和专家校验角色。
3. 调用求解代码或分析工具。
4. 根据中间结果进行纠错和协作调整。
5. 输出有限元分析结果。

## 5. 实验与验证

- 验证方式：simulation_validation
- 数据、任务与指标：线弹性有限元问题；比较不同协作配置成功率
- 关键结果：多代理角色组合显著影响求解稳定性
- 科学贡献类型：system_platform；engineering_analysis
- 证据强度：abstract-level first-hand evidence；approved arXiv fallback PDF 已归档，但本轮 closeout 仍为 `source_limited=yes`

## 6. 与已有工作的关系

- 与一般 code assistant 不同，这里强调多代理角色协同。
- 与通用 research-agent 平台不同，对象明确锚定在工程仿真。
- 可与结构分析、mechanics、CFD agent 样本并列。

## 7. 局限性与风险

- 当前强证据仍以 SSRN / arXiv 摘要级一手来源为主，官方 SSRN 全文在本环境仍 blocked。
- 科学贡献更偏流程自动化与协作优化，而非新工程规律发现。
- 主要剩余风险是 core-strength，而非主类风险。

## 8. 对综述写作的价值

- 可放入 `09` 类工程分析型 Agent 小节。
- 可支撑“多代理已进入工程科学仿真工作流”这一论点。
- 推荐引用强度：standard

## 9. 总结

### 9.1 一句话概括

多代理协作被直接用于有限元工程分析自动化。

### 9.2 速记版 pipeline

1. 接收工程仿真任务
2. 多代理分工求解
3. 调用分析代码
4. 反馈纠错
5. 输出 FEM 结果

### 9.3 标注字段汇总

```text
paper_id: ASD-0052
是否纳入：to_read
scientific_object_modules: 09
object_coverage_mode: single_module
primary_module_for_filing: 09
general_method_bucket: none
source_limited: yes
safety_access_status: source-limited: SSRN/DOI/PDF blocked or safe-open blocked; arXiv abstract available
归档细分标签: finite element analysis / engineering simulation; Engineering/scientific workflow agents
Agent 类型: LLM Agent; Multi-Agent System; Tool-using Agent
科研流程角色: simulation_modeling; tool_use_and_code_execution; evidence_assessment_and_validation
自主能力: planning; tool_use; feedback_iteration; multi_agent_collaboration
验证方式: simulation_validation
交叉属性: computation_driven; simulation_driven
科学贡献类型: system_platform; engineering_analysis
classification_confidence: high
纳入置信度: 高
first_hand_sources_checked: SSRN abstract page; DOI redirect / metadata check; arXiv abstract page
pdf_path: Reference_PDF/09_Engineering_and_Industrial_Technology_Sciences/Tian_2025_Autonomous_Finite_Element_Analysis.pdf
pdf_version: approved arXiv fallback PDF; local archive copy; `%PDF` header verified
推荐引用强度: standard
```
