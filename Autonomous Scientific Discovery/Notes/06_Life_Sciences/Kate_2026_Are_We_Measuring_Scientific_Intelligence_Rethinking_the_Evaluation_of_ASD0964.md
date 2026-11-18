# Are We Measuring Scientific Intelligence? Rethinking the Evaluation of AI Scientists

**论文信息**

- ID：ASD-0964
- 标题：Are We Measuring Scientific Intelligence? Rethinking the Evaluation of AI Scientists
- 作者：Zhang, Kate; Li, Yuante
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2610.04915
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0964.txt
- PDF / 本地文件路径：Reference_PDF/06_Life_Sciences/Kate_2026_Are_We_Measuring_Scientific_Intelligence_Rethinking_the_Evaluation_of_ASD0964.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 纳入判断：论文直接研究科研Agent或其评测。 | 论文质疑以固定答案正确率衡量AI Scientist是否真正使用数据。作者提出证据依赖评测：保持、撤除或反转关键数据证据，检查答案响应，并同步检查评分器是否奖励这种响应。 | TXT line 297；核验TXT行号 297 | AI agents can now carry out data-driven scientific analyses end to end, and benchmarks assess them by giving an agent a question and a dataset and scoring its final answer against a fixed key. These benchmarks assume that a correct answer was derived from the supplied data, a property we call evidence grounding. | 高（一手正文；非独立复现） |
| 对象证据：正文界定科学问题及研究对象。 | 评测任务直接分析单细胞生物数据及合成统计遗传问题。按当前树归入06.01.12生物信息学，并以06.03.04单细胞生物学标注主要真实数据对象；评测方法是副属性。 | TXT line 756；核验TXT行号 756 | We use BAISBench’s scientific-discovery split (BAIS-SD) [8] and GeneBench-Pro [9]. Of 193 BAIS-SD questions, 22 can be decided from the supplied single-cell data by a reference statistic. | 高（一手正文；非独立复现） |
| 方法证据：全文描述Agent操作或评测流程。 | 使用BAISBench的18个单细胞问题及GeneBench-Pro四个合成问题；配置证据保持、撤除、反转版本，在相同提示下运行，并比较无数据条件及多种评分。通过配对结果比较回答是否跟随数据。 | TXT line 763；核验TXT行号 297 | We evaluate three agent scaffolds and five models on 18 single-cell questions from BAISBench and four synthetic problems from GeneBench-Pro. | 高（一手正文；非独立复现） |
| 验证证据：实验报告任务、数据与验证设计。 | 贡献是逐题构造经核查反事实并提出证据依赖准确率，分别审计Agent是否跟随证据及评分器是否给出相应奖励。 | TXT line 1024；核验TXT行号 297 | On the single-cell questions, the Claude agents are 95% accurate and answer 83% correctly without any data, but their evidence-grounded accuracy is only 41%. | 高（一手正文；非独立复现） |
| 结果贡献：正文报告可核查结果和贡献。 | 科学对象是AI Scientist评测效度，生物数据分析仅为实验任务，故归入06而非生物发现模块。 | TXT line 297；核验TXT行号 297 | The benchmark score and LLM judges can also reward answers that ignore the changed evidence. Measuring scientific intelligence rather than recall therefore requires checking whether answers follow the evidence and whether scores reward them for it. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

论文质疑以固定答案正确率衡量AI Scientist是否真正使用数据。作者提出证据依赖评测：保持、撤除或反转关键数据证据，检查答案响应，并同步检查评分器是否奖励这种响应。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。正文提出科学研究或科学评测目标。
  - 原文位置：TXT line 297；核验TXT行号 297；引文：AI agents can now carry out data-driven scientific analyses end to end, and benchmarks assess them by giving an agent a question and a dataset and scoring its final answer against a fixed key. These benchmarks assume that a correct answer was derived from the supplied data, a property we call evidence grounding.
- 多步行动过程：yes。正文描述多阶段行动及反馈流程。
  - 原文位置：TXT line 297；核验TXT行号 297；引文：For each question, we build versions of its data files in which the evidence for the answer is left intact, withdrawn or reversed, check each edit with a pre-registered reference statistic, and run the same agent on every version.
