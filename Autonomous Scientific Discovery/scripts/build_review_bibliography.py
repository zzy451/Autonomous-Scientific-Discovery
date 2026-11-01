"""Generate one BibTeX source for core papers, background works and methods sources.

No external metadata is invented. Existing manuscript entries take precedence;
all incomplete metadata is exposed in the provenance inventory.
"""
import collections
import csv
import html
import json
import re
import unicodedata
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
TEX=ROOT.parent/'Agent_for_Science_Review_Overleaf'
if not TEX.exists():TEX=ROOT/'Manuscript'
OUT=ROOT/'Coverage_Check/bibliography_2026-10-30'

def clean(s):
    return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]*>','',str(s or '')))).strip()

def esc(s):
    s=clean(s)
    # Protect literal TeX metacharacters; encode Western accents for classic BibTeX.
    s=s.replace('\\','\\textbackslash{}')
    s=re.sub(r'([&%#$ _{}])',lambda m:'\\'+m[0] if m[0]!=' ' else ' ',s)
    special={'–':'--','—':'---','’':"'",'‘':"'",'“':'``','”':"''",'−':'-','×':r'$\times$','α':r'$\alpha$','β':r'$\beta$','γ':r'$\gamma$','δ':r'$\delta$','ε':r'$\epsilon$','λ':r'$\lambda$','μ':r'$\mu$','π':r'$\pi$','₂':'2','₃':'3','ł':r'{\l}','Ł':r'{\L}','ø':r'{\o}','Ø':r'{\O}','æ':r'{\ae}','œ':r'{\oe}','ß':r'{\ss}'}
    for a,b in special.items():s=s.replace(a,b)
    accents={'\u0301':"'",'\u0300':'`','\u0302':'^','\u0308':'"','\u0303':'~','\u030c':'v','\u0306':'u','\u0304':'=','\u0327':'c','\u030a':'r','\u0307':'.','\u0328':'k'}
    chars=list(unicodedata.normalize('NFD',s));result='';i=0
    while i<len(chars):
        if i+1<len(chars) and chars[i+1] in accents:
            result+='{\\'+accents[chars[i+1]]+'{'+chars[i]+'}}';i+=2
        else:result+=chars[i];i+=1
    # Corrupted source metadata is reported; do not silently transliterate CJK away.
    return result

def authors(s):
    s=clean(s)
    if not s or s.lower() in {'unknown','not available','n/a','none'}:return None
    s=re.sub(r'\bet\s+al\.?\.?','; others',s,flags=re.I)
    parts=[x.strip(' .,;') for x in s.split(';') if x.strip(' .,;')]
    return ' and '.join('others' if x=='others' else esc(x) for x in parts)

