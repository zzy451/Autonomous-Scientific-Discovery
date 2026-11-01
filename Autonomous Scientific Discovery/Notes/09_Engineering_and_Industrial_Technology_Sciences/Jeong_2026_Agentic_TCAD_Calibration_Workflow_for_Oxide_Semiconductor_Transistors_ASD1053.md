# Agentic TCAD Calibration Workflow for Oxide Semiconductor Transistors

## 当前分类（2026-11-01 实证复核）

- 当前纳入状态：`to_read`；主归档：`09`。
- 本块为当前有效结论；后文既有分类、来源限制与审计判断均保留为历史记录，与本块不一致者由本块取代。
- 当前对象模块：`04;09`。
- 代表分类每个模块保留一个落点，不表示穷尽全文全部细类。

| 模块 | 二级 | 三级 | 本轮结论 |
|---|---|---|---|
| 04 | 04.04 能源、电子与器件材料 | 04.04.04 半导体材料 | 已落地 |
| 09 | 09.08 材料与器件工程 | 09.08.02 半导体器件 | 已落地 |

- 模块04：氧化铟半导体晶体管模型校准和迁移测试。
  - 证据：PDF 第 [3, 4] 页；原文：The same fixed TCAD parameter set is used for the varying-drain-bias tests

- 完整裁决：`Coverage_Check/classification_recheck_2026-11-01/`。

## 既有笔记与历史审计记录

**论文信息**

- ID：ASD-1053
- 标题：Agentic TCAD Calibration Workflow for Oxide Semiconductor Transistors
- 作者：Gyujun Jeong; Junmo Lee; Sungwon Cho; Woohyun Hwang; Kwangyou Seo; Suhwan Lim; Wanki Kim; Daewon Ha; Rishi Ranade; Kihang Youn; Ram Cherukuri; Yiyi Wang; Asif Khan; Shimeng Yu
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2609.12184
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1053.txt
- PDF / 本地文件路径：Reference_PDF/09_Engineering_and_Industrial_Technology_Sciences/Jeong_2026_Agentic_TCAD_Calibration_Workflow_for_Oxide_Semiconductor_Transistors_ASD1053.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 真实器件对象 | 对象为已制造的底栅In–W–O氧化物半导体晶体管。 | Abstract；核验TXT行号 233 | We present the first demonstration of an agentic TCAD calibration workflow for a fabricated bottom-gate In–W–O (BG-IWO) transistor. | 高（一手正文；非独立复现） |
| 校准策略 | 测量—TCAD残差和局部灵敏度引导有界修改。 | Abstract；核验TXT行号 233 | the workflow uses measurement–TCAD residuals and local sensitivity tests to select bounded parameter corrections or evaluate additional physical models | 高（一手正文；非独立复现） |
| Agent控制 | LLM负责工作流编排，Sentaurus管理器件物理。 | Abstract；核验TXT行号 233 | while Sentaurus governs the device physics. | 高（一手正文；非独立复现） |
| 更新数量 | 2% W参考器件经五次Agent建议更新后得到固定校准模型。 | Abstract；核验TXT行号 233 | For the 2%-W reference device, five agent-suggested updates yield a fixed calibrated model, reducing the multi-metric device objective JJ by 14.3 | 高（一手正文；非独立复现） |
| 迁移验证 | 改变漏极偏压和沟道长度测试验证跨偏压/几何转移。 | Abstract；核验TXT行号 233 | Maximum VthV_{\mathrm{th}}/IonI_{\mathrm{on}} errors are 36.1 mV/0.022 decade for varying-drain-bias tests and 46.2 mV/0.062 decade for varying-channel-length tests | 高（一手正文；非独立复现） |
| 主控复核：具体科学对象 | 实测对象为制造的In–W–O氧化物半导体晶体管；TCAD校准直接涉及半导体材料组成和器件转移特性，建议在半导体器件09外补04.04.04。Sentaurus是工具。 | TXT line 233；核验TXT行号 233 | fabricated bottom-gate In–W–O (BG-IWO) transistor. Starting from the measured transfer curve and device information, the workflow uses measurement–TCAD residuals and local sensitivity tests to select bounded parameter corrections or evaluate additional physica | 高（一手正文；非独立复现） |

## 0. 摘要翻译

