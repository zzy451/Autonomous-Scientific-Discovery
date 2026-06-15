# ScienceAgentBench 2025

## 基本信息
- **论文**: ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery
- **作者**: Ziru Chen, Shijie Chen, Yuting Ning, Qianheng Zhang, Boshi Wang, Botao Yu, Yifei Li, Zeyi Liao, Chen Wei, Zitong Lu, Vishal Dey, Mingyi Xue, Frazier N. Baker, Benjamin Burns, Daniel Adu-Ampratwum, Xuhui Huang, Xia Ning, Song Gao, Yu Su, Huan Sun
- **年份**: 2025
- **来源**: arXiv:2410.05080
- **关键词**: benchmark, scientific discovery, data-driven, peer-reviewed, ICLR 2025, code generation, self-debug

## 核心思想
该文呼吁在宣称端到端自动化科学发现之前，应先对智能体在科学工作流中的个体任务进行严格评估。为此提出 ScienceAgentBench，从 4 个学科的 44 篇同行评审论文中抽取了 102 个任务，并由 9 位领域专家（subject matter experts, SMEs）验证。输出标准化为自包含的 Python 程序文件，从程序正确性（Valid Execution Rate）、执行结果（Success Rate）、代码相似度（CodeBERTScore）和成本（API Cost）等多维度评估。提出两种策略应对数据污染（随机删除 5 个测试数据点 + 重分配测试集标签为 dummy 值）。主实验中最佳智能体（Claude-3.5-Sonnet + self-debug）独立解决率仅为 32.4%（配合专家知识为 34.3%）；另行评估的 o1-preview 达到 42.2%，但成本是其他模型的十倍以上且因 API 限制不纳入同一主分析。结论：当前智能体在数据驱动发现编码方面仍十分有限，远不足以端到端自动化科学研究。发表于 ICLR 2025。

## 评测目标
严格评估语言智能体在数据驱动科学发现中执行编码任务的能力。直接动机是对"AI 科学家"（如 Lu et al. 2024 宣称的 The AI Scientist）过度宣称的回应——作者认为，如果一个智能体不能完成科学工作流中的基础编码任务（数据处理、模型开发、可视化），就不应宣称能端到端做科研。现有基准不足：(1) SWE-bench/ML-Bench 聚焦通用软件工程而非科学编码；(2) MLAgentBench 任务少且限于 ML 实验；(3) DiscoveryBench 通过自然语言假设间接评估程序而非直接评估代码执行结果；(4) SciCode/BLADE 仅函数级别代码补全而非完整文件级程序生成；(5) 缺少对科学数据异质性的覆盖。ScienceAgentBench 的独特价值在于：从真实已发表论文中提取任务、多学科覆盖、领域专家全程验证、严格的多维度评估、防污染和防捷径设计。

## 基准设计
- **题目数量/来源/难度分级**：102 个任务（从 110 个初筛中经专家验证和复现测试后保留），来自 44 篇同行评审论文，覆盖 4 个学科——Bioinformatics、Computational Chemistry、Geographical Information Science、Psychology & Cognitive Neuroscience。每个任务包含 Task Instruction、Dataset Information、Expert-Provided Knowledge（可选）、Annotated Program（参考实现）。子任务类型分布：Data Processing 23、Feature Engineering 20、Model Development 23（Deep Learning 14 + ML 9）、Data Analysis 59、Info Visualization 65。
- **评分方式**：(1) Valid Execution Rate (VER)：程序能否无错误执行并输出正确文件名（二元）；(2) Success Rate (SR)：程序输出是否满足任务特定成功标准（如表 1 中的 ROC-AUC ≥ 0.77、top-5 药物匹配、math.isclose 判断等），对应每任务实现的评估程序；(3) CodeBERTScore (CBS)：生成程序与标注程序的语义相似度，SR=1 时自动设为 1.0；(4) API Cost：完成任务的平均 API 费用（USD）。对于图像输出任务，使用 GPT-4o 作为评委（3 次采样取均分）。每任务运行 3 次独立实验，选取最佳结果（优先 SR → VER → CBS → Cost）。
- **人类基线 vs AI 基线**：无受控人类基线（任务不涉及时间控制的人机对比），但有人工标注者参考——训练后的标注者平均需 2.5-3 小时改编现有程序，领域科学家从头编写可能更久。最佳智能体结果：Claude 3.5 Sonnet + self-debug without knowledge: SR 32.4%, VER 92.2%, CBS 86.4, Cost $0.057/task；with knowledge: SR 34.3%, VER 86.3%, CBS 87.1, Cost $0.061。Claude 3.5 Sonnet + self-debug 相比 OpenHands CodeAct 性能提升 10.8% 而成本仅为 1/17。GPT-4o + OpenHands 是唯一在 OpenHands 中表现尚可的模型（SR 19.6% no knowledge, 27.5% with knowledge）。o1-preview + self-debug: SR 42.2% no knowledge, 41.2% with knowledge, Cost $0.636/task。
- **设计原则**：(i) 与领域专家协作设计确保科学真实性；(ii) 统一输出为 Python 文件的严格评估；(iii) 多阶段质量控制（标注 → 专家验证 → 标注者交叉验证）；(iv) 数据污染减缓策略（随机删除测试数据点 + 测试标签替换为 dummy 值）；(v) 任务特定 rubric（5 阶段：Data Loading → Data Processing → Modeling/Visualization → Output Formatting → Output Saving）。

