"""Figure assembly for the main-text version: cut-out render + vector labels, legend and inset (Arial).
Inputs : render_<v>_cut_<W>x<H>.png (RGBA), anchors_<v>_cut.json, labels_<v>.json, data.json
Outputs: fig10v2_<W>x<H>.svg (render embedded, text editable), .pdf (183 mm wide), _preview.png (on white)
Usage  : python overlay2.py archipelago 1536x960
"""
import sys, json, math, base64, io
from PIL import Image, ImageDraw, ImageFont

v, size = sys.argv[1], sys.argv[2]
W, H = (int(t) for t in size.split("x"))
A = json.load(open(f"anchors_{v}_cut.json")); LM = json.load(open(f"labels_{v}.json"))["meta"]; DD = json.load(open("data.json"))
ren = Image.open(f"render_{v}_cut_{W}x{H}.png").convert("RGBA")
k = W / 1536
FS = 1.25                                   # global type scale
AR, AB = "/usr/share/fonts/arial/Arial.ttf", "/usr/share/fonts/arial/Arial Bold.ttf"
F = lambda p, s: ImageFont.truetype(p, max(6, int(s * k)))
FB, FR, FT, FL, FLB = F(AB, 24), F(AR, 15.5), F(AR, 15.5), F(AR, 15), F(AB, 15.5)
img = Image.new("RGBA", (W, H), (255, 255, 255, 255)); img.alpha_composite(ren); d = ImageDraw.Draw(img)
INK, GREY, SEA = (29, 35, 41), (95, 100, 105), (52, 92, 110)
svg_text, placed = [], []


def esc(t):
    return str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def T(x, y, t, size, bold=False, fill="#1d2329", anchor="middle", halo=True):
    if halo:                                        # white halo as an underlay copy (cairosvg ignores paint-order)
        svg_text.append(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size*k:.2f}" font-weight="{700 if bold else 400}" '
                        f'text-anchor="{anchor}" fill="#ffffff" stroke="#ffffff" stroke-width="{(2.4 if bold else 1.6)*k:.2f}" '
                        f'stroke-linejoin="round">{esc(t)}</text>')
    svg_text.append(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size*k:.2f}" font-weight="{700 if bold else 400}" '
                    f'text-anchor="{anchor}" fill="{fill}">{esc(t)}</text>')


def L(x1, y1, x2, y2, col="#5f6469", w=0.7):
    svg_text.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="{w*k:.2f}"/>')


def free(b):
    return all(b[2] < p[0] or b[0] > p[2] or b[3] < p[1] or b[1] > p[3] for p in placed)


def put(x, y, w, h, xbias=1.0):
    for step in range(80):
        rr = 6 * k * step; a = step * 2.4
        cx, cy = x + rr * math.cos(a) * 1.8 * xbias, y + rr * math.sin(a)
        b = (cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2)
        if free(b) and b[0] >= 4 and b[2] <= W - 4 and b[1] >= 4 and b[3] <= H - 4:
            placed.append(b); return cx, cy
    placed.append((x - w / 2, y - h / 2, x + w / 2, y + h / 2)); return x, y


labs = [l for l in A["labels"] if 0 <= l["px"][0] <= W and 0 <= l["px"][1] <= H]
# reserve legend (bottom-left) and inset (bottom-right) areas first
LG = (16 * k, H - 140 * k, 340 * k, H - 8 * k); placed.append(LG)
SHORT = {"01": "Formal", "02": "Physics", "03": "Chemistry", "04": "Materials", "05": "Earth", "06": "Life", "07": "Medicine",
         "08": "Agriculture", "09": "Engineering", "10": "Aerospace", "11": "Society"}
drawn = {tuple(sorted(e[:2])) for e in LM["planar_edges"]}
alls = [(tuple(sorted((p["a"], p["b"]))), p["n"]) for p in DD["pairs"]]
rest = sorted([(pr, n) for pr, n in alls if pr not in drawn], key=lambda t: -t[1]); share = sum(n for _, n in rest) / sum(n for _, n in alls)
top = rest[:8]
_tmp = ImageDraw.Draw(Image.new('RGB', (10, 10)))
IW = max(_tmp.textlength('Cross-field links not drawn as borders', font=FLB), 340 * k) + 20 * k; IH = (60 + 20 * len(top)) * k
IN = (W - IW - 12 * k, H - IH - 8 * k, W - 12 * k, H - 8 * k); placed.append(IN)

