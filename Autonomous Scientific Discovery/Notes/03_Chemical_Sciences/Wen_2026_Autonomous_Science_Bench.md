# Autonomous Science Bench: Evaluating AI Agents for Autonomous Scientific Discovery

## 当前分类（2026-11-01 实证复核）

- 当前纳入状态：`included`；主归档：`03`。
- 本块为当前有效结论；后文既有分类、来源限制与审计判断均保留为历史记录，与本块不一致者由本块取代。
- 当前对象模块：`03;04;06`。
- 代表分类每个模块保留一个落点，不表示穷尽全文全部细类。

| 模块 | 二级 | 三级 | 本轮结论 |
|---|---|---|---|
| 03 | 03.03 合成、反应与催化 | 03.03.03 催化化学 | 已落地 |
| 04 | 04.04 能源、电子与器件材料 | 04.04.03 催化材料 | 已落地 |
| 06 | 06.03 生物技术相关科学 | 06.03.06 蛋白质科学 | 已落地 |

- 模块04：OER金属氧化物回放任务成分选择及过电位结果。
  - 证据：PDF 第 [7, 20] 页；原文：The agent orders four rounds of 48 from 3,419 two- and three-cation compositions

- 完整裁决：`Coverage_Check/classification_recheck_2026-11-01/`。

## 既有笔记与历史审计记录

**论文信息**

- ID：ASD-0914
- 标题：Autonomous Science Bench: Evaluating AI Agents for Autonomous Scientific Discovery
- 作者：Wen, Yibo; Liu, Han
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2610.18449
- 一手阅读来源：https://arxiv.org/abs/2610.18449
- 来源层级：全文
- 阅读版本：对应缓存来源版本，参见Evidence Log
- 阅读版本题名：Autonomous Science Bench: Evaluating AI Agents for Autonomous Scientific Discovery
- 原始全文缓存：C:/Users/20683/Desktop/综述/.tmp_asd_pdfs/source_F/2610.18449.pdf
- PDF / 本地文件路径：Reference_PDF/03_Chemical_Sciences/Wen_2026_Autonomous_Science_Bench.pdf
- 当前状态：included
- 阅读日期：2026-10-22
- 笔记作者：Codex（读者证据包经主控审核整合）

## Evidence Log

| 判断项 | 结论 / 原文概括 | 证据位置 | 可信度 |
|---|---|---|---|
| Agent交互 | Agent挑选实验batch并提交lab service，服务返回测量后Agent重拟合模型并选下一轮。 | §2；Fig. 1 | high |
| 实验依据 | 六项campaign基于已发表实验，覆盖生物、化学和材料领域。 | §2.5；Campaign Cards | high |
| 具体对象 | 卡片列出Nuclease Engineering、Cell-Free Biosensor、CO2-to-Propylene、Suzuki条件筛选及催化剂组成任务。 | §10 Campaign Cards | high |
| 评价方式 | Discovery gate评价已经测量的候选；Learning gate评价预测器对held-out候选的排序。 | §2.4 Two Gates | high |
| 试验结果 | 8种Agent/模型配置共144次trial，最佳通过率67%，最难campaign为3/24。 | §4 Results；Abstract | high |
| 解释价值 | 论文指出整体成功率会掩盖“发现好候选”与“学会泛化排序”的不同失败模式。 | §4.2 | high |

## 0. 摘要翻译

Autonomous Science Bench以有限预算的design-build-test-learn campaign评测Agent。Agent逐轮选择实验设计，lab service返回测量结果后再更新模型并选择下一轮。六项campaign源自已发表的生物、化学和材料实验。144次试验中最佳配置成功率67%，最难任务仅3/24成功；发现门和学习门能揭示不同失败类型。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 当前判断：included；读者建议：included。
全文明确Agent在有限预算下多轮选择设计、调用lab service、接收测量反馈并调整后续实验；六项campaign有具体实验对象与verifier，符合Agent标准。

### 1.2 排除风险检查

按具体对象记录03/04/06，不因benchmark形式归01.04。核酸酶工程归06.03.06蛋白质科学；cell-free biosensor暂归06.03.07生物制造/生物技术相关；化学反应与材料催化分别为03.03、04.04。
完整闭环不是纳入门槛；科研目标、多步行动、至少一项Agent能力及明确科研角色须同时成立。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：03;04;06
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：03（仅归档，不替代多模块事实）
- 模块内分类路径：03.03; 04.04; 06.03.06
- 分类深度：03/04使用二级；06/07使用固定三级；其余沿用现有树。
- 分类状态：原文证据复核

