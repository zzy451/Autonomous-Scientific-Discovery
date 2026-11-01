# Mind the alignment gap: a spatial transcriptomics benchmark for scientific coding agents

**论文信息**

- ID：ASD-0899
- 标题：Mind the alignment gap: a spatial transcriptomics benchmark for scientific coding agents
- 作者：Yiqun Chen; Stephanie C. Hicks
- 年份：2026
- 来源 / venue：openRxiv (preprint)
- DOI / arXiv / URL：https://doi.org/10.64898/2026.07.05.736638
- 一手阅读来源：https://www.biorxiv.org/content/10.64898/2026.07.05.736638v1.full
- 来源层级：全文
- 阅读版本：对应缓存来源版本，参见Evidence Log
- 阅读版本题名：Mind the alignment gap: a spatial transcriptomics benchmark for scientific coding agents
- 原始全文缓存：C:/Users/20683/Desktop/综述/.tmp_asd_pdfs/source_rescue/mind_html.html
- PDF / 本地文件路径：未归档PDF
- 当前状态：included
- 阅读日期：2026-10-22
- 笔记作者：Codex（读者证据包经主控审核整合）

## Evidence Log

| 判断项 | 结论 / 原文概括 | 证据位置 | 可信度 |
|---|---|---|---|
| 论文身份和研究对象 | 题名 Mind the Alignment Gap: A Spatial Transcriptomics Benchmark for Scientific Coding Agents；DOI 10.64898/2026.07.05.736638。 | bioRxiv全文首页 / DOI行 | high |
| 将空间组学论文基准转为隐藏评测任务并定义可见/隐藏信息 | 将SABench转为executable hidden-evaluation tasks；公开输入与输出schema，隐藏labels、held-out expression targets、gold coordinates、metric definitions和scorer metadata。 | Methods §2, “Methods”首段 | high |
| 任务规模和筛选过程 | 从SABench 295项选40项；按空间转录组技术/平台分层，因缺少中间合并文件或派生资产而排除无法复现的任务。 | Methods §2, “Methods”首段 | high |
| Agent任务确为组织切片空间配准 | Agent提交二维组织切片配准坐标表；使用隐藏评分器评估，支持空间组学与生物信息学对象分类。 | Methods §2, §2.1 “Agent setup” | high |
| 受控执行条件、Agent配置及重复数 | 三条件为Basic、Package-aware (PA)、Full + prior (FPP)；Codex CLI、固定划分和评价方案，每任务/条件独立运行三次。 | Methods §2.1 “Agent setup” | high |
| 专用包使用增加但聚合精度未随之增加 | FPP增加专用空间配准包使用；全文摘要给出总体均分0.36 vs 0.43（Basic较高），95% CI [-0.11,-0.03]。 | Results §3.1 “More prompt context increased package use, but not aggregate accuracy” | high |
| 分析了Agent具体执行轨迹和失效机制 | 轨迹和任务分析发现额外上下文可引发多余变换、脆弱的package-first流程及基础设施失败；简单几何启发式在部分切片任务表现更好。 | Results §3, task-level analysis / Discussion and Conclusion | high |
| 外推边界 | 作者说明仅一个模型/Agent配置、单一基准家族和单一来源论文，跨模型、跨Agent harness及其他领域的可推广性仍待检验。 | Discussion and Conclusion, limitations paragraph | high |

## 0. 摘要翻译

研究提出交互式框架，从论文构造可执行科学Agent基准并通过轨迹诊断Agent行为；以空间转录组配准为案例，将SABench中40/295项任务改造成隐藏评测，Agent需提交二维组织切片坐标配准结果。对三种执行条件进行120次独立运行：Basic、Package-aware、Full + prior。更丰富的软件包/环境提示提高专用包使用，但Full + prior平均得分低于Basic（0.36 vs 0.43；差值95% CI [-0.11,-0.03]）；轨迹显示多余变换、脆弱的包优先工作流和基础设施故障。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 当前判断：included；读者建议：included。
Agent在真实空间转录组切片对齐任务中自主执行代码、调用空间配准工具并提交坐标表；研究还对其执行条件、运行轨迹和结果进行系统评估。科学对象是空间转录组/组织切片配准，具体基准任务支持06分类；研究没有独立患者诊断或治疗任务，不增加07。

### 1.2 排除风险检查

