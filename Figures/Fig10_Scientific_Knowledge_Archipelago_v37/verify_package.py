"""Check that the downloaded package files match the published manifest."""
from pathlib import Path
import hashlib
import json

ROOT=Path(__file__).resolve().parent


if __name__=='__main__':
    manifest=json.loads((ROOT/'manifest.json').read_text(encoding='utf-8'))
    failures=[]
    for relative,expected in manifest['files'].items():
        p=ROOT/relative
        if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=expected:failures.append(relative)
    if failures:raise SystemExit('Package verification failed: '+', '.join(failures))
    print(f"Verified {len(manifest['files'])} package files (SHA-256).")
