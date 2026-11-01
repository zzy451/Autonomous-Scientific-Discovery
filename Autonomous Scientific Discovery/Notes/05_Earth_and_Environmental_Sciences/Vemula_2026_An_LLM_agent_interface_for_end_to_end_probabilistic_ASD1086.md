# An LLM-agent interface for end-to-end probabilistic seismic hazard and risk analysis

## 当前分类（2026-11-01 实证复核）

- 当前纳入状态：`to_read`；主归档：`05`。
- 本块为当前有效结论；后文既有分类、来源限制与审计判断均保留为历史记录，与本块不一致者由本块取代。
- 当前对象模块：`05;09`。
- 代表分类每个模块保留一个落点，不表示穷尽全文全部细类。

| 模块 | 二级 | 三级 | 本轮结论 |
|---|---|---|---|
| 05 | 05.01 地球科学基础 | 05.01.03 地球物理学 | 已落地 |
| 09 | 09.05 土木、建筑与水利工程 | 09.05.02 结构工程 | 已落地 |

- 模块09：建筑结构脆弱性损伤损失的实际计算。
  - 证据：PDF 第 [4] 页；原文：An end-to-end loss run across the capital-city panel

- 完整裁决：`Coverage_Check/classification_recheck_2026-11-01/`。

## 既有笔记与历史审计记录

**论文信息**

- ID：ASD-1086
- 标题：An LLM-agent interface for end-to-end probabilistic seismic hazard and risk analysis
- 作者：Sreenath Vemula; Pierre Jehel; Fabrice Cotton; Filippo Gatti
- 年份：2026
- 来源 / venue：npj Natural Hazards
- DOI / arXiv / URL：https://www.nature.com/articles/s44304-026-00262-z
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1086.txt
- PDF / 本地文件路径：Reference_PDF/05_Earth_and_Environmental_Sciences/Vemula_2026_An_LLM_agent_interface_for_end_to_end_probabilistic_ASD1086.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 科研目标 | 分析面向地震灾害和风险量化。 | Abstract, lines 11-12；核验TXT行号 11 | Probabilistic seismic hazard and risk analyses are backbone to building codes, insurance pricing, and disaster management. | 高（一手正文；非独立复现） |
| 具体对象与系统流程 | 服务暴露到OpenQuake及欧洲危险度/风险模型，数值部分由验证过的计算核心完成。 | Introduction, lines 91-97；核验TXT行号 91 | The server is organized as ﬁve layers. A protocol adapter publishes the tools and checks every incoming request, while an engineering-domain translator turns practitioner voca- bulary into model parameters. An engine-agnostic kernel dispatches the hazard computations | 高（一手正文；非独立复现） |
| Agent方法 | 模型编排并规划工具链，计算责任与LLM分离。 | Abstract, lines 16-17；核验TXT行号 16 | An agent is a large language model that chooses which tools to call and in what order, reads their results, and revises its plan. | 高（一手正文；非独立复现） |
| 05地震危险度验证 | 与欧洲地震危险度参考服务和完整逻辑树曲线比较。 | Results, Hazard distribution across Europe, lines 140-145；核验TXT行号 144 | The reference set uses the EFEHR hazard service, which evaluates the complete ESHM20 logic tree using 10,000 Monte-Carlo runs. | 高（一手正文；非独立复现） |
| 09建筑风险对象及贡献 | 提供单体建筑损伤/年均损失和改造对比。 | Introduction contributions, lines 112-116；核验TXT行号 113 | conditional mean spectra, deterministic scenarios, surface (site- ampliﬁed) hazard, per-building damage and average annual loss, retroﬁt comparison | 高（一手正文；非独立复现） |

## 0. 摘要翻译

论文提出一个基于MCP的LLM Agent接口，将OpenQuake与2020欧洲地震危险度/风险模型封装为24个类型化端点。Agent理解用户意图、选择并排序工具调用、读取结果并调整计划；经验证的OpenQuake和自定义程序负责危险度、损伤及损失计算。系统在73个欧洲城市复现475年重现期谱加速度，作者报告中位偏差约5%，97%城市偏差不超过28%，并扩展到条件谱、确定性情景、建筑损失和改造比较。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。目标是让用户执行概率地震危险度与风险分析并核验工程输出。
  - 原文位置：Abstract, lines 11-12；核验TXT行号 11；引文：Probabilistic seismic hazard and risk analyses are backbone to building codes, insurance pricing, and disaster management.
