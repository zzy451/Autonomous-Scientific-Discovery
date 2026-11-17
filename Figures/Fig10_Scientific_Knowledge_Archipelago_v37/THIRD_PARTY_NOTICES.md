# Third-party code and attribution

This package vendors the exact JavaScript files used by the delivered v37 figure. Rendering requires no CDN or later upstream release. Local file hashes are recorded in `manifest.json`.

| Component | Source and version | Usage | License notice |
|---|---|---|---|
| D3.js | [d3/d3 v4.13.0](https://github.com/d3/d3/tree/v4.13.0) | Voronoi geometry, selections and plotting utilities | `vendor/licenses/d3-BSD-3-Clause.txt` |
| Terrain algorithms | [mewo2/terrain](https://github.com/mewo2/terrain/tree/a2511d6b673ae92f5983f3343365ba9326c03b63) | Adapted procedural terrain and mesh implementation inside `fantasy_maps_map.js` | `vendor/licenses/mewo2-terrain-MIT.txt` |
| Naming-language algorithms | [mewo2/naming-language](https://github.com/mewo2/naming-language/tree/4abc8d392f9e536f86d546d446201002528cffc0) | Legacy helper code retained in the same bundled file; scientific labels replace generated fantasy names | `vendor/licenses/mewo2-naming-language-MIT.txt` |
| Priority queue | [adamhooper/js-priority-queue](https://github.com/adamhooper/js-priority-queue) | Source acknowledged by the adapted priority-queue implementation | `vendor/licenses/js-priority-queue-Public-Domain.txt` |

The bundled `fantasy_maps_map.js` is a local adaptation, not an unmodified checkout of either upstream commit. The source already marks the naming and terrain sections; the notices above preserve their provenance. The scientific-domain partition, selected shared seas, formal-category height fields, bilingual metadata and label layout are project-specific additions.

Playwright is installed separately using `requirements.txt`; its source is [microsoft/playwright-python](https://github.com/microsoft/playwright-python). Chromium is installed by Playwright. These runtimes and their binaries are not vendored in this asset.

The reference uses system Arial Regular/Bold. Font files are not redistributed here. Use a legally available installation when pixel-exact text rendering is required.

No blanket license is assigned here to the parent repository or its research data. This notice preserves third-party permissions and attribution; it does not replace those licenses.
