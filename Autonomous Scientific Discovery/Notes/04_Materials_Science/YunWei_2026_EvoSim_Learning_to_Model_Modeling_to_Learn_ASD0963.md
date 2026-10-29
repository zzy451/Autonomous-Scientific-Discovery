# EvoSim: Learning to Model, Modeling to Learn

**论文信息**

- ID：ASD-0963
- 标题：EvoSim: Learning to Model, Modeling to Learn
- 作者：Song, Yun-Wei; Tao, Jinkai; Zhang, Jun-Dong; Zhang, Rui; Wu, Yi-Min; Zhang, Qiang
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2610.11344
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0963.txt
- PDF / 本地文件路径：Reference_PDF/04_Materials_Science/YunWei_2026_EvoSim_Learning_to_Model_Modeling_to_Learn_ASD0963.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 纳入判断：论文直接研究科研Agent或其评测。 | EvoSim是物理建模AI Scientist，同时演化领域模型和可复用建模能力。论文以电池析锂起始和车辆动态电压预测为任务，研究模型假设搜索与程序复用能否提高准确性和效率。 | TXT line 925；核验TXT行号 925 | EvoSim uses COMSOL Multiphysics® to construct and solve the physics-based models. Each model undergoes three checks. The implementation check confirms the active equations and states. The solution check confirms that the requested simulation is complete and the outputs are finite. The measurement check compares the prediction with the specified observations. | 高（一手正文；非独立复现） |
| 对象证据：正文界定科学问题及研究对象。 | EvoSim在石墨电极析锂/剥离反应和电池车辆工况电压上开展实际物理建模，核心对象为电池材料系统（04.04.02），同时涉及电化学（03.02）。 | TXT line 954；核验TXT行号 954 | The measurements cover two graphite-electrode designs, A1 and A2, at temperatures of 25, 35, and 45∘C. Charging rates range from 2C to 6C. C-rate expresses charging current relative to rated cell capacity. The experimental target is the graphite state of charge (SOC) at which accumulated irreversible lithium reaches 0.05% of graphite capacity. This definition connects electrode design and charging conditions to fast-charge limits. | 高（一手正文；非独立复现） |
| 方法证据：全文描述Agent操作或评测流程。 | 析锂任务采用61个石墨电池中的20项测量，14种条件用于参数识别、6种留出验证；动态电压任务使用DST和US06时序数据，并在11个任务开展45组匹配运行。并记录每次模型修改的检查结果。 | TXT line 968；核验TXT行号 968 | On these held-out conditions, predicted onset SOC has an MAE of 1.79 SOC percentage points and an RMSE of 2.11 SOC percentage points (Figure 3a,b). | 高（一手正文；非独立复现） |
| 验证证据：实验报告任务、数据与验证设计。 | 科学贡献是电池析锂和动态电压模型结果；系统贡献是结合物理模型迭代与经核查的程序知识复用。 | TXT line 1093；核验TXT行号 1093 | We analyze 45 matched pairs across 11 modeling tasks. Each pair contains one Baseline run and one Scientific Evolution run. The two runs use the same task, starting model, data, solver, checks, and evaluation budget. | 高（一手正文；非独立复现） |
| 结果贡献：正文报告可核查结果和贡献。 | 对象明确为电池电化学及能源系统，归入04；Agent方法服务于该领域实验。 | TXT line 1117；核验TXT行号 1117 | We presented EvoSim, an AI scientist that co-evolves physics-based models and reusable modeling capabilities. The model evolving process investigates physical hypotheses in parallel, using experimental discrepancies to guide changes to mechanisms, equations, and couplings. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

EvoSim是物理建模AI Scientist，同时演化领域模型和可复用建模能力。论文以电池析锂起始和车辆动态电压预测为任务，研究模型假设搜索与程序复用能否提高准确性和效率。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。正文提出科学研究或科学评测目标。
  - 原文位置：TXT line 925；核验TXT行号 925；引文：EvoSim uses COMSOL Multiphysics® to construct and solve the physics-based models. Each model undergoes three checks. The implementation check confirms the active equations and states. The solution check confirms that the requested simulation is complete and the outputs are finite. The measurement check compares the prediction with the specified observations.
