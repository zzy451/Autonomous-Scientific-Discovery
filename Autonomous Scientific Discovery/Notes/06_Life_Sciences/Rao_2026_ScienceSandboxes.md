# Science sandboxes measure the scientific capability of AI agents

**论文信息**

- ID：ASD-0875
- 标题：Science sandboxes measure the scientific capability of AI agents
- 作者：Rao, Arya S.; Castro, Rodrigo I.; Gosai, Sager J.; Hsu, Kenneth B.; Ektefaie, Yasha; Singh, Shantanu; Bhatia, Sangeeta N.; Reilly, Steven K.; Tewhey, Ryan; Lander, Eric S.; Sabeti, Pardis C.
- 年份：2026
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2608.30165
- 一手阅读来源：https://arxiv.org/abs/2608.30165
- 来源层级：全文
- 阅读版本：对应缓存来源版本，参见Evidence Log
- 阅读版本题名：Science sandboxes measure the scientific capability of AI agents
- 原始全文缓存：C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/.tmp_asd_pdfs/2608.30165.html
- PDF / 本地文件路径：未归档PDF
- 当前状态：included
- 阅读日期：2026-10-22
- 笔记作者：Codex（读者证据包经主控审核整合）

## Evidence Log

| 判断项 | 结论 / 原文概括 | 证据位置 | 可信度 |
|---|---|---|---|
| 实验Agent进入oracle闭环。 | 每轮提出动作、接收反馈、记录解释并选下一轮实验。 | 全文§1及Figure 1 | high |
| MPRAbox选择调控DNA序列库。 | 目标是挑选信息量高的序列库以训练下游预测器。 | 全文MPRAbox方法 | high |
| CodonBox测试规则发现。 | 要求Agent从编码序列实验反馈归纳遗传规则。 | 全文CodonBox方法 | high |
| Agent在轮次间记录技能。 | 实验前查阅、实验后更新可复用skill。 | 全文Agent protocol | high |
| 指标优化与规则理解被分别评价。 | Agent可取得高分但不一定推断真实系统规律。 | 全文结果与讨论 | high |
| 对象覆盖生命科学。 | 分别含调控遗传序列及蛋白fitness任务。 | 全文两个sandbox结果节 | medium |

## 0. 摘要翻译

论文建立封闭oracle科学实验sandbox，让Agent重复提出实验、读取反馈、解释结果及修订假设。MPRAbox测试调控DNA序列库选择，CodonBox测试从编码序列与适应度反馈中发现规则；结果区分单纯提升指标与理解系统规律。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 当前判断：included；读者建议：included。
全文描述闭环实验Agent：每轮提出实验、接收oracle反馈、记录解释、修订假设并选择下一批实验；具有规划、工具交互与反馈迭代。

### 1.2 排除风险检查

MPRAbox调控DNA序列任务支持06.01.06遗传学；CodonBox涉及编码序列和蛋白fitness，支持06.03.06蛋白质科学。对象级任务排除01.04；研究对象不是科学共同体，非11.07。 主控模块内落点采用06.01.13计算生物学，以承载调控基因组与蛋白适应度两个实验对象簇；对象细节保留在证据日志。
完整闭环不是纳入门槛；科研目标、多步行动、至少一项Agent能力及明确科研角色须同时成立。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：06
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：06（仅归档，不替代多模块事实）
- 模块内分类路径：06.01.13
- 分类深度：03/04使用二级；06/07使用固定三级；其余沿用现有树。
- 分类状态：原文证据复核

### 2.2 对象优先判定

在调控序列与蛋白fitness两类sandbox比较Agent选序列、指标表现、规则归纳及规则变化时的泛化。发现Agent可提升分数但未理解规则，陌生规则下推理下降。

### 2.3 容易混淆的边界

