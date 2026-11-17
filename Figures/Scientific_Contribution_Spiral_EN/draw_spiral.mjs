// Geometry is executed using the original Charticulator MIT implementation.
// Layout, typography and simulated data are specific to this scientific figure.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import assert from 'node:assert/strict';
import * as native from './vendor/charticulator/native_geometry.mjs';

const root = path.dirname(fileURLToPath(import.meta.url));
const data = JSON.parse(fs.readFileSync(path.join(root, 'data', 'figure_data.json'), 'utf8'));
fs.mkdirSync(path.join(root,'outputs'),{recursive:true});
const cfg = JSON.parse(fs.readFileSync(path.join(root, 'figure_config.json'), 'utf8'));
const tau = Math.PI * 2, turns = data.periods.length, domainCount = data.fields.length;
const sector = tau / domainCount, startAngle = -Math.PI / 2;
const pitch = cfg.turn_spacing, innerRadius = cfg.inner_radius;
const b = pitch / tau, a = innerRadius - b * startAngle;
const maker = new native.PathMaker();
maker.archimedeanSpiral(0, 0, a, b, startAngle, startAngle + turns*tau, true);
const segments = [];
let previous;
for (const c of maker.path.cmds) {
  if (c.cmd === 'M') previous = {x:c.args[0], y:c.args[1]};
  if (c.cmd === 'C') {
    const q = c.args, end = {x:q[4], y:q[5]};
    segments.push(new native.BezierCurveParameterization(previous,
      {x:q[0],y:q[1]}, {x:q[2],y:q[3]}, end));
    previous = end;
  }
}
const curve = new native.MultiCurveParametrization(segments);
const cs = new native.BezierCurveCoordinates({x:0,y:0}, curve);
const helper = new native.CoordinateSystemHelper(cs);
const offsets = [0];
for (const seg of segments) offsets.push(offsets.at(-1) + seg.getLength());
const length = curve.getLength();
function sAtTurns(t) {
  const x = Math.min(segments.length - 1e-9, Math.max(0, t / turns * segments.length));
  const k = Math.floor(x);
  return offsets[k] + segments[k].getSFromT(x-k);
}
function d(element) {
  return element.cmds.map(c => c.cmd + c.args.map(v => {
    assert(Number.isFinite(v)); return v.toFixed(3);
  }).join(' ')).join(' ');
}
const esc = s => String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&apos;'}[c]));
const f = x => Number(x).toFixed(3);
const polar = (r,t) => ({x:r*Math.cos(t),y:r*Math.sin(t)});
const text = (x,y,value,attrs='') => `<text x="${f(x)}" y="${f(y)}" ${attrs}>${esc(value)}</text>`;
const line = (x1,y1,x2,y2,attrs='') => `<line x1="${f(x1)}" y1="${f(y1)}" x2="${f(x2)}" y2="${f(y2)}" ${attrs}/>`;
function arc(radius, t1, t2) {
  const p = polar(radius,t1), q = polar(radius,t2);
  return `M${f(p.x)} ${f(p.y)} A${radius} ${radius} 0 ${t2-t1>Math.PI?1:0} 1 ${f(q.x)} ${f(q.y)}`;
}

const backgrounds=[], bars=[], guides=[], labels=[], outer=[], eraLabels=[], defs=[];
const positions=[], colors=new Set(), padding=cfg.sector_padding_deg*Math.PI/180;
const valueMap = new Map(data.records.map(r=>[r.secondary_code+'@'+r.period_index,r]));