# 1 seas (data positions)
for lab in sorted([l for l in labs if l["kind"] == "sea"], key=lambda l: -l["n"]):
    x, y = lab["px"]; r = 14 * k
    if not free((x - r, y - r, x + r, y + r)):
        for a_ in range(12):
            nx_, ny_ = x + 2.4 * r * math.cos(a_ * 0.52), y + 2.4 * r * math.sin(a_ * 0.52)
            if free((nx_ - r, ny_ - r, nx_ + r, ny_ + r)):
                d.line((x, y, nx_, ny_), fill=SEA, width=max(1, int(k))); L(x, y, nx_, ny_, "#345c6e"); x, y = nx_, ny_; break
    placed.append((x - r, y - r, x + r, y + r))
    d.ellipse((x - r, y - r, x + r, y + r), fill=(255, 255, 255), outline=SEA, width=max(1, int(1.2 * k)))
    d.text((x, y), str(lab["text"]), font=FT, anchor="mm", fill=SEA)
    svg_text.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="#fff" stroke="#345c6e" stroke-width="{1.2*k:.2f}"/>')
    T(x, y + 5.5 * k, lab["text"], 15.5, fill="#345c6e", halo=False)

# 2 field names
fl = [l for l in labs if l["kind"] == "field"]
cxm = sum(l["px"][0] for l in fl) / len(fl); cym = sum(l["px"][1] for l in fl) / len(fl)


def lines_of(name):
    if len(name) <= 20 or " and " not in name:
        return [name]
    i = name.index(" and "); return [name[:i] + " and", name[i + 5:]]


import numpy as np
alpha = np.asarray(ren.getchannel("A"))
ys_, xs_ = np.nonzero(alpha > 128); ICX, ICY = xs_.mean(), ys_.mean()


def on_island(px, py):
    return 0 <= int(px) < W and 0 <= int(py) < H and alpha[int(py), int(px)] > 40


def draw_field(lab, tx, ty, w, h, ls, sub):
    y0 = ty - h / 2 + 13 * k
    for i, t in enumerate(ls):
        d.text((tx, y0 + 26 * k * i), t, font=FB, anchor="mm", fill=INK, stroke_width=int(4 * k), stroke_fill=(255, 255, 255))
        T(tx, y0 + 26 * k * i + 8 * k, t, 24, bold=True)
    ys = y0 + 26 * k * len(ls) - 3 * k
    d.text((tx, ys), sub, font=FR, anchor="mm", fill=(60, 65, 70), stroke_width=int(3 * k), stroke_fill=(255, 255, 255))
    T(tx, ys + 5.5 * k, sub, 15.5, fill="#3c4146")


