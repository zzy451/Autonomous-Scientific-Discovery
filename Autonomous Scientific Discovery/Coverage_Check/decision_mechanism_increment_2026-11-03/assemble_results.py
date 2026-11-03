"""Validate and assemble six-class incremental coding; never writes source files."""
from __future__ import annotations
import argparse
import collections
import csv
import hashlib
import html
import json
import re
from pathlib import Path

OUT = Path(__file__).resolve().parent
BASE = OUT.parent.parent
NAMES = {'D1':'符号/知识推理型','D2':'规划/模型驱动型','D3':'优化/概率决策型','D4':'学习策略型','D5':'LLM 驱动型','D6':'混合机制型'}
CONF = {'high':'高','medium':'中','low':'低'}

def read_jsonl(p):
    with p.open(encoding='utf-8-sig') as f:
        return [json.loads(line) for line in f if line.strip()]

def dump(p,value):
    p.write_text(json.dumps(value,ensure_ascii=False,indent=2),encoding='utf-8')

def safe_md(value):
    return str(value or '').replace('|','\\|').replace('\n',' ')

def load():
    manifest={r['paper_id']:r for r in csv.DictReader((BASE/'Coverage_Check/core_tag_alignment_2026-11-01/core_corpus_manifest.csv').open(encoding='utf-8-sig',newline=''))}
    packets={}
    for name in 'ABC':
        packets.update({r['paper_id']:r for r in read_jsonl(OUT/'inputs'/f'batch_{name}.jsonl')})
    assert set(packets)==set(manifest) and len(packets)==662
    assignments=json.loads((OUT/'batch_assignments.json').read_text(encoding='utf-8'))
    merged={};errors=[];reviewer_counts={}
    for name in 'ABC':
        p=OUT/f'reviewer_{name}.jsonl'
        rr=read_jsonl(p) if p.exists() else []
        reviewer_counts[name]=len(rr)
        owned=set(assignments[name]['ids'])
        seen=set()
        for r in rr:
            pid=r.get('paper_id')
            if pid not in owned:errors.append(f'{name}: non-owned ID {pid}')
            if pid in seen or pid in merged:errors.append(f'duplicate {pid}')
            seen.add(pid)
            merged[pid]={**r,'reviewer':name,'controller_reviewed':False}
    overrides=read_jsonl(OUT/'controller_review.jsonl') if (OUT/'controller_review.jsonl').exists() else []
    for r in overrides:
        pid=r['paper_id']
        if pid not in merged:
            errors.append(f'controller override without reviewer result: {pid}')
            continue
        merged[pid].update(r)
        merged[pid]['controller_reviewed']=True
    final=[]
    for pid,r in sorted(merged.items(),key=lambda x:int(x[0].split('-')[1])):
        if pid not in manifest:continue
        p=packets[pid];m=manifest[pid]
        if r.get('decision_class') not in NAMES:errors.append(f'{pid}: invalid class')
        if r.get('confidence') not in CONF:errors.append(f'{pid}: invalid confidence')
        if any(not isinstance(r.get(k),bool) for k in ('provisional','needs_fulltext_review')):errors.append(f'{pid}: bool fields missing')
        reason=r.get('rationale_zh','')
        if len(re.findall(r'[\u4e00-\u9fff]',reason))<8:errors.append(f'{pid}: insufficient Chinese rationale / possible encoding damage')
        if reason.count('?')>=4:errors.append(f'{pid}: possible question-mark encoding damage')
        note=(BASE/p['note_path']).read_text(encoding='utf-8-sig')
        quote=r.get('evidence_quote','')
        line=r.get('evidence_note_line',0)
        if not quote or quote not in note:errors.append(f'{pid}: evidence quote absent from note')
        elif not isinstance(line,int) or not 1<=line<=len(note.splitlines()) or quote not in note.splitlines()[line-1]:errors.append(f'{pid}: quote locator mismatch')
        if r.get('confidence')=='low' and not r.get('provisional'):errors.append(f'{pid}: low confidence must be provisional')
        basis=r.get('source_basis')
        if basis not in {'note','note_and_pdf','note_and_cached_fulltext','note_and_primary_web'}:errors.append(f'{pid}: invalid source_basis')
        if basis!='note' and not (r.get('primary_source_excerpt') and r.get('primary_source_locator')):errors.append(f'{pid}: primary-source evidence missing')
        final.append({
            'paper_id':pid,'title':m['title'],'year':m['year'],
            'scientific_object_modules':m['scientific_object_modules'],
            'decision_class':r.get('decision_class'),'decision_class_zh':NAMES.get(r.get('decision_class'),''),
            'confidence':r.get('confidence'),'provisional':r.get('provisional'),'needs_fulltext_review':r.get('needs_fulltext_review'),
            'rationale_zh':reason,'legacy_agent_type_raw':p['legacy_agent_type'],
            'legacy_note_agent_type':p['legacy_note_agent_type'],'note_path':p['note_path'],
            'evidence_note_line':line,'evidence_quote':quote,'source_basis':basis,
            'primary_source_excerpt':r.get('primary_source_excerpt',''),'primary_source_locator':r.get('primary_source_locator',''),
            'pdf_path':m['pdf_path'],'source_url':m['doi_or_url'],'reviewer':r['reviewer'],
            'controller_reviewed':r['controller_reviewed'],'controller_review_reason':r.get('controller_review_reason',''),
            'corpus_snapshot':'2026-11-01','classification_date':'2026-11-03',
        })
    return final,errors,reviewer_counts,sorted(set(manifest)-set(merged))

