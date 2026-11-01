"""Render reproducible domain and case figures from explicit source records."""
from pathlib import Path
import argparse
from collections import Counter
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.colors import ListedColormap

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--chinese-output', type=Path, help='Optional Chinese manuscript directory.')
args = parser.parse_args()
zhroot = args.chinese_output
# Reproduce the manuscript's dated corpus independently of later library audits.
snapshot = json.loads((root/'data/core_classification_snapshot_2026-11-01.json').read_text(encoding='utf-8-sig'))
records = json.loads((root/'data/corpus_landscape_records_2026-11-01.json').read_text(encoding='utf-8-sig'))['records']
core = [r for r in records if r.get('active_confirmed_core')]
profiles = json.loads((root/'data/illustrative_domain_profiles.json').read_text(encoding='utf-8'))
assert len(core) == snapshot['core_papers'] == 662
counts = Counter(m for r in core for m in r.get('scientific_object_modules', []))
assert all(counts[m['module']] == m['papers'] for m in snapshot['modules'])
years = Counter(str(r['year']) for r in core)
assert all(y.isdigit() for y in years)
source_summary = {'unique_core_works':len(core), 'memberships':sum(counts.values()),
                  'coverage_counts':dict(sorted(counts.items())), 'bibliographic_years':dict(sorted(years.items())),
                  'case_count':len(profiles['cases']), 'case_scope':profiles['scope']}
(root/'data/landscape_source_summary.json').write_text(json.dumps(source_summary,indent=2),encoding='utf-8')
blue, teal, orange, ink = '#20445C', '#147D82', '#AF642A', '#20333E'

