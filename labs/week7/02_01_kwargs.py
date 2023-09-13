## write a function that uses **kwargs as input
## it should print out the sum of all the integers found in the values

"""
input: hi = 2020, bye = 1000, see = 2, def = 'this'
output : 3022

The function should work for any kind of values and as many keyword arguments as the use would like to pass

"""

def main(**kargs):
    return sum(filter(lambda a: type(a) == int, kargs.values()))

print(main(hi = 2020, bye = 1000, see = 2, dif = 'this'))