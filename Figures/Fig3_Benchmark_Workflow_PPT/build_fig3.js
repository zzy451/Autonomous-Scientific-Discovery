// Fig. 3 (fig:benchmark) — "flow" redesign as one editable PowerPoint slide, Nature double column 183 x 170 mm.
// Rules kept: Arial 7 pt text (panel letters 8 pt bold), black/white text only, Wong colour-blind-safe accents,
// icons only for actors/objects. Visual idea: weights are ribbon widths (a: rubric tree, b: RCI confluence);
// Composite, O/V/L and RCI arrive at the report as separate streams.
// Usage: node build_fig3.js out.pptx
const pptxgen = require("pptxgenjs");
const React = require("react");
const RDS = require("react-dom/server");
const lu = require("react-icons/lu");
const sharp = require("sharp");

const W = 7.205, H = 8.21, L = 0.12, R = W - 0.12, FS = 7;
const INK = "1A1A1A", WHITE = "FFFFFF", ICON = "34404C", LINE = "6F7C89";
const SL = { d: "2C3E50", l: "E4E9EF", p: "F2F4F7", line: "8E9BA8" };
const BR_COL = ["3E5871", "56718A", "7088A0", "8BA0B5", "A9BACB"];   // slate ramp for B1..B5
const BR_TXT = [WHITE, WHITE, INK, INK, INK];
const O = { c: "0072B2", t: WHITE, p: "E3EFF7" }, V = { c: "CC79A7", t: INK, p: "F8EBF2" }, Lc = { c: "009E73", t: INK, p: "DFF2EC" };
const AM = { c: "E69F00", p: "FBE9C6", line: "B8955A" };

const pres = new pptxgen();
pres.defineLayout({ name: "NATURE183", width: W, height: H });
pres.layout = "NATURE183";
pres.title = "Paper-level scientific contribution scoring and RCI workflow";
const s = pres.addSlide();
s.background = { color: WHITE };

