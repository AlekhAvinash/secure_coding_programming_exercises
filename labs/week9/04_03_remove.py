"""
CAUTION
Deleting anything with python will permanently delete the file!
You will not be able to recover anything you delete with python!
USE CAUTION!
CAUTION

Use Path.rmdir() and Path.unlink() to delete a folder and file respectively

"""

from pathlib import Path

Path.unlink(Path("a.txt"))
Path.unlink(Path("out/a.txt"))
Path.rmdir(Path("out/"))