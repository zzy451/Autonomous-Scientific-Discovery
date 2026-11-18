# XScientist: A Git-Like Research Protocol for Long-Running Autonomous Scientific Discovery

## 当前分类（2026-11-01 实证复核）

- 当前纳入状态：`to_read`；主归档：`11`。
- 本块为当前有效结论；后文既有分类、来源限制与审计判断均保留为历史记录，与本块不一致者由本块取代。
- 当前对象模块：`01;11`。
- 代表分类每个模块保留一个落点，不表示穷尽全文全部细类。

| 模块 | 二级 | 三级 | 本轮结论 |
|---|---|---|---|
| 01 | 01.02 计算机科学 | 01.02.13 机器学习 | 已落地 |
| 11 | 11.07 科学系统与知识生产研究 | 11.07.09 科学解释与科学证据理论 | 已落地 |

- 模块01：实际运行AIRS-Bench SICK分类相似度实验。
  - 证据：PDF 第 [12, 13] 页；原文：On classification, XScientist scores 0.8182, compared with 0.8127 for AIDE and 0.8047 for AI Scientist-v2

- 完整裁决：`Coverage_Check/classification_recheck_2026-11-01/`。

## 既有笔记与历史审计记录

**论文信息**

- ID：ASD-0961
- 标题：XScientist: A Git-Like Research Protocol for Long-Running Autonomous Scientific Discovery
- 作者：Luo, Jixiang
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2607.12301
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0961.txt
- PDF / 本地文件路径：Reference_PDF/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Jixiang_2026_XScientist_A_Git_Like_Research_Protocol_for_Long_Running_ASD0961.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 纳入判断：论文直接研究科研Agent或其评测。 | XScientist将研究状态而非论文作为长程工作的延续单元，以Git式协议记录假设、实验、观察、主张、评审和交接，供后续Agent或研究者检查、分支和继续。系统强调跨会话可移交。 | TXT line 289；核验TXT行号 287 | Autonomous research systems can generate plausible papers while losing the decisions, failed branches, and evidence needed to inspect or continue the work. We present XScientist, a local-first, git-like protocol that treats research state, rather than a manuscript, as the unit of continuation. | 高（一手正文；非独立复现） |
| 对象证据：正文界定科学问题及研究对象。 | 论文对象是科研状态、实验分支、主张—证据闭合及研究记录完整性协议，属于计算机科学的软件工程实现与科学证据/知识生产研究；Breast Cancer Wisconsin数据用于协议完整性故障注入，不是癌症机制研究。 | TXT line 291；核验TXT行号 291 | Hypotheses, experiment attempts, observations, claims, reviews, and handoffs | 高（一手正文；非独立复现） |
| 方法证据：全文描述Agent操作或评测流程。 | 论文定义对象和转换协议，构建参考实现并设计完整性核查及外部任务试点。协议保留分支和更正，并将主张与证据关联；评估区分完整性与任务表现。并用受控操作记录人类授权边界。 | TXT line 298；核验TXT行号 297 | A reference implementation integrates planning, execution, review, repair, and supervised long-running operation while preserving provenance across these stages. | 高（一手正文；非独立复现） |
| 验证证据：实验报告任务、数据与验证设计。 | 工作贡献是让长期科研决策、失败路径及证据有可检查记录。故障测试覆盖多类不一致，外部任务被作者称为可行性研究。 | TXT line 1678；核验TXT行号 1678 | The study uses 20 real executions on the public Breast Cancer Wisconsin dataset [46, 47], producing 20 intact ARAs. Each is copied into six fixed single-fault variants (changed code, changed metric, graph cycle, dangling endpoint, missing code, and invalid schema type), yielding 120 paired fixtures. | 高（一手正文；非独立复现） |
| 结果贡献：正文报告可核查结果和贡献。 | 癌症数据实验仅作协议测试；论文贡献是科研基础设施而非生物学发现，归入01一般方法。 | TXT line 2382；核验TXT行号 2382 | XScientist does not make autonomous research automatically correct. The system can organize evidence, preserve provenance, and expose warnings, but human review remains necessary for scientific validity, ethical judgment, and final submission decisions. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

XScientist将研究状态而非论文作为长程工作的延续单元，以Git式协议记录假设、实验、观察、主张、评审和交接，供后续Agent或研究者检查、分支和继续。系统强调跨会话可移交。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。正文提出科学研究或科学评测目标。
  - 原文位置：TXT line 289；核验TXT行号 287；引文：Autonomous research systems can generate plausible papers while losing the decisions, failed branches, and evidence needed to inspect or continue the work. We present XScientist, a local-first, git-like protocol that treats research state, rather than a manuscript, as the unit of continuation.
