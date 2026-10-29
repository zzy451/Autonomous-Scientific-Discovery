# Agent-E2MD: Autonomous Translation of Interatomic Potential Equations into Physically Validated Pair Styles for Molecular Dynamics in LAMMPS

**论文信息**

- ID：ASD-0985
- 标题：Agent-E2MD: Autonomous Translation of Interatomic Potential Equations into Physically Validated Pair Styles for Molecular Dynamics in LAMMPS
- 作者：Bilvin Varughese; Orcun Yildiz; Aditya Koneru; Henry Chan; Tom Peterka; Subramanian Sankaranarayanan
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2609.26657
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0985.txt
- PDF / 本地文件路径：Reference_PDF/04_Materials_Science/Varughese_2026_Agent_E2MD_Autonomous_Translation_of_Interatomic_Potential_Equations_into_ASD0985.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 纳入与科学目标 | Agent-E2MD把用户给定的原子间势方程转成LAMMPS可运行的pair style，流程结合势函数架构分类、代码生成、构建—测试—修复、模拟执行与分层物理验证。论文覆盖七种势函数/材料组合，并用能量、力、晶格性质、空位形成能、弹性常数及有限温度行为检查实现是否符合参考。其重点是科学软件实现与物理一致性。 | 摘要；TXT第386行；核验TXT行号 386 | Interatomic potentials are the foundational ingredient of molecular dynamics simulations and govern the predictive fidelity of atomistic modeling across diverse classes of materials ranging from metals, semiconductors, oxides, and liquids to reactive systems. | 高（一手正文；非独立复现） |
| 方法与多步工作流 | 势函数方程和目标材料输入后，Agent先判断模型架构及所需邻居列表/导数计算方式，再生成C++实现；系统循环编译、运行测试并修复错误，继而执行LAMMPS计算，对照参考实现检查能量、力及材料物理量，最终交付可运行pair style和验证记录。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。 | 摘要；TXT第386行；核验TXT行号 386 | Here, we introduce Agent-E2MD, a knowledge-guided agentic workflow that translates user-specified interatomic models into executable LAMMPS pair styles. | 高（一手正文；非独立复现） |
| Agent能力与行动 | Agent-E2MD: Autonomous Translation of Interatomic Potential Equations into Physically Validated Pair Styles for Molecular Dynamics in LAMMPS。系统角色与能力：势函数方程和目标材料输入后，Agent先判断模型架构及所需邻居列表/导数计算方式，再生成C++实现；系统循环编译、运行测试并修复错误，继而执行LAMMPS计算，对照参考实现检查能量、力及材料物理量，最终交付可运行pair style和验证记录。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。 | 摘要；TXT第386行；核验TXT行号 386 | The workflow combines architectural classification, code generation, autonomous build-test-fix cycles, simulation execution, and hierarchical physical validation. | 高（一手正文；非独立复现） |
| 验证与结果 | 在七种材料势函数组合上比较生成实现与参考实现的单点能量和力；另以五个晶体多体基准核验弛豫晶格性质、空位形成能及弹性常数，并报告部分体系的有限温度模拟稳定性。 | 摘要；TXT第386行；核验TXT行号 386 | We evaluate Agent-E2MD using seven material-potential pairs: Lennard–Jones Ar, EAM/FS Ag, MEAM Bi, Tersoff Si, GAP Ni, ReaxFF C/H/N/O, and a recently developed Symbolic Regression EAM (Symb EAM) model for Al which is currently unavailable in LAMMPS. | 高（一手正文；非独立复现） |
| 贡献及适用对象 | 可支持综述关于Agent编写科学软件时如何把编译测试与物理不变量验证纳入工作流。 科学贡献与系统贡献按上述证据分别表述。 | 摘要；TXT第386行；核验TXT行号 386 | Single-point calculations show close energy and force agreement between the generated and reference implementations for all seven models. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

Agent-E2MD把用户给定的原子间势方程转成LAMMPS可运行的pair style，流程结合势函数架构分类、代码生成、构建—测试—修复、模拟执行与分层物理验证。论文覆盖七种势函数/材料组合，并用能量、力、晶格性质、空位形成能、弹性常数及有限温度行为检查实现是否符合参考。其重点是科学软件实现与物理一致性。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。Agent-E2MD把用户给定的原子间势方程转成LAMMPS可运行的pair style，流程结合势函数架构分类、代码生成、构建—测试—修复、模拟执行与分层物理验证。论文覆盖七种势函数/材料组合，并用能量、力、晶格性质、空位形成能、弹性常数及有限温度行为检查实现是否符合参考。其重点是科学软件实现与物理一致性。
  - 原文位置：摘要；TXT第386行；核验TXT行号 386；引文：Interatomic potentials are the foundational ingredient of molecular dynamics simulations and govern the predictive fidelity of atomistic modeling across diverse classes of materials ranging from metals, semiconductors, oxides, and liquids to reactive systems.
- 多步行动过程：yes。势函数方程和目标材料输入后，Agent先判断模型架构及所需邻居列表/导数计算方式，再生成C++实现；系统循环编译、运行测试并修复错误，继而执行LAMMPS计算，对照参考实现检查能量、力及材料物理量，最终交付可运行pair style和验证记录。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。
  - 原文位置：摘要；TXT第386行；核验TXT行号 386；引文：Here, we introduce Agent-E2MD, a knowledge-guided agentic workflow that translates user-specified interatomic models into executable LAMMPS pair styles.
