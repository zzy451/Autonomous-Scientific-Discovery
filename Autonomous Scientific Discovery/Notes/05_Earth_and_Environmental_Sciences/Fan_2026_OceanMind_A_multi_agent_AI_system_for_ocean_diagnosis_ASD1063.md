# OceanMind: A multi-agent AI system for ocean diagnosis

**论文信息**

- ID：ASD-1063
- 标题：OceanMind: A multi-agent AI system for ocean diagnosis
- 作者：Zhang, Fan; Cheng, Weicong; Chen, Yuheng; Kung, Hiuseut; Zhang, Ying; Han, Aixi; Zhong, Quanjia; Yang, Can; Gan, Jianping
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2610.03780
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1063.txt
- PDF / 本地文件路径：Reference_PDF/05_Earth_and_Environmental_Sciences/Fan_2026_OceanMind_A_multi_agent_AI_system_for_ocean_diagnosis_ASD1063.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 对象 | 分析动态三维海洋状态。 | TXT line 268；核验TXT行号 268 | In this study, we introduce OceanMind, a multi-agent AI system that directly couples LLMs with comprehensive time-dependent 3D multi-variables and physical-biogeochemical processes to automate analyses for hindcasting and forecasting ocean states (Fig. 1). To enable this end-to-end analytical process, OceanMind organizes these functions into four coordinated stages: Query Routing interprets user intent and identifies the required information sources; Skill-based Planning constructs a multi-step computational workflow that specifies how to extract the required information from the estimates; Tool Execution retrieves relevant Internet context when needed and extracts quantitative evidence from ocean state estimates; Evidence-based Summary Generation integrates these outputs and presents the synthesized results transparently. Specialized LLM agents perform distinct functions across these stages and together form OceanMind’s collaborative multi-agent architecture. Among the four stages, Skill-based Planning is particularly challenging because diverse analytical requests require different computational workflows rather than a common sequence of operations. Complex requests might involve long chains of interdependent tool calls, with some mechanism-ranking and evidence-synthesis tasks requiring more than 20 calls. To address this challenge, OceanMind incorporates 63 reusable ocean-specific analytical skills that serve as procedural manuals for the PlannerAgent in Skill-based Planning. For each type of analytical request, a skill guides the PlannerAgent in resolving the required data selections, choosing appropriate diagnostics, and coordinating compatible tools to produce the expected evidence. To improve the reliability of these plans, OceanMind further incorporates reflection and replanning mechanisms. When execution reveals a failed operation, invalid intermediate result, or unresolved dependency, the feedback is returned to the PlannerAgent to repair the workflow. By doing so, we endow OceanMind with the ability to conduct a reliable end-to-end analytical process. Together, the staged multi-agent architecture, skill-guided planning, and execution-informed replanning enable OceanMind to translate diverse requests into reliable workflows grounded in quantitative ocean evidence. Beyond reliable workflow generation, OceanMind provides a transparent and interactive analysis environment through a graphical user interface (GUI). The user can inspect analysis plans, follow the analysis execution, and examine intermediate results through the GUI. To summarize, OceanMind advances the integration of LLMs into time-dependent 3D ocean analysis, enabling researchers to focus on scientific interpretation and supporting non-specialists in formulating environmental policies grounded in quantitative ocean evidence. | 高（一手正文；非独立复现） |
| 基准 | 240题覆盖59项技能和四级复杂度。 | TXT line 275；核验TXT行号 275 | To assess OceanMind’s ability to analyze time-dependent 3D ocean state estimates, we evaluated OceanMind using three complementary perspectives. First, we evaluated whether OceanMind could translate diverse analytical requests into reliable computational workflows. For this first test, we constructed a benchmark of 240 queries spanning 59 target skills and four complexity levels (L1 to L4), using ocean state estimates from the China Sea Multiscale Ocean Modeling System (CMOMS) [21, 22, 23]. The results comparison used ReAct, a widely used general-purpose agent paradigm that interleaves reasoning and tool use, with access to the same registered tool pool. OceanMind achieved a 91.2% pass rate and 90.5% effective step efficiency. Its performance remained robust across task complexity, with pass rates of 100%, 96%, 83%, and 91% from L1 to L4, respectively. Second, we applied OceanMind to diagnose regional oceans using CMOMS results. This demonstration resulted in OceanMind reproducing published ocean state diagnostics, constructing traceable evidence chains for hypothesis validation, and supporting environmental decisions using spatially explicit risk assessment. Finally, we evaluated whether OceanMind could generalize from a CMOMS-based regional diagnosis to a global ocean diagnosis using products from the Copernicus Marine Environment Monitoring Service (CMEMS) [24]. For the last test, we applied the same analytical framework to the Gulf of Mexico and tropical Pacific. | 高（一手正文；非独立复现） |
| 基线 | ReAct缺少OceanMind的阶段化规划与验证。 | TXT line 345；核验TXT行号 345 | We benchmarked OceanMind against two ReAct baselines [27] that shared the same ocean-tool registry (Fig. 2a). OceanMind and ReAct(Claude) both used Claude Sonnet 4.5. ReAct(Qwen) used Qwen3 Max. The ReAct baselines followed a standard reason-act-observe loop over the available tools, without OceanMind’s staged routing, skill planning, execution validation, or reflection and re-planning steps. We evaluated each system using three criteria: (1) effectiveness, whether the final answer was scientifically adequate and constraints were consistent; (2) efficiency, how closely the number of executed core steps matched the canonical gold tool chain; and (3) robustness, whether performance held when tasks demanded greater composition, constraint tracking, and evidence synthesis. OceanMind achieved a 91.2% pass rate, compared to 64.6% for ReAct(Qwen) and 64.2% for ReAct(Claude), representing a 41.2% relative improvement over the stronger ReAct baseline (Fig. 2a). OceanMind also reached 90.5% effective step efficiency, compared to 74.5% for ReAct(Qwen) and 73.7% for ReAct(Claude), a relative improvement of 21.5%. The complexity-stratified results showed that OceanMind remained reliable as workflow demands increased. Its pass rates were 100.0%, 96.0%, 83.3%, and 90.6% from L1 to L4, compared to 87.5%, 75.0%, 61.9%, and 21.9% for ReAct(Qwen), and 79.2%, 73.0%, 63.1%, and 28.1% for ReAct(Claude). The biggest differences occurred on L4 tasks, indicating that OceanMind was beter at organizing long, dependent analytical workflows while preserving the user’s scientific constraints. | 高（一手正文；非独立复现） |
| 评测范围 | 结果包括时间序列、剖面、空间场和事件检测等。 | TXT line 802；核验TXT行号 802 | We evaluated OceanMind with a dedicated benchmarking package. The benchmark contained 240 supported natural language queries derived from 59 target ocean skills (Supplementary Section 2.3). The benchmark combined 200 base queries with 40 interpretation queries. The suite spanned four complexity levels: L1 tested direct extraction, visualization and simple statistics (24 queries); L2 tested preprocessing, event detection, resampling and derived diagnostics (100 queries); L3 tested multi-step diagnostic composition, including sections, Hovmöller diagrams, EOF analysis, correlations and event comparison (84 queries); and L4 tested mechanism interpretation, budget reasoning, environmental assessment and evidence synthesis for policy questions (32 queries). Each query was paired with a canonical gold tool chain constructed from the current skill workflows and registered tool contracts. | 高（一手正文；非独立复现） |
| 独立核验 | 以现场和卫星遥感观测核对诊断。 | TXT line 571；核验TXT行号 571 | The results from our test runs also show that OceanMind is much more than a plotting interface. In the reproduction case, OceanMind reconstructed literature level circulation diagnostics from validated ocean datasets and their inherent physics. Independent checks against in situ and satellite remote sensing observations further supported the correctness of the generated diagnostics. In the hypothesis validation cases, OceanMind exposed the evidence chain behind each conclusion, including uncertainty and residual terms when support was incomplete. In the management case, OceanMind connected ocean hazards such as hypoxia, warming, stratification, bloom pressure, and trend diagnostics to spatially explicit recommendations. The test results showed how OceanMind could support scientific research, hypothesis testing and evidence-based marine management without hiding the computations behind a free-form text answer. Moreover, we designed OceanMind to be extensible across ocean state estimates. The global applications showed that the same workflow could be transferred to other regions after data were converted into compatible variables, coordinates, time ranges, and depth dimensions. | 高（一手正文；非独立复现） |

