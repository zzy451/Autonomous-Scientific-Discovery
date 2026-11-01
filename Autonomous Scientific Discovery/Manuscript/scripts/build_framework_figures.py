"""Render bilingual vector figures for the conceptual framework; no inferred counts."""
from pathlib import Path
import argparse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib import font_manager

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--chinese-output', type=Path, help='Optional Chinese manuscript directory.')
args = parser.parse_args()
zhroot = args.chinese_output
languages = ['en', 'zh'] if zhroot is not None else ['en']
for out in [root / 'figures'] + ([zhroot / 'figures'] if zhroot is not None else []):
    out.mkdir(parents=True, exist_ok=True)

blue, teal, orange = '#20445C', '#147D82', '#AF642A'
light, ink = '#EFF4F7', '#20333E'


def canvas(height, lang):
    plt.rcParams.update({'font.family': 'Microsoft YaHei' if lang == 'zh' else 'DejaVu Sans',
                         'font.size': 11, 'pdf.fonttype': 42, 'axes.unicode_minus': False})
    fig, ax = plt.subplots(figsize=(11.8, height))
    ax.set(xlim=(0, 12), ylim=(0, height))
    ax.axis('off')
    fig.subplots_adjust(left=.015, right=.985, top=.98, bottom=.02)
    return fig, ax


def box(ax, x, y, w, h, text, fc=light, color=blue, size=11):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.07,rounding_size=0.12',
                               linewidth=1.1, facecolor=fc, edgecolor=color))
    ax.text(x + w/2, y + h/2, text, va='center', ha='center', fontsize=size, color=ink,
            linespacing=1.5)


def arrow(ax, a, b, color=teal, style='-|>', curve=0):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle=style, mutation_scale=12,
                                linewidth=1.3, color=color,
                                connectionstyle=f'arc3,rad={curve}'))


def save(fig, stem, lang):
    out = (zhroot if lang == 'zh' else root) / 'figures' / f'{stem}_{lang}.pdf'
    fig.savefig(out, facecolor='white')
    plt.close(fig)
    print(out.name)