# interior fields first (inside their territory), then coastal fields around the island
for lab in sorted(fl, key=lambda l: l.get("coastal", True)):
    x, y = lab["px"]; ls = lines_of(lab["text"]); sub = f'{lab["n"]} records'
    w = max([d.textlength(t, font=FB) for t in ls] + [d.textlength(sub, font=FR)]) + 8; h = (26 * len(ls) + 20) * k
    if not lab.get("coastal", True):
        tx, ty = put(x, y, w, h); draw_field(lab, tx, ty, w, h, ls, sub); continue
    base_ang = math.atan2((y - ICY), (x - ICX))
    done = False
    for dang in (0, 0.08, -0.08, 0.16, -0.16, 0.24, -0.24, 0.32, -0.32, 0.42, -0.42, 0.55, -0.55):
        ang = base_ang + dang; ux, uy = math.cos(ang), math.sin(ang)
        px_, py_ = ICX, ICY
        for _ in range(3000):                         # walk out from the island centre to the coast
            if not on_island(px_, py_) and math.hypot(px_ - ICX, py_ - ICY) > 30:
                break
            px_ += ux * 2; py_ += uy * 2
        gap = 26 * k
        cx_ = px_ + ux * (gap + w / 2 * abs(ux)); cy_ = py_ + uy * (gap + h / 2 * abs(uy))
        box = (cx_ - w / 2, cy_ - h / 2, cx_ + w / 2, cy_ + h / 2)
        if free(box) and box[0] >= 4 and box[2] <= W - 4 and box[1] >= 4 and box[3] <= H - 4:
            placed.append(box); tx, ty = cx_, cy_; done = True
            x, y = px_ - ux * 16 * k, py_ - uy * 16 * k      # leader starts just inside the coast of this territory
            break
    if not done:
        tx, ty = put(x, y, w, h)
    # leader: from the territory anchor to the nearest edge point of the label box
    ex = min(max(x, tx - w / 2), tx + w / 2); ey = min(max(y, ty - h / 2), ty + h / 2)
    d.line((x, y, ex, ey), fill=GREY, width=max(1, int(1.2 * k))); L(x, y, ex, ey, w=0.8)
    d.ellipse((x - 3 * k, y - 3 * k, x + 3 * k, y + 3 * k), fill=GREY)
    svg_text.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{3*k:.1f}" fill="#5f6469"/>')
    draw_field(lab, tx, ty, w, h, ls, sub)

# 3 top theme peak per field
tops = {}
for lab in labs:
    if lab["kind"] == "theme" and (lab["field"] not in tops or lab["n"] > tops[lab["field"]]["n"]):
        tops[lab["field"]] = lab
for lab in tops.values():
    x, y = lab["px"]; txt = f'{lab["text"]} · {lab["n"]}'; w = d.textlength(txt, font=FT) + 6; h = 19 * k
    d.ellipse((x - 2.4 * k, y - 2.4 * k, x + 2.4 * k, y + 2.4 * k), fill=INK)
    svg_text.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{2.4*k:.1f}" fill="#1d2329"/>')
    tx = ty = None
    for ddx, ddy in ((0, -13), (0, 13), (w / 2 / k + 6, 0), (-(w / 2 / k + 6), 0),
                     (w / 2 / k * 0.6, -14), (-(w / 2 / k * 0.6), -14), (w / 2 / k * 0.6, 14), (-(w / 2 / k * 0.6), 14)):
        cx_, cy_ = x + ddx * k, y + ddy * k
        b = (cx_ - w / 2, cy_ - h / 2, cx_ + w / 2, cy_ + h / 2)
        if free(b) and b[0] >= 4 and b[2] <= W - 4:
            placed.append(b); tx, ty = cx_, cy_; break
    if tx is None:
        tx, ty = put(x, y - 13 * k, w, h)
    if math.hypot(tx - x, ty - y) > max(w / 2 + 10 * k, 22 * k):
        ey = ty + (h / 2 if ty < y else -h / 2); d.line((x, y, tx, ey), fill=GREY, width=max(1, int(k))); L(x, y, tx, ey, w=0.5)
    d.text((tx, ty), txt, font=FT, anchor="mm", fill=(35, 40, 45), stroke_width=int(3 * k), stroke_fill=(255, 255, 255))
    T(tx, ty + 5.5 * k, txt, 15.5, fill="#23282d")

# 4 legend (bottom-left)
lx, ly = LG[0] + 4 * k, LG[1] + 12 * k
d.text((lx, ly), "Peak height scales with log(1 + records)", font=FLB, fill=INK, anchor="lm"); T(lx, ly + 5 * k, "Peak height scales with log(1 + records)", 15.5, True, anchor="start", halo=False)
base, scale = ly + 70 * k, 52 * k
for i, n in enumerate((1, 10, 100)):
    hh = scale * math.log1p(n) / math.log1p(113); xx = lx + 18 * k + 38 * k * i
    d.polygon([(xx - 13 * k, base), (xx, base - hh), (xx + 13 * k, base)], fill=(165, 174, 180))
    svg_text.append(f'<polygon points="{xx-13*k:.1f},{base:.1f} {xx:.1f},{base-hh:.1f} {xx+13*k:.1f},{base:.1f}" fill="#a5aeb4"/>')
    d.text((xx, base + 9 * k), str(n), font=FL, fill=INK, anchor="mm"); T(xx, base + 14 * k, n, 15, halo=False)
