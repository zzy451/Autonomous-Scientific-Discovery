"""Save controller adjudications as additive overrides; preserve reviewer records."""
import csv
import json
from pathlib import Path
import fitz

OUT=Path(__file__).resolve().parent
BASE=OUT.parent.parent
manifest={r['paper_id']:r for r in csv.DictReader((BASE/'Coverage_Check/core_tag_alignment_2026-11-01/core_corpus_manifest.csv').open(encoding='utf-8-sig',newline=''))}
initial={r['paper_id']:r for name in 'ABC' for r in [json.loads(s) for s in (OUT/f'reviewer_{name}.jsonl').read_text(encoding='utf-8').splitlines() if s.strip()]}

def excerpt(pid,page,needle):
    p=BASE/manifest[pid]['pdf_path']
    with fitz.open(p) as doc:text=' '.join(doc[page-1].get_text().split())
    index=text.casefold().find(needle.casefold())
    assert index>=0,(pid,page,needle)
    start=max(0,index-55)
    while start<index and not text[start-1:start].isspace():start+=1
    return text[start:min(len(text),index+len(needle)+280)], f'{manifest[pid]["pdf_path"]}; PDF p.{page}'

reviews=[]
def add(pid,code=None,confidence=None,provisional=None,needs=None,reason=None,review_reason=None,page=None,needle=None,note_line=None):
    prior=initial[pid]
    r={'paper_id':pid,'decision_class':code or prior['decision_class'],'confidence':confidence or prior['confidence'],
       'provisional':prior['provisional'] if provisional is None else provisional,
       'needs_fulltext_review':prior['needs_fulltext_review'] if needs is None else needs,
       'rationale_zh':reason or prior['rationale_zh'],
       'controller_review_reason':review_reason or '主控对照本轮原文核查关键决策机制，保留该主标签。',
       'initial_reviewer_class':prior['decision_class']}
    if note_line:
        lines=(BASE/manifest[pid]['note_path']).read_text(encoding='utf-8-sig').splitlines()
        r.update(evidence_quote=lines[note_line-1],evidence_note_line=note_line)
    if page:
        q,loc=excerpt(pid,page,needle)
        r.update(source_basis='note_and_pdf',primary_source_excerpt=q,primary_source_locator=loc)
    reviews.append(r)

add('ASD-0006',confidence='high',provisional=False,needs=False,
    reason='本轮PDF明确多个LLM代理按论文分节承担检索与生成，各代理在专门提示和工具下工作；科学内容组织与报告决策由语言代理主导。旧笔记的未取全文状态不再代表本轮来源可用性。',
    review_reason='直接读取已归档且身份相符的PDF p.2与p.7，补强旧低证据笔记；仅更新增量结果，不改原笔记。',page=7,needle='deployment of multiple LLM agents')
add('ASD-0012',code='D5',confidence='high',provisional=False,needs=False,page=2,needle='Once the program has been verified',note_line=161,
    reason='LLM把实验要求转为结构化程序并修正，验证后的程序交给TAMP求安全可执行机器人动作；运动规划实现既定实验，不足以构成共同选择科研实验的第二主机制。',
    review_reason='第二审阅者核对PDF后建议收紧D6，主控按科研决策与执行规划边界采纳D5。')
add('ASD-0016',page=1,needle='optimized using an active-learning approach',
    reason='语言模型提供初始合成配方，失败反馈后的下一实验由热力学信息下的主动学习/ARROWS选择，主标签取实验优化控制机制。')
add('ASD-0037',confidence='high',page=3,needle='a set of heuristics designed by scientists',
    reason='专家设计的显式heuristics把MS/NMR表征判为pass/fail，并按规则触发推进、复现和多样化实验；规则推理主导而非单一目标数值优化。')
add('ASD-0036',code='D5',confidence='high',provisional=False,needs=False,page=7,needle='next buffer solution',note_line=149,
    reason='Organa.Reasoner依据结果提出下一缓冲液和高层实验方案，Planner对既定实验求并行执行和时序；实际科研实验选择由语言Reasoner主导。',
    review_reason='交叉审阅发现原D6混合了科研选择与运动/调度实现，按原文Reasoner决策归D5。')
add('ASD-0062',page=2,needle='both the modern notion of intelligent LLM agents',
    reason='ACADEMY是跨资源Agent中间件，可承载LLM和传统控制等异质应用，无唯一科研决策机制；依六类单标签要求暂按有状态工作流推进近似D2，保留低置信和复核。',
    review_reason='原文证明该论文横跨多种Agent实现；唯一标签只是一种论文层面近似，不能视为中间件内所有Agent都使用D2。')
