"""Standalone, offline leaderboard page (one HTML file, data embedded, no network).

Ranks derived/leaderboard.csv (overall and within each field), writes the ranked table to
artifact/agent_science_leaderboard.csv (also the online dashboard's data) and the page to
out/agent_science_leaderboard.html. Usage: python3 make_leaderboard_html.py
"""
import csv, json
from pathlib import Path
import style as S

ROOT = Path(__file__).parent
SRC = ROOT / "artifact" / "agent_science_leaderboard.csv"
OUT = ROOT / "out" / "agent_science_leaderboard.html"
KEEP = ["paper_id", "system", "title", "year", "fields", "status", "reach", "mechanism", "mechanism_label",
        "venue", "problem", "link", "rank_all"] + [f"rank_{f}" for f in S.FIELDS]

TEMPLATE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Agent-for-Science Problem Leaderboard</title>
<style>
  /* Layout: one centred column; summary, chart, then the full table. Neutral ink ramp for status. */
  :root {
    --bg: #f7f6f3; --panel: #ffffff; --fg: #1d1d1b; --muted: #66625a; --line: #dedad2; --soft: #efece6;
    --m-llm: #2f5fb3; --m-opt: #d9622b; --m-hyb: #1a9b74; --m-cls: #a8326e;
    --sans: -apple-system, BlinkMacSystemFont, "Segoe UI", "Helvetica Neue", Arial, "PingFang SC", "Microsoft YaHei", sans-serif;
    --serif: "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, "Songti SC", serif;
    --mono: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
    color-scheme: light;
  }
  @media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
    --bg: #0d0f12; --panel: #15181d; --fg: #ebe8e1; --muted: #9b968c; --line: #2a2e35; --soft: #1d2127;
    --m-llm: #4a86e8; --m-opt: #e2682a; --m-hyb: #22a884; --m-cls: #b8396f; color-scheme: dark; } }
  :root[data-theme="dark"] {
    --bg: #0d0f12; --panel: #15181d; --fg: #ebe8e1; --muted: #9b968c; --line: #2a2e35; --soft: #1d2127;
    --m-llm: #4a86e8; --m-opt: #e2682a; --m-hyb: #22a884; --m-cls: #b8396f; color-scheme: dark; }
  * { box-sizing: border-box; }
  body { margin: 0; background: var(--bg); color: var(--fg); font: 15px/1.5 var(--sans); }
  .wrap { max-width: 1280px; margin: 0 auto; padding-block: 32px 56px;
    padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px));
    display: grid; gap: 24px; }
  .eyebrow { margin: 0; font-size: 12px; letter-spacing: .08em; text-transform: uppercase; color: var(--muted); }
  h1 { margin: 4px 0 6px; font: 400 clamp(26px, 4vw, 38px)/1.15 var(--serif); text-wrap: balance; }
  .take { margin: 0; color: var(--muted); max-width: 72ch; }
  .take b { color: var(--fg); font-variant-numeric: tabular-nums; }
  .topbar { display: flex; flex-wrap: wrap; justify-content: space-between; gap: 12px; align-items: start; }
  .theme { font: inherit; font-size: 13px; color: var(--fg); background: var(--panel); border: 1px solid var(--line); border-radius: 8px; padding: 6px 10px; cursor: pointer; }
  .tiles { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 170px), 1fr)); gap: 12px; }
  .tile { background: var(--panel); border: 1px solid var(--line); border-radius: 10px; padding: 14px 18px; min-width: 0; }
  .tile p { margin: 0; }
  .tile .lab { font-size: 12px; color: var(--muted); }
  .tile .val { font: 400 34px/1.2 var(--serif); font-variant-numeric: tabular-nums; margin: 2px 0; }
  .tile .note { font-size: 12px; color: var(--muted); }
  .card { background: var(--panel); border: 1px solid var(--line); border-radius: 10px; padding: 20px; display: grid; gap: 14px; min-width: 0; }
  .card h2 { margin: 0; font-size: 17px; font-weight: 600; }
  .card .note { margin: 0; font-size: 13px; color: var(--muted); max-width: 82ch; }
  .legend { display: flex; flex-wrap: wrap; gap: 6px 16px; margin: 0; padding: 0; list-style: none; font-size: 12px; color: var(--muted); }
  .legend li { display: inline-flex; align-items: center; gap: 6px; }
  .sw { width: 12px; height: 12px; border-radius: 3px; display: inline-block; background: var(--fg); }
  .o-strong { opacity: .92; } .o-computed { opacity: .55; } .o-benchmark { opacity: .32; } .o-claim { opacity: .14; }
  .sw.o-notcoded { background: transparent; border: 1px solid var(--line); }
  .chart { position: relative; min-height: 320px; }
  .chart svg { display: block; max-width: 100%; }
  .chart .row { cursor: pointer; }
  .chart .row:hover .hit, .chart .row.on .hit { fill: var(--fg); fill-opacity: .05; }
  .tip { position: absolute; pointer-events: none; background: var(--panel); border: 1px solid var(--line); border-radius: 8px;
    box-shadow: 0 6px 22px rgba(0,0,0,.16); padding: 6px 10px; font-size: 12px; line-height: 1.5; white-space: nowrap; }
  .tip .h { color: var(--muted); }
  .controls { display: flex; flex-wrap: wrap; gap: 10px 14px; align-items: center; }
  select, input[type=search] { font: inherit; font-size: 14px; color: var(--fg); background: var(--bg); border: 1px solid var(--line); border-radius: 8px; padding: 6px 10px; min-width: 0; }
  input[type=search] { flex: 1 1 220px; }
  .chips { display: flex; flex-wrap: wrap; gap: 6px; }
  .chip { font: inherit; font-size: 12px; color: var(--fg); background: transparent; border: 1px solid var(--line); border-radius: 999px; padding: 3px 11px; cursor: pointer; }
  .chip[aria-pressed="true"] { background: var(--fg); color: var(--bg); border-color: var(--fg); }
  .reset { font: inherit; font-size: 12px; color: var(--muted); background: none; border: 0; text-decoration: underline; cursor: pointer; padding: 0; }
  .count { font-size: 12px; color: var(--muted); font-variant-numeric: tabular-nums; }
  :is(.chip, .reset, .theme, select, input, .sort, a):focus-visible { outline: 2px solid var(--fg); outline-offset: 2px; }
  .tablebox { max-height: 72vh; overflow: auto; border: 1px solid var(--line); border-radius: 8px; }
  table { border-collapse: collapse; width: 100%; font-size: 13px; }
  th { position: sticky; top: 0; z-index: 1; background: var(--panel); text-align: left; font-weight: 600; color: var(--muted); border-bottom: 1px solid var(--line); padding: 0; }
  .sort { font: inherit; color: inherit; background: none; border: 0; padding: 8px 10px; width: 100%; text-align: left; cursor: pointer; white-space: nowrap; }
  td { padding: 7px 10px; border-bottom: 1px solid var(--line); vertical-align: top; }
  tr:hover td { background: var(--soft); }
  td.num { text-align: right; font-variant-numeric: tabular-nums; color: var(--muted); }
  td.id { font-family: var(--mono); font-size: 12px; color: var(--muted); white-space: nowrap; }
  td.sys { font-weight: 600; min-width: 170px; }
  td.prob { min-width: 240px; max-width: 520px; color: var(--muted); }
  td.lnk { max-width: 220px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
  td.lnk a { color: var(--fg); }
  .pill { display: inline-block; border-radius: 999px; padding: 1px 9px; font-size: 12px; font-weight: 600; white-space: nowrap; border: 1px solid transparent; }
  .p-strong { background: var(--fg); color: var(--bg); }
  .p-computed { background: color-mix(in srgb, var(--fg) 48%, var(--panel)); color: var(--bg); }
  .p-benchmark { background: color-mix(in srgb, var(--fg) 18%, var(--panel)); color: var(--fg); }
  .p-claim { border-color: var(--line); color: var(--fg); }
  .p-notcoded { color: var(--muted); }
  .reach { display: inline-block; border: 1px solid var(--fg); border-radius: 999px; padding: 0 7px; font-size: 12px; font-weight: 600; }
  .dot { display: inline-block; width: 9px; height: 9px; border-radius: 50%; margin-right: 6px; vertical-align: middle; }
  dl.defs { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 250px), 1fr)); gap: 10px 26px; margin: 0; font-size: 13px; color: var(--muted); }
  dl.defs dt { color: var(--fg); font-weight: 600; }
  dl.defs dd { margin: 0; }
  footer { font-size: 12px; color: var(--muted); }
  @media (max-width: 720px) { .h-id, td.id, .h-mech, td.mech { display: none; } }
  @media (prefers-reduced-motion: no-preference) { .chart .bar { transition: opacity .2s; } }
