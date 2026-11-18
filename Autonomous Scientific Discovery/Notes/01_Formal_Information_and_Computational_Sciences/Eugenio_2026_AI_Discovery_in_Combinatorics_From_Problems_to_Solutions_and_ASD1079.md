# AI Discovery in Combinatorics: From Problems to Solutions and Back to Bigger Problems

**论文信息**

- ID：ASD-1079
- 标题：AI Discovery in Combinatorics: From Problems to Solutions and Back to Bigger Problems
- 作者：Cainelli, Eugenio; Luccioli, Lorenzo; Iraci, Alessandro; Paolini, Giovanni
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2610.16555
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1079.txt
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Eugenio_2026_AI_Discovery_in_Combinatorics_From_Problems_to_Solutions_and_ASD1079.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 对象 | 29个代数组合学开放问题。 | TXT lines 17-18；核验TXT行号 17 | ABSTRACT We introduce qtBench, a benchmark of 29 open problems in algebraic combi- | 高（一手正文；非独立复现） |
| 科学目标 | 寻求解释多项式系数或恒等式的简洁组合算法。 | TXT lines 18-20；核验TXT行号 18 | We introduce qtBench, a benchmark of 29 open problems in algebraic combi- natorics. These problems ask for a simple combinatorial algorithm that explains given polynomial coefficients or identities. To help AI agents search for such algo- | 高（一手正文；非独立复现） |
| 工具 | 提供组合对象探索、反作弊和候选测试支架。 | TXT lines 20-22；核验TXT行号 20 | given polynomial coefficients or identities. To help AI agents search for such algo- rithms, we provide a scaffold for playing with combinatorial objects, countering cheating attempts, and testing candidate solutions. To explore how far frontier | 高（一手正文；非独立复现） |
| 评估 | 前沿AI系统对若干问题提出候选解。 | TXT lines 22-24；核验TXT行号 22 | cheating attempts, and testing candidate solutions. To explore how far frontier AI systems can go on these problems, we collaborated with OpenAI, whose re- searchers obtained proposed solutions to several of them. This highlights bigger | 高（一手正文；非独立复现） |
| 基准边界 | 论文同时讨论AI发现规模化的伦理问题。 | TXT lines 23-25；核验TXT行号 23 | AI systems can go on these problems, we collaborated with OpenAI, whose re- searchers obtained proposed solutions to several of them. This highlights bigger meta-problems: is AI discovery at scale ethical? How should these results be re- | 高（一手正文；非独立复现） |

## 0. 摘要翻译

qtBench收录29个代数组合学开放问题，目标是寻找解释给定多项式系数或恒等式的简洁组合算法。基准提供组合对象探索、反作弊和候选解测试支架，并与前沿AI系统合作尝试若干问题。论文同时讨论AI大规模数学发现的伦理及结果分享问题。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。建立代数组合学开放问题基准并支持候选解搜索。
  - 原文位置：TXT lines 17-18；核验TXT行号 17；引文：ABSTRACT We introduce qtBench, a benchmark of 29 open problems in algebraic combi-
- 多步行动过程：yes。工具帮助构造组合对象、检验候选并防止作弊。
  - 原文位置：TXT lines 20-22；核验TXT行号 20；引文：given polynomial coefficients or identities. To help AI agents search for such algo- rithms, we provide a scaffold for playing with combinatorial objects, countering cheating attempts, and testing candidate solutions. To explore how far frontier
- 至少一种Agent能力：yes。AI研究者已针对若干开放问题提出候选解。
  - 原文位置：TXT lines 22-24；核验TXT行号 22；引文：cheating attempts, and testing candidate solutions. To explore how far frontier AI systems can go on these problems, we collaborated with OpenAI, whose re- searchers obtained proposed solutions to several of them. This highlights bigger
- 明确科研流程角色：yes。Agent提出解释组合多项式系数或恒等式的算法。
  - 原文位置：TXT lines 18-20；核验TXT行号 18；引文：We introduce qtBench, a benchmark of 29 open problems in algebraic combi- natorics. These problems ask for a simple combinatorial algorithm that explains given polynomial coefficients or identities. To help AI agents search for such algo-

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：01
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：01（仅归档，不覆盖其他模块）
- 模块内分类路径：01.01.12 离散数学与组合数学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

对象为代数组合学问题与算法，属于01数学理论。

### 2.3 容易混淆的边界

对象为代数组合学问题与算法，属于01数学理论。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

mathematical_discovery_agent

### 3.2 科研流程角色

problem_solving；candidate_testing

AI系统利用问题专属脚手架操作组合对象、提出算法候选并接受测试；问题基准和反作弊检查提供外部约束。

### 3.3 自主能力

AI研究者已针对若干开放问题提出候选解。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

数学贡献为开放问题及若干候选解和更大问题线索；系统贡献为qtBench基准与防作弊候选测试工具。

### 4.2 系统流程与组件

输入开放组合问题及目标多项式/恒等式；Agent探索组合对象并提出统一算法，脚手架对候选进行数值或结构测试并检查作弊式硬编码；研究者核验候选是否解释更广参数范围并讨论解答回馈更大问题。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

基准含29题，具备组合对象操作、反作弊、候选测试及问题状态跟踪；解答由研究者提出并需数学审查。

### 5.2 基线、指标与结果

摘要称合作研究者为若干问题取得候选解；不应将所有候选等同正式发表的完整证明。

### 5.3 科学贡献与证据强度

数学贡献为开放问题及若干候选解和更大问题线索；系统贡献为qtBench基准与防作弊候选测试工具。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

延伸形式化猜想库和Erdos问题数据库，聚焦开放的代数组合学研究题。

## 7. 局限性与风险

- author_stated：开放问题可能在论文准备期间被解决；需关注发现规模的伦理与成果分享。
- reviewer_inference：候选解的正确性和原创性需逐题核查，基准结果不能代表一般数学能力。

## 8. 对综述写作的价值

可讨论开放问题基准如何连接Agent搜索、验证和科学发现伦理。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

qtBench为AI研究开放代数组合问题提供组合对象探索和候选测试支架。

### 9.2 速记版 pipeline

输入开放组合问题及目标多项式/恒等式；Agent探索组合对象并提出统一算法，脚手架对候选进行数值或结构测试并检查作弊式硬编码；研究者核验候选是否解释更广参数范围并讨论解答回馈更大问题。

### 9.3 标注字段汇总

```text
paper_id=ASD-1079
inclusion_status=to_read
scientific_object_modules=01
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=01
module_taxonomy_codes=01.01.12
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O5 开放数学 | 29个代数组合学开放问题寻求新算法 | “29 open problems in algebraic combi- natorics” · L22 |
| 验证强度 | V2 计算/仿真/回顾性 | 候选解经测试支架验证，需数学审查 | “testing candidate solutions” · L23 |
| 系统自主性 | L2 闭环执行者 | Agent搜索组合算法，人设定问题和审查结果 | — |

- 强验证（V3–V4）：否
- 置信度：medium；需全文复核：是；争议记录：无
- 复核状态：待专家复核：需全文复核
