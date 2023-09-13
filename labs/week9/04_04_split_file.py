"""

1. Open winnie_pooh.txt
2. read in 100 lines at a time
3. after each 100 lines, write those lines to a new file
4. name each file differently (create a system to auto-increment the file names)
5. place all the files in a new folder (that you needed to create earlier)


"""

from pathlib import Path
from math import ceil

ct = lambda a, b: ceil(a/b)*b

def get():
    with open("winnie_pooh.txt") as f:
        return f.readlines()

def main():
    txt = get()
    folder = Path('test/')
    folder.mkdir(parents=True, exist_ok=True)

    for i in range(0, ct(len(txt), 100), 100):
        file = Path(f'{i//100}.txt')
        file = folder/file
        file.write_text(''.join(txt[i:i+100]), encoding='utf-8')

main()