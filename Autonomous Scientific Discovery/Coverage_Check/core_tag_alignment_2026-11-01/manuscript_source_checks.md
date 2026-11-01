# 正文第三步补强：六篇代表论文一手证据核对

核对日期：2026-11-01。用途：为贡献类型、失败传播与恢复、多 Agent 协作、安全与权限、预算及学习机制分析提供可复核的窄范围事实。本文件为审阅产物，不修改论文正文、主列表或笔记。

所有页码均指本地 PDF 页码，从 1 开始；使用 PyMuPDF（`fitz`）提取。短引文仅合并换行，不改变原文含义。下列 source 路径相对于 `Autonomous Scientific Discovery/`；正文路径相对于工作区根目录。

## 1. 当前正文及可补强位置

已核对当前 Overleaf 的以下四节：

- `Agent_for_Science_Review_Overleaf/sections/conceptual_framework.tex`
- `Agent_for_Science_Review_Overleaf/sections/discussion.tex`
- `Agent_for_Science_Review_Overleaf/sections/paradigms_and_transfer.tex`
- `Agent_for_Science_Review_Overleaf/sections/future_directions.tex`

适合补强的位置：

| 正文位置 | 可由一手证据支持的补强 | 必须保留的边界 |
|---|---|---|
| `discussion.tex`：失败与评估段落 | MechAgents 的科学量错误与人类修正；Aleks 的泄漏与指标混淆；ChemCrow 的评估器失效 | 将不同错误链分开；不把执行成功等同科学正确 |
| `conceptual_framework.tex`：职责分配表 | Virtual Lab 的代理决策与人类执行；Sciencecraft 的目标输入、规划和命令执行 | 记录实际职责；未报告权限分配保持未报告 |
| `paradigms_and_transfer.tex`：协作与机制互补 | MechAgents 的特定任务互相纠错；AI co-scientist 的调度、状态、Meta-review | 不由个案推出多 Agent 普遍优势；不把提示更新写成权重学习 |
| `future_directions.tex`：恢复、安全、学习、成本 | 已有停止条件、错误反馈、预算记录及其限制 | 同预算比较、权限撤销、恢复率、全面成本核算仍是研究建议 |

证据状态采用：**观察**（论文报告发生的事件或结果）、**实施机制／职责**（系统实现或明确分工）、**作者建议**（未来方向或风险讨论）、**边界**（该证据不能支持的进一步推断）。实施了某机制，不等于已经报告其有效性或故障恢复率。

## 2. MechAgents — ASD-0128

**source：** `Reference_PDF/09_Engineering_and_Industrial_Technology_Sciences/Ni_2024_MechAgents.pdf`，25 页。

### 2.1 运行错误触发的自动修复

- **观察，PDF p3：** 初始线弹性脚本遗漏材料参数，执行反馈暴露 `lambda_` 和 `mu` 未定义；代理据此补充由杨氏模量及泊松比计算 Lamé 常数的代码。作者报告两轮调试后得到正确脚本。
- **短引文，p3：** “After two rounds of such debugging, the team renders a correct script”。
- **可支持的分析：** 运行错误 → 执行反馈 → 代码修复，是论文实际观察到的一种恢复路径。
- **边界：** 这不意味着所有科学错误都会产生运行错误，也不是跨任务的恢复率评估。

### 2.2 静默科学量错误及人类修正

- **观察，PDF p4：** 用户请求剪切应力分量 `σxy`，助手实际提取 von Mises 应力；脚本成功执行后，助手结束任务，没有发现错误。
- **短引文，p4：** “the assistant agent mistakenly extracts von Mises stress”；“without realizing its mistake”。
- **观察，PDF p4：** 下一轮获得人类明确指正后，代理一次修正并完成请求。
- **短引文，p4：** “when instruction from human intervention is provided”；“correct this mistake in one shot”。
- **可支持的分析：** 执行状态不能验证请求的科学量；概念性错误可能需要独立于运行反馈的审查。
- **边界：** 该例不能写成系统独立恢复。原文随后提到外部批评可以由其他专门代理提供，但不能用这一可能性替换该例实际发生的人类干预。

### 2.3 特定任务中的多代理互相纠错

