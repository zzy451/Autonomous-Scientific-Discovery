# Science Edge Evaluation: SEE the Missing Step Toward Real Scientific Discovery

**论文信息**

- ID：ASD-1096
- 标题：Science Edge Evaluation: SEE the Missing Step Toward Real Scientific Discovery
- 作者：Taolin Han; Yuchen Zhang; Jinghang Wang; Yun Wu; Wai Yuet Chiu; Zhaohai Li; Yifei Zhang; Jinxin Wang; Yuhao Zhou; Chen Zhao; Jiajia Li; Jiaxin Li; Qile Jin; Kewei Sun; Shuang Wu; Weiqi Zhai; Renquan Lv; Junchao Li; Ruodan Chen; Qingteng Chen; Zhibo Yang; Hu Wei; Lin Qu; Shuai Bai; Bing Zhao
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2608.06931
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1096.txt
- PDF / 本地文件路径：Reference_PDF/03_Chemical_Sciences/Han_2026_Science_Edge_Evaluation_SEE_the_Missing_Step_Toward_Real_ASD1096.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 研究对象与任务 | SEE评估化学、生物和材料实验问题；视觉工具Agent通过检查图像并使用工具获取信息，执行实验视觉材料分析。 | 全文TXT第396行；核验TXT行号 396 | Large language models (LLMs) are transforming the scientific discovery process by accelerating some of its main stages, including literature screening, computational simulation, code synthesis, and, more recently, autonomous experimentation. As these models become more capable and widely adopted, they are beginning to shape the way scientific knowledge is produced, evaluated, and applied across disciplines. This emerging role positions LLMs not merely as tools for information retrieval or text generation, but as active contributors to the broader research workflow. | 高（一手正文；非独立复现） |
| 系统输入及处理流程 | Agent接收包含实验图像/图表的科学问题，调用视觉工具提取或检查图像信息，再结合题目中的实验文字证据生成答案。 | 全文TXT第1556行；核验TXT行号 1556 | A study of generative large language model for medical research and healthcare. | 高（一手正文；非独立复现） |
| 实验或验证设置 | 作者将视觉工具Agent单独纳入评测，比较工具使用前后的答题准确率，并以专家标注答案及证据支持性进行分析。 | 全文TXT第2344行；核验TXT行号 2344 | Table 1: Inter-judge agreement between Gemini 3.1 Pro (default) and GPT-5.5 (independent). Agreement is the fraction of identically scored questions. κ\kappa is Cohen’s kappa. Δ\Delta Acc. is GPT-5.5 judge accuracy minus Gemini 3.1 Pro judge accuracy, in percentage points. The asterisk on Claude Opus 4.8 (Max) denotes safety-filtered no-response cases on biochemistry questions, counted as incorrect under the strict binary scoring protocol. | 高（一手正文；非独立复现） |
| 作者报告的贡献 | 视觉工具Agent最佳准确率达到52.7%，高于无该工具时报告的最佳模型48.7%；工具可扩展信息，但推断仍须受原始实验依据约束。 | 全文TXT第3125行；核验TXT行号 3125 | Table 7: Explicit missing-image acknowledgments in the text-only ablation. The denominator is all text-only instances for each model; the numerator includes only responses with refusal_type=no_image, i.e., responses explicitly classified as acknowledging missing image or visual evidence. Empty outputs, generation errors, generic refusals, and other non-answer cases are not counted. | 高（一手正文；非独立复现） |
| 适用范围与边界 | 这是面向化学、生物和材料科学实验材料的Agent辅助分析评测，支持科学目标、工具操作能力及研究分析角色；其范围是图像分析和证据综合，不代表自主设计或执行完整实验。 | 全文TXT第4102行；核验TXT行号 4102 | Table 9: Mean model accuracy across 19 evaluated models for each reported fine-grained discipline label. Labels with smaller sample sizes (e.g., Immunology, Physiology, Genetics) should be interpreted with care due to their limited support. | 高（一手正文；非独立复现） |
| 实际工具行动与科研角色 | 正文工具增强评测允许按步选择搜索或代码执行，反馈影响后续动作；构成局部科研证据分析Agent。 | Supplement B.5; local TXT line 2426；核验TXT行号 2426 | At each step, the model may invoke web search to gather external context or use the code interpreter to inspect and manipulate the visual input, perform computation, or verify an intermediate interpretation. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

Science Edge Evaluation（SEE）是由领域专家根据同行评审文献和实验实践构建的多模态科学任务基准，含化学、生物学和材料科学问题。作者评测19种多模态大模型，并专门评估可调用视觉工具的Agent对实验图像及证据的分析能力。最佳普通模型准确率为48.7%，视觉工具Agent最高达到52.7%；研究显示工具扩大信息来源，但仍需在原始实验依据范围内作可靠推断。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。面向真实科研文献、实验观测或可执行计算研究任务，科研目标明确。
  - 原文位置：Abstract; local TXT line 383；核验TXT行号 383；引文：Here we introduce Science Edge Evaluation (SEE), a multimodal benchmark of expert-curated questions grounded in peer-reviewed literature and experimental practice in chemistry, biology, and materials science.
- 多步行动过程：yes。正文描述多阶段研究或逐步工具调用，允许中间结果参与后续行动。
  - 原文位置：Supplement B.5; local TXT line 2426；核验TXT行号 2426；引文：At each step, the model may invoke web search to gather external context or use the code interpreter to inspect and manipulate the visual input, perform computation, or verify an intermediate interpretation.
