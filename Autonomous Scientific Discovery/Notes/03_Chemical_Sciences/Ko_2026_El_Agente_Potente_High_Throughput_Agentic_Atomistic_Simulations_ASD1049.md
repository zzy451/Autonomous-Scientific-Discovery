# El Agente Potente: High-Throughput Agentic Atomistic Simulations

**论文信息**

- ID：ASD-1049
- 标题：El Agente Potente: High-Throughput Agentic Atomistic Simulations
- 作者：Tsz Wai Ko; Jiaru Bai; Thomas Swanick; Yeonghun Kang; Changhyeok Choi; Angelina Qihong Jiang; Aiwei Yin; Varinia Bernales; Alán Aspuru-Guzik
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2609.14840
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1049.txt
- PDF / 本地文件路径：全文已缓存；PDF尚未归档，详见资料清单
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 方法系统 | 结合类型化执行图与编码Agent完成原子模拟。 | Abstract；核验TXT行号 629 | El Agente Potente: Natural-language scientific requests are adaptively routed to reusable computational capabilities for MLIP-driven atomistic simulation. | 高（一手正文；非独立复现） |
| 可靠性分工 | LLM限于规划路由，计算和验证由确定性Python执行。 | Abstract；核验TXT行号 562 | Typed execution graphs provide structured and provenance-aware execution for standardized workflows, with llm restricted to planning and routing while deterministic Python components perform scientific computation and validation. | 高（一手正文；非独立复现） |
| 材料对象 | 案例包括钙钛矿发现和超离子锂导体。 | Section 2.3.1；核验TXT行号 867 | Figure 3: Agentic workflows for materials discovery: Exploration of perovskite materials a and lithium superionic conductors b using mlip and generative models. | 高（一手正文；非独立复现） |
| 化学对象 | 案例覆盖分子构象、吸附和表面催化反应。 | Abstract / Results；核验TXT行号 981 | Low-energy conformer-search workflow. Starting from a user-specified molecular structure, the agent samples conformers with MLIPs, identifies low-energy candidates, reranks MLIP energies with more accurate DFT calculations, and performs vibrational-frequency calculations to generate infrared and Raman spectra. | 高（一手正文；非独立复现） |
| 验证 | 报告MLIP基准、可复现性和量化化学验证。 | Section 2.3.2；核验TXT行号 165 | Low-energy conformer search and validation with quantum chemistry | 高（一手正文；非独立复现） |
| 主控复核：具体科学对象 | 案例包括钙钛矿及超离子导体材料发现，也包括分子能景、表面吸附和过渡态/催化工作流；材料与化学过程均有具体任务。 | TXT line 157；核验TXT行号 157 | Superionic lithium-ion conductors 2.3.2 Molecular Energy Landscape Exploration Low-energy conformer search and validation with quantum chemistry Agent-driven metadynamics for conformational free-energy exploration 2.3.3 Adsorption and Catalytic Rea | 高（一手正文；非独立复现） |

## 0. 摘要翻译

El Agente Potente通过类型化执行图和编码Agent支持MLIP驱动的高通量原子模拟。前者为标准任务提供结构化、带来源记录的工作流；LLM负责规划和路由，确定性代码执行科学计算与验证。案例覆盖材料发现、分子能景、吸附和催化。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。目标是以ML interatomic potentials自动执行原子尺度材料、分子及反应计算。
  - 原文位置：Abstract；核验TXT行号 613；引文：El Agente Potente, an agentic framework for mlip-driven atomistic simulations that integrates structured workflow execution with programmable agentic flexibility.
- 多步行动过程：yes。流程以执行图管理标准化多步模拟，并可切换到灵活编码模式。
  - 原文位置：Abstract；核验TXT行号 562；引文：Typed execution graphs provide structured and provenance-aware execution for standardized workflows, with llm restricted to planning and routing while deterministic Python components perform scientific computation and validation.
- 至少一种Agent能力：yes。LLM计划和路由任务，确定性Python组件执行计算并验证。
  - 原文位置：Abstract；核验TXT行号 562；引文：Typed execution graphs provide structured and provenance-aware execution for standardized workflows, with llm restricted to planning and routing while deterministic Python components perform scientific computation and validation.