def main():
    OUT.mkdir(exist_ok=True)
    legacy=TEX/'references.tex'
    backup=OUT/'references_handwritten_original.tex'
    if not backup.exists():backup.write_bytes(legacy.read_bytes())
    source=backup.read_text(encoding='utf-8')
    records={};identities={};aliases={};inventory=[]
    def identity(e):
        if e.get('doi'):return 'doi:'+e['doi'].lower().strip().rstrip('.')
        u=e.get('url','');m=re.search(r'arxiv\.org/(?:abs|pdf)/([^/?#]+)',u)
        if m:return 'arxiv:'+re.sub(r'v\d+$','',m[1].removesuffix('.pdf'))
        return 'title:'+re.sub(r'[^a-z0-9]+','',clean(e['title']).lower())
    def add(key,e):
        ident=identity(e)
        if ident in identities:
            canonical=identities[ident];aliases[key]=canonical
            for k,v in e.items():
                if v and not records[canonical].get(k):records[canonical][k]=v
            return canonical
        assert key not in records,key
        identities[ident]=key;records[key]=e;return key
    # Preserve carefully specified published entries and existing citation keys.
    for match in re.finditer(r'\\bibitem(?:\[[^\n]*?\])?\{([^}]+)\}\s*(.*?)(?=\\bibitem|\\end\{thebibliography\})',source,re.S):
        key,body=match.groups()
        if key.startswith('asd') or key=='projecttaxonomy':continue
        lines=[x.strip() for x in body.splitlines() if x.strip() and not x.startswith('%')]
        if len(lines)<3:continue
        venue=re.search(r'\\emph\{([^}]+)\}',lines[2]);year=re.search(r'\\textbf\{(\d{4})\}',body)
        url=re.search(r'\\url\{([^}]*)\}',body);u=url[1] if url else ''
        e=dict(type='article',author=authors(lines[0]),title=clean(lines[1].rstrip('.')),journal=venue[1] if venue else '',year=year[1] if year else '',url=u)
        if 'doi.org/' in u:e['doi']=u.split('doi.org/')[-1]
        extra=re.search(r'\\textbf\{\d{4}\},\s*\\emph\{([^}]+)\},\s*([\d-]+)',body)
        if extra:e.update(volume=extra[1],pages=extra[2])
        add(key,e)
    online_path=OUT/'online_overrides.json'
    online=json.loads(online_path.read_text(encoding='utf-8')) if online_path.exists() else {}
    papers=[json.loads(s) for s in (ROOT/'Data/papers.jsonl').read_text(encoding='utf-8').splitlines() if s.strip()]
    for p in papers:
        if p['record_status'] not in {'active_confirmed_core','background_only'}:continue
        key='asd'+p['paper_id'].split('-')[1]
        doi=p.get('doi','');url=p.get('doi_or_url') or p.get('url','')
        if not doi and 'doi.org/' in url:doi=url.split('doi.org/')[-1]
        if doi.startswith('https://doi.org/'):doi=doi.split('doi.org/')[-1]
        e=dict(type='article',title=clean(p['title']),year=clean(p['year']),author=authors(p['authors']),journal=clean(p['source']),url=url,doi=doi)
        if 'arxiv' in e['journal'].lower() or 'arxiv.org/' in url:
            m=re.search(r'arxiv\.org/(?:abs|pdf)/([^/?#]+)',url)
            if m:e.update(eprint=m[1].removesuffix('.pdf'),archivePrefix='arXiv')
        if key in online:
            enriched=online[key]
            for field in ['title','year','journal','volume','number','pages','doi','url','eprint','archivePrefix']:
                if enriched.get(field):e[field]=enriched[field]
            if enriched.get('author_names'):
                e['author']=' and '.join(esc(n) for n in enriched['author_names'])
            e['type']='article'
        canonical=add(key,e)
        if key in online and canonical!=key:
            records[canonical].update({k:v for k,v in e.items() if v})
        issues=[]
        if not e.get('author') and not e.get('editor'):issues.append('missing_author')
        elif 'others' in e['author']:issues.append('abbreviated_author_list')
        if not e.get('doi') and not e.get('url'):issues.append('missing_identifier')
        if not re.fullmatch(r'\d{4}',e['year']):issues.append('year_not_four_digits')
        if '?' in e['title'] or '\ufffd' in e['title'] or re.search('[\u3400-\u9fff\ue000-\uf8ff]',e['title']):issues.append('title_needs_metadata_review')
        inventory.append(dict(paper_id=p['paper_id'],record_status=p['record_status'],citation_key=canonical,previous_id_key=key,title=e['title'],metadata_issues=';'.join(issues),online_source=online.get(key,{}).get('source_url','')))
    extra_path=OUT/'online_metadata/extra_sources.json'
    if extra_path.exists():
        for key,m in json.loads(extra_path.read_text(encoding='utf-8')).items():
            if key not in records or m.get('_error') or not m.get('author_names'):continue
            for field in ['title','year','journal','volume','number','pages','doi','url','eprint','archivePrefix']:
                if m.get(field):records[key][field]=m[field]
            records[key]['author']=' and '.join(esc(n) for n in m['author_names'])
    repo='https://github.com/zzy451/Autonomous-Scientific-Discovery'
    docs=[('projecttaxonomy','Scientific-domain taxonomy','science_domain_taxonomy.md'),('projectpolicy','Review scope and classification policy','review_scope_and_classification_policy.md'),('projectboundaries','Scientific-domain classification boundary rules','domain_classification_rules.md')]
    for key,title,path in docs:
        add(key,dict(type='misc',author='{Autonomous Scientific Discovery review project}',title=title,year='2026',howpublished='Living project documentation',url=repo+'/blob/main/Autonomous%20Scientific%20Discovery/'+path,note='Accessed 30 October 2026'))
    standards=[
        ('clc','Chinese Library Classification','https://www.ztflh.com/','Chinese Library Classification online'),
        ('lcc','Library of Congress Classification','https://www.loc.gov/catdir/cpso/lcco/','Library of Congress'),
        ('ddc','Dewey Decimal Classification','https://www.oclc.org/en/dewey.html','OCLC'),
        ('udc','Universal Decimal Classification','https://udcc.org/','UDC Consortium'),
    ]
    for key,title,url,org in standards:
        add(key,dict(type='misc',author='{'+org+'}',title=title,url=url,note='Online classification-system resource; accessed 30 October 2026'))
    # Full-library audit metadata is applied before version-specific PDF decisions.
    full_audit_path=OUT.parent/'bibliography_full_audit_2026-10-31/verified_overrides.json'
    if full_audit_path.exists():
        for key,fields in json.loads(full_audit_path.read_text(encoding='utf-8')).items():
            if key not in records:raise ValueError('Unknown full-audit citation: '+key)
            for field,value in fields.items():
                if field.startswith('_'):continue
                if field=='author_names':
                    records[key]['author']=' and '.join(n if n.startswith('{') and n.endswith('}') else esc(n) for n in value)
                elif value is None:records[key].pop(field,None)
                else:records[key][field]=value
    # Audited versions override automatic API metadata (e.g. issue year versus
    # first-online year, and the authors of the PDF actually read).
    audited_path=OUT.parent/'manuscript_evidence_audit_2026-10-30/audited_bibliography_overrides.json'
    if audited_path.exists():
        for key,fields in json.loads(audited_path.read_text(encoding='utf-8')).items():
            if key not in records:raise ValueError('Unknown audited citation: '+key)
            for field,value in fields.items():
                if field.startswith('_'):continue
                if field=='author_names':records[key]['author']=' and '.join(n if n.startswith('{') and n.endswith('}') else esc(n) for n in value)
                elif value is None:records[key].pop(field,None)
                else:records[key][field]=value
    # Current version reconciliation is separate from the dated historical audits.
    # Keep it last so rebuilding cannot restore a first-preprint/online year.
    alignment_path=OUT.parent/'core_tag_alignment_2026-11-01/bibliography_version_overrides.json'
    if alignment_path.exists():
        for key,fields in json.loads(alignment_path.read_text(encoding='utf-8')).items():
            if key not in records:raise ValueError('Unknown aligned citation: '+key)
            for field,value in fields.items():
                if field.startswith('_'):continue
                if value is None:records[key].pop(field,None)
                else:records[key][field]=value
    # Enrichment may discover a shared DOI after initial insertion. Reconcile it
    # before emitting entries so aliases cannot leave duplicate bibliography items.
    final_identities={};merged={}
    for key,e in records.items():
        ident=identity(e)
        if ident in final_identities:
            canonical=final_identities[ident];aliases[key]=canonical
            for field,value in e.items():
                if value and not merged[canonical].get(field):merged[canonical][field]=value
        else:final_identities[ident]=key;merged[key]=e
    records=merged
    def final_alias(key):
        seen=set()
        while key in aliases and key not in seen:
            seen.add(key);key=aliases[key]
        return key
    aliases={key:final_alias(value) for key,value in aliases.items()}
    for row in inventory:
        row['citation_key']=final_alias(row['citation_key'])
        e=records[row['citation_key']];issues=[]
        if not e.get('author') and not e.get('editor'):issues.append('missing_author')
        elif re.search(r'\band others\b',e.get('author','')):issues.append('abbreviated_author_list')
        if not e.get('doi') and not e.get('url'):issues.append('missing_identifier')
        if not re.fullmatch(r'\d{4}',e.get('year','')):issues.append('year_not_four_digits')
        if '\ufffd' in e['title'] or re.search('[\u3400-\u9fff\ue000-\uf8ff]',e['title']):issues.append('title_needs_metadata_review')
        row.update(title=e['title'],metadata_issues=';'.join(issues))
    text='% Unified bibliography: core research, background works, surveys, and classification sources.\n% Generated from local metadata; consult the provenance inventory for incomplete records.\n% Only cited entries appear in the manuscript. Do not add nocite{*}.\n\n'
    for key,e in records.items():
        text+='@'+e['type']+'{'+key+',\n'
        for name,value in e.items():
            if name=='type' or not value:continue
            if name=='author':v=value
            elif name in {'url','doi','eprint','archivePrefix'}:v=value
            else:v=esc(value)
            if name=='note' and e.get('url') and not e.get('doi') and not e.get('eprint'):
                v+=r'. Available at: \url{'+e['url']+'}'
            if name=='title':v='{'+v+'}'
            text+='  '+name+' = {'+v+'},\n'
        if not e.get('note') and e.get('url') and not e.get('doi') and not e.get('eprint'):
            text+=r'  note = {Available at: \url{'+e['url']+'}},\n'
        text+='}\n\n'
    (TEX/'references.bib').write_text(text,encoding='utf-8')
    # Existing aliases are replaced in source, rather than generating duplicate bibliography entries.
    for path in [TEX/'main.tex']+list((TEX/'sections').glob('*.tex')):
        s=path.read_text(encoding='utf-8')
        s=re.sub(r'(\\cite\w*\*?(?:\[[^\]]*\]){0,2}\{)([^}]+)(\})',lambda m:m[1]+','.join(aliases.get(k.strip(),k.strip()) for k in m[2].split(','))+m[3],s)
        if path.name=='main.tex':s=s.replace(r'\input{references}',r'\bibliography{references}')
        path.write_text(s,encoding='utf-8')
    methods=TEX/'sections/methods.tex';s=methods.read_text(encoding='utf-8')
    s=s.replace('and Universal Decimal Classification.','and Universal Decimal Classification~\\cite{clc,lcc,ddc,udc}.')
    s=s.replace('taxonomy~\\cite{projecttaxonomy}.','taxonomy~\\cite{projecttaxonomy,projectpolicy,projectboundaries}.')
    methods.write_text(s,encoding='utf-8')
    # Keep a compatible loader for any tools still expecting this filename.
    legacy.write_text('% Bibliography entries are maintained in references.bib.\n% The main manuscript calls \\bibliography{references} directly.\n',encoding='utf-8')
    keys=set(records);cited=set()
    for f in [TEX/'main.tex']+list((TEX/'sections').glob('*.tex')):
        for m in re.finditer(r'\\cite\w*\*?(?:\[[^\]]*\]){0,2}\{([^}]+)\}',f.read_text(encoding='utf-8')):cited.update(k.strip() for k in m[1].split(','))
    assert not cited-keys,sorted(cited-keys)
    with (OUT/'paper_citation_keys.csv').open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(inventory[0]));w.writeheader();w.writerows(inventory)
    result=dict(date='2026-10-30',bibliography_audit_date='2026-10-31' if full_audit_path.exists() else None,bib_entries=len(records),core_records=sum(x['record_status']=='active_confirmed_core' for x in inventory),background_records=sum(x['record_status']=='background_only' for x in inventory),cited_keys=len(cited),aliases=aliases,metadata_issue_counts=dict(collections.Counter(i for x in inventory for i in x['metadata_issues'].split(';') if i)),uncited_entries_printed=False)
    (OUT/'build_report.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='aliases'},ensure_ascii=True,indent=2))

if __name__=='__main__':main()