- 多步行动过程：yes。正文描述多阶段行动及反馈流程。
  - 原文位置：TXT line 961；核验TXT行号 961；引文：EvoSim starts from a one-dimensional porous-electrode model for electrolyte transport, electronic conduction, particle diffusion, and graphite intercalation. It adds a parallel plating and stripping reaction driven by the local plating overpotential.
- 至少一种Agent能力：yes。正文显示Agent使用工具、状态或证据进行决策。
  - 原文位置：TXT line 968；核验TXT行号 968；引文：On these held-out conditions, predicted onset SOC has an MAE of 1.79 SOC percentage points and an RMSE of 2.11 SOC percentage points (Figure 3a,b).
- 明确科研流程角色：yes。系统承担科研执行、理论发现或科研评价角色。
  - 原文位置：TXT line 1093；核验TXT行号 1093；引文：We analyze 45 matched pairs across 11 modeling tasks. Each pair contains one Baseline run and one Scientific Evolution run. The two runs use the same task, starting model, data, solver, checks, and evaluation budget.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：03;04
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：04（仅归档，不覆盖其他模块）
- 模块内分类路径：03.02 基础化学；04.04 能源、电子与器件材料
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

留出析锂与电池电压预测均以电池电极和电池运行行为为对象，优先归04.04.02电池材料；析锂/剥离反应具有明确电化学对象，故同时列03.02。

### 2.3 容易混淆的边界

留出析锂与电池电压预测均以电池电极和电池运行行为为对象，优先归04.04.02电池材料；析锂/剥离反应具有明确电化学对象，故同时列03.02。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

科学Agent；工具增强Agent

### 3.2 科研流程角色

物理建模；实验迭代；知识复用

Agent调用COMSOL求解物理模型，以实验偏差提出机制、方程或耦合改动；每个模型经过实现、求解和测量检查。科学演化模块从成功与失败研究提取经证据核查的程序并用于后续任务。

### 3.3 自主能力

正文显示Agent使用工具、状态或证据进行决策。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

相较只保存结果的记忆机制，EvoSim提炼可执行程序并迁移至后续建模；Naive Memory比较接近Baseline。

### 4.2 系统流程与组件

析锂任务采用61个石墨电池中的20项测量，14种条件用于参数识别、6种留出验证；动态电压任务使用DST和US06时序数据，并在11个任务开展45组匹配运行。并记录每次模型修改的检查结果。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

作者报告留出析锂条件SOC MAE为1.79个百分点；电压模型指定交叉验证RMSE为7.62 mV。45组匹配运行中模型及机制失败从33次降至21次，执行时间下降42.6%。

### 5.2 基线、指标与结果

科学贡献是电池析锂和动态电压模型结果；系统贡献是结合物理模型迭代与经核查的程序知识复用。

### 5.3 科学贡献与证据强度

相较只保存结果的记忆机制，EvoSim提炼可执行程序并迁移至后续建模；Naive Memory比较接近Baseline。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

证据主要来自两个工业电池任务及特定仿真器和评价流程，其对其他体系的泛化仍待验证。

## 7. 局限性与风险

对象明确为电池电化学及能源系统，归入04；Agent方法服务于该领域实验。

## 8. 对综述写作的价值

EvoSim以实验偏差驱动电池物理模型迭代，并复用研究程序；作者报告精度、失败率及效率改善。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

EvoSim以实验偏差驱动电池物理模型迭代，并复用研究程序；作者报告精度、失败率及效率改善。

### 9.2 速记版 pipeline

析锂任务采用61个石墨电池中的20项测量，14种条件用于参数识别、6种留出验证；动态电压任务使用DST和US06时序数据，并在11个任务开展45组匹配运行。并记录每次模型修改的检查结果。

### 9.3 标注字段汇总

```text
paper_id=ASD-0963
inclusion_status=to_read
scientific_object_modules=03;04
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=04
module_taxonomy_codes=03.02;04.04
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`04.04.02` 电池材料；二级：`04.04`。
- 原文位置：PDF p.1。
- 判定：电池锂析出及电压仿真校准，明确电池材料应用。
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