## 0. 摘要翻译

OceanMind连接LLM与时变三维海洋物理及生物地球化学状态，用于海洋诊断、假设检验和环境证据综合。系统由查询路由、技能规划、工具执行和证据总结阶段组成，以240题基准、ReAct对照及科学案例评估。 本记录依据全文摘要、方法、实验、结果和局限段落整理，具体依据与引用定位见上列证据日志。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。使用真实海洋状态数据进行分析与诊断。
  - 原文位置：TXT line 268；核验TXT行号 268；引文：In this study, we introduce OceanMind, a multi-agent AI system that directly couples LLMs with comprehensive time-dependent 3D multi-variables and physical-biogeochemical processes to automate analyses for hindcasting and forecasting ocean states (Fig. 1). To enable this end-to-end analytical process, OceanMind organizes these functions into four coordinated stages: Query Routing interprets user intent and identifies the required information sources; Skill-based Planning constructs a multi-step computational workflow that specifies how to extract the required information from the estimates; Tool Execution retrieves relevant Internet context when needed and extracts quantitative evidence from ocean state estimates; Evidence-based Summary Generation integrates these outputs and presents the synthesized results transparently. Specialized LLM agents perform distinct functions across these stages and together form OceanMind’s collaborative multi-agent architecture. Among the four stages, Skill-based Planning is particularly challenging because diverse analytical requests require different computational workflows rather than a common sequence of operations. Complex requests might involve long chains of interdependent tool calls, with some mechanism-ranking and evidence-synthesis tasks requiring more than 20 calls. To address this challenge, OceanMind incorporates 63 reusable ocean-specific analytical skills that serve as procedural manuals for the PlannerAgent in Skill-based Planning. For each type of analytical request, a skill guides the PlannerAgent in resolving the required data selections, choosing appropriate diagnostics, and coordinating compatible tools to produce the expected evidence. To improve the reliability of these plans, OceanMind further incorporates reflection and replanning mechanisms. When execution reveals a failed operation, invalid intermediate result, or unresolved dependency, the feedback is returned to the PlannerAgent to repair the workflow. By doing so, we endow OceanMind with the ability to conduct a reliable end-to-end analytical process. Together, the staged multi-agent architecture, skill-guided planning, and execution-informed replanning enable OceanMind to translate diverse requests into reliable workflows grounded in quantitative ocean evidence. Beyond reliable workflow generation, OceanMind provides a transparent and interactive analysis environment through a graphical user interface (GUI). The user can inspect analysis plans, follow the analysis execution, and examine intermediate results through the GUI. To summarize, OceanMind advances the integration of LLMs into time-dependent 3D ocean analysis, enabling researchers to focus on scientific interpretation and supporting non-specialists in formulating environmental policies grounded in quantitative ocean evidence.