data.fields.forEach((field, di) => {
  const n = field.classes.length, usable = sector - 2*padding, slot = usable/n;
  const fieldStart = startAngle + di*sector;
  const mid = fieldStart + sector/2;
  if (cfg.show_sector_guides) {
    const p = polar(cfg.secondary_label_radius+18,fieldStart);
    const q = polar(cfg.domain_bracket_radius-18,fieldStart);
    guides.push(line(p.x,p.y,q.x,q.y,'stroke="#E2E6E9" stroke-width="1"'));
  }
  outer.push(`<path d="${arc(cfg.domain_bracket_radius,fieldStart+padding,fieldStart+sector-padding)}" fill="none" stroke="#9AA7B0" stroke-width="1.35"/>`);
  for (const t of [fieldStart+padding,fieldStart+sector-padding]) {
    const p=polar(cfg.domain_bracket_radius-5,t),q=polar(cfg.domain_bracket_radius+5,t);
    outer.push(line(p.x,p.y,q.x,q.y,'stroke="#9AA7B0" stroke-width="1.35"'));
  }
  const op = polar(cfg.domain_label_radius,mid);
  let domainRotation = mid*180/Math.PI+90;
  if (Math.sin(mid)>0) domainRotation += 180;
  outer.push(`<text transform="translate(${f(op.x)} ${f(op.y)}) rotate(${f(domainRotation)})" font-size="${cfg.domain_font_size}" font-weight="600" text-anchor="middle" dominant-baseline="central" fill="#263B48">${esc(field.field_name)}</text>`);

  field.classes.forEach((cat, ci) => {
    const local = padding+(ci+.5)*slot;
    const theta = fieldStart+local;
    const phase = (di*sector+local)/tau;
    const barAngle = slot*cfg.bar_fill_fraction;
    const p = polar(cfg.secondary_label_radius,theta);
    const rotation = theta*180/Math.PI + (Math.cos(theta)<0 ? 180 : 0);
    const anchor = Math.cos(theta)<0 ? 'start' : 'end';
    const marker=polar(cfg.secondary_label_radius+11,theta);
    const labelFont = cat.display_font_size || cfg.secondary_font_size;
    labels.push(`<text class="secondary-label interactive" data-code="${cat.code}" transform="translate(${f(p.x)} ${f(p.y)}) rotate(${f(rotation)})" font-size="${labelFont}" text-anchor="${anchor}" dominant-baseline="central" fill="#3C4F5C">${esc(cat.name)}</text>`);
    labels.push(`<circle cx="${f(marker.x)}" cy="${f(marker.y)}" r="3.7" fill="${cat.color}"/>`);
    colors.add(cat.color);
    for (let era=0; era<turns; era++) {
      const r=valueMap.get(cat.code+'@'+era);
      const s1=sAtTurns(era+phase-barAngle/(2*tau));
      const s2=sAtTurns(era+phase+barAngle/(2*tau));
      const height = r.mean_score/100*cfg.max_bar_height;
      const shadow = helper.rect(s1,-cfg.max_bar_height,s2,0);
      const shape = helper.rect(s1,-height,s2,0);
      if (cfg.show_full_scale_background) backgrounds.push(`<path d="${d(shadow)}" fill="#EFF1F3"/>`);
      bars.push(`<path class="score-bar interactive" data-code="${cat.code}" data-period="${era}" d="${d(shape)}" fill="${cat.color}"><title>${esc(field.field_name+' / '+cat.name+'\n'+data.periods[era]+': '+r.mean_score+' points (simulated)')}</title></path>`);
      positions.push({secondary_code:cat.code, era, angle_phase:phase,
        angular_width:barAngle, score:r.mean_score, color:cat.color,
        geometric_height:height, curve_s1:s1,curve_s2:s2});
    }
  });
});

for(let era=0;era<turns;era++) {
  const start = sAtTurns(era+.010), end = sAtTurns(era+.068);
  const id='era-path-'+era;
  defs.push(`<path id="${id}" d="${d(helper.line(start,15,end,15))}"/>`);
  eraLabels.push(`<text font-size="18" fill="#465B68" font-weight="500" paint-order="stroke" stroke="white" stroke-width="4" stroke-linejoin="round"><textPath href="#${id}" startOffset="50%" text-anchor="middle">${esc(data.periods[era])}</textPath></text>`);
}

const center = [
  text(0,-81,'Mean contribution score','text-anchor="middle" fill="#536774" font-size="24"'),
  text(0,-26,'0–100','text-anchor="middle" fill="#263B48" font-size="43" font-weight="500"'),
  text(0,14,'Time progresses outward','text-anchor="middle" fill="#6A7A84" font-size="18"'),
  `<rect x="-39" y="51" width="23" height="72" fill="#EFF1F3"/>`,
  `<rect x="-39" y="87" width="23" height="36" fill="#1F78B4"/>`,
  line(-12,51,-3,51,'stroke="#93A0A8"'),
  line(-12,87,-3,87,'stroke="#93A0A8"'),
  line(-12,123,-3,123,'stroke="#93A0A8"'),
  text(6,56,'100','font-size="16" fill="#637580"'),
  text(6,92,'50','font-size="16" fill="#637580"'),
  text(6,128,'0','font-size="16" fill="#637580"'),
  text(0,162,'Pale gray: 100-point reference','text-anchor="middle" fill="#81909A" font-size="15"')
].join('\n');

