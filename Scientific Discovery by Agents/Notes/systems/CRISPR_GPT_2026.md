# CRISPR GPT 2026

## 基本信息
- **论文**: CRISPR-GPT for agentic automation of gene-editing experiments
- **作者**: Yuanhao Qu, Kaixuan Huang, Ming Yin, Kanghong Zhan, Dyllan Liu, Di Yin, Henry C. Cousins, William A. Johnson, Xiaotong Wang, Mihir Shah, Russ B. Altman, Denny Zhou, Mengdi Wang, Le Cong
- **年份**: 2026
- **来源**: Nature Biomedical Engineering, doi:10.1038/s41551-025-01463-z; PMCID:PMC12920143
- **关键词**: autonomous-science, gene-editing, crispr, protocol-skill, wet-lab-validation, multi-agent

## 核心思想
这篇论文关注的是：CRISPR gene-editing 实验需要同时理解编辑系统、目标生物体系、递送方式、gRNA 设计、off-target 风险、验证 assay 和数据分析。虽然已有很多单点工具和协议，但从实验目标到可执行方案再到结果分析的端到端流程对新手仍然复杂。

作者提出 CRISPR-GPT，希望把 CRISPR 实验设计和分析组织成一个 LLM-powered multi-agent co-pilot，使非 CRISPR 专家的研究者也能在系统指导下完成真实 gene-editing 实验。

## 方法细节
CRISPR-GPT 是一个组合式多智能体系统，支持四类主要 gene-editing modalities：

- knockout
- base editing
- prime editing
- epigenetic editing（CRISPRa/i）

系统提供三种交互模式：

- **Meta mode**：面向新手，按照预定义任务顺序逐步指导完整流程。
- **Auto mode**：面向高级用户，用户提出自由形式请求，LLM Planner 自动拆解任务、处理依赖并执行定制 workflow。
- **Q&A mode**：回答临时 gene-editing 问题，结合 CRISPR-Llama3、RAG 文献检索和通用 LLM。

系统由四个核心组件组成：

- User proxy：代表用户与系统交互，用户可监控和纠正。
- LLM Planner：根据用户请求分解任务、选择任务链。
- Task executor：把任务作为 state machines 执行，每个 state 对应一轮用户输入、工具调用、输出反馈和状态转移。
- Tool provider：封装 Google search、Google Scholar、文献检索、Primer3、CRISPRitz、CRISPResso2 等工具。

作者强调，CRISPR-GPT 不直接让 LLM 任意调用 API，而是把工具封装在 state machine 内，用手写说明和结构化接口暴露给 human/LLM User proxy。这使系统更像“协议化 workflow + LLM 决策”的组合，而不是完全自由行动的 agent。

## 关键结果

1. **覆盖范围**  
   CRISPR-GPT 实现了 **22 个 gene-editing experiment tasks**，覆盖系统选择、实验规划、gRNA 设计、递送方法选择、off-target 评估、实验协议、验证 assay 和数据分析等环节。

2. **Gene-editing bench**  
   作者构建了 **288 个 test cases** 的 Gene-editing bench，覆盖四类任务：gene-editing planning、CRISPR gRNA design、delivery method selection、gene-editing Q&A。其中 planning、gRNA design、delivery method selection 各有 **50 个**测试案例，Q&A 有 **138 个**问题。

3. **Planning 任务表现**  
   在 gene-editing planning test set 上，GPT-4o 驱动的 CRISPR-GPT 在 accuracy、precision、recall、F1 上均超过 **0.99**，并且生成计划与专家 golden answers 的 normalized Levenshtein distance 低于 **0.05**。

4. **Delivery method selection 与 gRNA design**  
   Delivery agent 针对 **50 个 biological systems** 选择主要和备选递送方式，由三名人类专家评分形成 ground truth。CRISPR-GPT 优于 GPT-4 和 GPT-3.5-turbo，尤其在 hard-to-transfect cell lines 和 primary cell types 等困难任务上更明显。  
   gRNA design agent 使用 CRISPick 预设计表格并结合 LLM reasoning 处理用户约束；在 BRD4 案例中，CRISPR-GPT 能选择 Exon 3-4 这类功能关键外显子，而 CRISPick/CHOPCHOP 的默认排序中 **7/8** gRNAs 映射到可能无效的非关键外显子。

