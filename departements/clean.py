from pathlib import Path
import re
import shutil
import os


files = list(Path().cwd().glob('*'))

def trim(path):
    string = path.name
    string = re.sub(r'([\d\w]+-logo-)', '', string=string).replace('departement', '')

    while string.startswith('-'):
        string = string[1:]
    while string.endswith('-'):
        string = string[:-1]

    return string

newfiles = list(map(trim, files))

for f,nf in zip(files,newfiles):
    os.system(f"mv {f} {nf}")