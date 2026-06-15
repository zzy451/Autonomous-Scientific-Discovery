# Generative Agents 2023

## 基本信息
- **论文**: Generative Agents: Interactive Simulacra of Human Behavior
- **作者**: Joon Sung Park, Joseph C. O'Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, Michael S. Bernstein
- **年份**: 2023
- **来源**: arXiv:2304.03442 (UIST '23)
- **关键词**: memory, reflection, planning, agent-architecture, emergent-behavior, social-simulation

## 核心思想
本文提出生成式智能体——在交互沙盒中展现可信人类行为的计算智能体。25 个智能体在《模拟人生》风格小镇 (Smallville) 中起床、做饭、上班，记住和反思过去并据此规划未来。架构将 LLM 扩展为三个组件：记忆流存储所有自然语言经验记录，反思将记忆合成为高层推断，检索动态提取相关记忆以规划行为。仅凭一条种子提示（某智能体想办情人节派对）即自主完成传播邀请、结交新朋友、协调到场时间等涌现社会行为。消融实验通过逐步移除观察/规划/反思可访问记忆来比较可信度，显示完整架构最佳、组件缺失会降低表现。发表于 UIST '23。

## 研究问题与动机
如何让 LLM Agent 长期保持行为连贯可信？与 MemGPT 关注"如何存更多"不同，
Generative Agents 关注"存了什么之后如何用"——记忆的组织、抽象和规划利用。三个挑战：(a) Agent 记忆随交互持续增长，远超 LLM 有限上下文窗口——gpt-3.5-turbo 无法容纳全量经验，全量填入反致无信息量应答；(b) 需从海量经验中提炼高层抽象——如从 "Klaus 反复读 gentrification 书籍+与图书管理员讨论研究" 推断"他对研究充满热情"，否则面对"你想和谁共度时光"时仅选互动频率最高的表面关系而非真正共享兴趣的人；(c) 需基于长期经验进行行为规划——仅凭"现在是中午"做瞬时决策将导致"12:00 吃午饭、12:30 又吃、1:00 还吃"这种瞬时可信但长期荒谬的行为。仅用一阶 prompt 无法解决。

## 方法细节
**记忆流 (Memory Stream)**：每个 Agent 维护按时间排序的自然语言记录列表。每条记忆对象含自然语言描述 + 创建时间戳 + 最近访问时间戳。基本元素=observation——Agent 直接感知的事件（自身行为/他人行为/环境对象状态），如 "Isabella Rodriguez is setting out the pastries"。

**检索 (Retrieval)**：三维度复合评分，min-max 归一化后加权求和（权重均 1）：
- Recency：指数衰减函数（衰减因子 0.995，基于距当前 sandbox 小时数），使刚刚或今晨的事件更可能留在注意力范围
- Importance：LLM 直接评分 1-10。完整 prompt——"On the scale of 1 to 10, where 1 is purely mundane (e.g., brushing teeth, making bed) and 10 is extremely poignant (e.g., a break up, college acceptance), rate the likely poignancy of the following piece of memory." "cleaning up the room"→2，"asking your crush out on a date"→8。评分在记忆创建时生成
- Relevance：LLM 生成记忆文本 embedding 向量，计算与当前查询情境的余弦相似度

**反思 (Reflection)**：周期性触发——当最新事件的 importance 总和超过阈值 150 时，智能体每天约反思 2-3 次。(1) 用最近 100 条记录提示 LLM 生成 "3 most salient high-level questions we can answer about the subjects"；(2) 以各问题为查询检索相关记忆（含已有反思，因此反思可递归堆叠）；(3) LLM 提取洞察并引用证据记忆编号——形成反思树（叶子=基观察，非叶子=逐层抽象），如 "Klaus Mueller is dedicated to his research on gentrification (because of 1, 2, 8, 15)"。反思结果作为新记忆存入记忆流，参与后续检索和再反思。

**规划 (Planning)**：自上而下递归分解。(1) 提示 LLM（Agent 摘要描述 + 前一天总结）生成日计划 5-8 个时间段（含地点/起始时间/持续时长）；(2) 递归分解为小时级动作（如 "1:00-5:00pm work on music composition"→"1:00pm brainstorm"..."4:00pm take a break"）；(3) 再分解为 5-15 分钟粒度（如 "4:00pm grab a light snack; 4:05pm take a short walk..."）。计划存入记忆流可被检索并在环境变化时实时调整。

**反应与对话**：每时间步用当前观察提示 LLM 判断继续执行计划或做出反应（需检索双方关系记忆生成上下文史："What is [observer]'s relationship with [observed entity]?"）。如果反应，重新生成从当前时间起的新计划。对话通过检索双方记忆交替生成 utterances 直到一方决定结束。环境交互：Smallville 沙盒树（世界→区域→物体）转为自然语言传递给 LLM，Agent 导航时递归遍历树结构选择最适区域。

## 关键结果
- **涌现社会行为（情人节派对）**：仅一条种子 → 25 Agent 在 2 天（游戏时间）内自主完成
  传播邀请（Isabella 在 Hobbs Cafe 向顾客和朋友发出邀请）、协调装饰（Maria 帮忙布置）、
  Maria 邀请暗恋对象 Klaus 为约会、5 名 Agent 于 2 月 14 日 5pm 最终到场。
  全过程存在大量潜在失败点但架构全部自主打通
- **信息扩散**：Sam 在杂货店→Tom 告知竞选意图 → Tom+John 讨论 Sam 胜算 → 消息自主传播形成舆论分化（支持 vs 犹豫）
- **关系记忆**：Sam 与 Latoya 初次相遇后记住她及摄影项目，后续对话主动问 "Hi, Latoya. How is your project going?" 得到回复 "Hi, Sam. It's going well!"
- **消融实验（访谈评估法）**：完整架构得分最高；逐步移除 Reflection、Planning、Observation 相关记忆会降低访谈可信度，但实验不是对每个组件做完全独立的单因素消融
- **三种主要失败模式**：(i) 未能检索到相关记忆——检索函数返回表面相关但实际无关的记忆
  (ii) 对记忆进行虚构性修饰——Agent 在回忆时添加了原始记忆中不存在的细节
  (iii) 继承了 LLM 的过度正式语言风格（instruction tuning 副作用），如"we have all agreed
  to vote for him because we like his platform" 这类不自然的表述

## 局限性
反思由近期事件 importance 累计超过阈值 150 触发，约每天 2-3 次，触发策略仍较固定；检索三维权重均固定为 1 缺乏自适应调优；大规模记忆检索可能返回表面相关但实际无关的内容；对话风格过于正式且过度合作（LLM instruction tuning 副作用）；仅使用 gpt-3.5-turbo（GPT-4 API 当时为邀请制），未在更强模型上验证性能上限；环境设计为手动生成无法自动扩展到新场景；两天 25 Agent 仿真成本高（论文称消耗数千美元 token credits 且需数天完成）。

## 核心贡献
第一条将 LLM 与持续记忆/反思/规划深度结合的 Agent 架构，单条种子驱动 25 Agent 产生完整社会涌现链（邀请→协调→约会→到场）。
Pipeline：Perceive → [Memory Stream → Retrieval (recency_decay_0.995 × importance_LLM_1-10 × relevance_cosine_embedding) + Reflection (importance_sum>150 → generate 3 salient questions → retrieve matches → extract insights with citations → store as reflective memory → recursive tree) + Planning (day_broad_chunks → hour_chunks → 5-15min actions; stored back in stream)] → Act / React / Dialogue (retrieve relationship memory → generate contextual utterances)

## 与综述的关联
LLM Agent 记忆系统的奠基性文献，"记忆流→检索→反思→规划"四阶段架构深刻影响了后续几乎所有 Agent 记忆系统设计。在科学发现场景中：反思≈从实验观察数据中自动提炼科学假设和抽象规律，规划≈实验方案的自动设计与执行调度，记忆流≈实验室知识库的持续积累，检索≈根据当前研究目标自动调取相关历史实验和文献。该架构启发了一整条从"模拟人类日常行为"到"模拟科学家科研行为"的技术迁移路径——科学发现本质上也是一系列持续观察积累、记忆维护、反思抽象和长期规划的过程。
