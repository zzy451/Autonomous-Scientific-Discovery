# GeoEvolve 2025

## 基本信息

- **论文**: GeoEvolve: Automating Geospatial Model Discovery via Multi-Agent Large Language Models
- **年份**: 2025
- **来源**: arXiv:2509.21593
- **系统名称**: GeoEvolve
- **关键词**: geospatial model discovery, multi-agent LLM, evolutionary search, GeoKnowRAG, code evolver

## 摘要要点

GeoEvolve 是面向 geospatial model discovery 的 multi-agent LLM framework。论文指出，AlphaEvolve 等通用代码演化框架能演化 generic code，但缺少 geospatial domain knowledge 和多步科学推理。GeoEvolve 将 evolutionary search 与 geospatial knowledge 结合，通过 inner code evolver 和 outer agentic controller 两层循环自动设计、变异和优化地理空间算法。

## 方法动机

地理空间建模需要理论先验、空间统计知识和计算效率。单纯代码演化可能找到看似有效但缺少地理意义的解。GeoEvolve 的假设是：如果演化搜索能够持续注入结构化地理知识，就能发现更可信、更高效的 geospatial algorithms。

## 方法设计

系统包含两个嵌套循环：

1. inner loop: code evolver 生成和变异候选 geospatial model / algorithm。
2. 候选代码被执行并在任务指标上评估。
3. outer agentic controller 汇总 global elites。
4. controller 查询 GeoKnowRAG，获得地理理论先验和领域约束。
5. 知识反馈注入下一轮 code mutation / refinement。
6. 多轮循环后输出性能更好且理论上更有意义的算法。

这是一种层级式演化搜索：内层演化代码，外层 agent 控制知识注入和 elite selection。

## 实验与结果

论文在 spatial interpolation / kriging 和 geospatial conformal prediction 两类任务上评估。结果显示 GeoEvolve 自动改进和发现新算法，空间插值 RMSE 降低 13-21%，不确定性估计性能提升 17%。消融实验显示 domain-guided retrieval 对稳定、高质量演化很重要。

## 局限性

- 当前任务集中在两个经典地理空间建模问题。
- 发现的算法仍需领域专家解释其科学意义。
- 代码演化可能过拟合 benchmark，需要更广泛外部验证。

## XYZ 分类

| 维度 | 标注 | 理由 |
|---|---|---|
| X | `X4` | outer agentic controller 与 inner code evolver 构成层级搜索组织 |
| Y | `Y4` | mutation、elite selection 和多轮 code evolution 是核心机制 |
| Z | `Z1,Z3,Z4,Z5,Z7,Z8` | 覆盖知识检索、模型/代码设计、执行、分析、验证和迭代 |

## 对综述的价值

GeoEvolve 是 `X4-Y4` 的重要证据，能说明 evolutionary workflow 不必是单层 code search；它可以由层级 agent 注入领域知识，从而服务于更可信的科学模型发现。