- 多步行动过程：yes。系统把路由、技能规划、工具执行和证据综合串联。
  - 原文位置：TXT line 275；核验TXT行号 275；引文：To assess OceanMind’s ability to analyze time-dependent 3D ocean state estimates, we evaluated OceanMind using three complementary perspectives. First, we evaluated whether OceanMind could translate diverse analytical requests into reliable computational workflows. For this first test, we constructed a benchmark of 240 queries spanning 59 target skills and four complexity levels (L1 to L4), using ocean state estimates from the China Sea Multiscale Ocean Modeling System (CMOMS) [21, 22, 23]. The results comparison used ReAct, a widely used general-purpose agent paradigm that interleaves reasoning and tool use, with access to the same registered tool pool. OceanMind achieved a 91.2% pass rate and 90.5% effective step efficiency. Its performance remained robust across task complexity, with pass rates of 100%, 96%, 83%, and 91% from L1 to L4, respectively. Second, we applied OceanMind to diagnose regional oceans using CMOMS results. This demonstration resulted in OceanMind reproducing published ocean state diagnostics, constructing traceable evidence chains for hypothesis validation, and supporting environmental decisions using spatially explicit risk assessment. Finally, we evaluated whether OceanMind could generalize from a CMOMS-based regional diagnosis to a global ocean diagnosis using products from the Copernicus Marine Environment Monitoring Service (CMEMS) [24]. For the last test, we applied the same analytical framework to the Gulf of Mexico and tropical Pacific.
- 至少一种Agent能力：yes。多Agent调用工具提取海洋变量并进行验证。
  - 原文位置：TXT line 345；核验TXT行号 345；引文：We benchmarked OceanMind against two ReAct baselines [27] that shared the same ocean-tool registry (Fig. 2a). OceanMind and ReAct(Claude) both used Claude Sonnet 4.5. ReAct(Qwen) used Qwen3 Max. The ReAct baselines followed a standard reason-act-observe loop over the available tools, without OceanMind’s staged routing, skill planning, execution validation, or reflection and re-planning steps. We evaluated each system using three criteria: (1) effectiveness, whether the final answer was scientifically adequate and constraints were consistent; (2) efficiency, how closely the number of executed core steps matched the canonical gold tool chain; and (3) robustness, whether performance held when tasks demanded greater composition, constraint tracking, and evidence synthesis. OceanMind achieved a 91.2% pass rate, compared to 64.6% for ReAct(Qwen) and 64.2% for ReAct(Claude), representing a 41.2% relative improvement over the stronger ReAct baseline (Fig. 2a). OceanMind also reached 90.5% effective step efficiency, compared to 74.5% for ReAct(Qwen) and 73.7% for ReAct(Claude), a relative improvement of 21.5%. The complexity-stratified results showed that OceanMind remained reliable as workflow demands increased. Its pass rates were 100.0%, 96.0%, 83.3%, and 90.6% from L1 to L4, compared to 87.5%, 75.0%, 61.9%, and 21.9% for ReAct(Qwen), and 79.2%, 73.0%, 63.1%, and 28.1% for ReAct(Claude). The biggest differences occurred on L4 tasks, indicating that OceanMind was beter at organizing long, dependent analytical workflows while preserving the user’s scientific constraints.
