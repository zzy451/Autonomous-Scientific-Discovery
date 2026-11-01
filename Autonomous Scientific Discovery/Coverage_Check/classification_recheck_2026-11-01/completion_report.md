# 剩余10篇分类缺项补证报告（2026-11-01）

> 后续同步（2026-11-01）：用户已裁定ChemCrow（ASD-0093）的化学/材料并行归属，材料三级补为04.04.05。当前剩余2篇二级、3篇三级缺项（4项映射）；正文、图表及中英文PDF已同步至最新核心库。本文保留当轮结果，最新状态见[本次裁决及同步报告](corpus_sync_report.md)与[最新清单](remaining_classification_queue.json)。

## 结果

逐项复核10篇论文的12项未完成映射，补齐6篇论文中的7项三级，其中2项同时补齐二级；另修正ASD-0873的化学二级暂存位置。没有删除模块或强行填平待核项。

| 指标 | 补证前 | 补证后 |
|---|---:|---:|
| 有二级缺项的论文 | 4 | 2 |
| 有三级缺项的论文 | 10 | 4 |
| 未完成三级的论文—模块映射 | 12 | 5 |
| 全部模块三级完整的正式学科论文 | 650/660 | 656/660 |
| 已完成二级的论文—模块映射 | 931/935 | 933/935 |
| 已完成三级的论文—模块映射 | 923/935 | 930/935 |

核心库仍为662篇，正式对象论文660篇、独立01.04为2篇、跨模块198篇、对象模块归属935项；needs_review为29篇，08仍覆盖9篇。本轮未进行新增文献搜索。

## 为什么此前留下缺项

缺项并不都表示未做分类。第一类是证据未展开：正文使用的外部基准或官方日志中已有可辨识对象，但前轮只查看领域总分。第二类是门槛过严：分类需要确认作者确实报告任务或结果，不能把独立复现也当作必需条件。第三类是真实信息缺口或对象边界：全文受阻、只公开汇总数量、计划与实跑无法对应，或化学分子与材料任务的界线仍不清楚。

## 已补齐条目

| 论文 | 原缺项原因 | 本轮补齐/修正 |
|---|---|---|
| ASD-0111 SciMaster: Towards general-purpose scientific AI agents, Part I. X-Master as foundation: Can we lead on Humanity's Last Exam? | 前轮只核对正文HLE/TRQA的聚合结果，未展开官方逐题执行日志。 | 06.01.06 遗传学 |
| ASD-0650 OpenEarth-Agent: From Tool Calling to Tool Creation for Open-Environment Earth Observation | 此前仅查看自建OpenEarth-Bench的农业占比，未展开论文实际评估的外部Earth-Bench任务。 | 08.01.08 农业气象学 |
| ASD-0845 SciDER: Scientific Data-centric End-to-end Researcher | 前轮将生成论文中的结果与独立执行日志一并作为门槛，忽略正文的完整执行声明。 | 11.05.04 学习分析 |
| ASD-0870 SR-Scientist: Scientific Equation Discovery With Agentic AI | 前轮只有领域数量与独立RL训练集变量描述，未核对实际测试集入口及其正式方程表。；缺少正式测试集的材料对象定义及方程，前轮未将训练和测试证据区分核实。 | 03.02.04 物理化学；04.01.01 材料物理 |
| ASD-0873 Large Knowledge Model: A Knowledge Foundation for Agentic Science at Scale | ChemBench总分支持化学，但前轮未展开题库配置和具体问题，03.01只是宽泛暂存。 | 03.02.03 分析化学 |
| ASD-1093 WhatWorkedBench: Benchmarking Experimental Understanding in AI Agents | 前轮缺少原始数据集标签的品种语义，未裁定作物学与种子科学边界。 | 08.01.07 种子科学与育种 |