5. **Q&A mode 的知识增强**  
   作者收集从 2013 年开始的 **11 年** CRISPR Google Group 开放讨论，整理成约 **4000 个 discussion threads** 和 **3000+ question-answer pairs**，微调 8B Llama3-instruct，得到 CRISPR-Llama3。Q&A mode 同时使用 fine-tuned CRISPR-Llama3、约 **50 篇**专家选择的关键 CRISPR 文献 RAG，以及 GPT-4o。

6. **专家用户体验评估**  
   作者邀请 **8 名独立 CRISPR 专家**测试系统 web interface。每位专家在 Meta mode 下提出 1 个 gene-editing 请求，在 Auto mode 下提出 2 个请求，并收集完整 chat history。

7. **真实湿实验：A549 knockout**  
   一名不熟悉 CRISPR 的 junior PhD scientist 在 CRISPR-GPT 指导下，用 CRISPR-Cas12a 在 A549 human lung adenocarcinoma cells 中 knockout **TGFβR1、SNAI1、BAX、BCL2L1** 四个基因。系统指导 Cas 系统选择、lentiviral delivery、gRNA 设计、cloning、病毒递送、NGS 验证和 CRISPResso2 分析。结果显示四个靶基因均有约 **80%** 编辑效率。TGFβR1 和 SNAI1 knockout 后，EMT 相关 marker 变化被抑制：CDH1 expression change 最多降低 **9-fold**，VIM expression change 最多降低 **34-fold**。

8. **真实湿实验：A375 CRISPR activation**  
   一名不熟悉 CRISPR 的 undergraduate student 在系统指导下，用 CRISPR-dCas9 在 A375 human melanoma model 中激活 **NCR3LG1** 和 **CEACAM1**。目标蛋白表达检测显示成功激活，NCR3LG1 最高 **56.5%**，CEACAM1 最高 **90.2%**。

9. **first-attempt success**  
   两组湿实验均由不熟悉 gene editing 的初级研究者完成，并且论文称都在第一次尝试中成功，结果由编辑效率、生物学表型和蛋白水平验证支持。

## 与综述的关联

CRISPR-GPT 是“skill-driven scientific discovery”中 protocol skill 最强的新增样本之一。它把基因编辑实验拆成状态机、任务依赖、工具调用和用户交互，几乎直接对应我们 taxonomy 中的 protocol skill / workflow skill。

在 Scientific Workflow 上，它覆盖 Experiment Design、Execution、Result Analysis 和 Verification，尤其强在 wet-lab protocol design 与 validation assay。

在 Skill Lifecycle 上，它对应：

- Representation：22 个任务被实现为 state machines，Meta mode 中还对应四类完整 gene-editing workflow。
- Acquisition：来自专家手写指南、peer-reviewed literature、公开 CRISPR 讨论数据、RAG 和微调模型。
- Retrieval：Google/Google Scholar、专家选择文献库、FAISS embedding retrieval、CRISPick 表格、工具数据库。
- Composition：LLM Planner 把任务 state machines 串联成定制 workflow。
- Execution：Task executor 调用 Primer3、CRISPRitz、CRISPResso2 等工具，并指导 wet-lab 操作。
- Verification：Gene-editing bench、专家评分、NGS、qPCR、FACS、蛋白表达验证。

Evidence Role 应标为 **Direct + Infrastructure**。它直接研究如何把实验技能组织为 agentic workflow，并提供真实 wet-lab 验证。与 Co-Scientist/Robin 相比，CRISPR-GPT 不主要追求新科学假设，而是把已知 CRISPR 实验能力封装成可执行、可组合、可监督的 protocol system。

## 局限性

- CRISPR-GPT 是 co-pilot，不是完全自动实验室；真实实验仍由人类研究者执行，系统主要指导设计、协议和分析。
- User oversight 仍然必要；论文明确鼓励用户监控任务进展并纠正错误或误解。
- 系统依赖高质量专家说明、专家讨论数据和人工整理的任务描述，这些数据难以收集，限制扩展。
- 当前 gRNA design 主要支持 human 和 mouse targets，跨物种能力仍需扩展。
- Planner 为了鲁棒性不能在执行过程中动态添加或删除 state machines；作者承认动态任务管理是未来更智能 science AI agent 的重要方向。
- delivery selection 使用 citation count 辅助排序，但引用数不是判断递送方式最合适的决定性指标。
- exon suggestion 对文献稀疏或在线信息少的基因可能表现有限。
- Gene-editing bench 和专家评估虽然覆盖多个任务，但仍主要评估设计质量，不等价于大规模真实实验成功率。
- 两个湿实验演示很有价值，但样本数量有限，且集中在癌症细胞系，不足以证明对所有 CRISPR modalities 和生物系统泛化。

