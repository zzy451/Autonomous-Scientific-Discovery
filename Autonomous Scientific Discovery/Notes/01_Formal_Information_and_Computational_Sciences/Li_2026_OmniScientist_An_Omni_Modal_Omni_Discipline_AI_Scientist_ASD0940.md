# OmniScientist: An Omni-Modal Omni-Discipline AI Scientist

**论文信息**

- ID：ASD-0940
- 标题：OmniScientist: An Omni-Modal Omni-Discipline AI Scientist
- 作者：Bobo Li; Hao Fei; Tianjie Ju; Mong-Li Lee; Wynne Hsu
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2608.13558
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-0940.txt
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Li_2026_OmniScientist_An_Omni_Modal_Omni_Discipline_AI_Scientist_ASD0940.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 研究目标/科学问题 | OmniScientist提出端到端多模态、多学科AI Scientist，从异质原始证据开展研究。系统由感知层以及构思、实验、写作三个自主Agent组成，采用确定性流程，让观察结果持续影响研究问题、实验决策和最终主张。正文包含数据标签修正及儿童胸片纹理特征等案例。 | 本地全文：ASD-0940中与研究目标/科学问题直接相关的原文句子；核验TXT行号 308 | Recent advances in foundation models have enabled AI scientists to automate increasingly complete research workflows, from hypothesis generation and code execution to manuscript preparation. Yet workflow coverage alone does not provide access to the full evidence on which scientific discovery depends. Existing systems typically reason over text, code, labels, or precomputed summaries, leaving scientifically decisive spatial, temporal, cross-channel, and procedural relations unavailable to the agent. We introduce OmniScientist, an end-to-end, omni-modal AI scientist that conducts multidisciplinary research directly from heterogeneous raw evidence. A perception layer and 3 autonomous agents for ideation, experiment, and writeup operate within a deterministic pipeline, allowing observations to shape research questions, experimental decisions, and final claims throughout the research lifecycle. By running idea, rigour, and claim checks in code, the system enforces novelty screening, statistical validity, execution provenance, and numerical traceability. We evaluate OmniScientist on 36 real-data cases spanning 5 discipline families, 4 families of scientific evidence, and modalities including images, signals, audio, video, 3-D structures, trajectories, tables, formulae, and graphs. The system completes the full path from raw data to a compiled manuscript in all 36 cases and achieves a mean overall paper score of 6.36.3 with the reference reasoning backbone. In paired comparisons against a blind variant that receives only precomputed scalar features, direct perception improves all 7 evaluation dimensions and wins 85%85\% of head-to-head judgments. These results show that lifecycle-wide perception is essential to the evidence-grounded scientific discovery and provides a practical path toward broadly capable AI scientists. | 高（一手正文；非独立复现） |
| 多步行动/研究流程 | 系统解析异质证据并生成问题，安排实验及分析，再形成报告；流程包含新颖性、统计、来源追溯和主张检查。 | 本地全文：ASD-0940中与多步行动/研究流程直接相关的原文句子；核验TXT行号 308 | A perception layer and 3 autonomous agents for ideation, experiment, and writeup operate within a deterministic pipeline, allowing observations to shape research questions, experimental decisions, and final claims throughout the research lifecycle. | 高（一手正文；非独立复现） |
| Agent实现与能力 | OmniScientist以多模态感知层接收原始证据，并由ideation、experiment和writeup三个Agent协同完成研究流程。 | 本地全文：ASD-0940中与Agent实现与能力直接相关的原文句子；核验TXT行号 4619 | While the previous case study demonstrated the system’s ability to correct dataset labels, this second evaluation illustrates its capacity to establish a novel positive finding directly from raw visual data. The agent received paediatric frontal chest radiographs carrying only a normal or pneumonia label, with no precomputed features. Reading the radiographs directly, it observed that pneumonic lung fields were not uniformly brighter but unevenly mottled, with dense patches sitting beside clear ones (Figure 12). It converted that observation into a measurable quantity, the spatial dispersion of a sliding-window local Shannon-entropy map, and pre-specified the hypothesis that this patchiness separates the two labels independently of the overall entropy level. | 高（一手正文；非独立复现） |
| 实验任务与验证设置 | 论文以多个跨模态学科案例评估，包括数据标签纠正和儿科胸部X光纹理签名发现；案例应按具体数据与验证流程解读。 | 本地全文：ASD-0940中与实验任务与验证设置直接相关的原文句子；核验TXT行号 4620 | The agent received paediatric frontal chest radiographs carrying only a normal or pneumonia label, with no precomputed features. | 高（一手正文；非独立复现） |
| 作者报告的结果/贡献 | 作者展示系统在案例中纠正数据标签并提出胸片纹理相关发现；这些案例证据不能单独确立临床效用或广泛学科通用性。 贡献是把多模态原始证据感知接入从问题形成到实验和写作的自动科研流程。 | 本地全文中包含该原句的位置；核验TXT行号 4621 | Reading the radiographs directly, it observed that pneumonic lung fields were not uniformly brighter but unevenly mottled, with dense patches sitting beside clear ones (Figure 12). | 高（一手正文；非独立复现） |