for lang in languages:
    zh = lang == 'zh'
    fig, ax = canvas(6.0, lang)
    ax.text(.2, 5.65, '研究对象、行动与证据' if zh else 'SCIENTIFIC OBJECTS, ACTIONS, AND EVIDENCE',
            weight='bold', fontsize=15, color=blue)
    box(ax, .25, 3.85, 3.35, 1.2,
        '领域与科学对象\n任务研究什么' if zh else 'Domain and scientific object\nWhat is investigated?')
    box(ax, 4.25, 3.85, 3.35, 1.2,
        '科研工作流角色\n执行哪些科研活动' if zh else 'Research workflow roles\nWhat activities are undertaken?')
    box(ax, 8.25, 3.85, 3.35, 1.2,
        '决策范式\n如何选择和协调行动' if zh else 'Decision paradigms\nHow are actions selected?')
    arrow(ax, (3.65, 4.45), (4.15, 4.45))
    arrow(ax, (7.65, 4.45), (8.15, 4.45))
    box(ax, .25, 2.02, 5.35, 1.05,
        '执行环境与组织方式\n工具、仪器、模拟、人类与智能体' if zh else
        'Environment and organization\nTools, instruments, simulations, people, agents', color=teal)
    box(ax, 6.25, 2.02, 5.35, 1.05,
        '自主性与责任分配\n目标、授权、恢复、解释与接受' if zh else
        'Autonomy and responsibilities\nGoals, authorization, recovery, interpretation', color=teal)
    for x in [1.9, 5.9, 9.9]:
        arrow(ax, (x, 3.7), (x if x != 5.9 else 3.0, 3.2))
    box(ax, .25, .25, 11.35, 1.0,
        '证据约束结论范围：操作成功、任务正确性与科学验证；科学发现还需新颖性依据' if zh else
        'Evidence constrains claims: execution, task correctness, scientific validation;\ndiscovery additionally requires substantiated novelty',
        fc='#FCF4EA', color=orange, size=11)
    arrow(ax, (3, 1.87), (3, 1.4), orange)
    arrow(ax, (9, 1.87), (9, 1.4), orange)
    save(fig, 'conceptual_framework', lang)

    fig, ax = canvas(6.0, lang)
    ax.text(.2, 5.65, '科研角色、反馈与决策责任' if zh else 'RESEARCH ROLES, FEEDBACK, AND RESPONSIBILITY',
            weight='bold', fontsize=15, color=blue)
    labels = (['知识获取', '问题与假设生成', '研究规划与设计', '实验与执行', '数据分析与解释', '验证与传播'] if zh else
              ['Knowledge\nacquisition', 'Question and\nhypothesis generation', 'Research planning\nand design',
               'Experimentation\nand execution', 'Data analysis\nand interpretation', 'Validation and\ncommunication'])
    positions = [(0.35, 3.7), (4.35, 3.7), (8.35, 3.7), (8.35, 1.7), (4.35, 1.7), (.35, 1.7)]
    for (x, y), label in zip(positions, labels):
        box(ax, x, y, 3.15, 1.0, label)
    for i in range(5):
        x, y = positions[i]; u, v = positions[i+1]
        a = (x+3.25, y+.5) if u>x else ((x-.1, y+.5) if u<x else (x+1.575, y-.1))
        b = (u-.1, v+.5) if u>x else ((u+3.25, v+.5) if u<x else (u+1.575, v+1.1))
        arrow(ax, a, b)
    arrow(ax, (1.9, 2.8), (5.9, 3.55), orange, curve=-.3)
    ax.text(4.2, 3.05, '证据驱动修正' if zh else 'Evidence-driven revision', color=orange, fontsize=10)
    box(ax, .35, .15, 11.15, .8,
        '各阶段记录：决策者、预设约束、人工干预与验证依据' if zh else
        'At each stage: decision owner, predefined constraints, human intervention, and validation',
        fc='#FCF4EA', color=orange, size=10)
    save(fig, 'research_workflow', lang)

    fig, ax = canvas(6.8, lang)
    ax.text(.2, 6.4, '互补范式的代表性历史锚点' if zh else 'SELECTED HISTORICAL ANCHORS OF COMPLEMENTARY PARADIGMS',
            weight='bold', fontsize=14, color=blue)
    ax.text(.2, 5.98, '按案例时间排列，不代表范式起源或替代关系' if zh else
            'Ordered by selected examples; dates do not establish origins or replacement.', color=ink, fontsize=10)
    rows = [
        ('2004', '符号与知识表示；模型规划' if zh else 'Symbolic knowledge; model-based planning',
         'Robot Scientist; Sciencecraft'),
        ('2018–2021', '学习驱动的反应选择' if zh else 'Learned selection of chemical experiments',
         'Granda et al.; Caramelli et al.'),
        ('2020', '概率优化与机器人实验' if zh else 'Probabilistic search and robotic experimentation',
         'Mobile robotic chemist; BEAR'),
        ('2023–2026', '语言模型与专业工具' if zh else 'Language models and specialized tools',
         'Coscientist; ChemCrow; Agent Laboratory'),
        ('2024–2026', '状态机整合与学习策略' if zh else 'State-machine integration; learned policies',
         'k-agents; RAVA'),
    ]
    for i, (date, mechanism, example) in enumerate(rows):
        y = 4.9-i*1.04
        box(ax, .3, y, 1.7, .72, date, fc='#E5F1F2', color=teal, size=11)
        ax.text(2.4, y+.51, mechanism, fontsize=11, weight='bold', color=blue)
        ax.text(2.4, y+.15, example, fontsize=10, color=ink)
    ax.text(.3, .12, '后续研究继续使用早期机制，并可与新组件结合。' if zh else
            'Earlier mechanisms remain applicable and can be coupled with newer components.', fontsize=10, color=teal)
    save(fig, 'historical_paradigms', lang)
