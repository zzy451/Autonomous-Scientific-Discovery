# SimpleQA 2024

## 基本信息
- **论文**: Measuring short-form factuality in large language models (SimpleQA)
- **作者**: Jason Wei, Nguyen Karina, Hyung Won Chung, Yunxin Joy Jiao, Spencer Papay, Amelia Glaese, John Schulman, William Fedus
- **年份**: 2024
- **来源**: arXiv:2411.04368
- **关键词**: benchmark, factuality, QA, calibration, GPT-4, hallucination

## 核心思想
该文提出 SimpleQA，一个包含 4,326 道简短事实性问题的基准，用于评估语言模型的事实准确性。设计遵循两个核心原则：一是针对 GPT-4 的响应进行对抗性收集以确保挑战性（GPT-4o 和 Claude 均低于 50%）；二是每个问题有且仅有一个无可争议的答案。每个回答被标记为正确（correct）、错误（incorrect）或未尝试（not attempted）。理想模型应在尽可能多的题目上正确作答，同时在不确定时选择不答。基准旨在成为测量模型"是否知道自己知道什么"的简单而可靠的工具，托管在 openai/simple-evals。

## 评测目标
衡量语言模型的事实性知识准确度和自知之明（calibration）。与 TriviaQA、Natural Questions 等已饱和的基准不同，SimpleQA 专门设计为对抗性——针对 GPT-4 容易出错的事实领域创建问题，确保对前沿模型仍有区分度。不测推理、不测长文生成、不测多轮对话——仅测试模型对简单事实问题的回答是否准确，以及模型是否能在不确定时选择"不回答"而非编造。这一设计直接针对 LLM 的幻觉问题。在科学发现场景中，事实准确性是智能体提出可靠科学主张的前提条件。

## 基准设计
- **题目数量/来源/难度分级**：4,326 道简短事实性问题。数据收集分两阶段：(1) AI 训练师（人类标注者）创建问题-答案对；(2) 另一位独立训练师回答同一问题，仅当答案一致时保留。主题分布（ChatGPT 后分类）：Science & Technology 19.8%、Politics 16.4%、Art 12.7%、Geography 9.8%、Sports 8.5%、Music 7.9%、TV shows 6.8%、History 4.0%、Video games 3.1%、Other 11.0%。答案类型分布：日期 32.8%、人名 24.1%、数字 15.3%、地名 9.9%、其他 18.0%。主要信息源：Wikipedia（3.5k/4.3k 题引用）、fandom.com（410）、ac.uk（154）、imdb.com（121）。
- **评分方式**：三级自动评分——Correct（预测答案完全包含参考答案且无矛盾）、Incorrect（存在任何矛盾，即使有 hedging）、Not Attempted（未给出完整答案且无矛盾）。使用 prompted ChatGPT classifier（向 grader 提供问题、参考答案和预测答案，详见论文 Appendix A）。手动验证 100+100+100 正确/错误/未尝试案例，仅发现 2 例与 grader 不一致。核心指标：Overall Correct（正确率）、Correct Given Attempted（尝试回答中的正确率）、F-score（两者调和平均）。第三种指标：加权得分 = 正确(1分) + 未尝试(0分) + 错误(-p分)，p 可根据应用场景设定。
- **人类基线 vs AI 基线**：人类：从 1,000 道随机题目中，第三位训练师（独立）的正确率为 94.4%。错误分析：3% 估计为基准本身错误（模糊问题、权威来源矛盾、多正确答案）。模型表现（Table 3）：GPT-4o Correct 38.2%、Not Attempted 1.0%、Incorrect 60.8%、Correct Given Attempted 38.0%、F-score 38.4%；OpenAI o1-preview Correct 42.7%、Not Attempted 9.2%、Incorrect 48.1%、Correct Given Attempted 47.0%、F-score 44.8%；Claude-3.5-sonnet Correct 28.9%、Not Attempted 35.0%、Incorrect 36.1%、Correct Given Attempted 44.5%、F-score 35.0%；GPT-4o-mini Correct 8.6%、Not Attempted 0.9%、Incorrect 90.5%、Correct Given Attempted 8.7%、F-score 8.6%。
- **设计原则**：(i) 高正确性——两位训练师独立验证每个答案，第三位训练师验证正确率 94.4%，基准错误率估计约 3%；(ii) 对抗性难度——每个问题至少让 4 个 GPT-4 版本中的 1 个出错；(iii) 易于使用的极简设计——短问题和短答案、快速 API grading、4,326 题确保低运行间方差；(iv) 必须指定单位/范围（如"which city"而非"where"、"what year"而非"when"）；(v) 答案不随时间变化；(vi) 所有问题在 2023-12-31 前可回答，确保对所有模型公平。

