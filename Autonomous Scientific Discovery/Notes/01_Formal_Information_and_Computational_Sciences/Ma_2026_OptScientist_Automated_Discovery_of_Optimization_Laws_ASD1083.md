# OptScientist: Automated Discovery of Optimization Laws

## 当前分类（2026-11-01 实证复核）

- 当前纳入状态：`to_read`；主归档：`01`。
- 本块为当前有效结论；后文既有分类、来源限制与审计判断均保留为历史记录，与本块不一致者由本块取代。
- 当前对象模块：`01;02;11`。
- 代表分类每个模块保留一个落点，不表示穷尽全文全部细类。

| 模块 | 二级 | 三级 | 本轮结论 |
|---|---|---|---|
| 01 | 01.01 数学 | 01.01.10 运筹学与优化 | 已落地 |
| 02 | 02.02 物理学 | 02.02.16 计算物理学 | 已落地 |
| 11 | 11.04 心理学与认知科学 | 11.04.06 行为科学 | 已落地 |

- 模块02：99个物理来源问题生成观测和恢复定律。
  - 证据：PDF 第 [8, 9, 10] 页；原文：OptScientist recovers diverse physical structures, including linear interactions, quadratic energy terms, inverse-square laws, heat-transfer terms and algebraically equivalent rational forms.

- 模块11：CPC18人类风险选择发现行为规律；另有央行货币政策。
  - 证据：PDF 第 [10, 11, 12] 页；原文：We next applied OptScientist to human decisions under risk and ambiguity

- 模块01：对象是优化规律，离散变量不等于组合数学。
  - 证据：PDF 第 [1, 8, 10] 页；原文：discovering compact symbolic optimization laws directly from data

- 完整裁决：`Coverage_Check/classification_recheck_2026-11-01/`。

## 既有笔记与历史审计记录

**论文信息**

- ID：ASD-1083
- 标题：OptScientist: Automated Discovery of Optimization Laws
- 作者：ZhenYao, Ma; Liang, Yue; Zhu, Jian-Qiao
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2610.28562
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1083.txt
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Ma_2026_OptScientist_Automated_Discovery_of_Optimization_Laws_ASD1083.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 科学目标 | 由数据发现紧凑符号优化规律。 | TXT lines 11-13；核验TXT行号 11 | recovering equations that describe observed input–output patterns. We introduce OptScientist, a novel automated framework for discovering compact symbolic optimization laws directly from data. OptScientist comprises (i) a model that | 高（一手正文；非独立复现） |
| 方法 | 理论先验、规律发现、机制抽象及建议采集数据。 | TXT lines 15-18；核验TXT行号 15 | optimization problem and then extracting its symbolic form, and (ii) an LLM agen- tic system embedding the model in a discovery process that integrates theoretical priors from scientific literature, discovers candidate laws, abstracts their underlying mechanisms, and suggests new data to collect. We first evaluate OptScientist on | 高（一手正文；非独立复现） |
| 基准 | OptFeynman含99个物理优化问题。 | TXT lines 18-20；核验TXT行号 18 | mechanisms, and suggests new data to collect. We first evaluate OptScientist on OptFeynman, a novel benchmark of 99 physics-derived optimization problems, where OptScientist recovers ground-truth laws for over 80% of the problems and | 高（一手正文；非独立复现） |
| 结果 | 恢复超过80%基准真实规律。 | TXT lines 19-21；核验TXT行号 19 | OptFeynman, a novel benchmark of 99 physics-derived optimization problems, where OptScientist recovers ground-truth laws for over 80% of the problems and remains robust to noisy contextual information, while substantially outperforming | 高（一手正文；非独立复现） |
| 跨领域案例 | 在人类风险选择和央行政策数据上测试预测表现。 | TXT lines 23-25；核验TXT行号 23 | man risky choice and central-bank monetary policy, OptScientist discovers compact symbolic optimization laws that achieve held-out predictive performance compet- itive with leading baselines, while using few parameters and substantially fewer | 高（一手正文；非独立复现） |

## 0. 摘要翻译

OptScientist从观测数据自动发现紧凑符号优化规律，由学习模型提取潜在优化问题结构，LLM Agent结合科学文献先验搜索候选规律、抽象机制并建议新数据。作者在99题物理基准上恢复超过80%的真实规律，并在行为选择和央行政策数据上取得与领先基线相当的留出预测表现。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。从观测数据发现产生现象的紧凑符号优化规律。
  - 原文位置：TXT lines 11-13；核验TXT行号 11；引文：recovering equations that describe observed input–output patterns. We introduce OptScientist, a novel automated framework for discovering compact symbolic optimization laws directly from data. OptScientist comprises (i) a model that
