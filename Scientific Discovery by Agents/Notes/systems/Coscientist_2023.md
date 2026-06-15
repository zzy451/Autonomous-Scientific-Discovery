# Coscientist 2023

## 基本信息
- **论文**: Autonomous chemical research with large language models
- **作者**: Daniil A. Boiko, Robert MacKnight, Ben Kline, Gabe Gomes
- **年份**: 2023
- **来源**: Nature, doi:10.1038/s41586-023-06792-0
- **关键词**: autonomous-science, chemistry, lab-automation, tool-use, robotic-experimentation, llm-agent

## 核心思想
这篇论文要解决的问题是：LLM 是否能不只回答化学问题，而是实际设计、规划并执行真实化学实验。传统自动化化学平台已经可以执行实验，但通常需要人类专家把科学目标翻译成仪器 API、实验步骤和优化策略；而通用 LLM 虽有化学与代码能力，却缺少直接控制实验设备、查阅硬件文档和根据实验反馈优化的能力。

作者提出 Coscientist，目标是把 GPT-4 与 web search、documentation retrieval、code execution 和实验自动化接口连接起来，使系统能够完成从实验规划到物理执行的化学研究任务。

## 方法细节
Coscientist 是一个由多个模块组成的 LLM agent 系统，核心是 GPT-4 驱动的 Planner。Planner 根据用户的自然语言目标调用四类命令：

- `GOOGLE`：调用 Web Searcher 搜索互联网、浏览网页并把信息返回给 Planner。
- `PYTHON`：在隔离 Docker 容器中执行代码，用于计算实验参数、处理数据和修正代码错误。
- `DOCUMENTATION`：检索并总结硬件或云实验室 API 文档，例如 Opentrons Python API 和 Emerald Cloud Lab 的 Symbolic Lab Language。
- `EXPERIMENT`：通过自动化 API 执行实验代码，或生成可用于人工执行的实验方案。

系统的关键设计是：Planner 不直接记忆所有仪器 API，而是通过文档检索获得当前硬件接口的用法，再生成代码或实验命令。这一点使它能处理训练数据 cutoff 之后发布的硬件模块，例如 Opentrons heater-shaker module。

论文展示了六类能力：

1. 通过公开数据规划已知化合物合成。
2. 搜索和理解大量硬件文档。
3. 使用文档在云实验室执行高层命令。
4. 用低层指令精确控制 liquid handler。
5. 组合多个硬件模块和数据源执行复杂实验。
6. 基于已有实验数据进行反应条件优化。

## 关键结果

1. **化合物合成规划**  
   作者构造了 7 个化合物合成任务，包括 acetaminophen、aspirin、benzoic acid、ethyl acetate、ibuprofen、nitroaniline、phenolphthalein。评分范围为 1-5，低于 3 视为失败。带 web search 的 GPT-4 版本整体表现最好；非 browsing 模型在 ibuprofen 合成等任务中容易给出错误路线。该实验说明 web search 对化学方案规划很关键。

2. **硬件文档检索与 API 使用**  
   Coscientist 使用文档检索生成 Opentrons heater-shaker module 的有效 Python API 代码，也能生成 Emerald Cloud Lab 中执行 HPLC 的 Symbolic Lab Language 函数调用。作者强调，文档检索对正确调用硬件 API 是关键。

3. **液体处理器与 UV-Vis 组合实验**  
   系统先让 liquid handler 准备小样本，再让 UV-Vis plate reader 读取 96-well plate 中的光谱。读取数据后，Coscientist 生成 Python 代码分析 NumPy array，识别不同颜色样本的位置。这展示了仪器控制、数据读取和代码分析的组合能力。

4. **Suzuki 与 Sonogashira 交叉偶联实验**  
   论文让 Coscientist 在给定可用化学品、两块 microplates、liquid handler 和 heater-shaker 的条件下，设计并执行 Suzuki-Miyaura 和 Sonogashira coupling reactions。系统搜索互联网确定反应条件、计算试剂体积、生成 OT-2 protocol，并在使用错误 heater-shaker API 方法名后调用文档检索修正代码。  
   后续 GC-MS 分析显示两类目标产物形成：Suzuki reaction 在 chromatogram **9.53 min** 处出现目标信号，Sonogashira reaction 在 **12.92 min** 处出现匹配信号。

