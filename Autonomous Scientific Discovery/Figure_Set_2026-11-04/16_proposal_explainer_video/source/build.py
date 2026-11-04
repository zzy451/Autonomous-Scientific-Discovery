"""Generate the HyperFrames project from narration.json, audio/*.mp3, audio/*.srt and scenes.py."""
import json, re, subprocess, pathlib, shutil
from scenes import SCENES

ROOT = pathlib.Path(__file__).parent
PROJ = ROOT / "project"
FFPROBE = ROOT / "tools/hf/node_modules/@ffprobe-installer/linux-x64/ffprobe"
GAP, LEAD = 0.6, 0.4  # silence between scenes; voice starts LEAD s into a scene

FONTS = """
@font-face{font-family:"HFSerif";font-weight:700;src:local("Noto Serif CJK SC Bold"),local("NotoSerifCJKsc-Bold");}
@font-face{font-family:"HFSerif";font-weight:900;src:local("Noto Serif CJK SC Black"),local("NotoSerifCJKsc-Black");}
@font-face{font-family:"HFSans";font-weight:400;src:local("Noto Sans CJK SC Regular"),local("NotoSansCJKsc-Regular"),local("Noto Sans CJK SC");}
@font-face{font-family:"HFSans";font-weight:700;src:local("Noto Sans CJK SC Bold"),local("NotoSansCJKsc-Bold");}
"""
BASE_CSS = FONTS + """
#root{position:absolute;inset:0;background:#F4F1EA;color:#1F2A36;font-family:"HFSans",sans-serif;overflow:hidden;}
#root .tag{position:absolute;left:150px;top:96px;font:700 28px "HFSans";letter-spacing:4px;color:#8A6A2F;}
#root .h{position:absolute;left:150px;top:140px;right:150px;font:900 64px/1.25 "HFSerif";color:#1F2A36;}
#root .abs{position:absolute;}
#root .prog{position:absolute;left:0;top:0;width:1920px;height:6px;background:#8A6A2F;}
#root .mono{font-family:"JetBrains Mono",monospace;}
"""


def dur(p):
    return float(subprocess.check_output([str(FFPROBE), "-v", "error", "-show_entries", "format=duration",
                                          "-of", "csv=p=0", str(p)]).decode())


def srt(p):
    cues = []
    for blk in p.read_text().strip().split("\n\n"):
        lines = blk.strip().split("\n")
        a, b = [sum(float(x) * m for x, m in zip(t.replace(",", ".").split(":"), (3600, 60, 1)))
                for t in lines[1].split(" --> ")]
        cues.append((a, b, "".join(lines[2:])))
    return cues


def phrases(a, b, text, limit=22):
    """Split a sentence into caption phrases at punctuation; spread its time by character count."""
    parts = [p for p in re.split(r"(?<=[，。：；？！、])", text) if p.strip()]
    merged = []
    for p in parts:
        if merged and len(merged[-1]) + len(p) <= limit and not merged[-1].endswith(("。", "？", "！")):
            merged[-1] += p
        else:
            merged.append(p)
    total = sum(len(p) for p in merged)
    t, out = a, []
    for p in merged:
        d = (b - a) * len(p) / total
        out.append((t, t + d, p.rstrip("，。：；、")))
        t += d
    return out


def scene_file(sid, cues, length, spec):
    cue_js = json.dumps([round(c[0] + LEAD, 2) for c in cues])
    return f"""<template>
  <style>{BASE_CSS}{spec['css']}</style>
  <div id="root" data-composition-id="{sid}" data-width="1920" data-height="1080">
{spec['html']}
    <div id="{sid}-prog" class="prog"></div>
    <div id="{sid}-out" class="abs" style="inset:0;background:#F4F1EA;opacity:0"></div>
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    const C = {cue_js}, END = {length:.2f};
    const IN = (s, t, y = 24) => tl.fromTo(s, {{opacity:0, y}}, {{opacity:1, y:0, duration:0.6, ease:"power3.out"}}, t);
    const NUM = (s, to, t, d = 1.2, suf = "") => {{ const o = {{v:0}};
      tl.fromTo(o, {{v:0}}, {{v:to, duration:d, ease:"power2.out",
        onUpdate:() => {{ document.querySelector(s).textContent = Math.round(o.v) + suf; }}}}, t); }};
    const GROW = (s, t, d = 0.9, origin = "left center") => tl.fromTo(s, {{scaleX:0, transformOrigin:origin}}, {{scaleX:1, duration:d, ease:"power3.inOut"}}, t);
{spec['js']}
    tl.fromTo("#{sid}-prog", {{scaleX:0, transformOrigin:"left center"}}, {{scaleX:1, duration:END, ease:"none"}}, 0);
    tl.fromTo("#{sid}-out", {{opacity:0}}, {{opacity:1, duration:0.35, ease:"power1.in"}}, END - 0.4);
    window.__timelines["{sid}"] = tl;
  </script>
</template>
"""


