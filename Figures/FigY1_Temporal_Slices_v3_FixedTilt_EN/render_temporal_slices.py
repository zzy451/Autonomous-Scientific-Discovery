"""Five wider non-occluding score/RCI slices, with v2's tilt preserved exactly.

Actual upstream code used:
  lanl/pymplot: isometric_projection, extracted unchanged, BSD-3-Clause.
  Point glow removed for this revision; only a soft density wash is used.
"""
from __future__ import annotations

import csv
import argparse
import hashlib
import json
from pathlib import Path
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, Normalize, to_rgb
from matplotlib.font_manager import FontProperties, fontManager
from matplotlib.patches import Polygon, FancyArrowPatch
from matplotlib.transforms import Affine2D
import numpy as np
from scipy.ndimage import gaussian_filter

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "vendor" / "pymplot"))
from pymplot_projection_adapter import isometric_projection


DEFAULTS = {
    "source_csv": "data/scenario_papers_1956_2026_EN.csv",
    "source_manifest": "data/domain_manifest_EN.json",
    "projection_angles_deg": [16.0, -4.0],
    "local_score_axis_length": 288.0,
    "local_rci_axis_length": 278.0,
    "projected_gap": 58.0,
    "era_vertical_step": 8.0,
    "origin": [92.0, 204.0],
    "canvas": [1810.0, 750.0],
    "cloud_grid_size": 280,
    "cloud_bandwidth_score_units": 5.8,
    "cloud_opacity": 0.28,
    "cloud_color_exponent": 1.7,
    "point_area_pt2": 15.0,
    "point_alpha": 0.79,
    "paper_background": "#ffffff",
    "sheet_background": "#fbfcfa",
    "domain_colors": ["#326fb2","#279fb5","#21977d","#879b26","#cf923a",
                      "#c4517c","#9b6b47","#7662b2","#559b59","#567f91","#a25497"],
    "dpi": 240,
    "preview_dpi": 110,
    "eras": [
        {"label": "Up to 1997", "start": 1900, "end": 1997, "name": "Rules and Search"},
        {"label": "1998–2012", "start": 1998, "end": 2012, "name": "Statistical Learning"},
        {"label": "2013–2019", "start": 2013, "end": 2019, "name": "Deep Learning"},
        {"label": "2020–2023", "start": 2020, "end": 2023, "name": "Foundation Models"},
        {"label": "2024–2026", "start": 2024, "end": 2026, "name": "Scientific Agents"},
    ],
}


def settings():
    path = ROOT / "design_parameters.json"
    if not path.exists():
        path.write_text(json.dumps(DEFAULTS, ensure_ascii=False, indent=2), encoding="utf-8")
    return json.loads(path.read_text(encoding="utf-8"))


def load_data(cfg):
    path = ROOT / cfg["source_csv"]
    rows = list(csv.DictReader(path.open(encoding="utf-8-sig", newline="")))
    meta = json.loads((ROOT / cfg["source_manifest"]).read_text(encoding="utf-8"))
    for row in rows:
        for key in ["domain_index", "disclosure_year"]:
            row[key] = int(row[key])
        for key in ["score", "rci"]:
            row[key] = float(row[key])
        indices = [i for i, e in enumerate(cfg["eras"])
                   if e["start"] <= row["disclosure_year"] <= e["end"]]
        if len(indices) != 1:
            raise ValueError((row["paper_id"], row["disclosure_year"], indices))
        row["fig1_era_index"] = indices[0]
        row["fig1_era_label"] = cfg["eras"][indices[0]]["label"]
    assert len(rows) == len({r["paper_id"] for r in rows}) == 1180
    assert all(0 <= r["score"] <= 100 and 0 <= r["rci"] <= 100 for r in rows)
    return rows, meta, hashlib.sha256(path.read_bytes()).hexdigest()


