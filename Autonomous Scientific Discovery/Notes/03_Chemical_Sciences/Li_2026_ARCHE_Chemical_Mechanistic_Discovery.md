# Autonomous Chemical Mechanistic Discovery through Agentic Reasoning and Validation

**论文信息**

- ID：ASD-0881
- 标题：Autonomous Chemical Mechanistic Discovery through Agentic Reasoning and Validation
- 作者：Li, Dong; Mi, Sixuan; Ye, Zihao; Xiong, Huan; XU, Tao; Zhu, Tong; Zhang, Aijia; Gao, Junqi; Zhang, Kaiyan; Wang, Shijie; Zhou, Bowen; Li, Yuqiang; Qi, Biqing
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2609.11147
- 一手阅读来源：https://arxiv.org/abs/2609.11147
- 来源层级：全文
- 阅读版本：arXiv 2609.11147全文PDF，194页（含补充材料）；题名与作者已核对。原ARCHE与后续Arche-Harness实现版本分开记录。
- 阅读版本题名：Autonomous Chemical Mechanistic Discovery through Agentic Reasoning and Validation
- 原始全文缓存：C:/Users/20683/Desktop/综述/.tmp_asd_pdfs/2609.11147.pdf
- PDF / 本地文件路径：Reference_PDF/03_Chemical_Sciences/Li_2026_ARCHE_Chemical_Mechanistic_Discovery.pdf
- 当前状态：included
- 阅读日期：2026-10-22
- 笔记作者：Codex（读者证据包经主控审核整合）

## Evidence Log

| 判断项 | 结论 / 原文概括 | 证据位置 | 可信度 |
|---|---|---|---|
| 论文系统及Agent闭环 | 通用推理模型负责规划，ARCHE-Chem检查Gaussian输入和输出，工具注册表执行计算；Agent根据失败诊断和计算结果修改假设及工作流。 | Paper PDF, Abstract; Results, ARCHE System Architecture; Supplementary A1.1 | high |
| 案例1：非对称aldol过渡态 | 论文称ARCHE找回文献报告的9个过渡态并识别3个额外候选；TS-2a/TS-2b骨架RMSD为0.01/0.15 Å，计算ΔΔG‡为1.9 kcal/mol，对照实验推算的1.6 kcal/mol。 | Paper PDF, Results, Revisiting a reported vicinal diamine-catalysed aldol reaction; Supplementary B.1.1 | high |
| 案例2：光致C–I断裂 | Agent在初始激发态假设未获支持后反思并修订模型；后续计算得到约64.0 kcal/mol激发能，接近450 nm光子能量63.6 kcal/mol，并提出光致均裂启动路径。 | Paper PDF, Results, Uncovering a mechanism for the photochemical C–I cleavage reaction; Supplementary B.1.2 | high |
| 案例3：镍催化迁移偶联选择性 | 规划器将候选构象假设转成受控几何畸变和二面角扫描，收敛到Br–N–N–H二面角畸变能；邻位甲基配体显示较低畸变代价，并对应迁移产物选择性。 | Paper PDF, Results, Abstracting a selectivity descriptor in nickel-catalysed migratory cross-coupling; Supplementary B.1.3 | high |
| 原始ARCHE仓库与计算数据 | 原始仓库README称results为作者运行结果；SI C.10说明三个公开JSON由Gaussian输出经cclib解析，包含几何、能量、热化学和激发态数据。GitHub递归树被截断，因此目录清单不完整；README与三个JSON可用。 | Original ARCHE repository README; supplementary/case1.json, case2.json, case3.json; Paper SI C.10 | high |
| Arche-Harness版本边界 | arXiv链接的Arche-Harness是关联的另一仓库，README称其基于原ARCHE重构规划、执行和反思流程；其MiniChem实现及后续验证不直接等同论文版本或论文实验。 | arXiv linked repository JetAstra/Arche-Harness README and validation documents | high |

## 0. 摘要翻译

