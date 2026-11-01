# CausalDS: Benchmarking Causal Reasoning in Data-Science Agents

**论文信息**

- ID：ASD-0876
- 标题：CausalDS: Benchmarking Causal Reasoning in Data-Science Agents
- 作者：Leban, Andrej; Saarinen, Theo; Sun, Yuekai
- 年份：2026
- 来源 / venue：arXiv
- DOI / arXiv / URL：https://arxiv.org/abs/2607.08093
- 一手阅读来源：https://arxiv.org/abs/2607.08093
- 来源层级：全文
- 阅读版本：对应缓存来源版本，参见Evidence Log
- 阅读版本题名：CausalDS: Benchmarking Causal Reasoning in Data-Science Agents
- 原始全文缓存：C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/.tmp_asd_pdfs/2607.08093.html
- PDF / 本地文件路径：未归档PDF
- 当前状态：included
- 阅读日期：2026-10-22
- 笔记作者：Codex（读者证据包经主控审核整合）

## Evidence Log

| 判断项 | 结论 / 原文概括 | 证据位置 | 可信度 |
|---|---|---|---|
| 测试场景以SCM为隐藏真值。 | 每个场景结合结构因果模型、合成观测数据与领域故事。 | 全文§1及§3 | high |
| 任务包含因果层级及弃答。 | 对不可识别目标要求Agent abstain。 | 全文任务设计及Table 3 | high |
| Agent通过shell工具交互。 | mini-swe-agent在隔离容器内执行bash命令。 | 全文§3.7 | high |
| 评测数据规模为953个场景。 | 作者报告本轮构建953 scenes。 | 全文数据生成与评测节 | high |
| 比较12类Agent系统。 | 包括5个闭源与7个开放权重系统。 | 全文评测设置 | high |
| 作者承认合成现实性限制。 | 无人工评估领域可信度，生成机制覆盖有限。 | 全文§A.17 | medium |

## 0. 摘要翻译

CausalDS是数据科学Agent因果推理基准。每个任务结合结构因果模型、合成观测数据和领域故事，要求Agent使用命令行工具完成因果识别、估计、诊断或对不可识别问题弃答。953个场景以经验分布生成，作者承认尚无人类评估其现实可信度。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 当前判断：included；读者建议：included。
mini-swe-agent中的模型通过bash调用数据分析工具，在容器中进行多步因果分析、估计与弃答，符合工具使用和科学分析流程。

### 1.2 排除风险检查

建议01.03，研究对象是结构因果模型、识别与计算推断。合成故事虽基于真实领域分布，但不是实测农业或其它自然对象；不应按故事包装扩多个领域。01.04不适用，因为有具体形式模型任务；与11.07无关。
完整闭环不是纳入门槛；科研目标、多步行动、至少一项Agent能力及明确科研角色须同时成立。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：01
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：01（仅归档，不替代多模块事实）
- 模块内分类路径：01.03
- 分类深度：03/04使用二级；06/07使用固定三级；其余沿用现有树。
- 分类状态：原文证据复核

### 2.2 对象优先判定

953个合成场景，比较12个Agent（5闭源、7开放权重）；评估因果识别、估计、校准、弃答及工具效率，并做变量/故事改写稳定性检查。

### 2.3 容易混淆的边界

建议01.03，研究对象是结构因果模型、识别与计算推断。合成故事虽基于真实领域分布，但不是实测农业或其它自然对象；不应按故事包装扩多个领域。01.04不适用，因为有具体形式模型任务；与11.07无关。

## 3. Agent 系统与科研流程角色

mini-swe-agent中的模型通过bash调用数据分析工具，在容器中进行多步因果分析、估计与弃答，符合工具使用和科学分析流程。

科研流程与自主能力以本文实际行动和工具调用为依据：

生成包含SCM、观测数据与故事的任务；设因果层级、不可识别目标与abstention；mini-swe-agent在断网容器通过bash调用科学计算工具。

## 4. 方法设计

### 4.1 方法动机与设计

把因果推理、真实数据分析、工具使用、不确定性及弃答纳入可生成的Agent benchmark。

### 4.2 系统流程与组件

生成包含SCM、观测数据与故事的任务；设因果层级、不可识别目标与abstention；mini-swe-agent在断网容器通过bash调用科学计算工具。

## 5. 实验与验证

### 5.1 验证方式、对象及任务

953个合成场景，比较12个Agent（5闭源、7开放权重）；评估因果识别、估计、校准、弃答及工具效率，并做变量/故事改写稳定性检查。

### 5.2 基线、指标与结果

953个合成场景，比较12个Agent（5闭源、7开放权重）；评估因果识别、估计、校准、弃答及工具效率，并做变量/故事改写稳定性检查。

### 5.3 科学贡献与证据强度

把因果推理、真实数据分析、工具使用、不确定性及弃答纳入可生成的Agent benchmark。

证据层级：原始全文支持；作者报告结果不等于独立复现。

## 6. 与已有工作的关系

与因果推理benchmark、数据科学任务集及Agentic DS评测相邻；结合SCM真值与多步agent执行。

## 7. 局限性与风险

场景全部合成；未由人工评估故事与数据的领域可信度；机制注册表有限；部分消融规模小且只支持描述性结论。

## 8. 对综述写作的价值

有助于确定01.03计算对象与01.04通用研究Agent方法边界。

推荐引用强度：普通引用，可在核对原文后用于相应领域案例。

## 9. 总结

### 9.1 一句话概括

以因果分析任务评估数据科学Agent

### 9.2 速记版 pipeline

生成包含SCM、观测数据与故事的任务；设因果层级、不可识别目标与abstention；mini-swe-agent在断网容器通过bash调用科学计算工具。

### 9.3 标注字段汇总

```text
paper_id=ASD-0876
inclusion_status=included
scientific_object_modules=01
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=01
module_taxonomy_codes=01.03
source_level=fulltext
fulltext_followup_required=false
```

### 全文后续要求

本轮已读原始全文并完成对象分类；无需为纳入/分类另做全文补读。具体引用时仍需回查相应原文位置。


## 2026-10-29 PDF补齐归档

- 本地PDF：`Reference_PDF/01_Formal_Information_and_Computational_Sciences/ASD-0876_CausalDS_Benchmarking_Causal_Reasoning_in_Data_Science_Agents.pdf`，共74页；已核验标题、页面解析和逐页渲染。
- 下载来源：https://arxiv.org/pdf/2607.08093
- 版本：official arXiv preprint PDF; version as downloaded。
- 本轮为来源文件归档，不自动改变既有科学分类或将未决PR意见标记为已结案。
