# SciToolAgent 2025

## 基本信息
- **论文**: SciToolAgent: A Knowledge Graph-Driven Scientific Agent for Multi-Tool Integration
- **作者**: Keyan Ding, Jing Yu, Junjie Huang, Yuchen Yang, Qiang Zhang, Huajun Chen
- **年份**: 2025
- **来源**: Nature Computational Science, doi:10.1038/s43588-025-00849-y; arXiv:2507.20280
- **关键词**: scientific-tools, knowledge-graph, multi-tool-agent, tool-retrieval, workflow-automation, safety-checking

## 核心思想
科学研究越来越依赖专业计算工具，但工具数量多、输入输出复杂、依赖关系强，非专家很难正确选择和组合。现有 LLM tool agents 常依赖 ReAct 式 in-context learning，工具集通常少于 20 个，并且很少显式建模工具之间的顺序依赖、输入输出兼容性和安全风险。

SciToolAgent 要解决的问题是：如何让 LLM agent 在 biology、chemistry、materials science 等领域中，从数百个科学工具中检索、规划、执行和总结多步工具链，同时进行安全检查。

## 方法细节
SciToolAgent 由三类 LLM-powered 组件和一个科学工具知识图谱组成：

- **SciToolKG**：手工构建的 scientific tool knowledge graph，记录工具名称、功能、输入/输出格式、应用场景、安全等级、依赖关系、兼容性等信息。
- **Planner**：基于 SciToolKG 做 graph-based RAG，先检索全图中相关工具，再探索候选工具的子图邻域，生成 chain-of-tools。
- **Executor**：按工具链顺序执行工具，格式化输入、调用 API 或本地工具，并在错误发生时重试。
- **Safety check module**：根据 safeguard database 检测潜在有害响应或高风险工具调用。
- **Summarizer**：汇总多个工具输出，判断问题是否解决；若失败，则提示 Planner 重新生成或调整 chain-of-tools。最终结果进入 memory module 作为后续查询上下文。

工具集覆盖 **500+ tools**，包括 web APIs、machine learning models、Python functions、knowledge databases 和自定义工具，涉及 biology、chemistry、materials science 等领域。

## 关键结果

1. **SciToolEval benchmark**  
   作者构建 SciToolEval，共 **531** 个科学工具使用问题，覆盖 molecular property prediction、protein analysis、material retrieval 等任务。数据分为两级：Level-1 **152** 个单工具问题，Level-2 **379** 个多工具问题。

2. **总体性能达到约 94%**  
   摘要报告 SciToolAgent 在 SciToolEval 上 overall accuracy 为 **94%**，比 state-of-the-art baselines 高 **10%**。评测指标包括 pass rate、tool planning accuracy 和 final answer accuracy。

3. **多工具任务优势更明显**  
   在 GPT-4o-based agents 比较中，SciToolAgent 在 Level-1、Level-2 和 overall 三种设置下均优于 ReAct、Reflexion、ChemCrow 和 CACTUS。论文特别指出，在 Level-2 多工具任务上，SciToolAgent 的 final answer accuracy 相比 ReAct 约高 **20%**，相比 Reflexion 约高 **10%**。

4. **SciToolKG 提升 tool planning**  
   ReAct 和 Reflexion 在候选工具很多、多步依赖复杂时容易出现 tool planning 和 execution 错误；SciToolAgent 通过 chain-of-tools 和 KG 邻域检索，能从全局角度规划工具顺序，减少 trial-and-error。

5. **基础模型影响明显**  
   在 SciToolAgent 框架内，OpenAI o1 表现最好，GPT-4o 取得较好的 accuracy/cost trade-off，因此作为默认模型。Qwen2.5-72B 有一定下降；Qwen2.5-7B 在 tool planning 上较弱，但用 SciToolKG 生成数据 fine-tune 后提升约 **10%**，接近更大模型。

6. **四个真实案例**  
   论文展示四类 case studies：protein design and analysis、chemical reactivity prediction、chemical synthesis and analysis、MOF materials screening。  
   在 protein design 中，SciToolAgent 组合 Chroma、ProteinForceGPT、ESMFold、ANM/ProDy、DSSP/BioPython 等工具生成序列、预测结构并分析力学/振动/二级结构。  
   在 chemical reactivity prediction 中，系统比较 RDK fingerprints、Morgan fingerprints、electrical descriptors，并进一步比较 MLP、AdaBoost、Random Forest；结果显示 electrical descriptors 表现更好，Random Forest 在后续比较中预测准确率最高。  
   在 MOF screening 中，系统筛选热稳定性、CO2 吸附能力和价格，并识别出 TBAPy Ti Andres.cif 作为满足条件的候选。

## 与综述的关联

SciToolAgent 是 **scientific tool composition skill** 的强直接证据。它把 skill 从单个工具调用推进到结构化工具生态：工具信息是 skill representation，SciToolKG 是 skill retrieval / composition infrastructure，Planner-Executor-Summarizer 构成工具链执行闭环。

在 Scientific Workflow 中，它覆盖 Knowledge Grounding、Execution、Result Analysis，并通过 safety module 连接 Verification。  

在 Skill Lifecycle 中，它对应：

- Representation：工具节点、输入输出 schema、安全等级、依赖关系。
- Retrieval：full-graph retrieval 与 sub-graph exploration。
- Composition：chain-of-tools，按输入输出和依赖关系组织工具。
- Execution：Executor 顺序调用工具并重试。
- Evolution：Summarizer 失败后触发 Planner 重新规划；memory module 保存上下文。
- Verification：pass rate、tool planning accuracy、final answer accuracy、安全检查。

Evidence Role 应标为 **Direct + Infrastructure**。它直接支撑 skill-driven 视角中“科学工具链可以被图结构表示、检索、组合和执行”，同时也是未来 scientific agent 的底层基础设施。

## 局限性

- SciToolKG 主要依赖人工构建和维护，工具信息更新、扩展和细粒度关系建模存在可扩展性挑战。
- 系统仍依赖强闭源模型；GPT-4o/o1 表现较好，但成本和可访问性限制实际部署。
- Qwen2.5-7B-FT 虽有提升，但在复杂工具规划和多步推理上仍落后 GPT-4o。
- 论文案例展示了自动化复杂计算 workflow，但不等同于湿实验闭环验证。
- safety module 是重要设计，但论文没有证明其能覆盖所有现实 scientific misuse 或 high-risk lab action。

## 核心贡献

SciToolAgent 的核心贡献是提出 SciToolKG 驱动的大规模科学工具集成框架，使 LLM agent 能够在 500+ 科学工具中进行结构化检索、chain-of-tools 规划、顺序执行和安全检查，为 skill-driven scientific discovery 提供了最直接的 tool-chain infrastructure 证据之一。