## 0. 摘要翻译

OmniScientist提出端到端多模态、多学科AI Scientist，从异质原始证据开展研究。系统由感知层以及构思、实验、写作三个自主Agent组成，采用确定性流程，让观察结果持续影响研究问题、实验决策和最终主张。正文包含数据标签修正及儿童胸片纹理特征等案例。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。OmniScientist提出端到端多模态、多学科AI Scientist，从异质原始证据开展研究。系统由感知层以及构思、实验、写作三个自主Agent组成，采用确定性流程，让观察结果持续影响研究问题、实验决策和最终主张。正文包含数据标签修正及儿童胸片纹理特征等案例。
  - 原文位置：本地全文：ASD-0940中与研究目标/科学问题直接相关的原文句子；核验TXT行号 308；引文：Recent advances in foundation models have enabled AI scientists to automate increasingly complete research workflows, from hypothesis generation and code execution to manuscript preparation. Yet workflow coverage alone does not provide access to the full evidence on which scientific discovery depends. Existing systems typically reason over text, code, labels, or precomputed summaries, leaving scientifically decisive spatial, temporal, cross-channel, and procedural relations unavailable to the agent. We introduce OmniScientist, an end-to-end, omni-modal AI scientist that conducts multidisciplinary research directly from heterogeneous raw evidence. A perception layer and 3 autonomous agents for ideation, experiment, and writeup operate within a deterministic pipeline, allowing observations to shape research questions, experimental decisions, and final claims throughout the research lifecycle. By running idea, rigour, and claim checks in code, the system enforces novelty screening, statistical validity, execution provenance, and numerical traceability. We evaluate OmniScientist on 36 real-data cases spanning 5 discipline families, 4 families of scientific evidence, and modalities including images, signals, audio, video, 3-D structures, trajectories, tables, formulae, and graphs. The system completes the full path from raw data to a compiled manuscript in all 36 cases and achieves a mean overall paper score of 6.36.3 with the reference reasoning backbone. In paired comparisons against a blind variant that receives only precomputed scalar features, direct perception improves all 7 evaluation dimensions and wins 85%85\% of head-to-head judgments. These results show that lifecycle-wide perception is essential to the evidence-grounded scientific discovery and provides a practical path toward broadly capable AI scientists.
- 多步行动过程：yes。系统解析异质证据并生成问题，安排实验及分析，再形成报告；流程包含新颖性、统计、来源追溯和主张检查。
  - 原文位置：本地全文：ASD-0940中与多步行动/研究流程直接相关的原文句子；核验TXT行号 308；引文：A perception layer and 3 autonomous agents for ideation, experiment, and writeup operate within a deterministic pipeline, allowing observations to shape research questions, experimental decisions, and final claims throughout the research lifecycle.
- 至少一种Agent能力：yes。OmniScientist以多模态感知层接收原始证据，并由ideation、experiment和writeup三个Agent协同完成研究流程。
  - 原文位置：本地全文：ASD-0940中与Agent实现与能力直接相关的原文句子；核验TXT行号 4619；引文：While the previous case study demonstrated the system’s ability to correct dataset labels, this second evaluation illustrates its capacity to establish a novel positive finding directly from raw visual data. The agent received paediatric frontal chest radiographs carrying only a normal or pneumonia label, with no precomputed features. Reading the radiographs directly, it observed that pneumonic lung fields were not uniformly brighter but unevenly mottled, with dense patches sitting beside clear ones (Figure 12). It converted that observation into a measurable quantity, the spatial dispersion of a sliding-window local Shannon-entropy map, and pre-specified the hypothesis that this patchiness separates the two labels independently of the overall entropy level.