研究任务以空间转录组数据、组织切片坐标配准和组学分析工具为直接科学对象，采用06.03.04单细胞/空间组学相关研究及06.01.12生物信息学代码。它不是只提出通用Agent benchmark的01.04论文，也没有独立的病人诊断/治疗任务支持07。
完整闭环不是纳入门槛；科研目标、多步行动、至少一项Agent能力及明确科研角色须同时成立。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：06
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：06（仅归档，不替代多模块事实）
- 模块内分类路径：06.03.04
- 分类深度：03/04使用二级；06/07使用固定三级；其余沿用现有树。
- 分类状态：原文证据复核

### 2.2 对象优先判定

40项空间转录组切片配准任务×3种条件×3次独立重复=120次运行。FPP使Agent更多使用PASTE2、PASTE、Spateo、SPACEL等专用包，但聚合得分低于Basic；摘要报告0.36 vs 0.43，95% CI [-0.11,-0.03]。结果部分对任务级差异和日志进行分析：更多上下文可引导到适用的配准包，也会使Agent偏离足够有效的简单几何解法；轨迹分析发现多余数据变换、脆弱的package-first执行及基础设施失败。

### 2.3 容易混淆的边界

研究任务以空间转录组数据、组织切片坐标配准和组学分析工具为直接科学对象，采用06.03.04单细胞/空间组学相关研究及06.01.12生物信息学代码。它不是只提出通用Agent benchmark的01.04论文，也没有独立的病人诊断/治疗任务支持07。

## 3. Agent 系统与科研流程角色

Agent在真实空间转录组切片对齐任务中自主执行代码、调用空间配准工具并提交坐标表；研究还对其执行条件、运行轨迹和结果进行系统评估。科学对象是空间转录组/组织切片配准，具体基准任务支持06分类；研究没有独立患者诊断或治疗任务，不增加07。

科研流程与自主能力以本文实际行动和工具调用为依据：

作者将已发表空间转录组配准基准SABench转化为可执行、隐藏评测的代码Agent任务：向Agent公开输入数据和输出格式，隐藏标签、held-out表达目标、gold坐标、指标定义与评分元数据，并以同一隐藏评分器评价提交。选取SABench 295项中40项可复现任务，按技术/平台分层抽样；设置Basic、Package-aware (PA)、Full + prior (FPP)三种提示/软件环境条件。使用Codex CLI和固定数据划分，每个任务×条件做3次独立运行；检查端到端配准得分、软件包使用、运行日志/trace和任务级失败原因。

## 4. 方法设计

### 4.1 方法动机与设计

提供从论文构造可执行科学Agent基准并审计运行轨迹的实证框架；空间转录组配准案例显示，增加领域包/环境提示会改变工具选择，却不保证科学对象上的配准质量提高，因此评测应并看最终输出、执行轨迹和工作流。

### 4.2 系统流程与组件

作者将已发表空间转录组配准基准SABench转化为可执行、隐藏评测的代码Agent任务：向Agent公开输入数据和输出格式，隐藏标签、held-out表达目标、gold坐标、指标定义与评分元数据，并以同一隐藏评分器评价提交。选取SABench 295项中40项可复现任务，按技术/平台分层抽样；设置Basic、Package-aware (PA)、Full + prior (FPP)三种提示/软件环境条件。使用Codex CLI和固定数据划分，每个任务×条件做3次独立运行；检查端到端配准得分、软件包使用、运行日志/trace和任务级失败原因。

## 5. 实验与验证

### 5.1 验证方式、对象及任务

40项空间转录组切片配准任务×3种条件×3次独立重复=120次运行。FPP使Agent更多使用PASTE2、PASTE、Spateo、SPACEL等专用包，但聚合得分低于Basic；摘要报告0.36 vs 0.43，95% CI [-0.11,-0.03]。结果部分对任务级差异和日志进行分析：更多上下文可引导到适用的配准包，也会使Agent偏离足够有效的简单几何解法；轨迹分析发现多余数据变换、脆弱的package-first执行及基础设施失败。

### 5.2 基线、指标与结果

40项空间转录组切片配准任务×3种条件×3次独立重复=120次运行。FPP使Agent更多使用PASTE2、PASTE、Spateo、SPACEL等专用包，但聚合得分低于Basic；摘要报告0.36 vs 0.43，95% CI [-0.11,-0.03]。结果部分对任务级差异和日志进行分析：更多上下文可引导到适用的配准包，也会使Agent偏离足够有效的简单几何解法；轨迹分析发现多余数据变换、脆弱的package-first执行及基础设施失败。

### 5.3 科学贡献与证据强度

