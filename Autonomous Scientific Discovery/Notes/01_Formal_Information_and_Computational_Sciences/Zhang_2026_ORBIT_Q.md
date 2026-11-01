# ORBIT-Q: Dual-axis benchmarking of autonomous agents in scientific quantum programming

## 当前分类（2026-11-01 实证复核）

- 当前纳入状态：`included`；主归档：`01`。
- 本块为当前有效结论；后文既有分类、来源限制与审计判断均保留为历史记录，与本块不一致者由本块取代。
- 当前对象模块：`01;02`。
- 代表分类每个模块保留一个落点，不表示穷尽全文全部细类。

| 模块 | 二级 | 三级 | 本轮结论 |
|---|---|---|---|
| 01 | 01.02 计算机科学 | 01.02.17 科学计算与高性能计算 | 已落地 |
| 02 | 02.02 物理学 | 02.02.06 量子力学 | 已落地 |

- 模块02：12项评测含量子态制备及弦序验证结果。
  - 证据：PDF 第 [3, 4] 页；原文：Spin-1 Haldane-chain state preparation and string-order verification

- 完整裁决：`Coverage_Check/classification_recheck_2026-11-01/`。

## 既有笔记与历史审计记录

**论文信息**

- ID：ASD-0905
- 标题：ORBIT-Q: Dual-axis benchmarking of autonomous agents in scientific quantum programming
- 作者：Zhang, Shi-Xin; Chen, Yu-Qin
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2607.03105
- 一手阅读来源：https://arxiv.org/abs/2607.03105
- 来源层级：全文
- 阅读版本：对应缓存来源版本，参见Evidence Log
- 阅读版本题名：ORBIT-Q: Dual-axis benchmarking of autonomous agents in scientific quantum programming
- 原始全文缓存：C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/.tmp_asd_pdfs/ASD-0905.html
- PDF / 本地文件路径：未归档PDF
- 当前状态：included
- 阅读日期：2026-10-22
- 笔记作者：Codex（读者证据包经主控审核整合）

## Evidence Log

| 判断项 | 结论 / 原文概括 | 证据位置 | 可信度 |
|---|---|---|---|
| 评测 Agent 执行研究级量子工作流 | 研究任务由 autonomous coding agents 实现。 | Abstract; Methods—Task generation | high |
| 测试包含 12 项具体科研任务 | 任务包括矩阵乘积态、变分优化、Kraus 通道校准等。 | Methods; Table 1 | high |
| 验证包含科学语义和功能正确性 | 三阶段过滤：确定性功能测试、模型语义审查、边界样本人工复核。 | Figure 1; verification pipeline | high |
| 设计两轴比较 Agent 和框架 | 固定框架比较 Agent，固定 Agent 比较软件框架。 | Abstract; Results | high |
| 报告框架通过数及专家差距 | TC 完成 10/12，PennyLane 8/12，TorchQuantum/MindQuantum 各 4/12；Agent 与专家实现仍有差距。 | Results; Discussion | high |

## 0. 摘要翻译

本文提出 ORBIT-Q，以 12 个研究级量子计算工作流评估自主编程 Agent，并通过多层验证比较 Agent 配置与量子软件框架。测试 TensorCircuit-NG、PennyLane、TorchQuantum、MindQuantum；结果显示框架表现不同，领先 Agent 与专家实现仍有差距。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 当前判断：included；读者建议：included。
具体实验是自主编码 Agent 在量子科研工作流中实现程序并迭代至验证通过；科研角色为量子计算程序实现。

### 1.2 排除风险检查

01.02.17 因研究科学计算程序及其验证；02.02.06 因实际任务是量子力学/量子算法工作流并检查物理保真。模块并列有对象依据，不因代码工具将其全部归 01。
完整闭环不是纳入门槛；科研目标、多步行动、至少一项Agent能力及明确科研角色须同时成立。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：01;02
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：01（仅归档，不替代多模块事实）
- 模块内分类路径：01.02.17; 02.02.06
- 分类深度：03/04使用二级；06/07使用固定三级；其余沿用现有树。
- 分类状态：原文证据复核

### 2.2 对象优先判定

