"""Prepare read-only evidence packets; all outputs stay in this new directory."""
from __future__ import annotations
import csv
import hashlib
import json
import re
from pathlib import Path

OUT = Path(__file__).resolve().parent
BASE = OUT.parent.parent
SNAPSHOT = BASE / 'Coverage_Check/core_tag_alignment_2026-11-01'

def dump(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding='utf-8')

def read_csv(path):
    return list(csv.DictReader(path.open(encoding='utf-8-sig', newline='')))

def selected_lines(text):
    lines = text.splitlines()
    ranked = []
    in_method = False
    terms = re.compile(r'LLM|GPT|language model|语言模型|贝叶斯|Bayesian|acquisition|采集函数|优化|optimization|optimisation|强化学习|reinforcement|policy|策略|规划|planning|符号|symbolic|逻辑|logic|knowledge graph|知识图谱|MCTS|evolution|进化|active learning|主动学习|决策|reasoning|推理|选择下一|选择实验|action|行动|闭环', re.I)
    for i, line in enumerate(lines, 1):
        if line.startswith('## '):
            in_method = bool(re.search(r'Agent 系统|方法设计|系统设计|核心方法|方法与|技术路线|Agent.*流程|方法机制|Evidence Log|核心机制', line, re.I))
        if not line.strip() or line.startswith('#'):
            continue
        hits = len(terms.findall(line))
        if hits:
            score = min(hits, 8) + (5 if in_method else 0)
            if 'Agent 类型' in line or 'Agent Type' in line: score -= 2
            ranked.append((score, i, line))
    chosen = []
    size = 0
    for score, i, line in sorted(ranked, key=lambda t:(-t[0],t[1])):
        # Keep complete lines when possible; a clipped line is explicitly marked.
        excerpt = line if len(line) <= 550 else line[:550] + ' [截断，完整原句见笔记]'
        if size + len(excerpt) > 2400 and chosen: continue
        chosen.append({'line':i,'text':excerpt})
        size += len(excerpt)
        if len(chosen) >= 12: break
    if not chosen:
        chosen = [{'line':i,'text':line[:350]} for i,line in enumerate(lines,1) if line.strip()][:7]
    return sorted(chosen, key=lambda x:x['line'])

def main():
    rows=read_csv(SNAPSHOT/'core_corpus_manifest.csv')
    rows.sort(key=lambda r:int(r['paper_id'].split('-')[1]))
    assert len(rows)==662 and len({r['paper_id'] for r in rows})==662
    tags={r['paper_id']:r for r in read_csv(SNAPSHOT/'coding_coverage_matrix.csv')}
    (OUT/'inputs').mkdir(exist_ok=True)
    (OUT/'scratch').mkdir(exist_ok=True)
    baseline=[]
    # Inventory all existing files outside this additive output; no mutation is needed.
    for p in BASE.rglob('*'):
        if p.is_file() and OUT not in p.parents:
            s=p.stat()
            baseline.append({'path':str(p.relative_to(BASE)).replace('\\','/'),'size':s.st_size,'mtime_ns':s.st_mtime_ns})
    dump(OUT/'source_file_inventory_before.json',baseline)
    sources={BASE/'Paper_Lists/agent_master_paper_list.md',BASE/'Data/papers.csv',BASE/'Data/papers.jsonl',SNAPSHOT/'core_corpus_manifest.csv',SNAPSHOT/'coding_coverage_matrix.csv',BASE/'paper_note_templates_and_prompts/ASD_annotation_schema.md'}
    packets=[]
    for pos,r in enumerate(rows):
        p=BASE/r['note_path'];sources.add(p)
        text=p.read_text(encoding='utf-8-sig')
        tag=tags[r['paper_id']]
        packets.append({'position':pos+1,'paper_id':r['paper_id'],'title':r['title'],'year':r['year'],'domains':r['scientific_object_modules'],'legacy_agent_type':tag['agent_type_raw'],'legacy_note_agent_type':tag['agent_type_note_summary'],'autonomy_note':tag['autonomy_note_summary_raw'],'note_path':r['note_path'],'pdf_path':r['pdf_path'],'pdf_exists':r['pdf_exists'],'source_url':r['doi_or_url'],'note_line_count':len(text.splitlines()),'evidence_lines':selected_lines(text)})
    dump(OUT/'source_hashes_before.json',{str(p.relative_to(BASE)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(sources) if p.exists()})
    assignments={}
    for name,start,end in [('A',0,221),('B',221,442),('C',442,662)]:
        subset=packets[start:end]
        with (OUT/'inputs'/f'batch_{name}.jsonl').open('w',encoding='utf-8') as f:
            for p in subset:f.write(json.dumps(p,ensure_ascii=False)+'\n')
        assignments[name]={'count':len(subset),'first':subset[0]['paper_id'],'last':subset[-1]['paper_id'],'ids':[p['paper_id'] for p in subset]}
        (OUT/'scratch'/name).mkdir(exist_ok=True)
    dump(OUT/'batch_assignments.json',assignments)
    print(json.dumps({'output':str(OUT),'papers':len(packets),'source_files_inventoried':len(baseline),'source_files_hashed':len(sources),'batches':{k:{kk:vv for kk,vv in v.items() if kk!='ids'} for k,v in assignments.items()}},ensure_ascii=False))

if __name__=='__main__':main()