for lang in (['en','zh'] if zhroot is not None else ['en']):
    zh = lang == 'zh'
    plt.rcParams.update({'font.family':'Microsoft YaHei' if zh else 'DejaVu Sans','font.size':10,'pdf.fonttype':42,'axes.unicode_minus':False})
    out = (zhroot if zh else root)/'figures'
    out.mkdir(parents=True, exist_ok=True)
    fig, axs = plt.subplots(1,2,figsize=(12,5.6),gridspec_kw={'width_ratios':[1.35,1]})
    modules = snapshot['modules']
    names = (['形式与计算','物理与天文','化学','材料','地球与环境','生命','医学与健康','农业与食品等','工程与工业','航天海洋交通','社会与知识系统'] if zh else
             ['Formal / computational','Physics / astronomy','Chemistry','Materials','Earth / environment','Life sciences','Medical / health','Agriculture / food, etc.','Engineering / industrial','Aerospace / marine / transport','Social / knowledge systems'])
    vals=[m['papers'] for m in modules]
    axs[0].barh(range(11),vals,color=[orange if i==7 else teal for i in range(11)],height=.65)
    axs[0].set_yticks(range(11),[f'{i+1:02d}  {n}' for i,n in enumerate(names)])
    axs[0].invert_yaxis();axs[0].set_xlim(0,192)
    axs[0].set_xlabel('非互斥领域归属数' if zh else 'Non-exclusive domain memberships')
    axs[0].set_title('A  学科覆盖' if zh else 'A  Domain coverage',loc='left',weight='bold',color=blue)
    for i,v in enumerate(vals):axs[0].text(v+2,i,str(v),va='center',fontsize=9)
    ordered=sorted(years,key=int)
    axs[1].bar(range(len(ordered)),[years[y] for y in ordered],color=[orange if y=='2026' else blue for y in ordered])
    ticks=[i for i,y in enumerate(ordered) if y in ['2004','2010','2015','2020','2023','2026']]
    axs[1].set_xticks(ticks,[ordered[i]+('*' if ordered[i]=='2026' else '') for i in ticks],rotation=45,ha='right')
    axs[1].set_title('B  文献记录年份' if zh else 'B  Recorded publication years',loc='left',weight='bold',color=blue)
    axs[1].set_ylabel('去重核心工作数' if zh else 'Unique core works')
    for ax in axs:
        for sp in ['top','right']:ax.spines[sp].set_visible(False)
        ax.grid(axis='x' if ax==axs[0] else 'y',alpha=.15);ax.set_axisbelow(True)
    fig.text(.5,.025,'*2026 为不完整年度；数量反映收集构成，不估计全球研究规模。' if zh else
             '*2026 is incomplete. Counts describe collection composition, not worldwide research prevalence.',ha='center',fontsize=9,color=ink)
    fig.subplots_adjust(left=.22,right=.98,top=.9,bottom=.19,wspace=.35)
    fig.savefig(out/f'domain_landscape_{lang}.pdf');plt.close(fig)

    cases=profiles['cases'];roles=profiles['role_order'];paradigms=profiles['paradigm_order']
    matrix=np.zeros((len(cases),12))
    for i,c in enumerate(cases):
        for j,role in enumerate(roles):matrix[i,j]=int(role in c['roles'])
        for j,p in enumerate(paradigms):matrix[i,j+6]=int(p in c['paradigms'])*2
    cols=(['知识','假设','设计','执行','分析','验证','符号','规划','优化','学习','LLM','混合'] if zh else
          ['Knowledge','Hypothesis','Design','Execution','Analysis','Validation','Symbolic','Planning','Optimization','Learning','LLM','Hybrid'])
    fig,ax=plt.subplots(figsize=(12,6.5))
    ax.imshow(matrix,aspect='auto',cmap=ListedColormap(['#F0F3F5',teal,blue]),vmin=0,vmax=2)
    ax.set_yticks(range(len(cases)),[c['module']+'  '+c['name'] for c in cases],fontsize=10)
    ax.set_xticks(range(12),cols,rotation=45,ha='right',fontsize=9)
    ax.set_xticks(np.arange(-.5,12,1),minor=True);ax.set_yticks(np.arange(-.5,len(cases),1),minor=True)
    ax.grid(which='minor',color='white',linewidth=2);ax.tick_params(which='minor',bottom=False,left=False)
    ax.axvline(5.5,color=orange,linewidth=2)
    for i in range(len(cases)):
        for j in range(12):
            if matrix[i,j]:ax.text(j,i,'●',ha='center',va='center',color='white',fontsize=9)
    ax.text(2.5,-1.3,'所选科研角色' if zh else 'Selected research roles',ha='center',weight='bold',color=teal)
    ax.text(8.5,-1.3,'所选决策机制' if zh else 'Selected decision mechanisms',ha='center',weight='bold',color=blue)
    for sp in ax.spines.values():sp.set_visible(False)
    fig.text(.5,.025,'标记表示已编码；空白不表示能力不存在。案例选择不用于估计全库比例。' if zh else
             'Marked = coded for the illustrated task. Unmarked = not coded, not absent. Selection is not a prevalence estimate.',ha='center',fontsize=9,color=ink)
    fig.subplots_adjust(left=.27,right=.98,top=.88,bottom=.21)
    fig.savefig(out/f'domain_workflow_paradigm_{lang}.pdf');plt.close(fig)

    fig,ax=plt.subplots(figsize=(12,6));ax.set(xlim=(0,12),ylim=(0,6));ax.axis('off')
    fig.subplots_adjust(left=.015,right=.985,top=.98,bottom=.02)
    def box(x,y,w,h,text,fc='#EFF4F7',ec=blue):
        ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.06,rounding_size=.10',facecolor=fc,edgecolor=ec,linewidth=1.2))
        ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=11,color=ink,linespacing=1.5)
    def arrow(a,b):ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=12,color=teal,linewidth=1.3))
    ax.text(.25,5.65,'未来科学智能体的研究组织' if zh else 'A RESEARCH ECOSYSTEM FOR SCIENTIFIC AGENTS',weight='bold',fontsize=15,color=blue)
    box(.3,3.9,3.1,1.05,'人类与科学目标\n意义、约束、责任' if zh else 'People and scientific goals\nSignificance, constraints, responsibility')
    box(4.4,3.9,3.1,1.05,'互补决策机制\n语言、规划、优化、控制' if zh else 'Complementary mechanisms\nLanguage, planning, search, control')
    box(8.5,3.9,3.1,1.05,'研究环境\n代码、实验室、现场、任务' if zh else 'Research environments\nCode, laboratories, fields, missions')
    arrow((3.5,4.42),(4.25,4.42));arrow((7.6,4.42),(8.35,4.42))
    box(.3,2.0,5.0,1.05,'科学记忆与可追溯记录\n样品、工具版本、失败与决策轨迹' if zh else 'Scientific memory and provenance\nSamples, tool versions, failures, decision traces',ec=teal)
    box(6.6,2.0,5.0,1.05,'独立与对象特定的验证\n任务检查、测量、复现与外部评价' if zh else 'Independent and object-specific validation\nTask checks, measurements, replication, external tests',ec=teal)
    arrow((10.05,3.75),(9.1,3.2));arrow((6.45,2.52),(5.45,2.52));arrow((2.8,3.2),(1.85,3.75))
    box(.3,.25,11.3,.92,'可积累的科学知识：带有证据、适用范围和可修订解释的结果' if zh else
        'Cumulative scientific knowledge: results with evidence, applicability conditions, and revisable explanations',fc='#FCF4EA',ec=orange)
    arrow((2.8,1.85),(2.8,1.32));arrow((9.1,1.85),(9.1,1.32))
    fig.savefig(out/f'future_ecosystem_{lang}.pdf');plt.close(fig)
    print(lang,'landscape, case matrix, future ecosystem')