let n = 0;
const nm = (p) => `${p}_${++n}`;
const R_ = (text, opt = {}) => ({ text, options: opt });
function box(x, y, w, h, o = {}) {
  s.addShape(o.shape || pres.shapes.ROUNDED_RECTANGLE, {
    x, y, w, h, rectRadius: o.r ?? 0.04,
    fill: o.fill ? { color: o.fill, transparency: o.tr ?? 0 } : { type: "none" },
    line: o.line ? { color: o.line, width: o.lw ?? 0.5, dashType: o.dash ? "dash" : "solid" } : { type: "none" },
    objectName: o.name || nm("shape"),
  });
}
function txt(runs, x, y, w, h, o = {}) {
  s.addText(runs, {
    x, y, w, h, isTextBox: true, margin: 0, fontFace: "Arial", fontSize: o.fs ?? FS, color: o.c ?? INK,
    bold: o.b ?? false, align: o.al ?? "left", valign: o.va ?? "middle", lineSpacingMultiple: 1.0,
    paraSpaceAfter: 0, paraSpaceBefore: 0, fit: "none", rotate: o.rot, objectName: o.name || nm("text"),
  });
}
function seg(x1, y1, x2, y2, o = {}) {
  s.addShape(pres.shapes.LINE, {
    x: Math.min(x1, x2), y: Math.min(y1, y2), w: Math.abs(x2 - x1), h: Math.abs(y2 - y1), flipH: x2 < x1, flipV: y2 < y1,
    line: { color: o.c ?? LINE, width: o.lw ?? 0.75, dashType: o.dash ? "dash" : "solid", endArrowType: o.arrow ? "triangle" : undefined },
    objectName: o.name || nm("line"),
  });
}
// free path in absolute inches: pts = [[x,y], ...] with optional {c:[x1,y1,x2,y2]} cubic control points
function path(pts, o = {}) {
  const xs = [], ys = [];
  pts.forEach((p) => { xs.push(p[0]); ys.push(p[1]); if (p[2]) { xs.push(p[2][0], p[2][2]); ys.push(p[2][1], p[2][3]); } });
  const x0 = Math.min(...xs), y0 = Math.min(...ys), w = Math.max(Math.max(...xs) - x0, 0.001), h = Math.max(Math.max(...ys) - y0, 0.001);
  const points = pts.map((p, i) => {
    const q = { x: p[0] - x0, y: p[1] - y0 };
    if (i === 0) q.moveTo = true;
    else if (p[2]) q.curve = { type: "cubic", x1: p[2][0] - x0, y1: p[2][1] - y0, x2: p[2][2] - x0, y2: p[2][3] - y0 };
    return q;
  });
  if (o.fill) points.push({ close: true });
  s.addShape(pres.shapes.CUSTOM_GEOMETRY, {
    x: x0, y: y0, w, h, points,
    fill: o.fill ? { color: o.fill, transparency: o.tr ?? 0 } : { type: "none" },
    line: o.fill ? { type: "none" } : { color: o.c ?? LINE, width: o.lw ?? 0.75, dashType: o.dash ? "dash" : "solid", endArrowType: o.arrow ? "triangle" : undefined },
    objectName: o.name || nm("path"),
  });
}
// horizontal ribbon from [a0,b0] at x0 to [a1,b1] at x1
function ribbon(x0, a0, b0, x1, a1, b1, color, tr, name) {
  const m = (x0 + x1) / 2;
  path([[x0, a0], [x1, a1, [m, a0, m, a1]], [x1, b1], [x0, b0, [m, b1, m, b0]]], { fill: color, tr, name });
}
// vertical S-curve connector
function curve(x0, y0, x1, y1, o = {}) {
  if (Math.abs(x1 - x0) < 0.01) return seg(x0, y0, x1, y1, o);
  const m = (y0 + y1) / 2;
  path([[x0, y0], [x1, y1, [x0, m, x1, m]]], o);
}
const iconCache = {};
async function icon(name, x, y, d, color = ICON) {
  const key = name + color;
  if (!iconCache[key]) {
    const svg = RDS.renderToStaticMarkup(React.createElement(lu[name], { size: 256, color: "#" + color, strokeWidth: 2 }));
    iconCache[key] = (await sharp(Buffer.from(svg)).png().toBuffer()).toString("base64");
  }
  s.addImage({ data: "image/png;base64," + iconCache[key], x, y, w: d, h: d, objectName: `icon_${name}_${++n}`, altText: name });
}
async function pill(x, y, w, h, label, o = {}) {
  box(x, y, w, h, { fill: o.fill ?? SL.l, line: o.line, dash: o.dash, lw: o.lw, r: o.r ?? Math.min(h / 2, 0.15), shape: o.shape, name: o.name });
  let tx = x + 0.08, tw = w - 0.16;
  if (o.icon) {
    const d = o.id ?? 0.17;
    await icon(o.icon, x + 0.09, y + (h - d) / 2, d, o.ic ?? ICON);
    if (o.al !== "center") { tx = x + 0.09 + d + 0.06; tw = w - (tx - x) - 0.07; }
  }
  txt(label, tx, y, tw, h, { b: o.b ?? true, c: o.c ?? INK, al: o.al ?? (o.icon ? "left" : "center"), name: (o.name || "pill") + "_t" });
}
function panel(letter, title, x, y) {
  txt(letter, x, y, 0.14, 0.15, { fs: 8, b: true, va: "top", name: `panel_${letter}` });
  txt(title, x + 0.16, y + 0.008, 3, 0.14, { b: true, va: "top", name: `panel_${letter}_title` });
}
const mix = (hex, t) => { const c = [0, 2, 4].map((k) => parseInt(hex.slice(k, k + 2), 16));
  return c.map((v) => Math.round(255 + (v - 255) * t).toString(16).padStart(2, "0")).join("").toUpperCase(); };
const lum = (hex) => { const c = [0, 2, 4].map((k) => parseInt(hex.slice(k, k + 2), 16) / 255).map((v) => v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4);
  return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]; };
const est = (t, bold) => t.length * (bold ? 0.053 : 0.0495);   // rough Arial 7 pt width (in)