</style>
</head>
<body>
<div class="wrap">
  <header>
    <div class="topbar">
      <p class="eyebrow">Agent-for-Science core corpus · snapshot 1 Nov 2026 · commit 60f8bad</p>
      <button class="theme" id="theme" type="button">Switch theme</button>
    </div>
    <h1>Agent-for-Science problem leaderboard</h1>
    <p class="take" id="take">Loading…</p>
  </header>

  <section class="tiles" aria-label="Headline figures">
    <div class="tile"><p class="lab">Papers</p><p class="val" id="v-papers">–</p><p class="note">core papers in this scope</p></div>
    <div class="tile"><p class="lab">Strongly verified</p><p class="val" id="v-closed">–</p><p class="note">V3–V4: experiment, proof or replication</p></div>
    <div class="tile"><p class="lab">Share strong</p><p class="val" id="v-share">–</p><p class="note">of coded papers</p></div>
    <div class="tile"><p class="lab">Problem stated</p><p class="val" id="v-prob">–</p><p class="note">papercards quoting the scientific problem</p></div>
  </section>

  <section class="card" id="status-by-field">
    <h2>Solution status by field</h2>
    <p class="note">Papers per field by evidence endpoint. A paper assigned to several fields counts in each. Click a field to filter the leaderboard; click it again to clear.</p>
    <ul class="legend">
      <li><span class="sw o-strong"></span>Strong (V3–V4)</li>
      <li><span class="sw o-computed"></span>Computed</li>
      <li><span class="sw o-benchmark"></span>Benchmark / internal (V1)</li>
      <li><span class="sw o-claim"></span>Claim only (V0)</li>
      <li><span class="sw o-notcoded"></span>Not coded</li>
    </ul>
    <div class="chart" id="chart"></div>
  </section>

  <section class="card" id="leaderboard">
    <h2>Leaderboard</h2>
    <p class="note">Ranked by verification strength (strong V3–V4, computed V2, benchmark V1, claim V0), then system autonomy (L3 first), then the earliest year. The rank is within the chosen field, or across the whole corpus. Click a column heading to sort.</p>
    <div class="controls">
      <select id="field" aria-label="Field"></select>
      <div class="chips" id="chips" role="group" aria-label="Status"></div>
      <input id="q" type="search" placeholder="Search system, problem or ID" aria-label="Search">
      <button class="reset" id="reset" type="button">Reset</button>
      <span class="count" id="count"></span>
    </div>
    <div class="tablebox"><table id="table"><thead></thead><tbody></tbody></table></div>
  </section>

  <section class="card" id="definitions">
    <h2>How to read the leaderboard</h2>
    <dl class="defs">
      <div><dt>Strong (V3–V4)</dt><dd>V3: a physical or prospective experiment by the authors covering the core claim. V4: a machine-checked formal proof or third-party replication. As self-reported in the paper.</dd></div>
      <div><dt>Computed (V2)</dt><dd>Computational or simulation validation, retrospective real data, or expert checking of a specific conclusion.</dd></div>
      <div><dt>Benchmark (V1) · Claim (V0)</dt><dd>Benchmark scores, ablations, LLM-judge or expert rating of output quality; or a demonstration with no systematic evaluation.</dd></div>
      <div><dt>Autonomy L0–L3</dt><dd>L1 task assistant, L2 closed-loop executor within a human-set goal, L3 autonomous researcher that chooses what to study.</dd></div>
      <div><dt>Mechanism</dt><dd>The paper's single dominant decision mechanism (D1–D6), from the 3 Nov 2026 classification.</dd></div>
      <div><dt>Problem</dt><dd>Quoted verbatim from the paper's papercard (section 最终科学问题); blank where the papercard has none.</dd></div>
    </dl>
  </section>
  <footer>Built by make_leaderboard_html.py from the project's classification records (core manifest, decision-mechanism table, papers.jsonl, papercard notes). No data leaves this file.</footer>
