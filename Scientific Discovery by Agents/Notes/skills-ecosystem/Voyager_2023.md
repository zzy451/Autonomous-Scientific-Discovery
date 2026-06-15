# Voyager 2023

## 基本信息
- **论文**: Voyager: An Open-Ended Embodied Agent with Large Language Models
- **作者**: Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi "Jim" Fan, Anima Anandkumar
- **年份**: 2023
- **来源**: arXiv:2305.16291
- **关键词**: skill-ecosystem

## 核心思想
首个 LLM 驱动的具身终身学习 Agent，在 Minecraft 中持续探索、获取多样技能，
无需人类干预。三大组件：(1) 最大化探索的自动课程，(2) 可执行代码构成的
持续增长技能库，(3) 融合环境反馈、执行错误和自我验证的迭代提示机制。
仅通过 GPT-4 黑盒查询实现，无需微调。技能具有时间扩展性、可解释性和
可组合性，使能力快速复合增长并缓解灾难性遗忘。MineDojo 评估：比先前
SOTA 多 3.3 倍独特物品、旅行 2.3 倍距离、技术树解锁快 15.3 倍。技能库
可跨世界零样本泛化到新任务（钻石镐、金剑、熔岩桶、指南针）。ReAct、Reflexion、AutoGPT 在 50 次 prompting iteration 内均未完成这些任务；去掉技能库的 Voyager 仍能完成部分任务，但效率和成功率低于完整 Voyager。

## 研究问题与动机
Minecraft 无预定义终端目标，要求从基础逐步进阶到复杂操作。传统方法三大
瓶颈：(a) RL 探索效率低（稀疏奖励、巨大空间），(b) ReAct 等 LLM Agent
每次从头推理无技能积累，(c) 持续学习灾难性遗忘。核心假设：用"代码作为
动作空间"替代低层电机指令——程序天然具备时间扩展性和可组合性。若 Agent
能自主编写、验证、存储、复用可执行技能，即可实现终身学习。

## 方法细节
三大模块闭环（全通过黑盒 GPT-4，无梯度更新）：
- 自动课程：GPT-4 (T=0.1) 根据当前完整状态（背包、装备、附近实体、生物
群系、生命值等）+ 历史完成/失败任务 + GPT-3.5 自问自答上下文，以"发现
尽可能多多样事物"为目标，自底向上提出新任务。本质是 in-context novelty
search。
- 技能库：每技能 = JavaScript 可执行函数 + NL 描述。通过后以 text-
embedding-ada-002 嵌入为 key 存向量 DB。检索时用当前计划+环境反馈嵌入
查 top-5 作 GPT-4 代码生成的 in-context 示例。技能可嵌套组合（如
craftStonePickaxe 调用 craftStick + mineStone）。
- 迭代提示：代码生成 → Mineflayer 执行 → 收集三类反馈（环境反馈 + 执行
错误 + GPT-4 自我验证/critique）→ 注入下轮精炼。最多 4 轮/任务，超时切换
目标。自我验证是消融中最重要的反馈（去掉降 73%）。

## 关键结果
基于 MineDojo + Mineflayer（无像素），基线为重新实现的 ReAct/Reflexion/
AutoGPT：
- 物品发现：160 迭代内 63 种独特物品（AutoGPT 19 种，3.3 倍）。ReAct/
Reflexion 几乎无进展。
- 技术树（木→石→铁→钻石）：木制解锁快 15.3 倍（6 vs 92 迭代），石制
8.5 倍（11 vs 94），铁制 6.4 倍（21 vs 135）。唯一解锁钻石（1/3 次，102
迭代）。
- 地图遍历：2.3 倍旅行距离。零样本泛化：完整 Voyager 在新世界中 3/3 完成钻石镐、金剑、熔岩桶、指南针四个未见任务，平均迭代数分别约 19、18、21、18；ReAct、Reflexion、AutoGPT 均为 0/3。AutoGPT + Voyager skill library 可完成部分任务，说明技能库具有可迁移的 plug-and-play 价值。
- 技能检索：附录报告 309 个样本上的技能检索 top-1 / top-5 accuracy 为 80.2% / 96.5%，支持其“检索相关代码技能作为 in-context 示例”的设计。
- 消融：去课程（随机替代）→ 物品 -93%；去技能库 → 后期停滞；去自我验证
→ -73%；GPT-3.5 代 GPT-4 → 物品仅 1/5.7。
## 局限性
- GPT-4 成本高，论文中约为 GPT-3.5 的 15 倍，但在该系统中又很难直接替代。
- 自我验证偶尔误判，可能把错误技能写入技能库或错过可用技能。
- 自动课程会出现幻觉，例如提出 Minecraft 中不存在的物品目标。
- 系统依赖 Mineflayer API 和 Minecraft 环境，不能直接说明真实科学实验技能也能同等方式积累。

## 核心贡献
核心：以"代码即技能"范式实现终身学习——技能以可执行代码形式积累，
知识存储即复用，能力复合增长。
Pipeline：自动课程提任务 → 技能库检索 top-5 技能 → GPT-4 生成 JS 代码 →
执行收集反馈/错误 → GPT-4 自我验证+critique → 通过入库/失败迭代（≤4 轮）。

## 与综述的关联
技能库是"实验技能生态系统"原型——实验设计、数据分析、假设检验可类比
可复用代码模块。自动课程映射为自主研究路径规划。该工作是技能生态子方向
的奠基性论文之一。技能应以可执行代码存储和复用的洞察直接启发了
Anthropic Skills Spec、SkillsBench 等后续设计。
