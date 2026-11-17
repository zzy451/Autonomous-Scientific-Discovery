"""Data-driven layout for the 3D knowledge archipelago (Fig. 10 redesign drafts).

From data.json (11 fields, 44 top-4 themes, field co-membership pairs, exact multi-field combinations):
  1. maximum-weight planar subgraph of the field co-membership graph (edges added by weight, kept if the graph
     stays planar; a planar map of 11 regions can show at most 3V-6 = 27 shared borders)
  2. field centres by a weighted spring layout on that subgraph
  3. territories on a grid: power diagram inside a smooth landmass, weights iterated so area is proportional to records
  4. theme peaks: Gaussian height log(1+n)/log(1+113) inside each territory; selected exact combinations become
     lakes on the shared border of their member fields
Writes layout_<variant>.npz (height, field id) and labels_<variant>.json (3D anchors) for render.py.
Variants: archipelago (one landmass, V2), islands (separate islands + bridges, V3).
Usage: python gen_layout.py
"""
import json
import numpy as np
import networkx as nx

D = json.load(open("data.json"))
codes = [f["code"] for f in D["fields"]]
NREC = {f["code"]: f["n"] for f in D["fields"]}
NAME = {f["code"]: f["name"] for f in D["fields"]}
R = 420                                   # grid cells per side
AX = 2.0                                  # domain aspect: the island is stretched left-right
NX = int(R * AX)
xs = np.linspace(-AX, AX, NX)
ys = np.linspace(-1, 1, R)
X, Y = np.meshgrid(xs, ys)
rng = np.random.default_rng(20261117)


def tutte_centres(P, radius=0.62):
    """Tutte barycentric embedding of the planar subgraph: outer face on a circle, every other field at the
    weighted barycentre of its neighbours (sqrt of shared records). Keeps the triangulation's faces as faces."""
    ok, emb = nx.check_planarity(P)
    faces, seen = [], set()
    for u, v in emb.edges():
        if (u, v) in seen:
            continue
        f = emb.traverse_face(u, v, mark_half_edges=seen); faces.append(f)
    outer = min(faces, key=lambda f: (-len(f), sum(NREC[c] for c in f)))   # small fields on the rim
    pos = {}
    for k, c in enumerate(outer):
        a = 2 * np.pi * k / len(outer) + 0.3; pos[c] = np.array([radius * np.cos(a), radius * np.sin(a)])
    inner = [c for c in codes if c not in pos]
    ix = {c: i for i, c in enumerate(inner)}
    A = np.zeros((len(inner), len(inner))); B = np.zeros((len(inner), 2))
    for c in inner:
        i = ix[c]
        for nb in P[c]:
            w = np.sqrt(P[c][nb]["w"]); A[i, i] += w
            if nb in ix:
                A[i, ix[nb]] -= w
            else:
                B[i] += w * pos[nb]
    sol = np.linalg.solve(A, B)
    for c in inner:
        pos[c] = sol[ix[c]]
    return pos, outer


def neighbour_pairs(own, land):
    """Field pairs that share a border on the grid (4-neighbourhood, land cells only)."""
    out = set()
    for a, b, la, lb in ((own[:, :-1], own[:, 1:], land[:, :-1], land[:, 1:]), (own[:-1], own[1:], land[:-1], land[1:])):
        m = (a != b) & la & lb
        for x, y in zip(a[m].ravel(), b[m].ravel()):
            out.add((min(x, y), max(x, y)))
    return out


def planar_subgraph():
    P = nx.Graph(); P.add_nodes_from(codes)
    for e in D["pairs"]:
        P.add_edge(e["a"], e["b"], w=e["n"])
        if not nx.check_planarity(P)[0]:
            P.remove_edge(e["a"], e["b"])
    tot = sum(e["n"] for e in D["pairs"])
    return P, sum(d["w"] for *_, d in P.edges(data=True)) / tot


WX = None


