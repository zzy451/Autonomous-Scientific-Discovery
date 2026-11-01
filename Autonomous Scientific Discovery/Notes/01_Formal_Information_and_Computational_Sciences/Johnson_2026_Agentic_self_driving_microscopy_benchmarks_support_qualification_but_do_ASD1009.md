# Agentic self-driving microscopy benchmarks support qualification but do not necessarily generalize to unseen tasks

## 当前分类（2026-11-01 实证复核）

- 当前纳入状态：`to_read`；主归档：`01`。
- 本块为当前有效结论；后文既有分类、来源限制与审计判断均保留为历史记录，与本块不一致者由本块取代。
- 当前对象模块：`01;04`。
- 代表分类每个模块保留一个落点，不表示穷尽全文全部细类。

| 模块 | 二级 | 三级 | 本轮结论 |
|---|---|---|---|
| 04 | 04.01 材料基础 | 04.01.03 材料表征 | 已落地 |
| 01 | 01.02 计算机科学 | 01.02.12 人工智能 | 已落地 |

- 模块04：真实样件尺寸断层扫描孔隙缺陷测量。
  - 证据：PDF 第 [7, 8, 9] 页；原文：additively manufactured PLA artifact

- 完整裁决：`Coverage_Check/classification_recheck_2026-11-01/`。

## 既有笔记与历史审计记录

**论文信息**

- ID：ASD-1009
- 标题：Agentic self-driving microscopy benchmarks support qualification but do not necessarily generalize to unseen tasks
- 作者：Nathan S Johnson; Ian Abshire
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2608.05266
- 原始全文缓存：.tmp_asd_pdfs/october198_sources/ASD-1009.txt
- PDF / 本地文件路径：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Johnson_2026_Agentic_self_driving_microscopy_benchmarks_support_qualification_but_do_ASD1009.pdf
- 当前状态：to_read（已确认核心，具体引用时回查原文）
- 阅读日期：2026-10-22
- 笔记作者：Codex主控整合并裁决

## Evidence Log

| 判断项 | 结论 | 证据位置 | 原文短摘 | 可信度 |
|---|---|---|---|---|
| 作者评估105种Agent配置在53项显微镜基准测试中的表现，并保留工具轨迹和RAG记录。 | 作者评估105种Agent配置在53项显微镜基准测试中的表现，并保留工具轨迹和RAG记录。 | Results；核验TXT行号 305 | We evaluated 105 configurations across 53 benchmark tests and linked every run to its configuration, tool trace, operational metrics, and RAG retrieval identifiers. We then used these data to ask three questions: whether agent configuration can be op | 高（一手正文；非独立复现） |
| 基准变化Agent拓扑、LLM、RAG/上下文参数和运行约束，并记录1949次测试运行。 | 基准变化Agent拓扑、LLM、RAG/上下文参数和运行约束，并记录1949次测试运行。 | Methods；核验TXT行号 250 | one-, two-, and three-agent graph topologies, five LLMs, RAG and context parameters, and operational constraints across 53 microscopy benchmark tests. In total, 105 agent configurations, 1,949 individual test runs, and 49,109 RAG retrievals were reco | 高（一手正文；非独立复现） |
| 作者发现基准可用于资格认证、回归测试和诊断，但异质测试套件不能支持任务无关的统一配置预测。 | 作者发现基准可用于资格认证、回归测试和诊断，但异质测试套件不能支持任务无关的统一配置预测。 | Results；核验TXT行号 250 | results show that these benchmarks are useful for qualification, regression testing, diagnosis, and direct comparison, but the current heterogeneous test suite does not support a task-independent global configuration model. 1 Introduction | 高（一手正文；非独立复现） |
| 历史配置数据不平衡，测试设备包括模拟器和多型号ZEISS Versa显微镜，重复运行并非完全独立。 | 历史配置数据不平衡，测试设备包括模拟器和多型号ZEISS Versa显微镜，重复运行并非完全独立。 | Limitations；核验TXT行号 877 | The configuration dataset was historical and unbalanced rather than a complete factorial experiment. Model, prompt, framework, code, software, and hardware versions changed during the study. Runs were collected using a simulator and multiple ZEISS Ve | 高（一手正文；非独立复现） |
| 论文使用模拟器和多个ZEISS Versa显微镜开展任务评估，并讨论运行独立性等限制。 | 论文使用模拟器和多个ZEISS Versa显微镜开展任务评估，并讨论运行独立性等限制。 | Methods/Limitations；核验TXT行号 877 | Runs were collected using a simulator and multiple ZEISS Versa microscope models. Repeated runs of the same task and configuration were not fully independent. Claude Opus 4.5 was also affected by an implementation incompatibility in the multi-agent g | 高（一手正文；非独立复现） |