### 2.2 对象优先判定

对象包括生物核酸酶工程和cell-free biosensor，化学CO2-to-propylene电催化和Suzuki–Miyaura条件筛选，及材料催化剂组成筛选。比较8种agent-model配置、144 trials。指标为已测设计的discovery gate、未测候选排序的learning gate和预算表现。最佳配置成功率67%，最难campaign仅3/24成功。

### 2.3 容易混淆的边界

按具体对象记录03/04/06，不因benchmark形式归01.04。核酸酶工程归06.03.06蛋白质科学；cell-free biosensor暂归06.03.07生物制造/生物技术相关；化学反应与材料催化分别为03.03、04.04。

## 3. Agent 系统与科研流程角色

全文明确Agent在有限预算下多轮选择设计、调用lab service、接收测量反馈并调整后续实验；六项campaign有具体实验对象与verifier，符合Agent标准。

科研流程与自主能力以本文实际行动和工具调用为依据：

每个campaign提供候选设计、初始数据和stateful lab API；Agent提交固定大小batch，获取隐藏测量后迭代更新模型；最终通过discovery gate与learning gate分别评分。

## 4. 方法设计

### 4.1 方法动机与设计

以可调用实验室服务和真实实验测量评估预算下的主动实验决策，并分开测量发现能力与对未见候选的泛化学习。

### 4.2 系统流程与组件

每个campaign提供候选设计、初始数据和stateful lab API；Agent提交固定大小batch，获取隐藏测量后迭代更新模型；最终通过discovery gate与learning gate分别评分。

## 5. 实验与验证

### 5.1 验证方式、对象及任务

对象包括生物核酸酶工程和cell-free biosensor，化学CO2-to-propylene电催化和Suzuki–Miyaura条件筛选，及材料催化剂组成筛选。比较8种agent-model配置、144 trials。指标为已测设计的discovery gate、未测候选排序的learning gate和预算表现。最佳配置成功率67%，最难campaign仅3/24成功。

### 5.2 基线、指标与结果

对象包括生物核酸酶工程和cell-free biosensor，化学CO2-to-propylene电催化和Suzuki–Miyaura条件筛选，及材料催化剂组成筛选。比较8种agent-model配置、144 trials。指标为已测设计的discovery gate、未测候选排序的learning gate和预算表现。最佳配置成功率67%，最难campaign仅3/24成功。

### 5.3 科学贡献与证据强度

以可调用实验室服务和真实实验测量评估预算下的主动实验决策，并分开测量发现能力与对未见候选的泛化学习。

证据层级：原始全文支持；作者报告结果不等于独立复现。

## 6. 与已有工作的关系

连接科学发现Agent、主动学习和实验规划benchmark；相对固定数据集或纯模拟环境，强调多轮实验测量反馈。

## 7. 局限性与风险

只覆盖六个campaign与固定候选池，不能推断所有实验科学任务或真实机器人实验室的可靠性。生物领域三级代码按核酸酶蛋白与biosensor生物技术暂拟。

## 8. 对综述写作的价值

本批最直接的主动实验Agent benchmark案例，可用于分析有限预算、真实测量、迭代决策和对象多模块分类。

推荐引用强度：普通引用，可在核对原文后用于相应领域案例。

## 9. 总结

### 9.1 一句话概括

用预算约束实验考核发现与学习

### 9.2 速记版 pipeline

每个campaign提供候选设计、初始数据和stateful lab API；Agent提交固定大小batch，获取隐藏测量后迭代更新模型；最终通过discovery gate与learning gate分别评分。

### 9.3 标注字段汇总

```text
paper_id=ASD-0914
inclusion_status=included
scientific_object_modules=03;04;06
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=03
module_taxonomy_codes=03.03; 04.04; 06.03.06
source_level=fulltext
fulltext_followup_required=false
```

### 全文后续要求

本轮已读原始全文并完成对象分类；无需为纳入/分类另做全文补读。具体引用时仍需回查相应原文位置。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O3 新实例 | Agent在有限预算内逐轮选择实验设计并从lab service获取测量结果，目标是在候选池中发现满足阈值的设计，答案可由完整测量验证 | “Agent挑选实验batch并提交lab service，服务返回测量后Agent重拟合模型” · L45 |
| 验证强度 | V2 计算/仿真/回顾性 | 六项campaign基于已发表实验的测量数据，discovery gate评价已测候选，learning gate评价held-out排序，属计算验证 | “六项campaign基于已发表实验” · L46 |
| 系统自主性 | L2 闭环执行者 |  | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