def check_sources():
    hashes=json.loads((OUT/'source_hashes_before.json').read_text(encoding='utf-8'))
    changed_hashes=[rel for rel,h in hashes.items() if not (BASE/rel).exists() or hashlib.sha256((BASE/rel).read_bytes()).hexdigest()!=h]
    inventory=json.loads((OUT/'source_file_inventory_before.json').read_text(encoding='utf-8'))
    changed_metadata=[]
    for r in inventory:
        p=BASE/r['path']
        if not p.exists():changed_metadata.append({'path':r['path'],'change':'missing'})
        else:
            s=p.stat()
            if s.st_size!=r['size'] or s.st_mtime_ns!=r['mtime_ns']:changed_metadata.append({'path':r['path'],'change':'size_or_mtime'})
    original_paths={r['path'] for r in inventory}
    new_outside=[str(p.relative_to(BASE)).replace('\\','/') for p in BASE.rglob('*') if p.is_file() and OUT not in p.parents and str(p.relative_to(BASE)).replace('\\','/') not in original_paths]
    return {'hashed_sources':len(hashes),'hash_changes':changed_hashes,'existing_files_inventoried':len(inventory),'metadata_changes':changed_metadata,'new_files_outside_increment':new_outside}

def write_csv(path,rows,fields=None):
    with path.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields or list(rows[0]) if rows else fields or ['paper_id'])
        w.writeheader();w.writerows(rows)

