"""Render the supplied fixed mock-data figure; no scoring or data generation."""
from pathlib import Path
import json
import shutil
import subprocess
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs"


def main():
    node=shutil.which("node")
    if node is None:
        raise SystemExit("Node.js 18+ is required. Install Node.js and retry.")
    subprocess.run([node,str(ROOT/"draw_spiral.mjs")],cwd=ROOT,check=True)
    cfg=json.loads((ROOT/"figure_config.json").read_text(encoding="utf-8"))
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True)
        page=browser.new_page(viewport={"width":cfg["width"],"height":cfg["height"]})
        page.goto((OUT/"scientific_contribution_spiral_EN.svg").as_uri(),wait_until="load")
        page.evaluate("document.fonts.ready")
        page.locator("svg").screenshot(path=str(OUT/"scientific_contribution_spiral_EN.png"))
        page.set_viewport_size({"width":1440,"height":1600})
        page.goto((OUT/"scientific_contribution_spiral_EN.html").as_uri(),wait_until="load")
        page.evaluate("document.fonts.ready")
        page.locator("#chart").screenshot(path=str(OUT/"scientific_contribution_spiral_EN_preview.png"))
        qa=page.evaluate("""() => ({
          category_labels:document.querySelectorAll('.secondary-label').length,
          bars:document.querySelectorAll('.score-bar').length,
          chinese_visible_text:/[\u4e00-\u9fff]/.test(document.body.innerText)
        })""")
        page.locator('.score-bar[data-code="01.01"][data-period="0"]').hover()
        qa["cross_period_highlight_count"]=page.locator(".score-bar.highlight").count()
        qa["tooltip_visible"]=page.locator("#tooltip").is_visible()
        (OUT/"render_checks.json").write_text(json.dumps(qa,indent=2),encoding="utf-8")
        assert qa["category_labels"]==48 and qa["bars"]==240 and not qa["chinese_visible_text"],qa
        assert qa["cross_period_highlight_count"]==5 and qa["tooltip_visible"],qa
        browser.close()
    print("Wrote SVG, HTML, full-resolution PNG and preview to outputs/.")


if __name__=="__main__":
    main()