- 至少一种Agent能力：yes。正文显示Agent使用工具、状态或证据进行决策。
  - 原文位置：TXT line 763；核验TXT行号 297；引文：We evaluate three agent scaffolds and five models on 18 single-cell questions from BAISBench and four synthetic problems from GeneBench-Pro.
- 明确科研流程角色：yes。系统承担科研执行、理论发现或科研评价角色。
  - 原文位置：TXT line 1024；核验TXT行号 297；引文：On the single-cell questions, the Claude agents are 95% accurate and answer 83% correctly without any data, but their evidence-grounded accuracy is only 41%.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：06
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：06（仅归档，不覆盖其他模块）
- 模块内分类路径：06.01.12 生物信息学；06.03.04 单细胞生物学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

本文研究AI Scientist的证据依赖，但评测对象是单细胞数据分析与统计遗传任务；按照按具体benchmark对象归档的规则列06.01.12及06.03.04，不归通用评测存放区。

### 2.3 容易混淆的边界

本文研究AI Scientist的证据依赖，但评测对象是单细胞数据分析与统计遗传任务；按照按具体benchmark对象归档的规则列06.01.12及06.03.04，不归通用评测存放区。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

科研Agent评测系统；语言模型Agent

### 3.2 科研流程角色

数据分析；证据跟踪；基准评估

同一Agent运行每项任务的配对反事实版本，先用预注册参考统计核查数据编辑，再依据输出评估Agent和评分器。

### 3.3 自主能力

正文显示Agent使用工具、状态或证据进行决策。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

相较单次正确率、无数据基线或过程评审，本文用配对干预验证答案与数据关系，并同步评估基准效度。

### 4.2 系统流程与组件

使用BAISBench的18个单细胞问题及GeneBench-Pro四个合成问题；配置证据保持、撤除、反转版本，在相同提示下运行，并比较无数据条件及多种评分。通过配对结果比较回答是否跟随数据。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

Claude Agent单细胞准确率95%，无数据时仍有83%，证据依赖准确率仅41%。隐藏基因名后，10个基因任务追随反转证据的比例从58%升至93%；作者还发现基准分及LLM评审可能奖励忽略变化。

### 5.2 基线、指标与结果

贡献是逐题构造经核查反事实并提出证据依赖准确率，分别审计Agent是否跟随证据及评分器是否给出相应奖励。

### 5.3 科学贡献与证据强度

相较单次正确率、无数据基线或过程评审，本文用配对干预验证答案与数据关系，并同步评估基准效度。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

研究限于18个单细胞和四个合成问题，反事实需人工构造核查；匿名化结果支持先验竞争解释，但不证明其为唯一原因。

## 7. 局限性与风险

科学对象是AI Scientist评测效度，生物数据分析仅为实验任务，故归入06而非生物发现模块。

## 8. 对综述写作的价值

论文用保持、撤除、反转证据的配对任务检验Agent是否真正依赖数据，发现常规准确率及评分可能掩盖差异。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

论文用保持、撤除、反转证据的配对任务检验Agent是否真正依赖数据，发现常规准确率及评分可能掩盖差异。

### 9.2 速记版 pipeline

使用BAISBench的18个单细胞问题及GeneBench-Pro四个合成问题；配置证据保持、撤除、反转版本，在相同提示下运行，并比较无数据条件及多种评分。通过配对结果比较回答是否跟随数据。

### 9.3 标注字段汇总

```text
paper_id=ASD-0964
inclusion_status=to_read
scientific_object_modules=06
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=06
module_taxonomy_codes=06.01.12;06.03.04
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O2 既定基准 | BAISBench和GeneBench-Pro为预定义基准任务 | “使用BAISBench的18个单细胞问题及GeneBench-Pro四个合成问题” · L95 |
| 验证强度 | V1 基准/内部评测 | 证据依赖准确率和LLM评审评估，无独立复现 | “配置证据保持、撤除、反转版本，在相同提示下运行” · L95 |
| 系统自主性 | L1 任务助手 | Agent执行数据分析任务，但评测框架控制条件 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
