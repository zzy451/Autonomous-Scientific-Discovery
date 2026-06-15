# AstroAgents 2025

## 基本信息
- **论文**: AstroAgents: A Multi-Agent AI for Hypothesis Generation from Mass Spectrometry Data
- **作者**: Daniel Saeedi, Denise Buckner, Jose C. Aponte, Amirali Aghazadeh
- **年份**: 2025
- **来源**: arXiv:2503.23170
- **关键词**: astrobiology, multi-agent, mass-spectrometry, hypothesis-generation

## 核心思想
AstroAgents 用多智能体系统从质谱数据和文献中生成关于生命起源的科学假设。

## 方法细节
系统包含 data analyst、planner、domain scientists、accumulator、literature reviewer 和 critic 等 8 个 agents。

## 关键结果
专家评估显示生成的 100 多个假设中，一部分被认为既 plausible 又 novel。

## 局限性
主要是 hypothesis generation，不包含真实实验验证。

## 核心贡献
展示多智能体可结合实验数据和文献提出领域科学假设。

## 与综述的关联
适合放入 `X2-Y2-Z1/Z2/Z5,Z7`，补强数据驱动 hypothesis generation。

## 原文核对与分类复核
- **原文核对**：原文明确列出八个 agents：data analyst、planner、three domain scientists、accumulator、literature reviewer、critic。
- **机制判断**：系统从质谱数据和文献生成天体生物学假设，并由专家评估 novelty/plausibility。
- **分类复核**：保持 `ASD 相关系统`；`X2` 正确；`Y2` 正确；`Z1,Z2,Z5,Z7` 正确。
- **写作用途**：适合说明多角色假设生成和数据驱动科学 ideation。

## 深读补充（按 MARS 标准）

### 研究问题
AstroAgents 关注从 mass spectrometry data 中生成 astrobiology hypotheses 的困难：数据噪声、污染物、峰值复杂、与文献交叉匹配困难。

### 系统架构 / 工作流
系统包含八个 agents：data analyst、planner、三个 domain scientists、accumulator、literature reviewer 和 critic。

### 关键机制
核心是多角色数据解释和假设生成。Planner 分派任务，domain scientists 深入探索，accumulator 汇总去重，literature reviewer 检索文献，critic 提出改进意见。

### 实验验证与证据
原文由天体生物学专家评估来自陨石和土壤样本的 100+ 假设，报告一定比例被认为 plausible 和 novel。

### 局限性补充
系统主要生成假设，未完成后续实验验证；专家评价成本较高。

### XYZ 分类逐项解释
- `X2`：八个固定角色 agents。
- `Y2`：生成、汇总、去重和评价候选假设。
- `Z1,Z2,Z5,Z7`：覆盖文献、假设、数据解释和专家评价。

### 综述写作用法
适合多智能体数据驱动假设生成案例。