def centres(G, k, seed, scale):
    pos = nx.spring_layout(G, weight="w", k=k, seed=seed, iterations=800)
    p = np.array([pos[c] for c in codes]); p -= p.mean(0); p *= scale / np.abs(p).max()
    return {c: p[i] for i, c in enumerate(codes)}


def noise(scale, amp, octaves=4):
    out = np.zeros_like(X)
    for o in range(octaves):
        f = scale * 2 ** o
        ph = rng.uniform(0, 2 * np.pi, 4)
        out += amp / 2 ** o * (np.sin(f * X + ph[0]) * np.cos(f * Y + ph[1]) + np.sin(f * 1.3 * Y + ph[2]) * np.cos(f * 0.7 * X + ph[3]))
    return out


def territories(C, land, iters=200):
    """Power diagram restricted to land; weights tuned so each area share matches records share."""
    w = np.zeros(len(codes)); target = np.array([NREC[c] for c in codes], float); target /= target.sum()
    P = np.stack([C[c] for c in codes])
    Xw, Yw = X + WX, Y + WY
    d2 = (Xw[None] - P[:, 0, None, None]) ** 2 + (Yw[None] - P[:, 1, None, None]) ** 2
    for _ in range(iters):
        own = np.argmin(d2 - w[:, None, None], 0)
        share = np.array([((own == i) & land).sum() for i in range(len(codes))], float); share /= share.sum()
        w += 0.02 * (np.log(target) - np.log(np.maximum(share, 1e-4)))
    own = np.argmin(d2 - w[:, None, None], 0)
    err = np.abs(share - target) / target
    return own, d2 - w[:, None, None], err


def peaks_and_height(own, land, C, sep_valley=True):
    """Continuous height: smooth coast x (lowland + theme peaks + fBm); territories only colour the surface."""
    from scipy.ndimage import gaussian_filter
    coast = np.clip(gaussian_filter(land.astype(float), 3.0) * 1.6 - 0.3, 0, 1)
    G = np.zeros_like(X); labels = []
    themes = D["themes"]; nmax = max(t["n"] for t in themes)
    for i, c in enumerate(codes):
        mask = (own == i) & land
        if not mask.any():
            continue
        cy, cx = Y[mask].mean(), X[mask].mean()
        r = np.sqrt(mask.sum() / np.pi) * (xs[1] - xs[0])
        ts = sorted([t for t in themes if t["field"] == c], key=lambda t: t["rank"])
        fmax = ts[0]["n"]
        for j, t in enumerate(ts):
            ang = 2 * np.pi * j / 4 + (0.6 if i % 2 else 0.0)
            rad = 0.0 if j == 0 else 0.5 * r
            px, py = cx + rad * np.cos(ang), cy + rad * np.sin(ang)
            ii, jj = int((py + 1) / 2 * (R - 1)), int((px + AX) / (2 * AX) * (NX - 1))
            if not mask[np.clip(ii, 0, R - 1), np.clip(jj, 0, NX - 1)]:
                px, py = cx + 0.5 * (px - cx), cy + 0.5 * (py - cy)
            amp = 0.05 + 0.30 * np.log1p(t["n"]) / np.log1p(nmax)
            s = (0.14 + 0.16 * np.sqrt(t["n"] / fmax)) * r
            G = np.maximum(G, amp * np.exp(-((X - px) ** 2 + (Y - py) ** 2) / (2 * s ** 2)))
            labels.append(dict(kind="theme", field=c, text=t["name"], n=t["n"], xy=[float(px), float(py)], z=float(0.02 + amp)))
        from scipy.ndimage import distance_transform_edt
        dt = distance_transform_edt(mask)
        pi, pj = np.unravel_index(np.argmax(dt), dt.shape)
        share = mask.sum() / land.sum()
        from scipy.ndimage import binary_dilation as _bd
        coastal = bool((_bd(mask, iterations=3) & ~land).any())
        labels.append(dict(kind="field", field=c, text=NAME[c], n=NREC[c], xy=[float(X[pi, pj]), float(Y[pi, pj])], z=0.04,
                           inside=bool(share >= 0.06), coastal=coastal, centroid=[float(cx), float(cy)]))
    rough = 1 + 0.35 * noise(14, 0.5, 5)
    H = coast * (0.02 + G * rough + 0.006 * noise(25, 1, 3)) - (1 - coast) * 0.05
    return H, labels


