# DrugTargetWorld: A Synthetic Biobank for Training and Benchmarking AI Scientists

**论文信息**

- ID：ASD-1039
- 标题：DrugTargetWorld: A Synthetic Biobank for Training and Benchmarking AI Scientists
- 作者：Margolis, Samuel; Schmiedmayer, Paul; Huang, Alan; Chen, Ethan; Bhattacharjee, Ishan; Shah, Atman; Viggiano, Ben; Cao, Fang; Reddy, Shriya; Xia, Roger; O'Sullivan, Jack; Katz, Daniel; Wheeler, Matthew; Ashley, Euan; Gomes, Bruna
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2610.09558
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1039.txt
- PDF / 本地文件路径：Reference_PDF/06_Life_Sciences/Samuel_2026_DrugTargetWorld_A_Synthetic_Biobank_for_Training_and_Benchmarking_AI_ASD1039.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| Agent科研目标 | 疾病靶点发现和干预方向推断。 | Abstract；核验TXT行号 35 | drug target discovery | 高（一手正文；非独立复现） |
| 模拟生物库 | 每个世界生成54000参与者并关联基因、蛋白、健康记录和结局。 | Abstract / Figure 1；核验TXT行号 128 | 54,000 participants with linked molecular measurements | 高（一手正文；非独立复现） |
| 隐藏真值 | 每个世界由隐藏因果模型规定真实因果蛋白、效应方向和混杂陷阱。 | Abstract；核验TXT行号 22 | Each world is governed by a concealed causal model | 高（一手正文；非独立复现） |
| 多步任务 | Agent构建疾病表型、确定靶点并可运行虚拟wet-lab实验。 | Abstract；核验TXT行号 26 | with the option to conduct virtual ‘wet lab’ experiments | 高（一手正文；非独立复现） |
| 比较规模 | 九个Agent在20 worlds、三种预算中完成540 episodes。 | Results；核验TXT行号 115 | We evaluated nine agents in 540 episodes across 20 worlds | 高（一手正文；非独立复现） |
| 结果限制 | 领先Agent恢复64%因果driver，但未可靠排除伪因果蛋白。 | Results；核验TXT行号 29 | no agent reliably distinguished misleading non-causal​ ​proteins | 高（一手正文；非独立复现） |
| 主控复核：具体科学对象 | 合成生物库包含遗传、蛋白、健康记录及心血管疾病表型；Agent识别致病驱动蛋白和干预方向，生命科学与药物发现对象均有支持。 | TXT line 19；核验TXT行号 19 | 54,000 participants, including 10,800​ ​with synthetic magnetic resonance imaging (MRI) data. The present study instantiates this framework in​ ​cardiovascular disease while the underlying world generation framework is designed to support other disease​ ​domai | 高（一手正文；非独立复现） |

## 0. 摘要翻译

DrugTargetWorld程序化生成具有隐藏因果真值的合成生物库，用于训练和评估Agent的端到端药物靶点发现。本文以心血管疾病实例化，Agent从原始数据构造疾病表型、寻找因果蛋白、判断干预方向并可使用虚拟实验。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。目标是让Agent从模拟生物库识别疾病因果蛋白及有益干预方向。
  - 原文位置：Abstract；核验TXT行号 84；引文：drug target discovery lacks such a verifiable reward
- 多步行动过程：yes。Agent需选择分析与虚拟实验，在有限预算内依序推进靶点发现。
  - 原文位置：Introduction / Methods；核验TXT行号 164；引文：determine which analyses and experiments to perform under finite resources
- 至少一种Agent能力：yes。不同Agent读取数据、运行遗传分析、选择实验并据隐藏因果真值得分。
  - 原文位置：Results；核验TXT行号 115；引文：We evaluated nine agents in 540 episodes across 20 worlds and three experimental budgets.
- 明确科研流程角色：yes。端到端研究任务是构建疾病表型、识别因果蛋白、推断干预方向。
  - 原文位置：Abstract；核验TXT行号 25；引文：identifying which proteins causally drive disease and inferring the beneficial direction of modulation

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：06;07
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：06（仅归档，不覆盖其他模块）
- 模块内分类路径：06.03.01 基因组学；07.04.01 药物发现
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

合成生物库包含遗传、蛋白、健康记录及心血管疾病表型；Agent识别致病驱动蛋白和干预方向，生命科学与药物发现对象均有支持。

### 2.3 容易混淆的边界

合成生物库包含遗传、蛋白、健康记录及心血管疾病表型；Agent识别致病驱动蛋白和干预方向，生命科学与药物发现对象均有支持。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM Agent；Tool-using Agent；Planning Agent

### 3.2 科研流程角色

hypothesis_generation；experimental_design；simulation_modeling；data_analysis；evidence_assessment_and_validation

可执行代码和工具的科研Agent在可重复合成biobank世界内进行顺序研究决策。

### 3.3 自主能力

不同Agent读取数据、运行遗传分析、选择实验并据隐藏因果真值得分。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

系统贡献为可扩展合成biobank和可验证奖励环境；科学对象任务覆盖遗传/蛋白和心血管疾病药物发现。

### 4.2 系统流程与组件

读取模拟参与者遗传、蛋白、病历、影像及结局数据；选择表型构建和遗传分析；判断蛋白因果关系和调节方向；分配有限预算并运行虚拟实验；按隐藏真值评分。 Agent在每个隐藏真值world内先从原始影像与健康记录构造表型，再选遗传分析和有限虚拟干预，按结果更新因果判断并提交靶点与方向。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

20个世界、3种预算、9个Agent和540 episodes；复合评分含靶点识别、因果置信、干预方向、偏差识别和疾病测量。

### 5.2 基线、指标与结果

两个领先Agent得分39.98和35.38，平均找回64%因果driver；未能可靠识别伪因果蛋白。

### 5.3 科学贡献与证据强度

系统贡献为可扩展合成biobank和可验证奖励环境；科学对象任务覆盖遗传/蛋白和心血管疾病药物发现。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

与一般科学Agent benchmark相比，该环境拥有已知但隐藏的因果真值，并允许有限预算下顺序选择分析/实验。

## 7. 局限性与风险

合成世界不替代真实患者群体验证；实际疾病域仅实例化心血管疾病；作者指出结论仍需真实队列/实验检验。

## 8. 对综述写作的价值

可支撑面向生物医学研究Agent的因果发现训练环境、预算决策和真值可验证评估。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

合成biobank为Agent提供可验证的药物靶点发现任务。

### 9.2 速记版 pipeline

读取模拟参与者遗传、蛋白、病历、影像及结局数据；选择表型构建和遗传分析；判断蛋白因果关系和调节方向；分配有限预算并运行虚拟实验；按隐藏真值评分。 Agent在每个隐藏真值world内先从原始影像与健康记录构造表型，再选遗传分析和有限虚拟干预，按结果更新因果判断并提交靶点与方向。

### 9.3 标注字段汇总

```text
paper_id=ASD-1039
inclusion_status=to_read
scientific_object_modules=06;07
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=06
module_taxonomy_codes=06.03.01;07.04.01
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O3 新实例 | 在合成生物库中识别隐藏因果蛋白 | “drug target discovery” · L38 |
| 验证强度 | V2 计算/仿真/回顾性 | 与隐藏真值比较为仿真环境验证 | “concealed causal model” · L23 |
| 系统自主性 | L2 闭环执行者 | Agent自主构建表型确定靶点并运行虚拟实验 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