- 至少一种Agent能力：yes。具备工具调用、状态保持和依据反馈选择后续行动的能力。
  - 原文位置：Supplement B.5; local TXT line 2426；核验TXT行号 2426；引文：The resulting text, numerical output, or processed visual observation is returned to the model and may inform its next action or final answer.
- 明确科研流程角色：yes。承担科研资料分析、计算或证据解释等局部研究角色；不要求完成整条发现闭环。
  - 原文位置：4.5 Tool-Augmented Visual-Agent Evaluation; local TXT line 861；核验TXT行号 861；引文：Models must decide which actions are relevant to the current problem, whether tool outputs are reliable, how retrieved or computed information should be integrated with the original experimental observation, and when to stop further interaction.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：03;04;06
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：03（仅归档，不覆盖其他模块）
- 模块内分类路径：03.02 基础化学；04.02 结构材料与无机材料；04.03 软物质与功能材料；06.02.02 病毒学；06.02.08 免疫学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

- 化学任务：有机化学、无机化学及分析化学实验问题
- 材料任务：金属材料、复合材料及高分子材料问题
- 生物任务：病毒/病原体及宿主相互作用、病原体结构表征与免疫学实验

### 2.3 容易混淆的边界

纳入依据是单独的工具增强视觉Agent评测：模型逐步调用搜索/代码工具，处理实验图像与中间观测并自主选择后续行动。静态问答基线不构成Agent依据；科学角色限定为固定输入的实验观测解释，不能称为端到端自主发现。03/04按二级记录，06按具体病毒/免疫学问题到三级。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签



### 3.2 科研流程角色



专家题目结合文本、图表及实验结果；模型先回答问题，视觉工具Agent可检查输入图像并调用工具获取图像信息，再将工具结果与实验文字证据结合形成回答。作者按专家标注答案评估正确性，并分析证据支持、跨学科问题及视觉证据冲突等情形。

### 3.3 自主能力

具备工具调用、状态保持和依据反馈选择后续行动的能力。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

贡献是对真实实验语境下多模态科学推理的基准评测，并包含视觉工具Agent分析实验图像、调用工具和综合证据的子评测。基准直接覆盖化学、生物和材料任务，Agent部分评估其证据限定分析能力；它是科研分析辅助评测，不应表述为已自主完成实验或产生新发现。

### 4.2 系统流程与组件

专家题目结合文本、图表及实验结果；模型先回答问题，视觉工具Agent可检查输入图像并调用工具获取图像信息，再将工具结果与实验文字证据结合形成回答。作者按专家标注答案评估正确性，并分析证据支持、跨学科问题及视觉证据冲突等情形。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

SEE含1,116道专家问题，覆盖化学、生物与材料科学及17个细分标签；对19种模型作准确率比较，并单独报告视觉工具Agent子评测。

### 5.2 基线、指标与结果

在19种多模态模型中，最佳模型报告48.7%准确率；视觉工具Agent评估中最佳准确率升至52.7%。作者同时报告通用模型平均优于科学专用模型，并指出工具增益不能保证推断始终受实验原始证据约束。

### 5.3 科学贡献与证据强度

贡献是对真实实验语境下多模态科学推理的基准评测，并包含视觉工具Agent分析实验图像、调用工具和综合证据的子评测。基准直接覆盖化学、生物和材料任务，Agent部分评估其证据限定分析能力；它是科研分析辅助评测，不应表述为已自主完成实验或产生新发现。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

相较只测试科学知识问答的基准，SEE强调多模态实验材料、跨学科证据整合和结论是否受原始实验依据支持；视觉工具子评测进一步考察工具辅助分析。

## 7. 局限性与风险

基准回答表现衡量的是给定题目上的证据分析能力，不等同于完整科研工作流或自主实验；准确率也不能单独概括推理可靠性。

## 8. 对综述写作的价值

可支持综述讨论科学多模态Agent的工具辅助分析、证据边界和专家基准验证。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

Science Edge Evaluation（SEE）是由领域专家根据同行评审文献和实验实践构建的多模态科学任务基准，含化学、生物学和材料科学问题。作者评测19种多模态大模型，并专门评估可调用视觉工具的Agent对实验图像及证据的分析能力。最佳普通模型准确率为48.7%，视觉工具Agent最高达到52.7%；研究显示工具扩大信息来源，但仍需在原始实验依据范围内作可靠推断。

### 9.2 速记版 pipeline

专家题目结合文本、图表及实验结果；模型先回答问题，视觉工具Agent可检查输入图像并调用工具获取图像信息，再将工具结果与实验文字证据结合形成回答。作者按专家标注答案评估正确性，并分析证据支持、跨学科问题及视觉证据冲突等情形。

### 9.3 标注字段汇总

```text
paper_id=ASD-1096
inclusion_status=to_read
scientific_object_modules=03;04;06
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=03
module_taxonomy_codes=03.02;04.02;04.03;06.02.02;06.02.08
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`03.02.03` 分析化学；二级：`03.02`。
- 原文位置：PDF pp.5,6,9。
- 判定：Concrete experiment/task evidence supports 03.02.03 (分析化学). Analytical Chemistry Physical Chemistry Organic Chemistry Polymer Chemistry Inorganic Chemistry Biochemistry Molecular Biology Cell Biology Structural Biology Biophysics Genetics Immunology Physiology Organic/Polymer Materials Inorganic Materials Composite Materials Metallic Materials Cross 2 disciplines Within-discipline Cross all 3 disciplines Chemistry Biology Materials Figure 2. SEE consists of 1,116 questions sp
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
