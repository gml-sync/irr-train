from pathlib import Path

print("Hello!")
path = Path.cwd().parent.parent.parent / 'sintelall/MPI-Sintel-complete/training/clean'
print("cwd:", path)
