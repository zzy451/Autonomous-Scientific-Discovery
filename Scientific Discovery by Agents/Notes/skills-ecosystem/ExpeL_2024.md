# ExpeL 2024

## 基本信息
- **论文**: ExpeL: LLM Agents Are Experiential Learners
- **作者**: Andrew Zhao, Daniel Huang, Quentin Xu, Matthieu Lin, Yong-Jin Liu, Gao Huang (清华大学)
- **年份**: 2024
- **来源**: AAAI 2024 (doi:10.1609/aaai.v38i17.29936), arXiv: 2308.10144
- **关键词**: 经验学习, LLM 智能体, 无需微调, 自然语言记忆, 试错学习, 知识迁移

## 核心思想
ExpeL 是清华大学团队在 AAAI 2024 提出的 LLM 智能体经验学习框架。核心思想：LLM 智能体可以通过"试错经验"的自然语言积累来提升任务表现，完全不需要对模型参数进行任何微调（gradient-free）。这一设计瞄准了一个关键痛点：GPT-4、Claude 等最先进模型仅通过 API 提供，参数权重不公开，传统微调路线不可行。ExpeL 证明，纯自然语言记忆池驱动的学习机制可以持续提升智能体表现。

## 方法细节
- **三阶段学习**：
  (1) 经验收集（Experience Gathering）——智能体在训练任务集合上执行任务，并借助 Reflexion 式重试收集成功与失败轨迹。
  (2) 洞察提取（Insight Extraction）——从成功/失败对或成功轨迹列表中抽象可迁移的自然语言洞察，并用 ADD、EDIT、UPVOTE、DOWNVOTE 操作维护 insight 列表。
  (3) 任务推理（Task Inference）——面对新任务时，将抽取出的洞察加入任务说明，并从成功轨迹池中检索 top-k 相似示例作为 few-shot 上下文。检索使用语义相似度，论文实现中使用 Faiss 与 all-mpnet-base-v2。
- **无需参数更新**：全过程不涉及梯度下降、LoRA、或任何形式的模型权重修改。这一特性对仅能通过 API 调用的闭源模型（如 GPT-4、Claude）至关重要，也为频繁更新的模型提供了"无需重训"的持续改进方案。
- **经验积累效果**：实验表明智能体在 HotpotQA、ALFWorld 和 WebShop 上总体优于 Act/ReAct 等基线，验证了纯语言记忆驱动的试错学习的可行性。定性分析进一步观察到了涌现能力（emerging capabilities）与知识迁移（transfer learning）的迹象。

## 关键结果
- 提出了梯度无关（gradient-free）的 LLM 智能体提升范式，区别于传统的 RLHF/微调路线。这是对"闭源 API 模型如何持续改进"这一实践问题的直接回应。
- 实验证明了自然语言经验池作为长期记忆机制的有效性——在 HotpotQA、ALFWorld、WebShop 三类文本环境中，ExpeL 总体优于 Act/ReAct 基线。论文还与 Reflexion 比较：HotpotQA 上 ExpeL 约 39%，接近 Reflexion R3 的 40%；ALFWorld 上 ExpeL 约 59%，高于 Reflexion R3 的 54%，且不需要在测试任务上反复重试。
- 消融显示 insight 与 retrieval 的作用具有任务差异：HotpotQA 中 insights-only / retrieve-only 分别约为 36% / 31%，ALFWorld 中约为 50% / 55%，WebShop 中二者接近（成功率约 37% / 38%，reward 约 0.675 / 0.67）。这说明抽象洞察与相似轨迹回忆不是同一种机制。
- 揭示了 LLM 智能体的迁移学习潜力：论文将 HotpotQA 上提取的洞察迁移到 FEVER fact verification，ExpeL Transfer 达 70%（vs ReAct 63%、Act 58%），表明经验提取并非只是在单一任务上过拟合。
- 定性观察发现了"涌现能力"——例如 HotpotQA 中根据已有 observation 作出有根据的回答，ALFWorld 中更新物体位置先验，以及拿错物体后的自我纠正。但这些是论文基于轨迹检查得到的定性观察，不应被解读为稳定、通用的 emergent intelligence。
- 为仅通过 API 访问的闭源模型（GPT-4、Claude）提供了可行的持续改进路径，无需等待模型供应商更新。

## 与 Skills 生态的关系
ExpeL 与本综述 Skills 生态维度存在深刻的"生成 vs 消费"张力：
- **ExpeL 视角**：经验洞察是自然语言形式的可迁移知识，LLM 可自主从经验中提取。本质上，ExpeL 是"技能的自动生成器"。
- **SkillsBench 视角**：模型无法自主生成有效技能——自生成技能平均无收益甚或负效果。
- **调和可能**：ExpeL 提取的是"经验层面的策略知识"（如在某个游戏中的试探偏序），而 SkillsBench 评估的是"工具层面的程序性知识"（如如何使用特定 API）。前者更抽象、更元认知，后者更具体、更依赖外部事实。两者的张力暗示：技能自动生成在抽象策略层面可能可行，在具体工具层面尚需人类监督。

## 核心贡献
ExpeL 2024 的核心贡献是把"经验"转化为可复用的自然语言洞察与成功轨迹检索机制，展示了无需参数更新的 agent skill acquisition / retrieval 路线：智能体可以从跨任务试错中提取策略性知识，并在新任务中以上下文形式复用。

## 与综述的关联
- 科学发现智能体的"学习与技能积累"范式——ExpeL 的经验学习机制为科研智能体提供了"从失败实验中学习"的理论基础。如果科研智能体能够以自然语言记录每个实验的成败经验，并在此后的研究中复用这些洞察，则系统能力可随时间持续提升而无需重启训练。
- 与 Buffer-of-Thoughts 形成互补：ExpeL 强调跨任务的经验迁移（"做过类似的事所以知道怎么做"），BoT 强调推理模板的高效复用（"见过类似的问题类型所以知道怎么推导"）。两者共同构成"无需微调的智能体提升"方法论家族。

## 局限性
- 经验提取的质量高度依赖 LLM 的归纳能力——弱模型可能从经验中提取出低质量或过拟合的"伪洞察"。
- 记忆池随经验增长而膨胀，语义检索的质量与效率在高容量场景下需额外工程优化。
- 实验主要是文本观察环境；作者明确指出真实场景常含图像观察，未来需要引入 vision-language agent。
- Insight 由 GPT-4-0613 抽取，而执行阶段使用 gpt-3.5-turbo-0613；框架效果部分依赖强模型的归纳与指令遵循能力。