const baseline = helper.line(0,0,length,0);
assert.equal(data.records.length,240);
assert.equal(colors.size,48);
assert.equal(baseline.cmds.filter(c=>c.cmd==='M').length,1);
assert.equal(baseline.cmds.filter(c=>c.cmd==='Z').length,0);
assert(cfg.max_bar_height<cfg.turn_spacing);
for(const field of data.fields) {
  for(let era=0;era<turns;era++) {
    const group=positions.filter(p=>p.era===era&&p.secondary_code.startsWith(field.field_code+'.'));
    assert.equal(new Set(group.map(p=>p.angular_width)).size,1);
  }
}
for(const cat of data.fields.flatMap(f=>f.classes)) {
  const group=positions.filter(p=>p.secondary_code===cat.code);
  assert.equal(group.length,5);
  assert.equal(new Set(group.map(p=>p.color)).size,1);
  assert.equal(new Set(group.map(p=>p.angle_phase)).size,1);
}

const svg=`<svg xmlns="http://www.w3.org/2000/svg" width="${cfg.width}" height="${cfg.height}" viewBox="0 0 ${cfg.width} ${cfg.height}" role="img" aria-labelledby="title description">
<title id="title">The Temporal Spiral of Scientific Contribution (Simulated Data)</title>
<desc id="description">Five historical periods, 11 fixed domain sectors, and 48 second-level categories. Bar heights represent simulated mean scientific contribution scores; category colors remain fixed across periods. All 240 values are illustrative.</desc>
<style>text{font-family:"Arial","Helvetica",sans-serif}.score-bar{transition:opacity .12s}.muted{opacity:.12}.highlight{filter:brightness(.92)}.secondary-label{cursor:default}</style>
<defs>${defs.join('\n')}</defs>
<rect width="100%" height="100%" fill="white"/>
${text(cfg.width/2,66,'The Temporal Spiral of Scientific Contribution','text-anchor="middle" font-size="35" font-weight="600" fill="#243B49"')}
${text(cfg.width/2,105,'11 domains | 48 second-level categories | 5 historical periods','text-anchor="middle" font-size="20" fill="#667B88"')}
<g transform="translate(${cfg.center_x} ${cfg.center_y})">
<g id="guides">${guides.join('\n')}</g>
<g id="full-scale-backgrounds">${backgrounds.join('\n')}</g>
<g id="score-bars">${bars.join('\n')}</g>
<path id="continuous-spiral-baseline" d="${d(baseline)}" stroke="#586A76" stroke-width="1.35" fill="none"/>
<g id="secondary-names">${labels.join('\n')}</g>
<g id="domain-names">${outer.join('\n')}</g>
<g id="period-names">${eraLabels.join('\n')}</g>
<g id="scale-legend">${center}</g>
</g>
${text(cfg.width/2,cfg.height-55,'SIMULATED DATA | Bar height = mean contribution score; category positions and colors are fixed across periods.','text-anchor="middle" font-size="19" fill="#667B88"')}
${text(cfg.width/2,cfg.height-23,'Palette adapted from the Charticulator gallery: 7 original base colors extended to 48 category colors.','text-anchor="middle" font-size="16" fill="#8A979F"')}
</svg>`;
fs.writeFileSync(path.join(root,'outputs','scientific_contribution_spiral_EN.svg'),svg);

