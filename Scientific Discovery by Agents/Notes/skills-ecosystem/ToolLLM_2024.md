# ToolLLM 2024

## 基本信息
- **论文**: ToolLLM: Facilitating Large Language Models to Master 16000+ Real-World APIs
- **作者**: Yujia Qin, Shihao Liang, Yining Ye, Kunlun Zhu, Lan Yan, Yaxi Lu, Yankai Lin, Xin Cong, Xiangru Tang, Bill Qian, Sihan Zhao, Lauren Hong, Runchu Tian, Ruobing Xie, Jie Zhou, Mark Gerstein, Dahai Li, Zhiyuan Liu, Maosong Sun
- **年份**: 2024
- **来源**: ICLR 2024; arXiv:2307.16789
- **关键词**: tool-use, api-retrieval, tool-learning, instruction-tuning, multi-tool-agent

## 核心思想
ToolLLM 关注开放源 LLM 的大规模工具使用能力：模型不仅要会调用单个 API，还要能在成千上万个真实 RESTful APIs 中检索合适工具，理解 API 文档，规划多步调用，并根据真实 API 返回结果完成用户任务。

作者认为已有 tool-learning 数据集存在三类不足：API 数量和多样性有限，常常只覆盖单工具场景；很多工作不执行真实 API 调用，缺少真实 response；用户需要手动指定 API 集合，无法适配真实的大规模 API 生态。

## 方法细节
ToolLLM 是一个包含数据构造、模型训练和评测的框架，核心产物包括 ToolBench、ToolLLaMA、API Retriever 和 ToolEval。

1. **ToolBench 数据构造**  
   作者从 RapidAPI Hub 收集真实 RESTful APIs，经过过滤后保留 **3,451 个高质量工具**和 **16,464 个 APIs**，覆盖 **49 个类别**。每个 API 记录名称、描述、参数、代码片段和示例返回。

2. **Instruction Generation**  
   使用 ChatGPT 根据 API 文档生成指令，覆盖三类场景：I1 单工具指令、I2 同类别多工具指令、I3 同 collection 多工具指令。最终得到近 **200k** 个合格的 instruction-relevant API pairs，其中 I1 **87,413**、I2 **84,815**、I3 **25,251**。

3. **Solution Path Annotation**  
   对每条指令，ChatGPT 在真实 API 调用和返回结果基础上搜索一条可行 solution path。为提升复杂任务标注效率，作者提出 **DFSDT**（depth-first search-based decision tree），允许模型探索多个 reasoning traces、回退失败步骤、继续扩展更有希望的路径。

4. **ToolLLaMA**  
   基于 ToolBench 微调 LLaMA-2 7B，并通过 positional interpolation 将上下文长度扩展到 **8192**，以容纳较长 API 文档和返回结果。

5. **API Retriever**  
   训练一个基于 BERT-base / Sentence-BERT 的 dense retriever，将用户指令和 API 文档编码后计算相似度，用于从 16k+ API 中推荐 relevant APIs。

6. **ToolEval**  
   使用 ChatGPT 自动评估 tool-use 过程，指标包括 pass rate（是否在预算内完成指令）和 win rate（两条 solution path 哪条更好）。ToolEval 与人类标注在 pass rate 上 agreement 为 **87.1%**，win rate 上为 **80.3%**。

## 关键结果

1. **ToolBench 显著扩展了 tool-learning 数据规模**  
   与 APIBench、API-Bank、ToolAlpaca 等相比，ToolBench 同时包含真实 API、真实调用返回、多工具场景、API retrieval 和多步推理。论文报告 ToolBench 包含 **16,464 APIs**、**126,486 instances**、**469,585 real API calls**，平均 reasoning traces 为 **4.0**。

2. **API Retriever 明显优于 BM25 和 OpenAI ada embedding**  
   Table 2 中，作者的 retriever 平均 NDCG@1 / NDCG@5 为 **78.0 / 84.9**，高于 BM25 的 **18.5 / 17.0** 和 Ada 的 **49.6 / 45.4**。单工具 I1 检索更容易，多工具 I2/I3 更难。

