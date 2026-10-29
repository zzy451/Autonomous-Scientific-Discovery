# Vision-Language Agents for Active Perception in Optics Laboratories

**论文信息**

- ID：ASD-1062
- 标题：Vision-Language Agents for Active Perception in Optics Laboratories
- 作者：Lopez, Ryan; Vaidya, Sachin; Choi, Seou; Landers, Serena; Soljačić, Marin
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2609.32918
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1062.txt
- PDF / 本地文件路径：Reference_PDF/02_Physics_Astronomy_and_Cosmic_Sciences/Ryan_2026_Vision_Language_Agents_for_Active_Perception_in_Optics_Laboratories_ASD1062.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 实验装置 | 真实Michelson干涉仪包括633nm HeNe激光、分束器、两面电控镜及相机。 | TXT line 390；核验TXT行号 390 | The Michelson interferometer setup consists of a HeNe laser at 633nm, a beamsplitter, two motorized mirrors, and a beam detection camera. | 高（一手正文；非独立复现） |
| 验证设计 | 每项实验使用十种固定的初始失准光路配置。 | TXT line 368；核验TXT行号 368 | For each experiment, we evaluate ten fixed initial misaligned optical configurations. | 高（一手正文；非独立复现） |
| 主动感知 | Agent固定其余控制量并改变一面镜子的单轴，以识别哪个可见光束响应。 | TXT line 436；核验TXT行号 436 | Starting from two separated spots, the agent varied one axis of the first mirror while holding the remaining controls fixed and identified which visible beam responded. | 高（一手正文；非独立复现） |
| 定量结果 | 作者报告三种模型的终端平均对准误差，图像分辨率相同。 | TXT line 429；核验TXT行号 429 | The mean terminal alignment error was 75 pixels for GPT-5.6 Sol, 161 pixels for Gemini 3.5 Flash, and 182 pixels for Claude Sonnet 5, for images of size 1920×10801920\times 1080 pixels. | 高（一手正文；非独立复现） |
| 错误分析 | Gemini部分低成功率运行主要受视觉解释错误影响；此句不单独支持仿真比较。 | TXT line 498；核验TXT行号 498 | The least successful Gemini 3.5 Flash runs were dominated by errors in visual interpretation. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

本文研究视觉语言Agent在实验室光学系统中主动感知并执行光路对准。Agent读取相机图像并控制电机调整反射镜，在Michelson干涉仪等任务中进行真实实验和仿真测试。不同模型成功率不同，且模型自报完成并不可靠。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。在真实光学实验平台完成光路对准。
  - 原文位置：TXT line 354；核验TXT行号 354；引文：We evaluate vision-language models as closed-loop controllers for three representative optical-alignment tasks: a Michelson interferometer, a two-mirror cavity, and a four-mirror relay.
- 多步行动过程：yes。根据相机观察多轮调整电机并重新观测。
  - 原文位置：TXT line 361；核验TXT行号 361；引文：The resulting control loop also naturally includes physical nonidealities such as motor slip, backlash, drift, and imperfect repeatability in camera placement, which the agent has to accommodate through subsequent visual observations.
- 至少一种Agent能力：yes。视觉模型控制镜面并判断光路状态。
  - 原文位置：TXT line 436；核验TXT行号 436；引文：Starting from two separated spots, the agent varied one axis of the first mirror while holding the remaining controls fixed and identified which visible beam responded.
- 明确科研流程角色：yes。承担光学实验平台操作及实验状态判断。
  - 原文位置：TXT line 390；核验TXT行号 390；引文：In this first experiment, we test whether a VLM-based agent can visually interpret an optical state and learn how its available actuators affect that state through interaction.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：02
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：02（仅归档，不覆盖其他模块）
- 模块内分类路径：02.02 物理学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

对象为实验光学系统，归入物理科学02，而非一般视觉问答。

### 2.3 容易混淆的边界

对象为实验光学系统，归入物理科学02，而非一般视觉问答。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

vision_language_agent

### 3.2 科研流程角色

instrument_operation；active_perception

视觉语言模型读取相机图像，调用镜面电机控制接口，并依据新图像反馈决定后续调整。

### 3.3 自主能力

视觉模型控制镜面并判断光路状态。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

系统贡献是VLM图像反馈控制光学器件；科学贡献是验证实验室光路对准能力。

### 4.2 系统流程与组件

输入对准目标后，Agent观察光斑，推断需调整的镜面并执行电机动作，再次观察并迭代；论文测试Michelson干涉仪和多镜系统，并比较现场实验与仿真。 这一工作流的实施细节、输入输出和验证范围均按原文所报告内容理解，不将展示案例外推为普遍能力。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

多个模型在真实干涉仪和隐藏初始配置上测试，另将仿真与实验行为比较；人工检查终点图像。

### 5.2 基线、指标与结果

Michelson任务中GPT成功9/10，Gemini 6/10，Qwen 0/10；另一配置中GPT 9/10、Gemini 10/10。

### 5.3 科学贡献与证据强度

系统贡献是VLM图像反馈控制光学器件；科学贡献是验证实验室光路对准能力。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

与仿真优化策略比较，并在相同提示及接口下评估不同VLM。

## 7. 局限性与风险

- author_stated：模型自报完成不能作为可靠对准判据。
- reviewer_inference：实验任务和光学构型有限，不能推论复杂光学实验的普适性。

## 8. 对综述写作的价值

可说明真实实验Agent须依据外部测量判定成功，并揭示模型差异。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

视觉语言Agent以图像反馈控制镜面完成部分真实光学对准任务。

### 9.2 速记版 pipeline

输入对准目标后，Agent观察光斑，推断需调整的镜面并执行电机动作，再次观察并迭代；论文测试Michelson干涉仪和多镜系统，并比较现场实验与仿真。 这一工作流的实施细节、输入输出和验证范围均按原文所报告内容理解，不将展示案例外推为普遍能力。

### 9.3 标注字段汇总

```text
paper_id=ASD-1062
inclusion_status=to_read
scientific_object_modules=02
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=02
module_taxonomy_codes=02.02
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`02.02.09` 光学；二级：`02.02`。
- 原文位置：PDF p.1。
- 判定：Michelson干涉仪与光学腔的真实对准实验，归光学。
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
