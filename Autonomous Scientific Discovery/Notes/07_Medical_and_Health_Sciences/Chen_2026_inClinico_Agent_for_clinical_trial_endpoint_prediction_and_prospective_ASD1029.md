# inClinico Agent for clinical trial endpoint prediction and prospective evaluation

**论文信息**

- ID：ASD-1029
- 标题：inClinico Agent for clinical trial endpoint prediction and prospective evaluation
- 作者：Jianjiu Chen; Chengchen Duan; Wenhao Gou; Jingwan Wang; Zetian Zheng; Howell Leung; Vladimir Naumov; Denis Sidorenko; Alex Aliper; Feng Ren; Frank W. Pun; Alex Zhavoronkov
- 年份：2026
- 来源 / venue：medRxiv preprint
- DOI / arXiv / URL：https://doi.org/10.64898/2026.10.13.26365373
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1029.txt
- PDF / 本地文件路径：Reference_PDF/07_Medical_and_Health_Sciences/Chen_2026_inClinico_Agent_for_clinical_trial_endpoint_prediction_and_prospective_ASD1029.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 科学目标 | 科学目标是前瞻预测临床试验能否达到主要终点；版权页不是目标证据。 | Full text, local TXT line 16；核验TXT行号 16 | prospectively forecasting whether an individual trial will achieve its primary endpoint remains challenging | 高（一手正文；非独立复现） |
| Agent架构 | 路由器选择技能和工具，Agent规划、执行、批判并报告，批判结果可返回规划阶段。 | Full text, local TXT line 77；核验TXT行号 77 | a routing layer selects skills and tools; agents plan, execute, critique and report; and the critique step can return a task to planning | 高（一手正文；非独立复现） |
| 方法与结果 | 模型用注册时特征预测试验终点；时间外测试集疗效模型AUROC为0.828。 | Full text, local TXT line 24；核验TXT行号 24 | the efficacy model achieved an area under the receiver operating characteristic curve (AUROC) of 0.828 | 高（一手正文；非独立复现） |
| 前瞻验证 | ClinBench纳入3311项进行中试验，作为待随试验完成追踪的前瞻评估集。 | Full text, local TXT line 29；核验TXT行号 29 | 3,311 ongoing trials evaluated by inClinico Agent and five frontier LLMs | 高（一手正文；非独立复现） |
| 限制与边界 | 作者承认训练集交叉拟合未按时间分块，可能残留有限的前视偏差。 | Full text, local TXT line 180；核验TXT行号 180 | cross-fitting is not time-blocked | 高（一手正文；非独立复现） |

## 0. 摘要翻译

本文提出inClinico临床试验终点预测系统，并建立ClinBench评估注册时点预测能力。模型按I—IV期及疗效/安全性终点分别预测，使用试验登记时可获得的特征以降低结果泄漏；ClinBench包含3,311项进行中试验，并与五种前沿LLM比较，另报告17项后来读出的前瞻性试验。该设计提供时间外评测基础，但真实前瞻性读出数较少，预测不能替代临床判断。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。科研目标是前瞻预测临床试验是否达到其主要终点；版权许可文字不属于科学目标。
  - 原文位置：Full text, local TXT line 16；核验TXT行号 16；引文：prospectively forecasting whether an individual trial will achieve its primary endpoint remains challenging
- 多步行动过程：yes。系统将请求路由到技能和工具，再经过规划、执行、批判及报告阶段。
  - 原文位置：Full text, local TXT line 77；核验TXT行号 77；引文：a routing layer selects skills and tools; agents plan, execute, critique and report
- 至少一种Agent能力：yes。Agent选择技能和工具并根据批判结果返回规划；终点预测仍由机器学习评分组件完成。
  - 原文位置：Full text, local TXT line 77；核验TXT行号 77；引文：a routing layer selects skills and tools; agents plan, execute, critique and report; and the critique step can return a task to planning
