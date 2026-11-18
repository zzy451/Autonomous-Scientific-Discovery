# Autonomous Quantum Transport Measurements of 2D Semiconductors by an AI Agent

## 当前分类（2026-11-01 实证复核）

- 当前纳入状态：`included`；主归档：`02`。
- 本块为当前有效结论；后文既有分类、来源限制与审计判断均保留为历史记录，与本块不一致者由本块取代。
- 当前对象模块：`02;04`。
- 代表分类每个模块保留一个落点，不表示穷尽全文全部细类。

| 模块 | 二级 | 三级 | 本轮结论 |
|---|---|---|---|
| 04 | 04.04 能源、电子与器件材料 | 04.04.04 半导体材料 | 已落地 |
| 02 | 02.02 物理学 | 02.02.08 凝聚态物理学 | 已落地 |

- 模块04：MoS2器件实际量子输运测量及相图。
  - 证据：PDF 第 [1, 3, 4] 页；原文：We demonstrate this AI workflow on multiple monolayer and bilayer

- 完整裁决：`Coverage_Check/classification_recheck_2026-11-01/`。

## 既有笔记与历史审计记录

**论文信息**

- ID：ASD-0904
- 标题：Autonomous Quantum Transport Measurements of 2D Semiconductors by an AI Agent
- 作者：Bauer, Brandon; Whalen, Matthew; Watanabe, Kenji; Taniguchi, Takashi; Xiao, John Q.; Li, Tao E.; Zhao, Wenjin
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2609.26661
- 一手阅读来源：https://arxiv.org/abs/2609.26661v1
- 来源层级：全文
- 阅读版本：arXiv 2609.26661v1，完整13页PDF；/src端点实际返回PDF，已按真实格式检查。
- 阅读版本题名：Autonomous Quantum Transport Measurements of 2D Semiconductors by an AI Agent
- 原始全文缓存：C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/.tmp_asd_pdfs/recheck_0904.pdf
- PDF / 本地文件路径：Reference_PDF/02_Physics_Astronomy_and_Cosmic_Sciences/Bauer_2026_Autonomous_Quantum_Transport.pdf
- 当前状态：included
- 阅读日期：2026-10-22
- 笔记作者：Codex（读者证据包经主控审核整合）

## Evidence Log

| 判断项 | 结论 / 原文概括 | 证据位置 | 可信度 |
|---|---|---|---|
| 研究目标是量子输运测量与半导体物性表征 | 摘要直接说明量子输运测量，并报告自旋轨道耦合能及层/谷相图。 | Abstract，第1-3句 | high |
| Agent 进行多步且多日任务规划 | 原文称 performs multi-step, multi-day measurements end-to-end，并从规划测量开始。 | Abstract，第2句 | high |
| Agent 调用并安全操作实验工具 | 原文明确 safely operates the cryogenic instruments；说明FermiLink harness关注仪器安全和可靠性。 | Abstract，第2句及FermiLink说明 | high |
| 系统在真实二维器件上实验 | 实验多个 monolayer 和 bilayer MoS2 devices。 | Abstract，第3句 | high |
| 单层与双层器件分别有可识别结果 | 测得单层导带自旋轨道耦合能，映射双层的层/谷分辨相图。 | Abstract，第4句 | high |
| 长时执行规模已报告 | autonomous measurement campaigns lasting up to six days。 | Abstract，第4句 | high |
| FermiLink拆分设备长时轮询与Agent决策，并在多轮实验/分析间交接 | FermiLink在没有LLM运行时轮询仪器；每步完成后将数据和项目记忆交给分析Agent；测量Agent决定下一命令，循环无需人工介入。 | 正文 “Autonomous Experimentation Framework”, PDF pp. 3-4 | high |
| 设备安全通过冻结采集脚本和硬约束保证 | 所有硬件访问经冻结Python acquisition script；gate voltage、sweep rate、磁场和温度范围硬编码，Agent无法修改。 | 正文 “Autonomous Experimentation Framework”, PDF p. 4 | high |
| 单层MoS2 campaign量化导带自旋轨道劈裂 | 报告在载流子密度约3.4×10^12 cm^-2以下只有低导带占据，估算SOC splitting为13 meV。 | 正文 “Monolayer MoS2 Device Campaign”, PDF pp. 6-7 | high |
| 在低质量样品负例中Agent根据结果停止后续实验 | 第二个低质量单层器件未得到清晰FFT峰；Agent在后续扫描仍为负结果后跳过余下测量并报告无峰通过。 | 正文 “Monolayer MoS2 Device Campaign”, PDF p. 7 | high |
| 作者明确限定自主性范围 | 每种新二维器件的Agent Skill目前仍需专家用已有数据dry run协作开发；作者称当前自主性主要在执行和适配专家定义的工作流。 | 正文 “Discussion and Outlook”, PDF pp. 10-11 | high |