class Slices:
    def __init__(self, cfg):
        self.cfg = cfg
        self.alpha, self.beta = cfg["projection_angles_deg"]
        self.width = cfg["local_score_axis_length"]
        self.height = cfg["local_rci_axis_length"]
        self.projected_width = float(self.width * np.cos(np.deg2rad(self.alpha)))
        self.depth_step = (self.projected_width + cfg["projected_gap"]) / np.cos(np.deg2rad(self.beta))
        self.native_vertical_step = -self.depth_step * np.sin(np.deg2rad(self.beta))

    def project(self, era, score, rci):
        x, y = isometric_projection(
            np.asarray(score) * self.width / 100.,
            -era * self.depth_step,
            np.asarray(rci) * self.height / 100.,
            [self.alpha, self.beta])
        # Translation only: retain both original projection angles without changing
        # the slope of either within-sheet coordinate axis.
        y = np.asarray(y) + era * (self.cfg["era_vertical_step"] - self.native_vertical_step)
        return np.asarray(x) + self.cfg["origin"][0], y + self.cfg["origin"][1]

    def vertices(self, era):
        x, y = self.project(era, [0, 100, 100, 0], [0, 0, 100, 100])
        return np.column_stack([x, y])

    def affine(self, era):
        ox, oy = self.project(era, 0, 0)
        return Affine2D.from_values(
            self.width * np.cos(np.deg2rad(self.alpha)) / 100.,
            self.width * np.sin(np.deg2rad(self.alpha)) / 100.,
            0., self.height / 100., float(ox), float(oy))


def setup_fonts():
    # Prefer the approved Arial appearance, with portable, distributable fallbacks.
    available={font.name for font in fontManager.ttflist}
    family=next((name for name in ["Arial","Liberation Sans","DejaVu Sans"] if name in available),"DejaVu Sans")
    plt.rcParams.update({"font.family":family,"axes.unicode_minus":False,
                         "svg.fonttype":"none","font.size":10})


def clouds_by_era(rows, cfg, colors):
    size = cfg["cloud_grid_size"]
    sigma = cfg["cloud_bandwidth_score_units"] * size / 100.
    fields = []
    for era in range(len(cfg["eras"])):
        local_fields = []
        for domain, color in enumerate(colors):
            selected = [r for r in rows if r["fig1_era_index"] == era and r["domain_index"] == domain]
            hist, _, _ = np.histogram2d(
                [r["rci"] for r in selected], [r["score"] for r in selected],
                bins=size, range=[[0, 100], [0, 100]])
            smoothed = gaussian_filter(hist, sigma=sigma, mode="constant")
            local_fields.append(smoothed)
        fields.append(np.stack(local_fields))
    maxima = [f.max(axis=0) for f in fields]
    nonzero = np.concatenate([t[t > 0] for t in maxima if np.any(t > 0)])
    # Shared domain-density scale. Keep strongly mixed areas almost clear rather
    # than blending all eleven colors into opaque gray fog.
    reference = float(np.quantile(nonzero, .996))
    images = []
    palette = np.asarray([to_rgb(c) for c in colors])
    for field in fields:
        total = field.sum(axis=0)
        maximum = field.max(axis=0)
        dominance = maximum / np.maximum(total, 1.e-15)
        weights = field ** cfg["cloud_color_exponent"]
        color = np.einsum("dhw,dc->hwc", weights, palette) / np.maximum(weights.sum(axis=0)[..., None], 1.e-20)
        normalized = np.clip(maximum / reference, 0, 1)
        strength = np.clip((normalized-.055)/.945, 0, 1) ** .8
        opacity = cfg["cloud_opacity"] * strength * (.20 + .80*dominance**.7)
        images.append(np.dstack([np.clip(color, 0, 1), opacity]))
    return images, reference


