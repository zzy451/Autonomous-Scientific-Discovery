# A RAG-enhanced multi-agent LLM/VLM framework for auditable and region-aware structural health monitoring of a historic masonry structure

**论文信息**

- ID：ASD-1088
- 标题：A RAG-enhanced multi-agent LLM/VLM framework for auditable and region-aware structural health monitoring of a historic masonry structure
- 作者：Kemal Hacıefendioğlu; Volkan Kahya; Tunahan Aslan
- 年份：2026
- 来源 / venue：Scientific Reports
- DOI / arXiv / URL：https://www.nature.com/articles/s41598-026-57424-2
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1088.txt
- PDF / 本地文件路径：Reference_PDF/09_Engineering_and_Industrial_Technology_Sciences/Hacefendioglu_2026_A_RAG_enhanced_multi_agent_LLM_VLM_framework_for_ASD1088.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 科学目标 | 工作聚焦历史砌体结构的非破坏性监测与解释。 | Abstract；核验TXT行号 1 | Historic masonry structures require monitoring workflows that are non-destructive, interpretable, and robust to field variability. | 高（一手正文；非独立复现） |
| 具体工程对象 | 案例是单座历史砌体宣礼塔，协调信号、视觉及融合分析。 | Abstract, case description；核验TXT行号 1 | single historic masonry minaret case study, in which a manager–orchestrator coordinates signal analysis, visual analysis, and cross-modal fusion. | 高（一手正文；非独立复现） |
| 方法流程 | 四个传感器数据经过预处理、健康基线训练和后续测量评估。 | Abstract；核验TXT行号 1 | Vibration data from four sensors installed on this minaret are processed through a reproducible pipeline that includes data cleaning, PSD-based baseline characterisation, adaptive windowing, robust normalisation, and anomaly screening with a 1D convolutional autoencoder trained on healthy reference data (Measurements 1–12), followed by evaluation on Measurements 13–20. | 高（一手正文；非独立复现） |
| Agent能力 | LLM、VLM和融合Agent通过RAG记忆协调多模态证据。 | Abstract；核验TXT行号 1 | A three-agent decision layer (Agent A: LLM+RAG, Agent B: VLM+RAG, Agent C: fusion + RAG) reconciles agreements and conflicts between signal- and image-derived evidence | 高（一手正文；非独立复现） |
| 验证边界 | 作者把本研究限定为单案例内的有/无RAG比较，而非独立准确率证明。 | Methods/Application, comparison framing；核验TXT行号 1 | The comparison is used to examine how retrieval-grounded context changes the interpretation of anomaly and visual-risk evidence, rather than to claim independently verified damage classification accuracy. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

论文在一座历史砌体宣礼塔上演示可审计的结构健康监测工作流。系统组合四个传感器的振动分析、传感器关系定位、巡检图像的视觉语言模型分析，以及包含几何、材料、动力基线和检查规程的检索记忆；三个Agent对信号和图像证据进行融合，输出区域级风险解释。作者比较有无RAG的单案例结果，强调该工作支持巡检优先级判断，而不是宣称经独立验证的损伤诊断准确率。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。在一座历史砌体宣礼塔案例中进行结构健康监测与区域风险解释。
  - 原文位置：Abstract opening；核验TXT行号 1；引文：Historic masonry structures require monitoring workflows that are non-destructive, interpretable, and robust to field variability.
- 多步行动过程：yes。从振动信号筛查、传感器关系定位、图像分析到跨模态融合和风险制图。
  - 原文位置：Abstract, method description；核验TXT行号 1；引文：Vibration data from four sensors installed on this minaret are processed through a reproducible pipeline that includes data cleaning, PSD-based baseline characterisation, adaptive windowing, robust normalisation, and anomaly screening with a 1D convolutional autoencoder trained on healthy reference data (Measurements 1–12), followed by evaluation on Measurements 13–20.
- 至少一种Agent能力：yes。三Agent使用检索记忆解释信号/图像，并协调冲突证据。
  - 原文位置：Abstract, agent decision layer；核验TXT行号 1；引文：A three-agent decision layer (Agent A: LLM+RAG, Agent B: VLM+RAG, Agent C: fusion + RAG) reconciles agreements and conflicts between signal- and image-derived evidence