## 关键数字
| 指标 | 值 |
|------|-----|
| 问题总数 | 4,326 |
| 基准错误率估计 | ~3% |
| 主题类别数 | 10 |
| GPT-4o Correct | 38.2% |
| GPT-4o Not Attempted | 1.0%（几乎总是尝试）|
| GPT-4o F-score | 38.4% |
| o1-preview Correct | 42.7% |
| o1-preview Correct Given Attempted | 47.0% |
| o1-preview Not Attempted | 9.2% |
| Claude-3.5-sonnet Correct | 28.9% |
| Claude-3.5-sonnet Not Attempted | 35.0%（更具自知之明）|
| GPT-4o-mini Correct | 8.6% |
| GPT-4o-mini Not Attempted / Incorrect | 0.9% / 90.5% |
| Claude-3.5-sonnet F-score | 35.0% |
| 人类第三训练师正确率 | 94.4% |
| 最大信息源 | Wikipedia（~81% 题目涉及）|
| 校准实验 | 100 次重复采样（temperature=1）|

## 设计哲学
- **"知道你所不知"的评估哲学**：SimpleQA 最独特的设计是三级评分（特别是 Not Attempted）。传统 QA 基准仅关注正确率，SimpleQA 额外惩罚"自信地犯错误"——这直接测量了模型的事实自知之明。Claude-3.5-sonnet 的 Not Attempted 率明显高于 GPT-4o，而 GPT-4o 和 GPT-4o-mini 几乎总是尝试作答，暴露出过度自信。
- **对抗性收集的方法论**：问题专门针对 GPT-4 弱点创建，而非从自然分布中采样。这确保基准不会因模型进步而快速饱和——只要模型在某些事实领域仍有盲点，SimpleQA 就能保持区分度。但这也意味着"SimpleQA 分数"不应被解释为模型在自然问题分布上的表现。
- **对 F-score 局限性的坦诚**：论文（Appendix B）明确推导了 F-score 在低表现区间的激励扭曲问题——当模型 >50% 确信时可从中获益，提出了带惩罚项 p 的替代评分方案。这种对自身评估指标的批判性反思在基准论文中罕见。
- **极简主义的评估美学**：SimpleQA 刻意做减法——不做多轮对话、不做长答案评估、不做推理链评估。这种"少即是多"的设计使基准成为纯事实性这一单一维度的可靠测量工具。

## 局限性
- 仅限于短答案事实问题，不评估结构化知识解释、因果推理或"如何"和"为什么"类问题。
- 对抗性收集针对 GPT-4，其他模型的能力画像可能不同，跨模型比较需谨慎。
- 事实知识的"唯一正确答案"假设在某些领域（如前沿科学、有争议的历史事件）本身存疑。论文承认约 3% 的基准错误率来自权威来源矛盾等。
- 不衡量知识的时效性——虽要求答案不随时间变化，但无法评估模型对最新信息的掌握。
- "Not Attempted" 作为安全策略在某些科学探索场景下过于保守——科学研究需要假设性推测和不确定性下的探索。
- 未评估事实知识的"深度"——模型可能给出正确答案但缺乏深层理解。
- 仅评估英文事实性知识，文化和语言覆盖面有限。

## 核心贡献
SimpleQA 2024 的核心贡献是用短答案、单一事实、三级评分的极简设置，把“事实正确性”和“是否知道自己不知道”拆成可低成本复测的评估维度。

## 与综述的关联
SimpleQA 是事实性知识基准的标杆，在本综述 benchmark 章节中代表"基础知识准确性"维度。科学发现智能体需要在大量事实性知识的基础上进行推理和假设，基础事实的准确性直接影响上层推理的可靠性。SimpleQA 的 Not Attempted 评分机制为评估智能体的自知之明提供了简单但有效的方法——这对科学发现中的不确定性管理至关重要（智能体应区分"已知的未知"和"已知的已知"）。它与 BrowseComp 形成"静态知识 vs 动态检索"的对照——SimpleQA 测模型内部存储的事实，BrowseComp 测模型查找未知事实的能力。
