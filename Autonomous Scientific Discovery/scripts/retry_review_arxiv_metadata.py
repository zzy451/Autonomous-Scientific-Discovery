"""Retry failed Atom batches one by one through arXiv abstract-page metadata."""
import concurrent.futures as cf
import json
import re
from html.parser import HTMLParser
from enrich_review_bibliography import CACHE, get

class Meta(HTMLParser):
    def __init__(self):super().__init__();self.data={}
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='meta' and a.get('name','').startswith('citation_'):
            self.data.setdefault(a['name'],[]).append(a.get('content',''))

def fetch(aid):
    try:
        url='https://arxiv.org/abs/'+aid
        r=get(url);p=Meta();p.feed(r.text);m=p.data
        assert m.get('citation_title') and m.get('citation_author')
        return aid,{'title':m['citation_title'][0],'author_names':m['citation_author'],'year':m.get('citation_date',[''])[0][:4],'journal':'arXiv','url':url,'eprint':aid,'archivePrefix':'arXiv','source_url':url,'retrieved_at':'2026-10-30'}
    except Exception as e:return aid,{'_error':type(e).__name__+': '+str(e)[:140]}

def main():
    path=CACHE/'arxiv.json';cache=json.loads(path.read_text(encoding='utf-8'))
    ids=[a for a,m in cache.items() if m.get('_error')]
    with cf.ThreadPoolExecutor(5) as pool:
        for i,(aid,m) in enumerate(pool.map(fetch,ids)):
            cache[aid]=m
            path.write_text(json.dumps(cache,ensure_ascii=False,indent=2),encoding='utf-8')
            if i%10==0:print('arxiv fallback',i+1,'/',len(ids),'total successes',sum(not x.get('_error') for x in cache.values()),flush=True)
if __name__=='__main__':main()
