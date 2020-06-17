from pathlib import Path
from skimage import io
from time import time
import lycon


print("Hello!")
path = Path.cwd().parent.parent.parent / 'sintelall/MPI-Sintel-complete/training/clean'
root = Path.cwd().parent.parent.parent
print("cwd:", path)

for x in sorted(path.rglob('*.png'))[:1]:
    img = io.imread(x)
    io.imwrite(root / 'a.jpg', img)

begin = time()

sintel_root = Path.cwd().parent.parent.parent
for x in sorted(path.rglob('*.png'))[:2]:
    img1 = io.imread(x)[:10, :10]
    img2 = lycon.load(str(x))[:10, :10]
    print(img1.dtype, img2.dtype)
    print(img1 - img2)

    #print(x.relative_to(sintel_root))

print('Spent {:.4f}'.format(time() - begin))