- 明确科研流程角色：yes。Core Skills明确面向临床试验评估和准备，构成临床研发研究支持角色。
  - 原文位置：Full text, local TXT line 99；核验TXT行号 99；引文：Core Skills are skill sets for clinical trial analysis, grouped into Trial Evaluation and Trial Preparation

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：07
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：07（仅归档，不覆盖其他模块）
- 模块内分类路径：07.04.01 药物发现
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

归入06.01临床试验与药物研发研究；Agent预测的是开发终点成功概率，不是疗效实验或监管决策的替代证据。

### 2.3 容易混淆的边界

归入06.01临床试验与药物研发研究；Agent预测的是开发终点成功概率，不是疗效实验或监管决策的替代证据。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM Agent；Tool-using Agent

### 3.2 科研流程角色

tool_use_and_code_execution；data_analysis；evidence_assessment_and_validation

inClinico Agent使用检索、评分和图表工具预测临床试验主要终点是否成功；论文另构建ClinBench，把前瞻性试验登记信息与真实读出连接以检验时间外预测。

### 3.3 自主能力

Agent选择技能和工具并根据批判结果返回规划；终点预测仍由机器学习评分组件完成。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

贡献是把临床试验终点预测改造成Agent可调用工具的流程，并提供以注册时信息构建的前瞻性评估基准。

### 4.2 系统流程与组件

模型针对I–IV期试验并区分疗效与安全/毒性主要终点，使用登记时可得特征避免结果泄漏；ClinBench含3,311项正在进行的试验，另分析17项后续读出的前瞻性试验，并与五种前沿LLM比较。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

评价包括历史数据模型测试、登记时点可用信息限制下的ClinBench前瞻性基准及17项实际读出的试验；时间切分和信息泄漏控制是核心设计，但交叉拟合并非时间块切分。

### 5.2 基线、指标与结果

作者报告inClinico Agent在试验终点预测任务中表现优于比较模型，并用ClinBench提供无结果泄漏的评测基础；17项读出规模较小，不能据此保证单项临床开发决策成功。

### 5.3 科学贡献与证据强度

贡献是把临床试验终点预测改造成Agent可调用工具的流程，并提供以注册时信息构建的前瞻性评估基准。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

相较使用已揭晓结果特征的回顾性预测，本文强调注册时点预测和前瞻性读出；ClinBench还将专用Agent与通用前沿LLM进行比较。

## 7. 局限性与风险

前瞻性真实读出仅17项，预测受适应症、试验设计和资料质量影响；交叉拟合未按时间块切分可能保留信息相关性，预测概率不能代替临床判断。

## 8. 对综述写作的价值

可用于评估临床试验成功预测Agent的前瞻性基准、时间信息控制和小样本读出限制。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

inClinico使用试验启动时可得信息预测临床试验主要终点，并以3,311项进行中试验建立ClinBench，另跟踪17项实际读出。其前瞻设计降低了结果泄漏风险，但样本规模和时间切分方式仍限制结论。

### 9.2 速记版 pipeline

模型针对I–IV期试验并区分疗效与安全/毒性主要终点，使用登记时可得特征避免结果泄漏；ClinBench含3,311项正在进行的试验，另分析17项后续读出的前瞻性试验，并与五种前沿LLM比较。

### 9.3 标注字段汇总

```text
paper_id=ASD-1029
inclusion_status=to_read
scientific_object_modules=07
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=07
module_taxonomy_codes=07.04.01
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O3 新实例 | 预测已登记试验的终点，答案将由试验读出验证 | “prospectively forecasting whether an individual trial will achieve its primary endpoint” · L21 |
| 验证强度 | V2 计算/仿真/回顾性 | 历史数据模型测试和前瞻基准，真实读出仅17项规模小 | “the efficacy model achieved an area under the receiver operating characteristic curve (AUROC) of 0.828” · L23 |
| 系统自主性 | L1 任务助手 | Agent执行预测任务，人决定研究流程 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
