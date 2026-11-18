# Long-Horizon Autonomous Architecture Research with a Language-Model Agent: A Behavioural Case Study

**论文信息**

- ID：ASD-0959
- 标题：Long-Horizon Autonomous Architecture Research with a Language-Model Agent: A Behavioural Case Study
- 作者：Safdar, Aon; Saadeldin, Mohamed
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2608.01995
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0959.txt
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Aon_2026_Long_Horizon_Autonomous_Architecture_Research_with_a_Language_Model_ASD0959.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 纳入核查：文章直接研究自动研究Agent或其基准。 | 纳入核查：文章直接研究自动研究Agent或其基准。 | TXT line 648；核验TXT行号 648 | Single agent, single hypothesis. At any time the agent is executing exactly one experiment. We intentionally do not parallelise: parallel execution dilutes the causal signal from each change and makes failure diagnosis harder. The cost of this discipline is wall-clock; the benefit is an unambiguous per-hypothesis outcome that the agent can reason about. | 高（一手正文；非独立复现） |
| 研究对象由正文任务或数据明确界定。 | 研究对象由正文任务或数据明确界定。 | TXT line 655；核验TXT行号 655 | Commit-or-discard as the evaluation rule. After each experiment, the agent compares the result against the current champion. If improved, the change is preserved in source control and becomes the new baseline; otherwise the experimental change is reverted and the next hypothesis begins. We will return to this choice in Section 6.5: it is operationally convenient and it structurally imposes greedy hill-climbing, which has observable downstream effects on the agent’s hypothesis distribution. | 高（一手正文；非独立复现） |
| 方法证据包括任务输入与迭代操作。 | 方法证据包括任务输入与迭代操作。 | TXT line 669；核验TXT行号 669 | End-of-turn after submission. The agent is instructed to end its turn immediately after submitting a training job, rather than to poll the scheduler itself. Control is returned when the job leaves the queue. This discipline keeps the agent’s token budget focused on scientific reasoning and avoids one class of autonomy failure; the concrete mechanism by which control is returned is an implementation detail described in Appendix A. | 高（一手正文；非独立复现） |
| 验证设计含有对照、多次执行或独立评分。 | 验证设计含有对照、多次执行或独立评分。 | TXT line 845；核验TXT行号 845 | Literature access. From the second phase onward the agent can query preprint servers, code repositories with associated documentation, and a model-and-dataset hub, via a uniform tool protocol. Prior to this, only internal reasoning is available. | 高（一手正文；非独立复现） |
| 正文报告了可核对结果或系统贡献。 | 正文报告了可核对结果或系统贡献。 | TXT line 926；核验TXT行号 926 | We enumerate every human intervention across the programme. Interventions are bounded and strategic: they declare phase transitions, repair reliability failures, or expand the tool surface. They never make tactical decisions (hypothesis selection, hyperparameter choice, code writing, result interpretation), which remain the agent’s responsibility. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

论文通过单个持久语言模型Agent在单个视觉架构上进行长期迭代的案例研究，观察通过人类给定研究简报、工具访问、实验记录和独立运行进行学术修改。作者分析多阶段训练轨迹和质量变化，但指出是单次运行、单一Agent和单一架构。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。正文设定了明确的科学目标或评测问题。
  - 原文位置：TXT line 648；核验TXT行号 648；引文：Single agent, single hypothesis. At any time the agent is executing exactly one experiment. We intentionally do not parallelise: parallel execution dilutes the causal signal from each change and makes failure diagnosis harder. The cost of this discipline is wall-clock; the benefit is an unambiguous per-hypothesis outcome that the agent can reason about.
- 多步行动过程：yes。方法需要反复提案、执行和判读结果。
  - 原文位置：TXT line 655；核验TXT行号 655；引文：Commit-or-discard as the evaluation rule. After each experiment, the agent compares the result against the current champion. If improved, the change is preserved in source control and becomes the new baseline; otherwise the experimental change is reverted and the next hypothesis begins. We will return to this choice in Section 6.5: it is operationally convenient and it structurally imposes greedy hill-climbing, which has observable downstream effects on the agent’s hypothesis distribution.
- 至少一种Agent能力：yes。系统具有调用工具并根据反馈继续的Agent能力。
  - 原文位置：TXT line 662；核验TXT行号 662；引文：Structured persistent memory. Every hypothesis is recorded in a single research log in a fixed template that captures motivation, literature grounding, the exact change applied, the parameter and compute budget, and the result. The log is both the agent’s primary cross-session memory and our primary unit of observation. We require the agent to read the log at the start of each session and to append to it before submitting each experiment.
