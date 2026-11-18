import json, subprocess, sys
T = "tools/venv/bin/edge-tts"
for s in json.load(open("narration.json")):
    i = s["id"]
    subprocess.run([T, "--voice", "zh-CN-YunyangNeural", "--rate=-4%", "--text", s["text"],
                    "--write-media", f"audio/{i}.mp3", "--write-subtitles", f"audio/{i}.srt"], check=True)
    print(i, "ok", flush=True)