def captions_file(groups, total):
    divs, js = [], []
    for i, (a, b, t) in enumerate(groups):
        divs.append(f'    <div id="cap-{i}" class="cap"><span>{t}</span></div>')
        js.append(f'tl.fromTo("#cap-{i}",{{opacity:0,y:8}},{{opacity:1,y:0,duration:0.15}},{a:.2f});'
                  f'tl.to("#cap-{i}",{{opacity:0,duration:0.1}},{b - 0.1:.2f});'
                  f'tl.set("#cap-{i}",{{visibility:"hidden"}},{b:.2f});')
    css = FONTS + """
#root{position:absolute;inset:0;pointer-events:none;}
#root .cap{position:absolute;left:0;right:0;bottom:64px;text-align:center;opacity:0;
  font:700 42px/1.3 "HFSans";color:#1F2A36;}
#root .cap span{background:rgba(244,241,234,0.92);padding:6px 22px;border-radius:8px;}
"""
    return f"""<template>
  <style>{css}</style>
  <div id="root" data-composition-id="captions" data-width="1920" data-height="1080" data-layout-allow-caption-zone>
{chr(10).join(divs)}
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    {chr(10).join(js)}
    window.__timelines["captions"] = tl;
  </script>
</template>
"""


def main():
    narr = json.load(open(ROOT / "narration.json"))
    if PROJ.exists():
        shutil.rmtree(PROJ / "compositions", ignore_errors=True)
    (PROJ / "compositions").mkdir(parents=True, exist_ok=True)
    (PROJ / "assets/audio").mkdir(parents=True, exist_ok=True)
    shutil.copy(ROOT / "fig1.png", PROJ / "assets/fig1.png")
    shutil.copy(ROOT / "tools/hf/node_modules/gsap/dist/gsap.min.js", PROJ / "assets/gsap.min.js")
    t, hosts, audios, groups = 0.0, [], [], []
    for k, s in enumerate(narr):
        sid = s["id"]
        mp3 = ROOT / f"audio/{sid}.mp3"
        shutil.copy(mp3, PROJ / f"assets/audio/{sid}.mp3")
        d = dur(mp3)
        length = LEAD + d + GAP + (1.6 if k == len(narr) - 1 else 0)
        cues = srt(ROOT / f"audio/{sid}.srt")
        (PROJ / f"compositions/{sid}.html").write_text(scene_file(sid, cues, length, SCENES[sid]))
        hosts.append(f'<div id="{sid}" data-composition-id="{sid}" data-composition-src="compositions/{sid}.html" '
                     f'data-start="{t:.2f}" data-duration="{length:.2f}" data-track-index="1" data-track-kind="graphics" '
                     f'data-width="1920" data-height="1080" style="z-index:1"></div>')
        audios.append(f'<audio id="vo-{sid}" class="clip" src="assets/audio/{sid}.mp3" data-start="{t + LEAD:.2f}" '
                      f'data-duration="{d:.2f}" data-track-index="10" data-volume="1"></audio>')
        for a, b, txt in cues:
            groups += [(t + LEAD + x, t + LEAD + y, p) for x, y, p in phrases(a, b, txt)]
        t += length
    (PROJ / "compositions/captions.html").write_text(captions_file(groups, t))
    hosts.append(f'<div id="captions" data-composition-id="captions" data-composition-src="compositions/captions.html" '
                 f'data-start="0" data-duration="{t:.2f}" data-track-index="2" data-track-kind="captions" '
                 f'data-width="1920" data-height="1080" style="z-index:5"></div>')
    nl = "\n      "
    (PROJ / "index.html").write_text(f"""<!doctype html>
<html lang="zh-CN">
  <head><meta charset="utf-8"><script src="assets/gsap.min.js"></script>
  <style>html,body{{margin:0;background:#F4F1EA;}}</style></head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{t:.2f}" data-width="1920" data-height="1080">
      {nl.join(hosts)}
      {nl.join(audios)}
    </div>
    <script>window.__timelines = window.__timelines || {{}}; window.__timelines["main"] = gsap.timeline({{ paused: true }});</script>
  </body>
</html>
""")
    print(f"total {t:.1f}s, {len(narr)} scenes, {len(groups)} caption groups")


if __name__ == "__main__":
    main()
