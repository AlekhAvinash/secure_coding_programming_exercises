""""
import the math library and use it to automatically generate a random list of numbers
You should generate 1000 random numbers.


"""

from random import randint

print([randint(1, 100) for i in range(1000)])