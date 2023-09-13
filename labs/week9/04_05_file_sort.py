"""

Create two new folders
a. vowel
b. consonant

Iterate over your previously created files from 04_04_split_file.py
Open each file and check if the first word begins in a vowel or consonant
If it begins in a vowel, move the file to the vowel folder
Otherwise move the file to the consonant folder

"""

from pathlib import Path
from shutil import move

def main():
    folders = [Path('vowel/'), Path('consonent/')]
    [i.mkdir(parents=True, exist_ok=True) for i in folders]

    for i in Path.iterdir(Path("test/")):
        x = Path(i)
        if open(x).read(1).lower() in "aeiou":
            move(x, folders[0])
        else:
            move(x, folders[1])

main()