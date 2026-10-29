# Multi-agent discovery of practical quantum LDPC codes

**论文信息**

- ID：ASD-1066
- 标题：Multi-agent discovery of practical quantum LDPC codes
- 作者：Qian, Dongheng; Li, Tianyi
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2608.08996
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1066.txt
- PDF / 本地文件路径：Reference_PDF/02_Physics_Astronomy_and_Cosmic_Sciences/Dongheng_2026_Multi_agent_discovery_of_practical_quantum_LDPC_codes_ASD1066.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 科研对象 | 量子纠错及LDPC码构造。 | TXT line 30；核验TXT行号 30 | Quantum error correction protects logical information by encoding it redundantly across physical | 高（一手正文；非独立复现） |
| 系统结构 | 三类Agent与固定评价器形成闭环。 | TXT line 115；核验TXT行号 115 | The framework couples three agent roles to a fixed evaluator in a closed discovery loop, as summarized | 高（一手正文；非独立复现） |
| 搜索机制 | 研究者与策展者分配方向、整理证据。 | TXT line 116；核验TXT行号 116 | A researcher council formulates scientific directions, a curator distills accumulated evidence | 高（一手正文；非独立复现） |
| 评估反馈 | 固定评估器对提交候选返回量化结果。 | TXT line 138；核验TXT行号 138 | After each worker submission, the fixed evaluator returns a quantitative outcome. | 高（一手正文；非独立复现） |
| 科学结果 | 报告多个具有已证明距离的码实例。 | TXT line 797；核验TXT行号 797 | In summary, our work makes both practical and methodological contributions. On the practical | 高（一手正文；非独立复现） |

## 0. 摘要翻译

本文构建多Agent搜索框架以发现满足实际长度和权重约束的量子LDPC纠错码。研究者议会提出搜索方向，策展者整理可证伪的设计经验，工作者生成候选，固定评估器返回量化结果，形成闭环。作者报告多个具有竞争力的有限长度码参数及结构不同的候选构造。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。搜索具有实用有限长度参数的量子LDPC纠错码。
  - 原文位置：TXT line 98；核验TXT行号 98；引文：The search yields competitive finite-length parameters in every
- 多步行动过程：yes。研究者、策展者和工作者Agent形成迭代发现闭环。
  - 原文位置：TXT line 115；核验TXT行号 115；引文：The framework couples three agent roles to a fixed evaluator in a closed discovery loop, as summarized
- 至少一种Agent能力：yes。Agent提出候选并利用评价反馈更新搜索。
  - 原文位置：TXT line 75；核验TXT行号 75；引文：long-horizon worker agents evolve executable code-family generators through repeated construction,
- 明确科研流程角色：yes。Agent承担纠错码构造搜索及候选整理。
  - 原文位置：TXT line 116；核验TXT行号 116；引文：A researcher council formulates scientific directions, a curator distills accumulated evidence

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：02
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：02（仅归档，不覆盖其他模块）
- 模块内分类路径：02.02 物理学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

对象是量子纠错码的数学构造，归入物理科学02量子信息，而非一般Agent方法。

### 2.3 容易混淆的边界

对象是量子纠错码的数学构造，归入物理科学02量子信息，而非一般Agent方法。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

multi_agent

### 3.2 科研流程角色

scientific_search；candidate_generation

Researcher Council提出方向，Curator整理经验，Worker探索码构造；固定确定性评估器提供定量评价。

### 3.3 自主能力

Agent提出候选并利用评价反馈更新搜索。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

科学贡献是发现新的实用量子LDPC码构造与参数；系统贡献是三Agent与固定评价器的迭代搜索框架。

### 4.2 系统流程与组件

输入为码率、长度、权重和距离等设计目标；研究者Agent分解方向，Curator将文献/搜索经验转为可证伪关系，Worker提出构造，评估器计算参数并反馈，Agent依据结果更新候选和探索方向。 这一工作流的实施细节、输入输出和验证范围均按原文所报告内容理解，不将展示案例外推为普遍能力。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

以固定评价器计算码参数，并报告距离经严格确立的实例；比较不同构造族和权重限制，含实际有限长度约束。

### 5.2 基线、指标与结果

作者报告[[288,16,18]]、[[288,18,18]]和[[234,28,18]]在指定权重条件下取得最高Q值；另有结构不同的候选。

### 5.3 科学贡献与证据强度

科学贡献是发现新的实用量子LDPC码构造与参数；系统贡献是三Agent与固定评价器的迭代搜索框架。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

与既有bivariate-bicycle和lifted-product码搜索相关，并与同期Agent量子纠错码探索工作架构不同。

## 7. 局限性与风险

- author_stated：研究使用受限构造空间与特定参数化；部分候选距离尚非严格确立。
- reviewer_inference：有限长度指标和模拟评价不等于完整硬件纠错演示。

## 8. 对综述写作的价值

说明多Agent可在确定性科学评价器约束下搜索离散科学/工程设计空间。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

多Agent闭环发现若干具有竞争力的量子LDPC码构造。

### 9.2 速记版 pipeline

输入为码率、长度、权重和距离等设计目标；研究者Agent分解方向，Curator将文献/搜索经验转为可证伪关系，Worker提出构造，评估器计算参数并反馈，Agent依据结果更新候选和探索方向。 这一工作流的实施细节、输入输出和验证范围均按原文所报告内容理解，不将展示案例外推为普遍能力。

### 9.3 标注字段汇总

```text
paper_id=ASD-1066
inclusion_status=to_read
scientific_object_modules=02
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=02
module_taxonomy_codes=02.02
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`02.02.06` 量子力学；二级：`02.02`。
- 原文位置：PDF pp.1。
- 判定：First-hand evidence supports 02.02.06; When evaluated under code-capacity depolarizing noise using a common BP?OSD decoding protocol, the discovered codes also exhibit low logical failure rates.
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
