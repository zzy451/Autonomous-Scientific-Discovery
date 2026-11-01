# Beyond Equation Search: Conjecture-Guided Discovery with SCOPE and ClosureBench

## 当前分类（2026-11-01 实证复核）

- 当前纳入状态：`to_read`；主归档：`01`。
- 本块为当前有效结论；后文既有分类、来源限制与审计判断均保留为历史记录，与本块不一致者由本块取代。
- 当前对象模块：`01;02;09`。
- 代表分类每个模块保留一个落点，不表示穷尽全文全部细类。

| 模块 | 二级 | 三级 | 本轮结论 |
|---|---|---|---|
| 01 | 01.01 数学 | 01.01.06 微分方程 | 已落地 |
| 02 | 02.02 物理学 | 02.02.05 热学与统计物理学 | 已落地 |
| 09 | 09.04 化学工程与过程工程 | 09.04.04 分离工程 | 已落地 |

- 模块02：实际电热耦合热传导和Joule闭合关系。
  - 证据：PDF 第 [15, 16] 页；原文：while its boundary is held at a prescribed thermal level.

- 模块09：逆流喷淋塔气液吸收闭合关系。
  - 证据：PDF 第 [15, 16, 17] 页；原文：Acid-bearing gas rises through falling alkaline droplets.

- 完整裁决：`Coverage_Check/classification_recheck_2026-11-01/`。

## 既有笔记与历史审计记录

**论文信息**

- ID：ASD-1082
- 标题：Beyond Equation Search: Conjecture-Guided Discovery with SCOPE and ClosureBench
- 作者：Hu, Yuxiao; Li, Qian; Wang, Ding; Chen, Siheng; Zhang, Linfeng; Yan, Jinyue; Chen, Yuntian
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2610.18938
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1082.txt
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Yuxiao_2026_Beyond_Equation_Search_Conjecture_Guided_Discovery_with_SCOPE_and_ASD1082.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 科学对象 | 已知PDE系统中的未知闭合关系。 | TXT line 532；核验TXT行号 532 | Most symbolic regression methods optimize candidate equations, but improving an equation’s fit does not establish whether its underlying scientific conjecture should be retained, revised, or rejected. | 高（一手正文；非独立复现） |
| 猜想形成 | Agent形成自然语言解释、变量关系和可检验预测。 | TXT line 572；核验TXT行号 572 | After initial data analysis and literature review, each scientist formulates a structured conjecture containing a natural-language explanation, variable relationships, testable predictions, and candidate equation space. | 高（一手正文；非独立复现） |
| 方法 | 多条独立猜想轨迹并行探索。 | TXT lines 1175-1180；核验TXT行号 1175 | Evaluating scientific discovery requires assessing not only the derived equations, but also the discovery process: how evidence is acquired and whether it supports the agent’s conclusions. We introduce ClosureBench, an interactive benchmark containing 60 closure-discovery tasks across five scientific domains. Each task embeds an unknown algebraic relation in a known PDE system. An OpenFOAM interface supports experimental evidence acquisition, while evaluation measures equation accuracy, identified scientific properties, evidential support, and improvement through interactive research. | 高（一手正文；非独立复现） |
| 基准 | ClosureBench含60任务和五个科学领域。 | TXT line 1405；核验TXT行号 1405 | As shown in Table 2, SCOPE generally outperforms the fixed-data and interactive baselines in final-equation accuracy with each of the three backbones. | 高（一手正文；非独立复现） |
| 贡献 | 基准用OpenFOAM实验评估证据忠实度、机制洞察和实验有效性。 | TXT line 2048；核验TXT行号 2048 | However, ClosureBench currently focuses on local algebraic closures in simulated PDE systems. | 高（一手正文；非独立复现） |
| 工程对象：反应与传质 | 加热通道中的反应源项是待发现关系，展示工程流动与反应过程。 | TXT line 3121；核验TXT行号 3121 | A dilute reactant flows through a two-dimensional channel whose upper wall is heated while the lower wall remains at 300​K300\,\mathrm{K}. | 高（一手正文；非独立复现） |
| 工程对象：电热过程 | 异质导电薄片中的焦耳热源是待发现闭合关系。 | TXT line 3212；核验TXT行号 3212 | A voltage drives current through a heterogeneous two-dimensional conducting sheet while its boundary is held at a prescribed thermal level. | 高（一手正文；非独立复现） |
| 工程对象：化工吸收 | 喷淋塔中气液吸收速率是待发现对象。 | TXT line 3312；核验TXT行号 3312 | Acid-bearing gas rises through falling alkaline droplets. The target Sabs | 高（一手正文；非独立复现） |
| 工程对象：聚合物加工 | 聚合物熔体流动诱导结晶率是待发现对象。 | TXT line 3412；核验TXT行号 3412 | A polymer melt flows through a cooled channel. A frozen velocity field supplies the local shear rate while crystallinity | 高（一手正文；非独立复现） |
| 工程对象：多孔介质 | 基准还包含双重孔隙介质中的流体交换闭合关系。 | TXT line 3071；核验TXT行号 3071 | Mobile–immobile dual-porosity exchange | 高（一手正文；非独立复现） |

