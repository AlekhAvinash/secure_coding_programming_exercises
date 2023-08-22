#!/usr/bin/python3
# Type casting Exercise - 2
# Addition of string and integer using explicit conversion



# Initialise a string variable and integer variable
a = 10
b = "10"



# After explicit conversion, use python to successfully perform
# the addition of these variables - print the result to the console
a1 = str(a)
print(a1 + b)

## Now try to convert this variable
c = "ten"
try:
	c1 = int(c)
	print(c)
except ValueError as er:
	print(er)

## What kind of error does python give?
## What do you think the reason is?
print("The c variable is a string despite it's meaning.")
