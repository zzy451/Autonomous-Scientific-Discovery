# Buffer of Thoughts 2024

## 基本信息
- **论文**: Buffer of Thoughts: Thought-Augmented Reasoning with Large Language Models
- **作者**: Ling Yang, Zhaochen Yu, Tianjun Zhang, Shiyi Cao, Minkai Xu, Wentao Zhang, Joseph E. Gonzalez, Bin Cui
- **年份**: 2024
- **来源**: NeurIPS 2024 Spotlight; arXiv:2406.04271
- **关键词**: skill-ecosystem

## 核心思想
Buffer of Thoughts (BoT) 是一种新颖通用的思维增强推理方法，同时提升 LLM
推理准确率、效率和稳健性。核心：meta-buffer——存储从不同任务求解过程中
提炼的高层思维模板（thought-template）。对新问题检索相关模板并自适应实例
化为具体推理。buffer-manager 动态更新 meta-buffer，使容量随任务解决持续增
强。10 个推理密集型基准全面显著提升：Game of 24 +11%、Geometric Shapes
+20%、Checkmate-in-One +51%。成本仅 ToT/GoT 等多查询方法平均 12%。
Llama3-8B+BoT 在部分任务上可超越 Llama3-70B。NeurIPS 2024 Spotlight。

## 研究问题与动机
现有方法两大瓶颈：(a) 单查询（CoT/Few-shot）：依赖人工设计任务特定提示，
缺乏通用性和跨任务可迁移性；(b) 多查询（ToT/GoT/Meta-prompting）：递归
搜索多路径，成本极高（数十上百次调用），每次从零构建无法利用历史方法论。
洞察来自人类：面对新问题不从零推导方法论，而是归纳通用思维模板（如"判
别式→根性质→求根公式"）再适配具体参数。假设：将推理方法论从已完成任
务蒸馏为参数无关高层模板，存入缓冲区，检索实例化，可同时实现高准确率、
高效率和强稳健性。

## 方法细节
三模块流水线，全 LLM in-context：
- Problem Distiller：元提示 φ 蒸馏 x_d = LLM(φ(x))。提取核心参数/变量、
目标/约束，将具体问题翻译为高层结构（如"促销利润"→"二次方程求解"）。
- Meta-Buffer 与检索：存储 (T_i, DT_i, C_k) 三元组——模板内容、描述、类别
（6 类：文本理解/创意生成/常识推理/数学推理/代码编程/应用调度）。检索计
算嵌入余弦相似度 ≥ δ(0.5-0.7) 选中；< δ 视为新任务用 3 个通用模板兜底。
- Instantiated Reasoning：检索到 T_j 后，LLM 自适应填充具体数值——如
Checkmate-in-One 中"棋局状态更新"模板实例化为当前棋局分析（类 OOP 实
例化）。
- Buffer-Manager：三步蒸馏——(1) 核心任务总结，(2) 通用求解步骤，(3) 通
用答案模板。跨任务示例增强泛化。动态更新：新模板与已有最大相似度 < δ 才
存入（去重），保证轻量高质量。

## 关键结果
GPT-4 基座（消融用 Llama3-8B/70B），10 个多样化基准：
- 准确率：Game of 24 82.4%（基线 3.0%，+79.4pct；vs ToT 74.0%）；
Checkmate-in-One 86.4%（基线 36.4%，+51%）；Geometric Shapes 93.6%（基线
52.6%）；Multi-Step Arithmetic 99.8%；Word Sorting 100%；Python Puzzles
52.4%（基线 31.1%）；MGSM 89.2%；Date Understanding 88.2%；Penguins
94.7%；Sonnet Writing 80.0%（仅 +0.4pct，创意任务提升有限）。
- 效率：平均 12% of ToT/GoT 成本。代码格式模板使单次查询完成推理。Game
of 24 ~5s vs ToT ~56s。
- 稳健性：1000 例重复 10 次，平均成功率 95.15%，超第二最佳 10pct+。
- 模型-性能权衡：Llama3-8B+BoT 在 Game of 24(73.4%) 和
Checkmate-in-One(56.7%) 上超过不加 BoT 的 Llama3-70B（分别 2.4%/15.0%），
但在 Word Sorting 上为 73.4%，低于 Llama3-70B 的 79.0%。论文表述为“小模型+BoT 有潜力超过单独的大模型”，不等同于所有任务上稳定替代大模型。
- 消融：去 Distiller→复杂任务 -8~9pct；去 Meta-Buffer→降幅最大（Game of
24 81.7%→65.6%，Checkmate 79.6%→27.4%）；去 Buffer-Manager→4 轮无改
善，启用版准确率升(56.8%→88.5%)时间降(297s→78.5s)。
## 局限性
- 创意任务提升有限，说明 thought-template 更适合结构化推理而非开放式创作。
- 弱模型初始化模板质量受限，早期模板错误会影响后续检索和实例化。
- 模板蒸馏过程本身不可微、不可直接优化，长期演化质量需要额外验证。

## 核心贡献
核心："思维模板"蒸馏-存储-检索-实例化循环替代每次从头推理，方法论复用
使推理既准又快（成本仅 ToT 12%）。
Pipeline：Distiller 蒸馏 → Meta-Buffer 检索最相似模板（<δ 用通用模板）→ 
自适应实例化 → 推理得解 → Buffer-Manager 蒸馏新模板去重入库 → 持续扩容。

## 与综述的关联
贡献"推理技能即模板"关键范式——不同于 Voyager 操作执行技能（可执行代码）
或 AWM 过程技能（workflows），BoT 聚焦方法论层面认知技能复用，是科学发
现最核心需求。学科方法论（统计检验、方程建模、实验设计、因果推断）可蒸
馏为 thought-template，Agent 检索实例化，避免从零推导。12% 成本对大规模
假设搜索至关重要，buffer-manager 也为"方法论持续进化"提供技术雏形。