## 0. 摘要翻译

论文检验自驱显微镜Agent的基准成绩能否预测未见任务表现。作者比较单/多Agent结构、LLM、RAG和运行参数，评估53项测试中的105种配置并记录工具轨迹和检索信息。基准适用于资格认证与诊断，但异质测试集不能支持任务无关的统一配置结论。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 明确科研目标：yes。研究问题是不同Agent配置能否可靠完成显微镜科研任务、以及历史基准表现能否预测未见任务表现。
  - 原文位置：Results；核验TXT行号 305；引文：We evaluated 105 configurations across 53 benchmark tests and linked every run to its configuration, tool trace, operational metrics, and RAG retrieval identifiers. We then used these data to ask three questions: whether agent configuration can be op
- 多步行动过程：yes。系统在53项测试上反复执行单动作和集成显微流程；另进行配置预测、未见任务测试及物理工作流验证。
  - 原文位置：Methods；核验TXT行号 250；引文：one-, two-, and three-agent graph topologies, five LLMs, RAG and context parameters, and operational constraints across 53 microscopy benchmark tests. In total, 105 agent configurations, 1,949 individual test runs, and 49,109 RAG retrievals were reco
- 至少一种Agent能力：yes。Agent可选择模型/拓扑、检索仪器指导并调用显微控制、几何计算、图像处理和Python工具；作者记录并分析执行轨迹。
  - 原文位置：Results；核验TXT行号 250；引文：results show that these benchmarks are useful for qualification, regression testing, diagnosis, and direct comparison, but the current heterogeneous test suite does not support a task-independent global configuration model. 1 Introduction
- 明确科研流程角色：yes。论文研究Agent在显微仪器科研流程中的资格、回归诊断和配置比较角色，同时验证物理采集和定量分析任务。
  - 原文位置：Limitations；核验TXT行号 877；引文：The configuration dataset was historical and unbalanced rather than a complete factorial experiment. Model, prompt, framework, code, software, and hardware versions changed during the study. Runs were collected using a simulator and multiple ZEISS Ve

### 1.2 排除风险检查

上述四门共同支持科研Agent纳入。完整发现闭环和全自主不作额外门槛；仅使用AI、单次预测或把被模拟对象称为agent均不足以单独纳入。具体边界以第2.3节和原文行动证据为准。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：01;04
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：01（仅归档，不覆盖其他模块）
- 模块内分类路径：01.02.12 人工智能；04.01 材料基础
- 分类深度：03/04最深二级；06/07固定三级；其他模块按证据。

### 2.2 对象优先判定

显微镜Agent配置的资格、工具使用与泛化评测；独立物理holdout对增材制造PLA样品进行微CT尺寸测量、重建及缺陷识别。

### 2.3 容易混淆的边界

