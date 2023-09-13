"""
Let's make a very basic Path object

"""

from pathlib import Path

##
cwd = Path.cwd()


## create a new path using concatenation

# you can use cwd.joinpath
new = cwd.joinpath('part1')
print(new)
# or you can use the special / symbol (overloaded for concatenation)
## examine your new path object

## print the following parts

# .parent
print(f"Parent: {new.parent}")
# .anchor
print(f"Anchor: {new.anchor}")
# .name
print(f"Name: {new.name}")
# .stem
print(f"Stem: {new.stem}")
# .suffix
print(f"Suffix: {new.suffix}")
# .parent
print(f"Parent: {new.parent}")

## check if your path is a directory or file

## .is_file()
print(new.is_file())
## .is_dir()
print(new.is_dir())

## print out your path and look at the type (you may need to print(type(your_path_here)))
## does it accurately reflect your OS?
print(new)
print(type(new))
print("No it doesn't reflect the OS")
