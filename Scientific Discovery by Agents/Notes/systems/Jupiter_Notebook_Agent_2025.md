# Jupiter Notebook Agent 2025

## 基本信息
- **论文**: Jupiter: Enhancing LLM Data Analysis Capabilities via Notebook and Inference-Time Value-Guided Search
- **作者**: Shuocheng Li, Yihao Liu, Silin Du, Wenxuan Zeng, Zhe Xu, Mengyu Zhou, Yeye He, Haoyu Dong, Shi Han, Dongmei Zhang
- **年份**: 2026（arXiv 预印本为 2025）
- **来源**: AAAI 2026, Proceedings of AAAI 40(37):31726-31733, doi:10.1609/aaai.v40i37.40440; arXiv:2509.09245v2
- **关键词**: system, notebook-agent, data-analysis, search, verification

## 核心思想
LLM 数据分析 agent 容易在 notebook 中走错分析路径。单次生成代码不能充分利用执行反馈，也难以在多个候选分析轨迹中选择更好的路径。

Jupiter 要解决的问题是：如何在 inference time 对 notebook analysis trajectories 进行搜索和价值评估，从而提升数据分析能力。

## 方法细节
Jupiter 结合 notebook environment 与 value-guided search。

核心机制包括：

1. 生成候选 notebook actions / cells；
2. 执行并观察输出；
3. 使用 value model 或 value-guided scoring 评估轨迹质量；
4. 通过 MCTS / search over trajectories 选择更优分析路径；
5. 最终输出更可靠的数据分析结果。

论文还构建 NbQA：从真实 Jupyter notebooks 和关联数据文件中抽取标准化 task-solution pairs，用于反映真实 data science 场景中的 tool-use pattern。该工作作为 AAAI 2026 论文发表，arXiv 版本时间为 2025 年。

## 关键结果

1. Jupiter 将 data analysis 形式化为 search problem，并用 MCTS 生成多样化解题轨迹用于 value model learning。
2. 推理时，Jupiter 结合 value model 和 node visit counts，以较少 search steps 收集可执行 multi-step plans。
3. 在 NbQA 训练/评测体系下，Qwen2.5-7B-Instruct 和 Qwen2.5-14B-Instruct 在 InfiAgent-DABench 上分别解决 **77.82%** 和 **86.38%** 的任务，达到或超过 GPT-4o 与 advanced agent frameworks。

## 与综述的关联

在 Scientific Workflow 中，它覆盖 Execution、Result Analysis 和 Verification。

在 Skill Lifecycle 中，它对应 Composition / search、Execution / code run 和 Verification / trajectory value estimation。

Evidence Role 应标为 **Direct**。Jupiter 说明科研数据分析 skill 不只是代码生成，也可以在运行时搜索多条分析轨迹并用价值函数选择。

## 局限性

Jupiter 偏 notebook data analysis，不覆盖湿实验或真实科学验证。value-guided search 带来额外计算成本，value model 的可靠性也会影响最终结果。

## 核心贡献

Jupiter 的核心贡献是把 notebook-based data analysis 变成 inference-time searchable workflow，用 value-guided search 改善 LLM agent 的分析路径选择。