def panel(ax, era, records, cloud, geometry, cfg, cmap, norm):
    vertices = geometry.vertices(era)
    # A very thin page edge, with the depth effect kept outside the data face.
    ax.add_patch(Polygon(vertices + [3, -3], closed=True, facecolor="#486a7d",
                         edgecolor="none", alpha=.025, zorder=1))
    ax.add_patch(Polygon(vertices + [-2, 1.5], closed=True, facecolor="#ffffff",
                         edgecolor="#dbe2e5", linewidth=.45, zorder=2))
    face = Polygon(vertices, closed=True, facecolor=cfg["sheet_background"],
                   edgecolor="#b7c4cc", linewidth=.65, zorder=3, alpha=.98)
    ax.add_patch(face)
    # All elements are clipped to their own sheet.
    image = ax.imshow(cloud, origin="lower", extent=[0, 100, 0, 100],
                      transform=geometry.affine(era) + ax.transData,
                      interpolation="bilinear", zorder=4, aspect="equal")
    image.set_clip_path(face)
    for tick in [25, 50, 75]:
        for xx, yy in [([tick, tick], [0, 100]), ([0, 100], [tick, tick])]:
            px, py = geometry.project(era, xx, yy)
            line, = ax.plot(px, py, color="#aabac3", lw=.40, alpha=.24, zorder=5)
            line.set_clip_path(face)
    if records:
        scores = [r["score"] for r in records]
        rcis = [r["rci"] for r in records]
        indices = [r["domain_index"] for r in records]
        x, y = geometry.project(era, scores, rcis)
        stars = ax.scatter(x, y, c=indices, cmap=cmap, norm=norm,
                           s=cfg["point_area_pt2"], edgecolors="none",
                           linewidths=0, alpha=cfg["point_alpha"], zorder=7)
        stars.set_clip_path(face)
    else:
        px, py = geometry.project(era, 50, 52)
        ax.text(px, py, "No simulated samples", color="#627d8b", ha="center", va="center",
                fontsize=9.5, zorder=8)
    # Repeat sparse, identical numerical scales so every point has an unambiguous frame.
    for tick in [0, 50, 100]:
        px, py = geometry.project(era, tick, 0)
        ax.plot([px, px], [py, py-5], color="#708e9d", lw=.7, zorder=8)
        ax.text(px, py-12, str(tick), color="#526d7b", ha="center", va="top", fontsize=8.4)
        if tick != 0:
            px, py = geometry.project(era, 0, tick)
            ax.plot([px-5, px], [py, py], color="#708e9d", lw=.7, zorder=8)
            ax.text(px-9, py, str(tick), color="#526d7b", ha="right", va="center", fontsize=8.4)
    sx, sy = geometry.project(era, 50, 0)
    score_angle = np.rad2deg(np.arctan2(
        geometry.width*np.sin(np.deg2rad(geometry.alpha)), geometry.projected_width))
    if era == 0:
        ax.text(sx, sy-46, "Scientific Contribution Score", color="#314d5c", fontsize=9.0,
                ha="center", va="top", rotation=score_angle, rotation_mode="anchor")
        rx, ry = geometry.project(era, 0, 50)
        ax.text(rx-39, ry, "Reference Context Index", color="#314d5c", fontsize=9.0,
                ha="center", va="center", rotation=90)
    era_info = cfg["eras"][era]
    center = (vertices[0, 0] + vertices[1, 0]) / 2
    top = float(vertices[:, 1].max())
    ax.text(center, top+28, era_info["label"], color="#233f50", fontsize=13.0,
            ha="center", va="bottom", weight="bold")
    ax.text(center, top+8, f"{len(records)} papers", color="#7a8f99", fontsize=8.7,
            ha="center", va="bottom")