def lakes(H, own, land, score, labels):
    """Selected exact combinations as lakes on the shared border of their members."""
    idx = {c: i for i, c in enumerate(codes)}
    order = np.argsort(score, 0)
    first, second, third = order[0], order[1], order[2]
    out = []
    for s in D["seas"]:
        mem = [idx[m] for m in s["members"].split(";")]
        if len(mem) == 2:
            a, b = mem
            border = land & (((first == a) & (second == b)) | ((first == b) & (second == a)))
        else:
            border = land & np.isin(first, mem) & np.isin(second, mem) & np.isin(third, mem)
        if border.sum() < 3 and len(mem) == 2:          # thin contact: fall back to grid neighbours of the two fields
            a, b = mem; oa, ob = (own == a) & land, (own == b) & land
            nb = np.zeros_like(oa)
            nb[:, :-1] |= oa[:, :-1] & ob[:, 1:]; nb[:, 1:] |= oa[:, 1:] & ob[:, :-1]
            nb[:-1] |= oa[:-1] & ob[1:]; nb[1:] |= oa[1:] & ob[:-1]
            border = nb
        if border.sum() < 1:
            out.append(dict(sea=s["sea_id"], members=s["members"], n=int(s["records"]), placed=False)); continue
        srt = np.sort(score, 0)
        gap = srt[1] - srt[0]                                         # small on a two-field border
        if len(mem) == 3:
            gap = srt[2] - srt[0]                                     # small where three fields meet
        cand = np.where(border, gap, np.inf)
        k = np.unravel_index(np.argmin(cand), cand.shape)
        lx, ly = X[k], Y[k]
        rad = 0.03 + 0.008 * np.sqrt(int(s["records"]))
        near = ((X - lx) ** 2 + (Y - ly) ** 2) < rad ** 2
        band = border | (np.abs(gap) < 0.004 * (1 + np.sqrt(int(s["records"])) / 4))
        strait = near & band & land
        from scipy.ndimage import binary_dilation, gaussian_filter
        strait = binary_dilation(strait, iterations=2)
        depth = np.clip(gaussian_filter(strait.astype(float), 3.0) * 1.8, 0, 1)
        H = H * (1 - depth) + (-0.035) * depth
        labels.append(dict(kind="sea", field=s["members"], text=s["records"], n=int(s["records"]), xy=[float(lx), float(ly)], z=0.0))
        out.append(dict(sea=s["sea_id"], members=s["members"], n=int(s["records"]), placed=True))
    return H, out


