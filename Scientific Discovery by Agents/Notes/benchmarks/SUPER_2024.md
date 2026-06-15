# SUPER 2024

## 基本信息
- **论文**: SUPER: Evaluating Agents on Setting Up and Executing Tasks from Research Repositories
- **作者**: Ben Bogin, Kejuan Yang, Shashank Gupta, Kyle Richardson, Erin Bransom, Peter Clark, Ashish Sabharwal, Tushar Khot (AI2 / University of Washington)
- **年份**: 2024
- **来源**: arXiv:2409.07440 (EMNLP 2024)
- **关键词**: benchmark, reproducibility, code-execution, agent-evaluation, ML/NLP

## 核心思想
SUPER（Setting UP and Executing tasks from Research repositories）是首个评估 LLM 智能体从研究代码仓库中"设置并执行任务"能力的基准。当研究人员面对一个低知名度、文档不全的 GitHub 仓库时，即使是安装依赖、配置数据、修改代码、解决运行错误这类例行操作也极其耗时。SUPER 精准捕捉了这一真实痛点——聚焦于低知名度仓库（中位数仅 14 个 GitHub stars），要求智能体完成从环境搭建到实验执行的全流程。基准包含三组问题：Expert 集（45 个端到端问题，附带专家编写的金标方案）、Masked 集（152 个子问题，通过对专家方案进行"代码掩码"提取，聚焦特定挑战类型）、Auto 集（604 个自动生成问题，用于大规模开发）。当前最强模型 GPT-4o 在 Expert 集上仅解决 16.3% 的端到端任务，在 Masked 子问题上解决 46.1%；开源模型表现大幅落后。SUPER 揭示了 LLM 智能体在"真实科研复现"场景下与人类仍有巨大差距，其核心短板在于仓库理解（需要浏览和读懂多文件代码结构）而非调试已知错误。

## 基准设计
- **三组问题集**：(a) Expert——45 个手动编写的端到端任务（基于 PapersWithCode 数据库筛选 2021 年后的 NLP/ML 仓库），包含在默认/自定义数据集上训练/评估模型的场景，由 Upwork 专家标注金标方案（平均 44.3 行代码、14.4 个 Notebook 单元）；(b) Masked——从 Expert 金标方案中通过"代码掩码"机制提取 152 个子问题，模拟"已有部分代码前缀，需完成剩余操作"的场景，分为 7 类：Goal(25.0%)、Issue(23.7%)、Dependencies(19.7%)、Data(12.5%)、Other(9.2%)、CPU(7.2%)、Configuration(2.6%)；(c) Auto——从 5,915 个仓库出发，经启发式规则 + GPT-4o 过滤（支持指定数据集/模型/CPU 运行/含可运行脚本），保留 1,006 个仓库，再让 GPT-4o 基于 README 生成任务，共 604 个。采样 100 个验证，81% 可行。
- **执行环境**：基于 Jupyter Notebook 引擎，同时支持 Python 代码和 Bash 命令的执行，状态在单元间保持。在 Modal 平台上沙箱化运行，单任务执行 2-3 美分（不含 API 费用）。
- **双轨评估**：(a) 精确度评估——将智能体输出的指标值与金标答案对比（容忍误差 10^-2）；(b) 里程碑评估——从金标方案中提取 2-6 个关键输出模式（如 "*** training completed ***"），检测智能体轨迹中是否触及这些里程碑，允许部分得分。
- **Auto 集代理指标**：Script-Executed——检查目标脚本是否在无异常情况下运行满最短时长（与里程碑评估 90% 一致，与精确度评估 69% 一致）。
- **基线智能体**：ReAct（标准思考-行动-观察循环）、ReAct-SUPER（增加 edit 命令，通过精确文本匹配替换文件内容，而非依赖 sed 或行号）、SWE-Agent（提供丰富的文件浏览/编辑/滚动工具）。
- **资源限制**：执行时间 30 分钟，Masked 子问题 token 上限 400k，Expert/Auto 任务 token 上限 600k；训练需 CPU 即可（通过限制小模型、小数据集、少 epoch 实现）。
- **低知名度仓库**：Expert 集仓库中位数 14 星（对比 DS-1000 35,309、ML-Bench 9,632、SWE-bench 12,557），Auto 集中位数 23 星。

