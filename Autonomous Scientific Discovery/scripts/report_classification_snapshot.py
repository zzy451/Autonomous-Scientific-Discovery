"""Report primary filing and non-exclusive module taxonomy separately."""
import collections
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'Coverage_Check'

def read_jsonl(path):
    return [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines() if line.strip()]

def main():
    papers = {p['paper_id']: p for p in read_jsonl(ROOT / 'Data/papers.jsonl') if p['active_confirmed_core']}
    mappings = read_jsonl(ROOT / 'Data/paper_module_taxonomy_assignments.jsonl')
    formal = [p for p in papers.values() if p['general_method_bucket'] == 'none']
    resolved = [p for p in formal if p['legacy_tertiary_class'] and p['legacy_tertiary_class'].startswith(p['legacy_secondary_class'] + '.') and p['legacy_tertiary_class'][:2] == p['primary_module_for_filing']]
    stats = dict(snapshot_date='2026-10-29', core_papers=len(papers), formal_domain_papers=len(formal), general_method_papers=len(papers)-len(formal), primary_tertiary_resolved=len(resolved), primary_tertiary_pending=len(formal)-len(resolved), legacy_tertiary_blank=sum(not p['legacy_tertiary_class'] for p in papers.values()), multi_module_papers=sum(len(p['scientific_object_modules'])>1 for p in papers.values()), module_pairs=len(mappings), module_pairs_with_tertiary=sum(bool(m['tertiary_taxonomy_code']) for m in mappings), pending_module_pairs=sum(m['assignment_status']=='pending_mapping' for m in mappings), local_core_pdfs=sum(p['pdf_exists'] for p in papers.values()))
    assert {(m['paper_id'],m['module_context']) for m in mappings} == {(p['paper_id'],mod) for p in papers.values() for mod in p['scientific_object_modules']}
    stats['module_pairs_without_tertiary']=len(mappings)-stats['module_pairs_with_tertiary']
    rows=[]
    for mod in [f'{i:02}' for i in range(1,12)]:
        ms=[m for m in mappings if m['module_context']==mod]
        rows.append(dict(module=mod, papers=sum(mod in p['scientific_object_modules'] for p in papers.values()),primary_filings=sum(p['primary_module_for_filing']==mod for p in formal),primary_tertiary_resolved=sum(p['primary_module_for_filing']==mod for p in resolved),module_tertiary_resolved=sum(bool(m['tertiary_taxonomy_code']) for m in ms),module_tertiary_pending=sum(not m['tertiary_taxonomy_code'] for m in ms)))
    stats['modules']=rows
    OUT.mkdir(exist_ok=True)
    (OUT/'core_classification_snapshot_2026-10-29.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    text='# 核心库分类快照（2026-10-29）\n\n'
    text+=f"核心库 **{len(papers)} 篇**；正式科学领域 {len(formal)} 篇；独立通用方法桶 {stats['general_method_papers']} 篇。正式领域主归档已有三级 {len(resolved)} 篇，待核 {stats['primary_tertiary_pending']} 篇；旧三级字段空值 {stats['legacy_tertiary_blank']} 篇。通用方法桶管理编号不计正式科学三级。\n\n"
    text+=f"多模块论文 {stats['multi_module_papers']} 篇，共 {len(mappings)} 个论文—模块映射；其中 {stats['module_pairs_with_tertiary']} 个已有三级，{stats['module_pairs_without_tertiary']} 个仍缺三级（含 {stats['pending_module_pairs']} 个内部位置尚未确定）。主归档填满并不意味着所有附加模块都已细分完成。\n\n"
    text+='| 模块 | 非互斥覆盖论文 | 主归档论文 | 主归档已有三级 | 模块映射已有三级 | 模块映射缺三级 |\n|---|---:|---:|---:|---:|---:|\n'
    for r in rows:text+='| '+' | '.join(map(str,r.values()))+' |\n'
    text+='\n## 二级与三级明细\n\n以下计数来自模块账本，同一论文可在不同模块出现；同一模块暂存一个代表三级。未决行不拆作零篇。\n\n| 模块 | 层级 | 分类代码 | 论文数 |\n|---|---|---|---:|\n'
    detail=[]
    for field,level in [('secondary_taxonomy_code','二级'),('tertiary_taxonomy_code','三级')]:
        for (mod,code),n in sorted(collections.Counter((m['module_context'],m[field] or '待定') for m in mappings).items()):
            detail.append(dict(module=mod,level=level,code=code,papers=n));text+=f'| {mod} | {level} | {code} | {n} |\n'
    (OUT/'core_classification_snapshot_2026-10-29.md').write_text(text,encoding='utf-8')
    with (OUT/'core_classification_counts_2026-10-29.csv').open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['module','level','code','papers']);w.writeheader();w.writerows(detail)
    print(json.dumps(stats,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