ASD-0873由03.01化学总论与化学方法修正为03.02基础化学，代表三级为03.02.03分析化学；其他已存在的对象模块不变。ASD-1093补为更具体的种子科学，不扩大为遗传育种效果。

## 逐项依据与解释范围

### ASD-0093 / 模块04：04.01 / 三级待核

- 原因：色团分子的溶液吸收实验与独立材料任务之间的对象边界尚未裁定。
- 裁决：官方执行notebook进一步确认对象为乙腈溶液中的分子吸收波长预测、分子筛选及合成。该证据支持现有03分子设计；但当前04定义不要求薄膜或器件，不能仅因缺少薄膜实验撤回04，也不能仅凭光吸收把化学分子任务确定为材料任务。维持04.01及三级待核。
- 来源：Reference_PDF/03_Chemical_Sciences/Bran_2024_ChemCrow.pdf；位置：pp.3–4,19；原文：Use only data with acetonitrile as solvent.
- 来源：https://raw.githubusercontent.com/ur-whitelab/chemcrow-runs/500104ed9a5d479a8dc4128afc463625ade5a409/chromaphore-rf-369.ipynb；位置：code cell 1；原文：Chromophore；按Chromophore/Absorption max两列构建SMILES/MorganFingerprint与随机森林，再筛选接近369 nm的分子。
- 解释范围/仍需证据：需明确将此色团作为分子光学材料的独立任务依据；04.01.04与04.04.05目前均不能高置信确定。

### ASD-0111 / 模块06：06.01.06

- 原因：前轮只核对正文HLE/TRQA的聚合结果，未展开官方逐题执行日志。
- 裁决：官方X-Master日志记录LIG1扰动对肌强直性营养不良背景下CTG重复序列体细胞不稳定性的具体题目、工具执行及最终答案。重复序列遗传稳定性支持06.01.06遗传学；疾病背景或蛋白名称不替代其基础遗传机制对象。
- 来源：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Chai_2025_SciMaster.pdf；位置：pp.7–8；原文：including the identification of therapeutic targets, and biomedical mechanisms.
- 来源：https://raw.githubusercontent.com/sjtu-sai-agents/X-Master/658698387d28d2063bb76a3d7c2fa491b2e82c94/logs/example.jsonl；位置：physical line 2; id=67018145e8c125b41caa9ee3；原文：What is the impact of knocking out LIG1 on CTG somatic instability in the context of Myotonic dystrophy?；gt=D；4次代码工具行动；最终<answer>D. No impact</answer>。
- 解释范围/仍需证据：这是基础遗传学问答任务的Agent执行证据，不是Agent实施了基因敲除实验，也不独立验证题中生物学结论。

### ASD-0547 / 模块04：04.04 / 三级待核

- 原因：没有本地全文；SPIE页面访问受阻，元数据不足以细分器件材料。
- 裁决：重新访问Crossref、DOI落地页、SPIE全文/摘要及会议入口，Crossref仍仅有题名和出版元数据，SPIE返回Incapsula页面，OpenAlex没有摘要或开放全文位置。保留04.04，不能仅凭metasurface题名推定光电或半导体材料三级。
- 来源：https://api.crossref.org/works/10.1117/12.3091089；位置：message.title; resource.primary.URL；原文：Closed-loop experimental AI for pixelated metasurface design
- 来源：https://doi.org/10.1117/12.3091089；位置：resolved SPIE endpoint；原文：Incapsula；HTTP 200实际为访问拦截HTML，不是可读论文。
- 解释范围/仍需证据：仍需正文、完整官方摘要或作者公开版本，明确被制备/测量的材料与目标性能。

### ASD-0650 / 模块08：08.01.08

