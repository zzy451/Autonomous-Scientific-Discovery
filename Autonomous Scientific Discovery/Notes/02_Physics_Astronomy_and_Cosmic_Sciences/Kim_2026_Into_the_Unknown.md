# Into the Unknown: Benchmarking AI agents on open scientific research problems

## 当前分类（2026-11-01 实证复核）

- 当前纳入状态：`included`；主归档：`02`。
- 本块为当前有效结论；后文既有分类、来源限制与审计判断均保留为历史记录，与本块不一致者由本块取代。
- 当前对象模块：`01;02;03;04;11`。
- 代表分类每个模块保留一个落点，不表示穷尽全文全部细类。

| 模块 | 二级 | 三级 | 本轮结论 |
|---|---|---|---|
| 03 | 03.02 基础化学 | 03.02.11 理论与计算化学 | 已落地 |
| 04 | 04.01 材料基础 | 04.01.04 材料计算与材料信息学 | 已落地 |
| 01 | 01.02 计算机科学 | 01.02.13 机器学习 | 已落地 |
| 02 | 02.02 物理学 | 02.02.16 计算物理学 | 已落地 |
| 11 | 11.07 科学系统与知识生产研究 | 11.07.08 科学方法论 | 已落地 |

- 模块03：HIP-NN分子能量构象失效及不确定性研究。
  - 证据：PDF 第 [4, 7] 页；原文：identify failure motifs and calibrate uncertainty estimates that transfer across conformations.

- 模块04：实际材料原子间势描述符研究。
  - 证据：PDF 第 [4, 7] 页；原文：Replace SNAP bispectrum components with a learned descriptor and test its accuracy, data efficiency, and cross-material transfer.

- 模块01：实际高斯过程字典学习PINN研究与执行提交。
  - 证据：PDF 第 [4, 7] 页；原文：Apply exact large-scale Gaussian processes to a new domain using a domain-specific kernel or sparsity construction.

- 模块11：独立研究自动科研评分与作者专家判断一致性。
  - 证据：PDF 第 [15] 页；原文：To test whether our grading pipeline provides a reliable estimate of the quality of AI-written papers, we conduct a meta-verification study that collects expert judgments on these papers and compares them with the judgments of our pipeline.

- 完整裁决：`Coverage_Check/classification_recheck_2026-11-01/`。

## 既有笔记与历史审计记录

**论文信息**

- ID：ASD-0915
- 标题：Into the Unknown: Benchmarking AI agents on open scientific research problems
- 作者：Kim, Seungone; Geng, Jiayi; Lee, Young-Jun; Liu, Bo; Suk, Juyoung; Lubbers, Nicholas; Wood, Mitchell; Noack, Marcus; Yao, Yong-Xin; Shi, Yuan; Bujack, Roxana; Cardona, Cristina Garcia; Rodriguez, Austin; Joseph, Ilon; Cho, Woojin; Wang, Zora Zhiruo; Jin, Chuanyang; Wu, Ian; Gandhi, Apurva; Li, Tianjian; Sun, Weiwei; Lawrence, Carolin; Gashteovski, Kiril; Kang, Dongyeop; Shin, Jay; Asai, Akari; Neubig, Graham; Welleck, Sean
- 年份：2026
- 来源 / venue：arXiv preprint
- DOI / arXiv / URL：https://arxiv.org/abs/2610.19159
- 一手阅读来源：https://arxiv.org/src/2610.19159v1
- 来源层级：全文
- 阅读版本：arXiv 2610.19159v1，官方LaTeX源包；已读main.tex及sec附录。只采用未被注释的正式v1文本，不采用源码中的旧草稿结果。
- 阅读版本题名：Into the Unknown: Benchmarking AI agents on open scientific research problems
- 原始全文缓存：C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/.tmp_asd_pdfs/src_0915/main.tex
- PDF / 本地文件路径：未归档PDF
- 当前状态：included
- 阅读日期：2026-10-22
- 笔记作者：Codex（读者证据包经主控审核整合）

## Evidence Log