- 明确科研流程角色：yes。论文以多个跨模态学科案例评估，包括数据标签纠正和儿科胸部X光纹理签名发现；案例应按具体数据与验证流程解读。
  - 原文位置：本地全文：ASD-0940中与实验任务与验证设置直接相关的原文句子；核验TXT行号 4620；引文：The agent received paediatric frontal chest radiographs carrying only a normal or pneumonia label, with no precomputed features.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：01;02;03;04;05;06;07;08;09;10
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：01（仅归档，不覆盖其他模块）
- 模块内分类路径：01.01 数学；01.02 计算机科学；02.01 天文学与天体物理学；03.01 化学总论与化学方法；04.01 材料基础；05.01 地球科学基础；05.04 地理科学与空间信息；06.01.02 细胞生物学；06.03.01 基因组学；07.01.04 病理学；08.01.06 植物保护；09.02 机械与制造工程；10.04 交通运输科学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

对象模块与代码沿用输入审计记录（01, 02, 03, 04, 05, 06, 07, 08, 09, 10；01.01, 01.02, 02.01, 03.01, 04.01, 05.01, 05.04, 06.01.02, 06.03.01, 07.01.04, 08.01.06, 09.02, 10.04）；是否纳入与对象分类分开判断。

### 2.3 容易混淆的边界

对象模块与代码沿用输入审计记录（01, 02, 03, 04, 05, 06, 07, 08, 09, 10；01.01, 01.02, 02.01, 03.01, 04.01, 05.01, 05.04, 06.01.02, 06.03.01, 07.01.04, 08.01.06, 09.02, 10.04）；是否纳入与对象分类分开判断。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

自主科研Agent

### 3.2 科研流程角色

科研问题处理；多步行动或评测

OmniScientist以多模态感知层接收原始证据，并由ideation、experiment和writeup三个Agent协同完成研究流程。

### 3.3 自主能力

OmniScientist以多模态感知层接收原始证据，并由ideation、experiment和writeup三个Agent协同完成研究流程。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

贡献是把多模态原始证据感知接入从问题形成到实验和写作的自动科研流程。

### 4.2 系统流程与组件

系统解析异质证据并生成问题，安排实验及分析，再形成报告；流程包含新颖性、统计、来源追溯和主张检查。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

论文以多个跨模态学科案例评估，包括数据标签纠正和儿科胸部X光纹理签名发现；案例应按具体数据与验证流程解读。

### 5.2 基线、指标与结果

作者展示系统在案例中纠正数据标签并提出胸片纹理相关发现；这些案例证据不能单独确立临床效用或广泛学科通用性。

### 5.3 科学贡献与证据强度

贡献是把多模态原始证据感知接入从问题形成到实验和写作的自动科研流程。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

论文以“OmniScientist: An Omni-Modal Omni-Discipline AI Scientist”对应的研究任务为对象，具体与哪些既有系统或基准比较，应结合其正文相关工作和实验基线判断；不把工具名称直接视为科学对象。

## 7. 局限性与风险

跨学科主张主要由论文案例支持；医疗影像发现仍需独立队列与专业临床验证。

## 8. 对综述写作的价值

可用于综述“OmniScientist: An Omni-Modal Omni-Discipline AI Scientist”所涉及的Agent任务、研究流程和验证方式；其证据边界为本论文实际报告的任务集与实验结果。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

OmniScientist将多模态证据感知连接到构思、实验和写作Agent。

### 9.2 速记版 pipeline

系统解析异质证据并生成问题，安排实验及分析，再形成报告；流程包含新颖性、统计、来源追溯和主张检查。

### 9.3 标注字段汇总

```text
paper_id=ASD-0940
inclusion_status=to_read
scientific_object_modules=01;02;03;04;05;06;07;08;09;10
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=01
module_taxonomy_codes=01.01;01.02;02.01;03.01;04.01;05.01;05.04;06.01.02;06.03.01;07.01.04;08.01.06;09.02;10.04
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`01.01.09` 统计学；二级：`01.01`。
- 原文位置：PDF pp.6,17,18 3.2 demonstration suite; Table 8 symbolic regression results。
- 判定：主归档01.01内有明确参数估计方差/噪声与取样范围验证；以统计学作为primary，比将通用框架直接归空更贴合实际结果。
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