## 0. 摘要翻译

本文提出由 FermiLink harness 实现的量子输运实验 Agent 工作流。给定简短指令后，Agent 规划多步测量，安全操作低温仪器，分析数据并生成报告。作者在多个单层及双层 MoS2 器件上开展最长六天的自主测量，测定单层 MoS2 导带自旋轨道耦合能，并绘制双层 MoS2 层与谷分辨相图。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 当前判断：included；读者建议：included。
摘要及 arXiv Atom 原始记录均明确科研目标、多步行动、计划生成、真实仪器工具调用、长时自主执行、数据分析和研究流程角色，超过普通自动化脚本或单步问答。Agent 四项最低标准均有直接证据。

### 1.2 排除风险检查

保持02与04双模块。研究是MoS2二维量子材料器件的低温输运；量子振荡、SOC劈裂、层/谷占据和量子相图是凝聚态物理对象（02.02.08）。同时器件由明确的MoS2半导体材料组成，论文描述其晶格、能带、单/双层结构并对材料电子性质进行表征，满足04.04能源、电子与器件材料对象覆盖。主展示取02，因为研究问题/测量结果是量子物理性质；04作为真实样品材料模块并列保留。该判断有正文材料结构和具体器件实验支持，并非只由标题中的semiconductor触发。
完整闭环不是纳入门槛；科研目标、多步行动、至少一项Agent能力及明确科研角色须同时成立。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：02;04
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：02（仅归档，不替代多模块事实）
- 模块内分类路径：02.02.08; 04.04
- 分类深度：03/04使用二级；06/07使用固定三级；其余沿用现有树。
- 分类状态：原文证据复核

### 2.2 对象优先判定

模拟dry run后，在单层和双层MoS2器件上执行真实低温输运实验；单层包括良好器件及低质量器件负例，双层另在第二器件重复campaign。10 mK低温环境；测量含Rxx门电压依赖、Landau fan/FFT频率及Hall电阻/密度。单层得出低带占据阈值约3.4×10^12 cm^-2和SOC劈裂13 meV；低质量器件上Agent识别FFT证据不足并提前终止。双层测得hBN层厚比例/相边界，并构建n-E平面上的层与谷占据图。无独立专家操作时间/性能基线；与理论已知频率、Hall density和器件物理关系作内部交叉分析。

### 2.3 容易混淆的边界

保持02与04双模块。研究是MoS2二维量子材料器件的低温输运；量子振荡、SOC劈裂、层/谷占据和量子相图是凝聚态物理对象（02.02.08）。同时器件由明确的MoS2半导体材料组成，论文描述其晶格、能带、单/双层结构并对材料电子性质进行表征，满足04.04能源、电子与器件材料对象覆盖。主展示取02，因为研究问题/测量结果是量子物理性质；04作为真实样品材料模块并列保留。该判断有正文材料结构和具体器件实验支持，并非只由标题中的semiconductor触发。

## 3. Agent 系统与科研流程角色

摘要及 arXiv Atom 原始记录均明确科研目标、多步行动、计划生成、真实仪器工具调用、长时自主执行、数据分析和研究流程角色，超过普通自动化脚本或单步问答。Agent 四项最低标准均有直接证据。

科研流程与自主能力以本文实际行动和工具调用为依据：

完整方法：专家经验初始化假设驱动Agent Skills，并用已有测量数据做dry-run迭代技能；FermiLink在长时测量期间负责设备状态轮询和阶段交接，测量Agent提出每个针对性问题的参数扫描，固定Python脚本执行设备控制并实施硬安全阈值，分析Agent处理数据、计算FFT/Hall density、按接受标准选择继续、重测或停止。跨日以共享项目文件/记忆维持状态。基础Agent配置为Codex与gpt-5.5-xhigh。

## 4. 方法设计

### 4.1 方法动机与设计

展示 Agent 对低温实验设备进行多步长时量子输运测量，并产出二维半导体物性的实验结果。

### 4.2 系统流程与组件