- 原因：此前仅查看自建OpenEarth-Bench的农业占比，未展开论文实际评估的外部Earth-Bench任务。
- 裁决：论文pp.10–11明确执行Earth-Bench跨基准评估并报告Table 3；该官方题库任务12以澳大利亚Murray–Darling作物热胁迫为对象，计算2023年1月LST>310 K且覆盖面积超过30%的天数。农业气象条件与作物胁迫支持08.01.08农业气象学。
- 来源：Reference_PDF/05_Earth_and_Environmental_Sciences/Zhao_2026_OpenEarth_Agent.pdf；位置：pp.10–11, §5.2, Table 3；原文：we conduct experiments on the cross-domain benchmark Earth-Bench
- 来源：https://raw.githubusercontent.com/opendatalab/Earth-Agent/ca1dfaef750654331308a434966d307f1728fd90/benchmark/question.json；位置：key 12; evaluation[1].question；原文：Based on thermal Band 31 and Band 32 data over the Murray–Darling Basin in Australia during January 2023, calculate how many days had more than 30% of the area with LST above 310 K, indicating heat stress on crops.
- 来源：https://huggingface.co/datasets/Sssunset/Earth-Bench/tree/49ce6b784c038b63b0817cbfa8211eb053b47e37/question12；位置：question12/2023_01_01_0050_BT_31.tif；原文：question12；数据快照最后修改2025-10-16，早于OpenEarth-Agent；该目录含138个影像文件。
- 解释范围/仍需证据：依据为实际执行的外部Earth-Bench，不是尚未开放的自建OpenEarth-Bench；没有逐题预测，不能宣称任务12被单独正确完成。任务2文案年份与影像年份不一致，未以其为主证据。

### ASD-0845 / 模块11：11.05.04

- 原因：前轮将生成论文中的结果与独立执行日志一并作为门槛，忽略正文的完整执行声明。
- 裁决：正文明确声明已完成方法设计、模型实现到定量评估的全流程；Fig.5报告ASSISTments 2009–2010少样本知识追踪的held-out结果，含三随机种子均值/标准差及ECE、Brier、AUC。对象是学生学习状态与知识追踪，可补11.05.04学习分析。
- 来源：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Unknown_2026_SciDER.pdf；位置：p.8；原文：SciDER executed the entire research pipeline from method design and model implementation to quantitative evaluation.
- 来源：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Unknown_2026_SciDER.pdf；位置：p.9, Fig.5；原文：Table 1: Held-out test performance on ASSISTments 2009–2010 few-shot episodes.；ECE=0.032、Brier=0.237；深度模型3 seeds。
- 解释范围/仍需证据：依据为作者报告的执行与结果；未独立复现，公开仓库未检得该教育案例的完整执行日志。

### ASD-0870 / 模块03：03.02.04

- 原因：前轮只有领域数量与独立RL训练集变量描述，未核对实际测试集入口及其正式方程表。
- 裁决：本文p.5实际评估LSR-Synth，官方推理预处理加载lsr_synth_chem_react。基准官方模块将对象定义为反应动力学的浓度变化速率、时间与浓度；基准作者论文Table 4公开CKR17、CKR22等反应速率方程。该对象支持03.02.04物理化学，不据动力学方程推定反应路径或机理实证。
- 来源：Reference_PDF/02_Physics_Astronomy_and_Cosmic_Sciences/Xia_2025_SR_Scientist.pdf；位置：pp.5–6, §4.1, Table 1；原文：We evaluate our methods on the synthetic part of the LLM-SRBench
- 来源：https://raw.githubusercontent.com/GAIR-NLP/SR-Scientist/00a44a11ff4bfd6e67cdfe8e6cc1ef5f5144b505/utils/data_preprocessing.py；位置：inference preprocessing；原文：for dataset_identifier in ['matsci','chem_react','bio_pop_growth','phys_osc']:
- 来源：https://raw.githubusercontent.com/deep-symbolic-mathematics/llm-srbench/6fdbe409b75ea749c0a93c69b6861637d804dec4/bench/datamodules.py；位置：ChemReactKineticsDataModule；原文：Rate of change of concentration in chemistry reaction kinetics
- 来源：https://arxiv.org/pdf/2504.10415；位置：benchmark paper, physical pp.14,24, Fig.9 and Table 4；原文：Chemistry: Reaction rate with respect to Time and Concentration；CKR17: −kA(t) + kf A(t)^0.33；CKR22: −kA(t)exp(−kst) + kqA(t)log(γt+1)。
- 解释范围/仍需证据：为合成方程任务的ID/OOD测试，不是新反应的湿实验发现；没有读取受限HF parquet；不以本文p.15独立RL训练示例替代测试证据。