- 明确科研流程角色：yes。承担海洋数据分析、诊断及证据综合。
  - 原文位置：TXT line 571；核验TXT行号 571；引文：The results from our test runs also show that OceanMind is much more than a plotting interface. In the reproduction case, OceanMind reconstructed literature level circulation diagnostics from validated ocean datasets and their inherent physics. Independent checks against in situ and satellite remote sensing observations further supported the correctness of the generated diagnostics. In the hypothesis validation cases, OceanMind exposed the evidence chain behind each conclusion, including uncertainty and residual terms when support was incomplete. In the management case, OceanMind connected ocean hazards such as hypoxia, warming, stratification, bloom pressure, and trend diagnostics to spatially explicit recommendations. The test results showed how OceanMind could support scientific research, hypothesis testing and evidence-based marine management without hiding the computations behind a free-form text answer. Moreover, we designed OceanMind to be extensible across ocean state estimates. The global applications showed that the same workflow could be transferred to other regions after data were converted into compatible variables, coordinates, time ranges, and depth dimensions.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：05
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：05（仅归档，不覆盖其他模块）
- 模块内分类路径：05.02 大气、海洋与水文科学
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

对象为海洋状态及相关过程，分类05；政策分析是应用场景。

### 2.3 容易混淆的边界

对象为海洋状态及相关过程，分类05；政策分析是应用场景。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

multi_agent；tool_augmented_llm

### 3.2 科研流程角色

data_analysis；hypothesis_testing；evidence_synthesis

六个LLM Agent与ToolOrchestrator调用CMOMS数据、计算工具及网络信息。

### 3.3 自主能力

多Agent调用工具提取海洋变量并进行验证。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

科学贡献为海洋状态分析及假设案例；系统贡献为技能规划、验证和重规划的多Agent架构。

### 4.2 系统流程与组件

自然语言问题经路由后匹配海洋技能和数据约束，规划器生成工具链，执行器提取时空变量，校验和反思环节必要时重试，综合器输出发现、限制与证据。 这一工作流的实施细节、输入输出和验证范围均按原文所报告内容理解，不将展示案例外推为普遍能力。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

240题覆盖59技能和四级复杂度，以CMOMS及共享工具池ReAct基线评估；规则检查结果类型、数据约束和诊断充分性，另有案例和观测核验。

### 5.2 基线、指标与结果

作者报告整体pass rate为91.2%；案例包括810个有效格点中识别200个热点，并报告独立现场及卫星观测检查。

### 5.3 科学贡献与证据强度

科学贡献为海洋状态分析及假设案例；系统贡献为技能规划、验证和重规划的多Agent架构。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

相较普通ReAct流程，增加路由、规划、执行校验和反思。

## 7. 局限性与风险

- author_stated：系统评估依赖已注册工具和技能覆盖。
- reviewer_inference：规则基准未必覆盖专家对机制解释的全部判断；案例演示不等同自主发现。

## 8. 对综述写作的价值

可讨论结构化工具链如何处理高维科研数据并呈现证据。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

OceanMind以多Agent工具流程分析三维海洋数据，并通过基准和案例验证。

### 9.2 速记版 pipeline

自然语言问题经路由后匹配海洋技能和数据约束，规划器生成工具链，执行器提取时空变量，校验和反思环节必要时重试，综合器输出发现、限制与证据。 这一工作流的实施细节、输入输出和验证范围均按原文所报告内容理解，不将展示案例外推为普遍能力。

### 9.3 标注字段汇总

```text
paper_id=ASD-1063
inclusion_status=to_read
scientific_object_modules=05
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=05
module_taxonomy_codes=05.02
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`05.02.05` 物理海洋学；二级：`05.02`。
- 原文位置：PDF pp.7,9。
- 判定：Concrete experiment/task evidence supports 05.02.05 (物理海洋学). required by such a multi-step workflow. We selected the China Seas circulation study of Gan et al. [21, 18] the authors identified vertically alternating rotating circulation through a connected sequence of transport stream function, Stokes’ theorem, and vorticity dynamics. This case, therefore, evaluated whether OceanMind could reconstruct a multi-step physical diagnosis rather than generate isolated plots. We appli
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