def archipelago():
    """Planar subgraph -> centres; centres are then nudged until every planar edge is a real shared border."""
    P, cov = planar_subgraph()
    C = centres(P, k=0.9, seed=11, scale=0.62)
    C = {c: np.array([p[0] * AX * 0.95, p[1] * 0.92]) for c, p in C.items()}
    idx = {c: i for i, c in enumerate(codes)}
    edges = sorted({(idx[a], idx[b]) for sea in D['seas'] for a, b in __import__('itertools').combinations(sea['members'].split(';'), 2)})
    lnoise = noise(6, 0.08)
    spread0 = np.sqrt(np.mean([np.sum(C[c] ** 2) for c in codes]))
    best = None
    for it in range(40):
        blob = sum(np.exp(-((X - C[c][0]) ** 2 + (Y - C[c][1]) ** 2) / (2 * (0.07 + 0.016 * np.sqrt(NREC[c])) ** 2)) for c in codes)
        land = (blob + lnoise) > 0.42
        own, score, err = territories(C, land, iters=220)
        adj = neighbour_pairs(np.where(land, own, -1), land)
        missing = [(i, j) for i, j in edges if (min(i, j), max(i, j)) not in adj]
        if best is None or len(missing) < len(best[0]):
            best = (missing, {c: C[c].copy() for c in codes}, land, own, score, err)
        if not missing:
            break
        for i, j in missing:
            a, b = codes[i], codes[j]; d = C[b] - C[a]
            C[a] = C[a] + 0.06 * d; C[b] = C[b] - 0.06 * d
        tot = sum(NREC.values()); la = land.sum() * (xs[1] - xs[0]) * (ys[1] - ys[0])
        rad = {c: np.sqrt(NREC[c] / tot * la / np.pi) for c in codes}
        for ia in range(len(codes)):
            for ib in range(ia + 1, len(codes)):
                a, b = codes[ia], codes[ib]; d = C[b] - C[a]; dist = np.hypot(*d) + 1e-6
                need = 0.65 * (rad[a] + rad[b])
                if dist < need:
                    push = 0.5 * (need - dist) * d / dist
                    C[a] = C[a] - push; C[b] = C[b] + push
        m = np.mean([C[c] for c in codes], 0); sp = np.sqrt(np.mean([np.sum((C[c] - m) ** 2) for c in codes]))
        for c in codes:                       # keep the overall spread: pulling must not shrink the map
            C[c] = (C[c] - m) * spread0 / sp
    missing, C, land, own, score, err = best
    H, labels = peaks_and_height(own, land, C)
    srt = np.sort(score, 0); gap = srt[1] - srt[0]
    H = np.where(land, H - 0.012 * np.exp(-gap / 0.004), H)
    H, seas = lakes(H, own, land, score, labels)
    meta = dict(variant="archipelago", planar_edges=[[a, b, d["w"]] for a, b, d in P.edges(data=True)], planar_coverage=cov,
                area_rel_error={c: float(e) for c, e in zip(codes, err)}, seas=seas, adjacency_iterations=it,
                planar_edges_not_adjacent=[[codes[i], codes[j]] for i, j in missing])
    return H, np.where(land, own, -1), labels, meta


def islands():
    G = nx.Graph(); G.add_nodes_from(codes)
    for e in D["pairs"]:
        G.add_edge(e["a"], e["b"], w=e["n"])
    C = centres(G, k=3.0, seed=5, scale=0.86)
    own = -np.ones_like(X, int); H = np.full_like(X, -0.05); labels = []
    for i, c in enumerate(codes):
        r = 0.07 + 0.012 * np.sqrt(NREC[c])
        d = np.sqrt((X - C[c][0]) ** 2 + (Y - C[c][1]) ** 2) * (1 + noise(8, 0.12))
        m = d < r
        own[m] = i
    land = own >= 0
    H, labels = peaks_and_height(own, land, C)
    bridges = [dict(a=e["a"], b=e["b"], n=e["n"]) for e in D["pairs"] if e["n"] >= 20]
    meta = dict(variant="islands", bridges=bridges, centres={c: C[c].tolist() for c in codes})
    return H, own, labels, meta


WX, WY = noise(5, 0.035, 4), noise(5.5, 0.035, 4)

if __name__ == "__main__":
    for fn in (archipelago,):
        H, own, labels, meta = fn()
        np.savez_compressed(f"layout_{meta['variant']}.npz", H=H.astype(np.float32), own=own.astype(np.int8), xs=xs, ys=ys)
        json.dump(dict(labels=labels, meta=meta, fields=D["fields"]), open(f"labels_{meta['variant']}.json", "w"), indent=1)
        print(meta["variant"], "labels", len(labels), {k: v for k, v in meta.items() if k in ("planar_coverage",)},
              "max area err %.2f" % max(meta.get("area_rel_error", {"x": 0}).values()))
