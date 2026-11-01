# DDA: a traceable multi-agent framework for automated structure-based drug design

**论文信息**

- ID：ASD-1016
- 标题：DDA: a traceable multi-agent framework for automated structure-based drug design
- 作者：Yutao Yu; Sicheng Tian; Guohua Wang; Yang Li
- 年份：2026
- 来源 / venue：Frontiers in Chemistry
- DOI / arXiv / URL：https://doi.org/10.3389/fchem.2026.1914886
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1016.txt
- PDF / 本地文件路径：全文已缓存；PDF尚未归档，详见资料清单
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| scientific object/task | 结构基础药物设计利用蛋白结构设计具有目标结合性质的小分子；DDA旨在自动化完整SBDD流程。 | Full text, extracted character offset 528；核验TXT行号 1 | Structure-Based Drug Design (SBDD) is a key computational paradigm that uses protein structural information to design and optimize small molecules with desired binding properties | 高（一手正文；非独立复现） |
| method or agent workflow | DDA从靶点准备和分子生成推进到多目标评价、候选排序，并记录执行轨迹。 | Full text, extracted character offset 1536；核验TXT行号 1 | enabling autonomous workflow execution from target preparation and molecular generation to multi-objective evaluation, candidate prioritization, and trajectory tracking | 高（一手正文；非独立复现） |
| evaluation design | 作者在CrossDocked2020上系统评估DDA，并与专门的SBDD生成方法及通用LLM Agent比较。 | Full text, extracted character offset 1706；核验TXT行号 1 | We systematically evaluated DDA on the CrossDocked2020 benchmark | 高（一手正文；非独立复现） |
| reported result | 闭环交付产生2,000条候选记录，联合筛选通过率比最强专用基线高20个百分点。 | 本地原文 TXT 第1行 | Under the closed-loop delivery protocol, the framework produced 2,000 final candidate records, with a joint screen-pass rate 20 percentage points higher than that of the strongest specialized baseline. | 高（一手正文；非独立复现） |
| limitation / boundary | 后续工作仍需扩展分子生成器、评估工具、合成规划及面向项目的多目标排序模块。 | Full text, extracted character offset 94544；核验TXT行号 1 | Future work will extend DDA in several directions. These include incorporating flexible structural-context definition strategies, additional molecular generators and evaluation tools, synthesis-planning modules, and project-specific multi-objective ranking policies | 高（一手正文；非独立复现） |

## 0. 摘要翻译

本文提出可追踪多Agent框架DDA，自动执行结构基础药物设计中的靶点结构分析、候选分子生成、ADMET筛选、对接和排序。作者在CrossDocked2020的固定100个靶点上评估，并与专用分子生成方法比较。结果显示该框架能够组织可审计的计算设计流程并产生有竞争力的候选。验证限于计算结构评分和预测，论文没有报告候选的生化或细胞实验活性。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。研究目标是依据蛋白结构设计和筛选小分子候选药物。
  - 原文位置：Full text, extracted character offset 528；核验TXT行号 1；引文：Structure-Based Drug Design (SBDD) is a key computational paradigm that uses protein structural information to design and optimize small molecules with desired binding properties
- 多步行动过程：yes。流程从靶点准备和分子生成推进至多目标评价与候选排序，包含连续分析行动。
  - 原文位置：Full text, extracted character offset 1536；核验TXT行号 1；引文：enabling autonomous workflow execution from target preparation and molecular generation to multi-objective evaluation, candidate prioritization, and trajectory tracking
- 至少一种Agent能力：yes。DDA协调生物信息学、分子建模和分子对接工具以执行结构基础药物设计。
  - 原文位置：Full text, extracted character offset 1536；核验TXT行号 1；引文：enabling autonomous workflow execution from target preparation and molecular generation to multi-objective evaluation, candidate prioritization, and trajectory tracking
- 明确科研流程角色：yes。系统承担从靶点准备、候选生成到评价排序的计算药物发现工作流。
  - 原文位置：Full text, extracted character offset 1536；核验TXT行号 1；引文：enabling autonomous workflow execution from target preparation and molecular generation to multi-objective evaluation, candidate prioritization, and trajectory tracking

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：06;07
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：06（仅归档，不覆盖其他模块）
- 模块内分类路径：06.03.06 蛋白质科学；07.04.01 药物发现
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

归入06.02药物发现与分子设计；仅有计算基准验证，不能视为已发现有效候选药物或证明药理活性。

### 2.3 容易混淆的边界

归入06.02药物发现与分子设计；仅有计算基准验证，不能视为已发现有效候选药物或证明药理活性。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM Agent；Tool-using Agent

### 3.2 科研流程角色

tool_use_and_code_execution；data_analysis；evidence_assessment_and_validation

DDA采用可追踪多Agent结构，把靶点/口袋分析、分子设计、ADMET筛选、对接与候选排序分派给专业步骤，并保留中间决策和结果记录。

### 3.3 自主能力

DDA协调生物信息学、分子建模和分子对接工具以执行结构基础药物设计。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

贡献是将多阶段SBDD工具协调和可审计轨迹结合起来，补足仅生成分子而未组织下游评估的流程缺口。

### 4.2 系统流程与组件

在CrossDocked2020固定100靶点集合评估，工作流读取蛋白结构，生成/优化小分子并进行结构对接及开发性筛选；结果与专门的结构基础药物设计生成模型比较。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

论文使用CrossDocked2020计算基准并与分子生成基线比较候选质量，评价属于结构和计算评分证据；没有报告候选的生化结合实验或细胞验证。

### 5.2 基线、指标与结果

作者认为DDA能执行可追踪的结构基础设计流程，并在固定靶点测试中获得有竞争力的候选；分子评分与对接结果只构成早期筛选证据。

### 5.3 科学贡献与证据强度

贡献是将多阶段SBDD工具协调和可审计轨迹结合起来，补足仅生成分子而未组织下游评估的流程缺口。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

与聚焦单个分子生成器的SBDD研究相比，DDA强调跨靶点的完整计算评估及可追踪决策；比较基线也包括专用生成方法。

## 7. 局限性与风险

固定100靶点基准的分布限制泛化判断；对接、ADMET预测和生成模型评分存在误差，需实验测定活性、选择性、毒性和可合成性。

## 8. 对综述写作的价值

可用于比较多Agent结构基础药物设计中可追踪工具编排与计算筛选证据的限度。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

DDA把蛋白结构、分子生成、ADMET预测和对接排序整合为可审计的药物设计流程，并在CrossDocked2020的100个靶点上测试。计算候选表现不等于实测结合或药理活性，后续仍需实验确认。

### 9.2 速记版 pipeline

在CrossDocked2020固定100靶点集合评估，工作流读取蛋白结构，生成/优化小分子并进行结构对接及开发性筛选；结果与专门的结构基础药物设计生成模型比较。

### 9.3 标注字段汇总

```text
paper_id=ASD-1016
inclusion_status=to_read
scientific_object_modules=06;07
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=06
module_taxonomy_codes=06.03.06;07.04.01
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 PDF补齐归档

- 本地PDF：`Reference_PDF/06_Life_Sciences/ASD-1016_DDA_a_traceable_multi_agent_framework_for_automated_structure_based_drug_design.pdf`，共21页；已核验标题、页面解析和逐页渲染。
- 下载来源：https://www.frontiersin.org/journals/chemistry/articles/10.3389/fchem.2026.1914886/pdf
- 版本：official publisher article PDF。
- 本轮为来源文件归档，不自动改变既有科学分类或将未决PR意见标记为已结案。
