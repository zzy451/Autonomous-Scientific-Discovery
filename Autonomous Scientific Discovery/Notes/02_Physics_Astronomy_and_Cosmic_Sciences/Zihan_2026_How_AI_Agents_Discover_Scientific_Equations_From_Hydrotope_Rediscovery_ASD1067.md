# How AI Agents Discover Scientific Equations: From Hydrotope Rediscovery to New Water-Wave Amplitudes

**论文信息**

- ID：ASD-1067
- 标题：How AI Agents Discover Scientific Equations: From Hydrotope Rediscovery to New Water-Wave Amplitudes
- 作者：Zhou, Zihan; Wadekar, Digvijay; Zaldarriaga, Matias
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2610.00435
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1067.txt
- PDF / 本地文件路径：Reference_PDF/02_Physics_Astronomy_and_Cosmic_Sciences/Zihan_2026_How_AI_Agents_Discover_Scientific_Equations_From_Hydrotope_Rediscovery_ASD1067.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 科学问题 | 水波散射公式的重发现和验证。 | TXT line 348；核验TXT行号 348 | We study how AI agents discover and validate scientific formulas using a controlled case | 高（一手正文；非独立复现） |
| 对象章节 | 论文直接以水波散射和hydrotope发现为研究对象。 | TXT lines 926-930；核验TXT行号 926 | In each run, the agent receives only a prompt and the Mathematica code OnShellBG.m, which numerically evaluates the amplitudes using the Berends–Giele recursion. We compare the three prompt packages summarized in Table 1; they vary both the suggested type of equation and the recommended tests. | 高（一手正文；非独立复现） |
| 方法比较 | 对比符号回归等方程搜索方法。 | TXT line 358；核验TXT行号 358 | Only four recover the formula across all kinematic chambers (i.e., regions in which | 高（一手正文；非独立复现） |
| 验证边界 | 作者指出固定训练测试划分与少样本结果的限制。 | TXT lines 1270-1276；核验TXT行号 1270 | Additional experiments test two harder settings. At n=7n=7, the target grows from 8 to 32 max⁡(x,0)\max(x,0) terms; at n=5n=5, an expanded search allows separate formulas for different regions. No fitted method is exact: allowing separate formulas can improve average prediction without recovering the slanted chamber boundaries or the short alternating subset sum. Figure 10 and Appendix C give the additional systems, numerical results, limits of the fixed train–test split, and the n=7n=7 results. | 高（一手正文；非独立复现） |
| 研究贡献 | 关注Agent公式发现并验证过程。 | TXT lines 2729-2736；核验TXT行号 2729 | The main limitations of the present comparisons point to two follow-up experiments. First, future tests should give single agents and teams of agents the same total computational resources and repeat each setup enough times to estimate reliability [29, 16, 47]. Second, the shared written record should connect each proposed formula with its supporting examples, counterexamples, code, and open questions. Agents can then retrieve only the material needed for the current task and avoid repeating earlier work. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

本文在表面水波散射的hydrotope问题上研究AI Agent如何发现和验证科学公式，从既有结果重发现延伸至新的水波振幅关系。作者比较公式搜索方法，考察数据表示、采样、表达式复杂度及验证流程对发现的影响，并讨论受控案例的边界。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。研究Agent如何发现并验证水波散射公式。
  - 原文位置：TXT line 348；核验TXT行号 348；引文：We study how AI agents discover and validate scientific formulas using a controlled case
- 多步行动过程：yes。Agent搜索表达式后需验证、比较并解释候选。
  - 原文位置：TXT line 997；核验TXT行号 997；引文：tests whether exact counterexamples make the agent abandon it.
- 至少一种Agent能力：yes。系统在已有水波问题上重发现并推广振幅公式。
  - 原文位置：TXT line 2323；核验TXT行号 2323；引文：The two-minus experiments show that the team can rediscover a known target
- 明确科研流程角色：yes。承担公式生成和科学验证工作。
  - 原文位置：TXT line 935；核验TXT行号 935；引文：Table 1: The repeated runs vary both the suggested type of equation and the

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

研究对象是物理水波散射及其数学关系，属于02物理科学。

### 2.3 容易混淆的边界

研究对象是物理水波散射及其数学关系，属于02物理科学。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

scientific_equation_agent

### 3.2 科研流程角色

equation_discovery；numerical_validation

AI Agent结合方程候选生成与数值计算/验证；可用候选方法依赖实验配置和允许运算。

### 3.3 自主能力

系统在已有水波问题上重发现并推广振幅公式。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

科学贡献是水波公式关系及Agent发现案例；方法贡献是分析Agent科学公式发现的过程和条件。

### 4.2 系统流程与组件

输入为水波散射数值或理论约束，Agent生成表达式候选并进行数值检验，研究者比较其对已知hydrotope结果的重发现能力及对新振幅关系的外推，再分析候选简洁性和误差。 这一工作流的实施细节、输入输出和验证范围均按原文所报告内容理解，不将展示案例外推为普遍能力。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

使用受控水波散射案例，比较公式与数值/理论结果，并讨论固定训练测试切分及小样本情形。

### 5.2 基线、指标与结果

论文报告hydrotope重发现及新的水波振幅候选；具体效度需结合正文中公式和验证条件解读。

### 5.3 科学贡献与证据强度

科学贡献是水波公式关系及Agent发现案例；方法贡献是分析Agent科学公式发现的过程和条件。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

与符号回归、遗传搜索及其他方程发现方法比较，讨论其变量、运算和采样依赖。

## 7. 局限性与风险

- author_stated：结果依赖输入变量、允许运算、训练点和搜索时间；固定切分与小样本结果存在限制。
- reviewer_inference：受控水波案例不足以证明跨领域公式发现能力。

## 8. 对综述写作的价值

可作为Agent从公式搜索到科学验证的案例，并支持区分发现过程和结论强度。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

本文以水波散射案例分析Agent的科学方程发现与验证。

### 9.2 速记版 pipeline

输入为水波散射数值或理论约束，Agent生成表达式候选并进行数值检验，研究者比较其对已知hydrotope结果的重发现能力及对新振幅关系的外推，再分析候选简洁性和误差。 这一工作流的实施细节、输入输出和验证范围均按原文所报告内容理解，不将展示案例外推为普遍能力。

### 9.3 标注字段汇总

```text
paper_id=ASD-1067
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

- 归档分类：`02.02.03` 经典力学；二级：`02.02`。
- 原文位置：PDF pp.2。
- 判定：Concrete experiment/task evidence supports 02.02.03 (经典力学). The underlying problem arises in one-dimensional deep-water surface-wave scattering. Linearizing the fluid equations makes infinitesimal waves obey superposition, but finite-amplitude waves satisfy nonlinear free-surface boundary conditions.
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