- 至少一种Agent能力：yes。Agent-E2MD: Autonomous Translation of Interatomic Potential Equations into Physically Validated Pair Styles for Molecular Dynamics in LAMMPS。系统角色与能力：势函数方程和目标材料输入后，Agent先判断模型架构及所需邻居列表/导数计算方式，再生成C++实现；系统循环编译、运行测试并修复错误，继而执行LAMMPS计算，对照参考实现检查能量、力及材料物理量，最终交付可运行pair style和验证记录。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。
  - 原文位置：摘要；TXT第386行；核验TXT行号 386；引文：The workflow combines architectural classification, code generation, autonomous build-test-fix cycles, simulation execution, and hierarchical physical validation.
- 明确科研流程角色：yes。在七种材料势函数组合上比较生成实现与参考实现的单点能量和力；另以五个晶体多体基准核验弛豫晶格性质、空位形成能及弹性常数，并报告部分体系的有限温度模拟稳定性。
  - 原文位置：摘要；TXT第386行；核验TXT行号 386；引文：We evaluate Agent-E2MD using seven material-potential pairs: Lennard–Jones Ar, EAM/FS Ag, MEAM Bi, Tersoff Si, GAP Ni, ReaxFF C/H/N/O, and a recently developed Symbolic Regression EAM (Symb EAM) model for Al which is currently unavailable in LAMMPS.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：04
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：04（仅归档，不覆盖其他模块）
- 模块内分类路径：04.01 材料基础；04.02 结构材料与无机材料
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

对象是分子动力学势函数的软件实现与原子尺度材料模拟，归04.01/04.02。贡献属于科学计算软件工程和物理验证，而非发现新材料本身。

### 2.3 容易混淆的边界

对象是分子动力学势函数的软件实现与原子尺度材料模拟，归04.01/04.02。贡献属于科学计算软件工程和物理验证，而非发现新材料本身。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM科研Agent

### 3.2 科研流程角色

计算/数据分析

Agent-E2MD: Autonomous Translation of Interatomic Potential Equations into Physically Validated Pair Styles for Molecular Dynamics in LAMMPS。系统角色与能力：势函数方程和目标材料输入后，Agent先判断模型架构及所需邻居列表/导数计算方式，再生成C++实现；系统循环编译、运行测试并修复错误，继而执行LAMMPS计算，对照参考实现检查能量、力及材料物理量，最终交付可运行pair style和验证记录。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 3.3 自主能力

Agent-E2MD: Autonomous Translation of Interatomic Potential Equations into Physically Validated Pair Styles for Molecular Dynamics in LAMMPS。系统角色与能力：势函数方程和目标材料输入后，Agent先判断模型架构及所需邻居列表/导数计算方式，再生成C++实现；系统循环编译、运行测试并修复错误，继而执行LAMMPS计算，对照参考实现检查能量、力及材料物理量，最终交付可运行pair style和验证记录。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

可支持综述关于Agent编写科学软件时如何把编译测试与物理不变量验证纳入工作流。 科学贡献与系统贡献按上述证据分别表述。

### 4.2 系统流程与组件

势函数方程和目标材料输入后，Agent先判断模型架构及所需邻居列表/导数计算方式，再生成C++实现；系统循环编译、运行测试并修复错误，继而执行LAMMPS计算，对照参考实现检查能量、力及材料物理量，最终交付可运行pair style和验证记录。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

在七种材料势函数组合上比较生成实现与参考实现的单点能量和力；另以五个晶体多体基准核验弛豫晶格性质、空位形成能及弹性常数，并报告部分体系的有限温度模拟稳定性。

### 5.2 基线、指标与结果

在七种材料势函数组合上比较生成实现与参考实现的单点能量和力；另以五个晶体多体基准核验弛豫晶格性质、空位形成能及弹性常数，并报告部分体系的有限温度模拟稳定性。

### 5.3 科学贡献与证据强度

可支持综述关于Agent编写科学软件时如何把编译测试与物理不变量验证纳入工作流。 科学贡献与系统贡献按上述证据分别表述。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

本文承接自动代码生成和分子动力学势函数实现工作，进一步将势函数方程翻译、编译修复及物理量核验连成Agent工作流。

## 7. 局限性与风险

作者及读者可确认的适用边界：验证覆盖七种势函数/材料组合及有限的晶体基准；生成代码通过这些物理测试不保证所有势函数、边界条件和系统规模均正确。

## 8. 对综述写作的价值

可支持综述关于Agent编写科学软件时如何把编译测试与物理不变量验证纳入工作流。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

Agent-E2MD把用户给定的原子间势方程转成LAMMPS可运行的pair style，流程结合势函数架构分类、代码生成、构建—测试—修复、模拟执行与分层物理验证。

### 9.2 速记版 pipeline

势函数方程和目标材料输入后，Agent先判断模型架构及所需邻居列表/导数计算方式，再生成C++实现；系统循环编译、运行测试并修复错误，继而执行LAMMPS计算，对照参考实现检查能量、力及材料物理量，最终交付可运行pair style和验证记录。 中间步骤依据上一轮数据调整，最终输出应保留输入、执行记录和结果来源，便于复核。

### 9.3 标注字段汇总

```text
paper_id=ASD-0985
inclusion_status=to_read
scientific_object_modules=04
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=04
module_taxonomy_codes=04.01;04.02
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`04.01.04` 材料计算与材料信息学；二级：`04.01`。
- 原文位置：PDF pp.2。
- 判定：Concrete experiment/task evidence supports 04.01.04 (材料计算与材料信息学). Single-point calculations show close energy and force agreement between the generated and reference implementations for all seven models. Five crystalline many-body benchmarks additionally recover reference relaxed lattice properties, vacancy formation energies, and elastic constants.
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
