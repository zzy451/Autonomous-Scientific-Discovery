# 十月第二轮广泛文献检索与候选分流（2026-10-22）

## 本轮结果

基线922条记录、494篇确认核心；本轮新增登记211条，其中候选candidate 144、待核needs_review 54、背景background_only 8、排除excluded 5。因此新增待阅读/审查队列为198篇，而非把全部登记记录都称作已纳入论文。全库现为1133条；没有核心晋升，确认核心仍494，既有核心缺笔记数仍0。新增候选尚未制作正式全文笔记。

ID范围：ASD-0923—ASD-1133。全库按DOI、arXiv ID（去版本号）、题名、已登记别名/出版DOI和相似题名核对；主控最终合并8次既有论文命中（不同来源重复命中次数，不等于不同论文数）。各组间相同记录合并保留多条来源轨迹。

## 时间口径

主窗口为2026-08-01至2026-10-22；另单列2026-07-08至07-31补漏。不是完整年度普查，也不以50篇或其他固定数量为配额。arXiv用官方首次提交日期；期刊/DOI日期仅表示当前可核出版版本，不保证首次公开就在这个窗口。较早预印本或改题版本未全部排除。

| 时间层 | 登记数 |
|---|---|
| 8—10月首次提交（arXiv） | 135 |
| 7月首次提交补漏（arXiv） | 8 |
| 7月当前出版版本补漏，更早谱系待核 | 11 |
| 8—10月当前出版/预印本DOI版本，更早谱系待核 | 56 |
| 精确日期仍待核 | 1 |

## 来源与筛选方法

继续使用六个gpt-6-luna/high领域分组；主控单写master并独立核对一手来源。期刊入口从Nature/Science及学科期刊开始，结合种子论文/作者/系统的引用与同项目扩展，再以arXiv、Europe PMC、Crossref和OpenAlex做薄弱学科补查。查询原始命中、实际返回、限流和逐条分流保存在各组JSON/log；原始命中不同查询大量重叠，不能相加当作读过或新增的篇数。

主控期刊检索先执行8个Crossref入口查询，再扩大Nature题名agent/autonomous及Oxford题名agent查询；三项扩大查询分别返回118/76/49条，与当次接口报告总量一致。综合初始查询并对全库精确去重后保留313条含混关键词命中；其中大量是生物活性制剂、自动驾驶或一般运维，并非313篇达标科研Agent论文。Elsevier扩大查询遇TLS错误，初轮Elsevier前100结果仍有召回上限。原始记录位于`.tmp_asd_pdfs/round2_journals/harvest_expanded.json`。

候选资格按明确科研目标、多步行动、至少一种规划/工具/反馈/决策/协作能力、科研流程角色四项判定。不要求LLM或完整发现闭环；也不因名称有agent或autonomous就通过。传统ABM、RL主动感知、BO实验选择和临床自动化均须区分其实际行动与科研角色。

## 各模块增加的研究队列

下表仅统计candidate/needs_review，按所有暂支持模块计数；一篇可多模块，列和不等于论文总数。分类仍为摘要/部分全文任务证据下的暂定映射，未写入确认核心ledger。03/04最多二级；06/07按已有固定三级，证据不足者保留待核。

| 模块 | 领域 | 候选/待审覆盖数 |
|---|---|---|
| 01 | 形式、信息与计算科学 | 51 |
| 02 | 物理、天文与宇宙科学 | 27 |
| 03 | 化学科学 | 9 |
| 04 | 材料科学 | 38 |
| 05 | 地球与环境科学 | 10 |
| 06 | 生命科学 | 24 |
| 07 | 医学与健康科学 | 29 |
| 08 | 农业、食品、林牧渔业 | 5 |
| 09 | 工程与工业技术 | 20 |
| 10 | 航空航天海洋交通 | 4 |
| 11 | 社会行为经济与知识系统 | 26 |

## 复核修正与薄弱方向

- E组原先排除的奶牛场减排肥料ABM与RAVA植物病害主动视觉，经独立复核改为needs_review；牛呼吸病会议摘要也保留边界线索。农场15年决策、社会传播和经验校准，及RAVA的序贯视野策略，都不能因非LLM一刀切排除。08有新增研究队列，但没有新增确认核心。
- 生物细胞ABM、ASCENT种群仿真及部分金融/社会ABM保留待审，具体区分“承担科研行动”与“仅是被模拟实体”；不先行确认，也不按传统Agent类型直接否定。
- WhatWorkedBench、SEE、K-Bench和OpenDiscoveryTrace有明确对象级任务，撤销01.04-only建议；SAIL按已核科研代码/文献任务暂记01/11，其余域待清单。TruthInsightBench等确有对象任务但域清单不足时保留分类待核，不能把01.04当作未知类别。
- Biomni的Science正式标题/DOI并入ASD-0118；Virtual Biotech、scBaseCount、Perturb-ME和GBClaw等既有记录均未新建重复ID。7月首发、8月更新的开放式AI研究论文按7月补漏登记，更新本身不算8月首发。

## 召回与证据限制

这仍是一轮扩大检索，不声称穷尽两个月所有论文。OpenAlex/Semantic Scholar/arXiv部分接口返回429，部分请求有TLS/403问题；各组有每页/每查询返回上限。A组前期OpenAlex原始缓存缺失的汇总不能复核，7月169条线索未审完，日志已标明，不拿它们充当已筛论文。D组前序摘要中的未留存查询量不作为本轮已完成量。正式可核输出、主控来源缓存及尚待二次判读的记录分别保留。

期刊当前出版日期与预印本首次提交日期不混算；主控取得元数据不代表已阅读全文。精确任务域、Agent资格、边界类别和旧预印本谱系仍须后续全文审查。新增论文的正式笔记为下一轮工作，未伪造阅读完成状态。

## 逐条新增登记