- 明确科研流程角色：yes。系统在文中承担科研Agent的实验、研发或评价角色。
  - 原文位置：TXT line 831；核验TXT行号 831；引文：Source and experiment management. A single version-control repository with a branching discipline: one branch per phase, one commit per accepted hypothesis. Rejected hypotheses are reverted from the working tree but preserved in the log.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：01
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：01（仅归档，不覆盖其他模块）
- 模块内分类路径：01.02 计算机科学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

使用视觉模型研究作为任务对象，但论文主要贡献是观察语言Agent的长时研究行为，无对专业视觉科学提出独立领域发现，归入01.02。

### 2.3 容易混淆的边界

使用视觉模型研究作为任务对象，但论文主要贡献是观察语言Agent的长时研究行为，无对专业视觉科学提出独立领域发现，归入01.02。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

语言模型Agent

### 3.2 科研流程角色

科研执行；实验评估

Long-Horizon Autonomous Architecture Research with a Language-Model Agent: A Behavioural Case Study?人类给出科学问题、设计约束和训练预算；Agent在仓库和参数配置中提出一次假设，修改模型代码后向集群提交单个训练任务；完成后读取训练曲线和测试分数，对比champion后提交或回退，以日志累积下一步知识。

### 3.3 自主能力

系统具有调用工具并根据反馈继续的Agent能力。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

科学贡献是上文实验任务中可复核的结果与对照；系统贡献是论文提出的Agent架构、迭代流程和评估方法。

### 4.2 系统流程与组件

人类给出科学问题、设计约束和训练预算；Agent在仓库和参数配置中提出一次假设，修改模型代码后向集群提交单个训练任务；完成后读取训练曲线和测试分数，对比champion后提交或回退，以日志累积下一步知识。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

此案例覆盖CIFAR-10、CIFAR-100和ImageNet-1K三阶段的视觉模型训练；按验证准确率记录所有假设，与每阶段champion进行连续比较，分析收益集中度和饱和。

### 5.2 基线、指标与结果

作者报告早期假设导致CIFAR准确率大幅提高，后续进入长时段饱和；ImageNet-1K阶段18个假设仅有2个被接受。

### 5.3 科学贡献与证据强度

科学贡献是上文实验任务中可复核的结果与对照；系统贡献是论文提出的Agent架构、迭代流程和评估方法。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

论文在自动研究Agent及长程轨迹研究的背景下与已有系统和评测基准比较，具体差异体现于上文所述的新监督、证据记忆或任务评价策略。

## 7. 局限性与风险

作者承认的局限以全文limitations段为准；读者风险：任务集和评分器不能代表全部真实研究环境，结果需按作者所设定的任务范围解读。

## 8. 对综述写作的价值

使用视觉模型研究作为任务对象，但论文主要贡献是观察语言Agent的长时研究行为，无对专业视觉科学提出独立领域发现，归入01.02。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

论文通过单个持久语言模型Agent在单个视觉架构上进行长期迭代的案例研究，观察通过人类给定研究简报、工具访问、实验记录和独立运行进行学术修改。作者分析多阶段训练轨迹和质量变化，但指出是单次运行、单一Agent和单一架构。

### 9.2 速记版 pipeline

人类给出科学问题、设计约束和训练预算；Agent在仓库和参数配置中提出一次假设，修改模型代码后向集群提交单个训练任务；完成后读取训练曲线和测试分数，对比champion后提交或回退，以日志累积下一步知识。

### 9.3 标注字段汇总

```text
paper_id=ASD-0959
inclusion_status=to_read
scientific_object_modules=01
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=01
module_taxonomy_codes=01.02
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O2 既定基准 | 在CIFAR和ImageNet视觉基准上进行架构研究 | “此案例覆盖CIFAR-10、CIFAR-100和ImageNet-1K三阶段的视觉模型训练” · L101 |
| 验证强度 | V1 基准/内部评测 | 验证准确率记录和假设接受率统计，无独立复现 | “按验证准确率记录所有假设，与每阶段champion进行连续比较” · L101 |
| 系统自主性 | L2 闭环执行者 | Agent在人设定目标内自主提出和检验架构假设多轮 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
