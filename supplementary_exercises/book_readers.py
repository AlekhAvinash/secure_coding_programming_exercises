# This folder contains another folder called `books/` that contains three text files
# of books from Project Gutenberg:
# 1. war_and_peace.txt
# 2. pride_and_prejudice.txt
# 3. crime_and_punishment.txt
#
# 1) Open `war_and_peace.txt`, read the whole file content and store it in a variable
# 2) Open `crime_and_punishment.txt` and overwrite the whole content with the last two words of the text of `war_and_peace.txt`
# 3) Loop over all three files and print out only the first word of each.

pwd = "books/"
lpa = [f"{pwd}war_and_peace.txt", f"{pwd}crime_and_punishment.txt", f"{pwd}pride_and_prejudice.txt"]
with open(lpa[0], "r") as f:
    wnp = f.read()

with open(lpa[1][:-4]+"_copy.txt", "w") as f:
    f.write(" ".join(wnp.split()[-2:]))

for i in lpa:
    print(open(i).read().split()[0])