# QuantumNovelty: A Skill-Orchestrating Language Agent for Referee-Style Review and Patentability Screening of Quantum Papers and Patents

## 当前分类（2026-11-01 实证复核）

- 当前纳入状态：`included`；主归档：`11`。
- 本块为当前有效结论；后文既有分类、来源限制与审计判断均保留为历史记录，与本块不一致者由本块取代。
- 当前对象模块：`02;11`。
- 代表分类每个模块保留一个落点，不表示穷尽全文全部细类。

| 模块 | 二级 | 三级 | 本轮结论 |
|---|---|---|---|
| 02 | 02.02 物理学 | 02.02.06 量子力学 | 已落地 |
| 11 | 11.07 科学系统与知识生产研究 | 11.07.08 科学方法论 | 已落地 |

- 模块02：实际两比特Hamiltonian候选电路SPSA优化。
  - 证据：PDF 第 [16] 页；原文：We drove the ansatz-discovery loop to a small archive of candidate circuits for a two-qubit Hamiltonian and scored each with the bundled state-vector evaluator

- 完整裁决：`Coverage_Check/classification_recheck_2026-11-01/`。

## 既有笔记与历史审计记录

**论文信息**

- ID：ASD-0922
- 标题：QuantumNovelty: A Skill-Orchestrating Language Agent for Referee-Style Review and Patentability Screening of Quantum Papers and Patents
- 作者：Kashani, Shlomo
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2608.16900
- 一手阅读来源：https://arxiv.org/abs/2608.16900
- 来源层级：全文
- 阅读版本：对应缓存来源版本，参见Evidence Log
- 阅读版本题名：QuantumNovelty: A Skill-Orchestrating Language Agent for Referee-Style Review and Patentability Screening of Quantum Papers and Patents
- 原始全文缓存：C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/.tmp_asd_pdfs/ASD-0922.html
- PDF / 本地文件路径：未归档PDF
- 当前状态：included
- 阅读日期：2026-10-22
- 笔记作者：Codex（读者证据包经主控审核整合）

## Evidence Log

| 判断项 | 结论 / 原文概括 | 证据位置 | 可信度 |
|---|---|---|---|
| Agent 生成和审查量子科研产物 | 可生成量子计算论文、Pareto ansatz、专利草稿并模拟审稿/审查面板。 | Abstract; §1 | high |
| 分派器路由至多种技能管线 | 含 novelty-audit、paper-audit、patent-audit、scout 和 authoring。 | §3 full execution flow; §4 | high |
| 确定性审计层检查主张 | 使用 Pareto 支配、文件复算、Wilson 区间、跨供应商共识保护。 | §5; Figure 2 | high |
| 对抗验证检查植入过度主张 | 摘要称植入主张全部检出且无误报。 | §10.2 | high |
| 真实部署不是专家准确率验证 | 六篇稿件和一个专利案例；没有人工审稿标签，作者明确不宣称模拟结果等同专家。 | §8; §9; §12 | high |

## 0. 摘要翻译

QuantumNovelty 是技能编排语言 Agent，可生成量子计算论文、Pareto ansatz 候选和专利草稿，也能模拟审稿人/专利审查面板进行审查。确定性审计/证伪门控限制可接受的主张，并记录模型调用来源与成本。作者不声称与人类专家一致；在植入对抗语料上检测所有植入过度主张且无误报，并报告六篇稿件及专利的部署。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 当前判断：included；读者建议：included。
Agent 按用户请求分派技能，执行多阶段论文生成或审阅，调用模型与确定性验证工具；角色包括量子研究产物生成、科研主张审查和证据核验。

### 1.2 排除风险检查

02 由量子算法/稿件具体案例支撑；11.07 由科学审稿、主张和证据核验工作流支撑。暂标 02.02.06、11.07.08/09；主展示取 11。专利部分不单独扩至工程/法律模块。
完整闭环不是纳入门槛；科研目标、多步行动、至少一项Agent能力及明确科研角色须同时成立。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：02;11
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：11（仅归档，不替代多模块事实）
- 模块内分类路径：02.02.06; 11.07.08; 11.07.09
- 分类深度：03/04使用二级；06/07使用固定三级；其余沿用现有树。
- 分类状态：原文证据复核

### 2.2 对象优先判定

对象：量子计算稿件/算法产物（VQE、LCU-Trotter、QML、QCNN、Majorana 等）与科学审稿/主张审计流程。对抗集测试植入主张检出；真实部署包括六篇稿件及专利审查案例。无人工审稿标签；与公开接受/授权结果仅作方向性比较，不是专家准确率。

### 2.3 容易混淆的边界

