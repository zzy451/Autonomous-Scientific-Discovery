"""Build the two standalone editors from explicit frozen inputs, without prior versions."""
from pathlib import Path
import argparse
import copy
import json
import re
import shutil
from recount import ROOT,table,audit_inputs


def build(output):
    audit=audit_inputs()
    fields=sorted(table(ROOT/'inputs/fields.csv'),key=lambda r:r['field_code'])
    themes=table(ROOT/'inputs/themes.csv')
    groups=[sorted([r for r in themes if r['field_code']==f['field_code']],key=lambda r:int(r['rank'])) for f in fields]
    params=json.loads((ROOT/'inputs/parameters.json').read_text(encoding='utf-8'))
    geometry=copy.deepcopy(params['geometry'])
    geometry['sharedSeas']=[]
    for r in table(ROOT/'inputs/selected_seas.csv'):
        geometry['sharedSeas'].append(dict(m=[int(x)-1 for x in r['members'].split(';')],n=int(r['records']),anchor=None if r['anchor_x']=='' else [float(r['anchor_x']),float(r['anchor_y'])],size=float(r['size']),stretch=float(r['stretch']),angle=None if r['angle']=='' else float(r['angle'])))
    values={
        'names':[r['name_en'] for r in fields],
        'counts':[int(r['layout_reference_records']) for r in fields],
        'displayRecordCounts':[int(r['display_records']) for r in fields],
        'colors':[r['color'] for r in fields],
        'themes':[[r['name_en'] for r in g] for g in groups],
        'formalTertiaryCodes':[[r['tertiary_code'] for r in g] for g in groups],
        'fieldTitleLines':[json.loads(r['title_lines']) for r in fields],
        'themeRecordCounts':[[int(r['all_records']) for r in g] for g in groups],
        'themeOffsets':params['theme_offsets'],
        'defaultCenters':geometry['centers'],
        'initial':geometry,
    }
    output.mkdir(parents=True,exist_ok=True)
    for kind,destination in [('geometry','figure.html'),('fast','figure_fast_editor.html')]:
        text=(ROOT/f'src/map_{kind}_template.html').read_text(encoding='utf-8')
        for name,value in values.items():
            pattern=r'(var '+name+r'\s*=\s*)(\[.*?\]|\{.*?\})(;)'
            text,n=re.subn(pattern,lambda m:m[1]+json.dumps(value,ensure_ascii=False,separators=(',',':'))+m[3],text,flags=re.S)
            assert n>=1,name
        seed=params['random_seed']
        text=text.replace('var seed = 20261115;',f'var seed = {seed};').replace('seed=20261115;',f'seed={seed};')
        (output/destination).write_text(text,encoding='utf-8')
    for name in ['d3.v4.min.js','fantasy_maps_map.js']:shutil.copy2(ROOT/'vendor'/name,output/name)
    (output/'input_audit.json').write_text(json.dumps(audit,indent=2)+'\n',encoding='utf-8')
    return audit


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,default=ROOT/'build')
    args=parser.parse_args();print(json.dumps(build(args.output.resolve()),indent=2))
