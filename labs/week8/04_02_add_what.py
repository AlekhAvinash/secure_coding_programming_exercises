"""
Write a function that takes two inputs and attempts to add them together.

Use a try/except block to catch all possible errors

Try adding
int + int
int + str
str + list
tuple + list
dict + dict
dict + str

Are all the exceptions the same?
"""

def adder(a, b):
    return a+b

adder(1, 2)

# adder(1, '2')
# adder('1', [2])
# adder((1, 2, 3), [2])
# adder({1: 123}, {5: 3523})
# adder({1: 123}, 'asd')

print("All cases except the first raise a Type Error.")