d.text((lx + 125 * k, base - 46 * k), "Area proportional to records", font=FL, fill=INK, anchor="lm"); T(lx + 125 * k, base - 41 * k, "Area proportional to records", 15, anchor="start", halo=False)
cx_, cy_ = lx + 133 * k, base - 20 * k
d.ellipse((cx_ - 8 * k, cy_ - 8 * k, cx_ + 8 * k, cy_ + 8 * k), fill=(255, 255, 255), outline=SEA, width=max(1, int(k)))
d.text((cx_, cy_), "n", font=FL, fill=SEA, anchor="mm")
svg_text.append(f'<circle cx="{cx_:.1f}" cy="{cy_:.1f}" r="{8*k:.1f}" fill="#fff" stroke="#345c6e" stroke-width="{k:.2f}"/>'); T(cx_, cy_ + 5 * k, "n", 15, fill="#345c6e", halo=False)
for i, t in enumerate(("records in exactly", "these fields")):
    d.text((lx + 146 * k, cy_ - 6 * k + 17 * k * i), t, font=FL, fill=INK, anchor="lm"); T(lx + 146 * k, cy_ - 1 * k + 17 * k * i, t, 15, anchor="start", halo=False)

# 5 inset (bottom-right): strongest links not drawn as shared borders
ix, iy = IN[0] + 6 * k, IN[1] + 12 * k
d.text((ix, iy), "Cross-field links not drawn as borders", font=FLB, fill=INK, anchor="lm"); T(ix, iy + 5 * k, "Cross-field links not drawn as borders", 15.5, True, anchor="start", halo=False)
sub = f"{share:.0%} of field-pair co-memberships; top 8"
d.text((ix, iy + 21 * k), sub, font=FL, fill=GREY, anchor="lm"); T(ix, iy + 25 * k, sub, 15, fill="#5f6469", anchor="start", halo=False)
nmax = top[0][1]
for i, ((a_, b_), n) in enumerate(top):
    yy = iy + (46 + 20 * i) * k; lab_ = f"{SHORT[a_]} × {SHORT[b_]}"; bw = (IW - 220 * k) * n / nmax
    d.text((ix, yy), lab_, font=FL, fill=INK, anchor="lm"); T(ix, yy + 5 * k, lab_, 15, anchor="start", halo=False)
    d.rectangle((ix + 180 * k, yy - 6 * k, ix + 180 * k + bw, yy + 6 * k), fill=(125, 145, 155))
    svg_text.append(f'<rect x="{ix+180*k:.1f}" y="{yy-6*k:.1f}" width="{bw:.1f}" height="{12*k:.1f}" fill="#7d919b"/>')
    d.text((ix + 184 * k + bw, yy), str(n), font=FL, fill=INK, anchor="lm"); T(ix + 184 * k + bw, yy + 5 * k, n, 15, anchor="start", halo=False)

img.convert("RGB").save(f"fig10v2_{W}x{H}_preview.png")
buf = io.BytesIO(); ren.save(buf, "PNG"); b64 = base64.b64encode(buf.getvalue()).decode()
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="183mm" height="{183*H/W:.1f}mm" viewBox="0 0 {W} {H}">'
       f'<rect width="{W}" height="{H}" fill="#ffffff"/><image width="{W}" height="{H}" xlink:href="data:image/png;base64,{b64}"/>'
       f'<g font-family="Arial, Helvetica, sans-serif">' + "".join(svg_text) + "</g></svg>")
open(f"fig10v2_{W}x{H}.svg", "w").write(svg)
try:
    import cairosvg
    cairosvg.svg2pdf(bytestring=svg.encode(), write_to=f"fig10v2_{W}x{H}.pdf")
except Exception as e:
    print("pdf failed:", e)
print("assembled", W, H, "share %.3f" % share)
