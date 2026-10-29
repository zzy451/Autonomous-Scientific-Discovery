# Agentic Active Learning Meets Visual Embeddings: Finding Anomalies among 370 000 Variable Stars from ASAS-SN

**论文信息**

- ID：ASD-1065
- 标题：Agentic Active Learning Meets Visual Embeddings: Finding Anomalies among 370 000 Variable Stars from ASAS-SN
- 作者：Pesta, Milan; Ting, Yuan-Sen
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2608.23688
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1065.txt
- PDF / 本地文件路径：Reference_PDF/02_Physics_Astronomy_and_Cosmic_Sciences/Milan_2026_Agentic_Active_Learning_Meets_Visual_Embeddings_Finding_Anomalies_among_ASD1065.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 对象和纳入 | 周期变星异常筛查。 | TXT line 299；核验TXT行号 299 | We present an active learning framework for detecting anomalies in samples of periodic variable stars, with the vetting delegated to multimodal large language model agents. | 高（一手正文；非独立复现） |
| 数据规模 | 作者使用ASAS-SN周期变星样本。 | TXT line 394；核验TXT行号 394 | To assemble our sample of variable stars, we queried the Sky Patrol V2.0 database through the pyasassn Python client [20] and performed an inner join of the stellar_main table with aavsovsx, corresponding to the International Variable Star Index (VSX)33 | 高（一手正文；非独立复现） |
| 方法 | DINOv2视觉嵌入与Isolation Forest初排，Agent迭代标注。 | TXT line 414；核验TXT行号 414 | First, we render raw ASAS-SN time series as phase-folded light curve images and embed them with a pre-trained vision model (Section III.1), then we establish a baseline anomaly ranking with class-conditional isolation forests trained on these embeddings (Section III.2). | 高（一手正文；非独立复现） |
| 结果 | 发现异常候选并由多Agent共识筛选。 | TXT line 1646；核验TXT行号 1646 | Applied to over 370 000370\,000 periodic variable stars from ASAS-SN Sky Patrol V2.0, the pipeline identified 2424 anomalies and 153153 potentially interesting objects among the 5 1005\,100 sources labeled by the agents (∼1%{\sim}1\% of the full sample) across 5050 active learning iterations and a single logistic regression step. | 高（一手正文；非独立复现） |
| 限制 | 表示形式限于周期相位折叠光变曲线且Agent无外部工具。 | TXT line 1601；核验TXT行号 1601 | A second major limitation is the lack of external tools available to the agents during evaluation. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

本文提出结合视觉嵌入与Agent主动学习的变星异常筛查方法。DINOv2将相位折叠光变曲线编码，Isolation Forest提供初始排序，多模态LLM Agent反复审阅高排名候选并传播标签，最终以多Agent共识过滤伪异常。方法应用于ASAS-SN约37万周期变星并产生新的候选异常。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。在ASAS-SN变星数据中筛查异常天体。
  - 原文位置：TXT line 299；核验TXT行号 299；引文：We present an active learning framework for detecting anomalies in samples of periodic variable stars, with the vetting delegated to multimodal large language model agents.
- 多步行动过程：yes。嵌入、异常排序、Agent标注、标签传播及复核构成迭代流程。
  - 原文位置：TXT line 299；核验TXT行号 299；引文：The agents iteratively review the light-curve images of the top-ranked candidates and assign relevance scores, which are propagated through the embedding space to prioritize the next targets.
- 至少一种Agent能力：yes。多模态LLM Agent对光变曲线图像进行相关性标注。
  - 原文位置：TXT line 365；核验TXT行号 365；引文：Our agents are deliberately minimal, with no memory across evaluations, access to external tools, or ability to plan their own actions.
- 明确科研流程角色：yes。Agent承担大规模巡天异常候选体的人类审阅替代与复核。
  - 原文位置：TXT line 414；核验TXT行号 414；引文：Finally, we subject all anomaly candidates flagged by the agents in the previous steps to a multi-agent consensus review (Section III.5), producing our final catalog of anomalies and potentially interesting objects.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：02
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：02（仅归档，不覆盖其他模块）
- 模块内分类路径：02.01 天文学与天体物理学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

对象为ASAS-SN变星与天文异常体，属天文学02；视觉模型是方法而非主要对象。

### 2.3 容易混淆的边界

对象为ASAS-SN变星与天文异常体，属天文学02；视觉模型是方法而非主要对象。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

multimodal_llm_annotator

### 3.2 科研流程角色

anomaly_detection；candidate_triage

Gemini 3 Flash多模态LLM充当独立标注员，无跨轮记忆、外部工具或自主计划；五个Agent执行共识复核。

### 3.3 自主能力

多模态LLM Agent对光变曲线图像进行相关性标注。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

科学贡献是发现和整理变星异常候选；系统贡献是将视觉嵌入、主动学习与LLM审阅组合扩展至巡天规模。

### 4.2 系统流程与组件

输入为ASAS-SN周期变星光变曲线；将其绘为图像并用DINOv2嵌入，以类别条件Isolation Forest排序；Agent审阅候选并给分，标签在嵌入邻域传播；逻辑回归扩展检索，最后多Agent共识筛选输出目录。 这一工作流的实施细节、输入输出和验证范围均按原文所报告内容理解，不将展示案例外推为普遍能力。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

对373646个周期变星运行流程，以人工定义的异常相关标签、候选复核及已知/新报告对象分析效果；评估视觉嵌入和主动学习环节。

### 5.2 基线、指标与结果

作者报告识别24个异常，其中18个此前未报告，另有153个潜在有趣对象。

### 5.3 科学贡献与证据强度

科学贡献是发现和整理变星异常候选；系统贡献是将视觉嵌入、主动学习与LLM审阅组合扩展至巡天规模。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

延伸传统Isolation Forest与人工主动学习异常审核，探索自然图像预训练嵌入用于光变形态。

## 7. 局限性与风险

- author_stated：依赖周期相位折叠图像，不易延伸到非周期源/暂现源；Agent无外部工具，依赖专有LLM且受API限制。
- reviewer_inference：Agent是受提示的标注员而非自主规划者，候选仍需后续天文确认。

## 8. 对综述写作的价值

可支撑科研Agent用于大规模天文候选分流，同时区分标注Agent与自主发现系统。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

主动学习Agent协助从ASAS-SN周期变星中筛出异常候选。

### 9.2 速记版 pipeline

输入为ASAS-SN周期变星光变曲线；将其绘为图像并用DINOv2嵌入，以类别条件Isolation Forest排序；Agent审阅候选并给分，标签在嵌入邻域传播；逻辑回归扩展检索，最后多Agent共识筛选输出目录。 这一工作流的实施细节、输入输出和验证范围均按原文所报告内容理解，不将展示案例外推为普遍能力。

### 9.3 标注字段汇总

```text
paper_id=ASD-1065
inclusion_status=to_read
scientific_object_modules=02
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=02
module_taxonomy_codes=02.01
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`02.01.03` 恒星与恒星演化；二级：`02.01`。
- 原文位置：PDF p.1。
- 判定：ASAS-SN周期变星异常发现，恒星与演化。
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
