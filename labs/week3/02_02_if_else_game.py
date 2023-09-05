# write a short command line game

# 1. ask the user for their name: (use the input() function)

# Say hello to them with their name
# If their name begins with a vowel say something funny about that ("Aha! Oho! Uhu! Ihi! etc", your name begins with a vowel!)
# If their name begins with a consonant make an even better joke about it.

inp = input("Enter your name: ")
print(f"Hello {inp}!")
if inp[0].lower() in "aeiou":
    print(f"{inp[0].upper()}h{inp[0].lower()}! your name begins with a vowel!")
else:
    print(f"Jeepers! Your name doesn't start with a vowel!!")

# 2. Ask them to pick a number between 1 and 10.
# If they guessed the right number, tell them they won
# Else, tell them they lost.

import random

random_number = random.randint(0, 10)
input_number = int(input("Enter a number: "))
if input_number == random_number:
    print("You guessed right!!")
else:
    print("Op! Wrong guess..")