提供从论文构造可执行科学Agent基准并审计运行轨迹的实证框架；空间转录组配准案例显示，增加领域包/环境提示会改变工具选择，却不保证科学对象上的配准质量提高，因此评测应并看最终输出、执行轨迹和工作流。

证据层级：原始全文支持；作者报告结果不等于独立复现。

## 6. 与已有工作的关系

与科学代码Agent benchmark、空间转录组配准工具和trace审计相关。具体生物发现不是论文目标，科学对象基准任务本身支持06分类。

## 7. 局限性与风险

该实证只使用单一Agent模型/配置、单一SABench来源论文与空间转录组配准基准；不能外推所有科学编码Agent或其他科学领域。部分原始SABench任务因中间文件/派生资产缺失而无法重建；环境提示引发的包安装/运行基础设施问题也影响表现。研究评的是计算配准任务，不是新的生物学发现或临床验证。

## 8. 对综述写作的价值

可为综述提供研究型Agent benchmark如何测试工具操作、科学对象结果及过程轨迹的案例。

推荐引用强度：普通引用，可在核对原文后用于相应领域案例。

## 9. 总结

### 9.1 一句话概括

评测空间组学Agent的配准行动

### 9.2 速记版 pipeline

作者将已发表空间转录组配准基准SABench转化为可执行、隐藏评测的代码Agent任务：向Agent公开输入数据和输出格式，隐藏标签、held-out表达目标、gold坐标、指标定义与评分元数据，并以同一隐藏评分器评价提交。选取SABench 295项中40项可复现任务，按技术/平台分层抽样；设置Basic、Package-aware (PA)、Full + prior (FPP)三种提示/软件环境条件。使用Codex CLI和固定数据划分，每个任务×条件做3次独立运行；检查端到端配准得分、软件包使用、运行日志/trace和任务级失败原因。

### 9.3 标注字段汇总

```text
paper_id=ASD-0899
inclusion_status=included
scientific_object_modules=06
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=06
module_taxonomy_codes=06.03.04
source_level=fulltext
fulltext_followup_required=false
```

### 全文后续要求

本轮已读原始全文并完成对象分类；无需为纳入/分类另做全文补读。具体引用时仍需回查相应原文位置。


## 2026-10-29 PR剩余差异复核

- 来源深度：`target_pdf_fulltext`。本轮涉及3条差异，其中3条已判定，0条待核。摘要或图注支持的判定不代表全文已逐页核验。
- 正式修正：科学对象模块为`01;06`；新增`01.02.12 人工智能`，保留`06.03.04`和生物主归档。PDF第3–4页的Basic/PA/FPP对照及失败行为分析构成独立计算实验。

- 原1664行号 `1134`：`accept_change`。The verified 16-page original bioRxiv PDF experimentally varies Basic/Package-aware/Full+prior agent conditions (p.3 section 2.1), measures 0.43/0.42/0.36 mean performance and paired comparisons (p.4 section 3.1), and systematically analyzes tool-use/failure behavior. Agent behavior is an independent computational research object, supporting added 01.02.12 artificial intelligence; retain the biological spatial-transcriptomics object under 06.03.04.
  - 位置：PDF p.3, section 2.1 Agent setup；来源：https://www.biorxiv.org/content/10.64898/2026.07.05.736638v1.full.pdf

- 原1664行号 `1135`：`reject_pr`。The original PDF explicitly studies spatial transcriptomics tissue-slice alignment; current taxonomy 06.03.04 single-cell biology exists. Reject deletion based on an obsolete absence of tertiary terms. This biological classification can coexist with the independently tested 01 agent-performance object.
  - 位置：PDF p.3, section 2.1 Agent setup；来源：https://www.biorxiv.org/content/10.64898/2026.07.05.736638v1.full.pdf

- 原1664行号 `1136`：`accept_change`。The verified 16-page original bioRxiv PDF experimentally varies Basic/Package-aware/Full+prior agent conditions (p.3 section 2.1), measures 0.43/0.42/0.36 mean performance and paired comparisons (p.4 section 3.1), and systematically analyzes tool-use/failure behavior. Agent behavior is an independent computational research object, supporting added 01.02.12 artificial intelligence; retain the biological spatial-transcriptomics object under 06.03.04.
  - 位置：PDF p.3, section 2.1 Agent setup；来源：https://www.biorxiv.org/content/10.64898/2026.07.05.736638v1.full.pdf

逐条引文、来源文件和限制见 `Coverage_Check/pr1_82_recheck_2026-10-29/final_review.json`。保留现有分类不等于全部分类边界已消除。
