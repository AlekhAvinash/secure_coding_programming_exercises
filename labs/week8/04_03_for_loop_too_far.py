"""
Wrap the code below in a try - except
What is the correct exception to use?

Fix the error by "padding" the word with blank spaces when the excption is hit.
"""

word = "hellothis"+" "*3

try:
    for i in range(12):
        print(word[i])
except IndexError as e:
    print(f"{e}\nThe word is of len {len(word)}.")