def excel(rows,summary):
    from openpyxl import Workbook
    from openpyxl.styles import Alignment,Font,PatternFill
    from openpyxl.worksheet.table import Table,TableStyleInfo
    from openpyxl.utils import get_column_letter
    from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE
    def xvalue(value):
        if isinstance(value,str):return ILLEGAL_CHARACTERS_RE.sub('',value)[:32767]
        return value
    wb=Workbook();wb.remove(wb.active)
    cols=[('paper_id','论文ID'),('title','论文题名'),('year','年份'),('decision_class','机制代码'),('decision_class_zh','唯一主标签'),('confidence','置信度'),('provisional','暂定'),('needs_fulltext_review','待全文复核'),('rationale_zh','分类理由'),('legacy_agent_type_raw','原始Agent类型'),('scientific_object_modules','科学对象模块'),('source_basis','本轮证据基础'),('note_path','笔记路径'),('evidence_note_line','笔记行号'),('evidence_quote','笔记原句'),('primary_source_locator','本轮原文核对位置'),('primary_source_excerpt','本轮原文片段'),('pdf_path','PDF路径'),('source_url','来源链接'),('reviewer','初审Agent'),('controller_reviewed','主控复核'),('controller_review_reason','复核说明')]
    for sheet_name,subset,table_name in [('全部662篇',rows,'AllPapers'),('待全文复核',[r for r in rows if r['needs_fulltext_review']],'ReviewQueue')]:
        ws=wb.create_sheet(sheet_name);ws.append([label for _,label in cols])
        for r in subset:
            ws.append([xvalue(r.get(key,'')) for key,_ in cols])
            idx=ws.max_row
            for col in (2,9,10,13,15,16,17,18,22):ws.cell(idx,col).alignment=Alignment(wrap_text=True,vertical='top')
            ws.row_dimensions[idx].height=58
            if r['confidence']=='low':
                for cell in ws[idx]:cell.fill=PatternFill('solid',fgColor='FFF1CC')
            note_cell=ws.cell(idx,13);note_cell.hyperlink=(BASE/r['note_path']).as_uri();note_cell.style='Hyperlink'
            if r['source_url']:ws.cell(idx,19).hyperlink=r['source_url'];ws.cell(idx,19).style='Hyperlink'
        ws.freeze_panes='C2'
        for j in range(1,len(cols)+1):ws.column_dimensions[get_column_letter(j)].width=17
        for col,width in [('B',64),('I',66),('J',45),('M',42),('O',76),('P',42),('Q',65),('R',42),('S',34),('V',56)]:ws.column_dimensions[col].width=width
        if subset:
            tab=Table(displayName=table_name,ref=f'A1:{get_column_letter(len(cols))}{ws.max_row}')
            tab.tableStyleInfo=TableStyleInfo(name='TableStyleMedium2',showRowStripes=True)
            ws.add_table(tab)
    ws=wb.create_sheet('分类汇总',0)
    ws.append(['代码','类别','篇数','占662篇比例','高置信','中置信','低置信','暂定','待全文复核'])
    for code,name in NAMES.items():
        rr=[r for r in rows if r['decision_class']==code]
        ws.append([code,name,len(rr),len(rr)/662,*[sum(r['confidence']==c for r in rr) for c in CONF],sum(r['provisional'] for r in rr),sum(r['needs_fulltext_review'] for r in rr)])
        ws.cell(ws.max_row,4).number_format='0.0%'
    ws.append(['合计','',len(rows),1,*[summary['confidence_counts'].get(c,0) for c in CONF],summary['provisional_count'],summary['needs_fulltext_review_count']])
    ws.append([]);ws.append(['说明','主标签互斥；暂定和待复核是状态，不是额外机制类。'])
    ws.append(['证据','以笔记为主要证据，部分边界本轮直接核对PDF/全文；不宣称全库重读原文。'])
    ws.append(['置信度','表示此次机制归类判断的把握程度，不表示科学发现验证强度。'])
    ws.append(['源文件','全部输出为新目录内的派生增量，原有主表/笔记/正文/PPT不写回。'])
    ws.column_dimensions['A'].width=15;ws.column_dimensions['B'].width=90
    for col in 'CDEFGHI':ws.column_dimensions[col].width=18
    ws=wb.create_sheet('六类规则')
    for line in (OUT/'classification_protocol.md').read_text(encoding='utf-8').splitlines():ws.append([line]);ws.cell(ws.max_row,1).alignment=Alignment(wrap_text=True,vertical='top')
    ws.column_dimensions['A'].width=145
    for ws in wb:
        for cell in ws[1]:cell.font=Font(bold=True,color='FFFFFF');cell.fill=PatternFill('solid',fgColor='24476A')
    wb.save(OUT/'classification_results_662.xlsx')