add('ASD-0063',page=1,needle='combination of evolutionary computation and LLM-based code generation')
add('ASD-0065',code='D5',confidence='medium',provisional=False,needs=False,page=7,needle='evolutionary optimization',note_line=162,
    reason='认知模块的语言Agent讨论形成假设与实验方案，执行模块落实方案并返回反馈；原文泛称迭代/evolutionary优化，未明确独立搜索选择器与语言认知共同主导，按可识别认知机制取D5。',
    review_reason='交叉阅读完整方法后收紧D6，泛称优化或演化不足以确立第二主决策机制。')
add('ASD-0385',page=2,needle='Reinforcement learning (RL) has recently emerged')
add('ASD-0388',page=3,needle='real-time, probabilistic analysis',
    reason='XCA以概率晶相推断辅助研究者判断，暂在六类中取D3概率决策辅助；原文主要展示预测/分析，没有充分证明自主选择下一科研动作，保留低置信与复核。',
    review_reason='本轮PDF确认概率分析而非自主实验selector；不能把分类器直接写成完整实验优化控制器。')
add('ASD-0455',page=1,needle='driven by a batched Bayesian search algorithm')
add('ASD-0501',page=2,needle='logical inference mechanism of abduction')
add('ASD-0512',page=2,needle='evolutionary',review_reason='本轮PDF核对LLM候选生成与进化程序库搜索的共同作用，保留D6。')
add('ASD-0612',code='D3',confidence='high',provisional=False,needs=False,page=2,needle='five principles to select effective precursors',
    reason='前驱体对按热力学驱动力、目标相凸包深度和竞争相条件排序，实质是科学模型提供目标与约束的候选优化选择，而非状态—动作序列规划。',
    review_reason='交叉审阅与主控原文核对一致，将D2收敛为D3；模型作为优化目标来源并不自动等于规划型。')
add('ASD-0634',confidence='high',provisional=False,needs=False,page=2,needle='multiple LLM-powered agents',
    reason='领域科学家、数据分析和机器学习工程三个LLM代理交换建模建议与结果反馈，决定下一轮分析和实现；共享记忆和建模工具服务语言团队。')
add('ASD-0636',confidence='high',provisional=False,needs=False,page=4,needle='the student learns to reproduce two outputs',
    reason='结构解析、证据检索与教师代理提供证据化推理和审稿，蒸馏后的语言学生生成推理及评价；科研审稿判断仍由语言模型完成。')
add('ASD-0647',page=1,needle='reinforcement learning')
add('ASD-0648',page=1,needle='reinforcement learning')
add('ASD-0656',confidence='high',provisional=False,needs=False,page=2,needle='multi-stage, multi-tool, LLM-based review pipeline',
    reason='多阶段多工具LLM审稿流程分解核查任务、使用代码与搜索并形成评审判断；不是另一个独立优化器在选择科研行动。')
add('ASD-0662',confidence='medium',provisional=False,needs=False,page=10,needle='Each mutation is proposed by an LLM',
    reason='LLM根据执行和LLM-judge反馈修改工作流提示、节点与连边，单incumbent改善接受规则不构成独立优化提案机制，主导决策仍为LLM。',
    review_reason='直接核对PDF pp.9–10后采用D5；固定分数接受/回滚本身不足以支持D6。')
add('ASD-0696',page=8,needle='target',review_reason='本轮PDF核对目标特征评分与排序，保留D3，不采用旧Planning标签直接映射。')
add('ASD-0698',confidence='high',provisional=False,needs=False,page=5,needle='An LLM',
    reason='LLM Reviewer依据发现的评价rubric生成评分与修改反馈，LLM修订代理循环改写论文；目标得分用于检查修订，核心修改与判断由语言代理完成。')
add('ASD-0699',confidence='high',provisional=False,needs=False,page=5,needle='LLM-based agentic extraction pipeline',
    reason='LLM按阶段结构化查询从论文抽取复现组件与原句证据，构建工作流图并判断复现评分；图表示服务语言判断，不能单凭workflow graph归为符号机制。')
add('ASD-0736',confidence='high',provisional=False,needs=False,page=5,needle='fully-automated LLM agents',
    reason='文献、实现、顾问与写作语言代理串联科研创新过程，Advisor反馈和Code修订驱动后续研究行动；工具执行和评价支撑LLM团队。')
add('ASD-0738',confidence='medium',provisional=False,needs=False,page=17,needle='The system leverages a LLM as a proposal generator',
    reason='LLM理解代码与论文，生成、排序和实施改进idea，并根据反思选择下一方向；固定性能记录、Git回滚和成功阈值不单独构成另一决策机制。',
    review_reason='直接核对PDF pp.17–18，明确区别于独立种群/采集函数搜索；保留D5。')
add('ASD-0820',confidence='high',provisional=False,needs=False,page=4,needle='Qwen',
    reason='LLM提出可行反应候选，Qwen-3-4B语言模型加线性action head经GRPO训练后选择候选槽位；决策核心仍为语言模型，不能仅因RL训练或action head归非LLM策略。',
    review_reason='方法正文纠正了摘要易产生的独立非LLM-RL印象；两语言模型分工保留D5。')
