from pathlib import Path
from skimage import io
from time import time
import lycon


print("Hello!")
path = Path.cwd().parent.parent.parent / 'sintelall/MPI-Sintel-complete/training/clean'
print("cwd:", path)

begin = time()

sintel_root = Path.cwd().parent.parent.parent
for x in sorted(path.rglob('*.png'))[:10]:
    #img = io.imread(x)
    img = lycon.load(str(x))

    #print(x.relative_to(sintel_root))

print('Spent {:.4f}'.format(time() - begin))
