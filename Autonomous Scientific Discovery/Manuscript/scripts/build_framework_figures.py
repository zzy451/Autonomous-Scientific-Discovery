"""Render bilingual vector figures for the conceptual framework; no inferred counts."""
from pathlib import Path
import argparse
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

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
bibliography = (root / 'references.bib').read_text(encoding='utf-8')


def reference_year(key):
    entry = re.search(r'(?ms)^@\w+\{' + re.escape(key) + r',\s*\n(.*?)(?=^@|\Z)', bibliography)
    if not entry:
        raise ValueError(f'Missing historical reference: {key}')
    year = re.search(r'\byear\s*=\s*\{(\d{4})\}', entry[1])
    if not year:
        raise ValueError(f'Missing historical reference year: {key}')
    return int(year[1])


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
    box(ax, .25, 2.02, 5.35, 1.05,
        '执行环境与组织方式\n工具、仪器、模拟、人类与智能体' if zh else
        'Environment and organization\nTools, instruments, simulations, people, agents', color=teal)
    box(ax, 6.25, 2.02, 5.35, 1.05,
        '自主性与责任分配\n目标、授权、恢复、解释与接受' if zh else
        'Autonomy and responsibilities\nGoals, authorization, recovery, interpretation, acceptance', color=teal, size=10)
    ax.text(6, 3.4, '并列维度共同描述同一对象—任务案例' if zh else
            'Complementary dimensions describing the same object-task case',
            ha='center', fontsize=10, color=teal)
    ax.text(6, 1.6, '各项判断均须与所支持的科学主张对应' if zh else
            'Each assessment is interpreted against the scientific claim it supports',
            ha='center', fontsize=10, color=orange)
    box(ax, .25, .25, 11.35, 1.0,
        '证据约束结论范围：操作成功、任务正确性与科学验证；科学发现还需新颖性依据' if zh else
        'Evidence constrains claims: execution, task correctness, scientific validation;\ndiscovery additionally requires substantiated novelty',
        fc='#FCF4EA', color=orange, size=11)
    save(fig, 'conceptual_framework', lang)

    fig, ax = canvas(6.0, lang)
    ax.text(.2, 5.65, '科研角色、反馈与决策责任' if zh else 'RESEARCH ROLES, FEEDBACK, AND RESPONSIBILITY',
            weight='bold', fontsize=15, color=blue)
    ax.text(.2, 5.18, '橙色反馈：依据证据修订问题、设计、测量或解释' if zh else
            'Orange feedback: revise questions, designs, measurements, or interpretation in light of evidence',
            color=orange, fontsize=10)
    labels = (['知识获取', '问题与假设生成', '研究规划与设计', '实验与执行', '数据分析与解释', '验证与传播'] if zh else
              ['Knowledge\nacquisition', 'Question and\nhypothesis generation', 'Research planning\nand design',
               'Experimentation\nand execution', 'Data analysis\nand interpretation', 'Validation and\ncommunication'])
    positions = [(0.35, 3.7), (4.35, 3.7), (8.35, 3.7), (8.35, 1.7), (4.35, 1.7), (.35, 1.7)]
    for (x, y), label in zip(positions, labels):
        box(ax, x, y, 3.15, 1.0, label)
    for i in range(5):
        x, y = positions[i]; u, v = positions[i+1]
        if i == 2:
            # Route the forward execution link outside the orange revision paths.
            ax.plot([11.6, 11.85, 11.85], [y+.5, y+.5, v+.5], color=teal, linewidth=1.3)
            arrow(ax, (11.85, v+.5), (11.6, v+.5))
            continue
        a = (x+3.25, y+.5) if u>x else ((x-.1, y+.5) if u<x else (x+1.575, y-.1))
        b = (u-.1, v+.5) if u>x else ((u+3.25, v+.5) if u<x else (u+1.575, v+1.1))
        arrow(ax, a, b)
    # Validation can redirect four distinct roles, without crossing their boxes.
    ax.plot([1.925, 1.925, 9.925], [2.8, 3.2, 3.2], color=orange, linewidth=1.3)
    for x in [5.925, 9.925]:
        arrow(ax, (x, 3.2), (x, 3.6), orange)
        arrow(ax, (x, 3.2), (x, 2.8), orange)
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
        ('符号与知识表示；模型规划' if zh else 'Symbolic knowledge; model-based planning',
         [('Robot Scientist', 'king2004'), ('Sciencecraft', 'asd0645')]),
        ('学习驱动的反应选择' if zh else 'Learned selection of chemical experiments',
         [('Granda et al.', 'asd0734'), ('Caramelli et al.', 'asd0428')]),
        ('概率优化与机器人实验' if zh else 'Probabilistic search and robotic experimentation',
         [('Mobile robotic chemist', 'burger2020'), ('BEAR', 'asd0504')]),
        ('语言模型与专业工具' if zh else 'Language models and specialized tools',
         [('Coscientist', 'boiko2023'), ('ChemCrow', 'bran2024'), ('Agent Laboratory', 'asd0018')]),
        ('状态机整合与学习策略' if zh else 'State-machine integration; learned policies',
         [('k-agents', 'asd0090'), ('RAVA', 'asd1133')]),
    ]
    for i, (mechanism, examples) in enumerate(rows):
        years = [reference_year(key) for _, key in examples]
        date = str(min(years)) if min(years) == max(years) else f'{min(years)}–{max(years)}'
        example = '; '.join(f'{name} ({year})' for (name, _), year in zip(examples, years))
        y = 4.9-i*1.04
        box(ax, .3, y, 1.7, .72, date, fc='#E5F1F2', color=teal, size=11)
        ax.text(2.4, y+.51, mechanism, fontsize=11, weight='bold', color=blue)
        ax.text(2.4, y+.15, example, fontsize=10, color=ink)
    ax.text(.3, .12, '后续研究继续使用早期机制，并可与新组件结合。' if zh else
            'Earlier mechanisms remain applicable and can be coupled with newer components.', fontsize=10, color=teal)
    save(fig, 'historical_paradigms', lang)
