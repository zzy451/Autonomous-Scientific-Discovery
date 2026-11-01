"""Build from the project root so MiKTeX resolves Definitions/mdpi.bst."""
from pathlib import Path
import re
import subprocess

root=Path(__file__).resolve().parent
(root/'build').mkdir(exist_ok=True)
steps=[['pdflatex','-interaction=nonstopmode','-halt-on-error','-output-directory=build','main.tex'],['bibtex','build/main']]
steps += [steps[0],steps[0]]
for i,args in enumerate(steps,1):
    result=subprocess.run(args,cwd=root,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    (root/'build'/f'build_step_{i}.txt').write_bytes(result.stdout)
    print(' '.join(args),':',result.returncode,flush=True)
    if result.returncode:
        print(result.stdout.decode(errors='replace')[-5000:]);raise SystemExit(result.returncode)
log=(root/'build/main.log').read_text(errors='replace')
if re.search(r'undefined citations|Citation .* undefined|There were undefined references',log):
    raise SystemExit('Unresolved references: inspect build/main.log')
print('Build completed; no undefined citations.')