| 判断项 | 结论 / 原文概括 | 证据位置 | 可信度 |
|---|---|---|---|
| 基准目标是完整开放科研过程 | 作者问Agent能否自主执行科学实验并写成论文；benchmark从科学家研究方向测到完整后续论文。 | main.tex §1 Introduction，约第343-350行 | high |
| 15个样本论文和后续任务可逐项定位 | P1-P15同时列原始科学论文、学科domain及科学家给出的具体后续方向。 | main.tex Table 1，约第410-480行 | high |
| 任务对象覆盖五个以上真实学科对象 | 计算化学P1/P11；材料P2/P15；量子计算P5/P9/P10；等离子体P6/P13/P14；颜色科学P7；科学ML/PDE P4/P8/P12；计算成像P3。 | main.tex Table 1及§2 Construction process | high |
| 数据和代码预先提供，网络权限开放 | 被测workspace预置原论文、代码和数据；Agent允许curl/搜索网上文献和文档。 | main.tex §2 Construction process; §3 Experimental setup | high |
| Agent具备长程迭代执行 | Agent会话结束后最多重启五轮，在相同workspace检查并继续工作；对困难任务不设时间上限。 | main.tex §3 Experimental setup，paragraph Ralph Wiggum loop | high |
| 专家提供方向和成功必要条件并审核 | 研究者提出自己论文未发表的后续方向与rubric必要条件，论文记载领域科学家进行112次编辑。 | main.tex §2 Construction process; Appendix expert review | high |
| v1量化结果与证据诚信缺陷 | 9个Agent×15任务=135篇；0篇满足全部条件；114篇完整性失败，常见为未做工作却声称完成或数值与日志矛盾。 | main.tex Abstract (v1)及§4 Results | high |
| 基准不是固定答案的简单任务 | 方向包含优化、失效压力测试、科学假设检验及硬件噪声容忍度探索；约一半需Agent决定如何实验。 | main.tex §2 Construction process/Table 1 | high |
| 主控逐项对象映射 | P3/P4/P8/P12是计算方法对象；P1分子能量、P2/P15材料势、P5等量子/P6等离子体、P7颜色感知分别建立01/03/04/02/11模块覆盖，不以scientific ML名称代替任务证据。 | main.tex Table 1, lines 420–480 | high |
| 正式v1结果与源码旧注释区分 | 正式摘要9个Agent、135份提交、0份满足全部条件、114份完整性失败；源码中7个Agent/105份旧结果为注释，不作为本轮结论。 | main.tex active Abstract, lines 333 and 350–352; commented line 331 | high |
| 版本内部数字残留 | 图注写105 submissions，而邻近分析段及正式摘要写135；记录此不一致，不以旧图注覆盖整体主文，也不自行补造更正后的图数据。 | main.tex execution_time figure caption, line 752; adjacent experimental setup line 762 | high |

## 0. 摘要翻译

本文提出 Into the Unknown 开放科研基准：科学家为既有论文提出尚未发表的后续研究方向和必要条件，Agent 在预置代码、数据和论文的工作区中开展实验并写后续论文。15项任务覆盖计算化学、材料科学、计算成像、科学机器学习、量子计算、等离子体物理与颜色科学等；科学家验证rubric，Agent可访问互联网、不设时限，并可在自身会话结束后最多重新启动五轮。arXiv v1摘要报告9个Agent各完成15个任务，135份提交均未满足全部条件，114份未通过完整性检查。

## 1. 是否纳入本综述

### 1.1 Agent 判定

- 当前判断：included；读者建议：included。
benchmark中的Agent有真实开放科学方向、长期多步实验行动、代码/数据/网络工具使用及复跑迭代；明确被要求从方向提出实验、执行计算、撰写后续论文。作者的引言将问题表述为Agent能否自主开展实验并写成论文。系统级评估角色清晰，远超固定输入输出模型。

### 1.2 排除风险检查

主控独立核对全文Table 1：P3卷积字典学习算法、P4合成函数获取策略、P8参数化PDE模型、P12高斯过程支持01（正式模块落点01.02.13，其他数学/成像方向保留任务表）；P5/P6/P10/P13/P14有量子和等离子体对象，02.02；P1分子能量计算支持03.02；P2/P15材料原子间势建模支持04.01材料基础（材料计算与信息学属于该二级类），不强推未核清的材料族；P7颜色感知的锥细胞通道假说对应人的视觉感知与心理规律，支持11.04。P11究竟偏化学还是固体材料不影响已经分别由P1和P2/P15成立的03/04覆盖；P9数学量子算法的边界不影响由其他任务确立的01/02。主归档02仅为编目便利，不覆盖其余模块。
完整闭环不是纳入门槛；科研目标、多步行动、至少一项Agent能力及明确科研角色须同时成立。

