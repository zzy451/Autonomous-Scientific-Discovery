# Evaluating a 4B open-weights local LLM for agentic DFT workflows: a literature reproducibility audit

**论文信息**

- ID：ASD-0887
- 标题：Evaluating a 4B open-weights local LLM for agentic DFT workflows: a literature reproducibility audit
- 作者：Sharma, Shambhu Bhandari
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2608.29665
- 一手阅读来源：https://arxiv.org/html/2608.29665
- 来源层级：全文
- 阅读版本：对应缓存来源版本，参见Evidence Log
- 阅读版本题名：Evaluating a 4B open-weights local LLM for agentic DFT workflows: a literature reproducibility audit
- 原始全文缓存：C:/Users/20683/Desktop/综述/.tmp_asd_pdfs/2608.29665.html
- PDF / 本地文件路径：未归档PDF
- 当前状态：included
- 阅读日期：2026-10-22
- 笔记作者：Codex（读者证据包经主控审核整合）

## Evidence Log

| 判断项 | 结论 / 原文概括 | 证据位置 | 可信度 |
|---|---|---|---|
| 研究对象 | 任务聚焦二维五角材料及其晶格参数。 | Abstract | high |
| 端到端行动 | 提取文献参数、转为DFT输入并运行到收敛。 | Abstract | high |
| 约束架构 | Agent提出而确定性代码裁决；本地部署、证据grounding和多轮合并。 | Methods §2.1 | high |
| 抽取评测 | 201项专家判断；精确率95.7%、召回率67.3%。 | Abstract/Results §3 | high |
| 物理复算 | 57项中19项参数可复现；保留原型时晶格常数平均相对误差2.3%。 | Abstract/Conclusions | high |

## 0. 摘要翻译

本文评估本地Qwen3:4B自主科学流水线在二维五角材料文献复现中的表现。系统从文本提取参数、生成DFT输入并驱动模拟收敛；Agent提议而确定性代码把关，并用逐字引文定位和多轮推理降低结构错误。Extractor在201条专家判断上的精确率为95.7%、召回率67.3%；57项研究中19项原则上可复现；结构保留原型时晶格常数复算平均相对误差2.3%。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 当前判断：included；读者建议：included。
全流程Agent承担文献提取、模拟输入生成与DFT执行/收敛任务，具有工具调用和诊断反馈；对象为二维五角材料。

### 1.2 排除风险检查

对象是二维五角晶体和材料结构/晶格常数，归04.02；DFT与文本抽取是研究方法，不另归01或03。
完整闭环不是纳入门槛；科研目标、多步行动、至少一项Agent能力及明确科研角色须同时成立。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：04
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：04（仅归档，不替代多模块事实）
- 模块内分类路径：04.02
- 分类深度：03/04使用二级；06/07使用固定三级；其余沿用现有树。
- 分类状态：原文证据复核

### 2.2 对象优先判定

201项专家标注评估抽取（precision 95.7%, recall 67.3%）；审计57篇五角二维材料研究，其中19篇满足理论可复现参数报告标准；晶格常数复算在结构保留原型时平均相对误差2.3%。

### 2.3 容易混淆的边界

对象是二维五角晶体和材料结构/晶格常数，归04.02；DFT与文本抽取是研究方法，不另归01或03。

## 3. Agent 系统与科研流程角色

全流程Agent承担文献提取、模拟输入生成与DFT执行/收敛任务，具有工具调用和诊断反馈；对象为二维五角材料。

科研流程与自主能力以本文实际行动和工具调用为依据：

本地Qwen3:4B/Ollama；流水线获取文献、Agent抽参、转写SIESTA输入、DFT重算至收敛；诊断/评论Agent监测；确定性校验要求逐字引文和来源定位，并合并多轮提取结果。

## 4. 方法设计

### 4.1 方法动机与设计

展示小型本地模型在证据约束下驱动材料文献复现与DFT计算，并量化硬件对可靠性的影响。

### 4.2 系统流程与组件

本地Qwen3:4B/Ollama；流水线获取文献、Agent抽参、转写SIESTA输入、DFT重算至收敛；诊断/评论Agent监测；确定性校验要求逐字引文和来源定位，并合并多轮提取结果。

## 5. 实验与验证

### 5.1 验证方式、对象及任务

201项专家标注评估抽取（precision 95.7%, recall 67.3%）；审计57篇五角二维材料研究，其中19篇满足理论可复现参数报告标准；晶格常数复算在结构保留原型时平均相对误差2.3%。

### 5.2 基线、指标与结果

201项专家标注评估抽取（precision 95.7%, recall 67.3%）；审计57篇五角二维材料研究，其中19篇满足理论可复现参数报告标准；晶格常数复算在结构保留原型时平均相对误差2.3%。

### 5.3 科学贡献与证据强度

展示小型本地模型在证据约束下驱动材料文献复现与DFT计算，并量化硬件对可靠性的影响。

证据层级：原始全文支持；作者报告结果不等于独立复现。

## 6. 与已有工作的关系

与ASD-0022 ChemGraph、ASD-0217 Aitomia同属计算材料/化学Agent工作流；本文重点是本地部署和复现审计。

## 7. 局限性与风险

召回率偏低，缺失率只可作上界；单专家标签样本；文本未覆盖补充材料；缺少结构坐标会限制复现；小显存导致模型脆弱。

## 8. 对综述写作的价值

提供计算材料Agent复现性和本地小模型证据，同时提示谨慎解读数据充分性。

推荐引用强度：普通引用，可在核对原文后用于相应领域案例。

## 9. 总结

### 9.1 一句话概括

审计小模型DFT复现工作流

### 9.2 速记版 pipeline

本地Qwen3:4B/Ollama；流水线获取文献、Agent抽参、转写SIESTA输入、DFT重算至收敛；诊断/评论Agent监测；确定性校验要求逐字引文和来源定位，并合并多轮提取结果。

### 9.3 标注字段汇总

```text
paper_id=ASD-0887
inclusion_status=included
scientific_object_modules=04
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=04
module_taxonomy_codes=04.02
source_level=fulltext
fulltext_followup_required=false
```

### 全文后续要求

本轮已读原始全文并完成对象分类；无需为纳入/分类另做全文补读。具体引用时仍需回查相应原文位置。


## 2026-10-29 PDF补齐归档

- 本地PDF：`Reference_PDF/04_Materials_Science/ASD-0887_Evaluating_a_4B_open_weights_local_LLM_for_agentic_DFT_workflows_a_literature_reproducibility_audit.pdf`，共14页；已核验标题、页面解析和逐页渲染。
- 下载来源：https://arxiv.org/pdf/2608.29665
- 版本：official arXiv preprint PDF; version as downloaded。
- 本轮为来源文件归档，不自动改变既有科学分类或将未决PR意见标记为已结案。
