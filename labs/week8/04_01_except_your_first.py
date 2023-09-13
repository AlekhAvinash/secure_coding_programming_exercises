"""
Write a function that accepts user input with the input() function
Try to convert their input to `int` and catch any exceptions that happen.

what kind of exceptions did you find?

"""

try:
    inp = int(input("Enter your age: "))
except ValueError as e:
    print(f"{e}\nOnly integer inputs are accepted!")