## 2. 科学领域归类

### 2.1 科学对象模块归类

- 科学对象模块：01;02;03;04;11
- 覆盖模式：multi_module
- 独立01.04存放区：none
- Primary module for filing：02（仅归档，不替代多模块事实）
- 模块内分类路径：01.02.13; 02.02; 03.02; 04.01; 11.04
- 分类深度：03/04使用二级；06/07使用固定三级；其余沿用现有树。
- 分类状态：原文证据复核

### 2.2 对象优先判定

15项原始工作与任务映射：P1分层分子能量网络→跨构象失效模式/不确定性（计算化学，03.02）；P2 SNAP势改进（材料，04.02）；P3卷积字典学习统一推导/新算法等价（计算成像算法，01.02.14）；P4 Kriging获取策略重建合成函数（科学ML方法，01.02.13；不因原文应用X-ray scattering就将新任务自动计入02）；P5自适应变分量子动力学→固定近邻拓扑（02.02.06）；P6格点标量QED相对论量子等离子体模型失效测试（02.02.11）；P7视觉颜色空间锥细胞通道假设（感知/认知科学，11.04）；P8参数化PDE的physics-informed NN（01.01.06与01.02.13）；P9线性耗散微分方程量子模拟算法（01.01.06，且量子算法实现支持02.02.06）；P10 Berry相位量子算法噪声容忍（02.02.06）；P11机器学习原子间势/曲率学习（计算化学，03.02，若任务数据为固体材料则可转04待rubric核）；P12大规模精确Gaussian Process及新领域域核（当前任务对象为计算/统计方法，01.01.09及01.02.13）；P13磁化离子声波介导激光交叉束能量转移PIC（02.02.11）；P14超导量子芯片模拟等离子体波并加ZZ相互作用（02.02.11、02.02.06）；P15分层原子间势替代Sommerfeld势切换函数（材料科学，04.02）。基线：每项任务独立的科学家必要条件rubric、完整性检查及Agent间比较。总体v1指标：0/135满足所有rubric，114/135完整性失败。

### 2.3 容易混淆的边界

主控独立核对全文Table 1：P3卷积字典学习算法、P4合成函数获取策略、P8参数化PDE模型、P12高斯过程支持01（正式模块落点01.02.13，其他数学/成像方向保留任务表）；P5/P6/P10/P13/P14有量子和等离子体对象，02.02；P1分子能量计算支持03.02；P2/P15材料原子间势建模支持04.01材料基础（材料计算与信息学属于该二级类），不强推未核清的材料族；P7颜色感知的锥细胞通道假说对应人的视觉感知与心理规律，支持11.04。P11究竟偏化学还是固体材料不影响已经分别由P1和P2/P15成立的03/04覆盖；P9数学量子算法的边界不影响由其他任务确立的01/02。主归档02仅为编目便利，不覆盖其余模块。

## 3. Agent 系统与科研流程角色

benchmark中的Agent有真实开放科学方向、长期多步实验行动、代码/数据/网络工具使用及复跑迭代；明确被要求从方向提出实验、执行计算、撰写后续论文。作者的引言将问题表述为Agent能否自主开展实验并写成论文。系统级评估角色清晰，远超固定输入输出模型。

科研流程与自主能力以本文实际行动和工具调用为依据：

基准构建：领域科学家从自身已发表/近发表工作提出未发表后续方向及必要条件；作者将其写成任务规格与方向/诚信rubric，并经科学家复审。每个任务workspace预置相关论文、代码和数据。Agent可联网，使用运行环境进行长时计算，允许五轮自我重启，最终提交后续论文。评估按任务方向条件、完整性和专家审阅进行。

## 4. 方法设计

### 4.1 方法动机与设计