| ID | 论文 | 状态 | 日期 | 暂定模块 | 归档二级/三级 | 依据与待核点 |
|---|---|---|---|---|---|---|
| ASD-0923 | [Training AI Scientists to Replicate Research](https://arxiv.org/abs/2608.13331) | candidate | 2026-08-13 | 11 | 11.07 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0924 | [SGHA: Evidence-Grounded Research Problem Discovery with Local Language Models](https://arxiv.org/abs/2608.17501) | candidate | 2026-08-18 | 01 | 01.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0925 | [Beyond Execution: Auditing Experimental Fidelity in LLM-Driven Scientific Research](https://arxiv.org/abs/2608.26753) | candidate | 2026-08-27 | 01 | 01.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0926 | [AutoData: Agentic Search for Pre-training Data Selection](https://arxiv.org/abs/2609.19754) | candidate | 2026-09-17 | 01 | 01.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0927 | [ScientistTwo: Pioneering the Human Knowledge Frontier with Autonomous AI](https://arxiv.org/abs/2609.19644) | candidate | 2026-09-17 | 01 | 01.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0928 | [EviGraph: Evidence-Guided Autonomous Research Agents](https://arxiv.org/abs/2608.04738) | candidate | 2026-08-05 | 01 | 01.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0929 | [Learning What to Investigate Next: Meta-Reasoning for Long-Horizon Research Agents](https://arxiv.org/abs/2610.02525) | candidate | 2026-10-01 | 01 | 01.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0930 | [ExpEvolve: Structuring and Reusing Experience for Open-Ended Discovery](https://arxiv.org/abs/2610.29303) | candidate | 2026-10-21 | 01 | 01.01 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0931 | [Can AI agents conduct open-ended AI research? Early evidence from two case studies](https://arxiv.org/abs/2607.27191) | candidate | 2026-07-29 | 01 | 01.02 | 7月29日首发、8月更新；未匹配既有922记录，作为7月遗漏的新入库工作，不能把v2更新计入8月首发增量。 |
| ASD-0932 | [The Agentic Scientist: Orchestrating Coding Agents for Automated Scientific (Co-)Discovery](https://arxiv.org/abs/2610.18933) | candidate | 2026-10-13 | 01 | 01.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0933 | [JANUS: Enhancing Long-Horizon Autonomous Research with Co-Evolving World Models](https://arxiv.org/abs/2610.13194) | candidate | 2026-10-09 | 01 | 01.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0934 | [YouRA: A Persistent-State Architecture for Evidence-Traceable Autonomous Research Agents](https://arxiv.org/abs/2610.01097) | candidate | 2026-10-01 | 01 | 01.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0935 | [DataSense-Bench: The First Step Toward an AI Scientist](https://arxiv.org/abs/2610.12190) | candidate | 2026-10-08 | 01 | 01.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0936 | [PaperGym: Rubric-Centered Evolution for Research-Plan Generation](https://arxiv.org/abs/2608.31119) | needs_review | 2026-08-31 | 11 | 11.07 | PaperGym按科研目标/方法/实验分别构造研究计划训练及评分语料，暂归科研方法与知识生产；科学计划是否有多步Agent执行仍待全文。 |
| ASD-0937 | [AppliedScientist: Automated Scientific Revision Through Iterative AI Reviewing](https://arxiv.org/abs/2609.14738) | candidate | 2026-09-13 | 11 | 11.07 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0938 | [Learning to Evaluate Before Improving: Automatic Rubric Induction for Automatic Research Agents](https://arxiv.org/abs/2608.31076) | needs_review | 2026-08-31 | 对象映射待核 |  | AutoSciRub有执行与反馈迭代，并在ResearchClawBench及AstaBench上评测；实际任务对象清单未核全，暂不填无对象01.04。 |
| ASD-0939 | [HypoForge: A Self-Improving Multi-Agent Framework for Automated Hypothesis Generation and Testing via Scientific Skill Learning](https://arxiv.org/abs/2608.25770) | needs_review | 2026-08-26 | 对象映射待核 |  | HypoForge假设生成和检验Agent有经验反馈，但摘要未列测试对象；实际任务域映射待核，不以通用方法替代对象分类。 |
| ASD-0940 | [OmniScientist: An Omni-Modal Omni-Discipline AI Scientist](https://arxiv.org/abs/2608.13558) | candidate | 2026-08-13 | 01;02;03;04;05;06;07;08;09;10 | 01.02 | OmniScientist官方Table 1列36个实际案例，覆盖光谱/分子/材料、天文地球、生命医学、农业生态、制造交通与计算任务；按这些案例暂作01—10多模块，归档01仅为编目便利，细分映射仍待核。 |
| ASD-0941 | [Can AI Agents Make Open-Ended Scientific Discovery? Evidence from Station](https://arxiv.org/abs/2610.08927) | needs_review | 2026-10-06 | 01 | 01.02 | Station摘要明确ICLR来源的开放式机器学习问题与实验，现有证据不足以添加D组建议的独立物理02。 |
| ASD-0942 | [Can AI Scientists Coordinate at Runtime?](https://arxiv.org/abs/2610.00980) | needs_review | 2026-10-01 | 对象映射待核 |  | RAC在三个AI科学家宿主和ResearchClawBench上进行运行时协调评测；任务对象尚未明确，留作分类待核。 |
| ASD-0943 | [Epi: Towards a Persistent, Self-Improving Agent for Autonomous Research](https://arxiv.org/abs/2610.24944) | candidate | 2026-10-18 | 01;09;10 | 01.01 | Épi给出组合数学界与证明，并在30项FrontierOR任务开发车辆路径、排程和生产计划求解器；数学为主，工程和运输覆盖仍需逐任务细核。 |
| ASD-0944 | [JevGPT: Thinking Fast and Slow in Autonomous Research](https://arxiv.org/abs/2610.18272) | needs_review | 2026-10-13 | 对象映射待核 |  | Agent资格、对象类别或来源证据仍有边界问题，保留逐篇审查队列。 已有实际任务，但当前对象映射证据不足，分类待核，不以01.04作兜底。 |
| ASD-0945 | [MMPostTrainBench: Benchmarking Autonomous Research for Multimodal Post-Training](https://arxiv.org/abs/2610.05398) | candidate | 2026-10-04 | 01 | 01.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0946 | [PrimeScientist: Strategic Allocation of Research Effort in Autonomous Research](https://arxiv.org/abs/2609.17846) | candidate | 2026-09-15 | 01 | 01.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0947 | [Experimental Experience Modeling for Autonomous Research](https://arxiv.org/abs/2609.39392) | needs_review | 2026-09-30 | 对象映射待核 |  | Agent资格、对象类别或来源证据仍有边界问题，保留逐篇审查队列。 已有实际任务，但当前对象映射证据不足，分类待核，不以01.04作兜底。 |
| ASD-0948 | [Collaborative Principle Evolution via Evidence Transfer for Scientific Discovery](https://arxiv.org/abs/2609.35315) | needs_review | 2026-09-28 | 对象映射待核 |  | Agent资格、对象类别或来源证据仍有边界问题，保留逐篇审查队列。 已有实际任务，但当前对象映射证据不足，分类待核，不以01.04作兜底。 |
| ASD-0949 | [TruthInsightBench: An Evidence-Grounded Benchmark for Automated Evaluation of Open-Ended Scientific Discovery Agents](https://arxiv.org/abs/2609.05079) | needs_review | 2026-09-04 | 对象映射待核 |  | TruthInsightBench确有40项研究数据分析任务，但当前证据未给出10个具体任务域清单；对象模块暂空并待审，不能以01.04替代缺失的分类证据。 |
| ASD-0950 | [Dr. Claw: An AI Scientist Workspace for Vibe Research](https://arxiv.org/abs/2609.00365) | needs_review | 2026-08-31 | 对象映射待核 |  | Agent资格、对象类别或来源证据仍有边界问题，保留逐篇审查队列。 已有实际任务，但当前对象映射证据不足，分类待核，不以01.04作兜底。 |
| ASD-0951 | [Reward Hacking Challenges Oversight of Autonomous Research Agents](https://arxiv.org/abs/2609.28614) | needs_review | 2026-09-23 | 对象映射待核 |  | Agent资格、对象类别或来源证据仍有边界问题，保留逐篇审查队列。 已有实际任务，但当前对象映射证据不足，分类待核，不以01.04作兜底。 |
| ASD-0952 | [AutoResearch: Insight In, Hallucination Out](https://arxiv.org/abs/2608.17906) | candidate | 2026-08-18 | 01 | 01.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0953 | [ScienceFlow: A long-horizon agent for ML research, scientific discovery and beyond](https://arxiv.org/abs/2608.14354) | candidate | 2026-08-14 | 01 | 01.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0954 | [Project2Task: Graph-Guided Project-Level Planning for Autonomous Research](https://arxiv.org/abs/2608.05225) | needs_review | 2026-08-05 | 对象映射待核 |  | Agent资格、对象类别或来源证据仍有边界问题，保留逐篇审查队列。 已有实际任务，但当前对象映射证据不足，分类待核，不以01.04作兜底。 |
| ASD-0955 | [AutoWorldModel-Bench: A State-Centric Benchmark for Automated World-Model Research](https://arxiv.org/abs/2608.11216) | candidate | 2026-07-20 | 01 | 01.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0956 | [Beneath the Diff: Diagnosing and Mitigating Algorithmic Mode Collapse in Code-Level Autonomous Research Loops](https://arxiv.org/abs/2609.00077) | candidate | 2026-08-31 | 01 | 01.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0957 | [Beyond Final Scores: A Systematic Evaluation of Agents for Long-Horizon AI Research and Development](https://arxiv.org/abs/2608.13417) | candidate | 2026-08-13 | 01 | 01.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0958 | [Beyond Solution-Centric Search: Adaptive Inquiry and Knowledge Revision for Autonomous ML Engineering](https://arxiv.org/abs/2608.02143) | candidate | 2026-08-03 | 01 | 01.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0959 | [Long-Horizon Autonomous Architecture Research with a Language-Model Agent: A Behavioural Case Study](https://arxiv.org/abs/2608.01995) | candidate | 2026-08-03 | 01 | 01.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0960 | [CausalSmith: A Formally Grounded, Self-Improving Agentic Framework for Automated Research in Causal Inference](https://arxiv.org/abs/2607.22511) | candidate | 2026-07-24 | 01 | 01.01 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0961 | [XScientist: A Git-Like Research Protocol for Long-Running Autonomous Scientific Discovery](https://arxiv.org/abs/2607.12301) | needs_review | 2026-07-14 | 对象映射待核 |  | Agent资格、对象类别或来源证据仍有边界问题，保留逐篇审查队列。 已有实际任务，但当前对象映射证据不足，分类待核，不以01.04作兜底。 |
| ASD-0962 | [Triage-PiEvo: Evidence Admission for Principle-Evolving Scientific Agents](https://arxiv.org/abs/2610.14683) | needs_review | 2026-10-10 | 对象映射待核 |  | Agent资格、对象类别或来源证据仍有边界问题，保留逐篇审查队列。 已有实际任务，但当前对象映射证据不足，分类待核，不以01.04作兜底。 |
| ASD-0963 | [EvoSim: Learning to Model, Modeling to Learn](https://arxiv.org/abs/2610.11344) | candidate | 2026-10-08 | 04 | 04.04 | EvoSim依据实验偏差修正电池物理机制/方程，并验证析锂起始和驾驶工况电压；按具体电池对象归能源材料，不因自称physics模型泛归01或02。 |
| ASD-0964 | [Are We Measuring Scientific Intelligence? Rethinking the Evaluation of AI Scientists](https://arxiv.org/abs/2610.04915) | candidate | 2026-10-04 | 06 | 06.03/06.03.04 | 在18项BAISBench单细胞问题和GeneBench合成任务上干预数据证据并反复运行Agent，具有具体单细胞生物学对象实验。 |
| ASD-0965 | [Can AI Scientists Change Their Minds? Prior-Evidence Conflict in Synthetic Universes](https://arxiv.org/abs/2609.36726) | candidate | 2026-09-29 | 01 | 01.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0966 | [AI for Science with GPT-6 Astra: Thermal Design and Electrothermal Analysis of 2D CFET](https://arxiv.org/abs/2609.17123) | candidate | 2026-09-15 | 09 | 09.08 | 2D CFET结构设计、共享电热仿真、敏感度和复现实验支持半导体器件工程；仅凭二维材料器件标签不足以另建材料对象04归属。 |
| ASD-0967 | [An immune world model for multiscale forecasting and therapeutic hypothesis generation](https://arxiv.org/abs/2609.14709) | candidate | 2026-09-13 | 06;07 | 06.03/06.03.04 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0968 | [Online Surrogate Repair: Decoupling High-Fidelity Feedback from Search Length in Closed-Loop Discovery](https://arxiv.org/abs/2609.07655) | needs_review | 2026-09-07 | 对象映射待核 |  | Agent资格、对象类别或来源证据仍有边界问题，保留逐篇审查队列。 已有实际任务，但当前对象映射证据不足，分类待核，不以01.04作兜底。 |
| ASD-0969 | [Mechanist: AI as a Scientific Instrument for Discovering the Mechanisms of Intelligence](https://arxiv.org/abs/2608.12036) | candidate | 2026-08-12 | 01 | 01.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0970 | [Adversarial Fast-Moving Real-World Domains as Test Beds for Benchmarking AI Scientist Capabilities](https://arxiv.org/abs/2608.03569) | background_only | 2026-08-04 | 对象映射待核 |  | F1设计想法和MTG组牌用于评价模型新颖性；当前摘要仅模型提案比较，未说明多步科研Agent行动，保留评测背景。 |
| ASD-0971 | [Sci$Π$vot: Benchmarking Principal-Investigator Judgment at Pivotal Moments of Scientific AutoResearch Agents](https://arxiv.org/abs/2610.21082) | candidate | 2026-10-15 | 11 | 11.07 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0972 | [EvoCast: Reliable Autonomous Research Agents for Iterative Forecasting Architecture Evolution](https://arxiv.org/abs/2610.04517) | candidate | 2026-10-03 | 01 | 01.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0973 | [Large-Scale Autonomous Discovery of Kissing Number Constructions](https://arxiv.org/abs/2609.35051) | candidate | 2026-09-28 | 01 | 01.01 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0974 | [What Happens During Autonomous Deep Research After the User Steps Away?](https://arxiv.org/abs/2609.33509) | needs_review | 2026-09-27 | 01 | 01.02 | DRaligned分析自主deep-research任务的请求、草稿和建议随用户因素变化；底层任务是否科研工作仍不明，保留资格待核。 |
| ASD-0975 | [A Case Study on Emergent Cheating and Whistleblowing in Autonomous Research Swarms](https://arxiv.org/abs/2609.04170) | candidate | 2026-09-03 | 01;11 | 11.07 | 100个Agent执行形式数学猜想证明并出现欺骗与举报、验证修补，支持数学任务01和科研共同体/制度11.07。 |
| ASD-0976 | [Andy: A Mathematical Agent for Rigorous Proof and Autonomous Research](https://arxiv.org/abs/2608.15052) | candidate | 2026-08-15 | 01 | 01.01 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0977 | [AgonAlpha: Autonomous Alpha Discovery via Prompt Economy and Scalable Agentic Search](https://arxiv.org/abs/2608.11250) | candidate | 2026-08-04 | 11 | 11.01 | 交易因子研究Agent基于可执行假设及平台反馈搜索，独立审查Agent重运行及否决；收益主张仍需全文证据。 |
| ASD-0978 | [OpenDiscoveryTrace: Process Traces for Evaluating AI Scientist Workflows](https://arxiv.org/abs/2609.09203) | candidate | 2026-09-05 | 04;06;07;11 | 11.07 | 124任务涵盖材料、基因组、药物发现与科学文献，记录工具使用轨迹；细分药物化学03对象尚待任务清单证据，不机械加入。 |
| ASD-0979 | [Autonomous in-silico inorganic materials discovery via multi-agent physics-aware scientific reasoning](https://www.nature.com/articles/s41524-026-02205-8) | candidate | 2026-07-08 | 04 | 04.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0980 | [Experiment automation agents: automating materials characterization with vision language model agents](https://www.nature.com/articles/s41524-026-02213-8) | candidate | 2026-07-31 | 04 | 04.01 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0981 | [A collaborative agent with two lightweight synergistic models for autonomous crystal materials research](https://www.nature.com/articles/s42256-026-01298-6) | candidate | 2026-09-10 | 04 | 04.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0982 | [Large-language-model-driven adaptive search space definition for autonomous closed-loop materials exploration](https://www.nature.com/articles/s43246-026-01304-9) | needs_review | 2026-08-25 | 04 | 04.02 | Agent资格、对象类别或来源证据仍有边界问题，保留逐篇审查队列。 |
| ASD-0983 | [Autonomous adaptive spectral analysis with an LLM agent for self-driving laboratories](https://arxiv.org/abs/2610.25619) | candidate | 2026-10-19 | 04 | 04.04 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0984 | [A self-learning scientific agent for X-ray diffraction](https://arxiv.org/abs/2610.07862) | candidate | 2026-10-06 | 04;03 | 04.01 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0985 | [Agent-E2MD: Autonomous Translation of Interatomic Potential Equations into Physically Validated Pair Styles for Molecular Dynamics in LAMMPS](https://arxiv.org/abs/2609.26657) | candidate | 2026-09-22 | 04 | 04.01 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0986 | [Hierarchical automation of scanning probe microscopy through agentic orchestration and algorithmic control](https://arxiv.org/abs/2609.04015) | candidate | 2026-09-03 | 04 | 04.03 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0987 | [Diagnosing and narrowing the simulation-to-real gap in powder X-ray diffraction with a wet-dry agentic loop](https://arxiv.org/abs/2608.22400) | candidate | 2026-08-23 | 04 | 04.01 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0988 | [PACE-SIMS: Checkpoint-Gated Autonomous SIMS Characterization with AI-Agent Quality Control](https://arxiv.org/abs/2608.12277) | candidate | 2026-08-12 | 04 | 04.01 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0989 | [Agent-MD: Selective LLM Intervention with Event-Driven Escalation for Stateful GCMC--MD Campaigns](https://arxiv.org/abs/2608.07637) | candidate | 2026-08-07 | 04 | 04.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0990 | [An LLM agent for end-to-end computational materials discovery](https://arxiv.org/abs/2608.20434) | candidate | 2026-08-20 | 04 | 04.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0991 | [ALKEMIE Agent: an autonomous platform for computational materials design](https://arxiv.org/abs/2608.15776) | needs_review | 2026-08-16 | 04 | 04.01 | Agent资格、对象类别或来源证据仍有边界问题，保留逐篇审查队列。 |
| ASD-0992 | [ElectrolyteMD-Bench: How Well Do AI Agents Conduct Molecular Dynamics Studies across Electrolyte Solvation Regimes?](https://arxiv.org/abs/2609.31743) | candidate | 2026-09-23 | 04;03 | 04.04 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0993 | [Vibe-FDTR: An agent-oriented framework for reproducible frequency-domain thermoreflectance data analysis](https://arxiv.org/abs/2607.28200) | candidate | 2026-07-30 | 04 | 04.01 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-0994 | [AEcroscopyWave: Towards Self-Driving Characterization Platforms for Agentic AI](https://arxiv.org/abs/2607.22975) | needs_review | 2026-07-25 | 04 | 04.01 | Agent资格、对象类别或来源证据仍有边界问题，保留逐篇审查队列。 |
| ASD-0995 | [Quality-controlled active learning via Gaussian processes for robust structure–property learning in autonomous microscopy](https://www.nature.com/articles/s41524-026-02248-x) | needs_review | 2026-08-21 | 04 | 04.03 | Agent资格、对象类别或来源证据仍有边界问题，保留逐篇审查队列。 |
| ASD-0996 | [ChemGraph-XANES: an agentic framework for XANES simulation and curation](https://pubs.rsc.org/en/content/articlelanding/2026/ra/d6ra06166d) | needs_review | 日期待核 | 03;04 | 04.01 | Agent资格、对象类别或来源证据仍有边界问题，保留逐篇审查队列。 |
| ASD-0997 | [Autonomous global-minimum search of Pd6Mo7 nanoclusters from deep reinforcement learning](https://doi.org/10.1016/j.nxmate.2026.103127) | needs_review | 2026-10 | 03;04 | 04.02 | Agent资格、对象类别或来源证据仍有边界问题，保留逐篇审查队列。 |
| ASD-0998 | [Toward autonomous experimentation: Bayesian optimization over problem formulation space for accelerated alloy development](https://doi.org/10.1016/j.matdes.2026.116585) | needs_review | 2026-09 | 04 | 04.02 | Agent资格、对象类别或来源证据仍有边界问题，保留逐篇审查队列。 |
| ASD-0999 | [Interpretable self-driving sputtering epitaxy reveals human-usable growth rules for β-Ga2O3 films](https://www.nature.com/articles/s41467-026-76533-0) | needs_review | 2026-08-13 | 04 | 04.04 | Agent资格、对象类别或来源证据仍有边界问题，保留逐篇审查队列。 |
| ASD-1000 | [Managing autonomous materials labs with multi-agent AI and its implications for the science of science](https://www.nature.com/articles/s43246-026-01219-5) | background_only | 2026-07-08 | 对象映射待核 |  | 背景讨论或方法综述，未据此确认新的科研Agent实证研究。 |
| ASD-1001 | [CompMat-Bench: Benchmarking AI Agents for Computational Materials Science](https://arxiv.org/abs/2610.00636) | candidate | 2026-09-30 | 04 | 04.01 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1002 | [ERAF4XRD: A multimodal agentic framework for constructing validated experimental X-ray diffraction databases from scientific literature](https://arxiv.org/abs/2609.18583) | candidate | 2026-09-16 | 04 | 04.01 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1003 | [Human-agent discovery of reconfigurable in-plane ferroelectric superdomain control](https://arxiv.org/abs/2609.06887) | candidate | 2026-09-07 | 04 | 04.03 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1004 | [Crystal-structure design by agentic AI in a language of motifs](https://arxiv.org/abs/2608.15900) | candidate | 2026-08-16 | 04 | 04.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1005 | [LATHE: LAnguage-driven Toolkit for Hypothesis-based crystal Editing](https://arxiv.org/abs/2610.02671) | candidate | 2026-10-02 | 04 | 04.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1006 | [Enabling large language model agents for high-fidelity many-body perturbation theory calculations](https://arxiv.org/abs/2610.20779) | candidate | 2026-10-14 | 04;02 | 04.01 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1007 | [Agentic schema-guided extraction of materials process knowledge from scientific literature](https://arxiv.org/abs/2610.06322) | candidate | 2026-10-05 | 04 | 04.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1008 | [Scaling LLM Agents for Materials Design through Hierarchical Collective Reasoning](https://arxiv.org/abs/2609.16466) | candidate | 2026-09-15 | 04 | 04.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1009 | [Agentic self-driving microscopy benchmarks support qualification but do not necessarily generalize to unseen tasks](https://arxiv.org/abs/2608.05266) | needs_review | 2026-08-05 | 04 | 04.01 | Agent资格、对象类别或来源证据仍有边界问题，保留逐篇审查队列。 |
| ASD-1010 | [Science Done on a Machine by a Machine: AI Agents in Computational Chemistry](https://arxiv.org/abs/2608.18508) | background_only | 2026-08-19 | 对象映射待核 |  | 背景讨论或方法综述，未据此确认新的科研Agent实证研究。 |
| ASD-1011 | [Stress-testing large language model agents in a robotic chemistry laboratory](https://arxiv.org/abs/2607.23045) | candidate | 2026-07-25 | 03 | 03.01 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1012 | [HealthFlow: automating electronic health record analysis via a strategically self-evolving multi-agent framework](https://doi.org/10.1038/s41746-026-03097-0) | candidate | 2026-08-17 | 07 | 07.03/07.03.08 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1013 | [From quantitative features to imaging signs: agentic AI-driven autonomous discovery in glioblastoma](https://doi.org/10.1038/s41746-026-03331-9) | candidate | 2026-10-07 | 07 | 07.02/07.02.05 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1014 | [An AI-powered self-driving microscope for low-cost acute leukemia detection](https://doi.org/10.1038/s41467-026-77130-x) | needs_review | 2026-08-27 | 07 | 07.01/07.01.04 | Agent资格、对象类别或来源证据仍有边界问题，保留逐篇审查队列。 |
| ASD-1015 | [MR-MAS: an end-to-end multi-agent system for autonomous Mendelian randomization analysis](https://doi.org/10.1093/bioinformatics/btag722) | candidate | 2026-10-20 | 07 | 07.03/07.03.01 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1016 | [DDA: a traceable multi-agent framework for automated structure-based drug design](https://doi.org/10.3389/fchem.2026.1914886) | candidate | 2026-09-01 | 06;07 | 07.04/07.04.01 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1017 | [DynaMate: An Autonomous Agent for Protein-Ligand Molecular Dynamics Simulations](https://doi.org/10.21203/rs.3.rs-10243410/v1) | candidate | 2026-08-27 | 06;07 | 07.04/07.04.01 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1018 | [GENIE: a multi-agent system for closed-loop autonomous microscopy](https://doi.org/10.64898/2026.10.12.758370) | candidate | 2026-10-13 | 06 | 06.03/06.03.04 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1019 | [A Conversational Multi-Agent AI System for Integrated Multi-Omics Analysis and Biomedical Discovery](https://doi.org/10.64898/2026.08.08.743577) | candidate | 2026-08-14 | 06;07 | 06.03/06.03.04 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1020 | [PromptBio: An Agentic Platform for End-to-End Computational Biomedical Research](https://doi.org/10.64898/2026.09.02.748774) | candidate | 2026-09-06 | 06 | 06.03/06.03.01 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1021 | [TRACEDD: A Tool-grounded Reasoning and Agentic Coordination for Explainable Drug Design](https://doi.org/10.64898/2026.09.12.751167) | candidate | 2026-09-18 | 06;07 | 07.04/07.04.01 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1022 | [Agentic campaign control for high-throughput de novo binder design](https://doi.org/10.64898/2026.09.22.753604) | candidate | 2026-09-23 | 06 | 06.03/06.03.06 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1023 | [Reliable and Efficient Agentic Protein Design with Toolset Harnessing](https://doi.org/10.64898/2026.10.19.759896) | candidate | 2026-10-20 | 06 | 06.03/06.03.06 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1024 | [Detailed curation of biological samples and experimental designs for genomics using LLM-supported agentic workflows](https://doi.org/10.64898/2026.07.30.741874) | candidate | 2026-08-02 | 06 | 06.03/06.03.01 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1025 | [From Prompt to Pipeline: A Comparative Evaluation of Large Language Model Coding Agents for Reproducible Bioinformatics Pipeline Construction](https://doi.org/10.64898/2026.09.11.751004) | candidate | 2026-09-17 | 06 | 06.03/06.03.01 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1026 | [ACCREDIT: A Quality-Aware Agentic Engine for Cell-resolved Cross-modal Image Registration with Dynamic Iterative Tuning](https://doi.org/10.64898/2026.08.08.743602) | needs_review | 2026-08-14 | 06;07 | 06.03/06.03.04 | Agent资格、对象类别或来源证据仍有边界问题，保留逐篇审查队列。 |
| ASD-1027 | [Human-Guided Agentic AI for End-to-End EHR Research: Sequential Antibody-Drug Conjugate Pathways in Breast Cancer](https://doi.org/10.64898/2026.10.13.26365479) | candidate | 2026-10-14 | 07 | 07.02/07.02.05 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1028 | [From seven combination hypotheses to one testable interaction: a gated agentic AI–QSP workflow applied to healthy-ageing interventions](https://doi.org/10.64898/2026.09.29.755460) | needs_review | 2026-10-01 | 07 | 07.03/07.03.04 | Agent资格、对象类别或来源证据仍有边界问题，保留逐篇审查队列。 |
| ASD-1029 | [inClinico Agent for clinical trial endpoint prediction and prospective evaluation](https://doi.org/10.64898/2026.10.13.26365373) | needs_review | 2026-10-15 | 07 | 07.04/07.04.01 | Agent资格、对象类别或来源证据仍有边界问题，保留逐篇审查队列。 |
| ASD-1030 | [MedKGent: a large language model agent framework for constructing temporally evolving medical knowledge graph](https://doi.org/10.1038/s41746-026-03058-7) | needs_review | 2026-08-04 | 07 | 07.03/07.03.08 | Agent资格、对象类别或来源证据仍有边界问题，保留逐篇审查队列。 |
| ASD-1031 | [OntoCodex: a multi-agent biomedical ontology enrichment framework](https://doi.org/10.1038/s44401-026-00117-9) | needs_review | 2026-08-05 | 07 | 07.03/07.03.08 | Agent资格、对象类别或来源证据仍有边界问题，保留逐篇审查队列。 |
| ASD-1032 | [RelAgent: a multi-agent solution for molecular relationship grounding](https://doi.org/10.1093/bioinformatics/btag541) | needs_review | 2026-07-23 | 06;07 | 06.03/06.03.06 | Agent资格、对象类别或来源证据仍有边界问题，保留逐篇审查队列。 |
| ASD-1033 | [Informing agent-based models with spatial data using convolutional autoencoders](https://doi.org/10.1093/bioinformatics/btag444) | needs_review | 2026-08-21 | 06;07 | 06.03/06.03.04 | 肿瘤/免疫细胞空间ABM参数校准与实测成像比较明确；Agent作为科研行动者或仅被模拟实体的边界待全文，不能仅因传统ABM排除。 主体有决策/交互与科学仿真结果，但其角色是科研行动者还是仅被模拟实体仍待全文；传统ABM及非LLM本身不是排除理由。 |
| ASD-1034 | [Agent-based modeling identifies multiple paths for inflammation resolution](https://doi.org/10.1093/bioinformatics/btag533) | needs_review | 2026-08-19 | 06;07 | 06.02/06.02.08 | 免疫细胞有趋化、极化、吞噬和信号动作，30万次模拟分析炎症消退机制；科研工作流角色边界仍待全文，保留待审而非直接排除。 主体有决策/交互与科学仿真结果，但其角色是科研行动者还是仅被模拟实体仍待全文；传统ABM及非LLM本身不是排除理由。 |
| ASD-1035 | [An open benchmark and language models for AI in aging biology](https://doi.org/10.1016/j.cell.2026.08.026) | excluded | 2026-09 | 对象映射待核 |  | 已检索但未检得符合本项目科研Agent四项标准的证据，保留排除记录。 |
| ASD-1036 | [Verification Debt in Automated Biological Research Workflows: A Proof-of-Concept](https://doi.org/10.64898/2026.09.29.755250) | candidate | 2026-10-05 | 06;07 | 07.04/07.04.01 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1037 | [hvantk: an agentic multi-omics framework for variant annotation and analysis](https://doi.org/10.64898/2026.10.19.760196) | candidate | 2026-10-21 | 06;07 | 07.03/07.03.01 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1038 | [Auto-MD-bench: Evaluating Autoresearch Agents for Real-World Medical Tasks](https://arxiv.org/abs/2610.25069) | candidate | 2026-10-18 | 07 | 07.03/07.03.08 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1039 | [DrugTargetWorld: A Synthetic Biobank for Training and Benchmarking AI Scientists](https://arxiv.org/abs/2610.09558) | candidate | 2026-10-07 | 06;07 | 06.03/06.03.01 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1040 | [Can Coding Agents Build Robust Baselines? A Skill-Based Approach for Automating the Medical Imaging Model-Development Pipeline](https://arxiv.org/abs/2608.23336) | candidate | 2026-08-24 | 07 | 07.01/07.01.04 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1041 | [NeuroAct: Advancing EEG Analysis and Decoding via Dual-Loop Autonomous Research](https://arxiv.org/abs/2610.25211) | candidate | 2026-10-18 | 07 | 07.01/07.01.03 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1042 | [TCMScience: An Autonomous Scientist for Traditional Chinese Medicine](https://arxiv.org/abs/2610.24601) | candidate | 2026-10-17 | 07 | 07.04/07.04.01 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1043 | [Solver Agent: an Agentic AI Framework for Theoretical Physics Computations Applied to F-theory Uplifts of O3-planes and S-folds](https://arxiv.org/abs/2609.35958) | candidate | 2026-09-28 | 02 | 02.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1044 | [VortexChat: An agentic framework for autonomous multi-objective integrated photonic design](https://arxiv.org/abs/2608.20688) | candidate | 2026-08-21 | 09 | 09.08 | VortexChat工具仿真/反馈迭代设计集成光子器件，并制造测试太赫兹涡旋复用器；对象是光电器件工程。 |
| ASD-1045 | [CFD Forge: A Physics-Constrained Agentic Framework for Autonomous CFD](https://arxiv.org/abs/2610.14104) | candidate | 2026-10-08 | 09 | 09.01 | CFD Forge以物理约束规划与执行计算流体力学实验，暂归工程建模/力学；其它独立物理对象覆盖待任务清单。 |
| ASD-1046 | [AI Agents as a Research Team: A Human-Supervised Case Study in Stellar Spectroscopy](https://arxiv.org/abs/2610.05424) | candidate | 2026-10-04 | 02 | 02.01 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1047 | [OPERA: Operator-residual feedback for reliable autonomous optical experiments with language-model agents](https://arxiv.org/abs/2608.05990) | candidate | 2026-08-06 | 02 | 02.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1048 | [Photonics-GCCE: group collaborative-competitive evolution multi-agent framework for universal and autonomous optical design](https://arxiv.org/abs/2609.28045) | candidate | 2026-09-23 | 09 | 09.08 | Photonics-GCCE在六类光子器件上比较协作竞争设计、制造敏感度和物理一致性；主归光电器件工程。 |
| ASD-1049 | [El Agente Potente: High-Throughput Agentic Atomistic Simulations](https://arxiv.org/abs/2609.14840) | candidate | 2026-09-13 | 04 | 04.01 | 原子级高通量仿真研究以具体材料结构/性质为对象，暂归材料基础；不因模拟用物理定律自动并列物理02。 |
| ASD-1050 | [HALO: A Physics-Aware LLM Agent Framework for Nanophotonic Design](https://arxiv.org/abs/2608.28877) | candidate | 2026-08-28 | 09 | 09.08 | HALO在52项纳米光子设计任务中执行电磁仿真、诊断及反馈修订；物理知识是约束，具体对象是器件工程。 |
| ASD-1051 | [Agentic AI for Density-Functional Development: Revisiting r2SCAN](https://arxiv.org/abs/2609.19419) | candidate | 2026-09-16 | 03;04 | 03.02 | r2SCAN修订有Agent提议、critic筛选与确定性验证；24固体带隙和329分子性质为独立材料与化学对象实验。 |
| ASD-1052 | [SolutionsX: supergravity theories/solutions as code, with an agentic workflow for machine-verifiable physics](https://arxiv.org/abs/2609.07826) | candidate | 2026-09-07 | 02 | 02.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1053 | [Agentic TCAD Calibration Workflow for Oxide Semiconductor Transistors](https://arxiv.org/abs/2609.12184) | candidate | 2026-09-10 | 09 | 09.08 | Agent利用实测晶体管曲线、TCAD残差和敏感度选择参数/模型并验证跨偏压几何迁移；归半导体器件工程。 |
| ASD-1054 | [Automated Discovery of Physically Interpretable Subgrid Length Scales for Detached Eddy Simulation via Agentic AI](https://arxiv.org/abs/2610.29850) | candidate | 2026-10-21 | 09 | 09.01 | Agent迭代发现分离涡仿真的可解释亚网格长度尺度，具体对象是流体工程模型与数值验证。 |
| ASD-1055 | [Demonstration of a Structured Agentic Workflow for Applied Quantum Computing Research](https://arxiv.org/abs/2610.05304) | candidate | 2026-10-04 | 02 | 02.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1056 | [LaMET-Agent: An Agent Framework for Large-Momentum Effective Theory Analysis](https://arxiv.org/abs/2609.32225) | candidate | 2026-09-26 | 02 | 02.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1057 | [SeisEvo: Evolution of Seismic Data Reconstruction Algorithms by Agents](https://arxiv.org/abs/2608.18272) | candidate | 2026-08-18 | 01;05 | 05.01 | SeisEvo演化地震数据插值/去噪算法并在未见数据验证，支持计算算法01和地球物理05；纠正来源初筛误归天文。 |
| ASD-1058 | [CosmoAgent: AI Agent for Theoretical Cosmology](https://arxiv.org/abs/2610.16536) | candidate | 2026-10-12 | 02 | 02.01 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1059 | [Automated Many-Body Simulations of Strongly Correlated Systems Using a Correlation-Aware Agentic Framework](https://arxiv.org/abs/2610.00943) | candidate | 2026-10-01 | 02 | 02.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1060 | [AstroGenesis: A Domain-Specific Multi-Agent AI for Astrophysical Research](https://arxiv.org/abs/2609.28579) | candidate | 2026-09-23 | 02 | 02.01 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1061 | [Agentic AI for operating scientific instruments for nanoscale characterization](https://arxiv.org/abs/2608.26198) | candidate | 2026-08-25 | 09 | 09.03 | 三类MCP Agent分别执行AFM指令、评价图像/调参及伪影修复，实机比较专家；当前明确对象为科学仪器与表征操作，具体样品材料类别待全文。 |
| ASD-1062 | [Vision-Language Agents for Active Perception in Optics Laboratories](https://arxiv.org/abs/2609.32918) | candidate | 2026-09-26 | 02 | 02.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1063 | [OceanMind: A multi-agent AI system for ocean diagnosis](https://arxiv.org/abs/2610.03780) | candidate | 2026-09-30 | 05 | 05.02 | OceanMind按真实三维海洋状态规划、执行诊断、反馈修复并复现海洋研究结果；纠正来源初筛误归天文02.01。 |
| ASD-1064 | [Agent-assisted experimental strategy transfer across quantum processors](https://arxiv.org/abs/2610.21047) | candidate | 2026-10-15 | 02 | 02.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1065 | [Agentic Active Learning Meets Visual Embeddings: Finding Anomalies among 370 000 Variable Stars from ASAS-SN](https://arxiv.org/abs/2608.23688) | candidate | 2026-08-24 | 02 | 02.01 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1066 | [Multi-agent discovery of practical quantum LDPC codes](https://arxiv.org/abs/2608.08996) | candidate | 2026-08-10 | 02 | 02.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1067 | [How AI Agents Discover Scientific Equations: From Hydrotope Rediscovery to New Water-Wave Amplitudes](https://arxiv.org/abs/2610.00435) | candidate | 2026-09-30 | 02 | 02.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1068 | [Brilliance: toward autonomous computational research in particle accelerator physics](https://arxiv.org/abs/2610.15615) | candidate | 2026-10-11 | 02 | 02.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1069 | [Jianmu-Q: Bridging Quantum Field Theory and Quantum Hardware with AI Agents](https://arxiv.org/abs/2610.21942) | candidate | 2026-10-15 | 02 | 02.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1070 | [FUSION: a skill-based research agent for publicly obtainable nuclear-physics codes](https://arxiv.org/abs/2609.04742) | candidate | 2026-09-04 | 02 | 02.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1071 | [From Earth to Mars and Beyond: AI-Driven Cosmic-Ray Validation and Prediction with CorsikaAgent](https://arxiv.org/abs/2610.16607) | candidate | 2026-10-12 | 02 | 02.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1072 | [HEPLocalAgent 1.0: Running Collider Simulations from Plain-Language Requests on Your Own Computer](https://arxiv.org/abs/2608.28244) | candidate | 2026-08-28 | 02 | 02.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1073 | [PTagent: An LLM-assisted tool for finite-temperature model construction in cosmological phase transitions](https://arxiv.org/abs/2610.21118) | candidate | 2026-10-15 | 02 | 02.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1074 | [VALG: An Agentic System for ML Theory Research](https://arxiv.org/abs/2608.13060) | candidate | 2026-08-13 | 01 | 01.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1075 | [ProofLoom: Proof-Obligation-Driven Theory Construction for Autoformalizing Research-Level Stochastic Optimization](https://arxiv.org/abs/2609.34960) | needs_review | 2026-09-28 | 01 | 01.01 | Agent资格、对象类别或来源证据仍有边界问题，保留逐篇审查队列。 |
| ASD-1076 | [FormaTheoria: Constructing Large-Scale Lean Theories from Mathematical Literature $-$ Toward the Formalization of the Classification of Finite Simple Groups](https://arxiv.org/abs/2608.10894) | needs_review | 2026-08-11 | 01 | 01.01 | Agent资格、对象类别或来源证据仍有边界问题，保留逐篇审查队列。 |
| ASD-1077 | [FLARE: Verifying MILP Reformulations with LLM-Based Theorem Proving](https://arxiv.org/abs/2608.25220) | excluded | 2026-08-25 | 01 | 01.02 | 已检索但未检得符合本项目科研Agent四项标准的证据，保留排除记录。 |
| ASD-1078 | [An AI-Assisted Formalization of the Poincaré Conjecture](https://arxiv.org/abs/2610.08329) | needs_review | 2026-10-06 | 01 | 01.01 | Agent资格、对象类别或来源证据仍有边界问题，保留逐篇审查队列。 |
| ASD-1079 | [AI Discovery in Combinatorics: From Problems to Solutions and Back to Bigger Problems](https://arxiv.org/abs/2610.16555) | needs_review | 2026-10-12 | 01 | 01.01 | Agent资格、对象类别或来源证据仍有边界问题，保留逐篇审查队列。 |
| ASD-1080 | [Euler: Towards Human-Centered Multi-Agent Mathematical Discovery](https://arxiv.org/abs/2610.19864) | candidate | 2026-10-14 | 01 | 01.01 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1081 | [The AI Theorist reveals excitonic structure in $\alpha$-RuCl$_3$](https://arxiv.org/abs/2610.02417) | candidate | 2026-10-01 | 02;04 | 02.02 | AI Theorist利用第一性原理/多体计算与光学实验解释α-RuCl3激子态，同时支持凝聚态物理02及量子材料04。 |
| ASD-1082 | [Beyond Equation Search: Conjecture-Guided Discovery with SCOPE and ClosureBench](https://arxiv.org/abs/2610.18938) | candidate | 2026-10-13 | 01;09 | 09.01 | SCOPE多Agent在OpenFOAM中主动取得PDE闭合数据并检验猜想，暂支持形式模型与工程仿真；五个任务域的其余模块待清单。 |
| ASD-1083 | [OptScientist: Automated Discovery of Optimization Laws](https://arxiv.org/abs/2610.28562) | candidate | 2026-10-20 | 01;02;11 | 02.02 | OptScientist实际评测99物理优化问题、人类风险选择和央行货币政策；不能只按方法名保留01/02而遗漏行为经济11。 |
| ASD-1084 | [Towards autonomous urban drainage modelling: evaluating AI agent architectures for automated SWMM calibration](https://www.nature.com/articles/s41545-026-00638-8) | candidate | 2026-09-14 | 05;09 | 09.05 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1085 | [Multi-agent AI for end-to-end air quality analysis and decision support](https://www.nature.com/articles/s44407-026-00102-4) | candidate | 2026-09-15 | 05 | 05.03 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1086 | [An LLM-agent interface for end-to-end probabilistic seismic hazard and risk analysis](https://www.nature.com/articles/s44304-026-00262-z) | candidate | 2026-08-26 | 05;09 | 05.01 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1087 | [LeakAgent: a multi-agent system for leak detection using multi-modal large language model coordination in water distribution network](https://www.nature.com/articles/s44488-026-00024-w) | needs_review | 2026-10-06 | 09 | 09.05 | Agent资格、对象类别或来源证据仍有边界问题，保留逐篇审查队列。 |
| ASD-1088 | [A RAG-enhanced multi-agent LLM/VLM framework for auditable and region-aware structural health monitoring of a historic masonry structure](https://www.nature.com/articles/s41598-026-57424-2) | needs_review | 2026-10-15 | 09 | 09.05 | Agent资格、对象类别或来源证据仍有边界问题，保留逐篇审查队列。 |
| ASD-1089 | [AFDBench: A Reasoning-First AI Scientist for NationalWeather Service Forecast Discussions](https://arxiv.org/abs/2608.24954) | excluded | 2026-08-25 | 05 | 05.02 | 已检索但未检得符合本项目科研Agent四项标准的证据，保留排除记录。 |
| ASD-1090 | [RingMoClaw: An Experience-Inspired Multi-Agent Framework for Self-Evolving Research in Remote Sensing](https://arxiv.org/abs/2609.00814) | candidate | 2026-09-01 | 05 | 05.04 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1091 | [Autonomous Research Project Management as an Agent Skill: A Case Study in Exact Spectral Spatial Regression](https://arxiv.org/abs/2609.31683) | candidate | 2026-09-16 | 01;05 | 01.02 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1092 | [MBA: Multimodal Benchmark and Agents for Real-World Business Ideation](https://arxiv.org/abs/2608.11616) | candidate | 2026-08-12 | 11 | 11.01 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1093 | [WhatWorkedBench: Benchmarking Experimental Understanding in AI Agents](https://arxiv.org/abs/2609.27490) | candidate | 2026-09-23 | 01;02;05;07;08;09;11 | 01.02 | 全文附录列太阳黑子/Hubble、CO2/ENSO/Nile、乳腺/ECG、豆/种子、翼型/混凝土等可运行任务；按实际任务对象暂作多模块，glass材料对象仍待核。 |
| ASD-1094 | [IdeaScientist: Orchestrating Agents for Grounded Scientific Ideation](https://arxiv.org/abs/2610.04074) | candidate | 2026-10-02 | 11 | 11.07 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1095 | [Benchmarking large language model agent societies against human behavioural distributions](https://arxiv.org/abs/2608.28182) | candidate | 2026-08-28 | 11 | 11.04 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1096 | [Science Edge Evaluation: SEE the Missing Step Toward Real Scientific Discovery](https://arxiv.org/abs/2608.06931) | candidate | 2026-08-07 | 03;04;06 | 03.01 | SEE明确以化学、生物、材料实验实践构造题目并评测visual-agent工具使用；Agent条件与静态模型条件需区分。 |
| ASD-1097 | [SAIL: Scientific Agentic Intelligence via a Science-Aware Loop](https://arxiv.org/abs/2610.11451) | candidate | 2026-10-08 | 01;11 | 01.02 | SAIL全文有SciCode/DS-1000科研代码、文献检索综合和复现评测，暂支持01和知识生产11；其余学科任务映射待核，不放无对象01.04。 |
| ASD-1098 | [K-Bench: measuring model performance on real scientific agent requests](https://arxiv.org/abs/2608.21601) | candidate | 2026-08-21 | 02;03;04;06;07;09 |  | K-Bench全文按化学材料、临床健康、生命、物理工程四组报告真实请求评测；细分任务与二/三级类别留待清单复核。 |
| ASD-1099 | [Exploring Causal Mechanisms with Generative Agent-Based Models](https://arxiv.org/abs/2609.35819) | candidate | 2026-09-21 | 11 | 11.04 | 摘要初筛支持科研目标、多步工具/决策/反馈过程及对象任务；细节见所附原文证据，完整笔记与最终纳入待后续。 |
| ASD-1100 | [A Society of Researchers: Designing Institutions for Populations of Autonomous Research Agents](https://arxiv.org/abs/2610.10468) | candidate | 2026-10-07 | 01;11 | 11.07 | 研究者群体的制度分配实验以语言模型预训练效率为具体任务，同时涉及科研制度11和计算机科学01。 |
| ASD-1101 | [Forecasting the future of American mass shootings with Bayesian agent-based model calibration](https://doi.org/10.1093/pnasnexus/pgag294) | needs_review | 2026-09-22 | 11 | 11.04 | Agent资格、对象类别或来源证据仍有边界问题，保留逐篇审查队列。 主体有决策/交互与科学仿真结果，但其角色是科研行动者还是仅被模拟实体仍待全文；传统ABM及非LLM本身不是排除理由。 |
| ASD-1102 | [Network structure versus financial soundness in systemic risk: evidence from an improved agent-based model simulation of Chinese banks](https://doi.org/10.1093/comnet/cnag029) | needs_review | 2026-08-27 | 11 | 11.01 | Agent资格、对象类别或来源证据仍有边界问题，保留逐篇审查队列。 主体有决策/交互与科学仿真结果，但其角色是科研行动者还是仅被模拟实体仍待全文；传统ABM及非LLM本身不是排除理由。 |
| ASD-1103 | [Agent-based modeling for blockchain-based Ponzi scheme evolution and dynamics](https://doi.org/10.1093/imaman/dpag040) | needs_review | 2026-10-09 | 11 | 11.01 | Agent资格、对象类别或来源证据仍有边界问题，保留逐篇审查队列。 主体有决策/交互与科学仿真结果，但其角色是科研行动者还是仅被模拟实体仍待全文；传统ABM及非LLM本身不是排除理由。 |
| ASD-1104 | [When cardinals strategize: An agent-based model of influence and ideology for the papal conclave](https://doi.org/10.1016/j.chaos.2026.118411) | needs_review | 2026-08 | 11 | 11.03 | 教皇选举中枢机群体影响与意识形态决策属于政治制度对象；摘要来源不足时仅作待核线索，不能只按心理行为泛归11.04。 主体有决策/交互与科学仿真结果，但其角色是科研行动者还是仅被模拟实体仍待全文；传统ABM及非LLM本身不是排除理由。 |
| ASD-1105 | [From Search to Research: Exploring Search Scaling in Autonomous Quantitative Factor Mining](https://arxiv.org/abs/2609.35559) | candidate | 2026-09-28 | 11 | 11.01 | 50个金融因子任务中Agent理解假设、编程、评估和迭代，实际金融研究与检验流程明确。 |
| ASD-1106 | [AutoResearch at Production Scale: Failure Modes and a Multi-Agent Framework](https://arxiv.org/abs/2609.30541) | candidate | 2026-09-24 | 01 | 01.02 | 两个表征学习系统执行220余次训练试验，Agent迭代修改脚本、反馈保留并自主设计fallback，支持机器学习算法实验而非仅生产运维。 |
| ASD-1107 | [Autonomous Research for Open-Ended Problems: A Case Study on Telecom Ticket Retrieval](https://arxiv.org/abs/2609.13073) | candidate | 2026-09-11 | 01 | 01.02 | Agent执行电信工单检索的开放式机器学习研究，探索表征、架构和数据生成，属于计算机科学对象实验，而非仅客服运营。 |
| ASD-1108 | [Auto-RecSys: Harnessing Autonomous Research Agents for Industry-Scale Recommender System](https://arxiv.org/abs/2609.10922) | candidate | 2026-09-10 | 01 | 01.02 | 推荐模型的长程并行实验、结果反馈与想法演化是明确机器学习研究行动；工业应用不自动排除计算科学研究。 |
| ASD-1109 | [AutoLR: Automating the Path from Research to Launch Review in Industrial Recommender Systems](https://arxiv.org/abs/2609.04871) | candidate | 2026-09-04 | 01 | 01.02 | 多专家Agent辩论研究方向、分配试验预算、修改代码并训练/离线实验，支持推荐算法研究；线上发布是后续工程阶段。 |
| ASD-1110 | [RecSys Factory: Bounding LLM Agent Autonomy to Decision Points in the Industrial Recommender Lifecycle](https://arxiv.org/abs/2608.11241) | needs_review | 2026-07-31 | 01 | 01.02 | 平台有工具调用及有界自主决策，但主要报告工业推荐运维；需全文区分科研实验与运营流程。 |
| ASD-1111 | [Autonomous Floquet engineering of bosonic codes via reinforcement learning](https://doi.org/10.1038/s42005-026-02875-2) | candidate | 2026-09-23 | 02 | 02.02 | 强化学习反复选择Floquet控制参数，依据量子态保真度和噪声优化玻色编码制备；摘要支持物理研究控制与决策，后续核全文动作序列。 |
| ASD-1112 | [Life-inspired interoceptive artificial intelligence for autonomous and adaptive agents](https://doi.org/10.1038/s42256-026-01296-8) | background_only | 2026-08-26 | 对象映射待核 | 01.03 | Perspective提出内感受AI概念与数学抽象，未证明已实现科研Agent工作流，保留方法背景。 |
| ASD-1113 | [Provenance grounds trust in autonomous science](https://doi.org/10.1038/s43588-026-01035-4) | background_only | 2026-08-20 | 对象映射待核 | 11.07 | Comment讨论自主科学来源可信度，不当作新科研Agent研究论文。 |
| ASD-1114 | [Scale-aware self-driving laboratories for multiscale process development](https://doi.org/10.1038/s44160-026-01125-1) | background_only | 2026-07-29 | 对象映射待核 | 09.04 | Comment讨论工业多尺度过程开发与SDL，非新Agent实证研究。 |
| ASD-1115 | [Towards self-driving laboratories in the biopharmaceutical industry](https://doi.org/10.1038/s44160-026-01131-3) | background_only | 2026-08-04 | 对象映射待核 | 07.04/07.04.01 | Perspective归纳生物制药SDL工业应用和障碍，作为引用扩展背景。 |
| ASD-1116 | [ALBATROSS: A bioinspired, aerially deployable, autonomous sailing sensor platform](https://doi.org/10.1126/scirobotics.aed1423) | needs_review | 2026-09-30 | 10 | 10.03 | ALBATROSS有海上自主传感动机、导航决策及海试，需全文区分科研观测行动与仅航行控制；不因具身或RL自动确认科研Agent。 |
| ASD-1117 | [A large language model-based agent system for interactive large-scale project scheduling](https://doi.org/10.1093/jcde/qwag082) | candidate | 2026-09-14 | 09 | 09.01 | LangGraph/ReAct Agent检索工程进度图谱，调用分析、修改和优化工具，按分析反馈迭代大规模排程；真实船厂项目验证，暂归系统工程而非仅按船厂应用归海洋。 |
| ASD-1118 | [290. Individual Cattle as Agents and Their Behavior in Healthy and Disease States in an Integrated Beef Production System: An Agent-based Simulation Approach.](https://doi.org/10.1093/jas/skag272.243) | needs_review | 2026-09-29 | 08 | 08.03 | 会议摘要报告牛只SEIR状态、个体决策及生产阶段交互，比较疫苗和隔离情景；仅摘要，研究Agent角色及正式全文仍待核。 |
| ASD-1119 | [HorAgent: a state-aware intelligent agent for expert-in-the-loop seismic horizon interpretation](https://doi.org/10.1093/jge/gxag112) | candidate | 2026-09-07 | 05 | 05.01 | HorAgent维护项目状态，协调地震数据准备、模型训练、质量评估、稠密预测及导出；F3和Penobscot实测解释结果提供地球物理对象证据。 |
| ASD-1120 | [MacroRisk-agent: a retrieval-augmented multi-agent framework with deterministic validation gates for auditable stress testing](https://doi.org/10.1038/s41598-026-73453-3) | candidate | 2026-10-08 | 11 | 11.01 | RAG将金融压力情景转为参数，多Agent模拟流动性反馈，再反事实重仿真；公开金融数据与合成组合验证，不夸大为真实部署。 |
| ASD-1121 | [Modeling network evolution by multi-agent reinforcement learning](https://doi.org/10.1038/s41467-026-75382-1) | candidate | 2026-07-21 | 01 | 01.03 | 自主节点通过策略学习和协调互动驱动复杂网络演化，复现实网统计和情景结果，支持一般网络科学对象。 |
| ASD-1122 | [ASCENT: a tensor-oriented approach to population-scale agent-based simulation](https://doi.org/10.1038/s41598-026-61495-6) | needs_review | 2026-07-24 | 06 | 06.01/06.01.09 | ASCENT对蚊虫个体生命周期、遗传和空间迁移进行多步交互仿真，报告Príncipe基因驱动释放的种群结果；三级拟06.01.09。 主体有决策/交互与科学仿真结果，但其角色是科研行动者还是仅被模拟实体仍待全文；传统ABM及非LLM本身不是排除理由。 |
| ASD-1123 | [Proof carrying agent actions enable verifiable licensing of language model tool use](https://doi.org/10.1038/s41598-026-74900-x) | excluded | 2026-10-13 | 对象映射待核 | 01.02 | 通用工具动作许可与支付微基准，缺少明确科学研究目标和科研流程角色。 |
| ASD-1124 | [Designing dynamic pricing for bike-sharing systems via differentiable agent-based simulation](https://doi.org/10.1038/s41598-026-73657-7) | needs_review | 2026-10-14 | 10;11 | 10.04 | 异质用户概率选择的Agent仿真与定价梯度优化耦合，含NYC Citi Bike实验；交通系统和用户经济选择为具体对象。 主体有决策/交互与科学仿真结果，但其角色是科研行动者还是仅被模拟实体仍待全文；传统ABM及非LLM本身不是排除理由。 |
| ASD-1125 | [A machine learning and agent-based modeling framework for tourism crisis management](https://doi.org/10.1038/s41598-026-63675-w) | needs_review | 2026-07-30 | 11 | 11.01 | 旅游危机下利益主体、基础设施和市场动态ABM校准，报告12危机场景及反事实恢复轨迹；统计主张仍需全文审查。 主体有决策/交互与科学仿真结果，但其角色是科研行动者还是仅被模拟实体仍待全文；传统ABM及非LLM本身不是排除理由。 |
| ASD-1126 | [A multimodal agent for ceramic management via LLM-driven knowledge and visual synergy](https://doi.org/10.1038/s40494-026-02868-y) | candidate | 2026-09-04 | 11 | 11.06 | CeramicAgent按结构化抽取、视觉分割和知识图谱推理协同分析故宫陶瓷数据；历史证据与微特征解释提供考古科学对象。 |
| ASD-1127 | [DHCBT: a digital human psychological counseling system with a CBT multi-agent framework](https://doi.org/10.1038/s41598-026-73798-9) | excluded | 2026-10-04 | 对象映射待核 | 07.02/07.02.07 | CBT多Agent用于心理咨询服务和可用性评估，摘要未显示其承担科研行动流程。 |
| ASD-1128 | [A hybrid multi-agent and genetic algorithm framework for multi-objective spatial allocation in urban regeneration](https://doi.org/10.1038/s41598-026-60992-y) | needs_review | 2026-09-04 | 09;11 | 09.05 | 武汉城市更新中政府、开发商、居民Agent反复协商并反馈遗传搜索；具体城乡规划与城市社会行为仿真结果。 主体有决策/交互与科学仿真结果，但其角色是科研行动者还是仅被模拟实体仍待全文；传统ABM及非LLM本身不是排除理由。 |
| ASD-1129 | [A Monte Carlo enhanced agent based model for Tokenized BIM Twin (TBT) resource reallocation in construction projects](https://doi.org/10.1038/s41598-026-66059-2) | needs_review | 2026-09-29 | 09 | 09.05 | 建设参与者在BIM/数字孪生/合约框架中交互、检测偏差和重配资源，450次蒙特卡洛场景结果；仅模拟，研究角色待全文细核。 主体有决策/交互与科学仿真结果，但其角色是科研行动者还是仅被模拟实体仍待全文；传统ABM及非LLM本身不是排除理由。 |
| ASD-1130 | [A multi-agent game-theoretic adversarial training framework with latency-aware reward shaping for robust high-frequency trading strategy design](https://doi.org/10.1038/s41598-026-60518-6) | candidate | 2026-07-13 | 11 | 11.01 | 交易主体和对抗Agent交替最小最大训练，依据订单簿仿真与延迟反馈优化策略；明确仅模拟性能。 |
| ASD-1131 | [Causal asymmetry of classical and quantum autonomous agents](https://doi.org/10.1038/s41534-026-01335-7) | background_only | 2026-09-01 | 对象映射待核 | 02.02 | 自主Agent在此是随机过程变换的经典/量子记忆数学主体，摘要未显示Agent承担科研工作流；暂作理论背景。 |
| ASD-1132 | [Agent-based modeling of low-emission fertilizer adoption for dairy farm decarbonisation using empirical farm data](https://www.nature.com/articles/s41598-026-63267-8) | needs_review | 2026-07-25 | 08 | 08.01 | 原排除理由‘模型是研究工具，不是自主 Agent’过于一刀切，忽略了本综述四项标准允许自主决策及 Agent 模型作为研究对象的空间。建议从 screened_out 改为 needs_review/candidate，交控制器明确本综述是否包含作为计算实验主体的传统 ABM。就农业对象分类而言，具体涉及农业环境与农场决策；建议 08.01.05（农业资源与环境）为首选，并可按论文实际的畜牧经营覆盖考虑 08.03.01。 |
| ASD-1133 | [RAVA: a robust recurrent active vision agent for plant disease diagnosis under severe environmental noise](https://www.nature.com/articles/s41598-026-67160-2) | needs_review | 2026-09-04 | 08 | 08.01 | 原排除理由‘没有科研 Agent workflow’低估了摘要所述的序贯感知策略和实验性鲁棒评测。建议至少改为 needs_review；若论文全文确认主动视野策略是部署/研究评测的核心且有明确动作轨迹，可纳入模块08植物保护。不能因为它解决病害诊断就按普通单次分类器排除，因其方法具有多步自主观察决策。 |

## 既有记录命中（不新增ID）

| 既有ID | 命中题名 | 本轮来源 |
|---|---|---|
| ASD-0118 | Autonomous biomedical research with an artificial intelligence agent | october_round2_C_life_health.json |
| ASD-0892 | The Virtual Biotech: A multi-agent AI framework for therapeutic discovery and development | october_round2_C_life_health.json |
| ASD-0902 | Perturb-ME: Scalable mechanism discovery from phenotype-enriched genome-wide screens | october_round2_C_life_health.json |
| ASD-0901 | scBaseCount: An AI agent-curated, standardized, auto-updated single-cell data repository | october_round2_C_life_health.json |
| ASD-0880 | Can Autonomous LLM Agents Execute Multireference Quantum Chemistry Calculations? | october_round2_D_formal_physics.json |
| ASD-0907 | SciExam for ENSO: Can AI Agents Build Climate Models? | october_round2_D_formal_physics.json |
| ASD-0883 | GBClaw: An agentic AI framework for atomistic grain boundary research and mechanistic discovery | october_round2_D_formal_physics.json |
| ASD-0888 | SQD-Agent: LLM-driven agentic framework for Quantum Chemistry workflows | october_round2_D_formal_physics.json |

## 文件与数据同步

控制文件：`Paper_Lists/october_round2_search_control_2026-10-22.md`；详细裁决：`Coverage_Check/october_round2_controller_decisions.json`；来源与两次独立复核：同目录`october_round2_*.json`/`*_log.md`；逐领域新增清单：`Paper_Lists/october_round2_*_2026-10-22.md`。

按既有精简发布规则，master、Notes、Paper_Lists、Coverage_Check和检索缓存保留本地；GitHub仅同步已有允许清单中的结构化数据。未强制加入内部检索材料。

## 最终数据校验

主控已逐条取得211条新增记录的一手来源元数据与摘要；这不等于完成全文阅读。`scripts/run_structured_data_pipeline.py`运行成功，结构化导出、一致性检查及SQLite构建全部通过：1133条论文、494篇确认核心、441篇核心有本地PDF、53篇核心缺PDF，工作流分类镜像的语义、顺序和总量偏差均为0。

结构化分类词表补齐既有分类树中的08.03、09.08、10.03、11.06四个分支，并记录影响；未新建分类体系。数据库构建脚本将待定分类枚举的空值保存为NULL，保留未定状态并满足原有约束。198篇研究候选/边界记录仍待全文审查，本轮没有核心晋升。