- **观察，PDF p6：** 含孔铜板任务中，两代理团队遗漏孔洞、正确弱形式、必要材料参数和正确牵引计算；成功执行后仍认可结果。
- **观察，PDF p6–8：** 同一任务交给较大分工团队后，critic 发现缺孔及不合理零牵引；engineer 修正边界标记／积分，完成任务。
- **短引文，p7：** “The code execution was successful, but the total force on the right edge is reported as 0.0, which seems incorrect.”
- **实施机制，PDF p5、10：** 团队分为 admin、planner、scientist、engineer、executor、critic 和 group-chat manager；manager 根据当前讨论与角色动态选择发言者。
- **可支持的分析：** 角色分工和外部批评在所展示任务中帮助识别没有运行报错的异常。
- **边界：** 这是特定任务对照，不是经过相等计算预算、token 或人工投入控制的多 Agent 普遍优势证明。critic 认可某个最终数值，也不能替代外部数值验证。
- **作者建议，PDF p8–10：** fine-tuned agents、检索增强、角色及聊天拓扑优化属于未来方向，不能当成该系统已执行的学习机制。

可直接用于正文的窄范围英文句：

> In MechAgents, execution feedback repaired missing code definitions, whereas a successfully executed script returned von Mises stress instead of the requested shear component; correcting that conceptual error required a human instruction.

## 3. Aleks — ASD-0634

**source：** `Reference_PDF/08_Agricultural_Food_Forestry_Animal_and_Fishery_Sciences/Jin_2025_Aleks.pdf`，14 页。

### 3.1 两种不同失败不能合并

- **观察，PDF p9：** 仅保留当前迭代历史的 Exp3，在 2024 预测问题第 14 轮出现 data leakage，下一轮得到纠正。
- **短引文，p9：** “a case of data leakage was identified at iteration 14”；“Although corrected in the following iteration”。
- **边界：** 此段没有清楚说明是谁识别并实施纠正。可写“下一轮得到纠正”，不能补写为人类或 DS agent 独立发现。
- **观察，PDF p9–10：** Exp4 原报告的 2024 最佳结果异常突出，促使人类科学家复查；人工验证发现最终迭代代码混淆训练与测试阶段指标。次优模型结果与其他运行相当。
- **短引文，p9：** “a coding error that conflated performance metrics between the training and testing phases”。
- **短引文，p10：** “the only instance where such a coding bug occurred and went undetected”。
- **可支持的分析：** 数据泄漏与训练／测试指标混淆是两条独立失败链；其中后一条直到人工复查才暴露。不能写成系统自动发现并纠正了全部错误。

### 3.2 共享历史、访问范围与执行反馈

- **观察，PDF p8–9：** 限制 DA 访问历史后，已评估且无益的特征会重复出现，特征选择较不连贯。
- **边界：** 该观察不能证明完整历史保证没有泄漏，也不能给出一般化的错误发生概率。
- **实施机制，PDF p4–5：** MLE 工作记忆限于当前任务、数据和建模建议；DA 可使用完整实验历史；记录按代理访问权限共享。
- **短引文，p4：** “according to their access privileges”。
- **实施机制，PDF p4：** 生成代码在 subprocess 中运行，错误信息反馈给 MLE 提示，直到取得有效解或达到重试上限；提示还设置内存使用和程序运行时间约束。
- **短引文，p4：** “until a valid solution is obtained or retry limits are reached”。
- **边界：** 这些是系统实现和提示约束，不是正式证明的权限隔离、资源强制执行或安全保证。

### 3.3 预算、leaderboard 与跨年评估