- 多步行动过程：yes。正文描述多阶段行动及反馈流程。
  - 原文位置：TXT line 291；核验TXT行号 291；引文：Hypotheses, experiment attempts, observations, claims, reviews, and handoffs are represented as typed, content-addressed objects in an exploration graph.
- 至少一种Agent能力：yes。正文显示Agent使用工具、状态或证据进行决策。
  - 原文位置：TXT line 298；核验TXT行号 297；引文：A reference implementation integrates planning, execution, review, repair, and supervised long-running operation while preserving provenance across these stages.
- 明确科研流程角色：yes。系统承担科研执行、理论发现或科研评价角色。
  - 原文位置：TXT line 1678；核验TXT行号 1678；引文：The study uses 20 real executions on the public Breast Cancer Wisconsin dataset [46, 47], producing 20 intact ARAs. Each is copied into six fixed single-fault variants (changed code, changed metric, graph cycle, dangling endpoint, missing code, and invalid schema type), yielding 120 paired fixtures.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：01;11
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：11（仅归档，不覆盖其他模块）
- 模块内分类路径：01.02.04 软件工程；11.07.09 科学解释与科学证据理论
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

协议的研究对象是科学工作记录和证据链，依11.07.09科学解释与科学证据理论归类；其可执行协议和版本化实现同时对应01.02.04软件工程。乳腺癌数据仅作为完整性工作负载，不构成生物学主张。

### 2.3 容易混淆的边界

协议的研究对象是科学工作记录和证据链，依11.07.09科学解释与科学证据理论归类；其可执行协议和版本化实现同时对应01.02.04软件工程。乳腺癌数据仅作为完整性工作负载，不构成生物学主张。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

科研工作流Agent；工具增强Agent

### 3.2 科研流程角色

状态管理；实验执行；评审修复

参考实现整合规划、执行、评审、修复和受监督运行；研究对象以类型化图节点保存，提供检查点、失败记录、证据闭合、重放边界和权限门控，并可导出ARA。

### 3.3 自主能力

正文显示Agent使用工具、状态或证据进行决策。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

相较只保存代码或实验追踪，XScientist将主张、证据、评审及交接纳入可移交的探索图，并强调完整性不等于科学正确。

### 4.2 系统流程与组件

论文定义对象和转换协议，构建参考实现并设计完整性核查及外部任务试点。协议保留分支和更正，并将主张与证据关联；评估区分完整性与任务表现。并用受控操作记录人类授权边界。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

完整性实验从20次真实执行生成20个完好ARA，再构造六类故障版本共120个配对样例；另报告多个有限范围的外部任务试点。

### 5.2 基线、指标与结果

工作贡献是让长期科研决策、失败路径及证据有可检查记录。故障测试覆盖多类不一致，外部任务被作者称为可行性研究。

### 5.3 科学贡献与证据强度

相较只保存代码或实验追踪，XScientist将主张、证据、评审及交接纳入可移交的探索图，并强调完整性不等于科学正确。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

外部任务规模有限；重执行可能依赖外部API或GPU；自然论文场景误报漏报率尚未测量，ARA也尚非通用标准。

## 7. 局限性与风险

癌症数据实验仅作协议测试；论文贡献是科研基础设施而非生物学发现，归入01一般方法。

## 8. 对综述写作的价值

XScientist提出Git式科研协议和ARA格式，并用20次执行与120个故障变体检查研究记录完整性；协议不能保证科学正确。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

XScientist提出Git式科研协议和ARA格式，并用20次执行与120个故障变体检查研究记录完整性；协议不能保证科学正确。

### 9.2 速记版 pipeline

论文定义对象和转换协议，构建参考实现并设计完整性核查及外部任务试点。协议保留分支和更正，并将主张与证据关联；评估区分完整性与任务表现。并用受控操作记录人类授权边界。

### 9.3 标注字段汇总

```text
paper_id=ASD-0961
inclusion_status=to_read
scientific_object_modules=01;11
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=11
module_taxonomy_codes=01.02.04;11.07.09
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O2 既定基准 | Breast Cancer Wisconsin数据用于协议完整性测试为预定义任务 | “完整性实验从20次真实执行生成20个完好ARA” · L120 |
| 验证强度 | V1 基准/内部评测 | 故障测试和完整性检查，无独立复现科学发现 | “再构造六类故障版本共120个配对样例” · L120 |
| 系统自主性 | L1 任务助手 | 系统记录研究状态和决策，但科学流程由框架管理 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
