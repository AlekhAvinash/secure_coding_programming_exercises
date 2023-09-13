"""
use a context manager to open the file winnie_pooh.txt

try it two ways
a) make a Path object that points to winnie_pooh.txt
b) just write it in as a string (don't use a Path object)

Both are valid! The first method is the OO way and will yield better programs down the line.
The second way is fine for quick scripts though

## Tasks to try
1. Print out of the first line of the file
2. Print out all the entire file
3. Print in the last line of the file
4. Add a new sentence to the file "I AM A NEW SENTENCE!"
5. 

"""

from pathlib import Path

class FileManager():
    def __init__(self, file, mode = ""):
        self.filename = file
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        if self.mode:
            self.file = open(self.filename, self.mode)
        else:
            self.file = open(self.filename)
        self.data = self.file.read()
        return self
    
    def __exit__(self, a, b, c):
        self.file.close()
    
    def printLine1(self):
        out = self.data.split('\n')[0]
        print(f"Line 1: {out}")
    
    def printFile(self):
        print(f"Length of entire file: {len(self.data)}")
    
    def printLast1(self):
        out = self.data.split('\n')[-1]
        print(f"Last Line 1: {out}")
    
    def appendStr(self, strg):
        assert 'a' in self.mode
        self.file.write(strg)

with FileManager(Path("winnie_pooh.txt")) as f:
    f.printLine1()
    f.printFile()
    f.printLast1()

with FileManager(Path("winnie_pooh.txt"), 'a+') as f:
    f.appendStr("I AM A NEW SENTENCE!")