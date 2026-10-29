# VALG: An Agentic System for ML Theory Research

**论文信息**

- ID：ASD-1074
- 标题：VALG: An Agentic System for ML Theory Research
- 作者：Zhang, Dechen; Tang, Xuan; Yin, Xinxiang; Chen, Xingwu; Qian, Jian; Zou, Difan
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2608.13060
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1074.txt
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Dechen_2026_VALG_An_Agentic_System_for_ML_Theory_Research_ASD1074.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 科研对象 | 机器学习理论问题及定理证明。 | TXT lines 14-16；核验TXT行号 14 | Machine learning theory studies learning procedures through mathematical setups in which the data model, training protocol, oracle access, loss, metric, and randomness define the phenomenon that a theorem is meant to explain. Solving an open problem therefore requires the problem | 高（一手正文；非独立复现） |
| 多步流程 | 失败后诊断推导、证明结构或定理表述。 | TXT lines 25-27；核验TXT行号 25 | local proofs in dependency order. When a proof attempt fails, VALG identifies whether the obstruction lies in a derivation, the proof structure, or the theorem formulation and routes the next attempt accordingly. Formulation-level obstructions initiate an explicitly related variant or | 高（一手正文；非独立复现） |
| 基准任务 | 评估九个子问题，来自五项COLT 2026开放问题。 | TXT lines 30-32；核验TXT行号 30 | We evaluate VALG on nine subproblems from five COLT 2026 open problems spanning tensor decomposition, learning complexity, one-bit mean estimation, differential privacy, and online optimization. Two runs produce internally finalized theorem candidates that match the | 高（一手正文；非独立复现） |
| 结果 | 两个运行产生匹配原问题范围的定理候选，其余为受限结果。 | TXT lines 32-35；核验TXT行号 32 | online optimization. Two runs produce internally finalized theorem candidates that match the scope of their source briefs and address the original subproblems; the remaining seven yield restricted-method results, special cases, or conditional theorems. For each candidate, we report the problem setup, theorem statement, and progress relative to the source problem. These case | 高（一手正文；非独立复现） |
| 局限 | 作者呼吁更广泛基准和更易核验的证明写作。 | TXT lines 2777-2780；核验TXT行号 2777 | derivations are plausible, these stylistic issues significantly increase the cost of expert verification. Rigorous evaluation also requires machine learning theory benchmarks that go beyond case studies of open problems. Our findings on COLT open problems indicate that difficult questions often benefit from multiple perspectives and evolving generation of ideas. However, to meaningfully | 高（一手正文；非独立复现） |

## 0. 摘要翻译

VALG将机器学习理论研究组织为源问题关联的定理分支，维持数学规格、证明依赖图和来源范围。证明失败时系统判断障碍来自推导、结构或定理表述，并选择局部修复或相关变体。九个COLT开放问题子题中，两个运行得到匹配原题范围的定理候选，其余产生受限、特殊或条件性结果。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。处理机器学习理论开放问题并生成定理候选。
  - 原文位置：TXT lines 19-20；核验TXT行号 19；引文：both assumptions and proofs. We investigate whether this process can be organized as an autonomous agentic workflow for ML theory research.
- 多步行动过程：yes。固定数学规格、依赖图证明、局部修复与问题重构构成循环。
  - 原文位置：TXT lines 25-27；核验TXT行号 25；引文：local proofs in dependency order. When a proof attempt fails, VALG identifies whether the obstruction lies in a derivation, the proof structure, or the theorem formulation and routes the next attempt accordingly. Formulation-level obstructions initiate an explicitly related variant or
- 至少一种Agent能力：yes。系统可检查证明图、构造局部证明并据失败类型调整。
  - 原文位置：TXT lines 2763-2765；核验TXT行号 2763；引文：VALG organizes informal ML-theory research around source-relative theorem branches whose assumptions, proof dependencies, and outcomes remain tied to the originating question. Its global- to-local proof process supports both local repair and formulation-level revision, allowing a failed
- 明确科研流程角色：yes。研究者角色为假设形成、验证及修订定理表述和证明。
  - 原文位置：TXT lines 17-19；核验TXT行号 17；引文：formulation, theorem target, and proof mechanism to be developed in concert. Researchers formulate hypotheses, test them through preliminary theoretical or empirical analysis, and refine both assumptions and proofs. We investigate whether this process can be organized as an

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

对象是机器学习理论与数学定理，归入01数学/理论科学。

### 2.3 容易混淆的边界

对象是机器学习理论与数学定理，归入01数学/理论科学。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

multi_agent_theory_system

### 3.2 科研流程角色

problem_formulation；proof_generation；proof_review

多Agent系统执行问题表述、证明依赖图管理、局部证明构造与验证，并按失败位置路由后续尝试。

### 3.3 自主能力

系统可检查证明图、构造局部证明并据失败类型调整。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

科学贡献是若干理论问题的定理候选及受限结果；系统贡献是来源范围追踪和全局到局部证明流程。

### 4.2 系统流程与组件

输入开放理论问题及源问题规格；系统形成假设和定理目标，构造类型化证明依赖图并按依赖顺序生成/检查局部证明；失败后定位推导、证明结构或问题表述障碍，修复或创建保持关联的变体，输出证明及范围分类。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

九个子问题、五个COLT 2026开放问题案例；按源问题范围、证明内部完成状态、假设和定理结论逐项报告。

### 5.2 基线、指标与结果

作者报告2/9得到范围匹配的内部定理候选，其余为受限方法结果、特殊情况或条件定理。

### 5.3 科学贡献与证据强度

科学贡献是若干理论问题的定理候选及受限结果；系统贡献是来源范围追踪和全局到局部证明流程。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

针对机器学习理论开放问题研究，强调定理形式化和证明依赖管理。

## 7. 局限性与风险

- author_stated：目前是开放问题案例研究，需超越案例的已知答案控制基准；机器生成证明可读性和形式化仍困难。
- reviewer_inference：内部完成候选不自动等同社区确认的新定理。

## 8. 对综述写作的价值

可支持讨论Agent失败诊断后修订科学问题范围并保持源问题关系。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

VALG管理ML理论问题分支并在九个子题上生成分级定理结果。

### 9.2 速记版 pipeline

输入开放理论问题及源问题规格；系统形成假设和定理目标，构造类型化证明依赖图并按依赖顺序生成/检查局部证明；失败后定位推导、证明结构或问题表述障碍，修复或创建保持关联的变体，输出证明及范围分类。

### 9.3 标注字段汇总

```text
paper_id=ASD-1074
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


## 2026-10-29 三级分类复核

- 归档分类：`01.02.13` 机器学习；二级：`01.02`。
- 原文位置：PDF p.1。
- 判定：机器学习理论问题和张量分解算法验证，机器学习；数学标签可交叉保留。
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