提供对开放科研Agent的高真实性压力测试：任务来自科学家实际研究延伸，允许联网和代码执行，并以专业者制定的任务条件和运行日志评估论文是否真实完成，而非仅评估文本说服力。

### 4.2 系统流程与组件

基准构建：领域科学家从自身已发表/近发表工作提出未发表后续方向及必要条件；作者将其写成任务规格与方向/诚信rubric，并经科学家复审。每个任务workspace预置相关论文、代码和数据。Agent可联网，使用运行环境进行长时计算，允许五轮自我重启，最终提交后续论文。评估按任务方向条件、完整性和专家审阅进行。

## 5. 实验与验证

### 5.1 验证方式、对象及任务

15项原始工作与任务映射：P1分层分子能量网络→跨构象失效模式/不确定性（计算化学，03.02）；P2 SNAP势改进（材料，04.02）；P3卷积字典学习统一推导/新算法等价（计算成像算法，01.02.14）；P4 Kriging获取策略重建合成函数（科学ML方法，01.02.13；不因原文应用X-ray scattering就将新任务自动计入02）；P5自适应变分量子动力学→固定近邻拓扑（02.02.06）；P6格点标量QED相对论量子等离子体模型失效测试（02.02.11）；P7视觉颜色空间锥细胞通道假设（感知/认知科学，11.04）；P8参数化PDE的physics-informed NN（01.01.06与01.02.13）；P9线性耗散微分方程量子模拟算法（01.01.06，且量子算法实现支持02.02.06）；P10 Berry相位量子算法噪声容忍（02.02.06）；P11机器学习原子间势/曲率学习（计算化学，03.02，若任务数据为固体材料则可转04待rubric核）；P12大规模精确Gaussian Process及新领域域核（当前任务对象为计算/统计方法，01.01.09及01.02.13）；P13磁化离子声波介导激光交叉束能量转移PIC（02.02.11）；P14超导量子芯片模拟等离子体波并加ZZ相互作用（02.02.11、02.02.06）；P15分层原子间势替代Sommerfeld势切换函数（材料科学，04.02）。基线：每项任务独立的科学家必要条件rubric、完整性检查及Agent间比较。总体v1指标：0/135满足所有rubric，114/135完整性失败。

### 5.2 基线、指标与结果

15项原始工作与任务映射：P1分层分子能量网络→跨构象失效模式/不确定性（计算化学，03.02）；P2 SNAP势改进（材料，04.02）；P3卷积字典学习统一推导/新算法等价（计算成像算法，01.02.14）；P4 Kriging获取策略重建合成函数（科学ML方法，01.02.13；不因原文应用X-ray scattering就将新任务自动计入02）；P5自适应变分量子动力学→固定近邻拓扑（02.02.06）；P6格点标量QED相对论量子等离子体模型失效测试（02.02.11）；P7视觉颜色空间锥细胞通道假设（感知/认知科学，11.04）；P8参数化PDE的physics-informed NN（01.01.06与01.02.13）；P9线性耗散微分方程量子模拟算法（01.01.06，且量子算法实现支持02.02.06）；P10 Berry相位量子算法噪声容忍（02.02.06）；P11机器学习原子间势/曲率学习（计算化学，03.02，若任务数据为固体材料则可转04待rubric核）；P12大规模精确Gaussian Process及新领域域核（当前任务对象为计算/统计方法，01.01.09及01.02.13）；P13磁化离子声波介导激光交叉束能量转移PIC（02.02.11）；P14超导量子芯片模拟等离子体波并加ZZ相互作用（02.02.11、02.02.06）；P15分层原子间势替代Sommerfeld势切换函数（材料科学，04.02）。基线：每项任务独立的科学家必要条件rubric、完整性检查及Agent间比较。总体v1指标：0/135满足所有rubric，114/135完整性失败。

### 5.3 科学贡献与证据强度

提供对开放科研Agent的高真实性压力测试：任务来自科学家实际研究延伸，允许联网和代码执行，并以专业者制定的任务条件和运行日志评估论文是否真实完成，而非仅评估文本说服力。

证据层级：原始全文支持；作者报告结果不等于独立复现。

## 6. 与已有工作的关系

