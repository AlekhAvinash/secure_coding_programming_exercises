# Use string indexing and string concatenation (or f-strings)
# to write the sentence "we see trees" only by picking
# the necessary letters from the given string.

word = "tweezers "

we = word[1:3]
see = word[::-1][1:6:2]
trees = f"{word[::6]}{see[::-1]}"
print(f"{we}{word[-1]}{see}{word[-1]}{trees}")