### ASD-0870 / 模块04：04.01.01

- 原因：缺少正式测试集的材料对象定义及方程，前轮未将训练和测试证据区分核实。
- 裁决：本文实际测试LSR-Synth；官方推理入口加载matsci测试部分。基准作者论文Fig.9明确材料对象为应力随应变及温度变化，Table 4公开MatSci5、MatSci12等本构式，支持04.01.01材料物理。任务的物理语义已可识别，不必要求具体材料商品名。
- 来源：Reference_PDF/02_Physics_Astronomy_and_Cosmic_Sciences/Xia_2025_SR_Scientist.pdf；位置：pp.5–6, §4.1, Table 1；原文：material science
- 来源：https://raw.githubusercontent.com/GAIR-NLP/SR-Scientist/00a44a11ff4bfd6e67cdfe8e6cc1ef5f5144b505/utils/data_preprocessing.py；位置：inference preprocessing；原文：for dataset_identifier in ['matsci','chem_react','bio_pop_growth','phys_osc']:
- 来源：https://arxiv.org/pdf/2504.10415；位置：benchmark paper, physical pp.14,27, Fig.9 and Table 4；原文：Material Science: Stress with respect to Strain and Temperature；MatSci5: E0ε² + η(T−T0)log(ε+1)；MatSci12: Kε^N exp(−Q/(RT)) + ε³η(T−T0)。
- 解释范围/仍需证据：仅支持合成材料本构方程任务；不声称真实材料测量或实验室材料发现。

### ASD-0873 / 模块03：03.02.03

- 原因：ChemBench总分支持化学，但前轮未展开题库配置和具体问题，03.01只是宽泛暂存。
- 裁决：本文p.9评估ChemBench全量2785题并报告结果；官方题库九配置总数恰为2785，其中analytical_chemistry含152题，实际可核验NMR光谱信号判别题。按每模块一个代表位置，修正二级03.01为03.02基础化学，并补03.02.03分析化学。知识图谱架构本身不作为化学信息学分类证据。
- 来源：Reference_PDF/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/ASD-0873_Large_Knowledge_Model_A_Knowledge_Foundation_for_Agentic_Science_at_Scale.pdf；位置：p.9, §5.3 and Table 3；原文：For question answering, GPT-5.4 is fixed as the answering model on ChemBench (n=2,785)；无检索64.78，LKM 74.08；只变更检索来源。
- 来源：https://huggingface.co/datasets/jablonkagroup/ChemBench/resolve/6e1d25748952393f44e35b8e85bbe567246a6430/README.md；位置：dataset_info, nine configurations；原文：analytical_chemistry；题数152+1000+149+92+83+429+165+40+675=2785。
- 来源：https://datasets-server.huggingface.co/rows?dataset=jablonkagroup/ChemBench&config=analytical_chemistry&split=train&offset=0&length=1；位置：UUID 3d4326c7-0aaa-ed9e-ab64-9b140eccd056；原文：How many distinct signals are observed for the aldehyde \ce{(CH3)3CCH2CHO} in 1H NMR and 13C NMR spectra?；关键词nuclear magnetic resonance、NMR、analytical-chemistry；正确选项3个氢谱信号/4个碳谱信号。
- 解释范围/仍需证据：没有逐题运行UUID，不能宣称该NMR题被单独答对。HF题库存储分片名train不代表LKM用该题训练；本文明确用于QA评估。