5. **实验设置仍不是完全自动化**  
   作者明确说明，在 cross-coupling 实验中，plates 仍由人类手动移动，但“no human decision-making was involved”。也就是说，它自动化了决策、规划、代码和仪器指令，但没有完全自动化所有物理动作。

6. **反应条件优化**  
   作者在两个已有完整映射的 reaction condition datasets 上评估 Coscientist：Perera 等人的 Suzuki reaction dataset，以及 Doyle 的 Buchwald-Hartwig reaction dataset。每个任务最多允许 **20 iterations**，分别只覆盖总搜索空间的 **5.2%** 和 **6.9%**。作者用 normalized advantage / normalized maximum advantage 衡量性能，观察到 GPT-4-based approaches 的 normalized advantage 随迭代上升，并且与 Bayesian optimization 相比表现有竞争力。

7. **安全与开放限制**  
   由于安全担忧，论文没有完整公开所有数据、代码、prompt 和模型输出；只公开了简化实现和用于定量分析的生成输出。作者也专门讨论了智能 agent 和自动实验系统的 dual-use 风险。

## 与综述的关联

Coscientist 是 autonomous scientific discovery 里非常关键的 Infrastructure 论文。它不是“发现新理论”的系统，而是展示了 LLM agent 如何连接真实实验设备、硬件文档、代码执行和化学实验，从而把 scientific workflow 从文本推理推进到 physical action。

在 Scientific Workflow 上，它覆盖 Experiment Design、Execution、Result Analysis 和 Evolution。其中 Execution 是最突出部分：系统能调用 cloud lab、liquid handler、heater-shaker、UV-Vis、HPLC/GC-MS 相关流程。

在 Skill Lifecycle 上，它对应：

- Representation：实验命令、API 文档调用、Python protocol、SLL 函数调用可视为 code skill / protocol skill。
- Acquisition：通过 web search、documentation retrieval 和实验反馈获得任务知识。
- Retrieval：使用 Google search、文档 embedding/vector search、硬件 API 文档检索。
- Composition：Planner 把 GOOGLE、PYTHON、DOCUMENTATION、EXPERIMENT 组合成实验 workflow。
- Execution：调用 Docker 代码环境和真实实验自动化设备。
- Verification：通过 UV-Vis、HPLC、GC-MS 和反应产物信号验证。

Evidence Role 应标为 **Infrastructure + Boundary**。它为 skill-driven science 提供物理执行层证据，但也划出边界：实验动作不完全自动化，安全限制强，真实科研发现仍需要更复杂的闭环设计。

与 Co-Scientist 和 Robin 相比，Coscientist 更偏实验执行 infrastructure：它不强调生物医学假设演化，而是证明 LLM 可以把自然语言目标转成可运行实验。与 self-driving lab 文献相比，它的创新点在于用 LLM 作为 planner 和 API/documentation bridge，而不是传统 Bayesian optimization 控制器。

## 局限性

- 实验平台不是完全闭环自动化；cross-coupling 实验中 plates 需要人工移动。
- Coscientist 的化学合成规划、文档检索和实验执行依赖 GPT-4 与 prompt engineering，模型错误仍可能导致错误实验方案或 API 调用。
- 化学合成规划评分带有主观性，作者也承认 1-5 分标签难以完全形式化。
- 文档检索和 web search 的可靠性受网页质量、文档覆盖和检索结果影响。
- 反应优化实验主要基于已有完整映射的数据集，不等同于在未知真实化学空间中完成新发现。
- 出于安全原因，完整数据、代码、prompt 和输出未全部公开，外部复现受到限制。
- 论文讨论 dual-use 风险，说明能控制实验设备的 agent 必须有更严格的权限、安全审计和任务过滤机制。

## 核心贡献

Coscientist 的核心贡献是展示 GPT-4 驱动的 LLM agent 可以通过 web search、文档检索、代码执行和实验自动化 API，规划并执行真实化学实验，包括交叉偶联反应和反应条件优化，从而把 LLM agent 从“科研文本助手”推进到“物理实验执行接口”。