def figure(rows, meta, cfg):
    setup_fonts()
    geometry = Slices(cfg)
    base = cfg["domain_colors"]
    # Stronger domain colors on pale sheets; no neon scatter glow.
    lifted = [to_rgb(c) for c in base]
    cmap = ListedColormap(lifted)
    norm = Normalize(vmin=-.5, vmax=10.5)
    images, normalization = clouds_by_era(rows, cfg, lifted)
    width, height = cfg["canvas"]
    fig = plt.figure(figsize=(20., 20.*height/width), facecolor=cfg["paper_background"])
    ax = fig.add_axes([.02, .02, .96, .96])
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.text(55, height-42, "Scientific Contribution and External Recognition", fontsize=22.,
            color="#213e50", weight="bold", va="top")
    ax.text(width-56, height-45, cfg["simulation_label"], fontsize=9.7,
            color="#a56348", va="top", ha="right")

    boxes = []
    for i in range(len(cfg["eras"])):
        selected = [r for r in rows if r["fig1_era_index"] == i]
        panel(ax, i, selected, images[i], geometry, cfg, cmap, norm)
        v = geometry.vertices(i)
        boxes.append([float(v[:, 0].min()), float(v[:, 0].max()),
                      float(v[:, 1].min()), float(v[:, 1].max())])
    gaps = [boxes[i+1][0]-boxes[i][1] for i in range(len(boxes)-1)]
    assert all(gap >= cfg["projected_gap"]-.001 for gap in gaps)
    assert boxes[-1][1] < width-40

    centers = [(b[0]+b[1])/2 for b in boxes]
    ytime = 133
    ax.add_patch(FancyArrowPatch((centers[0]-100, ytime), (centers[-1]+105, ytime),
                                arrowstyle="-|>", mutation_scale=10.,
                                color="#879eaa", linewidth=.95))
    for i, x in enumerate(centers):
        ax.plot([x, x], [ytime-5, ytime+5], color="#879eaa", lw=1.)
    # A shared legend, deliberately outside the data sheets.
    # Two rows accommodate full English domain names in the existing footer.
    for j, domain in enumerate(meta["domains"]):
        legend_y = 82 - (j // 6)*40
        x = 70 + (j % 6)*280
        ax.scatter([x], [legend_y], s=24., c=[lifted[j]],
                   edgecolors="none", zorder=10)
        ax.text(x+15, legend_y, domain["name"], ha="left", va="center",
                fontsize=8.9, color="#344f5f")
    stem = ROOT / cfg["output_stem"]
    fig.savefig(stem.with_suffix(".png"), dpi=cfg["dpi"], facecolor=fig.get_facecolor())
    fig.savefig(stem.with_suffix(".svg"), facecolor=fig.get_facecolor())
    fig.savefig(ROOT / (cfg["output_stem"]+"_preview.png"), dpi=cfg["preview_dpi"], facecolor=fig.get_facecolor())
    import xml.etree.ElementTree as ET
    renderer = fig.canvas.get_renderer()
    text_artists = [t for t in ax.texts if t.get_text()]
    outside = []
    overlaps = []
    for text in text_artists:
        box = text.get_window_extent(renderer)
        if box.x0 < 0 or box.y0 < 0 or box.x1 > fig.bbox.width or box.y1 > fig.bbox.height:
            outside.append(text.get_text())
    for i, a in enumerate(text_artists):
        for b in text_artists[i+1:]:
            if a.get_window_extent(renderer).overlaps(b.get_window_extent(renderer)):
                overlaps.append([a.get_text(), b.get_text()])
    (ROOT / "outputs" / "text_qa.json").write_text(json.dumps({"text_labels":len(text_artists),
        "labels_outside_canvas":outside,"bounding_box_overlap_candidates":overlaps},indent=2),encoding="utf-8")
    plt.close(fig)
    return {"projection_angles_deg": cfg["projection_angles_deg"],
            "within_sheet_score_axis_angle_deg": float(score_slope_angle(geometry)),
            "era_vertical_step": cfg["era_vertical_step"],
            "projected_sheet_boxes": boxes, "projected_gaps": gaps,
            "cloud_normalization": normalization,
            "all_sheets_non_occluding": all(gap > 0 for gap in gaps)}


def score_slope_angle(geometry):
    x,y = geometry.project(0,[0,100],[0,0])
    return np.rad2deg(np.arctan2(y[1]-y[0],x[1]-x[0]))


def render_variant(cfg, variant="scenario"):
    if variant != "scenario":
        raise ValueError("Only the approved fixed synthetic scenario is bundled.")
    cfg=dict(cfg)
    cfg.setdefault("output_stem","outputs/FigY1_v3_fixed_tilt_EN")
    cfg.setdefault("simulation_label","Simulated scenario | 1,180 papers")
    (ROOT/"outputs").mkdir(exist_ok=True)
    rows, meta, source_sha = load_data(cfg)
    qa = figure(rows, meta, cfg)
    fields = list(rows[0])
    with (ROOT / (cfg["output_stem"]+"_data.csv")).open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    manifest = {
        "synthetic": True, "source_data_sha256": source_sha,
        "dataset_variant": variant,
        "source_file": cfg["source_csv"],
        "data_change_policy": "Uses supplied fixed synthetic inputs; does not resimulate or score papers",
        "n_unique_papers": len(rows),
        "era_counts": [{**e, "n": sum(r["fig1_era_index"]==i for r in rows)}
                       for i,e in enumerate(cfg["eras"])],
        "encoding": {"x_in_each_slice": "score", "y_in_each_slice": "rci",
                     "point_color": "domain", "slice": "first_public_disclosure_era",
                     "cloud": "local domain-density wash, hue-preserving compositor; no point glow"},
        "geometry": qa,
        "upstream_code_used": [
            {"repository": "https://github.com/lanl/pymplot", "function": "isometric_projection",
             "license": "BSD-3-Clause", "usage": "Unchanged extracted function called for all coordinates."}
        ],
        "caveats": ["All 1180 records are simulated, not empirical observations.",
                    "Period labels follow Fig.1; intervals are ordered, not a linear year scale.",
                    "No contour lines or arbitrary background stars; every plotted core dot is one input paper."]
    }
    (ROOT / (cfg["output_stem"]+"_manifest.json")).write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps({"variant":variant,"n":len(rows),"geometry":qa},ensure_ascii=False))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", choices=["scenario"], default="scenario")
    args = parser.parse_args()
    cfg = settings()
    assert cfg["projection_angles_deg"] == [16., -4.], "User requested original tilt."
    for variant in [args.dataset]:
        render_variant(cfg,variant)


if __name__ == "__main__":
    main()