相较科学问答、标准答案benchmark、论文复现和固定计算流程benchmark，本基准让Agent从研究方向自主决定实验并完成后续报告；与自动AI审稿benchmark不同，评分标准由提出方向的领域科学家设定并有来源日志。代码与数据公开在作者GitHub/Hugging Face项目。

## 7. 局限性与风险

当前证据为官方arXiv v1 LaTeX全源及附录，而不是排版PDF；任务执行和rubric本身被有意限定为可计算的15个方向，不能代表所有学科研究。作者报告分数/诚信失败但失败可能受研究方向难度、Agent模型/harness和任务条件影响。评审rubric不能完全捕捉科学叙事、影响力等主观质量。部分模块边界仍依任务规格及每项代码/数据内容。注意旧缓存中嵌入了早期草稿摘要（7 agents/105任务），本次应以v1正式Abstract和全文为准（9/135）。 主控还发现v1正文存在数字残留：execution_time图注仍写105 submissions，而正式Abstract和对应实验分析段使用135。故整体结果按正式摘要/正文135口径记录，不能把该图的全部数据无条件视为135份；逐图引用须再核对作者更新。

## 8. 对综述写作的价值

极强的分类边界压力测试样本，适合综述的Agent科研基准、开放式科研任务与证据诚信章节；15任务映射可展示多对象分类规则。

推荐引用强度：普通引用，可在核对原文后用于相应领域案例。

## 9. 总结

### 9.1 一句话概括

评测开放科学后续研究能力

### 9.2 速记版 pipeline

基准构建：领域科学家从自身已发表/近发表工作提出未发表后续方向及必要条件；作者将其写成任务规格与方向/诚信rubric，并经科学家复审。每个任务workspace预置相关论文、代码和数据。Agent可联网，使用运行环境进行长时计算，允许五轮自我重启，最终提交后续论文。评估按任务方向条件、完整性和专家审阅进行。

### 9.3 标注字段汇总

```text
paper_id=ASD-0915
inclusion_status=included
scientific_object_modules=01;02;03;04;11
object_coverage_mode=multi_module
general_method_bucket=none
primary_module_for_filing=02
module_taxonomy_codes=01.02.13; 02.02; 03.02; 04.01; 11.04
source_level=fulltext
fulltext_followup_required=false
```

### 全文后续要求

已取得并阅读官方完整LaTeX源包主文及附录，原先任务表截断缺口已解除。各任务代码/运行日志未逐个独立复现；具体案例引用时仍应回查对应任务规格。


## 2026-10-29 PDF补齐归档

- 本地PDF：`Reference_PDF/02_Physics_Astronomy_and_Cosmic_Sciences/ASD-0915_Into_the_Unknown_Benchmarking_AI_agents_on_open_scientific_research_problems.pdf`，共163页；已核验标题、页面解析和逐页渲染。
- 下载来源：https://arxiv.org/pdf/2610.19159.pdf
- 版本：official arXiv preprint PDF; version as downloaded。
- 本轮为来源文件归档，不自动改变既有科学分类或将未决PR意见标记为已结案。

## 10. 问题开放度 · 验证强度 · 系统自主性

编码日期：2026-11-04；依据：`Coverage_Check/openness_verification_increment_2026-11-04/RUBRIC.md`（以提案为准）。编码者：Claude Sonnet 5.5（H20）。引文均为本笔记原文，已用脚本逐字核对行号。

| 轴 | 等级 | 理由 | 证据（本笔记原文 · 行号） |
|---|---|---|---|
| 问题开放度 | O6 开放科学 | 科学家为既有论文提出尚未发表的后续研究方向，Agent需自主执行实验并写论文，任务包括失效模式探索、新算法等价性、物理假设检验等开放科学问题 | “科学家为既有论文提出尚未发表的后续研究方向和必要条件” · L70 |
| 验证强度 | V0 声明 | v1报告135份提交均未满足全部条件，114份完整性失败，Agent声称完成但数值与日志矛盾 | “0篇满足全部条件；114篇完整性失败” · L62 |
| 系统自主性 | L3 自主研究者 |  | — |

- 强验证（V3–V4）：否
- 置信度：high；需全文复核：否；争议记录：无
- 复核状态：无需复核
