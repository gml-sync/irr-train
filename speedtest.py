from pathlib import Path
from skimage import io
from time import time

print("Hello!")
path = Path.cwd().parent.parent.parent / 'sintelall/MPI-Sintel-complete/training/clean'
print("cwd:", path)

begin = time()

sintel_root = Path.cwd().parent.parent.parent
for x in sorted(path.rglob('*.png'))[:10]:
    img = io.imread(x)
    #print(x.relative_to(sintel_root))

print('Spent {:.2f}'.format(time() - begin))