纳入Agent相关研究，但主要对象是显微镜Agent软件/工具配置的资格与泛化评测，建议01.02.12人工智能为主。核对53项任务分布（6端到端、12集成、19原子仪器控制、6几何/配方、8回归/性能、1图像分析、1调试）后，不能仅凭microscopy一词归04。另有不属于53项代理模型训练集的物理holdout，对3D打印PLA样品做尺寸测量、微CT重建及>1 mm孔洞/缺陷计数，提供有限但真实的材料表征证据，可加04.01.03作为次模块；不据此把整个基准描述成材料科学研究。主模块01。

## 3. Agent 系统与科研流程角色

### 3.1 Agent 类型标签

LLM Agent；Tool-using Agent；Multi-Agent System

### 3.2 科研流程角色

tool_use_and_code_execution；data_analysis；evidence_assessment_and_validation

研究把自驱显微镜Agent配置、运行轨迹、检索上下文和任务结果纳入统一基准，重点检验基准成绩能否预测未见任务，而非提出新的成像硬件。

### 3.3 自主能力

Agent可选择模型/拓扑、检索仪器指导并调用显微控制、几何计算、图像处理和Python工具；作者记录并分析执行轨迹。

### 3.4 交叉属性标签

方法、工具和平台只作副标签；科学对象模块由实际任务证据决定。

## 4. 方法设计

### 4.1 方法动机与设计

贡献是对显微镜Agent基准的预测效度作压力测试，区分已知测试上的资格认证能力与跨任务泛化能力。

### 4.2 系统流程与组件

作者评估105种配置、53项基准测试，改变单/多Agent拓扑、LLM、RAG上下文和运行参数；记录轨迹与检索内容，并用历史成绩拟合代理预测，再进行物理显微工作流和验证任务。

## 5. 实验与验证

### 5.1 验证方式、对象与任务

验证同时包含配置基准、已知与未见任务间的预测分析、RAG检索审计，以及模拟器和多台ZEISS Versa显微镜上的运行。历史配置数据不平衡，非完整因子实验。

### 5.2 基线、指标与结果

基准适合资格测试、回归检查和故障诊断，但代理模型在已知测试上插值后不能可靠推广到未见任务；增加Agent有效率成本，检索审计可发现问题上下文，却未给出通用剪枝规则。

### 5.3 科学贡献与证据强度

贡献是对显微镜Agent基准的预测效度作压力测试，区分已知测试上的资格认证能力与跨任务泛化能力。

证据强度：原始全文支持；以上结果为作者报告，本轮没有独立复现实验。

## 6. 与已有工作的关系

相较只报告Agent在显微任务上的成功率，本文研究基准本身是否能代表未来任务，并比较架构、模型与RAG变化造成的性能差异。

## 7. 局限性与风险

配置数据为历史收集且分布不均，任务集异质；模拟器与少数显微镜型号覆盖有限。观测到的配置关联不能视作完整控制变量的因果比较。

## 8. 对综述写作的价值

可用于区分显微镜Agent基准的资格认证价值、未见任务预测局限和配置比较中的混杂问题。

推荐引用强度：普通核心引用；正式引用数字及结论前回查Evidence Log原文位置。

## 9. 总结

### 9.1 一句话概括

论文检验自驱显微镜Agent的基准成绩能否预测未见任务表现。作者比较单/多Agent结构、LLM、RAG和运行参数，评估53项测试中的105种配置并记录工具轨迹和检索信息。基准适用于资格认证与诊断，但异质测试集不能支持任务无关的统一配置结论。

### 9.2 速记版 pipeline

作者评估105种配置、53项基准测试，改变单/多Agent拓扑、LLM、RAG上下文和运行参数；记录轨迹与检索内容，并用历史成绩拟合代理预测，再进行物理显微工作流和验证任务。

### 9.3 标注字段汇总

```text
paper_id=ASD-1009
inclusion_status=to_read
scientific_object_modules=01;04
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=01
module_taxonomy_codes=01.02.12;04.01
source_level=first_hand_full_text
fulltext_followup_required=false
```

### 全文后续要求

纳入与当前分类依据已核对；如需补读其他细节，按第7节继续追踪。
