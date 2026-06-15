# TianJi 2026

## 基本信息
- **论文**: TianJi: An Autonomous AI Meteorologist for Discovering Physical Mechanisms in Atmospheric Science
- **作者**: Kaikai Zhang, Xiang Wang, Haoluo Zhao, Nan Chen, Mengyang Yu Jing-Jia Luo, Tao Song, Fan Meng
- **年份**: 2026
- **来源**: arXiv:2603.27738
- **关键词**: system, atmospheric-science, climate, scientific-discovery, simulation

## 核心思想
大气科学不只需要预测天气，还需要发现 physical mechanisms。传统 AI weather models 主要优化预测精度，而机制发现需要结合文献、数值实验、物理解释和验证。

TianJi 要解决的问题是：能否构建 autonomous AI meteorologist，自动提出机制假设、设计数值实验并验证大气科学中的物理机制。

## 方法细节
TianJi 被定位为 autonomous AI meteorologist。

核心流程包括：

1. 阅读或检索相关 atmospheric science 文献；
2. 生成 physical mechanism hypothesis；
3. 设计并运行 numerical model experiments；
4. 分析模拟结果；
5. 根据物理一致性和实验结果更新机制解释。

## 关键结果

1. TianJi 使用 LLM-driven multi-agent architecture，将科学研究拆成 cognitive planning 和 engineering execution。
2. Meta-planner 负责解释 hypothesis 并规划实验路线；specialized worker agents 负责数据准备、模型配置和多维结果分析。
3. 论文在两个经典大气动力学场景中验证：squall-line cold pools 和 typhoon track deflections。
4. TianJi 在零人工干预下完成 expert-level end-to-end numerical experiment operations，将研究周期压缩到数小时，并能根据输出自主判断和解释假设有效性。

## 与综述的关联

在 Scientific Workflow 中，它覆盖 Knowledge Grounding、Hypothesis Generation、Experiment Design、Simulation、Result Analysis 和 Verification。

在 Skill Lifecycle 中，它对应 Literature-derived acquisition、Simulation execution、Composition / multi-step workflow 和 Verification / physical consistency。

Evidence Role 应标为 **Direct**。它补足我们文献池中非生物医学、非材料的 earth science 方向，说明 agentic scientific discovery 可以扩展到 numerical-model-based science。

## 局限性

TianJi 是 arXiv 候选，需核查实际机制发现是否经过独立专家或后续观测验证。它主要依赖数值实验，不等同于实地观测或实验室验证。

## 核心贡献

TianJi 的核心贡献是把 atmospheric mechanism discovery 组织为文献、假设、数值实验和物理验证组成的 agentic workflow。
