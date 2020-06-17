from pathlib import Path
from skimage import io
from time import time
import lycon
import numpy as np


print("Hello!")
path = Path.cwd().parent.parent.parent / 'sintelall/MPI-Sintel-complete/training/clean'
root = Path.cwd().parent.parent.parent
print("cwd:", path)

sintel_root = Path.cwd().parent.parent.parent

begin = time()
for x in sorted(path.rglob('*.png')):
    #img1 = io.imread(x)[:10, :10]
    img2 = lycon.load(str(x))

print('Lycon spent {:.4f}'.format(time() - begin))

begin = time()
for x in sorted(path.rglob('*.png')):
    img1 = io.imread(x)[:10, :10]
    #img2 = lycon.load(str(x))

print('Skimage spent {:.4f}'.format(time() - begin))
