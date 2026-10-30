"""Fetch bibliographic metadata; retain responses and conservative identity checks."""
import concurrent.futures as cf
import difflib
import html
import json
import re
import time
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import quote
import requests

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'Coverage_Check/bibliography_2026-10-30'
CACHE=OUT/'online_metadata'
CACHE.mkdir(exist_ok=True)
PAPERS=[json.loads(s) for s in (ROOT/'Data/papers.jsonl').read_text(encoding='utf-8').splitlines() if s.strip()]
PAPERS=[p for p in PAPERS if p['record_status'] in {'active_confirmed_core','background_only'}]

def get(url):
    for attempt in range(2):
        try:
            r=requests.get(url,timeout=25,headers={'User-Agent':'ASD-bibliography-metadata/1.0'})
            r.raise_for_status()
            return r
        except Exception:
            if attempt:raise
            time.sleep(1)

def arxiv_batch(ids):
    url='https://export.arxiv.org/api/query?id_list='+','.join(ids)+'&max_results=50'
    try:
        r=get(url); root=ET.fromstring(r.content); ns={'a':'http://www.w3.org/2005/Atom'}; result={}
        for e in root.findall('a:entry',ns):
            aid=e.findtext('a:id','',ns).split('/abs/')[-1]
            aid=re.sub(r'v\d+$','',aid)
            if aid not in ids:continue
            result[aid]={'title':' '.join(e.findtext('a:title','',ns).split()),'author_names':[a.findtext('a:name','',ns) for a in e.findall('a:author',ns)],'year':e.findtext('a:published','',ns)[:4], 'journal':'arXiv','url':'https://arxiv.org/abs/'+aid,'eprint':aid,'archivePrefix':'arXiv','source_url':url,'retrieved_at':'2026-10-30'}
        return result
    except Exception as e:return {'_error':type(e).__name__+': '+str(e)[:140], '_ids':ids}

def crossref(doi):
    url='https://api.crossref.org/works/'+quote(doi,safe='')
    try:
        m=get(url).json()['message']
        names=[]
        for a in m.get('author',[]):
            names.append(a.get('family','')+', '+a.get('given','') if a.get('family') else a.get('name',''))
        date=m.get('published',m.get('issued',{})).get('date-parts',[[None]])[0][0]
        return {'title':html.unescape(re.sub('<[^>]*>','',m.get('title',[''])[0])),'author_names':names,'year':str(date) if date else '', 'journal':m.get('container-title',[''])[0] if m.get('container-title') else '', 'volume':m.get('volume',''),'number':m.get('issue',''),'pages':m.get('page',m.get('article-number','')),'doi':m.get('DOI',doi),'url':m.get('URL',''),'source_url':url,'retrieved_at':'2026-10-30'}
    except Exception as e:return {'_error':type(e).__name__+': '+str(e)[:140]}

def norm(s):return re.sub(r'[^a-z0-9]','',html.unescape(s).lower())

def main():
    arxiv={};dois={}
    for p in PAPERS:
        u=p.get('doi_or_url','') or p.get('url',''); doi=p.get('doi','')
        if not doi and 'doi.org/' in u:doi=u.split('doi.org/')[-1]
        if doi:dois.setdefault(doi.replace('https://doi.org/','').strip(),[]).append(p)
        else:
            m=re.search(r'arxiv.org/(?:abs|pdf)/([^?#\s]+)',u)
            aid=p.get('arxiv_id','') or (m[1].removesuffix('.pdf') if m else '')
            if aid:arxiv.setdefault(re.sub(r'v\d+$','',aid),[]).append(p)
    af=CACHE/'arxiv.json'; df=CACHE/'crossref.json'
    ac=json.loads(af.read_text(encoding='utf-8')) if af.exists() else {}
    dc=json.loads(df.read_text(encoding='utf-8')) if df.exists() else {}
    missing=[a for a in arxiv if a not in ac or ac[a].get('_error')]
    if '--cached-only' in sys.argv:missing=[]
    batches=[missing[i:i+30] for i in range(0,len(missing),30)]
    with cf.ThreadPoolExecutor(3) as pool:
        fs=[pool.submit(arxiv_batch,b) for b in batches]
        for i,f in enumerate(cf.as_completed(fs)):
            result=f.result()
            if '_error' in result:
                for a in result['_ids']:ac[a]={'_error':result['_error']}
            else:ac.update(result)
            af.write_text(json.dumps(ac,ensure_ascii=False,indent=2),encoding='utf-8')
            print('arxiv batches',i+1,'/',len(batches),'resolved',sum(not x.get('_error') for x in ac.values()),flush=True)
    missing=[d for d in dois if d not in dc or dc[d].get('_error')]
    if '--cached-only' in sys.argv:missing=[]
    with cf.ThreadPoolExecutor(4) as pool:
        fs={pool.submit(crossref,d):d for d in missing}
        for i,f in enumerate(cf.as_completed(fs)):
            dc[fs[f]]=f.result()
            df.write_text(json.dumps(dc,ensure_ascii=False,indent=2),encoding='utf-8')
            if i%10==0:print('crossref',i+1,'/',len(missing),flush=True)
    overrides={}; audit=[]
    for kind,groups,cache in [('arxiv',arxiv,ac),('crossref',dois,dc)]:
        for ident,ps in groups.items():
            m=cache.get(ident,{'_error':'no response entry'})
            for p in ps:
                sim=difflib.SequenceMatcher(None,norm(p['title']),norm(m.get('title',''))).ratio()
                accepted=not m.get('_error') and sim>=0.65 and bool(m.get('author_names'))
                key='asd'+p['paper_id'].split('-')[1]
                audit.append({'paper_id':p['paper_id'],'key':key,'provider':kind,'identifier':ident,'title_similarity':round(sim,3),'accepted':accepted,'local_title':p['title'],'online_title':m.get('title',''),'error':m.get('_error',''),'source_url':m.get('source_url','')})
                if accepted:overrides[key]=m
    title_path=CACHE/'title_search.json'
    title_cache=json.loads(title_path.read_text(encoding='utf-8')) if title_path.exists() else {}
    for pid,m in title_cache.items():
        key='asd'+pid.split('-')[1]
        if not m.get('_error') and m.get('author_names'):overrides[key]=m
        audit.append(dict(paper_id=pid,key=key,provider='crossref_title_search',accepted=not m.get('_error'),title_similarity=m.get('match_similarity',0),online_title=m.get('title',''),error=m.get('_error',''),source_url=m.get('source_url','')))
    (OUT/'online_overrides.json').write_text(json.dumps(overrides,ensure_ascii=False,indent=2),encoding='utf-8')
    (OUT/'online_lookup_audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2),encoding='utf-8')
    print('accepted',len(overrides),'attempted records',len(audit),flush=True)

if __name__=='__main__':main()