## 0. 摘要翻译

SCOPE让多个科学家Agent各自沿结构化猜想开展研究，不只优化候选公式，还把数据分析、文献、实验问题和证据修订连接起来。ClosureBench提供60个跨五领域闭合发现任务，Agent可在OpenFOAM中控制实验条件以获取数据；除方程精度外，还评估证据忠实度、机制洞察和实验有效性。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。发现PDE系统中的科学闭合关系并检验相关猜想。
  - 原文位置：TXT line 572；核验TXT行号 572；引文：Each scientist agent pursues a complete research trajectory rather than merely optimizing candidate equations.
- 多步行动过程：yes。科学家Agent建立猜想、搜索公式、执行实验并据证据修订。
  - 原文位置：TXT line 572；核验TXT行号 572；引文：After initial data analysis and literature review, each scientist formulates a structured conjecture containing a natural-language explanation, variable relationships, testable predictions, and candidate equation space.
- 至少一种Agent能力：yes。Agent围绕局部反应、焦耳热、吸收、结晶和多孔介质交换等具体闭合对象控制实验条件并获取发现证据。
  - 原文位置：TXT line 532；核验TXT行号 532；引文：Each task embeds an unknown algebraic relation in a known PDE system, where agents control experimental conditions in OpenFOAM to acquire new data for equation discovery.
- 明确科研流程角色：yes。承担方程建模、实验问题形成和证据驱动修订。
  - 原文位置：TXT line 572；核验TXT行号 572；引文：ce SCOPE (Scientific Conjecture-Oriented Parallel Exploration), a framework for parallel scientific agent investigation guided by structured conjectures.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：01;09
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：01（仅归档，不覆盖其他模块）
- 模块内分类路径：01.01.06 微分方程；09.01 工程基础
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

主要对象是嵌入已知PDE的局部代数闭合关系；01.01.06对应方程对象，09.01对应加热通道、焦耳热、喷淋吸收、聚合物结晶及多孔介质等工程科学任务，归类依据是任务对象而非OpenFOAM工具。

### 2.3 容易混淆的边界

主要对象是嵌入已知PDE的局部代数闭合关系；01.01.06对应方程对象，09.01对应加热通道、焦耳热、喷淋吸收、聚合物结晶及多孔介质等工程科学任务，归类依据是任务对象而非OpenFOAM工具。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

multi_agent_scientists

### 3.2 科研流程角色

conjecture_formation；equation_discovery；experiment_design

多个Scientist Agent独立提出猜想并搜索方程，周期性交换证据；OpenFOAM执行交互式实验，研究轨迹输出科学报告。

### 3.3 自主能力

Agent围绕局部反应、焦耳热、吸收、结晶和多孔介质交换等具体闭合对象控制实验条件并获取发现证据。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

科学贡献是通过实验数据发现PDE闭合关系；系统贡献是猜想驱动并行Agent框架及交互式基准。

### 4.2 系统流程与组件

Agent先分析数据和文献，构造含解释、变量关系、预测及候选方程空间的猜想；符号回归寻找符合猜想的表达式，随后Agent提出实验问题并控制OpenFOAM条件取数，依据证据评估并修订猜想，形成报告。 这一工作流的实施细节、输入输出和验证范围均按原文所报告内容理解，不将展示案例外推为普遍能力。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

ClosureBench含60项、五领域任务，嵌入已知PDE中的隐藏闭合关系；与多类基线比较，按方程准确性、证据忠实度、机制洞察和实验有效性评价。

### 5.2 基线、指标与结果

作者报告SCOPE在ClosureBench上提升方程准确性；具体结论须结合各基准子任务和基线读取。

### 5.3 科学贡献与证据强度

科学贡献是通过实验数据发现PDE闭合关系；系统贡献是猜想驱动并行Agent框架及交互式基准。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

超越单纯符号回归拟合，将科学猜想、主动实验和证据修订纳入发现流程。

## 7. 局限性与风险

- author_stated：论文设有结论与局限章节，基准范围为五领域的闭合发现任务。
- reviewer_inference：PDE基准表现不能直接代表所有科学发现任务。

## 8. 对综述写作的价值

可支持综述从方程搜索转向猜想形成、主动实验与证据质量的论点。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

SCOPE和ClosureBench将猜想驱动Agent研究与OpenFOAM实验验证结合。

### 9.2 速记版 pipeline

Agent先分析数据和文献，构造含解释、变量关系、预测及候选方程空间的猜想；符号回归寻找符合猜想的表达式，随后Agent提出实验问题并控制OpenFOAM条件取数，依据证据评估并修订猜想，形成报告。 这一工作流的实施细节、输入输出和验证范围均按原文所报告内容理解，不将展示案例外推为普遍能力。

### 9.3 标注字段汇总

```text
paper_id=ASD-1082
inclusion_status=to_read
scientific_object_modules=01;09
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=01
module_taxonomy_codes=01.01.06;09.01
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。