- 多步行动过程：yes。结合文献先验、候选规律发现、机制抽象和新数据建议。
  - 原文位置：TXT lines 15-18；核验TXT行号 15；引文：optimization problem and then extracting its symbolic form, and (ii) an LLM agen- tic system embedding the model in a discovery process that integrates theoretical priors from scientific literature, discovers candidate laws, abstracts their underlying mechanisms, and suggests new data to collect. We first evaluate OptScientist on
- 至少一种Agent能力：yes。符号模型和Agent协同生成、解释并检验规律。
  - 原文位置：TXT lines 18-20；核验TXT行号 18；引文：mechanisms, and suggests new data to collect. We first evaluate OptScientist on OptFeynman, a novel benchmark of 99 physics-derived optimization problems, where OptScientist recovers ground-truth laws for over 80% of the problems and
- 明确科研流程角色：yes。应用范围涵盖物理、生物、行为及社会科学优化机制。
  - 原文位置：TXT lines 26-29；核验TXT行号 26；引文：tokens than LLM baselines. Overall, OptScientist extends automated scientific discovery to uncovering optimization laws that generate observed phenomena, enabling automated theory building across the physical, biological, behavioral, and social sciences.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：01;02;11
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：01（仅归档，不覆盖其他模块）
- 模块内分类路径：01.01 数学；02.02 物理学；11.01 经济学；11.04 心理学与认知科学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

01为数学优化关系，02为物理基准，11为行为/社会对象，按多对象覆盖保留三模块。

### 2.3 容易混淆的边界

01为数学优化关系，02为物理基准，11为行为/社会对象，按多对象覆盖保留三模块。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

llm_scientific_agent

### 3.2 科研流程角色

law_discovery；mechanism_interpretation；experiment_suggestion

Optimization Learner学习数据的优化表示，Discoverer提取符号形式，LLM Agent负责文献先验、规律解释、候选筛选和新数据建议。

### 3.3 自主能力

符号模型和Agent协同生成、解释并检验规律。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

科学贡献是多个物理及社会行为数据中的优化规律；系统贡献是将符号学习与Agent文献推理和实验建议结合。

### 4.2 系统流程与组件

输入观测数据及文献先验；OptLearner将数据表示为优化问题，OptDiscover从学习表示中蒸馏目标和约束的符号形式；Agent解释机制并比较候选，结合证据提出后续数据，输出优化定律及预测。 这一工作流的实施细节、输入输出和验证范围均按原文所报告内容理解，不将展示案例外推为普遍能力。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

OptFeynman 99个物理问题以真实规律恢复率和噪声稳健性评估；人类风险选择和央行政策数据以留出预测对比机器学习、符号和LLM基线。

### 5.2 基线、指标与结果

作者报告基准恢复率超过80%；两个社会科学案例的留出预测与领先基线竞争，同时使用较少参数。

### 5.3 科学贡献与证据强度

科学贡献是多个物理及社会行为数据中的优化规律；系统贡献是将符号学习与Agent文献推理和实验建议结合。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

区别于发现输入输出方程的符号回归、预设优化形式的逆优化及仅生成解释性程序的方法。

## 7. 局限性与风险

- author_stated：正文局限讨论指出优化规律的可辨识性受观测数据和设定限制，具体案例的解释仍需科学判断。
- reviewer_inference：预测性能相当不等于所推断的潜在优化机制为唯一真实解释。

## 8. 对综述写作的价值

支持自动科研从拟合输入输出规律转向发现生成现象的潜在优化问题。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

OptScientist结合符号学习和Agent推理从数据发现优化规律。

### 9.2 速记版 pipeline

输入观测数据及文献先验；OptLearner将数据表示为优化问题，OptDiscover从学习表示中蒸馏目标和约束的符号形式；Agent解释机制并比较候选，结合证据提出后续数据，输出优化定律及预测。 这一工作流的实施细节、输入输出和验证范围均按原文所报告内容理解，不将展示案例外推为普遍能力。

### 9.3 标注字段汇总

```text
paper_id=ASD-1083
inclusion_status=to_read
scientific_object_modules=01;02;11
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=01
module_taxonomy_codes=01.01;02.02;11.01;11.04
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O2 既定基准 | 在OptFeynman基准恢复真实优化规律 | “OptFeynman, a novel benchmark of 99 physics-derived” · L49 |
| 验证强度 | V1 基准/内部评测 | 基准恢复率及留出预测评估无独立实验 | “recovers ground-truth laws for over 80%” · L49 |
| 系统自主性 | L2 闭环执行者 | Agent搜索候选规律并建议新数据采集 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