本文在实际制造的底栅In–W–O晶体管上展示Agentic TCAD校准。LLM Agent用测量和TCAD结果残差及局部灵敏度测试选择有界参数修正或额外物理模型，Sentaurus负责器件物理计算，更新需改善多个器件指标方可接受。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。目标是校准已制造氧化物半导体晶体管的预测性TCAD模型。
  - 原文位置：Abstract；核验TXT行号 233；引文：We present the first demonstration of an agentic TCAD calibration workflow for a fabricated bottom-gate In–W–O (BG-IWO) transistor.
- 多步行动过程：yes。Agent反复比较测量与仿真、测试敏感性并选择参数/模型更新。
  - 原文位置：Abstract；核验TXT行号 233；引文：the workflow uses measurement–TCAD residuals and local sensitivity tests to select bounded parameter corrections or evaluate additional physical models
- 至少一种Agent能力：yes。LLM编排有界参数修正或增加物理模型，按器件指标接受更新。
  - 原文位置：Abstract；核验TXT行号 233；引文：the workflow uses measurement–TCAD residuals and local sensitivity tests to select bounded parameter corrections or evaluate additional physical models
- 明确科研流程角色：yes。Agent承担器件模型校准、残差分析及工艺模型开发。
  - 原文位置：Abstract；核验TXT行号 233；引文：while Sentaurus governs the device physics.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：04;09
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：09（仅归档，不覆盖其他模块）
- 模块内分类路径：04.04 能源、电子与器件材料；09.08.02 半导体器件
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

实测对象为制造的In–W–O氧化物半导体晶体管；TCAD校准直接涉及半导体材料组成和器件转移特性，建议在半导体器件09外补04.04.04。Sentaurus是工具。

### 2.3 容易混淆的边界

实测对象为制造的In–W–O氧化物半导体晶体管；TCAD校准直接涉及半导体材料组成和器件转移特性，建议在半导体器件09外补04.04.04。Sentaurus是工具。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM Agent；Tool-using Agent；Hybrid Agent

### 3.2 科研流程角色

simulation_modeling；tool_use_and_code_execution；data_analysis；evidence_assessment_and_validation

LLM控制校准流程并提出参数/模型行动；Sentaurus执行半导体器件TCAD；残差、灵敏度分析与器件指标检查充当反馈和验收层。

### 3.3 自主能力

LLM编排有界参数修正或增加物理模型，按器件指标接受更新。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

工程器件侧给出In–W–O晶体管的可转移校准模型；系统侧以残差和灵敏度把Agent参数搜索限定为可解释的迭代流程。

### 4.2 系统流程与组件

输入实测转移曲线及器件信息；运行TCAD并计算测量残差；通过局部敏感性辨别可校准参数；Agent提出有限参数修正或模型扩充；重跑并按多指标判断更新；在偏压、沟道长度及W成分测试中复核。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

以制造器件实测转移特性为参考，校准2%-W基准器件，并在不同漏极偏压、沟道长度和W成分条件下检查指标和模型转移。

### 5.2 基线、指标与结果

作者报告五次Agent建议更新后，器件多指标目标J下降14.3倍；最大阈值电压/开态电流误差分别为36.1 mV/0.022 decade及46.2 mV/0.062 decade。

### 5.3 科学贡献与证据强度

工程器件侧给出In–W–O晶体管的可转移校准模型；系统侧以残差和灵敏度把Agent参数搜索限定为可解释的迭代流程。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

相比单一曲线拟合，本文强调多指标校准与偏压/几何变化下的转移性；相比普通TCAD脚本，将残差诊断及模型修订交由Agent协同。

## 7. 局限性与风险

目前只展示一种器件平台和有限组成/几何条件；模型跨工艺泛化仍需更广数据。Agent提出更新不等同于独立发现新的器件物理。

## 8. 对综述写作的价值

可用于综述工程Agent如何把器件测量、TCAD仿真和可解释校准组合成反馈工作流。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

Agent依据晶体管测量与TCAD残差校准氧化物半导体器件模型。

### 9.2 速记版 pipeline

输入实测转移曲线及器件信息；运行TCAD并计算测量残差；通过局部敏感性辨别可校准参数；Agent提出有限参数修正或模型扩充；重跑并按多指标判断更新；在偏压、沟道长度及W成分测试中复核。

### 9.3 标注字段汇总

```text
paper_id=ASD-1053
inclusion_status=to_read
scientific_object_modules=04;09
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=09
module_taxonomy_codes=04.04;09.08.02
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。
