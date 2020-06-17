from pathlib import Path
from skimage import io
from time import time

print("Hello!")
path = Path.cwd().parent.parent.parent / 'sintelall/MPI-Sintel-complete/training/clean'
print("cwd:", path)


sintel_root = Path.cwd().parent.parent.parent
for x in path.rglob('*.png'):
    pass
    #print(x.relative_to(sintel_root))