- 明确科研流程角色：yes。为历史建筑巡检与保护提供结构健康监测的风险分区决策支持。
  - 原文位置：Introduction, Study aim and contributions；核验TXT行号 1；引文：The central objective is to move from anomaly flagging to context-aware, zone-level risk interpretation that supports inspection planning and conservation decisions.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：09
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：09（仅归档，不覆盖其他模块）
- 模块内分类路径：09.05.02 结构工程
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

归09.05.02结构工程：实验对象是历史建筑结构的健康状态和区域损伤风险。文化遗产背景只是案例语境，不形成11类人文研究对象。

### 2.3 容易混淆的边界

归09.05.02结构工程：实验对象是历史建筑结构的健康状态和区域损伤风险。文化遗产背景只是案例语境，不形成11类人文研究对象。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM Agent；Multi-Agent System；Retrieval-augmented Agent

### 3.2 科研流程角色

data_analysis；result_interpretation；evidence_assessment_and_validation

Manager-orchestrator协调信号分析Agent、视觉分析Agent和融合Agent；检索记忆提供该塔结构背景，输出包含JSON记录、传感器/图像发现、叙述报告和风险图。

### 3.3 自主能力

三Agent使用检索记忆解释信号/图像，并协调冲突证据。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

工程贡献是将全局异常、关系定位、区域映射和现场图像置于同一可追溯决策支持链；系统贡献是引入多Agent、多模态融合和检索记忆。没有确证新的结构损伤机理。

### 4.2 系统流程与组件

输入包括四个位置的振动测量、检查图像及结构记忆。信号支路清理数据、建立功率谱密度基线、窗化和归一化，再用健康期测量训练自编码器并筛查异常；传感器对关系用于定位，视觉支路评估图像区域。LLM/VLM分别检索塔体背景，融合Agent处理一致与冲突证据，最后生成带来源和置信度的区域风险解释；比较当前证据模式与增加RAG记忆模式。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

单一İskenderpaşa Mosque minaret案例；测量1–12作为健康参考、13–20评估；四传感器振动数据与关联检查图像；比较有/无RAG，并做案例内统计分析，不是跨建筑独立测试。

### 5.2 基线、指标与结果

作者报告有RAG和无RAG会改变区域风险解释及风险图；论文明确不把该比较解释为独立验证的损伤分类准确率。

### 5.3 科学贡献与证据强度

工程贡献是将全局异常、关系定位、区域映射和现场图像置于同一可追溯决策支持链；系统贡献是引入多Agent、多模态融合和检索记忆。没有确证新的结构损伤机理。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

承接振动型异常检测、视觉巡检及知识增强SHM工作，针对单独模态难以提供物理区域解释的问题整合证据。

## 7. 局限性与风险

作者强调单一案例、决策支持性质及需现场检查/无损检测确认。读者应避免把模型生成的区域风险图当成已确诊结构损伤。

## 8. 对综述写作的价值

可支持综述讨论工程监测Agent如何融合传感器与图像证据，并以检索增强提升审计和解释能力，同时指出单案例验证边界。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

多Agent融合传感器、图像和结构记忆监测历史建筑。

### 9.2 速记版 pipeline

输入包括四个位置的振动测量、检查图像及结构记忆。信号支路清理数据、建立功率谱密度基线、窗化和归一化，再用健康期测量训练自编码器并筛查异常；传感器对关系用于定位，视觉支路评估图像区域。LLM/VLM分别检索塔体背景，融合Agent处理一致与冲突证据，最后生成带来源和置信度的区域风险解释；比较当前证据模式与增加RAG记忆模式。

### 9.3 标注字段汇总

```text
paper_id=ASD-1088
inclusion_status=to_read
scientific_object_modules=09
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=09
module_taxonomy_codes=09.05.02
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O3 新实例 | 结构健康监测风险判断可由信号和图像核对 | “structural health monitoring of a historic masonry structure” · L1 |
| 验证强度 | V2 计算/仿真/回顾性 | 单案例振动数据和巡检图像分析无独立验证 | “four sensors installed on this minaret” · L23 |
| 系统自主性 | L2 闭环执行者 | 三Agent融合信号和图像证据自主生成区域风险 | — |

- 强验证（V3–V4）：否
- 置信度：medium；需全文复核：是；争议记录：无
- 复核状态：待专家复核：需全文复核