ARCHE把通用推理模型、领域模型ARCHE-Chem和结构化工具注册表组合成反应机理研究Agent。系统提出并排序假设、规划计算工作流，并依据计算结果反思修订。论文通过三类任务验证：非对称aldol反应的立体选择性过渡态重建、α-碘硼酸酯的光化学C–I断裂路径，以及镍催化迁移偶联的选择性描述符。原始ARCHE仓库公开结构化Gaussian计算结果；后续Arche-Harness重构项目的能力不倒推为原论文结果。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 当前判断：included；读者建议：included。
完整论文及补充材料明确给出科研目标、假设生成排序、计算规划执行、失败诊断和基于计算证据的反思。Agent承担反应机理与催化选择性研究角色，满足四项最低纳入标准；原文与原始代码数据分别作为方法和实现证据。

### 1.2 排除风险检查

The three research objects concern reaction mechanisms, catalytic selectivity, transition states, and molecular or complex electronic structure, fitting 03.03. Excited-state calculations support the alpha-iodoboronate mechanism and do not constitute independent condensed-matter materials research.
完整闭环不是纳入门槛；科研目标、多步行动、至少一项Agent能力及明确科研角色须同时成立。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：03
- 覆盖模式：single_module
- 独立01.04存放区：none
- Primary module for filing：03（仅归档，不替代多模块事实）
- 模块内分类路径：03.03
- 分类深度：03/04使用二级；06/07使用固定三级；其余沿用现有树。
- 分类状态：原文证据复核

### 2.2 对象优先判定

作者报告找回文献9个aldol过渡态并发现3个额外候选，主要/次要过渡态骨架RMSD为0.01/0.15 Å；计算ΔΔG‡为1.9 kcal/mol，对照实验推算1.6 kcal/mol。光化学案例约64.0 kcal/mol激发能与450 nm光子能量63.6 kcal/mol相近；镍催化案例提出Br–N–N–H二面角畸变能描述符。补充材料C.10将case1/2/3 JSON说明为cclib解析的Gaussian输出。这些是作者报告的计算验证，本轮未独立重算。

### 2.3 容易混淆的边界

The three research objects concern reaction mechanisms, catalytic selectivity, transition states, and molecular or complex electronic structure, fitting 03.03. Excited-state calculations support the alpha-iodoboronate mechanism and do not constitute independent condensed-matter materials research.

## 3. Agent 系统与科研流程角色

完整论文及补充材料明确给出科研目标、假设生成排序、计算规划执行、失败诊断和基于计算证据的反思。Agent承担反应机理与催化选择性研究角色，满足四项最低纳入标准；原文与原始代码数据分别作为方法和实现证据。

科研流程与自主能力以本文实际行动和工具调用为依据：

通用推理模型提出和排序机理假设，将其转换为量子化学计算任务；ARCHE-Chem支持Gaussian输入检查与输出解释，工具注册表连接计算流程。系统由规划、执行和反思模块协作，诊断计算失败并修订路径。三类案例分别采用过渡态与自由能分析、激发态及均裂路径计算、镍配合物受控几何/二面角扫描。原始仓库JSON是Gaussian输出解析数据，Arche-Harness属于后续相关实现。

## 4. 方法设计

### 4.1 方法动机与设计

The agent coordinates computational chemistry tools, generates mechanistic hypotheses, plans and runs computational validation, and revises conclusions from evidence. The paper demonstrates the tool workflow across three chemistry cases.

### 4.2 系统流程与组件

通用推理模型提出和排序机理假设，将其转换为量子化学计算任务；ARCHE-Chem支持Gaussian输入检查与输出解释，工具注册表连接计算流程。系统由规划、执行和反思模块协作，诊断计算失败并修订路径。三类案例分别采用过渡态与自由能分析、激发态及均裂路径计算、镍配合物受控几何/二面角扫描。原始仓库JSON是Gaussian输出解析数据，Arche-Harness属于后续相关实现。

## 5. 实验与验证

### 5.1 验证方式、对象及任务