## 关键数字
| 指标 | 值 |
|------|-----|
| 任务总数 | 102 |
| 来源论文数 | 44（同行评审）|
| 覆盖学科数 | 4 |
| 专家验证人数 | 9（高年级博士生和教授）|
| 最佳独立 SR（no knowledge）| Claude 3.5 Sonnet + self-debug: 32.4% |
| 最佳独立 SR（with knowledge）| Claude 3.5 Sonnet + self-debug: 34.3% |
| o1-preview SR（self-debug, no knowledge）| 42.2% |
| o1-preview Cost/task | $0.636（其他模型 10x+）|
| Claude self-debug vs OpenHands SR 差距 | +10.8%（成本仅为 1/17）|
| Claude self-debug VER（no knowledge）| 92.2% |
| 直接 Prompting 最佳 SR | Claude 3.5 Sonnet 17.7%（no knowledge，Table 3 best-run 选择规则）|
| 标注者手动改编需时 | 2.5-3 小时/任务 |
| 智能体生成初稿需时 | <10 分钟/任务 |
| 测试框架数 | 3（Direct Prompting, OpenHands CodeAct, Self-Debug）|
| 测试 LLM 数 | 6（含 o1-preview 参考）|

## 设计哲学
- **"先走再跑"的方法论立场**：该文最鲜明的哲学立场——在端到端自动化科学发现之前，必须先证明智能体能完成其中的基础步骤。这是一种"分解验证"策略，与 MLE-Bench/RE-Bench 的端到端评估形成方法论互补。
- **科学真实性 > 规模**：102 个任务是中等规模（远小于 SWE-bench 的 2294），但每个任务都经历"论文提取 → 标注 → 专家验证 → 交叉验证"的多阶段质控流程。这种"深度质量优先于广度"的设计选择反映了对科学严谨性的追求。
- **反污染设计的前瞻性**：通过随机删除测试数据和替换测试标签，有效地使"背诵代码"的策略失效。这种做法在 ScienceAgentBench 和 CORE-Bench 中均有采用，代表了新一代基准的方法趋势。
- **cost-aware 评估**：将 API 成本作为正式评估指标之一，呼应了 Kapoor et al. (2024) 对"AI agents that matter"的呼吁——不仅报告性能，也要考虑实际效用和经济性。self-debug 以 1/17 的成本超越 OpenHands 的结果是这一哲学的最好例证。

## 局限性
- 102 个任务虽有一定覆盖面，但各学科分布不均（如 Computational Chemistry 和 Psychology 的任务较少）。所有任务均限定为"数据驱动的 Python 编码任务"，不涉及实验设计、假设生成、文献综述等更广泛科学实践。
- 专家知识提供方式不统一——不同专家提供的知识详尽程度和风格不同，可能影响对比公平性。
- 任务复杂度与金牌程序长度相关——超过 75% 的成功任务对应金牌程序 <58.6 行（均值），说明当前智能体主要在简单任务上成功，复杂任务仍是瓶颈。
- Rubric 评估仅基于金牌程序的实现路径，可能忽略等价但不完全相同的正确解答（如用随机森林替代神经网络）。
- 虽声称是对 The AI Scientist 等过度宣称的回应，但其评估与"端到端科研"之间的鸿沟仍无直接量化。
- 仅评估最终代码输出和结果，不评估智能体求解过程中的推理质量或科研洞察。

## 核心贡献
ScienceAgentBench 2025 的核心贡献是把“数据驱动科学发现中的基础编码任务”拆成可执行、可复现、可计成本的文件级程序生成评测，提供了一个反驳端到端自动科研过度宣称的分解验证基准。

## 与综述的关联
ScienceAgentBench 是本综述 benchmark 章节中最直接针对"科学发现"场景的基准。它区别于 MLE-Bench（ML 工程竞赛）、RE-Bench（ML 研究工程）、MLAgentBench（ML 实验迭代），聚焦于跨学科科学领域的计算任务。其核心方法论——从已发表论文中提取可复现任务、由领域专家验证、统一为自包含 Python 程序——为该类基准设立了质量标准。它也是少数把 API cost 作为正式评估指标的科学 agent 基准，与 Kapoor et al. (2024) 的"agents that matter"主张共振。
