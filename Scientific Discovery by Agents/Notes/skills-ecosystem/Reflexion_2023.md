# Reflexion 2023

## 基本信息
- **论文**: Reflexion: Language Agents with Verbal Reinforcement Learning
- **作者**: Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao
- **年份**: 2023
- **来源**: arXiv:2303.11366
- **关键词**: skill-ecosystem

## 核心思想
无需更新模型权重的"语言强化学习"框架——Agent 任务失败后生成 NL 反思
文本，存入情景记忆缓冲区，后续尝试中参考累积反思改进决策。灵活支持多种
反馈信号（标量/自由文本）和来源（外部环境/内部模拟）。三领域显著提升：
AlfWorld 12 次迭代 +22%，130/134 任务；HumanEval 91% pass@1（GPT-4
基线 80%）；HotPotQA +20%。贡献 LeetcodeHardGym——40 道 GPT-4 训练截
止后的 Leetcode hard 题。

## 研究问题与动机
传统 RL 微调成本高，标量奖励难以传达精确语义改进方向（信用分配问题）。
核心洞察：人类解决复杂任务时并非梯度更新大脑，而是反思失败、提炼教训、
调整策略——本质是自然语言空间的"语义梯度"。假设：(a) LLM 能生成比标量
奖励丰富得多的 NL 反思（具体指出"哪错、为什么、怎么做"），(b) 持久化
反思为情景记忆并提供为后续上下文，可无需改参数实现策略迭代优化，(c) 效
果随 LLM 自我评估能力增强而增强。

## 方法细节
三模型协同（全 in-context learning）：
- Actor (M_a)：LLM 动作生成器，条件于状态 o_t + memory（短期轨迹+长期
反思），内置 CoT/ReAct。π_θ(a_t|s_t)，θ = {M_a, mem}。
- Evaluator (M_e)：评估轨迹输出 r。三实现：(a) 精确匹配（推理），(b) 启发
式（AlfWorld：连续 3 次同动作或超 30 步触发），(c) LLM 自评估（代码用
自写单元测试）。
- Self-Reflection (M_sr) 核心：输入稀疏奖励 r、轨迹 τ 和记忆 mem，输出
NL 反思 sr。如"锅不在炉灶上却试图捡起→下次应先确认位置"。sr 追加长期
记忆（1-3 条）。与 Self-Refine 关键区别：记忆跨试次持久化。
流程：Actor 生成 τ_0 → Evaluator 评 r_0 → 未通过 → Self-Reflection 分析
{τ_0, r_0} 生成 sr_0 → 追加 mem → Actor 基于增强 mem 生成 τ_1 → 循环。

## 关键结果
GPT-3/3.5/4 基座，三领域验证：
- AlfWorld（134 任务，6 类型）：ReAct+Reflexion（启发式）12 试次后 130/134，
+22% 绝对提升。幻觉（误以为持有物品）和低效规划均持续改善。ReAct-only
幻觉率停滞 22% 无法恢复。
- HotPotQA（100 题）：论文总述称 Reflexion 带来约 +20% 提升；具体表格中，
GPT-4 CoT(GT)+Reflexion 从 0.68 提升到 0.80（+12pct），GPT-3.5 CoT(GT)+Reflexion
从 0.57 提升到 0.71（+14pct）。消融显示，反思比简单情景记忆额外提升约
8pct——"反思指导的精炼才有效"。
- 代码：HumanEval 91%（基线 80%，+11pct）；Rust 68%；LeetcodeHardGym
翻倍（15% vs 7.5%）。MBPP Python 略低于基线——根因 16.3% 假阳性（vs
HumanEval 1.4%）。消融：去内部测试→52%（<60%基线）；去 NL 反思→无
提升（60%=基线）——缺一不可。
- 模型阈值：StarChat-beta 完全无效（26%=26%）——反思是强模型新兴属性。
## 局限性
- 评估能力决定反思上限；如果 evaluator 本身错误，反思会强化错误方向。
- 记忆通常只有 1-3 条，难以覆盖复杂长程任务的多类失败模式。
- 系统可能陷入局部最优；假阳性测试会导致过早终止。
- 失败信用分配仍未被规范解决，反思文本不一定定位到真正错误原因。

## 核心贡献
核心：NL 反思作"语义梯度"，不更新权重实现 Agent 自我改进——"试错→反
思→记忆→重试"语义化策略优化循环。
Pipeline：Actor 基于记忆生成轨迹 → Evaluator 返回成功/失败 → Self-
Reflection 生成 NL 反思（哪错+为什么+怎么做）→ 反思存入情景记忆 → Actor
基于增强记忆调整 → 迭代至成功。

## 与综述的关联
为科学发现 Agent 提供"从失败实验中学习"核心机制。实验失败是常态——
Reflexion 使 Agent 自动诊断失败、将教训转持久 NL 记忆、后续实验主动规避
历史错误。记忆机制是"实验日志→经验归纳→假设修正"循环的计算化实现。
与 Voyager 互补：Voyager 通过成功经验技能化积累提升上限，Reflexion 通过
失败反思学习抬升下限。两者构成完整"试错+技能积累"生态闭环。
