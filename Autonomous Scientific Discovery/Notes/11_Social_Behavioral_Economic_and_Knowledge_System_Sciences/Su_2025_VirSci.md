# Su et al. 2025 - Many heads are better than one: Improved scientific idea generation by a LLM-based multi-agent system

**论文信息**
- 标题：Many heads are better than one: Improved scientific idea generation by a LLM-based multi-agent system
- 作者：Su et al.
- 年份：2025
- 来源 / venue：ACL
- DOI / arXiv / URL：https://aclanthology.org/2025.acl-long.1368/
- PDF / 本地文件路径：`Reference_PDF/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Su_2025_VirSci.pdf`
- First-hand source checked：ACL landing page；ACL PDF
- PDF version：official ACL PDF
- Source-limited status：no
- 论文类型：系统论文 / scientific idea-generation agent
- 当前状态：to_read
- 阅读与复核日期：2026-06-22
- 笔记作者：Codex

## Evidence Log

### 2026-06-22 reaudit writeback revision

- Round decision：从旧的 `01 / 01.04` framing 改为 `scientific_object_modules=11`，`primary_module_for_filing=11`，`general_method_bucket=none`。
- Archive sync：已写入 canonical PDF 路径 `Reference_PDF/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Su_2025_VirSci.pdf`。
- Filing note：本 note 已从旧的 `Notes/01_Formal_Information_and_Computational_Sciences/` 路径迁移到 `Notes/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/`；note 位置仅反映 filing convenience，不作为独立分类证据。
- Policy note：这篇论文不应继续写成 general-method `01.04`。其稳定对象是 scientific idea generation 这一知识生产环节本身，因此更适合 `11` 的 scientific-knowledge-production framing。

| 判断项 | 结论 | 证据位置 | 原文短摘或概括 | 可信度 |
|---|---|---|---|---|
| Agent 纳入 | 是 | ACL landing；ACL PDF | 系统面向明确科研目标，包含多 Agent 协作、想法生成、互评与筛选流程 | 高 |
| 科学对象归类 | `11` | ACL PDF | 论文研究的是 scientific idea generation 与研究想法评估这一知识生产过程，而不是领域无关 research-agent infrastructure | 中高 |
| 方法流程 | 多 Agent idea-generation workflow | ACL PDF | 多个 agent 协同生成、批评、改写和筛选 scientific ideas | 高 |
| 实验验证 | benchmark / human evaluation | ACL PDF | 主要通过 scientific idea generation benchmark 与人工评估检验想法质量提升 | 中高 |
| 边界判断 | 不应继续留在 `01` / `01.04` | ACL PDF | 研究对象不是形式/计算对象本身，而是 scientific knowledge production 中的 idea-generation 环节 | 中高 |

## 0. 摘要概述

论文围绕 scientific idea generation 提出一个 LLM-based multi-agent system，核心是把研究想法的生成、互评、修订和筛选组织成可迭代的知识生产流程。当前项目口径下，它不应再被写成通用 scientific workflow method 或独立 `01.04` bucket。更稳定的理解是：这篇论文直接研究 scientific idea generation 这一 research-community / knowledge-production object，因此应放入 `11`。

## 1. 是否纳入本综述

- 是否属于 Agent 文献：是
- 判断依据：系统围绕科研目标执行多步 idea-generation workflow，并具备规划、反馈迭代和多 Agent 协作
- 判定置信度：高
- 在科研流程中承担的明确角色：hypothesis_generation；scientific_problem_formulation；evidence_assessment_and_validation
- 是否仍需进一步全文复核：否，ACL landing 与 ACL PDF 已足以支撑本轮写回

## 2. 科学领域归类

