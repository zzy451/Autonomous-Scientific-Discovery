# Interpretable self-driving sputtering epitaxy reveals human-usable growth rules for β-Ga2O3 films

**论文信息**

- ID：ASD-0999
- 标题：Interpretable self-driving sputtering epitaxy reveals human-usable growth rules for β-Ga2O3 films
- 作者：Yuki K. Wakabayashi; Yui Ogawa; Franz Benedict Romero; Coleman Wagner; Takuma Otsuka; Yoshitaka Taniyasu
- 年份：2026
- 来源 / venue：Nature Communications
- DOI / arXiv / URL：https://www.nature.com/articles/s41467-026-76533-0
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0999.txt
- PDF / 本地文件路径：Reference_PDF/04_Materials_Science/Wakabayashi_2026_Interpretable_self_driving_sputtering_epitaxy_reveals_human_usable_growth_ASD0999.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 纳入与科学目标 | 研究把自驱动溅射外延优化产生的数据转成可解释、可由人执行的β-Ga2O3薄膜生长规则。系统用贝叶斯优化寻找生长条件，以自动光学Urbach能量作为亚带隙无序指标，再用随机森林代理解释参数贡献与温度—氧气交互。人类按提取规则重新优化并获得更低Urbach能量。 | 摘要；TXT第1行；核验TXT行号 1 | Self-driving laboratories are powerful tools for navigating high-dimensional process spaces, yet Bayesian-optimization decision layers optimize black-box objective functions without distilling transferable process understanding. | 高（一手正文；非独立复现） |
| 方法与多步工作流 | 自动化平台围绕溅射参数进行贝叶斯优化，生长薄膜后自动测量光学透射并计算Urbach能量，结果反馈至下一轮参数选择。完成闭环后，随机森林代理分析参数影响并生成逐步可执行规则，由研究者据此重新优化并验证规则的迁移性。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。 | 摘要；TXT第1行；核验TXT行号 1 | Here, we demonstrate a mathematically interpretable self-driving laboratory framework that transforms autonomous optimization data into human-executable growth rules. | 高（一手正文；非独立复现） |
| Agent能力与行动 | Interpretable self-driving sputtering epitaxy reveals human-usable growth rules for β-Ga2O3 films。系统角色与能力：自动化平台围绕溅射参数进行贝叶斯优化，生长薄膜后自动测量光学透射并计算Urbach能量，结果反馈至下一轮参数选择。完成闭环后，随机森林代理分析参数影响并生成逐步可执行规则，由研究者据此重新优化并验证规则的迁移性。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。 | 摘要；TXT第1行；核验TXT行号 1 | To convert closed-loop data into interpretable growth rules, we train a random forest surrogate and reveal that the growth landscape is described by additive contributions from four growth parameters, with a temperature–oxygen interaction. | 高（一手正文；非独立复现） |
| 验证与结果 | 异质外延获得182 meV Urbach能量；优化窗口迁移到基底实现单晶同质外延并由STEM佐证；从代理模型提取规则后，人类执行重新优化得到163 meV。 | 摘要；TXT第1行；核验TXT行号 1 | By combining Bayesian optimization with automated optical evaluation of the Urbach energy as a sub-bandgap disorder metric, the self-driving system identifies heteroepitaxial conditions yielding an Urbach energy of 182 meV, below previously reported values for sputtered β -Ga 2 O 3 films. | 高（一手正文；非独立复现） |
| 贡献及适用对象 | 可支持综述讨论自驱实验从黑箱寻优走向人可用工艺知识提取。 科学贡献与系统贡献按上述证据分别表述。 | 摘要；TXT第1行；核验TXT行号 1 | This establishes an interpretable self-driving workflow that converts autonomous optimization data into validated, human-usable growth rules. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

研究把自驱动溅射外延优化产生的数据转成可解释、可由人执行的β-Ga2O3薄膜生长规则。系统用贝叶斯优化寻找生长条件，以自动光学Urbach能量作为亚带隙无序指标，再用随机森林代理解释参数贡献与温度—氧气交互。人类按提取规则重新优化并获得更低Urbach能量。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。研究把自驱动溅射外延优化产生的数据转成可解释、可由人执行的β-Ga2O3薄膜生长规则。系统用贝叶斯优化寻找生长条件，以自动光学Urbach能量作为亚带隙无序指标，再用随机森林代理解释参数贡献与温度—氧气交互。人类按提取规则重新优化并获得更低Urbach能量。
  - 原文位置：摘要；TXT第1行；核验TXT行号 1；引文：Self-driving laboratories are powerful tools for navigating high-dimensional process spaces, yet Bayesian-optimization decision layers optimize black-box objective functions without distilling transferable process understanding.
- 多步行动过程：yes。自动化平台围绕溅射参数进行贝叶斯优化，生长薄膜后自动测量光学透射并计算Urbach能量，结果反馈至下一轮参数选择。完成闭环后，随机森林代理分析参数影响并生成逐步可执行规则，由研究者据此重新优化并验证规则的迁移性。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。
  - 原文位置：摘要；TXT第1行；核验TXT行号 1；引文：Here, we demonstrate a mathematically interpretable self-driving laboratory framework that transforms autonomous optimization data into human-executable growth rules.