## 核心贡献

CRISPR-GPT 的核心贡献是把 CRISPR 实验设计、工具调用、协议生成和数据分析组织成多智能体状态机 workflow，并通过 A549 knockout 和 A375 CRISPR activation 两个真实湿实验展示非专家研究者可在 AI 指导下完成有效 gene-editing。

## 论证级补充

### 方法流程细化

1. **输入**：用户提出 gene-editing 目标，可选择 Meta、Auto 或 Q&A mode。
2. **规划**：LLM Planner 将目标拆成任务链，例如系统选择、gRNA 设计、递送方式、off-target 检查、验证 assay。
3. **表示**：22 个实验任务被封装为 state machines，限制自由工具调用带来的不稳定性。
4. **执行**：Task executor 调用 Primer3、CRISPRitz、CRISPResso2、CRISPick 表格、文献检索和 RAG。
5. **湿实验**：非专家用户按照系统指导完成 A549 knockout 和 A375 CRISPR activation。
6. **验证**：通过 NGS、CRISPResso2、qPCR、FACS 和蛋白表达检测验证编辑效果。

### 关键数字核对

| 指标 | 数值 | 可用于正文的说法 |
|---|---:|---|
| gene-editing tasks | 22 | 实验能力被显式拆成 protocol/workflow units |
| modalities | 4 | 覆盖 knockout、base editing、prime editing、CRISPRa/i |
| interaction modes | 3 | Meta、Auto、Q&A 支持不同用户水平 |
| Gene-editing bench | 288 test cases | 评估设计和问答能力 |
| planning metrics | accuracy/precision/recall/F1 > 0.99 | 规划任务上表现强，但不等于大规模实验成功率 |
| CRISPR discussion data | 4000 threads / 3000+ QA pairs | domain-specific knowledge acquisition |
| A549 knockout targets | 4 genes | 初级研究者在系统指导下完成真实 wet-lab demo |
| knockout editing efficiency | 约 80% | 真实验证支持 protocol skill 可执行 |
| A375 activation | NCR3LG1 56.5%; CEACAM1 90.2% | CRISPRa wet-lab demo |

### 可支撑的论点

- 实验 protocol 可以被表示为 state-machine workflow skill。
- Scientific skill 的可靠性来自受限工具接口、任务依赖、专家知识和人类监督，而不是自由 LLM action。
- Protocol skill 可以指导非专家完成真实湿实验，但仍需要 human-in-the-loop。

### 不能支撑的过度结论

- 不能说 CRISPR-GPT 是机器人实验室；实验由人类执行。
- 不能说其覆盖所有 CRISPR modalities 和所有生物系统。
- 不能把两个 wet-lab demos 等同于大规模实验成功率。
- 不能说 Planner 已能动态发明新 state machines；论文承认这是未来工作。

### 与其他 anchor papers 的关系

- **互补 Co-Scientist / Robin**：它不主打新假设，而是把既有 CRISPR 实验技能封装为可执行 protocol。
- **互补 A-Lab / RoboChem-Flex**：CRISPR-GPT 有 wet-lab protocol guidance，A-Lab/RoboChem-Flex 有机器人或自动实验闭环。
- **互补 MOSAIC**：二者都把实验知识组织成 protocol-like skill，MOSAIC 偏化学合成，CRISPR-GPT 偏 gene editing。
- **受 SafeScientist 约束**：gene-editing protocol skill 必须有安全和伦理边界。

### 框架映射

| 维度 | 标签 |
|---|---|
| Scientific Workflow | Experiment Design; Execution; Result Analysis; Verification |
| Skill Lifecycle | Representation / protocol skill; Composition / state-machine workflow; Execution / tool use and wet-lab guidance; Verification / assay |
| Evidence Role | Direct; Infrastructure |
| Cross-cutting Constraints | Physical Grounding; Human Oversight; Auditability |
