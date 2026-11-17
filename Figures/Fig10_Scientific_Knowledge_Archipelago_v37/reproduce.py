"""Build, render and verify Fig.10 v37 without network access during rendering."""
from pathlib import Path
import argparse
import hashlib
import importlib.metadata
import itertools
import json
import platform
import re
from xml.etree import ElementTree as ET
from build import ROOT,build


def overlap(a,b):
    return max(0,min(a['x']+a['width'],b['x']+b['width'])-max(a['x'],b['x']))*max(0,min(a['y']+a['height'],b['y']+b['height'])-max(a['y'],b['y']))


def selected_nodes(root,tag,cls):
    return [n for n in root.iter() if n.tag.split('}')[-1]==tag and cls in n.get('class','').split()]


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=ROOT/'build')
    parser.add_argument('--build-only',action='store_true',help='Only build HTML and recount inputs; no Playwright needed.')
    parser.add_argument('--strict-pixels',action='store_true',help='Also require the PNG to match the reference byte-for-byte. Requires the recorded Windows/Arial/browser environment.')
    args=parser.parse_args();output=args.output.resolve();inputs=build(output)
    if args.build_only:print(json.dumps(inputs,indent=2));return
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        browser=pw.chromium.launch(headless=True)
        page=browser.new_page(viewport={'width':1900,'height':1600},device_scale_factor=1)
        errors=[];remote_requests=[]
        page.on('pageerror',lambda e:errors.append(str(e)))
        def offline(route):
            url=route.request.url
            if url.startswith(('http://','https://')):remote_requests.append(url);route.abort()
            else:route.continue_()
        page.route('**/*',offline)
        page.goto((output/'figure.html').as_uri(),wait_until='load',timeout=300000)
        page.wait_for_function('window.__geometryEditorReady===true && window.__textLayoutAudit && window.__tertiaryDisplayAudit.length===44',timeout=180000)
        page.evaluate("document.getElementById('geometry-panel').style.display='none'")
        page.locator('#svg').screenshot(path=str(output/'fig10_v37.png'))
        raw=page.locator('#svg').evaluate('e=>e.outerHTML')
        css='\n'.join(page.locator('style').all_text_contents())
        svg=raw.replace('<svg ','<svg xmlns="http://www.w3.org/2000/svg" ',1).replace('>','><style><![CDATA['+css+']]></style>',1)
        (output/'fig10_v37.svg').write_text('<?xml version="1.0" encoding="UTF-8"?>\n'+svg,encoding='utf-8')
        layout=page.evaluate('({classes:window.__tertiaryDisplayAudit,seas:window.__seaAudit,labels:window.__textLayoutAudit})')
        markers=page.locator('circle.theme-dot').evaluate_all("es=>es.map(e=>({radius:+e.getAttribute('r'),fill:getComputedStyle(e).fill,stroke:getComputedStyle(e).stroke}))")
        environment=dict(python=platform.python_version(),os=platform.platform(),chromium=browser.version,playwright=importlib.metadata.version('playwright'))
        browser.close()
    assert not errors,errors
    assert not remote_requests,remote_requests
    assert len(layout['classes'])==44 and len(layout['seas'])==11 and all(s['valid'] and s['connected'] for s in layout['seas'])
    assert len(markers)==44 and all(m['radius']==2.4 and m['fill']=='none' for m in markers)
    current=ET.fromstring(svg);reference=ET.parse(ROOT/'reference/fig10_v37.svg').getroot()
    assert [n.attrib for n in selected_nodes(current,'polygon','domain-cell')]==[n.attrib for n in selected_nodes(reference,'polygon','domain-cell')],'Base territory/sea cells changed'
    assert [n.attrib for n in selected_nodes(current,'path','theme-contour')]==[n.attrib for n in selected_nodes(reference,'path','theme-contour')],'Terrain contours changed'
    labels=layout['labels']
    collisions=[(a['text'],b['text']) for a,b in itertools.combinations(labels,2) if overlap(a['box'],b['box'])>.1]
    cropped=[a['text'] for a in labels if a['box']['x']< -500 or a['box']['y']< -500 or a['box']['x']+a['box']['width']>500 or a['box']['y']+a['box']['height']>500]
    non_english=[''.join(n.itertext()) for n in current.iter() if n.tag.split('}')[-1]=='text' and re.search(r'[\u3400-\u9fff]',''.join(n.itertext()))]
    original_labels=json.loads((ROOT/'reference/label_layout_audit.json').read_text(encoding='utf-8'))['labels']
    assert {(r['kind'],r['text']) for r in labels}=={(r['kind'],r['text']) for r in original_labels}
    def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
    png_identical=digest(output/'fig10_v37.png')==digest(ROOT/'reference/fig10_v37.png')
    label_positions_identical=labels==original_labels
    report=dict(inputs=inputs,environment=environment,network_requests=remote_requests,javascript_errors=errors,text_overlaps=collisions,cropped_labels=cropped,non_english_labels=non_english,markers=markers,base_cells_match=True,contours_match=True,labels_and_counts_match=True,label_positions_identical=label_positions_identical,png_byte_identical=png_identical,reference_png_sha256=digest(ROOT/'reference/fig10_v37.png'),rendered_png_sha256=digest(output/'fig10_v37.png'))
    (output/'verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    assert not collisions,collisions
    assert not cropped,cropped
    assert not non_english,non_english
    if args.strict_pixels:assert png_identical,'Pixel-exact reference requires the recorded browser, OS and Arial fonts; see README.'
    print(json.dumps({k:v for k,v in report.items() if k not in ['markers']},indent=2))


if __name__=='__main__':main()