- 多步行动过程：yes。Agent 规划并串接危险度、损伤和损失工具，读取结果后修订后续调用。
  - 原文位置：Abstract, lines 16-17；核验TXT行号 16；引文：An agent is a large language model that chooses which tools to call and in what order, reads their results, and revises its plan.
- 至少一种Agent能力：yes。具备工具选择、顺序规划和根据结果修订计划能力。
  - 原文位置：Abstract, lines 16-17；核验TXT行号 16；引文：An agent is a large language model that chooses which tools to call and in what order, reads their results, and revises its plan.
- 明确科研流程角色：yes。承担危险度到风险分析链的数值工作流编排和结果呈现。
  - 原文位置：Abstract, lines 17-18；核验TXT行号 17；引文：LLM is conﬁned to the role of an orchestrator, while the OpenQuake engine and custom codes compute hazard, damage, and loss.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：05;09
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：05（仅归档，不覆盖其他模块）
- 模块内分类路径：05.01.03 地球物理学；09.05.01 土木工程
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

05.01.03由地震危险度及地面运动对象支持；09.05.01由建筑损伤、损失与改造分析支持。灾害自然过程与建筑工程后果是两个可识别对象，故多模块合理。

### 2.3 容易混淆的边界

05.01.03由地震危险度及地面运动对象支持；09.05.01由建筑损伤、损失与改造分析支持。灾害自然过程与建筑工程后果是两个可识别对象，故多模块合理。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM Agent；Tool-using Agent

### 3.2 科研流程角色

tool_use_and_code_execution；data_analysis；result_interpretation

LLM充当会话编排器；MCP服务器提供24个OpenQuake/ESHM20/ESRM20端点，工程术语翻译层、计算内核、空间缓存及来源追踪共同支撑分析。

### 3.3 自主能力

具备工具选择、顺序规划和根据结果修订计划能力。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

科学侧贡献是把现有地震危险度/风险分析链用于可复现的地点和建筑分析，并展示模型替换传播；没有提出新地震学定律。系统侧贡献是可追溯的Agent编排接口和24个端点。

### 4.2 系统流程与组件

用户提出地点、危险度或建筑风险问题后，Agent把自然语言转为参数，规划并调用MCP工具；服务器调度危险度模型、地面运动模型和暴露/脆弱性数据，返回带模型与数据来源的结果。Agent读取中间输出后可追加调用或修订解释，最终形成谱、曲线、地图或建筑损失报告。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

验证包括方程对外部解析参考核对、与EFEHR完整逻辑树比较、73城ESHM20谱加速度复现、定制地面运动模型替换及建筑损失案例；对照对象包括公布参考值和全树计算。

### 5.2 基线、指标与结果

作者报告：73个欧洲城市的475年谱加速度中位偏差约5%，97%城市偏差在28%以内；Vienna/Istanbul等曲线与参考接近，Bucharest三分支均值在475年PGA低估38%。

### 5.3 科学贡献与证据强度

科学侧贡献是把现有地震危险度/风险分析链用于可复现的地点和建筑分析，并展示模型替换传播；没有提出新地震学定律。系统侧贡献是可追溯的Agent编排接口和24个端点。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

工作建立在OpenQuake、ESHM20/ESRM20与MCP工具调用之上，重点补足跨计算链的对话式编排及来源追踪。

## 7. 局限性与风险

作者指出敏感性分析虽可扩展但未在本文开展。验证依赖欧洲参考模型和选定地点；LLM仅编排，数值科学责任仍在计算内核，不能等同自主地震研究发现。

## 8. 对综述写作的价值

可用于说明领域Agent可通过工具调用组织成熟科学软件，而保持计算与语言模型责任分离；亦可讨论科学工作流接口与结果溯源。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

以LLM编排OpenQuake地震危险度与建筑风险分析。

### 9.2 速记版 pipeline

用户提出地点、危险度或建筑风险问题后，Agent把自然语言转为参数，规划并调用MCP工具；服务器调度危险度模型、地面运动模型和暴露/脆弱性数据，返回带模型与数据来源的结果。Agent读取中间输出后可追加调用或修订解释，最终形成谱、曲线、地图或建筑损失报告。

### 9.3 标注字段汇总

```text
paper_id=ASD-1086
inclusion_status=to_read
scientific_object_modules=05;09
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=05
module_taxonomy_codes=05.01.03;09.05.01
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。