add('ASD-0856',page=2,needle='MCTS procedure',review_reason='原文确认LLM产生假设与belief，独立MCTS以surprisal控制搜索分支，保留D6。')
add('ASD-0868',code='D5',confidence='high',provisional=False,needs=False,page=4,needle='single language model agent equipped with a suite of tools',
    reason='KeplerAgent由单一LLM依据经验日志逐步决定工具调用、修改函数库与约束，PySR/PySINDy是其配置的符号回归工具；现有证据支持LLM主导。',
    review_reason='交叉审阅及主控PDF p.4一致，D6改D5；配置一个数值搜索工具并不自动等于双机制共同主导。')
add('ASD-0874',page=2,needle='stochastic search with a better success predicate',
    reason='作者自己的RNA算子被描述为带更好成功判据的随机搜索，暂按D3；论文同时审计多个LLM及人工算子，无唯一系统，单标签仅为论文层面近似。',
    review_reason='直接读PDF pp.1–4确认作者主动描述为stochastic search；保留低置信与异质系统范围限制。')
add('ASD-0877',page=2,needle='MLEvolve',
    reason='论文评估ReAct、AIDE、MLEvolve等独立数据科学系统，LLM生成代码与建模是共同主干；D5仅概括共同机制，不能代表各系统搜索器完全相同。',
    review_reason='本轮PDF确认是多个系统的比较分析；按用户单标签要求保留低置信论文级概括。')
add('ASD-0900',confidence='high',page=4,needle='extract keywords',
    reason='LLM主要抽取用户基因/物种关键词，后续引物由保守区域、长度、GC/Tm与间隔等显式筛选组合规则选择，科研设计判断由规则主导。')
add('ASD-0919',confidence='high',page=1,needle='Large language model agents',
    reason='SciDisco语言Agent通过多轮分析、代码执行和验证反馈选择行动，DiscoPO是其训练方法；RL训练的语言决策者仍归D5。')
add('ASD-0967',code='D5',confidence='medium',provisional=True,needs=True,page=17,needle='The planner proposed architectural or workflow changes',
    reason='语言Scientist团队提出架构、工作流和分析方案，预设性能门槛决定接受/回滚；尚未见区别于普通门控的独立进化候选选择控制器，保守暂归D5并保留机制复核。',
    review_reason='交叉审阅有分歧。主控核对PDF pp.17–18，按与Mimosa相同边界：lineage命名、性能阈值及接受/回滚本身不足证明D6。',note_line=77)
add('ASD-1014',code='D2',confidence='low',provisional=True,needs=True,
    reason='现有笔记仅支持自动视野定位、细胞检测与诊断阶段推进，未证明学得的显微行为策略；在六类限制下暂按显式流程控制近似D2，需全文确认而非把监督预测器当D4。',
    review_reason='交叉审阅纠正预测模型与行动policy混淆，D4改D2暂定；无本轮直接全文证据。',note_line=77)
add('ASD-1048',confidence='medium',page=8,needle='The Optimization Agent employs PSO, SA, and g-RCWA',
    reason='LLM团队选择材料、结构布局、目标FOM和优化方案，独立PSO/SA/g-RCWA搜索具体器件结构参数；高层研究设计与对象逆设计优化共同控制，组间语言互评本身不是第二机制。',
    review_reason='保留D6并纠正依据：共同控制来自实质结构优化而非竞赛命名或终局FOM评测。',note_line=96)
add('ASD-1083',confidence='medium',page=7,needle='These priors guide the search',
    reason='以完整OptScientist Agent为编码对象：LLM理论代理选择变量、算子与先验并建议下一轮研究，OptDiscover独立按拟合与复杂度搜索符号结构；若仅看无LLM核心模型则是另一范围，不冒充全文所有模块都混合。',
    review_reason='限定full Agent范围后保留D6；core-model benchmark与完整Agent案例需区分，拟合对象模型不等于非LLM行动policy。',note_line=103)
add('ASD-1111',confidence='high',provisional=False,needs=False,page=2,needle='twin-delayed deep deterministic',
    reason='非LLM TD3 actor-critic控制策略学习量子态制备波形，训练后直接部署神经控制策略输出动作，属于学习策略型。')

with (OUT/'controller_review.jsonl').open('w',encoding='utf-8') as f:
    for r in reviews:f.write(json.dumps(r,ensure_ascii=False)+'\n')
print(json.dumps({'controller_reviews':len(reviews),'label_changes':[{ 'paper_id':r['paper_id'],'before':r['initial_reviewer_class'],'after':r['decision_class']} for r in reviews if r['decision_class']!=r['initial_reviewer_class']]},ensure_ascii=False))
