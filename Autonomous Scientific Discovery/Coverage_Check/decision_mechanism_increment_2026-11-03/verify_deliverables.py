"""Data integrity checks for completed exports and cited primary excerpts."""
import collections
import csv
import json
import re
import unicodedata
from pathlib import Path
import fitz
from openpyxl import load_workbook

OUT=Path(__file__).resolve().parent
BASE=OUT.parent.parent
with (OUT/'classification_results_662.jsonl').open(encoding='utf-8') as f:rows=[json.loads(s) for s in f if s.strip()]
csvrows=list(csv.DictReader((OUT/'classification_results_662.csv').open(encoding='utf-8-sig',newline='')))
assert len(rows)==len(csvrows)==662
assert len({r['paper_id'] for r in rows})==662
assert all(r['decision_class'] in {'D1','D2','D3','D4','D5','D6'} for r in rows)
assert [r['paper_id'] for r in rows]==[r['paper_id'] for r in csvrows]
summary=json.loads((OUT/'classification_summary.json').read_text(encoding='utf-8'))
assert collections.Counter(r['decision_class'] for r in rows)=={c:v['count'] for c,v in summary['classes'].items()}
wb=load_workbook(OUT/'classification_results_662.xlsx',read_only=False,data_only=True)
assert wb['全部662篇'].max_row==663
assert wb['待全文复核'].max_row==1+summary['needs_fulltext_review_count']
assert len(wb['全部662篇'].tables)==1
assert len({wb['全部662篇'].cell(i,1).value for i in range(2,664)})==662

def norm(s,dehyphen=True):
    s=unicodedata.normalize('NFKC',s)
    if dehyphen:s=re.sub(r'-\s*\n\s*','',s)
    return re.sub(r'\s+','',s).casefold().replace('\u00ad','')

checks=[]
for r in rows:
    if r['source_basis']=='note_and_pdf':
        p=BASE/r['pdf_path']
        if not p.is_file():
            checks.append({'paper_id':r['paper_id'],'status':'pdf_missing','locator':r['primary_source_locator']});continue
        q=norm(r['primary_source_excerpt'])
        q_strict=norm(r['primary_source_excerpt'],False)
        with fitz.open(p) as doc:
            pages=[]
            for i in range(len(doc)):
                text=doc[i].get_text()
                if q in norm(text) or q_strict in norm(text,False):pages.append(i+1)
        checks.append({'paper_id':r['paper_id'],'status':'matched' if pages else 'unmatched','matched_pages':pages,'locator':r['primary_source_locator']})
    elif r['source_basis']=='note_and_cached_fulltext':
        # Existing HTML caches are read-only, and can reside at workspace root.
        loc=r['primary_source_locator'];candidate=loc.split('，')[0].split(',')[0]
        paths=[BASE/candidate,BASE.parent/candidate]
        found=next((p for p in paths if p.is_file()),None)
        if found:
            text=found.read_text(encoding='utf-8',errors='replace')
            status='matched' if norm(r['primary_source_excerpt']) in norm(text) else 'unmatched'
        else:status='cache_path_unresolved'
        checks.append({'paper_id':r['paper_id'],'status':status,'locator':loc})
result={'unique_records':662,'csv_jsonl_ids_identical':True,'six_class_single_assignment':True,'xlsx_rows':662,'xlsx_review_queue_rows':summary['needs_fulltext_review_count'],'primary_excerpt_checks':dict(collections.Counter(r['status'] for r in checks)),'primary_excerpt_details':checks,'issues':[r for r in checks if r['status']!='matched']}
(OUT/'deliverable_verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='primary_excerpt_details'},ensure_ascii=False,indent=2))
