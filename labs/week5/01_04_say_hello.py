# complete the function below
# say_hello should accept a users name, and then print out a custom greeting with their name

# print(say_hello('gilad'))
# should output something funny like : "hey gilad, your pants are on fire!!!!"

from random import choice

def say_hello(nme):
    lst = [f"hello, {nme}", f"good to see you, {nme}", f"hey {nme}, your pants are on fire", f"top of the morning, {nme}"]
    return choice(lst)

print(say_hello("alekh"))