3. **DFSDT 比 ReACT 更适合复杂多工具规划**  
   Table 3 中，ChatGPT + DFSDT 的平均 pass rate 为 **63.8**，高于 ReACT 的 **35.3** 和成本对齐后的 ReACT@N 的 **44.5**。提升在 I2、I3 复杂指令上更明显，说明多路径搜索和回退对多工具任务很关键。

4. **ToolLLaMA 接近 ChatGPT，并显著优于较弱模型**  
   主实验用 ToolEval 比较 ChatGPT、GPT-4、Claude-2、Text-Davinci-003、Vicuna、Alpaca、ToolLLaMA 等。作者报告 ToolLLaMA + DFSDT 在 unseen instructions 和 unseen tools 上表现接近 teacher model ChatGPT，明显优于 Text-Davinci-003 和 Claude-2，并仅略低于 GPT-4。加入 API Retriever 后，ToolLLaMA-DFSDT-Retriever 在报告设置中还能超过使用 ground-truth API set 的普通 ToolLLaMA-DFSDT。

5. **使用检索器比 oracle API set 还可能更好**  
   真实使用中，用户无法手动指定 API。作者将 API Retriever 推荐的 top-5 APIs 输入 ToolLLaMA，发现 ToolLLaMA-DFSDT-Retriever 的表现反而超过 ground-truth API set，原因是 retriever 可能找到功能更合适的替代 API，扩大了工具搜索空间。

6. **在 APIBench 上具备 OOD 泛化**  
   ToolLLaMA 未在 APIBench 的 TorchHub、TensorHub、HuggingFace API 或指令上训练，但仍能迁移。Table 5 显示，ToolLLaMA + Our Retriever 在 HuggingFace / TorchHub / TensorHub 上的 AST accuracy 为 **16.77 / 51.16 / 40.59**；使用 Oracle retriever 时为 **88.80 / 85.88 / 88.62**。

## 与综述的关联

ToolLLM 是 Skill Lifecycle 中 **Representation / Retrieval / Composition / Execution** 的直接证据。它把工具能力从单个 API 调用推进到大规模 API 生态：API 文档是 tool skill 的表示，retriever 是 skill retrieval，DFSDT 是 tool-chain composition，真实 API call 是 skill execution。

在 Scientific Workflow 中，它主要支撑 Execution，但对科学发现尤其重要：科学 Agent 往往需要在数据库、仿真器、代码库、仪器接口、统计工具、文献工具之间选择和组合。ToolLLM 提供了非科学领域的大规模 API 学习底座，可迁移为 scientific tool-use skill 的基础设施。

Evidence Role 应标为 **Direct + Infrastructure**。它直接支持“工具技能可检索、可组合、可执行、可评测”的观点，但不直接证明科学发现本身；它更像科学 Agent 调用外部工具生态之前必须具备的通用能力层。

与 Toolformer 相比，Toolformer 证明模型能自监督学习 API call，ToolLLM 则强调真实 API 生态、大规模 retrieval、多工具规划和评测。两者共同构成 tool-use skill 的底层谱系。

## 局限性

- 数据构造大量依赖 ChatGPT，ToolBench 的指令和 solution path 可能继承 teacher model 的偏差。
- ToolEval 也是 ChatGPT-based evaluator，虽然与人类有较高 agreement，但仍可能偏向 ChatGPT 风格的 solution path。
- RapidAPI 中 API 的可靠性、时效性、费用和访问限制会影响复现与长期使用。
- 多工具任务仍以文本 API 为主，不能直接覆盖实验室机器人、湿实验室仪器或安全关键物理系统。
- 论文中的 OOD 泛化依赖 API 文档出现在 prompt 中；如果 API 文档不完整、过长或返回格式复杂，性能可能下降。
- API Retriever 找到替代 API 有时能提升性能，但在安全关键科研任务中，替代工具是否等价需要额外验证。

## 核心贡献

ToolLLM 的核心贡献是把 tool-use skill 从单工具演示扩展到 16k+ 真实 API 的检索、组合、执行和自动评测框架，为科学发现 Agent 未来接入大规模 scientific tools 提供了可迁移的系统蓝图。
