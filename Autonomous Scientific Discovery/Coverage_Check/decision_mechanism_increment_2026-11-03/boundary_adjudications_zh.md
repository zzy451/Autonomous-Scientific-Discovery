# 机制边界裁决记录

所有判断仅写本增量目录；不改原始笔记或标签。此表记录本轮归类所用的操作边界，完整逐篇证据见结果表。

| 论文/边界 | 本轮判断 | 理由 |
|---|---|---|
| A-Lab（ASD-0016） | D3 | 文献语言模型提出配方，ARROWS/主动学习在热力学信息下控制失败后的下一实验；主标签取实验选择机制。 |
| CLAIRify（ASD-0012）/Organa（ASD-0036） | D5 | LLM决定实验语义或下一缓冲液；符号任务—运动规划器实现已确定实验，单纯执行规划不足证明共同选择科研实验。 |
| MatPilot（ASD-0065） | D5 | 语言认知模块生成假设及实验方案；泛称evolutionary optimization而未明确独立采集/搜索选择器，不直接判D6。 |
| Dai移动机器人（ASD-0037） | D1 | PDF p3明确专家设计heuristics，将MS/NMR表征按规则判pass/fail后决定后续合成，并非最大化单一性能目标。 |
| Robot Scientist（ASD-0501） | D1 | 逻辑模型上的abduction提出假设、deduction检验，成本与信息实验选择服务于该科学推理过程。 |
| FunSearch/AlphaEvolve | D6 | LLM生成程序，独立进化搜索、种群/档案选择与评估共同控制下一候选及搜索更新。 |
| AEGIS系列 | D3 | 目标特征加权评分排序选点；旧Planning标签和航天平台不决定主标签。 |
| Mimosa（ASD-0662） | D5 | LLM提出结构/提示变异、LLM judge评价；单候选接受/回滚不单独当成另一种实质决策机制。 |
| MolReAct（ASD-0820） | D5 | 进一步读PDF发现选择器是Qwen-3-4B语言模型加action head；不是抽象中容易误认的独立非LLM RL。两个语言模型分工不等于两种机制。 |
| SciDisco（ASD-0919） | D5 | RL训练LLM Agent不等于非LLM策略系统。 |
| Immune World Model（ASD-0967） | D5暂定 | 两个交叉审阅者对lineage metric门控是否构成独立演化控制有分歧；主控按与Mimosa同一边界，固定接受/回滚与阈值不足，暂取语言Scientist主导并留待复核。 |
| Bosonic Floquet control（ASD-1111） | D4 | TD3神经控制策略直接输出动作；与LLM语言行动决策不同。 |
| 比较多种独立Agent的论文 | 唯一主标签+明确概括限制 | 依用户要求每篇仅一类；若无唯一核心系统，降低置信度，不能把并列对比系统写成系统内融合。 |

置信度只描述此次标签判断，不表示科学结果验证强度；暂定与待全文复核是状态字段，不增设第七类。