def assemble(rows,source_check,reviewer_counts):
    counts=collections.Counter(r['decision_class'] for r in rows)
    summary={'papers':len(rows),'unique_papers':len({r['paper_id'] for r in rows}),'classes':{c:{'name':n,'count':counts[c],'percent':round(counts[c]/662*100,2)} for c,n in NAMES.items()},'confidence_counts':dict(collections.Counter(r['confidence'] for r in rows)),'provisional_count':sum(r['provisional'] for r in rows),'needs_fulltext_review_count':sum(r['needs_fulltext_review'] for r in rows),'source_basis_counts':dict(collections.Counter(r['source_basis'] for r in rows)),'controller_reviewed_count':sum(r['controller_reviewed'] for r in rows),'reviewer_counts':reviewer_counts,'source_integrity':source_check,'models':{'reviewer_A':'gpt-6.1-sol/high','reviewer_B':'gpt-6.1-sol/high','reviewer_C':'gpt-6.1-sol/high'},'corpus_snapshot':'2026-11-01','classification_date':'2026-11-03'}
    cross_paths=[OUT/'scratch/A/cross_review.jsonl',OUT/'scratch/C/cross_review_A_D6.jsonl']
    cross_ids={r['paper_id'] for p in cross_paths if p.exists() for r in read_jsonl(p)}
    summary['independent_cross_reviewed_count']=len(cross_ids)
    summary['independent_cross_review_files']=[str(p.relative_to(OUT)).replace('\\','/') for p in cross_paths]
    dump(OUT/'classification_summary.json',summary)
    with (OUT/'classification_results_662.jsonl').open('w',encoding='utf-8') as f:
        for r in rows:
            line=json.dumps(r,ensure_ascii=False)
            for ch in ('\u0085','\u2028','\u2029'):line=line.replace(ch,f'\\u{ord(ch):04x}')
            f.write(line+'\n')
    write_csv(OUT/'classification_results_662.csv',rows)
    queue=[r for r in rows if r['needs_fulltext_review']]
    write_csv(OUT/'fulltext_review_queue.csv',queue,list(rows[0]))
    domain_rows=[]
    for domain in [f'{i:02d}' for i in range(1,12)]+['general_method']:
        rr=[r for r in rows if domain in json.loads(r['scientific_object_modules'])] if domain!='general_method' else [r for r in rows if not json.loads(r['scientific_object_modules'])]
        domain_rows.append({'module':domain,'unique_works':len(rr),**{code:sum(r['decision_class']==code for r in rr) for code in NAMES}})
    write_csv(OUT/'domain_by_decision_mechanism.csv',domain_rows)
    excel(rows,summary)
    table=['| 代码 | 唯一主标签 | 篇数 | 占比 | 高/中/低置信 | 暂定 | 待全文复核 |','|---|---|---:|---:|---|---:|---:|']
    for code,name in NAMES.items():
        rr=[r for r in rows if r['decision_class']==code]
        cs='/'.join(str(sum(r['confidence']==c for r in rr)) for c in CONF)
        table.append(f'| {code} | {name} | {len(rr)} | {len(rr)/662:.1%} | {cs} | {sum(r["provisional"] for r in rr)} | {sum(r["needs_fulltext_review"] for r in rr)} |')
    report=['# 662篇核心论文主导决策机制增量分类','',f'分类日期：2026-11-03；核心库快照：2026-11-01。共{len(rows)}篇，每篇恰好一个D1—D6主标签。', '',*table,'',f'置信度：高{summary["confidence_counts"].get("high",0)}篇、中{summary["confidence_counts"].get("medium",0)}篇、低{summary["confidence_counts"].get("low",0)}篇；暂定{summary["provisional_count"]}篇，待全文复核{summary["needs_fulltext_review_count"]}篇。低置信/暂定记录依用户六类限制给出当前最佳判断，不能与已充分核实记录混为一谈。','', '## 查看结果','', '- [Excel完整清单（可筛选，含证据、理由、置信度和复核表）](classification_results_662.xlsx)','- [CSV完整清单](classification_results_662.csv)','- [按六类浏览全部论文](classification_results_662_zh.md)','- [待全文复核清单](fulltext_review_queue.csv)','- [六类操作规则](classification_protocol.md)','- [边界裁决说明](boundary_adjudications_zh.md)','- [领域×机制交叉表](domain_by_decision_mechanism.csv)','', '## 证据与解释范围','',f'三个独立分片Agent均使用gpt-6.1-sol、high推理，分别处理221、221、220篇。其后对{len(cross_ids)}篇少数类及争议记录进行独立交叉复核；主控合并并裁决机制边界。旧Agent类型仅作线索，主标签依据关键科研动作的实际生成/选择/更新机制。证据字段区分笔记转述和本轮直接核对原文。','',f'本轮证据基础：{json.dumps(summary["source_basis_counts"],ensure_ascii=False)}；主控记录复核{summary["controller_reviewed_count"]}篇。高置信表示机制归类把握，不是科学结果的验证强度。未宣称662篇全部重读原文。','', 'D6仅用于具有共同决策作用且难分主导的机制组合；工具、RAG、多Agent、普通验证器、机器人平台或旧Hybrid标签本身不充分。RL训练的LLM在部署时由语言推理选择行动，原则上归D5；非LLM学习策略归D4。', '', '对多个独立系统的比较论文、基础设施或只展示预测辅助的工作，唯一标签可能只是论文层面的近似；相应理由说明范围限制并进入复核状态。暂定分类不改变其既有纳入状态。','', '这是独立增量，不替换原有Agent类型、科学对象模块、纳入状态、主表、笔记或正文。领域交叉表按非排他领域归属计数，跨领域论文会重复进入不同领域；机制总表则按662篇唯一工作计数。','', '## 原有文件完整性','',f'对{source_check["existing_files_inventoried"]}个既有项目文件比对大小与修改时间，对{source_check["hashed_sources"]}个直接来源文件比对SHA-256。内容哈希变化{len(source_check["hash_changes"])}项，文件元数据变化{len(source_check["metadata_changes"])}项，增量目录外新增文件{len(source_check["new_files_outside_increment"])}项。详情见[source_integrity_check.json](source_integrity_check.json)。','']
    report += ['检查期间另观察到增量目录外的新文件，仅作盘点记录；它们不纳入本次分类交付，本轮未对其写入、移动或删除。','']
    verification_path=OUT/'deliverable_verification.json'
    if verification_path.exists():
        v=json.loads(verification_path.read_text(encoding='utf-8'))
        report += ['## 交付校验','',f'JSONL、CSV、Excel均为662个唯一论文ID，六类单标签和汇总计数一致；Excel复核表{v["xlsx_review_queue_rows"]}篇。本轮最终表中直接核对原文的{sum(v["primary_excerpt_checks"].values())}条记录，其原文摘录均在相应本地PDF或全文缓存中匹配，未解决引用问题{len(v["issues"])}项。详见[deliverable_verification.json](deliverable_verification.json)。','']
    (OUT/'classification_report_zh.md').write_text('\n'.join(report),encoding='utf-8')
    md=['# 662篇核心论文：六类主导决策机制清单','', '[汇总与证据说明](classification_report_zh.md)；完整原句、原文核对位置及旧标签见[Excel](classification_results_662.xlsx)。暂定/复核状态不构成额外类别。','']
    for code,name in NAMES.items():
        rr=[r for r in rows if r['decision_class']==code]
        md += [f'## {code} {name}（{len(rr)}篇）','','| 论文ID | 论文题名 | 置信/状态 | 分类理由 | 笔记证据 |','|---|---|---|---|---|']
        for r in rr:
            status=CONF[r['confidence']]+('；暂定' if r['provisional'] else '')+('；待全文复核' if r['needs_fulltext_review'] else '')
            link=(BASE/r['note_path']).as_posix()
            md.append(f'| {r["paper_id"]} | {safe_md(r["title"])} | {status} | {safe_md(r["rationale_zh"])} | [L{r["evidence_note_line"]}](<{link}:{r["evidence_note_line"]}>) |')
        md.append('')
    (OUT/'classification_results_662_zh.md').write_text('\n'.join(md),encoding='utf-8')
    return summary

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--partial',action='store_true');args=ap.parse_args()
    rows,errors,counts,missing=load()
    check={'rows':len(rows),'reviewer_counts':counts,'errors':errors,'missing':missing}
    dump(OUT/'validation_status.json',check)
    if args.partial:
        print(json.dumps(check,ensure_ascii=False));return
    assert not errors,errors
    assert not missing and len(rows)==662,missing
    source_check=check_sources();dump(OUT/'source_integrity_check.json',source_check)
    assert not source_check['hash_changes'],'Original source content changed'
    assert not source_check['metadata_changes'],'Existing file metadata changed'
    # Other workspace work may create new files concurrently. Record them without
    # claiming ownership, moving them, or touching them; protect existing sources.
    summary=assemble(rows,source_check,counts)
    print(json.dumps(summary,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