02 由量子算法/稿件具体案例支撑；11.07 由科学审稿、主张和证据核验工作流支撑。暂标 02.02.06、11.07.08/09；主展示取 11。专利部分不单独扩至工程/法律模块。

## 3. Agent 系统与科研流程角色

Agent 按用户请求分派技能，执行多阶段论文生成或审阅，调用模型与确定性验证工具；角色包括量子研究产物生成、科研主张审查和证据核验。

科研流程与自主能力以本文实际行动和工具调用为依据：

意图路由器按请求选择作者、审查、漏洞审计、专利审查等 pipeline；生成端创建量子论文/ansatz，审查端由模型面板与确定性 gate 复算产物、指标及证据，并记录调用/成本。

## 4. 方法设计

### 4.1 方法动机与设计

提出可审计、可复算并记录成本的量子科研生成与评审 Agent，并限定结论强度。

### 4.2 系统流程与组件

意图路由器按请求选择作者、审查、漏洞审计、专利审查等 pipeline；生成端创建量子论文/ansatz，审查端由模型面板与确定性 gate 复算产物、指标及证据，并记录调用/成本。

## 5. 实验与验证

### 5.1 验证方式、对象及任务

对象：量子计算稿件/算法产物（VQE、LCU-Trotter、QML、QCNN、Majorana 等）与科学审稿/主张审计流程。对抗集测试植入主张检出；真实部署包括六篇稿件及专利审查案例。无人工审稿标签；与公开接受/授权结果仅作方向性比较，不是专家准确率。

### 5.2 基线、指标与结果

对象：量子计算稿件/算法产物（VQE、LCU-Trotter、QML、QCNN、Majorana 等）与科学审稿/主张审计流程。对抗集测试植入主张检出；真实部署包括六篇稿件及专利审查案例。无人工审稿标签；与公开接受/授权结果仅作方向性比较，不是专家准确率。

### 5.3 科学贡献与证据强度

提出可审计、可复算并记录成本的量子科研生成与评审 Agent，并限定结论强度。

证据层级：原始全文支持；作者报告结果不等于独立复现。

## 6. 与已有工作的关系

与直接操作实验设备的量子 Agent 不同，核心职责是研究产物生成、模拟审稿和证据核验；较通用 LLM-as-judge 增加确定性证伪门控。

## 7. 局限性与风险

样本小、缺少专家标签，真实案例只是使用展示；部分 pipeline 未在真实输入上端到端运行；专利审查不能代表同行评议。

## 8. 对综述写作的价值

适合讨论科学 Agent 自审、证据完整性、自动同行评议边界及 02/11 多模块分类。

推荐引用强度：普通引用，可在核对原文后用于相应领域案例。

## 9. 总结

### 9.1 一句话概括

Agent核验量子论文与专利新颖性

### 9.2 速记版 pipeline

意图路由器按请求选择作者、审查、漏洞审计、专利审查等 pipeline；生成端创建量子论文/ansatz，审查端由模型面板与确定性 gate 复算产物、指标及证据，并记录调用/成本。

### 9.3 标注字段汇总

```text
paper_id=ASD-0922
inclusion_status=included
scientific_object_modules=02;11
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=11
module_taxonomy_codes=02.02.06; 11.07.08; 11.07.09
source_level=fulltext
fulltext_followup_required=false
```

### 全文后续要求

本轮已读原始全文并完成对象分类；无需为纳入/分类另做全文补读。具体引用时仍需回查相应原文位置。


## 2026-10-29 PDF补齐归档

- 本地PDF：`Reference_PDF/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/ASD-0922_QuantumNovelty_A_Skill_Orchestrating_Language_Agent_for_Referee_Style_Review_and_Patentability_Screening_.pdf`，共26页；已核验标题、页面解析和逐页渲染。
- 下载来源：https://arxiv.org/pdf/2608.16900
- 版本：official arXiv preprint PDF; version as downloaded。
- 本轮为来源文件归档，不自动改变既有科学分类或将未决PR意见标记为已结案。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O3 新实例 | 模拟量子计算稿件审稿和专利审查，确定性审计层检查Pareto支配、文件复算等主张，答案可由计算验证 | “使用 Pareto 支配、文件复算、Wilson 区间、跨供应商共识保护” · L46 |
| 验证强度 | V1 基准/内部评测 | 对抗验证检出植入主张，真实部署无人工审稿标签，不是专家准确率验证 | “植入主张全部检出且无误报” · L47 |
| 系统自主性 | L2 闭环执行者 |  | — |

- 强验证（V3–V4）：否
- 置信度：medium；需全文复核：是；争议记录：无
- 复核状态：待专家复核：需全文复核