- 最终科学对象模块：`11`
- primary_module_for_filing：`11`
- general_method_bucket：`none`
- 对象覆盖方式：single-module
- 描述性子方向：scientific knowledge production / research idea generation
- 最终科学研究对象：scientific idea generation 与 research-idea evaluation
- 最终科学问题：如何通过多 Agent 协作提升科研想法生成质量
- 容易混淆的边界：`01.04`；一般通用 workflow agent
- 最终判定：改归 `11`
- 判定理由：论文直接研究和优化的是 scientific knowledge production 中的 idea-generation 环节，而不是形式/计算对象实验，也不是无具体对象的通用科研平台

## 3. Agent 系统与科研流程角色

- Agent 类型标签：LLM Agent；Multi-Agent System；Hybrid Agent
- 科研流程角色：hypothesis_generation；scientific_problem_formulation；evidence_assessment_and_validation
- 自主能力：planning；feedback_iteration；autonomous_decision_making；multi_agent_collaboration
- 交叉属性标签：computation_driven；knowledge_production_support

## 4. 方法设计

1. 输入研究主题或问题上下文。
2. 多个 agent 生成候选 scientific ideas。
3. Agent 间对候选想法进行批评、比较和修订。
4. 汇总多轮反馈并筛选更优研究想法。
5. 输出质量更高的 scientific ideas 及其评价结果。

## 5. 实验与验证

- 验证方式：benchmark；expert_evaluation
- 数据、任务与指标：scientific idea generation benchmark；人工评估/质量比较
- 关键结果：多 Agent 协作优于单头式 idea generation setting
- 科学贡献类型：hypothesis；system_platform；knowledge_production_analysis
- 证据强度：first_hand_full_text

## 6. 与已有工作的关系

- 与普通 AI for Science 方法的区别：它研究的不是自然科学对象实验，而是科研想法生成这一知识生产过程。
- 与一般 `01.04` 通用 workflow 系统的区别：这里的验证对象和改进目标就是 scientific idea generation quality itself。
- 与同一科学领域其他 Agent 文献的关系：可与 ResearchTown、peer-review agents、scientific-evaluation systems 共同构成 `11` 中的 knowledge-production 子群。

## 7. 局限性与风险

- 当前验证仍主要依赖 benchmark 与人工评估，而非真实长期科研产出追踪。
- `11` 内部更细的 `11.07` 子方向描述是合理候选，但本轮主模块层面只需稳定落在 `11`。
- 代表性强度仍受 idea-quality evaluation design 影响。

## 8. 对综述写作的价值

- 可放入 `11` 社会、行为、经济与知识系统科学章节中的 scientific knowledge production 脉络。
- 可支撑“scientific idea generation itself is a knowledge-production object”这一论点。
- 也可作为 `11 / 01.04` 边界样本，说明研究对象若是科研知识生产环节本身，就不应继续留在独立 general-method bucket。
- 推荐引用强度：standard

## 9. 总结

### 9.1 一句话概括

这篇论文研究的是科研想法生成这一知识生产过程本身，因此应归入 `11`，而不再是旧的 `01 / 01.04` 记录。

### 9.2 速记版 pipeline

1. 接收研究主题
2. 多 Agent 生成候选 idea
3. 互评、批改与筛选
4. 输出更高质量的 scientific ideas

### 9.3 标注字段汇总

```text
是否纳入：to_read
scientific_object_modules：11
primary_module_for_filing：11
general_method_bucket：none
object_coverage_mode：single_module
描述性子方向：scientific knowledge production / research idea generation
Agent 类型：LLM Agent; Multi-Agent System; Hybrid Agent
科研流程角色：hypothesis_generation; scientific_problem_formulation; evidence_assessment_and_validation
自主能力：planning; feedback_iteration; autonomous_decision_making; multi_agent_collaboration
验证方式：benchmark; expert_evaluation
交叉属性：computation_driven
科学贡献类型：hypothesis; system_platform; knowledge_production_analysis
证据强度：first_hand_full_text
source_limited：no
归类置信度：中高
纳入置信度：高
推荐引用强度：standard
```
