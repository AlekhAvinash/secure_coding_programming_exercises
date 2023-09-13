"""
Use the following commands to look around your directory
You may want to do this exercise interactively with an interpreter session

Path.cwd() gets the current working directory, returns a Path object
os.chdir(path)  changes directory	

os.listdir() files and directories, returns a list
Path.glob(“*”)  returns a generator that you can use to iterate over all files and directories. Advantage is you can filter the results easily on the input.
Path.iterdir()

"""

from pathlib import Path
import os

print(Path.cwd())
os.chdir("../")
print(Path.cwd())
cur = Path.cwd()

print(os.listdir())

print("Glob")
print(*[i for i in Path.glob(cur, "*")], sep='\n')

print("Iter")
print(*[i for i in Path.iterdir(cur)], sep='\n')