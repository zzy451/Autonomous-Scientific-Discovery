"""Scientific contribution rainclouds from the existing temporal-slice mock data.

This script changes no scores and invokes no LLM or evidence collection.
"""
from pathlib import Path
import csv
import hashlib
import json
import xml.etree.ElementTree as ET

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb, to_rgba
from matplotlib.font_manager import fontManager
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
import numpy as np
from scipy.stats import gaussian_kde

ROOT = Path(__file__).resolve().parent
OUTPUTS = ROOT / 'outputs'


def dump(name, value):
    (OUTPUTS / name).write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')


def reflected_kde(values, grid, bandwidth):
    """A shared absolute bandwidth; reflection keeps probability within 0–100."""
    spread = float(np.std(values, ddof=1))
    if spread <= 0:
        raise ValueError('The supplied fixed scenario has nonzero score variance in every domain.')
    kde = gaussian_kde(values, bw_method=bandwidth/spread)
    density = kde(grid)+kde(-grid)+kde(200-grid)
    density /= np.trapezoid(density, grid)
    return density


def draw():
    cfg = json.loads((ROOT / 'plot_config.json').read_text(encoding='utf-8'))
    data_path = ROOT / 'data' / 'temporal_slice_simulated_data.csv'
    OUTPUTS.mkdir(exist_ok=True)
    rows = list(csv.DictReader(data_path.open(encoding='utf-8-sig', newline='')))
    assert len(rows) == len({r['paper_id'] for r in rows}) == 1180
    assert all(str(r['synthetic']).lower() == 'true' for r in rows)
    assert all(0 <= float(r['score']) <= 100 for r in rows)
    domains = cfg['domains']
    assert len(domains) == 11
    groups = [np.array([float(r['score']) for r in rows if int(r['domain_index']) == i]) for i in range(11)]
    assert sum(map(len, groups)) == 1180
    for i, domain in enumerate(domains):
        assert len(groups[i]) == domain['n']
        assert {r['domain'] for r in rows if int(r['domain_index'])==i} == {domain['name']}

    available = {f.name for f in fontManager.ttflist}
    family = next((name for name in ['Arial','Liberation Sans','DejaVu Sans'] if name in available),'DejaVu Sans')
    plt.rcParams.update({'font.family':family, 'svg.fonttype':'none', 'axes.unicode_minus':False})
    fig = plt.figure(figsize=cfg['figure_size_inches'], dpi=120, facecolor='white')
    ax = fig.add_axes([.065,.23,.92,.60])
    ax.set_xlim(-.60,10.58)
    ax.set_ylim(0,100)
    ax.set_axisbelow(True)
    ax.set_yticks(np.arange(0,101,20))
    ax.yaxis.grid(True, color='#E5EBEF', linewidth=.70)
    ax.xaxis.grid(False)
    ax.spines[['top','right']].set_visible(False)
    for side in ['left','bottom']:
        ax.spines[side].set_color('#B7C5CE')
        ax.spines[side].set_linewidth(.75)
    ax.tick_params(axis='y',labelsize=11,colors='#5D7380',length=3,pad=7)
    ax.tick_params(axis='x',length=0,pad=16,labelsize=11,colors='#354F5F')
    ax.set_ylabel('Scientific Contribution Score',fontsize=13,color='#304C5D',labelpad=17)
    ax.set_xticks(range(11),[d['wrapped_label'] for d in domains])

    grid = np.linspace(0,100,1001)
    densities = [reflected_kde(v,grid,cfg['kde_bandwidth_score_units']) for v in groups]
    common_peak = max(float(p.max()) for p in densities)
    density_scale = cfg['maximum_cloud_width']/common_peak
    rng = np.random.default_rng(cfg['jitter_seed'])
    summaries, positions = [], []
    point_count = 0
    for i,(domain,values,density) in enumerate(zip(domains,groups,densities)):
        color = domain['color']
        dark = tuple(np.array(to_rgb(color))*.76)
        cloud_start = i+.085
        cloud_edge = cloud_start+density*density_scale
        ax.fill_betweenx(grid,cloud_start,cloud_edge,
                         facecolor=to_rgba(color,.17),edgecolor='none',zorder=1)
        ax.plot(cloud_edge,grid,color=to_rgba(color,.58),linewidth=1.25,zorder=2)

        x = i+rng.uniform(-.40,-.145,len(values))
        ax.scatter(x,values,s=cfg['point_area_pt2'],c=color,alpha=cfg['point_alpha'],
                   edgecolors='white',linewidths=.28,zorder=4)
        point_count += len(values)
        records = [r for r in rows if int(r['domain_index'])==i]
        positions.extend(dict(paper_id=r['paper_id'],domain=domain['name'],domain_index=i,
                              score=float(v),plot_x=float(xx)) for r,v,xx in zip(records,values,x))

        box = ax.boxplot([values],positions=[i-.025],widths=.13,orientation='vertical',
            whis=1.5,showfliers=False,showmeans=False,patch_artist=True,
            manage_ticks=False,zorder=5,
            boxprops={'facecolor':to_rgba(color,.27),'edgecolor':dark,'linewidth':1.2},
            whiskerprops={'color':dark,'linewidth':1.05},
            capprops={'color':dark,'linewidth':1.05},
            medianprops={'color':dark,'linewidth':2.0})
        ax.text(i,1.034,f'n = {len(values)}',transform=ax.get_xaxis_transform(),
                ha='center',va='bottom',fontsize=11,color='#506A79')

        q1,median,q3 = np.percentile(values,[25,50,75])
        iqr = q3-q1
        inside = values[(values>=q1-1.5*iqr)&(values<=q3+1.5*iqr)]
        summaries.append(dict(domain=domain['name'],color_hex=color,n=len(values),
            mean=float(np.mean(values)),median=float(median),q1=float(q1),q3=float(q3),
            iqr=float(iqr),standard_deviation=float(np.std(values,ddof=1)),
            minimum=float(values.min()),maximum=float(values.max()),
            lower_whisker=float(inside.min()),upper_whisker=float(inside.max())))
    assert point_count == 1180

    fig.text(.065,.957,'Scientific Contribution Distribution',fontsize=25,fontweight='bold',
             color='#213E50',ha='left',va='top')
    fig.text(.065,.905,'Same 1,180 simulated papers as the temporal-slice figure | Pooled across all five periods',
             fontsize=11.5,color='#6D818D',ha='left',va='top')
    fig.text(.985,.95,'11 DOMAINS',fontsize=10.5,color='#8A9AA3',ha='right',va='top')
    legend_handles = [
        Line2D([],[],marker='o',linestyle='none',markerfacecolor='#6A8291',
               markeredgecolor='white',markersize=6,label='Individual paper'),
        Patch(facecolor='#CDD8DF',edgecolor='#647C8C',label='Median and interquartile range'),
        Patch(facecolor='#E3EBEF',edgecolor='#91A4B0',label='Within-domain score density'),
    ]
    fig.legend(handles=legend_handles,loc='lower center',bbox_to_anchor=(.52,.073),
               ncol=3,frameon=False,fontsize=10.5,labelcolor='#536D7B',handlelength=1.6,
               columnspacing=3.5,handletextpad=.8)
    fig.text(.52,.041,'Whiskers: 1.5 × interquartile range. Density curves use a shared width scale; sample sizes are shown above.',
             fontsize=9,color='#83949E',ha='center',va='center')
    fig.text(.52,.020,'SIMULATED DATA — descriptive visualization only.',
             fontsize=9,color='#9C7968',ha='center',va='center')

    with (OUTPUTS/'domain_score_summary.csv').open('w',encoding='utf-8-sig',newline='') as fp:
        writer=csv.DictWriter(fp,fieldnames=list(summaries[0]))
        writer.writeheader();writer.writerows(summaries)
    with (OUTPUTS/'plotted_point_positions.csv').open('w',encoding='utf-8-sig',newline='') as fp:
        writer=csv.DictWriter(fp,fieldnames=list(positions[0]))
        writer.writeheader();writer.writerows(positions)

    fig.canvas.draw()
    renderer=fig.canvas.get_renderer()
    texts=list(ax.texts)+list(fig.texts)+list(ax.get_xticklabels())+list(ax.get_yticklabels())+[ax.yaxis.label]
    texts += list(fig.legends[0].get_texts())
    boxes=[t.get_window_extent(renderer) for t in texts]
    outside=[t.get_text() for t,b in zip(texts,boxes)
             if b.x0<0 or b.y0<0 or b.x1>fig.bbox.width or b.y1>fig.bbox.height]
    collisions=[]
    for i,(a,ba) in enumerate(zip(texts,boxes)):
        for bb,b in zip(boxes[i+1:],texts[i+1:]):
            if ba.overlaps(bb):collisions.append([a.get_text(),b.get_text()])
    assert not outside,outside
    assert not collisions,collisions

    stem=OUTPUTS/'Scientific_Contribution_Raincloud_EN'
    fig.savefig(stem.with_suffix('.png'),dpi=cfg['dpi'],facecolor='white')
    fig.savefig(stem.with_suffix('.svg'),facecolor='white')
    fig.savefig(OUTPUTS/'Scientific_Contribution_Raincloud_EN_preview.png',dpi=cfg['preview_dpi'],facecolor='white')
    plt.close(fig)
    ns={'s':'http://www.w3.org/2000/svg'}
    tree=ET.parse(stem.with_suffix('.svg'))
    text=''.join(''.join(e.itertext()) for e in tree.findall('.//s:text',ns))
    assert not any('\u4e00'<=c<='\u9fff' for c in text)
    qa=dict(passed=True,synthetic=True,n_unique_papers=len(rows),n_points_plotted=point_count,
            domain_counts=[dict(name=d['name'],n=len(v),color=d['color']) for d,v in zip(domains,groups)],
            all_figure_text_english=True,labels_outside_canvas=outside,text_overlap_candidates=collisions,
            score_limits=[0,100],kde_bandwidth_score_units=cfg['kde_bandwidth_score_units'],
            density_definition='Reflected Gaussian KDE normalized to unit probability on 0–100, using one shared width scale across domains.',
            jitter_changes='Horizontal position only; no score or group change.',
            source_data_sha256=hashlib.sha256(data_path.read_bytes()).hexdigest())
    dump('render_checks.json',qa)
    print(json.dumps({'passed':True,'n_points':point_count,'domains':11,'counts':[len(v) for v in groups]}))


if __name__=='__main__':
    draw()