- **预算，PDF p6：** 研究预算定义为最多 20 次迭代，由小规模预试验决定。
- **短引文，p6：** “The research budget, defined as a maximum of 20 iterations”。
- **边界：** 这不是金钱、token 或固定训练算力预算。
- **观察，PDF p9：** 在完整历史上增加简化 leaderboard，没有带来明显行为或性能改善；20 轮记录当时能装入模型上下文。
- **短引文，p9：** “the token limit was not a constraint”。
- **边界：** 不能据此写成 leaderboard 已解决长上下文扩展；作者把复杂任务中的潜在收益留待未来研究。
- **评估设计，PDF p6、12：** 跨年验证将某年选出的特征方案用于训练另一年的模型，反向亦然。
- **短引文，p6：** “the optimal feature set … was used to train a model … and vice versa”。此处省略号仅标示摘取的句内间隔。
- **边界：** 应称为特征／建模建议的跨年复用与重新训练，不是冻结模型的零样本跨年迁移。
- **观察，PDF p12：** 论文称最佳模型用于生成空间图，帮助人类研究者选择商业葡萄园组织采样位置。
- **边界：** 这不等于已由系统自主开展新的田间干预实验或发现新病理机制；原文明确当前未完整整合收集新数据的硬件。
- **作者建议，PDF p10、12：** 用正式方法检查生成代码、处理共享偏差和错误传播，是研究方向；对多代理强化共享偏差的讨论不是本研究量化的发生率。

可直接用于正文的窄范围英文句：

> Aleks illustrates two distinct failure paths: leakage appeared under restricted historical context and was corrected in the next iteration, whereas a separate training–test metric conflation remained undetected until manual review.

## 4. ChemCrow — ASD-0093

**source：** `Reference_PDF/03_Chemical_Sciences/Bran_2024_ChemCrow.pdf`，38 页。

### 4.1 评估器失效的观察与具体例子

- **观察，PDF p5–6、20：** 四名专家从化学正确性、推理质量、任务完成度评估；专家总体偏好 ChemCrow，而 EvaluatorGPT 平均更偏好 GPT-4。
- **短引文，p6：** “typically basing its results in the fluency and apparent completeness of its responses”。
- **观察，PDF p21：** Takemoto organocatalyst 案例中，GPT-4 路线不能得到目标，并含不必要保护／脱保护及可能损失手性的操作。EvaluatorGPT 仍给出更高评分，称其“addresses stereochemistry and protecting group strategies”。
- **可支持的分析：** 这是一条可审查的评估失效链，不只是生成系统能力不足；流畅且看似完整的答复可能掩盖化学错误。
- **边界：** 结论限于论文所测任务、模型和评估设置，不能推广成所有 LLM 评估在所有科学任务中失效。

### 4.2 工具接口和安全停止条件

- **实施／机制分析，PDF p5：** 工具质量、输入质量及调用推理相互影响；工具输出不准确可导向错误结论。
- **短引文，p5：** “inaccurate outputs from the tools can lead the agent to wrong conclusions”。
- **边界：** 该段支持接口错误传播机制，没有量化端到端传播概率。
- **实际实施的安全措施，PDF p6–7、10：** 请求合成方法或执行时自动调用 `ControlledChemicalCheck`；名单命中则停止。
- **短引文，p10：** “the agent immediately stops execution”。
- **可支持的分析：** 这是工具层实际实现的停止条件。
- **作者建议，PDF p6–7：** 额外专家审查、访问控制、更广泛验证系统以 “could involve／could be incorporated” 等形式提出。
- **边界：** 不能将所有建议都写成已部署权限系统；名单检查也不等于全面化学安全验证。

## 5. AI co-scientist — ASD-0115

**source：** `Reference_PDF/07_Medical_and_Health_Sciences/Gottweis_2025_Co_Scientist.pdf`，81 页；本地版本为 *Towards an AI co-scientist*。

### 5.1 协作的具体组织机制

- **实施结构，PDF p7–9：** Supervisor 管理异步 worker 队列、分配专门代理和计算资源。六类代理为 Generation、Reflection、Ranking、Proximity、Evolution、Meta-review。
- **短引文，p7：** “manages the worker task queue”；“allocates resources”。
- **实施机制，PDF p9：** Supervisor 根据假设数、待审状态、tournament 进展及生成策略表现，对代理执行重新加权与采样。
- **可支持的分析：** 协作贡献可具体写成任务调度、共享状态和反馈分配，不必仅泛称集体智能。
- **实施设计，PDF p8：** 持久上下文保存代理和系统状态；作者称其使组件故障后的重启更容易。
- **短引文，p8：** “easy restarts in-case of any failure in the system components”。
- **边界：** 这是恢复支持设计，不是报告恢复次数、耗时或成功率的故障实验。