- 至少一种Agent能力：yes。Interpretable self-driving sputtering epitaxy reveals human-usable growth rules for β-Ga2O3 films。系统角色与能力：自动化平台围绕溅射参数进行贝叶斯优化，生长薄膜后自动测量光学透射并计算Urbach能量，结果反馈至下一轮参数选择。完成闭环后，随机森林代理分析参数影响并生成逐步可执行规则，由研究者据此重新优化并验证规则的迁移性。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。
  - 原文位置：摘要；TXT第1行；核验TXT行号 1；引文：To convert closed-loop data into interpretable growth rules, we train a random forest surrogate and reveal that the growth landscape is described by additive contributions from four growth parameters, with a temperature–oxygen interaction.
- 明确科研流程角色：yes。异质外延获得182 meV Urbach能量；优化窗口迁移到基底实现单晶同质外延并由STEM佐证；从代理模型提取规则后，人类执行重新优化得到163 meV。
  - 原文位置：摘要；TXT第1行；核验TXT行号 1；引文：By combining Bayesian optimization with automated optical evaluation of the Urbach energy as a sub-bandgap disorder metric, the self-driving system identifies heteroepitaxial conditions yielding an Urbach energy of 182 meV, below previously reported values for sputtered β -Ga 2 O 3 films.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：04
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：04（仅归档，不覆盖其他模块）
- 模块内分类路径：04.04 能源、电子与器件材料
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

对象为β-Ga2O3薄膜溅射外延及生长工艺，04.04材料合成/实验。需要区分Agent/优化器自动运行部分与研究者执行的二次优化。

### 2.3 容易混淆的边界

对象为β-Ga2O3薄膜溅射外延及生长工艺，04.04材料合成/实验。需要区分Agent/优化器自动运行部分与研究者执行的二次优化。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM科研Agent

### 3.2 科研流程角色

计算/数据分析

Interpretable self-driving sputtering epitaxy reveals human-usable growth rules for β-Ga2O3 films。系统角色与能力：自动化平台围绕溅射参数进行贝叶斯优化，生长薄膜后自动测量光学透射并计算Urbach能量，结果反馈至下一轮参数选择。完成闭环后，随机森林代理分析参数影响并生成逐步可执行规则，由研究者据此重新优化并验证规则的迁移性。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 3.3 自主能力

Interpretable self-driving sputtering epitaxy reveals human-usable growth rules for β-Ga2O3 films。系统角色与能力：自动化平台围绕溅射参数进行贝叶斯优化，生长薄膜后自动测量光学透射并计算Urbach能量，结果反馈至下一轮参数选择。完成闭环后，随机森林代理分析参数影响并生成逐步可执行规则，由研究者据此重新优化并验证规则的迁移性。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

可支持综述讨论自驱实验从黑箱寻优走向人可用工艺知识提取。 科学贡献与系统贡献按上述证据分别表述。

### 4.2 系统流程与组件

自动化平台围绕溅射参数进行贝叶斯优化，生长薄膜后自动测量光学透射并计算Urbach能量，结果反馈至下一轮参数选择。完成闭环后，随机森林代理分析参数影响并生成逐步可执行规则，由研究者据此重新优化并验证规则的迁移性。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

异质外延获得182 meV Urbach能量；优化窗口迁移到基底实现单晶同质外延并由STEM佐证；从代理模型提取规则后，人类执行重新优化得到163 meV。

### 5.2 基线、指标与结果

异质外延获得182 meV Urbach能量；优化窗口迁移到基底实现单晶同质外延并由STEM佐证；从代理模型提取规则后，人类执行重新优化得到163 meV。

### 5.3 科学贡献与证据强度

可支持综述讨论自驱实验从黑箱寻优走向人可用工艺知识提取。 科学贡献与系统贡献按上述证据分别表述。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

本文在自驱实验室贝叶斯优化基础上，结合可解释代理模型，从黑箱生长参数优化中提取人可执行规则。

## 7. 局限性与风险

作者及读者可确认的适用边界：实验对象为β-Ga2O3溅射外延这一材料和工艺窗口；可迁移规则需在其他化合物、设备及沉积条件下验证。

## 8. 对综述写作的价值

可支持综述讨论自驱实验从黑箱寻优走向人可用工艺知识提取。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

研究把自驱动溅射外延优化产生的数据转成可解释、可由人执行的β-Ga2O3薄膜生长规则。

### 9.2 速记版 pipeline

自动化平台围绕溅射参数进行贝叶斯优化，生长薄膜后自动测量光学透射并计算Urbach能量，结果反馈至下一轮参数选择。完成闭环后，随机森林代理分析参数影响并生成逐步可执行规则，由研究者据此重新优化并验证规则的迁移性。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 9.3 标注字段汇总

```text
paper_id=ASD-0999
inclusion_status=to_read
scientific_object_modules=04
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=04
module_taxonomy_codes=04.04
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`04.04.04` 半导体材料；二级：`04.04`。
- 原文位置：PDF p.1。
- 判定：βGa2O3半导体薄膜制备与光学品质指标。
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
