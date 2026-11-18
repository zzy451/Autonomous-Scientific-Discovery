# An AI-powered self-driving microscope for low-cost acute leukemia detection

**论文信息**

- ID：ASD-1014
- 标题：An AI-powered self-driving microscope for low-cost acute leukemia detection
- 作者：Ethan S. Yan; Shenghuan Sun; Zhanghan Yin; Ali Kamali; Jacob Van Cleave; Irem S. Isgor; Brenda Fried; Cesar Colorado-Jimenez; Deepika Dilip; Jeeyeon Baik; Allyne Manzo; Sean Paulsen; Siddharth Singi; Scott Drapeau; Ozgur Can Eren; Joanne K. Chun; Aijazuddin Syed; Anthony Cardillo; Melissa Pulitzer; Maly Fenelus; David Kim; Jamal Benhamida; Dianna Ng; Orly Ardon; Mikhael Roshal; Ahmet Dogan; Chad Vanderbilt; Khawaja H. Bilal; Gregory M. Goldgof
- 年份：2026
- 来源 / venue：Nature Communications
- DOI / arXiv / URL：https://doi.org/10.1038/s41467-026-77130-x
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1014.txt
- PDF / 本地文件路径：全文已缓存；PDF尚未归档，详见资料清单
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| scientific object/task | 目标是低成本自驱显微镜白血病检测，解决全玻片扫描设备昂贵、资源有限地区难以部署的问题。 | Full text, extracted character offset 270；核验TXT行号 1 | We present ALLocate, a low-cost, artificial intelligence-powered microscope plugin that enables self-driving microscopy for leukemia detection | 高（一手正文；非独立复现） |
| method or agent workflow | 系统从ROI定位到细胞检测再到整张玻片诊断和定量，组成逐级处理的诊断流程。 | Full text, extracted character offset 553；核验TXT行号 1 | We evaluate its robustness at three levels: region-of-interest identification, cell detection, and end-to-end slide-level diagnosis | 高（一手正文；非独立复现） |
| evaluation design | 评估使用超过11,000个标注区域及130,000个细胞，并以多机构独立队列和165张实体骨髓涂片验证。 | Full text, extracted character offset 686；核验TXT行号 1 | The system is trained and evaluated using more than 11,000 annotated regions and 130,000 annotated cells and is further validated using independent multi-institutional cohorts, including 165 physical bone marrow smear slides | 高（一手正文；非独立复现） |
| reported result | ALLocate在玻片级诊断达到88%准确率，无需全玻片扫描仪。 | Full text, extracted character offset 1137；核验TXT行号 1 | accuracy for slide-level diagnosis on glass slides | 高（一手正文；非独立复现） |
| limitation / boundary | 现有硬件可自动进行XY扫描但没有自动Z轴聚焦，仍可能需要人工输入以避免区域失焦。 | Full text, extracted character offset 32371；核验TXT行号 1 | it lacks automated Z-axis focusing, which, without human input, may result in focal variability across regions | 高（一手正文；非独立复现） |

## 0. 摘要翻译

本文介绍低成本自驱显微镜系统ALLocate，用于骨髓涂片急性白血病检测。作者分别评价视野区域定位、原始细胞检测和玻片级诊断，使用超过11,000个标注区域、130,000个细胞及多机构队列，并在165张实体骨髓涂片上验证。区域定位AUC超过0.99，细胞检测mAP@0.5为0.90，实体玻片诊断准确率为88%。结果显示无需全玻片扫描仪也可完成端到端图像分析，但仍需更大规模前瞻性临床验证。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。研究针对骨髓涂片中的急性白血病识别，目标兼顾诊断准确性与低成本部署。
  - 原文位置：Full text, extracted character offset 270；核验TXT行号 1；引文：We present ALLocate, a low-cost, artificial intelligence-powered microscope plugin that enables self-driving microscopy for leukemia detection
- 多步行动过程：yes。从ROI定位、原始细胞检测到全片诊断和定量是明确的多阶段处理链。
  - 原文位置：Full text, extracted character offset 553；核验TXT行号 1；引文：We evaluate its robustness at three levels: region-of-interest identification, cell detection, and end-to-end slide-level diagnosis