作者报告找回文献9个aldol过渡态并发现3个额外候选，主要/次要过渡态骨架RMSD为0.01/0.15 Å；计算ΔΔG‡为1.9 kcal/mol，对照实验推算1.6 kcal/mol。光化学案例约64.0 kcal/mol激发能与450 nm光子能量63.6 kcal/mol相近；镍催化案例提出Br–N–N–H二面角畸变能描述符。补充材料C.10将case1/2/3 JSON说明为cclib解析的Gaussian输出。这些是作者报告的计算验证，本轮未独立重算。

### 5.2 基线、指标与结果

作者报告找回文献9个aldol过渡态并发现3个额外候选，主要/次要过渡态骨架RMSD为0.01/0.15 Å；计算ΔΔG‡为1.9 kcal/mol，对照实验推算1.6 kcal/mol。光化学案例约64.0 kcal/mol激发能与450 nm光子能量63.6 kcal/mol相近；镍催化案例提出Br–N–N–H二面角畸变能描述符。补充材料C.10将case1/2/3 JSON说明为cclib解析的Gaussian输出。这些是作者报告的计算验证，本轮未独立重算。

### 5.3 科学贡献与证据强度

The agent coordinates computational chemistry tools, generates mechanistic hypotheses, plans and runs computational validation, and revises conclusions from evidence. The paper demonstrates the tool workflow across three chemistry cases.

证据层级：原始全文支持；作者报告结果不等于独立复现。

## 6. 与已有工作的关系

Related to ASD-0664 on autonomous computational catalysis. ARCHE focuses on reaction mechanisms and catalytic selectivity. Arche-Harness is a later refactoring based on original ARCHE code; its full capabilities are not attributed to the paper version.

## 7. 局限性与风险

论文与补充材料已取得，但作者运行结果不等于独立复现。原始仓库递归目录API返回截断清单，主控未据此声称已获得全部计算输入/日志；README和三个case JSON可读。Arche-Harness为后续重构项目，其MiniChem与分步验证结果不等同论文原始实验。对模型、人工参与和不同反应体系的外推需结合具体案例评估。

## 8. 对综述写作的价值

A 03.03 agent case study combining mechanistic hypotheses, computational tools, and interpretable selectivity, with evidence separated across the paper, original repository data, and later refactoring.

推荐引用强度：普通引用，可在核对原文后用于相应领域案例。

## 9. 总结

### 9.1 一句话概括

Agent辅助化学机制发现

### 9.2 速记版 pipeline

通用推理模型提出和排序机理假设，将其转换为量子化学计算任务；ARCHE-Chem支持Gaussian输入检查与输出解释，工具注册表连接计算流程。系统由规划、执行和反思模块协作，诊断计算失败并修订路径。三类案例分别采用过渡态与自由能分析、激发态及均裂路径计算、镍配合物受控几何/二面角扫描。原始仓库JSON是Gaussian输出解析数据，Arche-Harness属于后续相关实现。

### 9.3 标注字段汇总

```text
paper_id=ASD-0881
inclusion_status=included
scientific_object_modules=03
object_coverage_mode=single_module
general_method_bucket=none
primary_module_for_filing=03
module_taxonomy_codes=03.03
source_level=fulltext
fulltext_followup_required=false
```

### 全文后续要求

本轮已取得并阅读论文及补充材料，原先全文缺失标记已解除；具体数值引用可回查案例正文和SI C.10。未执行Gaussian计算的独立复现。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O3 新实例 | 恢复已知反应机理并提出新过渡态候选 | “找回文献9个aldol过渡态并发现3个额外候选” · L62 |
| 验证强度 | V2 计算/仿真/回顾性 | 计算验证，ΔΔG‡为1.9对照实验1.6 kcal/mol | “计算ΔΔG‡为1.9 kcal/mol，对照实验推算的1.6” · L26 |
| 系统自主性 | L2 闭环执行者 | agent根据计算反馈反思并修订机理假设 | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