### ASD-0919 / 模块05：二级及三级待核

- 原因：只有地学环境总量及USGS来源，没有具体任务变量与结果。
- 裁决：本轮另查官方HTML、LaTeX源包及附属文件入口，仍只有219个Earth science环境与USGS来源计数。唯一公开具体轨迹属于CDC FluView；没有USGS任务的变量、假设与结果，不能从机构名称推断水文学或空间信息分类。
- 来源：Reference_PDF/07_Medical_and_Health_Sciences/ASD-0919_Scaling_Scientific_Discovery_Environments_for_Turn_Level_Agentic_RL.pdf；位置：pp.12–13,17–18；原文：These counts are snapshot metadata for the environment corpus.
- 来源：https://arxiv.org/src/2607.28990v1；位置：acl_latex.tex, lines 570–589；原文：USGS；源包仅含正文、参考文献、样式和框架图，无逐任务目录。
- 解释范围/仍需证据：需公开地学任务目录或一条可辨识对象的实际轨迹。

### ASD-0919 / 模块11：11.01 / 三级待核

- 原因：经济环境数量及FRED来源只能支持经济学二级，缺具体经济问题。
- 裁决：新增检查官方源包后，仍未见FRED序列标识、经济假设及对应结果。保留11.01经济学；不能仅因采用统计方法或FRED数据就细分为计量经济学、金融学或劳动经济学。
- 来源：Reference_PDF/07_Medical_and_Health_Sciences/ASD-0919_Scaling_Scientific_Discovery_Environments_for_Turn_Level_Agentic_RL.pdf；位置：pp.12–13,17–18；原文：These counts are snapshot metadata for the environment corpus.
- 来源：https://arxiv.org/src/2607.28990v1；位置：acl_latex.tex, lines 570–589；原文：FRED；452个Economics环境为汇总元数据，未披露实际问题与变量。
- 解释范围/仍需证据：需实际经济任务问题、变量/序列及运行结果。

### ASD-0925 / 模块02：二级及三级待核

- 原因：正文仅有computational physics和Scientific Simulation标签，缺具体任务对应链。
- 裁决：官方仓库新增检得FHN/KS偏微分方程预测计划及Physical Modeling聚合结果，但该计划生成日期07-21晚于聚合结果截止日期07-10，无法证明计划被执行或对应正文4项Scientific Simulation。正文称30项复现含computational physics，附录具体清单却均为ML；本轮存在两种审查意见，主控按来源链尚未闭合保留待核。02.02.16计算物理学仅列候选。
- 来源：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Yu_2026_Beyond_Execution_Auditing_Experimental_Fidelity_in_LLM_Driven_Scientific_ASD0925.pdf；位置：p.5；原文：We construct a benchmark consisting of 30 distinct reproduction tasks derived from classic ML, computational physics, and bio-informatics domains
- 来源：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Yu_2026_Beyond_Execution_Auditing_Experimental_Fidelity_in_LLM_Driven_Scientific_ASD0925.pdf；位置：p.8, Table 4；原文：Scientific Simulation；4项任务，1项达到SOTA；没有对象清单。
- 来源：https://raw.githubusercontent.com/Flavorfish/AutoRepro/67ada1c0cfc3aa3b0304b1bf1a83786daf18ee27/data/naturebench_plans/nb_s42256-022-00464-w.yaml；位置：datasets; generation_metadata；原文：generated_at: '2026-07-21T10:07:51.867368'；fhn、ks_l22仅能确认任务计划定义。
- 来源：https://raw.githubusercontent.com/Flavorfish/AutoRepro/67ada1c0cfc3aa3b0304b1bf1a83786daf18ee27/NATUREBENCH_INTEGRATION.md；位置：实验结果汇总；原文：截至 2026-07-10；Physical Modeling聚合3次，未绑定具体计划。
- 解释范围/仍需证据：需正文4项任务ID与执行记录的对应；不得写成FHN/KS已执行或达到SOTA。