</div>

<script id="data" type="application/json">__DATA__</script>
<script>
(() => {
  const ROWS = JSON.parse(document.getElementById('data').textContent);
  const FIELDS = __FIELDS__;
  const ORDER = __ORDER__;                                  // explicit: JS would put '10','11' before '01'
  const STATUS = ['strong', 'computed', 'benchmark', 'claim', 'not coded'];
  const MECH_VAR = {'LLM-driven': '--m-llm', 'Optimization': '--m-opt', 'Hybrid': '--m-hyb',
                    'Planning': '--m-cls', 'Symbolic': '--m-cls', 'Learned policy': '--m-cls'};
  const fmt = (n) => Number(n).toLocaleString('en');
  const state = {field: 'all', status: 'all', q: '', sort: null, dir: 1};
  const $ = (id) => document.getElementById(id);
  const inField = (r, f) => f === 'all' || r.fields.split(';').includes(f);
  const el = (tag, cls, text) => { const e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; };

  // theme toggle (remembered per browser when storage is available)
  const root = document.documentElement;
  try { const t = localStorage.getItem('lb-theme'); if (t) root.dataset.theme = t; } catch (e) {}
  $('theme').addEventListener('click', () => {
    const dark = root.dataset.theme ? root.dataset.theme === 'dark' : matchMedia('(prefers-color-scheme: dark)').matches;
    root.dataset.theme = dark ? 'light' : 'dark';
    try { localStorage.setItem('lb-theme', root.dataset.theme); } catch (e) {}
    drawChart();
  });

  // controls
  const fsel = $('field');
  fsel.appendChild(new Option('All fields', 'all'));
  ORDER.forEach((k) => fsel.appendChild(new Option(k + ' ' + FIELDS[k], k)));
  fsel.addEventListener('change', () => { state.field = fsel.value; render(); });
  ['all', ...STATUS.slice(0, 4)].forEach((s) => {
    const b = el('button', 'chip', s === 'all' ? 'All statuses' : s[0].toUpperCase() + s.slice(1));
    b.type = 'button'; b.dataset.s = s;
    b.addEventListener('click', () => { state.status = s; render(); });
    $('chips').appendChild(b);
  });
  $('q').addEventListener('input', (e) => { state.q = e.target.value.trim().toLowerCase(); renderTable(); });
  $('reset').addEventListener('click', () => { Object.assign(state, {field: 'all', status: 'all', q: '', sort: null, dir: 1}); $('q').value = ''; render(); });

  function scopeRows() { return ROWS.filter((r) => inField(r, state.field)); }

  function renderSummary() {
    const rows = scopeRows();
    const coded = rows.filter((r) => r.status !== 'not coded').length;
    const closed = rows.filter((r) => r.status === 'strong').length;
    $('v-papers').textContent = fmt(rows.length);
    $('v-closed').textContent = fmt(closed);
    $('v-share').textContent = coded ? Math.round(100 * closed / coded) + '%' : '–';
    $('v-prob').textContent = fmt(rows.filter((r) => r.problem.trim()).length);
    const rk = state.field === 'all' ? 'rank_all' : 'rank_' + state.field;
    const top = rows.find((r) => String(r[rk]) === '1');
    const take = $('take'); take.replaceChildren();
    take.append('In ' + (state.field === 'all' ? 'the whole corpus' : FIELDS[state.field]) + ', ',
      el('b', null, fmt(closed)), ' of ', el('b', null, fmt(coded)),
      ' papers are strongly verified (V3–V4: physical experiment, formal proof or third-party replication).');
    if (top) take.append(' The top-ranked entry is ', el('b', null, top.system), ' (' + top.year + ').');
  }

  function drawChart() {
    const box = $('chart'); box.replaceChildren();
    const css = getComputedStyle(root);
    const fg = css.getPropertyValue('--fg').trim(), muted = css.getPropertyValue('--muted').trim(), line = css.getPropertyValue('--line').trim();
    const data = ORDER.map((f) => {
      const rs = ROWS.filter((r) => inField(r, f));
      const c = (s) => rs.filter((r) => r.status === s).length;
      return {f, n: rs.length, strong: c('strong'), computed: c('computed'), benchmark: c('benchmark'), claim: c('claim'), notcoded: c('not coded')};
    });
    const W = Math.round(box.getBoundingClientRect().width);
    if (W < 40) return;                                   // not laid out yet; the ResizeObserver redraws
    const rowH = 28, top = 4, lab = Math.min(230, W * 0.38), right = 46;
    const H = top + data.length * rowH + 24;
    const max = Math.max(...data.map((d) => d.n));
    const step = max > 150 ? 50 : max > 60 ? 25 : 10;
    const x = (v) => lab + (W - right - lab) * v / max;
    const NS = 'http://www.w3.org/2000/svg';
    const mk = (t, a) => { const e = document.createElementNS(NS, t); Object.entries(a).forEach(([k, v]) => e.setAttribute(k, v)); return e; };
    const svg = mk('svg', {viewBox: `0 0 ${W} ${H}`, width: W, height: H, role: 'img', 'aria-label': 'Papers per field by evidence endpoint'});
    for (let t = 0; t <= max; t += step) {
      svg.appendChild(mk('line', {x1: x(t), x2: x(t), y1: top, y2: H - 20, stroke: line, 'stroke-width': 1}));
      const tx = mk('text', {x: x(t), y: H - 5, 'text-anchor': 'middle', 'font-size': 11, fill: muted}); tx.textContent = fmt(t); svg.appendChild(tx);
    }
    const tip = el('div', 'tip'); tip.hidden = true;
    const op = {strong: .92, computed: .55, benchmark: .32, claim: .14};
    data.forEach((d, i) => {
      const g = mk('g', {class: 'row' + (d.f === state.field ? ' on' : ''), transform: `translate(0 ${top + i * rowH})`, tabindex: 0, role: 'button',
                          'aria-label': FIELDS[d.f] + ', ' + d.n + ' papers'});
      g.appendChild(mk('rect', {class: 'hit', x: 0, y: 0, width: W, height: rowH, fill: 'transparent'}));
      const t = mk('text', {x: lab - 8, y: rowH / 2 + 4, 'text-anchor': 'end', 'font-size': 12, fill: fg}); t.textContent = d.f + '  ' + FIELDS[d.f]; g.appendChild(t);
      let x0 = x(0);
      ['strong', 'computed', 'benchmark', 'claim', 'notcoded'].forEach((k) => {
        const w = x(d[k]) - x(0); if (w <= 0) return;
        g.appendChild(mk('rect', {class: 'bar', x: x0, y: 6, width: Math.max(0, w - 1), height: rowH - 12, rx: 2,
          fill: k === 'notcoded' ? 'none' : fg, 'fill-opacity': op[k] || 0, stroke: (k === 'notcoded' || k === 'claim') ? line : 'none'}));
        x0 += w;
      });
      const v = mk('text', {x: x0 + 6, y: rowH / 2 + 4, 'font-size': 11, fill: muted}); v.textContent = fmt(d.n); g.appendChild(v);
      const pick = () => { state.field = state.field === d.f ? 'all' : d.f; render(); };
      g.addEventListener('click', pick);
      g.addEventListener('keydown', (e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); pick(); } });
      g.addEventListener('mousemove', (e) => {
        const r = box.getBoundingClientRect();
        tip.replaceChildren(el('div', 'h', FIELDS[d.f] + ' · ' + fmt(d.n) + ' papers'),
          ...[['Strong', d.strong], ['Computed', d.computed], ['Benchmark', d.benchmark], ['Claim only (V0)', d.claim], ['Not coded', d.notcoded]]
            .map(([a, b]) => el('div', null, a + ': ' + fmt(b))));
        tip.hidden = false;
        const tw = tip.offsetWidth;
        tip.style.left = Math.min(Math.max(0, e.clientX - r.left + 12), box.clientWidth - tw) + 'px';
        tip.style.top = (e.clientY - r.top + 12) + 'px';
      });
      g.addEventListener('mouseleave', () => { tip.hidden = true; });
      svg.appendChild(g);
    });
    box.append(svg, tip);
  }

  const COLS = [
    {k: 'rank', label: '#', cls: 'num', num: true},
    {k: 'paper_id', label: 'ID', cls: 'id', h: 'h-id'},
    {k: 'system', label: 'System', cls: 'sys'},
    {k: 'year', label: 'Year', cls: 'num', num: true},
    {k: 'status', label: 'Status'},
    {k: 'reach', label: 'Reach'},
    {k: 'mechanism_label', label: 'Mechanism', cls: 'mech', h: 'h-mech'},
    {k: 'problem', label: 'Problem (papercard)', cls: 'prob'},
    {k: 'link', label: 'Link', cls: 'lnk'},
  ];
  function renderTable() {
    const rk = state.field === 'all' ? 'rank_all' : 'rank_' + state.field;
    let rows = scopeRows().filter((r) => (state.status === 'all' || r.status === state.status)
      && (!state.q || [r.system, r.title, r.problem, r.paper_id].some((v) => String(v).toLowerCase().includes(state.q))));
    const val = (r, k) => k === 'rank' ? Number(r[rk]) : k === 'year' ? Number(r.year) : String(r[k] || '');
    const by = state.sort || 'rank';
    rows = rows.slice().sort((a, b) => {
      const va = val(a, by), vb = val(b, by);
      const c = typeof va === 'number' ? va - vb : va.localeCompare(vb);
      return (c || Number(a[rk]) - Number(b[rk])) * (state.sort ? state.dir : 1);
    });
    const thead = $('table').tHead; thead.replaceChildren();
    const hr = thead.insertRow();
    COLS.forEach((c) => {
      const th = el('th', c.h || null);
      th.setAttribute('aria-sort', state.sort === c.k ? (state.dir > 0 ? 'ascending' : 'descending') : 'none');
      const b = el('button', 'sort', c.label + (state.sort === c.k ? (state.dir > 0 ? ' ↑' : ' ↓') : ''));
      b.type = 'button';
      b.addEventListener('click', () => { state.dir = state.sort === c.k ? -state.dir : 1; state.sort = c.k; renderTable(); });
      th.appendChild(b); hr.appendChild(th);
    });
    const tb = $('table').tBodies[0]; tb.replaceChildren();
    const frag = document.createDocumentFragment();
    rows.forEach((r) => {
      const tr = document.createElement('tr');
      COLS.forEach((c) => {
        const td = el('td', c.cls || null);
        const v = c.k === 'rank' ? String(r[rk]) : String(r[c.k] || '');
        if (c.k === 'status') td.appendChild(el('span', 'pill p-' + v.replace(' ', ''), v));
        else if (c.k === 'reach') { if (v) td.appendChild(el('span', 'reach', v)); }
        else if (c.k === 'mechanism_label') { const d = el('span', 'dot'); d.style.background = 'var(' + (MECH_VAR[v] || '--muted') + ')'; td.append(d, v + ' · ' + r.mechanism); }
        else if (c.k === 'system') { td.textContent = v; td.title = r.title; }
        else if (c.k === 'link') { if (/^https?:\/\//i.test(v)) { const a = el('a', null, v); a.href = v; a.target = '_blank'; a.rel = 'noopener noreferrer'; td.appendChild(a); } else td.textContent = v; }
        else td.textContent = v;
        tr.appendChild(td);
      });
      frag.appendChild(tr);
    });
    tb.appendChild(frag);
    $('count').textContent = fmt(rows.length) + ' papers shown';
  }

  function render() {
    fsel.value = state.field;
    document.querySelectorAll('.chip').forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.s === state.status)));
    renderSummary(); drawChart(); renderTable();
  }
  let lastW = 0;
  new ResizeObserver(([e]) => {                           // redraw the chart at its real width
    const w = Math.round(e.contentRect.width);
    if (w !== lastW) { lastW = w; drawChart(); }
  }).observe($('chart'));
  render();
})();
</script>
</body>
</html>
"""


ST = {"E3": "strong", "E2": "computed", "E1": "benchmark", "E0": "claim", "": "not coded"}
MECH = {"D1": "Symbolic", "D2": "Planning", "D3": "Optimization", "D4": "Learned policy", "D5": "LLM-driven", "D6": "Hybrid"}


def ranked():
    """Rows with ranks: evidence endpoint, then reach (L4 first), then earliest year, then ID."""
    rows = list(csv.DictReader(open(S.DER / "leaderboard.csv", encoding="utf-8")))
    cards = {c["paper_id"]: c for c in S.papercards()}
    key = lambda r: (-(int(r["evidence_tier"][1:]) if r["evidence_tier"] else -1),
                     -(int(r["loop_reach"][1:]) if r["loop_reach"] else -1), int(r["year"]), r["paper_id"])
    out = {r["paper_id"]: dict(paper_id=r["paper_id"], system=r["system"], title=cards[r["paper_id"]]["title"],
                               year=r["year"], fields=r["field"], status=ST[r["evidence_tier"]],
                               evidence_tier=r["evidence_tier"], reach=r["loop_reach"], mechanism=r["mechanism"],
                               mechanism_label=MECH[r["mechanism"]], venue=r["venue"], problem=r["problem"],
                               link=r["link"]) for r in rows}
    for i, r in enumerate(sorted(rows, key=key), 1):
        out[r["paper_id"]]["rank_all"] = i
    for f in S.FIELDS:
        for i, r in enumerate(sorted([r for r in rows if f in r["field"].split(";")], key=key), 1):
            out[r["paper_id"]][f"rank_{f}"] = i
    return sorted(out.values(), key=lambda r: r["rank_all"])


def main():
    rows = ranked()
    cols = KEEP[:6] + ["evidence_tier"] + KEEP[6:]
    SRC.parent.mkdir(exist_ok=True)
    with open(SRC, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols); w.writeheader()
        w.writerows({c: r.get(c, "") for c in cols} for r in rows)
    rows = [{k: str(r.get(k, "")) for k in KEEP} for r in rows]
    data = json.dumps(rows, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    html = TEMPLATE.replace("__DATA__", data).replace("__FIELDS__", json.dumps(S.FNAME, ensure_ascii=False))
    html = html.replace("__ORDER__", json.dumps(S.FIELDS))
    OUT.write_text(html, encoding="utf-8")
    print(OUT, len(html.encode()) // 1024, "KB", len(rows), "rows")


if __name__ == "__main__":
    main()