- 明确科研流程角色：yes。系统开展材料筛选、分子能景探索、吸附和催化反应研究。
  - 原文位置：Abstract；核验TXT行号 651；引文：across molecules, bulk materials, and interfaces.

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：03;04
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：03（仅归档，不覆盖其他模块）
- 模块内分类路径：03.03 合成、反应与催化；04.01 材料基础
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

案例包括钙钛矿及超离子导体材料发现，也包括分子能景、表面吸附和过渡态/催化工作流；材料与化学过程均有具体任务。

### 2.3 容易混淆的边界

案例包括钙钛矿及超离子导体材料发现，也包括分子能景、表面吸附和过渡态/催化工作流；材料与化学过程均有具体任务。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM Agent；Tool-using Agent；Hybrid Agent

### 3.2 科研流程角色

experimental_design；simulation_modeling；tool_use_and_code_execution；data_analysis；evidence_assessment_and_validation

系统包含图式工作流Agent和更灵活的编码Agent；通过组件注册、共享状态、计算软件路由及知识图谱持久化组织材料/分子任务，并让确定性模拟程序负责数值结果。

### 3.3 自主能力

LLM计划和路由任务，确定性Python组件执行计算并验证。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

材料科学贡献是以计算流程筛选候选和评估稳定性；化学贡献是分子能景、吸附及催化反应计算；系统贡献是图式审计可靠性与代码灵活性互补。

### 4.2 系统流程与组件

输入材料/分子问题及候选结构；规划图式计算或生成定制workflow代码；执行结构弛豫、性质计算、能景采样或反应搜索；用量化化学、稳定性过滤和其他物理检查复核；聚合结果与 provenance。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

含标准高通量可复现性测试、MLIP模型benchmark、与skill-based coding agent比较；案例包括钙钛矿、超离子导体、构象搜索、metadynamics、表面吸附/过渡态与MOF气体插入。

### 5.2 基线、指标与结果

作者报告多个材料和化学工作流案例及基准；分子低能构象用PySCF重排验证，模拟对象覆盖真实材料、分子和反应体系。本文不应把单一复现率或速度概括成未报告的数字。

### 5.3 科学贡献与证据强度

材料科学贡献是以计算流程筛选候选和评估稳定性；化学贡献是分子能景、吸附及催化反应计算；系统贡献是图式审计可靠性与代码灵活性互补。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

不同于只提供MLIP调用的高通量软件，本文引入Agent规划路由与任务级workflow构造；同时把LLM从科学数值计算中隔离。

## 7. 局限性与风险

证据均为计算模拟；预测材料与反应结果仍需实验验证。MLIP适用域、外推误差及Agent构造代码的可重复性是实际风险。

## 8. 对综述写作的价值

可支持综述比较高通量原子模拟Agent如何平衡流程可审计性、灵活度与计算验证。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

El Agente Potente以可追溯执行图与编码Agent开展材料和化学原子模拟。

### 9.2 速记版 pipeline

输入材料/分子问题及候选结构；规划图式计算或生成定制workflow代码；执行结构弛豫、性质计算、能景采样或反应搜索；用量化化学、稳定性过滤和其他物理检查复核；聚合结果与 provenance。

### 9.3 标注字段汇总

```text
paper_id=ASD-1049
inclusion_status=to_read
scientific_object_modules=03;04
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=03
module_taxonomy_codes=03.03;04.01
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。


## 2026-10-29 三级分类复核

- 归档分类：`03.03.04` 反应机理；二级：`03.03`。
- 原文位置：PDF p.16, Transition-state search in surface reactions。
- 判定：Fe(110)表面反应路径与过渡态搜索直接支持反应机理；吸附、分子构象、材料计算另保留多对象覆盖。
- 台账：[本轮决策记录](../../Coverage_Check/tertiary_145_decisions_2026-10-29.json)。保留其他有证据的科学对象模块；归档分类不表示全文只涉及单一对象。