### ASD-1093 / 模块08：08.01.07

- 原因：前轮缺少原始数据集标签的品种语义，未裁定作物学与种子科学边界。
- 裁决：论文实际执行并冷回放全部native目录任务；UCI原始元数据明确Dry Bean为7个登记品种的种子形态分类，Seeds为Kama/Rosa/Canadian三品种小麦籽粒几何特征。论文以原始类别计算K-means聚类NMI。按更具体的种子形态/品种类别对象归08.01.07种子科学与育种。
- 来源：Reference_PDF/01_Formal_Information_and_Computational_Sciences/Ning_2026_WhatWorkedBench_Benchmarking_Experimental_Understanding_in_AI_Agents_ASD1093.pdf；位置：pp.4–6,15–16；原文：K-means fits the feature representation for each mask, and the original class labels enter the external NMI calculation.
- 来源：https://archive.ics.uci.edu/api/dataset?id=602；位置：data.additional_info.summary；原文：A computer vision system was developed to distinguish seven different registered varieties of dry beans with similar features in order to obtain uniform seed classification.
- 来源：https://archive.ics.uci.edu/api/dataset?id=236；位置：data.additional_info.summary；原文：The examined group comprised kernels belonging to three different varieties of wheat: Kama, Rosa and Canadian
- 解释范围/仍需证据：仅指种子形态与品种类别benchmark，不代表种子活力、遗传改良或育种效果验证；两项不属于正文108-episode核心Agent子集，归属依据为已执行native benchmark任务。

## 保留待核与边界裁决

| 论文 | 待核模块 | 尚缺层级 | 需要补充的证据 |
|---|---|---|---|
| ASD-0093 | 04 | 三级 | 需明确将此色团作为分子光学材料的独立任务依据；04.01.04与04.04.05目前均不能高置信确定。 |
| ASD-0547 | 04 | 三级 | 仍需正文、完整官方摘要或作者公开版本，明确被制备/测量的材料与目标性能。 |
| ASD-0919 | 05, 11 | 二级及三级 | 需公开地学任务目录或一条可辨识对象的实际轨迹。；需实际经济任务问题、变量/序列及运行结果。 |
| ASD-0925 | 02 | 二级及三级 | 需正文4项任务ID与执行记录的对应；不得写成FHN/KS已执行或达到SOTA。 |

ASD-0925存在两种审查意见：正文computational physics标签可被认为足以匹配宽泛的02.02.16；但附录任务清单及新增计划仍未建立对象—实跑—结果对应。主控采用较保守裁决，维持待核，不宣称FHN/KS已运行。ASD-0093也没有因缺少薄膜或器件而删除04；材料任务并不必然要求这两种形态。

当前没有足够证据支持重构一级分类，问题主要集中在边界解释与低覆盖类稀缺性判断。08不因低覆盖而扩大范围。

## 写回与验证

- 主事实源：主论文列表、进度镜像、模块分类账本及10篇笔记已同步；主归档二三级没有变化，稳定归档码及词表无需改动。
- 变更日志：CL-002776—CL-002785，保留逐篇owner前后状态、证据与笔记哈希。
- 已按export → check → build重建派生记录、清单及SQLite；检查器规则没有改动。
- `ERROR`: 0
- `WARNING`: 100
- `INFO`: 416
- 当前快照和README更新为补证后的缺项数；前一轮全量复核报告作为历史保留，并链接本报告。
- 正文、图表、Overleaf和中英文PDF的冻结语料版本不在本轮分类写回范围。

## 文件索引

- [12项机器可读裁决](completion_decisions.jsonl)
- [补证来源与下载哈希](completion_sources.json)
- [剩余4篇/5项清单](remaining_classification_queue.json)
- [最新分类快照](../core_classification_snapshot_2026-11-01.md)