对象：量子机器学习、变分量子算法等量子工作流。框架：TC、PennyLane、TorchQuantum、MindQuantum。基线：不同 Agent、专家参考实现、不同框架。指标：任务通过数、运行时间、资源及成本；通过数 TC 10/12、PennyLane 8/12、另两者各 4/12。

### 2.3 容易混淆的边界

01.02.17 因研究科学计算程序及其验证；02.02.06 因实际任务是量子力学/量子算法工作流并检查物理保真。模块并列有对象依据，不因代码工具将其全部归 01。

## 3. Agent 系统与科研流程角色

具体实验是自主编码 Agent 在量子科研工作流中实现程序并迭代至验证通过；科研角色为量子计算程序实现。

科研流程与自主能力以本文实际行动和工具调用为依据：

建立 12 项 framework-neutral 量子科研代码任务，以容器化环境运行；框架提示、执行镜像和 verifier 随任务配置。采用确定性功能评估、GPT-5.5 语义审查及人工复核；分开比较 Agent 与框架。

## 4. 方法设计

### 4.1 方法动机与设计

提出兼顾 Agent 能力、量子软件适配和科学正确性的研究级量子编程基准。

### 4.2 系统流程与组件

建立 12 项 framework-neutral 量子科研代码任务，以容器化环境运行；框架提示、执行镜像和 verifier 随任务配置。采用确定性功能评估、GPT-5.5 语义审查及人工复核；分开比较 Agent 与框架。

## 5. 实验与验证

### 5.1 验证方式、对象及任务

对象：量子机器学习、变分量子算法等量子工作流。框架：TC、PennyLane、TorchQuantum、MindQuantum。基线：不同 Agent、专家参考实现、不同框架。指标：任务通过数、运行时间、资源及成本；通过数 TC 10/12、PennyLane 8/12、另两者各 4/12。

### 5.2 基线、指标与结果

对象：量子机器学习、变分量子算法等量子工作流。框架：TC、PennyLane、TorchQuantum、MindQuantum。基线：不同 Agent、专家参考实现、不同框架。指标：任务通过数、运行时间、资源及成本；通过数 TC 10/12、PennyLane 8/12、另两者各 4/12。

### 5.3 科学贡献与证据强度

提出兼顾 Agent 能力、量子软件适配和科学正确性的研究级量子编程基准。

证据层级：原始全文支持；作者报告结果不等于独立复现。

## 6. 与已有工作的关系

超出硬件质量或简单代码功能测试基准，强调科研流程工作流、框架-Agent联合表现和物理保真。

## 7. 局限性与风险

仅 12 项代表任务以控制计算成本；语义审查含模型评审和人工边界复核；基准性能不等同于新物理发现。

## 8. 对综述写作的价值

量子计算 Agent 评测、科学代码验证及计算科学/物理模块边界的案例。

推荐引用强度：普通引用，可在核对原文后用于相应领域案例。

## 9. 总结

### 9.1 一句话概括

Agent执行并验证量子程序

### 9.2 速记版 pipeline

建立 12 项 framework-neutral 量子科研代码任务，以容器化环境运行；框架提示、执行镜像和 verifier 随任务配置。采用确定性功能评估、GPT-5.5 语义审查及人工复核；分开比较 Agent 与框架。

### 9.3 标注字段汇总

```text
paper_id=ASD-0905
inclusion_status=included
scientific_object_modules=01;02
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=01
module_taxonomy_codes=01.02.17; 02.02.06
source_level=fulltext
fulltext_followup_required=false
```

### 全文后续要求

本轮已读原始全文并完成对象分类；无需为纳入/分类另做全文补读。具体引用时仍需回查相应原文位置。


## 2026-10-29 PDF补齐归档

- 本地PDF：`Reference_PDF/01_Formal_Information_and_Computational_Sciences/ASD-0905_ORBIT_Q_Dual_axis_benchmarking_of_autonomous_agents_in_scientific_quantum_programming.pdf`，共23页；已核验标题、页面解析和逐页渲染。
- 下载来源：https://arxiv.org/pdf/2607.03105
- 版本：official arXiv preprint PDF; version as downloaded。
- 本轮为来源文件归档，不自动改变既有科学分类或将未决PR意见标记为已结案。