## 关键数字
- Expert 集（端到端）：GPT-4o + SWE-Agent 16.3% 精确度 / 36.8% 里程碑；GPT-4o + ReAct-SUPER 14.4% / 42.6%；GPT-4o Mini + SWE-Agent 仅 3.3% / 16.1%
- Masked 集（子问题）：GPT-4o + SWE-Agent 46.1% 精确度 / 74.9% 里程碑；GPT-4o + ReAct-SUPER 41.6% / 72.5%；Llama 3.1 70B 仅 17.4%-22.8%
- Auto 集（Script-Executed）：GPT-4o + ReAct-SUPER 18.8%，SWE-Agent 18.0%，GPT-4o Mini 5.2%-16.0%
- 开源 vs 闭源差距：Mixtral 8x22B 在 Expert 上仅 1.1% 精确度、0% 里程碑
- Reflexion（失败后反思重试 k=3）：Masked 上精确度从 41.6% 微弱提升至 45.4%，里程碑从 72.5% 至 76.6%
- 金标方案平均 44.3 行代码、14.4 个 Notebook 单元、3 个里程碑
- 任务难度分层（Masked 精确度）：CPU 73% > Issue 61% > Dependencies 54% > Goal 43% > Configuration 38% > Data 27%
- 智能体常见错误：跳过仓库浏览直接幻觉脚本参数（如添加不存在的 n_examples=10），或遗漏脚本参数；一旦采用某个方案就不重新考虑直到失败

## 设计哲学
- **"低知名度仓库"作为核心挑战**：SUPER 的关键设计选择是聚焦低知名度仓库（而非 SWE-bench 的知名开源项目或 ML-Bench 的热门仓库）。理由是：(a) 低知名度仓库文档/维护质量差，设置成本高，这正是科研复现中最耗时的部分；(b) 热门仓库的训练/执行模式可能已被 LLM 在预训练中记忆，评测失去了对"真实理解和推理"的区分度。
- **从端到端到子问题的逐级拆解**：借鉴完形填空（Cloze Test）和掩码语言模型（MLM）的思想，通过对金标方案"掩码"特定代码块生成子问题，既保留了金标评估的确定性，又提供了细粒度的诊断信号——能精确回答"智能体到底卡在哪类挑战上"。
- **计算亲和性设计**：刻意限制为 CPU 可运行、小模型、小数据、少 epoch，使得基准对硬件要求低，研究者可负担重复实验。但这些限制本身反而增加了任务难度——智能体需要修改 GPU 代码适配 CPU、限制数据加载、调整超参数等。
- **"精确度 + 里程碑"双评估机制**：精确度保证了结果正确性的严格评估，里程碑防止了"全有或全无"的评分缺陷——即使智能体未能完全完成任务，也能评估其进展。两者并非严格包含关系（完美里程碑不等于完美精确度，反之亦然），互为补充。
- **L 型评估器梯度**：Expert 集用于严格评测，Masked 集用于诊断分析，Auto 集用于大规模开发/训练。三级层次允许模型开发者在 Auto 集上进行快速迭代，避免过拟合到 Expert/Masked。且 Auto 集上模型排名与 Masked 集基本一致，验证了其作为开发代理的可靠性。

## 局限性
- Expert 和 Masked 集规模较小（45 + 152），统计显著性有限——尽管作者引用 tinyBenchmarks 等研究论证小规模高质量基准的有效性。
- 仅支持 Python 语言、文本模态的 NLP/ML 仓库；其他编程语言和科学领域（化学、生物等）的仓库复现挑战可能不同。
- 依赖外部资源（GitHub、pip、HuggingFace、Google Drive），不可控的外部变化可能导致评估结果无法完全复现。
- Script-Executed 代理指标与真实正确性有 31% 的不一致率（69% 一致性），Auto 集上的排名可靠性仍需进一步验证。
- Expert 集由 Upwork 平台雇佣专家标注，成本较高（未公开具体金额但有详细指南），限制了基准的持续扩展。
- 30 分钟/任务的执行限制和 600k token 上限对某些长训练任务可能不足。
- 训练数据截止后仓库可能变化（通过 git commit hash 和依赖版本列表缓解，但未来可能需更新）。

## 核心贡献
SUPER 2024 的核心贡献是把科研复现中最常见但常被低估的“设置并运行低知名度研究仓库”做成可执行 agent benchmark，并用 Expert / Masked / Auto 三层任务同时支持严格评测、错误诊断和开发迭代。

## 与综述的关联
SUPER 是"科学发现智能体执行能力"评测的核心基准，直接测量智能体能否完成科学发现流程中最基础也最被忽视的环节——"把别人的代码跑起来"。与 Paper2Code（生成代码）构成互补——Paper2Code 从论文出发生成新代码，SUPER 从已有仓库出发执行/修改代码。SUPER 的发现（智能体长于调试已知错误、短于理解多文件代码结构）揭示了当前 LLM 在科研自动化中的核心瓶颈：不是"写代码"能力不足，而是"读懂别人的代码并做出适应性修改"的能力严重欠缺。这一洞察对设计科学发现智能体的架构具有重要指导意义——未来系统需要更强的仓库理解与文件间导航能力，而非仅仅是更强的代码生成能力。SUPER 也与 CORE-Bench、PaperBench 一同构成评测科学可复现性智能体的完整生态。