(async () => {
  // Layout (reading order): a Composite rubric scorecard | b O/V/L profile  //  c RCI flow | d benchmark workflow
  // ═════════════ a  Composite rubric as an answer sheet: each criterion is marked 0-4 and carries its weight ═════════════
  panel("a", "Composite rubric", 0.04, 0.03);
  const BR = [
    { id: "B1", name: "Scientific Significance and Field Need", wt: 20, leaves: [["Scientific Significance", 10], ["Field Need", 10]] },
    { id: "B2", name: "Scientific Originality", wt: 20, leaves: [] },
    { id: "B3", name: "Substantive Knowledge Increment", wt: 25, leaves: [] },
    { id: "B4", name: "Evidence Auditability and Scope Control", wt: 25,
      leaves: [["Scope and Version Completeness", 5], ["Evidence Traceability and Provenance", 5],
               ["Failure and Uncertainty Disclosure", 5], ["Replication Classification", 5], ["Artifact Accessibility", 5]] },
    { id: "B5", name: "AI Contribution and Decision Traceability", wt: 10,
      leaves: [["AI Contribution", 4], ["Decision Traceability", 3], ["Human Intervention Record", 3]] },
  ];
  const AX1 = 4.82, SX0 = L, SY0 = 0.26;
  const CN0 = SX0 + 0.10, CWT0 = 2.72, WMAX = 0.62, wbar = (w) => WMAX * w / 25;
  const BUB0 = 3.85, BSTEP = 0.205, BD = 0.155;
  const nRows = BR.reduce((a, b) => a + 1 + b.leaves.length, 0), RHh = 0.185, GAP = 0.05;
  const sheetH = nRows * RHh + GAP * (BR.length - 1) + 0.16;
  // title bar on top, same style as the previous total row
  const TBH = 0.28;
  box(SX0 + 0.05, SY0, AX1 - SX0 - 0.10, TBH, { fill: SL.d, r: 0.06, name: "a_title_bar" });
  txt("Composite Score (0–100)", SX0 + 0.05, SY0, AX1 - SX0 - 0.10, TBH, { b: true, c: WHITE, al: "center", name: "a_title_bar_t" });
  const bubbles = (yy, key) => {
    for (let a = 0; a <= 4; a++) {
      const cx = BUB0 + a * BSTEP;
      s.addShape(pres.shapes.OVAL, { x: cx - BD / 2, y: yy + RHh / 2 - BD / 2, w: BD, h: BD, fill: { color: WHITE }, line: { color: SL.line, width: 0.75 }, objectName: `${key}_b${a}` });
      txt(String(a), cx - BD / 2, yy + RHh / 2 - BD / 2, BD, BD, { al: "center", name: `${key}_b${a}_t` });
    }
  };
  // column headers; the score row maps each anchor column to its score
  const HY0 = SY0 + TBH + 0.07;
  txt("Criterion", CN0, HY0, 1.2, 0.14, { b: true, name: "a_h_criterion" });
  txt("Weight", CWT0, HY0, 0.8, 0.14, { b: true, name: "a_h_weight" });
  txt("Anchor → mapped score", 3.20, HY0, BUB0 + 4 * BSTEP + BD / 2 - 3.20, 0.14, { b: true, al: "right", name: "a_h_anchor" });
  txt("Score", BUB0 - 0.62, HY0 + 0.17, 0.48, 0.14, { al: "right", name: "a_h_score" });
  [0, 20, 45, 70, 100].forEach((v, a) => txt(String(v), BUB0 + a * BSTEP - 0.15, HY0 + 0.17, 0.30, 0.14, { b: true, al: "center", name: `a_h_score${a}` }));
  let y = HY0 + 0.37;
  BR.forEach((b, i) => {
    const gh = (1 + b.leaves.length) * RHh;
    box(SX0 + 0.05, y, AX1 - SX0 - 0.10, gh, { fill: mix(BR_COL[i], 0.10), r: 0.04, name: `a_group${i + 1}` });
    txt([R_(`${b.id}  `), R_(b.name)], CN0, y, CWT0 - CN0 - 0.08, RHh, { b: true, name: `a_${b.id}_name` });
    box(CWT0, y + RHh / 2 - 0.05, wbar(b.wt), 0.10, { fill: BR_COL[i], r: 0, shape: pres.shapes.RECTANGLE, name: `a_group${i + 1}_w` });
    txt(`${b.wt}%`, CWT0 + wbar(b.wt) + 0.05, y, 0.4, RHh, { b: true, name: `a_group${i + 1}_wt` });
    if (!b.leaves.length) bubbles(y, `a_group${i + 1}`);
    y += RHh;
    b.leaves.forEach(([ln, w], j) => {
      txt(ln, CN0 + 0.18, y, CWT0 - CN0 - 0.26, RHh, { name: `a_g${i + 1}_item${j + 1}` });
      box(CWT0, y + RHh / 2 - 0.04, wbar(w), 0.08, { fill: mix(BR_COL[i], 0.55), r: 0, shape: pres.shapes.RECTANGLE, name: `a_g${i + 1}_item${j + 1}_w` });
      txt(`${w}%`, CWT0 + wbar(w) + 0.05, y, 0.4, RHh, { name: `a_g${i + 1}_item${j + 1}_wt` });
      bubbles(y, `a_g${i + 1}_item${j + 1}`);
      y += RHh;
    });
    y += GAP;
  });
  // atomic evidence checks behind every mark
  box(SX0 + 0.05, y, AX1 - SX0 - 0.10, 0.24, { fill: SL.p, r: 0.04, name: "a_checks" });
  txt("Atomic evidence checks", CN0, y, 1.5, 0.24, { b: true, name: "a_checks_t" });
  let ckx = CN0 + 1.52;
  for (const [k, t] of ["Bias Control", "Coverage", "Consensus", "Sensitivity"].entries()) {
    await icon("LuCircleCheck", ckx, y + 0.06, 0.12, SL.d);
    txt(t, ckx + 0.16, y, 0.75, 0.24, { name: `a_check_${k + 1}` });
    ckx += 0.16 + est(t, false) + 0.14;
  }
  const TOP_END = y + 0.24;

  // ═════════════ b  Independent O/V/L profile: one level per axis ═════════════
  const BX = 4.97, BW = R - BX;
  panel("b", "Independent O/V/L profile", BX - 0.08, 0.03);
  const AXS = [
    { k: "O", name: "Problem Openness", col: O, levels: [["O1", "Closed rule world"], ["O2", "Pre-defined benchmark"], ["O3", "New instance, answer knowable"],
      ["O4", "New object, made and tested"], ["O5", "Open mathematical or computational problem"], ["O6", "Open scientific question"]] },
    { k: "V", name: "Verification Strength", col: V, levels: [["V0", "Not verified"], ["V1", "Benchmark"], ["V2", "Third-party replication"],
      ["V3", "Formal proof or physical experiment"], ["V4", "Deployment and field consensus"]] },
    { k: "L", name: "Level of Autonomy", col: Lc, levels: [["L1", "Computational oracle"], ["L2", "Automated research assistant"],
      ["L3", "Autonomous scientific partner"], ["L4", "Generative architect"]] },
  ];
  let yy = 0.27;
  const LH1 = 0.145, LH2 = 0.27, LGAP = 0.025;
  for (const ax of AXS) {
    s.addShape(pres.shapes.OVAL, { x: BX, y: yy, w: 0.18, h: 0.18, fill: { color: ax.col.c }, line: { type: "none" }, objectName: `b_${ax.k}_badge` });
    txt(ax.k, BX, yy, 0.18, 0.18, { b: true, c: ax.col.t, al: "center", name: `b_${ax.k}_letter` });
    txt(ax.name, BX + 0.25, yy, BW - 0.25, 0.18, { b: true, name: `b_${ax.k}_name` });
    yy += 0.23;
    const nL = ax.levels.length, y1 = yy;
    const rows = ax.levels.map(([id, lab]) => { const two = est(lab, false) > BW - 0.60; const r = { id, lab, two, y: yy }; yy += (two ? LH2 : LH1) + LGAP; return r; });
    yy -= LGAP;
    rows.forEach((r, i) => {
      const f = mix(ax.col.c, 0.2 + 0.8 * i / (nL - 1)), tc = lum(f) < 0.25 ? WHITE : INK;
      s.addShape(pres.shapes.OVAL, { x: BX + 0.03, y: r.y + LH1 / 2 - 0.06, w: 0.12, h: 0.12, fill: { color: WHITE }, line: { color: SL.line, width: 0.75 }, objectName: `b_${r.id}_bubble` });
      box(BX + 0.25, r.y, 0.29, LH1, { fill: f, r: 0.03, name: `b_${r.id}` });
      txt(r.id, BX + 0.25, r.y, 0.29, LH1, { b: true, c: tc, al: "center", name: `b_${r.id}_t` });
      txt(r.lab, BX + 0.60, r.y, BW - 0.60, r.two ? LH2 : LH1, { va: r.two ? "top" : "middle", name: `b_${r.id}_label` });
    });
    yy += 0.09;
  }

  // ═════════════ c  RCI: records -> four components -> RCI ═════════════
  const PY = Math.max(TOP_END, yy) + 0.10;
  panel("c", "RCI scoring flow", 0.04, PY);
  const AG = 0.19;                                       // arrow gap used throughout c and d
  const BX1 = 3.05, RX0 = L, RX1 = 1.52, RXC = (RX0 + RX1) / 2;
  const cy0 = PY + 0.22;
  await pill(L, cy0, BX1 - L, 0.26, "Fixed as-of date and work identifier", { fill: SL.p, icon: "LuCalendarClock", name: "c_input" });
  seg(RXC, cy0 + 0.26, RXC, cy0 + 0.26 + AG, { arrow: true, name: "c_a1" });
  const ev0 = cy0 + 0.26 + AG;
  await pill(L, ev0, BX1 - L, 0.32, "Evidence IDs, source-specific records and collection metadata", { fill: SL.p, icon: "LuDatabase", r: 0.10, name: "c_evidence" });
  seg(RXC, ev0 + 0.32, RXC, ev0 + 0.32 + AG, { arrow: true, name: "c_a2" });
  const RC = [["R1", "Normalized scholarly uptake", 30], ["R2", "Independent reuse or replication", 30],
              ["R3", "Reproducibility and access", 20], ["R4", "Operational or decision use", 20]];
  const CY0 = ev0 + 0.32 + AG, FB = H - 0.10 - CY0 - 0.18 - 0.05, DCX = 2.62, DR = 0.40, DCY = CY0 + (FB + 0.18) / 2;
  let cy = CY0, ey = DCY - 0.26;
  RC.forEach(([id, t, wt]) => {
    const h = FB * wt / 100, eh = 0.52 * wt / 100;
    ribbon(RX1, cy, cy + h, DCX - DR + 0.05, ey, ey + eh, AM.c, 45, `c_${id}_flow`);
    box(RX0, cy, RX1 - RX0, h, { fill: AM.p, r: 0.04, name: `c_${id}` });
    box(RX0 + 0.06, cy + h / 2 - 0.07, 0.25, 0.14, { fill: AM.c, r: 0.03, name: `c_${id}_chip` });
    txt(id, RX0 + 0.06, cy + h / 2 - 0.07, 0.25, 0.14, { b: true, al: "center", name: `c_${id}_id` });
    txt(t, RX0 + 0.37, cy, RX1 - RX0 - 0.42, h, { name: `c_${id}_name` });
    txt(`${wt}%`, RX1 + 0.05, cy + h / 2 - 0.065, 0.32, 0.13, { b: true, name: `c_${id}_pct` });
    cy += h + 0.06; ey += eh;
  });
  s.addShape(pres.shapes.OVAL, { x: DCX - DR, y: DCY - DR, w: 2 * DR, h: 2 * DR, fill: { color: AM.c }, line: { color: WHITE, width: 1.5 }, objectName: "c_rci" });
  await icon("LuGauge", DCX - 0.11, DCY - 0.20, 0.22, INK);
  txt("RCI", DCX - DR, DCY + 0.02, 2 * DR, 0.15, { b: true, al: "center", name: "c_rci_label" });
  await icon("LuSigma", DCX - 0.075, DCY - DR - 0.52, 0.15);
  txt("Weighted sum with missingness handling", DCX - 0.52, DCY - DR - 0.34, 1.04, 0.27, { b: true, al: "center", va: "top", name: "c_wsum_t" });
  txt("RCI score and status", DCX - 0.6, DCY + DR + 0.04, 1.2, 0.14, { b: true, al: "center", name: "c_rci_t" });

  // ═════════════ d  Benchmark workflow on a 3-column grid ═════════════
  const CX0 = 3.25, CG = 0.1475, CW3 = (R - CX0 - 2 * CG) / 3;
  const colX = [0, 1, 2].map((i) => CX0 + i * (CW3 + CG)), colC = colX.map((x) => x + CW3 / 2);
  const cspan = (a, b) => [colX[a], colX[b] + CW3 - colX[a]];
  const RH = 0.26, DH = 0.34, P = RH + AG;
  const Y = [PY + 0.22]; for (let k = 1; k <= 4; k++) Y.push(Y[k - 1] + P);
  Y.push(Y[4] + DH + AG); Y.push(Y[5] + P);                   // Y[4] = decision diamond top
  const down = (x, y0, y1, o = {}) => seg(x, y0, x, y1, { arrow: true, ...o });
  panel("d", "Benchmark workflow", CX0 - 0.08, PY);
  { const [x, w] = cspan(0, 2);
    await pill(x, Y[0], w, RH, "Paper version and evidence cutoff", { fill: SL.p, icon: "LuFileText", r: 0.08, al: "center", name: "d_version" });
    down(colC[1], Y[0] + RH, Y[1], { name: "d_a_version" });
    box(x, Y[1], w, RH, { fill: SL.l, r: 0.08, name: "d_packet" });
    await icon("LuPackage", x + 0.09, Y[1] + (RH - 0.17) / 2, 0.17);
    txt([R_("Evidence packet", { bold: true, breakLine: true }), R_("Claims · Prior art · Evidence IDs · Decision records")],
        x + 0.33, Y[1] - 0.01, w - 0.40, RH + 0.02, { name: "d_packet_t" }); }
  down(colC[0], Y[1] + RH, Y[2], { dash: true, name: "d_a_human" });
  down(colC[1], Y[1] + RH, Y[2], { name: "d_a_j1" });
  down(colC[2], Y[1] + RH, Y[2], { name: "d_a_j2" });
  await pill(colX[0], Y[2], CW3, RH, "Human expert review", { fill: SL.p, line: SL.line, dash: true, lw: 0.75, icon: "LuUserCheck", r: 0.08, name: "d_human" });
  await pill(colX[1], Y[2], CW3, RH, "LLM Judge 1", { fill: WHITE, line: SL.line, icon: "LuBot", r: 0.08, name: "d_judge1" });
  await pill(colX[2], Y[2], CW3, RH, "LLM Judge 2", { fill: WHITE, line: SL.line, icon: "LuBot", r: 0.08, name: "d_judge2" });
  down(colC[1], Y[2] + RH, Y[3], { name: "d_a_gap1" });
  down(colC[2], Y[2] + RH, Y[3], { name: "d_a_gap2" });
  const spine = (colC[1] + colC[2]) / 2;
  { const [x, w] = cspan(1, 2);
    await pill(x, Y[3], w, RH, "Score disagreement", { fill: SL.l, icon: "LuScale", r: 0.08, al: "center", name: "d_gap" }); }
  down(spine, Y[3] + RH, Y[4], { name: "d_a_decision" });
  s.addShape(pres.shapes.DIAMOND, { x: colC[1], y: Y[4], w: colC[2] - colC[1], h: DH, fill: { color: WHITE }, line: { color: SL.d, width: 0.75 }, objectName: "d_decision" });
  txt("≤ 15 points?", spine - 0.45, Y[4], 0.9, DH, { b: true, al: "center", name: "d_decision_t" });
  down(colC[1], Y[4] + DH / 2, Y[5], { name: "d_yes" });
  down(colC[2], Y[4] + DH / 2, Y[5], { name: "d_no" });
  txt("Yes", colC[1] - 0.40, Y[4] + DH / 2 + 0.03, 0.33, 0.13, { b: true, al: "right", name: "d_yes_t" });
  txt("No", colC[2] + 0.07, Y[4] + DH / 2 + 0.03, 0.33, 0.13, { b: true, name: "d_no_t" });
  await pill(colX[1], Y[5], CW3, RH, "Average mapped leaf scores", { fill: WHITE, line: SL.line, r: 0.08, name: "d_average" });
  await pill(colX[2], Y[5], CW3, RH, "Third LLM Judge", { fill: WHITE, line: SL.line, icon: "LuBot", r: 0.08, name: "d_judge3" });
  down(colC[1], Y[5] + RH, Y[6], { name: "d_a_rc1" });
  down(colC[2], Y[5] + RH, Y[6], { name: "d_a_rc2" });
  { const [x, w] = cspan(1, 2);
    await pill(x, Y[6], w, RH, "Recompute Composite and record O/V/L", { fill: SL.l, icon: "LuCalculator", r: 0.08, al: "center", name: "d_recompute" });
    const yc = Y[6] + RH / 2, rr = 0.08;
    path([[colC[0], Y[2] + RH], [colC[0], yc - rr], [colC[0] + rr, yc, [colC[0], yc - rr / 2, colC[0] + rr / 2, yc]], [x, yc]],
         { dash: true, arrow: true, name: "d_human_to_recompute" }); }
  // paper-level report: RCI (from panel c) | Composite | O/V/L
  const FY = Y[6] + RH + 0.10, TY = FY + 0.02, PYo = Y[6] + RH + AG + 0.08, PH = 0.25;
  box(CX0 - 0.05, FY, R - CX0 + 0.10, PYo + PH + 0.05 - FY, { fill: SL.p, r: 0.08, name: "d_report" });
  await icon("LuClipboardCheck", colX[0] + 0.02, TY - 0.005, 0.14);
  txt("Paper-level report", colX[0] + 0.20, TY, 1.0, 0.13, { b: true, name: "d_report_title" });
  seg(colC[1], Y[6] + RH, colC[1], PYo, { arrow: true, c: SL.d, name: "d_to_composite" });
  seg(colC[2], Y[6] + RH, colC[2], PYo, { arrow: true, c: SL.d, name: "d_to_ovl" });
  box(colX[0], PYo, CW3, PH, { fill: AM.c, r: 0.08, name: "d_out_rci" });
  txt("RCI", colX[0], PYo, CW3, PH, { b: true, al: "center", name: "d_out_rci_t" });
  box(colX[1], PYo, CW3, PH, { fill: SL.d, r: 0.08, name: "d_out_composite" });
  txt("Composite Score", colX[1], PYo, CW3, PH, { b: true, c: WHITE, al: "center", name: "d_out_composite_t" });
  box(colX[2], PYo, CW3, PH, { fill: WHITE, line: SL.line, r: 0.08, name: "d_out_ovl" });
  [O, V, Lc].forEach((col, i) => s.addShape(pres.shapes.OVAL, { x: colX[2] + 0.09 + i * 0.085, y: PYo + PH / 2 - 0.035, w: 0.07, h: 0.07, fill: { color: col.c }, line: { type: "none" }, objectName: `d_out_ovl_dot${i}` }));
  txt("O/V/L Profile", colX[2] + 0.37, PYo, CW3 - 0.42, PH, { b: true, name: "d_out_ovl_t" });
  const GX = 3.15, rr = 0.08, ryc = PYo + PH / 2;
  path([[DCX + DR, DCY], [GX - rr, DCY], [GX, DCY + rr, [GX - rr / 2, DCY, GX, DCY + rr / 2]], [GX, ryc - rr],
        [GX + rr, ryc, [GX, ryc - rr / 2, GX + rr / 2, ryc]], [colX[0], ryc]],
       { c: AM.c, lw: 1.5, arrow: true, name: "rci_stream" });
  console.log("bottom of d:", (PYo + PH + 0.05).toFixed(3), "page H:", H, "top end:", TOP_END.toFixed(3), "b end:", yy.toFixed(3));

  await pres.writeFile({ fileName: process.argv[2] || "fig3_benchmark.pptx" });
  console.log("wrote", process.argv[2]);
})();