### 5.2 “学习”与计算扩展的实际含义

- **实施机制，PDF p9–10：** Meta-review 汇总审查结果，反馈下一轮追加到代理提示；不使用反向传播、fine-tuning 或 reinforcement learning。
- **短引文，p9：** “learning without back-propagation techniques”。
- **短引文，p10：** “simply appended to their prompts in the next iteration”。
- **边界：** 不应把该机制写成已执行权重更新或策略训练。
- **观察，PDF p15–16：** 203 个研究目标上，较晚时间桶的假设获得更高 Elo；15 个专家整理目标另作基线比较。
- **短引文，p15：** “the Elo metric is auto-evaluated and not based on independent ground truth”。
- **边界：** 这支持内部 Elo 评分下的计算扩展趋势，不能等同于独立验证的科学发现质量随预算增加。论文 p16 也指出此指标可能偏好未必符合科学家偏好、质量或准确性的属性。

### 5.3 当前安全机制与人类最终决策

- **实施机制，PDF p29–30：** 输入研究目标安全审查；不安全假设不进入 tournament、不继续发展且不呈给用户；另有研究方向监控、日志和推理记录。
- **职责，PDF p30：** 系统设计保留持续专家监督及人类最终决策。
- **短引文，p30：** “final decisions are always made by scientists exercising their expert judgment”。
- **作者建议，PDF p29：** 更广泛的访问控制、逐步发布、人工审查标记等，应与当前实现的安全机制分开叙述。
- **边界：** 有安全审查机制，不等于不存在漏检、对抗绕过或不安全中间步骤；本记录不增补原文未核对的有效率数值。

## 6. Virtual Lab — ASD-0054

**source：** `Reference_PDF/07_Medical_and_Health_Sciences/Swanson_2025_Virtual_Lab_Nanobodies.pdf`，22 页；Nature 版本。

### 6.1 人类与代理的职责

- **职责，PDF p3、9：** 人类提供会议议程、问题及规则，设讨论轮数和发言顺序；PI 综合意见并形成建议，Scientific Critic 提供反馈。
- **短引文，p9：** “with N set by the human researcher”。
- **职责，PDF p6：** 代理编写 ESM、AlphaFold-Multimer、Rosetta 脚本；人类另写适配基础设施的数据处理与作业调度脚本，全部脚本由人类运行。
- **短引文，p6：** “All scripts were run by the human researcher in accordance with the decisions made by the agents.”
- **职责，PDF p5–6：** 表达及结合验证由人类研究者实施。
- **边界：** 支持代理设计／选择、人类执行／验证的责任分布；不支持机器人湿实验自主执行，也不能由 human-in-the-loop 推断每项行动都有正式审批闸门。
- **观察，PDF p3：** 实现阶段设额外会议修代码；ESM 与 AlphaFold-Multimer 各一次，Rosetta 两次。
- **可支持的分析：** 恢复有额外迭代成本，不能将第一次生成等同最终可执行成果。

### 6.2 成本和时间必须按阶段核算

- **预算，PDF p6：** 会议阶段约 1–2 小时、US$10–20 GPT-4o token 成本；每次会议或并行会议组约 5–10 分钟、US$1–2。
- **短引文，p6：** “1–2 h (US$10–20 GPT-4o token cost)”。短引文按原文字义记录时间和费用，PDF 排版使用细空格。
- **预算，PDF p6：** 加入提示调整及人工审阅调试后，流程设计用数日；计算设计管线约一周，纳米抗体合成约六周，结合实验约两周。
- **边界：** 不能写成整个经过实验验证的发现仅花 20 美元或两小时；论文估计的独立人类工作数周，也不是同预算受控比较。
- **观察，PDF p6：** 人类会议文字为 1,596 words，占 1.3%。
- **边界：** 这不是人类劳动时间或责任占比；脚本运行、额外代码、调试和实验工作均不能由此省略。

### 6.3 协作和安全权限的证据边界

