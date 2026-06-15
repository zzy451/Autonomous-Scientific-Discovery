# Toolformer 2023

## 基本信息
- **论文**: Toolformer: Language Models Can Teach Themselves to Use Tools
- **作者**: Timo Schick, Jane Dwivedi-Yu, Roberto Dessi, Roberta Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola Cancedda, Thomas Scialom
- **年份**: 2023
- **来源**: NeurIPS 2023; arXiv:2302.04761
- **关键词**: tool-use, self-supervised-learning, api-calling, skill-acquisition, language-models

## 核心思想
大语言模型在少样本和零样本任务上表现强，但在算术、事实查询、时间感知、低资源语言等基础能力上仍容易失败；这些能力反而可以由简单外部工具完成。Toolformer 要解决的问题是：如何让语言模型在没有大规模人工标注的情况下，自己学会何时调用工具、调用哪个工具、传什么参数，以及如何利用工具返回结果继续生成文本。

这篇论文不是科学发现系统论文，但它是 tool-use skill acquisition 的基础文献：把工具调用从人工写规则或任务专用链条，变成可通过自监督数据构造学习出来的通用能力。

## 方法细节
Toolformer 基于 GPT-J 6.7B，在普通语言建模文本中自动插入 API 调用样例，并用这些样例微调模型。核心流程是三步：

1. **Sample API Calls**：对每个工具手写少量 in-context demonstrations，让原始模型在文本不同位置采样潜在 API call。
2. **Execute API Calls**：真实执行这些 API，得到文本形式的返回结果。
3. **Filter API Calls**：如果“插入 API 调用及其结果”能降低模型预测后续 token 的 loss，并且降低幅度超过阈值，就保留该调用；否则丢弃。

保留后的 API call 被线性化插入原始语料，形成带工具调用的训练集，再对 GPT-J 进行微调。论文使用的工具包括：

- Question Answering system
- Calculator
- Wikipedia Search
- Machine Translation system
- Calendar

推理时，Toolformer 不依赖任务专用示例。模型在生成过程中自主决定是否插入 API call；作者为了鼓励调用工具，把 `<API>` token 进入 top-k 候选时也允许触发工具调用，并限制每个输入最多调用一次 API。

## 关键结果

1. **LAMA 事实补全显著提升**  
   在 LAMA 子集上，Toolformer 得分为 SQuAD **33.8**、Google-RE **11.5**、T-REx **53.5**，高于 GPT-J、GPT-J+CC、Toolformer disabled、OPT 66B 和 GPT-3 175B。作者说明它在 T-REx 设置下 **98.1%** 的样例会调用 QA 工具。

2. **数学任务主要受益于 Calculator**  
   在 ASDiv、SVAMP、MAWPS 上，Toolformer 分别达到 **40.4 / 29.4 / 44.0**，明显高于 GPT-J (**7.5 / 5.2 / 9.9**) 和 GPT-3 175B (**14.0 / 10.0 / 19.8**)。模型在 **97.9%** 的数学样例中调用 calculator。

3. **开放问答提升但仍落后 GPT-3**  
   在 WebQS、Natural Questions、TriviaQA 上，Toolformer 为 **26.3 / 17.7 / 48.8**，高于同规模 GPT-J 系列，但低于 GPT-3 175B 的 **29.0 / 22.6 / 65.9**。作者认为原因包括 Wikipedia search API 简单、不能交互式改写 query 或浏览多个结果。

4. **多语言问答收益不稳定**  
   MLQA 上，机器翻译工具在大多数语言中被频繁调用，例如除 Hindi 外使用率为 **63.8% 到 94.9%**；但由于 CCNet 微调对某些语言造成分布漂移，Toolformer 并不稳定优于原始 GPT-J。

5. **时间任务中 Calendar 对 DATESET 有效，但对 TEMPLAMA 不一定有效**  
   Toolformer 在 TEMPLAMA / DATESET 上达到 **16.3 / 27.3**，高于 GPT-J、OPT 和 GPT-3。DATESET 的提升可归因于 calendar tool，调用率为 **54.8%**；而 TEMPLAMA 的提升主要来自 Wikipedia search 和 QA tool，calendar 只在 **0.2%** 样例中被调用。

6. **工具微调没有明显损害语言建模能力**  
   在 WikiText 和 CCNet 验证集上，Toolformer disabled 的 perplexity 与 GPT-J+CC 接近（WikiText **10.3**、CCNet **10.5**），说明插入 API call 的微调没有明显破坏无工具语言建模。

7. **工具使用能力具有模型规模门槛**  
   作者把方法扩展到 GPT-2 系列 124M、355M、775M、1.6B，并发现能有效利用工具的能力大约在 **775M 参数**附近出现；更小模型即使给工具也难以稳定受益。

## 与综述的关联

Toolformer 是 Skill Lifecycle 中 **Acquisition / Execution** 的基础证据。它说明“工具使用”可以被表示为文本中的 API call，并通过自监督方式从少量示例扩展到大规模训练数据。这为 scientific agents 中的数据库查询、计算、检索、仿真、代码执行、实验设备调用等 tool skill 提供了通用机制来源。

在 Scientific Workflow 中，它主要对应 Execution，但在科学发现场景中可间接支撑 Knowledge Grounding（检索/QA）、Result Analysis（计算）、Experiment Design（调用专业工具或模拟器）等阶段。

Evidence Role 应标为 **Direct + Infrastructure**：它直接证明 tool-use skill 可以学习，同时又是科学发现 agent 的底层能力，而不是科学发现领域内的完整系统。

与 Voyager、SkillOS、Perplexity/Anthropic Skills Spec 相比，Toolformer 更早、更底层：它没有显式 skill library、版本管理或 human-readable skill file，而是把工具调用能力内化到模型参数中。对我们的综述来说，它帮助区分两类 skill：一种是外部可管理的 procedure/artifact skill，另一种是通过训练获得的 implicit tool-use skill。

## 局限性

- 当前方法不能进行链式工具调用，即不能把一个工具的输出作为另一个工具的输入。
- 工具调用不是交互式的，特别是 search engine 不能浏览多个结果或改写 query。
- 模型对 prompt wording 敏感，是否调用 API 可能受输入表述影响。
- 样本效率较低，例如处理大量文档后只有少量 calculator API calls 被保留为有用样例。
- 只考虑调用工具对预测 loss 的帮助，没有建模不同工具的计算成本。
- 每个输入最多调用一次 API，这限制了复杂科学任务中多步工具链的表达能力。

## 核心贡献

Toolformer 的核心贡献是提出了一种自监督 API-call 数据构造和过滤机制，使语言模型能够学习“何时、如何、为何调用工具”，为后续 agent skill acquisition 和 scientific tool-use 提供了重要底层范式。
