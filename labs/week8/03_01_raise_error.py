"""
Write a function that accepts user input with the input() function
Specify that they must use alphabet characters only.
Then raise an exception if they enter anything that is not able an alphabet character!

Hint: you can use .isalpha() to check if a character is an alpha character.
"""

inp = input("Enter your name (accepts only alphabets): ")
for i in inp:
    if not i.isalpha():
        raise Exception("Error: All characters aren't alphabets!!")

print(f"Hello, {inp}!!")