- 至少一种Agent能力：yes。系统驱动显微镜并处理数字及实体玻片，输出细胞和全片层面的诊断结果。
  - 原文位置：Full text, extracted character offset 553；核验TXT行号 1；引文：We evaluate its robustness at three levels: region-of-interest identification, cell detection, and end-to-end slide-level diagnosis
- 明确科研流程角色：yes。ALLocate将自动显微成像及病理分析用于骨髓涂片筛查这一实际诊断工作流。
  - 原文位置：Full text, extracted character offset 270；核验TXT行号 1；引文：We present ALLocate, a low-cost, artificial intelligence-powered microscope plugin that enables self-driving microscopy for leukemia detection

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：07
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：07（仅归档，不覆盖其他模块）
- 模块内分类路径：07.01.04 病理学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

归入06.01血液病理与白血病诊断；结果是医学图像算法和设备流程验证，临床部署价值尚不能由离线准确率单独确定。

### 2.3 容易混淆的边界

归入06.01血液病理与白血病诊断；结果是医学图像算法和设备流程验证，临床部署价值尚不能由离线准确率单独确定。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM Agent；Tool-using Agent

### 3.2 科研流程角色

tool_use_and_code_execution；data_analysis；evidence_assessment_and_validation

ALLocate把低成本显微镜插件、自动视野定位与细胞检测模型组合成自驱诊断流程，从骨髓涂片图像采集到玻片级急性白血病判断。

### 3.3 自主能力

系统驱动显微镜并处理数字及实体玻片，输出细胞和全片层面的诊断结果。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

贡献是将自动显微成像和多层级白血病图像分析整合到常规显微镜上，降低对昂贵全玻片扫描设备的依赖。

### 4.2 系统流程与组件

系统处理ROI识别、blast细胞检测和玻片诊断三个层级；训练/评估使用超过11,000个标注区域和130,000个标注细胞，并在多机构队列及165张实体骨髓涂片上测试。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

作者分别报告ROI的AUC、细胞检测mAP@0.5和实体玻片诊断准确率，且含独立多机构验证；证据支持图像任务性能，不等同于完整临床效用试验。

### 5.2 基线、指标与结果

ROI识别AUC超过0.99，细胞检测mAP@0.5为0.90，实体玻片上的玻片级诊断准确率为88%，无需全玻片扫描仪。结果支持低成本自动化的技术可行性。

### 5.3 科学贡献与证据强度

贡献是将自动显微成像和多层级白血病图像分析整合到常规显微镜上，降低对昂贵全玻片扫描设备的依赖。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

相较依赖高成本全玻片扫描器的AI病理流程，ALLocate通过显微镜插件采集并自动定位；与单纯细胞分类器相比，它评估端到端玻片任务。

## 7. 局限性与风险

性能受硬件扫描范围、涂片质量、病例组成及标注标准影响；165张实体玻片仍不足以证明跨机构常规部署的诊断效益，需前瞻性临床评估。

## 8. 对综述写作的价值

可用于比较低成本自驱显微镜在ROI、细胞和玻片诊断三个层级上的验证强度。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

ALLocate把自动视野定位、白血病细胞识别和玻片诊断整合到普通显微镜插件，并在多机构图像和实体骨髓涂片上测试。实体玻片诊断准确率为88%，支持其技术可行性；临床部署效益仍需前瞻性验证。

### 9.2 速记版 pipeline

系统处理ROI识别、blast细胞检测和玻片诊断三个层级；训练/评估使用超过11,000个标注区域和130,000个标注细胞，并在多机构队列及165张实体骨髓涂片上测试。

### 9.3 标注字段汇总

```text
paper_id=ASD-1014
inclusion_status=to_read
scientific_object_modules=07
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=07
module_taxonomy_codes=07.01.04
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O3 新实例 | 新玻片诊断可由专家核对 | “165 physical bone marrow smear slides” · L23 |
| 验证强度 | V2 计算/仿真/回顾性 | 专家对诊断结论核对 | “accuracy for slide-level diagnosis on glass slides” · L24 |
| 系统自主性 | L2 闭环执行者 | 系统自主扫描并分析多层级 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
