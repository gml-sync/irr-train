from pathlib import Path
import skimage.transform
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
print('Images:', len(sorted(path.rglob('*.png'))))
for x in sorted(path.rglob('*.png'))[:60]:
    #img1 = io.imread(x)[:10, :10]
    img2 = lycon.load(str(x))
    h, w = img2.shape[:2]
    resized = lycon.resize(img2, width=w // 2, height=h // 2, interpolation=lycon.Interpolation.NEAREST)

print('Lycon spent {:.4f}'.format(time() - begin))

begin = time()
for x in sorted(path.rglob('*.png'))[:60]:
    img1 = io.imread(x)
    h, w = img1.shape[:2]
    resized = skimage.transform.resize(img1, (h // 2, w // 2))
    #img2 = lycon.load(str(x))

print('Skimage spent {:.4f}'.format(time() - begin))