完整方法：专家经验初始化假设驱动Agent Skills，并用已有测量数据做dry-run迭代技能；FermiLink在长时测量期间负责设备状态轮询和阶段交接，测量Agent提出每个针对性问题的参数扫描，固定Python脚本执行设备控制并实施硬安全阈值，分析Agent处理数据、计算FFT/Hall density、按接受标准选择继续、重测或停止。跨日以共享项目文件/记忆维持状态。基础Agent配置为Codex与gpt-5.5-xhigh。

## 5. 实验与验证

### 5.1 验证方式、对象及任务

模拟dry run后，在单层和双层MoS2器件上执行真实低温输运实验；单层包括良好器件及低质量器件负例，双层另在第二器件重复campaign。10 mK低温环境；测量含Rxx门电压依赖、Landau fan/FFT频率及Hall电阻/密度。单层得出低带占据阈值约3.4×10^12 cm^-2和SOC劈裂13 meV；低质量器件上Agent识别FFT证据不足并提前终止。双层测得hBN层厚比例/相边界，并构建n-E平面上的层与谷占据图。无独立专家操作时间/性能基线；与理论已知频率、Hall density和器件物理关系作内部交叉分析。

### 5.2 基线、指标与结果

模拟dry run后，在单层和双层MoS2器件上执行真实低温输运实验；单层包括良好器件及低质量器件负例，双层另在第二器件重复campaign。10 mK低温环境；测量含Rxx门电压依赖、Landau fan/FFT频率及Hall电阻/密度。单层得出低带占据阈值约3.4×10^12 cm^-2和SOC劈裂13 meV；低质量器件上Agent识别FFT证据不足并提前终止。双层测得hBN层厚比例/相边界，并构建n-E平面上的层与谷占据图。无独立专家操作时间/性能基线；与理论已知频率、Hall density和器件物理关系作内部交叉分析。

### 5.3 科学贡献与证据强度

展示 Agent 对低温实验设备进行多步长时量子输运测量，并产出二维半导体物性的实验结果。

证据层级：原始全文支持；作者报告结果不等于独立复现。

## 6. 与已有工作的关系

属于凝聚态/介观与纳米尺度物理中的自动化量子输运实验，也与自驱动实验室的实验仪器Agent相关。系统贡献重点是FermiLink控制和测量分析工作流。

## 7. 局限性与风险

作者明确承认：每种新二维器件仍需人类专家与Agent用存量数据共同开发和dry-run验证Agent Skills；已展示的自主性主要是执行与适配专家定义流程，而非从第一原理独立提出测量策略或科研问题。实验设备为受硬编码阈值保护的特定稀释制冷机/量子输运平台，向新器件泛化需重新验证。

## 8. 对综述写作的价值

高价值真实量子材料实验Agent和02/04边界案例；正文特别适合讨论多Agent阶段交接、硬件安全门、长时间自主测量，以及“执行已定义流程”与更强科学自主性之间的界限。

推荐引用强度：普通引用，可在核对原文后用于相应领域案例。

## 9. 总结

### 9.1 一句话概括

Agent开展多日量子输运测量

### 9.2 速记版 pipeline

完整方法：专家经验初始化假设驱动Agent Skills，并用已有测量数据做dry-run迭代技能；FermiLink在长时测量期间负责设备状态轮询和阶段交接，测量Agent提出每个针对性问题的参数扫描，固定Python脚本执行设备控制并实施硬安全阈值，分析Agent处理数据、计算FFT/Hall density、按接受标准选择继续、重测或停止。跨日以共享项目文件/记忆维持状态。基础Agent配置为Codex与gpt-5.5-xhigh。

### 9.3 标注字段汇总

```text
paper_id=ASD-0904
inclusion_status=included
scientific_object_modules=02;04
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=02
module_taxonomy_codes=02.02.08; 04.04
source_level=fulltext
fulltext_followup_required=false
```

### 全文后续要求

本轮已读原始全文并完成对象分类；无需为纳入/分类另做全文补读。具体引用时仍需回查相应原文位置。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O4 需物理检验 | 在单层和双层MoS2器件上执行量子输运测量，产生自旋轨道耦合能和层/谷相图等物性结果，需物理测量检验 | “测得单层导带自旋轨道耦合能，映射双层的层/谷分辨相图” · L48 |
| 验证强度 | V3 物理实验 | Agent在10 mK低温环境真实执行多日量子输运实验，测量Landau fan/FFT频率、Hall电阻等物理量 | “autonomous measurement campaigns lasting up to six days” · L49 |
| 系统自主性 | L2 闭环执行者 |  | — |

- 强验证（V3–V4）：是
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