- **观察／分析，PDF p6–7：** 角色化团队、Scientific Critic、并行会议对讨论输出质量的帮助，有论文讨论分析及补充消融支撑。
- **边界：** 不应把会议回答质量直接等同于每项下游实验指标的改善。
- **作者建议，PDF p7：** 能让代理独立安装、调试和运行工具的 sandbox 属于未来工作。
- **短引文，p7：** “future work could explore developing sandboxed environments”。
- **边界：** 当前论文不能作为这种独立执行权限已经实现的证据。

## 7. Sciencecraft — ASD-0645

**source：** `Reference_PDF/10_Aerospace_Marine_and_Transportation_Sciences/Tran_2004_Autonomous_Sciencecraft_EO1.pdf`，2 页；AAAI 2004 演示论文。

### 7.1 已报告的在轨运行

- **观察，PDF p1：** 2003 年秋上传后，ASE 已指挥 EO-1 运行，并实现自主重定向以捕捉动态科学事件。
- **短引文，p1：** “has successfully commanded EO-1 operations and enabled autonomous retargeting”。
- **边界：** 可以写软件已在轨执行，不能把论文所有拟演示功能都写成已在轨实测。

### 7.2 目标、规划、执行和资源边界

- **职责／实施机制，PDF p1：** 科学团队上行目标，或机载科学分析模块插入目标；CASPER 根据航天器约束模型生成计划；SCL 把计划展开为低级命令并监控执行，也处理局部异常。
- **短引文，p1：** “goals uplinked by the EO-1 Science Team or inserted by the onboard science analysis module”；“local responses to anomalies”。
- **预算／环境，PDF p1：** 每天八次、每次约十分钟通信机会；EO-1 团队为全部 ASE 软件分配 4 MIPS。
- **短引文，p1：** “allocated 4 MIPS for all of the ASE software”。
- **可支持的分析：** 资源和通信边界塑造决策及执行设计；自主性不是代理数量的同义词。
- **边界：** 两页论文没有报告逐动作人类审批、权限撤销、异常恢复率或安全事件率，不能由模型约束和监控架构推断这些已测量。

### 7.3 完整科学响应是模拟演示

- **计划的模拟演示，PDF p2：** 火山检测后建议追加观测、云遮挡后建议删除低价值图像及替换目标、CASPER 重排计划，属于完整 science-response 模拟演示的描述。
- **短引文，p2：** “The second part of the demonstration will simulate an ASE mission scenario.”
- **短引文，p2：** “command a software simulation of the EO-1 spacecraft”。
- **边界：** 这些具体响应不可全部称为该文报告的真实在轨事件。论文第一页的已在轨运行，与第二页的完整模拟演示必须分别归因。

## 8. 当前 domain_synthesis.tex 的 Sciencecraft 核对

核对文件：`Agent_for_Science_Review_Overleaf/sections/domain_synthesis.tex`。

**结论：当前版本没有混同模拟与在轨证据，不需要因本项核对而改写。**

- **第 80 行**明确同时记录在轨运行和模拟情景：

  > Its software was already commanding the spacecraft in orbit, although the conference demonstration also included a simulated science-response scenario. The distinction matters when attributing evidence to operational or simulated behavior.

  前半句对应 PDF p1 的已在轨运行，后半句对应 PDF p2 的完整模拟演示；归因边界与原文一致。

- **第 84 行**将 operators／onboard analysis 提供目标和规划执行机制，与自主问题形成、额外科学收益分开：

  > Replanning establishes responsiveness under those models; autonomous question formation and additional scientific return require separate evidence.

  这一行保留了科学贡献边界。它不是火山或云遮挡情景已经在轨完成的声明。

- 当前第 80 行没有逐项列举火山追踪或云遮挡数据删除，因此不存在这些具体模拟功能被误记为在轨事件的问题。

## 9. 可用于综合论述的最小结论

以下概括有逐例观察支持，但范围限于所核对案例，不表示全库频率：

> Successful execution can leave scientific errors undetected, while recovery depends on the information available to the reviewing agent or human. Multi-agent organization changes task allocation and feedback routes; its scientific benefit must be assessed separately from additional computation, internal scoring, and the human work needed to execute and validate the proposed investigation.

同预算比较、干预成本核算、权限撤销测试和恢复率测量，应明确作为本综述提出的研究建议，不能写成上述六篇已共同完成的验证。