const table=data.fields.map(field=>`<section><h2>${esc(field.field_name)}</h2><table><thead><tr><th>Second-level category</th><th>Hex color</th>${data.periods.map(p=>`<th>${esc(p)}</th>`).join('')}</tr></thead><tbody>${field.classes.map(cat=>`<tr data-code="${cat.code}"><td><i style="background:${cat.color}"></i>${esc(cat.name)}</td><td><code>${cat.color}</code></td>${data.periods.map((_,i)=>`<td>${valueMap.get(cat.code+'@'+i).mean_score.toFixed(1)}</td>`).join('')}</tr>`).join('')}</tbody></table></section>`).join('');
const html=`<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Scientific Contribution Spiral | Simulated Data</title><style>
*{box-sizing:border-box}body{margin:0;background:#fff;color:#263b48;font-family:"Arial",sans-serif}.toolbar{display:flex;align-items:center;justify-content:center;gap:15px;padding:13px;border-bottom:1px solid #edf0f2;font-size:13px;color:#71828d}a{color:#416b84;text-decoration:none}button{border:1px solid #d9e1e6;padding:6px 14px;background:#fff;border-radius:4px;color:#416b84;cursor:pointer}#frame{overflow:auto;text-align:center}#chart{width:min(100%,1440px);margin:auto;display:block}#chart svg{display:block;width:100%;height:auto}#chart.zoom{width:2400px;max-width:none}.data{max-width:1180px;margin:20px auto 80px;padding:0 25px}summary{cursor:pointer;color:#526d7d;font-size:14px}h2{font-size:17px;margin-top:28px}table{border-collapse:collapse;width:100%;font-size:13px}th,td{text-align:left;padding:9px 12px;border-bottom:1px solid #edf0f2}th{color:#71828d;font-weight:400}i{display:inline-block;width:12px;height:12px;margin-right:10px;vertical-align:-1px;border-radius:2px}tr{cursor:default}#tooltip{display:none;position:fixed;pointer-events:none;z-index:5;padding:10px 13px;border:1px solid #dce4ea;box-shadow:0 5px 20px #243b4914;border-radius:6px;background:#fffffff2;font-size:13px;line-height:1.7;color:#354e5e;white-space:pre-line}
</style><div class="toolbar"><span>Simulated data | Hover over a category to highlight all five periods</span><button id="zoom">Zoom in</button><a href="scientific_contribution_spiral_EN.svg">Vector SVG</a><a href="../data/simulated_category_means.csv">Mock data CSV</a></div><div id="frame"><div id="chart">${svg}</div></div><div id="tooltip"></div><div class="data"><details><summary>Show category colors and simulated scores for all five periods</summary><p>All values are simulated category means for layout evaluation, not measured paper scores. Color identifies categories, not score magnitude.</p>${table}</details></div><script>
const all=[...document.querySelectorAll('.interactive')], tooltip=document.querySelector('#tooltip');
function highlight(code){all.forEach(e=>{e.classList.toggle('muted',!!code&&e.dataset.code!==code);e.classList.toggle('highlight',!!code&&e.dataset.code===code)})}
all.forEach(e=>{e.addEventListener('mouseenter',()=>{highlight(e.dataset.code);const t=e.querySelector('title');if(t){tooltip.textContent=t.textContent;tooltip.style.display='block'}});e.addEventListener('mouseleave',()=>{highlight(null);tooltip.style.display='none'});e.addEventListener('mousemove',ev=>{tooltip.style.left=Math.min(ev.clientX+16,innerWidth-300)+'px';tooltip.style.top=Math.min(ev.clientY+16,innerHeight-90)+'px'})});
document.querySelector('#zoom').onclick=()=>{document.querySelector('#chart').classList.toggle('zoom');document.querySelector('#zoom').textContent=document.querySelector('#chart').classList.contains('zoom')?'Fit to window':'Zoom in'};
document.querySelectorAll('tr[data-code]').forEach(e=>{e.onmouseenter=()=>highlight(e.dataset.code);e.onmouseleave=()=>highlight(null)});
</script></html>`;
fs.writeFileSync(path.join(root,'outputs','scientific_contribution_spiral_EN.html'),html);
fs.writeFileSync(path.join(root,'outputs','geometry_checks.json'),JSON.stringify({
  passed:true,simulated:true,total_bars:positions.length,secondary_classes:colors.size,domains:domainCount,periods:turns,
  equal_angular_width_within_each_domain:true,category_angles_fixed_across_periods:true,
  one_color_per_category_across_periods:true,height_scale_0_100:cfg.max_bar_height,
  continuous_baseline_subpaths:1,strict_closed_rings:false,
  native_geometry:'Microsoft Charticulator MIT algorithms; full editor not rebuilt',
  layout:positions
},null,2));
console.log(JSON.stringify({passed:true,bars:positions.length,colors:colors.size,periods:turns}));
