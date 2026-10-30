"""Resolve records without DOI/arXiv identifiers by conservative Crossref title search."""
import concurrent.futures as cf
import json
import re
from urllib.parse import quote
from enrich_review_bibliography import OUT, CACHE, PAPERS, get, norm, difflib

def lookup(p):
    url='https://api.crossref.org/works?rows=3&query.title='+quote(p['title'])
    try:
        items=get(url).json()['message']['items']
        candidates=[]
        for m in items:
            title=m.get('title',[''])[0]
            sim=difflib.SequenceMatcher(None,norm(title),norm(p['title'])).ratio()
            year=m.get('published',m.get('issued',{})).get('date-parts',[[None]])[0][0]
            local=re.search(r'\d{4}',p['year'])
            if sim<0.95 or (local and year and abs(int(local[0])-year)>1):continue
            names=[a.get('family','')+', '+a.get('given','') if a.get('family') else a.get('name','') for a in m.get('author',[])]
            if not names:continue
            candidates.append((sim,dict(title=title,author_names=names,year=str(year) if year else '',journal=m.get('container-title',[''])[0] if m.get('container-title') else '',volume=m.get('volume',''),number=m.get('issue',''),pages=m.get('page',m.get('article-number','')),doi=m.get('DOI',''),url=m.get('URL',''),source_url=url,retrieved_at='2026-10-30',match_similarity=sim)))
        candidates.sort(key=lambda x:x[0],reverse=True)
        if not candidates:return p['paper_id'],{'_error':'No sufficiently close title/year match','source_url':url}
        if len(candidates)>1 and candidates[0][0]-candidates[1][0]<0.01 and candidates[0][1]['doi']!=candidates[1][1]['doi']:
            return p['paper_id'],{'_error':'Ambiguous close title matches','source_url':url}
        return p['paper_id'],candidates[0][1]
    except Exception as e:return p['paper_id'],{'_error':type(e).__name__+': '+str(e)[:140],'source_url':url}

def main():
    path=CACHE/'title_search.json'
    cache=json.loads(path.read_text(encoding='utf-8')) if path.exists() else {}
    papers=[p for p in PAPERS if not p.get('doi') and not p.get('arxiv_id') and not re.search(r'doi.org/|arxiv.org/',p.get('doi_or_url','')) and p['paper_id'] not in cache]
    with cf.ThreadPoolExecutor(3) as pool:
        for i,(pid,m) in enumerate(pool.map(lookup,papers)):
            cache[pid]=m;path.write_text(json.dumps(cache,ensure_ascii=False,indent=2),encoding='utf-8')
            if i%10==0:print('title search',i+1,'/',len(papers),'accepted',sum(not x.get('_error') for x in cache.values()),flush=True)
if __name__=='__main__':main()