MPRAbox调控DNA序列任务支持06.01.06遗传学；CodonBox涉及编码序列和蛋白fitness，支持06.03.06蛋白质科学。对象级任务排除01.04；研究对象不是科学共同体，非11.07。 主控模块内落点采用06.01.13计算生物学，以承载调控基因组与蛋白适应度两个实验对象簇；对象细节保留在证据日志。

## 3. Agent 系统与科研流程角色

全文描述闭环实验Agent：每轮提出实验、接收oracle反馈、记录解释、修订假设并选择下一批实验；具有规划、工具交互与反馈迭代。

科研流程与自主能力以本文实际行动和工具调用为依据：

建立sealed-oracle sandbox。MPRAbox要求选择高信息量调控DNA序列库；CodonBox测试从序列与反馈进行de novo rule discovery。Agent跨轮保留解释、假设和可复用技能。

## 4. 方法设计

### 4.1 方法动机与设计

提出可控重复实验框架，区分找到高分解与学会系统规则并据此设计实验。

### 4.2 系统流程与组件

建立sealed-oracle sandbox。MPRAbox要求选择高信息量调控DNA序列库；CodonBox测试从序列与反馈进行de novo rule discovery。Agent跨轮保留解释、假设和可复用技能。

## 5. 实验与验证

### 5.1 验证方式、对象及任务

在调控序列与蛋白fitness两类sandbox比较Agent选序列、指标表现、规则归纳及规则变化时的泛化。发现Agent可提升分数但未理解规则，陌生规则下推理下降。

### 5.2 基线、指标与结果

在调控序列与蛋白fitness两类sandbox比较Agent选序列、指标表现、规则归纳及规则变化时的泛化。发现Agent可提升分数但未理解规则，陌生规则下推理下降。

### 5.3 科学贡献与证据强度

提出可控重复实验框架，区分找到高分解与学会系统规则并据此设计实验。

证据层级：原始全文支持；作者报告结果不等于独立复现。

## 6. 与已有工作的关系

承接AI experimentalist/self-driving science基准，强化反馈循环和规则发现能力测量。

## 7. 局限性与风险

封闭oracle与真实湿实验有外部效度差距；结果依赖所设规则；Agent可复用skills，因此技能记忆可能影响实验表现。

## 8. 对综述写作的价值

支持Agent自主能力、反馈实验和生物对象分类的多模块讨论。

推荐引用强度：普通引用，可在核对原文后用于相应领域案例。

## 9. 总结

### 9.1 一句话概括

用生物实验沙盒检验Agent研究能力

### 9.2 速记版 pipeline

建立sealed-oracle sandbox。MPRAbox要求选择高信息量调控DNA序列库；CodonBox测试从序列与反馈进行de novo rule discovery。Agent跨轮保留解释、假设和可复用技能。

### 9.3 标注字段汇总

```text
paper_id=ASD-0875
inclusion_status=included
scientific_object_modules=06
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=06
module_taxonomy_codes=06.01.13
source_level=fulltext
fulltext_followup_required=false
```

### 全文后续要求

本轮已读原始全文并完成对象分类；无需为纳入/分类另做全文补读。具体引用时仍需回查相应原文位置。


## 2026-10-29 PDF补齐归档

- 本地PDF：`Reference_PDF/06_Life_Sciences/ASD-0875_Science_sandboxes_measure_the_scientific_capability_of_AI_agents.pdf`，共72页；已核验标题、页面解析和逐页渲染。
- 下载来源：https://arxiv.org/pdf/2608.30165v1
- 版本：official arXiv preprint PDF; version as downloaded。
- 本轮为来源文件归档，不自动改变既有科学分类或将未决PR意见标记为已结案。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O2 既定基准 | 在封闭oracle sandbox中执行预定义调控序列与蛋白任务 | “调控序列与蛋白fitness两类sandbox” · L62 |
| 验证强度 | V1 基准/内部评测 | sandbox仿真环境，agent提升分数但未理解真实规则 | “发现Agent可提升分数但未理解规则” · L62 |
| 系统自主性 | L2 闭环执行者 | agent重复提出实验、读取反馈、修订假设 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
