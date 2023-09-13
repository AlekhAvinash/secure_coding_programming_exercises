"""
Use pathlib.Path objects to 

a) create a new directory
b) create a new file
c) move a file from your current directory into the new directory

use shutil to
d) copy the file back into the original location (while keeping it in the new directory)

"""

from pathlib import Path
from shutil import copy

folder = Path('out/')
folder.mkdir(parents=True, exist_ok=True)

file = Path('a.txt')
file = folder/file
file.write_text('hello', encoding='utf-8')

copy(file, folder.parent)