# Proposal explainer video

A 6 min 38 s walkthrough of *From Computable Tasks to Open Science: A Chronicle of AI Problem Solving*, with Mandarin narration and burned-in captions. It has 14 scenes.

| File | Content |
|---|---|
| `proposal_explainer_1080p.mp4` | Full-quality render, 1920 × 1080 (34.7 MB) |
| `proposal_explainer_480p.mp4` | Compressed copy for chat and email (2.4 MB) |
| `source/narration.json` | Narration script, one entry per scene (`s01`–`s14`) |
| `source/tts.py` | Text-to-speech: edge-tts, voice `zh-CN-YunyangNeural`, rate −4%; writes `audio/sNN.mp3` and `.srt` |
| `source/scenes.py`, `scenes_a.py`, `scenes_b.py` | Per-scene layout and animation (HTML + GSAP) |
| `source/build.py` | Builds the HyperFrames project from the narration, audio, subtitles and scenes |
| `source/project/` | The generated HyperFrames composition (`index.html`, `compositions/`, `assets/`) |
| `source/audio/` | Narration audio and subtitles |
| `source/final_sheet.jpg` | Contact sheet of rendered frames, used for the visual check |

## Rebuild

This was rendered on H20 in `/root/mjm_pv`. The dependencies there (`tools/`: edge-tts venv, HyperFrames, ffmpeg) are not committed.

```bash
cd source
python3 tts.py          # needs edge-tts on PATH as tools/venv/bin/edge-tts
python3 build.py        # writes project/
cd project && npx hyperframes render -o ../proposal_explainer.mp4
```

The narration follows the proposal text. It does not include the corpus results from `Coverage_Check/openness_verification_increment_2026-11-04/`.
